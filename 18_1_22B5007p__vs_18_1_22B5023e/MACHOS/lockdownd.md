## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1319.0.4.0.0
-  __TEXT.__text: 0x10385c
+1319.0.7.0.0
+  __TEXT.__text: 0x10275c
   __TEXT.__auth_stubs: 0x2cd0
   __TEXT.__objc_stubs: 0x43e0
   __TEXT.__objc_methlist: 0x3438
-  __TEXT.__cstring: 0x4cf53
-  __TEXT.__const: 0x16300
+  __TEXT.__cstring: 0x4d277
+  __TEXT.__const: 0x160f0
   __TEXT.__oslogstring: 0x788
   __TEXT.__gcc_except_tab: 0x399c
   __TEXT.__objc_classname: 0xbb3

   __TEXT.__objc_methtype: 0xe80
   __TEXT.__services: 0x2d8f
   __TEXT.__unwind_info: 0x2d28
-  __TEXT.__eh_frame: 0x1188
+  __TEXT.__eh_frame: 0x10b8
   __DATA_CONST.__auth_got: 0x1680
-  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__got: 0x698
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0xac90
+  __DATA_CONST.__const: 0xa948
   __DATA_CONST.__cfstring: 0x17c20
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x270
-  __DATA_CONST.__objc_intobj: 0xd8
+  __DATA_CONST.__objc_intobj: 0xf0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA.__objc_const: 0x6290
   __DATA.__objc_selrefs: 0x1480
   __DATA.__objc_ivar: 0x410
   __DATA.__objc_data: 0x1900
-  __DATA.__data: 0x2b28
+  __DATA.__data: 0x2b68
   __DATA.__bss: 0x1042
   __DATA.__common: 0x1a48
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2914
-  Symbols:   923
-  CStrings:  9443
+  Functions: 2935
+  Symbols:   925
+  CStrings:  9457
 
Symbols:
+ _SBUserNotificationAlternateButtonPresentationStyleKey
+ _SBUserNotificationDefaultButtonPresentationStyleKey
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
+ "HelsinkiRestore-56.0.32"
+ "VinylRestore-78~964"
+ "Warning: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
+ "cbdrRefreshGradesSLC"
+ "cbdrRefreshGradesSLC_"
+ "cbdrScanPctSLC"
+ "cbdrScanPctSLC_"
+ "hostWritesPerThrottleZone"
+ "hostWritesPerThrottleZone_"
+ "libauthinstall_device-1033.40.1"
+ "prefetchNextRange"
+ "ramrod_disable_usbcretimer set in boot-args, disabling hardware support and not waiting for retimers\n"
+ "unexpectedBlanksInternal"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMaxTempHisto(327): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): (#22) cfg elements != (%!d(MISSING)) buffer elements"
- "ASPFTLParseBufferToCxt: bandsMinTempHisto(328): Cannot add 22 elements to context"
- "ASPFTLParseBufferToCxt: unexpectedBlanks(596) cannot add 1 element to context"
- "Error: NANDInfo: NANDExporter: serializeAccess already locked. waiting for lock !\n"
- "HelsinkiRestore-56.0.28"
- "VinylRestore-78~110"
- "libauthinstall_device-1033.0.4"
- "ramrod_disable_usbcretimer set in boot-args, disabling hardware support.\n"
- "unexpectedBlanks"

```
