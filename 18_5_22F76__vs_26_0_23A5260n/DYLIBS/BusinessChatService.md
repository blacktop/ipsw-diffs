## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`

```diff

-30095.35.3.18.4
-  __TEXT.__text: 0x73550
-  __TEXT.__auth_stubs: 0x9f0
-  __TEXT.__objc_methlist: 0x81b4
-  __TEXT.__const: 0x210
-  __TEXT.__cstring: 0x82ee
-  __TEXT.__oslogstring: 0x476d
-  __TEXT.__gcc_except_tab: 0xb3c
-  __TEXT.__ustring: 0x5b0
-  __TEXT.__unwind_info: 0x1740
-  __TEXT.__objc_classname: 0x171e
-  __TEXT.__objc_methname: 0xe029
-  __TEXT.__objc_methtype: 0x323f
-  __TEXT.__objc_stubs: 0x9880
-  __DATA_CONST.__got: 0x408
-  __DATA_CONST.__const: 0x1be0
-  __DATA_CONST.__objc_classlist: 0x4b8
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x2f8
+30109.30.5.20.1
+  __TEXT.__text: 0x6d060
+  __TEXT.__auth_stubs: 0x9c0
+  __TEXT.__objc_methlist: 0x788c
+  __TEXT.__const: 0x240
+  __TEXT.__cstring: 0x8a70
+  __TEXT.__oslogstring: 0x4d89
+  __TEXT.__gcc_except_tab: 0x7c0
+  __TEXT.__unwind_info: 0x1548
+  __TEXT.__objc_classname: 0x1755
+  __TEXT.__objc_methname: 0xacea
+  __TEXT.__objc_methtype: 0x3153
+  __TEXT.__objc_stubs: 0x79e0
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__const: 0x1ce0
+  __DATA_CONST.__objc_classlist: 0x4a0
+  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x300
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3168
-  __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x398
-  __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x508
-  __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x5da0
-  __AUTH_CONST.__objc_const: 0x104c8
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0xdb90
+  __DATA_CONST.__objc_selrefs: 0x2748
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_superrefs: 0x388
+  __AUTH_CONST.__auth_got: 0x4f0
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x4920
+  __AUTH_CONST.__objc_const: 0xfba8
+  __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x4c8
+  __DATA.__data: 0x2400
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x2b8
-  __DATA_DIRTY.__objc_data: 0x2ee0
-  __DATA_DIRTY.__bss: 0x190
+  __DATA_DIRTY.__objc_ivar: 0x2f8
+  __DATA_DIRTY.__objc_data: 0x2cb0
+  __DATA_DIRTY.__bss: 0xa8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor
+  - /System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation
   - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4A223F27-65A9-3978-95DE-CD3D48C3A833
-  Functions: 2569
-  Symbols:   9071
-  CStrings:  5050
+  UUID: 75B1BFE7-195B-35A8-8A27-13ECD471DB41
+  Functions: 2368
+  Symbols:   8336
+  CStrings:  4359
 
Symbols:
+ +[BCSWebPresentmentItem supportsSecureCoding]
+ +[BCSWebPresentmentItem(Caching) itemFromStatement:]
+ +[BCSWebPresentmentItemIdentifier _truncatedHashForBrandID:]
+ +[BCSWebPresentmentItemIdentifier supportsSecureCoding]
+ +[BCSWebPresentmentParquetMessage nameType]
+ +[BCSWebPresentmentPermissionsItem supportsSecureCoding]
+ +[BCSWebPresentmentPermissionsItem(Caching) itemFromStatement:]
+ +[BCSWebPresentmentPersistentStore debugQueueName]
+ -[BCSBusinessQueryController fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:]
+ -[BCSBusinessQueryController fetchWebPresentmentPermissionsWithIdentifier:forClientBundleID:completion:]
+ -[BCSBusinessQueryController initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:businessEmailMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:businessEmailConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:businessEmailShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:businessEmailItemResolver:webPresentmentItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:]
+ -[BCSBusinessQueryController initWithChatSuggestMegashardFetcher:businessLinkMegashardFetcher:businessCallerMegashardFetcher:businessEmailMegashardFetcher:shardCache:cacheManager:chatSuggestRemoteFetcher:businessLinkRemoteFetcher:businessCallerRemoteFetcher:businessEmailRemoteFetcher:webPresentmentRemoteFetcher:userDefaults:metricFactory:]
+ -[BCSBusinessQueryService fetchBrandWithIdentifier:serviceType:completion:]
+ -[BCSBusinessQueryService fetchWebPresentmentPermissionsWithIdentifier:completion:]
+ -[BCSMeasurementFactory webPresentmentFetchTimingMeasurementForItemIdentifier:]
+ -[BCSPIRServerEnvironment pirCompressionType]
+ -[BCSQuery initWithItemIdentifier:clientBundleId:shardType:cacheOnly:skipRegistrationCheck:skipConfigFetch:]
+ -[BCSQuery setSkipConfigFetch:]
+ -[BCSQuery skipConfigFetch]
+ -[BCSWebPresentmentItem .cxx_destruct]
+ -[BCSWebPresentmentItem brandId]
+ -[BCSWebPresentmentItem businessId]
+ -[BCSWebPresentmentItem companyId]
+ -[BCSWebPresentmentItem copyWithZone:]
+ -[BCSWebPresentmentItem debugDescription]
+ -[BCSWebPresentmentItem encodeWithCoder:]
+ -[BCSWebPresentmentItem hash]
+ -[BCSWebPresentmentItem identifier]
+ -[BCSWebPresentmentItem initWithBrandID:defaultsDictionary:]
+ -[BCSWebPresentmentItem initWithBrandID:localizedNames:]
+ -[BCSWebPresentmentItem initWithBrandID:localizedNames:businessId:companyId:]
+ -[BCSWebPresentmentItem initWithCoder:]
+ -[BCSWebPresentmentItem initWithMessage:logoURL:]
+ -[BCSWebPresentmentItem isEqual:]
+ -[BCSWebPresentmentItem itemIdentifier]
+ -[BCSWebPresentmentItem itemTTL]
+ -[BCSWebPresentmentItem localizedNames]
+ -[BCSWebPresentmentItem logoData]
+ -[BCSWebPresentmentItem logoFormat]
+ -[BCSWebPresentmentItem logoURL]
+ -[BCSWebPresentmentItem matchesItemIdentifying:]
+ -[BCSWebPresentmentItem message]
+ -[BCSWebPresentmentItem name]
+ -[BCSWebPresentmentItem setLogoURL:]
+ -[BCSWebPresentmentItem setMessage:]
+ -[BCSWebPresentmentItem truncatedHash]
+ -[BCSWebPresentmentItem type]
+ -[BCSWebPresentmentItem(Caching) updateStatementValues:withItemIdentifier:]
+ -[BCSWebPresentmentItemIdentifier .cxx_destruct]
+ -[BCSWebPresentmentItemIdentifier brandId]
+ -[BCSWebPresentmentItemIdentifier computedTruncatedHash]
+ -[BCSWebPresentmentItemIdentifier copyWithZone:]
+ -[BCSWebPresentmentItemIdentifier encodeWithCoder:]
+ -[BCSWebPresentmentItemIdentifier initWithBrandID:serverType:]
+ -[BCSWebPresentmentItemIdentifier initWithCoder:]
+ -[BCSWebPresentmentItemIdentifier itemIdentifier]
+ -[BCSWebPresentmentItemIdentifier matchesItemIdentifying:]
+ -[BCSWebPresentmentItemIdentifier pirKey]
+ -[BCSWebPresentmentItemIdentifier serverType]
+ -[BCSWebPresentmentItemIdentifier truncatedHash]
+ -[BCSWebPresentmentItemIdentifier type]
+ -[BCSWebPresentmentItemResolver .cxx_destruct]
+ -[BCSWebPresentmentItemResolver _metadataMatching:metric:completion:]
+ -[BCSWebPresentmentItemResolver _permissionsMatching:metric:completion:]
+ -[BCSWebPresentmentItemResolver cachedItemMatching:]
+ -[BCSWebPresentmentItemResolver initWithMetadataEnvironment:permissionsEnvironment:itemCache:cacheSkipper:metricFactory:]
+ -[BCSWebPresentmentItemResolver itemCacheSkipper]
+ -[BCSWebPresentmentItemResolver itemCache]
+ -[BCSWebPresentmentItemResolver itemMatching:metric:completion:]
+ -[BCSWebPresentmentItemResolver metricFactory]
+ -[BCSWebPresentmentItemResolver pirFetchMetadata]
+ -[BCSWebPresentmentItemResolver pirFetchPermissions]
+ -[BCSWebPresentmentItemResolver setMetricFactory:]
+ -[BCSWebPresentmentItemResolver setPirFetchMetadata:]
+ -[BCSWebPresentmentItemResolver setPirFetchPermissions:]
+ -[BCSWebPresentmentLocalizedString .cxx_destruct]
+ -[BCSWebPresentmentLocalizedString copyTo:]
+ -[BCSWebPresentmentLocalizedString copyWithZone:]
+ -[BCSWebPresentmentLocalizedString description]
+ -[BCSWebPresentmentLocalizedString dictionaryRepresentation]
+ -[BCSWebPresentmentLocalizedString hasIsDefault]
+ -[BCSWebPresentmentLocalizedString hasLocale]
+ -[BCSWebPresentmentLocalizedString hasText]
+ -[BCSWebPresentmentLocalizedString hash]
+ -[BCSWebPresentmentLocalizedString isDefault]
+ -[BCSWebPresentmentLocalizedString isEqual:]
+ -[BCSWebPresentmentLocalizedString locale]
+ -[BCSWebPresentmentLocalizedString mergeFrom:]
+ -[BCSWebPresentmentLocalizedString readFrom:]
+ -[BCSWebPresentmentLocalizedString setHasIsDefault:]
+ -[BCSWebPresentmentLocalizedString setIsDefault:]
+ -[BCSWebPresentmentLocalizedString setLocale:]
+ -[BCSWebPresentmentLocalizedString setText:]
+ -[BCSWebPresentmentLocalizedString text]
+ -[BCSWebPresentmentLocalizedString writeTo:]
+ -[BCSWebPresentmentParquetMessage .cxx_destruct]
+ -[BCSWebPresentmentParquetMessage addName:]
+ -[BCSWebPresentmentParquetMessage bcBrandId]
+ -[BCSWebPresentmentParquetMessage businessId]
+ -[BCSWebPresentmentParquetMessage clearNames]
+ -[BCSWebPresentmentParquetMessage companyId]
+ -[BCSWebPresentmentParquetMessage copyTo:]
+ -[BCSWebPresentmentParquetMessage copyWithZone:]
+ -[BCSWebPresentmentParquetMessage description]
+ -[BCSWebPresentmentParquetMessage dictionaryRepresentation]
+ -[BCSWebPresentmentParquetMessage hasBcBrandId]
+ -[BCSWebPresentmentParquetMessage hasBusinessId]
+ -[BCSWebPresentmentParquetMessage hasCompanyId]
+ -[BCSWebPresentmentParquetMessage hasItemTtl]
+ -[BCSWebPresentmentParquetMessage hasLogoFormat]
+ -[BCSWebPresentmentParquetMessage hasLogo]
+ -[BCSWebPresentmentParquetMessage hash]
+ -[BCSWebPresentmentParquetMessage isEqual:]
+ -[BCSWebPresentmentParquetMessage itemTtl]
+ -[BCSWebPresentmentParquetMessage logoFormat]
+ -[BCSWebPresentmentParquetMessage logo]
+ -[BCSWebPresentmentParquetMessage mergeFrom:]
+ -[BCSWebPresentmentParquetMessage nameAtIndex:]
+ -[BCSWebPresentmentParquetMessage namesCount]
+ -[BCSWebPresentmentParquetMessage names]
+ -[BCSWebPresentmentParquetMessage readFrom:]
+ -[BCSWebPresentmentParquetMessage setBcBrandId:]
+ -[BCSWebPresentmentParquetMessage setBusinessId:]
+ -[BCSWebPresentmentParquetMessage setCompanyId:]
+ -[BCSWebPresentmentParquetMessage setHasItemTtl:]
+ -[BCSWebPresentmentParquetMessage setItemTtl:]
+ -[BCSWebPresentmentParquetMessage setLogo:]
+ -[BCSWebPresentmentParquetMessage setLogoFormat:]
+ -[BCSWebPresentmentParquetMessage setNames:]
+ -[BCSWebPresentmentParquetMessage writeTo:]
+ -[BCSWebPresentmentPermissionsItem .cxx_destruct]
+ -[BCSWebPresentmentPermissionsItem brandId]
+ -[BCSWebPresentmentPermissionsItem copyWithZone:]
+ -[BCSWebPresentmentPermissionsItem data]
+ -[BCSWebPresentmentPermissionsItem debugDescription]
+ -[BCSWebPresentmentPermissionsItem encodeWithCoder:]
+ -[BCSWebPresentmentPermissionsItem hash]
+ -[BCSWebPresentmentPermissionsItem identifier]
+ -[BCSWebPresentmentPermissionsItem initWithBrandID:]
+ -[BCSWebPresentmentPermissionsItem initWithBrandID:data:]
+ -[BCSWebPresentmentPermissionsItem initWithCoder:]
+ -[BCSWebPresentmentPermissionsItem isEqual:]
+ -[BCSWebPresentmentPermissionsItem itemIdentifier]
+ -[BCSWebPresentmentPermissionsItem matchesItemIdentifying:]
+ -[BCSWebPresentmentPermissionsItem setBrandId:]
+ -[BCSWebPresentmentPermissionsItem setData:]
+ -[BCSWebPresentmentPermissionsItem setIdentifier:]
+ -[BCSWebPresentmentPermissionsItem truncatedHash]
+ -[BCSWebPresentmentPermissionsItem type]
+ -[BCSWebPresentmentPermissionsItem(Caching) updateStatementValues:withItemIdentifier:]
+ -[BCSWebPresentmentPersistentStore databasePath]
+ -[BCSWebPresentmentPersistentStore deleteExpiredItemsOfType:]
+ -[BCSWebPresentmentPersistentStore deleteItemMatching:]
+ -[BCSWebPresentmentPersistentStore deleteItemsOfType:]
+ -[BCSWebPresentmentPersistentStore init]
+ -[BCSWebPresentmentPersistentStore itemMatching:]
+ -[BCSWebPresentmentPersistentStore schemaVersionWillChangeForDatabase:fromSchemaVersion:toSchemaVersion:]
+ -[BCSWebPresentmentPersistentStore schemaVersion]
+ -[BCSWebPresentmentPersistentStore schema]
+ -[BCSWebPresentmentPersistentStore updateItem:withItemIdentifier:]
+ -[NSData(Compression) inflate:error:]
+ -[NSData(Compression) inflateGzipWithError:]
+ -[NSData(Compression) inflateLZRawWithError:]
+ GCC_except_table98
+ _BCSWebPresentmentLocalizedStringReadFrom
+ _BCSWebPresentmentStoreDataFromStatement
+ _BCSWebPresentmentStoreStringFromStatement
+ _BCSWebPresentmentStoreTypeForItemIdentifier
+ _OBJC_CLASS_$_BCSWebPresentmentItem
+ _OBJC_CLASS_$_BCSWebPresentmentItemIdentifier
+ _OBJC_CLASS_$_BCSWebPresentmentItemResolver
+ _OBJC_CLASS_$_BCSWebPresentmentLocalizedString
+ _OBJC_CLASS_$_BCSWebPresentmentParquetMessage
+ _OBJC_CLASS_$_BCSWebPresentmentPermissionsItem
+ _OBJC_CLASS_$_BCSWebPresentmentPersistentStore
+ _OBJC_CLASS_$_BFPhoneNumberNormalizer
+ _OBJC_IVAR_$_BCSBusinessQueryController._webPresentmentItemResolver
+ _OBJC_IVAR_$_BCSItemCache._webPresentmentStore
+ _OBJC_IVAR_$_BCSQuery._skipConfigFetch
+ _OBJC_IVAR_$_BCSUrlPattern._path
+ _OBJC_IVAR_$_BCSUrlPattern._query
+ _OBJC_IVAR_$_BCSWebPresentmentItemIdentifier._brandId
+ _OBJC_IVAR_$_BCSWebPresentmentItemIdentifier._computedTruncatedHash
+ _OBJC_IVAR_$_BCSWebPresentmentItemIdentifier._serverType
+ _OBJC_IVAR_$_BCSWebPresentmentItemResolver._itemCache
+ _OBJC_IVAR_$_BCSWebPresentmentItemResolver._itemCacheSkipper
+ _OBJC_IVAR_$_BCSWebPresentmentItemResolver._metricFactory
+ _OBJC_IVAR_$_BCSWebPresentmentItemResolver._pirFetchMetadata
+ _OBJC_IVAR_$_BCSWebPresentmentItemResolver._pirFetchPermissions
+ _OBJC_IVAR_$_BCSWebPresentmentPersistentStore._schemaVersion
+ _OBJC_METACLASS_$_BCSWebPresentmentItem
+ _OBJC_METACLASS_$_BCSWebPresentmentItemIdentifier
+ _OBJC_METACLASS_$_BCSWebPresentmentItemResolver
+ _OBJC_METACLASS_$_BCSWebPresentmentLocalizedString
+ _OBJC_METACLASS_$_BCSWebPresentmentParquetMessage
+ _OBJC_METACLASS_$_BCSWebPresentmentPermissionsItem
+ _OBJC_METACLASS_$_BCSWebPresentmentPersistentStore
+ _PBDataWriterWriteUint64Field
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_BCSProtoLocalizedStringsHelper
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSData_$_Compression
+ __OBJC_$_CATEGORY_NSArray_$_BCSProtoLocalizedStringsHelper
+ __OBJC_$_CATEGORY_NSData_$_Compression
+ __OBJC_$_CLASS_METHODS_BCSWebPresentmentItem(Caching)
+ __OBJC_$_CLASS_METHODS_BCSWebPresentmentItemIdentifier
+ __OBJC_$_CLASS_METHODS_BCSWebPresentmentParquetMessage
+ __OBJC_$_CLASS_METHODS_BCSWebPresentmentPermissionsItem(Caching)
+ __OBJC_$_CLASS_METHODS_BCSWebPresentmentPersistentStore
+ __OBJC_$_CLASS_PROP_LIST_BCSWebPresentmentItem
+ __OBJC_$_CLASS_PROP_LIST_BCSWebPresentmentItemIdentifier
+ __OBJC_$_CLASS_PROP_LIST_BCSWebPresentmentPermissionsItem
+ __OBJC_$_INSTANCE_METHODS_BCSWebPresentmentItem(Caching)
+ __OBJC_$_INSTANCE_METHODS_BCSWebPresentmentItemIdentifier
+ __OBJC_$_INSTANCE_METHODS_BCSWebPresentmentItemResolver
+ __OBJC_$_INSTANCE_METHODS_BCSWebPresentmentLocalizedString
+ __OBJC_$_INSTANCE_METHODS_BCSWebPresentmentParquetMessage
+ __OBJC_$_INSTANCE_METHODS_BCSWebPresentmentPermissionsItem(Caching)
+ __OBJC_$_INSTANCE_METHODS_BCSWebPresentmentPersistentStore
+ __OBJC_$_INSTANCE_VARIABLES_BCSWebPresentmentItem
+ __OBJC_$_INSTANCE_VARIABLES_BCSWebPresentmentItemIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_BCSWebPresentmentItemResolver
+ __OBJC_$_INSTANCE_VARIABLES_BCSWebPresentmentLocalizedString
+ __OBJC_$_INSTANCE_VARIABLES_BCSWebPresentmentParquetMessage
+ __OBJC_$_INSTANCE_VARIABLES_BCSWebPresentmentPermissionsItem
+ __OBJC_$_INSTANCE_VARIABLES_BCSWebPresentmentPersistentStore
+ __OBJC_$_PROP_LIST_BCSWebPresentmentItem
+ __OBJC_$_PROP_LIST_BCSWebPresentmentItemIdentifier
+ __OBJC_$_PROP_LIST_BCSWebPresentmentItemResolver
+ __OBJC_$_PROP_LIST_BCSWebPresentmentLocalizedString
+ __OBJC_$_PROP_LIST_BCSWebPresentmentParquetMessage
+ __OBJC_$_PROP_LIST_BCSWebPresentmentPermissionsItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSXPCDaemonWebPresentmentDaemonInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCSXPCDaemonWebPresentmentDaemonInterface
+ __OBJC_CLASS_PROTOCOLS_$_BCSWebPresentmentItem
+ __OBJC_CLASS_PROTOCOLS_$_BCSWebPresentmentItemIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_BCSWebPresentmentItemResolver
+ __OBJC_CLASS_PROTOCOLS_$_BCSWebPresentmentLocalizedString
+ __OBJC_CLASS_PROTOCOLS_$_BCSWebPresentmentParquetMessage
+ __OBJC_CLASS_PROTOCOLS_$_BCSWebPresentmentPermissionsItem
+ __OBJC_CLASS_PROTOCOLS_$_BCSWebPresentmentPersistentStore
+ __OBJC_CLASS_RO_$_BCSWebPresentmentItem
+ __OBJC_CLASS_RO_$_BCSWebPresentmentItemIdentifier
+ __OBJC_CLASS_RO_$_BCSWebPresentmentItemResolver
+ __OBJC_CLASS_RO_$_BCSWebPresentmentLocalizedString
+ __OBJC_CLASS_RO_$_BCSWebPresentmentParquetMessage
+ __OBJC_CLASS_RO_$_BCSWebPresentmentPermissionsItem
+ __OBJC_CLASS_RO_$_BCSWebPresentmentPersistentStore
+ __OBJC_LABEL_PROTOCOL_$_BCSXPCDaemonWebPresentmentDaemonInterface
+ __OBJC_METACLASS_RO_$_BCSWebPresentmentItem
+ __OBJC_METACLASS_RO_$_BCSWebPresentmentItemIdentifier
+ __OBJC_METACLASS_RO_$_BCSWebPresentmentItemResolver
+ __OBJC_METACLASS_RO_$_BCSWebPresentmentLocalizedString
+ __OBJC_METACLASS_RO_$_BCSWebPresentmentParquetMessage
+ __OBJC_METACLASS_RO_$_BCSWebPresentmentPermissionsItem
+ __OBJC_METACLASS_RO_$_BCSWebPresentmentPersistentStore
+ __OBJC_PROTOCOL_$_BCSXPCDaemonWebPresentmentDaemonInterface
+ __OBJC_PROTOCOL_REFERENCE_$_BCSItemIdentifying
+ ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.248
+ ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.251
+ ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.258
+ ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.260
+ ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke_2.259
+ ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke_2.267
+ ___100-[BCSRemoteFetchCloudKit fetchItemsWithBucketStartIndex:endIndex:type:forClientBundleID:completion:]_block_invoke.134
+ ___104-[BCSBusinessQueryController fetchWebPresentmentPermissionsWithIdentifier:forClientBundleID:completion:]_block_invoke
+ ___109-[BCSBusinessQueryController lookupBloomFiltersForURL:chopURL:forClientBundleID:registeredMetric:completion:]_block_invoke.38
+ ___134-[BCSBusinessQueryController fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:metadataCallback:logoURLCallback:completion:]_block_invoke.202
+ ___39-[BCSMegashardFetcher addFetchTrigger:]_block_invoke.13
+ ___58-[BCSRemoteFetchPIR fetchDataMatching:timeout:completion:]_block_invoke.90
+ ___58-[BCSRemoteFetchPIR fetchDataMatching:timeout:completion:]_block_invoke.92
+ ___60-[BCSBusinessQueryController fetchItemWithQuery:completion:]_block_invoke.162
+ ___61-[BCSBusinessQueryController fetchShardWithQuery:completion:]_block_invoke.51
+ ___62-[BCSBusinessQueryController fetchShardsWithQuery:completion:]_block_invoke.60
+ ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.291
+ ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.292
+ ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.293
+ ___69-[BCSWebPresentmentItemResolver _metadataMatching:metric:completion:]_block_invoke
+ ___71-[BCSRemoteFetchCloudKit fetchShardMatching:clientBundleID:completion:]_block_invoke.105
+ ___72-[BCSWebPresentmentItemResolver _permissionsMatching:metric:completion:]_block_invoke
+ ___75-[BCSBusinessQueryService fetchBrandWithIdentifier:serviceType:completion:]_block_invoke
+ ___75-[BCSCacheManager initWithBloomFilterShardCache:domainItemCache:itemCache:]_block_invoke.23
+ ___76-[BCSBusinessQueryController fetchIsBusinessRegisteredWithQuery:completion:]_block_invoke.67
+ ___76-[BCSMegashardFetcher _fetchMegashardForReason:withBGSystemTask:completion:]_block_invoke.17
+ ___76-[BCSMegashardFetcher _fetchMegashardForReason:withBGSystemTask:completion:]_block_invoke_2.19
+ ___76-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke.42
+ ___79-[BCSBusinessQueryController fetchAreBusinessesRegisteredWithQuery:completion:]_block_invoke.139
+ ___79-[BCSBusinessQueryController fetchItemsWithQuery:perItemCompletion:completion:]_block_invoke.174
+ ___83-[BCSBusinessQueryService fetchWebPresentmentPermissionsWithIdentifier:completion:]_block_invoke
+ ___86-[BCSBusinessQueryController fetchLinkItemModelWithHash:forClientBundleID:completion:]_block_invoke.40
+ ___87-[BCSRemoteFetchCloudKit fetchConfigItemWithType:clientBundleID:systemTask:completion:]_block_invoke.90
+ ___89-[BCSBusinessQueryController fetchBusinessMetadataForEmail:forClientBundleID:completion:]_block_invoke.224
+ ___90-[BCSRemoteFetchCloudKit fetchMegashardItemWithType:clientBundleID:systemTask:completion:]_block_invoke.119
+ ___90-[BCSRemoteFetchCloudKit fetchMegashardItemWithType:clientBundleID:systemTask:completion:]_block_invoke.121
+ ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.28
+ ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.31
+ ___94-[BCSBusinessQueryController isBusinessRegisteredForURL:chopURL:forClientBundleID:completion:]_block_invoke.35
+ ___96-[BCSBusinessQueryController fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:]_block_invoke
+ ___96-[BCSBusinessQueryController fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:]_block_invoke.283
+ ___96-[BCSBusinessQueryController fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:]_block_invoke_2
+ ___98-[BCSBusinessQueryController fetchBusinessLogoForBusinessIdentifier:forClientBundleID:completion:]_block_invoke.238
+ ___block_descriptor_40_e8_32bs_e43_v24?0"BCSWebPresentmentItem"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e41_v24?0"<BCSBusinessConfig>"8"NSError"16ls32l8s48l8s40l8
+ ___block_literal_global.25
+ _kBCSDefaultBusinessCallerPIRCompressionType
+ _kBCSDefaultBusinessEmailLogoPIRCompressionType
+ _kBCSDefaultBusinessEmailPIRCompressionType
+ _kBCSDefaultWebPresentmentCKContainerID
+ _kBCSDefaultWebPresentmentCKContainerIDCI
+ _kBCSDefaultWebPresentmentCKContainerIDQA
+ _kBCSDefaultWebPresentmentPIRCompressionType
+ _kBCSDefaultWebPresentmentPIRUseCase
+ _kBCSDefaultWebPresentmentPIRUseCaseQA
+ _kBCSDefaultWebPresentmentPermissionsPIRCompressionType
+ _kBCSDefaultWebPresentmentPermissionsPIRUseCase
+ _kBCSDefaultWebPresentmentPermissionsPIRUseCaseQA
+ _kBCSDefaultsBusinessCallerPIRCompressionType
+ _kBCSDefaultsBusinessEmailLogoPIRCompressionType
+ _kBCSDefaultsBusinessEmailPIRCompressionType
+ _kBCSDefaultsWebPresentmentCustomContainerId
+ _kBCSDefaultsWebPresentmentCustomEnvironment
+ _kBCSDefaultsWebPresentmentICloudStagingMode
+ _kBCSDefaultsWebPresentmentPIRCompressionType
+ _kBCSDefaultsWebPresentmentPIRUseCase
+ _kBCSDefaultsWebPresentmentPIRUsesCompression
+ _kBCSDefaultsWebPresentmentPermissionsPIRCompressionType
+ _kBCSDefaultsWebPresentmentPermissionsPIRUseCase
+ _kBCSDefaultsWebPresentmentPermissionsPIRUsesCompression
+ _kBCSDefaultsWebPresentmentSecondaryIdentifier
+ _kBCSDefaultsWebPresentmentSkipDiskCaching
+ _kBCSDefaultsWebPresentmentSkipEdgeCaching
+ _kBCSPIRSecondaryIdentifierForWebPresentment
+ _objc_msgSend$_permissionsMatching:metric:completion:
+ _objc_msgSend$_setError
+ _objc_msgSend$_truncatedHashForBrandID:
+ _objc_msgSend$bcBrandId
+ _objc_msgSend$brandId
+ _objc_msgSend$dataWithData:
+ _objc_msgSend$fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:
+ _objc_msgSend$fetchWebPresentmentPermissionsWithIdentifier:forClientBundleID:completion:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$hasItemTtl
+ _objc_msgSend$increaseLengthBy:
+ _objc_msgSend$inflate:error:
+ _objc_msgSend$inflateGzipWithError:
+ _objc_msgSend$inflateLZRawWithError:
+ _objc_msgSend$initWithBrandID:data:
+ _objc_msgSend$initWithBrandID:defaultsDictionary:
+ _objc_msgSend$initWithBrandID:localizedNames:businessId:companyId:
+ _objc_msgSend$initWithBrandID:serverType:
+ _objc_msgSend$initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:businessEmailMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:businessEmailConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:businessEmailShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:businessEmailItemResolver:webPresentmentItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:
+ _objc_msgSend$initWithItemIdentifier:clientBundleId:shardType:cacheOnly:skipRegistrationCheck:skipConfigFetch:
+ _objc_msgSend$itemTtl
+ _objc_msgSend$logoData
+ _objc_msgSend$pirCompressionType
+ _objc_msgSend$pirFetchPermissions
+ _objc_msgSend$position
+ _objc_msgSend$setBcBrandId:
+ _objc_msgSend$setItemTtl:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$skipConfigFetch
- +[BCSPhoneNumberNormalizer countryCode]
- +[BCSPhoneNumberNormalizer normalizedPhoneNumberForPhoneNumber:]
- +[_NBMetadataHelper CCode2CNMap]
- +[_NBMetadataHelper CN2CCodeMap]
- +[_NBMetadataHelper countryCodeFromRegionCode:]
- +[_NBMetadataHelper hasValue:]
- +[_NBMetadataHelper jsonObjectFromZippedDataWithBytes:compressedLength:expandedLength:]
- +[_NBMetadataHelper phoneNumberDataMap]
- +[_NBMetadataHelper regionCodeFromCountryCode:]
- +[_NBPhoneNumberUtil initialize]
- +[_NBPhoneNumberUtil sharedInstance]
- +[_NBRegularExpressionCache sharedInstance]
- -[BCSBusinessQueryController initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:businessEmailMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:businessEmailConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:businessEmailShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:businessEmailItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:]
- -[BCSBusinessQueryController initWithChatSuggestMegashardFetcher:businessLinkMegashardFetcher:businessCallerMegashardFetcher:businessEmailMegashardFetcher:shardCache:cacheManager:chatSuggestRemoteFetcher:businessLinkRemoteFetcher:businessCallerRemoteFetcher:businessEmailRemoteFetcher:userDefaults:metricFactory:]
- -[BCSQuery initWithItemIdentifier:clientBundleId:shardType:cacheOnly:]
- -[BCSRemoteFetchPIR decompressData:error:]
- -[NSArray(_NBAdditions) nb_safeArrayAtIndex:]
- -[NSArray(_NBAdditions) nb_safeDataAtIndex:]
- -[NSArray(_NBAdditions) nb_safeNumberAtIndex:]
- -[NSArray(_NBAdditions) nb_safeObjectAtIndex:class:]
- -[NSArray(_NBAdditions) nb_safeStringAtIndex:]
- -[_NBAsYouTypeFormatter .cxx_destruct]
- -[_NBAsYouTypeFormatter CHARACTER_CLASS_PATTERN_]
- -[_NBAsYouTypeFormatter DIGIT_PATTERN_]
- -[_NBAsYouTypeFormatter ELIGIBLE_FORMAT_PATTERN_]
- -[_NBAsYouTypeFormatter NATIONAL_PREFIX_SEPARATORS_PATTERN_]
- -[_NBAsYouTypeFormatter STANDALONE_DIGIT_PATTERN_]
- -[_NBAsYouTypeFormatter ableToExtractLongerNdd_]
- -[_NBAsYouTypeFormatter ableToFormat_]
- -[_NBAsYouTypeFormatter accruedInputWithoutFormatting_]
- -[_NBAsYouTypeFormatter accruedInput_]
- -[_NBAsYouTypeFormatter appendNationalNumber_:]
- -[_NBAsYouTypeFormatter attemptToChooseFormattingPattern_]
- -[_NBAsYouTypeFormatter attemptToChoosePatternWithPrefixExtracted_]
- -[_NBAsYouTypeFormatter attemptToExtractCountryCallingCode_]
- -[_NBAsYouTypeFormatter attemptToExtractIdd_]
- -[_NBAsYouTypeFormatter attemptToFormatAccruedDigits_]
- -[_NBAsYouTypeFormatter clear]
- -[_NBAsYouTypeFormatter createFormattingTemplate_:]
- -[_NBAsYouTypeFormatter currentFormattingPattern_]
- -[_NBAsYouTypeFormatter currentMetaData_]
- -[_NBAsYouTypeFormatter currentOutput_]
- -[_NBAsYouTypeFormatter defaultCountry_]
- -[_NBAsYouTypeFormatter defaultMetaData_]
- -[_NBAsYouTypeFormatter description]
- -[_NBAsYouTypeFormatter formattingTemplate_]
- -[_NBAsYouTypeFormatter getAvailableFormats_:]
- -[_NBAsYouTypeFormatter getFormattingTemplate_:numberFormat:]
- -[_NBAsYouTypeFormatter getMetadataForRegion_:]
- -[_NBAsYouTypeFormatter getRememberedPosition]
- -[_NBAsYouTypeFormatter initWithRegionCode:]
- -[_NBAsYouTypeFormatter initWithRegionCode:bundle:]
- -[_NBAsYouTypeFormatter init]
- -[_NBAsYouTypeFormatter inputAccruedNationalNumber_]
- -[_NBAsYouTypeFormatter inputDigit:]
- -[_NBAsYouTypeFormatter inputDigitAndRememberPosition:]
- -[_NBAsYouTypeFormatter inputDigitHelper_:]
- -[_NBAsYouTypeFormatter inputDigitWithOptionToRememberPosition_:rememberPosition:]
- -[_NBAsYouTypeFormatter inputHasFormatting_]
- -[_NBAsYouTypeFormatter inputString:]
- -[_NBAsYouTypeFormatter inputStringAndRememberPosition:]
- -[_NBAsYouTypeFormatter isCompleteNumber_]
- -[_NBAsYouTypeFormatter isDigitOrLeadingPlusSign_:]
- -[_NBAsYouTypeFormatter isExpectingCountryCallingCode_]
- -[_NBAsYouTypeFormatter isFormatEligible_:]
- -[_NBAsYouTypeFormatter isNanpaNumberWithNationalPrefix_]
- -[_NBAsYouTypeFormatter isSuccessfulFormatting]
- -[_NBAsYouTypeFormatter lastMatchPosition_]
- -[_NBAsYouTypeFormatter maybeCreateNewTemplate_]
- -[_NBAsYouTypeFormatter narrowDownPossibleFormats_:]
- -[_NBAsYouTypeFormatter nationalNumber_]
- -[_NBAsYouTypeFormatter nationalPrefixExtracted_]
- -[_NBAsYouTypeFormatter normalizeAndAccrueDigitsAndPlusSign_:rememberPosition:]
- -[_NBAsYouTypeFormatter originalPosition_]
- -[_NBAsYouTypeFormatter phoneUtil_]
- -[_NBAsYouTypeFormatter positionToRemember_]
- -[_NBAsYouTypeFormatter possibleFormats_]
- -[_NBAsYouTypeFormatter prefixBeforeNationalNumber_]
- -[_NBAsYouTypeFormatter removeLastDigitAndRememberPosition]
- -[_NBAsYouTypeFormatter removeLastDigit]
- -[_NBAsYouTypeFormatter removeNationalPrefixFromNationalNumber_]
- -[_NBAsYouTypeFormatter setAbleToFormat_:]
- -[_NBAsYouTypeFormatter setAccruedInputWithoutFormatting_:]
- -[_NBAsYouTypeFormatter setAccruedInput_:]
- -[_NBAsYouTypeFormatter setCHARACTER_CLASS_PATTERN_:]
- -[_NBAsYouTypeFormatter setCurrentFormattingPattern_:]
- -[_NBAsYouTypeFormatter setCurrentMetaData_:]
- -[_NBAsYouTypeFormatter setCurrentOutput_:]
- -[_NBAsYouTypeFormatter setDIGIT_PATTERN_:]
- -[_NBAsYouTypeFormatter setDefaultCountry_:]
- -[_NBAsYouTypeFormatter setDefaultMetaData_:]
- -[_NBAsYouTypeFormatter setELIGIBLE_FORMAT_PATTERN_:]
- -[_NBAsYouTypeFormatter setFormattingTemplate_:]
- -[_NBAsYouTypeFormatter setInputHasFormatting_:]
- -[_NBAsYouTypeFormatter setIsCompleteNumber_:]
- -[_NBAsYouTypeFormatter setIsExpectingCountryCallingCode_:]
- -[_NBAsYouTypeFormatter setLastMatchPosition_:]
- -[_NBAsYouTypeFormatter setNATIONAL_PREFIX_SEPARATORS_PATTERN_:]
- -[_NBAsYouTypeFormatter setNationalNumber_:]
- -[_NBAsYouTypeFormatter setNationalPrefixExtracted_:]
- -[_NBAsYouTypeFormatter setOriginalPosition_:]
- -[_NBAsYouTypeFormatter setPhoneUtil_:]
- -[_NBAsYouTypeFormatter setPositionToRemember_:]
- -[_NBAsYouTypeFormatter setPossibleFormats_:]
- -[_NBAsYouTypeFormatter setPrefixBeforeNationalNumber_:]
- -[_NBAsYouTypeFormatter setSTANDALONE_DIGIT_PATTERN_:]
- -[_NBAsYouTypeFormatter setShouldAddSpaceAfterNationalPrefix_:]
- -[_NBAsYouTypeFormatter shouldAddSpaceAfterNationalPrefix_]
- -[_NBMetadataHelper .cxx_destruct]
- -[_NBMetadataHelper getAllMetadata]
- -[_NBMetadataHelper getMetadataForNonGeographicalRegion:]
- -[_NBMetadataHelper getMetadataForRegion:]
- -[_NBMetadataHelper init]
- -[_NBMetadataHelper metadataCache]
- -[_NBMetadataHelper setMetadataCache:]
- -[_NBNumberFormat .cxx_destruct]
- -[_NBNumberFormat copyWithZone:]
- -[_NBNumberFormat description]
- -[_NBNumberFormat domesticCarrierCodeFormattingRule]
- -[_NBNumberFormat format]
- -[_NBNumberFormat initWithEntry:]
- -[_NBNumberFormat initWithPattern:withFormat:withLeadingDigitsPatterns:withNationalPrefixFormattingRule:whenFormatting:withDomesticCarrierCodeFormattingRule:]
- -[_NBNumberFormat leadingDigitsPatterns]
- -[_NBNumberFormat nationalPrefixFormattingRule]
- -[_NBNumberFormat nationalPrefixOptionalWhenFormatting]
- -[_NBNumberFormat pattern]
- -[_NBNumberFormat setDomesticCarrierCodeFormattingRule:]
- -[_NBNumberFormat setFormat:]
- -[_NBNumberFormat setLeadingDigitsPatterns:]
- -[_NBNumberFormat setNationalPrefixFormattingRule:]
- -[_NBNumberFormat setNationalPrefixOptionalWhenFormatting:]
- -[_NBNumberFormat setPattern:]
- -[_NBPhoneMetaData .cxx_destruct]
- -[_NBPhoneMetaData codeID]
- -[_NBPhoneMetaData countryCode]
- -[_NBPhoneMetaData description]
- -[_NBPhoneMetaData emergency]
- -[_NBPhoneMetaData fixedLine]
- -[_NBPhoneMetaData generalDesc]
- -[_NBPhoneMetaData initWithEntry:]
- -[_NBPhoneMetaData init]
- -[_NBPhoneMetaData internationalPrefix]
- -[_NBPhoneMetaData intlNumberFormats]
- -[_NBPhoneMetaData leadingDigits]
- -[_NBPhoneMetaData leadingZeroPossible]
- -[_NBPhoneMetaData mainCountryForCode]
- -[_NBPhoneMetaData mobile]
- -[_NBPhoneMetaData nationalPrefixForParsing]
- -[_NBPhoneMetaData nationalPrefixTransformRule]
- -[_NBPhoneMetaData nationalPrefix]
- -[_NBPhoneMetaData noInternationalDialling]
- -[_NBPhoneMetaData numberFormatsFromEntry:]
- -[_NBPhoneMetaData numberFormats]
- -[_NBPhoneMetaData pager]
- -[_NBPhoneMetaData personalNumber]
- -[_NBPhoneMetaData preferredExtnPrefix]
- -[_NBPhoneMetaData preferredInternationalPrefix]
- -[_NBPhoneMetaData premiumRate]
- -[_NBPhoneMetaData sameMobileAndFixedLinePattern]
- -[_NBPhoneMetaData setCodeID:]
- -[_NBPhoneMetaData setCountryCode:]
- -[_NBPhoneMetaData setEmergency:]
- -[_NBPhoneMetaData setFixedLine:]
- -[_NBPhoneMetaData setGeneralDesc:]
- -[_NBPhoneMetaData setInternationalPrefix:]
- -[_NBPhoneMetaData setIntlNumberFormats:]
- -[_NBPhoneMetaData setLeadingDigits:]
- -[_NBPhoneMetaData setLeadingZeroPossible:]
- -[_NBPhoneMetaData setMainCountryForCode:]
- -[_NBPhoneMetaData setMobile:]
- -[_NBPhoneMetaData setNationalPrefix:]
- -[_NBPhoneMetaData setNationalPrefixForParsing:]
- -[_NBPhoneMetaData setNationalPrefixTransformRule:]
- -[_NBPhoneMetaData setNoInternationalDialling:]
- -[_NBPhoneMetaData setNumberFormats:]
- -[_NBPhoneMetaData setPager:]
- -[_NBPhoneMetaData setPersonalNumber:]
- -[_NBPhoneMetaData setPreferredExtnPrefix:]
- -[_NBPhoneMetaData setPreferredInternationalPrefix:]
- -[_NBPhoneMetaData setPremiumRate:]
- -[_NBPhoneMetaData setSameMobileAndFixedLinePattern:]
- -[_NBPhoneMetaData setSharedCost:]
- -[_NBPhoneMetaData setTollFree:]
- -[_NBPhoneMetaData setUan:]
- -[_NBPhoneMetaData setVoicemail:]
- -[_NBPhoneMetaData setVoip:]
- -[_NBPhoneMetaData sharedCost]
- -[_NBPhoneMetaData tollFree]
- -[_NBPhoneMetaData uan]
- -[_NBPhoneMetaData voicemail]
- -[_NBPhoneMetaData voip]
- -[_NBPhoneNumber .cxx_destruct]
- -[_NBPhoneNumber clearCountryCodeSource]
- -[_NBPhoneNumber copyWithZone:]
- -[_NBPhoneNumber countryCodeSource]
- -[_NBPhoneNumber countryCode]
- -[_NBPhoneNumber description]
- -[_NBPhoneNumber encodeWithCoder:]
- -[_NBPhoneNumber extension]
- -[_NBPhoneNumber getCountryCodeSourceOrDefault]
- -[_NBPhoneNumber hash]
- -[_NBPhoneNumber initWithCoder:]
- -[_NBPhoneNumber init]
- -[_NBPhoneNumber isEqual:]
- -[_NBPhoneNumber italianLeadingZero]
- -[_NBPhoneNumber nationalNumber]
- -[_NBPhoneNumber numberOfLeadingZeros]
- -[_NBPhoneNumber preferredDomesticCarrierCode]
- -[_NBPhoneNumber rawInput]
- -[_NBPhoneNumber setCountryCode:]
- -[_NBPhoneNumber setCountryCodeSource:]
- -[_NBPhoneNumber setExtension:]
- -[_NBPhoneNumber setItalianLeadingZero:]
- -[_NBPhoneNumber setNationalNumber:]
- -[_NBPhoneNumber setNumberOfLeadingZeros:]
- -[_NBPhoneNumber setPreferredDomesticCarrierCode:]
- -[_NBPhoneNumber setRawInput:]
- -[_NBPhoneNumberDesc .cxx_destruct]
- -[_NBPhoneNumberDesc description]
- -[_NBPhoneNumberDesc exampleNumber]
- -[_NBPhoneNumberDesc initWithEntry:]
- -[_NBPhoneNumberDesc nationalNumberMatcherData]
- -[_NBPhoneNumberDesc nationalNumberPattern]
- -[_NBPhoneNumberDesc possibleLengthLocalOnly]
- -[_NBPhoneNumberDesc possibleLength]
- -[_NBPhoneNumberDesc possibleNumberMatcherData]
- -[_NBPhoneNumberDesc possibleNumberPattern]
- -[_NBPhoneNumberUtil .cxx_destruct]
- -[_NBPhoneNumberUtil CAPTURING_DIGIT_PATTERN]
- -[_NBPhoneNumberUtil DIGIT_MAPPINGS]
- -[_NBPhoneNumberUtil VALID_ALPHA_PHONE_PATTERN]
- -[_NBPhoneNumberUtil buildNationalNumberForParsing:nationalNumber:]
- -[_NBPhoneNumberUtil canBeInternationallyDialled:]
- -[_NBPhoneNumberUtil canBeInternationallyDialled:error:]
- -[_NBPhoneNumberUtil checkRegionForParsing:defaultRegion:]
- -[_NBPhoneNumberUtil chooseFormattingPatternForNumber:nationalNumber:]
- -[_NBPhoneNumberUtil componentsSeparatedByRegex:regex:]
- -[_NBPhoneNumberUtil convertAlphaCharactersInNumber:]
- -[_NBPhoneNumberUtil countryCodeByCarrier]
- -[_NBPhoneNumberUtil descHasPossibleNumberData:]
- -[_NBPhoneNumberUtil entireRegularExpressionWithPattern:options:error:]
- -[_NBPhoneNumberUtil entireStringCacheLock]
- -[_NBPhoneNumberUtil entireStringRegexCache]
- -[_NBPhoneNumberUtil errorWithObject:withDomain:]
- -[_NBPhoneNumberUtil extractCountryCode:nationalNumber:]
- -[_NBPhoneNumberUtil extractPossibleNumber:]
- -[_NBPhoneNumberUtil format:numberFormat:]
- -[_NBPhoneNumberUtil format:numberFormat:error:]
- -[_NBPhoneNumberUtil formatByPattern:numberFormat:userDefinedFormats:]
- -[_NBPhoneNumberUtil formatByPattern:numberFormat:userDefinedFormats:error:]
- -[_NBPhoneNumberUtil formatInOriginalFormat:regionCallingFrom:]
- -[_NBPhoneNumberUtil formatInOriginalFormat:regionCallingFrom:error:]
- -[_NBPhoneNumberUtil formatNationalNumberWithCarrierCode:carrierCode:]
- -[_NBPhoneNumberUtil formatNationalNumberWithCarrierCode:carrierCode:error:]
- -[_NBPhoneNumberUtil formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:]
- -[_NBPhoneNumberUtil formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:error:]
- -[_NBPhoneNumberUtil formatNsn:metadata:phoneNumberFormat:carrierCode:]
- -[_NBPhoneNumberUtil formatNsnUsingPattern:formattingPattern:numberFormat:carrierCode:]
- -[_NBPhoneNumberUtil formatNumberForMobileDialing:regionCallingFrom:withFormatting:]
- -[_NBPhoneNumberUtil formatNumberForMobileDialing:regionCallingFrom:withFormatting:error:]
- -[_NBPhoneNumberUtil formatOutOfCountryCallingNumber:regionCallingFrom:]
- -[_NBPhoneNumberUtil formatOutOfCountryCallingNumber:regionCallingFrom:error:]
- -[_NBPhoneNumberUtil formatOutOfCountryKeepingAlphaChars:regionCallingFrom:]
- -[_NBPhoneNumberUtil formatOutOfCountryKeepingAlphaChars:regionCallingFrom:error:]
- -[_NBPhoneNumberUtil formattingRuleHasFirstGroupOnly:]
- -[_NBPhoneNumberUtil getCountryCodeForRegion:]
- -[_NBPhoneNumberUtil getCountryCodeForValidRegion:error:]
- -[_NBPhoneNumberUtil getCountryMobileTokenFromCountryCode:]
- -[_NBPhoneNumberUtil getExampleNumber:error:]
- -[_NBPhoneNumberUtil getExampleNumberForNonGeoEntity:error:]
- -[_NBPhoneNumberUtil getExampleNumberForType:type:error:]
- -[_NBPhoneNumberUtil getLengthOfGeographicalAreaCode:]
- -[_NBPhoneNumberUtil getLengthOfGeographicalAreaCode:error:]
- -[_NBPhoneNumberUtil getLengthOfNationalDestinationCode:]
- -[_NBPhoneNumberUtil getLengthOfNationalDestinationCode:error:]
- -[_NBPhoneNumberUtil getMetadataForRegionOrCallingCode:regionCode:]
- -[_NBPhoneNumberUtil getNationalSignificantNumber:]
- -[_NBPhoneNumberUtil getNddPrefixForRegion:stripNonDigits:]
- -[_NBPhoneNumberUtil getNumberDescByType:type:]
- -[_NBPhoneNumberUtil getNumberType:]
- -[_NBPhoneNumberUtil getNumberTypeHelper:metadata:]
- -[_NBPhoneNumberUtil getRegionCodeForCountryCode:]
- -[_NBPhoneNumberUtil getRegionCodeForNumber:]
- -[_NBPhoneNumberUtil getRegionCodeForNumberFromRegionList:regionCodes:]
- -[_NBPhoneNumberUtil getRegionCodesForCountryCode:]
- -[_NBPhoneNumberUtil getSupportedRegions]
- -[_NBPhoneNumberUtil hasFormattingPatternForNumber:]
- -[_NBPhoneNumberUtil hasUnexpectedItalianLeadingZero:]
- -[_NBPhoneNumberUtil hasValidCountryCallingCode:]
- -[_NBPhoneNumberUtil helper]
- -[_NBPhoneNumberUtil indexOfStringByString:target:]
- -[_NBPhoneNumberUtil initNormalizationMappings]
- -[_NBPhoneNumberUtil initRegularExpressionSet]
- -[_NBPhoneNumberUtil init]
- -[_NBPhoneNumberUtil isAllDigits:]
- -[_NBPhoneNumberUtil isAlphaNumber:]
- -[_NBPhoneNumberUtil isLeadingZeroPossible:]
- -[_NBPhoneNumberUtil isNANPACountry:]
- -[_NBPhoneNumberUtil isNationalNumberSuffixOfTheOther:second:]
- -[_NBPhoneNumberUtil isNumberGeographical:]
- -[_NBPhoneNumberUtil isNumberMatch:second:]
- -[_NBPhoneNumberUtil isNumberMatch:second:error:]
- -[_NBPhoneNumberUtil isNumberMatchingDesc:numberDesc:]
- -[_NBPhoneNumberUtil isPossibleNumber:]
- -[_NBPhoneNumberUtil isPossibleNumber:error:]
- -[_NBPhoneNumberUtil isPossibleNumberString:regionDialingFrom:error:]
- -[_NBPhoneNumberUtil isPossibleNumberWithReason:]
- -[_NBPhoneNumberUtil isPossibleNumberWithReason:error:]
- -[_NBPhoneNumberUtil isStartingStringByRegex:regex:]
- -[_NBPhoneNumberUtil isValidNumber:]
- -[_NBPhoneNumberUtil isValidNumberForRegion:regionCode:]
- -[_NBPhoneNumberUtil isValidRegionCode:]
- -[_NBPhoneNumberUtil isViablePhoneNumber:]
- -[_NBPhoneNumberUtil lockPatternCache]
- -[_NBPhoneNumberUtil matchFirstByRegex:regex:]
- -[_NBPhoneNumberUtil matchedStringByRegex:regex:]
- -[_NBPhoneNumberUtil matcher]
- -[_NBPhoneNumberUtil matchesByRegex:regex:]
- -[_NBPhoneNumberUtil matchesEntirely:string:]
- -[_NBPhoneNumberUtil maybeExtractCountryCode:metadata:nationalNumber:keepRawInput:phoneNumber:error:]
- -[_NBPhoneNumberUtil maybeGetFormattedExtension:metadata:numberFormat:]
- -[_NBPhoneNumberUtil maybeStripExtension:]
- -[_NBPhoneNumberUtil maybeStripInternationalPrefixAndNormalize:possibleIddPrefix:]
- -[_NBPhoneNumberUtil maybeStripNationalPrefixAndCarrierCode:metadata:carrierCode:]
- -[_NBPhoneNumberUtil normalize:]
- -[_NBPhoneNumberUtil normalizeDiallableCharsOnly:]
- -[_NBPhoneNumberUtil normalizeDigitsOnly:]
- -[_NBPhoneNumberUtil normalizeHelper:normalizationReplacements:removeNonMatches:]
- -[_NBPhoneNumberUtil normalizeSB:]
- -[_NBPhoneNumberUtil parse:defaultRegion:error:]
- -[_NBPhoneNumberUtil parseAndKeepRawInput:defaultRegion:error:]
- -[_NBPhoneNumberUtil parseHelper:defaultRegion:keepRawInput:checkRegion:error:]
- -[_NBPhoneNumberUtil parsePrefixAsIdd:sourceString:]
- -[_NBPhoneNumberUtil parseWithPhoneCarrierRegion:error:]
- -[_NBPhoneNumberUtil prefixNumberWithCountryCallingCode:phoneNumberFormat:formattedNationalNumber:formattedExtension:]
- -[_NBPhoneNumberUtil rawInputContainsNationalPrefix:nationalPrefix:regionCode:]
- -[_NBPhoneNumberUtil regexPatternCache]
- -[_NBPhoneNumberUtil regularExpressionWithPattern:options:error:]
- -[_NBPhoneNumberUtil replaceFirstStringByRegex:regex:withTemplate:]
- -[_NBPhoneNumberUtil replaceStringByRegex:regex:withTemplate:]
- -[_NBPhoneNumberUtil setCAPTURING_DIGIT_PATTERN:]
- -[_NBPhoneNumberUtil setEntireStringCacheLock:]
- -[_NBPhoneNumberUtil setEntireStringRegexCache:]
- -[_NBPhoneNumberUtil setHelper:]
- -[_NBPhoneNumberUtil setItalianLeadingZerosForPhoneNumber:phoneNumber:]
- -[_NBPhoneNumberUtil setLockPatternCache:]
- -[_NBPhoneNumberUtil setMatcher:]
- -[_NBPhoneNumberUtil setRegexPatternCache:]
- -[_NBPhoneNumberUtil setVALID_ALPHA_PHONE_PATTERN:]
- -[_NBPhoneNumberUtil stringByReplacingOccurrencesString:withMap:removeNonMatches:]
- -[_NBPhoneNumberUtil stringPositionByRegex:regex:]
- -[_NBPhoneNumberUtil telephonyNetworkInfo]
- -[_NBPhoneNumberUtil testNumberLength:desc:]
- -[_NBPhoneNumberUtil truncateTooLongNumber:]
- -[_NBPhoneNumberUtil validateNumberLength:metadata:]
- -[_NBPhoneNumberUtil validateNumberLength:metadata:type:]
- -[_NBRegExMatcher matchNationalNumber:phoneNumberDesc:allowsPrefixMatch:]
- -[_NBRegularExpressionCache .cxx_destruct]
- -[_NBRegularExpressionCache cache]
- -[_NBRegularExpressionCache init]
- -[_NBRegularExpressionCache regularExpressionForPattern:error:]
- -[_NBRegularExpressionCache setCache:]
- GCC_except_table115
- GCC_except_table118
- GCC_except_table3
- GCC_except_table32
- GCC_except_table34
- GCC_except_table43
- GCC_except_table45
- GCC_except_table47
- GCC_except_table50
- GCC_except_table52
- GCC_except_table54
- GCC_except_table57
- GCC_except_table62
- GCC_except_table87
- GCC_except_table92
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _GEO_MOBILE_COUNTRIES
- _NB_NON_BREAKING_SPACE
- _NB_PLUS_CHARS
- _NB_REGION_CODE_FOR_NON_GEO_ENTITY
- _NB_UNKNOWN_REGION
- _NB_VALID_DIGITS_STRING
- _NSLocaleIdentifier
- _OBJC_CLASS_$_BCSPhoneNumberNormalizer
- _OBJC_CLASS_$_CTTelephonyNetworkInfo
- _OBJC_CLASS_$_NSCache
- _OBJC_CLASS_$_NSConstantArray
- _OBJC_CLASS_$_NSMutableCharacterSet
- _OBJC_CLASS_$_NSRegularExpression
- _OBJC_CLASS_$__NBAsYouTypeFormatter
- _OBJC_CLASS_$__NBMetadataHelper
- _OBJC_CLASS_$__NBNumberFormat
- _OBJC_CLASS_$__NBPhoneMetaData
- _OBJC_CLASS_$__NBPhoneNumber
- _OBJC_CLASS_$__NBPhoneNumberDesc
- _OBJC_CLASS_$__NBPhoneNumberUtil
- _OBJC_CLASS_$__NBRegExMatcher
- _OBJC_CLASS_$__NBRegularExpressionCache
- _OBJC_EHTYPE_$_NSException
- _OBJC_IVAR_$__NBAsYouTypeFormatter._CHARACTER_CLASS_PATTERN_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._DIGIT_PATTERN_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._ELIGIBLE_FORMAT_PATTERN_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._NATIONAL_PREFIX_SEPARATORS_PATTERN_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._STANDALONE_DIGIT_PATTERN_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._ableToFormat_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._accruedInputWithoutFormatting_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._accruedInput_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._currentFormattingPattern_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._currentMetaData_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._currentOutput_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._defaultCountry_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._defaultMetaData_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._formattingTemplate_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._inputHasFormatting_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._isCompleteNumber_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._isExpectingCountryCallingCode_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._isSuccessfulFormatting
- _OBJC_IVAR_$__NBAsYouTypeFormatter._lastMatchPosition_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._nationalNumber_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._nationalPrefixExtracted_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._originalPosition_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._phoneUtil_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._positionToRemember_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._possibleFormats_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._prefixBeforeNationalNumber_
- _OBJC_IVAR_$__NBAsYouTypeFormatter._shouldAddSpaceAfterNationalPrefix_
- _OBJC_IVAR_$__NBMetadataHelper._metadataCache
- _OBJC_IVAR_$__NBNumberFormat._domesticCarrierCodeFormattingRule
- _OBJC_IVAR_$__NBNumberFormat._format
- _OBJC_IVAR_$__NBNumberFormat._leadingDigitsPatterns
- _OBJC_IVAR_$__NBNumberFormat._nationalPrefixFormattingRule
- _OBJC_IVAR_$__NBNumberFormat._nationalPrefixOptionalWhenFormatting
- _OBJC_IVAR_$__NBNumberFormat._pattern
- _OBJC_IVAR_$__NBPhoneMetaData._codeID
- _OBJC_IVAR_$__NBPhoneMetaData._countryCode
- _OBJC_IVAR_$__NBPhoneMetaData._emergency
- _OBJC_IVAR_$__NBPhoneMetaData._fixedLine
- _OBJC_IVAR_$__NBPhoneMetaData._generalDesc
- _OBJC_IVAR_$__NBPhoneMetaData._internationalPrefix
- _OBJC_IVAR_$__NBPhoneMetaData._intlNumberFormats
- _OBJC_IVAR_$__NBPhoneMetaData._leadingDigits
- _OBJC_IVAR_$__NBPhoneMetaData._leadingZeroPossible
- _OBJC_IVAR_$__NBPhoneMetaData._mainCountryForCode
- _OBJC_IVAR_$__NBPhoneMetaData._mobile
- _OBJC_IVAR_$__NBPhoneMetaData._nationalPrefix
- _OBJC_IVAR_$__NBPhoneMetaData._nationalPrefixForParsing
- _OBJC_IVAR_$__NBPhoneMetaData._nationalPrefixTransformRule
- _OBJC_IVAR_$__NBPhoneMetaData._noInternationalDialling
- _OBJC_IVAR_$__NBPhoneMetaData._numberFormats
- _OBJC_IVAR_$__NBPhoneMetaData._pager
- _OBJC_IVAR_$__NBPhoneMetaData._personalNumber
- _OBJC_IVAR_$__NBPhoneMetaData._preferredExtnPrefix
- _OBJC_IVAR_$__NBPhoneMetaData._preferredInternationalPrefix
- _OBJC_IVAR_$__NBPhoneMetaData._premiumRate
- _OBJC_IVAR_$__NBPhoneMetaData._sameMobileAndFixedLinePattern
- _OBJC_IVAR_$__NBPhoneMetaData._sharedCost
- _OBJC_IVAR_$__NBPhoneMetaData._tollFree
- _OBJC_IVAR_$__NBPhoneMetaData._uan
- _OBJC_IVAR_$__NBPhoneMetaData._voicemail
- _OBJC_IVAR_$__NBPhoneMetaData._voip
- _OBJC_IVAR_$__NBPhoneNumber._countryCode
- _OBJC_IVAR_$__NBPhoneNumber._countryCodeSource
- _OBJC_IVAR_$__NBPhoneNumber._extension
- _OBJC_IVAR_$__NBPhoneNumber._italianLeadingZero
- _OBJC_IVAR_$__NBPhoneNumber._nationalNumber
- _OBJC_IVAR_$__NBPhoneNumber._numberOfLeadingZeros
- _OBJC_IVAR_$__NBPhoneNumber._preferredDomesticCarrierCode
- _OBJC_IVAR_$__NBPhoneNumber._rawInput
- _OBJC_IVAR_$__NBPhoneNumberDesc._exampleNumber
- _OBJC_IVAR_$__NBPhoneNumberDesc._nationalNumberMatcherData
- _OBJC_IVAR_$__NBPhoneNumberDesc._nationalNumberPattern
- _OBJC_IVAR_$__NBPhoneNumberDesc._possibleLength
- _OBJC_IVAR_$__NBPhoneNumberDesc._possibleLengthLocalOnly
- _OBJC_IVAR_$__NBPhoneNumberDesc._possibleNumberMatcherData
- _OBJC_IVAR_$__NBPhoneNumberDesc._possibleNumberPattern
- _OBJC_IVAR_$__NBPhoneNumberUtil._CAPTURING_DIGIT_PATTERN
- _OBJC_IVAR_$__NBPhoneNumberUtil._VALID_ALPHA_PHONE_PATTERN
- _OBJC_IVAR_$__NBPhoneNumberUtil._entireStringCacheLock
- _OBJC_IVAR_$__NBPhoneNumberUtil._entireStringRegexCache
- _OBJC_IVAR_$__NBPhoneNumberUtil._helper
- _OBJC_IVAR_$__NBPhoneNumberUtil._lockPatternCache
- _OBJC_IVAR_$__NBPhoneNumberUtil._matcher
- _OBJC_IVAR_$__NBPhoneNumberUtil._regexPatternCache
- _OBJC_IVAR_$__NBRegularExpressionCache._cache
- _OBJC_METACLASS_$_BCSPhoneNumberNormalizer
- _OBJC_METACLASS_$__NBAsYouTypeFormatter
- _OBJC_METACLASS_$__NBMetadataHelper
- _OBJC_METACLASS_$__NBNumberFormat
- _OBJC_METACLASS_$__NBPhoneMetaData
- _OBJC_METACLASS_$__NBPhoneNumber
- _OBJC_METACLASS_$__NBPhoneNumberDesc
- _OBJC_METACLASS_$__NBPhoneNumberUtil
- _OBJC_METACLASS_$__NBRegExMatcher
- _OBJC_METACLASS_$__NBRegularExpressionCache
- _StringByTrimming
- __OBJC_$_CATEGORY_NSArray_$__NBAdditions
- __OBJC_$_CLASS_METHODS_BCSPhoneNumberNormalizer
- __OBJC_$_CLASS_METHODS__NBMetadataHelper
- __OBJC_$_CLASS_METHODS__NBPhoneNumberUtil
- __OBJC_$_CLASS_METHODS__NBRegularExpressionCache
- __OBJC_$_INSTANCE_METHODS_NSArray(_NBAdditions|BCSProtoLocalizedStringsHelper)
- __OBJC_$_INSTANCE_METHODS__NBAsYouTypeFormatter
- __OBJC_$_INSTANCE_METHODS__NBMetadataHelper
- __OBJC_$_INSTANCE_METHODS__NBNumberFormat
- __OBJC_$_INSTANCE_METHODS__NBPhoneMetaData
- __OBJC_$_INSTANCE_METHODS__NBPhoneNumber
- __OBJC_$_INSTANCE_METHODS__NBPhoneNumberDesc
- __OBJC_$_INSTANCE_METHODS__NBPhoneNumberUtil
- __OBJC_$_INSTANCE_METHODS__NBRegExMatcher
- __OBJC_$_INSTANCE_METHODS__NBRegularExpressionCache
- __OBJC_$_INSTANCE_VARIABLES__NBAsYouTypeFormatter
- __OBJC_$_INSTANCE_VARIABLES__NBMetadataHelper
- __OBJC_$_INSTANCE_VARIABLES__NBNumberFormat
- __OBJC_$_INSTANCE_VARIABLES__NBPhoneMetaData
- __OBJC_$_INSTANCE_VARIABLES__NBPhoneNumber
- __OBJC_$_INSTANCE_VARIABLES__NBPhoneNumberDesc
- __OBJC_$_INSTANCE_VARIABLES__NBPhoneNumberUtil
- __OBJC_$_INSTANCE_VARIABLES__NBRegularExpressionCache
- __OBJC_$_PROP_LIST__NBAsYouTypeFormatter
- __OBJC_$_PROP_LIST__NBMetadataHelper
- __OBJC_$_PROP_LIST__NBNumberFormat
- __OBJC_$_PROP_LIST__NBPhoneMetaData
- __OBJC_$_PROP_LIST__NBPhoneNumber
- __OBJC_$_PROP_LIST__NBPhoneNumberDesc
- __OBJC_$_PROP_LIST__NBPhoneNumberUtil
- __OBJC_$_PROP_LIST__NBRegularExpressionCache
- __OBJC_CLASS_PROTOCOLS_$__NBPhoneNumber
- __OBJC_CLASS_RO_$_BCSPhoneNumberNormalizer
- __OBJC_CLASS_RO_$__NBAsYouTypeFormatter
- __OBJC_CLASS_RO_$__NBMetadataHelper
- __OBJC_CLASS_RO_$__NBNumberFormat
- __OBJC_CLASS_RO_$__NBPhoneMetaData
- __OBJC_CLASS_RO_$__NBPhoneNumber
- __OBJC_CLASS_RO_$__NBPhoneNumberDesc
- __OBJC_CLASS_RO_$__NBPhoneNumberUtil
- __OBJC_CLASS_RO_$__NBRegExMatcher
- __OBJC_CLASS_RO_$__NBRegularExpressionCache
- __OBJC_METACLASS_RO_$_BCSPhoneNumberNormalizer
- __OBJC_METACLASS_RO_$__NBAsYouTypeFormatter
- __OBJC_METACLASS_RO_$__NBMetadataHelper
- __OBJC_METACLASS_RO_$__NBNumberFormat
- __OBJC_METACLASS_RO_$__NBPhoneMetaData
- __OBJC_METACLASS_RO_$__NBPhoneNumber
- __OBJC_METACLASS_RO_$__NBPhoneNumberDesc
- __OBJC_METACLASS_RO_$__NBPhoneNumberUtil
- __OBJC_METACLASS_RO_$__NBRegExMatcher
- __OBJC_METACLASS_RO_$__NBRegularExpressionCache
- ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.247
- ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.250
- ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.257
- ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke.259
- ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke_2.258
- ___100-[BCSBusinessQueryController fetchBusinessMetadataForEmails:forClientBundleID:requestId:completion:]_block_invoke_2.266
- ___100-[BCSRemoteFetchCloudKit fetchItemsWithBucketStartIndex:endIndex:type:forClientBundleID:completion:]_block_invoke.119
- ___109-[BCSBusinessQueryController lookupBloomFiltersForURL:chopURL:forClientBundleID:registeredMetric:completion:]_block_invoke.37
- ___134-[BCSBusinessQueryController fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:metadataCallback:logoURLCallback:completion:]_block_invoke.201
- ___32+[_NBMetadataHelper CCode2CNMap]_block_invoke
- ___36+[_NBPhoneNumberUtil sharedInstance]_block_invoke
- ___36-[_NBPhoneNumberUtil DIGIT_MAPPINGS]_block_invoke
- ___39+[_NBMetadataHelper phoneNumberDataMap]_block_invoke
- ___39-[BCSMegashardFetcher addFetchTrigger:]_block_invoke.10
- ___41-[_NBPhoneNumberUtil getSupportedRegions]_block_invoke
- ___42-[_NBPhoneNumberUtil telephonyNetworkInfo]_block_invoke
- ___43+[_NBRegularExpressionCache sharedInstance]_block_invoke
- ___46-[_NBPhoneNumberUtil initRegularExpressionSet]_block_invoke
- ___47-[_NBPhoneNumberUtil initNormalizationMappings]_block_invoke
- ___58-[BCSRemoteFetchPIR fetchDataMatching:timeout:completion:]_block_invoke.84
- ___58-[BCSRemoteFetchPIR fetchDataMatching:timeout:completion:]_block_invoke.87
- ___60-[BCSBusinessQueryController fetchItemWithQuery:completion:]_block_invoke.161
- ___61-[BCSBusinessQueryController fetchShardWithQuery:completion:]_block_invoke.50
- ___62-[BCSBusinessQueryController fetchShardsWithQuery:completion:]_block_invoke.59
- ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.270
- ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.271
- ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.272
- ___71-[BCSRemoteFetchCloudKit fetchShardMatching:clientBundleID:completion:]_block_invoke.90
- ___75-[BCSCacheManager initWithBloomFilterShardCache:domainItemCache:itemCache:]_block_invoke.14
- ___76-[BCSBusinessQueryController fetchIsBusinessRegisteredWithQuery:completion:]_block_invoke.66
- ___76-[BCSMegashardFetcher _fetchMegashardForReason:withBGSystemTask:completion:]_block_invoke.14
- ___76-[BCSMegashardFetcher _fetchMegashardForReason:withBGSystemTask:completion:]_block_invoke_2.16
- ___76-[BCSRemoteFetchPIR fetchDataMatchingBatch:timeout:perItemBlock:completion:]_block_invoke.36
- ___79-[BCSBusinessQueryController fetchAreBusinessesRegisteredWithQuery:completion:]_block_invoke.138
- ___79-[BCSBusinessQueryController fetchItemsWithQuery:perItemCompletion:completion:]_block_invoke.173
- ___86-[BCSBusinessQueryController fetchLinkItemModelWithHash:forClientBundleID:completion:]_block_invoke.39
- ___87-[BCSRemoteFetchCloudKit fetchConfigItemWithType:clientBundleID:systemTask:completion:]_block_invoke.75
- ___89-[BCSBusinessQueryController fetchBusinessMetadataForEmail:forClientBundleID:completion:]_block_invoke.223
- ___90-[BCSRemoteFetchCloudKit fetchMegashardItemWithType:clientBundleID:systemTask:completion:]_block_invoke.104
- ___90-[BCSRemoteFetchCloudKit fetchMegashardItemWithType:clientBundleID:systemTask:completion:]_block_invoke.106
- ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.27
- ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.29
- ___94-[BCSBusinessQueryController isBusinessRegisteredForURL:chopURL:forClientBundleID:completion:]_block_invoke.33
- ___98-[BCSBusinessQueryController fetchBusinessLogoForBusinessIdentifier:forClientBundleID:completion:]_block_invoke.236
- ___StringByTrimming_block_invoke
- ___block_descriptor_32_e25_B24?08"NSDictionary"16l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_48_e8_32s40bs_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e41_v24?0"<BCSBusinessConfig>"8"NSError"16ls48l8s32l8s40l8
- ___block_literal_global.117
- ___block_literal_global.16
- ___block_literal_global.293
- ___block_literal_global.569
- ___block_literal_global.590
- ___block_literal_global.825
- ___isNan_block_invoke
- _initNormalizationMappings.onceToken
- _initRegularExpressionSet.onceToken
- _isNan
- _kPhoneNumberMetaData
- _objc_begin_catch
- _objc_end_catch
- _objc_exception_rethrow
- _objc_msgSend$CCode2CNMap
- _objc_msgSend$CHARACTER_CLASS_PATTERN_
- _objc_msgSend$CN2CCodeMap
- _objc_msgSend$DIGIT_MAPPINGS
- _objc_msgSend$ELIGIBLE_FORMAT_PATTERN_
- _objc_msgSend$ISOCountryCodes
- _objc_msgSend$NATIONAL_PREFIX_SEPARATORS_PATTERN_
- _objc_msgSend$STANDALONE_DIGIT_PATTERN_
- _objc_msgSend$ableToExtractLongerNdd_
- _objc_msgSend$ableToFormat_
- _objc_msgSend$accruedInputWithoutFormatting_
- _objc_msgSend$accruedInput_
- _objc_msgSend$appendNationalNumber_:
- _objc_msgSend$arrayByAddingObjectsFromArray:
- _objc_msgSend$attemptToChooseFormattingPattern_
- _objc_msgSend$attemptToChoosePatternWithPrefixExtracted_
- _objc_msgSend$attemptToExtractCountryCallingCode_
- _objc_msgSend$attemptToExtractIdd_
- _objc_msgSend$attemptToFormatAccruedDigits_
- _objc_msgSend$buildNationalNumberForParsing:nationalNumber:
- _objc_msgSend$cache
- _objc_msgSend$canBeInternationallyDialled:
- _objc_msgSend$checkRegionForParsing:defaultRegion:
- _objc_msgSend$chooseFormattingPatternForNumber:nationalNumber:
- _objc_msgSend$clear
- _objc_msgSend$clearCountryCodeSource
- _objc_msgSend$componentsSeparatedByRegex:regex:
- _objc_msgSend$containsObject:
- _objc_msgSend$countryCode
- _objc_msgSend$countryCodeByCarrier
- _objc_msgSend$countryCodeSource
- _objc_msgSend$createFormattingTemplate_:
- _objc_msgSend$currentFormattingPattern_
- _objc_msgSend$currentMetaData_
- _objc_msgSend$currentOutput_
- _objc_msgSend$decimalDigitCharacterSet
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$decompressData:error:
- _objc_msgSend$defaultCountry_
- _objc_msgSend$defaultMetaData_
- _objc_msgSend$descHasPossibleNumberData:
- _objc_msgSend$dictionaryWithObject:forKey:
- _objc_msgSend$displayNameForKey:value:
- _objc_msgSend$domesticCarrierCodeFormattingRule
- _objc_msgSend$entireRegularExpressionWithPattern:options:error:
- _objc_msgSend$errorWithObject:withDomain:
- _objc_msgSend$exampleNumber
- _objc_msgSend$extension
- _objc_msgSend$extractCountryCode:nationalNumber:
- _objc_msgSend$extractPossibleNumber:
- _objc_msgSend$filteredArrayUsingPredicate:
- _objc_msgSend$firstMatchInString:options:range:
- _objc_msgSend$fixedLine
- _objc_msgSend$formUnionWithCharacterSet:
- _objc_msgSend$format
- _objc_msgSend$format:numberFormat:
- _objc_msgSend$format:numberFormat:error:
- _objc_msgSend$formatByPattern:numberFormat:userDefinedFormats:
- _objc_msgSend$formatInOriginalFormat:regionCallingFrom:
- _objc_msgSend$formatNationalNumberWithCarrierCode:carrierCode:
- _objc_msgSend$formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:
- _objc_msgSend$formatNsn:metadata:phoneNumberFormat:carrierCode:
- _objc_msgSend$formatNsnUsingPattern:formattingPattern:numberFormat:carrierCode:
- _objc_msgSend$formatNumberForMobileDialing:regionCallingFrom:withFormatting:
- _objc_msgSend$formatOutOfCountryCallingNumber:regionCallingFrom:
- _objc_msgSend$formatOutOfCountryKeepingAlphaChars:regionCallingFrom:
- _objc_msgSend$formattingRuleHasFirstGroupOnly:
- _objc_msgSend$formattingTemplate_
- _objc_msgSend$generalDesc
- _objc_msgSend$getAvailableFormats_:
- _objc_msgSend$getCountryCodeForRegion:
- _objc_msgSend$getCountryCodeForValidRegion:error:
- _objc_msgSend$getExampleNumberForType:type:error:
- _objc_msgSend$getFormattingTemplate_:numberFormat:
- _objc_msgSend$getLengthOfGeographicalAreaCode:
- _objc_msgSend$getLengthOfNationalDestinationCode:
- _objc_msgSend$getMetadataForNonGeographicalRegion:
- _objc_msgSend$getMetadataForRegion:
- _objc_msgSend$getMetadataForRegionOrCallingCode:regionCode:
- _objc_msgSend$getMetadataForRegion_:
- _objc_msgSend$getNationalSignificantNumber:
- _objc_msgSend$getNddPrefixForRegion:stripNonDigits:
- _objc_msgSend$getNumberDescByType:type:
- _objc_msgSend$getNumberType:
- _objc_msgSend$getNumberTypeHelper:metadata:
- _objc_msgSend$getRegionCodeForCountryCode:
- _objc_msgSend$getRegionCodeForNumber:
- _objc_msgSend$getRegionCodeForNumberFromRegionList:regionCodes:
- _objc_msgSend$hasFormattingPatternForNumber:
- _objc_msgSend$hasSuffix:
- _objc_msgSend$hasValidCountryCallingCode:
- _objc_msgSend$hasValue:
- _objc_msgSend$helper
- _objc_msgSend$indexOfObject:
- _objc_msgSend$indexOfStringByString:target:
- _objc_msgSend$initNormalizationMappings
- _objc_msgSend$initRegularExpressionSet
- _objc_msgSend$initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:businessEmailMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:businessEmailConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:businessEmailShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:businessEmailItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:
- _objc_msgSend$initWithEntry:
- _objc_msgSend$initWithItemIdentifier:clientBundleId:shardType:cacheOnly:
- _objc_msgSend$initWithPattern:options:error:
- _objc_msgSend$initWithPattern:withFormat:withLeadingDigitsPatterns:withNationalPrefixFormattingRule:whenFormatting:withDomesticCarrierCodeFormattingRule:
- _objc_msgSend$initWithRegionCode:bundle:
- _objc_msgSend$inputAccruedNationalNumber_
- _objc_msgSend$inputDigit:
- _objc_msgSend$inputDigitAndRememberPosition:
- _objc_msgSend$inputDigitHelper_:
- _objc_msgSend$inputDigitWithOptionToRememberPosition_:rememberPosition:
- _objc_msgSend$inputHasFormatting_
- _objc_msgSend$internationalPrefix
- _objc_msgSend$intlNumberFormats
- _objc_msgSend$invertedSet
- _objc_msgSend$isCompleteNumber_
- _objc_msgSend$isDigitOrLeadingPlusSign_:
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$isExpectingCountryCallingCode_
- _objc_msgSend$isFormatEligible_:
- _objc_msgSend$isLeadingZeroPossible:
- _objc_msgSend$isNANPACountry:
- _objc_msgSend$isNanpaNumberWithNationalPrefix_
- _objc_msgSend$isNationalNumberSuffixOfTheOther:second:
- _objc_msgSend$isNumberGeographical:
- _objc_msgSend$isNumberMatch:second:
- _objc_msgSend$isNumberMatchingDesc:numberDesc:
- _objc_msgSend$isPossibleNumber:
- _objc_msgSend$isPossibleNumberWithReason:
- _objc_msgSend$isStartingStringByRegex:regex:
- _objc_msgSend$isValidNumber:
- _objc_msgSend$isValidNumberForRegion:regionCode:
- _objc_msgSend$isValidRegionCode:
- _objc_msgSend$isViablePhoneNumber:
- _objc_msgSend$isoCountryCode
- _objc_msgSend$italianLeadingZero
- _objc_msgSend$jsonObjectFromZippedDataWithBytes:compressedLength:expandedLength:
- _objc_msgSend$lastMatchPosition_
- _objc_msgSend$lastObject
- _objc_msgSend$leadingDigits
- _objc_msgSend$leadingDigitsPatterns
- _objc_msgSend$leadingZeroPossible
- _objc_msgSend$localeIdentifierFromComponents:
- _objc_msgSend$matchFirstByRegex:regex:
- _objc_msgSend$matchedStringByRegex:regex:
- _objc_msgSend$matchesByRegex:regex:
- _objc_msgSend$matchesEntirely:string:
- _objc_msgSend$matchesInString:options:range:
- _objc_msgSend$maybeCreateNewTemplate_
- _objc_msgSend$maybeExtractCountryCode:metadata:nationalNumber:keepRawInput:phoneNumber:error:
- _objc_msgSend$maybeGetFormattedExtension:metadata:numberFormat:
- _objc_msgSend$maybeStripExtension:
- _objc_msgSend$maybeStripInternationalPrefixAndNormalize:possibleIddPrefix:
- _objc_msgSend$maybeStripNationalPrefixAndCarrierCode:metadata:carrierCode:
- _objc_msgSend$mobile
- _objc_msgSend$narrowDownPossibleFormats_:
- _objc_msgSend$nationalNumber
- _objc_msgSend$nationalNumberPattern
- _objc_msgSend$nationalNumber_
- _objc_msgSend$nationalPrefix
- _objc_msgSend$nationalPrefixExtracted_
- _objc_msgSend$nationalPrefixForParsing
- _objc_msgSend$nationalPrefixFormattingRule
- _objc_msgSend$nationalPrefixOptionalWhenFormatting
- _objc_msgSend$nationalPrefixTransformRule
- _objc_msgSend$nb_safeArrayAtIndex:
- _objc_msgSend$nb_safeDataAtIndex:
- _objc_msgSend$nb_safeNumberAtIndex:
- _objc_msgSend$nb_safeObjectAtIndex:class:
- _objc_msgSend$nb_safeStringAtIndex:
- _objc_msgSend$noInternationalDialling
- _objc_msgSend$normalize:
- _objc_msgSend$normalizeAndAccrueDigitsAndPlusSign_:rememberPosition:
- _objc_msgSend$normalizeDigitsOnly:
- _objc_msgSend$normalizeHelper:normalizationReplacements:removeNonMatches:
- _objc_msgSend$normalizeSB:
- _objc_msgSend$numberFormats
- _objc_msgSend$numberFormatsFromEntry:
- _objc_msgSend$numberOfLeadingZeros
- _objc_msgSend$numberOfRanges
- _objc_msgSend$originalPosition_
- _objc_msgSend$pager
- _objc_msgSend$parse:defaultRegion:error:
- _objc_msgSend$parseHelper:defaultRegion:keepRawInput:checkRegion:error:
- _objc_msgSend$parsePrefixAsIdd:sourceString:
- _objc_msgSend$personalNumber
- _objc_msgSend$phoneNumberDataMap
- _objc_msgSend$phoneUtil_
- _objc_msgSend$positionToRemember_
- _objc_msgSend$possibleFormats_
- _objc_msgSend$possibleLength
- _objc_msgSend$possibleLengthLocalOnly
- _objc_msgSend$possibleNumberPattern
- _objc_msgSend$predicateWithBlock:
- _objc_msgSend$preferredDomesticCarrierCode
- _objc_msgSend$preferredExtnPrefix
- _objc_msgSend$preferredInternationalPrefix
- _objc_msgSend$prefixBeforeNationalNumber_
- _objc_msgSend$prefixNumberWithCountryCallingCode:phoneNumberFormat:formattedNationalNumber:formattedExtension:
- _objc_msgSend$premiumRate
- _objc_msgSend$range
- _objc_msgSend$rangeAtIndex:
- _objc_msgSend$rangeOfCharacterFromSet:
- _objc_msgSend$rangeOfFirstMatchInString:options:range:
- _objc_msgSend$rangeOfString:options:range:
- _objc_msgSend$rawInput
- _objc_msgSend$rawInputContainsNationalPrefix:nationalPrefix:regionCode:
- _objc_msgSend$regionCodeFromCountryCode:
- _objc_msgSend$regularExpressionForPattern:error:
- _objc_msgSend$regularExpressionWithPattern:options:error:
- _objc_msgSend$removeNationalPrefixFromNationalNumber_
- _objc_msgSend$removeObjectAtIndex:
- _objc_msgSend$replaceFirstStringByRegex:regex:withTemplate:
- _objc_msgSend$replaceStringByRegex:regex:withTemplate:
- _objc_msgSend$sameMobileAndFixedLinePattern
- _objc_msgSend$setAbleToFormat_:
- _objc_msgSend$setAccruedInputWithoutFormatting_:
- _objc_msgSend$setAccruedInput_:
- _objc_msgSend$setCHARACTER_CLASS_PATTERN_:
- _objc_msgSend$setCountryCode:
- _objc_msgSend$setCountryCodeSource:
- _objc_msgSend$setCurrentFormattingPattern_:
- _objc_msgSend$setCurrentMetaData_:
- _objc_msgSend$setCurrentOutput_:
- _objc_msgSend$setDIGIT_PATTERN_:
- _objc_msgSend$setDefaultCountry_:
- _objc_msgSend$setDefaultMetaData_:
- _objc_msgSend$setELIGIBLE_FORMAT_PATTERN_:
- _objc_msgSend$setExtension:
- _objc_msgSend$setFormat:
- _objc_msgSend$setFormattingTemplate_:
- _objc_msgSend$setInputHasFormatting_:
- _objc_msgSend$setIsCompleteNumber_:
- _objc_msgSend$setIsExpectingCountryCallingCode_:
- _objc_msgSend$setItalianLeadingZero:
- _objc_msgSend$setItalianLeadingZerosForPhoneNumber:phoneNumber:
- _objc_msgSend$setLastMatchPosition_:
- _objc_msgSend$setNATIONAL_PREFIX_SEPARATORS_PATTERN_:
- _objc_msgSend$setNationalNumber:
- _objc_msgSend$setNationalNumber_:
- _objc_msgSend$setNationalPrefixExtracted_:
- _objc_msgSend$setNationalPrefixFormattingRule:
- _objc_msgSend$setNumberOfLeadingZeros:
- _objc_msgSend$setOriginalPosition_:
- _objc_msgSend$setPattern:
- _objc_msgSend$setPhoneUtil_:
- _objc_msgSend$setPositionToRemember_:
- _objc_msgSend$setPossibleFormats_:
- _objc_msgSend$setPreferredDomesticCarrierCode:
- _objc_msgSend$setPrefixBeforeNationalNumber_:
- _objc_msgSend$setRawInput:
- _objc_msgSend$setSTANDALONE_DIGIT_PATTERN_:
- _objc_msgSend$setShouldAddSpaceAfterNationalPrefix_:
- _objc_msgSend$setString:
- _objc_msgSend$sharedCost
- _objc_msgSend$shouldAddSpaceAfterNationalPrefix_
- _objc_msgSend$sortedArrayUsingSelector:
- _objc_msgSend$stringByPaddingToLength:withString:startingAtIndex:
- _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
- _objc_msgSend$stringByReplacingOccurrencesString:withMap:removeNonMatches:
- _objc_msgSend$stringPositionByRegex:regex:
- _objc_msgSend$stringWithCharacters:length:
- _objc_msgSend$stringWithString:
- _objc_msgSend$subscriberCellularProvider
- _objc_msgSend$substringFromIndex:
- _objc_msgSend$systemLocale
- _objc_msgSend$telephonyNetworkInfo
- _objc_msgSend$testNumberLength:desc:
- _objc_msgSend$tollFree
- _objc_msgSend$truncateTooLongNumber:
- _objc_msgSend$uan
- _objc_msgSend$unsignedLongLongValue
- _objc_msgSend$uppercaseString
- _objc_msgSend$validateNumberLength:metadata:
- _objc_msgSend$validateNumberLength:metadata:type:
- _objc_msgSend$voicemail
- _objc_msgSend$voip
- _objc_msgSend$whitespaceAndNewlineCharacterSet
- _objc_terminate
CStrings:
+ "%s (%@)"
+ "%s - Failed to inflate (!done)"
+ "%s - Failed to inflate (gzip inflate()): %d"
+ "%s - Failed to inflate (gzip inflateInit2())"
+ "%s - Failed to inflate (gzip inflatedEnd())"
+ "%s - Fetch completed with error: %@"
+ "%s - Item successfully fetched from PIR for metadata - type: %@"
+ "%s - No logo found"
+ "%s - Unsupported type: %@"
+ "-[BCSBusinessQueryController fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:]"
+ "-[BCSBusinessQueryController fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:]_block_invoke"
+ "-[BCSBusinessQueryController fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:]_block_invoke_2"
+ "-[BCSBusinessQueryController fetchWebPresentmentPermissionsWithIdentifier:forClientBundleID:completion:]"
+ "-[BCSBusinessQueryController fetchWebPresentmentPermissionsWithIdentifier:forClientBundleID:completion:]_block_invoke"
+ "-[BCSBusinessQueryService fetchBrandWithIdentifier:serviceType:completion:]"
+ "-[BCSBusinessQueryService fetchWebPresentmentPermissionsWithIdentifier:completion:]"
+ "-[BCSWebPresentmentItemResolver _metadataMatching:metric:completion:]_block_invoke"
+ "-[BCSWebPresentmentItemResolver _permissionsMatching:metric:completion:]_block_invoke"
+ "-[BCSWebPresentmentItemResolver cachedItemMatching:]"
+ "-[BCSWebPresentmentItemResolver itemMatching:metric:completion:]"
+ "-[BCSWebPresentmentPersistentStore deleteExpiredItemsOfType:]"
+ "-[BCSWebPresentmentPersistentStore deleteItemMatching:]"
+ "-[BCSWebPresentmentPersistentStore deleteItemsOfType:]"
+ "-[BCSWebPresentmentPersistentStore itemMatching:]"
+ "-[BCSWebPresentmentPersistentStore schemaVersionWillChangeForDatabase:fromSchemaVersion:toSchemaVersion:]"
+ "-[BCSWebPresentmentPersistentStore updateItem:withItemIdentifier:]"
+ "-[NSData(Compression) inflateGzipWithError:]"
+ "-[NSData(Compression) inflateLZRawWithError:]"
+ "<%@ { brandId: %@, data: %@>"
+ "<%@ { brandId: %@, name: %@, businessId: %@, companyId: %@>"
+ "@\"<BCSPIRItemRemoteFetching>\""
+ "@\"BCSWebPresentmentItemIdentifier\""
+ "@\"BCSWebPresentmentParquetMessage\""
+ "@\"BCSWebPresentmentPersistentStore\""
+ "@120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
+ "@264@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256"
+ "@32@0:8Q16^@24"
+ "@52@0:8@16@24q32B40B44B48"
+ "Attempting to decompress data using %@ (%lu)"
+ "BCSBusinessCallerPIRCompressionType"
+ "BCSBusinessEmailLogoPIRCompressionType"
+ "BCSBusinessEmailPIRCompressionType"
+ "BCSBusinessWebPresentmentStubEntry"
+ "BCSCacheManagerWebPresentmentConfigItemDefaultsKey"
+ "BCSMegashardPrefetchLastSuccessfulFetchWebPresentment"
+ "BCSWebPresentmentCustomContainerId"
+ "BCSWebPresentmentCustomEnvironment"
+ "BCSWebPresentmentICloudStagingMode"
+ "BCSWebPresentmentItem"
+ "BCSWebPresentmentItemIdentifier"
+ "BCSWebPresentmentItemResolver"
+ "BCSWebPresentmentLocalizedString"
+ "BCSWebPresentmentPIRCompressionType"
+ "BCSWebPresentmentPIRUseCase"
+ "BCSWebPresentmentPIRUsesCompression"
+ "BCSWebPresentmentParquetMessage"
+ "BCSWebPresentmentPermissionsItem"
+ "BCSWebPresentmentPermissionsPIRCompressionType"
+ "BCSWebPresentmentPermissionsPIRUseCase"
+ "BCSWebPresentmentPermissionsPIRUsesCompression"
+ "BCSWebPresentmentPersistentStore"
+ "BCSWebPresentmentPersistentStore.m"
+ "BCSWebPresentmentSecondaryIdentifier"
+ "BCSWebPresentmentSkipDiskCaching"
+ "BCSWebPresentmentSkipEdgeCaching"
+ "BCSWebPresentmentStoreTypeForItemIdentifier"
+ "BCSXPCDaemonWebPresentmentDaemonInterface"
+ "BrandID"
+ "BrandId"
+ "CREATE TABLE IF NOT EXISTS web_presentment_items    (key TEXT PRIMARY KEY,     message BLOB,     expiration_date DOUBLE);CREATE TABLE IF NOT EXISTS web_presentment_permissions    (key TEXT PRIMARY KEY,     data BLOB,     expiration_date DOUBLE)"
+ "Compression"
+ "DELETE FROM web_presentment_items"
+ "DELETE FROM web_presentment_items WHERE expiration_date <= \"%f\""
+ "DELETE FROM web_presentment_items WHERE key = \"%@\""
+ "DELETE FROM web_presentment_permissions"
+ "DELETE FROM web_presentment_permissions WHERE expiration_date <= \"%f\""
+ "DELETE FROM web_presentment_permissions WHERE key = \"%@\""
+ "DROP TABLE IF EXISTS web_presentment_items"
+ "DROP TABLE IF EXISTS web_presentment_permissions"
+ "Data"
+ "Failed to decompress data"
+ "Failed to decompress data (%@): %@"
+ "Failed to insert web presentment item: %d (%s)"
+ "Failed to insert web presentment permissions item: %d (%s)"
+ "INSERT OR REPLACE INTO web_presentment_items    (key, message, expiration_date)    VALUES (?,?,?)"
+ "INSERT OR REPLACE INTO web_presentment_permissions    (key, data, expiration_date)    VALUES (?,?,?)"
+ "Invalid item (expected BCSWebPresentmentItem): %@"
+ "Invalid item (expected BCSWebPresentmentPermissionsItem): %@"
+ "Invalid item identifier server type: %ld"
+ "No item and no error - interpreting as item not found"
+ "PIRServerType"
+ "SELECT key, data, expiration_date    FROM web_presentment_permissions    WHERE key = \"%@\""
+ "SELECT key, message, expiration_date    FROM web_presentment_items    WHERE key = \"%@\""
+ "Skipping config fetch as specified in query"
+ "T@\"<BCSPIRItemRemoteFetching>\",&,N,V_pirFetchMetadata"
+ "T@\"<BCSPIRItemRemoteFetching>\",&,N,V_pirFetchPermissions"
+ "T@\"BCSWebPresentmentItemIdentifier\",&,N,V_identifier"
+ "T@\"BCSWebPresentmentItemIdentifier\",R,N,V_identifier"
+ "T@\"BCSWebPresentmentParquetMessage\",&,N,V_message"
+ "T@\"NSData\",&,N,V_data"
+ "T@\"NSString\",&,N,V_bcBrandId"
+ "T@\"NSString\",&,N,V_brandId"
+ "T@\"NSString\",R,N,V_brandId"
+ "T@\"NSURL\",&,N,V_logoURL"
+ "TB,N,V_skipConfigFetch"
+ "TQ,N,V_itemTtl"
+ "Tq,R,N,V_serverType"
+ "Unsupported service type"
+ "Updating WebPresentment metadata item in cache with ID: %@, expiration: %@"
+ "Updating WebPresentment permissions item in cache with ID: %@, expiration: %@"
+ "Web Presentment Shard"
+ "WebPresentment"
+ "WebPresentment-config-v1"
+ "WebPresentment: Returning metadata for web presentment matching STUB DATA"
+ "WebPresentment: Returning permissions for web presentment matching STUB DATA"
+ "WebPresentment: Stub logo data: %@"
+ "WebPresentmentConfig"
+ "WebPresentmentConfigMegashard"
+ "WebPresentmentFilter"
+ "WebPresentmentIsEnabledCheck"
+ "WebPresentment_BlastDoorProcessing"
+ "WebPresentment_CloudKitFetchBucket"
+ "WebPresentment_CloudKitFetchBucketAndDecode"
+ "WebPresentment_CloudKitFetchConfig"
+ "WebPresentment_CloudKitFetchConfigAndDecode"
+ "WebPresentment_CloudKitFetchMegashard"
+ "WebPresentment_CloudKitFetchMegashardAndDecode"
+ "WebPresentment_CloudKitFetchShard"
+ "WebPresentment_CloudKitFetchShardAndDecode"
+ "WebPresentment_ConfigResolution"
+ "WebPresentment_Filter_%lld_%lld"
+ "WebPresentment_ItemFetch"
+ "WebPresentment_ItemFetchChop"
+ "WebPresentment_ItemHashFetch"
+ "WebPresentment_ItemResolution"
+ "WebPresentment_PIRItemFetch"
+ "WebPresentment_ShardCacheHit"
+ "WebPresentment_ShardCacheMiss"
+ "WebPresentment_ShardResolution"
+ "X-CloudKit-WebPresentment-QueryName"
+ "_bcBrandId"
+ "_brandId"
+ "_data"
+ "_itemTtl"
+ "_permissionsMatching:metric:completion:"
+ "_pirFetchPermissions"
+ "_setError"
+ "_skipConfigFetch"
+ "_truncatedHashForBrandID:"
+ "_webPresentmentItemResolver"
+ "_webPresentmentStore"
+ "bcBrandId"
+ "bc_brand_id"
+ "brandId"
+ "com.apple.businessservices.persistentStore.webPresentmentItems"
+ "dataWithData:"
+ "error while dropping web_presentment_items table: %s"
+ "error while dropping web_presentment_permissions table: %s"
+ "fetchBrandWithIdentifier:forClientBundleID:serviceType:completion:"
+ "fetchBrandWithIdentifier:serviceType:completion:"
+ "fetchWebPresentmentPermissionsWithIdentifier:completion:"
+ "fetchWebPresentmentPermissionsWithIdentifier:forClientBundleID:completion:"
+ "getBytes:range:"
+ "gzip"
+ "hasBcBrandId"
+ "hasError"
+ "hasItemTtl"
+ "increaseLengthBy:"
+ "inflate:error:"
+ "inflateGzipWithError:"
+ "inflateLZRawWithError:"
+ "initWithBrandID:"
+ "initWithBrandID:data:"
+ "initWithBrandID:defaultsDictionary:"
+ "initWithBrandID:localizedNames:"
+ "initWithBrandID:localizedNames:businessId:companyId:"
+ "initWithBrandID:serverType:"
+ "initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:businessEmailMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:businessEmailConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:businessEmailShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:businessEmailItemResolver:webPresentmentItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:"
+ "initWithChatSuggestMegashardFetcher:businessLinkMegashardFetcher:businessCallerMegashardFetcher:businessEmailMegashardFetcher:shardCache:cacheManager:chatSuggestRemoteFetcher:businessLinkRemoteFetcher:businessCallerRemoteFetcher:businessEmailRemoteFetcher:webPresentmentRemoteFetcher:userDefaults:metricFactory:"
+ "initWithItemIdentifier:clientBundleId:shardType:cacheOnly:skipRegistrationCheck:skipConfigFetch:"
+ "logoData"
+ "lz4_raw"
+ "lz4_rwa"
+ "permissions"
+ "pirCompressionType"
+ "pirFetchPermissions"
+ "position"
+ "setBcBrandId:"
+ "setBrandId:"
+ "setData:"
+ "setHasItemTtl:"
+ "setIdentifier:"
+ "setItemTtl:"
+ "setPirFetchPermissions:"
+ "setPosition:"
+ "setSkipConfigFetch:"
+ "skipConfigFetch"
+ "v24@?0@\"BCSWebPresentmentItem\"8@\"NSError\"16"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v48@0:8@\"NSString\"16@\"NSString\"24q32@?<v@?@\"BCSWebPresentmentItem\"@\"NSError\">40"
+ "v48@0:8@16@24q32@?40"
+ "webPresentmentBrandEntitlements"
+ "webPresentmentBrandEntitlementsStaging"
+ "webPresentmentBrandInformation"
+ "webPresentmentBrandInformationStaging"
+ "webPresentmentFetchTimingMeasurementForItemIdentifier:"
+ "web_presentment_items.db"
+ "{?=\"itemTtl\"b1}"
- "\b "
- "\r\xff"
- "\x0e\xff"
- "\x0f\xff"
- "\x10 "
- "\x10\xff"
- "\x11 "
- "\x11\xff"
- "\x12 "
- "\x12\""
- "\x12\xff"
- "\x13 "
- "\x13\xff"
- "\x14 "
- "\x14\xff"
- "\x15 "
- "\x15\xff"
- "\x16\xff"
- "\x17\xff"
- "\x18\xff"
- "\x19\xff"
- " "
- " - countryCode[%@], nationalNumber[%@], extension[%@], italianLeadingZero[%@], numberOfLeadingZeros[%@], rawInput[%@] countryCodeSource[%@] preferredDomesticCarrierCode[%@]"
- " ext. "
- "$1"
- "$1$2"
- "%@ %@ %@%@"
- "%@%@%@"
- "%@+%@-%@%@"
- "%C"
- "%s Failed to get E164 formated phone number with error %@"
- "%s Failed to get normalized phone number with error %@"
- "%s Successfully truncated a too long phone number"
- "(?:%@)$"
- "(?:.*?[A-Za-z]){3}.*"
- "([%@])"
- "(\\$\\d)"
- "(\\d+)(.*)"
- "* codeID[%@] countryCode[%@] generalDesc[%@] fixedLine[%@] mobile[%@] tollFree[%@] premiumRate[%@] sharedCost[%@] personalNumber[%@] voip[%@] pager[%@] uan[%@] emergency[%@] voicemail[%@] noInternationalDialling[%@] internationalPrefix[%@] preferredInternationalPrefix[%@] nationalPrefix[%@] preferredExtnPrefix[%@] nationalPrefixForParsing[%@] nationalPrefixTransformRule[%@] sameMobileAndFixedLinePattern[%@] numberFormats[%@] intlNumberFormats[%@] mainCountryForCode[%@] leadingDigits[%@] leadingZeroPossible[%@]"
- "+"
- "+%@ %@%@"
- "+%@%@"
- "+%@%@%@"
- "+[BCSPhoneNumberNormalizer normalizedPhoneNumberForPhoneNumber:]"
- "-"
- "-[BCSRemoteFetchPIR decompressData:error:]"
- "."
- "0"
- "001"
- "1%@"
- "2"
- "3"
- "4"
- "5"
- "6"
- "7"
- "8"
- "9"
- "999999999999999"
- ";"
- ";ext="
- ";isub="
- ";phone-context="
- "<SEP>"
- "@\"NSCache\""
- "@\"NSMutableString\""
- "@\"NSRegularExpression\""
- "@\"_NBMetadataHelper\""
- "@\"_NBPhoneMetaData\""
- "@\"_NBPhoneNumberDesc\""
- "@\"_NBPhoneNumberUtil\""
- "@\"_NBRegExMatcher\""
- "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
- "@256@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248"
- "@28@0:8@16B24"
- "@32@0:8Q16#24"
- "@36@0:8@16@24B32"
- "@40@0:8*16Q24Q32"
- "@40@0:8@16Q24^@32"
- "@40@0:8@16q24^@32"
- "@44@0:8@16@24B32^@36"
- "@48@0:8@16@24B32B36^@40"
- "@48@0:8@16@24q32@40"
- "@48@0:8@16q24@32^@40"
- "@60@0:8@16@24@32@40B48@52"
- "@60@0:8@16@24^@32B40^@44^@52"
- "A"
- "A-Za-z"
- "AR"
- "B24@?0@8@\"NSDictionary\"16"
- "B32@0:8@16^@24"
- "B36@0:8@16@24B32"
- "B40@0:8@16@24^@32"
- "B40@0:8^@16@24^@32"
- "BCSPhoneNumberNormalizer"
- "BR"
- "C"
- "CAPTURING_DIGIT_PATTERN"
- "CCode2CNMap"
- "CHARACTER_CLASS_PATTERN_"
- "CN2CCodeMap"
- "CO"
- "D"
- "DIGIT_MAPPINGS"
- "DIGIT_PATTERN_"
- "E"
- "ELIGIBLE_FORMAT_PATTERN_"
- "Error fetching data from PIR (%@): %@"
- "F"
- "Failed to decompress data (%@)!"
- "Failed to unzip data"
- "G"
- "H"
- "I"
- "INVALID_COUNTRY_CODE"
- "INVALID_COUNTRY_CODE:%@"
- "INVALID_REGION_CODE"
- "ISOCountryCodes"
- "Invalid country code:%@"
- "Invalid region code:%@"
- "J"
- "K"
- "L"
- "M"
- "MX"
- "N"
- "NA"
- "NATIONAL_PREFIX_SEPARATORS_PATTERN_"
- "NOT_A_NUMBER"
- "NOT_A_NUMBER:%@"
- "Nil item & nil fetchItemError"
- "NonMatch"
- "O"
- "P"
- "R"
- "S"
- "STANDALONE_DIGIT_PATTERN_"
- "T"
- "T@\"CTTelephonyNetworkInfo\",R,N"
- "T@\"NSArray\",&,N,V_intlNumberFormats"
- "T@\"NSArray\",&,N,V_leadingDigitsPatterns"
- "T@\"NSArray\",&,N,V_numberFormats"
- "T@\"NSArray\",R,N,V_possibleLength"
- "T@\"NSArray\",R,N,V_possibleLengthLocalOnly"
- "T@\"NSCache\",&,N,V_cache"
- "T@\"NSCache\",&,N,V_metadataCache"
- "T@\"NSData\",R,N,V_nationalNumberMatcherData"
- "T@\"NSData\",R,N,V_possibleNumberMatcherData"
- "T@\"NSLock\",&,N,V_entireStringCacheLock"
- "T@\"NSLock\",&,N,V_lockPatternCache"
- "T@\"NSMutableArray\",&,N,V_possibleFormats_"
- "T@\"NSMutableDictionary\",&,N,V_entireStringRegexCache"
- "T@\"NSMutableDictionary\",&,N,V_regexPatternCache"
- "T@\"NSMutableString\",&,N,V_accruedInputWithoutFormatting_"
- "T@\"NSMutableString\",&,N,V_accruedInput_"
- "T@\"NSMutableString\",&,N,V_formattingTemplate_"
- "T@\"NSMutableString\",&,N,V_nationalNumber_"
- "T@\"NSMutableString\",&,N,V_prefixBeforeNationalNumber_"
- "T@\"NSNumber\",&,N,V_countryCode"
- "T@\"NSNumber\",&,N,V_countryCodeSource"
- "T@\"NSNumber\",&,N,V_nationalNumber"
- "T@\"NSNumber\",&,N,V_numberOfLeadingZeros"
- "T@\"NSRegularExpression\",&,N,V_CAPTURING_DIGIT_PATTERN"
- "T@\"NSRegularExpression\",&,N,V_CHARACTER_CLASS_PATTERN_"
- "T@\"NSRegularExpression\",&,N,V_DIGIT_PATTERN_"
- "T@\"NSRegularExpression\",&,N,V_ELIGIBLE_FORMAT_PATTERN_"
- "T@\"NSRegularExpression\",&,N,V_NATIONAL_PREFIX_SEPARATORS_PATTERN_"
- "T@\"NSRegularExpression\",&,N,V_STANDALONE_DIGIT_PATTERN_"
- "T@\"NSRegularExpression\",&,N,V_VALID_ALPHA_PHONE_PATTERN"
- "T@\"NSString\",&,N,V_codeID"
- "T@\"NSString\",&,N,V_currentFormattingPattern_"
- "T@\"NSString\",&,N,V_currentOutput_"
- "T@\"NSString\",&,N,V_defaultCountry_"
- "T@\"NSString\",&,N,V_domesticCarrierCodeFormattingRule"
- "T@\"NSString\",&,N,V_extension"
- "T@\"NSString\",&,N,V_format"
- "T@\"NSString\",&,N,V_internationalPrefix"
- "T@\"NSString\",&,N,V_leadingDigits"
- "T@\"NSString\",&,N,V_nationalPrefix"
- "T@\"NSString\",&,N,V_nationalPrefixExtracted_"
- "T@\"NSString\",&,N,V_nationalPrefixForParsing"
- "T@\"NSString\",&,N,V_nationalPrefixFormattingRule"
- "T@\"NSString\",&,N,V_nationalPrefixTransformRule"
- "T@\"NSString\",&,N,V_pattern"
- "T@\"NSString\",&,N,V_preferredDomesticCarrierCode"
- "T@\"NSString\",&,N,V_preferredExtnPrefix"
- "T@\"NSString\",&,N,V_preferredInternationalPrefix"
- "T@\"NSString\",&,N,V_rawInput"
- "T@\"NSString\",R,N,V_exampleNumber"
- "T@\"NSString\",R,N,V_nationalNumberPattern"
- "T@\"NSString\",R,N,V_possibleNumberPattern"
- "T@\"_NBMetadataHelper\",&,N,V_helper"
- "T@\"_NBPhoneMetaData\",&,N,V_currentMetaData_"
- "T@\"_NBPhoneMetaData\",&,N,V_defaultMetaData_"
- "T@\"_NBPhoneNumberDesc\",&,N,V_emergency"
- "T@\"_NBPhoneNumberDesc\",&,N,V_fixedLine"
- "T@\"_NBPhoneNumberDesc\",&,N,V_generalDesc"
- "T@\"_NBPhoneNumberDesc\",&,N,V_mobile"
- "T@\"_NBPhoneNumberDesc\",&,N,V_noInternationalDialling"
- "T@\"_NBPhoneNumberDesc\",&,N,V_pager"
- "T@\"_NBPhoneNumberDesc\",&,N,V_personalNumber"
- "T@\"_NBPhoneNumberDesc\",&,N,V_premiumRate"
- "T@\"_NBPhoneNumberDesc\",&,N,V_sharedCost"
- "T@\"_NBPhoneNumberDesc\",&,N,V_tollFree"
- "T@\"_NBPhoneNumberDesc\",&,N,V_uan"
- "T@\"_NBPhoneNumberDesc\",&,N,V_voicemail"
- "T@\"_NBPhoneNumberDesc\",&,N,V_voip"
- "T@\"_NBPhoneNumberUtil\",&,N,V_phoneUtil_"
- "T@\"_NBRegExMatcher\",&,N,V_matcher"
- "TB,N,V_ableToFormat_"
- "TB,N,V_inputHasFormatting_"
- "TB,N,V_isCompleteNumber_"
- "TB,N,V_isExpectingCountryCallingCode_"
- "TB,N,V_italianLeadingZero"
- "TB,N,V_leadingZeroPossible"
- "TB,N,V_mainCountryForCode"
- "TB,N,V_nationalPrefixOptionalWhenFormatting"
- "TB,N,V_sameMobileAndFixedLinePattern"
- "TB,N,V_shouldAddSpaceAfterNationalPrefix_"
- "TB,R,N,V_isSuccessfulFormatting"
- "TOO_LONG"
- "TOO_LONG:%@"
- "TOO_SHORT_AFTER_IDD"
- "TOO_SHORT_AFTER_IDD:%@"
- "TOO_SHORT_NSN"
- "TOO_SHORT_NSN:%@"
- "TQ,N,V_lastMatchPosition_"
- "TQ,N,V_originalPosition_"
- "TQ,N,V_positionToRemember_"
- "U"
- "V"
- "VALID_ALPHA_PHONE_PATTERN"
- "W"
- "X"
- "Y"
- "Z"
- "ZZ"
- "[%@%@]"
- "[%@]+"
- "[- ]"
- "[\\\\\\/] *x"
- "[\\d]+(?:[~\\u2053\\u223C\\uFF5E][\\d]+)?"
- "[^%@%@#]+$"
- "[pattern:%@, format:%@, leadingDigitsPattern:%@, nationalPrefixFormattingRule:%@, nationalPrefixOptionalWhenFormatting:%@, domesticCarrierCodeFormattingRule:%@]"
- "\\$1"
- "\\$CC"
- "\\$FG"
- "\\$NP"
- "\\D+"
- "\\[([^\\[\\]])*\\]"
- "\\\\d"
- "\\d(?=[^,}][^,}])"
- "^"
- "^%@"
- "^(?:%@)"
- "^(?:%@)$"
- "^(?:\\+|%@)"
- "^[%@]+"
- "^\\(?\\$1\\)?"
- "_CAPTURING_DIGIT_PATTERN"
- "_CHARACTER_CLASS_PATTERN_"
- "_DIGIT_PATTERN_"
- "_ELIGIBLE_FORMAT_PATTERN_"
- "_NATIONAL_PREFIX_SEPARATORS_PATTERN_"
- "_NBAdditions"
- "_NBAsYouTypeFormatter"
- "_NBMetadataHelper"
- "_NBNumberFormat"
- "_NBPhoneMetaData"
- "_NBPhoneNumber"
- "_NBPhoneNumberDesc"
- "_NBPhoneNumberUtil"
- "_NBRegExMatcher"
- "_NBRegularExpressionCache"
- "_STANDALONE_DIGIT_PATTERN_"
- "_VALID_ALPHA_PHONE_PATTERN"
- "_ableToFormat_"
- "_accruedInputWithoutFormatting_"
- "_accruedInput_"
- "_cache"
- "_codeID"
- "_countryCodeSource"
- "_currentFormattingPattern_"
- "_currentMetaData_"
- "_currentOutput_"
- "_defaultCountry_"
- "_defaultMetaData_"
- "_domesticCarrierCodeFormattingRule"
- "_emergency"
- "_entireStringCacheLock"
- "_entireStringRegexCache"
- "_exampleNumber"
- "_extension"
- "_fixedLine"
- "_format"
- "_formattingTemplate_"
- "_generalDesc"
- "_helper"
- "_inputHasFormatting_"
- "_internationalPrefix"
- "_intlNumberFormats"
- "_isCompleteNumber_"
- "_isExpectingCountryCallingCode_"
- "_isSuccessfulFormatting"
- "_italianLeadingZero"
- "_lastMatchPosition_"
- "_leadingDigits"
- "_leadingDigitsPatterns"
- "_leadingZeroPossible"
- "_lockPatternCache"
- "_mainCountryForCode"
- "_matcher"
- "_metadataCache"
- "_mobile"
- "_nationalNumber"
- "_nationalNumberMatcherData"
- "_nationalNumberPattern"
- "_nationalNumber_"
- "_nationalPrefix"
- "_nationalPrefixExtracted_"
- "_nationalPrefixForParsing"
- "_nationalPrefixFormattingRule"
- "_nationalPrefixOptionalWhenFormatting"
- "_nationalPrefixTransformRule"
- "_noInternationalDialling"
- "_numberFormats"
- "_numberOfLeadingZeros"
- "_originalPosition_"
- "_pager"
- "_personalNumber"
- "_phoneUtil_"
- "_positionToRemember_"
- "_possibleFormats_"
- "_possibleLength"
- "_possibleLengthLocalOnly"
- "_possibleNumberMatcherData"
- "_possibleNumberPattern"
- "_preferredDomesticCarrierCode"
- "_preferredExtnPrefix"
- "_preferredInternationalPrefix"
- "_prefixBeforeNationalNumber_"
- "_premiumRate"
- "_rawInput"
- "_regexPatternCache"
- "_sameMobileAndFixedLinePattern"
- "_sharedCost"
- "_shouldAddSpaceAfterNationalPrefix_"
- "_tollFree"
- "_uan"
- "_voicemail"
- "_voip"
- "`\x06"
- "` "
- "a\x06"
- "ableToExtractLongerNdd_"
- "ableToFormat_"
- "accruedInputWithoutFormatting_"
- "accruedInput_"
- "appendNationalNumber_:"
- "arrayByAddingObjectsFromArray:"
- "attemptToChooseFormattingPattern_"
- "attemptToChoosePatternWithPrefixExtracted_"
- "attemptToExtractCountryCallingCode_"
- "attemptToExtractIdd_"
- "attemptToFormatAccruedDigits_"
- "b"
- "b\x06"
- "buildNationalNumberForParsing:nationalNumber:"
- "c"
- "c\x06"
- "cache"
- "canBeInternationallyDialled:"
- "canBeInternationallyDialled:error:"
- "checkRegionForParsing:defaultRegion:"
- "chooseFormattingPatternForNumber:nationalNumber:"
- "clear"
- "clearCountryCodeSource"
- "codeID"
- "componentsSeparatedByRegex:regex:"
- "containsObject:"
- "convertAlphaCharactersInNumber:"
- "countryCode"
- "countryCodeByCarrier"
- "countryCodeFromRegionCode:"
- "countryCodeSource"
- "countryCodeToRegionCodeMap"
- "countryToMetadata"
- "createFormattingTemplate_:"
- "currentFormattingPattern_"
- "currentMetaData_"
- "currentOutput_"
- "d\x06"
- "decimalDigitCharacterSet"
- "decodeObjectForKey:"
- "decompressData:error:"
- "defaultCountry_"
- "defaultMetaData_"
- "descHasPossibleNumberData:"
- "dictionaryWithObject:forKey:"
- "displayNameForKey:value:"
- "domesticCarrierCodeFormattingRule"
- "e"
- "e\x06"
- "emergency"
- "entireRegularExpressionWithPattern:options:error:"
- "entireStringCacheLock"
- "entireStringRegexCache"
- "errorWithObject:withDomain:"
- "exampleNumber"
- "extension"
- "extractCountryCode:nationalNumber:"
- "extractPossibleNumber:"
- "f"
- "f\x06"
- "f\t"
- "filteredArrayUsingPredicate:"
- "firstMatchInString:options:range:"
- "fixedLine"
- "formUnionWithCharacterSet:"
- "format"
- "format:numberFormat:"
- "format:numberFormat:error:"
- "formatByPattern:numberFormat:userDefinedFormats:"
- "formatByPattern:numberFormat:userDefinedFormats:error:"
- "formatInOriginalFormat:regionCallingFrom:"
- "formatInOriginalFormat:regionCallingFrom:error:"
- "formatNationalNumberWithCarrierCode:carrierCode:"
- "formatNationalNumberWithCarrierCode:carrierCode:error:"
- "formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:"
- "formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:error:"
- "formatNsn:metadata:phoneNumberFormat:carrierCode:"
- "formatNsnUsingPattern:formattingPattern:numberFormat:carrierCode:"
- "formatNumberForMobileDialing:regionCallingFrom:withFormatting:"
- "formatNumberForMobileDialing:regionCallingFrom:withFormatting:error:"
- "formatOutOfCountryCallingNumber:regionCallingFrom:"
- "formatOutOfCountryCallingNumber:regionCallingFrom:error:"
- "formatOutOfCountryKeepingAlphaChars:regionCallingFrom:"
- "formatOutOfCountryKeepingAlphaChars:regionCallingFrom:error:"
- "formattingRuleHasFirstGroupOnly:"
- "formattingTemplate_"
- "g"
- "g\x06"
- "g\t"
- "generalDesc"
- "getAllMetadata"
- "getAvailableFormats_:"
- "getCountryCodeForRegion:"
- "getCountryCodeForValidRegion:error:"
- "getCountryCodeSourceOrDefault"
- "getCountryMobileTokenFromCountryCode:"
- "getExampleNumber:error:"
- "getExampleNumberForNonGeoEntity:error:"
- "getExampleNumberForType:type:error:"
- "getFormattingTemplate_:numberFormat:"
- "getLengthOfGeographicalAreaCode:"
- "getLengthOfGeographicalAreaCode:error:"
- "getLengthOfNationalDestinationCode:"
- "getLengthOfNationalDestinationCode:error:"
- "getMetadataForNonGeographicalRegion:"
- "getMetadataForRegion:"
- "getMetadataForRegionOrCallingCode:regionCode:"
- "getMetadataForRegion_:"
- "getNationalSignificantNumber:"
- "getNddPrefixForRegion:stripNonDigits:"
- "getNumberDescByType:type:"
- "getNumberType:"
- "getNumberTypeHelper:metadata:"
- "getRegionCodeForCountryCode:"
- "getRegionCodeForNumber:"
- "getRegionCodeForNumberFromRegionList:regionCodes:"
- "getRegionCodesForCountryCode:"
- "getRememberedPosition"
- "getSupportedRegions"
- "h"
- "h\x06"
- "h\t"
- "hasFormattingPatternForNumber:"
- "hasSuffix:"
- "hasUnexpectedItalianLeadingZero:"
- "hasValidCountryCallingCode:"
- "hasValue:"
- "helper"
- "i\x06"
- "i\t"
- "i32@0:8@16@24"
- "i32@0:8@16^@24"
- "indexOfObject:"
- "indexOfStringByString:target:"
- "initNormalizationMappings"
- "initRegularExpressionSet"
- "initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:businessEmailMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:businessEmailConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:businessEmailShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:businessEmailItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:"
- "initWithChatSuggestMegashardFetcher:businessLinkMegashardFetcher:businessCallerMegashardFetcher:businessEmailMegashardFetcher:shardCache:cacheManager:chatSuggestRemoteFetcher:businessLinkRemoteFetcher:businessCallerRemoteFetcher:businessEmailRemoteFetcher:userDefaults:metricFactory:"
- "initWithEntry:"
- "initWithItemIdentifier:clientBundleId:shardType:cacheOnly:"
- "initWithPattern:options:error:"
- "initWithPattern:withFormat:withLeadingDigitsPatterns:withNationalPrefixFormattingRule:whenFormatting:withDomesticCarrierCodeFormattingRule:"
- "initWithRegionCode:"
- "initWithRegionCode:bundle:"
- "initialize"
- "inputAccruedNationalNumber_"
- "inputDigit:"
- "inputDigitAndRememberPosition:"
- "inputDigitHelper_:"
- "inputDigitWithOptionToRememberPosition_:rememberPosition:"
- "inputHasFormatting_"
- "inputString:"
- "inputStringAndRememberPosition:"
- "internationalPrefix"
- "intlNumberFormats"
- "invertedSet"
- "isAllDigits:"
- "isAlphaNumber:"
- "isCompleteNumber_"
- "isDigitOrLeadingPlusSign_:"
- "isEqualToNumber:"
- "isExpectingCountryCallingCode_"
- "isFormatEligible_:"
- "isLeadingZeroPossible:"
- "isNANPACountry:"
- "isNanpaNumberWithNationalPrefix_"
- "isNationalNumberSuffixOfTheOther:second:"
- "isNumberGeographical:"
- "isNumberMatch:second:"
- "isNumberMatch:second:error:"
- "isNumberMatchingDesc:numberDesc:"
- "isPossibleNumber:"
- "isPossibleNumber:error:"
- "isPossibleNumberString:regionDialingFrom:error:"
- "isPossibleNumberWithReason:"
- "isPossibleNumberWithReason:error:"
- "isStartingStringByRegex:regex:"
- "isSuccessfulFormatting"
- "isValidNumber:"
- "isValidNumberForRegion:regionCode:"
- "isValidRegionCode:"
- "isViablePhoneNumber:"
- "isoCountryCode"
- "italianLeadingZero"
- "j\t"
- "jsonObjectFromZippedDataWithBytes:compressedLength:expandedLength:"
- "k"
- "k\t"
- "l"
- "l\t"
- "lastMatchPosition_"
- "lastObject"
- "leadingDigits"
- "leadingDigitsPatterns"
- "leadingZeroPossible"
- "localeIdentifierFromComponents:"
- "lockPatternCache"
- "m"
- "m\t"
- "mainCountryForCode"
- "matchFirstByRegex:regex:"
- "matchNationalNumber:phoneNumberDesc:allowsPrefixMatch:"
- "matchedStringByRegex:regex:"
- "matcher"
- "matchesByRegex:regex:"
- "matchesEntirely:string:"
- "matchesInString:options:range:"
- "maybeCreateNewTemplate_"
- "maybeExtractCountryCode:metadata:nationalNumber:keepRawInput:phoneNumber:error:"
- "maybeGetFormattedExtension:metadata:numberFormat:"
- "maybeStripExtension:"
- "maybeStripInternationalPrefixAndNormalize:possibleIddPrefix:"
- "maybeStripNationalPrefixAndCarrierCode:metadata:carrierCode:"
- "metadata"
- "metadataCache"
- "mobile"
- "n"
- "n\t"
- "narrowDownPossibleFormats_:"
- "nationalNumber"
- "nationalNumberMatcherData"
- "nationalNumberPattern"
- "nationalNumberPattern[%@] possibleNumberPattern[%@] possibleLength[%@] possibleLengthLocalOnly[%@] exampleNumber[%@]"
- "nationalNumber_"
- "nationalPrefix"
- "nationalPrefixExtracted_"
- "nationalPrefixForParsing"
- "nationalPrefixFormattingRule"
- "nationalPrefixOptionalWhenFormatting"
- "nationalPrefixTransformRule"
- "nb_safeArrayAtIndex:"
- "nb_safeDataAtIndex:"
- "nb_safeNumberAtIndex:"
- "nb_safeObjectAtIndex:class:"
- "nb_safeStringAtIndex:"
- "noInternationalDialling"
- "normalize:"
- "normalizeAndAccrueDigitsAndPlusSign_:rememberPosition:"
- "normalizeDiallableCharsOnly:"
- "normalizeDigitsOnly:"
- "normalizeHelper:normalizationReplacements:removeNonMatches:"
- "normalizeSB:"
- "numberFormats"
- "numberFormatsFromEntry:"
- "numberOfLeadingZeros"
- "numberOfRanges"
- "o"
- "o\t"
- "originalPosition_"
- "p"
- "pager"
- "parse:defaultRegion:error:"
- "parseAndKeepRawInput:defaultRegion:error:"
- "parseHelper:defaultRegion:keepRawInput:checkRegion:error:"
- "parsePrefixAsIdd:sourceString:"
- "parseWithPhoneCarrierRegion:error:"
- "personalNumber"
- "phoneNumberDataMap"
- "phoneUtil_"
- "positionToRemember_"
- "possibleFormats_"
- "possibleLength"
- "possibleLengthLocalOnly"
- "possibleNumberMatcherData"
- "possibleNumberPattern"
- "predicateWithBlock:"
- "preferredDomesticCarrierCode"
- "preferredExtnPrefix"
- "preferredInternationalPrefix"
- "prefixBeforeNationalNumber_"
- "prefixNumberWithCountryCallingCode:phoneNumberFormat:formattedNationalNumber:formattedExtension:"
- "premiumRate"
- "q32@0:8@16@24"
- "q32@0:8@16^@24"
- "q32@0:8^@16@24"
- "q40@0:8@16@24^@32"
- "q40@0:8@16@24q32"
- "r"
- "range"
- "rangeAtIndex:"
- "rangeOfCharacterFromSet:"
- "rangeOfFirstMatchInString:options:range:"
- "rangeOfString:options:range:"
- "rawInput"
- "rawInputContainsNationalPrefix:nationalPrefix:regionCode:"
- "regexPatternCache"
- "regionCodeFromCountryCode:"
- "regularExpressionForPattern:error:"
- "regularExpressionWithPattern:options:error:"
- "removeLastDigit"
- "removeLastDigitAndRememberPosition"
- "removeNationalPrefixFromNationalNumber_"
- "removeObjectAtIndex:"
- "replaceFirstStringByRegex:regex:withTemplate:"
- "replaceStringByRegex:regex:withTemplate:"
- "s"
- "sameMobileAndFixedLinePattern"
- "setAbleToFormat_:"
- "setAccruedInputWithoutFormatting_:"
- "setAccruedInput_:"
- "setCAPTURING_DIGIT_PATTERN:"
- "setCHARACTER_CLASS_PATTERN_:"
- "setCache:"
- "setCodeID:"
- "setCountryCode:"
- "setCountryCodeSource:"
- "setCurrentFormattingPattern_:"
- "setCurrentMetaData_:"
- "setCurrentOutput_:"
- "setDIGIT_PATTERN_:"
- "setDefaultCountry_:"
- "setDefaultMetaData_:"
- "setDomesticCarrierCodeFormattingRule:"
- "setELIGIBLE_FORMAT_PATTERN_:"
- "setEmergency:"
- "setEntireStringCacheLock:"
- "setEntireStringRegexCache:"
- "setExtension:"
- "setFixedLine:"
- "setFormat:"
- "setFormattingTemplate_:"
- "setGeneralDesc:"
- "setHelper:"
- "setInputHasFormatting_:"
- "setInternationalPrefix:"
- "setIntlNumberFormats:"
- "setIsCompleteNumber_:"
- "setIsExpectingCountryCallingCode_:"
- "setItalianLeadingZero:"
- "setItalianLeadingZerosForPhoneNumber:phoneNumber:"
- "setLastMatchPosition_:"
- "setLeadingDigits:"
- "setLeadingDigitsPatterns:"
- "setLeadingZeroPossible:"
- "setLockPatternCache:"
- "setMainCountryForCode:"
- "setMatcher:"
- "setMetadataCache:"
- "setMobile:"
- "setNATIONAL_PREFIX_SEPARATORS_PATTERN_:"
- "setNationalNumber:"
- "setNationalNumber_:"
- "setNationalPrefix:"
- "setNationalPrefixExtracted_:"
- "setNationalPrefixForParsing:"
- "setNationalPrefixFormattingRule:"
- "setNationalPrefixOptionalWhenFormatting:"
- "setNationalPrefixTransformRule:"
- "setNoInternationalDialling:"
- "setNumberFormats:"
- "setNumberOfLeadingZeros:"
- "setOriginalPosition_:"
- "setPager:"
- "setPattern:"
- "setPersonalNumber:"
- "setPhoneUtil_:"
- "setPositionToRemember_:"
- "setPossibleFormats_:"
- "setPreferredDomesticCarrierCode:"
- "setPreferredExtnPrefix:"
- "setPreferredInternationalPrefix:"
- "setPrefixBeforeNationalNumber_:"
- "setPremiumRate:"
- "setRawInput:"
- "setRegexPatternCache:"
- "setSTANDALONE_DIGIT_PATTERN_:"
- "setSameMobileAndFixedLinePattern:"
- "setSharedCost:"
- "setShouldAddSpaceAfterNationalPrefix_:"
- "setString:"
- "setTollFree:"
- "setUan:"
- "setVALID_ALPHA_PHONE_PATTERN:"
- "setVoicemail:"
- "setVoip:"
- "sharedCost"
- "shouldAddSpaceAfterNationalPrefix_"
- "sortedArrayUsingSelector:"
- "stringByPaddingToLength:withString:startingAtIndex:"
- "stringByReplacingMatchesInString:options:range:withTemplate:"
- "stringByReplacingOccurrencesString:withMap:removeNonMatches:"
- "stringPositionByRegex:regex:"
- "stringWithCharacters:length:"
- "stringWithString:"
- "subscriberCellularProvider"
- "substringFromIndex:"
- "systemLocale"
- "t"
- "tel:"
- "telephonyNetworkInfo"
- "testNumberLength:desc:"
- "tollFree"
- "truncateTooLongNumber:"
- "u"
- "uan"
- "unsignedLongLongValue"
- "uppercaseString"
- "us"
- "v"
- "v24@0:8^@16"
- "v32@0:8@16^@24"
- "validateNumberLength:metadata:"
- "validateNumberLength:metadata:type:"
- "voicemail"
- "voip"
- "w"
- "whitespaceAndNewlineCharacterSet"
- "x"
- "y"
- "z"
- "|"
- "~"
- "\xa0"
- "\xe6\t"
- "\xe7\t"
- "\xe8\t"
- "\xe9\t"
- "\xea\t"
- "\xeb\t"
- "\xec\t"
- "\xed\t"
- "\xee\t"
- "\xef\t"
- "\xf0\x06"
- "\xf1\x06"
- "\xf2\x06"
- "\xf3\x06"
- "\xf4\x06"
- "\xf5\x06"
- "\xf6\x06"
- "\xf7\x06"
- "\xf8\x06"
- "\xf9\x06"

```
