## HeartRateCoordinator

> `/System/Library/PrivateFrameworks/HeartRateCoordinator.framework/HeartRateCoordinator`

```diff

-  __TEXT.__text: 0x46b0
-  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__text: 0x4a80
+  __TEXT.__objc_methlist: 0x874
   __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x2e0
-  __TEXT.__oslogstring: 0x44f
+  __TEXT.__gcc_except_tab: 0x30c
+  __TEXT.__oslogstring: 0x48d
   __TEXT.__cstring: 0x25a
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x298
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x430
+  __DATA_CONST.__objc_selrefs: 0x458
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x10
-  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x1190
+  __AUTH_CONST.__objc_const: 0x11d8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0xc8
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x3c0
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 151
-  Symbols:   666
-  CStrings:  44
+  Functions: 158
+  Symbols:   688
+  CStrings:  45
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[HRCHeartRateRequestor handleRecentHighConfidenceHeartRates:]
+ -[HRCHeartRateRequestor recentHighConfidenceHeartRatesRequested]
+ -[HRCHeartRateRequestor setRecentHighConfidenceHeartRatesRequested:]
+ -[HRCHeartRateRequestorXPCHelper handleRecentHighConfidenceHeartRates:]
+ -[HRCHeartRateRequestorXPCHelper requestRecentHighConfidenceHeartRates]
+ GCC_except_table11
+ GCC_except_table14
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table9
+ _OBJC_IVAR_$_HRCHeartRateRequestor._recentHighConfidenceHeartRatesRequested
+ ___62-[HRCHeartRateRequestor handleRecentHighConfidenceHeartRates:]_block_invoke
+ ___62-[HRCHeartRateRequestor handleRecentHighConfidenceHeartRates:]_block_invoke_2
+ ___82-[HRCHeartRateRequestor initWithDelegate:onQueue:connectionHelper:privacyMonitor:]_block_invoke_3
+ _objc_msgSend$handleRecentHighConfidenceHeartRates:
+ _objc_msgSend$recentHighConfidenceHeartRatesRequested
+ _objc_msgSend$requestRecentHighConfidenceHeartRates
+ _objc_msgSend$setRecentHighConfidenceHeartRatesRequested:
+ _objc_msgSend$setWithObjects:
- GCC_except_table10
- GCC_except_table12
- GCC_except_table15
- GCC_except_table7
CStrings:
+ "handling recent high confidence heart rates in client process"

```
