# Tongue-Diagnosis-Device
- [Device] RaspberryPi(Using Camera Tongue detection) & Arduino(Circular LED control)
- [Software] Pytorch(Disease classfication) and Opencv with python(Divide Tongue part & Analysis Tongue part)


## Function

1. In Device, Taking Pictrue in realtime video
2. In Device, Control Circular LED brightness
3. In Software, Classfication of Tongue Disease (using tongue state : red tongue/white tongue/pink tongue/little coated/white coated/yellow coated/Existence of tooth scar -> Disease Diagnosis)
4. In Software, Divide and Analysis Tongue part (Divide Tongue into Top/Bottom/Side/Center part and Divide coated part or not)

## Presentation


## Result Video Clip

<div>
  <p> - Device Video Clip</p>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/66882526-b2fdf000-f005-11e9-80f5-95da78d58809.gif"/>
  
  <p> - Website Video Clip</p>
  <img width="800" src="https://user-images.githubusercontent.com/37185394/66881933-847f1580-f003-11e9-86bd-84b11912d8ee.gif"/>
</div>


## pip install

```python 3.5
(option) conda activate
pip3 install numpy
pip3 install cv2
pip3 install tesnorflow
```
