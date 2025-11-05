## DeviceCheckInternal

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/Versions/A/DeviceCheckInternal`

```diff

-88.3.0.0.0
-  __TEXT.__text: 0x8d9c
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x4c4
-  __TEXT.__const: 0x166
-  __TEXT.__cstring: 0x551
-  __TEXT.__oslogstring: 0xbd7
-  __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__unwind_info: 0x260
+108.2.0.0.0
+  __TEXT.__text: 0x14ad0
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_methlist: 0x68c
+  __TEXT.__const: 0x1691
+  __TEXT.__cstring: 0xc00
+  __TEXT.__oslogstring: 0x11ae
+  __TEXT.__gcc_except_tab: 0x270
+  __TEXT.__unwind_info: 0x3d0
   __TEXT.__objc_classname: 0x121
-  __TEXT.__objc_methname: 0xf32
-  __TEXT.__objc_methtype: 0x334
-  __TEXT.__objc_stubs: 0xe80
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0xf0
+  __TEXT.__objc_methname: 0x103f
+  __TEXT.__objc_methtype: 0x342
+  __TEXT.__objc_stubs: 0xf60
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__const: 0x1518
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x430
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2c0
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x2e0
-  __AUTH_CONST.__objc_const: 0x1008
+  __DATA_CONST.__objc_selrefs: 0x508
+  __DATA_CONST.__objc_superrefs: 0x8
+  __AUTH_CONST.__auth_got: 0x3c8
+  __AUTH_CONST.__const: 0x4b0
+  __AUTH_CONST.__cfstring: 0x320
+  __AUTH_CONST.__objc_const: 0xd90
   __AUTH.__objc_data: 0x410
   __DATA.__objc_ivar: 0x48
   __DATA.__data: 0x208
-  __DATA.__bss: 0x68
+  __DATA.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31B3A6EF-676E-34D3-971D-1D5655C90FD6
-  Functions: 211
-  Symbols:   666
-  CStrings:  416
+  UUID: CA86AA52-F906-398A-9DC9-C5DDB0C9E99D
+  Functions: 337
+  Symbols:   1127
+  CStrings:  455
 
