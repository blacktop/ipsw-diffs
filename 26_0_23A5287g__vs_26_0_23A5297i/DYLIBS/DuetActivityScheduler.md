## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-2109.0.69.0.1
-  __TEXT.__text: 0x34bc0
-  __TEXT.__auth_stubs: 0x6b0
+2109.0.84.0.0
+  __TEXT.__text: 0x34ec4
+  __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x4108
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x14e4
-  __TEXT.__cstring: 0x2600
-  __TEXT.__oslogstring: 0x2ec0
-  __TEXT.__unwind_info: 0xfa0
+  __TEXT.__gcc_except_tab: 0x1530
+  __TEXT.__cstring: 0x25d8
+  __TEXT.__oslogstring: 0x2f8a
+  __TEXT.__unwind_info: 0xfc0
   __TEXT.__objc_classname: 0x727
   __TEXT.__objc_methname: 0xa298
   __TEXT.__objc_methtype: 0x1ae3
   __TEXT.__objc_stubs: 0x5a60
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0xee0
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0xe98
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x110

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x368
-  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__auth_got: 0x398
+  __AUTH_CONST.__const: 0x260
   __AUTH_CONST.__cfstring: 0x3680
   __AUTH_CONST.__objc_const: 0x73a8
   __AUTH_CONST.__objc_arrayobj: 0xa8

   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x460
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x428
   __DATA.__data: 0xdf0
   __DATA.__bss: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C25C62E-38C8-3EC5-B6EA-490331ED5B80
-  Functions: 1473
-  Symbols:   5146
-  CStrings:  3206
+  UUID: D2BBDFC4-CF65-31E1-ABB4-4A0ADA54554A
+  Functions: 1479
+  Symbols:   5164
+  CStrings:  3209
 
Symbols:
+ _CFBinaryHeapAddValue
+ _CFBinaryHeapCreate
+ _CFBinaryHeapGetCount
+ _CFBinaryHeapGetMinimum
+ _CFBinaryHeapRemoveMinimumValue
+ _CFRelease
+ __DASBinaryHeapBiomeStoreEventCallbacks
+ __DASBinaryHeapReleaseCallback
+ __DASBinaryHeapRetainCallback
+ __DASBiomeStoreEventCompareByDate
+ ___35-[_DASBMHistogramBuilder histogram]_block_invoke.64
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.349.cold.1
+ ___73-[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]_block_invoke.9.cold.1
+ ___73-[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]_block_invoke.9.cold.2
+ ___78-[_DASBMMinimumSpanConfiguration deriveSpanTuplesWithMinimumDurationOnStream:]_block_invoke.12
+ ___block_literal_global.61
+ _kCFAllocatorDefault
- GCC_except_table28
- ___35-[_DASBMHistogramBuilder histogram]_block_invoke.67
- ___73-[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]_block_invoke_2
- ___78-[_DASBMMinimumSpanConfiguration deriveSpanTuplesWithMinimumDurationOnStream:]_block_invoke.14
- ___block_descriptor_32_e39_q24?0"BMStoreEvent"8"BMStoreEvent"16l
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_literal_global.17
- ___block_literal_global.64
CStrings:
+ "Cannot create heap, expected item count is too large; bailing"
+ "Error trying to get allocations for given parameters"
+ "Failed to create heap; bailing"
+ "Successfully retrieved allocations for given parameters"
- "q24@?0@\"BMStoreEvent\"8@\"BMStoreEvent\"16"

```
