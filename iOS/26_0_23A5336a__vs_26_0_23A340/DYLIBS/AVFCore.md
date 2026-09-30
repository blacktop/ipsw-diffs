## AVFCore

> `/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`

```diff

 2360.79.1.1.0
-  __TEXT.__text: 0x1b00dc
+  __TEXT.__text: 0x1b0618
   __TEXT.__auth_stubs: 0x3bf0
-  __TEXT.__objc_methlist: 0x1afa4
-  __TEXT.__cstring: 0x23be6
+  __TEXT.__objc_methlist: 0x1afcc
+  __TEXT.__cstring: 0x24056
   __TEXT.__const: 0x1dd0
   __TEXT.__gcc_except_tab: 0x6920
   __TEXT.__oslogstring: 0x3c56

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x94c8
+  __TEXT.__unwind_info: 0x94d0
   __TEXT.__objc_classname: 0x5ee3
-  __TEXT.__objc_methname: 0x360fa
+  __TEXT.__objc_methname: 0x361ca
   __TEXT.__objc_methtype: 0x9da9
-  __TEXT.__objc_stubs: 0x209e0
+  __TEXT.__objc_stubs: 0x20a40
   __DATA_CONST.__got: 0x4630
-  __DATA_CONST.__const: 0x5578
+  __DATA_CONST.__const: 0x5618
   __DATA_CONST.__objc_classlist: 0x1198
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xabb0
+  __DATA_CONST.__objc_selrefs: 0xabc8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0xce8
-  __DATA_CONST.__objc_arraydata: 0x298
+  __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x1e08
   __AUTH_CONST.__const: 0x1118
-  __AUTH_CONST.__cfstring: 0x18de0
-  __AUTH_CONST.__objc_const: 0x30780
+  __AUTH_CONST.__cfstring: 0x190e0
+  __AUTH_CONST.__objc_const: 0x307a0
   __AUTH_CONST.__objc_intobj: 0x288
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
+  __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x7a10
   __AUTH.__data: 0x1f8
-  __DATA.__objc_ivar: 0x2574
+  __DATA.__objc_ivar: 0x2578
   __DATA.__data: 0x1800
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x180

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1229A55F-74E9-375E-877A-2B3914FB8EC7
-  Functions: 11360
-  Symbols:   38838
-  CStrings:  16725
+  UUID: 942CF4C2-348C-3499-AF07-6243CAB08F66
+  Functions: 11364
+  Symbols:   38870
+  CStrings:  16777
 
Symbols:
+ -[AVAssetWriterInputWritingHelper _checkIfClientSetProResRAWRequiredMetadataReturningError:]
+ -[AVAssetWriterInputWritingHelper _checkProResRAWRequiredMetadataForPixelBufferReturningError:]
+ -[AVAssetWriterInputWritingHelper _checkProResRAWRequiredMetadataForSampleBuffer:error:]
+ GCC_except_table397
+ _AVMetadataIdentifierQuickTimeMetadataCameraISOSensitivity
+ _AVMetadataIdentifierQuickTimeMetadataCameraLensIrisFNumber
+ _AVMetadataIdentifierQuickTimeMetadataCameraShutterSpeedAngle
+ _AVMetadataIdentifierQuickTimeMetadataCameraShutterSpeedTime
+ _AVMetadataIdentifierQuickTimeMetadataCameraWhiteBalance
+ _AVMetadataIdentifierQuickTimeMetadataFrontAndBackCameraComposition
+ _AVMetadataIdentifierQuickTimeMetadataFrontAndBackCameraCompositionPictureInPictureRect
+ _AVMetadataIdentifierQuickTimeMetadataWhiteBalanceByCCTColorMatrices
+ _AVMetadataIdentifierQuickTimeMetadataWhiteBalanceByCCTWhiteBalanceFactors
+ _AVMetadataQuickTimeMetadataKeyCameraISOSensitivity
+ _AVMetadataQuickTimeMetadataKeyCameraLensIrisFNumber
+ _AVMetadataQuickTimeMetadataKeyCameraShutterSpeedAngle
+ _AVMetadataQuickTimeMetadataKeyCameraShutterSpeedTime
+ _AVMetadataQuickTimeMetadataKeyCameraWhiteBalance
+ _AVMetadataQuickTimeMetadataKeyFrontAndBackCameraComposition
+ _AVMetadataQuickTimeMetadataKeyFrontAndBackCameraCompositionPictureInPictureRect
+ _AVMetadataQuickTimeMetadataKeyWhiteBalanceByCCTColorMatrices
+ _AVMetadataQuickTimeMetadataKeyWhiteBalanceByCCTWhiteBalanceFactors
+ _AVVideoCodecTypeAppleProResRAW
+ _AVVideoCodecTypeAppleProResRAWHQ
+ _OBJC_IVAR_$_AVAssetWriterInputWritingHelper._didCheckProResRAWRequiredMetadata
+ _objc_msgSend$_checkIfClientSetProResRAWRequiredMetadataReturningError:
+ _objc_msgSend$_checkProResRAWRequiredMetadataForPixelBufferReturningError:
+ _objc_msgSend$_checkProResRAWRequiredMetadataForSampleBuffer:error:
- GCC_except_table394
- GCC_except_table448
CStrings:
+ "AVError-2025"
+ "AVErrorAutoWhiteBalanceNotLocked"
+ "AVErrorFollowExternalSyncDeviceTimedOut"
+ "AVErrorNoSmartFramingsEnabled"
+ "The required metadata for ProResRAW movie are not set. Missing movie level metadata keys {%@}."
+ "_checkIfClientSetProResRAWRequiredMetadataReturningError:"
+ "_checkProResRAWRequiredMetadataForPixelBufferReturningError:"
+ "_checkProResRAWRequiredMetadataForSampleBuffer:error:"
+ "_didCheckProResRAWRequiredMetadata"
+ "aprh"
+ "aprn"
+ "com.apple.proresraw.whitebalance.bycct.colormatrices"
+ "com.apple.proresraw.whitebalance.bycct.whitebalancefactors"
+ "com.apple.quicktime.camera.lens_irisfnumber"
+ "com.apple.quicktime.front-and-back-camera-composition"
+ "com.apple.quicktime.front-and-back-camera-composition-picture-in-picture-rect"
+ "mdta/com.apple.proresraw.whitebalance.bycct.colormatrices"
+ "mdta/com.apple.proresraw.whitebalance.bycct.whitebalancefactors"
+ "mdta/com.apple.quicktime.camera.lens_irisfnumber"
+ "mdta/com.apple.quicktime.front-and-back-camera-composition"
+ "mdta/com.apple.quicktime.front-and-back-camera-composition-picture-in-picture-rect"
+ "mdta/org.smpte.rdd18.camera.isosensitivity"
+ "mdta/org.smpte.rdd18.camera.shutterspeed_angle"
+ "mdta/org.smpte.rdd18.camera.shutterspeed_time"
+ "mdta/org.smpte.rdd18.camera.whitebalance"
+ "org.smpte.rdd18.camera.isosensitivity"
+ "org.smpte.rdd18.camera.shutterspeed_angle"
+ "org.smpte.rdd18.camera.shutterspeed_time"
+ "org.smpte.rdd18.camera.whitebalance"
- "AVError"

```
