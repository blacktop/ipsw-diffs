## DeviceCheckInternal

> `/System/Library/PrivateFrameworks/DeviceCheckInternal.framework/DeviceCheckInternal`

```diff

-132.2.0.0.0
-  __TEXT.__text: 0x14634
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x684
-  __TEXT.__const: 0x5ea8
-  __TEXT.__cstring: 0xbba
-  __TEXT.__oslogstring: 0x108b
-  __TEXT.__gcc_except_tab: 0x280
-  __TEXT.__unwind_info: 0x420
-  __TEXT.__objc_classname: 0x121
-  __TEXT.__objc_methname: 0xfe7
-  __TEXT.__objc_methtype: 0x343
-  __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x3bd0
-  __DATA_CONST.__objc_classlist: 0x68
+151.0.0.0.0
+  __TEXT.__text: 0x15a18
+  __TEXT.__objc_methlist: 0x6ec
+  __TEXT.__const: 0xbcf3
+  __TEXT.__cstring: 0xd06
+  __TEXT.__oslogstring: 0x136e
+  __TEXT.__gcc_except_tab: 0x218
+  __TEXT.__unwind_info: 0x428
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x4238
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f0
-  __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x448
+  __DATA_CONST.__objc_selrefs: 0x570
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x300
-  __AUTH_CONST.__objc_const: 0xd90
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x48
+  __AUTH_CONST.__cfstring: 0x420
+  __AUTH_CONST.__objc_const: 0x1038
+  __AUTH_CONST.__auth_got: 0x490
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x208
   __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4DDE2062-9BC2-3FE1-B0F3-EBBB4A12DDA9
-  Functions: 349
-  Symbols:   1704
-  CStrings:  443
+  UUID: 150946B8-524A-322B-BC04-9E8D9E5C799D
+  Functions: 371
+  Symbols:   1826
+  CStrings:  199
 
Symbols:
+ -[DCCryptoProxyImpl .cxx_destruct]
+ -[DCCryptoProxyImpl fetchAssetInfo:]
+ -[DCCryptoProxyImpl setUafAssetManager:]
+ -[DCCryptoProxyImpl uafAssetManager]
+ -[DCEncryptionKeyAsset .cxx_destruct]
+ -[DCEncryptionKeyAsset fetchEncryptionKey]
+ -[DCEncryptionKeyAsset fetchEncryptionKey].cold.1
+ -[DCEncryptionKeyAsset fetchEncryptionKey].cold.2
+ -[DCEncryptionKeyAsset fetchEncryptionKey].cold.3
+ -[DCEncryptionKeyAsset fetchEncryptionKey].cold.4
+ -[DCEncryptionKeyAsset filePath]
+ -[DCEncryptionKeyAsset initWithFilePath:]
+ -[DCEncryptionKeyAsset setFilePath:]
+ -[DCUAFAssetConfiguration .cxx_destruct]
+ -[DCUAFAssetConfiguration assetName]
+ -[DCUAFAssetConfiguration assetSetName]
+ -[DCUAFAssetConfiguration description]
+ -[DCUAFAssetConfiguration initWithAssetSetName:assetName:subscriber:subscriptionName:usageType:]
+ -[DCUAFAssetConfiguration subscriber]
+ -[DCUAFAssetConfiguration subscriptionName]
+ -[DCUAFAssetConfiguration usageType]
+ -[DCUAFAssetInfo .cxx_destruct]
+ -[DCUAFAssetInfo assetDataURL]
+ -[DCUAFAssetInfo description]
+ -[DCUAFAssetInfo initWithName:assetDataURL:version:]
+ -[DCUAFAssetInfo name]
+ -[DCUAFAssetInfo version]
+ -[DCUAFAssetManager .cxx_destruct]
+ -[DCUAFAssetManager configuration]
+ -[DCUAFAssetManager fetchWithCompletion:]
+ -[DCUAFAssetManager initWithConfiguration:]
+ -[DCUAFAssetManager subscribeWithCompletion:]
+ -[DCUAFAssetManager subscribeWithCompletion:].cold.1
+ -[DCUAFAssetManager subscribed]
+ -[DCUAFAssetManager subscribed].cold.1
+ -[DCUAFAssetManager subscribed].cold.2
+ -[DCUAFAssetManager unsubscribeWithCompletion:]
+ -[DCUAFDeviceCheckAsset .cxx_destruct]
+ -[DCUAFDeviceCheckAsset encryptionKeyAsset]
+ -[DCUAFDeviceCheckAsset initWithFilePath:]
+ -[DCUAFDeviceCheckAsset initWithFilePath:].cold.1
+ -[DCUAFDeviceCheckAsset setEncryptionKeyAsset:]
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1PublicKey
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1SKID
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1SPKI
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_public_key
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_skid
+ _ApplePlatformCodeSigningMLDSA_RSARootCAG1_spki
+ _CTEvaluateKeyTransparency
+ _CTEvaluateVLTileSigning
+ _CTGetAKIDFromCertificate
+ _CTGetSKIDFromCertificate
+ _CTOidAppleAAICA
+ _CTOidAppleKeyTransparencyLeaf
+ _CTOidAppleVLTilesSigning
+ _OBJC_CLASS_$_DCEncryptionKeyAsset
+ _OBJC_CLASS_$_DCUAFAssetConfiguration
+ _OBJC_CLASS_$_DCUAFAssetInfo
+ _OBJC_CLASS_$_DCUAFAssetManager
+ _OBJC_CLASS_$_DCUAFDeviceCheckAsset
+ _OBJC_CLASS_$_NSPropertyListSerialization
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_CLASS_$_UAFAssetSetSubscription
+ _OBJC_IVAR_$_DCCryptoProxyImpl._uafAssetManager
+ _OBJC_IVAR_$_DCEncryptionKeyAsset._filePath
+ _OBJC_IVAR_$_DCUAFAssetConfiguration._assetName
+ _OBJC_IVAR_$_DCUAFAssetConfiguration._assetSetName
+ _OBJC_IVAR_$_DCUAFAssetConfiguration._subscriber
+ _OBJC_IVAR_$_DCUAFAssetConfiguration._subscriptionName
+ _OBJC_IVAR_$_DCUAFAssetConfiguration._usageType
+ _OBJC_IVAR_$_DCUAFAssetInfo._assetDataURL
+ _OBJC_IVAR_$_DCUAFAssetInfo._name
+ _OBJC_IVAR_$_DCUAFAssetInfo._version
+ _OBJC_IVAR_$_DCUAFAssetManager._configuration
+ _OBJC_IVAR_$_DCUAFDeviceCheckAsset._encryptionKeyAsset
+ _OBJC_METACLASS_$_DCEncryptionKeyAsset
+ _OBJC_METACLASS_$_DCUAFAssetConfiguration
+ _OBJC_METACLASS_$_DCUAFAssetInfo
+ _OBJC_METACLASS_$_DCUAFAssetManager
+ _OBJC_METACLASS_$_DCUAFDeviceCheckAsset
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_71
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1PublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1SKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1SPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWPublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWSKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HWSPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_HW_spki
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13PublicKey
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13SKID
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13SPKI
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_draft13_spki
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_public_key
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_skid
+ _TestApplePlatformCodeSigningMLDSA_RSARootCAG1_spki
+ _X509ExtensionParseKeyTransparencyLeaf
+ _X509PolicyVLTile
+ __OBJC_$_INSTANCE_METHODS_DCEncryptionKeyAsset
+ __OBJC_$_INSTANCE_METHODS_DCUAFAssetConfiguration
+ __OBJC_$_INSTANCE_METHODS_DCUAFAssetInfo
+ __OBJC_$_INSTANCE_METHODS_DCUAFAssetManager
+ __OBJC_$_INSTANCE_METHODS_DCUAFDeviceCheckAsset
+ __OBJC_$_INSTANCE_VARIABLES_DCCryptoProxyImpl
+ __OBJC_$_INSTANCE_VARIABLES_DCEncryptionKeyAsset
+ __OBJC_$_INSTANCE_VARIABLES_DCUAFAssetConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DCUAFAssetInfo
+ __OBJC_$_INSTANCE_VARIABLES_DCUAFAssetManager
+ __OBJC_$_INSTANCE_VARIABLES_DCUAFDeviceCheckAsset
+ __OBJC_$_PROP_LIST_DCEncryptionKeyAsset
+ __OBJC_$_PROP_LIST_DCUAFAssetConfiguration
+ __OBJC_$_PROP_LIST_DCUAFAssetInfo
+ __OBJC_$_PROP_LIST_DCUAFAssetManager
+ __OBJC_$_PROP_LIST_DCUAFDeviceCheckAsset
+ __OBJC_CLASS_RO_$_DCEncryptionKeyAsset
+ __OBJC_CLASS_RO_$_DCUAFAssetConfiguration
+ __OBJC_CLASS_RO_$_DCUAFAssetInfo
+ __OBJC_CLASS_RO_$_DCUAFAssetManager
+ __OBJC_CLASS_RO_$_DCUAFDeviceCheckAsset
+ __OBJC_METACLASS_RO_$_DCEncryptionKeyAsset
+ __OBJC_METACLASS_RO_$_DCUAFAssetConfiguration
+ __OBJC_METACLASS_RO_$_DCUAFAssetInfo
+ __OBJC_METACLASS_RO_$_DCUAFAssetManager
+ __OBJC_METACLASS_RO_$_DCUAFDeviceCheckAsset
+ ___23+[DCTaskCreator create]_block_invoke.24
+ ___23+[DCTaskCreator create]_block_invoke.24.cold.1
+ ___23+[DCTaskCreator create]_block_invoke.24.cold.2
+ ___23+[DCTaskCreator create]_block_invoke.cold.1
+ ___23+[DCTaskCreator create]_block_invoke.cold.2
+ ___23+[DCTaskCreator create]_block_invoke.cold.3
+ ___36-[DCCryptoProxyImpl fetchAssetInfo:]_block_invoke
+ ___36-[DCCryptoProxyImpl fetchAssetInfo:]_block_invoke.cold.1
+ ___36-[DCCryptoProxyImpl fetchAssetInfo:]_block_invoke.cold.2
+ ___37-[DCCryptoProxyImpl _fetchPublicKey:]_block_invoke.cold.3
+ ___41-[DCUAFAssetManager fetchWithCompletion:]_block_invoke
+ ___41-[DCUAFAssetManager fetchWithCompletion:]_block_invoke.cold.1
+ ___41-[DCUAFAssetManager fetchWithCompletion:]_block_invoke.cold.2
+ ___41-[DCUAFAssetManager fetchWithCompletion:]_block_invoke.cold.3
+ ___41-[DCUAFAssetManager fetchWithCompletion:]_block_invoke.cold.4
+ ___45-[DCUAFAssetManager subscribeWithCompletion:]_block_invoke
+ ___45-[DCUAFAssetManager subscribeWithCompletion:]_block_invoke.cold.1
+ ___47-[DCUAFAssetManager unsubscribeWithCompletion:]_block_invoke
+ ___47-[DCUAFAssetManager unsubscribeWithCompletion:]_block_invoke.cold.1
+ ___47-[DCUAFAssetManager unsubscribeWithCompletion:]_block_invoke.cold.2
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e8_32bs_e24_v16?0"DCUAFAssetInfo"8ls32l8
+ ___block_descriptor_40_e8_32bs_e36_v24?0"DCUAFAssetInfo"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e21_v16?0"UAFAssetSet"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.182
+ ___block_literal_global.154
+ ___block_literal_global.184
+ ___block_literal_global.29
+ _algorithmIsPQCComposite
+ _cchybridsig_import_pubkey
+ _cchybridsig_lamps13_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_mldsa87_rsa3072_pub_ctx_init
+ _cchybridsig_verify_prehashed_with_context
+ _kUAFAssetMetadataAssetVersionKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$absoluteString
+ _objc_msgSend$assetDataURL
+ _objc_msgSend$assetName
+ _objc_msgSend$assetNamed:
+ _objc_msgSend$assetSetName
+ _objc_msgSend$configuration
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$encryptionKeyAsset
+ _objc_msgSend$fetchAssetInfo:
+ _objc_msgSend$fetchEncryptionKey
+ _objc_msgSend$fetchWithCompletion:
+ _objc_msgSend$filePath
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$initWithAssetSetName:assetName:subscriber:subscriptionName:usageType:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithFilePath:
+ _objc_msgSend$initWithName:assetDataURL:version:
+ _objc_msgSend$initWithName:assetSets:usageAliases:expires:
+ _objc_msgSend$location
+ _objc_msgSend$metadata
+ _objc_msgSend$name
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$path
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$retrieveAssetSet:usages:queue:completion:
+ _objc_msgSend$setEncryptionKeyAsset:
+ _objc_msgSend$setFilePath:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$subscribe:subscriptions:queue:completion:
+ _objc_msgSend$subscribeWithCompletion:
+ _objc_msgSend$subscribed
+ _objc_msgSend$subscriber
+ _objc_msgSend$subscriptionName
+ _objc_msgSend$subscriptionsForSubscriber:
+ _objc_msgSend$unsubscribe:subscriptionNames:queue:completion:
+ _objc_msgSend$usageType
+ _objc_msgSend$version
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
+ _pqcCompositeAlgs
+ _sha512WithMLDSA87_RSA3072_draft13
+ _sha512WithMLDSA87_RSA3072_draft7
+ _validateSignaturePQCComposite
- +[DCAsset assetWithMobileAsset:]
- +[DCAsset assetWithMobileAsset:].cold.1
- +[DCAsset assetWithMobileAsset:].cold.2
- +[DCAssetFetcher sharedFetcher]
- -[DCAsset .cxx_destruct]
- -[DCAsset description]
- -[DCAsset publicKeyRefreshInterval]
- -[DCAsset publicKey]
- -[DCAsset setPublicKey:]
- -[DCAsset setPublicKeyRefreshInterval:]
- -[DCAsset setVersion:]
- -[DCAsset version]
- -[DCAssetFetcher _assetQuery]
- -[DCAssetFetcher _fetchAssetWithContext:completionHandler:]
- -[DCAssetFetcher _fetchAssetWithContext:completionHandler:].cold.1
- -[DCAssetFetcher _handleMissingMetadataWithContext:completion:]
- -[DCAssetFetcher _handleMissingMetadataWithContext:completion:].cold.1
- -[DCAssetFetcher _handleMissingMetadataWithContext:completion:].cold.2
- -[DCAssetFetcher _handleMissingMetadataWithContext:completion:].cold.3
- -[DCAssetFetcher _handleSuccessForQuery:completion:]
- -[DCAssetFetcher _handleSuccessForQuery:completion:].cold.1
- -[DCAssetFetcher _handleSuccessForQuery:completion:].cold.2
- -[DCAssetFetcher _queryMetadataWithContext:completion:]
- -[DCAssetFetcher _queryMetadataWithContext:completion:].cold.1
- -[DCAssetFetcher _queryMetadataWithContext:completion:].cold.2
- -[DCAssetFetcher _validateAsset:error:]
- -[DCAssetFetcher _validateAsset:error:].cold.1
- -[DCAssetFetcher fetchPublicKeyAssetWithCompletion:]
- -[DCAssetFetcher initiateMetadataFetchIgnoringCachesWithCompletion:]
- -[DCAssetFetcher initiateMetadataFetchIgnoringCachesWithCompletion:].cold.1
- -[DCAssetFetcherContext allowCatalogRefresh]
- -[DCAssetFetcherContext description]
- -[DCAssetFetcherContext ignoreCachedMetadata]
- -[DCAssetFetcherContext setAllowCatalogRefresh:]
- -[DCAssetFetcherContext setIgnoreCachedMetadata:]
- -[DCDDeviceMetadata baaSignatureForData:completion:]
- -[DCDDeviceMetadata baaSignaturesForData:completion:]
- _ASAttributeContentVersion
- _OBJC_CLASS_$_DCAsset
- _OBJC_CLASS_$_DCAssetFetcher
- _OBJC_CLASS_$_DCAssetFetcherContext
- _OBJC_CLASS_$_MAAsset
- _OBJC_CLASS_$_MAAssetQuery
- _OBJC_IVAR_$_DCAsset._publicKey
- _OBJC_IVAR_$_DCAsset._publicKeyRefreshInterval
- _OBJC_IVAR_$_DCAsset._version
- _OBJC_IVAR_$_DCAssetFetcherContext._allowCatalogRefresh
- _OBJC_IVAR_$_DCAssetFetcherContext._ignoreCachedMetadata
- _OBJC_METACLASS_$_DCAsset
- _OBJC_METACLASS_$_DCAssetFetcher
- _OBJC_METACLASS_$_DCAssetFetcherContext
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_48
- _OUTLINED_FUNCTION_54
- _OUTLINED_FUNCTION_62
- _OUTLINED_FUNCTION_68
- _X509ExtensionParseMFIAuthv3Leaf
- __OBJC_$_CLASS_METHODS_DCAsset
- __OBJC_$_CLASS_METHODS_DCAssetFetcher
- __OBJC_$_INSTANCE_METHODS_DCAsset
- __OBJC_$_INSTANCE_METHODS_DCAssetFetcher
- __OBJC_$_INSTANCE_METHODS_DCAssetFetcherContext
- __OBJC_$_INSTANCE_VARIABLES_DCAsset
- __OBJC_$_INSTANCE_VARIABLES_DCAssetFetcherContext
- __OBJC_$_PROP_LIST_DCAsset
- __OBJC_$_PROP_LIST_DCAssetFetcherContext
- __OBJC_CLASS_RO_$_DCAsset
- __OBJC_CLASS_RO_$_DCAssetFetcher
- __OBJC_CLASS_RO_$_DCAssetFetcherContext
- __OBJC_METACLASS_RO_$_DCAsset
- __OBJC_METACLASS_RO_$_DCAssetFetcher
- __OBJC_METACLASS_RO_$_DCAssetFetcherContext
- ___23+[DCTaskCreator create]_block_invoke_2
- ___23+[DCTaskCreator create]_block_invoke_2.cold.1
- ___23+[DCTaskCreator create]_block_invoke_2.cold.2
- ___23+[DCTaskCreator create]_block_invoke_2.cold.3
- ___31+[DCAssetFetcher sharedFetcher]_block_invoke
- ___63-[DCAssetFetcher _handleMissingMetadataWithContext:completion:]_block_invoke
- ___63-[DCAssetFetcher _handleMissingMetadataWithContext:completion:]_block_invoke.cold.1
- ___68-[DCAssetFetcher initiateMetadataFetchIgnoringCachesWithCompletion:]_block_invoke
- ___68-[DCAssetFetcher initiateMetadataFetchIgnoringCachesWithCompletion:]_block_invoke.cold.1
- ___block_descriptor_32_e8_v16?0q8l
- ___block_descriptor_40_e8_32bs_e29_v24?0"DCAsset"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v16?0q8ls48l8s32l8s40l8
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.181
- ___block_literal_global.153
- ___block_literal_global.183
- ___block_literal_global.356
- ___block_literal_global.8
- _objc_msgSend$_assetQuery
- _objc_msgSend$_fetchAssetWithContext:completionHandler:
- _objc_msgSend$_handleMissingMetadataWithContext:completion:
- _objc_msgSend$_handleSuccessForQuery:completion:
- _objc_msgSend$_queryMetadataWithContext:completion:
- _objc_msgSend$_validateAsset:error:
- _objc_msgSend$allowCatalogRefresh
- _objc_msgSend$assetProperty:
- _objc_msgSend$assetWithMobileAsset:
- _objc_msgSend$attributes
- _objc_msgSend$doubleValue
- _objc_msgSend$fetchPublicKeyAssetWithCompletion:
- _objc_msgSend$firstObject
- _objc_msgSend$ignoreCachedMetadata
- _objc_msgSend$initWithType:
- _objc_msgSend$initiateMetadataFetchIgnoringCachesWithCompletion:
- _objc_msgSend$publicKeyRefreshInterval
- _objc_msgSend$queryMetaDataSync
- _objc_msgSend$results
- _objc_msgSend$setAllowCatalogRefresh:
- _objc_msgSend$setIgnoreCachedMetadata:
- _objc_msgSend$setPublicKeyRefreshInterval:
- _objc_msgSend$setVersion:
- _objc_msgSend$sharedFetcher
- _objc_msgSend$sharedInstance
- _objc_msgSend$startCatalogDownload:then:
- _objc_msgSend$state
- _objc_msgSend$unsignedIntegerValue
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x27
- _sharedFetcher.onceToken
- _sharedFetcher.sharedFetcher
CStrings:
+ "%25s:%-5d Already subscribed to UAF asset. { taskID=%s }"
+ "%25s:%-5d Failed to access system task object."
+ "%25s:%-5d Failed to fetch TwoBit UAF asset. { error=%@ }"
+ "%25s:%-5d Failed to fetch asset from asset set. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to fetch asset location. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to fetch asset set. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to fetch asset version. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to fetch encryption key from asset, configuring fallback."
+ "%25s:%-5d Failed to find Two Bit dictionary in configurations. { configurations=%@ }"
+ "%25s:%-5d Failed to find encoded public key in configurations. { configurations=%@ }"
+ "%25s:%-5d Failed to initialize asset configuration."
+ "%25s:%-5d Failed to parse configurations file data. { filePath=%@ }"
+ "%25s:%-5d Failed to parse configurations file. { filePath=%@ }"
+ "%25s:%-5d Failed to subscribe to UAF asset. { taskID=%s, error=%@ }"
+ "%25s:%-5d Failed to subscribe to asset. { error=%{public}@, assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Failed to unsubscribe to asset set. { error=%{public}@, assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Fetched asset. { assetInfo={ %@ } }"
+ "%25s:%-5d Fetched configurations file path. { filePath=%@ }"
+ "%25s:%-5d Fetched encryption key from asset. { key=%@ }"
+ "%25s:%-5d No asset info found, configuring fallback."
+ "%25s:%-5d Subscribed to UAF asset. { taskID=%s }"
+ "%25s:%-5d Subscription to asset set already exists for subscriber. { %{public}@, assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Subscription to asset set already exists for subscriber. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Subscription to asset set does not exist for subscriber. { assetConfiguration { %{public}@ } }"
+ "%25s:%-5d Unsubscribed from UAF asset set. { assetConfiguration { %{public}@ } }"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCEncryptionKeyAsset.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCUAFAssetManager.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCUAFDeviceCheckAsset.m"
+ "1"
+ "1.0.0"
+ "TwoBit"
+ "assetSetName=%@, subscriber=%@, subscriptionName=%@"
+ "com.apple.devicecheck.two.bit"
+ "com.apple.devicecheck.twobit"
+ "com.apple.devicecheck.uafassetmanager"
+ "configurations.plist"
+ "devicecheck.twobit"
+ "encodedPublicKey"
+ "local-asset"
+ "localAssetDataFilePath"
+ "twobit.encryption"
+ "v16@?0@\"DCUAFAssetInfo\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"UAFAssetSet\"8"
+ "v24@?0@\"DCUAFAssetInfo\"8@\"NSError\"16"
+ "{ name=%@, assetDataURL=%@, version=%@ }"
- "!"
- "#16@0:8"
- "%25s:%-5d Attempting to download catalog."
- "%25s:%-5d Attempting to fetch asset, querying metadata. { context=%@ }"
- "%25s:%-5d Attempting to validate asset: { asset=%@, state=%ld, attributes=%@ }"
- "%25s:%-5d Downloaded catalog. { result=%ld }"
- "%25s:%-5d Executed query successfully. { numResults=%lu }"
- "%25s:%-5d Failed to fetch catalog, not allowed."
- "%25s:%-5d Failed to fetch mobile asset, using locally cached public key. { error=%@ }"
- "%25s:%-5d Failed to initiate metadata fetch. { taskID=%s }"
- "%25s:%-5d Failed to parse asset, public key is missing."
- "%25s:%-5d Failed to query metadata. { result=%ld }"
- "%25s:%-5d Failed to to initiate metadata fetch. { taskID=%s, error=%@ }"
- "%25s:%-5d Fetching asset. { context=%@ }"
- "%25s:%-5d Initiated MobileAsset fetch. { taskID=%s }"
- "%25s:%-5d Initiated an out of band catalog download completed. { result=%ld }"
- "%25s:%-5d Initiating an out of band catalog download"
- "%25s:%-5d Parsed asset. { asset=%@ }"
- "%25s:%-5d Query sync result indicated missing asset catalog."
- "%25s:%-5d Refreshed mobile asset and fetched remote public key."
- "%25s:%-5d Unexpected result count. { numResults=%lu }"
- ".cxx_destruct"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCAsset.m"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TwoBit/DeviceCheckInternal/Source/Core/Mobile Asset/DCAssetFetcher.m"
- "<%@: %p - refreshAllowed: %d, ignoreMetadataCache: %d>"
- "<%@: %p - version: %lu, refreshInterval: %f>"
- "@\"<DCCryptoProxy>\""
- "@\"DCContext\""
- "@\"DCCryptoProxyImpl\""
- "@\"NSData\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUserDefaults\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^@24"
- "@32@0:8q16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16^{__SecKey=}24^@32"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16d24"
- "DCAsset"
- "DCAssetFetcher"
- "DCAssetFetcherContext"
- "DCBAASigner"
- "DCBAASigningController"
- "DCBGSTask"
- "DCBGSTaskController"
- "DCCertificateGenerator"
- "DCContext"
- "DCCryptoProxy"
- "DCCryptoProxyImpl"
- "DCCryptoUtilities"
- "DCDDeviceMetadata"
- "DCTaskCreator"
- "DeviceCheck"
- "I16@0:8"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q"
- "Q16@0:8"
- "Signing"
- "T#,R"
- "T@\"DCBAASigner\",R,N"
- "T@\"DCContext\",&,N,V_context"
- "T@\"DCCryptoProxyImpl\",&,N,V_cryptoProxy"
- "T@\"NSData\",&,N,V_publicKey"
- "T@\"NSData\",C,N,V_publicKey"
- "T@\"NSMutableArray\",&,N,V_tasks"
- "T@\"NSNumber\",&,N,V_refreshInterval"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_expiryQueue"
- "T@\"NSString\",&,N,V_observerID"
- "T@\"NSString\",&,N,V_taskID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,V_clientAppID"
- "T@\"NSString\",R,C"
- "T@\"NSUserDefaults\",&,N,V_defaultsSuite"
- "T@?,C,N,V_taskHandler"
- "TB,N,V_allowCatalogRefresh"
- "TB,N,V_ignoreCachedMetadata"
- "TB,R"
- "TQ,N,V_version"
- "TQ,R"
- "Td,N,V_publicKeyRefreshInterval"
- "UTF8String"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_allowCatalogRefresh"
- "_assetQuery"
- "_attestationWithCertificates:error:"
- "_context"
- "_cryptoProxy"
- "_defaultsSuite"
- "_expiryQueue"
- "_fetchAssetWithContext:completionHandler:"
- "_fetchPublicKey:"
- "_handleMissingMetadataWithContext:completion:"
- "_handleSuccessForQuery:completion:"
- "_ignoreCachedMetadata"
- "_observerID"
- "_publicKey"
- "_publicKeyRefreshInterval"
- "_queryMetadataWithContext:completion:"
- "_refreshInterval"
- "_signatureForData:withReferenceKey:error:"
- "_taskHandler"
- "_taskID"
- "_tasks"
- "_validateAsset:error:"
- "_version"
- "addObject:"
- "addObserver:forKeyPath:options:context:"
- "allowCatalogRefresh"
- "appendBytes:length:"
- "appendData:"
- "arrayWithObjects:count:"
- "assetProperty:"
- "assetWithMobileAsset:"
- "attributes"
- "autorelease"
- "baaSignatureForData:completion:"
- "baaSignaturesForData:completion:"
- "base64EncodedDataWithOptions:"
- "base64EncodedStringWithOptions:"
- "boolForKey:"
- "bytes"
- "class"
- "clientAppID"
- "com.apple.MobileAsset.DeviceCheck"
- "com.apple.devicecheck.pubvalue"
- "com.apple.devicecheck.refreshtimer"
- "com.apple.twobit.fetcherror"
- "conformsToProtocol:"
- "context"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "create"
- "createPEMCertificateChainFrom:completion:"
- "cryptoProxy"
- "d"
- "d16@0:8"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithJSONObject:options:error:"
- "date"
- "dc_compressedData:"
- "dc_errorWithCode:"
- "dc_errorWithCode:userInfo:"
- "debugDescription"
- "decodeObjectOfClass:forKey:"
- "defaultsSuite"
- "description"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encryptData:serverSyncedDate:error:"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "expiryQueue"
- "fetchOpaqueBlobWithContext:completion:"
- "fetchPublicKeyAssetWithCompletion:"
- "fetchTaskForTaskIdentifier:"
- "firstObject"
- "generateCertificateChainWithCompletion:"
- "generateEncryptedBlobWithCompletion:"
- "generateEncryptedCertificateChainWithCompletion:"
- "generateTTL"
- "getBytes:range:"
- "handleTask:shouldExit:"
- "hash"
- "i16@0:8"
- "identifier"
- "identityCertificateOptions"
- "ignoreCachedMetadata"
- "init"
- "initWithBytes:length:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithContext:cryptoProxy:"
- "initWithContext:publicKey:"
- "initWithSuiteName:"
- "initWithTaskIdentifier:observerIdentifier:"
- "initWithType:"
- "initiateMetadataFetchIgnoringCachesWithCompletion:"
- "integerForKey:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNSDate:"
- "isProxy"
- "isVirtualMachine"
- "keybagHandle"
- "length"
- "localizedDescription"
- "numberWithDouble:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "observerID"
- "parseDERCertificatesFromChain:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "publicKey"
- "publicKeyRefreshInterval"
- "queryMetaDataSync"
- "refreshInterval"
- "registerForTask:"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "release"
- "replaceObjectAtIndex:withObject:"
- "respondsToSelector:"
- "results"
- "retain"
- "retainCount"
- "self"
- "setAllowCatalogRefresh:"
- "setClientAppID:"
- "setContext:"
- "setCryptoProxy:"
- "setDefaultsSuite:"
- "setExpirationHandler:"
- "setExpiryQueue:"
- "setIgnoreCachedMetadata:"
- "setInterval:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setObserverID:"
- "setPublicKey:"
- "setPublicKeyRefreshInterval:"
- "setRefreshInterval:"
- "setTaskCompleted"
- "setTaskHandler:"
- "setTaskID:"
- "setTasks:"
- "setVersion:"
- "sharedFetcher"
- "sharedInstance"
- "sharedScheduler"
- "sharedSigner"
- "signatureForData:completion:"
- "signaturesForData:completion:"
- "startCatalogDownload:then:"
- "state"
- "stringWithFormat:"
- "substringWithRange:"
- "superclass"
- "supportsSecureCoding"
- "taskHandler"
- "taskID"
- "taskRequestForIdentifier:"
- "tasks"
- "timeIntervalSince1970"
- "unsignedIntegerValue"
- "updateTaskRequest:error:"
- "updateTaskWithIdentifier:withRefreshInterval:"
- "v16@0:8"
- "v16@?0q8"
- "v20@0:8B16"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@?0@\"DCAsset\"8@\"NSError\"16"
- "v32@0:8@\"DCContext\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSData\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v32@0:8@16^B24"
- "v48@0:8@16@24@32^v40"
- "version"
- "zone"

```
