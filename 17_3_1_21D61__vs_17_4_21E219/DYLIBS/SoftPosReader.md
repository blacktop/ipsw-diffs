## SoftPosReader

> `/System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader`

```diff

-21.3.0.0.0
-  __TEXT.__text: 0x2ea4c
-  __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x13cc
-  __TEXT.__const: 0x11f0
-  __TEXT.__cstring: 0x2fb4
-  __TEXT.__oslogstring: 0x47e
+24.12.0.0.0
+  __TEXT.__text: 0x3f920
+  __TEXT.__auth_stubs: 0x1280
+  __TEXT.__objc_methlist: 0x12f4
+  __TEXT.__const: 0x1c88
+  __TEXT.__cstring: 0x34cd
+  __TEXT.__oslogstring: 0x431
   __TEXT.__gcc_except_tab: 0x4d4
-  __TEXT.__constg_swiftt: 0x184
-  __TEXT.__swift5_typeref: 0x16b
-  __TEXT.__swift5_builtin: 0xc8
-  __TEXT.__swift5_reflstr: 0x3b
-  __TEXT.__swift5_fieldmd: 0x38
-  __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x60
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__unwind_info: 0xa68
-  __TEXT.__objc_classname: 0x3d3
-  __TEXT.__objc_methname: 0x3d70
-  __TEXT.__objc_methtype: 0x1276
-  __TEXT.__objc_stubs: 0x1ca0
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x1480
+  __TEXT.__constg_swiftt: 0x46c
+  __TEXT.__swift5_typeref: 0x3a4
+  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_reflstr: 0x167
+  __TEXT.__swift5_fieldmd: 0x1c4
+  __TEXT.__swift5_assocty: 0x128
+  __TEXT.__swift5_proto: 0xc0
+  __TEXT.__swift5_types: 0x5c
+  __TEXT.__swift5_capture: 0x20
+  __TEXT.__unwind_info: 0x16ec
+  __TEXT.__eh_frame: 0x7c8
+  __TEXT.__objc_classname: 0x3cc
+  __TEXT.__objc_methname: 0x416f
+  __TEXT.__objc_methtype: 0x12b6
+  __TEXT.__objc_stubs: 0x19a0
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__const: 0x1510
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2988
-  __DATA_CONST.__objc_selrefs: 0xdc0
-  __AUTH_CONST.__cfstring: 0x1860
-  __AUTH_CONST.__objc_const: 0xfe0
-  __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__auth_got: 0x500
-  __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0x190
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x16c
-  __DATA.__data: 0x860
-  __DATA.__bss: 0xcc8
-  __DATA.__common: 0x2
+  __DATA_CONST.__objc_const: 0x2bc0
+  __DATA_CONST.__objc_selrefs: 0xd38
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x190
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__cfstring: 0x1800
+  __AUTH_CONST.__objc_const: 0xf08
+  __AUTH_CONST.__const: 0xb08
+  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH_CONST.__auth_got: 0x950
+  __AUTH.__objc_data: 0xaa0
+  __AUTH.__data: 0x1b0
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0xba8
+  __DATA.__bss: 0x18e0
+  __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  UUID: 7E218452-B527-3407-A51F-6548D8B37C27
-  Functions: 1196
-  Symbols:   3570
-  CStrings:  1570
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: B719BD59-100B-358F-AFDA-09E150156E94
+  Functions: 1776
+  Symbols:   3666
+  CStrings:  1583
 
Symbols:
+ -[SPRAttestationManager requestTokenWithWarningsAndReturnError:]
+ -[SPRConfigurator prepareAndWarnAndReturnError:]
+ -[SPRConfigurator prepareAndWarnWithForce:error:]
+ -[SPRPINCrypto initWithPeerPublicKey:]
+ -[SPRPINCrypto peerPublicKey]
+ -[SPRPINData initWithPinCipherBlob:pinKeyBlob:casd:pinAppletAttestationData:pinKEKHash:isPinBypass:]
+ -[SPRPINData initWithPinCipherBlob:pinKeyBlob:casd:pinAppletAttestationData:pinKEKHash:isPinBypass:isPinBypassEnabled:]
+ -[SPRPINData isPinBypassEnabled]
+ -[SPRPINData pinCipherBlob]
+ -[SPRPINData pinKeyBlob]
+ -[SPRTransactionData initWithVasResponses:transactionCipherBlob:transactionKeyBlob:network:outcomeStatus:errorIndicationStatusWord:errorIndicationMsgOnError:cvmType:cvmResult:merchantCategoryCode:pinRequired:kernelIdentityKeyAttestation:ecdsaCertificate:transactionResultData:kekId:pinKekId:isPinSupported:languagePreference:transactionId:readError:payAppletFinalStatus:isPINBypassAllowed:forFallback:fallbackAmount:switchInterfaceOrNoCVMSuccess:]
+ -[SPRTransactionData initWithVasResponses:transactionCipherBlob:transactionKeyBlob:network:outcomeStatus:errorIndicationStatusWord:errorIndicationMsgOnError:cvmType:cvmResult:merchantCategoryCode:pinRequired:kernelIdentityKeyAttestation:ecdsaCertificate:transactionResultData:kekId:pinKekId:isPinSupported:languagePreference:transactionId:readError:payAppletFinalStatus:isPINBypassEnabled:isPINBypassAllowed:forFallback:fallbackAmount:switchInterfaceOrNoCVMSuccess:]
+ -[SPRTransactionData isPINBypassEnabled]
+ -[SPRTransactionData transactionCipherBlob]
+ -[SPRTransactionData transactionKeyBlob]
+ GCC_except_table18
+ GCC_except_table31
+ _OBJC_CLASS_$_NSScanner
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_SPRConfigurator._tokenKey
+ _OBJC_IVAR_$_SPRPINData._isPinBypassEnabled
+ _OBJC_IVAR_$_SPRPINData._pinCipherBlob
+ _OBJC_IVAR_$_SPRPINData._pinKeyBlob
+ _OBJC_IVAR_$_SPRTransactionData._isPINBypassEnabled
+ _OBJC_IVAR_$_SPRTransactionData._transactionCipherBlob
+ _OBJC_IVAR_$_SPRTransactionData._transactionKeyBlob
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OUTLINED_FUNCTION_7
+ _SPRCardReaderBlobIsPinBypassEnabled
+ _SPRCardReaderBlobKeyData
+ _SPRCardReaderBlobPinCipherBlob
+ _SPRCardReaderBlobPinData
+ _SPRCardReaderBlobPinKeyBlob
+ _SPRCardReaderBlobTransactionCipherBlob
+ _SPRCardReaderBlobTransactionKeyBlob
+ _SecCertificateCopyData
+ _SecCertificateCopyKey
+ _SecCertificateCreateWithData
+ _SecKeyCreateEncryptedDataWithParameters
+ _SecRandomCopyBytes
+ __DATA__TtC7SPRBase3TLV
+ __IVARS__TtC7SPRBase3TLV
+ __METACLASS_DATA__TtC7SPRBase3TLV
+ __OBJC_$_INSTANCE_METHODS_SPRPINCrypto(SPRPINCryptoSwift)
+ __OBJC_$_PROP_LIST_SPRPINCrypto
+ __Z35SSESetEffacementNotificationHandlerPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFv19SSEEffacementReasonE
+ __Z35SSESetEffacementNotificationHandlerPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFv19SSEEffacementReasonE.cold.1
+ __Z35SSESetEffacementNotificationHandlerU13block_pointerFv19SSEEffacementReasonE
+ __Z42SSESetAuthKeyRevocationNotificationHandlerPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFv26SSEAuthKeyRevocationReasonE
+ __Z42SSESetAuthKeyRevocationNotificationHandlerPU28objcproto17OS_dispatch_queue8NSObjectU13block_pointerFv26SSEAuthKeyRevocationReasonE.cold.1
+ __Z42SSESetAuthKeyRevocationNotificationHandlerU13block_pointerFv26SSEAuthKeyRevocationReasonE
+ ___29-[SPRAttestationManager ping]_block_invoke.15
+ ___29-[SPRAttestationManager stop]_block_invoke.14
+ ___30-[SPRAttestationManager start]_block_invoke.13
+ ___33-[SPRAttestationManager getToken]_block_invoke.9
+ ___38-[SPRAttestationManager isValidToken:]_block_invoke.11
+ ___49-[SPRConfigurator prepareAndWarnWithForce:error:]_block_invoke
+ ___49-[SPRConfigurator prepareAndWarnWithForce:error:]_block_invoke_2
+ ___64-[SPRAttestationManager requestTokenWithWarningsAndReturnError:]_block_invoke
+ ___64-[SPRAttestationManager requestTokenWithWarningsAndReturnError:]_block_invoke_2
+ ___block_literal_global.162
+ ___block_literal_global.167
+ ___block_literal_global.176
+ ___block_literal_global.203
+ ___block_literal_global.210
+ ___chkstk_darwin
+ ___serviceNotificationHandler_block_invoke_3
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy17_8
+ ___swift_memcpy1_1
+ ___swift_memcpy24_8
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ ___swift_project_value_buffer
+ __authKeyRevocationNtfHandler
+ __authKeyRevocationNtfQueue
+ __effacemenNtfQueue
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SPRBase
+ __swift_FORCE_LOAD_$_swiftDarwin_$_SPRBase
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SPRBase
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SPRBase
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SPRBase
+ __swift_FORCE_LOAD_$_swiftXPC_$_SPRBase
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SoftPosReader
+ __swift_stdlib_malloc_size
+ _associated conformance 7SPRBase18LazyPaddedSequenceVyxGSTAA8IteratorST_St
+ _associated conformance 7SPRBase18LazyPaddedSequenceVyxGs0bD8ProtocolAA8ElementssAEP_ST
+ _associated conformance 7SPRBase18LazyPaddedSequenceVyxGs0bD8ProtocolAAST
+ _associated conformance 7SPRBase8TLVErrorOSHAASQ
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation021_ObjectiveCBridgeableB0SCs0B0
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation13CustomNSErrorSCs0B0
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_AC01_bC8Protocol
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_SY
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC021_ObjectiveCBridgeableB0
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomG0
+ _associated conformance SC20SPRSecurityErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC20SPRSecurityErrorCodeLeVSHSCSQ
+ _associated conformance So11CFStringRefa14CoreFoundation9_CFObjectSCSH
+ _associated conformance So11CFStringRefaSHSCSQ
+ _associated conformance So20SPRSecurityErrorCodeV10Foundation01_bC8ProtocolSC01_B4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So20SPRSecurityErrorCodeV10Foundation01_bC8ProtocolSCSQ
+ _kSecKeyEncryptionParameterSymmetricKeySizeInBits
+ _kSecRandomDefault
+ _malloc_size
+ _memcpy
+ _objc_msgSend$prepareAndWarnAndReturnError:
+ _objc_msgSend$prepareAndWarnWithForce:error:
+ _objc_msgSend$prepareAndWarnWithForce:reply:
+ _objc_msgSend$requestTokenWithWarningsAndReturnError:
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_allocateGenericValueMetadata
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_checkMetadataState
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_deletedMethodError
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_getGenericMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_initStackObject
+ _swift_initStructMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic $sST
+ _symbolic $sSt
+ _symbolic $ss20LazySequenceProtocolP
+ _symbolic 7ElementSTQz
+ _symbolic 8IteratorSTQz
+ _symbolic SaySsG
+ _symbolic SaySuG
+ _symbolic Say_____G 7SPRBase3TLVC
+ _symbolic Say_____G s5UInt8V
+ _symbolic Say_____GSg 7SPRBase3TLVC
+ _symbolic Sb
+ _symbolic Su
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 7SPRBase10TLVScannerV
+ _symbolic _____ 7SPRBase18LazyPaddedSequenceV
+ _symbolic _____ 7SPRBase18LazyPaddedSequenceV8IteratorV
+ _symbolic _____ 7SPRBase3OIDV
+ _symbolic _____ 7SPRBase3TLVC
+ _symbolic _____ 7SPRBase6TLVTagV
+ _symbolic _____ 7SPRBase8TLVErrorO
+ _symbolic _____ 7SPRBase9BitStringV
+ _symbolic _____ SC20SPRSecurityErrorCodeLeV
+ _symbolic _____ SS5IndexV
+ _symbolic _____ So20SPRSecurityErrorCodeV
+ _symbolic _____ s5UInt8V
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg So11CFStringRefa
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______pSg 10Foundation15ContiguousBytesP
+ _symbolic ______ypt So11CFStringRefa
+ _symbolic _____ySay_____GG s18ReversedCollectionV s5UInt8V
+ _symbolic _____ySiG s23_ContiguousArrayStorageC
+ _symbolic _____ySsG s23_ContiguousArrayStorageC
+ _symbolic _____ySuG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G s15CollectionOfOneV s5UInt8V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____SgSiG s18_DictionaryStorageC So11CFStringRefa
+ _symbolic _____y_____Sg_SitG s23_ContiguousArrayStorageC So11CFStringRefa
+ _symbolic _____y______pG s23_ContiguousArrayStorageC s7CVarArgP
+ _symbolic _____y______yptG s23_ContiguousArrayStorageC So11CFStringRefa
+ _symbolic _____y_____ypG s18_DictionaryStorageC So11CFStringRefa
+ _symbolic _____yxG 7SPRBase18LazyPaddedSequenceV
+ _symbolic _____yx_G 7SPRBase18LazyPaddedSequenceV8IteratorV
+ _symbolic x
- +[SPRPINCrypto verifySignature:onRequest:usingKey:error:]
- +[SPRTLV TLVSsWithBytes:length:requireDefiniteEncoding:]
- +[SPRTLV TLVWithData:simple:]
- +[SPRTLV TLVWithTag:children:]
- +[SPRTLV TLVWithTag:fromData:]
- +[SPRTLV TLVWithTag:unsignedChar:]
- +[SPRTLV TLVWithTag:unsignedLongValue:]
- +[SPRTLV TLVWithTag:value:]
- +[SPRTLV TLVsWithData:]
- +[SPRTLV TLVsWithData:requireDefiniteEncoding:]
- +[SPRTLV _intToData:]
- +[SPRTLV _parseTLVs:end:simple:definite:]
- +[SPRTLV scanData:forTag:]
- +[SPRTLV simpleTLVsWithData:]
- +[SPRTLV simpleTLVsWithTag:fromData:]
- -[SPRPINCrypto encryptDigit:error:]
- -[SPRPINCrypto initWithAttestationData:casdCertificate:error:]
- -[SPRTLV .cxx_destruct]
- -[SPRTLV asData]
- -[SPRTLV asMutableData]
- -[SPRTLV childWithTag:]
- -[SPRTLV childrenWithTag:]
- -[SPRTLV children]
- -[SPRTLV containsTag:]
- -[SPRTLV containsValue:]
- -[SPRTLV description]
- -[SPRTLV tag]
- -[SPRTLV valueAsHexString]
- -[SPRTLV valueAsString]
- -[SPRTLV valueAsUnsignedLongLong]
- -[SPRTLV valueAsUnsignedLong]
- -[SPRTLV valueAsUnsignedShort]
- -[SPRTLV value]
- GCC_except_table24
- GCC_except_table3
- GCC_except_table30
- _OBJC_CLASS_$_SPRTLV
- _OBJC_IVAR_$_SPRTLV._children
- _OBJC_IVAR_$_SPRTLV._tag
- _OBJC_IVAR_$_SPRTLV._value
- _OBJC_METACLASS_$_SPRTLV
- _SSESetEffacementNotificationHandler
- _SSESetEffacementNotificationHandler.cold.1
- _SecKeyCreateEncryptedData
- __OBJC_$_CLASS_METHODS_SPRPINCrypto
- __OBJC_$_CLASS_METHODS_SPRTLV
- __OBJC_$_INSTANCE_METHODS_SPRPINCrypto
- __OBJC_$_INSTANCE_METHODS_SPRTLV
- __OBJC_$_INSTANCE_VARIABLES_SPRTLV
- __OBJC_$_PROP_LIST_SPRTLV
- __OBJC_CLASS_RO_$_SPRTLV
- __OBJC_METACLASS_RO_$_SPRTLV
- ___29-[SPRAttestationManager ping]_block_invoke.12
- ___29-[SPRAttestationManager stop]_block_invoke.11
- ___30-[SPRAttestationManager start]_block_invoke.10
- ___33-[SPRAttestationManager getToken]_block_invoke.6
- ___38-[SPRAttestationManager isValidToken:]_block_invoke.8
- ___42-[SPRConfigurator prepareWithForce:error:]_block_invoke
- ___42-[SPRConfigurator prepareWithForce:error:]_block_invoke_2
- ___52-[SPRAttestationManager requestTokenAndReturnError:]_block_invoke
- ___52-[SPRAttestationManager requestTokenAndReturnError:]_block_invoke_2
- ___block_literal_global.161
- ___block_literal_global.166
- ___block_literal_global.175
- ___block_literal_global.202
- ___block_literal_global.209
- _objc_msgSend$TLVWithTag:children:
- _objc_msgSend$TLVWithTag:value:
- _objc_msgSend$TLVsWithData:
- _objc_msgSend$_intToData:
- _objc_msgSend$_parseTLVs:end:simple:definite:
- _objc_msgSend$appendBytes:length:
- _objc_msgSend$asData
- _objc_msgSend$asMutableData
- _objc_msgSend$children
- _objc_msgSend$containsTag:
- _objc_msgSend$containsValue:
- _objc_msgSend$data
- _objc_msgSend$dataWithCapacity:
- _objc_msgSend$initWithDERRepresentation:error:
- _objc_msgSend$isEqualToData:
- _objc_msgSend$lastObject
- _objc_msgSend$prepareWithForce:error:
- _objc_msgSend$prepareWithForce:reply:
- _objc_msgSend$publicKeyInfo
- _objc_msgSend$request
- _objc_msgSend$resetBytesInRange:
- _objc_msgSend$scanData:forTag:
- _objc_msgSend$signature
- _objc_msgSend$simpleTLVsWithData:
- _objc_msgSend$subdataWithRange:
- _objc_msgSend$tag
- _objc_msgSend$value
- _objc_msgSend$verifySignature:onRequest:usingKey:error:
CStrings:
+ "\x16"
+ " "
+ "-----BEGIN CERTIFICATE-----"
+ "-----BEGIN CERTIFICATE-----\n"
+ "-----END CERTIFICATE-----"
+ "/\x11"
+ "@180@0:8@16@24@32@40C48@52C60C64@68@76B84@88@96@104@112@120B128@132@140q148C156B160B164@168B176"
+ "@184@0:8@16@24@32@40C48@52C60C64@68@76B84@88@96@104@112@120B128@132@140q148C156B160B164B168@172B180"
+ "@24@0:8^{__SecKey=}16"
+ "@60@0:8@16@24@32@40@48B56"
+ "@64@0:8@16@24@32@40@48B56B60"
+ "CASD certificate has unexpected format"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "SPRPINCrypto.encryptDigit(_:)"
+ "SPRPINCrypto.init(attestationData: %s, casdCertificate: %s)"
+ "SPRPINCrypto.verify(signature:request:key:)"
+ "SPRPINCryptoSwift"
+ "SecKeyCreateEncryptedData error: %s"
+ "SecKeyCreateFromSubjectPublicKeyInfoData on attestationInfo.request.publicKeyInfo failed"
+ "SecKeyCreateWithData error: %s"
+ "SecKeyVerifySignature error: %s"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSData\",R,C,N,V_pinCipherBlob"
+ "T@\"NSData\",R,C,N,V_pinKeyBlob"
+ "T@\"NSData\",R,C,N,V_transactionCipherBlob"
+ "T@\"NSData\",R,C,N,V_transactionKeyBlob"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_isPINBypassEnabled"
+ "TB,R,N,V_isPinBypassEnabled"
+ "T^{__SecKey=},R,N,V_peerPublicKey"
+ "Tue Feb  6 20:24:05 2024"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Vv28@0:8B16@?<v@?@\"NSDictionary\"@\"NSError\">20"
+ "^{__SecKey=}"
+ "^{__SecKey=}16@0:8"
+ "_TtC7SPRBase3TLV"
+ "_dataRepresentation"
+ "_isPINBypassEnabled"
+ "_isPinBypassEnabled"
+ "_pinCipherBlob"
+ "_pinKeyBlob"
+ "_tokenKey"
+ "_transactionCipherBlob"
+ "_transactionKeyBlob"
+ "casdPublicKeyData: %s"
+ "com.apple.softposreader"
+ "empty"
+ "initWithBase64EncodedString:options:"
+ "initWithPeerPublicKey:"
+ "initWithPinCipherBlob:pinKeyBlob:casd:pinAppletAttestationData:pinKEKHash:isPinBypass:"
+ "initWithPinCipherBlob:pinKeyBlob:casd:pinAppletAttestationData:pinKEKHash:isPinBypass:isPinBypassEnabled:"
+ "initWithString:"
+ "initWithVasResponses:transactionCipherBlob:transactionKeyBlob:network:outcomeStatus:errorIndicationStatusWord:errorIndicationMsgOnError:cvmType:cvmResult:merchantCategoryCode:pinRequired:kernelIdentityKeyAttestation:ecdsaCertificate:transactionResultData:kekId:pinKekId:isPinSupported:languagePreference:transactionId:readError:payAppletFinalStatus:isPINBypassAllowed:forFallback:fallbackAmount:switchInterfaceOrNoCVMSuccess:"
+ "initWithVasResponses:transactionCipherBlob:transactionKeyBlob:network:outcomeStatus:errorIndicationStatusWord:errorIndicationMsgOnError:cvmType:cvmResult:merchantCategoryCode:pinRequired:kernelIdentityKeyAttestation:ecdsaCertificate:transactionResultData:kekId:pinKekId:isPinSupported:languagePreference:transactionId:readError:payAppletFinalStatus:isPINBypassEnabled:isPINBypassAllowed:forFallback:fallbackAmount:switchInterfaceOrNoCVMSuccess:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isAtEnd"
+ "isPINBypassEnabled"
+ "isPinBypassEnabled"
+ "peerPublicKey"
+ "pinCipherBlob"
+ "pinData"
+ "pinKeyBlob"
+ "prepareAndWarnAndReturnError:"
+ "prepareAndWarnWithForce:error:"
+ "prepareAndWarnWithForce:reply:"
+ "requestTokenWithWarningsAndReturnError:"
+ "scannedForChildren"
+ "setCharactersToBeSkipped:"
+ "token"
+ "transactionCipherBlob"
+ "transactionKeyBlob"
+ "{vasResponses: %@, transactionCipherBlob: %@, transactionKeyBlob: %@, network(50): %@, outcomeStatus: 0x%02X, errorIndicationStatusWord: %@, errorIndicationMsgOnError: 0x%02X, cvmType: 0x%02X, cvmResult(9F34): %@, merchantCategoryCode(9F15): %@, pinRequired: %@, transactionResultData(DF81FE): %@, isPinSupported: %@, languagePreference(5F2D): %@, readError: %ld, payAppletFinalStatus: 0x%02X, isPINBypassEnabled: %@, isPINBypassAllowed: %@, forFallback: %@, fallbackAmount: %@, switchInterfaceOrNoCVMSuccess: %@}"
+ "{vasResponses=%@, transactionCipherBlob=%@, transactionKeyBlob=%@, network(50)=%@, outcomeStatus=0x%02X, errorIndicationStatusWord=%@, errorIndicationMsgOnError=0x%02X, cvmType=0x%02X, cvmResult(9F34)=%@, merchantCategoryCode(9F15)=%@, pinRequired=%@, kernelIdentityKeyAttestation=%@, ecdsaCertificate=%@, transactionResultData(DF81FE)=%@, kekId=%@, pinKekId=%@, isPinSupported=%@, languagePreference(5F2D)=%@, transactionId=%@, readError=%ld, payAppletFinalStatus=0x%02X, isPINBypassEnabled=%@, isPINBypassAllowed=%@, forFallback=%@, fallbackAmount=%@, switchInterfaceOrNoCVMSuccess=%@}"
- "\x14"
- "%@ %02x : %@"
- "%@ %02x = %@"
- "%@ %02x = %@ \"%@\""
- "%@.encryptDigit(*)"
- "-\x11"
- "@20@0:8I16"
- "@24@0:8I16C20"
- "@24@0:8I16I20"
- "@28@0:8@16B24"
- "@28@0:8@16I24"
- "@28@0:8I16@20"
- "@36@0:8r^v16Q24B32"
- "@40@0:8r^*16r*24B32B36"
- "B20@0:8I16"
- "CASD certificate"
- "Fri Sep 29 13:36:22 2023"
- "More than one TLV detected"
- "No TLV detected"
- "Require definite encoding, but got zero tag and len"
- "SPRPINCrypto.init(attestationData:%@, casdCertificate:%@)"
- "SPRTLV"
- "SecKeyCreateEncryptedData"
- "SecKeyCreateWithData"
- "SecKeyVerifySignature"
- "T@\"NSArray\",R,N"
- "T@\"NSData\",R,N"
- "TI,R,N"
- "TLVSsWithBytes:length:requireDefiniteEncoding:"
- "TLVWithData:simple:"
- "TLVWithTag:children:"
- "TLVWithTag:fromData:"
- "TLVWithTag:unsignedChar:"
- "TLVWithTag:unsignedLongValue:"
- "TLVWithTag:value:"
- "TLVsWithData:"
- "TLVsWithData:requireDefiniteEncoding:"
- "Underflow: tag=0x%x"
- "Value too large: %@"
- "Vv24@0:8@?<v@?@\"NSString\"@\"NSError\">16"
- "Vv28@0:8B16@?<v@?@\"NSString\"@\"NSError\">20"
- "[SPRTLV TLVWithTag:children:] failed!"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
- "_intToData:"
- "_parseTLVs:end:simple:definite:"
- "_tag"
- "appendBytes:length:"
- "asData"
- "asMutableData"
- "attestated public key"
- "childWithTag:"
- "children"
- "childrenWithTag:"
- "containsTag:"
- "containsValue:"
- "data"
- "dataWithCapacity:"
- "isEqualToData:"
- "lastObject"
- "prepareWithForce:reply:"
- "resetBytesInRange:"
- "scanData:forTag:"
- "simpleTLVsWithData:"
- "simpleTLVsWithTag:fromData:"
- "subdataWithRange:"
- "value"
- "valueAsHexString"
- "valueAsString"
- "valueAsUnsignedLong"
- "valueAsUnsignedLongLong"
- "valueAsUnsignedShort"
- "verifySignature:onRequest:usingKey:error:"
- "{vasResponses: %@, cardHolderData(DF81FF): %@, network(50): %@, outcomeStatus: 0x%02X, errorIndicationStatusWord: %@, errorIndicationMsgOnError: 0x%02X, cvmType: 0x%02X, cvmResult(9F34): %@, merchantCategoryCode(9F15): %@, pinRequired: %@, transactionResultData(DF81FE): %@, isPinSupported: %@, languagePreference(5F2D): %@, readError: %ld, payAppletFinalStatus: 0x%02X, isPINBypassAllowed: %@, forFallback: %@, fallbackAmount: %@, switchInterfaceOrNoCVMSuccess: %@}"
- "{vasResponses=%@, cardHolderData(DF81FF)=%@, network(50)=%@, outcomeStatus=0x%02X, errorIndicationStatusWord=%@, errorIndicationMsgOnError=0x%02X, cvmType=0x%02X, cvmResult(9F34)=%@, merchantCategoryCode(9F15)=%@, pinRequired=%@, kernelIdentityKeyAttestation=%@, ecdsaCertificate=%@, transactionResultData(DF81FE)=%@, kekId=%@, pinKekId=%@, isPinSupported=%@, languagePreference(5F2D)=%@, transactionId=%@, readError=%ld, payAppletFinalStatus=0x%02X, isPINBypassAllowed=%@ forFallback=%@, fallbackAmount=%@, switchInterfaceOrNoCVMSuccess=%@}"

```
