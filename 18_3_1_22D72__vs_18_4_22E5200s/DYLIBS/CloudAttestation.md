## CloudAttestation

> `/System/Library/PrivateFrameworks/CloudAttestation.framework/CloudAttestation`

```diff

-196.0.0.0.0
-  __TEXT.__text: 0x105868
-  __TEXT.__auth_stubs: 0x21f0
-  __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x97f0
-  __TEXT.__cstring: 0x24bf
-  __TEXT.__constg_swiftt: 0x2338
-  __TEXT.__swift5_typeref: 0x1fd5
-  __TEXT.__swift5_reflstr: 0x2352
-  __TEXT.__swift5_fieldmd: 0x2c9c
-  __TEXT.__swift5_assocty: 0x4b0
-  __TEXT.__swift5_proto: 0x908
-  __TEXT.__swift5_types: 0x354
-  __TEXT.__swift5_capture: 0xe0
-  __TEXT.__oslogstring: 0x1d4b
+199.100.10.0.4
+  __TEXT.__text: 0xf8cd8
+  __TEXT.__auth_stubs: 0x2590
+  __TEXT.__objc_methlist: 0x164
+  __TEXT.__const: 0xb91e
+  __TEXT.__cstring: 0x2554
+  __TEXT.__constg_swiftt: 0x2894
+  __TEXT.__swift5_typeref: 0x25dc
+  __TEXT.__swift5_fieldmd: 0x3174
+  __TEXT.__swift5_proto: 0x9c8
+  __TEXT.__swift5_types: 0x3bc
+  __TEXT.__oslogstring: 0x2288
+  __TEXT.__swift5_reflstr: 0x28a3
+  __TEXT.__swift_as_entry: 0x224
+  __TEXT.__swift_as_ret: 0x1e0
+  __TEXT.__swift5_capture: 0x158
+  __TEXT.__swift5_assocty: 0x508
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0x94
   __TEXT.__swift5_protos: 0x28
-  __TEXT.__unwind_info: 0x3b80
-  __TEXT.__eh_frame: 0x64d0
-  __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x3a1
+  __TEXT.__unwind_info: 0x42e0
+  __TEXT.__eh_frame: 0x81d8
+  __TEXT.__objc_classname: 0x3b
+  __TEXT.__objc_methname: 0x3b5
   __TEXT.__objc_methtype: 0x16c
-  __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x158
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x20
+  __DATA_CONST.__got: 0x5b0
+  __DATA_CONST.__const: 0x430
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb0
-  __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x10f8
-  __AUTH_CONST.__auth_ptr: 0xa88
-  __AUTH_CONST.__const: 0x50f0
-  __AUTH_CONST.__objc_const: 0x738
-  __AUTH.__objc_data: 0x160
-  __AUTH.__data: 0x1778
-  __DATA.__data: 0x1f98
-  __DATA.__common: 0x708
-  __DATA.__bss: 0xf280
+  __DATA_CONST.__objc_selrefs: 0x160
+  __DATA_CONST.__objc_protorefs: 0x20
+  __AUTH_CONST.__auth_got: 0x12c8
+  __AUTH_CONST.__auth_ptr: 0xc28
+  __AUTH_CONST.__const: 0x5a30
+  __AUTH_CONST.__objc_const: 0x658
+  __AUTH.__objc_data: 0x1b0
+  __AUTH.__data: 0x1de8
+  __DATA.__data: 0x29d8
+  __DATA.__bss: 0xff80
+  __DATA.__common: 0x208
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x1af8
-  __DATA_DIRTY.__bss: 0x1c80
+  __DATA_DIRTY.__data: 0x1ea8
   __DATA_DIRTY.__common: 0x158
+  __DATA_DIRTY.__bss: 0x2400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/SecureConfigDB.framework/SecureConfigDB
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore

   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
-  - /System/Library/PrivateFrameworks/SwiftASN1.framework/SwiftASN1
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
+  - /System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal
   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
   - /System/Library/PrivateFrameworks/libnarrativecert.framework/libnarrativecert
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4740
-  Symbols:   273
-  CStrings:  498
+  Functions: 5543
+  Symbols:   350
+  CStrings:  531
 
Symbols:
+ _MAEIssueDCRTWithCompletion
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _SecCertificateCopyNotValidAfterDate
+ _SecGenerateSelfSignedCertificate
+ _SecIdentityCreate
+ _SecTrustCopyCertificateChain
+ _kMAOptionsIgnoreExistingDCRT
+ _kMAOptionsNetworkTimeoutInterval
+ _kSecAttrKeyTypeECSECPrimeRandomPKA
+ _kSecAttrKeyTypeX25519
+ _kSecCertificateExtensions
+ _kSecCertificateKeyUsage
+ _kSecCertificateLifetime
+ _kSecCertificateSerialNumber
+ _kSecOidCommonName
+ _sec_identity_create
+ _sec_protocol_options_set_challenge_block
+ _sec_protocol_options_set_min_tls_protocol_version
+ _sec_protocol_options_set_peer_authentication_required
+ _sec_protocol_options_set_verify_block
+ _sec_trust_copy_ref
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getExistentialTypeMetadata
+ _swift_getFunctionTypeMetadata0
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
+ _swift_retain_n
+ _swift_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_singlePayloadEnumGeneric_getEnumTag
+ _swift_task_create
+ _sysctlbyname
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initEnumMetadataSinglePayload
- _swift_initStructMetadata
CStrings:
+ " missing "
+ " notEqual "
+ "%s is covered by proxy attestation"
+ "AttestationBundle passed ProxiedReleaseTransparencyPolicy: All proxied releases are included in the transparency log"
+ "Failed to read cryptex sealed hashes from %{public}s"
+ "Failed to read seled hashes from %{public}s"
+ "GenericAttestor.AssetProvider"
+ "IODeviceTree:/product"
+ "Invalid transparency proof for digest %{public}s"
+ "MutualTLS.Certificate"
+ "MutualTLS.OptionsFactory"
+ "OS_sec_identity"
+ "OS_sec_trust"
+ "PrivateCloudCompute.ProxyNodeMetadata"
+ "Proxied release metadata is missing transparency proofs"
+ "Release %{public}s has expired in the transparency log"
+ "Release %{public}s is included in transparency log"
+ "Release %{public}s is not included in transparency log, this is likely indicative of using the wrong transparency log"
+ "SEP Cryptex Sealed Hash Slot is missing .cryptexMeasurement"
+ "SWTransparency threw unknown error for release %{public}s: %{public}@"
+ "SecKeyCopyExternalRepresentation failed but did not return an error object"
+ "SecTrust verification completedly successfully"
+ "SecTrust verification failed: %@"
+ "SecureConfigDB contains more than one darwin-init entry"
+ "Unknown transparency proof validation result for digest %{public}s: %{public}lu"
+ "Valid transparency proof for digest %{public}s (expires %{public}s"
+ "Verifying inclusion of proxied release %{public}s in transparency log"
+ "_TtCFV16CloudAttestation17SWTransparencyLog14proveInclusionFzZT2ofV10Foundation4Data_VS_21TransparencyLogProofsL_8Delegate"
+ "_TtCV16CloudAttestation23Proto_AttestationBundleP33_F901BED425ACAF29EDCFC5235099436113_StorageClass"
+ "_apTicket"
+ "_appData"
+ "_keyExpiration"
+ "_provisioningCertificateChain"
+ "_sealedHashes"
+ "_sepAttestation"
+ "_transparencyProofs"
+ "app_data"
+ "attestation creation failed: %@"
+ "com.apple.CloudAttestation.TransparencyPolicy"
+ "com.apple.PrivateCloudCompute"
+ "darwin-init contains ensemble certificate fingerprints"
+ "darwin-init missing from SecureConfigDB"
+ "dcrt chain not castable to [SecCertificate]"
+ "ephemeral-data-mode"
+ "failed to issue DCRT: %@"
+ "failed to read IODeviceTree:/product 'ephemeral-data-mode'"
+ "failed to read sysctl('security.mac.amfi.developer_mode_status')"
+ "failed to read sysctl('security.mac.amfi.restricted_execution_mode_status')"
+ "generic"
+ "name"
+ "proofsExpiration keyExpiration "
+ "proxied_release"
+ "replayed expeced "
+ "replayed expected "
+ "secureConfigLocked sealedHashLocked "
+ "security.mac.amfi.developer_mode_status"
+ "security.mac.amfi.restricted_execution_mode_status"
+ "uuid value "
+ "v24@?0@\"<OS_sec_protocol_metadata>\"8@?<v@?@\"<OS_sec_identity>\">16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "v32@?0@\"<OS_sec_protocol_metadata>\"8@\"<OS_sec_trust>\"16@?<v@?B>24"
+ "verifyExpiringProofs:forDigest:configuration:completion:"
- "Attestation udid %{public}s does not match %{public}s"
- "Attestation udid %{public}s matches %{public}s"
- "Can't construct Array with count < 0"
- "Insufficient space allocated to copy string contents"
- "Invalid transparency proof for: %{public}s"
- "Must take zero or more splits"
- "Not enough bits to represent the passed value"
- "Range requires lowerBound <= upperBound"
- "Swift/Array.swift"
- "Swift/Collection.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/Integers.swift"
- "Swift/Range.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "Unknown transparency proof validation result: %{public}lu"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Valid transparency proof for: %{public}s (expires %{public}s"
- "_TtCFV16CloudAttestation17SWTransparencyLog14proveInclusionFzZT2ofVS_7Release_VS_21TransparencyLogProofsL_8Delegate"
- "com.apple.CloudAttestation.AttestationProtocolError"
- "invalid Collection: less than 'count' elements in collection"
- "verifyExpiringProofs:for:completion:"

```
