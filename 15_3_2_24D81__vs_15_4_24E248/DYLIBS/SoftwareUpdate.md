## SoftwareUpdate

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate`

```diff

-2078.80.2.0.2
-  __TEXT.__text: 0x82614
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x5bc0
-  __TEXT.__const: 0x680
-  __TEXT.__gcc_except_tab: 0x13bc
-  __TEXT.__cstring: 0x83aa
-  __TEXT.__oslogstring: 0xb7b0
+2078.101.1.0.0
+  __TEXT.__text: 0x83714
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_methlist: 0x653c
+  __TEXT.__const: 0x670
+  __TEXT.__gcc_except_tab: 0x135c
+  __TEXT.__cstring: 0x8628
+  __TEXT.__oslogstring: 0xb730
   __TEXT.__dof_SoftwareU: 0xc9e
-  __TEXT.__unwind_info: 0x2158
-  __TEXT.__objc_classname: 0x873
-  __TEXT.__objc_methname: 0x117bc
-  __TEXT.__objc_methtype: 0x1cd3
-  __TEXT.__objc_stubs: 0xc0e0
-  __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0xa60
-  __DATA_CONST.__objc_classlist: 0x248
-  __DATA_CONST.__objc_catlist: 0x48
+  __TEXT.__unwind_info: 0x2200
+  __TEXT.__eh_frame: 0x48
+  __TEXT.__objc_classname: 0x875
+  __TEXT.__objc_methname: 0x119c2
+  __TEXT.__objc_methtype: 0x1cd4
+  __TEXT.__objc_stubs: 0xc2c0
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__const: 0xa80
+  __DATA_CONST.__objc_classlist: 0x240
+  __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3de0
+  __DATA_CONST.__objc_selrefs: 0x3f70
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x828
-  __AUTH_CONST.__const: 0x2a40
-  __AUTH_CONST.__cfstring: 0x7420
-  __AUTH_CONST.__objc_const: 0x9e18
+  __AUTH_CONST.__auth_got: 0x848
+  __AUTH_CONST.__const: 0x2a60
+  __AUTH_CONST.__cfstring: 0x75c0
+  __AUTH_CONST.__objc_const: 0x8bc8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0xc0
-  __AUTH.__objc_data: 0x16d0
-  __DATA.__objc_ivar: 0x7e4
+  __AUTH.__objc_data: 0x1680
+  __DATA.__objc_ivar: 0x7b8
   __DATA.__data: 0x5c8
-  __DATA.__bss: 0x270
+  __DATA.__bss: 0x280
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: C1B7BF9E-2B81-3002-B869-64EABA4CAEE4
-  Functions: 3155
-  Symbols:   7070
-  CStrings:  6004
+  UUID: 8CCF9767-E200-3F52-AB79-FC7F8953C6E2
+  Functions: 3207
+  Symbols:   7141
+  CStrings:  6050
 
