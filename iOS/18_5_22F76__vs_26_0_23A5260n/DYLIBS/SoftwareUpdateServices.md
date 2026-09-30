## SoftwareUpdateServices

> `/System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices`

```diff

-905.120.4.0.0
-  __TEXT.__text: 0xaddb8
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0xaafc
-  __TEXT.__cstring: 0x1f219
-  __TEXT.__const: 0x2b0
-  __TEXT.__gcc_except_tab: 0x1078
+950.0.1.0.2
+  __TEXT.__text: 0xaeb48
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_methlist: 0xab2c
+  __TEXT.__const: 0x318
+  __TEXT.__cstring: 0x206fd
+  __TEXT.__gcc_except_tab: 0x1014
   __TEXT.__oslogstring: 0xd81
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3168
-  __TEXT.__objc_classname: 0xed4
-  __TEXT.__objc_methname: 0x186d3
-  __TEXT.__objc_methtype: 0x34c9
-  __TEXT.__objc_stubs: 0x13d80
-  __DATA_CONST.__got: 0xd60
-  __DATA_CONST.__const: 0x2940
+  __TEXT.__unwind_info: 0x3158
+  __TEXT.__objc_classname: 0xeed
+  __TEXT.__objc_methname: 0x1898c
+  __TEXT.__objc_methtype: 0x344d
+  __TEXT.__objc_stubs: 0x14060
+  __DATA_CONST.__got: 0xd70
+  __DATA_CONST.__const: 0x2900
   __DATA_CONST.__objc_classlist: 0x3d0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b08
+  __DATA_CONST.__objc_selrefs: 0x5b70
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x318
-  __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x12a80
-  __AUTH_CONST.__objc_const: 0x155d0
+  __DATA_CONST.__objc_arraydata: 0xa0
+  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__const: 0x780
+  __AUTH_CONST.__cfstring: 0x128a0
+  __AUTH_CONST.__objc_const: 0x15698
   __AUTH_CONST.__objc_intobj: 0x240
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH.__objc_data: 0x1068
-  __DATA.__objc_ivar: 0x94c
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH.__objc_data: 0xfc8
+  __DATA.__objc_ivar: 0x944
   __DATA.__data: 0xe98
-  __DATA.__bss: 0x100
-  __DATA_DIRTY.__objc_data: 0x15b8
-  __DATA_DIRTY.__bss: 0x1e0
+  __DATA.__bss: 0xe8
+  __DATA_DIRTY.__objc_data: 0x1658
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BatteryCenter.framework/BatteryCenter
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/LockdownMode.framework/LockdownMode
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience

   - /usr/lib/libamsupport.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libc++.1.dylib
-  - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 2F443938-97AF-3C29-8D76-16F04F3664C2
-  Functions: 4398
-  Symbols:   14704
-  CStrings:  9938
+  UUID: 0A647743-89DB-360A-9769-F896185EA532
+  Functions: 4448
+  Symbols:   14762
+  CStrings:  10009
 
Symbols:
+ +[SUAssetSupport tryCreateDocumentationFromDocumentationAsset:]
+ +[SUUtility isReturnToServiceModeActive]
+ -[SUDescriptor setUnentitledReserveAmount:]
+ -[SUDescriptor unentitledReserveAmount]
+ -[SUManagerClient disableReserveSpace:completion:]
+ -[SUManagerClient overrideSoftwareUpdateReserve:systemGrowthMarginSize:completion:]
+ -[SUManagerClient softwareUpdateReserveSizes:]
+ -[SUManagerCore disableReserveSpace:]
+ -[SUManagerCore donateSUErrorToBiome:]
+ -[SUManagerCore donateSuccessToBiomeFor:]
+ -[SUManagerCore overrideSoftwareUpdateReserve:systemGrowthMarginSize:]
+ -[SUManagerCore preferences:didChangePreference:toValue:]
+ -[SUManagerCore resumeReserveSpaceStateIfNeeded]
+ -[SUManagerCore softwareUpdateReserveSizes]
+ -[SUManagerCore(Analytics) _augmentCoreAnalyticsEvent:withUpdate:]
+ -[SUManagerCore(Analytics) _createCoreAnalyticsEventWithCurrentDownloadFor:error:]
+ -[SUManagerCore(Analytics) _getAmountDataAvailable]
+ -[SUManagerCore(Analytics) _submitCoreAnalyticsEvent:]
+ -[SUManagerCore(Analytics) reportCoreAnalyticsOTAAbandonedEvent:]
+ -[SUManagerCore(Analytics) reportCoreAnalyticsOTAAvailableEvent:]
+ -[SUManagerCore(Analytics) reportCoreAnalyticsOTADownloadedEvent]
+ -[SUManagerCore(Analytics) reportCoreAnalyticsOTAStartedDownloadingEvent:]
+ -[SUManagerCore(MDM) amendManagedScanOptions:withResponse:]
+ -[SUManagerCore(MDM) delayEndDate]
+ -[SUManagerCore(MDM) isDelayingUpdates]
+ -[SUManagerCore(MDM) isManaged]
+ -[SUManagerCore(MDM) managedInstallRequested]
+ -[SUManagerCore(MDM) softwareUpdatePathRestriction]
+ -[SUManagerCore(MDM) updatesDelayPeriodSeconds]
+ -[SUManagerCore(Splat) eligibleRollbackWithOptions:]
+ -[SUManagerCore(Splat) isRollingBack]
+ -[SUManagerCore(Splat) isSplatOnlyUpdateRollbackSuggested]
+ -[SUManagerCore(Splat) isSplatRollbackAllowed:]
+ -[SUManagerCore(Splat) isSplatRollbackEnabled]
+ -[SUManagerCore(Splat) presentRollbackSuggestionAlertWithDescriptor:info:]
+ -[SUManagerCore(Splat) presentRollbackSuggestionFollowUpWithCoreDescriptor:info:]
+ -[SUManagerCore(Splat) presentRollbackSuggestionFollowUpWithRollbackDescriptor:info:]
+ -[SUManagerCore(Splat) previousRollbackWithOptions:]
+ -[SUManagerCore(Splat) revokedUpdateFound:]
+ -[SUManagerCore(Splat) rollbackCompleted:withError:]
+ -[SUManagerCore(Splat) rollbackReadyForReboot]
+ -[SUManagerCore(Splat) rollbackStarted:]
+ -[SUManagerCore(Splat) rollbackUpdateWithOptions:withResult:]
+ -[SUManagerCore(Splat) securityResponseRollbackSuggested:withResult:]
+ -[SUManagerCore(Splat) shouldShowRollbackSuggestionAlert:error:]
+ -[SUManagerCore(Splat) splatUpdatesAllowed]
+ -[SUManagerCore(Splat) suggestRollback:rollbackDescriptor:withResult:]
+ -[SUManagerPolicy disableReserveSpace:withResult:]
+ -[SUManagerPolicy overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:]
+ -[SUManagerPolicy softwareUpdateReserveSizes:]
+ -[SUManagerServer disableReserveSpace:withResult:]
+ -[SUManagerServer overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:]
+ -[SUManagerServer softwareUpdateReserveSizes:]
+ -[SUPreferences .cxx_destruct]
+ -[SUPreferences _loadPreferences:]
+ -[SUPreferences _setCachedObjectPreferenceForKey:value:]
+ -[SUPreferences _setupSoftwareUpdateReserveDisabled]
+ -[SUPreferences disableSoftwareUpdateReserve:]
+ -[SUPreferences overrideSessionIDRampingPortion]
+ -[SUPreferences setSoftwareUpdateReserveSize:]
+ -[SUPreferences setSystemGrowthMarginSize:]
+ -[SUPreferences softwareUpdateReserveDisabled]
+ -[SUPreferences softwareUpdateReserveSize]
+ -[SUPreferences systemGrowthMarginSize]
+ GCC_except_table102
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table157
+ GCC_except_table201
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table228
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table290
+ GCC_except_table292
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table341
+ GCC_except_table441
+ GCC_except_table45
+ GCC_except_table72
+ GCC_except_table85
+ GCC_except_table96
+ GCC_except_table98
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMDiscoverabilitySignals
+ _OBJC_CLASS_$_SUCoreUUID
+ _OBJC_CLASS_$_UIDevice
+ _OBJC_IVAR_$_SUDescriptor._assetID
+ _OBJC_IVAR_$_SUDescriptor._audienceType
+ _OBJC_IVAR_$_SUDescriptor._autoDownloadAllowableForCellular
+ _OBJC_IVAR_$_SUDescriptor._autoUpdateEnabled
+ _OBJC_IVAR_$_SUDescriptor._criticalOutOfBoxOnly
+ _OBJC_IVAR_$_SUDescriptor._disableAppDemotion
+ _OBJC_IVAR_$_SUDescriptor._disableCDLevel4
+ _OBJC_IVAR_$_SUDescriptor._disableInstallTonight
+ _OBJC_IVAR_$_SUDescriptor._disableMASuspension
+ _OBJC_IVAR_$_SUDescriptor._disableSiriVoiceDeletion
+ _OBJC_IVAR_$_SUDescriptor._documentation
+ _OBJC_IVAR_$_SUDescriptor._downloadSize
+ _OBJC_IVAR_$_SUDescriptor._downloadable
+ _OBJC_IVAR_$_SUDescriptor._forcePasscodeRequired
+ _OBJC_IVAR_$_SUDescriptor._granularlyRamped
+ _OBJC_IVAR_$_SUDescriptor._hideInstallAlert
+ _OBJC_IVAR_$_SUDescriptor._humanReadableUpdateName
+ _OBJC_IVAR_$_SUDescriptor._installationSize
+ _OBJC_IVAR_$_SUDescriptor._isSplatOnly
+ _OBJC_IVAR_$_SUDescriptor._isSplombo
+ _OBJC_IVAR_$_SUDescriptor._mandatoryUpdateEligible
+ _OBJC_IVAR_$_SUDescriptor._mandatoryUpdateOptional
+ _OBJC_IVAR_$_SUDescriptor._mandatoryUpdateRestrictedToOutOfTheBox
+ _OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMax
+ _OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMin
+ _OBJC_IVAR_$_SUDescriptor._mdmDelayInterval
+ _OBJC_IVAR_$_SUDescriptor._minimumSystemPartitionSize
+ _OBJC_IVAR_$_SUDescriptor._msuPrepareSize
+ _OBJC_IVAR_$_SUDescriptor._preSUStagingOptionalSize
+ _OBJC_IVAR_$_SUDescriptor._preSUStagingRequiredSize
+ _OBJC_IVAR_$_SUDescriptor._preferenceType
+ _OBJC_IVAR_$_SUDescriptor._preparationSize
+ _OBJC_IVAR_$_SUDescriptor._prerequisiteBuild
+ _OBJC_IVAR_$_SUDescriptor._prerequisiteOS
+ _OBJC_IVAR_$_SUDescriptor._productBuildVersion
+ _OBJC_IVAR_$_SUDescriptor._productSystemName
+ _OBJC_IVAR_$_SUDescriptor._productVersion
+ _OBJC_IVAR_$_SUDescriptor._productVersionExtra
+ _OBJC_IVAR_$_SUDescriptor._promoteAlternateUpdate
+ _OBJC_IVAR_$_SUDescriptor._publisher
+ _OBJC_IVAR_$_SUDescriptor._rampEnabled
+ _OBJC_IVAR_$_SUDescriptor._releaseDate
+ _OBJC_IVAR_$_SUDescriptor._releaseType
+ _OBJC_IVAR_$_SUDescriptor._rsepDigest
+ _OBJC_IVAR_$_SUDescriptor._rsepTBMDigest
+ _OBJC_IVAR_$_SUDescriptor._sepDigest
+ _OBJC_IVAR_$_SUDescriptor._sepTBMDigest
+ _OBJC_IVAR_$_SUDescriptor._setupCritical
+ _OBJC_IVAR_$_SUDescriptor._splatComboBuildVersion
+ _OBJC_IVAR_$_SUDescriptor._systemPartitionPadding
+ _OBJC_IVAR_$_SUDescriptor._totalRequiredFreeSpace
+ _OBJC_IVAR_$_SUDescriptor._unarchiveSize
+ _OBJC_IVAR_$_SUDescriptor._unentitledReserveAmount
+ _OBJC_IVAR_$_SUDescriptor._updateType
+ _OBJC_IVAR_$_SUDescriptor._upgradeType
+ _SUBiomeContentIdentifierError
+ _SUBiomeContentIdentifierSucceeded
+ _SUBiomeOperationDownload
+ _SUBiomeOperationInstall
+ _SUBiomeOperationScan
+ __OBJC_$_INSTANCE_METHODS_SUManagerCore(Analytics|MDM|Splat)
+ ___32-[SUInstaller installCompleted:]_block_invoke.381
+ ___32-[SUInstaller installCompleted:]_block_invoke_2.382
+ ___32-[SUInstaller installCompleted:]_block_invoke_3.388
+ ___34-[SUPreferences _loadPreferences:]_block_invoke
+ ___37-[SUScanner scanForUpdates:complete:]_block_invoke
+ ___37-[SUScanner scanForUpdates:complete:]_block_invoke_2
+ ___37-[SUScanner scanForUpdates:complete:]_block_invoke_3
+ ___37-[SUScanner scanForUpdates:complete:]_block_invoke_4
+ ___38-[SUManagerCore donateSUErrorToBiome:]_block_invoke
+ ___40-[SUManagerCore(Splat) rollbackStarted:]_block_invoke
+ ___41-[SUManagerCore donateSuccessToBiomeFor:]_block_invoke
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.529
+ ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.533
+ ___46-[SUManagerClient softwareUpdateReserveSizes:]_block_invoke
+ ___46-[SUManagerClient softwareUpdateReserveSizes:]_block_invoke_2
+ ___46-[SUManagerPolicy softwareUpdateReserveSizes:]_block_invoke
+ ___46-[SUManagerPolicy softwareUpdateReserveSizes:]_block_invoke_2
+ ___46-[SUManagerServer softwareUpdateReserveSizes:]_block_invoke
+ ___46-[SUManagerServer softwareUpdateReserveSizes:]_block_invoke_2
+ ___46-[SUManagerServer softwareUpdateReserveSizes:]_block_invoke_3
+ ___50-[SUManagerClient disableReserveSpace:completion:]_block_invoke
+ ___50-[SUManagerClient disableReserveSpace:completion:]_block_invoke_2
+ ___50-[SUManagerPolicy disableReserveSpace:withResult:]_block_invoke
+ ___50-[SUManagerServer disableReserveSpace:withResult:]_block_invoke
+ ___50-[SUManagerServer disableReserveSpace:withResult:]_block_invoke_2
+ ___50-[SUManagerServer disableReserveSpace:withResult:]_block_invoke_3
+ ___52-[SUDownloader startDownloadWithOptions:withResult:]_block_invoke_10
+ ___52-[SUManagerCore(Splat) rollbackCompleted:withError:]_block_invoke
+ ___56-[SUPreferences _setCachedObjectPreferenceForKey:value:]_block_invoke
+ ___57-[SUManagerCore preferences:didChangePreference:toValue:]_block_invoke
+ ___59-[SUManagerCore(MDM) amendManagedScanOptions:withResponse:]_block_invoke
+ ___59-[SUManagerCore(MDM) amendManagedScanOptions:withResponse:]_block_invoke_2
+ ___65-[SUManagerCore(Analytics) reportCoreAnalyticsOTAAvailableEvent:]_block_invoke
+ ___68-[SUInstaller isUpdateReadyForInstallationWithOptions:replyHandler:]_block_invoke
+ ___74-[SUManagerCore(Splat) presentRollbackSuggestionAlertWithDescriptor:info:]_block_invoke
+ ___83-[SUManagerClient overrideSoftwareUpdateReserve:systemGrowthMarginSize:completion:]_block_invoke
+ ___83-[SUManagerClient overrideSoftwareUpdateReserve:systemGrowthMarginSize:completion:]_block_invoke_2
+ ___83-[SUManagerPolicy overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:]_block_invoke
+ ___83-[SUManagerServer overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:]_block_invoke
+ ___83-[SUManagerServer overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:]_block_invoke_2
+ ___83-[SUManagerServer overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:]_block_invoke_3
+ ___86-[SUManagerCore updatesDownloadableWithOptions:alternateDownloadOptions:replyHandler:]_block_invoke.496
+ ___block_descriptor_48_e8_32s40bs_e23_v24?0B8B12"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e35_v24?0"SUScanOptions"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8u56l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e23_v24?0B8B12"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.357
+ ___block_literal_global.395
+ ___block_literal_global.400
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.413
+ ___block_literal_global.419
+ ___block_literal_global.441
+ ___block_literal_global.472
+ ___block_literal_global.519
+ ___block_literal_global.544
+ ___block_literal_global.549
+ ___block_literal_global.558
+ ___block_literal_global.580
+ ___block_literal_global.590
+ ___block_literal_global.622
+ ___block_literal_global.654
+ __os_feature_enabled_impl
+ _allowAutoDownloadOnBattery
+ _appDemotionDisabled
+ _assetID
+ _audienceType
+ _autoDownloadOnBatteryDelay
+ _autoDownloadOnBatteryMinBattery
+ _autoUpdateEnabled
+ _cdLevel4Disabled
+ _criticalOutOfBoxOnly
+ _documentation
+ _downloadSize
+ _forcePasscodeRequired
+ _granularlyRamped
+ _hideInstallAlert
+ _humanReadableUpdateName
+ _installTonightDisabled
+ _installationSize
+ _isDownloadable
+ _isDownloadableOverCellular
+ _isSplatOnly
+ _isSplombo
+ _kSUPreferencesDisableAutoDownload
+ _maSuspensionDisabled
+ _mandatoryUpdateEligible
+ _mandatoryUpdateOptional
+ _mandatoryUpdateRestrictedToOutOfTheBox
+ _mandatoryUpdateVersionMax
+ _mandatoryUpdateVersionMin
+ _mdmDelayInterval
+ _minimumSystemPartitionSize
+ _objc_msgSend$Discoverability
+ _objc_msgSend$MADownloadErrorCodeToSUDownloadErrorCode:
+ _objc_msgSend$Signals
+ _objc_msgSend$UUIDForSoftwareUpdate
+ _objc_msgSend$_loadPreferences:
+ _objc_msgSend$_setCachedObjectPreferenceForKey:value:
+ _objc_msgSend$_setupSoftwareUpdateReserveDisabled
+ _objc_msgSend$buildVersion
+ _objc_msgSend$cacheDeleteDisableReserveSpace
+ _objc_msgSend$cacheDeleteGetReserveSpace:withError:
+ _objc_msgSend$cacheDeletePauseReserveSpace:unentitledSpace:withPurpose:
+ _objc_msgSend$cacheDeleteResumeReserveSpace
+ _objc_msgSend$cacheDeleteSetReserveSpace:systemGrowthMarginSize:
+ _objc_msgSend$disableReserveSpace:
+ _objc_msgSend$disableReserveSpace:withResult:
+ _objc_msgSend$disableSoftwareUpdateReserve:
+ _objc_msgSend$donateSUErrorToBiome:
+ _objc_msgSend$donateSuccessToBiomeFor:
+ _objc_msgSend$getFreeSpaceAvailableForSoftwareUpdate:
+ _objc_msgSend$initWithContentIdentifier:context:osBuild:userInfo:
+ _objc_msgSend$initWithTitle:message:buttons:
+ _objc_msgSend$modelSpecificLocalizedStringKeyForKey:
+ _objc_msgSend$overrideSessionIDRampingPortion
+ _objc_msgSend$overrideSoftwareUpdateReserve:systemGrowthMarginSize:
+ _objc_msgSend$overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:
+ _objc_msgSend$resumeReserveSpaceStateIfNeeded
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$setBaseApplyOptions:
+ _objc_msgSend$setReserveSpaceSizeOverride:
+ _objc_msgSend$setSoftwareUpdateReserveSize:
+ _objc_msgSend$setSystemGrowthMarginOverride:
+ _objc_msgSend$setSystemGrowthMarginSize:
+ _objc_msgSend$setUnentitledReserveAmount:
+ _objc_msgSend$setUseReserveSpace:
+ _objc_msgSend$softwareUpdateReserveDisabled
+ _objc_msgSend$softwareUpdateReserveSize
+ _objc_msgSend$softwareUpdateReserveSizes
+ _objc_msgSend$softwareUpdateReserveSizes:
+ _objc_msgSend$source
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$systemGrowthMarginSize
+ _objc_msgSend$unentitledReserveAmount
+ _preSUStagingOptionalSize
+ _preSUStagingRequiredSize
+ _preferenceType
+ _preparationSize
+ _prerequisiteBuild
+ _prerequisiteOS
+ _productBuildVersion
+ _productSystemName
+ _productVersion
+ _productVersionExtra
+ _promoteAlternateUpdate
+ _publisher
+ _rampEnabled
+ _releaseDate
+ _releaseType
+ _rsepDigest
+ _rsepTBMDigest
+ _sepDigest
+ _sepTBMDigest
+ _setupCritical
+ _siriVoiceDeletionDisabled
+ _splatComboBuildVersion
+ _systemPartitionPadding
+ _totalRequiredFreeSpace
+ _updateType
+ _upgradeType
- +[SUUtility URLIfFileExists:]
- +[SUUtility alarmSetBeforeDate:]
- +[SUUtility appDemoteableSpace]
- +[SUUtility appDemotionIsEnabled]
- +[SUUtility appDemotionSettingQueue]
- +[SUUtility appDemotionSettingQueue].cold.1
- +[SUUtility enableAppDemotion:]
- +[SUUtility totalPurgeableSpace:]
- -[SUAlertItemDefinition setButtons:]
- -[SUAlertItemDefinition setMessage:]
- -[SUAlertItemDefinition setTitle:]
- -[SUInstaller isUpdateReadyForInstallation:]
- -[SUManagerClient totalPurgeableSpace]
- -[SUManagerCore _augmentCoreAnalyticsEvent:withUpdate:]
- -[SUManagerCore _createCoreAnalyticsEventWithCurrentDownloadFor:error:]
- -[SUManagerCore _getAmountDataAvailable]
- -[SUManagerCore _submitCoreAnalyticsEvent:]
- -[SUManagerCore adoptPotentialSessionID]
- -[SUManagerCore amendManagedScanOptions:withResponse:]
- -[SUManagerCore createSessionID]
- -[SUManagerCore createpotentialNextSessionID]
- -[SUManagerCore delayEndDate]
- -[SUManagerCore eligibleRollbackWithOptions:]
- -[SUManagerCore installUpdateWithOptions:withResult:]
- -[SUManagerCore isDelayingUpdates]
- -[SUManagerCore isManaged]
- -[SUManagerCore isRollingBack]
- -[SUManagerCore isSplatOnlyUpdateRollbackSuggested]
- -[SUManagerCore isSplatRollbackAllowed:]
- -[SUManagerCore isSplatRollbackEnabled]
- -[SUManagerCore isUpdateReadyForInstallation:]
- -[SUManagerCore managedInstallRequested]
- -[SUManagerCore potentialNextSessionID]
- -[SUManagerCore presentRollbackSuggestionAlertWithDescriptor:info:]
- -[SUManagerCore presentRollbackSuggestionFollowUpWithCoreDescriptor:info:]
- -[SUManagerCore presentRollbackSuggestionFollowUpWithRollbackDescriptor:info:]
- -[SUManagerCore previousRollbackWithOptions:]
- -[SUManagerCore reportCoreAnalyticsOTAAbandonedEvent:]
- -[SUManagerCore reportCoreAnalyticsOTAAvailableEvent:]
- -[SUManagerCore reportCoreAnalyticsOTADownloadedEvent]
- -[SUManagerCore reportCoreAnalyticsOTAStartedDownloadingEvent:]
- -[SUManagerCore revokedUpdateFound:]
- -[SUManagerCore rollbackCompleted:withError:]
- -[SUManagerCore rollbackReadyForReboot]
- -[SUManagerCore rollbackStarted:]
- -[SUManagerCore rollbackUpdateWithOptions:withResult:]
- -[SUManagerCore scanForUpdates:shouldUseDDMInState:complete:]
- -[SUManagerCore securityResponseRollbackSuggested:withResult:]
- -[SUManagerCore setPotentialNextSessionID:]
- -[SUManagerCore shouldShowRollbackSuggestionAlert:error:]
- -[SUManagerCore softwareUpdatePathRestriction]
- -[SUManagerCore splatUpdatesAllowed]
- -[SUManagerCore suggestRollback:rollbackDescriptor:withResult:]
- -[SUManagerCore updatesDelayPeriodSeconds]
- -[SUManagerPolicy isUpdateReadyForInstallation:]
- -[SUManagerPolicy isUpdateReadyForInstallationWithReplyHandler:]
- -[SUManagerPolicy scanForUpdates:shouldUseDDMInState:complete:]
- -[SUPolicyGlobalOptions setUpdateMetricEventFields:]
- -[SUPreferences _loadPreferences]
- -[SUPreferences overrideScanSessionIDRampingPortion]
- -[SUScanner scanForUpdates:shouldUseDDMInState:complete:]
- -[SUState sessionID]
- -[SUState setSessionID:]
- GCC_except_table101
- GCC_except_table105
- GCC_except_table111
- GCC_except_table113
- GCC_except_table116
- GCC_except_table119
- GCC_except_table123
- GCC_except_table125
- GCC_except_table129
- GCC_except_table131
- GCC_except_table135
- GCC_except_table145
- GCC_except_table147
- GCC_except_table149
- GCC_except_table193
- GCC_except_table196
- GCC_except_table199
- GCC_except_table220
- GCC_except_table225
- GCC_except_table230
- GCC_except_table248
- GCC_except_table251
- GCC_except_table282
- GCC_except_table284
- GCC_except_table285
- GCC_except_table286
- GCC_except_table287
- GCC_except_table333
- GCC_except_table429
- GCC_except_table44
- GCC_except_table46
- GCC_except_table52
- GCC_except_table60
- GCC_except_table76
- GCC_except_table88
- GCC_except_table89
- GCC_except_table93
- GCC_except_table95
- GCC_except_table99
- OBJC_IVAR_$_SUDescriptor._assetID
- OBJC_IVAR_$_SUDescriptor._audienceType
- OBJC_IVAR_$_SUDescriptor._autoDownloadAllowableForCellular
- OBJC_IVAR_$_SUDescriptor._autoUpdateEnabled
- OBJC_IVAR_$_SUDescriptor._criticalOutOfBoxOnly
- OBJC_IVAR_$_SUDescriptor._disableAppDemotion
- OBJC_IVAR_$_SUDescriptor._disableCDLevel4
- OBJC_IVAR_$_SUDescriptor._disableIntallTonight
- OBJC_IVAR_$_SUDescriptor._disableMASuspension
- OBJC_IVAR_$_SUDescriptor._disableSiriVoiceDeletion
- OBJC_IVAR_$_SUDescriptor._documentation
- OBJC_IVAR_$_SUDescriptor._downloadAllowableForCellular
- OBJC_IVAR_$_SUDescriptor._downloadSize
- OBJC_IVAR_$_SUDescriptor._downloadable
- OBJC_IVAR_$_SUDescriptor._forcePasscodeRequired
- OBJC_IVAR_$_SUDescriptor._granularlyRamped
- OBJC_IVAR_$_SUDescriptor._hideInstallAlert
- OBJC_IVAR_$_SUDescriptor._humanReadableUpdateName
- OBJC_IVAR_$_SUDescriptor._installationSize
- OBJC_IVAR_$_SUDescriptor._isSplatOnly
- OBJC_IVAR_$_SUDescriptor._isSplombo
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateEligible
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateOptional
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateRestrictedToOutOfTheBox
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMax
- OBJC_IVAR_$_SUDescriptor._mandatoryUpdateVersionMin
- OBJC_IVAR_$_SUDescriptor._mdmDelayInterval
- OBJC_IVAR_$_SUDescriptor._minimumSystemPartitionSize
- OBJC_IVAR_$_SUDescriptor._msuPrepareSize
- OBJC_IVAR_$_SUDescriptor._preSUStagingOptionalSize
- OBJC_IVAR_$_SUDescriptor._preSUStagingRequiredSize
- OBJC_IVAR_$_SUDescriptor._preferenceType
- OBJC_IVAR_$_SUDescriptor._preparationSize
- OBJC_IVAR_$_SUDescriptor._prerequisiteBuild
- OBJC_IVAR_$_SUDescriptor._prerequisiteOS
- OBJC_IVAR_$_SUDescriptor._productBuildVersion
- OBJC_IVAR_$_SUDescriptor._productSystemName
- OBJC_IVAR_$_SUDescriptor._productVersion
- OBJC_IVAR_$_SUDescriptor._productVersionExtra
- OBJC_IVAR_$_SUDescriptor._promoteAlternateUpdate
- OBJC_IVAR_$_SUDescriptor._publisher
- OBJC_IVAR_$_SUDescriptor._rampEnabled
- OBJC_IVAR_$_SUDescriptor._releaseDate
- OBJC_IVAR_$_SUDescriptor._releaseType
- OBJC_IVAR_$_SUDescriptor._rsepDigest
- OBJC_IVAR_$_SUDescriptor._rsepTBMDigest
- OBJC_IVAR_$_SUDescriptor._sepDigest
- OBJC_IVAR_$_SUDescriptor._sepTBMDigest
- OBJC_IVAR_$_SUDescriptor._setupCritical
- OBJC_IVAR_$_SUDescriptor._splatComboBuildVersion
- OBJC_IVAR_$_SUDescriptor._systemPartitionPadding
- OBJC_IVAR_$_SUDescriptor._totalRequiredFreeSpace
- OBJC_IVAR_$_SUDescriptor._unarchiveSize
- OBJC_IVAR_$_SUDescriptor._updateType
- OBJC_IVAR_$_SUDescriptor._upgradeType
- OBJC_IVAR_$_SUState._sessionID
- _CFArrayGetTypeID
- _CFDateCompare
- _CFDateGetTypeID
- _CFDictionaryGetValue
- _CFPreferencesAppSynchronize
- _CFPreferencesGetAppBooleanValue
- _CFPreferencesSetAppValue
- _CacheDeleteCopyPurgeableSpaceWithInfo
- _IOPMCopyScheduledPowerEvents
- _OBJC_CLASS_$_ASDPurgeableAppRequest
- _OBJC_CLASS_$_ASDPurgeableAppRequestOptions
- _OBJC_IVAR_$_SUManagerCore._potentialNextSessionID
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- __Block_object_assign
- __OBJC_$_INSTANCE_METHODS_SUManagerCore
- ___20-[SUState sessionID]_block_invoke
- ___24-[SUState setSessionID:]_block_invoke
- ___31+[SUUtility appDemoteableSpace]_block_invoke
- ___31+[SUUtility enableAppDemotion:]_block_invoke
- ___32-[SUInstaller installCompleted:]_block_invoke.370
- ___32-[SUInstaller installCompleted:]_block_invoke_2.371
- ___32-[SUInstaller installCompleted:]_block_invoke_3.377
- ___33+[SUUtility appDemotionIsEnabled]_block_invoke
- ___33-[SUManagerCore rollbackStarted:]_block_invoke
- ___33-[SUPreferences _loadPreferences]_block_invoke
- ___36+[SUUtility appDemotionSettingQueue]_block_invoke
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.526
- ___42-[SUManagerEngine action_RemoveAll:error:]_block_invoke.530
- ___45-[SUManagerCore rollbackCompleted:withError:]_block_invoke
- ___48-[SUManagerPolicy isUpdateReadyForInstallation:]_block_invoke
- ___54-[SUManagerCore amendManagedScanOptions:withResponse:]_block_invoke
- ___54-[SUManagerCore amendManagedScanOptions:withResponse:]_block_invoke_2
- ___54-[SUManagerCore reportCoreAnalyticsOTAAvailableEvent:]_block_invoke
- ___57-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]_block_invoke
- ___57-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]_block_invoke_2
- ___57-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]_block_invoke_3
- ___57-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]_block_invoke_4
- ___57-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]_block_invoke_5
- ___57-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]_block_invoke_6
- ___57-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]_block_invoke_7
- ___58-[SUInstaller installUpdateWithInstallOptions:withResult:]_block_invoke_10
- ___63-[SUManagerPolicy scanForUpdates:shouldUseDDMInState:complete:]_block_invoke
- ___64-[SUManagerPolicy isUpdateReadyForInstallationWithReplyHandler:]_block_invoke
- ___64-[SUManagerPolicy isUpdateReadyForInstallationWithReplyHandler:]_block_invoke_2
- ___64-[SUManagerPolicy isUpdateReadyForInstallationWithReplyHandler:]_block_invoke_3
- ___67-[SUManagerCore presentRollbackSuggestionAlertWithDescriptor:info:]_block_invoke
- ___block_descriptor_33_e5_v8?0l
- ___block_descriptor_48_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e48_v28?0B8"ASDPurgeableAppResponse"12"NSError"20lr40l8s32l8
- ___block_descriptor_49_e8_32o40o_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e23_v24?0B8B12"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e35_v24?0"SUScanOptions"8"NSError"16ls32l8s48l8s40l8s56l8
- ___block_literal_global.284
- ___block_literal_global.379
- ___block_literal_global.394
- ___block_literal_global.399
- ___block_literal_global.402
- ___block_literal_global.404
- ___block_literal_global.410
- ___block_literal_global.416
- ___block_literal_global.438
- ___block_literal_global.466
- ___block_literal_global.513
- ___block_literal_global.538
- ___block_literal_global.543
- ___block_literal_global.548
- ___block_literal_global.587
- ___block_literal_global.640
- ___block_literal_global.648
- ___block_literal_global.721
- ___block_literal_global.881
- ___queryLocalAssetsForTypeV2_block_invoke
- __eventIsBlacklisted
- _appDemotionSettingQueue.__appDemotionSettingQueue
- _appDemotionSettingQueue.queuePredicate
- _objc_msgSend$_loadPreferences
- _objc_msgSend$addObjectsFromArray:
- _objc_msgSend$adoptPotentialSessionID
- _objc_msgSend$appDemotionSettingQueue
- _objc_msgSend$arrayWithContentsOfFile:
- _objc_msgSend$createSessionID
- _objc_msgSend$createpotentialNextSessionID
- _objc_msgSend$fileSystemRepresentation
- _objc_msgSend$overrideScanSessionIDRampingPortion
- _objc_msgSend$purgeableSize
- _objc_msgSend$scanForUpdates:shouldUseDDMInState:complete:
- _objc_msgSend$setButtons:
- _objc_msgSend$setPotentialNextSessionID:
- _objc_msgSend$setUrgency:
- _objc_msgSend$setVolume:
- _objc_msgSend$startWithCompletionBlock:
- _objc_msgSend$substringWithRange:
- _objc_msgSend$totalPurgeableSpace:
- _objc_msgSend$wasPurgeable
- _purgeAssetSpace
- _purgeAssetSpaceForOTAUpdate
- _purgeAssetSpaceV2
- _purgeableAssetSpaceAvailable
- _purgeableAssetSpaceAvailableForOTAUpdate
- _purgeableAssetSpaceAvailableV2
- _queryLocalAssetsForType
- _queryLocalAssetsForTypeV2
- _writeArrayToFile
CStrings:
+ "\n            ClientName: %@\n            downloadOnly: %@\n            autoDownload: %@\n            userUpdateTonight: %@\n            allowUnrestrictedCellularDownload: %@\n            downloadFeeAgreementStatus: %@\n            termsAndConditionsAgreementStatus: %@\n            activeDownloadPolicyType: %@\n            enabledForCellular: %@\n            enabledForWifi: %@\n            enabledOnBatteryPower: %@\n            enabledForCellularRoaming: %@\n            descriptor: %@\n"
+ "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %llu\n            UnarchiveSize: %llu\n            MSUPrepareSize: %llu\n            PreparationSize: %llu\n            InstallationSize: %llu\n            PreSUStagingRequiredSize: %llu\n            PreSUStagingOptionalSize: %llu\n            UnentitledReserveAmount: %llu\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %@\n            TotalRequiredFreeSpace: %llu\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %llu\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@"
+ "%ld"
+ "%s: Auto installation failed to start due to SUErrorCodeInstallInProgress; do not show the alert"
+ "%s: Client delegate %@ receive status - %d"
+ "%s: Delegating to client %@"
+ "%s: Iterating over all the change preferences, ChangePref: %@"
+ "%s: reloaded preferences after getting, but nothing seems to have changed."
+ "%s: unable to get reserve space info, Error: %@"
+ "-[SUDownloader startDownloadWithOptions:withResult:]"
+ "-[SUInstaller autoSUFailedWithError:]"
+ "-[SUInstaller installCompleted:]"
+ "-[SUInstaller installCompleted:]_block_invoke"
+ "-[SUInstaller installUpdateWithInstallOptions:withResult:]"
+ "-[SUInstaller installUpdateWithInstallOptions:withResult:]_block_invoke_3"
+ "-[SUManagerClient automaticDownloadDidFailToStartForNewUpdateAvailable:withError:]"
+ "-[SUManagerClient clearingSpaceForDownload:clearing:]"
+ "-[SUManagerClient deviceBootedAfterRollback:]"
+ "-[SUManagerClient deviceBootedAfterSplatUpdate]"
+ "-[SUManagerClient disableReserveSpace:completion:]"
+ "-[SUManagerClient disableReserveSpace:completion:]_block_invoke"
+ "-[SUManagerClient downloadDidFail:withError:]"
+ "-[SUManagerClient downloadDidFinish:]"
+ "-[SUManagerClient downloadDidFinish:withInstallPolicy:]"
+ "-[SUManagerClient downloadDidStart:]"
+ "-[SUManagerClient downloadProgressDidChange:]"
+ "-[SUManagerClient downloadWasInvalidatedForNewUpdateAvailable:]"
+ "-[SUManagerClient downloadWasInvalidatedForNewUpdatesAvailable:]"
+ "-[SUManagerClient handleUIForDDMDeclaration:]"
+ "-[SUManagerClient handleUIForDDMGlobalSettings:]"
+ "-[SUManagerClient inUserInteraction:]"
+ "-[SUManagerClient installDidFail:withError:]"
+ "-[SUManagerClient installDidFinish:]"
+ "-[SUManagerClient installDidStart:]"
+ "-[SUManagerClient installPolicyDidChange:]"
+ "-[SUManagerClient installTonightScheduled:operationID:]"
+ "-[SUManagerClient installWantsToStart:completion:]"
+ "-[SUManagerClient overrideSoftwareUpdateReserve:systemGrowthMarginSize:completion:]"
+ "-[SUManagerClient overrideSoftwareUpdateReserve:systemGrowthMarginSize:completion:]_block_invoke"
+ "-[SUManagerClient preferences:didChangePreference:toValue:]_block_invoke"
+ "-[SUManagerClient presentingRecommendedUpdate:shouldPresent:]"
+ "-[SUManagerClient rollbackDidFail:withError:]"
+ "-[SUManagerClient rollbackDidFinish:]"
+ "-[SUManagerClient rollbackDidStart:]"
+ "-[SUManagerClient rollbackReadyForReboot:]"
+ "-[SUManagerClient rollbackReadyToStart:options:completion:]"
+ "-[SUManagerClient rollbackSuggested:info:]"
+ "-[SUManagerClient scanDidCompleteForOptions:results:error:]"
+ "-[SUManagerClient scanDidCompleteWithNewUpdateAvailable:error:]"
+ "-[SUManagerClient scanRequestDidFinishForOptions:results:error:]"
+ "-[SUManagerClient scanRequestDidFinishForOptions:update:error:]"
+ "-[SUManagerClient scanRequestDidStartForOptions:]"
+ "-[SUManagerClient softwareUpdateReserveSizes:]"
+ "-[SUManagerClient softwareUpdateReserveSizes:]_block_invoke"
+ "-[SUManagerClient userWantsToDeferInstall]"
+ "-[SUManagerCore softwareUpdateReserveSizes]"
+ "-[SUManagerCore(Analytics) _createCoreAnalyticsEventWithCurrentDownloadFor:error:]"
+ "-[SUManagerCore(Analytics) _getAmountDataAvailable]"
+ "-[SUManagerCore(MDM) amendManagedScanOptions:withResponse:]"
+ "-[SUManagerCore(MDM) isManaged]"
+ "-[SUManagerCore(MDM) softwareUpdatePathRestriction]"
+ "-[SUManagerCore(MDM) updatesDelayPeriodSeconds]"
+ "-[SUManagerCore(Splat) eligibleRollbackWithOptions:]"
+ "-[SUManagerCore(Splat) isSplatOnlyUpdateRollbackSuggested]"
+ "-[SUManagerCore(Splat) isSplatRollbackEnabled]"
+ "-[SUManagerCore(Splat) splatUpdatesAllowed]"
+ "-[SUManagerServer autoInstallManager:didCancelOperation:]_block_invoke_2"
+ "-[SUManagerServer autoInstallManager:didExpireOperation:withError:]_block_invoke_2"
+ "-[SUManagerServer autoInstallManager:isReadyToInstall:withResult:]_block_invoke_2"
+ "-[SUManagerServer autoInstallManager:operationWasConsented:]_block_invoke_2"
+ "-[SUManagerServer autoInstallManager:passcodePolicyChanged:forOperation:]_block_invoke_2"
+ "-[SUManagerServer automaticDownloadDidFailToStartForNewUpdateAvailable:withError:]_block_invoke_2"
+ "-[SUManagerServer clearingSpaceForDownload:clearing:]_block_invoke_2"
+ "-[SUManagerServer disableReserveSpace:withResult:]_block_invoke"
+ "-[SUManagerServer downloadDidFail:withError:]_block_invoke_2"
+ "-[SUManagerServer downloadDidFinish:withInstallPolicy:]_block_invoke_3"
+ "-[SUManagerServer downloadDidStart:]_block_invoke_2"
+ "-[SUManagerServer downloadProgressDidChange:]_block_invoke_2"
+ "-[SUManagerServer downloadWasInvalidatedForNewUpdatesAvailable:]_block_invoke_2"
+ "-[SUManagerServer installDidFail:withError:]_block_invoke_3"
+ "-[SUManagerServer installDidFinish:]_block_invoke_3"
+ "-[SUManagerServer installDidStart:]_block_invoke_2"
+ "-[SUManagerServer installPolicyDidChange:]_block_invoke_2"
+ "-[SUManagerServer installTonightScheduled:]_block_invoke_2"
+ "-[SUManagerServer installWantsToStart:completion:]_block_invoke_2"
+ "-[SUManagerServer isAnyClientInUserInteraction:]_block_invoke_2"
+ "-[SUManagerServer managedInstallationRequested:]_block_invoke_2"
+ "-[SUManagerServer overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:]_block_invoke"
+ "-[SUManagerServer presentingRecommendedUpdate:shouldPresent:]_block_invoke_2"
+ "-[SUManagerServer rollbackDidFail:withError:]_block_invoke_2"
+ "-[SUManagerServer rollbackDidStart:]_block_invoke_2"
+ "-[SUManagerServer rollbackReadyForReboot:]_block_invoke_2"
+ "-[SUManagerServer rollbackReadyToStart:options:completion:]_block_invoke_2"
+ "-[SUManagerServer rollbackSucceeded:]_block_invoke_3"
+ "-[SUManagerServer rollbackSuggested:info:]_block_invoke_2"
+ "-[SUManagerServer scanDidCompleteForOptions:results:error:]_block_invoke_2"
+ "-[SUManagerServer scanDidCompleteWithNewUpdateAvailable:error:]_block_invoke_2"
+ "-[SUManagerServer scanRequestDidFinishForOptions:results:error:]_block_invoke_2"
+ "-[SUManagerServer scanRequestDidFinishForOptions:update:error:]_block_invoke_2"
+ "-[SUManagerServer scanRequestDidStartForOptions:]_block_invoke_2"
+ "-[SUManagerServer sendDDMDeclarationToUI:]_block_invoke_2"
+ "-[SUManagerServer sendDDMGlobalSettingsToUI:]_block_invoke_2"
+ "-[SUManagerServer softwareUpdateReserveSizes:]_block_invoke"
+ "-[SUManagerServer splatRollbackDetected:]_block_invoke_2"
+ "-[SUManagerServer splatUpdateDetected]_block_invoke_2"
+ "-[SUManagerServer userAskedToDeferInstall]_block_invoke_4"
+ "-[SUPreferences _loadPreferences:]_block_invoke"
+ "-[SUScanner scanForUpdates:complete:]"
+ "1@`"
+ "Analytics"
+ "CANCEL_UPDATE_BUTTON"
+ "Connection received %lu bytes of data."
+ "Connection received response: %ld"
+ "Discoverability"
+ "Download"
+ "Enable/Disable the reserve space feature"
+ "Failed to query for installed builds: %ld"
+ "Failed to query matching assetID: %@ QueryResult: %ld"
+ "Install"
+ "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@"
+ "Lost download task. Please try again."
+ "MDM"
+ "MobileAsset data processing failure. Please make sure you have at least UI Binary disclosure for the release you're trying to update to."
+ "MobileAsset found %lu installed build%s: assetIDs: %@"
+ "MobileAsset returned %lu matching assets"
+ "PreallocatedSpace"
+ "SUOverrideSessionIDRampingPortion"
+ "SUSController-installCompleted-retry"
+ "SUSController-installUpdateWithInstallOptions"
+ "SUSController-startDownloadWithOptions"
+ "SUSoftwareUpdateReserveDisabled"
+ "SUSoftwareUpdateReserveSize"
+ "SUSystemGrowthMarginSize"
+ "Scan"
+ "Setting software update reserve size to %@"
+ "Setting software update reserve space to %@"
+ "Setting systemGrowthMarginSize to %@"
+ "Signals"
+ "SoftwareUpdate"
+ "T@\"NSArray\",R,&,N,V_buttons"
+ "T@\"NSDictionary\",R,N,V_updateMetricEventFields"
+ "T@\"NSNumber\",&,N"
+ "T@\"NSString\",&,N,V_splatComboBuildVersion"
+ "T@\"NSString\",&,SsetSuggestedRollbackSplatVersion:"
+ "T@\"NSString\",R,&,N,V_message"
+ "T@\"NSString\",R,&,N,V_title"
+ "TB,N,GinstallTonightDisabled,S_setDisableInstallTonight:,V_disableInstallTonight"
+ "TB,N,SdisableSoftwareUpdateReserve:"
+ "TB,N,V_granularlyRamped"
+ "TB,N,V_rampEnabled"
+ "TQ,N,V_unentitledReserveAmount"
+ "To override the ramping portion of the session id"
+ "UUIDForSoftwareUpdate"
+ "Unable to cancel downloading asset: %ld"
+ "Unable to purge asset: %ld"
+ "Virtual device does not require installation keybag"
+ "[Auto download] Apple Internal: Downloading every 1 day"
+ "[Auto download] Beta: Downloading every 1 day"
+ "[Auto download]: Lockdown mode enabled: Downloading every 1 day"
+ "[PREFERENCES] Default set to override granular ramping to YES"
+ "[PREFERENCES] Default set to override ramping to YES"
+ "[PREFERENCES] Default set to override splatComboBuildVersion"
+ "[PREFERENCES] session id ramping portion is set to %@"
+ "[Space] %s Setting entitled space to %llu (%llu MB) and unentitled to %llu (%llu MB)"
+ "[Space] %s Setting entitled space to %llu (%llu MB) and unentitledSpace to %llu (%llu MB)"
+ "[Space] %s releasing entitled space and resume CD reserve monitoring"
+ "__NoStashbagCommit"
+ "_disableInstallTonight"
+ "_loadPreferences:"
+ "_setCachedObjectPreferenceForKey:value:"
+ "_setupSoftwareUpdateReserveDisabled"
+ "_unentitledReserveAmount"
+ "asset query failed: %ld"
+ "cacheDeleteDisableReserveSpace"
+ "cacheDeleteGetReserveSpace:withError:"
+ "cacheDeletePauseReserveSpace:unentitledSpace:withPurpose:"
+ "cacheDeleteResumeReserveSpace"
+ "cacheDeleteSetReserveSpace:systemGrowthMarginSize:"
+ "com.apple.softwareupdateservices.error"
+ "com.apple.softwareupdateservices.succeeded"
+ "disableReserveSpace:"
+ "disableReserveSpace:completion:"
+ "disableReserveSpace:withResult:"
+ "disableSoftwareUpdateReserve:"
+ "donateSUErrorToBiome:"
+ "donateSuccessToBiomeFor:"
+ "failed to download %@ catalog: %ld"
+ "getFreeSpaceAvailableForSoftwareUpdate:"
+ "initWithContentIdentifier:context:osBuild:userInfo:"
+ "isReturnToServiceModeActive"
+ "modelSpecificLocalizedStringKeyForKey:"
+ "override the reserve size for software update on the device"
+ "override the system growth estiamtion of the new software update"
+ "overrideSessionIDRampingPortion"
+ "overrideSoftwareUpdateReserve:systemGrowthMarginSize:"
+ "overrideSoftwareUpdateReserve:systemGrowthMarginSize:completion:"
+ "overrideSoftwareUpdateReserve:systemGrowthMarginSize:withResult:"
+ "queryMetaDataSync failed in _cleanupAllAssetsOfType: %ld"
+ "resumeReserveSpaceStateIfNeeded"
+ "sendEvent:"
+ "setBaseApplyOptions:"
+ "setReserveSpaceSizeOverride:"
+ "setSoftwareUpdateReserveSize:"
+ "setSystemGrowthMarginOverride:"
+ "setSystemGrowthMarginSize:"
+ "setUnentitledReserveAmount:"
+ "setUseReserveSpace:"
+ "softwareUpdateReserveDisabled"
+ "softwareUpdateReserveSize"
+ "softwareUpdateReserveSizes"
+ "softwareUpdateReserveSizes:"
+ "source"
+ "substringToIndex:"
+ "systemGrowthMarginSize"
+ "tryCreateDocumentationFromDocumentationAsset:"
+ "unentitledReserveAmount"
+ "v28@0:8B16@?<v@?B@\"NSError\">20"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?B@\"NSError\">32"
- "\n            ClientName: %@\n            downloadOnly: %@\n            autoDownoad: %@\n            userUpdateTonight: %@\n            allowUnrestrictedCellularDownload: %@\n            downloadFeeAgreementStatus: %@\n            termsAndConditionsAgreementStatus: %@\n            activeDownloadPolicyType: %@\n            enabledForCellular: %@\n            enabledForWifi: %@\n            enabledOnBatteryPower: %@\n            enabledForCellularRoaming: %@\n            descriptor: %@\n"
- "\n            Publisher: %@\n            HumanReadableUpdateName: %@\n            ProductSystemName: %@\n            ProductVersion: %@\n            ProductVersionExtra: %@\n            ProductBuildVersion: %@\n            PrerequisiteBuild: %@\n            PrerequisiteOS: %@\n            ReleaseType: %@\n            DownloadSize: %@\n            UnarchiveSize: %@\n            MSUPrepareSize: %@\n            PreparationSize: %@\n            InstallationSize: %@\n            PreSUStagingRequiredSize: %@\n            PreSUStagingOptionalSize: %@\n            UpdateType: %@\n            Downloadable: %@\n            DownloadableOverCellular: %@\n            AutoDownloadableOverCellular: %@\n            AutoUpdateEnabled: %@\n            StreamingZipCapable: %d\n            TotalRequiredFreeSpace: %@\n            Documentation: %@\n            SiriVoiceDeletion: %d\n            CDLevel4DeletionDisabled: %d\n            appDemotionDisabled: %d\n            maSuspensionDisabled: %d\n            installTonightDisabled: %d\n            rampEnabled: %d\n            granularlyRamped: %d\n            setupCritical: %@\n            criticalOutOfBoxOnly: %d\n            criticalDownloadPolicy: %@\n            releaseDate: %@\n            mdmDelayInterval: %@\n            assetID: %@\n            hideInstallAlert: %@\n            audienceType: %@\n            preferenceType: %@\n            upgradeType: %@\n            promoteAlternateUpdate: %@\n            isSplatOnly: %@\n            mandatoryUpdateEligible: %@\n            mandatoryUpdateVersionMin: %@\n            mandatoryUpdateVersionMax: %@\n            mandatoryUpdateOptional: %@\n            mandatoryUpdateRestrictedToOutOfTheBox: %@\n            forcePasscodeRequired: %@\n            allowAutoDownloadOnBattery: %@\n            autoDownloadOnBatteryDelay: %u\n            autoDownloadOnBatteryMinbattery: %u%%\n            isSplombo: %@\n            splatComboBuildVersion: %@"
- "\nEvent name: %@"
- "\nEvent time:  %@"
- "%@: %llu\n"
- "%s is called"
- "-[SUInstaller installUpdateWithInstallOptions:withResult:]_block_invoke"
- "-[SUInstaller isUpdateReadyForInstallation:]"
- "-[SUManagerClient totalPurgeableSpace]"
- "-[SUManagerCore _createCoreAnalyticsEventWithCurrentDownloadFor:error:]"
- "-[SUManagerCore _getAmountDataAvailable]"
- "-[SUManagerCore amendManagedScanOptions:withResponse:]"
- "-[SUManagerCore eligibleRollbackWithOptions:]"
- "-[SUManagerCore isManaged]"
- "-[SUManagerCore isSplatOnlyUpdateRollbackSuggested]"
- "-[SUManagerCore isSplatRollbackEnabled]"
- "-[SUManagerCore softwareUpdatePathRestriction]"
- "-[SUManagerCore splatUpdatesAllowed]"
- "-[SUManagerCore updatesDelayPeriodSeconds]"
- "-[SUPreferences _loadPreferences]_block_invoke"
- "-[SUScanner scanForUpdates:shouldUseDDMInState:complete:]"
- "/Library/SoftwareUpdate/deletedAssets.plist"
- "/private/var"
- "@\"SUAnalyticsManager\"16@0:8"
- "Adopted potentialNextSessionID as new sessionID: %@"
- "Alarm %@ is on AutoInstall alarm blacklist. Ignoring alarm"
- "B32@0:8@\"SURollbackSuggestionInfo\"16@?<v@?B@\"NSError\">24"
- "CACHE_DELETE_AMOUNT"
- "CACHE_DELETE_URGENCY"
- "CACHE_DELETE_VOLUME"
- "Connection received %d bytes of data."
- "Connection received response: %d"
- "Created new potentialNextSessionID: %@"
- "Created new sessionID: %@"
- "Creating potentialNextSessionID when no sessionID"
- "Default set to override granular ramping to YES"
- "Default set to override ramping to YES"
- "Default set to override splatComboBuildVersion"
- "Deleting %llu (%@)\n"
- "Event is scheduled before provided time"
- "Failed to create ASDPurgeableAppRequest"
- "Failed to create ASDPurgeableAppRequestOptions"
- "Failed to delete asset (%@) assetID: %@\n"
- "Failed to query for installed builds: %d"
- "Failed to query matching assetID: %@ QueryResult: %d"
- "Failed to write deleted asset plist to disk"
- "LastDownload: %@            \npreferredLastScannedCoreDescriptor: %@            \nalternateLastScannedCoreDescriptor: %@            \nFailedPatchBuildVersions: %@            \nScheduledManualDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadWifiPeriodEndTime: %@            \nScheduledAutoDownloadPolicyChangeTime: %@            \nLastScanDate: %@            \nLastAutoDownloadDate: %@            \nNeedsOneTimeAutoDownloadRetry: %@            \nLastProductVersion: %@            \nLastProductBuild: %@            \nLastProductType: %@            \nLastReleaseType: %@            \nLastSplatRestoreVersion: %@            \nLastAutoInstallOperationModel: %@            \nManagedDeviceDelay: %@            \nInstallPolicy: %@            \nMandatoryUpdateDict: %@            \nLastRollbackRecommendedBuildVersion: %@            \rolledBackBuildVersions: %@            \nsessionID: %@            \nlastDeletedAssetID: %@            \nlastAssetAudience: %@            \nappliedSate: %@            \nunderExclusiveControl: %@            \nLastRecommendedUpdateVersion: %@            \nLastRecommendedUpdateInterval: %@            \nLastRecommendedUpdateDiscoveryDate: %@            \nUpdateDiscoveryDates: %@"
- "MobileAsset data processing failure."
- "MobileAsset found %d installed build%s: assetIDs: %@"
- "MobileAsset returned %d matching assets"
- "PersistentConnectionMaintenance"
- "SUOverrideScanSessionIDRampingPortion"
- "T@\"NSArray\",&,N,V_buttons"
- "T@\"NSDictionary\",&,N,V_updateMetricEventFields"
- "T@\"NSString\",&,N,GsplatComboBuildVersion,V_splatComboBuildVersion"
- "T@\"NSString\",&,N,V_potentialNextSessionID"
- "T@\"NSString\",SsetSuggestedRollbackSplatVersion:"
- "T@\"SUAnalyticsManager\",&,N"
- "TB,N,GgranularlyRamped,V_granularlyRamped"
- "TB,N,GinstallTonightDisabled,S_setDisableInstallTonight:,V_disableIntallTonight"
- "TB,N,GrampEnabled,V_rampEnabled"
- "The ramping portion is set to %@ by default"
- "To override the ramping portion of a scan session id"
- "URLIfFileExists:"
- "Unable to cancel downloading asset: %d"
- "Unable to purge asset: %d"
- "UserVisible"
- "[Auto scan] Apple Internal: Downloading every 1 day"
- "[Auto scan] Customer: Downloading every 5 days"
- "[Auto scan]: Lockdown mode enabled: Downloading every 1 day"
- "[LEGACY]%@,%@,%@,%@,%@,%@,%@,%@"
- "_disableIntallTonight"
- "_loadPreferences"
- "_potentialNextSessionID"
- "addObjectsFromArray:"
- "adoptPotentialSessionID"
- "alarmSetBeforeDate:"
- "analyticsManager"
- "appDemoteableSpace"
- "appDemotionIsEnabled"
- "appDemotionSettingQueue"
- "arrayWithContentsOfFile:"
- "asset query failed: %d"
- "autoOff"
- "autoOn"
- "bg"
- "com.apple.MobileAsset.VoiceServices.CustomVoice"
- "com.apple.MobileAsset.VoiceServices.GryphonVoice"
- "com.apple.MobileAsset.VoiceServicesVocalizerVoice"
- "com.apple.donotdisturb.server"
- "com.apple.softwareupdateservices.appDemotionSettingQueue"
- "com.apple.softwareupdateservicesd.activity"
- "createSessionID"
- "createpotentialNextSessionID"
- "enableAppDemotion:"
- "failed to download %@ catalog: %d"
- "failed to query metadata: %ld"
- "false"
- "fg"
- "fileSystemRepresentation"
- "isUpdateReadyForInstallationWithReplyHandler:"
- "loading saved sessionID: %@"
- "overrideScanSessionIDRampingPortion"
- "potentialNextSessionID"
- "purgeableSize"
- "queryMetaDataSync failed in _cleanupAllAssetsOfType: %d"
- "request for purgeable app space failed. Result: %d Error: %@"
- "scanForUpdates:shouldUseDDMInState:complete:"
- "scheduledby"
- "setAnalyticsManager:"
- "setButtons:"
- "setPotentialNextSessionID:"
- "setUpdateMetricEventFields:"
- "setUrgency:"
- "setVolume:"
- "startWithCompletionBlock:"
- "substringWithRange:"
- "time"
- "toggleADOff"
- "toggleADOn"
- "toggleAIOff"
- "toggleAIOn"
- "toggleAIRSROff"
- "toggleAIRSROn"
- "toggleAISDFOff"
- "toggleAISDFOn"
- "totalPurgeableSpace"
- "totalPurgeableSpace:"
- "true"
- "v24@0:8@\"SUAnalyticsManager\"16"
- "v24@0:8@?<v@?BB@\"NSError\">16"
- "v28@?0B8@\"ASDPurgeableAppResponse\"12@\"NSError\"20"
- "v36@0:8@\"SUScanOptions\"16B24@?<v@?@\"SUScanResults\"@\"NSError\">28"
- "wasPurgeable"

```
