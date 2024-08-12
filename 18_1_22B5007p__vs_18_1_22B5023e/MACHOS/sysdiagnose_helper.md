## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1431.0.0.0.0
-  __TEXT.__text: 0x34344
-  __TEXT.__auth_stubs: 0xb30
+1438.0.0.0.0
+  __TEXT.__text: 0x34608
+  __TEXT.__auth_stubs: 0xb60
   __TEXT.__objc_stubs: 0x13a0
   __TEXT.__objc_methlist: 0x508
   __TEXT.__const: 0x3b8
   __TEXT.__gcc_except_tab: 0x7c0
-  __TEXT.__oslogstring: 0x1f17
-  __TEXT.__cstring: 0x2b3f8
+  __TEXT.__oslogstring: 0x1fa0
+  __TEXT.__cstring: 0x2b6d8
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
   __TEXT.__objc_methname: 0x13eb
   __TEXT.__unwind_info: 0x4e8
-  __DATA_CONST.__auth_got: 0x5a8
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x640
   __DATA_CONST.__cfstring: 0x1a40

   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
   Functions: 307
-  Symbols:   240
-  CStrings:  3751
+  Symbols:   243
+  CStrings:  3765
 
Symbols:
+ __os_log_fault_impl
+ _getgid
+ _getuid
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
+ "Assuming root identity when the process already runs as root."
+ "Attempting to restore an identity without having first assumed an identity"
+ "Warning: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
+ "cbdrRefreshGradesSLC_"
+ "cbdrScanPctSLC_"
+ "gcUpdateResumeAttempt"
+ "gcUpdateResumeFailure"
+ "gcUpdateResumeSuccess"
+ "hostWritesPerThrottleZone_"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: unexpectedBlanks(596) cannot add 1 element to context"
- "Error: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
- "unexpectedBlanks"

```
