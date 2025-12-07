#!/usr/bin/env python3
"""
Face Recognition Pipeline - Main Entry Point
Orchestrates capture, training, and prediction workflows
"""

import sys
import os

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def display_menu():
    """Display main menu with status information"""
    from src.utils import get_dataset_stats, get_model_info
    
    clear_screen()
    print("=" * 60)
    print("  Face Recognition Pipeline")
    print("  MediaPipe + LBPH")
    print("=" * 60)
    
    # Display status
    dataset_stats = get_dataset_stats()
    model_info = get_model_info()
    
    print("\n  Status:")
    print(f"    Dataset: {dataset_stats['people']} people, "
          f"{dataset_stats['total_images']} images")
    print(f"    Model: {'Trained' if model_info['exists'] else 'Not trained'}")
    if model_info['exists']:
        print(f"    Recognized people: {', '.join(model_info['people'])}")
    
    print("\n" + "-" * 60)
    print("\n1. Capture Face Images")
    print("2. Train Model")
    print("3. Run Face Recognition")
    print("4. View Dataset Info")
    print("5. Exit")
    print("\n" + "=" * 60)

def capture_faces():
    """Run face capture module"""
    from src.capture import run_capture
    run_capture()

def train_model():
    """Run training module"""
    from src.train import run_training
    run_training()

def predict_faces():
    """Run prediction module"""
    from src.predict import run_prediction
    run_prediction()

def view_dataset_info():
    """Display detailed dataset information"""
    from src.utils import list_people_in_dataset, get_dataset_stats
    
    print("\n" + "=" * 60)
    print("  Dataset Information")
    print("=" * 60)
    
    stats = get_dataset_stats()
    people = list_people_in_dataset()
    
    if not people:
        print("\nNo dataset found. Please capture face images first.")
        return
    
    print(f"\nTotal people: {stats['people']}")
    print(f"Total images: {stats['total_images']}")
    print(f"\nPeople in dataset:")
    
    for person in people:
        person_path = os.path.join("dataset", person)
        image_count = len([f for f in os.listdir(person_path) 
                          if f.endswith(('.jpg', '.jpeg', '.png'))])
        print(f"  - {person}: {image_count} images")

def check_environment():
    """Check if environment is properly set up"""
    from src.utils import validate_environment
    
    is_valid, errors = validate_environment()
    
    if not is_valid:
        print("\n" + "=" * 60)
        print("  Environment Setup Issues")
        print("=" * 60)
        print("\nThe following dependencies are missing:")
        for error in errors:
            print(f"  - {error}")
        print("\nPlease run: pip install -r requirements.txt")
        print("=" * 60)
        return False
    
    return True

def main():
    """Main application loop"""
    # Check environment on startup
    if not check_environment():
        sys.exit(1)
    
    while True:
        display_menu()
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            capture_faces()
            input("\nPress Enter to continue...")
        elif choice == '2':
            train_model()
            input("\nPress Enter to continue...")
        elif choice == '3':
            predict_faces()
            input("\nPress Enter to continue...")
        elif choice == '4':
            view_dataset_info()
            input("\nPress Enter to continue...")
        elif choice == '5':
            print("\nExiting... Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid option. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
