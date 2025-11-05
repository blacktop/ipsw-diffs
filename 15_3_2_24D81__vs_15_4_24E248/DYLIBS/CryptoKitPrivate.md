## CryptoKitPrivate

> `/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/Versions/A/CryptoKitPrivate`

```diff

-241.60.5.0.0
-  __TEXT.__text: 0x86fac
-  __TEXT.__auth_stubs: 0x19b0
-  __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0x3d08
-  __TEXT.__cstring: 0x25e5
-  __TEXT.__swift5_typeref: 0xfda
-  __TEXT.__swift5_reflstr: 0x18ed
-  __TEXT.__swift5_assocty: 0x2e8
-  __TEXT.__constg_swiftt: 0x1c1c
-  __TEXT.__swift5_fieldmd: 0x1dd0
+241.100.42.0.0
+  __TEXT.__text: 0x96a60
+  __TEXT.__auth_stubs: 0x1bb0
+  __TEXT.__objc_methlist: 0x8e4
+  __TEXT.__const: 0x3cc8
+  __TEXT.__cstring: 0x22a5
+  __TEXT.__swift5_typeref: 0x1150
+  __TEXT.__swift5_reflstr: 0x1a6d
+  __TEXT.__swift5_assocty: 0x2e0
+  __TEXT.__constg_swiftt: 0x1bd4
+  __TEXT.__swift5_fieldmd: 0x1d7c
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_proto: 0x290
+  __TEXT.__swift5_proto: 0x27c
   __TEXT.__swift5_types: 0x240
   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x1d08
-  __TEXT.__eh_frame: 0x4848
-  __TEXT.__objc_classname: 0x19c
-  __TEXT.__objc_methname: 0x1158
-  __TEXT.__objc_methtype: 0x409
-  __TEXT.__objc_stubs: 0x840
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x148
-  __DATA_CONST.__objc_classlist: 0x128
+  __TEXT.__unwind_info: 0x1c00
+  __TEXT.__eh_frame: 0x4e50
+  __TEXT.__objc_classname: 0x19a
+  __TEXT.__objc_methname: 0x1114
+  __TEXT.__objc_methtype: 0x3ef
+  __TEXT.__objc_stubs: 0x780
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0xf8
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x418
+  __DATA_CONST.__objc_selrefs: 0x408
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xce0
-  __AUTH_CONST.__const: 0x3260
+  __AUTH_CONST.__auth_got: 0xde0
+  __AUTH_CONST.__const: 0x3338
   __AUTH_CONST.__cfstring: 0xa0
-  __AUTH_CONST.__objc_const: 0x21c0
-  __AUTH.__objc_data: 0x1318
+  __AUTH_CONST.__objc_const: 0x1d08
+  __AUTH.__objc_data: 0x10b0
   __AUTH.__data: 0xc10
-  __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x14a0
-  __DATA.__bss: 0x4d00
-  __DATA.__common: 0xf8
+  __DATA.__objc_ivar: 0x7c
+  __DATA.__data: 0x1598
+  __DATA.__bss: 0x4a80
+  __DATA.__common: 0x118
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 313CA47D-6547-3DED-925A-F0B968F4AAC8
-  Functions: 2440
-  Symbols:   1154
-  CStrings:  485
+  UUID: 23A20151-183A-3306-98B3-7C962E188A21
+  Functions: 2256
+  Symbols:   1138
+  CStrings:  456
 
Symbols:
+ -[KVACAwaitingActivation activateWithResponseData:error:]
+ -[KVACAwaitingActivation initWithRequestContext:serverCommitments:presentationLimit:error:]
+ -[KVACCredential getCredentialDataError:]
+ -[KVACCredential initWithCredentialResponseData:client:error:]
+ -[KVACCredential presentWithPresentationContext:error:]
+ -[KVACPresentation initWithCredential:presentationContext:error:]
+ -[KVACResponse .cxx_destruct]
+ -[KVACResponse initWithResponseData:]
+ -[KVACResponse responseData]
+ -[KVACTestServer getServerCommitments]
+ -[KVACTestServer respondWithRequestData:error:]
+ -[KVACTestServer verifyWithPresentationData:requestContext:presentationContext:presentationLimit:]
+ OBJC_IVAR_$_KVACResponse._responseData
+ _OBJC_CLASS_$_KVACResponse
+ _OBJC_METACLASS_$_KVACResponse
+ __OBJC_$_INSTANCE_METHODS_KVACResponse
+ __OBJC_$_INSTANCE_VARIABLES_KVACResponse
+ __OBJC_$_PROP_LIST_KVACResponse
+ __OBJC_CLASS_RO_$_KVACResponse
+ __OBJC_METACLASS_RO_$_KVACResponse
+ ___swift_assign_boxed_opaque_existential_1
+ ___swift_memcpy136_8
+ ___swift_memcpy72_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___unnamed_5
+ __swiftEmptySetSingleton
+ _associated conformance 16CryptoKitPrivate04CoreA11HashToCurveVyxGAA0eF5GroupAA1GAaEP_7ElementAA0H0PAA09OPRFGroupI0
+ _associated conformance 16CryptoKitPrivate04CoreA11HashToCurveVyxGAA0eF5GroupAA1GAaEP_AA0H0
+ _associated conformance 16CryptoKitPrivate04CoreA11HashToCurveVyxGAA0eF5GroupAA1HAaEP_0aB00E8Function
+ _objc_msgSend$getCredentialDataAndReturnError:
+ _objc_msgSend$getServerCommitments
+ _objc_msgSend$initWithCredential:presentationContext:error:
+ _objc_msgSend$initWithCredentialResponseData:client:error:
+ _objc_msgSend$initWithRequestContext:serverCommitmentsData:presentationLimit:error:
+ _objc_msgSend$initWithResponseData:
+ _objc_msgSend$makeCredentialWithResponseData:error:
+ _objc_msgSend$makePresentationWithPresentationContext:error:
+ _objc_msgSend$respondWithRequestData:error:
+ _objc_msgSend$verifyWithPresentationData:requestContext:presentationContext:presentationLimit:
+ _swift_makeBoxUnique
+ _swift_stdlib_random
+ _symbolic 1G______7Element_____6Scalar_____QZ 16CryptoKitPrivate11HashToGroupP AA0F0P AA0F7ElementP
+ _symbolic SDy_____SaySiGG 10Foundation4DataV
+ _symbolic SDy_____ShySiGG 10Foundation4DataV
+ _symbolic SG_p
+ _symbolic Say1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate11HashToGroupP AA0F0P AA0F7ElementP
+ _symbolic SaySaySiGG
+ _symbolic Say_____G 10Foundation4DataV
+ _symbolic Say_____G 16CryptoKitPrivate3PIRO10HashBucketV0eF5EntryV
+ _symbolic Say_____SgG 10Foundation4DataV
+ _symbolic Say_____ySaySiGGG s10ArraySliceV
+ _symbolic _____ 16CryptoKitPrivate04CoreA11HashToCurveV
+ _symbolic _____ 16CryptoKitPrivate3PIRO10HashBucketV
+ _symbolic _____ 16CryptoKitPrivate3PIRO10HashBucketV0eF5EntryV
+ _symbolic _____ 16CryptoKitPrivate3PIRO11CuckooTableV
+ _symbolic _____ 16CryptoKitPrivate3PIRO17CuckooTableConfigV
+ _symbolic _____ 16CryptoKitPrivate3PIRO21BatchKeywordPirClientV
+ _symbolic _____ 16CryptoKitPrivate4KVACO13ClientSecretsV
+ _symbolic _____ 16CryptoKitPrivate4KVACO13ServerSecretsV
+ _symbolic _____ 16CryptoKitPrivate4KVACO17CredentialRequestV
+ _symbolic _____ 16CryptoKitPrivate4KVACO17ServerCommitmentsV
+ _symbolic _____ 16CryptoKitPrivate6AesRngV
+ _symbolic _____ySaySaySiGGG s23_ContiguousArrayStorageC
+ _symbolic _____ySaySiGG s10ArraySliceV
+ _symbolic _____ySaySiGG s23_ContiguousArrayStorageC
+ _symbolic _____ySay_____GG s23_ContiguousArrayStorageC 10Foundation4DataV
+ _symbolic _____ySay_____GG s23_ContiguousArrayStorageC 16CryptoKitPrivate2HEO20SerializedCiphertextO
+ _symbolic _____ySay_____ySaySiGGGG s23_ContiguousArrayStorageC s0B5SliceV
+ _symbolic _____ySiG s10ArraySliceV
+ _symbolic _____ySiG s11_SetStorageC
+ _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate4ATHMO13ClientSecretsV AA11HashToGroupP AA0I0P AA0I7ElementP
+ _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate4ATHMO13ServerSecretsV AA11HashToGroupP AA0I0P AA0I7ElementP
+ _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate4KVACO13ClientSecretsV AA11HashToGroupP AA0I0P AA0I7ElementP
+ _symbolic _____y_1G______7Element_____6Scalar_____QZG 16CryptoKitPrivate4KVACO13ServerSecretsV AA11HashToGroupP AA0I0P AA0I7ElementP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 16CryptoKitPrivate3PIRO10HashBucketV0hI5EntryV
+ _symbolic _____y_____SaySiGG s18_DictionaryStorageC 10Foundation4DataV
+ _symbolic _____y_____SgG s23_ContiguousArrayStorageC 10Foundation4DataV
+ _symbolic _____y_____ShySiGG s18_DictionaryStorageC 10Foundation4DataV
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ClientV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ServerV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO10CredentialV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO6ClientV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO6ServerV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4OPRFO16VerifiableClientV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y______y_____GG 16CryptoKitPrivate4OPRFO16VerifiableServerV AA04CoreA11HashToCurveV 0aB04P384O
+ _symbolic _____y_____ySaySiGGG s23_ContiguousArrayStorageC s0B5SliceV
+ _symbolic _____y_____ySiGG s23_ContiguousArrayStorageC s0B5SliceV
+ _symbolic _____y_xG 16CryptoKitPrivate4KVACO17CredentialRequestV
+ _symbolic _____y_xG 16CryptoKitPrivate4KVACO17ServerCommitmentsV
- -[KVACAwaitingActivation activateWithIssuanceData:error:]
- -[KVACAwaitingActivation initWithTokenChallenge:error:]
- -[KVACAwaitingActivation request]
- -[KVACCredential credentialData]
- -[KVACCredential initWithIssuanceData:client:request:error:]
- -[KVACCredential presentWithTagPrefix:error:]
- -[KVACCredential serverKeyId]
- -[KVACIssuance .cxx_destruct]
- -[KVACIssuance initWithIssuance:]
- -[KVACIssuance issuanceData]
- -[KVACIssuance keyId]
- -[KVACPresentation initWithCredential:tagPrefix:error:]
- -[KVACPresentation prefix]
- -[KVACPresentation serverKeyId]
- -[KVACPresentation tag]
- -[KVACTestServer issueWithRequestData:error:]
- -[KVACTestServer keyId]
- -[KVACTestServer verifyWithPresentationData:tokenChallenge:]
- OBJC_IVAR_$_KVACAwaitingActivation._request
- OBJC_IVAR_$_KVACCredential._credentialData
- OBJC_IVAR_$_KVACCredential._serverKeyId
- OBJC_IVAR_$_KVACIssuance._issuanceData
- OBJC_IVAR_$_KVACIssuance._keyId
- OBJC_IVAR_$_KVACPresentation._prefix
- OBJC_IVAR_$_KVACPresentation._serverKeyId
- OBJC_IVAR_$_KVACPresentation._tag
- OBJC_IVAR_$_KVACTestServer._keyId
- _OBJC_CLASS_$_KVACIssuance
- _OBJC_CLASS_$__TtC16CryptoKitPrivate18KVACRequestWrapper
- _OBJC_CLASS_$__TtC16CryptoKitPrivate19KVACIssuanceWrapper
- _OBJC_CLASS_$__TtC16CryptoKitPrivate23KVACPresentationWrapper
- _OBJC_METACLASS_$_KVACIssuance
- _OBJC_METACLASS_$__TtC16CryptoKitPrivate18KVACRequestWrapper
- _OBJC_METACLASS_$__TtC16CryptoKitPrivate19KVACIssuanceWrapper
- _OBJC_METACLASS_$__TtC16CryptoKitPrivate23KVACPresentationWrapper
- __DATA__TtC16CryptoKitPrivate18KVACRequestWrapper
- __DATA__TtC16CryptoKitPrivate19KVACIssuanceWrapper
- __DATA__TtC16CryptoKitPrivate23KVACPresentationWrapper
- __INSTANCE_METHODS__TtC16CryptoKitPrivate18KVACRequestWrapper
- __INSTANCE_METHODS__TtC16CryptoKitPrivate19KVACIssuanceWrapper
- __INSTANCE_METHODS__TtC16CryptoKitPrivate23KVACPresentationWrapper
- __IVARS__TtC16CryptoKitPrivate18KVACRequestWrapper
- __IVARS__TtC16CryptoKitPrivate19KVACIssuanceWrapper
- __IVARS__TtC16CryptoKitPrivate23KVACPresentationWrapper
- __METACLASS_DATA__TtC16CryptoKitPrivate18KVACRequestWrapper
- __METACLASS_DATA__TtC16CryptoKitPrivate19KVACIssuanceWrapper
- __METACLASS_DATA__TtC16CryptoKitPrivate23KVACPresentationWrapper
- __OBJC_$_INSTANCE_METHODS_KVACIssuance
- __OBJC_$_INSTANCE_VARIABLES_KVACIssuance
- __OBJC_$_PROP_LIST_KVACIssuance
- __OBJC_CLASS_RO_$_KVACIssuance
- __OBJC_METACLASS_RO_$_KVACIssuance
- __PROPERTIES__TtC16CryptoKitPrivate10KVACServer
- __PROPERTIES__TtC16CryptoKitPrivate18KVACRequestWrapper
- __PROPERTIES__TtC16CryptoKitPrivate19KVACIssuanceWrapper
- __PROPERTIES__TtC16CryptoKitPrivate21KVACCredentialWrapper
- __PROPERTIES__TtC16CryptoKitPrivate23KVACPresentationWrapper
- _associated conformance 16CryptoKitPrivate04CoreA10Hash2CurveVyxGAA11HashToGroupAA1GAaEP_AA0I0
- _associated conformance 16CryptoKitPrivate04CoreA10Hash2CurveVyxGAA11HashToGroupAA1HAaEP_0aB00G8Function
- _associated conformance 16CryptoKitPrivate04CoreA10Hash2CurveVyxGAA11HashToGroupAA2GEAaEP_AA16OPRFGroupElement
- _associated conformance 16CryptoKitPrivate10KVACErrorsOSHAASQ
- _associated conformance 16CryptoKitPrivate10OPRFErrorsOSHAASQ
- _objc_msgSend$credentialData
- _objc_msgSend$initWithCredential:tagPrefix:error:
- _objc_msgSend$initWithIssuance:
- _objc_msgSend$initWithIssuanceData:client:request:error:
- _objc_msgSend$initWithIssuanceData:error:
- _objc_msgSend$initWithTokenChallenge:error:
- _objc_msgSend$issuanceData
- _objc_msgSend$issueWithRequestData:error:
- _objc_msgSend$makeCredentialWithIssuance:request:error:
- _objc_msgSend$makePresentationWithTagPrefix:error:
- _objc_msgSend$prefix
- _objc_msgSend$presentationData
- _objc_msgSend$requestData
- _objc_msgSend$serverKeyId
- _objc_msgSend$tag
- _objc_msgSend$verifyWithPresentationData:tokenChallenge:
- _symbolic 2GE_____Qz 16CryptoKitPrivate11HashToGroupP
- _symbolic 2GE______6Scalar_____QZ 16CryptoKitPrivate11HashToGroupP AA0F7ElementP
- _symbolic Say2GE______6Scalar_____QZG 16CryptoKitPrivate11HashToGroupP AA0F7ElementP
- _symbolic Say_____G 16CryptoKitPrivate3PIRO16KeywordPirClientV10HashBucketV0hI5EntryV
- _symbolic _____ 16CryptoKitPrivate04CoreA10Hash2CurveV
- _symbolic _____ 16CryptoKitPrivate10KVACErrorsO
- _symbolic _____ 16CryptoKitPrivate10OPRFErrorsO
- _symbolic _____ 16CryptoKitPrivate18KVACRequestWrapperC
- _symbolic _____ 16CryptoKitPrivate19KVACIssuanceWrapperC
- _symbolic _____ 16CryptoKitPrivate23KVACPresentationWrapperC
- _symbolic _____ 16CryptoKitPrivate3PIRO16KeywordPirClientV10HashBucketV
- _symbolic _____ 16CryptoKitPrivate3PIRO16KeywordPirClientV10HashBucketV0hI5EntryV
- _symbolic _____ 16CryptoKitPrivate4ATHMO13ResponseProofV
- _symbolic _____ 16CryptoKitPrivate4KVACO16EncryptedRequestV
- _symbolic _____ 16CryptoKitPrivate4KVACO17EncryptedIssuanceV
- _symbolic _____y_2GE______6Scalar_____QZG 16CryptoKitPrivate4ATHMO13ClientSecretsV AA11HashToGroupP AA0I7ElementP
- _symbolic _____y_2GE______6Scalar_____QZG 16CryptoKitPrivate4ATHMO13ServerSecretsV AA11HashToGroupP AA0I7ElementP
- _symbolic _____y_____G s23_ContiguousArrayStorageC 16CryptoKitPrivate3PIRO16KeywordPirClientV10HashBucketV0kL5EntryV
- _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ClientV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4ATHMO6ServerV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO10CredentialV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO16EncryptedRequestV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO17EncryptedIssuanceV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO6ClientV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4KVACO6ServerV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4OPRFO16VerifiableClientV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GG 16CryptoKitPrivate4OPRFO16VerifiableServerV AA04CoreA10Hash2CurveV 0aB04P384O
- _symbolic _____y______y_____GGSg 16CryptoKitPrivate4ATHMO13ResponseProofV AA04CoreA10Hash2CurveV 0aB04P384O
CStrings:
+ "@48@0:8@16@24Q32^@40"
+ "@48@0:8@16@24q32^@40"
+ "B48@0:8@16@24@32Q40"
+ "B48@0:8@16@24@32q40"
+ "CryptoKitPrivate/AesRng.swift"
+ "CryptoKitPrivate/CKHybridSecretSharing.swift"
+ "CryptoKitPrivate/CKRawShamirSecretSharing.swift"
+ "CryptoKitPrivate/ECToolbox_cc.swift"
+ "KVAC.CredentialRequest"
+ "KVAC.CredentialResponse"
+ "KVAC.Presentation"
+ "KVAC.error"
+ "KVAC.requestContext"
+ "KVACResponse"
+ "T@\"NSData\",R,&,N,V_responseData"
+ "Test presentation context"
+ "Unsupported H2G ciphersuite."
+ "_responseData"
+ "getCredentialDataAndReturnError:"
+ "getCredentialDataError:"
+ "getServerCommitments"
+ "initWithCredential:presentationContext:error:"
+ "initWithCredentialResponseData:client:error:"
+ "initWithRequestContext:serverCommitments:presentationLimit:error:"
+ "initWithRequestContext:serverCommitmentsData:presentationLimit:error:"
+ "initWithResponseData:"
+ "makeCredentialWithResponseData:error:"
+ "makePresentationWithPresentationContext:error:"
+ "presentWithPresentationContext:error:"
+ "respondWithRequestData:error:"
+ "responseData"
+ "verifyWithPresentationData:requestContext:presentationContext:presentationLimit:"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CryptoKit/CryptoKitPrivate/Secret Sharing/CKHybridSecretSharing.swift"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CryptoKit/CryptoKitPrivate/Secret Sharing/CKRawShamirSecretSharing.swift"
- "@\"_TtC16CryptoKitPrivate18KVACRequestWrapper\""
- "@48@0:8@16@24@32^@40"
- "CryptoKitPrivate.KVACIssuanceWrapper"
- "CryptoKitPrivate.KVACPresentationWrapper"
- "CryptoKitPrivate.KVACRequestWrapper"
- "CryptoKitPrivate/NISTCurveGroups.swift"
- "KVACIssuance"
- "OPRFs only supports corecrypto H2G."
- "T@\"NSData\",R,&,N,V_credentialData"
- "T@\"NSData\",R,&,N,V_issuanceData"
- "T@\"NSData\",R,&,N,V_prefix"
- "T@\"NSData\",R,&,N,V_serverKeyId"
- "T@\"NSData\",R,&,N,V_tag"
- "T@\"_TtC16CryptoKitPrivate18KVACRequestWrapper\",R,N,V_request"
- "Test tag prefix"
- "_TtC16CryptoKitPrivate18KVACRequestWrapper"
- "_TtC16CryptoKitPrivate19KVACIssuanceWrapper"
- "_TtC16CryptoKitPrivate23KVACPresentationWrapper"
- "_credentialData"
- "_issuanceData"
- "_prefix"
- "_request"
- "_serverKeyId"
- "_tag"
- "activateWithIssuanceData:error:"
- "com.apple.cryptokit.KVAC.EncryptedIssuance"
- "com.apple.cryptokit.KVAC.EncryptedRequest"
- "com.apple.cryptokit.KVAC.Presentation"
- "com.apple.cryptokit.KVAC.Tag"
- "com.apple.cryptokit.KVAC.error"
- "com.apple.cryptokit.KVAC.generatorH"
- "com.apple.cryptokit.KVAC.keyId"
- "com.apple.cryptokit.KVAC.tokenChallenge"
- "credentialData"
- "initWithCredential:tagPrefix:error:"
- "initWithIssuance:"
- "initWithIssuanceData:client:request:error:"
- "initWithIssuanceData:error:"
- "initWithTokenChallenge:error:"
- "issuance"
- "issuanceData"
- "issueWithRequestData:error:"
- "makeCredentialWithIssuance:request:error:"
- "makePresentationWithTagPrefix:error:"
- "prefix"
- "presentWithTagPrefix:error:"
- "scalar count at deserialization: "
- "serverKeyId"
- "verifyWithPresentationData:tokenChallenge:"

```
