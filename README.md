# Face Recognition Pipeline (MediaPipe + LBPH)

A classical face recognition system using computer vision techniques without deep learning. Combines MediaPipe for face detection with OpenCV's LBPH (Local Binary Patterns Histograms) algorithm for recognition.

## Features

- ✅ Real-time face detection using MediaPipe Face Mesh
- ✅ Face recognition using LBPH algorithm (no ML models required)
- ✅ Interactive menu-driven interface
- ✅ Multi-person support
- ✅ Docker containerization for easy deployment
- ✅ Persistent storage for datasets and trained models

## How It Works

1. **MediaPipe Face Mesh** - Detects faces and identifies 468 facial landmarks
2. **LBPH Algorithm** - Extracts texture features and recognizes faces based on local binary patterns
3. **Training** - Builds a model from captured face images stored in `dataset/`
4. **Recognition** - Identifies faces in real-time and displays names with confidence scores

## Project Structure

```
face-recognition/
├── main.py                 # Main application entry point
├── src/
│   ├── capture.py          # Face image capture module
│   ├── train.py            # LBPH model training module
│   ├── predict.py          # Real-time face recognition
│   └── utils.py            # Utility functions
├── tests/
│   └── test_utils.py       # Test suite
├── dataset/                # Captured face images (auto-generated)
│   └── <person_name>/      # One folder per person
│       └── *.jpg           # Face images
├── models/                 # Trained models (auto-generated)
│   ├── lbph_model.xml      # Trained LBPH recognizer
│   └── label_map.json      # Person name to label mapping
├── requirements.txt        # Python dependencies
├── setup.sh                # Automated setup script
├── Dockerfile              # Docker container definition
├── docker-compose.yml      # Docker Compose configuration
├── docker-run.sh           # Docker run helper script
└── Makefile               # Build automation commands
```

## Prerequisites

- Python 3.11 or higher
- Webcam/Camera device
- Linux/Mac OS (for X11 GUI support)
- Docker (optional, for containerized deployment)

## Installation & Setup

### Option 1: Quick Setup (Recommended)

Run the automated setup script:

```bash
chmod +x setup.sh
./setup.sh
source venv/bin/activate
```

This will:
- Create a virtual environment
- Install all dependencies
- Create necessary directories (`dataset/`, `models/`)

### Option 2: Manual Setup

1. **Create virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create directories:**

```bash
mkdir -p dataset models
```

**Note:** The `opencv-contrib-python` package is required for LBPH algorithm support.

## How to Run

### Step 1: Start the Application

Activate your virtual environment and run:

```bash
source venv/bin/activate  # Skip if already activated
python main.py
```

You'll see an interactive menu:

```
==============================================================
  Face Recognition Pipeline
  MediaPipe + LBPH
==============================================================

  Status:
    Dataset: 0 people, 0 images
    Model: Not trained

--------------------------------------------------------------

1. Capture Face Images
2. Train Model
3. Run Face Recognition
4. View Dataset Info
5. Exit

==============================================================
```

### Step 2: Capture Face Images

1. Select option **1** from the menu
2. Enter the person's name when prompted
3. Position your face in front of the camera
4. The system will automatically capture face images
5. Press **Q** to stop capturing

**Output:** Images saved to `dataset/<person_name>/`

### Step 3: Train the Model

1. Select option **2** from the menu
2. The system will load all images from `dataset/`
3. Training progress will be displayed

**Output:** 
- `models/lbph_model.xml` - Trained LBPH recognizer
- `models/label_map.json` - Name-to-label mapping

### Step 4: Run Face Recognition

1. Select option **3** from the menu
2. Position your face in front of the camera
3. The system will display:
   - Green rectangle around detected faces
   - Person's name
   - Confidence score (lower is better)
4. Press **Q** to stop recognition

### Step 5: Add More People (Optional)

To recognize multiple people:
1. Repeat Step 2 (Capture) for each new person
2. Run Step 3 (Train) again to update the model
3. Run Step 4 (Recognize) to test

### View Dataset Information

Select option **4** to see:
- Total number of people in dataset
- Total number of images
- Images per person

## Complete Workflow Example

```bash
# 1. Setup (one-time)
./setup.sh
source venv/bin/activate

# 2. Run application
python main.py

# 3. In the menu:
#    - Select 1: Capture images for "Alice"
#    - Select 1: Capture images for "Bob"
#    - Select 2: Train model
#    - Select 3: Run recognition
#    - Press Q to stop
#    - Select 5: Exit

# Models are saved in models/ folder:
ls models/
# Output: lbph_model.xml  label_map.json
```

## Standalone Module Usage

Each module can run independently:

```bash
python -m src.capture   # Capture faces only
python -m src.train     # Train model only
python -m src.predict   # Run recognition only
```

## Docker Deployment (Alternative)

### Option 1: Quick Docker Run

```bash
chmod +x docker-run.sh
./docker-run.sh
```

This script handles:
- X11 forwarding for GUI
- Camera device access
- Volume mounting for persistent data

### Option 2: Docker Compose

```bash
# Start
xhost +local:docker
docker-compose up

# Stop
docker-compose down
xhost -local:docker
```

### Option 3: Manual Docker

```bash
# Build
docker build -t face-recognition:latest .

# Run
docker run -it --rm \
    --device=/dev/video0:/dev/video0 \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $(pwd)/dataset:/app/dataset \
    -v $(pwd)/models:/app/models \
    --privileged \
    face-recognition:latest
```

### Using Makefile

```bash
make help           # Show all commands
make setup          # Setup local environment
make run            # Run locally
make test           # Run tests
make build          # Build Docker image
make docker-run     # Run in Docker
make clean          # Clean up
```

## Troubleshooting

### Camera Not Detected

```bash
# Check camera device
ls /dev/video*

# Test camera access
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"
```

### OpenCV GUI Not Showing (Docker)

```bash
# Allow X11 forwarding
xhost +local:docker

# Check DISPLAY variable
echo $DISPLAY
```

### Import Errors

```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt

# Verify opencv-contrib
python -c "import cv2; cv2.face.LBPHFaceRecognizer_create()"
```

### Low Recognition Accuracy

- Capture more images per person (50-100 recommended)
- Ensure good lighting conditions
- Capture from different angles
- Retrain the model after adding more images

## Model Storage

All trained models are saved in the `models/` directory:

```
models/
├── lbph_model.xml      # Trained LBPH recognizer (OpenCV format)
└── label_map.json      # Mapping of numeric labels to person names
```

**Example label_map.json:**
```json
{
  "0": "Alice",
  "1": "Bob",
  "2": "Charlie"
}
```

The model persists across runs and can be backed up or transferred to other systems.

## Testing

Run the test suite:

```bash
python tests/test_utils.py
```

## Technical Details

- **Face Detection:** MediaPipe Face Mesh (468 landmarks)
- **Recognition Algorithm:** LBPH (Local Binary Patterns Histograms)
- **Image Format:** Grayscale JPEG
- **Model Format:** OpenCV XML
- **Confidence Score:** Lower values indicate better matches (typically < 50 for good matches)
