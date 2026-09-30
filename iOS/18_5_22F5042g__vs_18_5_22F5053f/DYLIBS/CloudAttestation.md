## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-199.120.1.0.0
-  __TEXT.__text: 0x10d970
-  __TEXT.__auth_stubs: 0x25a0
+199.120.9.0.0
+  __TEXT.__text: 0x109418
+  __TEXT.__auth_stubs: 0x2420
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0xbe5e
-  __TEXT.__cstring: 0x25c4
-  __TEXT.__constg_swiftt: 0x2960
-  __TEXT.__swift5_typeref: 0x264e
-  __TEXT.__swift5_fieldmd: 0x32b4
-  __TEXT.__swift5_proto: 0xa0c
-  __TEXT.__swift5_types: 0x3d0
-  __TEXT.__oslogstring: 0x2488
-  __TEXT.__swift5_reflstr: 0x29c2
-  __TEXT.__swift_as_entry: 0x284
-  __TEXT.__swift_as_ret: 0x248
-  __TEXT.__swift5_capture: 0x16c
-  __TEXT.__swift5_assocty: 0x558
-  __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_mpenum: 0xb8
+  __TEXT.__const: 0xbebe
+  __TEXT.__cstring: 0x2894
+  __TEXT.__constg_swiftt: 0x2928
+  __TEXT.__swift5_typeref: 0x2660
+  __TEXT.__swift5_fieldmd: 0x31dc
+  __TEXT.__swift5_proto: 0xa30
+  __TEXT.__swift5_types: 0x3b4
+  __TEXT.__oslogstring: 0x22e8
+  __TEXT.__swift5_reflstr: 0x2812
+  __TEXT.__swift_as_entry: 0x298
+  __TEXT.__swift_as_ret: 0x24c
+  __TEXT.__swift5_capture: 0x280
+  __TEXT.__swift5_assocty: 0x588
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_mpenum: 0x98
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x4608
-  __TEXT.__eh_frame: 0x8d50
+  __TEXT.__unwind_info: 0x4600
+  __TEXT.__eh_frame: 0x8bb0
   __TEXT.__objc_classname: 0x3b
-  __TEXT.__objc_methname: 0x3b5
+  __TEXT.__objc_methname: 0x3ce
   __TEXT.__objc_methtype: 0x16c
-  __DATA_CONST.__got: 0x6d8
-  __DATA_CONST.__const: 0x400
-  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__got: 0x6a8
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x160
+  __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x12d0
-  __AUTH_CONST.__auth_ptr: 0xa80
-  __AUTH_CONST.__const: 0x5e00
-  __AUTH_CONST.__objc_const: 0x658
-  __AUTH.__objc_data: 0x1b0
-  __AUTH.__data: 0x1e38
-  __DATA.__data: 0x2ba8
-  __DATA.__bss: 0x10880
-  __DATA.__common: 0x208
-  __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x1eb8
+  __AUTH_CONST.__auth_got: 0x1210
+  __AUTH_CONST.__auth_ptr: 0xa68
+  __AUTH_CONST.__const: 0x5cc0
+  __AUTH_CONST.__objc_const: 0x730
+  __AUTH.__objc_data: 0x200
+  __AUTH.__data: 0x2170
+  __DATA.__data: 0x2e10
+  __DATA.__bss: 0x10f80
+  __DATA.__common: 0x1d8
+  __DATA_DIRTY.__data: 0x1ba0
   __DATA_DIRTY.__common: 0x158
-  __DATA_DIRTY.__bss: 0x2400
+  __DATA_DIRTY.__bss: 0x2180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/SecureConfigDB.framework/SecureConfigDB
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
-  - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5750
-  Symbols:   350
-  CStrings:  542
+  Functions: 5795
+  Symbols:   346
+  CStrings:  548
 
Symbols:
+ _SecIdentityCopyCertificate
+ _objc_retain_x9
- _SecKeyCreateWithData
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- _kSecAttrKeyClass
- _kSecAttrKeyClassPrivate
CStrings:
+ "AttestedTLS.Configurator"
+ "AttestedTLS.OptionsFactory"
+ "Curve25519 keys not yet supported"
+ "PrivateCloudCompute.TransparencyLog.ATActiveRecordsRequest"
+ "PrivateCloudCompute.TransparencyLog.ATActiveRecordsResponse"
+ "PrivateCloudCompute.TransparencyLog.ATInsertData"
+ "PrivateCloudCompute.TransparencyLog.ATLogInsertRequest"
+ "PrivateCloudCompute.TransparencyLog.ATLogInsertResponse"
+ "PrivateCloudCompute.TransparencyLog.ATLogProofRequest"
+ "PrivateCloudCompute.TransparencyLog.ATLogProofResponse"
+ "PrivateCloudCompute.TransparencyLog.ATLogProofs"
+ "PrivateCloudCompute.TransparencyLog.LogConsistency"
+ "SEED"
+ "_TtCO16CloudAttestation11AttestedTLS15IdentityStorage"
+ "_TtCV16CloudAttestation50PrivateCloudCompute_TransparencyLog_LogConsistencyP33_41967CC35744CDFB8E92E7B80EC2B17A13_StorageClass"
+ "dataHash"
+ "finishTasksAndInvalidate"
+ "identity"
+ "leaves"
+ "proofsExpiration expiration "
+ "rawData"
+ "release sha256:%s is covered by proxy node attestation"
+ "releaseType"
- "%s is covered by proxy node attestation"
- "B6FF3FC5-7CAF-4898-82F5-4887ED946ABC"
- "EnsembleChannelSecurity.Leader"
- "Follower UDID %{public}s does not match provisioning certificate UDID %{public}s"
- "Follower UDID %{public}s not in expected set %{public}s"
- "Follower completed pairing with leader: %{public}s"
- "Follower rekeyed"
- "Leader attestation generated"
- "Leader pairing with %{public}s"
- "Leader rekeyed"
- "Malformed darwin-init: %{public}@"
- "MutualTLS.OptionsFactory"
- "No SecureConfig entries in SecureConfigDB"
- "No darwin-init entry in SecureConfigDB"
- "_TtCV16CloudAttestation14LogConsistencyP33_41967CC35744CDFB8E92E7B80EC2B17A13_StorageClass"
- "identifier"
- "serverEventInfo"

```
