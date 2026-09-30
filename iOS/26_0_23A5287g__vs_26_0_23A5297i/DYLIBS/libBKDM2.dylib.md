## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

```diff

-870.0.0.0.0
-  __TEXT.__text: 0x7d434
+872.0.0.0.0
+  __TEXT.__text: 0x7d774
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x5aac
+  __TEXT.__objc_methlist: 0x5ab4
   __TEXT.__const: 0x8d2f
-  __TEXT.__cstring: 0x65d5
-  __TEXT.__oslogstring: 0x4016
-  __TEXT.__gcc_except_tab: 0x15fc
+  __TEXT.__cstring: 0x65fe
+  __TEXT.__oslogstring: 0x3fb6
+  __TEXT.__gcc_except_tab: 0x1620
   __TEXT.__ustring: 0x11c
   __TEXT.__unwind_info: 0xd38
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x375
-  __TEXT.__objc_methname: 0x14489
+  __TEXT.__objc_methname: 0x144da
   __TEXT.__objc_methtype: 0x2920
-  __TEXT.__objc_stubs: 0x7ae0
+  __TEXT.__objc_stubs: 0x7b60
   __DATA_CONST.__got: 0x460
   __DATA_CONST.__const: 0x13a8
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b98
+  __DATA_CONST.__objc_selrefs: 0x3bb0
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x318
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x9a8
-  __AUTH_CONST.__cfstring: 0x5e00
+  __AUTH_CONST.__cfstring: 0x5e40
   __AUTH_CONST.__objc_const: 0x9068
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0xa0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: AB490488-217F-3E50-B2C6-1C8D060B7B37
-  Functions: 2735
-  Symbols:   8267
-  CStrings:  5339
+  UUID: E0998F83-4BA1-3D1A-A512-34EF2C13E4E5
+  Functions: 2736
+  Symbols:   8273
+  CStrings:  5345
 
Symbols:
+ -[PearlCoreAnalytics secureFaceDetectSupported]
+ -[PearlCoreAnalytics setSecureFaceDetectSupported:]
+ -[PearlCoreAnalyticsEvent getPrintableArray]
+ -[PearlCoreAnalyticsEvent prepareEventDictionary:]
+ -[PearlCoreAnalyticsFaceDetectEvent prepareEventDictionary:]
+ -[PearlCoreAnalyticsMatchEvent prepareEventDictionary:]
+ -[PearlCoreAnalyticsMatchEvent prepareEventDictionary:].cold.1
+ _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectSupported
+ _OBJC_IVAR_$_PearlCoreAnalytics._secureFaceDetectSupported
+ ___50-[PearlCoreAnalyticsEvent prepareEventDictionary:]_block_invoke
+ _objc_msgSend$appendString:
+ _objc_msgSend$getEventDictionary
+ _objc_msgSend$getParagraphStart:end:contentsEnd:forRange:
+ _objc_msgSend$getPrintableArray
+ _objc_msgSend$prepareEventDictionary:
+ _objc_msgSend$setSecureFaceDetectSupported:
- -[PearlCoreAnalytics secureFaceDetectSuported]
- -[PearlCoreAnalytics setSecureFaceDetectSuported:]
- -[PearlCoreAnalyticsEvent prepareEventDictionary]
- -[PearlCoreAnalyticsFaceDetectEvent prepareEventDictionary]
- -[PearlCoreAnalyticsMatchEvent prepareEventDictionary]
- -[PearlCoreAnalyticsMatchEvent prepareEventDictionary].cold.1
- _OBJC_IVAR_$_BiometricKitXPCServerPearl._secureFaceDetectSuported
- _OBJC_IVAR_$_PearlCoreAnalytics._secureFaceDetectSuported
- ___49-[PearlCoreAnalyticsEvent prepareEventDictionary]_block_invoke
- _objc_msgSend$prepareEventDictionary
- _objc_msgSend$setSecureFaceDetectSuported:
Functions:
- -[PearlCoreAnalyticsFaceDetectEvent prepareEventDictionary]
~ -[PearlCoreAnalytics sendMatchEventAnalytics:orientation:identities:] : 6316 -> 6568
+ -[PearlCoreAnalyticsFaceDetectEvent prepareEventDictionary:]
~ -[PearlCoreAnalyticsEvent postEventExtendedBy:] : 536 -> 540
+ -[PearlCoreAnalyticsEvent getPrintableArray]
CStrings:
+ "\n"
+ "%@\n"
+ "PearlCAEvent: %@ (print %ld of %ld):\n"
+ "PearlCoreAnalytics sendMatchEventAnalytics: _secureFaceDetect, _previousSecureFaceDetect matchCAEvent:\n"
+ "TB,V_secureFaceDetectSupported"
+ "_secureFaceDetectSupported"
+ "appendString:"
+ "getParagraphStart:end:contentsEnd:forRange:"
+ "getPrintableArray"
+ "prepareEventDictionary:"
+ "secureFaceDetectSupported"
+ "setSecureFaceDetectSupported:"
- "PearlCoreAnalytics sendMatchEventAnalytics: _previousSecureFaceDetect: %@\n"
- "PearlCoreAnalytics sendMatchEventAnalytics: _secureFaceDetect: %@\n"
- "PearlCoreAnalytics sendMatchEventAnalytics: matchCAEvent: %@\n"
- "TB,V_secureFaceDetectSuported"
- "_secureFaceDetectSuported"
- "prepareEventDictionary"
- "secureFaceDetectSuported"
- "setSecureFaceDetectSuported:"

```
