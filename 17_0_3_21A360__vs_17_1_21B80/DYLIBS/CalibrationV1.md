## CalibrationV1

> `/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1`

```diff

-458.3.12.1.0
-  __TEXT.__text: 0x1b264
+465.15.2.0.0
+  __TEXT.__text: 0x1b538
   __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_methlist: 0xb00
   __TEXT.__const: 0xe4c
-  __TEXT.__cstring: 0x2fc7
+  __TEXT.__cstring: 0x329c
   __TEXT.__unwind_info: 0x390
   __TEXT.__objc_classname: 0xef
-  __TEXT.__objc_methname: 0x33b9
+  __TEXT.__objc_methname: 0x33c1
   __TEXT.__objc_methtype: 0x16f7
   __TEXT.__objc_stubs: 0x1240
-  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 303
-  Symbols:   128
-  CStrings:  979
+  Symbols:   127
+  CStrings:  987
 
Symbols:
- _kFigCaptureStreamProperty_ZoomFactor
CStrings:
+ "ADC did not converge, applying previous temporal biases to the initial calibration."
+ "ADC: Could not apply the temporal biases after calibration refinement."
+ "__tg_fabs((__typeof__(__tg_promote((refinedCalModel.pixelSize_um[CalBufferTypeAuxiliary]))))(refinedCalModel.pixelSize_um[CalBufferTypeAuxiliary])) > 1e-5"
+ "__tg_fabs((__typeof__(__tg_promote((refinedCalModel.pixelSize_um[CalBufferTypeReference]))))(refinedCalModel.pixelSize_um[CalBufferTypeReference])) > 1e-5"
+ "__tg_fabs((__typeof__(__tg_promote((refinedDistortionTele.pixelSizeMM))))(refinedDistortionTele.pixelSizeMM)) > 1e-8"
+ "__tg_fabs((__typeof__(__tg_promote((refinedDistortionWide.pixelSizeMM))))(refinedDistortionWide.pixelSizeMM)) > 1e-8"
+ "_referenceCalibrationScalingFactor"
+ "adcSuccessful"
+ "skip_biases"
- "_referenceDigitalZoomFactor"

```
