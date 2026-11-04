## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-2467.40.49.0.0
-  __TEXT.__text: 0x3e170
-  __TEXT.__objc_methlist: 0x4a48
+2467.60.9.0.0
+  __TEXT.__text: 0x3e57c
+  __TEXT.__objc_methlist: 0x4a78
   __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x1628
-  __TEXT.__cstring: 0x4280
-  __TEXT.__oslogstring: 0x32d7
-  __TEXT.__unwind_info: 0x1768
+  __TEXT.__gcc_except_tab: 0x1644
+  __TEXT.__cstring: 0x42dd
+  __TEXT.__oslogstring: 0x32ff
+  __TEXT.__unwind_info: 0x1780
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2960
+  __DATA_CONST.__objc_selrefs: 0x2988
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__got: 0x330
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x5340
-  __AUTH_CONST.__objc_const: 0x7fb8
+  __AUTH_CONST.__cfstring: 0x5420
+  __AUTH_CONST.__objc_const: 0x7ff0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x228

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x4a8
+  __DATA.__objc_ivar: 0x4ac
   __DATA.__data: 0xd68
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x730

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1695
-  Symbols:   2847
-  CStrings:  1010
+  Functions: 1703
+  Symbols:   2853
+  CStrings:  1018
 
Symbols:
+ -[_DASActivity launchQoS]
+ -[_DASActivity setLaunchQoS:]
+ -[_DASScheduler carryLaunchQoSFromActivity:toActivity:]
+ -[_DASScheduler setDoItNowRuntimeBudget:groupType:percentAvailable:]
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table144
+ GCC_except_table148
+ GCC_except_table158
+ GCC_except_table191
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table286
+ GCC_except_table289
+ GCC_except_table292
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table316
+ GCC_except_table319
+ GCC_except_table322
+ _OBJC_IVAR_$__DASActivity._launchQoS
+ __DASQoSClassName
+ ___68-[_DASScheduler setDoItNowRuntimeBudget:groupType:percentAvailable:]_block_invoke
- GCC_except_table123
- GCC_except_table136
- GCC_except_table139
- GCC_except_table142
- GCC_except_table145
- GCC_except_table157
- GCC_except_table190
- GCC_except_table221
- GCC_except_table224
- GCC_except_table227
- GCC_except_table230
- GCC_except_table233
- GCC_except_table236
- GCC_except_table246
- GCC_except_table249
- GCC_except_table252
- GCC_except_table255
- GCC_except_table258
- GCC_except_table261
- GCC_except_table264
- GCC_except_table267
- GCC_except_table270
- GCC_except_table273
- GCC_except_table276
- GCC_except_table279
- GCC_except_table282
- GCC_except_table285
- GCC_except_table288
- GCC_except_table291
- GCC_except_table294
- GCC_except_table297
- GCC_except_table300
- GCC_except_table303
- GCC_except_table306
- GCC_except_table309
- GCC_except_table312
- GCC_except_table315
- GCC_except_table318
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__DASActivitySchedulerIntrospectingServer
CStrings:
+ ", Launch QoS: %@"
+ "Error setting runtime budget for %@: %@"
+ "QoS %u"
+ "QoS Downgrade,"
+ "Unspecified"
+ "User Initiated"
+ "User Interactive"
+ "launchQoS"
```
