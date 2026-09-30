## com.apple.aonsensed.camera-xpc

> `/System/Library/PrivateFrameworks/AONSenseService.framework/XPCServices/com.apple.aonsensed.camera-xpc.xpc/com.apple.aonsensed.camera-xpc`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-118.0.2.0.0
-  __TEXT.__text: 0x12c28
+131.0.0.0.0
+  __TEXT.__text: 0x12ef0
   __TEXT.__auth_stubs: 0xcb0
   __TEXT.__objc_stubs: 0xae0
   __TEXT.__objc_methlist: 0x2a0
   __TEXT.__const: 0x9a0
   __TEXT.__swift5_typeref: 0x6e4
-  __TEXT.__oslogstring: 0x166f
   __TEXT.__cstring: 0x3a4
-  __TEXT.__objc_methname: 0x101a
+  __TEXT.__oslogstring: 0x167f
+  __TEXT.__objc_methname: 0x103a
   __TEXT.__swift5_capture: 0x1d8
   __TEXT.__objc_methtype: 0x3f1
   __TEXT.__objc_classname: 0x162
   __TEXT.__constg_swiftt: 0x47c
-  __TEXT.__swift5_reflstr: 0x4d3
-  __TEXT.__swift5_fieldmd: 0x2fc
+  __TEXT.__swift5_reflstr: 0x4f3
+  __TEXT.__swift5_fieldmd: 0x308
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_assocty: 0x90

   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x400
+  __TEXT.__unwind_info: 0x408
   __TEXT.__eh_frame: 0x158
   __DATA_CONST.__const: 0x938
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__auth_got: 0x660
   __DATA_CONST.__got: 0x218
   __DATA_CONST.__auth_ptr: 0x270
-  __DATA.__objc_const: 0xa80
+  __DATA.__objc_const: 0xaa0
   __DATA.__objc_selrefs: 0x3c8
-  __DATA.__objc_data: 0x518
+  __DATA.__objc_data: 0x520
   __DATA.__data: 0x528
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 316
-  Symbols:   1224
-  CStrings:  315
+  Functions: 317
+  Symbols:   1226
+  CStrings:  317
 
Symbols:
+ _$s30com_apple_aonsensed_camera_xpc18ALCameraXPCServiceC22disableConvergenceGate33_22D344278D26B8DDDF15E77B95C8AE90LLSbvpWvd
+ _$s30com_apple_aonsensed_camera_xpc18ALCameraXPCServiceC22disableConvergenceGate33_22D344278D26B8DDDF15E77B95C8AE90LLSbvpfi
+ _$s30com_apple_aonsensed_camera_xpc18ALCameraXPCServiceC27configureDynamicAspectRatio33_22D344278D26B8DDDF15E77B95C8AE90LL3forSbSo15AVCaptureDeviceC_tF
+ _$s30com_apple_aonsensed_camera_xpc18ALCameraXPCServiceC27configureDynamicAspectRatio33_22D344278D26B8DDDF15E77B95C8AE90LL3forSbSo15AVCaptureDeviceC_tFTf4nd_n
- _$s30com_apple_aonsensed_camera_xpc18ALCameraXPCServiceC27configureDynamicAspectRatio33_22D344278D26B8DDDF15E77B95C8AE90LL3forySo15AVCaptureDeviceC_tF
- _$s30com_apple_aonsensed_camera_xpc18ALCameraXPCServiceC27configureDynamicAspectRatio33_22D344278D26B8DDDF15E77B95C8AE90LL3forySo15AVCaptureDeviceC_tFTf4nd_n
CStrings:
+ "Camera XPC: DisableCameraConvergenceGate = %s"
+ "Camera XPC: Failed to lock camera for configuration: %s, falling back to minimal full-FoV"
+ "Camera XPC: No format supports dynamic aspect ratio on %s, falling back to minimal full-FoV"
+ "Camera XPC: selectActiveFormat for %s — isFrontUltraWide=%{bool}d"
+ "DisableCameraConvergenceGate"
+ "disableConvergenceGate"
- "Camera XPC: Failed to lock camera for configuration: %s"
- "Camera XPC: No format supports dynamic aspect ratio on this device, continuing with default"
- "Camera XPC: selectActiveFormat for %s — isFrontUltraWide=%{bool}d, EnableNonCroppedFCAMFullFoV=%{bool}d, useDynamicAspectRatio=%{bool}d"
- "EnableNonCroppedFCAMFullFoV"
```
