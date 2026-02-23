## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4097.100.6.122.2
-  __TEXT.__text: 0x405b3c
+4097.100.8.0.0
+  __TEXT.__text: 0x407360
   __TEXT.__auth_stubs: 0x68a0
-  __TEXT.__objc_methlist: 0x2fd50
-  __TEXT.__const: 0x22f14
-  __TEXT.__gcc_except_tab: 0x30a8
-  __TEXT.__cstring: 0x1c1d5
-  __TEXT.__oslogstring: 0x16444
+  __TEXT.__objc_methlist: 0x2fd60
+  __TEXT.__const: 0x230b4
+  __TEXT.__gcc_except_tab: 0x30bc
+  __TEXT.__cstring: 0x1c1a5
+  __TEXT.__oslogstring: 0x16514
   __TEXT.__dlopen_cstrs: 0x3b9
   __TEXT.__ustring: 0x8
-  __TEXT.__constg_swiftt: 0x5fe8
-  __TEXT.__swift5_typeref: 0x27dd0
-  __TEXT.__swift5_reflstr: 0x625a
-  __TEXT.__swift5_fieldmd: 0x5388
+  __TEXT.__constg_swiftt: 0x60f8
+  __TEXT.__swift5_typeref: 0x27e12
+  __TEXT.__swift5_reflstr: 0x63ea
+  __TEXT.__swift5_fieldmd: 0x5468
   __TEXT.__swift5_builtin: 0x438
   __TEXT.__swift5_assocty: 0x1648
   __TEXT.__swift5_proto: 0xac4
-  __TEXT.__swift5_types: 0x568
-  __TEXT.__swift5_capture: 0x2760
+  __TEXT.__swift5_types: 0x570
+  __TEXT.__swift5_capture: 0x2770
   __TEXT.__swift_as_entry: 0xd4
   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift5_mpenum: 0x20
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__unwind_info: 0xf938
-  __TEXT.__eh_frame: 0x2a40
+  __TEXT.__unwind_info: 0xf9e0
+  __TEXT.__eh_frame: 0x2a80
   __TEXT.__objc_classname: 0x61c7
-  __TEXT.__objc_methname: 0xa16b7
-  __TEXT.__objc_methtype: 0x10cd2
-  __TEXT.__objc_stubs: 0x5c1c0
+  __TEXT.__objc_methname: 0xa1767
+  __TEXT.__objc_methtype: 0x10c93
+  __TEXT.__objc_stubs: 0x5c200
   __DATA_CONST.__got: 0x4458
-  __DATA_CONST.__const: 0x7eb0
+  __DATA_CONST.__const: 0x7ed8
   __DATA_CONST.__objc_classlist: 0x1230
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x7c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a070
+  __DATA_CONST.__objc_selrefs: 0x1a080
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xd98
   __DATA_CONST.__objc_arraydata: 0x1048
   __AUTH_CONST.__auth_got: 0x3460
-  __AUTH_CONST.__const: 0xe3c8
+  __AUTH_CONST.__const: 0xe510
   __AUTH_CONST.__cfstring: 0x16740
-  __AUTH_CONST.__objc_const: 0x50b00
+  __AUTH_CONST.__objc_const: 0x50ba0
   __AUTH_CONST.__objc_intobj: 0x1860
   __AUTH_CONST.__objc_doubleobj: 0x540
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0xcf0
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0x5d70
-  __AUTH.__data: 0x1040
-  __DATA.__objc_ivar: 0x3c70
-  __DATA.__data: 0xb6e8
-  __DATA.__bss: 0x117c0
+  __AUTH.__objc_data: 0x5e60
+  __AUTH.__data: 0x1048
+  __DATA.__objc_ivar: 0x3c74
+  __DATA.__data: 0xb708
+  __DATA.__bss: 0x117e0
   __DATA.__common: 0x179
   __DATA_DIRTY.__objc_data: 0x78e0
-  __DATA_DIRTY.__data: 0x3480
+  __DATA_DIRTY.__data: 0x3488
   __DATA_DIRTY.__bss: 0x4340
   __DATA_DIRTY.__common: 0x128
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4B516776-FDB1-31A3-B128-2E010B23AC1D
-  Functions: 26285
-  Symbols:   60661
-  CStrings:  31453
+  UUID: 23078086-8CBC-3E3D-BA94-3101D09997AE
+  Functions: 26327
+  Symbols:   60679
+  CStrings:  31462
 
