## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

```diff

-775.3.1.1.1
-  __TEXT.__text: 0x136580
-  __TEXT.__stubs: 0x27f0
+775.3.1.101.3
+  __TEXT.__text: 0x136700
+  __TEXT.__stubs: 0x27d8
   __TEXT.__objc_methlist: 0x910
   __TEXT.__const: 0x3275c
   __TEXT.__gcc_except_tab: 0x300
-  __TEXT.__cstring: 0x2b7ca
-  __TEXT.__unwind_info: 0x12cc
+  __TEXT.__cstring: 0x2b7ed
+  __TEXT.__unwind_info: 0x12d0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x144
   __TEXT.__objc_methname: 0x2649
   __TEXT.__objc_methtype: 0x142a
   __TEXT.__objc_stubs: 0x2780
-  __DATA_CONST.__got: 0x21e0
+  __DATA_CONST.__got: 0x21d0
   __DATA_CONST.__const: 0xbf40
   __DATA_CONST.__cfstring: 0xa2c0
   __DATA_CONST.__objc_classlist: 0x58

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1510
-  Symbols:   2678
-  CStrings:  5137
+  Functions: 1509
+  Symbols:   2675
+  CStrings:  5131
 
Symbols:
+ _APSIsRestrictiveHKAccessControl
- _DataBuffer_AppendFile
- _DataBuffer_Commit
- _DataBuffer_RunProcessAndAppendOutput
CStrings:
+ "### [%{ptr}] Failed to tear down session [%{ptr}]\n"
+ "### [%{ptr}] Failed to tear down session [%{ptr}] for SDP audio\n"
+ "OSStatus _GetDecryptKey(AirPlayReceiverSessionRef, CFDictionaryRef, FPSAPContextRef *, int, AirPlayEncryptionType, uint8_t *, uint8_t *)"
+ "[%{ptr}] Control pair-verify CU, type %u, is not allowed based on access control\n"
- "+-+ syslog +--\n"
- "/log"
- "/logs"
- "/var/mobile/Library/Logs/AirPlay.log"
- "===================\n"
- "AirPlay Diagnostics\n"
- "OSStatus _GetDecryptKey(AirPlayReceiverSessionRef, CFDictionaryRef, FPSAPContextRef, int, AirPlayEncryptionType, uint8_t *, uint8_t *)"
- "airplayReqProcessor_requestProcessGetLog"
- "syslog"
- "text/plain"

```
