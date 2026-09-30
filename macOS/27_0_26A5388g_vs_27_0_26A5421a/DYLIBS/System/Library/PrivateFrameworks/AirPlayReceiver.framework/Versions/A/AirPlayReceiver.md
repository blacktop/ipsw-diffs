## AirPlayReceiver

> `/System/Library/PrivateFrameworks/AirPlayReceiver.framework/Versions/A/AirPlayReceiver`

```diff

-980.71.1.0.0
-  __TEXT.__text: 0xf81e8
+980.77.5.3.0
+  __TEXT.__text: 0xf831c
   __TEXT.__objc_methlist: 0xca4
-  __TEXT.__const: 0xd4c1
+  __TEXT.__const: 0xd4f3
   __TEXT.__dlopen_cstrs: 0x103
-  __TEXT.__gcc_except_tab: 0x854
-  __TEXT.__cstring: 0x2ed77
+  __TEXT.__gcc_except_tab: 0x850
+  __TEXT.__cstring: 0x2ee48
   __TEXT.__oslogstring: 0x2eb
-  __TEXT.__unwind_info: 0x1340
+  __TEXT.__unwind_info: 0x1348
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c00
+  __DATA_CONST.__const: 0x1c30
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x878
   __AUTH_CONST.__const: 0x3d60
-  __AUTH_CONST.__cfstring: 0xb1e0
+  __AUTH_CONST.__cfstring: 0xb200
   __AUTH_CONST.__objc_const: 0x18f8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1469
-  Symbols:   3759
-  CStrings:  4785
+  Functions: 1471
+  Symbols:   3763
+  CStrings:  4789
 
Symbols:
+ -[APAdvertiserBTLEManager dispatchSourceState:changed:]
+ APReceiverUIControllerHidePIN
+ GCC_except_table1040
+ GCC_except_table1059
+ GCC_except_table1110
+ GCC_except_table1114
+ GCC_except_table1166
+ GCC_except_table1174
+ GCC_except_table1176
+ GCC_except_table1220
+ GCC_except_table1282
+ GCC_except_table206
+ GCC_except_table213
+ GCC_except_table389
+ GCC_except_table445
+ GCC_except_table469
+ GCC_except_table521
+ GCC_except_table525
+ GCC_except_table532
+ GCC_except_table540
+ GCC_except_table720
+ GCC_except_table732
+ GCC_except_table735
+ GCC_except_table738
+ GCC_except_table746
+ GCC_except_table761
+ GCC_except_table932
+ _GestaltGetDeviceClass
+ __IgnoreTerminationForSession
+ __IsRequestPairSetupRelated
+ ___55-[APAdvertiserBTLEManager dispatchSourceState:changed:]_block_invoke
+ ___audioSessionBufferedHose_handleAudioDataConnectionEvent_block_invoke
+ _kAPReceiverRequestProcessorAirPlayProperty_IsPersistentSession
+ _objc_msgSend$dispatchSourceState:changed:
- -[APAdvertiserBTLEManager dispatchEvent:]
- GCC_except_table1037
- GCC_except_table1056
- GCC_except_table1107
- GCC_except_table1111
- GCC_except_table1163
- GCC_except_table1171
- GCC_except_table1173
- GCC_except_table1217
- GCC_except_table1279
- GCC_except_table208
- GCC_except_table214
- GCC_except_table390
- GCC_except_table446
- GCC_except_table470
- GCC_except_table522
- GCC_except_table526
- GCC_except_table533
- GCC_except_table541
- GCC_except_table718
- GCC_except_table730
- GCC_except_table733
- GCC_except_table736
- GCC_except_table744
- GCC_except_table757
- GCC_except_table930
- __APAdvertiserHandleSourceDeviceNearbyEvent
- ___41-[APAdvertiserBTLEManager dispatchEvent:]_block_invoke
- _memchr
- _objc_msgSend$dispatchEvent:
CStrings:
+ "\n %-*s: soloSourceNearby=%s, nanSourceNearby=%s, enforceSoloAdvertising=%s"
+ "### Request denied, sender not admissible (User-Agent '%.*s'): %.*s %.*s\n"
+ "%@ audio data connection %s. Terminating Receiver session: %#m"
+ "%s device nearby %{flags}"
+ "-[APAdvertiserBTLEManager dispatchSourceState:changed:]"
+ "980.77.5.3"
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
- "\n %-*s: soloSourceNearby=%s, enforceSoloAdvertising=%s"
- "### Rejecting PIN mode for old audio client\n"
- "### Reporting incompatible sender: '%.*s'\n"
- "### [%{ptr}] Reporting incompatible sender: '%.*s'\n"
- "%s device nearby\n"
- "980.71.1"
- "Invalid during BTLE event %d."
- "OSStatus _APAdvertiserHandleSourceDeviceNearbyEvent(APAdvertiserRef, Boolean)"
- "Unrecognized BTLE event %d."
- "void _APAdvertiserBTLEEventHandler(APAdvertiserBTLEManagerRef, APAdvertiserBTLEEventType, CFTypeRef _Nullable)_block_invoke"
- "void _requestReportIfIncompatibleSender(AirPlayReceiverConnectionRef, HTTPMessageRef)"
- "void airplayReqProcessor_requestReportIfIncompatibleSender(APReceiverRequestProcessorRef, CFDictionaryRef)"
```
