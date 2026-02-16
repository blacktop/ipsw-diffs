## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-8.303.0.0.0
-  __TEXT.__text: 0x4b41c
-  __TEXT.__auth_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x214c
-  __TEXT.__const: 0x3aa8
-  __TEXT.__cstring: 0x2096
-  __TEXT.__oslogstring: 0x3f4c
+8.415.0.0.0
+  __TEXT.__text: 0x3e898
+  __TEXT.__auth_stubs: 0xbf0
+  __TEXT.__objc_methlist: 0x21c4
+  __TEXT.__const: 0x3650
+  __TEXT.__cstring: 0x1a7b
+  __TEXT.__oslogstring: 0x3e6c
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__constg_swiftt: 0x900
-  __TEXT.__swift5_typeref: 0xe70
+  __TEXT.__constg_swiftt: 0x7d0
+  __TEXT.__swift5_typeref: 0xc87
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x746
-  __TEXT.__swift5_fieldmd: 0x7f0
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x2cc
-  __TEXT.__swift5_types: 0xf4
-  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_reflstr: 0x334
+  __TEXT.__swift5_fieldmd: 0x65c
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x2b4
+  __TEXT.__swift5_types: 0xe4
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__swift5_capture: 0x5a0
-  __TEXT.__swift_as_entry: 0xd8
-  __TEXT.__swift_as_ret: 0xf0
-  __TEXT.__unwind_info: 0x1998
-  __TEXT.__eh_frame: 0x23b8
-  __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x45d6
-  __TEXT.__objc_methtype: 0xfc1
-  __TEXT.__objc_stubs: 0x1b00
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xa28
+  __TEXT.__swift5_capture: 0x2f4
+  __TEXT.__swift_as_entry: 0x6c
+  __TEXT.__swift_as_ret: 0x84
+  __TEXT.__unwind_info: 0x1548
+  __TEXT.__eh_frame: 0x1678
+  __TEXT.__objc_classname: 0x3e2
+  __TEXT.__objc_methname: 0x4974
+  __TEXT.__objc_methtype: 0x12da
+  __TEXT.__objc_stubs: 0x1d80
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x9f0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcc8
+  __DATA_CONST.__objc_selrefs: 0xca0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xb8
-  __AUTH_CONST.__auth_got: 0x720
-  __AUTH_CONST.__const: 0x2450
-  __AUTH_CONST.__cfstring: 0x1780
-  __AUTH_CONST.__objc_const: 0x37e0
-  __AUTH.__objc_data: 0x2a8
-  __AUTH.__data: 0x1b8
-  __DATA.__objc_ivar: 0x24c
-  __DATA.__data: 0xcf8
-  __DATA.__bss: 0x5a00
+  __DATA_CONST.__objc_superrefs: 0xc0
+  __AUTH_CONST.__auth_got: 0x608
+  __AUTH_CONST.__const: 0x1b50
+  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__objc_const: 0x3960
+  __AUTH.__objc_data: 0x2f8
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x264
+  __DATA.__data: 0xc10
+  __DATA.__bss: 0x5700
   __DATA_DIRTY.__objc_data: 0x708
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B884EE9F-AB9F-35A7-8197-8F984FC8270F
-  Functions: 2462
-  Symbols:   3462
-  CStrings:  1506
+  UUID: 0ED7DCBC-24EB-3EC2-B5EB-165987F09692
+  Functions: 2143
+  Symbols:   3401
+  CStrings:  1492
 
