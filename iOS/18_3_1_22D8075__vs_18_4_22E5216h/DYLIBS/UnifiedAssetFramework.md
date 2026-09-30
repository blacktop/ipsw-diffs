## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3402.65.1.11.1
-  __TEXT.__text: 0x62da8
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x30f0
+3404.58.2.0.0
+  __TEXT.__text: 0x689a0
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x34d8
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x10b0
-  __TEXT.__cstring: 0x95ce
-  __TEXT.__oslogstring: 0xadfa
   __TEXT.__dlopen_cstrs: 0x296
-  __TEXT.__unwind_info: 0x10e0
-  __TEXT.__objc_classname: 0x411
-  __TEXT.__objc_methname: 0x98de
-  __TEXT.__objc_methtype: 0xeae
-  __TEXT.__objc_stubs: 0x7b60
-  __DATA_CONST.__got: 0x4d0
-  __DATA_CONST.__const: 0x1a18
-  __DATA_CONST.__objc_classlist: 0x158
+  __TEXT.__gcc_except_tab: 0x1358
+  __TEXT.__cstring: 0x9e5d
+  __TEXT.__oslogstring: 0xbbc1
+  __TEXT.__unwind_info: 0x1158
+  __TEXT.__objc_classname: 0x424
+  __TEXT.__objc_methname: 0x9f26
+  __TEXT.__objc_methtype: 0xfe4
+  __TEXT.__objc_stubs: 0x8100
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0x1b40
+  __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24e0
+  __DATA_CONST.__objc_selrefs: 0x26f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x580
+  __DATA_CONST.__objc_arraydata: 0x108
+  __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x3e60
-  __AUTH_CONST.__objc_const: 0x44d0
+  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__objc_const: 0x42d0
   __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x338
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x34c
   __DATA.__data: 0x230
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__bss: 0x2e0
+  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA_DIRTY.__bss: 0x2f0
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 1356
-  Symbols:   1941
-  CStrings:  3449
+  Functions: 1408
+  Symbols:   2009
+  CStrings:  3616
 
