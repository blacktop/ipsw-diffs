## DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

-684.100.52.0.1
-  __TEXT.__text: 0x4dab0
-  __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_stubs: 0x30e0
-  __TEXT.__objc_methlist: 0x1354
-  __TEXT.__const: 0x4188
-  __TEXT.__cstring: 0x25d0
-  __TEXT.__objc_methname: 0x3da3
-  __TEXT.__objc_classname: 0x467
-  __TEXT.__objc_methtype: 0xc78
-  __TEXT.__oslogstring: 0x127e
-  __TEXT.__gcc_except_tab: 0x220
-  __TEXT.__swift5_typeref: 0x8b8
-  __TEXT.__swift5_fieldmd: 0x15bc
-  __TEXT.__constg_swiftt: 0xddc
-  __TEXT.__swift5_reflstr: 0x1a83
+684.100.58.0.1
+  __TEXT.__text: 0x4fcac
+  __TEXT.__auth_stubs: 0x1130
+  __TEXT.__objc_stubs: 0x3080
+  __TEXT.__objc_methlist: 0x1384
+  __TEXT.__const: 0x41c8
+  __TEXT.__cstring: 0x25e0
+  __TEXT.__objc_methname: 0x3de3
+  __TEXT.__objc_classname: 0x477
+  __TEXT.__objc_methtype: 0xc98
+  __TEXT.__oslogstring: 0x1262
+  __TEXT.__gcc_except_tab: 0x1f0
+  __TEXT.__swift5_typeref: 0x8f6
+  __TEXT.__swift5_fieldmd: 0x15d8
+  __TEXT.__constg_swiftt: 0xe18
+  __TEXT.__swift5_reflstr: 0x1a93
   __TEXT.__swift5_capture: 0x24
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_proto: 0x310
-  __TEXT.__swift5_types: 0x17c
+  __TEXT.__swift5_types: 0x180
   __TEXT.__swift5_assocty: 0x5e8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1c48
-  __TEXT.__eh_frame: 0x4110
-  __DATA_CONST.__auth_got: 0x830
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__auth_ptr: 0x280
+  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__eh_frame: 0x4368
+  __DATA_CONST.__auth_got: 0x8a8
+  __DATA_CONST.__got: 0x548
+  __DATA_CONST.__auth_ptr: 0x290
   __DATA_CONST.__const: 0x2d08
