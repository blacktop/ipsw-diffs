## fmflocatord

> `/usr/libexec/fmflocatord`

```diff

-87.32.7.13.7
-  __TEXT.__text: 0x3624c
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_stubs: 0x6e20
-  __TEXT.__objc_methlist: 0x304c
+87.32.7.13.10
+  __TEXT.__text: 0x36c1c
+  __TEXT.__auth_stubs: 0x14f0
+  __TEXT.__objc_stubs: 0x6e60
+  __TEXT.__objc_methlist: 0x3074
   __TEXT.__objc_classname: 0x606
-  __TEXT.__objc_methname: 0x7f33
+  __TEXT.__objc_methname: 0x7f62
   __TEXT.__objc_methtype: 0x121a
   __TEXT.__const: 0x550
-  __TEXT.__cstring: 0x3441
-  __TEXT.__oslogstring: 0x3fe4
+  __TEXT.__cstring: 0x3421
+  __TEXT.__oslogstring: 0x40a4
   __TEXT.__gcc_except_tab: 0x9dc
   __TEXT.__swift5_typeref: 0x21b
   __TEXT.__swift5_capture: 0x108

   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0xde8
+  __TEXT.__unwind_info: 0xdf0
   __TEXT.__eh_frame: 0x638
-  __DATA_CONST.__auth_got: 0xa70
-  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__auth_got: 0xa88
+  __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x1bd0
-  __DATA_CONST.__cfstring: 0x3e60
+  __DATA_CONST.__const: 0x1bd8
+  __DATA_CONST.__cfstring: 0x3e40
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xd0

   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x9580
-  __DATA.__objc_selrefs: 0x1f70
+  __DATA.__objc_const: 0x95a0
+  __DATA.__objc_selrefs: 0x1f88
   __DATA.__objc_ivar: 0x294
   __DATA.__objc_data: 0x1190
   __DATA.__data: 0xa70

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1442
-  Symbols:   556
-  CStrings:  2675
+  Functions: 1448
+  Symbols:   562
+  CStrings:  2681
 
Symbols:
+ _$s12FindMyLocate5FenceV8ScheduleV11descriptionSSvg
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSd5write2toyxz_ts16TextOutputStreamRzlF
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ __swift_FORCE_LOAD_$_swiftOSLog
CStrings:
+ "Fence is already monitored. No need to update monitored region of fence %!@(MISSING)"
+ "Monitoring %!l(MISSING)d fences in fmflocatord & %!l(MISSING)d fences in CoreLocation"
+ "Removing the monitored fences by location manager..."
+ "Starting monitoring fence %!@(MISSING)"
+ "_updateGeoFences"
+ "cleanupLocMgr"
+ "updateGeoFences"
- "Removing the FMF fences location manager..."
- "fmf fences - expected:%!l(MISSING)d, actual:%!l(MISSING)d"

```
