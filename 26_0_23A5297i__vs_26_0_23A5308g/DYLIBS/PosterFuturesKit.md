## PosterFuturesKit

> `/System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit`

```diff

-286.101.0.0.0
-  __TEXT.__text: 0x15f78
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x20f4
+289.103.0.0.0
+  __TEXT.__text: 0x166b8
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x2134
   __TEXT.__const: 0xd0
   __TEXT.__cstring: 0x891
-  __TEXT.__gcc_except_tab: 0x570
+  __TEXT.__gcc_except_tab: 0x594
   __TEXT.__oslogstring: 0x4b4
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0xad0
+  __TEXT.__unwind_info: 0xaf0
   __TEXT.__objc_classname: 0x615
-  __TEXT.__objc_methname: 0x30ec
-  __TEXT.__objc_methtype: 0xa03
-  __TEXT.__objc_stubs: 0x24c0
+  __TEXT.__objc_methname: 0x31e0
+  __TEXT.__objc_methtype: 0xa26
+  __TEXT.__objc_stubs: 0x24e0
   __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0xd10
+  __DATA_CONST.__const: 0xd38
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdb8
+  __DATA_CONST.__objc_selrefs: 0xde0
   __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0x480
   __AUTH_CONST.__cfstring: 0x680
   __AUTH_CONST.__objc_const: 0xa258

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0DC7D49C-8D5F-39A4-ADEA-11DE014A8C84
-  Functions: 813
-  Symbols:   3102
-  CStrings:  945
+  UUID: BEAE7345-463B-3813-AAAC-AE1394768085
+  Functions: 825
+  Symbols:   3130
+  CStrings:  952
 
Symbols:
+ +[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]
+ +[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]
+ +[PFTScheduler serialDispatchQueueSchedulerWithName:qualityOfService:]
+ -[PFTFuture flatMap:continuationScheduler:]
+ -[PFTFuture flatMap:continuationScheduler:schedulerProvider:]
+ -[PFTFuture recover:onErrorScheduler:]
+ -[PFTFuture recover:onErrorScheduler:schedulerProvider:]
+ -[PFTFuture timeoutAfter:cleanup:]
+ -[PFTFuture timeoutAfter:scheduler:cleanup:]
+ GCC_except_table37
+ GCC_except_table53
+ _BSDispatchQueueCreateSerialWithQoS
+ __OBJC_$_PROP_LIST_PFTFuture.178
+ ___44-[PFTFuture timeoutAfter:scheduler:cleanup:]_block_invoke
+ ___44-[PFTFuture timeoutAfter:scheduler:cleanup:]_block_invoke_2
+ ___44-[PFTFuture timeoutAfter:scheduler:cleanup:]_block_invoke_3
+ ___66+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke
+ ___66+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke_2
+ ___66+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke_3
+ ___66+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke_4
+ ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke
+ ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_2
+ ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_3
+ ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_4
+ ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e8_v16?08ls48l8s32l8s40l8
+ _objc_msgSend$flatMap:continuationScheduler:schedulerProvider:
+ _objc_msgSend$flatMap:withBlock:continuationScheduler:schedulerProvider:
+ _objc_msgSend$recover:onErrorScheduler:schedulerProvider:
+ _objc_msgSend$recover:withBlock:onErrorScheduler:schedulerProvider:
+ _objc_msgSend$timeoutAfter:scheduler:cleanup:
- +[PFTFuture flatMap:withBlock:schedulerProvider:]
- +[PFTFuture recover:withBlock:schedulerProvider:]
- -[PFTFuture flatMap:schedulerProvider:]
- -[PFTFuture recover:schedulerProvider:]
- GCC_except_table31
- __OBJC_$_PROP_LIST_PFTFuture.172
- ___49+[PFTFuture flatMap:withBlock:schedulerProvider:]_block_invoke
- ___49+[PFTFuture flatMap:withBlock:schedulerProvider:]_block_invoke_2
- ___49+[PFTFuture recover:withBlock:schedulerProvider:]_block_invoke
- ___49+[PFTFuture recover:withBlock:schedulerProvider:]_block_invoke_2
- ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e8_v16?08ls40l8s32l8
- _objc_msgSend$flatMap:schedulerProvider:
- _objc_msgSend$flatMap:withBlock:schedulerProvider:
- _objc_msgSend$recover:schedulerProvider:
- _objc_msgSend$recover:withBlock:schedulerProvider:
CStrings:
+ "@28@0:8@16I24"
+ "@40@0:8d16@24@?32"
+ "@48@0:8@16@?24@32@40"
+ "flatMap:continuationScheduler:"
+ "flatMap:continuationScheduler:schedulerProvider:"
+ "flatMap:withBlock:continuationScheduler:schedulerProvider:"
+ "recover:onErrorScheduler:"
+ "recover:onErrorScheduler:schedulerProvider:"
+ "recover:withBlock:onErrorScheduler:schedulerProvider:"
+ "serialDispatchQueueSchedulerWithName:qualityOfService:"
+ "timeoutAfter:cleanup:"
+ "timeoutAfter:scheduler:cleanup:"
- "@40@0:8@16@?24@32"
- "flatMap:schedulerProvider:"
- "flatMap:withBlock:schedulerProvider:"
- "recover:schedulerProvider:"
- "recover:withBlock:schedulerProvider:"

```