Symbols:
+ +[SUAdminInstallController sharedAdminInstallController].cold.1
+ +[SUAppStoreUpdate _connectToService].cold.2
+ +[SUAppStoreUpdateController sharedUpdateController].cold.1
+ +[SUBackgroundManager sharedBackgroundManager].cold.1
+ +[SUBootPolicyUtil sharedInstance].cold.1
+ +[SUCatalog initialize].cold.1
+ +[SUCatalogDataManager sharedCatalogDataManager].cold.1
+ +[SUDownloadCache defaultCache].cold.1
+ +[SUDownloadCache getCacheQueue].cold.1
+ +[SUHelperProxy sharedHelperProxy].cold.1
+ +[SUInstallOperation _isCurrentlyStagedWithLocalProducts:purgeableSize:].cold.1
+ +[SUInstalledUpdateJournal sharedJournal].cold.1
+ +[SUOSNotificationBundleHandler sharedNotificationBundleHandler].cold.1
+ +[SUOSUDDMConfiguration sharedInstance]
+ +[SUOSUDDMConfiguration sharedInstance].cold.1
+ +[SUProductManager defaultManager].cold.1
+ +[SUScanController sharedScanController].cold.1
+ +[SUSharedAuthenticationHandler sharedAuthenticationHandler].cold.1
+ +[SUSharedPrefs isAppleInternal].cold.1
+ +[SUSharedPrefs isCustomBaseSystemAllowed].cold.1
+ +[SUSignedFlatPkg verifyPackageAtPath:minimumTrust:error:].cold.2
+ +[SUTelemetryEventFormatter formatBool:]
+ +[SUTelemetryEventFormatter formatDate:]
+ +[SUTelemetryEventFormatter formatDouble:]
+ +[SUTelemetryEventFormatter formatInteger:]
+ +[SUTelemetryEventFormatter formatResult:]
+ +[SUTelemetryEventFormatter formatUnsignedLongLong:]
+ +[SUTelemetryEventFormatter formatValuesInDict:]
+ +[SUTelemetryEventFormatter roundToMB:]
+ +[SUTelemetryManager advancedPreferencesEvent]
+ +[SUTelemetryManager downloadEvent]
+ +[SUTelemetryManager installEvent]
+ +[SUTelemetryManager preferencesEvent]
+ +[SUTelemetryManager scanEvent]
+ +[SUTestDefaults sharedDefaults].cold.1
+ +[SUUpdateServiceDaemon sharedUpdateServiceDaemon].cold.1
+ +[SUUpdateSession sharedUpdateSession].cold.1
+ +[SUUtilities cacheDeletePurgeableSpace]
+ +[SUUtilities createCacheDeleteInfoDictionaryWithUrgencyLevel:spaceToPurge:]
+ +[SUUtilities systemIsAPFS].cold.1
+ +[SUUtilities systemIsMemberOfReadOnlySystemGroup].cold.1
+ -[NSPredicate(SU_Sanitization) _su_allExpressions]
+ -[NSPredicate(SU_Sanitization) _su_containsBlockOrFunctionPredicatesOrExpressions]
+ -[SUAppStoreUpdateController _clearUserSideStashCredentials].cold.6
+ -[SUAppStoreUpdateController _setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]
+ -[SUAppStoreUpdateController fetchMajorProductForUpdate:withCompletionHandler:].cold.2
+ -[SUBackgroundManager synchronousRefreshAvailableUpdatesIfRequired]
+ -[SUCatalogPackageSource registerProduct:].cold.2
+ -[SUDeferredUpdateManager sharedDeferredUpdateManager].cold.1
+ -[SUDownloader _suPackageReferencesToContentCachingRefs:].cold.1
+ -[SUHelperProxy cacheDeletePurgeableSpace]
+ -[SUHelperProxy prepareForLogoutAndInstall]
+ -[SUInstallOperation _initWithLocalProducts:stageOnly:spaceRequired:].cold.1
+ -[SUInstallOperation _initWithLocalProducts:stageOnly:spaceRequired:].cold.2
+ -[SUInstallOperation main].cold.2
+ -[SUInstallOperation main].cold.3
+ -[SUInstallOperation main].cold.4
+ -[SUInstallOperation performPreflightChecks].cold.1
+ -[SUOSUDDMConfiguration ddmConfiguration]
+ -[SUOSUDDMConfiguration dealloc]
+ -[SUOSUDDMConfiguration init]
+ -[SUOSUDDMConfiguration setDdmConfiguration:]
+ -[SUPowerAssertionManager createUserActivityAssertionWithDescription:timeout:]
+ -[SUPowerAssertionManager createUserActivityAssertionWithDescription:timeout:].cold.1
+ -[SUPreferenceManager isMacOSAutoUpdateManaged]
+ -[SUProduct invalidatePackageIdentifierInCache:].cold.1
+ -[SUProduct packageInfoForPackageRefURL:].cold.1
+ -[SUProduct packageIntegrityInformationForRefURL:].cold.1
+ -[SUProduct packageReferenceForPackageIdentifier:].cold.1
+ -[SUProduct setIntegrityInformation:preserveOriginalData:].cold.1
+ -[SUProduct setPKMDataByPackageURL:preserveOriginalData:].cold.1
+ -[SUProductStub dealloc]
+ -[SUProductStubImpl dealloc]
+ -[SUSharedPrefs ddmConfiguration]
+ -[SUSharedPrefs dealloc]
+ -[SUSharedPrefs setDdmConfiguration:]
+ -[SUSharedPrefs(AnyUserPrefs) _daysToSeconds:]
+ -[SUSharedPrefs(AnyUserPrefs) _firstOfferDates]
+ -[SUSharedPrefs(AnyUserPrefs) appCloseNotificationDelay]
+ -[SUSharedPrefs(AnyUserPrefs) fakeMaxPreSUStagingSize]
+ -[SUSharedPrefs(AnyUserPrefs) fakeMobileAssetEstimateBytesReclaimedSuccess]
+ -[SUSharedPrefs(AnyUserPrefs) firstInstallTonightDateForProductKey:]
+ -[SUSharedPrefs(AnyUserPrefs) firstInstallTonightDatesByProductKey]
+ -[SUSharedPrefs(AnyUserPrefs) firstOfferDateForProductKey:]
+ -[SUSharedPrefs(AnyUserPrefs) globalSettings]
+ -[SUSharedPrefs(AnyUserPrefs) majorOSDeferralPeriod]
+ -[SUSharedPrefs(AnyUserPrefs) majorOSDeferralPeriod].cold.1
+ -[SUSharedPrefs(AnyUserPrefs) majorOSDeferralPeriod].cold.2
+ -[SUSharedPrefs(AnyUserPrefs) minorOSDeferralPeriod]
+ -[SUSharedPrefs(AnyUserPrefs) minorOSDeferralPeriod].cold.1
+ -[SUSharedPrefs(AnyUserPrefs) minorOSDeferralPeriod].cold.2
+ -[SUSharedPrefs(AnyUserPrefs) nonOSDeferralPeriod]
+ -[SUSharedPrefs(AnyUserPrefs) nonOSDeferralPeriod].cold.1
+ -[SUSharedPrefs(AnyUserPrefs) nonOSDeferralPeriod].cold.2
+ -[SUSharedPrefs(AnyUserPrefs) setFirstInstallTonightDateForProductKey:]
+ -[SUSharedPrefs(AnyUserPrefs) setFirstOfferDateForProductKey:]
+ -[SUSharedPrefs(AnyUserPrefs) updatesAvailableNotificationDelay]
+ -[SUSharedPrefs(ScanStatus) lastLoginWindowHarvestDate]
+ -[SUSharedPrefs(ScanStatus) lastLoginWindowHarvestMethod]
+ -[SUSharedPrefs(ScanStatus) lastSuccessfulMSUBackgroundScanDate]
+ -[SUSharedPrefs(ScanStatus) setLastLoginWindowHarvestDate:]
+ -[SUSharedPrefs(ScanStatus) setLastLoginWindowHarvestMethod:]
+ -[SUSharedPrefs(ScanStatus) setLastSuccessfulMSUBackgroundScanDate:]
+ -[SUTelemetryDownloadEvent dealloc]
+ -[SUTelemetryInstallEvent dealloc]
+ -[SUTelemetryManager dealloc]
+ -[SUTelemetryScanEvent dealloc]
+ -[SUUpdateServiceDaemon _runBackgroundActionsOnCurrentQueueIfAppropriate:]
+ GCC_except_table103
+ GCC_except_table115
+ GCC_except_table137
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table152
+ GCC_except_table156
+ GCC_except_table163
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table96
+ OBJC_IVAR_$_SUOSUDDMConfiguration._ddmConfiguration
+ OBJC_IVAR_$_SUSharedPrefs._ddmConfiguration
+ SUError.cold.1
+ SUErrorSetCurrentUpdateServerName.cold.1
+ SUMessageTracerUniqueID.cold.1
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _IOPMAssertionCreateWithProperties
+ _NSOpenStepRootDirectory
+ _OBJC_CLASS_$_LPStaticAPFSVolume
+ _OBJC_CLASS_$_LPStaticMedia
+ _OBJC_CLASS_$_NSBlockPredicate
+ _OBJC_CLASS_$_NSComparisonPredicate
+ _OBJC_CLASS_$_NSCompoundPredicate
+ _OBJC_CLASS_$_SUCorePolicyDDMConfiguration
+ _OBJC_CLASS_$_SUOSUDDMConfiguration
+ _OBJC_METACLASS_$_SUOSUDDMConfiguration
+ _SULoginWindowCookiePath
+ _SUOSUkDDMStatePersistencePath
+ _SUTelemetryPayloadKeyLastLoginWindowHarvestMethod
+ _SUTelemetryPayloadKeyMinutesSinceLastHarvest
+ _SUTelemetryPayloadKeyMinutesSinceLastLoginWindowHarvest
+ _SUTelemetryPayloadKeyStashState
+ __107-[SUAppStoreUpdateController _setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke.100
+ __107-[SUAppStoreUpdateController _setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke.cold.1
+ __107-[SUAppStoreUpdateController _setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke_2.105
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.189
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.199
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.200
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.200.cold.1
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.200.cold.2
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.201
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.203
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.203.cold.1
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.204
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.205
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.205.cold.1
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.211.cold.1
+ __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke_2.213
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.140
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.147.cold.1
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.148
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.153
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.155.cold.1
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.156
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke_2.141
+ __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke_2.154
+ __32-[SUAppStoreUpdate _setProduct:]_block_invoke.cold.1
+ __34-[SUAppStoreUpdateController init]_block_invoke.45
+ __41-[SUAppStoreUpdateController _connection]_block_invoke.62
+ __49-[SUAppStoreUpdateController _authorizeIfNeeded:]_block_invoke.186
+ __50-[SUAppStoreUpdateController installUpdatesLater:]_block_invoke.234
+ __52-[SUAppStoreUpdateController installedUpdateJournal]_block_invoke.166
+ __55-[SUAppStoreUpdateController updatesToBeInstalledLater]_block_invoke.247
+ __58-[SUAppStoreUpdateController diskSpaceRequiredForUpdates:]_block_invoke.178
+ __61-[SUAppStoreUpdateController updatesToBeInstalledAfterLogout]_block_invoke.231
+ __62-[SUAppStoreUpdateController removeAllUpdatesFromInstallLater]_block_invoke.240
+ __63-[SUAppStoreUpdateController __queryForAvailableUpdatesHelper:]_block_invoke.114
+ __63-[SUAppStoreUpdateController authChallengeWasReceived:handled:]_block_invoke.294
+ __67-[SUAppStoreUpdateController installedUpdateJournalPrunedAndSorted]_block_invoke.172
+ __67-[SUBackgroundManager synchronousRefreshAvailableUpdatesIfRequired]_block_invoke.71
+ __69-[SUAppStoreUpdateController isDownloadRequiredForPostLogoutUpdates:]_block_invoke.220
+ __79-[SUAppStoreUpdateController _retrieveCatalogInformationWithCompletionHandler:]_block_invoke.159
+ __79-[SUAppStoreUpdateController fetchMajorProductForUpdate:withCompletionHandler:]_block_invoke.87
+ __82-[SUAppStoreUpdateController(SoftwareUpdatePrefPane) cancelUpdatesForProductKeys:]_block_invoke.488
+ __83-[SUAppStoreUpdateController(SoftwareUpdatePrefPane) combinedStatusForProductKeys:]_block_invoke.483
+ __84-[SUAppStoreUpdateController registerRequestsToInstallAfterPostLogoutUpdates:error:]_block_invoke.271
+ __85-[SUAppStoreUpdateController installUpdatesAfterNextLogout:restartingNow:nowIsLater:]_block_invoke.229
+ __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke.131
+ __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke.133
+ __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke_2.132
+ __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke_2.132.cold.1
+ __95-[SUAppStoreUpdateController(SoftwareUpdatePrefPane) productKeysInActiveForegroundTransactions]_block_invoke.480
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSPredicate_$_SU_Sanitization
+ __OBJC_$_CATEGORY_NSPredicate_$_SU_Sanitization
+ __OBJC_$_CLASS_METHODS_SUOSUDDMConfiguration
+ __OBJC_$_INSTANCE_METHODS_SUOSUDDMConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUDDMConfiguration
+ __OBJC_$_PROP_LIST_SUOSUDDMConfiguration
+ __OBJC_CLASS_RO_$_SUOSUDDMConfiguration
+ __OBJC_METACLASS_RO_$_SUOSUDDMConfiguration
+ ___107-[SUAppStoreUpdateController _setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke
+ ___107-[SUAppStoreUpdateController _setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke_2
+ ___39+[SUOSUDDMConfiguration sharedInstance]_block_invoke
+ ___42-[SUHelperProxy cacheDeletePurgeableSpace]_block_invoke
+ ___43-[SUHelperProxy prepareForLogoutAndInstall]_block_invoke
+ ___67-[SUBackgroundManager synchronousRefreshAvailableUpdatesIfRequired]_block_invoke
+ ___74-[SUUpdateServiceDaemon _runBackgroundActionsOnCurrentQueueIfAppropriate:]_block_invoke
+ ___SULogObject_block_invoke.cold.2
+ __block_literal_global.139
+ __block_literal_global.165
+ __block_literal_global.171
+ __block_literal_global.177
+ __block_literal_global.233
+ __block_literal_global.237
+ __block_literal_global.239
+ __block_literal_global.255
+ __block_literal_global.270
+ __block_literal_global.293
+ __block_literal_global.459
+ __block_literal_global.479
+ __block_literal_global.482
+ __block_literal_global.487
+ __block_literal_global.92
+ __block_literal_global.96
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _localizedDescriptionForKey.cold.1
+ _objc_msgSend$_daysToSeconds:
+ _objc_msgSend$_firstOfferDates
+ _objc_msgSend$_runBackgroundActionsOnCurrentQueueIfAppropriate:
+ _objc_msgSend$_setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:
+ _objc_msgSend$_su_allExpressions
+ _objc_msgSend$_su_containsBlockOrFunctionPredicatesOrExpressions
+ _objc_msgSend$adminInstallRequired
+ _objc_msgSend$advancedPreferencesEvent
+ _objc_msgSend$automaticallyDownload
+ _objc_msgSend$automaticallyInstallOSUpdates
+ _objc_msgSend$automaticallyInstallSystemAndSecurityUpdates
+ _objc_msgSend$cacheDeletePurgeableSpace
+ _objc_msgSend$currentGlobalSettingsDeclaration
+ _objc_msgSend$ddmConfiguration
+ _objc_msgSend$enableGlobalNotifications
+ _objc_msgSend$enableRapidSecurityResponse
+ _objc_msgSend$enableRapidSecurityResponseRollback
+ _objc_msgSend$expressionType
+ _objc_msgSend$firstInstallTonightDatesByProductKey
+ _objc_msgSend$globalSettings
+ _objc_msgSend$initWithStatePersistencePath:
+ _objc_msgSend$leftExpression
+ _objc_msgSend$majorOSDeferralPeriod
+ _objc_msgSend$minorOSDeferralPeriod
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$preferencesEvent
+ _objc_msgSend$prepareForLogoutAndInstall
+ _objc_msgSend$rightExpression
+ _objc_msgSend$setReporter:
+ _objc_msgSend$subpredicates
+ _objc_msgSend$synchronousRefreshAvailableUpdatesIfRequired
+ _objc_msgSend$systemUpdatesDeferralPeriod
+ _su_firmware_updates_directory
+ _suhelperd_client_reclaimable_space_from_cache_delete
+ _wrapRunLoopWithAutoreleasePoolHandler.cold.1
+ sharedInstance.instance
+ sharedInstance.onceToken
- +[SUTelemetryEventFormatter defaultFormatter]
- -[SUAppStoreUpdateController _setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]
- -[SUBackgroundManager refreshAvailableUpdatesIfRequiredWithSynchronousScan:]
- -[SUExternalTaskManager _flushTaskOutput]
- -[SUExternalTaskManager _processTaskOutput:]
- -[SUExternalTaskManager _processTaskOutput:].cold.1
- -[SUExternalTaskManager _readTaskOutput:]
- -[SUExternalTaskManager dealloc]
- -[SUExternalTaskManager initTaskWithLaunchPath:arguments:logWithPrefix:]
- -[SUExternalTaskManager initWithTask:logWithPrefix:]
- -[SUExternalTaskManager run]
- -[SUExternalTaskManager run].cold.1
- -[SUExternalTaskManager run].cold.2
- -[SUExternalTaskManager run].cold.3
- -[SUHelperProxy prepareForLogoutAndInstall:]
- -[SUHelperProxy removeUpdatesAvailableCookie]
- -[SUPreferenceManager recommendedUpdatesAvailable]
- -[SUSharedPrefs(AnyUserPrefs) allowScanForMajorMSUAsset]
- -[SUSharedPrefs(ScanStatus) lastRecommendedUpdatesAvailable]
- -[SUSharedPrefs(ScanStatus) lastUpdatesAvailable]
- -[SUTelemetryEvent formatter]
- -[SUTelemetryEventFormatter dateFormatter]
- -[SUTelemetryEventFormatter formatBool:]
- -[SUTelemetryEventFormatter formatDate:]
- -[SUTelemetryEventFormatter formatDouble:]
- -[SUTelemetryEventFormatter formatInteger:]
- -[SUTelemetryEventFormatter formatResult:]
- -[SUTelemetryEventFormatter formatUnsignedLongLong:]
- -[SUTelemetryEventFormatter formatValuesInDict:]
- -[SUTelemetryEventFormatter init]
- -[SUTelemetryEventFormatter setDateFormatter:]
- -[SUTelemetryManager advancedPreferencesEvent]
- -[SUTelemetryManager downloadEvent]
- -[SUTelemetryManager formatter]
- -[SUTelemetryManager installEvent]
- -[SUTelemetryManager preferencesEvent]
- -[SUTelemetryManager scanEvent]
- -[SUTelemetryManager setFormatter:]
- -[SUTelemetryManager setSharedPrefs:]
- -[SUTelemetryManager sharedPrefs]
- -[SUTelemetryReporter formatter]
- -[SUTelemetryReporter setFormatter:]
- -[SUUpdateServiceDaemon _runBackgroundActionsOnCurrentQueueIfAppropriate:shouldSkipScanning:]
- GCC_except_table104
- GCC_except_table116
- GCC_except_table138
- GCC_except_table144
- GCC_except_table147
- GCC_except_table153
- GCC_except_table157
- GCC_except_table164
- GCC_except_table194
- GCC_except_table197
- GCC_except_table209
- GCC_except_table3
- GCC_except_table80
- GCC_except_table88
- GCC_except_table92
- GCC_except_table94
- GCC_except_table97
- OBJC_IVAR_$_SUExternalTaskManager._logOnlyStandardError
- OBJC_IVAR_$_SUExternalTaskManager._logPrefix
- OBJC_IVAR_$_SUExternalTaskManager._outputReadHandle
- OBJC_IVAR_$_SUExternalTaskManager._partialLine
- OBJC_IVAR_$_SUExternalTaskManager._task
- OBJC_IVAR_$_SUSharedPrefs._notifyQueue
- OBJC_IVAR_$_SUSharedPrefs._previousManagedPrefsPayloadUUID
- OBJC_IVAR_$_SUSharedPrefs._updatesToInstall
- OBJC_IVAR_$_SUTelemetryEvent._formatter
- OBJC_IVAR_$_SUTelemetryEventFormatter._dateFormatter
- OBJC_IVAR_$_SUTelemetryManager._formatter
- OBJC_IVAR_$_SUTelemetryManager._sharedPrefs
- OBJC_IVAR_$_SUTelemetryReporter._formatter
- _NSFileHandleNotificationDataItem
- _NSFileHandleReadCompletionNotification
- _OBJC_CLASS_$_LPAPFSVolume
- _OBJC_CLASS_$_LPMedia
- _OBJC_CLASS_$_NSPipe
- _OBJC_CLASS_$_SUExternalTaskManager
- _OBJC_CLASS_$_SUSharedPaths
- _OBJC_METACLASS_$_SUExternalTaskManager
- _OBJC_METACLASS_$_SUSharedPaths
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _SUAppStoreAvailableUpdatesChangedNotification
- _SUAppStoreHasIgnoredUpdatesChangedNotification
- _SUScanPrefLastRecommendedUpdatesAvailableKey
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.196
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.206
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.207
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.207.cold.1
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.207.cold.2
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.210
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.210.cold.1
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.212.cold.1
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.215
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.218
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.218.cold.1
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke.219
- __107-[SUAppStoreUpdateController _startSessionForUpdates:withInstall:usingForeground:notifyOn:progress:finish:]_block_invoke_2.220
- __116-[SUAppStoreUpdateController _setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke.106
- __116-[SUAppStoreUpdateController _setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke.120
- __116-[SUAppStoreUpdateController _setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke.cold.1
- __116-[SUAppStoreUpdateController _setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke_2.111
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.154
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.154.cold.1
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.160
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.162
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.162.cold.1
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke.163
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke_2.148
- __127-[SUAppStoreUpdateController startScanningForUpdatesIncludingPrerelease:rampedUnseen:evenIfUnchanged:notifyOn:progress:finish:]_block_invoke_2.161
- __34-[SUAppStoreUpdateController init]_block_invoke.51
- __41-[SUAppStoreUpdateController _connection]_block_invoke.74
- __49-[SUAppStoreUpdateController _authorizeIfNeeded:]_block_invoke.193
- __50-[SUAppStoreUpdateController installUpdatesLater:]_block_invoke.241
- __52-[SUAppStoreUpdateController installedUpdateJournal]_block_invoke.173
- __55-[SUAppStoreUpdateController updatesToBeInstalledLater]_block_invoke.254
- __58-[SUAppStoreUpdateController diskSpaceRequiredForUpdates:]_block_invoke.185
- __61-[SUAppStoreUpdateController updatesToBeInstalledAfterLogout]_block_invoke.238
- __62-[SUAppStoreUpdateController removeAllUpdatesFromInstallLater]_block_invoke.247
- __63-[SUAppStoreUpdateController __queryForAvailableUpdatesHelper:]_block_invoke.121
- __63-[SUAppStoreUpdateController authChallengeWasReceived:handled:]_block_invoke.301
- __67-[SUAppStoreUpdateController installedUpdateJournalPrunedAndSorted]_block_invoke.179
- __69-[SUAppStoreUpdateController isDownloadRequiredForPostLogoutUpdates:]_block_invoke.227
- __76-[SUBackgroundManager refreshAvailableUpdatesIfRequiredWithSynchronousScan:]_block_invoke.71
- __79-[SUAppStoreUpdateController _retrieveCatalogInformationWithCompletionHandler:]_block_invoke.166
- __79-[SUAppStoreUpdateController fetchMajorProductForUpdate:withCompletionHandler:]_block_invoke.93
- __82-[SUAppStoreUpdateController(SoftwareUpdatePrefPane) cancelUpdatesForProductKeys:]_block_invoke.495
- __83-[SUAppStoreUpdateController(SoftwareUpdatePrefPane) combinedStatusForProductKeys:]_block_invoke.490
- __84-[SUAppStoreUpdateController registerRequestsToInstallAfterPostLogoutUpdates:error:]_block_invoke.278
- __85-[SUAppStoreUpdateController installUpdatesAfterNextLogout:restartingNow:nowIsLater:]_block_invoke.236
- __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke.138
- __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke.140
- __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke_2.139
- __86-[SUAppStoreUpdateController availableUpdatesMatchingPredicate:withCompletionHandler:]_block_invoke_2.139.cold.1
- __95-[SUAppStoreUpdateController(SoftwareUpdatePrefPane) productKeysInActiveForegroundTransactions]_block_invoke.487
- __OBJC_$_INSTANCE_METHODS_SUExternalTaskManager
- __OBJC_$_INSTANCE_METHODS_SUTelemetryEventFormatter
- __OBJC_$_INSTANCE_VARIABLES_SUExternalTaskManager
- __OBJC_$_INSTANCE_VARIABLES_SUTelemetryEvent
- __OBJC_$_INSTANCE_VARIABLES_SUTelemetryEventFormatter
- __OBJC_$_PROP_LIST_SUTelemetryEvent
- __OBJC_$_PROP_LIST_SUTelemetryEventFormatter
- __OBJC_CLASS_RO_$_SUExternalTaskManager
- __OBJC_CLASS_RO_$_SUSharedPaths
- __OBJC_METACLASS_RO_$_SUExternalTaskManager
- __OBJC_METACLASS_RO_$_SUSharedPaths
- ___116-[SUAppStoreUpdateController _setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke
- ___116-[SUAppStoreUpdateController _setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:]_block_invoke_2
- ___44-[SUHelperProxy prepareForLogoutAndInstall:]_block_invoke
- ___45-[SUHelperProxy removeUpdatesAvailableCookie]_block_invoke
- ___76-[SUBackgroundManager refreshAvailableUpdatesIfRequiredWithSynchronousScan:]_block_invoke
- ___93-[SUUpdateServiceDaemon _runBackgroundActionsOnCurrentQueueIfAppropriate:shouldSkipScanning:]_block_invoke
- __block_literal_global.108
- __block_literal_global.146
- __block_literal_global.172
- __block_literal_global.178
- __block_literal_global.240
- __block_literal_global.253
- __block_literal_global.262
- __block_literal_global.277
- __block_literal_global.300
- __block_literal_global.441
- __block_literal_global.486
- __block_literal_global.489
- __block_literal_global.494
- __block_literal_global.98
- _objc_msgSend$_flushTaskOutput
- _objc_msgSend$_processTaskOutput:
- _objc_msgSend$_runBackgroundActionsOnCurrentQueueIfAppropriate:shouldSkipScanning:
- _objc_msgSend$_setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:
- _objc_msgSend$dateFormatter
- _objc_msgSend$fileHandleForReading
- _objc_msgSend$formatter
- _objc_msgSend$initWithFormat:
- _objc_msgSend$initWithTask:logWithPrefix:
- _objc_msgSend$lastRecommendedUpdatesAvailable
- _objc_msgSend$launchPath
- _objc_msgSend$objectForAnyUserPreference:usingManaged:usingDefaultOverride:
- _objc_msgSend$prepareForLogoutAndInstall:
- _objc_msgSend$readInBackgroundAndNotify
- _objc_msgSend$refreshAvailableUpdatesIfRequiredWithSynchronousScan:
- _objc_msgSend$removeUpdatesAvailableCookie
- _objc_msgSend$setStandardError:
- _suhelperd_client_remove_updates_available_cookie
CStrings:
+ " - Display Sleep Assertion"
+ "%@: No auth, can't proceed with cacheDeletePurgeableSpace"
+ "%s: Display sleep prevention failed."
+ "%s: Major OS deferral is disabled"
+ "%s: Minor OS deferral is disabled"
+ "%s: Non OS deferral is disabled"
+ "%s: Period: %@"
+ "%s: Preventing display sleep with assertion %@."
+ "-[SUPowerAssertionManager createUserActivityAssertionWithDescription:timeout:]"
+ "-[SUSharedPrefs(AnyUserPrefs) majorOSDeferralPeriod]"
+ "-[SUSharedPrefs(AnyUserPrefs) minorOSDeferralPeriod]"
+ "-[SUSharedPrefs(AnyUserPrefs) nonOSDeferralPeriod]"
+ "/Library/Updates/Firmware"
+ "/var/db/.SoftwareUpdateAtLogout"
+ "/var/db/softwareupdate/SoftwareUpdateDDMStatePersistence.plist"
+ "@\"SUCorePolicyDDMConfiguration\""
+ "@28@0:8i16q20"
+ "AppliesOnLidClose"
+ "AssertName"
+ "AssertType"
+ "CACHE_DELETE_AMOUNT"
+ "CACHE_DELETE_URGENCY"
+ "CACHE_DELETE_VOLUME"
+ "FakeAppCloseNotificationDelay"
+ "FakeMAEstimateBytesReclaimedSuccess"
+ "FakeMaxPreSUStagingSize"
+ "FirstInstallTonightDateDictionary"
+ "FirstOfferDateDictionary"
+ "LWHarvestMethod"
+ "LastLoginWindowHarvestDate"
+ "LastLoginWindowHarvestMethod"
+ "LastSuccessfulBackgroundMSUScanDate"
+ "Products %@ is marked as greater than Downloaded but the product is in fact not downloaded; setting downloadOrStagingRequired to YES."
+ "SUOSUDDMConfiguration"
+ "SU_Sanitization"
+ "T@\"SUCorePolicyDDMConfiguration\",&,V_ddmConfiguration"
+ "T@\"SUTelemetryReporter\",&,N,V_reporter"
+ "TimeoutSeconds"
+ "UpdatesAvailableNotificationDelay"
+ "UserIsActive"
+ "_daysToSeconds:"
+ "_ddmConfiguration"
+ "_firstOfferDates"
+ "_runBackgroundActionsOnCurrentQueueIfAppropriate:"
+ "_setAvailableUpdates:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:"
+ "_su_allExpressions"
+ "_su_containsBlockOrFunctionPredicatesOrExpressions"
+ "appCloseNotificationDelay"
+ "automaticallyDownload"
+ "automaticallyInstallOSUpdates"
+ "automaticallyInstallSystemAndSecurityUpdates"
+ "cacheDeletePurgeableSpace"
+ "createCacheDeleteInfoDictionaryWithUrgencyLevel:spaceToPurge:"
+ "createUserActivityAssertionWithDescription:timeout:"
+ "currentGlobalSettingsDeclaration"
+ "ddmConfiguration"
+ "enableGlobalNotifications"
+ "enableRapidSecurityResponse"
+ "enableRapidSecurityResponseRollback"
+ "expressionType"
+ "fakeMaxPreSUStagingSize"
+ "fakeMobileAssetEstimateBytesReclaimedSuccess"
+ "firstInstallTonightDateForProductKey:"
+ "firstInstallTonightDatesByProductKey"
+ "firstOfferDateForProductKey:"
+ "globalSettings"
+ "initWithStatePersistencePath:"
+ "lastLoginWindowHarvestDate"
+ "lastLoginWindowHarvestMethod"
+ "lastSuccessfulMSUBackgroundScanDate"
+ "leftExpression"
+ "majorOSDeferralPeriod"
+ "minSinceHarvest"
+ "minSinceLWHarvest"
+ "minorOSDeferralPeriod"
+ "nonOSDeferralPeriod"
+ "numberWithLongLong:"
+ "prepareForLogoutAndInstall"
+ "rightExpression"
+ "roundToMB:"
+ "setDdmConfiguration:"
+ "setFirstInstallTonightDateForProductKey:"
+ "setFirstOfferDateForProductKey:"
+ "setLastLoginWindowHarvestDate:"
+ "setLastLoginWindowHarvestMethod:"
+ "setLastSuccessfulMSUBackgroundScanDate:"
+ "stashState"
+ "subpredicates"
+ "synchronousRefreshAvailableUpdatesIfRequired"
+ "systemUpdatesDeferralPeriod"
+ "updatesAvailableNotificationDelay"
+ "v24@0:8^B16"
+ "v32@0:8@16d24"
- "\n"
- "%@: "
- "%s%s"
- "/var/run/com.apple.softwareupdate.availableupdatesupdated"
- "@\"NSFileHandle\""
- "@\"SUTelemetryEventFormatter\""
- "AllowMajorMobileAsset"
- "BackgroundActions: Skipping background scan as requested, proceeded to evaluate results of most recent scan by force setting _timeToScan"
- "LastRecommendedUpdatesAvailable"
- "LastUpdatesAvailable"
- "Products %@ is marked as greater than Downloaded but the product is in fact not downloaded; setting needsDownload and downloadOrStagingRequired to YES."
- "SUExternalTaskManager"
- "SUExternalTaskManager: ERROR: Unable to process output from (%s)"
- "SUExternalTaskManager: FAILED (NO task attributes: (%s))"
- "SUExternalTaskManager: FAILED (task attributes: (%s))"
- "SUExternalTaskManager: encountered EXCEPTION (%s)"
- "SUSharedPaths"
- "T@\"NSDateFormatter\",V_dateFormatter"
- "T@\"SUTelemetryEventFormatter\",R,V_formatter"
- "T@\"SUTelemetryEventFormatter\",V_formatter"
- "T@\"SUTelemetryReporter\",V_reporter"
- "_dateFormatter"
- "_flushTaskOutput"
- "_logOnlyStandardError"
- "_logPrefix"
- "_outputReadHandle"
- "_partialLine"
- "_previousManagedPrefsPayloadUUID"
- "_processTaskOutput:"
- "_readTaskOutput:"
- "_runBackgroundActionsOnCurrentQueueIfAppropriate:shouldSkipScanning:"
- "_setAvailableUpdatesAndNotify:withMajorOSUpdates:currentStatus:deferredUpdatesChanged:"
- "_task"
- "_updatesToInstall"
- "allowScanForMajorMSUAsset"
- "availableUpdatesChanged"
- "dateFormatter"
- "defaultFormatter"
- "fileHandleForReading"
- "formatter"
- "hasIgnoredUpdatesChanged"
- "i20@0:8B16"
- "initTaskWithLaunchPath:arguments:logWithPrefix:"
- "initWithFormat:"
- "initWithTask:logWithPrefix:"
- "lastRecommendedUpdatesAvailable"
- "lastUpdatesAvailable"
- "launchPath"
- "majorOS:%@"
- "minorOS:%@"
- "objectForAnyUserPreference:usingManaged:usingDefaultOverride:"
- "prepareForLogoutAndInstall:"
- "readInBackgroundAndNotify"
- "recommendedUpdatesAvailable"
- "refreshAvailableUpdatesIfRequiredWithSynchronousScan:"
- "removeUpdatesAvailableCookie"
- "setDateFormatter:"
- "setFormatter:"
- "setStandardError:"
- "v28@0:8^B16B24"

```
