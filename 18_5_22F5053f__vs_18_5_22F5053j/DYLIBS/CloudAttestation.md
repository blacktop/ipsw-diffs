## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-199.120.9.0.0
-  __TEXT.__text: 0x109418
-  __TEXT.__auth_stubs: 0x2420
+199.120.9.0.1
+  __TEXT.__text: 0x1185c8
+  __TEXT.__auth_stubs: 0x25e0
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0xbebe
-  __TEXT.__cstring: 0x2894
-  __TEXT.__constg_swiftt: 0x2928
-  __TEXT.__swift5_typeref: 0x2660
-  __TEXT.__swift5_fieldmd: 0x31dc
-  __TEXT.__swift5_proto: 0xa30
-  __TEXT.__swift5_types: 0x3b4
-  __TEXT.__oslogstring: 0x22e8
-  __TEXT.__swift5_reflstr: 0x2812
-  __TEXT.__swift_as_entry: 0x298
-  __TEXT.__swift_as_ret: 0x24c
-  __TEXT.__swift5_capture: 0x280
+  __TEXT.__const: 0xc5fe
+  __TEXT.__cstring: 0x28e4
+  __TEXT.__constg_swiftt: 0x2ad4
+  __TEXT.__swift5_typeref: 0x2784
+  __TEXT.__swift5_fieldmd: 0x3480
+  __TEXT.__swift5_proto: 0xa70
+  __TEXT.__swift5_types: 0x3e8
+  __TEXT.__oslogstring: 0x24c8
+  __TEXT.__swift5_reflstr: 0x2a62
+  __TEXT.__swift_as_entry: 0x2cc
+  __TEXT.__swift_as_ret: 0x288
+  __TEXT.__swift5_capture: 0x2a0
   __TEXT.__swift5_assocty: 0x588
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_mpenum: 0x98
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_mpenum: 0xb0
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x4600
-  __TEXT.__eh_frame: 0x8bb0
+  __TEXT.__unwind_info: 0x4968
+  __TEXT.__eh_frame: 0x96b8
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methname: 0x3ce
   __TEXT.__objc_methtype: 0x16c
-  __DATA_CONST.__got: 0x6a8
-  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__const: 0x400
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1210
-  __AUTH_CONST.__auth_ptr: 0xa68
-  __AUTH_CONST.__const: 0x5cc0
+  __AUTH_CONST.__auth_got: 0x12f0
+  __AUTH_CONST.__auth_ptr: 0xaa0
+  __AUTH_CONST.__const: 0x60a0
   __AUTH_CONST.__objc_const: 0x730
   __AUTH.__objc_data: 0x200
-  __AUTH.__data: 0x2170
-  __DATA.__data: 0x2e10
-  __DATA.__bss: 0x10f80
-  __DATA.__common: 0x1d8
+  __AUTH.__data: 0x23a0
+  __DATA.__data: 0x2f98
+  __DATA.__bss: 0x11780
+  __DATA.__common: 0x208
   __DATA_DIRTY.__data: 0x1ba0
   __DATA_DIRTY.__common: 0x158
   __DATA_DIRTY.__bss: 0x2180

   - /System/Library/Frameworks/SecureConfigDB.framework/SecureConfigDB
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5795
-  Symbols:   1572
-  CStrings:  548
+  Functions: 6019
+  Symbols:   1629
+  CStrings:  560
 
Symbols:
+ _SecKeyCreateWithData
+ ___swift_memcpy33_8
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit_$_CloudAttestation
+ _associated conformance 16CloudAttestation12EnsembleHPKEO5ErrorOSHAASQ
+ _associated conformance 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV10CodingKeys33_AED713BC47CB23669FD121EC32555A91LLOSHAASQ
+ _associated conformance 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV10CodingKeys33_AED713BC47CB23669FD121EC32555A91LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV10CodingKeys33_AED713BC47CB23669FD121EC32555A91LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 16CloudAttestation23EnsembleChannelSecurityO11PairingDataVSHAASQ
+ _get_enum_tag_for_layout_string 16CloudAttestation23EnsembleChannelSecurityO5ErrorO
+ _get_enum_tag_for_layout_string 16CloudAttestation23EnsembleChannelSecurityO5ErrorO023ProvisioningCertificateF0O
+ _get_enum_tag_for_layout_string 16CloudAttestation23EnsembleChannelSecurityO5ErrorO08TopologyF0O
+ _kSecAttrKeyClass
+ _kSecAttrKeyClassPrivate
+ _symbolic SDySSShySSGG
+ _symbolic SS7chassis_Si5countSi7maximumt
+ _symbolic SS8provided_SS11certificatet
+ _symbolic ShySSG
+ _symbolic Si5count_Si7maximumt
+ _symbolic _____ 16CloudAttestation12EnsembleHPKEO
+ _symbolic _____ 16CloudAttestation12EnsembleHPKEO5ErrorO
+ _symbolic _____ 16CloudAttestation12EnsembleHPKEO6LeaderV
+ _symbolic _____ 16CloudAttestation12EnsembleHPKEO8FollowerV
+ _symbolic _____ 16CloudAttestation14SendableSecKey33_A3EB2001BB80B769F4496A57F0023FDCLLV
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV10CodingKeys33_AED713BC47CB23669FD121EC32555A91LLO
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO5ErrorO
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO5ErrorO023ProvisioningCertificateF0O
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO5ErrorO08TopologyF0O
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO6LeaderV
+ _symbolic _____ 16CloudAttestation23EnsembleChannelSecurityO8FollowerV
+ _symbolic _____ 9CryptoKit12SymmetricKeyV
+ _symbolic ______p 16CloudAttestation8AttestorP
+ _symbolic _____ySSG s11_SetStorageC
+ _symbolic _____ySSShySSGG s18_DictionaryStorageC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV10CodingKeys33_AED713BC47CB23669FD121EC32555A91LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV10CodingKeys33_AED713BC47CB23669FD121EC32555A91LLO
+ _type_layout_string 16CloudAttestation14SendableSecKey33_A3EB2001BB80B769F4496A57F0023FDCLLV
+ _type_layout_string 16CloudAttestation23EnsembleChannelSecurityO11PairingDataV
+ _type_layout_string 16CloudAttestation23EnsembleChannelSecurityO5ErrorO
+ _type_layout_string 16CloudAttestation23EnsembleChannelSecurityO5ErrorO023ProvisioningCertificateF0O
+ _type_layout_string 16CloudAttestation23EnsembleChannelSecurityO5ErrorO08TopologyF0O
CStrings:
+ "B6FF3FC5-7CAF-4898-82F5-4887ED946ABC"
+ "EnsembleChannelSecurity.Leader"
+ "Follower UDID %{public}s does not match provisioning certificate UDID %{public}s"
+ "Follower UDID %{public}s not in expected set %{public}s"
+ "Follower completed pairing with leader: %{public}s"
+ "Follower rekeyed"
+ "Leader attestation generated"
+ "Leader pairing with %{public}s"
+ "Leader rekeyed"
+ "Malformed darwin-init: %{public}@"
+ "No SecureConfig entries in SecureConfigDB"
+ "No darwin-init entry in SecureConfigDB"

```
