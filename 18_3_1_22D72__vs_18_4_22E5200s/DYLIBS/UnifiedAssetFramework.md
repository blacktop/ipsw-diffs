## UnifiedAssetFramework

> `/System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework`

```diff

-3402.65.1.11.1
-  __TEXT.__text: 0x62da8
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x30f0
+3404.50.4.1.3
+  __TEXT.__text: 0x66110
+  __TEXT.__auth_stubs: 0xb40
+  __TEXT.__objc_methlist: 0x33dc
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
+  __TEXT.__gcc_except_tab: 0x134c
+  __TEXT.__cstring: 0x9afd
+  __TEXT.__oslogstring: 0xb322
+  __TEXT.__unwind_info: 0x1110
+  __TEXT.__objc_classname: 0x413
+  __TEXT.__objc_methname: 0x9cd3
+  __TEXT.__objc_methtype: 0xf69
+  __TEXT.__objc_stubs: 0x7e80
+  __DATA_CONST.__got: 0x4d8
+  __DATA_CONST.__const: 0x1aa8
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24e0
+  __DATA_CONST.__objc_selrefs: 0x2648
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x580
+  __DATA_CONST.__objc_arraydata: 0x108
+  __AUTH_CONST.__auth_got: 0x5b0
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x3e60
-  __AUTH_CONST.__objc_const: 0x44d0
+  __AUTH_CONST.__cfstring: 0x4000
+  __AUTH_CONST.__objc_const: 0x4238
   __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x338
+  __AUTH.__objc_data: 0x140
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
+  Functions: 1384
+  Symbols:   1980
+  CStrings:  3540
 
Symbols:
+ _OBJC_CLASS_$_MAAutoAssetSetRapidLock
+ _fcntl
+ _kUAFDeprecatedConfigurationDir
+ _kUAFDeprecatedSeparator
+ _kUAFObservePolicyIgnoreMobileAssetStartup
+ _malloc_type_calloc
+ _malloc_type_malloc
+ _proc_listpidspath
+ _proc_pidfdinfo
+ _proc_pidinfo
+ _sysctlbyname
- _objc_retain_x6
CStrings:
+ "%s #settings Auto retry skipped due to need for inexpensive network"
+ "%s #settings Download API call"
+ "%s #settings Skipping due to one attempt already in progress"
+ "%s %{public}@: MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil for asset set - %{public}@"
+ "%s %{public}@: updateAssets for subscribers '%{public}@'"
+ "%s Auto asset set %{public}@ has expected specifiers %{public}@ and is %{public}@"
+ "%s Can't unlock %{public}@: already unlocked"
+ "%s Cannot add deprecated values from %{public}@ to %{public}@"
+ "%s Could not prepare statements after database recreation"
+ "%s Could not rename %@ to %@: %{public}@"
+ "%s Deprecated value %{public}@ already defined"
+ "%s Detected database corruption.  Deleting database and recreating: %d"
+ "%s Download status of assets for subscribers: %{public}@"
+ "%s Exlocked %{public}@"
+ "%s Failed fcntl %{public}@ to check nature of lock: %{public}@"
+ "%s Failed to add deprecated values from %{public}@"
+ "%s Failed to lock %{public}@: %{public}@"
+ "%s Failed to open %{public}@ to check nature of lock: %{public}@"
+ "%s Failed to open %{public}@: %{public}@"
+ "%s Failed to unlock %{public}@: %{public}@"
+ "%s Found pids %{public}@ locking %{public}@"
+ "%s Loading deprecated values to process subscription for usage alias %{public}@ with value %{public}@"
+ "%s Locked %{public}@"
+ "%s Not actually locking %{public}@ and instead incrementing ref count to %lld"
+ "%s Not actually locking %{public}@ as there is no atomic instance but roots are present"
+ "%s Not actually unlocking %{public}@ and instead decrementing ref count to %lld"
+ "%s Not actually unlocking %{public}@ as there is no atomic instance"
+ "%s Not trying to load %@ as a deprecated usage alias configuration file as it for usage alias %{public}@, not %{public}@"
+ "%s Not trying to load %@ as a deprecated usage alias configuration file as it lacks the \"plist\" extension"
+ "%s Opened %{public}@"
+ "%s Returning asset download status: %lu for subscribers: %{public}@"
+ "%s Returning status: %lu for subscribers: %{public}@ as the asset set usages are nil"
+ "%s SQL error while executing statement: '%{public}@': (%d) '%{public}s"
+ "%s Unlocked %{public}@"
+ "%s UpdateTrialFactors complete"
+ "%s proc_listpidspath of %{public}@ failed: %{public}@"
+ "%s proc_pidinfo for pid %lld for file %{public}@ failed: %{public}@"
+ "%s stat of %{public}@ failed: %{public}@"
+ "'"
+ "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:downloaded:]"
+ "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:downloaded:]"
+ "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:downloaded:locked:userInitiated:removalNeeded:]"
+ "+[UAFAutoAssetManager stageAssetSet:targets:]"
+ "+[UAFAutoAssetSet autoAssetSetStatus:]"
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
+ "-[UAFSubscriptionStoreManager _openDatabaseFile:existed:]"
+ "-[UAFSubscriptionStoreManager _prepareStatements]"
+ "-[UAFUsageAliasConfiguration addDeprecatedValues:]"
+ "-[UAFXPCConnection subscriptionsForSubscriber:completion:]_block_invoke_2"
+ ".corrupt"
+ ".deprecated"
+ "@\"MAAutoAssetSetRapidLock\""
+ "@28@0:8B16^B20"
+ "@32@0:8@16^B24"
+ "@48@0:8@16@24@32^B40"
+ "@48@0:8@16@24^B32^B40"
+ "@52@0:8@16@24B32^B36^B44"
+ "@52@0:8@16B24@28@36@?44"
+ "@64@0:8@16@24@32@40@48@56"
+ "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@ with ref count %lld) experiment %@ preinstalledAssetsSummary %@ bootUUID %@ isBootUUIDCurrent %d"
+ "B36@0:8i16^{stat=iSSQIIi{timespec=qq}{timespec=qq}{timespec=qq}{timespec=qq}qqiIIi[2q]}20^@28"
+ "B64@0:8@16@24B32B36^B40^B48^B56"
+ "Deprecated"
+ "IgnoreMobileAssetStartup"
+ "T@\"MAAutoAssetSetRapidLock\",R,N,V_rapidLock"
+ "T@\"NSString\",R,N,V_bootUUID"
+ "TB,R,N,V_isBootUUIDCurrent"
+ "TB,R,N,V_locked"
+ "The bootUUID doesn't match the current bootUUID"
+ "There are no underlying assets (neither atomic instance nor asset roots)"
+ "Ti,N,V_refCount"
+ "_bootUUID"
+ "_completionWatchdogInProgress"
+ "_isBootUUIDCurrent"
+ "_openDatabaseFile:existed:"
+ "_prepareStatements"
+ "_rapidLock"
+ "_refCount"
+ "acquireShortTermLockSync"
+ "addDeprecatedValues:"
+ "assetSetIdForSELF:stagedDuringSU:"
+ "assetSetUsagesForSubscribers:storeManager:configurationManager:anyUnknown:"
+ "autoAssetSetStatus:"
+ "bootUUID"
+ "bootUUIDError"
+ "configureAssetSet:specifiers:changed:downloaded:"
+ "copyBootSessionUUID"
+ "defaultCheckPolicy"
+ "defaultNeedPolicy"
+ "diskSpaceNeededForSubscribers:error:"
+ "diskSpaceNeededForSubscribers:storeManager:configurationManager:error:"
+ "downloadStatusForSubscribers:"
+ "downloadStatusForSubscribers:queue:completion:"
+ "downloaded"
+ "endShortTermLockSync"
+ "exlock:"
+ "fileLockPolicy"
+ "getAutoAssetSet:specifiers:addEntries:configured:downloaded:"
+ "getDeprecatedUsageAliasNameFromPath:"
+ "getUsageAlias:includeDeprecatedValues:"
+ "hasIdenticalAssets:"
+ "init:assetSetIdentifier:assetSetAtomicInstance:"
+ "initWithAssetSet:ignoreMobileAssetStartup:configurationDirURLs:queue:updateHandler:"
+ "initWithUTF8String:"
+ "initWithUUID:assetSetName:atomicInstance:experiment:preinstalledAssetsSummary:bootUUID:"
+ "isBootUUIDCurrent"
+ "kern.bootsessionuuid"
+ "latestDownloadedAtomicInstanceFromPreSUStaging"
+ "nolock:"
+ "not downloaded"
+ "observeAssetSet:policies:queue:handler:"
+ "processIdIsLockingToken:statBuffer:error:"
+ "processIdsLockingToken:"
+ "rapidLock"
+ "refCount"
+ "setFromPreSoftwareUpdateStaging:"
+ "setRefCount:"
+ "shouldCheckAssetSet:autoAssetSet:changed:downloaded:locked:userInitiated:removalNeeded:"
+ "stageAssetSet:targets:"
+ "unlockableTokenError"
+ "updateAssetsForSubscribers:policies:queue:detailedProgress:completion:"
+ "updateAssetsForSubscribers:policies:queue:progress:detailedProgress:completion:storeManager:configurationManager:"
+ "v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v80@0:8@16@24@32@?40@?48@?56@64@72"
+ "vendingAtomicInstanceForConfiguredEntries"
- "%@: %@"
- "%s %{public}@: updateAssets for subscriber '%{public}@' with subscription '%{public}@'"
- "%s Auto asset set %{public}@ has expected specifiers %{public}@"
- "%s AutoAssetSet %{public}@ not provided, creating a new one for staging."
- "%s Can't unlock %@: already unlocked"
- "%s Could not create array from '%{public}@'"
- "%s Could not get auto asset type of auto asset set %{public}@: no config file found"
- "%s Downloading assets for subscriber: %{public}@ and subscription: %{public}@"
- "%s Failed to lock %@: %@"
- "%s Failed to unlock %@: %@"
- "%s Locked %@"
- "%s MA AutoAssetSet's downloadedCatalogCachedAssetSetID is nil for asset set - %{public}@"
- "%s No subscriptions for %{public}@ %{public}@: %{public}@"
- "%s Returning asset download status: %lu for subscriber: %{public}@ and subscription: %{public}@"
- "%s Returning status: %lu for subscriber: %{public}@ and subscription: %{public}@ as the asset set usages are nil"
- "%s Subscriptions for %{public}@ %{public}@: %{public}@"
- "%s Unlocked %@"
- "+[UAFAutoAssetManager configureAssetSet:specifiers:changed:]"
- "+[UAFAutoAssetManager getAutoAssetSet:specifiers:addEntries:configured:]"
- "+[UAFAutoAssetManager shouldCheckAssetSet:autoAssetSet:changed:locked:]"
- "+[UAFAutoAssetManager stageAssetSet:targets:autoAssetSet:]"
- "+[UAFAutoAssetSet catalogAssetSetID:]"
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
- "Asset Set Consistency Token %@ for assetSet %@ with atomic instance %@ (%@) experiment %@ preinstalledAssetsSummary %@"
- "B44@0:8@16@24B32^B36"
- "TB,N,V_locked"
- "assetSetIdForSELF:"
- "assetSetUsagesForStatusForSubscriber:subscriptionName:status:"
- "catalogAssetSetID:"
- "configureAssetSet:specifiers:changed:"
- "diskSpaceNeededForSubscriber:subscriptionName:storeManager:configurationManager:error:"
- "getAutoAssetSet:specifiers:addEntries:configured:"
- "getUsageAlias:"
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
