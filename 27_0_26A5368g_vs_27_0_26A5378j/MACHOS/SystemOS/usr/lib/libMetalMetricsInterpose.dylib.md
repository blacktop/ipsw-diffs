## libMetalMetricsInterpose.dylib

> `/usr/lib/libMetalMetricsInterpose.dylib`

```diff

-  __TEXT.__text: 0x1491c
-  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__text: 0x14800
+  __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0xf40
   __TEXT.__objc_methlist: 0xf8
-  __TEXT.__gcc_except_tab: 0x1328
+  __TEXT.__gcc_except_tab: 0x1308
   __TEXT.__const: 0x4c8
   __TEXT.__cstring: 0x5c9
-  __TEXT.__objc_methname: 0xdc0
+  __TEXT.__objc_methname: 0xdab
   __TEXT.__objc_classname: 0x1e
   __TEXT.__objc_methtype: 0x3b7
   __TEXT.__unwind_info: 0x8d8

   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x110
   __DATA.__objc_const: 0x220
   __DATA.__objc_selrefs: 0x438
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1
+  __DATA.__data: 0x10
   __DATA.__thread_vars: 0xa8
   __DATA.__thread_bss: 0x7
   __DATA.__common: 0x9

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 391
-  Symbols:   985
+  Symbols:   988
   CStrings:  238
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__thread_vars : content changed
Symbols:
+ __ZL24_EncoderCounterOffsetKey
+ _objc_getAssociatedObject
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_setAssociatedObject
- _objc_msgSend$metalGetEncoderCounterOffset:encoderTraceId:
Functions:
~ __Z30_MTMResolveEncoderGPUTimestampyym23FPMTLMetricsEncoderTypebPy : 412 -> 460
~ __ZL60MTL4CommandBuffer_renderCommandEncoderWithDescriptor_optionsPFvvEP11objc_objectP13objc_selectorP24MTL4RenderPassDescriptorm : 952 -> 1072
~ __ZL39MTL4CommandBuffer_computeCommandEncoderPFvvEP11objc_objectP13objc_selector : 564 -> 692
~ __ZL36MTL4RenderCommandEncoder_EndEncodingPFvvEP11objc_objectP13objc_selector : 988 -> 736
~ __ZL37MTL4ComputeCommandEncoder_EndEncodingPFvvEP11objc_objectP13objc_selector : 948 -> 704
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE25__parse_equivalence_classIPKcEET_S7_S7_PNS_20__bracket_expressionIcS2_EE : 524 -> 500
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE23__parse_character_classIPKcEET_S7_S7_PNS_20__bracket_expressionIcS2_EE : 176 -> 152
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE24__parse_collating_symbolIPKcEET_S7_S7_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE : 228 -> 204
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE19__add_back_capacityEv : 480 -> 468
CStrings:
+ "numberWithUnsignedLong:"
- "metalGetEncoderCounterOffset:encoderTraceId:"

```
