## VoiceOver

> `/System/Library/AccessibilityBundles/VoiceOver.axuiservice/VoiceOver`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__objc_stublist`

```diff

-2482.13.4.0.0
-  __TEXT.__text: 0x24f64
-  __TEXT.__auth_stubs: 0x1400
-  __TEXT.__objc_stubs: 0x4de0
-  __TEXT.__objc_methlist: 0x1e84
+2482.13.12.0.0
+  __TEXT.__text: 0x25688
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_stubs: 0x4f40
+  __TEXT.__objc_methlist: 0x1f0c
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__const: 0xca0
-  __TEXT.__objc_classname: 0x640
-  __TEXT.__objc_methname: 0x7150
+  __TEXT.__const: 0xcb0
+  __TEXT.__objc_classname: 0x654
+  __TEXT.__objc_methname: 0x72c3
   __TEXT.__constg_swiftt: 0xaa4
   __TEXT.__swift5_typeref: 0x10ce
   __TEXT.__swift5_reflstr: 0x413
   __TEXT.__swift5_fieldmd: 0x4e8
   __TEXT.__swift5_proto: 0x80
   __TEXT.__swift5_types: 0x44
-  __TEXT.__cstring: 0x1428
+  __TEXT.__cstring: 0x1467
   __TEXT.__swift5_assocty: 0x98
-  __TEXT.__objc_methtype: 0x1df6
+  __TEXT.__objc_methtype: 0x1e58
   __TEXT.__swift5_capture: 0x198
-  __TEXT.__oslogstring: 0x35c
+  __TEXT.__oslogstring: 0x40e
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x2c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__unwind_info: 0xbe8
+  __TEXT.__gcc_except_tab: 0x27c
+  __TEXT.__unwind_info: 0xc10
   __TEXT.__eh_frame: 0x4a0
-  __DATA_CONST.__const: 0x2068
+  __DATA_CONST.__const: 0x2090
   __DATA_CONST.__cfstring: 0xde0
   __DATA_CONST.__objc_classlist: 0x120
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0x150
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0xa10
-  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__auth_ptr: 0x2f8
-  __DATA.__objc_const: 0x38f0
-  __DATA.__objc_selrefs: 0x1ac8
-  __DATA.__objc_ivar: 0x204
+  __DATA.__objc_const: 0x3988
+  __DATA.__objc_selrefs: 0x1b38
+  __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0xae0
-  __DATA.__data: 0x16c8
+  __DATA.__data: 0x1728
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x28
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities
   - /System/Library/PrivateFrameworks/AXRuntime.framework/AXRuntime
+  - /System/Library/PrivateFrameworks/AccessibilitySharedSupport.framework/AccessibilitySharedSupport
   - /System/Library/PrivateFrameworks/AccessibilityUIService.framework/AccessibilityUIService
   - /System/Library/PrivateFrameworks/AccessibilityUIShared.framework/AccessibilityUIShared
   - /System/Library/PrivateFrameworks/AccessibilityUIUtilities.framework/AccessibilityUIUtilities

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 849
-  Symbols:   420
-  CStrings:  1536
+  Functions: 858
+  Symbols:   427
+  CStrings:  1565
 
Symbols:
+ _AXHingeFoldAxisForMagicPose
+ _CGAffineTransformEqualToTransform
+ _CGAffineTransformMakeTranslation
+ _OBJC_CLASS_$_AXHingePoseMonitor
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_release_x1
CStrings:
+ "AXHingePoseObserver"
+ "Assessment mode changed, restricted: %d"
+ "Began hinge pose monitoring"
+ "Cursor hidden from screen capture: %d"
+ "Ended hinge pose monitoring"
+ "Rotor hinge fold axis %ld -> %ld (pose %ld)"
+ "_applyHingeFoldOffsetAnimated:"
+ "_assessmentModeChanged"
+ "_assessmentModeNotifyToken"
+ "_captionTextShouldShow"
+ "_hingeFoldAxis"
+ "_isMonitoringHingePose"
+ "_updateCaptureMask"
+ "addObserver:"
+ "com.apple.accessibility.guidedaccess.restrictedForAAC"
+ "hingePoseMonitor:didUpdateAngle:"
+ "hingePoseMonitor:didUpdateMagicPose:"
+ "isAvailable"
+ "isRestrictedForAAC"
+ "setHingeFoldAxis:animated:"
+ "sharedMonitor"
+ "transform"
+ "v12@?0i8"
+ "v28@0:8q16B24"
+ "v32@0:8@\"AXHingePoseMonitor\"16d24"
+ "v32@0:8@\"AXHingePoseMonitor\"16q24"
+ "v32@0:8@16d24"
+ "viewDidLayoutSubviews"
+ "viewIfLoaded"
```