Symbols:
+ _OBJC_CLASS_$_MAAutoAssetSetRapidLock
+ _OBJC_CLASS_$_UAFExpiredAssets
+ _OBJC_METACLASS_$_UAFExpiredAssets
+ _fcntl
+ _kUAFAutoAssetDiscretionaryReason
+ _kUAFCacheDir
+ _kUAFDeprecatedConfigurationDir
+ _kUAFDeprecatedSeparator
+ _kUAFExpiredAssetsDir
+ _kUAFObservePolicyIgnoreMobileAssetStartup
+ _kUAFTokenExtension
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _proc_listpidspath
+ _proc_pidfdinfo
+ _proc_pidinfo
+ _sysctlbyname
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _objc_retain_x6
CStrings:
+ "%s #settings Auto retry skipped due to need for inexpensive network"
+ "%s #settings Download API call"
+ "%s #settings Skipping due to one attempt already in progress"
+ "%s %{public}@: MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil for asset set - %{public}@"
+ "%s %{public}@: updateAssets for subscribers '%{public}@'"
+ "%s Asset set %{public}@ incompatible with current OS, removing"
+ "%s AssetSet Token: %{public}@: %{public}@"
+ "%s Attempting force remove of asset set '%{public}@'"
+ "%s Auto asset set %{public}@ has expected specifiers %{public}@ and is %{public}@"
+ "%s Auto asset set %{public}@ is configured, has atomic instance %{public}@, is available to clients, and current OS supported but current assets %{public}@ are marked as expired"
+ "%s Can't unlock %{public}@: already unlocked"
+ "%s Cannot add deprecated values from %{public}@ to %{public}@"
+ "%s Commit of exclusive transaction of tables creation failed"
+ "%s Could not get AFSiriCapabilitiesServiceClient class"
+ "%s Could not initialize a new AFSiriCapabilitiesClient"
+ "%s Could not prepare statements after database recreation"
+ "%s Could not rename %@ to %@: %{public}@"
+ "%s Could not set discretionary policy for asset set %{public}@ : %{public}@"
+ "%s Deprecated value %{public}@ already defined"
+ "%s Detected database corruption.  Deleting database and recreating: %d"
+ "%s Download status of assets for subscribers: %{public}@"
+ "%s Emitting asset set arrived daily status event for auto asset set %{public}@, pre-staged:%d"
+ "%s Emitting daily status scheduled event for asset set %{public}@, pre-staged: %d"
+ "%s Exlocked %{public}@"
+ "%s Expired Asset Set Token: %{public}@"
+ "%s Expired assets token from %{public}@ does match %{public}@: %{public}@"
+ "%s Expired assets token from %{public}@ does not match %{public}@: %{public}@"
+ "%s Failed fcntl %{public}@ to check nature of lock: %{public}@"
+ "%s Failed to add deprecated values from %{public}@"
+ "%s Failed to archive expired assets token %{public}@: %{public}@"
+ "%s Failed to create expired assets token dir %{public}@ for token %{public}@: %{public}@"
+ "%s Failed to get expired assets token dir for %{public}@: %{public}@"
+ "%s Failed to get expired assets token dir: %{public}@"
+ "%s Failed to lock %{public}@: %{public}@"
+ "%s Failed to open %{public}@ to check nature of lock: %{public}@"
+ "%s Failed to open %{public}@: %{public}@"
+ "%s Failed to read expired assets token from %{public}@: %{public}@"
+ "%s Failed to remove token at %{public}@: %{public}@"
+ "%s Failed to unarchive expired assets token from %{public}@: %{public}@"
+ "%s Failed to unlock %{public}@: %{public}@"
+ "%s Failed to write expired assets token %{public}@ to %{public}@: %{public}@"
+ "%s Force remove of asset set '%{public}@' failed: %@"
+ "%s Found pids %{public}@ locking %{public}@"
+ "%s Generating expired asset set tokens"
+ "%s Invalid Pallas override URL: %{public}@ population: %{public}@"
+ "%s Invalid Pallas server URL: %{public}@ population: %{public}@"
+ "%s Loading deprecated values to process subscription for usage alias %{public}@ with value %{public}@"
+ "%s Locked %{public}@"
+ "%s Marking token %{public}@ expired completed (error = %{public}@)"
+ "%s Not actually locking %{public}@ and instead incrementing ref count to %lld"
+ "%s Not actually locking %{public}@ as there is no atomic instance but roots are present"
+ "%s Not actually unlocking %{public}@ and instead decrementing ref count to %lld"
+ "%s Not actually unlocking %{public}@ as there is no atomic instance"
+ "%s Not trying to load %@ as a deprecated usage alias configuration file as it for usage alias %{public}@, not %{public}@"
+ "%s Not trying to load %@ as a deprecated usage alias configuration file as it lacks the \"plist\" extension"
+ "%s Opened %{public}@"
+ "%s Reconfiguration of %{public}@ produced no autoAssetSet"
+ "%s Removal of incompatible asset set %{public}@ complete, reconfiguring"
+ "%s Returning asset download status: %lu for subscribers: %{public}@"
+ "%s Returning status: %lu for subscribers: %{public}@ as the asset set usages are nil"
+ "%s Rollback exclusive transaction of tables creation failed"
+ "%s Rolling back exclusive transaction of tables creation"
+ "%s SQL error while executing statement: '%{public}@': (%d) '%{public}s"
+ "%s Setting need policy for asset set '%{public}@' to not user initiated"
+ "%s Setting nil default for Pallas server URL for population %{public}@"
+ "%s Siri IE is now: wants assets: %d, language: %{public}@, mode: %{public}@"
+ "%s Siri configured for: language %{public}@, mode: %{public}@ (assistant enabled: %d, assistant language: %{public}@)"
+ "%s Unlocked %{public}@"
+ "%s UpdateTrialFactors complete"
+ "%s Wrote expired assets token %{public}@ to %{public}@"
+ "%s markAssetsExpired of %{public}@ complete"
+ "%s markAssetsExpired of %{public}@ failed with: %@"
+ "%s proc_listpidspath of %{public}@ failed: %{public}@"
+ "%s proc_pidinfo for pid %lld for file %{public}@ failed: %{public}@"
+ "%s stat of %{public}@ failed: %{public}@"
+ "'"
+ "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:downloaded:currentPolicy:]"
+ "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke"
+ "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:]_block_invoke_2"
+ "+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]"
+ "+[UAFAutoAssetManager releaseIncompatibleAssetSet:specifiers:configuration:]_block_invoke"
+ "+[UAFAutoAssetManager setBackgroundNeedPolicy:]"
+ "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:]"
+ "+[UAFAutoAssetManager stageAssetSet:targets:]"
+ "+[UAFAutoAssetSet autoAssetSetStatus:]"
+ "+[UAFCommonUtilities _setUAFPopulation:forAssetTypes:url:]"
+ "+[UAFCommonUtilities deviceSupportAssistantEngine]"
+ "+[UAFExpiredAssets assetsExpired:error:]"
+ "+[UAFExpiredAssets expiredTokens:]"
+ "+[UAFExpiredAssets loadToken:error:]"
+ "+[UAFExpiredAssets markAssetsExpired:error:]"
+ "+[UAFExpiredAssets removeToken:]"
+ "+[UAFInstrumentationProvider _constructSelfAssetSet:storeManager:]"
+ "+[UAFInstrumentationProvider logSubscriptionsStatus]_block_invoke"
+ "-[UAFAssetSet assetSetIdForSELF:stagedDuringSU:]"
+ "-[UAFAssetSetConsistencyToken exlock:]"
+ "-[UAFAssetSetConsistencyToken nolock:]"
+ "-[UAFAssetSetConsistencyToken processIdIsLockingToken:statBuffer:error:]"
+ "-[UAFAssetSetConsistencyToken processIdsLockingToken:]"
+ "-[UAFAssetSetManager assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:]"
+ "-[UAFAssetSetManager diskSpaceNeededForSubscribers:storeManager:configurationManager:error:]"
+ "-[UAFAssetSetManager downloadStatusForSubscribers:]"
+ "-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]"
+ "-[UAFAssetSetManager downloadStatusForSubscribers:queue:completion:]_block_invoke_2"
+ "-[UAFAssetSetManager markAssetsExpired:completion:]_block_invoke"
+ "-[UAFAssetSetManager observeAssetSet:policies:queue:handler:]"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke"
+ "-[UAFAssetSetManager updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_8"
+ "-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]"
+ "-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke"
+ "-[UAFAssetSetObserver initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:]_block_invoke_2"
+ "-[UAFAssetUtilities _downloadSiriAssetsWithDelay:]"
+ "-[UAFAssetUtilities downloadSiriAssetsIfNeeded]"
+ "-[UAFAssetUtilities downloadSiriAssetsOverCellular]"
+ "-[UAFAssetUtilities downloadSiriAssets]"
+ "-[UAFAssetUtilitiesService _triggerCompletionTimerForLanguage:]"
+ "-[UAFConfigurationManager getUsageAlias:includeDeprecatedValues:]"
+ "-[UAFSubscriptionStoreManager _dropTable:]"
+ "-[UAFSubscriptionStoreManager _openDatabaseFile:existed:]"
+ "-[UAFSubscriptionStoreManager _prepareStatements]"
+ "-[UAFUsageAliasConfiguration addDeprecatedValues:]"
+ "-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke"
+ "-[UAFXPCConnection markAssetsExpired:completion:]_block_invoke_2"
+ "-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke_2"
+ ".corrupt"
+ ".deprecated"
+ "@\"MAAutoAssetSetRapidLock\""
+ "@28@0:8B16^B20"
+ "@32@0:8@16^B24"
+ "@48@0:8@16@24@32^B40"
+ "@48@0:8@16@24B32B36@40"
+ "@52@0:8@16B24@28@36@?44"
+ "@56@0:8@16@24^B32^B40^@48"
+ "@60@0:8@16@24B32^B36^B44^@52"
+ "@64@0:8@16@24@32@40@48@56"
+ "AFSiriCapabilitiesServiceClient"
+ "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@ with ref count %lld) experiment %@ preinstalledAssetsSummary %@ bootUUID %@ isBootUUIDCurrent %d"
+ "AssetSetTokens"
+ "B36@0:8i16^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}20^@28"
+ "B72@0:8@16@24B32B36@40^B48^B56^B64"
+ "DROP TABLE IF EXISTS %@"
+ "Deprecated"
+ "ExpiredAssetSetTokens"
+ "ExpiredAssets"
+ "IgnoreMobileAssetStartup"
+ "T@\"MAAutoAssetSetRapidLock\",R,N,V_rapidLock"
+ "T@\"NSString\",R,N,V_bootUUID"
+ "TB,R,N,V_isBootUUIDCurrent"
+ "TB,R,N,V_locked"
+ "The bootUUID doesn't match the current bootUUID"
+ "There are no underlying assets (neither atomic instance nor asset roots)"
+ "Ti,N,V_refCount"
+ "UAFExpiredAssets"
+ "URLForDirectory:inDomain:appropriateForURL:create:error:"
+ "Vv32@0:8@\"UAFAssetSetConsistencyToken\"16@?<v@?@\"NSError\">24"
+ "_assistantUsageAliasForMode:"
+ "_bootUUID"
+ "_completionWatchdogInProgress"
+ "_currentAssistantMode:"
+ "_dropTable:"
+ "_isBootUUIDCurrent"
+ "_openDatabaseFile:existed:"
+ "_prepareStatements"
+ "_rapidLock"
+ "_refCount"
+ "_setUAFPopulation:forAssetTypes:url:"
+ "acquireShortTermLockSync"
+ "addDeprecatedValues:"
+ "assetSetIdForSELF:stagedDuringSU:"
+ "assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:"
+ "assetsExpired:error:"
+ "autoAssetSetStatus:"
+ "backgroundNeedPolicy"
+ "bootUUID"
+ "bootUUIDError"
+ "configureAssetSet:specifiers:changed:downloaded:currentPolicy:"
+ "copyBootSessionUUID"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "defaultCheckPolicy"
+ "discretionary"
+ "diskSpaceNeededForSubscribers:error:"
+ "diskSpaceNeededForSubscribers:storeManager:configurationManager:error:"
+ "downloadStatusForSubscribers:"
+ "downloadStatusForSubscribers:queue:completion:"
+ "downloaded"
+ "endShortTermLockSync"
+ "exlock:"
+ "expiredTokens:"
+ "fileLockPolicy"
+ "fromPreSoftwareUpdateStaging"
+ "getAutoAssetSet:specifiers:addEntries:configured:downloaded:currentPolicy:"
+ "getDeprecatedUsageAliasNameFromPath:"
+ "getSpecifiers:assetSetUsages:experiment:"
+ "getUsageAlias:includeDeprecatedValues:"
+ "hasIdenticalAssets:"
+ "hasIdenticalAssets:includeBootUUID:"
+ "immediateNeedPolicy"
+ "init:assetSetIdentifier:assetSetAtomicInstance:"
+ "initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:"
+ "initWithUTF8String:"
+ "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:"
+ "isBootUUIDCurrent"
+ "jsonDictionary"
+ "kern.bootsessionuuid"
+ "latestDownloadedAtomicInstanceFromPreSUStaging"
+ "loadToken:error:"
+ "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:experiment:"
+ "manageGMSSiriLanguageSubscription:language:mode:"
+ "markAssetsExpired:completion:"
+ "markAssetsExpired:error:"
+ "new"
+ "nolock:"
+ "not downloaded"
+ "observeAssetSet:policies:queue:handler:"
+ "processIdIsLockingToken:statBuffer:error:"
+ "processIdsLockingToken:"
+ "q24@0:8^@16"
+ "rapidLock"
+ "refCount"
+ "releaseIncompatibleAssetSet:specifiers:configuration:"
+ "removeToken:"
+ "setBackgroundNeedPolicy:"
+ "setFromPreSoftwareUpdateStaging:"
+ "setRefCount:"
+ "setUAFPopulation:url:"
+ "shouldCheckAssetSet:autoAssetSet:changed:downloaded:experiment:locked:userInitiated:removalNeeded:"
+ "shouldDownloadAssetsForSiriSystemAssistantExperienceSync"
+ "stageAssetSet:targets:"
+ "tokenDir:"
+ "tokenFilename:"
+ "uaftoken"
+ "unlockableTokenError"
+ "updateAssetsForSubscribers:policies:queue:detailedProgress:completion:"
+ "updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:"
+ "userInitiated"
+ "v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v36@0:8B16@20q28"
+ "v80@0:8@16@24@32@?40@?48@?56@64@72"
+ "vendingAtomicInstanceForConfiguredEntries"
+ "writeToURL:options:error:"
- "%@/%@"
- "%@: %@"
- "%s %{public}@: updateAssets for subscriber '%{public}@' with subscription '%{public}@'"
- "%s Auto asset set %{public}@ has expected specifiers %{public}@"
- "%s AutoAssetSet %{public}@ not provided, creating a new one for staging."
- "%s Can't unlock %@: already unlocked"
- "%s Could not create array from '%{public}@'"
- "%s Could not get auto asset type of auto asset set %{public}@: no config file found"
- "%s Downloading assets for subscriber: %{public}@ and subscription: %{public}@"
- "%s Emitting asset set arrived daily status event for auto asset set %{public}@:"
- "%s Experimentation not enabled for asset set %{public}@"
- "%s Failed to lock %@: %@"
- "%s Failed to unlock %@: %@"
- "%s Locked %@"
- "%s MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil for asset set - %{public}@"
- "%s No subscriptions for %{public}@ %{public}@: %{public}@"
- "%s Returning asset download status: %lu for subscriber: %{public}@ and subscription: %{public}@"
- "%s Returning status: %lu for subscriber: %{public}@ and subscription: %{public}@ as the asset set usages are nil"
- "%s Siri IE is now: wants assets: %d, language: %@"
- "%s Siri configured for: language %{public}@, mode: %{public}@"
- "%s Subscriptions for %{public}@ %{public}@: %{public}@"
- "%s Unexpected experiment file content for Asset Set %{public}@"
- "%s Unlocked %@"
- "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:]"
- "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:]"
- "+[UAFAutoAssetManager getSpecifiers:assetSetUsages:disableExperimentation:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke"
- "+[UAFAutoAssetManager manageAssetSet:specifiers:lockIfUnchanged:userInitiated:]_block_invoke_2"
- "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]"
- "+[UAFAutoAssetManager stageAssetSet:targets:autoAssetSet:]"
- "+[UAFAutoAssetSet catalogAssetSetID:]"
- "+[UAFCommonUtilities _setUAFPopulation:forAssetTypes:]"
- "+[UAFInstrumentationProvider logSubscriptionsStatus]"
- "-[UAFAssetSetManager assetSetUsagesForStatusForSubscriber:subscriptionName:status:]"
- "-[UAFAssetSetManager diskSpaceNeededForSubscriber:subscriptionName:storeManager:configurationManager:error:]"
- "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:]"
- "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]"
- "-[UAFAssetSetManager downloadStatusForSubscriber:subscriptionName:queue:completion:]_block_invoke_2"
- "-[UAFAssetSetManager observeAssetSet:queue:handler:]"
- "-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]"
- "-[UAFAssetSetManager updateAssetsForSubscriber:subscriptionName:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:]_block_invoke_7"
- "-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]"
- "-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]_block_invoke"
- "-[UAFAssetSetObserver initWithAssetSet:configurationDirURLs:queue:updateHandler:]_block_invoke_2"
- "-[UAFConfigurationManager getUsageAlias:]"
- "@40@0:8@16@24^Q32"
- "@44@0:8@16@24B32^B36"
- "@56@0:8@16@24@32@40^@48"
- "AFDeviceSupportsSAE"
- "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@) experiment %@ preinstalledAssetsSummary %@"
- "B44@0:8@16@24B32^B36"
- "TB,N,V_locked"
- "_setUAFPopulation:forAssetTypes:"
- "assetSetIdForSELF:"
- "assetSetUsagesForStatusForSubscriber:subscriptionName:status:"
- "catalogAssetSetID:"
- "checkResourceIsReachableAndReturnError:"
- "configureAssetSet:specifiers:changed:"
- "diskSpaceNeededForSubscriber:subscriptionName:storeManager:configurationManager:error:"
- "getAutoAssetSet:specifiers:addEntries:configured:"
- "getSpecifiers:assetSetUsages:"
- "getSpecifiers:assetSetUsages:disableExperimentation:"
- "getUsageAlias:"
- "initFileURLWithPath:"
- "manageAssetSet:specifiers:lockIfUnchanged:userInitiated:"
- "manageGMSSiriLanguageSubscription:language:"
- "setLocked:"
- "shouldCheckAssetSet:autoAssetSet:changed:locked:"
- "stageAssetSet:targets:autoAssetSet:"
- "updateAssets:policies:queue:progress:completion:"
- "updateAssets:policies:queue:progress:completion:storeManager:configurationManager:"
- "updateAssets:subscription:policies:queue:progress:completion:"
- "updateAssets:subscription:policies:queue:progress:completion:storeManager:configurationManager:"
- "updateAssets:subscription:policies:queue:progressWithStatus:completion:"
- "updateFinished"
- "v72@0:8@16@24@32@?40@?48@56@64"
- "v80@0:8@16@24@32@40@?48@?56@64@72"

```