Symbols:
+ -[CAMTimelapseController _focusLockTimeoutTimer]
+ -[CAMTimelapseController _resetFocusLockTimeoutTimer]
+ -[CAMTimelapseController set_focusLockTimeoutTimer:]
+ GCC_except_table31
+ _OBJC_IVAR_$_CAMTimelapseController.__focusLockTimeoutTimer
+ ___66-[CAMTimelapseController _updateFocusAndExposureForStartCapturing]_block_invoke.225
+ ___66-[CAMTimelapseController _updateFocusAndExposureForStartCapturing]_block_invoke.cold.1
+ ___block_descriptor_52_e8_32s40w_e17_v16?0"NSTimer"8lw40l8s32l8
+ _get_enum_tag_for_layout_string So14CMDeviceMotionCIegg_Sg
+ _objc_msgSend$_focusLockTimeoutTimer
+ _objc_msgSend$_resetFocusLockTimeoutTimer
+ _objc_msgSend$set_focusLockTimeoutTimer:
+ _symbolic _____ 8CameraUI19OvershootCalculator33_066F33B1B548941972E875719D022C2CLLV
+ _symbolic _____ 8CameraUI23GravityStabilityMonitorV
+ _symbolic _____Sg So14CMAccelerationa
+ _symbolic ySo14CMDeviceMotionCcSg
+ _type_layout_string 8CameraUI19OvershootCalculator33_066F33B1B548941972E875719D022C2CLLV
+ _type_layout_string 8CameraUI23GravityStabilityMonitorV
- -[CAMMotionController roughOrientationDidChange:]
- _objc_msgSend$roughOrientationDidChange:
CStrings:
+ "/Library/Caches/com.apple.xbs/CF432FD4-7022-4393-9786-1B55B06601BE/TemporaryDirectory.m2LT11/Sources/Camera/CameraUI/BurstAnalysisCore/Projections/FastRegistration_Core.c"
+ "/Library/Caches/com.apple.xbs/CF432FD4-7022-4393-9786-1B55B06601BE/TemporaryDirectory.m2LT11/Sources/Camera/CameraUI/BurstAnalysisCore/Projections/Projections_Core.c"
+ "/Library/Caches/com.apple.xbs/CF432FD4-7022-4393-9786-1B55B06601BE/TemporaryDirectory.m2LT11/Sources/Camera/CameraUI/BurstAnalysisCore/Projections/Projections_Optimizer.c"
+ "Capture orientation %{public}@ (override)"
+ "Considered Orientation: %s gravity: %s%s"
+ "Locked & Ignored Orientation: %s gravity: %s%s"
+ "OrientationModel deinitialized"
+ "OrientationModel initialized"
+ "T@\"NSTimer\",&,N,V__focusLockTimeoutTimer"
+ "Timed out on lockFocusAtLensPosition, proceeding to capture"
+ "Update Orientation to: %s gravity: %s%s"
+ "__focusLockTimeoutTimer"
+ "_flatOvershootCalculator"
+ "_focusLockTimeoutTimer"
+ "_gravityAndYawBasedOrientationsAgree"
+ "_gravityStabilityMonitor"
+ "_resetFocusLockTimeoutTimer"
+ "_uprightOvershootCalculator"
+ "set_focusLockTimeoutTimer:"
- "/Library/Caches/com.apple.xbs/3ABBF605-1E82-45C3-94DF-8497F7801711/TemporaryDirectory.DS99Ky/Sources/Camera/CameraUI/BurstAnalysisCore/Projections/FastRegistration_Core.c"
- "/Library/Caches/com.apple.xbs/3ABBF605-1E82-45C3-94DF-8497F7801711/TemporaryDirectory.DS99Ky/Sources/Camera/CameraUI/BurstAnalysisCore/Projections/Projections_Core.c"
- "/Library/Caches/com.apple.xbs/3ABBF605-1E82-45C3-94DF-8497F7801711/TemporaryDirectory.DS99Ky/Sources/Camera/CameraUI/BurstAnalysisCore/Projections/Projections_Optimizer.c"
- "Considered Orientation: %s gravity: %s"
- "Updated Orientation: "
- "Updated Orientation: %s gravity: %s"
- "portraitUpsideDown"
- "roughOrientationDidChange:"
- "v24@0:8@\"CAMOrientationModel\"16"

```
