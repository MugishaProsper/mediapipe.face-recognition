"""Utility functions for face recognition pipeline"""

import os
import json
from typing import Dict, List, Tuple


def get_dataset_stats() -> Dict[str, int]:
    """Get statistics about the dataset"""
    DATASET_DIR = "dataset"
    
    if not os.path.exists(DATASET_DIR):
        return {"people": 0, "total_images": 0}
    
    stats = {"people": 0, "total_images": 0}
    
    for person in os.listdir(DATASET_DIR):
        person_path = os.path.join(DATASET_DIR, person)
        if not os.path.isdir(person_path):
            continue
        
        stats["people"] += 1
        image_count = len([f for f in os.listdir(person_path) 
                          if f.endswith(('.jpg', '.jpeg', '.png'))])
        stats["total_images"] += image_count
    
    return stats


def get_model_info() -> Dict[str, any]:
    """Get information about trained model"""
    MODEL_PATH = "models/lbph_model.xml"
    LABEL_MAP_PATH = "models/label_map.json"
    
    info = {
        "exists": False,
        "people": [],
        "count": 0
    }
    
    if os.path.exists(MODEL_PATH) and os.path.exists(LABEL_MAP_PATH):
        info["exists"] = True
        
        with open(LABEL_MAP_PATH, "r") as f:
            label_map = json.load(f)
            info["people"] = list(label_map.values())
            info["count"] = len(label_map)
    
    return info


def list_people_in_dataset() -> List[str]:
    """List all people in the dataset"""
    DATASET_DIR = "dataset"
    
    if not os.path.exists(DATASET_DIR):
        return []
    
    people = []
    for person in os.listdir(DATASET_DIR):
        person_path = os.path.join(DATASET_DIR, person)
        if os.path.isdir(person_path):
            people.append(person)
    
    return sorted(people)


def validate_environment() -> Tuple[bool, List[str]]:
    """Validate that all dependencies are available"""
    errors = []
    
    try:
        import cv2
    except ImportError:
        errors.append("OpenCV (opencv-python) is not installed")
    
    try:
        import mediapipe
    except ImportError:
        errors.append("MediaPipe is not installed")
    
    try:
        import numpy
    except ImportError:
        errors.append("NumPy is not installed")
    
    # Check for opencv-contrib
    try:
        import cv2
        cv2.face.LBPHFaceRecognizer_create()
    except AttributeError:
        errors.append("opencv-contrib-python is not installed (required for LBPH)")
    except:
        pass
    
    return len(errors) == 0, errors
