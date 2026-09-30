## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices`

```diff

-96.1.1.0.0
-  __TEXT.__text: 0x23dfc
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x2564
+96.5.0.0.0
+  __TEXT.__text: 0x27828
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x279c
   __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x6c8
-  __TEXT.__cstring: 0x1232
-  __TEXT.__oslogstring: 0x2e56
-  __TEXT.__unwind_info: 0xa78
-  __TEXT.__objc_classname: 0x4ba
-  __TEXT.__objc_methname: 0x4f29
-  __TEXT.__objc_methtype: 0x133c
-  __TEXT.__objc_stubs: 0x43e0
-  __DATA_CONST.__got: 0x2b8
-  __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__objc_classlist: 0x148
+  __TEXT.__gcc_except_tab: 0x6e4
+  __TEXT.__cstring: 0x1413
+  __TEXT.__oslogstring: 0x32b7
+  __TEXT.__unwind_info: 0xb90
+  __TEXT.__objc_classname: 0x520
+  __TEXT.__objc_methname: 0x52e9
+  __TEXT.__objc_methtype: 0x146b
+  __TEXT.__objc_stubs: 0x4720
+  __DATA_CONST.__got: 0x2e8
+  __DATA_CONST.__const: 0xe28
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1338
+  __DATA_CONST.__objc_selrefs: 0x1410
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x1540
-  __AUTH_CONST.__objc_const: 0x79e8
+  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x16c0
+  __AUTH_CONST.__objc_const: 0x8b18
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x1fc
-  __DATA.__data: 0xab0
-  __DATA.__bss: 0x38
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x20c
+  __DATA.__data: 0xbd0
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0xe8

   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
+  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85C95C7D-891D-3C72-BAE0-50C6DF5FD906
-  Functions: 878
-  Symbols:   3438
-  CStrings:  1706
+  UUID: CCBC2FA1-F16E-3C1D-AA8F-CC35861299BE
+  Functions: 954
+  Symbols:   3728
+  CStrings:  1809
 
Symbols:
+ +[DDSUAFAssetProvider sharedProvider]
+ +[DDSUAFAssetProvider sharedProvider].cold.1
+ +[DDSUAFManager subscriberNameForClientID:]
+ +[DDSUAFManager subscriptionNameForAssertionID:withIndex:]
+ +[DDSUAFManager subscriptionNamePrefixForAssertionID:]
+ -[DDSAssertionTracker createUAFSubscriptionsForTrackedAssertions]
+ -[DDSAssertionTracker initWithDataHandler:uafManager:]
+ -[DDSAssertionTracker uafManager]
+ -[DDSUAFAssetProvider .cxx_destruct]
+ -[DDSUAFAssetProvider assetSetManager]
+ -[DDSUAFAssetProvider initWithAssetSetManager:]
+ -[DDSUAFAssetProvider init]
+ -[DDSUAFAssetProvider subscribe:subscriptions:completion:]
+ -[DDSUAFAssetProvider subscriptionsForSubscriber:]
+ -[DDSUAFAssetProvider subscriptionsForSubscriber:].cold.1
+ -[DDSUAFAssetProvider unsubscribe:subscriptionNames:completion:]
+ -[DDSUAFManager .cxx_destruct]
+ -[DDSUAFManager _createAssetSetUsagesFromQuery:]
+ -[DDSUAFManager _createAssetSetUsagesFromQuery:].cold.1
+ -[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]
+ -[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:].cold.1
+ -[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:].cold.2
+ -[DDSUAFManager assertionIDsForClientID:]
+ -[DDSUAFManager assertionIDsForClientID:].cold.1
+ -[DDSUAFManager assetProvider]
+ -[DDSUAFManager dataSource]
+ -[DDSUAFManager initWithAssetProvider:dataSource:]
+ -[DDSUAFManager removeAssertionWithIdentifier:clientID:]
+ -[DDSUAFManager removeAssertionWithIdentifier:clientID:].cold.1
+ -[DDSUAFManager removeAssertionWithIdentifier:clientID:].cold.2
+ -[DDSUAFManager setAssetProvider:]
+ -[DDSUAFManagerLDDataSource _deviceType]
+ -[DDSUAFManagerLDDataSource assetSetName]
+ -[DDSUAFManagerLDDataSource supportedLocales]
+ -[DDSUAFManagerLDDataSource supportedLocales].cold.1
+ -[DDSUAFManagerLDDataSource supportsQuery:]
+ -[DDSUAFManagerLDDataSource uafUsagesForQuery:]
+ -[DDSUAFManagerLDDataSource uafUsagesForQuery:].cold.1
+ -[DDSUAFManagerStub addAssertionForAssetsWithQuery:assertionID:clientID:]
+ -[DDSUAFManagerStub addAssertionForAssetsWithQuery:assertionID:clientID:].cold.1
+ -[DDSUAFManagerStub assertionIDsForClientID:]
+ -[DDSUAFManagerStub assertionIDsForClientID:].cold.1
+ -[DDSUAFManagerStub removeAssertionWithIdentifier:clientID:]
+ -[DDSUAFManagerStub removeAssertionWithIdentifier:clientID:].cold.1
+ _DDSUAFAssetProviderErrorDomain
+ _DDSUAFSupportedLocalesForLinguisticDataAssets
+ _DDS_GET_PLATFORM_VERSION
+ _DDS_GET_PLATFORM_VERSION.cold.1
+ _DDS_USE_UAF_MANAGER_PRESU_STAGING
+ _OBJC_CLASS_$_DDSUAFAssetProvider
+ _OBJC_CLASS_$_DDSUAFManager
+ _OBJC_CLASS_$_DDSUAFManagerLDDataSource
+ _OBJC_CLASS_$_DDSUAFManagerStub
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_CLASS_$_UAFAssetSetSubscription
+ _OBJC_IVAR_$_DDSAssertionTracker._uafManager
+ _OBJC_IVAR_$_DDSUAFAssetProvider._assetSetManager
+ _OBJC_IVAR_$_DDSUAFManager._assetProvider
+ _OBJC_IVAR_$_DDSUAFManager._dataSource
+ _OBJC_METACLASS_$_DDSUAFAssetProvider
+ _OBJC_METACLASS_$_DDSUAFManager
+ _OBJC_METACLASS_$_DDSUAFManagerLDDataSource
+ _OBJC_METACLASS_$_DDSUAFManagerStub
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _UAFAssetManagerLog
+ _UAFAssetManagerLog.cold.1
+ _UAFAssetManagerLog.logFacility
+ _UAFAssetManagerLog.onceToken
+ _UAFAssetProviderLog
+ _UAFAssetProviderLog.cold.1
+ _UAFAssetProviderLog.logFacility
+ _UAFAssetProviderLog.onceToken
+ __OBJC_$_CLASS_METHODS_DDSUAFAssetProvider
+ __OBJC_$_CLASS_METHODS_DDSUAFManager
+ __OBJC_$_INSTANCE_METHODS_DDSUAFAssetProvider
+ __OBJC_$_INSTANCE_METHODS_DDSUAFManager
+ __OBJC_$_INSTANCE_METHODS_DDSUAFManagerLDDataSource
+ __OBJC_$_INSTANCE_METHODS_DDSUAFManagerStub
+ __OBJC_$_INSTANCE_VARIABLES_DDSUAFAssetProvider
+ __OBJC_$_INSTANCE_VARIABLES_DDSUAFManager
+ __OBJC_$_PROP_LIST_DDSUAFAssetProvider
+ __OBJC_$_PROP_LIST_DDSUAFManager
+ __OBJC_$_PROP_LIST_DDSUAFManagerDataSource
+ __OBJC_$_PROP_LIST_DDSUAFManagerLDDataSource
+ __OBJC_$_PROP_LIST_DDSUAFManagerStub
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DDSUAFAssetProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DDSUAFManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DDSUAFManagerDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DDSUAFAssetProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DDSUAFManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DDSUAFManagerDataSource
+ __OBJC_$_PROTOCOL_REFS_DDSUAFAssetProvider
+ __OBJC_$_PROTOCOL_REFS_DDSUAFManager
+ __OBJC_$_PROTOCOL_REFS_DDSUAFManagerDataSource
+ __OBJC_CLASS_PROTOCOLS_$_DDSUAFAssetProvider
+ __OBJC_CLASS_PROTOCOLS_$_DDSUAFManager
+ __OBJC_CLASS_PROTOCOLS_$_DDSUAFManagerLDDataSource
+ __OBJC_CLASS_PROTOCOLS_$_DDSUAFManagerStub
+ __OBJC_CLASS_RO_$_DDSUAFAssetProvider
+ __OBJC_CLASS_RO_$_DDSUAFManager
+ __OBJC_CLASS_RO_$_DDSUAFManagerLDDataSource
+ __OBJC_CLASS_RO_$_DDSUAFManagerStub
+ __OBJC_LABEL_PROTOCOL_$_DDSUAFAssetProvider
+ __OBJC_LABEL_PROTOCOL_$_DDSUAFManager
+ __OBJC_LABEL_PROTOCOL_$_DDSUAFManagerDataSource
+ __OBJC_METACLASS_RO_$_DDSUAFAssetProvider
+ __OBJC_METACLASS_RO_$_DDSUAFManager
+ __OBJC_METACLASS_RO_$_DDSUAFManagerLDDataSource
+ __OBJC_METACLASS_RO_$_DDSUAFManagerStub
+ __OBJC_PROTOCOL_$_DDSUAFAssetProvider
+ __OBJC_PROTOCOL_$_DDSUAFManager
+ __OBJC_PROTOCOL_$_DDSUAFManagerDataSource
+ ___37+[DDSUAFAssetProvider sharedProvider]_block_invoke
+ ___45-[DDSUAFManagerLDDataSource supportedLocales]_block_invoke
+ ___45-[DDSUAFManagerLDDataSource supportedLocales]_block_invoke.cold.1
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.313
+ ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.313.cold.1
+ ___56-[DDSUAFManager removeAssertionWithIdentifier:clientID:]_block_invoke
+ ___56-[DDSUAFManager removeAssertionWithIdentifier:clientID:]_block_invoke.cold.1
+ ___58-[DDSUAFAssetProvider subscribe:subscriptions:completion:]_block_invoke
+ ___58-[DDSUAFAssetProvider subscribe:subscriptions:completion:]_block_invoke.cold.1
+ ___58-[DDSUAFAssetProvider subscribe:subscriptions:completion:]_block_invoke.cold.2
+ ___64-[DDSUAFAssetProvider unsubscribe:subscriptionNames:completion:]_block_invoke
+ ___64-[DDSUAFAssetProvider unsubscribe:subscriptionNames:completion:]_block_invoke.cold.1
+ ___64-[DDSUAFAssetProvider unsubscribe:subscriptionNames:completion:]_block_invoke.cold.2
+ ___65-[DDSAssertionTracker createUAFSubscriptionsForTrackedAssertions]_block_invoke
+ ___69-[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]_block_invoke
+ ___69-[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]_block_invoke.cold.1
+ ___UAFAssetManagerLog_block_invoke
+ ___UAFAssetProviderLog_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8r80l8r88l8
+ ___block_literal_global.15
+ ___block_literal_global.16
+ ___block_literal_global.20
+ _objc_msgSend$_createAssetSetUsagesFromQuery:
+ _objc_msgSend$_deviceType
+ _objc_msgSend$addAssertionForAssetsWithQuery:assertionID:clientID:
+ _objc_msgSend$assetProvider
+ _objc_msgSend$assetSetManager
+ _objc_msgSend$assetSetName
+ _objc_msgSend$assetSets
+ _objc_msgSend$createUAFSubscriptionsForTrackedAssertions
+ _objc_msgSend$initWithAssetProvider:dataSource:
+ _objc_msgSend$initWithAssetSetManager:
+ _objc_msgSend$initWithDataHandler:uafManager:
+ _objc_msgSend$initWithName:assetSets:usageAliases:
+ _objc_msgSend$name
+ _objc_msgSend$removeAssertionWithIdentifier:clientID:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$sharedProvider
+ _objc_msgSend$subscribe:subscriptions:completion:
+ _objc_msgSend$subscribe:subscriptions:queue:completion:
+ _objc_msgSend$subscriberNameForClientID:
+ _objc_msgSend$subscriptionNameForAssertionID:withIndex:
+ _objc_msgSend$subscriptionNamePrefixForAssertionID:
+ _objc_msgSend$subscriptionsForSubscriber:
+ _objc_msgSend$supportedLocales
+ _objc_msgSend$supportsQuery:
+ _objc_msgSend$uafManager
+ _objc_msgSend$uafUsagesForQuery:
+ _objc_msgSend$unsubscribe:subscriptionNames:completion:
+ _objc_msgSend$unsubscribe:subscriptionNames:queue:completion:
+ _sharedProvider.onceToken
+ _sharedProvider.sharedInstance
+ _supportedLocales.onceToken
+ _supportedLocales.supportedLocales
- +[DDSMobileAssetv2Provider platformVersion]
- +[DDSMobileAssetv2Provider platformVersion].cold.1
- -[DDSAssertionTracker initWithDataHandler:]
- _CFRelease
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.309
- ___48-[DDSServer listener:shouldAcceptNewConnection:]_block_invoke.309.cold.1
- ___block_descriptor_96_e8_32s40s48s56s64s72r80r88r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8s64l8r80l8r88l8
- ___block_literal_global.14
- ___block_literal_global.19
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithDataHandler:
- _objc_msgSend$platformVersion
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "%@%lu"
+ "%@.DataDeliveryService"
+ "%@.DataDeliveryService_"
+ "%@: %@"
+ "-[DDSUAFManager addAssertionForAssetsWithQuery:assertionID:clientID:]"
+ "-[DDSUAFManager assertionIDsForClientID:]"
+ "-[DDSUAFManager removeAssertionWithIdentifier:clientID:]"
+ "@\"<DDSUAFAssetProvider>\""
+ "@\"<DDSUAFManager>\""
+ "@\"<DDSUAFManagerDataSource>\""
+ "@\"NSArray\"24@0:8@\"NSString\"16"
+ "@\"UAFAssetSetManager\""
+ "@32@0:8@16Q24"
+ "B24@0:8@\"DDSAssetQuery\"16"
+ "Create UAF subscriptions for existing assertions"
+ "DDSUAFAssetProvider"
+ "DDSUAFAssetProviderErrorDomain"
+ "DDSUAFManager"
+ "DDSUAFManager.m"
+ "DDSUAFManagerDataSource"
+ "DDSUAFManagerLDDataSource"
+ "DDSUAFManagerStub"
+ "DDSUAFManagerStub: addAssertionForAssetsWithQuery called (no-op)"
+ "DDSUAFManagerStub: assertionIDsForClientID called (returning empty set)"
+ "DDSUAFManagerStub: removeAssertionWithIdentifier called (no-op)"
+ "Found %lu subscriptions for subscriber %{public}@ : %{public}@"
+ "Getting subscriptions for subscriber %@"
+ "Locale not found in query"
+ "Locale: %@ is not supported by UAF manager"
+ "No asset set usages created from query: %{public}@"
+ "Subscribe failed for %{public}@ with error: %{public}@"
+ "Subscribe request failed with error: %{public}@ for query: %{public}@"
+ "Subscribing %{public}@ to %lu subscriptions"
+ "Successfully subscribed %@"
+ "Successfully subscribed client %{public}@ with assertion %{public}@ for subscriptions: \n%{public}@"
+ "Successfully unsubscribed %@"
+ "Successfully unsubscribed client %{public}@ with assertion %{public}@ for subscriptions: %{public}@"
+ "T@\"<DDSUAFAssetProvider>\",&,N,V_assetProvider"
+ "T@\"<DDSUAFManager>\",R,N,V_uafManager"
+ "T@\"<DDSUAFManagerDataSource>\",R,N,V_dataSource"
+ "T@\"UAFAssetSetManager\",R,N,V_assetSetManager"
+ "UAF Supported locales : %@"
+ "UAFAssetDeliveryPreSUStaging"
+ "UAFAssetManager"
+ "UAFAssetProvider"
+ "UAFManager is not supported for query: %@"
+ "UAFSupportedLocales"
+ "Unsubscribe failed for %{public}@ with error: %{public}@"
+ "Unsubscribe request failed with error: %{public}@"
+ "Unsubscribing %{public}@ from %lu subscriptions"
+ "_assetProvider"
+ "_assetSetManager"
+ "_createAssetSetUsagesFromQuery:"
+ "_deviceType"
+ "_uafManager"
+ "addAssertionForAssetsWithQuery:assertionID:clientID:"
+ "assertionID.length != 0"
+ "assetProvider"
+ "assetSetManager"
+ "assetSetName"
+ "assetSets"
+ "clientID.length != 0"
+ "com.apple.linguisticdata"
+ "createUAFSubscriptionsForTrackedAssertions"
+ "device"
+ "iOS Simulator"
+ "initWithAssetProvider:dataSource:"
+ "initWithAssetSetManager:"
+ "initWithDataHandler:uafManager:"
+ "initWithName:assetSets:usageAliases:"
+ "ld.device"
+ "ld.language"
+ "name"
+ "removeAssertionWithIdentifier:clientID:"
+ "setAssetProvider:"
+ "sharedManager"
+ "sharedProvider"
+ "simulator"
+ "subscribe:subscriptions:completion:"
+ "subscribe:subscriptions:queue:completion:"
+ "subscriberNameForClientID:"
+ "subscriptionNameForAssertionID:withIndex:"
+ "subscriptionNamePrefixForAssertionID:"
+ "subscriptionsForSubscriber:"
+ "supportedLocales"
+ "supportsQuery:"
+ "uafManager"
+ "uafUsagesForQuery:"
+ "unsubscribe:subscriptionNames:completion:"
+ "unsubscribe:subscriptionNames:queue:completion:"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v40@0:8@\"DDSAssetQuery\"16@\"NSString\"24@\"NSString\"32"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "initWithDataHandler:"
- "platformVersion"

```
