## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

-592.0.4.0.0
-  __TEXT.__text: 0x19ff8
+592.40.2.0.0
+  __TEXT.__text: 0x1a164
   __TEXT.__auth_stubs: 0x240
-  __TEXT.__cstring: 0x281bb
+  __TEXT.__cstring: 0x284c2
   __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0x191
-  __TEXT.__info_plist: 0x49c
+  __TEXT.__info_plist: 0x4a8
   __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__auth_got: 0x120
   __DATA_CONST.__got: 0x38

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
-  Functions: 87
+  Functions: 85
   Symbols:   47
-  CStrings:  2844
+  CStrings:  2858
 
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
+ "Warning: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
+ "cbdrRefreshGradesSLC"
+ "cbdrRefreshGradesSLC_"
+ "cbdrScanPctSLC"
+ "cbdrScanPctSLC_"
+ "hostWritesPerThrottleZone"
+ "hostWritesPerThrottleZone_"
+ "prefetchNextRange"
+ "unexpectedBlanksInternal"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: unexpectedBlanks(596) cannot add 1 element to context"
- "Error: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
- "unexpectedBlanks"

```
