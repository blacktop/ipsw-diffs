## CoreMotion

> `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`

```diff

-3186.0.17.0.1
-  __TEXT.__text: 0x3c73bc
-  __TEXT.__objc_methlist: 0xd994
+3186.0.21.0.0
+  __TEXT.__text: 0x3c76ec
+  __TEXT.__objc_methlist: 0xd9ac
   __TEXT.__const: 0xcd60
   __TEXT.__swift5_typeref: 0x257
   __TEXT.__swift5_reflstr: 0x2e

   __TEXT.__constg_swiftt: 0xb8
   __TEXT.__swift5_fieldmd: 0x70
   __TEXT.__swift5_capture: 0x40
-  __TEXT.__oslogstring: 0x2fcb7
-  __TEXT.__cstring: 0x47a46
+  __TEXT.__oslogstring: 0x2fcd1
+  __TEXT.__cstring: 0x47ac5
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x10
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x30
-  __TEXT.__gcc_except_tab: 0xd4dc
-  __TEXT.__unwind_info: 0xd0d8
+  __TEXT.__gcc_except_tab: 0xd50c
+  __TEXT.__unwind_info: 0xd0f0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5718
+  __DATA_CONST.__objc_selrefs: 0x5728
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x7c8
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__got: 0x828
   __AUTH_CONST.__const: 0x158b8
   __AUTH_CONST.__cfstring: 0x13d20
-  __AUTH_CONST.__objc_const: 0x1dd68
+  __AUTH_CONST.__objc_const: 0x1dd78
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x90

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 12716
+  Functions: 12719
   Symbols:   1815
-  CStrings:  11438
+  CStrings:  11440
 
CStrings:
+ "#Spi, _CLInternalClearLocationAuthorizationLoctool failed"
+ "-[CLLocationInternalClient_CoreMotion clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:]_block_invoke"
+ "CLMotionTypeAngleEventPhase toCLMotionType(CMAngleReportEventPhase)"
+ "[CLAngleNotifier] Unrecognized phase 0x%{public}x"
+ "[CMAngleManager] Unrecognized phase 0x%{public}x"
+ "const char *toString(CMAngleReportEventPhase)"
- "-[CMDeviceStateManager queryDeviceStateBlocking]"
- "-[CMDeviceStateManager queryDeviceStateWithHandler:]"
- "queryDeviceStateBlocking is unsupported and should not be used."
- "queryDeviceStateWithHandler is unsupported and should not be used."
```
