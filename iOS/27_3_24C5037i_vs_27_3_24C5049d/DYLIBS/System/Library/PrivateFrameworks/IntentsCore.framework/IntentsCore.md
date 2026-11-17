## IntentsCore

> `/System/Library/PrivateFrameworks/IntentsCore.framework/IntentsCore`

```diff

-4016.2.7.0.0
-  __TEXT.__text: 0x16fcc
-  __TEXT.__objc_methlist: 0x10e4
+4016.2.11.0.0
+  __TEXT.__text: 0x171f8
+  __TEXT.__objc_methlist: 0x110c
   __TEXT.__const: 0xa8
   __TEXT.__dlopen_cstrs: 0x4e4
   __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__cstring: 0x234a
+  __TEXT.__cstring: 0x2399
   __TEXT.__oslogstring: 0x2175
-  __TEXT.__unwind_info: 0x778
+  __TEXT.__unwind_info: 0x780
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_selrefs: 0x1190
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__got: 0x428
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x640
-  __AUTH_CONST.__objc_const: 0x2350
+  __AUTH_CONST.__objc_const: 0x2380
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x14c
+  __DATA.__objc_ivar: 0x150
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x420
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 448
-  Symbols:   1128
+  Functions: 451
+  Symbols:   1135
   CStrings:  348
 
Symbols:
+ -[INCExtensionProxy _extensionAuditTokenData]
+ -[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:intentResponseSenderAuditTokenData:]
+ -[INCExtensionTransactionState initWithType:intent:intentResponse:intentResponseSenderAuditTokenData:userActivities:]
+ -[INCExtensionTransactionState intentResponseSenderAuditTokenData]
+ GCC_except_table196
+ GCC_except_table209
+ GCC_except_table212
+ GCC_except_table236
+ GCC_except_table254
+ GCC_except_table255
+ GCC_except_table262
+ GCC_except_table266
+ GCC_except_table270
+ GCC_except_table274
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table284
+ GCC_except_table297
+ GCC_except_table311
+ GCC_except_table316
+ GCC_except_table391
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table413
+ GCC_except_table436
+ GCC_except_table441
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_IVAR_$_INCExtensionTransactionState._intentResponseSenderAuditTokenData
+ ___118-[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:intentResponseSenderAuditTokenData:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56bs_e47_v32?0"INIntentResponse"8"NSData"16"NSSet"24ls32l8s40l8s48l8s56l8
+ _class_getSuperclass
+ _object_getClass
- -[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:]
- GCC_except_table194
- GCC_except_table207
- GCC_except_table210
- GCC_except_table234
- GCC_except_table252
- GCC_except_table253
- GCC_except_table260
- GCC_except_table264
- GCC_except_table268
- GCC_except_table272
- GCC_except_table275
- GCC_except_table278
- GCC_except_table282
- GCC_except_table295
- GCC_except_table309
- GCC_except_table314
- GCC_except_table388
- GCC_except_table393
- GCC_except_table397
- GCC_except_table410
- GCC_except_table433
- GCC_except_table438
- ___83-[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56bs_e36_v24?0"INIntentResponse"8"NSSet"16ls32l8s40l8s48l8s56l8
CStrings:
+ "-[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:intentResponseSenderAuditTokenData:]"
+ "-[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:intentResponseSenderAuditTokenData:]_block_invoke"
+ "v32@?0@\"INIntentResponse\"8@\"NSData\"16@\"NSSet\"24"
- "-[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:]"
- "-[INCExtensionTransaction _updateCurrentUserActivityForType:intent:intentResponse:]_block_invoke"
- "v24@?0@\"INIntentResponse\"8@\"NSSet\"16"
```
