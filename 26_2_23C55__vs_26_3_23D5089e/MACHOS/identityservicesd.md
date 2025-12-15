## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1968.300.31.0.0
-  __TEXT.__text: 0x93fb3c
+1968.400.1.0.0
+  __TEXT.__text: 0x940c94
   __TEXT.__auth_stubs: 0x5ba0
-  __TEXT.__objc_stubs: 0x46c20
-  __TEXT.__objc_methlist: 0x298cc
+  __TEXT.__objc_stubs: 0x46cc0
+  __TEXT.__objc_methlist: 0x2992c
   __TEXT.__const: 0x64ef0
-  __TEXT.__gcc_except_tab: 0x29ddc
-  __TEXT.__objc_methname: 0x737f0
-  __TEXT.__cstring: 0x59ac7
-  __TEXT.__oslogstring: 0x7b2db
+  __TEXT.__gcc_except_tab: 0x29f10
+  __TEXT.__objc_methname: 0x7395d
+  __TEXT.__cstring: 0x59c47
+  __TEXT.__oslogstring: 0x7b45b
   __TEXT.__objc_classname: 0x440c
-  __TEXT.__objc_methtype: 0x124cd
+  __TEXT.__objc_methtype: 0x1255b
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
   __TEXT.__swift5_typeref: 0x60b2

   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_assocty: 0xfc0
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x12330
+  __TEXT.__unwind_info: 0x12358
   __TEXT.__eh_frame: 0x9ae4
   __DATA_CONST.__auth_got: 0x2de0
-  __DATA_CONST.__got: 0x38b8
+  __DATA_CONST.__got: 0x38d8
   __DATA_CONST.__auth_ptr: 0x7a8
-  __DATA_CONST.__const: 0x2e068
-  __DATA_CONST.__cfstring: 0x34900
+  __DATA_CONST.__const: 0x2e0b8
+  __DATA_CONST.__cfstring: 0x349e0
   __DATA_CONST.__objc_classlist: 0x1130
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x760

   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x483a0
-  __DATA.__objc_selrefs: 0x15f48
-  __DATA.__objc_ivar: 0x32b0
+  __DATA.__objc_const: 0x48438
+  __DATA.__objc_selrefs: 0x15f80
+  __DATA.__objc_ivar: 0x32bc
   __DATA.__objc_data: 0xd788
   __DATA.__data: 0xec30
   __DATA.__bss: 0x17158

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 28047F2F-8F31-3841-AACD-182307C420B8
-  Functions: 25439
-  Symbols:   2753
-  CStrings:  41611
+  UUID: F752739E-E2DB-3786-A702-BF15EF250742
+  Functions: 25448
+  Symbols:   2757
+  CStrings:  41649
 
Symbols:
+ _IDSDSessionMessageLocalHandshakeCellularOnly
+ _IDSDSessionMessageLocalHandshakeMessage
+ _IDSSessionDisallowHandshakeOverQRKey
+ _IDSSessionLocalNetworkHandshakeKey
CStrings:
+ "20:36:46"
+ "@\"NSString\"84@?0@\"NSString\"8I16@\"NSString\"20q28S36Q40S48@\"NSData\"52@\"NSData\"60B68B72i76i80"
+ "@80@0:8@16@24@32B40@44^{?=SSQC*I*}52@60@?68i76"
+ "@92@0:8@16I24@28q36S44Q48S56@60@68B76B80i84i88"
+ "B64@0:8@16@24Q32S40S44@48@56"
+ "Dec  8 2025"
+ "Done with incoming network availability check; networkOkForSession: %@, cellularOnly: %@"
+ "Done with outgoing network availability check; networkOkForSession: %@ cellularOnly: %@"
+ "Handshake invitation was dropped as the originator only has viable cellular connection and no local WiFi"
+ "Handshake invitation was sent over cellular: %@"
+ "Handshake session: %@."
+ "IMNetworkAvailabilityFlags resultFlags: %lu"
+ "Is handshake invitation: %@"
+ "Loaded %d sms signatures mechanisms"
+ "Sending handshake push with nil connection data over cellular %@"
+ "TB,N,V_disallowHandshakeOverQR"
+ "TB,N,V_isCellularOnly"
+ "TB,N,V_isHandshakeSession"
+ "_disallowHandshakeOverQR"
+ "_isCellularOnly"
+ "_isHandshakeSession"
+ "addConnectStatus, groupID: %@, relaySessionID: %@i, data: %u %u %@ %@"
+ "cached response previous connect status, reason/error/token/ip: %u %u %@ %@"
+ "com.apple.private.alloy.phonecontinuity.ping"
+ "didReceiveLocalNetworkHandshake:handshakeSucceeded:forTopic:sessionID:toIdentifier:fromID:error:"
+ "disallowHandshakeOverQR"
+ "isCellularOnly"
+ "isHandshakeSession"
+ "setDisallowHandshakeOverQR:"
+ "setIsCellularOnly:"
+ "setIsHandshakeSession:"
+ "v16@?0B8B12"
+ "v24@0:8@?<v@?BB>16"
+ "v32@0:8@\"IDSDSession\"16@?<v@?BB>24"
+ "v68@0:8@\"NSDictionary\"16B24@\"NSString\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSError\"60"
+ "v68@0:8@16B24@28@36@44@52@60"
- "21:15:43"
- "@\"NSString\"80@?0@\"NSString\"8I16@\"NSString\"20q28S36Q40S48I52@\"NSData\"56B64B68i72i76"
- "@80@0:8@16@24@32B40@44^{?=SSIQI*}52@60@?68i76"
- "@88@0:8@16I24@28q36S44Q48S56I60@64B72B76i80i84"
- "B60@0:8@16@24Q32S40S44I48@52"
- "Done with incoming network availability check; networkOkForSession: %@"
- "Done with outgoing network availability check; networkOkForSession: %@"
- "Nov 12 2025"
- "addConnectStatus, groupID: %@, relaySessionID: %@i, data: %u %u %u %@"
- "cached response previous connect status, reason/error/token/ip: %u %u %u %@"
- "v32@0:8@\"IDSDSession\"16@?<v@?B>24"

```
