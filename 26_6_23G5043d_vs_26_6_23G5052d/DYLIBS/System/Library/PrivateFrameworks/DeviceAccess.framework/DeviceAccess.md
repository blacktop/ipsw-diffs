## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-  __TEXT.__text: 0x563cc
+  __TEXT.__text: 0x564c0
   __TEXT.__auth_stubs: 0x1640
-  __TEXT.__objc_methlist: 0x45dc
+  __TEXT.__objc_methlist: 0x45ec
   __TEXT.__const: 0x900
-  __TEXT.__cstring: 0x9f33
+  __TEXT.__cstring: 0x9fc3
   __TEXT.__gcc_except_tab: 0x1330
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x264

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x1500
+  __TEXT.__unwind_info: 0x1508
   __TEXT.__eh_frame: 0x5c0
   __TEXT.__objc_classname: 0x6b4
-  __TEXT.__objc_methname: 0x8ac4
+  __TEXT.__objc_methname: 0x8ae4
   __TEXT.__objc_methtype: 0xc26
   __TEXT.__objc_stubs: 0x4ba0
   __DATA_CONST.__got: 0x530

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f60
+  __DATA_CONST.__objc_selrefs: 0x1f68
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_arraydata: 0x30
+  __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0xb30
   __AUTH_CONST.__const: 0x6d0
-  __AUTH_CONST.__cfstring: 0x3540
-  __AUTH_CONST.__objc_const: 0x7e18
+  __AUTH_CONST.__cfstring: 0x3580
+  __AUTH_CONST.__objc_const: 0x7e28
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xb60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2297
-  Symbols:   6483
-  CStrings:  3753
+  Functions: 2299
+  Symbols:   6487
+  CStrings:  3760
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[DADeviceRegistry requiresCompanionApp]
+ ___30-[DADiscovery _activateDirect]_block_invoke_2.cold.1
+ ___block_literal_global.268
+ ___block_literal_global.279
+ ___block_literal_global.286
- ___block_literal_global.262
- ___block_literal_global.273
- ___block_literal_global.280
Functions:
~ ___30-[DADiscovery _activateDirect]_block_invoke_2 : 500 -> 556
+ -[DADeviceRegistry requiresCompanionApp]
+ ___29-[DADiscovery migrateDevices]_block_invoke.cold.1
CStrings:
+ "-[DADiscovery _activateDirect]_block_invoke_2"
+ "Discovery Extension count : %lu"
+ "bluetoothDualModeAppRequired"
+ "bluetoothLEModeAppRequired"
+ "requiresCompanionApp"

```
