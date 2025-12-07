"""Basic tests for utility functions"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import validate_environment, get_dataset_stats, get_model_info


def test_validate_environment():
    """Test environment validation"""
    is_valid, errors = validate_environment()
    print(f"Environment valid: {is_valid}")
    if not is_valid:
        print("Errors found:")
        for error in errors:
            print(f"  - {error}")
    assert is_valid, "Environment validation failed"


def test_get_dataset_stats():
    """Test dataset statistics"""
    stats = get_dataset_stats()
    print(f"Dataset stats: {stats}")
    assert isinstance(stats, dict)
    assert "people" in stats
    assert "total_images" in stats


def test_get_model_info():
    """Test model information retrieval"""
    info = get_model_info()
    print(f"Model info: {info}")
    assert isinstance(info, dict)
    assert "exists" in info


if __name__ == "__main__":
    print("Running tests...\n")
    
    try:
        test_validate_environment()
        print("✓ Environment validation test passed\n")
    except AssertionError as e:
        print(f"✗ Environment validation test failed: {e}\n")
    
    try:
        test_get_dataset_stats()
        print("✓ Dataset stats test passed\n")
    except Exception as e:
        print(f"✗ Dataset stats test failed: {e}\n")
    
    try:
        test_get_model_info()
        print("✓ Model info test passed\n")
    except Exception as e:
        print(f"✗ Model info test failed: {e}\n")
    
    print("Tests completed!")
