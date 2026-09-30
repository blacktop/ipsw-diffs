## AppC3D

> `/System/Library/PrivateFrameworks/AppC3D.framework/AppC3D`

```diff

-1.15.1.0.0
-  __TEXT.__text: 0x62dec4
-  __TEXT.__auth_stubs: 0x2140
-  __TEXT.__cstring: 0x11d32
-  __TEXT.__const: 0x5c737
-  __TEXT.__oslogstring: 0x315
-  __TEXT.__gcc_except_tab: 0x4e4b4
-  __TEXT.__unwind_info: 0x12e58
+1.15.4.0.0
+  __TEXT.__text: 0x62eb34
+  __TEXT.__auth_stubs: 0x2160
+  __TEXT.__cstring: 0x11e3a
+  __TEXT.__const: 0x5c597
+  __TEXT.__oslogstring: 0x36b
+  __TEXT.__gcc_except_tab: 0x4e52c
+  __TEXT.__unwind_info: 0x12e80
   __TEXT.__eh_frame: 0x300
   __TEXT.__objc_methname: 0x4f
   __TEXT.__objc_stubs: 0xa0

   __DATA_CONST.__const: 0x1470
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x10b0
+  __AUTH_CONST.__auth_got: 0x10c0
   __AUTH_CONST.__auth_ptr: 0x68
-  __AUTH_CONST.__const: 0x20630
+  __AUTH_CONST.__const: 0x205d0
   __AUTH_CONST.__cfstring: 0x300
-  __AUTH.__data: 0x28
-  __DATA.__data: 0x5450
+  __DATA.__data: 0x5458
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0x90
   __DATA.__common: 0x90
-  __DATA_DIRTY.__data: 0x60
+  __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x2200
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 12482
-  Symbols:   693
-  CStrings:  1751
+  Functions: 12484
+  Symbols:   695
+  CStrings:  1760
 
Symbols:
+ _CFDictionaryCreateMutableCopy
+ _CFErrorCopyUserInfo
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/AppC3D/library/Kit/Foundation/src/ErrorRef.cpp"
+ "Buffer expired"
+ "Calibration data missing"
+ "Camera matrices contain NaNs."
+ "Camera matrices contain NaNs."
+ "ComputePatchCameraFocalLength: Patch diameter should be non-zero and non-negative."
+ "ComputePatchCameraFocalLength: Patch distance should be non-zero and non-negative."
+ "Failed to compile model using e5 API"
+ "Failed to create e5 compiler"
+ "Failed to initialize Espresso model"
+ "Failed to initialize e5 program library for model"
+ "Model bundle folder structure mismatch"
+ "Model bundle format not supported"
+ "ODT"
+ "ODT detector creation failed: %!s(MISSING)"
+ "ODT tracker loading failed: %!s(MISSING)"
+ "Patch center is nan."
+ "Patch diameter is nan."
+ "Patch distance is nan."
+ "Pipeline not initialized"
+ "Pipeline type not supported. Choose either Detect or DetectTrackRefine."
+ "Reference object metadata file invalid"
+ "Reference objects have conflicting versions"
- "DetectPipeline config validation failed: "
- "DetectPipeline creation failed"
- "DetectTrackRefinePipeline creation failed"
- "Detector model creation error: "
- "Failed to initialize a pixel transfer session for detector."
- "ODT Error"
- "ODT: DetectPipeline init failed with error: %!s(MISSING)"
- "ODT: DetectPipeline reconfiguration failed with error: %!s(MISSING)"
- "ODT: DetectTrackRefinePipeline reconfiguration failed with error: %!s(MISSING)"
- "PatchTracker creation failed"
- "Result dropped"
- "Tracker model creation error: "
- "Unable to create compiler: "
- "patch_diameter > 0.0f && patch_distance > 0.0f"

```
