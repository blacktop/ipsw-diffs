## tailspind

> `/usr/libexec/tailspind`

```diff

-200.0.0.0.0
-  __TEXT.__text: 0x8f48
+200.1.0.0.0
+  __TEXT.__text: 0x9258
   __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x104
+  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_methlist: 0x14c
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x867
-  __TEXT.__objc_methname: 0x7a3
-  __TEXT.__oslogstring: 0x1fa4
+  __TEXT.__cstring: 0x8d8
+  __TEXT.__objc_methname: 0x92c
+  __TEXT.__oslogstring: 0x1ff1
   __TEXT.__objc_classname: 0x16
-  __TEXT.__objc_methtype: 0xda
+  __TEXT.__objc_methtype: 0xe5
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__unwind_info: 0x1a8
   __DATA_CONST.__auth_got: 0x590
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x370
-  __DATA_CONST.__cfstring: 0x400
+  __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x180
-  __DATA.__objc_selrefs: 0x218
-  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_const: 0x210
+  __DATA.__objc_selrefs: 0x250
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2168
   __DATA.__crash_info: 0x40

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 147
+  Functions: 154
   Symbols:   228
-  CStrings:  312
+  CStrings:  332
 
CStrings:
+ "LostTimePeriodAtStart"
+ "PercentageTimeCovered"
+ "RequestProcessingLatency"
+ "Td,R,N,V_lostTimePeriodAtStartSecs"
+ "Td,R,N,V_ratioTimePeriodCovered"
+ "Td,R,N,V_requestProcessingLatencySecs"
+ "_lostTimePeriodAtStartSecs"
+ "_ratioTimePeriodCovered"
+ "_requestProcessingLatencySecs"
+ "client %!s(MISSING) [%!d(MISSING)] requested for tailspin data but was rejected by the allowlist"
+ "hangtracerd"
+ "lostTimePeriodAtStartSecs"
+ "numberWithInt:"
+ "ratioTimePeriodCovered"
+ "recordLostTimePeriodAtStart:"
+ "recordRatioTimePeriodCovered:"
+ "recordRequestProcessingLatencySecsWithStartMCT:endMCT:"
+ "requestProcessingLatencySecs"
+ "tailspin_dump_request_timestamp"
+ "v24@0:8d16"

```
