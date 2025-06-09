## CryptoKitPrivate

> `/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate`

```diff

-241.120.2.0.0
-  __TEXT.__text: 0x84d38
-  __TEXT.__auth_stubs: 0x1da0
-  __TEXT.__objc_methlist: 0x8e4
-  __TEXT.__const: 0x4c70
-  __TEXT.__cstring: 0x22a5
-  __TEXT.__swift5_typeref: 0x1157
-  __TEXT.__swift5_reflstr: 0x1a5d
-  __TEXT.__swift5_assocty: 0x2e0
-  __TEXT.__constg_swiftt: 0x1bd4
-  __TEXT.__swift5_fieldmd: 0x1d7c
+324.0.2.0.0
+  __TEXT.__text: 0x8c530
+  __TEXT.__auth_stubs: 0x1ed0
+  __TEXT.__objc_methlist: 0x994
+  __TEXT.__const: 0x4bd0
+  __TEXT.__cstring: 0x2305
+  __TEXT.__swift5_typeref: 0x134a
+  __TEXT.__swift5_reflstr: 0x1c2b
+  __TEXT.__swift5_assocty: 0x2f8
+  __TEXT.__constg_swiftt: 0x1dc0
+  __TEXT.__swift5_fieldmd: 0x2060
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_proto: 0x27c
-  __TEXT.__swift5_types: 0x240
-  __TEXT.__swift5_capture: 0x40
+  __TEXT.__swift5_proto: 0x280
+  __TEXT.__swift5_types: 0x260
   __TEXT.__swift5_protos: 0x28
+  __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1a30
-  __TEXT.__eh_frame: 0x4e50
-  __TEXT.__objc_classname: 0x19a
-  __TEXT.__objc_methname: 0x1114
-  __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__objc_stubs: 0x780
-  __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0xf0
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__unwind_info: 0x1998
+  __TEXT.__eh_frame: 0x4648
+  __TEXT.__objc_classname: 0x1a9
+  __TEXT.__objc_methname: 0x1364
+  __TEXT.__objc_methtype: 0x4ad
+  __TEXT.__objc_stubs: 0x7e0
+  __DATA_CONST.__got: 0x4b0
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x408
-  __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xed8
-  __AUTH_CONST.__const: 0x3338
-  __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x1d08
-  __AUTH.__objc_data: 0xd8
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0x7c
-  __DATA.__data: 0x1170
-  __DATA.__bss: 0x4280
-  __DATA.__common: 0xf8
-  __DATA_DIRTY.__objc_data: 0xfd8
-  __DATA_DIRTY.__data: 0xfa0
-  __DATA_DIRTY.__common: 0x20
-  __DATA_DIRTY.__bss: 0x800
+  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_superrefs: 0x78
+  __AUTH_CONST.__auth_got: 0xf70
+  __AUTH_CONST.__const: 0x3490
+  __AUTH_CONST.__cfstring: 0x80
+  __AUTH_CONST.__objc_const: 0x1f58
+  __AUTH.__objc_data: 0x860
+  __AUTH.__data: 0x2f8
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__data: 0x17a0
+  __DATA.__bss: 0x4b00
+  __DATA.__common: 0x100
+  __DATA_DIRTY.__objc_data: 0x9a0
+  __DATA_DIRTY.__data: 0xd58
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 12DD86F7-7FB3-38B4-BC1A-A46442D14CF9
-  Functions: 2008
-  Symbols:   1356
-  CStrings:  456
+  UUID: 6EF3AD8F-D083-3308-988E-90FC699B67BF
+  Functions: 2067
+  Symbols:   1406
+  CStrings:  487
 
Symbols:
+ -[ARCAwaitingActivation .cxx_destruct]
+ -[ARCAwaitingActivation activateWithResponseData:error:]
+ -[ARCAwaitingActivation initWithRequestContext:serverPublicKey:error:]
+ -[ARCAwaitingActivation precredential]
+ -[ARCAwaitingActivation requestData]
+ -[ARCCredential .cxx_destruct]
+ -[ARCCredential credential]
+ -[ARCCredential getCredentialDataError:]
+ -[ARCCredential getRemainingPresentationCountWithPresentationContext:presentationLimit:error:]
+ -[ARCCredential initWithCredentialData:error:]
+ -[ARCCredential initWithCredentialResponseData:precredential:error:]
+ -[ARCCredential presentWithPresentationContext:presentationLimit:error:]
+ -[ARCPresentation .cxx_destruct]
+ -[ARCPresentation initWithCredential:presentationContext:presentationLimit:error:]
+ -[ARCPresentation nonce]
+ -[ARCPresentation presentationData]
+ -[ARCPresentation presentation]
+ -[ARCResponse .cxx_destruct]
+ -[ARCResponse initWithResponseData:]
+ -[ARCResponse responseData]
+ -[ARCTestServer .cxx_destruct]
+ -[ARCTestServer getServerPublicKey]
+ -[ARCTestServer init]
+ -[ARCTestServer respondWithRequestData:error:]
+ -[ARCTestServer server]
+ -[ARCTestServer verifyWithPresentationData:nonce:requestContext:presentationContext:presentationLimit:]
+ -[ATHMAwaitingActivation activateWithResponseData:nbuckets:error:]
+ -[ATHMPresentation .cxx_destruct]
+ -[ATHMPresentation initWithClient:responseData:nbuckets:error:]
+ -[ATHMPresentation nbuckets]
+ -[ATHMPresentation presentationData]
+ -[ATHMTestServer readMetadataWithPresentationData:nbuckets:error:]
+ -[ATHMTestServer respondWithRequestData:metadata:nbuckets:error:]
+ _OBJC_CLASS_$_ARCAwaitingActivation
+ _OBJC_CLASS_$_ARCCredential
+ _OBJC_CLASS_$_ARCPresentation
+ _OBJC_CLASS_$_ARCResponse
+ _OBJC_CLASS_$_ARCTestServer
+ _OBJC_CLASS_$_ATHMPresentation
+ _OBJC_CLASS_$__TtC16CryptoKitPrivate20ARCCredentialWrapper
+ _OBJC_CLASS_$__TtC16CryptoKitPrivate22ARCPresentationWrapper
+ _OBJC_CLASS_$__TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper
+ _OBJC_CLASS_$__TtC16CryptoKitPrivate9ARCServer
+ _OBJC_IVAR_$_ARCAwaitingActivation._precredential
+ _OBJC_IVAR_$_ARCAwaitingActivation._requestData
+ _OBJC_IVAR_$_ARCCredential._credential
+ _OBJC_IVAR_$_ARCPresentation._nonce
+ _OBJC_IVAR_$_ARCPresentation._presentation
+ _OBJC_IVAR_$_ARCPresentation._presentationData
+ _OBJC_IVAR_$_ARCResponse._responseData
+ _OBJC_IVAR_$_ARCTestServer._server
+ _OBJC_IVAR_$_ATHMPresentation._nbuckets
+ _OBJC_IVAR_$_ATHMPresentation._presentationData
+ _OBJC_METACLASS_$_ARCAwaitingActivation
+ _OBJC_METACLASS_$_ARCCredential
+ _OBJC_METACLASS_$_ARCPresentation
+ _OBJC_METACLASS_$_ARCResponse
+ _OBJC_METACLASS_$_ARCTestServer
+ _OBJC_METACLASS_$_ATHMPresentation
+ _OBJC_METACLASS_$__TtC16CryptoKitPrivate20ARCCredentialWrapper
+ _OBJC_METACLASS_$__TtC16CryptoKitPrivate22ARCPresentationWrapper
+ _OBJC_METACLASS_$__TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper
+ _OBJC_METACLASS_$__TtC16CryptoKitPrivate9ARCServer
+ _SPAKE2GetSessionKey
+ __DATA__TtC16CryptoKitPrivate20ARCCredentialWrapper
+ __DATA__TtC16CryptoKitPrivate22ARCPresentationWrapper
+ __DATA__TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper
+ __DATA__TtC16CryptoKitPrivate9ARCServer
+ __INSTANCE_METHODS__TtC16CryptoKitPrivate20ARCCredentialWrapper
+ __INSTANCE_METHODS__TtC16CryptoKitPrivate22ARCPresentationWrapper
+ __INSTANCE_METHODS__TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper
+ __INSTANCE_METHODS__TtC16CryptoKitPrivate9ARCServer
+ __IVARS__TtC16CryptoKitPrivate20ARCCredentialWrapper
+ __IVARS__TtC16CryptoKitPrivate22ARCPresentationWrapper
+ __IVARS__TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper
+ __IVARS__TtC16CryptoKitPrivate9ARCServer
+ __METACLASS_DATA__TtC16CryptoKitPrivate20ARCCredentialWrapper
+ __METACLASS_DATA__TtC16CryptoKitPrivate22ARCPresentationWrapper
+ __METACLASS_DATA__TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper
+ __METACLASS_DATA__TtC16CryptoKitPrivate9ARCServer
+ __OBJC_$_INSTANCE_METHODS_ARCAwaitingActivation
+ __OBJC_$_INSTANCE_METHODS_ARCCredential
+ __OBJC_$_INSTANCE_METHODS_ARCPresentation
+ __OBJC_$_INSTANCE_METHODS_ARCResponse
+ __OBJC_$_INSTANCE_METHODS_ARCTestServer
+ __OBJC_$_INSTANCE_METHODS_ATHMPresentation
+ __OBJC_$_INSTANCE_VARIABLES_ARCAwaitingActivation
+ __OBJC_$_INSTANCE_VARIABLES_ARCCredential
+ __OBJC_$_INSTANCE_VARIABLES_ARCPresentation
+ __OBJC_$_INSTANCE_VARIABLES_ARCResponse
+ __OBJC_$_INSTANCE_VARIABLES_ARCTestServer
+ __OBJC_$_INSTANCE_VARIABLES_ATHMPresentation
+ __OBJC_$_PROP_LIST_ARCAwaitingActivation
+ __OBJC_$_PROP_LIST_ARCCredential
+ __OBJC_$_PROP_LIST_ARCPresentation
+ __OBJC_$_PROP_LIST_ARCResponse
+ __OBJC_$_PROP_LIST_ARCTestServer
+ __OBJC_$_PROP_LIST_ATHMPresentation
+ __OBJC_CLASS_RO_$_ARCAwaitingActivation
+ __OBJC_CLASS_RO_$_ARCCredential
+ __OBJC_CLASS_RO_$_ARCPresentation
+ __OBJC_CLASS_RO_$_ARCResponse
+ __OBJC_CLASS_RO_$_ARCTestServer
+ __OBJC_CLASS_RO_$_ATHMPresentation
+ __OBJC_METACLASS_RO_$_ARCAwaitingActivation
+ __OBJC_METACLASS_RO_$_ARCCredential
+ __OBJC_METACLASS_RO_$_ARCPresentation
+ __OBJC_METACLASS_RO_$_ARCResponse
+ __OBJC_METACLASS_RO_$_ARCTestServer
+ __OBJC_METACLASS_RO_$_ATHMPresentation
+ ___swift_get_extra_inhabitant_indexTm
+ ___swift_store_extra_inhabitant_indexTm
+ ___unnamed_3
+ ___unnamed_7
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CryptoKitPrivate
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CryptoKitPrivate
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CryptoKitPrivate
+ _associated conformance 16CryptoKitPrivate3ARCO6ErrorsOSHAASQ
+ _associated conformance 16CryptoKitPrivate6ProverVyxGAA16ProofParticipantAA5PointAaEP_AA12GroupElement
+ _objc_msgSend$finalizeWithResponseData:nbuckets:error:
+ _objc_msgSend$getNonce
+ _objc_msgSend$getPresentationData
+ _objc_msgSend$getRemainingPresentationCountWithPresentationContext:presentationLimit:
+ _objc_msgSend$getServerPublicKey
+ _objc_msgSend$initWithClient:responseData:nbuckets:error:
+ _objc_msgSend$initWithCredential:presentationContext:presentationLimit:error:
+ _objc_msgSend$initWithCredentialResponseData:precredential:error:
+ _objc_msgSend$initWithRequestContext:serverPublicKeyData:error:
+ _objc_msgSend$makePresentationWithPresentationContext:presentationLimit:error:
+ _objc_msgSend$makeRequest
+ _objc_msgSend$readMetadataWithPresentationData:nbuckets:
+ _objc_msgSend$respondWithRequestData:metadata:nbuckets:error:
+ _objc_msgSend$verifyWithPresentationData:nonce:requestContext:presentationContext:presentationLimit:
+ _swift_coroFrameAlloc
+ _swift_unknownObjectRelease_n
+ _symbolic SDy_____Si_ShySiGtG 10Foundation4DataV
+ _symbolic SS_yXlt
+ _symbolic Say1G______7Element_____QZG 16CryptoKitPrivate11HashToGroupP AA0F0P
+ _symbolic SaySSG
+ _symbolic Say______Say______AAtGtG 16CryptoKitPrivate8PointVarV AA06ScalarE0V
+ _symbolic Say_____y_____GG 16CryptoKitPrivate04CoreA11GroupScalarV 0aB04P256O
+ _symbolic Say_____y_____GG 16CryptoKitPrivate04CoreA11GroupScalarV 0aB04P384O
+ _symbolic _____ 16CryptoKitPrivate20ARCCredentialWrapperC
+ _symbolic _____ 16CryptoKitPrivate22ARCPresentationWrapperC
+ _symbolic _____ 16CryptoKitPrivate28ARCAwaitingActivationWrapperC
+ _symbolic _____ 16CryptoKitPrivate3ARCO
+ _symbolic _____ 16CryptoKitPrivate3ARCO06ServerC3KeyV
+ _symbolic _____ 16CryptoKitPrivate3ARCO10CredentialV
+ _symbolic _____ 16CryptoKitPrivate3ARCO11CiphersuiteV
+ _symbolic _____ 16CryptoKitPrivate3ARCO12PresentationV
+ _symbolic _____ 16CryptoKitPrivate3ARCO13ClientSecretsV
+ _symbolic _____ 16CryptoKitPrivate3ARCO13PrecredentialV
+ _symbolic _____ 16CryptoKitPrivate3ARCO15ServerPublicKeyV
+ _symbolic _____ 16CryptoKitPrivate3ARCO17CredentialRequestV
+ _symbolic _____ 16CryptoKitPrivate3ARCO17PresentationStateV
+ _symbolic _____ 16CryptoKitPrivate3ARCO18CredentialResponseV
+ _symbolic _____ 16CryptoKitPrivate3ARCO6ErrorsO
+ _symbolic _____ 16CryptoKitPrivate3ARCO6ServerV
+ _symbolic _____ 16CryptoKitPrivate4ATHMO13ResponseProofV
+ _symbolic _____ 16CryptoKitPrivate4ATHMO13TokenResponseV
+ _symbolic _____ 16CryptoKitPrivate6AesPrgV
+ _symbolic _____ 16CryptoKitPrivate6ProverV
+ _symbolic _____ 16CryptoKitPrivate6SPAKE2O0D6FramerV
+ _symbolic _____ 16CryptoKitPrivate9ARCServerC
+ _symbolic _____ 9CryptoKit3AESO12StreamingCTRV
+ _symbolic _____Sg 16CryptoKitPrivate6SPAKE2O0D6FramerV
+ _symbolic ______yXlt So11CFStringRefa
+ _symbolic _____ySay_____G______G s12Zip2SequenceV8IteratorV s5UInt8V 10Foundation4DataV
+ _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate3ARCO06ServerC3KeyV AA11HashToGroupP AA0I0P AA0I7ElementP
+ _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate3ARCO13ClientSecretsV AA11HashToGroupP AA0I0P AA0I7ElementP
+ _symbolic _____y_____G 16CryptoKitPrivate04CoreA11GroupScalarV 0aB04P256O
+ _symbolic _____y_____G 16CryptoKitPrivate20CorecryptoCurvePointV 0aB04P256O
+ _symbolic _____y_____G 9CryptoKit24HashedAuthenticationCodeV AA6SHA256V
+ _symbolic _____y_____G 9CryptoKit24HashedAuthenticationCodeV AA6SHA384V
+ _symbolic _____y_____G 9CryptoKit24HashedAuthenticationCodeV AA6SHA512V
+ _symbolic _____y_____Si_ShySiGtG s18_DictionaryStorageC 10Foundation4DataV
+ _symbolic _____y______y_____GG 16CryptoKitPrivate3ARCO10CredentialV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate3ARCO11CiphersuiteV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate3ARCO12PresentationV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate3ARCO13PrecredentialV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate3ARCO18CredentialResponseV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate3ARCO6ServerV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO13TokenResponseV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y_____ySay_____G_____GACG s15LazyMapSequenceV s04Zip2C0V s5UInt8V 10Foundation4DataV
+ _symbolic _____y_____ySay_____G_____GAC_G s15LazyMapSequenceV8IteratorV s04Zip2C0V s5UInt8V 10Foundation4DataV
+ _symbolic _____y_____ySay_____G_____GAC_G_Sit s15LazyMapSequenceV8IteratorV s04Zip2C0V s5UInt8V 10Foundation4DataV
+ _symbolic _____y_____y_____GG 16CryptoKitPrivate6ProverV AA04CoreA11HashToCurveV 0aB04P256O
+ _symbolic _____y_____y_____GG 16CryptoKitPrivate6ProverV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y_xG 16CryptoKitPrivate3ARCO11CiphersuiteV
+ _symbolic _____y_xG 16CryptoKitPrivate3ARCO15ServerPublicKeyV
+ _symbolic _____y_xG 16CryptoKitPrivate3ARCO17CredentialRequestV
+ _symbolic _____y_xG 16CryptoKitPrivate4ATHMO13ResponseProofV
+ _type_layout_string 16CryptoKitPrivate11HashToGroupRzlAA3ARCO11CiphersuiteVy_xG
+ _type_layout_string 16CryptoKitPrivate11HashToGroupRzlAA6ProverVyxG
+ _type_layout_string 16CryptoKitPrivate3ARCO17PresentationStateV
- -[ATHMAwaitingActivation activateWithResponseData:error:]
- -[ATHMTestServer readBitWithPresentationData:error:]
- -[ATHMTestServer respondWithRequestData:b:error:]
- -[KVACAwaitingActivation .cxx_destruct]
- -[KVACAwaitingActivation activateWithResponseData:error:]
- -[KVACAwaitingActivation client]
- -[KVACAwaitingActivation initWithRequestContext:serverCommitments:presentationLimit:error:]
- -[KVACAwaitingActivation requestData]
- -[KVACCredential .cxx_destruct]
- -[KVACCredential credential]
- -[KVACCredential getCredentialDataError:]
- -[KVACCredential initWithCredentialData:error:]
- -[KVACCredential initWithCredentialResponseData:client:error:]
- -[KVACCredential presentWithPresentationContext:error:]
- -[KVACPresentation .cxx_destruct]
- -[KVACPresentation initWithCredential:presentationContext:error:]
- -[KVACPresentation presentationData]
- -[KVACResponse .cxx_destruct]
- -[KVACResponse initWithResponseData:]
- -[KVACResponse responseData]
- -[KVACTestServer .cxx_destruct]
- -[KVACTestServer getServerCommitments]
- -[KVACTestServer init]
- -[KVACTestServer respondWithRequestData:error:]
- -[KVACTestServer server]
- -[KVACTestServer verifyWithPresentationData:requestContext:presentationContext:presentationLimit:]
- _OBJC_CLASS_$_KVACAwaitingActivation
- _OBJC_CLASS_$_KVACCredential
- _OBJC_CLASS_$_KVACPresentation
- _OBJC_CLASS_$_KVACResponse
- _OBJC_CLASS_$_KVACTestServer
- _OBJC_CLASS_$__TtC16CryptoKitPrivate10KVACClient
- _OBJC_CLASS_$__TtC16CryptoKitPrivate10KVACServer
- _OBJC_CLASS_$__TtC16CryptoKitPrivate21KVACCredentialWrapper
- _OBJC_IVAR_$_KVACAwaitingActivation._client
- _OBJC_IVAR_$_KVACAwaitingActivation._requestData
- _OBJC_IVAR_$_KVACCredential._credential
- _OBJC_IVAR_$_KVACPresentation._presentationData
- _OBJC_IVAR_$_KVACResponse._responseData
- _OBJC_IVAR_$_KVACTestServer._server
- _OBJC_METACLASS_$_KVACAwaitingActivation
- _OBJC_METACLASS_$_KVACCredential
- _OBJC_METACLASS_$_KVACPresentation
- _OBJC_METACLASS_$_KVACResponse
- _OBJC_METACLASS_$_KVACTestServer
- _OBJC_METACLASS_$__TtC16CryptoKitPrivate10KVACClient
- _OBJC_METACLASS_$__TtC16CryptoKitPrivate10KVACServer
- _OBJC_METACLASS_$__TtC16CryptoKitPrivate21KVACCredentialWrapper
- __DATA__TtC16CryptoKitPrivate10KVACClient
- __DATA__TtC16CryptoKitPrivate10KVACServer
- __DATA__TtC16CryptoKitPrivate21KVACCredentialWrapper
- __INSTANCE_METHODS__TtC16CryptoKitPrivate10KVACClient
- __INSTANCE_METHODS__TtC16CryptoKitPrivate10KVACServer
- __INSTANCE_METHODS__TtC16CryptoKitPrivate21KVACCredentialWrapper
- __IVARS__TtC16CryptoKitPrivate10KVACClient
- __IVARS__TtC16CryptoKitPrivate10KVACServer
- __IVARS__TtC16CryptoKitPrivate21KVACCredentialWrapper
- __METACLASS_DATA__TtC16CryptoKitPrivate10KVACClient
- __METACLASS_DATA__TtC16CryptoKitPrivate10KVACServer
- __METACLASS_DATA__TtC16CryptoKitPrivate21KVACCredentialWrapper
- __OBJC_$_INSTANCE_METHODS_KVACAwaitingActivation
- __OBJC_$_INSTANCE_METHODS_KVACCredential
- __OBJC_$_INSTANCE_METHODS_KVACPresentation
- __OBJC_$_INSTANCE_METHODS_KVACResponse
- __OBJC_$_INSTANCE_METHODS_KVACTestServer
- __OBJC_$_INSTANCE_VARIABLES_KVACAwaitingActivation
- __OBJC_$_INSTANCE_VARIABLES_KVACCredential
- __OBJC_$_INSTANCE_VARIABLES_KVACPresentation
- __OBJC_$_INSTANCE_VARIABLES_KVACResponse
- __OBJC_$_INSTANCE_VARIABLES_KVACTestServer
- __OBJC_$_PROP_LIST_KVACAwaitingActivation
- __OBJC_$_PROP_LIST_KVACCredential
- __OBJC_$_PROP_LIST_KVACPresentation
- __OBJC_$_PROP_LIST_KVACResponse
- __OBJC_$_PROP_LIST_KVACTestServer
- __OBJC_CLASS_RO_$_KVACAwaitingActivation
- __OBJC_CLASS_RO_$_KVACCredential
- __OBJC_CLASS_RO_$_KVACPresentation
- __OBJC_CLASS_RO_$_KVACResponse
- __OBJC_CLASS_RO_$_KVACTestServer
- __OBJC_METACLASS_RO_$_KVACAwaitingActivation
- __OBJC_METACLASS_RO_$_KVACCredential
- __OBJC_METACLASS_RO_$_KVACPresentation
- __OBJC_METACLASS_RO_$_KVACResponse
- __OBJC_METACLASS_RO_$_KVACTestServer
- ___swift_memcpy112_8
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_CryptoKitPrivate
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_CryptoKitPrivate
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_CryptoKitPrivate
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_CryptoKitPrivate
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_CryptoKitPrivate
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_CryptoKitPrivate
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_CryptoKitPrivate
- _associated conformance 16CryptoKitPrivate4KVACO6ErrorsOSHAASQ
- _objc_msgSend$dataUsingEncoding:
- _objc_msgSend$finalizeWithResponseData:error:
- _objc_msgSend$getServerCommitments
- _objc_msgSend$initWithCredential:presentationContext:error:
- _objc_msgSend$initWithCredentialResponseData:client:error:
- _objc_msgSend$initWithRequestContext:serverCommitmentsData:presentationLimit:error:
- _objc_msgSend$makePresentationWithPresentationContext:error:
- _objc_msgSend$makeRequestAndReturnError:
- _objc_msgSend$readBitWithPresentationData:error:
- _objc_msgSend$respondWithRequestData:b:error:
- _objc_msgSend$verifyWithPresentationData:requestContext:presentationContext:presentationLimit:
- _objc_retain_x1
- _objc_retain_x11
- _objc_retain_x9
- _symbolic SDy_____ShySiGG 10Foundation4DataV
- _symbolic ShySiG
- _symbolic _____ 16CryptoKitPrivate10KVACClientC
- _symbolic _____ 16CryptoKitPrivate10KVACServerC
- _symbolic _____ 16CryptoKitPrivate21KVACCredentialWrapperC
- _symbolic _____ 16CryptoKitPrivate4KVACO
- _symbolic _____ 16CryptoKitPrivate4KVACO10CredentialV
- _symbolic _____ 16CryptoKitPrivate4KVACO11CiphersuiteV
- _symbolic _____ 16CryptoKitPrivate4KVACO13ClientSecretsV
- _symbolic _____ 16CryptoKitPrivate4KVACO13ServerSecretsV
- _symbolic _____ 16CryptoKitPrivate4KVACO17CredentialRequestV
- _symbolic _____ 16CryptoKitPrivate4KVACO17ServerCommitmentsV
- _symbolic _____ 16CryptoKitPrivate4KVACO6ClientV
- _symbolic _____ 16CryptoKitPrivate4KVACO6ErrorsO
- _symbolic _____ 16CryptoKitPrivate4KVACO6ServerV
- _symbolic _____ 16CryptoKitPrivate6AesRngV
- _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate4KVACO13ClientSecretsV AA11HashToGroupP AA0I0P AA0I7ElementP
- _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate4KVACO13ServerSecretsV AA11HashToGroupP AA0I0P AA0I7ElementP
- _symbolic _____y_____G1C_AC1Dt 16CryptoKitPrivate20CorecryptoCurvePointV 0aB04P384O
- _symbolic _____y_____ShySiGG s18_DictionaryStorageC 10Foundation4DataV
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO10CredentialV AA04CoreA11HashToCurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO6ClientV AA04CoreA11HashToCurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO6ServerV AA04CoreA11HashToCurveV 0aB04P384O
- _symbolic _____y_xG 16CryptoKitPrivate4KVACO11CiphersuiteV
- _symbolic _____y_xG 16CryptoKitPrivate4KVACO17CredentialRequestV
- _symbolic _____y_xG 16CryptoKitPrivate4KVACO17ServerCommitmentsV
- _type_layout_string 16CryptoKitPrivate11HashToGroupRzlAA4KVACO11CiphersuiteVy_xG
- _type_layout_string 16CryptoKitPrivate6SPAKE2O6ProverV
CStrings:
+ "@\"_TtC16CryptoKitPrivate20ARCCredentialWrapper\""
+ "@\"_TtC16CryptoKitPrivate22ARCPresentationWrapper\""
+ "@\"_TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper\""
+ "@\"_TtC16CryptoKitPrivate9ARCServer\""
+ "@40@0:8@16Q24^@32"
+ "@40@0:8@16q24^@32"
+ "@48@0:8@16q24q32^@40"
+ "ARC.error"
+ "ARCAwaitingActivation"
+ "ARCCredential"
+ "ARCPresentation"
+ "ARCResponse"
+ "ARCTestServer"
+ "ATHMPresentation"
+ "B56@0:8@16Q24@32@40Q48"
+ "B56@0:8@16q24@32@40q48"
+ "CredentialPresentation"
+ "CredentialRequest"
+ "CredentialResponse"
+ "CryptoKitPrivate.ARCAwaitingActivationWrapper"
+ "CryptoKitPrivate.ARCCredentialWrapper"
+ "CryptoKitPrivate.ARCPresentationWrapper"
+ "CryptoKitPrivate/ARCBridging.swift"
+ "CryptoKitPrivate/AesPrg.swift"
+ "Q16@0:8"
+ "T@\"_TtC16CryptoKitPrivate20ARCCredentialWrapper\",R,&,N,V_credential"
+ "T@\"_TtC16CryptoKitPrivate22ARCPresentationWrapper\",R,&,N,V_presentation"
+ "T@\"_TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper\",R,N,V_precredential"
+ "T@\"_TtC16CryptoKitPrivate9ARCServer\",R,N,V_server"
+ "TQ,R,N,V_nbuckets"
+ "TQ,R,N,V_nonce"
+ "_TtC16CryptoKitPrivate20ARCCredentialWrapper"
+ "_TtC16CryptoKitPrivate22ARCPresentationWrapper"
+ "_TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper"
+ "_TtC16CryptoKitPrivate9ARCServer"
+ "_nbuckets"
+ "_nonce"
+ "_precredential"
+ "_presentation"
+ "activateWithResponseData:nbuckets:error:"
+ "finalizeWithResponseData:nbuckets:error:"
+ "getNonce"
+ "getPresentationData"
+ "getRemainingPresentationCountWithPresentationContext:presentationLimit:"
+ "getRemainingPresentationCountWithPresentationContext:presentationLimit:error:"
+ "getServerPublicKey"
+ "initWithClient:responseData:nbuckets:error:"
+ "initWithCredential:presentationContext:presentationLimit:error:"
+ "initWithCredentialResponseData:precredential:error:"
+ "initWithPresentationData:nonce:error:"
+ "initWithRequestContext:serverPublicKey:error:"
+ "initWithRequestContext:serverPublicKeyData:error:"
+ "makePresentationWithPresentationContext:presentationLimit:error:"
+ "makeRequest"
+ "nbuckets"
+ "precredential"
+ "presentWithPresentationContext:presentationLimit:error:"
+ "presentation"
+ "q16@0:8"
+ "q32@0:8@16q24"
+ "q40@0:8@16Q24^@32"
+ "q40@0:8@16q24^@32"
+ "readMetadataWithPresentationData:nbuckets:"
+ "readMetadataWithPresentationData:nbuckets:error:"
+ "respondWithRequestData:metadata:nbuckets:error:"
+ "verifyWithPresentationData:nonce:requestContext:presentationContext:presentationLimit:"
- "@\"_TtC16CryptoKitPrivate10KVACClient\""
- "@\"_TtC16CryptoKitPrivate10KVACServer\""
- "@\"_TtC16CryptoKitPrivate21KVACCredentialWrapper\""
- "B48@0:8@16@24@32Q40"
- "B48@0:8@16@24@32q40"
- "CryptoKitPrivate.KVACClient"
- "CryptoKitPrivate.KVACCredentialWrapper"
- "CryptoKitPrivate/AesRng.swift"
- "CryptoKitPrivate/KVACBridging.swift"
- "KVAC.CredentialRequest"
- "KVAC.CredentialResponse"
- "KVAC.Presentation"
- "KVAC.error"
- "KVAC.requestContext"
- "KVACAwaitingActivation"
- "KVACCredential"
- "KVACPresentation"
- "KVACResponse"
- "KVACTestServer"
- "T@\"_TtC16CryptoKitPrivate10KVACClient\",R,N,V_client"
- "T@\"_TtC16CryptoKitPrivate10KVACServer\",R,N,V_server"
- "T@\"_TtC16CryptoKitPrivate21KVACCredentialWrapper\",R,&,N,V_credential"
- "Test presentation context"
- "_TtC16CryptoKitPrivate10KVACClient"
- "_TtC16CryptoKitPrivate10KVACServer"
- "_TtC16CryptoKitPrivate21KVACCredentialWrapper"
- "finalizeWithResponseData:error:"
- "getServerCommitments"
- "initWithCredential:presentationContext:error:"
- "initWithCredentialResponseData:client:error:"
- "initWithInteger:"
- "initWithRequestContext:serverCommitments:presentationLimit:error:"
- "initWithRequestContext:serverCommitmentsData:presentationLimit:error:"
- "makePresentationWithPresentationContext:error:"
- "makeRequestAndReturnError:"
- "presentWithPresentationContext:error:"
- "readBitWithPresentationData:error:"
- "respondWithRequestData:b:error:"
- "verifyWithPresentationData:requestContext:presentationContext:presentationLimit:"

```
