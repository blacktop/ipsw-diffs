## securepairingd

> `/usr/libexec/securepairingd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_protos`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0x4969c
-  __TEXT.__auth_stubs: 0x1770
+67.3.0.0.0
+  __TEXT.__text: 0x78fdc
+  __TEXT.__auth_stubs: 0x1800
   __TEXT.__objc_stubs: 0xc0
-  __TEXT.__const: 0x7e68
-  __TEXT.__constg_swiftt: 0x1fec
-  __TEXT.__swift5_typeref: 0x17f9
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_types: 0x280
-  __TEXT.__objc_classname: 0x6b7
-  __TEXT.__objc_methname: 0x1ef
-  __TEXT.__swift5_reflstr: 0x864
-  __TEXT.__swift5_fieldmd: 0x17fc
-  __TEXT.__swift5_capture: 0x4a4
-  __TEXT.__oslogstring: 0x129d
-  __TEXT.__cstring: 0x1060
-  __TEXT.__swift5_assocty: 0x2d8
-  __TEXT.__swift5_proto: 0x7d0
-  __TEXT.__swift_as_entry: 0x4c
-  __TEXT.__swift_as_ret: 0x28
-  __TEXT.__swift_as_cont: 0x94
+  __TEXT.__objc_methlist: 0x104
+  __TEXT.__const: 0xe158
+  __TEXT.__constg_swiftt: 0x2bdc
+  __TEXT.__swift5_typeref: 0x26e9
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__swift5_types: 0x3d4
+  __TEXT.__objc_methname: 0x3f5
+  __TEXT.__objc_methtype: 0xde
+  __TEXT.__objc_classname: 0x707
+  __TEXT.__swift5_reflstr: 0xcf2
+  __TEXT.__swift5_fieldmd: 0x273c
+  __TEXT.__oslogstring: 0x21ad
+  __TEXT.__cstring: 0x1970
+  __TEXT.__swift5_capture: 0x950
+  __TEXT.__swift5_assocty: 0x530
+  __TEXT.__swift5_proto: 0xdac
+  __TEXT.__swift_as_entry: 0x84
+  __TEXT.__swift_as_ret: 0x40
+  __TEXT.__swift_as_cont: 0x130
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methtype: 0x2e
-  __TEXT.__swift5_mpenum: 0x30
+  __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x1b58
-  __TEXT.__eh_frame: 0x2e00
-  __DATA_CONST.__const: 0x46e8
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__unwind_info: 0x2ab0
+  __TEXT.__eh_frame: 0x4898
+  __DATA_CONST.__const: 0x7b50
+  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xbc0
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__auth_ptr: 0x3e0
-  __DATA.__objc_const: 0x1978
-  __DATA.__objc_selrefs: 0x30
-  __DATA.__data: 0x3242
-  __DATA.__common: 0x68
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__auth_got: 0xc08
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__auth_ptr: 0x4c8
+  __DATA.__objc_const: 0x1ba8
+  __DATA.__objc_selrefs: 0xd0
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0x46c2
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1861
-  Symbols:   577
-  CStrings:  265
+  Functions: 2937
+  Symbols:   589
+  CStrings:  422
 
