# Quick Start Guide

Get up and running in 5 minutes!

## 1. Setup (One-Time)

```bash
# Clone or navigate to project directory
cd face-recognition

# Run setup script
chmod +x setup.sh
./setup.sh

# Activate virtual environment
source venv/bin/activate
```

## 2. Run the Application

```bash
python main.py
```

## 3. Follow the Workflow

### First Time Setup:

1. **Select 1** - Capture Face Images
   - Enter your name
   - Look at the camera
   - Press Q when done (capture 30-50 images)

2. **Select 2** - Train Model
   - Wait for training to complete

3. **Select 3** - Run Face Recognition
   - Your name should appear above your face
   - Press Q to stop

### Add More People:

1. **Select 1** - Capture images for another person
2. **Select 2** - Retrain the model
3. **Select 3** - Test recognition

## 4. Check Your Results

```bash
# View captured images
ls dataset/

# View trained model
ls models/
# Should show: lbph_model.xml  label_map.json
```

## Docker Alternative

If you prefer Docker:

```bash
chmod +x docker-run.sh
./docker-run.sh
```

## Need Help?

- Camera not working? Check `ls /dev/video*`
- Import errors? Run `pip install -r requirements.txt`
- See full documentation in `README.md`

## Tips for Best Results

- Capture 50-100 images per person
- Use good lighting
- Capture from different angles
- Look directly at the camera
- Retrain after adding new people

That's it! You're ready to go. 🚀