Symbols:
+ +[DCAsset assetWithMobileAsset:].cold.2
+ +[DCBAASigner sharedSigner].cold.1
+ +[DCTaskCreator setupObserverFor:repeatingSystemTask:]
+ -[DCAssetFetcher _fetchAssetWithContext:completionHandler:].cold.1
+ -[DCAssetFetcher _handleMissingMetadataWithContext:completion:].cold.2
+ -[DCAssetFetcher _handleMissingMetadataWithContext:completion:].cold.3
+ -[DCAssetFetcher _handleSuccessForQuery:completion:].cold.2
+ -[DCAssetFetcher _queryMetadataWithContext:completion:].cold.2
+ -[DCAssetFetcher _validateAsset:error:].cold.1
+ -[DCAssetFetcher initiateMetadataFetchIgnoringCachesWithCompletion:].cold.1
+ -[DCBGSTaskController handleTask:].cold.1
+ -[DCCertificateGenerator context]
+ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:]
+ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:].cold.1
+ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:].cold.2
+ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:].cold.3
+ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:].cold.4
+ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:].cold.5
+ -[DCCertificateGenerator createPEMCertificateChainFrom:completion:].cold.6
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:]
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:].cold.1
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:].cold.2
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:].cold.3
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:].cold.4
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:].cold.5
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:].cold.6
+ -[DCCertificateGenerator encryptData:serverSyncedDate:error:].cold.7
+ -[DCCertificateGenerator generateCertificateChainWithCompletion:]
+ -[DCCertificateGenerator generateCertificateChainWithCompletion:].cold.1
+ -[DCCertificateGenerator isNSDate:]
+ -[DCCertificateGenerator isVirtualMachine]
+ -[DCCertificateGenerator parseDERCertificatesFromChain:]
+ -[DCCertificateGenerator parseDERCertificatesFromChain:].cold.1
+ -[DCCertificateGenerator parseDERCertificatesFromChain:].cold.2
+ -[DCCertificateGenerator publicKey]
+ -[DCCertificateGenerator setContext:]
+ -[DCCertificateGenerator setPublicKey:]
+ -[DCCryptoProxyImpl baaSignatureForData:completion:].cold.1
+ -[DCCryptoProxyImpl fetchOpaqueBlobWithContext:completion:].cold.1
+ DCInternalLogSystem.cold.1
+ DCInternalLogSystem.log
+ DCInternalLogSystem.onceToken
+ GCC_except_table10
+ GCC_except_table5
+ GCC_except_table9
+ _ACRTRootPublicKey
+ _AppleRootCA
+ _AppleRootCAG2
+ _AppleRootCAG3
+ _AppleRootCAPublicKey
+ _AppleRootCASKID
+ _AppleRootCASPKI
+ _AppleRootG2PublicKey
+ _AppleRootG2SKID
+ _AppleRootG2SPKI
+ _AppleRootG3PublicKey
+ _AppleRootG3SKID
+ _AppleRootG3SPKI
+ _AppleRoots
+ _BAARoots
+ _BASepAppRoot
+ _BASepAppRootPublicKey
+ _BASepAppRootSKID
+ _BASepAppRootSPKI
+ _BASystemRoot
+ _BASystemRootPublicKey
+ _BASystemRootSKID
+ _BASystemRootSPKI
+ _BAUserRoot
+ _BAUserRootPublicKey
+ _BAUserRootSKID
+ _BAUserRootSPKI
+ _BlockedYonkersPublicKey
+ _BlockedYonkersSPKI
+ _CMSAttributeParseAppleHashAgility
+ _CMSAttributeParseContentType
+ _CMSAttributeParseMessageDigest
+ _CMSAttributeParseSMIMECapabilities
+ _CMSAttributeParseSigningTime
+ _CMSBuildPath
+ _CMSParseContentInfoSignedData
+ _CMSParseContentInfoSignedDataWithOptions
+ _CMSParseImplicitCertificateSet
+ _CMSParseSignerInfos
+ _CMSVerify
+ _CMSVerifyAndReturnSignedData
+ _CMSVerifySignedData
+ _CMSVerifySignedDataWithLeaf
+ _CTCompareGeneralNameToHostname
+ _CTCopyUID
+ _CTEvaluateAcrt
+ _CTEvaluateAppleSSL
+ _CTEvaluateAppleSSLWithOptionalTemporalCheck
+ _CTEvaluateCertifiedChip
+ _CTEvaluateCertsForPolicy
+ _CTEvaluateKDLSignatureCMS
+ _CTEvaluatePragueSignatureCMS
+ _CTEvaluateSEK
+ _CTEvaluateSatori
+ _CTEvaluateSavageCerts
+ _CTEvaluateSavageCertsWithUID
+ _CTEvaluateSensorCerts
+ _CTEvaluateUcrt
+ _CTEvaluateUcrtTestRoot
+ _CTEvaluateYonkersCerts
+ _CTGetSEKType
+ _CTOctetServerAuthEKU
+ _CTOidAlgorithmProtection
+ _CTOidAppleAAICAG3
+ _CTOidAppleASICA4
+ _CTOidAppleCertifiedChipCA
+ _CTOidAppleCertifiedChipLeaf
+ _CTOidAppleCloudManaged
+ _CTOidAppleCodeSigningCA
+ _CTOidAppleComponentAuth
+ _CTOidAppleDeveloperID
+ _CTOidAppleDeveloperIDCA
+ _CTOidAppleDeviceAttestationDeviceOSInformation
+ _CTOidAppleDeviceAttestationHardwareProperties
+ _CTOidAppleDeviceAttestationIdentity
+ _CTOidAppleDeviceAttestationKeyUsageProperties
+ _CTOidAppleDeviceAttestationNonce
+ _CTOidAppleExtensionArc
+ _CTOidAppleGenericSSLMarker
+ _CTOidAppleHashAgility
+ _CTOidAppleHashAgilityV2
+ _CTOidAppleHaven
+ _CTOidAppleImg4Manifest
+ _CTOidAppleKextDenyListSigning
+ _CTOidAppleMFI4Properties
+ _CTOidAppleMFIAuthv3
+ _CTOidAppleMFISWAuth
+ _CTOidAppleMacAppStore
+ _CTOidAppleMacAppStoreDev
+ _CTOidAppleMacDeveloper
+ _CTOidAppleMacPlatform
+ _CTOidAppleMacSubmission
+ _CTOidApplePragueSigning
+ _CTOidAppleProvisioningProfileSigner
+ _CTOidAppleSatoriExternalEncryption
+ _CTOidAppleServerAuthCA
+ _CTOidAppleServerAuthExtensionPrefix
+ _CTOidAppleServerAuthExtensionPrefixLen
+ _CTOidAppleServerAuthExtensionPrefixString
+ _CTOidAppleTVOSAppStoreDev
+ _CTOidAppleTVOSAppStoreProd
+ _CTOidAppleTestFlightDev
+ _CTOidAppleTestFlightProd
+ _CTOidAppleUniqueDeviceIdentifiers
+ _CTOidAppleWWDRCA
+ _CTOidAppleXROSAppStoreDev
+ _CTOidAppleXROSAppStoreProd
+ _CTOidAppleiPhoneAppStoreDev
+ _CTOidAppleiPhoneAppStoreProd
+ _CTOidAppleiPhoneCA
+ _CTOidAppleiPhoneDeveloper
+ _CTOidAppleiPhoneDistribution
+ _CTOidAppleiPhoneVPNAppDev
+ _CTOidAppleiPhoneVPNAppProd
+ _CTOidAuthorityKeyID
+ _CTOidBasicConstraints
+ _CTOidCommonName
+ _CTOidContentType
+ _CTOidExtendedKeyUsage
+ _CTOidItemAppleDeviceAttestationDeviceOSInformation
+ _CTOidItemAppleDeviceAttestationHardwareProperties
+ _CTOidItemAppleDeviceAttestationKeyUsageProperties
+ _CTOidItemAppleDeviceAttestationNonce
+ _CTOidItemAppleImg4Manifest
+ _CTOidKeyUsage
+ _CTOidMessageDigest
+ _CTOidSECP256r1
+ _CTOidSECP384r1
+ _CTOidSECP521r1
+ _CTOidSMIMECapabilities
+ _CTOidServerAuthEKU
+ _CTOidSha1
+ _CTOidSha224
+ _CTOidSha256
+ _CTOidSha384
+ _CTOidSha512
+ _CTOidSigningTime
+ _CTOidSubjectAltName
+ _CTOidSubjectKeyID
+ _CTParseCertificateSet
+ _CTParseExtensionValue
+ _CTParseKey
+ _CTVerifyAppleMarkerExtension
+ _CTVerifyHostname
+ _CodeSigningCAName
+ _CodeSigningCAName_str
+ _DCInternalLogSystem
+ _DCLogDebugBinary.cold.2
+ _DeviceIdentityCreateHostSignatureWithCompletion
+ _MFICommonNamePrefix
+ _MFICommonNamePrefix_str
+ _MFi4AccessoryCAName
+ _MFi4AccessoryCAName_str
+ _MFi4AttestationCAName
+ _MFi4AttestationCAName_str
+ _MFi4ProvisioningCAName
+ _MFi4ProvisioningCAName_str
+ _MFi4ProvisioningHostNamePrefix
+ _MFi4ProvisioningHostNamePrefix_str
+ _MFi4RootPublicKey
+ _MFi4RootSKID
+ _MFi4RootSpki
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SEKProdRoot
+ _SEKProdRootPublicKey
+ _SEKProdRootSKID
+ _SEKProdRootSPKI
+ _SEKTestRoot
+ _SEKTestRootPublicKey
+ _SEKTestRootSKID
+ _SEKTestRootSPKI
+ _TestAppleRootCA
+ _TestAppleRootCAPublicKey
+ _TestAppleRootCASKID
+ _TestAppleRootCASPKI
+ _TestAppleRootECC
+ _TestAppleRootECCPublicKey
+ _TestAppleRootECCSKID
+ _TestAppleRootECCSPKI
+ _TestAppleRootG2
+ _TestAppleRootG2PublicKey
+ _TestAppleRootG2SKID
+ _TestAppleRootG2SPKI
+ _TestAppleRootG3
+ _TestAppleRootG3PublicKey
+ _TestAppleRootG3SKID
+ _TestAppleRootG3SPKI
+ _UcrtRootPublicKey
+ _UcrtRootSpki
+ _X509CertificateCheckSignature
+ _X509CertificateCheckSignatureDigest
+ _X509CertificateCheckSignatureWithPublicKey
+ _X509CertificateGetNotAfter
+ _X509CertificateGetNotBefore
+ _X509CertificateIsValid
+ _X509CertificateParse
+ _X509CertificateParseGeneralNamesContent
+ _X509CertificateParseImplicit
+ _X509CertificateParseKey
+ _X509CertificateParseSPKI
+ _X509CertificateParseValidity
+ _X509CertificateParseWithExtension
+ _X509CertificateSubjectNameGetCommonName
+ _X509CertificateValidAtTime
+ _X509CertificateVerifyOnlyOneAppleExtension
+ _X509ChainBuildPath
+ _X509ChainBuildPathPartial
+ _X509ChainCheckPath
+ _X509ChainCheckPathWithOptions
+ _X509ChainGetAppleRootUsingKeyIdentifier
+ _X509ChainGetBAARootUsingKeyIdentifier
+ _X509ChainGetCertificateUsingKeyIdentifier
+ _X509ChainParseCertificateSet
+ _X509ChainResetChain
+ _X509ExtensionParseAppleExtension
+ _X509ExtensionParseAuthorityKeyIdentifier
+ _X509ExtensionParseBasicConstraints
+ _X509ExtensionParseCertifiedChipIntermediate
+ _X509ExtensionParseComponentAuth
+ _X509ExtensionParseDeviceAttestationIdentity
+ _X509ExtensionParseExtendedKeyUsage
+ _X509ExtensionParseGenericSSLMarker
+ _X509ExtensionParseKeyUsage
+ _X509ExtensionParseMFI4Properties
+ _X509ExtensionParseMFIAuthv3Leaf
+ _X509ExtensionParseMFISWAuth
+ _X509ExtensionParseServerAuthMarker
+ _X509ExtensionParseSubjectAltName
+ _X509ExtensionParseSubjectKeyIdentifier
+ _X509MatchSignatureAlgorithm
+ _X509PolicyACRT
+ _X509PolicyCheckForBlockedKeys
+ _X509PolicySEK
+ _X509PolicySatori
+ _X509PolicySavage
+ _X509PolicySensor
+ _X509PolicySetFlagsForCommonNames
+ _X509PolicySetFlagsForMFI
+ _X509PolicySetFlagsForRoots
+ _X509PolicySetFlagsForTestAnchor
+ _X509PolicyUcrt
+ _X509PolicyYonkers
+ _X509TimeConvert
+ __34-[DCBGSTaskController handleTask:]_block_invoke.cold.2
+ __37-[DCCryptoProxyImpl _fetchPublicKey:]_block_invoke.cold.1
+ __37-[DCCryptoProxyImpl _fetchPublicKey:]_block_invoke.cold.2
+ __44-[DCBAASigner signaturesForData:completion:]_block_invoke.6
+ __44-[DCBAASigner signaturesForData:completion:]_block_invoke.6.cold.1
+ __44-[DCBAASigner signaturesForData:completion:]_block_invoke.6.cold.2
+ __44-[DCBAASigner signaturesForData:completion:]_block_invoke.6.cold.3
+ __44-[DCBAASigner signaturesForData:completion:]_block_invoke.cold.4
+ __54+[DCTaskCreator setupObserverFor:repeatingSystemTask:]_block_invoke.cold.1
+ __54+[DCTaskCreator setupObserverFor:repeatingSystemTask:]_block_invoke.cold.2
+ __54+[DCTaskCreator setupObserverFor:repeatingSystemTask:]_block_invoke.cold.3
+ __54+[DCTaskCreator setupObserverFor:repeatingSystemTask:]_block_invoke.cold.4
+ __63-[DCAssetFetcher _handleMissingMetadataWithContext:completion:]_block_invoke.cold.1
+ __65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.8
+ __65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.8.cold.1
+ __65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.8.cold.2
+ __65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.cold.1
+ __65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.cold.2
+ __65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke.cold.3
+ __68-[DCAssetFetcher initiateMetadataFetchIgnoringCachesWithCompletion:]_block_invoke.cold.1
+ __OBJC_$_PROP_LIST_DCCertificateGenerator
+ ___54+[DCTaskCreator setupObserverFor:repeatingSystemTask:]_block_invoke
+ ___65-[DCCertificateGenerator generateCertificateChainWithCompletion:]_block_invoke
+ ___DCInternalLogSystem_block_invoke
+ ___block_descriptor_40_e8_v16?08l
+ ___block_descriptor_48_e8_32r40w_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e40_v32?0"NSData"8"NSArray"16"NSError"24l
+ ___block_descriptor_48_e8_32s40s_e8_v12?0i8l
+ ___block_descriptor_80_e8_32s40s48s56s64r_e15_v32?0816^B24l
+ ___copy_helper_block_e8_32r40w
+ ___copy_helper_block_e8_32s40s
+ ___copy_helper_block_e8_32s40s48s56s64r
+ ___destroy_helper_block_e8_32r40w
+ ___destroy_helper_block_e8_32s40s48s56s64r
+ ___memcpy_chk
+ __acrt_root_public_key
+ __baa_sep_app_root_public_key
+ __baa_sep_app_root_skid
+ __baa_sep_app_root_spki
+ __baa_system_root_public_key
+ __baa_system_root_skid
+ __baa_system_root_spki
+ __baa_user_root_public_key
+ __baa_user_root_skid
+ __baa_user_root_spki
+ __block_literal_global.22
+ __block_literal_global.302
+ __dispatch_main_q
+ __mfi4_root_pub_key
+ __mfi4_root_skid
+ __mfi4_root_spki
+ __sek_prod_root_public_key
+ __sek_prod_root_skid
+ __sek_prod_root_spki
+ __sek_test_root_public_key
+ __sek_test_root_skid
+ __sek_test_root_spki
+ __ucrt_root_pub_key
+ __ucrt_root_spki
+ _asciiNibbleToByte
+ _ccder_blob_check_null
+ _ccder_blob_decode_AlgorithmIdentifierNULL
+ _ccder_blob_decode_GeneralName
+ _ccder_blob_decode_Time
+ _ccder_blob_decode_ber_len
+ _ccder_blob_decode_ber_tl
+ _ccder_blob_decode_bitstring
+ _ccder_blob_decode_eoc
+ _ccder_blob_decode_uint64
+ _ccder_blob_eat_ber_inner
+ _ccder_decode_rsa_pub_n
+ _ccder_sizeof_len
+ _ccder_sizeof_tag
+ _ccdigest
+ _ccdigest_init
+ _ccdigest_update
+ _ccec_compressed_x962_export_pub
+ _ccec_compressed_x962_export_pub_size
+ _ccec_compressed_x962_import_pub
+ _ccec_cp_521
+ _ccec_cp_for_oid
+ _ccec_import_pub
+ _ccec_keysize_is_supported
+ _ccec_verify
+ _ccec_verify_composite
+ _ccec_x963_import_pub_size
+ _ccrsa_import_pub
+ _ccrsa_verify_pkcs1v15_allowshortsigs
+ _ccsha1_di
+ _ccsha224_di
+ _ccsha256_di
+ _ccsha384_di
+ _ccsha512_di
+ _compare_octet_string
+ _compare_octet_string_partial
+ _compare_octet_string_raw
+ _compressECPublicKey
+ _decompressECPublicKey
+ _der_get_boolean
+ _difftime
+ _digests
+ _ecAlgs
+ _ecPublicKey
+ _ecPublicKey_oid
+ _find_digest
+ _find_digestOID_for_signingOID
+ _find_digest_by_type
+ _iPhoneCAName
+ _iPhoneCAName_str
+ _memset
+ _merge_dict_cb.cold.1
+ _notify_post
+ _notify_register_dispatch
+ _null_octet
+ _numAppleProdRoots
+ _numAppleRoots
+ _numBAARoots
+ _objc_msgSend$context
+ _objc_msgSend$createPEMCertificateChainFrom:completion:
+ _objc_msgSend$encryptData:serverSyncedDate:error:
+ _objc_msgSend$generateCertificateChainWithCompletion:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$isNSDate:
+ _objc_msgSend$isVirtualMachine
+ _objc_msgSend$setContext:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setupObserverFor:repeatingSystemTask:
+ _objc_msgSend$stringByAppendingString:
+ _objc_opt_new
+ _objc_sync_enter
+ _objc_sync_exit
+ _oidForPubKeyLength
+ _pkcs7_data_oid
+ _pkcs7_data_oid_str
+ _pkcs7_signedData_oid
+ _pkcs7_signedData_oid_str
+ _powersOfTen
+ _rsaAlgs
+ _rsaEncryption
+ _rsaEncryption_oid
+ _secp256r1_encoded_oid
+ _secp384r1_encoded_oid
+ _secp521r1_encoded_oid
+ _sha1WithECDSA_oid
+ _sha1WithRSA_oid
+ _sha256WithECDSA_oid
+ _sha256WithRSA_oid
+ _sha384WithECDSA_oid
+ _sha384WithRSA_oid
+ _sha512WithECDSA_oid
+ _sha512WithRSA_oid
+ _strptime
+ _sysctlbyname
+ _time
+ _timegm
+ _validateOIDs
+ _validateSignatureEC
+ _validateSignatureRSA
+ _validateSignerInfo
+ _validateSignerInfoAndChain
+ der_key_validate.cold.1
+ der_key_validate.cold.2
+ get_aks_client_connection.cold.1
- -[DCCertificateGenerator _encryptData:serverSyncedDate:error:]
- -[DCCertificateGenerator _encryptData:serverSyncedDate:error:].cold.1
- -[DCCertificateGenerator _encryptData:serverSyncedDate:error:].cold.2
- -[DCCertificateGenerator _encryptData:serverSyncedDate:error:].cold.3
- -[DCCertificateGenerator _encryptData:serverSyncedDate:error:].cold.4
- -[DCCertificateGenerator _encryptData:serverSyncedDate:error:].cold.5
- -[DCCertificateGenerator _encryptData:serverSyncedDate:error:].cold.6
- -[DCCertificateGenerator _generateCertificateChainWithCompletion:]
- -[DCCertificateGenerator _isNSDate:]
- -[DCCertificateGenerator dealloc]
- _DCAALogSystem.log
- _DCAALogSystem.onceToken
- _DCLogSystem.log
- _DCLogSystem.onceToken
- __34-[DCBGSTaskController handleTask:]_block_invoke.10
- __34-[DCBGSTaskController handleTask:]_block_invoke.10.cold.1
- __34-[DCBGSTaskController handleTask:]_block_invoke.10.cold.2
- __34-[DCBGSTaskController handleTask:]_block_invoke.10.cold.3
- __44-[DCBAASigner signaturesForData:completion:]_block_invoke.5
- __44-[DCBAASigner signaturesForData:completion:]_block_invoke.5.cold.1
- __44-[DCBAASigner signaturesForData:completion:]_block_invoke.5.cold.2
- __44-[DCBAASigner signaturesForData:completion:]_block_invoke.5.cold.3
- __66-[DCCertificateGenerator _generateCertificateChainWithCompletion:]_block_invoke.cold.1
- __DCAALogSystem
- __DCLogSystem
- ___66-[DCCertificateGenerator _generateCertificateChainWithCompletion:]_block_invoke
- ____DCAALogSystem_block_invoke
- ____DCLogSystem_block_invoke
- ___block_descriptor_32_e8_v16?08l
- ___block_descriptor_40_e8_32w_e5_v8?0l
- ___block_descriptor_56_e8_32s40r48w_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48r_e15_v32?0816^B24l
- ___copy_helper_block_e8_32s40r48w
- ___copy_helper_block_e8_32s40s48r
- ___copy_helper_block_e8_32w
- ___destroy_helper_block_e8_32s40r48w
- ___destroy_helper_block_e8_32s40s48r
- ___destroy_helper_block_e8_32w
- __block_literal_global.4
- __os_log_error_impl
- _dispatch_async
- _objc_msgSend$_encryptData:serverSyncedDate:error:
- _objc_msgSend$_generateCertificateChainWithCompletion:
- _objc_msgSend$_isNSDate:
- _objc_msgSend$expiryQueue
CStrings:
+ "%25s:%-5d Attempting to download catalog."
+ "%25s:%-5d Attempting to fetch asset, querying metadata. { context=%@ }"
+ "%25s:%-5d Attempting to generate certificate chain on VM, using host identity."
+ "%25s:%-5d Attempting to generate certificate data. { minTtl=%dh, validity=%dh, maxTtl=%dh }"
+ "%25s:%-5d Attempting to sign data. { key=%@, object=%@ }"
+ "%25s:%-5d Attempting to update task's refresh interval. { taskID=%s, refreshInterval=%f }"
+ "%25s:%-5d Attempting to validate asset: { asset=%@, state=%ld, attributes=%@ }"
+ "%25s:%-5d Cannot sign data, empty. { key=%@ }"
+ "%25s:%-5d Cannot sign data, platform is not supported by DeviceIdentity."
+ "%25s:%-5d Cannot sign empty data."
+ "%25s:%-5d Cannot sign empty data. { length=%lu }"
+ "%25s:%-5d Cannot update to refresh interval, failed to fetch task. { taskID=%s, refreshInterval=%f }"
+ "%25s:%-5d Certificate issued, processing."
+ "%25s:%-5d Certificate processed. { certificateChainLength=%lu }"
+ "%25s:%-5d Created signature using host identity. { signatureLength=%lu, certificateCount=%lu }"
+ "%25s:%-5d Creating PEM certificate chain."
+ "%25s:%-5d Dispatching task exit notification. { identifier=%@ }"
+ "%25s:%-5d Downloaded catalog. { result=%ld }"
+ "%25s:%-5d Encrypting certificate chain data. { timestamp=%@ }"
+ "%25s:%-5d Executed query successfully. { numResults=%lu }"
+ "%25s:%-5d Failed to allocate buffer for compressed data."
+ "%25s:%-5d Failed to compress data."
+ "%25s:%-5d Failed to create ECDH key: %d\n"
+ "%25s:%-5d Failed to create PEM data from certificate. { error=%@ }"
+ "%25s:%-5d Failed to create host signature. { error=%@ }"
+ "%25s:%-5d Failed to fetch BAA certificates."
+ "%25s:%-5d Failed to fetch BAA certificates. { error=%@ }"
+ "%25s:%-5d Failed to fetch catalog, not allowed."
+ "%25s:%-5d Failed to fetch client certificate. { error=%@ }"
+ "%25s:%-5d Failed to fetch mobile asset, using locally cached public key. { error=%@ }"
+ "%25s:%-5d Failed to generate signature for data. { data=%@, error=%@ }"
+ "%25s:%-5d Failed to initiate metadata fetch. { taskID=%s }"
+ "%25s:%-5d Failed to mark task as expired. { error=%@, task=%@ }"
+ "%25s:%-5d Failed to obtain valid certificates from server.  { error=%@ }"
+ "%25s:%-5d Failed to parse asset, public key is missing."
+ "%25s:%-5d Failed to parse certificate set. rc=%d, numCerts=%zu"
+ "%25s:%-5d Failed to parse certificate to SecCertificateRef type."
+ "%25s:%-5d Failed to perform AES-GSM encryption with shared key: %d\n"
+ "%25s:%-5d Failed to perform ECDH with server pubkey: %d\n"
+ "%25s:%-5d Failed to perform HKDF with shared key: %d\n"
+ "%25s:%-5d Failed to query metadata. { result=%ld }"
+ "%25s:%-5d Failed to serialize attestation dictionary."
+ "%25s:%-5d Failed to serialize attestation dictionary. { error=%@ }"
+ "%25s:%-5d Failed to sign key."
+ "%25s:%-5d Failed to sign key. { error=%@ }"
+ "%25s:%-5d Failed to to initiate metadata fetch. { taskID=%s, error=%@ }"
+ "%25s:%-5d Failed to update task."
+ "%25s:%-5d Failed to update task. { error=%@ }"
+ "%25s:%-5d Fetching asset. { context=%@ }"
+ "%25s:%-5d Generating encrypted certificate. { clientAppID=%@ }"
+ "%25s:%-5d Initiated MobileAsset fetch. { taskID=%s }"
+ "%25s:%-5d Initiated an out of band catalog download completed. { result=%ld }"
+ "%25s:%-5d Initiating an out of band catalog download"
+ "%25s:%-5d Invalid certificate data."
+ "%25s:%-5d Invoking handler for task. { taskID=%@ }"
+ "%25s:%-5d Key was changed. { key=%@ }"
+ "%25s:%-5d Marked task as expired. { task=%@ }"
+ "%25s:%-5d Overflow while attempting to compress data."
+ "%25s:%-5d Parsed asset. { asset=%@ }"
+ "%25s:%-5d Query sync result indicated missing asset catalog."
+ "%25s:%-5d Received task exit notification. { identifier=%@ }"
+ "%25s:%-5d Refreshed mobile asset and fetched remote public key."
+ "%25s:%-5d Registered task. { taskID=%s, success=%d }"
+ "%25s:%-5d Requested refresh interval must be greater than base refresh interval. { refreshInterval=%f, baseRefreshInterval=%d }"
+ "%25s:%-5d Signed data. { signatureData=%@, attestationData=%@, error=%@ }"
+ "%25s:%-5d Signing data with BAA certificates."
+ "%25s:%-5d Signing dictionary with BAA certificates."
+ "%25s:%-5d System task handler called. { task=%@ }"
+ "%25s:%-5d System task object is nil, cannot expire task."
+ "%25s:%-5d Task expiration handler invoked. { taskID=%s }"
+ "%25s:%-5d Token timestamp: %f"
+ "%25s:%-5d Unexpected pubkey size. expected %ld got %ld\n"
+ "%25s:%-5d Unexpected result count. { numResults=%lu }"
+ "%25s:%-5d Updated task. { taskID=%s, refreshInterval=%f }"
+ "%25s:%-5d Using device timestamp."
+ "%25s:%-5d Using synced timestamp. { serverSyncedDate=%@ }"
+ "%25s:%-5d out_data_to_send is NULL!\n"
+ "%F"
+ "%Y%m%d%H%M%SZ"
+ "%y%m%d%H%M%SZ"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCBAASigner.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCCertificateGenerator.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/DCCryptoUtilities.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Core/Crypto/NSData+Signing.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCAsset.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCAssetFetcher.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCBGSTaskController.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCCryptoProxyImpl.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/TwoBit/DeviceCheckInternal/Source/Interfaces/DCTaskCreator.m"
+ "2006-05-31"
+ "Expected date field, failing."
+ "Failed to create PEM data from certificate"
+ "T@\"DCContext\",&,N,V_context"
+ "T@\"NSData\",&,N,V_publicKey"
+ "_exit_observer"
+ "context"
+ "createPEMCertificateChainFrom:completion:"
+ "dci"
+ "encryptData:serverSyncedDate:error:"
+ "generateCertificateChainWithCompletion:"
+ "initWithBytes:length:"
+ "isNSDate:"
+ "isVirtualMachine"
+ "kern.hv_vmm_present"
+ "parseDERCertificatesFromChain:"
+ "setContext:"
+ "setObject:atIndexedSubscript:"
+ "setupObserverFor:repeatingSystemTask:"
+ "stringByAppendingString:"
+ "v12@?0i8"
+ "v32@0:8@16@24"
+ "v32@?0@\"NSData\"8@\"NSArray\"16@\"NSError\"24"
- "%@ = %@"
- "Attempting to download catalog, waiting for result..."
- "Attempting to generate certificate data... (%dh/%dh/%dh)"
- "Attempting to update task's refresh interval. { taskID=%s, refreshInterval=%f }"
- "Attempting to validate asset: <%@ - %ld> - %@"
- "Attestation Error %@"
- "Cannot update to refresh interval, failed to fetch task. { taskID=%s, refreshInterval=%f }"
- "Catalog downloaded with result %ld..."
- "Catalog refetch not allowed, failing..."
- "Certificate issued, processing.."
- "Certificate processed... (%lu)"
- "DCBAASigner signatureForData: - No data, nothing to sign."
- "DCCertificateGenerator generator going away..."
- "Encrypting data..."
- "Expected date field, failing..."
- "Failed to BAA, error: %@"
- "Failed to BAA, failed to generate signature: %@"
- "Failed to BAA, failed to generate signature: unknown error!"
- "Failed to BAA, failed to serialize: %@"
- "Failed to BAA, failed to serialize: unknown error!"
- "Failed to BAA, unknown error!"
- "Failed to allocate buffer for compressed data!"
- "Failed to compress data!"
- "Failed to create ECDH key: %d\n"
- "Failed to generate signatures, bailing!"
- "Failed to initiate metadata fetch. { taskID=%s }"
- "Failed to obtain valid certificates from server: %@"
- "Failed to parse asset, required fields are missing!"
- "Failed to perform AES-GSM encryption with shared key: %d\n"
- "Failed to perform ECDH with server pubkey: %d\n"
- "Failed to perform HKDF with shared key: %d\n"
- "Failed to set task expired. { backOff=%lu }"
- "Failed to set task expired. { error=%@, backOff=%lu }"
- "Failed to to initiate metadata fetch. { taskID=%s, error=%@ }"
- "Failed to update task."
- "Failed to update task. { error=%@ }"
- "Falling back to locally cached key... Asset fetch failed: %@"
- "Fetched remote public key..."
- "Generating certificate..."
- "Initiated MobileAsset fetch. { taskID=%s }"
- "Initiated an out of band catalog download completed with result: %ld"
- "Initiating an out of band catalog download"
- "Invoking handler for task. { taskID=%s }"
- "Key was changed. { key=%@ }"
- "Nothing to sign for key: %@, bailing!"
- "Overflow while attempting to compress data!"
- "Platform not supported by Device Identity"
- "Query success, results count: %lu"
- "Query sync result indicated missing asset catalog"
- "Querying..."
- "Registered task. { taskID=%s, success=%d }"
- "Requested refresh interval must be greater than base refresh interval. { refreshInterval=%f, baseRefreshInterval=%d }"
- "Returning parsed asset: %@"
- "Signing Completed in DeviceCheckd - SignatureData: %@, AttestationData: %@, Error:%@"
- "Signing with baa certs for data..."
- "Signing with baa certs for dictionary"
- "Starting to fetch asset with context: %@"
- "System task handler called. { task=%@ }"
- "Task expiration handler invoked. { taskID=%s }"
- "Task requested to exit, attempting to mark as expired. { task=%@ }"
- "Token timestamp: %f"
- "Unexpected pubkey size. expected %ld got %ld\n"
- "Unexpected query result: %ld"
- "Unexpected result count detected!!!"
- "Updated task. { taskID=%s, refreshInterval=%f }"
- "Using device timestamp..."
- "Using synced timestamp..."
- "_encryptData:serverSyncedDate:error:"
- "_generateCertificateChainWithCompletion:"
- "_isNSDate:"
- "attestation"
- "core"
- "dealloc"
- "out_data_to_send is NULL!\n"
- "signaturesForData: - No data, nothing to sign."

```