Symbols:
+ _$s13SecurePairing0aB5ErrorV4CodeO21audioListeningFailureyA2EmFWC
+ _$s19SecureAudioPasscode0A20PairingInputRecorderC4stopSbyFTj
+ _$s19SecureAudioPasscode0A20PairingInputRecorderC5startSbyFTj
+ _$s19SecureAudioPasscode0A20PairingInputRecorderCACyKcfc
+ _$s19SecureAudioPasscode0A20PairingInputRecorderCMa
+ _$s19SecureAudioPasscode0A20PairingInputRecorderCMn
+ _$s9Tightbeam0A7EncoderV6encodeyys6UInt32VF
+ _$sScTss5NeverORszABRs_rlE11isCancelledSbvgZ
+ _$ss6UInt32VSEsWP
+ _$ss6UInt32VSesWP
+ _swift_release_x9
+ _swift_updateClassMetadata2
CStrings:
+ "#16@0:8"
+ ".domainKeysLeadExchange("
+ ".domainKeysPeerExchange("
+ ".sigmaPeerPairing("
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "Attempted SecurePairingInputRecorder.start() with result: %{bool}d"
+ "Attempted SecurePairingInputRecorder.stop() with result: %{bool}d"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "Cleaning up session: %s"
+ "Conclave initialization with resource com.apple.securepairingd.sigmapeerservice failed: %@. That is either build configuration error or given device does not support exclaves. Clients should check SecurePairing.supported property before attempting to call any framework SPI."
+ "Creating ACM context from user provided externalized form"
+ "Creating service: com.apple.securepairingd.sigmapeerservice"
+ "Ignoring suspicious attempt to stop listening from ownerId=%llu, current=%s"
+ "Invalid key value while decoding result type for cancelDomainPairing"
+ "Invalid key value while decoding result type for completeAttestation"
+ "Invalid key value while decoding result type for getAttestation"
+ "Invalid key value while decoding result type for handleDomainKeys"
+ "Invalid key value while decoding result type for handleDomainKeysAck"
+ "Invalid key value while decoding result type for handleMissingKeyTypesAck"
+ "Invalid key value while decoding result type for handleMissingKeyTypesCont"
+ "Invalid key value while decoding result type for handleStartKeyTransfer"
+ "Invalid key value while decoding result type for startDomainPairing"
+ "Invalid key value while decoding result type for startListening"
+ "Invalid key value while decoding result type for testSetProximityInfo"
+ "Invalid key value while decoding result type for verifyRandomK"
+ "NSObject"
+ "OS_os_transaction"
+ "Q16@0:8"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "Using legacy ACM context creation. Please switch to using the SecurePairingContext"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "_TtC14securepairingd19SecureAudioListener"
+ "autorelease"
+ "cancelDomainPairing"
+ "class"
+ "com.apple.securepairing.audioListen"
+ "com.apple.securepairing.domainKeysExchange.lead."
+ "com.apple.securepairing.domainKeysExchange.peer."
+ "com.apple.securepairing.pairingSession.peer."
+ "com.apple.securepairingd.sigmapeerservice"
+ "completeAttestation"
+ "conformsToProtocol:"
+ "debugDescription"
+ "description"
+ "domainCancelPairing"
+ "domainCancelPairing error: %@"
+ "domainHandleDomainKeys"
+ "domainHandleDomainKeys error: %@"
+ "domainHandleDomainKeysAck"
+ "domainHandleDomainKeysAck error: %@"
+ "domainHandleMissingKeyTypesAck"
+ "domainHandleMissingKeyTypesAck error: %@"
+ "domainPeerCancelPairing"
+ "domainPeerCancelPairing error: %@"
+ "domainPeerHandleDomainKeys"
+ "domainPeerHandleDomainKeys error: %@"
+ "domainPeerHandleDomainKeysAck"
+ "domainPeerHandleDomainKeysAck error: %@"
+ "domainPeerHandleMissingKeyTypes"
+ "domainPeerHandleMissingKeyTypes error: %@"
+ "domainPeerHandleMissingKeyTypesCont"
+ "domainPeerHandleMissingKeyTypesCont error: %@"
+ "domainPeerHandleStartKeyTransfer"
+ "domainPeerHandleStartKeyTransfer error: %@"
+ "domainPeerSessionEnded"
+ "domainSessionEnded"
+ "domainStartKeyTransfer"
+ "domainStartKeyTransfer error: %@"
+ "domainStartPairing"
+ "domainStartPairing error: %@"
+ "domainStartPeerPairing"
+ "externalizedACMContext"
+ "getAttestation (peer)"
+ "handleDomainKeys"
+ "handleDomainKeysAck"
+ "handleMissingKeyTypes"
+ "handleMissingKeyTypesAck"
+ "handleMissingKeyTypesCont"
+ "handleStartKeyTransfer"
+ "hash"
+ "initSecureIntent"
+ "inputRecorder"
+ "invalid rawValue for TransferEncoding: "
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "osTransaction"
+ "ownerId"
+ "parkedAudioBoostContinuation"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "preferedEncoding"
+ "processing XPC request domainCancelPairing"
+ "processing XPC request domainHandleDomainKeys"
+ "processing XPC request domainHandleDomainKeysAck"
+ "processing XPC request domainHandleMissingKeyTypesAck"
+ "processing XPC request domainPeerCancelPairing"
+ "processing XPC request domainPeerHandleDomainKeys"
+ "processing XPC request domainPeerHandleDomainKeysAck"
+ "processing XPC request domainPeerHandleMissingKeyTypes"
+ "processing XPC request domainPeerHandleMissingKeyTypesCont"
+ "processing XPC request domainPeerHandleStartKeyTransfer"
+ "processing XPC request domainPeerSessionEnded for pairingID=%llu"
+ "processing XPC request domainSessionEnded for pairingID=%llu"
+ "processing XPC request domainStartKeyTransfer"
+ "processing XPC request domainStartPairing"
+ "processing XPC request sigmaPeerCancelPairing for pairingID=%llu"
+ "processing XPC request sigmaPeerSessionEnded for pairingID=%llu"
+ "processing XPC request sigmaSessionInit (POR)"
+ "processing XPC request sigmaStartListening"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "securepairingd/SecureAudioSupport.swift"
+ "securepairingd/SecurePairingServicesInternal_swift.swift"
+ "self"
+ "sigmaCompleteAttestation"
+ "sigmaCompleteAttestation (peer)"
+ "sigmaCompleteAttestation error: %@"
+ "sigmaPeerCancelPairing"
+ "sigmaPeerCancelPairing conclave error: %@"
+ "sigmaPeerCancelPairing: context cleared for pairingID=%llu"
+ "sigmaPeerSessionEnded"
+ "sigmaProximityBypass"
+ "sigmaProximityBypass error: %@"
+ "sigmaSessionInit"
+ "sigmaSessionInit error: %@"
+ "sigmaSetRandomK"
+ "sigmaSetRandomK error: %@"
+ "sigmaStartListening"
+ "sigmaStartListening error: %@"
+ "sigmaVerifyRandomK"
+ "sigmaVerifyRandomK error: %@"
+ "startDomainPairing"
+ "startListening (peer)"
+ "startListening(ownerId:timeout:)"
+ "startPairing (peer)"
+ "stopListening(ownerId:)"
+ "superclass"
+ "testSetProximityInfo (peer)"
+ "timeoutTask"
+ "unexpected randomK data size"
+ "unexpected wka passcode data size"
+ "zone"
- "Cleaning up session: %llu"
- "securepairingd/SecurePairingServices_swift.swift"
```
