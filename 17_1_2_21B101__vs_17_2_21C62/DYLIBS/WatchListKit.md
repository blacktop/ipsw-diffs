## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-800.10.14.0.0
-  __TEXT.__text: 0x5b678
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_methlist: 0x5d08
+800.20.10.0.0
+  __TEXT.__text: 0x5aabc
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_methlist: 0x5ce8
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x6b33
-  __TEXT.__oslogstring: 0x5050
-  __TEXT.__gcc_except_tab: 0xca4
+  __TEXT.__cstring: 0x6b8b
+  __TEXT.__oslogstring: 0x4b7c
+  __TEXT.__gcc_except_tab: 0xb74
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x19b4
-  __TEXT.__objc_classname: 0x11ec
-  __TEXT.__objc_methname: 0xe198
-  __TEXT.__objc_methtype: 0x1b1e
-  __TEXT.__objc_stubs: 0x8cc0
+  __TEXT.__unwind_info: 0x1984
+  __TEXT.__objc_classname: 0x11d8
+  __TEXT.__objc_methname: 0xe1da
+  __TEXT.__objc_methtype: 0x1ade
+  __TEXT.__objc_stubs: 0x8c60
   __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__const: 0x2188
-  __DATA_CONST.__objc_classlist: 0x508
+  __DATA_CONST.__const: 0x2168
+  __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xd518
-  __DATA_CONST.__objc_selrefs: 0x3048
+  __DATA_CONST.__objc_const: 0xd580
+  __DATA_CONST.__objc_selrefs: 0x3060
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__cfstring: 0x81c0
+  __AUTH_CONST.__cfstring: 0x8260
   __AUTH_CONST.__objc_intobj: 0x378
-  __AUTH_CONST.__objc_const: 0x4298
-  __AUTH_CONST.__const: 0xd40
+  __AUTH_CONST.__objc_const: 0x4208
+  __AUTH_CONST.__const: 0xd20
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0x438
+  __AUTH_CONST.__auth_got: 0x430
   __AUTH.__objc_data: 0x18b0
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x680
-  __DATA.__objc_superrefs: 0x470
-  __DATA.__objc_ivar: 0x96c
+  __DATA.__objc_classrefs: 0x688
+  __DATA.__objc_superrefs: 0x468
+  __DATA.__objc_ivar: 0x974
   __DATA.__data: 0x7a0
   __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0x19a0
+  __DATA_DIRTY.__objc_data: 0x1950
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x400
+  __DATA_DIRTY.__bss: 0x3f0
   __DATA_DIRTY.__common: 0x1
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/ParsecSubscriptionServiceSupport.framework/ParsecSubscriptionServiceSupport
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/TVAppServices.framework/TVAppServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7506316-AED3-33FC-AF28-557BF4C83E55
-  Functions: 2385
-  Symbols:   8951
+  UUID: AE06E5EE-CE55-3020-BB8C-DC5A9B1DB1CC
+  Functions: 2382
+  Symbols:   8933
   CStrings:  5527
 
