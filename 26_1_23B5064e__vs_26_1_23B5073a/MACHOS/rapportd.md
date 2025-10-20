## rapportd

> `/usr/libexec/rapportd`

```diff

-716.200.62.0.0
-  __TEXT.__text: 0x128968
-  __TEXT.__auth_stubs: 0x3530
-  __TEXT.__objc_stubs: 0x10600
-  __TEXT.__objc_methlist: 0x8584
-  __TEXT.__const: 0x4f78
-  __TEXT.__cstring: 0x2dfc1
-  __TEXT.__objc_classname: 0xa81
-  __TEXT.__objc_methtype: 0x3caa
+716.201.11.0.0
+  __TEXT.__text: 0x128f90
+  __TEXT.__auth_stubs: 0x3510
+  __TEXT.__objc_stubs: 0x10680
+  __TEXT.__objc_methlist: 0x85ac
+  __TEXT.__const: 0x53e0
+  __TEXT.__cstring: 0x2e151
+  __TEXT.__objc_classname: 0xa71
+  __TEXT.__objc_methtype: 0x3d01
   __TEXT.__gcc_except_tab: 0x208c
-  __TEXT.__objc_methname: 0x178ba
-  __TEXT.__oslogstring: 0x1c12
-  __TEXT.__swift5_typeref: 0x1114
-  __TEXT.__swift5_capture: 0x8bc
-  __TEXT.__swift5_reflstr: 0xc34
+  __TEXT.__objc_methname: 0x17968
+  __TEXT.__oslogstring: 0x1b92
+  __TEXT.__swift5_typeref: 0x113c
+  __TEXT.__swift5_capture: 0x890
+  __TEXT.__swift5_reflstr: 0xc64
   __TEXT.__swift5_assocty: 0x130
-  __TEXT.__constg_swiftt: 0xb48
+  __TEXT.__constg_swiftt: 0xb60
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_fieldmd: 0xd80
+  __TEXT.__swift5_fieldmd: 0xd98
   __TEXT.__swift5_proto: 0x1dc
   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift_as_entry: 0x178

   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_acfuncs: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4490
+  __TEXT.__unwind_info: 0x4480
   __TEXT.__eh_frame: 0x2ee4
-  __DATA_CONST.__auth_got: 0x1aa8
+  __DATA_CONST.__auth_got: 0x1a98
   __DATA_CONST.__got: 0x900
-  __DATA_CONST.__auth_ptr: 0x588
-  __DATA_CONST.__const: 0x6f30
+  __DATA_CONST.__auth_ptr: 0x580
+  __DATA_CONST.__const: 0x6ed8
   __DATA_CONST.__cfstring: 0x5e80
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x160
+  __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0xc0
+  __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_intobj: 0x360
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0xeb48
-  __DATA.__objc_selrefs: 0x50f0
-  __DATA.__objc_ivar: 0xe6c
-  __DATA.__objc_data: 0x23d0
-  __DATA.__data: 0x3168
-  __DATA.__bss: 0x4690
+  __DATA.__objc_const: 0xeba8
+  __DATA.__objc_selrefs: 0x5100
+  __DATA.__objc_ivar: 0xe70
+  __DATA.__objc_data: 0x23d8
+  __DATA.__data: 0x30f8
+  __DATA.__bss: 0x4680
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 41DFA22B-ED88-3704-873F-944A89ECECCA
+  UUID: 7AB3C45F-C8A9-3745-9AB3-7D1AF1ABD105
   Functions: 6662
-  Symbols:   1316
-  CStrings:  10108
+  Symbols:   1313
+  CStrings:  10120
 
Symbols:
- _$s7Network12NWParametersCMn
- _$sSS10FoundationE4data8encodingSSSgAA4DataVh_SSAAE8EncodingVtcfC
- _sec_protocol_options_set_pake_challenge_block
CStrings:
+ "%@ LISTEN: Creating pairing server, advertise sensitive info: %s"
+ "%@ LISTEN: Pairing session stopped due to state update."
+ "%@ LISTEN: Stopping existing pairing session to restart with updated state: %s"
+ "%@ Stopped listener pairing session after removal of PairingConfiguration"
+ "-[RPNWAgentClient updateListenerPairingStateIfNeeded:]_block_invoke"
+ "-[RPNWNetworkAgent(Pairing) createPairingListener:endpoint:pin:]_block_invoke"
+ "-[RPNWNetworkAgent(Pairing) createPairingListener:endpoint:pin:]_block_invoke_4"
+ "RPPairingPairVerifyStream"
+ "TI,N,V_listenerPairingState"
+ "_listenerPairingState"
+ "activateForServerWithPin:advertiseSensitiveInfo:completionHandler:"
+ "agentClientListenerAdvertiseSensitiveInfo:"
+ "encryptionStream"
+ "encryptionStreams"
+ "listenerPairingState"
+ "onAdvertiseSensitiveInfo"
+ "onHideSensitiveInfo"
+ "rppairing-bonjour-resolve"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "setListenerPairingState:"
+ "updateListenerPairingStateIfNeeded:"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "%@ LISTEN: Creating pairing server, hide sensitive info: %s"
- "-[RPNWNetworkAgent(Pairing) createPairingListener:endpoint:pin:]_block_invoke_3"
- "Looking for PAKE credential: client=%s, server=%s"
- "Missing client or server identity in offered PAKE"
- "OS_sec_identity"
- "activateForServerWithPin:hideSensitiveInfo:completionHandler:"
- "agentClientListenerHideSensitiveInfo:"
- "client_identity"
- "server_identity"
- "v32@?0@\"<OS_sec_protocol_metadata>\"8@\"SecOfferedPAKEIdentity\"16@?<v@?@\"<OS_sec_identity>\">24"

```
