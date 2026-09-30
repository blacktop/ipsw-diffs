## PosterFuturesKit

> `/System/Library/PrivateFrameworks/PosterFuturesKit.framework/PosterFuturesKit`

```diff

-304.5.1.0.0
-  __TEXT.__text: 0x16d8c
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x2134
+304.5.3.0.0
+  __TEXT.__text: 0x1717c
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0x213c
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x891
-  __TEXT.__gcc_except_tab: 0x58c
-  __TEXT.__oslogstring: 0x4b4
+  __TEXT.__cstring: 0x933
+  __TEXT.__gcc_except_tab: 0x59c
+  __TEXT.__oslogstring: 0x568
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__unwind_info: 0xae0
+  __TEXT.__unwind_info: 0xb00
   __TEXT.__objc_classname: 0x615
-  __TEXT.__objc_methname: 0x31e0
-  __TEXT.__objc_methtype: 0xa26
-  __TEXT.__objc_stubs: 0x24e0
+  __TEXT.__objc_methname: 0x31e8
+  __TEXT.__objc_methtype: 0xa53
+  __TEXT.__objc_stubs: 0x24c0
   __DATA_CONST.__got: 0x290
   __DATA_CONST.__const: 0xd38
   __DATA_CONST.__objc_classlist: 0x1a8

   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xde0
-  __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x3f0
+  __DATA_CONST.__objc_superrefs: 0x108
+  __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x680
-  __AUTH_CONST.__objc_const: 0xa258
+  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__objc_const: 0xa278
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x13c
+  __DATA.__objc_ivar: 0x140
   __DATA.__data: 0x620
   __DATA.__bss: 0x2e8
   __DATA_DIRTY.__objc_data: 0x820

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CE847A40-3C9C-30F2-8967-97F427086E62
-  Functions: 830
-  Symbols:   3140
-  CStrings:  952
+  UUID: 3E4279A7-3843-3765-8F32-2C6ED89BEBD9
+  Functions: 834
+  Symbols:   3146
+  CStrings:  957
 
Symbols:
+ -[PFTFutureResult init]
+ GCC_except_table44
+ _OBJC_IVAR_$_PFTFutureResult._lock
+ _OBJC_IVAR_$_PFTFutureResult._lock_error
+ _OBJC_IVAR_$_PFTFutureResult._lock_result
+ __BSIsInternalInstall
+ __OBJC_$_PROP_LIST_PFTFuture.181
+ ___66+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke.12
+ ___66+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke_3.cold.1
+ ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke.8
+ ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_2.10
+ ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_2.cold.1
- _OBJC_IVAR_$_PFTFutureResult._error
- _OBJC_IVAR_$_PFTFutureResult._result
- __OBJC_$_PROP_LIST_PFTFuture.178
- ___66+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke_4
- ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_3
- ___71+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_4
- _objc_msgSend$setResult:
CStrings:
+ "+[PFTFuture flatMap:withBlock:continuationScheduler:schedulerProvider:]_block_invoke_2"
+ "+[PFTFuture recover:withBlock:onErrorScheduler:schedulerProvider:]_block_invoke_3"
+ "T@\"NSError\",C,N"
+ "T@,&,N"
+ "_lock_error"
+ "_lock_result"
+ "flatMap continuation returned nil — this is a programming error. Call stack: %{public}@"
+ "recover continuation returned nil — this is a programming error. Call stack: %{public}@"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "T@\"NSError\",C,N,V_error"
- "T@,&,N,V_result"

```