Symbols:
+ -[WLKPrewarming _prefetchAppLibrary]
+ -[WLKPrewarming _prefetchIfNeeded:]
+ -[WLKSettingsStore _loadFromDiskWithCompletion:]
+ -[WLKSettingsStore refreshWithCompletion:]
+ -[WLKUserSettings _patchData]
+ -[WLKUserSettings _patchJSONDictionary]
+ -[WLKUserSettings brandSidebarSetting]
+ -[WLKUserSettings initWithBrandId:shouldHide:]
+ -[WLKUserSettings initWithBrandSidebarSetting]
+ -[WLKUserSettings initWithFavoritesSync]
+ -[WLKUserSettings setInitWithBrandSidebarSetting:]
+ -[WLKUserSettings setInitWithFavoritesSync:]
+ GCC_except_table104
+ GCC_except_table113
+ GCC_except_table18
+ GCC_except_table29
+ GCC_except_table36
+ GCC_except_table60
+ GCC_except_table76
+ GCC_except_table80
+ GCC_except_table89
+ GCC_except_table98
+ _OBJC_CLASS_$_SportsFavoriteServiceObjC
+ _OBJC_CLASS_$_TVAppBag
+ _OBJC_IVAR_$_WLKPrewarming._prefetchQueue
+ _OBJC_IVAR_$_WLKUserSettings._brandSidebarSetting
+ _OBJC_IVAR_$_WLKUserSettings._initWithBrandSidebarSetting
+ _OBJC_IVAR_$_WLKUserSettings._initWithFavoritesSync
+ _WLKNotificationsKeySymbolName
+ _WLKUserSettingsResponseKeyBrandSidebarSettingsIsHidden
+ ___132-[WLKSportsFavoriteManager watchlistd_performUserSettingsAction:setFavoritesSyncEnabled:caller:overrideLastModifiedDate:completion:]_block_invoke.188
+ ___24-[WLKSettingsStore init]_block_invoke_3
+ ___28-[WLKPrewarming _connection]_block_invoke.38
+ ___35-[WLKPrewarming _prefetchIfNeeded:]_block_invoke
+ ___35-[WLKPrewarming _prefetchIfNeeded:]_block_invoke.22
+ ___36-[WLKPrewarming _prefetchAppLibrary]_block_invoke
+ ___39-[WLKAppLibraryCore fetchApplications:]_block_invoke.5
+ ___39-[WLKSportsFavoriteManager _connection]_block_invoke.168
+ ___40+[WLKSettingsCloudUtilities _connection]_block_invoke.105
+ ___40-[WLKPrewarming prewarmDeviceAndNetwork]_block_invoke.30
+ ___40-[WLKPrewarming prewarmSubscriptionData]_block_invoke.24
+ ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke.175
+ ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke_2.176
+ ___44-[WLKSettingsStore _writeToDisk:completion:]_block_invoke_7
+ ___46-[WLKPrewarming prewarmWithConfigCachePolicy:]_block_invoke.14
+ ___48-[WLKSettingsStore _loadFromDiskWithCompletion:]_block_invoke
+ ___48-[WLKSettingsStore _loadFromDiskWithCompletion:]_block_invoke_2
+ ___49-[WLKAppLibraryCore _fetchApplicationsInProcess:]_block_invoke.28
+ ___49-[WLKAppLibraryCore _fetchApplicationsInProcess:]_block_invoke.37
+ ___49-[WLKAppLibraryCore _fetchApplicationsInProcess:]_block_invoke.40
+ ___50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.92
+ ___50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.92.cold.1
+ ___50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.94
+ ___50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.95
+ ___69+[WLKSettingsCloudUtilities _postChangeDictionaryToCloud:completion:]_block_invoke.97
+ ___69+[WLKSettingsCloudUtilities _postChangeDictionaryToCloud:completion:]_block_invoke.98
+ ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.179
+ ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.181
+ ___84+[WLKSettingsCloudUtilities _runSynchronizeSettingsFromCloudIfNeededWithCompletion:]_block_invoke.70
+ ___84+[WLKSettingsCloudUtilities _runSynchronizeSettingsFromCloudIfNeededWithCompletion:]_block_invoke.70.cold.1
+ ___84+[WLKSettingsCloudUtilities _runSynchronizeSettingsFromCloudIfNeededWithCompletion:]_block_invoke.73
+ ___84+[WLKSettingsCloudUtilities _runSynchronizeSettingsFromCloudIfNeededWithCompletion:]_block_invoke_2
+ ___97-[WLKSportsFavoriteManager _performUserSettingsAction:setFavoritesSyncEnabled:caller:completion:]_block_invoke.183
+ ___block_descriptor_40_e52_v24?0"WLKServerConfigurationResponse"8"NSError"16l
+ ___block_descriptor_48_e8_32bs_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e22_v16?0"NSDictionary"8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e52_v24?0"WLKServerConfigurationResponse"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88w_e5_v8?0lw88l8s80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.104
+ ___block_literal_global.112
+ ___block_literal_global.167
+ ___block_literal_global.170
+ ___block_literal_global.173
+ ___block_literal_global.193
+ ___block_literal_global.24
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_msgSend$_loadFromDiskWithCompletion:
+ _objc_msgSend$_patchData
+ _objc_msgSend$_patchJSONDictionary
+ _objc_msgSend$_prefetchAppLibrary
+ _objc_msgSend$_prefetchIfNeeded:
+ _objc_msgSend$accountDidChange
+ _objc_msgSend$app
+ _objc_msgSend$cachedIntegerForKey:
+ _objc_msgSend$cachedStringForKey:
+ _objc_msgSend$cachedURLForKey:
+ _objc_msgSend$refreshWithCompletion:
+ _os_signpost_id_generate
- +[WLKCachedBagManager sharedInstance]
- -[WLKCachedBagManager .cxx_destruct]
- -[WLKCachedBagManager _extractMissingKeys:dictionary:]
- -[WLKCachedBagManager _isParameterConfigurationValid:amsBag:completion:]
- -[WLKCachedBagManager _isParameterConfigurationValid:amsBag:completion:].cold.1
- -[WLKCachedBagManager _isParameterConfigurationValid:amsBag:completion:].cold.2
- -[WLKCachedBagManager _queryAMSBag:amsBag:resultHandler:]
- -[WLKCachedBagManager _queryAMSCachedBag:amsBag:observationToken:waitForUpdateOnCacheMiss:resultHandler:]
- -[WLKCachedBagManager _queryMemoryCache:]
- -[WLKCachedBagManager fetchValuesWithCompletion:waitForUpdateOnCacheMiss:amsBag:completion:]
- -[WLKCachedBagManager init]
- -[WLKSettingsStore _loadFromDisk]
- -[WLKSettingsStore refresh]
- -[WLKUserSettings _data]
- -[WLKUserSettings _jsonDictionary]
- GCC_except_table10
- GCC_except_table100
- GCC_except_table111
- GCC_except_table13
- GCC_except_table34
- GCC_except_table59
- GCC_except_table71
- GCC_except_table74
- GCC_except_table79
- GCC_except_table87
- GCC_except_table94
- _OBJC_CLASS_$_WLKCachedBagManager
- _OBJC_IVAR_$_WLKCachedBagManager._memoryCache
- _OBJC_IVAR_$_WLKCachedBagManager._operationQueue
- _OBJC_METACLASS_$_WLKCachedBagManager
- __OBJC_$_CLASS_METHODS_WLKCachedBagManager
- __OBJC_$_INSTANCE_METHODS_WLKCachedBagManager
- __OBJC_$_INSTANCE_VARIABLES_WLKCachedBagManager
- __OBJC_CLASS_RO_$_WLKCachedBagManager
- __OBJC_METACLASS_RO_$_WLKCachedBagManager
- ___105-[WLKCachedBagManager _queryAMSCachedBag:amsBag:observationToken:waitForUpdateOnCacheMiss:resultHandler:]_block_invoke
- ___105-[WLKCachedBagManager _queryAMSCachedBag:amsBag:observationToken:waitForUpdateOnCacheMiss:resultHandler:]_block_invoke.8
- ___105-[WLKCachedBagManager _queryAMSCachedBag:amsBag:observationToken:waitForUpdateOnCacheMiss:resultHandler:]_block_invoke.8.cold.1
- ___132-[WLKSportsFavoriteManager watchlistd_performUserSettingsAction:setFavoritesSyncEnabled:caller:overrideLastModifiedDate:completion:]_block_invoke.187
- ___28-[WLKPrewarming _connection]_block_invoke.37
- ___33-[WLKSettingsStore _loadFromDisk]_block_invoke
- ___33-[WLKSettingsStore _loadFromDisk]_block_invoke_2
- ___37+[WLKCachedBagManager sharedInstance]_block_invoke
- ___39-[WLKSportsFavoriteManager _connection]_block_invoke.167
- ___40+[WLKSettingsCloudUtilities _connection]_block_invoke.100
- ___40-[WLKPrewarming prewarmDeviceAndNetwork]_block_invoke.29
- ___40-[WLKPrewarming prewarmSubscriptionData]_block_invoke.22
- ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke.174
- ___40-[WLKSportsFavoriteManager isOnboarded:]_block_invoke_2.175
- ___46-[WLKPrewarming prewarmWithConfigCachePolicy:]_block_invoke.12
- ___46-[WLKPrewarming prewarmWithConfigCachePolicy:]_block_invoke.17
- ___49-[WLKAppLibraryCore _fetchApplicationsInProcess:]_block_invoke_2
- ___49-[WLKAppLibraryCore _fetchApplicationsInProcess:]_block_invoke_3
- ___49-[WLKAppLibraryCore _fetchApplicationsInProcess:]_block_invoke_4
- ___50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.88
- ___50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.88.cold.1
- ___50+[WLKSettingsCloudUtilities _fetchSyncDictionary:]_block_invoke.90
- ___57-[WLKCachedBagManager _queryAMSBag:amsBag:resultHandler:]_block_invoke
- ___57-[WLKCachedBagManager _queryAMSBag:amsBag:resultHandler:]_block_invoke_2
- ___69+[WLKSettingsCloudUtilities _postChangeDictionaryToCloud:completion:]_block_invoke.92
- ___69+[WLKSettingsCloudUtilities _postChangeDictionaryToCloud:completion:]_block_invoke.93
- ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.178
- ___69-[WLKSportsFavoriteManager _performAction:withIDs:caller:completion:]_block_invoke.180
- ___84+[WLKSettingsCloudUtilities _runSynchronizeSettingsFromCloudIfNeededWithCompletion:]_block_invoke.69
- ___92-[WLKCachedBagManager fetchValuesWithCompletion:waitForUpdateOnCacheMiss:amsBag:completion:]_block_invoke
- ___97-[WLKSportsFavoriteManager _performUserSettingsAction:setFavoritesSyncEnabled:caller:completion:]_block_invoke.181
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e22_v16?0"NSDictionary"8lw40l8s32l8
- ___block_descriptor_48_e8_32s_e52_v24?0"WLKServerConfigurationResponse"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32bs40r48r56r_e22_v16?0"NSDictionary"8lr40l8r48l8r56l8s32l8
- ___block_descriptor_64_e8_32s40s48r56r_e23_v28?08B16"NSError"20lr48l8s32l8r56l8s40l8
- ___block_descriptor_80_e8_32s40bs48r56r64r72w_e37_v28?0"NSDictionary"8"NSError"16B24lw72l8r48l8r56l8r64l8s32l8s40l8
- ___block_descriptor_80_e8_32s40s48bs56r64r72w_e5_v8?0lw72l8r56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8s72l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e5_v8?0lw80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.105
- ___block_literal_global.166
- ___block_literal_global.169
- ___block_literal_global.172
- ___block_literal_global.190
- ___block_literal_global.23
- ___block_literal_global.36
- ___block_literal_global.62
- ___block_literal_global.99
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_group_notify
- _objc_msgSend$_data
- _objc_msgSend$_extractMissingKeys:dictionary:
- _objc_msgSend$_isParameterConfigurationValid:amsBag:completion:
- _objc_msgSend$_jsonDictionary
- _objc_msgSend$_loadFromDisk
- _objc_msgSend$_queryAMSBag:amsBag:resultHandler:
- _objc_msgSend$_queryAMSCachedBag:amsBag:observationToken:waitForUpdateOnCacheMiss:resultHandler:
- _objc_msgSend$_queryMemoryCache:
- _objc_msgSend$cachedValuesForKeys:observationToken:updateHandler:
- _objc_msgSend$dictionaryWithDictionary:
- _objc_msgSend$fetchValuesWithCompletion:waitForUpdateOnCacheMiss:amsBag:completion:
- _objc_msgSend$minusSet:
- _objc_msgSend$removeObserverWithToken:
- _objc_msgSend$uninitializedToken
CStrings:
+ "Config.prefetchAppLibrary"
+ "LibraryCore.configureDemoBundles"
+ "LibraryCore.fetchApplicationsInProcess"
+ "LibraryCore.fetchApplicationsInProcess.ActiveSubscription"
+ "LibraryCore.fetchApplicationsInProcess.InstalledAppBundles"
+ "LibraryCore.fetchApplicationsInProcess.SubscribedAppBundle"
+ "LibraryCore.fetchApplicationsInProcess.checkAppRecords"
+ "LibraryCore.fetchApplicationsInProcess.filter"
+ "Nil Self"
+ "T@\"NSDictionary\",R,C,N,V_brandSidebarSetting"
+ "TB,N,V_initWithBrandSidebarSetting"
+ "TB,N,V_initWithFavoritesSync"
+ "WLKAppLibraryCore - enumerate apps elapsed time: %.5f, recordCount=%d"
+ "WLKAppLibraryCore - filter elapsed time: %.5f"
+ "WLKPrewarming - prefetchAppLibrary begin"
+ "WLKPrewarming - prefetchAppLibrary end"
+ "WLKSettingsCloudUtilities - SettingStore maxAge configuration is nil, use default value=%lu"
+ "WLKSettingsCloudUtilities - SettingStore maxAge=%lu"
+ "WLKSettingsStore: ignoring refreshWithCompletion call since ignoreChangesCount is > 0."
+ "_brandSidebarSetting"
+ "_initWithBrandSidebarSetting"
+ "_initWithFavoritesSync"
+ "_loadFromDiskWithCompletion:"
+ "_patchData"
+ "_patchJSONDictionary"
+ "_prefetchAppLibrary"
+ "_prefetchIfNeeded:"
+ "_prefetchQueue"
+ "accountDidChange"
+ "app"
+ "brandSidebarSetting"
+ "cachedIntegerForKey:"
+ "cachedStringForKey:"
+ "cachedURLForKey:"
+ "com.apple.watchlistkit.prefetch"
+ "initWithBrandId:shouldHide:"
+ "initWithBrandSidebarSetting"
+ "initWithFavoritesSync"
+ "isHidden"
+ "jasper"
+ "refreshWithCompletion:"
+ "setInitWithBrandSidebarSetting:"
+ "setInitWithFavoritesSync:"
+ "symbolName"
- "B40@0:8@16@24@?32"
- "Error: AMS Bag is nil"
- "Error: Must supply at least one key to fetch."
- "WLKAppLibraryCore - enumerate apps elapsed time: %.5f"
- "WLKCachedBag.GetValues"
- "WLKCachedBag.GetValues.AsyncUpdate"
- "WLKCachedBag.GetValues.CachedReturn"
- "WLKCachedBag.GetValues.MemoryCache"
- "WLKCachedBag.GetValues.NetworkReturn"
- "WLKCachedBagManager"
- "WLKCachedBagManager - AMS cached update handler has fired after a timeout has occurred. Ignore since we are using the regular AMSBag."
- "WLKCachedBagManager - AMSBag observation token has not changed from uninitialized state. Ignoring removal from AMSBag."
- "WLKCachedBagManager - Cached dictionary is missing keys=%@, waiting for updateHandler before calling completion"
- "WLKCachedBagManager - Calling final completion handler"
- "WLKCachedBagManager - Completed fetching values from AMSBag"
- "WLKCachedBagManager - Error: AMS Bag is nil"
- "WLKCachedBagManager - Error: Bailing with empty key set"
- "WLKCachedBagManager - Fetching key set: %@"
- "WLKCachedBagManager - Finish handler called. didRemoveObserver=%d stopObserving=%d didCallCompletion=%d"
- "WLKCachedBagManager - Querying AMSBag for non-AppleTV process"
- "WLKCachedBagManager - Querying AMSCachedBag in AppleTV process"
- "WLKCachedBagManager - Received cached dictionary from AMS bag. Keys returned count=%lu"
- "WLKCachedBagManager - Received updated values from AMS update handler validity: %d, for keys: %@"
- "WLKCachedBagManager - Removed AMSBag observer with token %llu"
- "WLKCachedBagManager - Returning with cached dictionary"
- "WLKCachedBagManager - Returning with memory cache hit. Continuing with AMSBag call in background."
- "WLKCachedBagManager - Running key set query on AMS Bag for keys: %@"
- "WLKCachedBagManager - Running key set query on AMS Cached Bag"
- "WLKCachedBagManager - Timeout handler fired, but cached bag callback has not executed. Resorting to AMSBag call for keys: %@"
- "WLKCachedBagManager - Timeout handler fired, but cached bag update handler has already executed as expected. Ignoring."
- "WLKCachedBagManager - Updating memory cache"
- "_extractMissingKeys:dictionary:"
- "_isParameterConfigurationValid:amsBag:completion:"
- "_jsonDictionary"
- "_loadFromDisk"
- "_memoryCache"
- "_operationQueue"
- "_queryAMSBag:amsBag:resultHandler:"
- "_queryAMSCachedBag:amsBag:observationToken:waitForUpdateOnCacheMiss:resultHandler:"
- "_queryMemoryCache:"
- "cachedValuesForKeys:observationToken:updateHandler:"
- "com.apple.WatchListKit.WLKCachedBagManager"
- "dictionaryWithDictionary:"
- "fetchValuesWithCompletion:waitForUpdateOnCacheMiss:amsBag:completion:"
- "minusSet:"
- "removeObserverWithToken:"
- "uninitializedToken"
- "v28@?0@\"NSDictionary\"8@\"NSError\"16B24"
- "v44@0:8@16B24@28@?36"
- "v52@0:8@16@24^Q32B40@?44"

```