-  __DATA_CONST.__cfstring: 0x15e0
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__cfstring: 0x14c0
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x2500
-  __DATA.__objc_selrefs: 0xe50
-  __DATA.__objc_ivar: 0xfc
-  __DATA.__objc_data: 0xe78
-  __DATA.__data: 0x2490
+  __DATA.__objc_const: 0x2640
+  __DATA.__objc_selrefs: 0xe48
+  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_data: 0xf38
+  __DATA.__data: 0x24f0
   __DATA.__bss: 0x5bc0
   __DATA.__common: 0x140
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 93D6B42B-A554-38D2-853D-335DE0199FFF
-  Functions: 2293
-  Symbols:   346
-  CStrings:  1311
+  UUID: FA3F2880-7BF1-37BF-8ACC-10DC12737B66
+  Functions: 2320
+  Symbols:   359
+  CStrings:  1312
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _NSUnderlyingErrorKey
+ __DPDediscoErrorDomain
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ _malloc_size
+ _memmove
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_dynamicCast
+ _swift_getObjectType
+ _swift_initStackObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_setDeallocating
- _OBJC_CLASS_$__DPLHBitacoraLogger
CStrings:
+ "%@, error: %@"
+ "@56@0:8@16@24C32C36@40@48"
+ "Bypassing SGX for collectionID %@ - sending DAP report only"
+ "C"
+ "DPSubmissionService.HPKEConfigShim"
+ "Failed to encrypt shares"
+ "Failed to encrypt, error: %@"
+ "Failed to extract helper server name."
+ "Failed to extract leader server name."
+ "Failed to find a HPKE configuration with the supported cipher suite."
+ "Failed to find server %@ under role %@"
+ "Failed to obtain HPKE config and signature fields from Dedisco V2 configuration file for server %@."
+ "Failed to obtain certificate from Dedisco V2 configuration file for server %@."
+ "Failed to parse HPKEConfig bytes."
+ "Failed to parse HPKEConfigList bytes."
+ "Failed to send V1 payloads for collectionID %@ - http upload is forbidden"
+ "Failed to serialize DediscoAlgorithmParametersOtherParams, error: %@"
+ "Failed to serialize payload"
+ "Failed to upload DAP report, error: %@"
+ "HPKEConfigShim"
+ "Leader URL is empty"
+ "Nothing to upload: serialized report is empty"
+ "OHTTP is not enabled in donation metadata"
+ "Report upload was successful"
+ "T@\"NSString\",R,N,V_helperURL"
+ "T@\"NSString\",R,N,V_leaderURL"
+ "TC,R,N,V_helperHPKEConfigID"
+ "TC,R,N,V_leaderHPKEConfigID"
+ "The total size of payload exceeds 1MB"
+ "Timeout uploading to %@"
+ "Unable to determine if OHTTP is enabled: %@"
+ "Unable to extracting base64 representation from public key, error: %@"
+ "Upload rejected for %@, error: %@"
+ "Upload rejected, error: %@"
+ "Uploading DAP report to %@, OHTTP:%s"
+ "Uploading to %@, body size: %lu"
+ "Uploading via V2 with OHTTP for %@"
+ "Uploading via V2 without OHTTP for %@"
+ "_helperHPKEConfigID"
+ "_leaderHPKEConfigID"
+ "arrayWithCapacity:"
+ "configID"
+ "fromHPKEConfigBytes:error:"
+ "fromHPKEConfigListBytes:error:"
+ "hpke_config"
+ "hpke_config_signature"
+ "initWithDestinationKey:facilitatorPublicKey:leaderHPKEConfigID:helperHPKEConfigID:leaderURL:helperURL:"
+ "initWithDomain:code:userInfo:"
+ "number type UInt16."
+ "number type UInt32."
+ "number type UInt8."
+ "of it to decode TLS number type UInt16."
+ "of it to decode TLS number type UInt32."
+ "of it to decode TLS number type UInt8."
- "%@; "
- "Bypassing SGX for collectionID %@ - Sending DAP report only"
- "Dedisco V2 config is malformed; HPKE configuration is not supported."
- "Dedisco V2 config is malformed; buffer length does not match the expected value."
- "Dedisco V2 config is malformed; public key length is zero."
- "Error encrypting: %@"
- "Error extracting base64 representation from public key: %@"
- "Failed to decode the DAP encoded configuration file"
- "Failed to fetch %ld tokens out of %ld with errors: %@"
- "Failed to obtain fields from Dedisco V2 configuration file for server %@."
- "Failed to send V1 payloads collectionID %@ - http upload is forbidden"
- "Failed to serialize DediscoAlgorithmParametersOtherParams: %@"
- "Failed to upload DAP Payload: %@"
- "Failed to upload DAP payload: leader URL is empty"
- "Failed to upload DAP report to %@, error: %@"
- "Found %lu number of leader and helpers; at least one leader and one helper role needs to be provided."
- "Malformed Dedisco V2 config, the buffer length is lower than the minimum length."
- "Nothing to upload: serialized report is empty: %@"
- "OHTTP is not enabled in donation metadata, but it should be strictly required."
- "Submitting via V2 with OHTTP for key=%@"
- "Submitting via V2 without OHTTP for key=%@"
- "The total size of payload exceeds 1 MB."
- "Time out while uploading DAP report to %@"
- "Timeout uploading: %@"
- "Token count: %lu; %@"
- "Unable to encrypt shares."
- "Unable to serialize payload dictionary."
- "Upload rejected due to missing OHTTP: %@"
- "Upload rejected: unable to determine OHTTP flag: %@"
- "Upload via HTTP body size: %lu - uploading to %@"
- "Uploading DAP payload to %@, OHTTP:%s"
- "aead_id"
- "dataWithBytes:length:"
- "decodeDAPEncodedConfig:withError:"
- "donateEventToBitacoraForKey:eventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:telemetryAllowed:"
- "donateTokenCountToBitacoraForDirPath:"
- "fedstats:com.apple.Bitacora.TokenFetcher:000:000:iOS"
- "id"
- "initWithDestinationKey:facilitatorPublicKey:keysMetadataArray:"
- "kdf_id"
- "kem_id"
- "numberWithChar:"
- "numberWithUnsignedShort:"
- "unsignedShortValue"

```