Symbols:
+ +[DCPayloadProperties supportsSecureCoding]
+ -[DCCredentialPayload initWithFormat:protectionType:docType:createdAt:updatedAt:validFrom:validUntil:signedAt:elementIdentifiersByNamespace:issuerCertificateChain:region:issuingJurisdiction:issuingAuthority:credentialRevocationInfo:payloadData:]
+ -[DCCredentialProperties payloads]
+ -[DCCredentialProperties setPayloads:]
+ -[DCCredentialRevocationInfo copyWithZone:]
+ -[DCPayloadProperties .cxx_destruct]
+ -[DCPayloadProperties createdAt]
+ -[DCPayloadProperties credentialRevocationInfo]
+ -[DCPayloadProperties description]
+ -[DCPayloadProperties documentType]
+ -[DCPayloadProperties encodeWithCoder:]
+ -[DCPayloadProperties ingestionHash]
+ -[DCPayloadProperties initWithCoder:]
+ -[DCPayloadProperties init]
+ -[DCPayloadProperties issuerCertificateChain]
+ -[DCPayloadProperties issuingAuthority]
+ -[DCPayloadProperties issuingJurisdiction]
+ -[DCPayloadProperties lock]
+ -[DCPayloadProperties region]
+ -[DCPayloadProperties setCreatedAt:]
+ -[DCPayloadProperties setCredentialRevocationInfo:]
+ -[DCPayloadProperties setDocumentType:]
+ -[DCPayloadProperties setIngestionHash:]
+ -[DCPayloadProperties setIssuerCertificateChain:]
+ -[DCPayloadProperties setIssuingAuthority:]
+ -[DCPayloadProperties setIssuingJurisdiction:]
+ -[DCPayloadProperties setLock:]
+ -[DCPayloadProperties setRegion:]
+ -[DCPayloadProperties setSignedAt:]
+ -[DCPayloadProperties setUpdatedAt:]
+ -[DCPayloadProperties setValidFrom:]
+ -[DCPayloadProperties setValidUntil:]
+ -[DCPayloadProperties signedAt]
+ -[DCPayloadProperties updatedAt]
+ -[DCPayloadProperties validFrom]
+ -[DCPayloadProperties validUntil]
+ -[DCPresentmentProposalReaderMetadata iconDigestAlgorithm]
+ -[DCPresentmentProposalReaderMetadata iconDigest]
+ -[DCPresentmentProposalReaderMetadata initWithIdentifier:organization:organizationalUnit:iconData:iconURL:iconDigest:iconDigestAlgorithm:iconMediaType:privacyPolicyURL:merchantCategoryCode:]
+ _DIP_LOG_MILESTONE_LOG
+ _DIP_LOG_MILESTONE_LOG.cold.1
+ _DIP_LOG_MILESTONE_LOG.log
+ _DIP_LOG_MILESTONE_LOG.once
+ _OBJC_CLASS_$_DCPayloadProperties
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_IVAR_$_DCCredentialProperties._payloads
+ _OBJC_IVAR_$_DCPayloadProperties._createdAt
+ _OBJC_IVAR_$_DCPayloadProperties._credentialRevocationInfo
+ _OBJC_IVAR_$_DCPayloadProperties._documentType
+ _OBJC_IVAR_$_DCPayloadProperties._ingestionHash
+ _OBJC_IVAR_$_DCPayloadProperties._issuerCertificateChain
+ _OBJC_IVAR_$_DCPayloadProperties._issuingAuthority
+ _OBJC_IVAR_$_DCPayloadProperties._issuingJurisdiction
+ _OBJC_IVAR_$_DCPayloadProperties._lock
+ _OBJC_IVAR_$_DCPayloadProperties._region
+ _OBJC_IVAR_$_DCPayloadProperties._signedAt
+ _OBJC_IVAR_$_DCPayloadProperties._updatedAt
+ _OBJC_IVAR_$_DCPayloadProperties._validFrom
+ _OBJC_IVAR_$_DCPayloadProperties._validUntil
+ _OBJC_IVAR_$_DCPresentmentProposalReaderMetadata._iconDigest
+ _OBJC_IVAR_$_DCPresentmentProposalReaderMetadata._iconDigestAlgorithm
+ _OBJC_METACLASS_$_DCPayloadProperties
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_CLASS_METHODS_DCPayloadProperties
+ __OBJC_$_CLASS_PROP_LIST_DCPayloadProperties
+ __OBJC_$_INSTANCE_METHODS_DCPayloadProperties
+ __OBJC_$_INSTANCE_VARIABLES_DCPayloadProperties
+ __OBJC_$_PROP_LIST_DCPayloadProperties
+ __OBJC_CLASS_PROTOCOLS_$_DCPayloadProperties
+ __OBJC_CLASS_RO_$_DCPayloadProperties
+ __OBJC_METACLASS_RO_$_DCPayloadProperties
+ __PROTOCOLS__TtC10CoreIDCred31XPCCredentialPresentmentRequest.2
+ ___245-[DCCredentialPayload initWithFormat:protectionType:docType:createdAt:updatedAt:validFrom:validUntil:signedAt:elementIdentifiersByNamespace:issuerCertificateChain:region:issuingJurisdiction:issuingAuthority:credentialRevocationInfo:payloadData:]_block_invoke
+ ___64-[DCCredentialStore(DebugAPIs) eraseLegacySEKeySlot:completion:]_block_invoke.277
+ ___64-[DCCredentialStore(DebugAPIs) keyInfoForCredential:completion:]_block_invoke.279
+ ___64-[DCCredentialStore(DebugAPIs) payloadsOfCredential:completion:]_block_invoke.274
+ ___71-[DCCredentialStore(DebugAPIs) occupiedLegacySEKeySlotsWithCompletion:]_block_invoke.276
+ ___76-[DCCredentialStore(DebugAPIs) allElementsOfCredential:authData:completion:]_block_invoke.275
+ ___81-[DCCredentialStore(DebugAPIs) clearPresentmentKeyUsageForCredential:completion:]_block_invoke.278
+ ___DIP_LOG_MILESTONE_LOG_block_invoke
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_CoreIDCred
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_CoreIDCred
+ _associated conformance 10CoreIDCred31XPCCredentialPresentmentRequestC0A9IDVShared17XPCValueContainerAA5ValueAdEP_SE
+ _associated conformance 10CoreIDCred31XPCCredentialPresentmentRequestC0A9IDVShared17XPCValueContainerAA5ValueAdEP_Se
+ _block_copy_helper.101
+ _block_copy_helper.188
+ _block_copy_helper.211
+ _block_copy_helper.236
+ _block_copy_helper.55
+ _block_copy_helper.78
+ _block_descriptor.103
+ _block_descriptor.190
+ _block_descriptor.213
+ _block_descriptor.238
+ _block_descriptor.57
+ _block_descriptor.80
+ _block_destroy_helper.102
+ _block_destroy_helper.189
+ _block_destroy_helper.212
+ _block_destroy_helper.237
+ _block_destroy_helper.56
+ _block_destroy_helper.79
+ _kReaderMetadataIconDigest
+ _kReaderMetadataIconDigestAlgorithm
+ _objc_msgSend$buildCredentialResponseFor:completionHandler:
+ _objc_msgSend$buildErrorResponseWith:completionHandler:
+ _objc_msgSend$buildGenericDataResponse:completionHandler:
+ _objc_msgSend$buildResponseFor:completionHandler:
+ _objc_msgSend$configureWithPartitions:presentmentType:options:completionHandler:
+ _objc_msgSend$count
+ _objc_msgSend$documentType
+ _objc_msgSend$encodedData
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$failWithError:
+ _objc_msgSend$finishDecoding
+ _objc_msgSend$finishEncoding
+ _objc_msgSend$generateTransportKeyFor:completionHandler:
+ _objc_msgSend$ingestionHash
+ _objc_msgSend$initForReadingFromData:error:
+ _objc_msgSend$initRequiringSecureCoding:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithFormat:protectionType:docType:createdAt:updatedAt:validFrom:validUntil:signedAt:elementIdentifiersByNamespace:issuerCertificateChain:region:issuingJurisdiction:issuingAuthority:credentialRevocationInfo:payloadData:
+ _objc_msgSend$initWithPartitions:presentmentType:options:
+ _objc_msgSend$initWithSessionEstablishment:sessionTranscript:
+ _objc_msgSend$interpretCredentialRequest:completionHandler:
+ _objc_msgSend$interpretGenericDataRequest:completionHandler:
+ _objc_msgSend$interpretRequest:completionHandler:
+ _objc_msgSend$payloads
+ _objc_msgSend$requiredPublicKeyIdentifier
+ _objc_msgSend$sessionEncryptionIntermediateKeyMaterial
+ _objc_msgSend$sessionEstablishment
+ _objc_msgSend$sessionTranscript
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setRequiredPublicKeyIdentifier:
+ _objc_msgSend$setSessionEncryptionIntermediateKeyMaterial:
+ _objc_msgSend$setSessionEstablishment:
+ _objc_msgSend$setSessionTranscript:
+ _objectdestroy.42Tm
+ _objectdestroy.83Tm
+ _symbolic $s13CoreIDVShared17XPCValueContainerP
+ _symbolic _____y______pG 13CoreIDVShared21SendableXPCConnectionC 0A6IDCred24DCPresentmentXPCProtocolP
- -[DCCredentialPayload init]
- -[DCCredentialPayload setCreatedAt:]
- -[DCCredentialPayload setCredentialRevocationInfo:]
- -[DCCredentialPayload setDocType:]
- -[DCCredentialPayload setElementIdentifiersByNamespace:]
- -[DCCredentialPayload setFormat:]
- -[DCCredentialPayload setIssuerCertificateChain:]
- -[DCCredentialPayload setIssuingAuthority:]
- -[DCCredentialPayload setIssuingJurisdiction:]
- -[DCCredentialPayload setPayloadData:]
- -[DCCredentialPayload setProtectionType:]
- -[DCCredentialPayload setRegion:]
- -[DCCredentialPayload setSignedAt:]
- -[DCCredentialPayload setUpdatedAt:]
- -[DCCredentialPayload setValidFrom:]
- -[DCCredentialPayload setValidUntil:]
- -[DCCredentialProperties issuerCertificateChain]
- -[DCCredentialProperties issuingAuthority]
- -[DCCredentialProperties issuingJurisdiction]
- -[DCCredentialProperties region]
- -[DCCredentialProperties setCredentialRevocationInfo:]
- -[DCCredentialProperties setDocType:]
- -[DCCredentialProperties setIssuerCertificateChain:]
- -[DCCredentialProperties setIssuingAuthority:]
- -[DCCredentialProperties setIssuingJurisdiction:]
- -[DCCredentialProperties setPayloadIngestionHash:]
- -[DCCredentialProperties setPayloadSignedAt:]
- -[DCCredentialProperties setPayloadValidFrom:]
- -[DCCredentialProperties setPayloadValidUntil:]
- -[DCCredentialProperties setRegion:]
- -[DCPresentmentProposalReaderMetadata initWithIdentifier:organization:organizationalUnit:iconData:iconURL:iconMediaType:privacyPolicyURL:merchantCategoryCode:]
- _DC_LOG_MILESTONE_LOG
- _DC_LOG_MILESTONE_LOG.cold.1
- _DC_LOG_MILESTONE_LOG.log
- _DC_LOG_MILESTONE_LOG.once
- _NSDebugDescriptionErrorKey
- _NSUnderlyingErrorKey
- _OBJC_CLASS_$__TtCs12_SwiftObject
- _OBJC_IVAR_$_DCCredentialProperties._credentialRevocationInfo
- _OBJC_IVAR_$_DCCredentialProperties._docType
- _OBJC_IVAR_$_DCCredentialProperties._issuerCertificateChain
- _OBJC_IVAR_$_DCCredentialProperties._issuingAuthority
- _OBJC_IVAR_$_DCCredentialProperties._issuingJurisdiction
- _OBJC_IVAR_$_DCCredentialProperties._payloadIngestionHash
- _OBJC_IVAR_$_DCCredentialProperties._payloadSignedAt
- _OBJC_IVAR_$_DCCredentialProperties._payloadValidFrom
- _OBJC_IVAR_$_DCCredentialProperties._payloadValidUntil
- _OBJC_IVAR_$_DCCredentialProperties._region
- _OBJC_METACLASS_$__TtCs12_SwiftObject
- __DATA__TtC10CoreIDCredP33_EE8AC1BF542F16A00864CAE0BC17C92B11BundleToken
- __IVARS__TtC10CoreIDCred21SendableXPCConnection
- __METACLASS_DATA__TtC10CoreIDCredP33_EE8AC1BF542F16A00864CAE0BC17C92B11BundleToken
- __PROTOCOLS__TtC10CoreIDCred31XPCCredentialPresentmentRequest.3
- ___64-[DCCredentialStore(DebugAPIs) eraseLegacySEKeySlot:completion:]_block_invoke.289
- ___64-[DCCredentialStore(DebugAPIs) keyInfoForCredential:completion:]_block_invoke.291
- ___64-[DCCredentialStore(DebugAPIs) payloadsOfCredential:completion:]_block_invoke.286
- ___71-[DCCredentialStore(DebugAPIs) occupiedLegacySEKeySlotsWithCompletion:]_block_invoke.288
- ___76-[DCCredentialStore(DebugAPIs) allElementsOfCredential:authData:completion:]_block_invoke.287
- ___81-[DCCredentialStore(DebugAPIs) clearPresentmentKeyUsageForCredential:completion:]_block_invoke.290
- ___DC_LOG_MILESTONE_LOG_block_invoke
- ___swift_allocate_value_buffer
- ___swift_instantiateGenericMetadata
- ___swift_project_value_buffer
- ___unnamed_2
- __swiftImmortalRefCount
- __swift_stdlib_bridgeErrorToNSError
- __swift_stdlib_malloc_size
- _associated conformance 10CoreIDCred31XPCCredentialPresentmentRequestCAA17XPCValueContainerAA5ValueAaDP_SE
- _associated conformance 10CoreIDCred31XPCCredentialPresentmentRequestCAA17XPCValueContainerAA5ValueAaDP_Se
- _associated conformance 10CoreIDCred8DIPErrorV10Foundation13CustomNSErrorAAs5Error
- _associated conformance 10CoreIDCred8DIPErrorV10Foundation26_ObjectiveCBridgeableErrorAAs0G0
- _associated conformance 10CoreIDCred8DIPErrorV4CodeOSHAASQ
- _block_copy_helper.113
- _block_copy_helper.119
- _block_copy_helper.227
- _block_copy_helper.233
- _block_copy_helper.256
- _block_copy_helper.279
- _block_copy_helper.302
- _block_copy_helper.306
- _block_copy_helper.312
- _block_copy_helper.354
- _block_copy_helper.360
- _block_copy_helper.60
- _block_copy_helper.63
- _block_copy_helper.66
- _block_copy_helper.69
- _block_copy_helper.85
- _block_copy_helper.87
- _block_descriptor.115
- _block_descriptor.121
- _block_descriptor.229
- _block_descriptor.235
- _block_descriptor.258
- _block_descriptor.281
- _block_descriptor.304
- _block_descriptor.308
- _block_descriptor.314
- _block_descriptor.356
- _block_descriptor.362
- _block_descriptor.62
- _block_descriptor.65
- _block_descriptor.68
- _block_descriptor.71
- _block_descriptor.87
- _block_descriptor.89
- _block_destroy_helper.114
- _block_destroy_helper.120
- _block_destroy_helper.228
- _block_destroy_helper.234
- _block_destroy_helper.257
- _block_destroy_helper.280
- _block_destroy_helper.303
- _block_destroy_helper.307
- _block_destroy_helper.313
- _block_destroy_helper.355
- _block_destroy_helper.361
- _block_destroy_helper.61
- _block_destroy_helper.64
- _block_destroy_helper.67
- _block_destroy_helper.70
- _block_destroy_helper.86
- _block_destroy_helper.88
- _free
- _malloc
- _malloc_size
- _memcpy
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$setCreatedAt:
- _objc_msgSend$setCredentialRevocationInfo:
- _objc_msgSend$setDocType:
- _objc_msgSend$setElementIdentifiersByNamespace:
- _objc_msgSend$setFormat:
- _objc_msgSend$setIssuerCertificateChain:
- _objc_msgSend$setIssuingAuthority:
- _objc_msgSend$setIssuingJurisdiction:
- _objc_msgSend$setPayloadData:
- _objc_msgSend$setProtectionType:
- _objc_msgSend$setRegion:
- _objc_msgSend$setSignedAt:
- _objc_msgSend$setUpdatedAt:
- _objc_msgSend$setValidFrom:
- _objc_msgSend$setValidUntil:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x5
- _objectdestroy.147Tm
- _objectdestroy.43Tm
- _objectdestroy.55Tm
- _objectdestroy.76Tm
- _objectdestroy.80Tm
- _swift_allocateGenericClassMetadata
- _swift_bridgeObjectRelease_n
- _swift_coroFrameAlloc
- _swift_deallocClassInstance
- _swift_deletedMethodError
- _swift_errorRetain
- _swift_getErrorValue
- _swift_getGenericMetadata
- _swift_initClassMetadata2
- _swift_once
- _symbolic $s10CoreIDCred17XPCValueContainerP
- _symbolic 5Value_____Qz 10CoreIDCred17XPCValueContainerP
- _symbolic B0
- _symbolic B1
- _symbolic G0R1_
- _symbolic Ieg_
- _symbolic IeyB_
- _symbolic ScCyq_______pG s5ErrorP
- _symbolic So8NSObjectCSg
- _symbolic _____ 10CoreIDCred11BundleToken33_EE8AC1BF542F16A00864CAE0BC17C92BLLC
- _symbolic _____ 10CoreIDCred21SendableXPCConnectionC
- _symbolic _____ 10CoreIDCred8DIPErrorV
- _symbolic _____ 10CoreIDCred8DIPErrorV4CodeO
- _symbolic ______p 10CoreIDCred24DCPresentmentXPCProtocolP
- _symbolic ______pAA_pSgYbc s5ErrorP
- _symbolic ______pSaySo21DCPresentmentProposalCG______pIeghHnrzo_ 10CoreIDCred24DCPresentmentXPCProtocolP s5ErrorP
- _symbolic ______pSg s5ErrorP
- _symbolic ______pSo20DCCredentialResponseC______pIeghHnrzo_ 10CoreIDCred24DCPresentmentXPCProtocolP s5ErrorP
- _symbolic ______p___________pIeghHnrzo_ 10CoreIDCred24DCPresentmentXPCProtocolP 10Foundation4DataV s5ErrorP
- _symbolic ______p______pIeghHnzo_ 10CoreIDCred24DCPresentmentXPCProtocolP s5ErrorP
- _symbolic ______pyt______pIeghHnrzo_ 10CoreIDCred24DCPresentmentXPCProtocolP s5ErrorP
- _symbolic _____ySo15NSXPCConnectionCG 2os21OSAllocatedUnfairLockV
- _symbolic _____ySo15NSXPCConnectionC_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
- _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
- _symbolic _____y______pG 10CoreIDCred21SendableXPCConnectionC AA24DCPresentmentXPCProtocolP
- _symbolic _____yxG 10CoreIDCred21SendableXPCConnectionC
- _symbolic q_
- _symbolic qd__
- _symbolic x
- _symbolic x______pIeghHnzo_ s5ErrorP
- _symbolic xq_______pIeghHnrzo_ s5ErrorP
- _symbolic ytIegr_
- _type_layout_string 10CoreIDCred8DIPErrorV
CStrings:
+ "/Library/Caches/com.apple.xbs/BDB88372-C6EA-4334-9D37-CA9DFBF06FD5/TemporaryDirectory.gVVRor/Sources/CoreIDV_framework/CoreIDCred/Biometric Storage/DCBiometricStoreClient.m"
+ "@136@0:8Q16Q24@32@40@48@56@64@72@80@88@96@104@112@120@128"
+ "@96@0:8@16@24@32@40@48@56Q64@72@80@88"
+ "DCPayloadProperties"
+ "T@\"DCCredentialRevocationInfo\",R,N"
+ "T@\"NSArray\",&,N,V_payloads"
+ "T@\"NSArray\",R,N,V_issuerCertificateChain"
+ "T@\"NSData\",&,N,V_ingestionHash"
+ "T@\"NSData\",R,N"
+ "T@\"NSData\",R,N,V_iconDigest"
+ "T@\"NSData\",R,N,V_payloadData"
+ "T@\"NSDate\",R,N"
+ "T@\"NSDate\",R,N,V_signedAt"
+ "T@\"NSDate\",R,N,V_validFrom"
+ "T@\"NSDate\",R,N,V_validUntil"
+ "T@\"NSDictionary\",R,N,V_elementIdentifiersByNamespace"
+ "T@\"NSString\",&,N,V_documentType"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_issuingAuthority"
+ "TQ,R,N,V_format"
+ "TQ,R,N,V_iconDigestAlgorithm"
+ "TQ,R,N,V_protectionType"
+ "_documentType"
+ "_iconDigest"
+ "_iconDigestAlgorithm"
+ "_ingestionHash"
+ "_payloads"
+ "count"
+ "documentType"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "iconDigest"
+ "iconDigestAlgorithm"
+ "ingestionHash"
+ "initWithCapacity:"
+ "initWithFormat:protectionType:docType:createdAt:updatedAt:validFrom:validUntil:signedAt:elementIdentifiersByNamespace:issuerCertificateChain:region:issuingJurisdiction:issuingAuthority:credentialRevocationInfo:payloadData:"
+ "initWithIdentifier:organization:organizationalUnit:iconData:iconURL:iconDigest:iconDigestAlgorithm:iconMediaType:privacyPolicyURL:merchantCategoryCode:"
+ "payloads"
+ "setDocumentType:"
+ "setIngestionHash:"
+ "setObject:forKeyedSubscript:"
+ "setPayloads:"
+ "v32@?0@\"NSString\"8@\"NSArray\"16^B24"
- " cannot be cast to "
- "/Library/Caches/com.apple.xbs/Sources/CoreIDV_framework/CoreIDCred/Biometric Storage/DCBiometricStoreClient.m"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "DCPresentmentXPCProtocol"
- "Remote proxy object "
- "SendableXPCConnection error occurred when cancelling the task: %@"
- "SendableXPCConnection executing cancellation handler"
- "SendableXPCConnection onCancel is nil"
- "T@\"NSData\",&,N,V_payloadData"
- "T@\"NSData\",&,N,V_payloadIngestionHash"
- "T@\"NSDate\",&,N,V_payloadSignedAt"
- "T@\"NSDate\",&,N,V_payloadValidFrom"
- "T@\"NSDate\",&,N,V_payloadValidUntil"
- "T@\"NSDictionary\",&,N,V_elementIdentifiersByNamespace"
- "T@\"NSString\",&,N,V_docType"
- "TQ,N,V_format"
- "TQ,N,V_protectionType"
- "XPC connection error"
- "XPC connection error: %s"
- "_TtC10CoreIDCredP33_EE8AC1BF542F16A00864CAE0BC17C92B11BundleToken"
- "_connection"
- "_payloadIngestionHash"
- "_payloadSignedAt"
- "_payloadValidFrom"
- "_payloadValidUntil"
- "connectionErrorMapper"
- "domain"
- "exportedObject"
- "initWithIdentifier:organization:organizationalUnit:iconData:iconURL:iconMediaType:privacyPolicyURL:merchantCategoryCode:"
- "initWithListenerEndpoint:"
- "invalidationHandler"
- "performWithRemoteObjectProxy(of:_:)"
- "setDocType:"
- "setElementIdentifiersByNamespace:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFormat:"
- "setInvalidationHandler:"
- "setPayloadData:"
- "setPayloadIngestionHash:"
- "setPayloadSignedAt:"
- "setPayloadValidFrom:"
- "setPayloadValidUntil:"
- "setProtectionType:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "userInfo"

```
