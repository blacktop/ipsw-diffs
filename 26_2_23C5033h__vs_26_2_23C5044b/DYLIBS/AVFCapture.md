## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-664.60.7.0.0
-  __TEXT.__text: 0x11f264
+664.62.12.0.0
+  __TEXT.__text: 0x11f2a8
   __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_methlist: 0xf0ac
   __TEXT.__const: 0xb72

   __TEXT.__objc_methname: 0x2aa0b
   __TEXT.__objc_methtype: 0x4080
   __TEXT.__objc_stubs: 0x18bc0
-  __DATA_CONST.__got: 0x2a88
+  __DATA_CONST.__got: 0x2a90
   __DATA_CONST.__const: 0x7ce0
   __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E6589B3B-08D2-3E6E-AB2A-5214EE76DA3B
+  UUID: 758D6CE7-543C-309E-B569-3E79A971AA9B
   Functions: 6465
-  Symbols:   22738
+  Symbols:   22739
   CStrings:  12672
 
Symbols:
+ _kFigCaptureSourceAttributeKey_PhotoModeFrameRatesForSystemPressureLevel
+ _kFigCaptureSourceAttributeKey_PortraitFrameRatesForSystemPressureLevel
- _kFigCaptureSourceAttributeKey_FrameRatesForSystemPressureLevel
Functions:
~ -[AVCaptureSystemPressureState isEqual:] : 224 -> 288
~ -[AVCaptureFigVideoDevice _recommendedFrameRateRangeForVideoFormat:depthFormat:figSystemPressureLevel:] : 624 -> 604
~ -[AVCaptureFigVideoDevice _handleNotification:payload:] : 13812 -> 13836
CStrings:
+ "description=CameraCapture_AVF-664.62.12"
- "description=CameraCapture_AVF-664.60.7"

```
