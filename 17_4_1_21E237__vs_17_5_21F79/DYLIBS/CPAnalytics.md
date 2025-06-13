## CPAnalytics

> `/System/Library/PrivateFrameworks/CPAnalytics.framework/CPAnalytics`

```diff

-646.1.102.0.0
-  __TEXT.__text: 0xf300
+652.0.100.0.0
+  __TEXT.__text: 0xf668
   __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x10b0
+  __TEXT.__objc_methlist: 0x10e0
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__cstring: 0x16a6
-  __TEXT.__oslogstring: 0xd71
-  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__gcc_except_tab: 0x118
+  __TEXT.__cstring: 0x16af
+  __TEXT.__oslogstring: 0xdc4
+  __TEXT.__unwind_info: 0x498
   __TEXT.__objc_classname: 0x3ad
-  __TEXT.__objc_methname: 0x306e
+  __TEXT.__objc_methname: 0x30b4
   __TEXT.__objc_methtype: 0x4cf
-  __TEXT.__objc_stubs: 0x2900
+  __TEXT.__objc_stubs: 0x2940
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0x670
   __DATA_CONST.__objc_classlist: 0xd0

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1e40
-  __DATA_CONST.__objc_selrefs: 0xb10
+  __DATA_CONST.__objc_selrefs: 0xb20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__cfstring: 0x1e20
+  __AUTH_CONST.__cfstring: 0x1e40
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x2d8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftDemangle.dylib
-  UUID: ED85A960-4B34-36D2-AA4D-76431094E96D
-  Functions: 357
-  Symbols:   1680
-  CStrings:  1195
+  UUID: C55C517C-F550-3EE0-B097-0F3262ACC38A
+  Functions: 362
+  Symbols:   1693
+  CStrings:  1201
 
Symbols:
+ +[CPAnalytics updateWithConfiguration:]
+ -[CPAnalytics updateWithConfiguration:]
+ -[CPAnalyticsDestinationsRegistry updateWithConfiguration:cpAnalyticsInstance:]
+ -[CPAnalyticsEventCounter description]
+ GCC_except_table120
+ GCC_except_table127
+ GCC_except_table130
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table328
+ ___39-[CPAnalytics updateWithConfiguration:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_literal_global.288
+ ___block_literal_global.523
+ ___block_literal_global.650
+ ___block_literal_global.920
+ _objc_msgSend$updateWithConfiguration:
+ _objc_msgSend$updateWithConfiguration:cpAnalyticsInstance:
- GCC_except_table119
- GCC_except_table123
- GCC_except_table128
- GCC_except_table159
- GCC_except_table323
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_literal_global.284
- ___block_literal_global.521
- ___block_literal_global.646
- ___block_literal_global.915
CStrings:
+ "Name: %@"
+ "[AppStateDestination] Updated %d featureCounters %@"
+ "update: empty configuration %@"
+ "updateWithConfiguration:"
+ "updateWithConfiguration:cpAnalyticsInstance:"

```
