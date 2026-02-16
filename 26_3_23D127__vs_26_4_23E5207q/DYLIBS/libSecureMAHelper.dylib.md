## libSecureMAHelper.dylib

> `/usr/lib/libSecureMAHelper.dylib`

```diff

-1837.80.27.0.1
-  __TEXT.__text: 0x1f0ec
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0x530
-  __TEXT.__cstring: 0x75c0
-  __TEXT.__oslogstring: 0x2dc3
-  __TEXT.__gcc_except_tab: 0x9a0
-  __TEXT.__unwind_info: 0x588
-  __TEXT.__objc_classname: 0x98
-  __TEXT.__objc_methname: 0x1a90
+1837.100.235.0.0
+  __TEXT.__text: 0x1f004
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x55c
+  __TEXT.__const: 0x500
+  __TEXT.__cstring: 0x6bb7
+  __TEXT.__oslogstring: 0x2cf6
+  __TEXT.__gcc_except_tab: 0x964
+  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__objc_classname: 0x80
+  __TEXT.__objc_methname: 0x1908
   __TEXT.__objc_methtype: 0x250
-  __TEXT.__objc_stubs: 0x1ea0
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__const: 0xf50
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__objc_stubs: 0x1e00
+  __DATA_CONST.__got: 0x2b8
+  __DATA_CONST.__const: 0xc40
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x880
-  __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x678
-  __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0x8000
-  __AUTH_CONST.__objc_const: 0x848
-  __AUTH_CONST.__objc_intobj: 0x8d0
+  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0x2e0
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__const: 0x430
+  __AUTH_CONST.__cfstring: 0x76e0
+  __AUTH_CONST.__objc_const: 0x6e8
+  __AUTH_CONST.__objc_intobj: 0x948
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x44
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x38
   __DATA.__data: 0xb8
-  __DATA.__bss: 0x258
+  __DATA.__bss: 0x1f8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0349D1E0-C1EE-3004-917C-0B78314C09C3
-  Functions: 467
-  Symbols:   1592
-  CStrings:  2650
+  UUID: C0116241-8872-31E9-B86D-87E9D97B2C4A
+  Functions: 423
+  Symbols:   1379
+  CStrings:  2481
 
Symbols:
+ GCC_except_table112
+ _MAPreferencesCopyNSStringValue
+ _MAPreferencesCopyValue
+ _MAPreferencesGetAppBooleanValue
+ _MAPreferencesIsCentralizedCacheDeleteEnabled
+ _MAPreferencesIsInternalAllowed
+ _MAPreferencesIsVerboseLoggingEnabled
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1263
+ ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.479
+ ___block_literal_global.1209
+ ___block_literal_global.1215
+ ___block_literal_global.1253
+ ___block_literal_global.1255
+ ___block_literal_global.1259
+ ___block_literal_global.1264
+ ___block_literal_global.1269
+ ___block_literal_global.1274
+ ___block_literal_global.1279
+ ___block_literal_global.1298
+ ___block_literal_global.1391
+ ___block_literal_global.1513
+ ___block_literal_global.1519
+ ___block_literal_global.1524
+ ___block_literal_global.1535
+ ___block_literal_global.1540
+ ___block_literal_global.1562
+ ___block_literal_global.1698
+ ___block_literal_global.2253
+ ___block_literal_global.2927
+ ___block_literal_global.2929
+ ___block_literal_global.2931
+ ___block_literal_global.2933
+ ___block_literal_global.2935
+ ___block_literal_global.2974
+ ___block_literal_global.2987
+ _doesEnvironmentSupportBackgroundTasks
+ _getStringValue
+ _isAutoCatalogTaskDescriptor
+ _matchPreferenceFromMADefaults
+ _objc_msgSend$commonPrefixWithString:options:
+ _objc_retainAutoreleasedReturnValue
+ _os_variant_uses_ephemeral_storage
+ _stringForTaskDescriptorType
- +[MAAssetTypeDescriptor _assetTypeDescriptors]
- +[MAAssetTypeDescriptor _assetTypeDescriptors].cold.1
- +[MAAssetTypeDescriptor _loadDescriptorsFromPath:intoDictionary:]
- +[MAAssetTypeDescriptor _secureAssetTypeDescriptors]
- +[MAAssetTypeDescriptor _secureAssetTypeDescriptors].cold.1
- +[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]
- +[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]
- +[MAAssetTypeDescriptor descriptorForAssetType:]
- +[MAAssetTypeDescriptor typeDescriptorsToDataVault]
- +[MAAssetTypeDescriptor typeDescriptorsToRemoveV1Assets]
- -[MAAssetTypeDescriptor .cxx_destruct]
- -[MAAssetTypeDescriptor assetProperties]
- -[MAAssetTypeDescriptor assetSpecifiers]
- -[MAAssetTypeDescriptor assetType]
- -[MAAssetTypeDescriptor description]
- -[MAAssetTypeDescriptor initWithAssetType:]
- -[MAAssetTypeDescriptor isSecure]
- -[MAAssetTypeDescriptor shouldMakeDataVault]
- -[MAAssetTypeDescriptor shouldRemoveV1Assets]
- GCC_except_table111
- _CFPreferencesAppSynchronize
- _CFPreferencesCopyAppValue
- _MAAssetTypeDescriptorKeyAssetSpecifiers
- _MAAssetTypeDescriptorKeyAssetType
- _MAAssetTypeDescriptorKeyMakeDataVault
- _MAAssetTypeDescriptorKeyMobileAssetProperties
- _MAAssetTypeDescriptorKeyRemoveV1Assets
- _MABrainUtilityAllowDownloadedBrain
- _MABrainUtilitySupportsGracefulUngraft
- _NSURLIsRegularFileKey
- _OBJC_IVAR_$_MAAssetTypeDescriptor._assetType
- _OBJC_IVAR_$_MAAssetTypeDescriptor._isSecure
- _OBJC_IVAR_$_MAAssetTypeDescriptor._typeDescriptor
- _OBJC_METACLASS_$_MAAssetTypeDescriptor
- _OUTLINED_FUNCTION_2
- __MAPreferencesCopyNSStringValue
- __MAPreferencesCopyValue
- __MAPreferencesGetAppBooleanValue
- __MAPreferencesIsCentralizedCacheDeleteEnabled
- __MAPreferencesIsCentralizedCacheDeleteEnabled._centralizedCacheDeleteEnabled
- __MAPreferencesIsCentralizedCacheDeleteEnabled.cold.1
- __MAPreferencesIsCentralizedCacheDeleteEnabled.onceToken
- __MAPreferencesIsInternalAllowed
- __MAPreferencesIsInternalAllowed._isAppleInternal
- __MAPreferencesIsInternalAllowed.cold.1
- __MAPreferencesIsInternalAllowed.onceToken
- __MAPreferencesIsVerboseLoggingEnabled
- __MAPreferencesIsVerboseLoggingEnabled._verboseLoggingEnabled
- __MAPreferencesIsVerboseLoggingEnabled.cold.1
- __MAPreferencesIsVerboseLoggingEnabled.onceToken
- __OBJC_$_CLASS_METHODS_MAAssetTypeDescriptor
- __OBJC_$_INSTANCE_METHODS_MAAssetTypeDescriptor
- __OBJC_$_INSTANCE_VARIABLES_MAAssetTypeDescriptor
- __OBJC_$_PROP_LIST_MAAssetTypeDescriptor
- __OBJC_CLASS_RO_$_MAAssetTypeDescriptor
- __OBJC_METACLASS_RO_$_MAAssetTypeDescriptor
- ___46+[MAAssetTypeDescriptor _assetTypeDescriptors]_block_invoke
- ___52+[MAAssetTypeDescriptor _secureAssetTypeDescriptors]_block_invoke
- ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke
- ___60+[MAAssetTypeDescriptor _typeDescriptorsMatchingBooleanKey:]_block_invoke_2
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1179
- ___79+[MAAssetTypeDescriptor _typeDescriptorDictionaryForAssetType:typeDescriptors:]_block_invoke
- ___MABrainUtilityScheduleDeviceUnlockAction_block_invoke.416
- ____MAPreferencesCopyValue_block_invoke
- ____MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke
- ____MAPreferencesIsCentralizedCacheDeleteEnabled_block_invoke.cold.1
- ____MAPreferencesIsInternalAllowed_block_invoke
- ____MAPreferencesIsVerboseLoggingEnabled_block_invoke
- ____MAPreferencesIsVerboseLoggingEnabled_block_invoke.cold.1
- ____preferencesDomainProtectionDispatchQueue_block_invoke
- ___block_descriptor_48_e8_32s40r_e29_v32?08"NSDictionary"16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e22_v16?0"NSDictionary"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8s40l8
- ___block_literal_global.1125
- ___block_literal_global.1131
- ___block_literal_global.1148
- ___block_literal_global.1169
- ___block_literal_global.1171
- ___block_literal_global.1175
- ___block_literal_global.1180
- ___block_literal_global.1185
- ___block_literal_global.1190
- ___block_literal_global.1195
- ___block_literal_global.1214
- ___block_literal_global.1307
- ___block_literal_global.1381
- ___block_literal_global.1386
- ___block_literal_global.1388
- ___block_literal_global.1432
- ___block_literal_global.1438
- ___block_literal_global.1443
- ___block_literal_global.1454
- ___block_literal_global.1459
- ___block_literal_global.1481
- ___block_literal_global.1614
- ___block_literal_global.2169
- ___block_literal_global.2822
- ___block_literal_global.2824
- ___block_literal_global.2826
- ___block_literal_global.2828
- ___block_literal_global.2830
- ___block_literal_global.2869
- ___block_literal_global.2873
- __assetTypeDescriptors.assetTypeDescriptors
- __assetTypeDescriptors.onceToken
- __preferencesDomainProtectionDispatchQueue
- __preferencesDomainProtectionDispatchQueue.cold.1
- __preferencesDomainProtectionDispatchQueue.preferencesDomainQueue
- __preferencesDomainProtectionDispatchQueue.preferencesDomainQueueOnce
- __secureAssetTypeDescriptors.onceToken
- __secureAssetTypeDescriptors.secureAssetTypeDescriptors
- _dispatch_sync
- _kMobileAssetPreferencesAnalyticsClearOnLaunch
- _kMobileAssetPreferencesAnalyticsClientNameTestToolOverride
- _kMobileAssetPreferencesAnalyticsClientNameTestToolPrepend
- _kMobileAssetPreferencesAnalyticsLevelOnLaunch
- _kMobileAssetPreferencesAnalyticsSendImmediate
- _kMobileAssetPreferencesAnalyticsSubmitOnLaunch
- _kMobileAssetPreferencesAutoAssetActivityAggressiveAssetType
- _kMobileAssetPreferencesAutoAssetActivityAggressiveIntervalSecs
- _kMobileAssetPreferencesAutoAssetActivityHeightenedAssetType
- _kMobileAssetPreferencesAutoAssetActivityHeightenedIntervalSecs
- _kMobileAssetPreferencesAutoAssetActivityIntervalSecs
- _kMobileAssetPreferencesAutoAssetActivityTickerSecs
- _kMobileAssetPreferencesAutoAssetAlwaysPromoteStagedAssets
- _kMobileAssetPreferencesAutoAssetAsIfBackground
- _kMobileAssetPreferencesAutoAssetAsIfBootedOSIsBuildVersion
- _kMobileAssetPreferencesAutoAssetAsIfBootedOSIsOSVersion
- _kMobileAssetPreferencesAutoAssetAsIfRamp
- _kMobileAssetPreferencesAutoAssetBeforeFirstDefaultTimeoutSecs
- _kMobileAssetPreferencesAutoAssetBeforeFirstPollSecs
- _kMobileAssetPreferencesAutoAssetConnectorBackoffRetryTimes
- _kMobileAssetPreferencesAutoAssetConnectorInitialWaitSecs
- _kMobileAssetPreferencesAutoAssetConnectorWaitBeforeRetrySecs
- _kMobileAssetPreferencesAutoAssetLogSetCompare
- _kMobileAssetPreferencesAutoAssetLookupCacheAssetSelectorValidSecs
- _kMobileAssetPreferencesAutoAssetLookupCacheSetConfigurationValidSecs
- _kMobileAssetPreferencesAutoAssetMaxStagerDeterminingSecs
- _kMobileAssetPreferencesAutoAssetNoPersistedOverflowLimit
- _kMobileAssetPreferencesAutoAssetObserverIgnoreNetworkStatus
- _kMobileAssetPreferencesAutoAssetPerformanceLoggingEnabled
- _kMobileAssetPreferencesAutoAssetPersistedTableLoggingEnabled
- _kMobileAssetPreferencesAutoAssetPushActivityIntervalSecs
- _kMobileAssetPreferencesAutoAssetScheduledAlwaysNonDiscretionary
- _kMobileAssetPreferencesAutoAssetScheduledAsIfNotInternal
- _kMobileAssetPreferencesAutoAssetScheduledBackupTriggersDisabled
- _kMobileAssetPreferencesAutoAssetScheduledOnlyForAssetTypes
- _kMobileAssetPreferencesAutoAssetSecureSimulateFailureAll
- _kMobileAssetPreferencesAutoAssetSecureSimulateGraftFailure
- _kMobileAssetPreferencesAutoAssetSecureSimulateRequireAll
- _kMobileAssetPreferencesAutoAssetSessionIDBase
- _kMobileAssetPreferencesAutoAssetSimulatedDownloadFailureResult
- _kMobileAssetPreferencesAutoAssetSimulatedStagingLookupFailureResult
- _kMobileAssetPreferencesAutoAssetStagerDetermineLastRequiredTimesOut
- _kMobileAssetPreferencesAutoAssetStagerDeterminePallasResponseFewer
- _kMobileAssetPreferencesAutoAssetStagerDownloadFirstNotInCatalog
- _kMobileAssetPreferencesAutoAssetStagerFilesystemMaxMegabytes
- _kMobileAssetPreferencesAutoAssetStagerInjectAvailableDups
- _kMobileAssetPreferencesAutoAssetStagerInjectAvailableOlderVersions
- _kMobileAssetPreferencesAutoAssetStagingLookupFlipRequiredOptional
- _kMobileAssetPreferencesAutoAssetStartupSimulateFirstBoot
- _kMobileAssetPreferencesAutoAssetSuspendResumeEnabled
- _kMobileAssetPreferencesAutoAssetSuspendResumeForSUSetsOverride
- _kMobileAssetPreferencesAutoAssetSuspendResumeTimeoutCancelOverride
- _kMobileAssetPreferencesAutoAssetSuspendResumeTimeoutEvictOverride
- _kMobileAssetPreferencesAutoHealthReportSetNames
- _kMobileAssetPreferencesAutoStartupHealthReport
- _kMobileAssetPreferencesDefaultNumberOfSecsGC
- _kMobileAssetPreferencesDomain
- _kMobileAssetPreferencesEnableCentralizedCacheDelete
- _kMobileAssetPreferencesEnableVerboseLogging
- _kMobileAssetPreferencesFakeAvailableSpaceInBytesForSpaceCheck
- _kMobileAssetPreferencesForceAutoCacheDelete
- _kMobileAssetPreferencesForceBatteryAllowedDownload
- _kMobileAssetPreferencesForceBeforeFirstUnlock
- _kMobileAssetPreferencesForceInProcessDownloads
- _kMobileAssetPreferencesForceNonDiscretionaryDownload
- _kMobileAssetPreferencesGarbageCollectionAlterAssetType
- _kMobileAssetPreferencesGarbageCollectionAlterBehavior
- _kMobileAssetPreferencesGarbageCollectionCurrentTimeDeltaSecs
- _kMobileAssetPreferencesMABrainForceStartupBusy
- _kMobileAssetPreferencesPallasTimeout
- _kMobileAssetPreferencesPreciousNumberOfSecsGC
- _kMobileAssetPreferencesReclaimStatOnlyForAssetTypes
- _kMobileAssetPreferencesSplunkTimeout
- _kMobileAssetPreferencesSupportedFeaturesOverride
- _kMobileAssetPreferencesTestMABrainReplaceAllowed
- _kMobileAssetPreferencesThirdPartyStagingBucketPathComponent
- _kMobileAssetPreferencesThirdPartyStagingPathComponent
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:
- _objc_msgSend$dictionaryWithContentsOfURL:
- _objc_msgSend$getResourceValue:forKey:error:
- _objc_msgSend$initWithAssetType:
- _objc_msgSend$isSecure
- _objc_msgSend$stringByDeletingPathExtension
- _objc_opt_self
- _objc_retainAutoreleaseReturnValue
- _objc_retainBlock
- _objc_retain_x1
- _objc_retain_x4
- _syncPreferences
CStrings:
+ ".*"
+ "<undefined>"
+ "Download failed due to a server redirect to a nonexistent location."
+ "Download failed due to invalid asset receipts in response from live asset server."
+ "Exact Match"
+ "Failed to get key: %{public}s due to not being present"
+ "Failed to graft/mount asset at %@: %@\n"
+ "ServiceConnect"
+ "Successfully %@ asset at %@\n"
+ "TASK_DESCRIPTOR_ASSET"
+ "TASK_DESCRIPTOR_AUTO_ASSET"
+ "TASK_DESCRIPTOR_AUTO_CATALOG"
+ "TASK_DESCRIPTOR_INVALID"
+ "TASK_DESCRIPTOR_MAX"
+ "TASK_DESCRIPTOR_PMV"
+ "TASK_DESCRIPTOR_XML"
+ "UsageRequiresDaemonRestart"
+ "UsageRequiresDeviceUnlock"
+ "UsageRequiresRepersonalization"
+ "UsageRequiresRescan"
+ "Wildcard Match with key %@"
+ "commonPrefixWithString:options:"
+ "grafted"
+ "mounted"
+ "{getStringValue} invalid type for input:%{public}@ | expecting string or number or boolean"
- "/System/Library/AssetTypeDescriptors/"
- "/System/Library/SecureAssetTypeDescriptors/"
- "<MAAssetTypeDescriptor: %p>: (AssetType: %@, Secure: %d)"
- "AnalyticsClearOnLaunch"
- "AnalyticsClientNameTestToolOverride"
- "AnalyticsClientNameTestToolPrepend"
- "AnalyticsLevelOnLaunch"
- "AnalyticsSendImmediate"
- "AnalyticsSubmitOnLaunch"
- "Asset Specifiers"
- "Asset Type"
- "AutoAssetActivityAggressiveAssetType"
- "AutoAssetActivityAggressiveIntervalSecs"
- "AutoAssetActivityHeightenedAssetType"
- "AutoAssetActivityHeightenedIntervalSecs"
- "AutoAssetActivityIntervalSecs"
- "AutoAssetActivityTickerSecs"
- "AutoAssetAlwaysPromoteStagedAssets"
- "AutoAssetAsIfBackground"
- "AutoAssetAsIfBootedOSIsBuildVersion"
- "AutoAssetAsIfBootedOSIsOSVersion"
- "AutoAssetAsIfRamp"
- "AutoAssetBeforeFirstDefaultTimeoutSecs"
- "AutoAssetBeforeFirstPollSecs"
- "AutoAssetConnectorBackoffRetryTimes"
- "AutoAssetConnectorInitialWaitSecs"
- "AutoAssetConnectorWaitBeforeRetrySecs"
- "AutoAssetLogSetCompare"
- "AutoAssetLookupCacheAssetSelectorValidSecs"
- "AutoAssetLookupCacheSetConfigurationValidSecs"
- "AutoAssetMaxStagerDeterminingSecs"
- "AutoAssetNoPersistedOverflowLimit"
- "AutoAssetObserverIgnoreNetworkStatus"
- "AutoAssetPerformanceLoggingEnabled"
- "AutoAssetPersistedTableLoggingEnabled"
- "AutoAssetPushActivityIntervalSecs"
- "AutoAssetScheduledAlwaysNonDiscretionary"
- "AutoAssetScheduledAsIfNotInternal"
- "AutoAssetScheduledBackupTriggersDisabled"
- "AutoAssetScheduledOnlyForAssetTypes"
- "AutoAssetSecureSimulateFailureAll"
- "AutoAssetSecureSimulateGraftFailure"
- "AutoAssetSecureSimulateRequireAll"
- "AutoAssetSessionIDBase"
- "AutoAssetSimulatedDownloadFailureResult"
- "AutoAssetSimulatedStagingLookupFailureResult"
- "AutoAssetStagerDetermineLastRequiredTimesOut"
- "AutoAssetStagerDeterminePallasResponseFewer"
- "AutoAssetStagerDownloadFirstNotInCatalog"
- "AutoAssetStagerFilesystemMaxMegabytes"
- "AutoAssetStagerInjectAvailableDups"
- "AutoAssetStagerInjectAvailableOlderVersions"
- "AutoAssetStagingLookupFlipRequiredOptional"
- "AutoAssetStartupSimulateFirstBoot"
- "AutoAssetSuspendResumeForSUEnabled"
- "AutoAssetSuspendResumeForSUSetsOverride"
- "AutoAssetSuspendResumeTimeoutCancelOverride"
- "AutoAssetSuspendResumeTimeoutEvictOverride"
- "AutoHealthReportSets"
- "AutoStartupHealthReport"
- "BrainVersion"
- "Downlaod failed due to a server redirect to a nonexistent location."
- "Download failed due to invalid asset reciepts in response from live asset server."
- "EnableCentralizedCacheDelete"
- "EnableVerboseLogging"
- "FailPersonalizationConfig"
- "Failed to get key: %{public}s due to not beinng present"
- "Failed to graft asset at %@: %@\n"
- "Failed to load asset descriptors from path %{public}@. %@"
- "FakeAvailableSpaceInBytesForSpaceCheck"
- "FakeDeviceOSBuildVersion"
- "FakeDeviceRecoveryMode"
- "ForceAutoCacheDelete"
- "ForceBatteryAllowedDownload"
- "ForceBeforeFirstUnlock"
- "ForceNonDiscretionaryDownload"
- "GarbageCollectionAlterAssetType"
- "GarbageCollectionAlterBehavior"
- "GarbageCollectionCurrentTimeDeltaSecs"
- "LBJfwOEzExRxzlAnSuI7eg"
- "MAAssetTypeDescriptor"
- "MABrainAllowDownloaded"
- "MABrainForceStartupBusy"
- "Make Repository Data Vault"
- "NO"
- "PallasTimeout"
- "ReclaimStatOnlyForAssetTypes"
- "RemoveV1Assets"
- "SplunkTimeout"
- "Successfully grafted asset at %@\n"
- "SupportedFeaturesOverride"
- "T@\"NSArray\",R,D,N"
- "T@\"NSDictionary\",R,D,N"
- "T@\"NSString\",R,N,V_assetType"
- "TB,R,D,N"
- "TB,R,N,V_isSecure"
- "TestMABrainReplaceAllowed"
- "ThirdPartyStagingBucketPathComponent"
- "ThirdPartyStagingPathComponent"
- "YES"
- "[MA_PREFS] {%{public}@} [%{public}@] Could not synchronize preferences for %{public}@ - this may be a permissions error"
- "[MA_PREFS] {_MAPreferencesCopyNSStringValue} invalid type for key:%{public}@ | expecting string or number or boolean"
- "_isSecure"
- "assetProperties"
- "assetSpecifiers"
- "com.apple.MobileAsset.preferencesDomain"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "defaultNumberOfSecsGC"
- "dictionaryWithContentsOfURL:"
- "forceInProcessDownloads"
- "getResourceValue:forKey:error:"
- "initWithAssetType:"
- "isSecure"
- "preciousNumberOfSecsGC"
- "shouldMakeDataVault"
- "shouldRemoveV1Assets"
- "stringByDeletingPathExtension"
- "typeDescriptorsToDataVault"
- "typeDescriptorsToRemoveV1Assets"
- "v16@?0@\"NSDictionary\"8"
- "v32@?0@8@\"NSDictionary\"16^B24"

```
