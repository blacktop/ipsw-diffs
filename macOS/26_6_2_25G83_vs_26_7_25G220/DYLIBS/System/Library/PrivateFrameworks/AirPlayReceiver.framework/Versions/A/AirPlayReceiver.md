## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver`

```diff

-960.13.1.0.0
-  __TEXT.__text: 0xe134c
+960.13.25.1.0
+  __TEXT.__text: 0xe15c4
   __TEXT.__auth_stubs: 0x35e0
   __TEXT.__objc_methlist: 0x924
   __TEXT.__const: 0xd155
   __TEXT.__dlopen_cstrs: 0xad
   __TEXT.__gcc_except_tab: 0x720
-  __TEXT.__cstring: 0x2a679
+  __TEXT.__cstring: 0x2a5d8
   __TEXT.__unwind_info: 0x1158
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methname: 0x1f66

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1335
-  Symbols:   3354
-  CStrings:  4889
+  Functions: 1336
+  Symbols:   3356
+  CStrings:  4891
 
Symbols:
+ APReceiverUIControllerHidePIN
+ GCC_except_table1048
+ GCC_except_table1058
+ GCC_except_table922
+ GCC_except_table941
+ GCC_except_table992
+ GCC_except_table996
+ _APSIsHomeAccessory
+ __IsRequestPairSetupRelated
- GCC_except_table1046
- GCC_except_table1054
- GCC_except_table920
- GCC_except_table939
- GCC_except_table990
- GCC_except_table994
- _memchr
CStrings:
+ "### Request denied, sender not admissible (User-Agent '%.*s'): %.*s %.*s\n"
+ "960.13.25.1"
+ "AAC_ELD/48000/7.1.4"
+ "AAC_ELD/48000/9.1.6"
+ "AAC_LC/48000/7.1.4"
+ "AAC_LC/48000/9.1.6"
+ "AirPlay/"
+ "iTunes/"
- "### Rejecting PIN mode for old audio client\n"
- "### Reporting incompatible sender: '%.*s'\n"
- "### [%{ptr}] Reporting incompatible sender: '%.*s'\n"
- "960.13.1"
- "void _requestReportIfIncompatibleSender(AirPlayReceiverConnectionRef, HTTPMessageRef)"
- "void airplayReqProcessor_requestReportIfIncompatibleSender(APReceiverRequestProcessorRef, CFDictionaryRef)"
```
