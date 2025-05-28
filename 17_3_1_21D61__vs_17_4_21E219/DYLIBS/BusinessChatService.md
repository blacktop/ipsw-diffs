## BusinessChatService

> `/System/Library/PrivateFrameworks/BusinessChatService.framework/BusinessChatService`

```diff

-30062.31.8.11.2
-  __TEXT.__text: 0x5897c
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x594c
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x67b8
-  __TEXT.__oslogstring: 0x343d
-  __TEXT.__gcc_except_tab: 0x5bc
+30064.34.9.13.23
+  __TEXT.__text: 0x5eaec
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x5f94
+  __TEXT.__const: 0x100
+  __TEXT.__cstring: 0x6cb6
+  __TEXT.__oslogstring: 0x37c9
+  __TEXT.__gcc_except_tab: 0x630
   __TEXT.__ustring: 0x5b0
-  __TEXT.__unwind_info: 0x12d0
-  __TEXT.__objc_classname: 0x1213
-  __TEXT.__objc_methname: 0xba69
-  __TEXT.__objc_methtype: 0x2650
-  __TEXT.__objc_stubs: 0x8280
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x1400
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __TEXT.__unwind_info: 0x13e4
+  __TEXT.__objc_classname: 0x1360
+  __TEXT.__objc_methname: 0xc7da
+  __TEXT.__objc_methtype: 0x28af
+  __TEXT.__objc_stubs: 0x8b20
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x1600
+  __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xba38
-  __DATA_CONST.__objc_selrefs: 0x2948
+  __DATA_CONST.__objc_const: 0xc318
+  __DATA_CONST.__objc_selrefs: 0x2c30
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x520
+  __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__objc_const: 0x3090
-  __AUTH_CONST.__cfstring: 0x5000
-  __AUTH_CONST.__const: 0x260
+  __AUTH_CONST.__objc_const: 0x33a8
+  __AUTH_CONST.__cfstring: 0x5280
+  __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x4c0
-  __AUTH.__objc_data: 0xde8
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x4d8
-  __DATA.__objc_superrefs: 0x2d0
-  __DATA.__objc_ivar: 0x4cc
-  __DATA.__data: 0xd2f0
+  __AUTH_CONST.__auth_got: 0x4e0
+  __AUTH.__objc_data: 0xf78
+  __DATA.__objc_ivar: 0x510
+  __DATA.__data: 0xd4d0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_ivar: 0x240
-  __DATA_DIRTY.__objc_data: 0x1978
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__objc_ivar: 0x258
+  __DATA_DIRTY.__objc_data: 0x19c8
+  __DATA_DIRTY.__bss: 0x188
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/BlastDoor.framework/BlastDoor
+  - /System/Library/PrivateFrameworks/CipherML.framework/CipherML
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
+  - /System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/MessagesBlastDoorSupport
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2047
-  Symbols:   7285
-  CStrings:  3559
+  Functions: 2188
+  Symbols:   7777
+  CStrings:  3786
 
Symbols:
+ +[BCSBlastDoorHelper defaultHelper]
+ +[BCSCallerIdParquetMessage intentType]
+ +[BCSCallerIdParquetMessage nameType]
+ +[BCSExecutionTimer timeExecutionOfBlock:]
+ +[BCSPathProvider sharedInstance]
+ -[BCSBlastDoorHelper .cxx_destruct]
+ -[BCSBlastDoorHelper initWithPersistentStore:]
+ -[BCSBlastDoorHelper safeImageURLFromImage:imageFormat:error:]
+ -[BCSBlastDoorHelper safeImageURLFromImage:imageFormat:maxPixelDimension:scale:error:]
+ -[BCSBlastDoorHelper safeImageURLFromImageURL:error:]
+ -[BCSBlastDoorHelper safeImageURLFromImageURL:maxPixelDimension:scale:error:]
+ -[BCSBlastDoorHelper setStore:]
+ -[BCSBlastDoorHelper store]
+ -[BCSBlastDoorHelper warmUpBlastDoor]
+ -[BCSBlastDoorPersistentStore .cxx_destruct]
+ -[BCSBlastDoorPersistentStore cacheURL]
+ -[BCSBlastDoorPersistentStore deleteExpiredImages]
+ -[BCSBlastDoorPersistentStore deleteImageWithName:]
+ -[BCSBlastDoorPersistentStore fileURLForImageWithName:error:]
+ -[BCSBlastDoorPersistentStore initWithCacheURL:]
+ -[BCSBlastDoorPersistentStore setCacheURL:]
+ -[BCSBlastDoorPersistentStore updateImageWithName:error:]
+ -[BCSBusinessCallerItem initWithPhoneNumber:name:department:logoURL:logo:logoFormat:verified:]
+ -[BCSBusinessCallerItem initWithPhoneNumber:phoneHash:localizedNames:localizedDepartments:logoURL:logo:logoFormat:verified:]
+ -[BCSBusinessCallerItem isVerified]
+ -[BCSBusinessCallerItem localizedDepartments]
+ -[BCSBusinessCallerItem localizedNames]
+ -[BCSBusinessCallerItem logoFormat]
+ -[BCSBusinessCallerItem logo]
+ -[BCSBusinessCallerItem message]
+ -[BCSBusinessCallerItem setLogoURL:]
+ -[BCSBusinessCallerItem setMessage:]
+ -[BCSBusinessCallerItem(ProtoConversion) initWithParquetMessage:]
+ -[BCSBusinessQueryController fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:metadataCallback:logoURLCallback:completion:]
+ -[BCSBusinessQueryController initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:]
+ -[BCSBusinessQueryService fetchBusinessCallerMetadataForPhoneNumber:metadataCallback:logoURLCallback:completion:]
+ -[BCSCallerIdParquetMessage .cxx_destruct]
+ -[BCSCallerIdParquetMessage addIntent:]
+ -[BCSCallerIdParquetMessage addName:]
+ -[BCSCallerIdParquetMessage clearIntents]
+ -[BCSCallerIdParquetMessage clearNames]
+ -[BCSCallerIdParquetMessage copyTo:]
+ -[BCSCallerIdParquetMessage copyWithZone:]
+ -[BCSCallerIdParquetMessage description]
+ -[BCSCallerIdParquetMessage dictionaryRepresentation]
+ -[BCSCallerIdParquetMessage hasIsVerified]
+ -[BCSCallerIdParquetMessage hasLogoFormat]
+ -[BCSCallerIdParquetMessage hasLogo]
+ -[BCSCallerIdParquetMessage hasPhoneHash]
+ -[BCSCallerIdParquetMessage hasPhoneNumber]
+ -[BCSCallerIdParquetMessage hash]
+ -[BCSCallerIdParquetMessage intentAtIndex:]
+ -[BCSCallerIdParquetMessage intentsCount]
+ -[BCSCallerIdParquetMessage intents]
+ -[BCSCallerIdParquetMessage isEqual:]
+ -[BCSCallerIdParquetMessage isVerified]
+ -[BCSCallerIdParquetMessage logoFormat]
+ -[BCSCallerIdParquetMessage logo]
+ -[BCSCallerIdParquetMessage mergeFrom:]
+ -[BCSCallerIdParquetMessage nameAtIndex:]
+ -[BCSCallerIdParquetMessage namesCount]
+ -[BCSCallerIdParquetMessage names]
+ -[BCSCallerIdParquetMessage phoneHash]
+ -[BCSCallerIdParquetMessage phoneNumber]
+ -[BCSCallerIdParquetMessage readFrom:]
+ -[BCSCallerIdParquetMessage setHasIsVerified:]
+ -[BCSCallerIdParquetMessage setHasPhoneHash:]
+ -[BCSCallerIdParquetMessage setIntents:]
+ -[BCSCallerIdParquetMessage setIsVerified:]
+ -[BCSCallerIdParquetMessage setLogo:]
+ -[BCSCallerIdParquetMessage setLogoFormat:]
+ -[BCSCallerIdParquetMessage setNames:]
+ -[BCSCallerIdParquetMessage setPhoneHash:]
+ -[BCSCallerIdParquetMessage setPhoneNumber:]
+ -[BCSCallerIdParquetMessage writeTo:]
+ -[BCSCallerIdParquetWrapper .cxx_destruct]
+ -[BCSCallerIdParquetWrapper copyTo:]
+ -[BCSCallerIdParquetWrapper copyWithZone:]
+ -[BCSCallerIdParquetWrapper description]
+ -[BCSCallerIdParquetWrapper dictionaryRepresentation]
+ -[BCSCallerIdParquetWrapper hasMessage]
+ -[BCSCallerIdParquetWrapper hash]
+ -[BCSCallerIdParquetWrapper isEqual:]
+ -[BCSCallerIdParquetWrapper mergeFrom:]
+ -[BCSCallerIdParquetWrapper message]
+ -[BCSCallerIdParquetWrapper readFrom:]
+ -[BCSCallerIdParquetWrapper setMessage:]
+ -[BCSCallerIdParquetWrapper writeTo:]
+ -[BCSCallerIdResolver .cxx_destruct]
+ -[BCSCallerIdResolver cachedItemMatching:]
+ -[BCSCallerIdResolver decompressData:]
+ -[BCSCallerIdResolver environment]
+ -[BCSCallerIdResolver fetchDataMatching:timeout:completion:]
+ -[BCSCallerIdResolver initWithEnvironment:itemCache:cacheSkipper:metricFactory:]
+ -[BCSCallerIdResolver itemCacheSkipper]
+ -[BCSCallerIdResolver itemCache]
+ -[BCSCallerIdResolver itemMatching:config:clientBundleID:metric:completion:]
+ -[BCSCallerIdResolver metricFactory]
+ -[BCSCallerIdResolver pirClient]
+ -[BCSCallerIdResolver pirQueue]
+ -[BCSCallerIdResolver setMetricFactory:]
+ -[BCSCallerIdResolver setPirClient:]
+ -[BCSCallerIdResolver setPirQueue:]
+ -[BCSExecutionTimer init]
+ -[BCSExecutionTimer milliseconds]
+ -[BCSExecutionTimer nanoseconds]
+ -[BCSExecutionTimer seconds]
+ -[BCSExecutionTimer setStartTime:]
+ -[BCSExecutionTimer startTime]
+ -[BCSICloudServerEnvironment _productionContainerID]
+ -[BCSICloudServerEnvironment pirUseCase]
+ -[BCSMeasurementFactory blastDoorTimingMeasurementForItemIdentifier:]
+ -[BCSMeasurementFactory businessCallerFetchTimingMeasurementForItemIdentifier:]
+ -[BCSPathProvider .cxx_destruct]
+ -[BCSPathProvider _setupStorageWithBaseFileURL:applyFileProtectionType:verificationToken:]
+ -[BCSPathProvider _setupStorageWithSearchPathDirectory:applyFileProtectionType:verificationToken:]
+ -[BCSPathProvider brandLogoCacheURL]
+ -[BCSPathProvider cachesDirectoryFileProtectionLevelVerified]
+ -[BCSPathProvider cachesURL]
+ -[BCSPathProvider documentsDirectoryFileProtectionLevelVerified]
+ -[BCSPathProvider documentsURL]
+ -[BCSPathProvider fileManager]
+ -[BCSPathProvider initWithFileManager:temporaryDirectoryBuilder:]
+ -[BCSPathProvider init]
+ -[BCSPathProvider setCachesDirectoryFileProtectionLevelVerified:]
+ -[BCSPathProvider setDocumentsDirectoryFileProtectionLevelVerified:]
+ -[BCSPathProvider setFileManager:]
+ -[BCSPathProvider setTemporaryDirectoryBuilder:]
+ -[BCSPathProvider tempURL]
+ -[BCSPathProvider temporaryDirectoryBuilder]
+ -[BCSRealTimeTimingSignposter _handleBlastDoorProcessing:]
+ -[BCSRemoteFetchCloudKit environment]
+ GCC_except_table60
+ _BCSAppErrorDomain
+ _BCSErrorDescriptionKey
+ _BCSErrorDeserializingCode
+ _BCSErrorInvalidEntitlementCode
+ _BCSErrorParsingCode
+ _BCSErrorReturnedNoDataCode
+ _BCSErrorTimeoutCode
+ _BCSErrorUnkownCode
+ _BCSNetworkErrorDomain
+ _BCSTimeExecutionOfBlock
+ _BSBrandLogoEntitlement
+ _BlastDoorInstanceTypeDefault
+ _NSFileModificationDate
+ _NSURLContentModificationDateKey
+ _NSURLNameKey
+ _OBJC_CLASS_$_BCSBlastDoorHelper
+ _OBJC_CLASS_$_BCSBlastDoorPersistentStore
+ _OBJC_CLASS_$_BCSCallerIdParquetMessage
+ _OBJC_CLASS_$_BCSCallerIdParquetWrapper
+ _OBJC_CLASS_$_BCSCallerIdResolver
+ _OBJC_CLASS_$_BCSExecutionTimer
+ _OBJC_CLASS_$_CMLClientConfig
+ _OBJC_CLASS_$_CMLKeywordPIRClient
+ _OBJC_CLASS_$_IMMessagesBlastDoorInterface
+ _OBJC_IVAR_$_BCSBlastDoorHelper._blastdoor
+ _OBJC_IVAR_$_BCSBlastDoorHelper._store
+ _OBJC_IVAR_$_BCSBlastDoorPersistentStore._cacheURL
+ _OBJC_IVAR_$_BCSBusinessQueryController._blastDoorHelper
+ _OBJC_IVAR_$_BCSBusinessQueryController._blastDoorWarmedUp
+ _OBJC_IVAR_$_BCSCallerIdParquetWrapper._message
+ _OBJC_IVAR_$_BCSCallerIdResolver._environment
+ _OBJC_IVAR_$_BCSCallerIdResolver._itemCache
+ _OBJC_IVAR_$_BCSCallerIdResolver._itemCacheSkipper
+ _OBJC_IVAR_$_BCSCallerIdResolver._metricFactory
+ _OBJC_IVAR_$_BCSCallerIdResolver._pirClient
+ _OBJC_IVAR_$_BCSCallerIdResolver._pirQueue
+ _OBJC_IVAR_$_BCSExecutionTimer._startTime
+ _OBJC_IVAR_$_BCSPathProvider._cachesDirectoryFileProtectionLevelVerified
+ _OBJC_IVAR_$_BCSPathProvider._documentsDirectoryFileProtectionLevelVerified
+ _OBJC_IVAR_$_BCSPathProvider._fileManager
+ _OBJC_IVAR_$_BCSPathProvider._temporaryDirectoryBuilder
+ _OBJC_METACLASS_$_BCSBlastDoorHelper
+ _OBJC_METACLASS_$_BCSBlastDoorPersistentStore
+ _OBJC_METACLASS_$_BCSCallerIdParquetMessage
+ _OBJC_METACLASS_$_BCSCallerIdParquetWrapper
+ _OBJC_METACLASS_$_BCSCallerIdResolver
+ _OBJC_METACLASS_$_BCSExecutionTimer
+ __OBJC_$_CLASS_METHODS_BCSBlastDoorHelper
+ __OBJC_$_CLASS_METHODS_BCSBusinessCallerItem(ProtoConversion|BCSProtoConversion|Caching)
+ __OBJC_$_CLASS_METHODS_BCSCallerIdParquetMessage
+ __OBJC_$_CLASS_METHODS_BCSExecutionTimer
+ __OBJC_$_CLASS_METHODS_BCSPathProvider
+ __OBJC_$_CLASS_PROP_LIST_BCSBlastDoorHelper
+ __OBJC_$_INSTANCE_METHODS_BCSBlastDoorHelper
+ __OBJC_$_INSTANCE_METHODS_BCSBlastDoorPersistentStore
+ __OBJC_$_INSTANCE_METHODS_BCSBusinessCallerItem(ProtoConversion|BCSProtoConversion|Caching)
+ __OBJC_$_INSTANCE_METHODS_BCSCallerIdParquetMessage
+ __OBJC_$_INSTANCE_METHODS_BCSCallerIdParquetWrapper
+ __OBJC_$_INSTANCE_METHODS_BCSCallerIdResolver
+ __OBJC_$_INSTANCE_METHODS_BCSExecutionTimer
+ __OBJC_$_INSTANCE_METHODS_BCSPathProvider
+ __OBJC_$_INSTANCE_VARIABLES_BCSBlastDoorHelper
+ __OBJC_$_INSTANCE_VARIABLES_BCSBlastDoorPersistentStore
+ __OBJC_$_INSTANCE_VARIABLES_BCSCallerIdParquetMessage
+ __OBJC_$_INSTANCE_VARIABLES_BCSCallerIdParquetWrapper
+ __OBJC_$_INSTANCE_VARIABLES_BCSCallerIdResolver
+ __OBJC_$_INSTANCE_VARIABLES_BCSExecutionTimer
+ __OBJC_$_INSTANCE_VARIABLES_BCSPathProvider
+ __OBJC_$_PROP_LIST_BCSBlastDoorHelper
+ __OBJC_$_PROP_LIST_BCSBlastDoorPersistentStore
+ __OBJC_$_PROP_LIST_BCSCallerIdParquetMessage
+ __OBJC_$_PROP_LIST_BCSCallerIdParquetWrapper
+ __OBJC_$_PROP_LIST_BCSCallerIdResolver
+ __OBJC_$_PROP_LIST_BCSExecutionTimer
+ __OBJC_$_PROP_LIST_BCSPIRServerEnvironmentProtocol
+ __OBJC_$_PROP_LIST_BCSPathProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSBlastDoorImageCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSPIRServerEnvironmentProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSXPCDaemonBusinessCallerIDDaemonInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSXPCDaemonBusinessLinkDaemonInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSXPCDaemonChatSuggestDaemonInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCSBlastDoorImageCache
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCSPIRServerEnvironmentProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCSXPCDaemonBusinessCallerIDDaemonInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCSXPCDaemonBusinessLinkDaemonInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BCSXPCDaemonChatSuggestDaemonInterface
+ __OBJC_$_PROTOCOL_REFS_BCSBlastDoorImageCache
+ __OBJC_$_PROTOCOL_REFS_BCSXPCDaemonProtocol
+ __OBJC_CLASS_PROTOCOLS_$_BCSBlastDoorPersistentStore
+ __OBJC_CLASS_PROTOCOLS_$_BCSCallerIdParquetMessage
+ __OBJC_CLASS_PROTOCOLS_$_BCSCallerIdParquetWrapper
+ __OBJC_CLASS_PROTOCOLS_$_BCSCallerIdResolver
+ __OBJC_CLASS_RO_$_BCSBlastDoorHelper
+ __OBJC_CLASS_RO_$_BCSBlastDoorPersistentStore
+ __OBJC_CLASS_RO_$_BCSCallerIdParquetMessage
+ __OBJC_CLASS_RO_$_BCSCallerIdParquetWrapper
+ __OBJC_CLASS_RO_$_BCSCallerIdResolver
+ __OBJC_CLASS_RO_$_BCSExecutionTimer
+ __OBJC_LABEL_PROTOCOL_$_BCSBlastDoorImageCache
+ __OBJC_LABEL_PROTOCOL_$_BCSPIRServerEnvironmentProtocol
+ __OBJC_LABEL_PROTOCOL_$_BCSXPCDaemonBusinessCallerIDDaemonInterface
+ __OBJC_LABEL_PROTOCOL_$_BCSXPCDaemonBusinessLinkDaemonInterface
+ __OBJC_LABEL_PROTOCOL_$_BCSXPCDaemonChatSuggestDaemonInterface
+ __OBJC_METACLASS_RO_$_BCSBlastDoorHelper
+ __OBJC_METACLASS_RO_$_BCSBlastDoorPersistentStore
+ __OBJC_METACLASS_RO_$_BCSCallerIdParquetMessage
+ __OBJC_METACLASS_RO_$_BCSCallerIdParquetWrapper
+ __OBJC_METACLASS_RO_$_BCSCallerIdResolver
+ __OBJC_METACLASS_RO_$_BCSExecutionTimer
+ __OBJC_PROTOCOL_$_BCSBlastDoorImageCache
+ __OBJC_PROTOCOL_$_BCSPIRServerEnvironmentProtocol
+ __OBJC_PROTOCOL_$_BCSXPCDaemonBusinessCallerIDDaemonInterface
+ __OBJC_PROTOCOL_$_BCSXPCDaemonBusinessLinkDaemonInterface
+ __OBJC_PROTOCOL_$_BCSXPCDaemonChatSuggestDaemonInterface
+ ___100-[BCSRemoteFetchCloudKit fetchItemsWithBucketStartIndex:endIndex:type:forClientBundleID:completion:]_block_invoke.102
+ ___101-[BCSBusinessQueryController fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:completion:]_block_invoke_2
+ ___101-[BCSBusinessQueryController fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:completion:]_block_invoke_3
+ ___109-[BCSBusinessQueryController lookupBloomFiltersForURL:chopURL:forClientBundleID:registeredMetric:completion:]_block_invoke.32
+ ___113-[BCSBusinessQueryService fetchBusinessCallerMetadataForPhoneNumber:metadataCallback:logoURLCallback:completion:]_block_invoke
+ ___113-[BCSBusinessQueryService fetchBusinessCallerMetadataForPhoneNumber:metadataCallback:logoURLCallback:completion:]_block_invoke_2
+ ___113-[BCSBusinessQueryService fetchBusinessCallerMetadataForPhoneNumber:metadataCallback:logoURLCallback:completion:]_block_invoke_3
+ ___134-[BCSBusinessQueryController fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:metadataCallback:logoURLCallback:completion:]_block_invoke
+ ___23-[BCSPathProvider init]_block_invoke
+ ___33+[BCSPathProvider sharedInstance]_block_invoke
+ ___37-[BCSBlastDoorHelper warmUpBlastDoor]_block_invoke
+ ___42-[BCSBusinessQueryController startUpTasks]_block_invoke
+ ___60-[BCSCallerIdResolver fetchDataMatching:timeout:completion:]_block_invoke
+ ___60-[BCSCallerIdResolver fetchDataMatching:timeout:completion:]_block_invoke_2
+ ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.145
+ ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.146
+ ___71-[BCSRemoteFetchCloudKit fetchShardMatching:clientBundleID:completion:]_block_invoke.75
+ ___76-[BCSCallerIdResolver itemMatching:config:clientBundleID:metric:completion:]_block_invoke
+ ___86-[BCSBusinessQueryController fetchLinkItemModelWithHash:forClientBundleID:completion:]_block_invoke.33
+ ___88-[BCSRemoteFetchCloudKit fetchConfigItemWithType:clientBundleID:xpcActivity:completion:]_block_invoke.58
+ ___91-[BCSRemoteFetchCloudKit fetchMegashardItemWithType:clientBundleID:xpcActivity:completion:]_block_invoke.89
+ ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.22
+ ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.24
+ ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.25
+ ___94-[BCSBusinessQueryController isBusinessRegisteredForURL:chopURL:forClientBundleID:completion:]_block_invoke.28
+ ___94-[BCSBusinessQueryController isBusinessRegisteredForURL:chopURL:forClientBundleID:completion:]_block_invoke.29
+ ___95-[BCSBusinessQueryController _itemWithIdentifier:forClientBundleID:skipFilterCheck:completion:]_block_invoke.102
+ ___95-[BCSBusinessQueryController _itemWithIdentifier:forClientBundleID:skipFilterCheck:completion:]_block_invoke.103
+ ___block_descriptor_32_e15_"NSString"8?0l
+ ___block_descriptor_40_e8_32bs_e15_v16?0"NSURL"8ls32l8
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32bs_e31_v16?0"BCSBusinessCallerItem"8ls32l8
+ ___block_descriptor_40_e8_32r_e15_v16?0"NSURL"8lr32l8
+ ___block_descriptor_40_e8_32r_e31_v16?0"BCSBusinessCallerItem"8lr32l8
+ ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40bs48r_e28_v24?0"NSData"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72bs80bs_e29_v24?0"BCSItem"8"NSError"16ls32l8s64l8s40l8s72l8s48l8s56l8s80l8
+ ___block_literal_global.6
+ _compression_decode_buffer
+ _dispatch_after
+ _kBCSDefaultBusinessCallerCKContainerID
+ _kBCSDefaultBusinessCallerCKContainerIDCI
+ _kBCSDefaultBusinessCallerCKContainerIDQA
+ _kBCSDefaultBusinessCallerPIRUseCase
+ _kBCSDefaultBusinessCallerPIRUseCaseQA
+ _kBCSDefaultBusinessLinkCKContainerID
+ _kBCSDefaultBusinessLinkCKContainerIDCI
+ _kBCSDefaultBusinessLinkCKLinkContainerIDQA
+ _kBCSDefaultChatSuggestCKContainerID
+ _kBCSDefaultChatSuggestCKContainerIDCI
+ _kBCSDefaultChatSuggestCKContainerIDQA
+ _kBCSDefaultsBusinessCallerPIRUseCase
+ _mach_absolute_time
+ _mach_timebase_info
+ _objc_msgSend$_setupStorageWithBaseFileURL:applyFileProtectionType:verificationToken:
+ _objc_msgSend$_setupStorageWithSearchPathDirectory:applyFileProtectionType:verificationToken:
+ _objc_msgSend$addIntent:
+ _objc_msgSend$addName:
+ _objc_msgSend$blastDoorTimingMeasurementForItemIdentifier:
+ _objc_msgSend$businessCallerFetchTimingMeasurementForItemIdentifier:
+ _objc_msgSend$cacheURL
+ _objc_msgSend$cachesURL
+ _objc_msgSend$clearIntents
+ _objc_msgSend$clearNames
+ _objc_msgSend$decompressData:
+ _objc_msgSend$defaultHelper
+ _objc_msgSend$documentsURL
+ _objc_msgSend$environment
+ _objc_msgSend$fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:metadataCallback:logoURLCallback:completion:
+ _objc_msgSend$fetchDataMatching:timeout:completion:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fileManager
+ _objc_msgSend$fileURLForImageWithName:error:
+ _objc_msgSend$generateImagePreviewForFileURL:maxPixelDimension:scale:error:
+ _objc_msgSend$getResourceValue:forKey:error:
+ _objc_msgSend$hasMessage
+ _objc_msgSend$image
+ _objc_msgSend$initWithBlastDoorInstanceType:
+ _objc_msgSend$initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:
+ _objc_msgSend$initWithClientConfig:
+ _objc_msgSend$initWithFileManager:temporaryDirectoryBuilder:
+ _objc_msgSend$initWithParquetMessage:
+ _objc_msgSend$initWithPersistentStore:
+ _objc_msgSend$initWithPhoneNumber:name:department:logoURL:logo:logoFormat:verified:
+ _objc_msgSend$initWithPhoneNumber:phoneHash:localizedNames:localizedDepartments:logoURL:logo:logoFormat:verified:
+ _objc_msgSend$initWithUseCase:
+ _objc_msgSend$intentAtIndex:
+ _objc_msgSend$intents
+ _objc_msgSend$intentsCount
+ _objc_msgSend$itemCache
+ _objc_msgSend$itemCacheSkipper
+ _objc_msgSend$languageCode
+ _objc_msgSend$locale
+ _objc_msgSend$logo
+ _objc_msgSend$logoFormat
+ _objc_msgSend$message
+ _objc_msgSend$metricFactory
+ _objc_msgSend$milliseconds
+ _objc_msgSend$nameAtIndex:
+ _objc_msgSend$names
+ _objc_msgSend$namesCount
+ _objc_msgSend$nanoseconds
+ _objc_msgSend$now
+ _objc_msgSend$pathExtension
+ _objc_msgSend$pirClient
+ _objc_msgSend$pirQueue
+ _objc_msgSend$pirUseCase
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$requestDataByStringKeyword:completionHandler:
+ _objc_msgSend$safeImageURLFromImage:imageFormat:error:
+ _objc_msgSend$safeImageURLFromImage:imageFormat:maxPixelDimension:scale:error:
+ _objc_msgSend$safeImageURLFromImageURL:maxPixelDimension:scale:error:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setIsDefault:
+ _objc_msgSend$setIsVerified:
+ _objc_msgSend$setLogo:
+ _objc_msgSend$setLogoFormat:
+ _objc_msgSend$setLogoURL:
+ _objc_msgSend$setPhoneHash:
+ _objc_msgSend$set_sourceApplicationSecondaryIdentifier:
+ _objc_msgSend$startTime
+ _objc_msgSend$store
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$tempURL
+ _objc_msgSend$temporaryDirectoryBuilder
+ _objc_msgSend$timeExecutionOfBlock:
+ _objc_msgSend$warmUpBlastDoor
+ _objc_msgSend$writeToURL:atomically:
+ _objc_msgSend$writeToURL:usingEncoding:error:
+ _objc_retain_x6
+ _warmUpBlastDoor.warmUpGIFBytes
- +[BCSPathProvider _createBundleBasedDirectoryIfNecessary:]
- +[BCSPathProvider documentsPath]
- +[BCSPathProvider tempPath]
- -[BCSBusinessCallerItem initWithPhoneNumber:name:department:logoURL:]
- -[BCSBusinessCallerItem initWithPhoneNumber:phoneHash:name:department:logoURL:]
- -[BCSBusinessCallerItem(BCSProtoConversion) initWithCallerIdMessage:bucketID:]
- -[BCSBusinessQueryController initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:queryChopper:patternController:metricFactory:housekeeper:]
- GCC_except_table53
- _BCSStoreStringFromStatement
- _CKContainerEnvironmentFromString
- __OBJC_$_CLASS_METHODS_BCSBusinessCallerItem(BCSProtoConversion|Caching)
- __OBJC_$_INSTANCE_METHODS_BCSBusinessCallerItem(BCSProtoConversion|Caching)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_BCSXPCDaemonProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_BCSXPCDaemonProtocol
- ___100-[BCSRemoteFetchCloudKit fetchItemsWithBucketStartIndex:endIndex:type:forClientBundleID:completion:]_block_invoke.99
- ___109-[BCSBusinessQueryController lookupBloomFiltersForURL:chopURL:forClientBundleID:registeredMetric:completion:]_block_invoke.30
- ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.137
- ___63-[BCSBusinessQueryController prefetchMegashardsWithCompletion:]_block_invoke.138
- ___71-[BCSRemoteFetchCloudKit fetchShardMatching:clientBundleID:completion:]_block_invoke.72
- ___86-[BCSBusinessQueryController fetchLinkItemModelWithHash:forClientBundleID:completion:]_block_invoke.31
- ___88-[BCSRemoteFetchCloudKit fetchConfigItemWithType:clientBundleID:xpcActivity:completion:]_block_invoke.55
- ___91-[BCSRemoteFetchCloudKit fetchMegashardItemWithType:clientBundleID:xpcActivity:completion:]_block_invoke.86
- ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.19
- ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.21
- ___93-[BCSBusinessQueryController fetchLinkItemModelWithURL:chopURL:forClientBundleID:completion:]_block_invoke.23
- ___94-[BCSBusinessQueryController isBusinessRegisteredForURL:chopURL:forClientBundleID:completion:]_block_invoke.26
- ___94-[BCSBusinessQueryController isBusinessRegisteredForURL:chopURL:forClientBundleID:completion:]_block_invoke.27
- ___95-[BCSBusinessQueryController _itemWithIdentifier:forClientBundleID:skipFilterCheck:completion:]_block_invoke.100
- ___95-[BCSBusinessQueryController _itemWithIdentifier:forClientBundleID:skipFilterCheck:completion:]_block_invoke.99
- ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"BCSItem"8"NSError"16ls32l8s48l8s40l8
- _documentsPath.verifiedFileProtectionLevel
- _objc_msgSend$hasLogoUrl
- _objc_msgSend$initWithCallerIdMessage:bucketID:
- _objc_msgSend$initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:queryChopper:patternController:metricFactory:housekeeper:
- _objc_msgSend$initWithPhoneNumber:name:department:logoURL:
- _objc_msgSend$initWithPhoneNumber:phoneHash:name:department:logoURL:
- _objc_msgSend$intent
- _objc_msgSend$logoUrl
CStrings:
+ "\x06"
+ "\x1f\f"
+ "%@-safe.%@"
+ "%@.%@"
+ "%s - Error fetching from PIR for - type: %@, error: %@"
+ "%s - Failed to unzip"
+ "%s - Invalid message from PIR for - type: %@, data: %@"
+ "%s - Item fetched from PIR for - type: %@, item: %@"
+ "-[BCSBlastDoorHelper safeImageURLFromImage:imageFormat:error:]"
+ "-[BCSBlastDoorHelper safeImageURLFromImage:imageFormat:maxPixelDimension:scale:error:]"
+ "-[BCSBlastDoorHelper safeImageURLFromImageURL:error:]"
+ "-[BCSBlastDoorHelper safeImageURLFromImageURL:maxPixelDimension:scale:error:]"
+ "-[BCSBusinessQueryController fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:metadataCallback:logoURLCallback:completion:]"
+ "-[BCSBusinessQueryController startUpTasks]"
+ "-[BCSBusinessQueryService fetchBusinessCallerMetadataForPhoneNumber:metadataCallback:logoURLCallback:completion:]"
+ "-[BCSCallerIdResolver cachedItemMatching:]"
+ "-[BCSCallerIdResolver decompressData:]"
+ "-[BCSCallerIdResolver itemMatching:config:clientBundleID:metric:completion:]"
+ "-[BCSCallerIdResolver itemMatching:config:clientBundleID:metric:completion:]_block_invoke"
+ "@\"<BCSBlastDoorImageCache>\""
+ "@\"<BCSCloudKitContainerProtocol>\""
+ "@\"<BCSFileManagementProviding>\""
+ "@\"<BCSICloudServerEnvironmentProtocol><BCSPIRServerEnvironmentProtocol>\""
+ "@\"<BCSPIRServerEnvironmentProtocol>\""
+ "@\"BCSBlastDoorHelper\""
+ "@\"BCSCallerIdParquetMessage\""
+ "@\"CMLKeywordPIRClient\""
+ "@\"IMMessagesBlastDoorInterface\""
+ "@\"NSURL\"32@0:8@\"NSString\"16^@24"
+ "@224@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216"
+ "@32@0:8@16@?24"
+ "@40@0:8@16@24^B32"
+ "@40@0:8@16f24f28^@32"
+ "@40@0:8Q16@24^B32"
+ "@48@0:8@16@24f32f36^@40"
+ "@68@0:8@16@24@32@40@48@56B64"
+ "@76@0:8@16q24@32@40@48@56@64B72"
+ "Asked to delete image but unable to construct file URL"
+ "BCSAppErrorDomain"
+ "BCSBlastDoorHelper"
+ "BCSBlastDoorImageCache"
+ "BCSBlastDoorPersistentStore"
+ "BCSBusinessCallerPIRUseCase"
+ "BCSCallerIdParquetMessage"
+ "BCSCallerIdParquetWrapper"
+ "BCSCallerIdResolver"
+ "BCSExecutionTimer"
+ "BCSNetworkErrorDomain"
+ "BCSPIRServerEnvironmentProtocol"
+ "BCSXPCDaemonBusinessCallerIDDaemonInterface"
+ "BCSXPCDaemonBusinessLinkDaemonInterface"
+ "BCSXPCDaemonChatSuggestDaemonInterface"
+ "BlastDoor already warm"
+ "BlastDoor init took  %llu ms"
+ "BlastDoor processing took  %llu ms"
+ "BrandLogos"
+ "BusinessCaller_BlastDoorProcessing"
+ "BusinessCaller_CloudKitFetchBucket"
+ "BusinessCaller_CloudKitFetchBucketAndDecode"
+ "BusinessCaller_CloudKitFetchConfig"
+ "BusinessCaller_CloudKitFetchConfigAndDecode"
+ "BusinessCaller_CloudKitFetchMegashard"
+ "BusinessCaller_CloudKitFetchMegashardAndDecode"
+ "BusinessCaller_CloudKitFetchShard"
+ "BusinessCaller_CloudKitFetchShardAndDecode"
+ "BusinessCaller_ConfigResolution"
+ "BusinessCaller_ItemFetch"
+ "BusinessCaller_ItemFetchChop"
+ "BusinessCaller_ItemHashFetch"
+ "BusinessCaller_ItemResolution"
+ "BusinessCaller_ShardCacheHit"
+ "BusinessCaller_ShardCacheMiss"
+ "BusinessCaller_ShardResolution"
+ "BusinessDomain_ShardCacheHit"
+ "BusinessDomain_ShardCacheMiss"
+ "BusinessDomain_ShardResolution"
+ "BusinessLink_BlastDoorProcessing"
+ "BusinessLink_CloudKitFetchBucket"
+ "BusinessLink_CloudKitFetchBucketAndDecode"
+ "BusinessLink_CloudKitFetchConfig"
+ "BusinessLink_CloudKitFetchConfigAndDecode"
+ "BusinessLink_CloudKitFetchMegashard"
+ "BusinessLink_CloudKitFetchMegashardAndDecode"
+ "BusinessLink_CloudKitFetchShard"
+ "BusinessLink_CloudKitFetchShardAndDecode"
+ "BusinessLink_ConfigCacheHit"
+ "BusinessLink_ConfigCacheMiss"
+ "BusinessLink_ConfigResolution"
+ "BusinessLink_ItemCacheHit"
+ "BusinessLink_ItemCacheMiss"
+ "BusinessLink_ItemFetch"
+ "BusinessLink_ItemFetchChop"
+ "BusinessLink_ItemHashFetch"
+ "BusinessLink_ItemResolution"
+ "BusinessLink_ShardCacheHit"
+ "BusinessLink_ShardCacheMiss"
+ "BusinessLink_ShardResolution"
+ "CREATE TABLE IF NOT EXISTS business_caller_items    (phone_hash INTEGER PRIMARY KEY,     phone TEXT,     message BLOB,     expiration_date DOUBLE)"
+ "ChatSuggest_BlastDoorProcessing"
+ "ChatSuggest_CloudKitFetchBucket"
+ "ChatSuggest_CloudKitFetchBucketAndDecode"
+ "ChatSuggest_CloudKitFetchConfig"
+ "ChatSuggest_CloudKitFetchConfigAndDecode"
+ "ChatSuggest_CloudKitFetchMegashard"
+ "ChatSuggest_CloudKitFetchMegashardAndDecode"
+ "ChatSuggest_CloudKitFetchShard"
+ "ChatSuggest_CloudKitFetchShardAndDecode"
+ "ChatSuggest_ConfigCacheHit"
+ "ChatSuggest_ConfigCacheMiss"
+ "ChatSuggest_ConfigResolution"
+ "ChatSuggest_ItemCacheHit"
+ "ChatSuggest_ItemCacheMiss"
+ "ChatSuggest_ItemFetch"
+ "ChatSuggest_ItemFetchChop"
+ "ChatSuggest_ItemHashFetch"
+ "ChatSuggest_ItemResolution"
+ "ChatSuggest_ShardCacheHit"
+ "ChatSuggest_ShardCacheMiss"
+ "ChatSuggest_ShardResolution"
+ "Creating BlastDoor image cache at: %@"
+ "Deleting expired images"
+ "Deleting image named: %@"
+ "Error creating BlastDoor cache store: %@"
+ "Error creating BlastDoor cache store: unexpected state (found file instead of directory)"
+ "Error creating temp file for image copy: %@"
+ "Error creating temp file for warm up image: %@"
+ "Error finding default cache directory for BlastDoor image store: %@"
+ "Error generating BlastDoor preview: %@"
+ "Error getting safe image from BlastDoor: %@"
+ "Error removing unexpected file (instead of directory): %@"
+ "Error writing BlastDoor image copy: %@"
+ "Error writing temp file for warm up image"
+ "Failed to create copy of image data"
+ "Failed to decode PIR record"
+ "Failed to determine modification date for file: %@"
+ "Failed to set the file protection level to class C on the caches directory, error: %@"
+ "Failed to unzip the PIR record"
+ "INSERT OR REPLACE INTO business_caller_items    (phone_hash, phone, message, expiration_date)    VALUES (?,?,?,?)"
+ "Invalid type"
+ "Message"
+ "ProtoConversion"
+ "Q24@0:8@?16"
+ "Removing expired file: %@"
+ "SELECT phone_hash, phone, message, expiration_date    FROM business_caller_items    WHERE phone_hash = %lld"
+ "Successfully set caches directory file protection level to class C"
+ "T@\"<BCSBlastDoorImageCache>\",&,N,V_store"
+ "T@\"<BCSFileManagementProviding>\",&,N,V_fileManager"
+ "T@\"<BCSICloudServerEnvironmentProtocol><BCSPIRServerEnvironmentProtocol>\",R,&,N,V_environment"
+ "T@\"<BCSItemCacheSkipping>\",R,&,N,V_itemCacheSkipper"
+ "T@\"<BCSItemCaching>\",R,&,N,V_itemCache"
+ "T@\"<BCSMetricFactoryProtocol>\",&,N,V_metricFactory"
+ "T@\"<BCSPIRServerEnvironmentProtocol>\",R,&,N,V_environment"
+ "T@\"BCSBlastDoorHelper\",R"
+ "T@\"BCSCallerIdParquetMessage\",C,N,V_message"
+ "T@\"CMLKeywordPIRClient\",&,N,V_pirClient"
+ "T@\"NSData\",&,N,V_logo"
+ "T@\"NSData\",&,N,V_message"
+ "T@\"NSData\",R,N"
+ "T@\"NSMutableArray\",&,N,V_intents"
+ "T@\"NSMutableArray\",&,N,V_names"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_pirQueue"
+ "T@\"NSString\",&,N,V_logoFormat"
+ "T@\"NSString\",&,N,V_phoneNumber"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSURL\",C,N,V_cacheURL"
+ "T@\"NSURL\",C,N,V_logoURL"
+ "T@\"NSURL\",R"
+ "T@?,C,N,V_temporaryDirectoryBuilder"
+ "TB,N,V_cachesDirectoryFileProtectionLevelVerified"
+ "TB,N,V_documentsDirectoryFileProtectionLevelVerified"
+ "TQ,N,V_startTime"
+ "Timeout waiting for response from PIR"
+ "Unable to determine directory from NSFileManager: %@"
+ "Warmed up BlastDoor interface in %llu ms"
+ "Warming up BlastDoor interface"
+ "_BlastDoorProcessing"
+ "_CloudKitFetchBucket"
+ "_CloudKitFetchBucketAndDecode"
+ "_CloudKitFetchConfig"
+ "_CloudKitFetchConfigAndDecode"
+ "_CloudKitFetchMegashard"
+ "_CloudKitFetchMegashardAndDecode"
+ "_CloudKitFetchShard"
+ "_CloudKitFetchShardAndDecode"
+ "_ConfigCacheHit"
+ "_ConfigCacheMiss"
+ "_ConfigResolution"
+ "_ItemCacheHit"
+ "_ItemCacheMiss"
+ "_ItemFetch"
+ "_ItemFetchChop"
+ "_ItemHashFetch"
+ "_ItemResolution"
+ "_ShardCacheHit"
+ "_ShardCacheMiss"
+ "_ShardResolution"
+ "_blastDoorHelper"
+ "_blastDoorWarmedUp"
+ "_blastdoor"
+ "_cacheURL"
+ "_cachesDirectoryFileProtectionLevelVerified"
+ "_documentsDirectoryFileProtectionLevelVerified"
+ "_fileManager"
+ "_intents"
+ "_logo"
+ "_logoFormat"
+ "_names"
+ "_pirClient"
+ "_pirQueue"
+ "_setupStorageWithBaseFileURL:applyFileProtectionType:verificationToken:"
+ "_setupStorageWithSearchPathDirectory:applyFileProtectionType:verificationToken:"
+ "_startTime"
+ "_store"
+ "_temporaryDirectoryBuilder"
+ "addIntent:"
+ "addName:"
+ "blastDoorTimingMeasurementForItemIdentifier:"
+ "brandLogoCacheURL"
+ "businessCallerFetchTimingMeasurementForItemIdentifier:"
+ "cacheURL"
+ "cachesDirectoryFileProtectionLevelVerified"
+ "cachesURL"
+ "callerId"
+ "callerIdStaging"
+ "clearIntents"
+ "clearNames"
+ "com.apple.CommCenter.BrandedCalling"
+ "com.apple.businesschat.calleridresolver.pir"
+ "com.apple.businessservicesd.brandLogo"
+ "com.apple.businessservicesd/temp"
+ "com.apple.icloud-bcassets-internal"
+ "com.apple.icloud-bcassets-qa"
+ "com.apple.icloud-businesslinks-internal"
+ "com.apple.icloud-businesslinks-qa"
+ "decompressData:"
+ "defaultHelper"
+ "deleteExpiredImages"
+ "deleteImageWithName:"
+ "documentsDirectoryFileProtectionLevelVerified"
+ "documentsURL"
+ "environment"
+ "fetchBusinessCallerMetadataForPhoneNumber:forClientBundleID:metadataCallback:logoURLCallback:completion:"
+ "fetchBusinessCallerMetadataForPhoneNumber:metadataCallback:logoURLCallback:completion:"
+ "fetchDataMatching:timeout:completion:"
+ "fileExistsAtPath:isDirectory:"
+ "fileManager"
+ "fileURLForImageWithName:error:"
+ "generateImagePreviewForFileURL:maxPixelDimension:scale:error:"
+ "getResourceValue:forKey:error:"
+ "hasLogo"
+ "hasLogoFormat"
+ "hasPhoneNumber"
+ "heic"
+ "image"
+ "initWithBlastDoorInstanceType:"
+ "initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:queryChopper:patternController:metricFactory:blastDoorHelper:housekeeper:"
+ "initWithClientConfig:"
+ "initWithFileManager:temporaryDirectoryBuilder:"
+ "initWithParquetMessage:"
+ "initWithPersistentStore:"
+ "initWithPhoneNumber:name:department:logoURL:logo:logoFormat:verified:"
+ "initWithPhoneNumber:phoneHash:localizedNames:localizedDepartments:logoURL:logo:logoFormat:verified:"
+ "initWithUseCase:"
+ "intentAtIndex:"
+ "intentType"
+ "intents"
+ "intentsCount"
+ "itemCache"
+ "itemCacheSkipper"
+ "languageCode"
+ "localizedDepartments"
+ "localizedNames"
+ "logoFormat"
+ "logo_format"
+ "milliseconds"
+ "nameAtIndex:"
+ "nameType"
+ "names"
+ "namesCount"
+ "nanoseconds"
+ "now"
+ "pathExtension"
+ "phone_number"
+ "pirClient"
+ "pirQueue"
+ "pirUseCase"
+ "removeItemAtURL:error:"
+ "requestDataByStringKeyword:completionHandler:"
+ "safeImageURLFromImage:imageFormat:error:"
+ "safeImageURLFromImage:imageFormat:maxPixelDimension:scale:error:"
+ "safeImageURLFromImageURL processing took  %llu ms (total)"
+ "safeImageURLFromImageURL:error:"
+ "safeImageURLFromImageURL:maxPixelDimension:scale:error:"
+ "seconds"
+ "setAttributes:ofItemAtPath:error:"
+ "setCacheURL:"
+ "setCachesDirectoryFileProtectionLevelVerified:"
+ "setDocumentsDirectoryFileProtectionLevelVerified:"
+ "setFileManager:"
+ "setIntents:"
+ "setLogo:"
+ "setLogoFormat:"
+ "setLogoURL:"
+ "setMetricFactory:"
+ "setNames:"
+ "setPirClient:"
+ "setPirQueue:"
+ "setStartTime:"
+ "setStore:"
+ "setTemporaryDirectoryBuilder:"
+ "set_sourceApplicationSecondaryIdentifier:"
+ "startTime"
+ "store"
+ "stringByDeletingPathExtension"
+ "subdataWithRange:"
+ "tempURL"
+ "temporaryDirectoryBuilder"
+ "timeExecutionOfBlock:"
+ "updateImageWithName:error:"
+ "v16@?0@\"BCSBusinessCallerItem\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSURL\"8"
+ "v40@0:8@16q24@?32"
+ "v48@0:8@16@?24@?32@?40"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"BCSBusinessCallerItem\">32@?<v@?@\"NSURL\">40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@?32@?40@?48"
+ "warmUp.gif"
+ "warmUpBlastDoor"
+ "writeToURL:atomically:"
+ "writeToURL:usingEncoding:error:"
- "\x0f\v"
- " - CloudKit Fetch Bucket"
- " - CloudKit Fetch Bucket + Decode"
- " - CloudKit Fetch Config"
- " - CloudKit Fetch Config + Decode"
- " - CloudKit Fetch Megashard"
- " - CloudKit Fetch Megashard + Decode"
- " - CloudKit Fetch Shard"
- " - CloudKit Fetch Shard + Decode"
- " - ConfigCacheHit"
- " - ConfigCacheMiss"
- " - ConfigResolution"
- " - ItemCacheHit"
- " - ItemCacheMiss"
- " - ItemFetch"
- " - ItemFetchChop"
- " - ItemHashFetch"
- " - ItemResolution"
- " - ShardCacheHit"
- " - ShardCacheMiss"
- " - ShardResolution"
- "@\"<BCSICloudServerEnvironmentProtocol>\""
- "@\"CKContainer\""
- "@216@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208"
- "@56@0:8@16q24@32@40@48"
- "BCSBusinessCallerItem: BCSBusinessCallerItem object didn't initialize correctly"
- "BusinessCaller - CloudKit Fetch Bucket"
- "BusinessCaller - CloudKit Fetch Bucket + Decode"
- "BusinessCaller - CloudKit Fetch Config"
- "BusinessCaller - CloudKit Fetch Config + Decode"
- "BusinessCaller - CloudKit Fetch Megashard"
- "BusinessCaller - CloudKit Fetch Megashard + Decode"
- "BusinessCaller - CloudKit Fetch Shard"
- "BusinessCaller - CloudKit Fetch Shard + Decode"
- "BusinessCaller - ConfigResolution"
- "BusinessCaller - ItemFetch"
- "BusinessCaller - ItemFetchChop"
- "BusinessCaller - ItemHashFetch"
- "BusinessCaller - ItemResolution"
- "BusinessCaller - ShardCacheHit"
- "BusinessCaller - ShardCacheMiss"
- "BusinessCaller - ShardResolution"
- "BusinessDomain - ShardCacheHit"
- "BusinessDomain - ShardCacheMiss"
- "BusinessDomain - ShardResolution"
- "BusinessLink - CloudKit Fetch Bucket"
- "BusinessLink - CloudKit Fetch Bucket + Decode"
- "BusinessLink - CloudKit Fetch Config"
- "BusinessLink - CloudKit Fetch Config + Decode"
- "BusinessLink - CloudKit Fetch Megashard"
- "BusinessLink - CloudKit Fetch Megashard + Decode"
- "BusinessLink - CloudKit Fetch Shard"
- "BusinessLink - CloudKit Fetch Shard + Decode"
- "BusinessLink - ConfigCacheHit"
- "BusinessLink - ConfigCacheMiss"
- "BusinessLink - ConfigResolution"
- "BusinessLink - ItemCacheHit"
- "BusinessLink - ItemCacheMiss"
- "BusinessLink - ItemFetch"
- "BusinessLink - ItemFetchChop"
- "BusinessLink - ItemHashFetch"
- "BusinessLink - ItemResolution"
- "BusinessLink - ShardCacheHit"
- "BusinessLink - ShardCacheMiss"
- "BusinessLink - ShardResolution"
- "CREATE TABLE IF NOT EXISTS business_caller_items    (phone_hash INTEGER PRIMARY KEY,     phone TEXT,     business_name TEXT,     department TEXT,     logo_url TEXT,     expiration_date DOUBLE)"
- "ChatSuggest - CloudKit Fetch Bucket"
- "ChatSuggest - CloudKit Fetch Bucket + Decode"
- "ChatSuggest - CloudKit Fetch Config"
- "ChatSuggest - CloudKit Fetch Config + Decode"
- "ChatSuggest - CloudKit Fetch Megashard"
- "ChatSuggest - CloudKit Fetch Megashard + Decode"
- "ChatSuggest - CloudKit Fetch Shard"
- "ChatSuggest - CloudKit Fetch Shard + Decode"
- "ChatSuggest - ConfigCacheHit"
- "ChatSuggest - ConfigCacheMiss"
- "ChatSuggest - ConfigResolution"
- "ChatSuggest - ItemCacheHit"
- "ChatSuggest - ItemCacheMiss"
- "ChatSuggest - ItemFetch"
- "ChatSuggest - ItemFetchChop"
- "ChatSuggest - ItemHashFetch"
- "ChatSuggest - ItemResolution"
- "ChatSuggest - ShardCacheHit"
- "ChatSuggest - ShardCacheMiss"
- "ChatSuggest - ShardResolution"
- "Department"
- "Failed to set the file protection level to class C on the documents directory"
- "INSERT OR REPLACE INTO business_caller_items    (phone_hash, phone, business_name, department, logo_url, expiration_date)    VALUES (?,?,?,?,?,?)"
- "Identifier"
- "Name"
- "No custom cloudKit environment set in user defaults, using %{public}@"
- "PhoneNumber"
- "SELECT phone_hash, phone, business_name, department, logo_url, expiration_date    FROM business_caller_items    WHERE phone_hash = %lld"
- "Successfully set documents directory file protection level to class C"
- "T@\"NSString\",R,C,N,V_department"
- "T@\"NSURL\",R,C,N,V_logoURL"
- "Trying to use %{public}@ for the cloudKit environment name"
- "Unable to determine caches directory: %@"
- "_department"
- "initWithCallerIdMessage:bucketID:"
- "initWithChatSuggestMegashardFetchTrigger:businessLinkMegashardFetchTrigger:businessCallerMegashardFetchTrigger:entitlementVerifier:identityService:chatSuggestController:iconController:cacheClearer:shardCache:configCache:configCacheSkip:shardCacheSkip:chatSuggestConfigResolver:linkConfigResolver:businessCallerConfigResolver:chatSuggestShardResolver:linkShardResolver:businessCallerShardResolver:chatSuggestItemResolver:linkItemResolver:businessCallerItemResolver:queryChopper:patternController:metricFactory:housekeeper:"
- "initWithPhoneNumber:name:department:logoURL:"
- "initWithPhoneNumber:phoneHash:name:department:logoURL:"

```
