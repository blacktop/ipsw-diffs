## hangreporter

> `/usr/libexec/hangreporter`

```diff

-326.0.0.0.0
-  __TEXT.__text: 0x36c8c
+331.0.0.0.0
+  __TEXT.__text: 0x36ef0
   __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_stubs: 0x2a60
-  __TEXT.__objc_methlist: 0xd1c
+  __TEXT.__objc_stubs: 0x2a80
+  __TEXT.__objc_methlist: 0xd2c
   __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x2b92e
+  __TEXT.__cstring: 0x2bc63
   __TEXT.__oslogstring: 0x41f7
   __TEXT.__gcc_except_tab: 0x7ac
-  __TEXT.__objc_methname: 0x4c2a
+  __TEXT.__objc_methname: 0x4cba
   __TEXT.__objc_classname: 0x113
   __TEXT.__objc_methtype: 0x851
   __TEXT.__unwind_info: 0x448
   __DATA_CONST.__auth_got: 0x750
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1328
-  __DATA_CONST.__cfstring: 0x4860
+  __DATA_CONST.__const: 0x1330
+  __DATA_CONST.__cfstring: 0x4880
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x2628
-  __DATA.__objc_selrefs: 0xed8
-  __DATA.__objc_ivar: 0x238
+  __DATA.__objc_const: 0x2658
+  __DATA.__objc_selrefs: 0xee8
+  __DATA.__objc_ivar: 0x23c
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x638
   __DATA.__bss: 0xb8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 559
+  Functions: 558
   Symbols:   318
-  CStrings:  4614
+  CStrings:  4633
 
CStrings:
+ "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): (#30) cfg elements != (%!d(MISSING)) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): Cannot add 30 elements to context"
+ "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): (#30) cfg elements != (%!d(MISSING)) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): Cannot add 30 elements to context"
+ "ASPFTLParseBufferToCxt: cbdrRefreshGradesSLC(767): (#10) cfg elements != (%!d(MISSING)) buffer elements"
+ "ASPFTLParseBufferToCxt: cbdrRefreshGradesSLC(767): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: cbdrScanPctSLC(769): (#5) cfg elements != (%!d(MISSING)) buffer elements"
+ "ASPFTLParseBufferToCxt: cbdrScanPctSLC(769): Cannot add 5 elements to context"
+ "ASPFTLParseBufferToCxt: hostWritesPerThrottleZone(1215): (#5) cfg elements != (%!d(MISSING)) buffer elements"
+ "ASPFTLParseBufferToCxt: hostWritesPerThrottleZone(1215): Cannot add 5 elements to context"
+ "ASPFTLParseBufferToCxt: prefetchNextRange(831) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: unexpectedBlanksInternal(596) cannot add 1 element to context"
+ "HangTracerThirdPartyIncludeNonDevelopmentApps"
+ "TB,R,V_thirdPartyIncludeNonDevelopmentApps"
+ "Warning: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
+ "_thirdPartyIncludeNonDevelopmentApps"
+ "cbdrRefreshGradesSLC"
+ "cbdrRefreshGradesSLC_"
+ "cbdrScanPctSLC"
+ "cbdrScanPctSLC_"
+ "hostWritesPerThrottleZone"
+ "hostWritesPerThrottleZone_"
+ "prefetchNextRange"
+ "setDisplayTrialInformation:"
+ "thirdPartyIncludeNonDevelopmentApps"
+ "unexpectedBlanksInternal"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: unexpectedBlanks(596) cannot add 1 element to context"
- "Error: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
- "unexpectedBlanks"

```
