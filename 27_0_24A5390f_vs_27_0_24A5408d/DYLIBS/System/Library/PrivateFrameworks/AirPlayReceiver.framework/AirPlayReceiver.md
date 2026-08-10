## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/AirPlayReceiver`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0x17bd68
+980.75.1.0.0
+  __TEXT.__text: 0x17bef0
   __TEXT.__objc_methlist: 0xaec
-  __TEXT.__const: 0x275a9
+  __TEXT.__const: 0x275db
   __TEXT.__dlopen_cstrs: 0xad
-  __TEXT.__gcc_except_tab: 0x838
-  __TEXT.__cstring: 0x3304b
+  __TEXT.__gcc_except_tab: 0x834
+  __TEXT.__cstring: 0x33173
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x1688
+  __TEXT.__unwind_info: 0x1690
   __TEXT.__eh_frame: 0x128
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2020
+  __DATA_CONST.__const: 0x2048
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x988
   __AUTH_CONST.__const: 0x9400
-  __AUTH_CONST.__cfstring: 0xba40
+  __AUTH_CONST.__cfstring: 0xba60
   __AUTH_CONST.__objc_const: 0x1550
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1701
-  Symbols:   3910
-  CStrings:  5189
+  Functions: 1703
+  Symbols:   3913
+  CStrings:  5194
 
Symbols:
+ -[APAdvertiserBTLEManager dispatchSourceState:changed:]
+ GCC_except_table1001
+ GCC_except_table1114
+ GCC_except_table1133
+ GCC_except_table1184
+ GCC_except_table1188
+ GCC_except_table1241
+ GCC_except_table1249
+ GCC_except_table1251
+ GCC_except_table1296
+ GCC_except_table1359
+ GCC_except_table207
+ GCC_except_table214
+ GCC_except_table220
+ GCC_except_table409
+ GCC_except_table472
+ GCC_except_table521
+ GCC_except_table579
+ GCC_except_table583
+ GCC_except_table590
+ GCC_except_table598
+ GCC_except_table735
+ _GestaltGetDeviceClass
+ __IgnoreTerminationForSession
+ __IsRequestPairSetupRelated
+ ___55-[APAdvertiserBTLEManager dispatchSourceState:changed:]_block_invoke
+ ___audioSessionBufferedHose_handleAudioDataConnectionEvent_block_invoke
+ _kAPReceiverRequestProcessorAirPlayProperty_IsPersistentSession
+ _objc_msgSend$dispatchSourceState:changed:
- -[APAdvertiserBTLEManager dispatchEvent:]
- GCC_except_table1111
- GCC_except_table1130
- GCC_except_table1181
- GCC_except_table1185
- GCC_except_table1238
- GCC_except_table1246
- GCC_except_table1248
- GCC_except_table1293
- GCC_except_table1356
- GCC_except_table209
- GCC_except_table215
- GCC_except_table221
- GCC_except_table410
- GCC_except_table473
- GCC_except_table522
- GCC_except_table580
- GCC_except_table584
- GCC_except_table591
- GCC_except_table599
- GCC_except_table733
- GCC_except_table999
- __APAdvertiserHandleSourceDeviceNearbyEvent
- ___41-[APAdvertiserBTLEManager dispatchEvent:]_block_invoke
- _memchr
- _objc_msgSend$dispatchEvent:
CStrings:
+ "\n %-*s: soloSourceNearby=%s, nanSourceNearby=%s, enforceSoloAdvertising=%s"
+ "### Request denied, sender not admissible (User-Agent '%.*s'): %.*s %.*s\n"
+ "### Terminating AirPlay session(s) on simulated UserStop\n"
+ "%@ audio data connection %s. Terminating Receiver session: %#m"
+ "%s device nearby %{flags}"
+ "-[APAdvertiserBTLEManager dispatchSourceState:changed:]"
+ "980.75.1"
+ "<APConn> Ignoring UserStop for persistent session [%{ptr}] to keep cluster topology intact.\n"
+ "AirPlay/"
+ "Boolean _IgnoreTerminationForSession(APReceiverRequestProcessorRef, AirPlayReceiverSessionTerminationReason)"
+ "Disconnected"
+ "Invalid during BTLE source state update %{flags}."
+ "OSStatus _APAdvertiserHandleSourceDeviceNearbyEvent(APAdvertiserRef, APAdvertiserBTLESourceState)"
+ "Source state: %#{flags}"
+ "iTunes/"
+ "isPersistentSession"
+ "void _APAdvertiserBTLEEventHandler(APAdvertiserBTLEManagerRef, APAdvertiserBTLESourceState, APAdvertiserBTLESourceState, CFTypeRef _Nullable)_block_invoke"
+ "void _HandleSimulateUserStop(AirPlayReceiverServerRef)"
- "\n %-*s: soloSourceNearby=%s, enforceSoloAdvertising=%s"
- "### Rejecting PIN mode for old audio client\n"
- "### Reporting incompatible sender: '%.*s'\n"
- "### [%{ptr}] Reporting incompatible sender: '%.*s'\n"
- "%s device nearby\n"
- "980.71.1"
- "Invalid during BTLE event %d."
- "OSStatus _APAdvertiserHandleSourceDeviceNearbyEvent(APAdvertiserRef, Boolean)"
- "Unrecognized BTLE event %d."
- "_HandleSimulateUserStop"
- "void _APAdvertiserBTLEEventHandler(APAdvertiserBTLEManagerRef, APAdvertiserBTLEEventType, CFTypeRef _Nullable)_block_invoke"
- "void _requestReportIfIncompatibleSender(AirPlayReceiverConnectionRef, HTTPMessageRef)"
- "void airplayReqProcessor_requestReportIfIncompatibleSender(APReceiverRequestProcessorRef, CFDictionaryRef)"
```
