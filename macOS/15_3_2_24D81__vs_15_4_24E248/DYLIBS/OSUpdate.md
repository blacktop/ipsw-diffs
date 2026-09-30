## OSUpdate

> `/System/Library/PrivateFrameworks/OSUpdate.framework/Versions/A/OSUpdate`

```diff

-2078.80.2.0.2
-  __TEXT.__text: 0x86ebc
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x5a08
+2078.101.1.0.0
+  __TEXT.__text: 0x8e4c0
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x6e34
   __TEXT.__const: 0x191
-  __TEXT.__cstring: 0x5da5
-  __TEXT.__gcc_except_tab: 0x2018
-  __TEXT.__oslogstring: 0xaef8
+  __TEXT.__cstring: 0x64ae
+  __TEXT.__oslogstring: 0xbe41
+  __TEXT.__gcc_except_tab: 0x2028
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1b68
-  __TEXT.__objc_classname: 0x7b1
-  __TEXT.__objc_methname: 0x13702
-  __TEXT.__objc_methtype: 0x1f24
-  __TEXT.__objc_stubs: 0xd3c0
-  __DATA_CONST.__got: 0x978
-  __DATA_CONST.__const: 0xc00
-  __DATA_CONST.__objc_classlist: 0x200
+  __TEXT.__unwind_info: 0x1d00
+  __TEXT.__objc_classname: 0x81b
+  __TEXT.__objc_methname: 0x150d0
+  __TEXT.__objc_methtype: 0x20a4
+  __TEXT.__objc_stubs: 0xe340
+  __DATA_CONST.__got: 0x9d8
+  __DATA_CONST.__const: 0xc48
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4000
+  __DATA_CONST.__objc_selrefs: 0x4518
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x180
-  __DATA_CONST.__objc_arraydata: 0x3f0
-  __AUTH_CONST.__auth_got: 0x550
-  __AUTH_CONST.__const: 0x24e0
-  __AUTH_CONST.__cfstring: 0x4d80
-  __AUTH_CONST.__objc_const: 0x94b0
-  __AUTH_CONST.__objc_intobj: 0x180
+  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_arraydata: 0x3f8
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__const: 0x2730
+  __AUTH_CONST.__cfstring: 0x52c0
+  __AUTH_CONST.__objc_const: 0x8928
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x190
-  __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x578
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x654
   __DATA.__data: 0x612
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x90
   __DATA_DIRTY.__objc_data: 0xa50
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x58
+  - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/Versions/A/AppleAccount
+  - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/BridgeOSSoftwareUpdate.framework/Versions/A/BridgeOSSoftwareUpdate
   - /System/Library/PrivateFrameworks/ConfigurationProfiles.framework/Versions/A/ConfigurationProfiles
   - /System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet

   - /System/Library/PrivateFrameworks/IASUtilities.framework/Versions/A/IASUtilities
   - /System/Library/PrivateFrameworks/LocalAuthenticationUI.framework/Versions/A/LocalAuthenticationUI
   - /System/Library/PrivateFrameworks/MobileAsset.framework/Versions/A/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
+  - /System/Library/PrivateFrameworks/OSIntelligence.framework/Versions/A/OSIntelligence
   - /System/Library/PrivateFrameworks/PackageUIKit.framework/Versions/A/PackageUIKit
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbootpolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70E60ABA-80FA-39FA-8452-59DD641E4627
-  Functions: 2699
-  Symbols:   6525
-  CStrings:  5436
+  UUID: 6D524FEC-7D2E-37EF-89DC-3B2541A68E99
+  Functions: 2908
+  Symbols:   6958
+  CStrings:  5871
 
Symbols:
+ +[SUOSUAuthorizationController sharedInstance].cold.1
+ +[SUOSUCloudDeviceManager sharedManager]
+ +[SUOSUDDMController sharedInstance].cold.1
+ +[SUOSUFollowUpHelper sharedInstance].cold.1
+ +[SUOSUInstalledUpdateJournal sharedJournal].cold.1
+ +[SUOSULoginCredentialPolicy lastVendedPolicyMode]
+ +[SUOSULoginCredentialPolicy setLastVendedPolicyMode:]
+ +[SUOSUServiceDaemon sharedInstance].cold.1
+ +[SUOSUUpdateController sharedInstance].cold.1
+ +[SUOSUUpdatesAvailablePolicy _reminderDaysForCount:]
+ +[SUOSUUpdatesAvailablePolicy _reminderDaysForCount:finalNotification:]
+ +[SUOSUUserPrefs sharedInstance].cold.1
+ +[SUOSUUtilities appsThatWillPreventRestart]
+ +[SUOSUUtilities parseProductMarketingVersion:systemVersion:]
+ +[SUOSUUtilities stringForSystemVersion:]
+ -[SUOSUClient cacheDeletePurgeableSpaceWithCompletionHandler:]
+ -[SUOSUCloudDevice .cxx_destruct]
+ -[SUOSUCloudDevice description]
+ -[SUOSUCloudDevice initWithName:operatingSystemName:operatingSystemVersion:]
+ -[SUOSUCloudDevice name]
+ -[SUOSUCloudDevice operatingSystemName]
+ -[SUOSUCloudDevice operatingSystemVersion]
+ -[SUOSUCloudDevice setName:]
+ -[SUOSUCloudDevice setOperatingSystemName:]
+ -[SUOSUCloudDevice setOperatingSystemVersion:]
+ -[SUOSUCloudDeviceManager .cxx_destruct]
+ -[SUOSUCloudDeviceManager _productNameForModel:]
+ -[SUOSUCloudDeviceManager cacheDate]
+ -[SUOSUCloudDeviceManager cachedDevices]
+ -[SUOSUCloudDeviceManager devices]
+ -[SUOSUCloudDeviceManager devices].cold.1
+ -[SUOSUCloudDeviceManager setCacheDate:]
+ -[SUOSUCloudDeviceManager setCachedDevices:]
+ -[SUOSUExternalUpdateProvider queueAllUpdatesForAutoInstallTonightWithReason:]
+ -[SUOSUInactivityPredictor .cxx_destruct]
+ -[SUOSUInactivityPredictor client]
+ -[SUOSUInactivityPredictor endDate]
+ -[SUOSUInactivityPredictor initWithClient:startDate:endDate:]
+ -[SUOSUInactivityPredictor initWithStartDate:endDate:]
+ -[SUOSUInactivityPredictor predictedInactivityDate]
+ -[SUOSUInactivityPredictor predictedInactivityDate].cold.1
+ -[SUOSUInactivityPredictor setClient:]
+ -[SUOSUInactivityPredictor setEndDate:]
+ -[SUOSUInactivityPredictor setStartDate:]
+ -[SUOSUInactivityPredictor startDate]
+ -[SUOSUInstallTonightManager queueDescriptorForInstallTonight:withReason:stashState:]
+ -[SUOSULoginCredentialCacheInfo .cxx_destruct]
+ -[SUOSULoginCredentialCacheInfo descriptor]
+ -[SUOSULoginCredentialCacheInfo downloadedAndPrepared]
+ -[SUOSULoginCredentialCacheInfo initWithDescriptor:downloadedAndPrepared:]
+ -[SUOSULoginCredentialCacheInfo setDescriptor:]
+ -[SUOSULoginCredentialCacheInfo setDownloadedAndPrepared:]
+ -[SUOSULoginCredentialPolicyManager _allowedToRequireCredentialsForProductKey:]
+ -[SUOSULoginCredentialPolicyManager _isUpdateDownloadedAndPreparedWithCompletion:]
+ -[SUOSULoginCredentialPolicyManager _modeFromCachedInfo:]
+ -[SUOSULoginCredentialPolicyManager _willAutoInstallDescriptor:withProductKey:]
+ -[SUOSULoginCredentialPolicyManager cachedInfo]
+ -[SUOSULoginCredentialPolicyManager cachedMode]
+ -[SUOSULoginCredentialPolicyManager defaultRequiredInterval]
+ -[SUOSULoginCredentialPolicyManager getCurrentLoginCredentialPolicyWithCompletion:]
+ -[SUOSULoginCredentialPolicyManager initWithSharedPrefs:msuController:installTonightManager:]
+ -[SUOSULoginCredentialPolicyManager installTonightManager]
+ -[SUOSULoginCredentialPolicyManager msuController]
+ -[SUOSULoginCredentialPolicyManager refreshCachedMode]
+ -[SUOSULoginCredentialPolicyManager setCachedInfo:]
+ -[SUOSULoginCredentialPolicyManager setDefaultRequiredInterval:]
+ -[SUOSULoginCredentialPolicyManager setInstallTonightManager:]
+ -[SUOSULoginCredentialPolicyManager setMsuController:]
+ -[SUOSULoginCredentialPolicyManager setStaleUpdateInterval:]
+ -[SUOSULoginCredentialPolicyManager setStaleUpdateRequiredInterval:]
+ -[SUOSULoginCredentialPolicyManager staleUpdateInterval]
+ -[SUOSULoginCredentialPolicyManager staleUpdateRequiredInterval]
+ -[SUOSUMacBuddyController client:installRequiresUserAction:details:completionHandler:].cold.1
+ -[SUOSUMajorProductStubImpl allowedToUseInstallLater]
+ -[SUOSUMajorProductStubImpl isSplatCombo]
+ -[SUOSUMajorProductStubImpl postInstallAction]
+ -[SUOSUMajorProductStubImpl shortAttributedDescription]
+ -[SUOSUMajorProductStubImpl splatAppliedRestartNow]
+ -[SUOSUManagedServiceDaemon invalidAndRemoveOldDeclarations]
+ -[SUOSUMobileSoftwareUpdateController _configureOverridesForOptionalPSUSDownload:forDescriptor:]
+ -[SUOSUMobileSoftwareUpdateController _configureOverridesForOptionalPSUSDownload:forDescriptor:].cold.1
+ -[SUOSUMobileSoftwareUpdateController _shouldIgnoreDescriptorFromScan:withOptions:]
+ -[SUOSUMobileSoftwareUpdateController clientID]
+ -[SUOSUMobileSoftwareUpdateController setClientID:]
+ -[SUOSUNotificationManagerController evaluateAndPostInstallTonightAppCloseNotification]
+ -[SUOSUNotificationManagerController queueAllUpdatesForAutoInstallTonightWithReason:]
+ -[SUOSUPostLogoutInstallOperation _createPreUpdateAPFSSnapshot].cold.3
+ -[SUOSUProduct alignediOSMajorVersion]
+ -[SUOSUProduct deviceCompatibilityNotificationBodyString]
+ -[SUOSUProduct deviceCompatibilityNotificationTitleString]
+ -[SUOSUProduct disableDeviceCompatibilityNotification]
+ -[SUOSUProduct disableSecurityAdvisoryNotification]
+ -[SUOSUProduct securityAdvisoryNotificationBodyString]
+ -[SUOSUProduct securityAdvisoryNotificationTitleString]
+ -[SUOSUProduct setAlignediOSMajorVersion:]
+ -[SUOSUProductStub allowedToUseInstallTonight]
+ -[SUOSUProductStub init:]
+ -[SUOSUProductStub isSplatCombo]
+ -[SUOSUProductStub loadLongSummary]
+ -[SUOSUProductStub loadMajorIcon]
+ -[SUOSUProductStub loadMinorIcon]
+ -[SUOSUProductStub loadShortSummary]
+ -[SUOSUProductStub postInstallAction]
+ -[SUOSUProductStub productVersionExtra]
+ -[SUOSUProductStub setAllowedToUseInstallTonight:]
+ -[SUOSUProductStub setIsSplatCombo:]
+ -[SUOSUProductStub setPostInstallAction:]
+ -[SUOSUProductStub setProductVersionExtra:]
+ -[SUOSUProductStub setShortAttributedDescription:]
+ -[SUOSUProductStub setShortDescription:]
+ -[SUOSUProductStub setSplatAppliedUpdateNow:]
+ -[SUOSUProductStub shortAttributedDescription]
+ -[SUOSUProductStub shortDescription]
+ -[SUOSUProductStub splatAppliedUpdateNow]
+ -[SUOSUProductStubImpl allowedToUseInstallLater]
+ -[SUOSUProductStubImpl isSplatCombo]
+ -[SUOSUProductStubImpl postInstallAction]
+ -[SUOSUProductStubImpl productVersionExtra]
+ -[SUOSUProductStubImpl shortAttributedDescription]
+ -[SUOSUProductStubImpl splatAppliedRestartNow]
+ -[SUOSUServiceClient evaluateAndPostInstallTonightAppCloseNotification]
+ -[SUOSUServiceClient queueAllUpdatesForAutoInstallTonightWithReason:]
+ -[SUOSUServiceClientManager .cxx_destruct]
+ -[SUOSUServiceClientManager activeNotificationManagerClient]
+ -[SUOSUServiceClientManager addClient:]
+ -[SUOSUServiceClientManager allClients]
+ -[SUOSUServiceClientManager clients]
+ -[SUOSUServiceClientManager init]
+ -[SUOSUServiceClientManager notificationManagerClients]
+ -[SUOSUServiceClientManager removeClient:]
+ -[SUOSUServiceClientManager setClients:]
+ -[SUOSUServiceClientManager setSunmClients:]
+ -[SUOSUServiceClientManager sunmClients]
+ -[SUOSUServiceDaemon _cancelScheduledAppCloseNotification]
+ -[SUOSUServiceDaemon _mobileKeyBagStashStateForUser:]
+ -[SUOSUServiceDaemon _postAppCloseNotificationIfAppropriate]
+ -[SUOSUServiceDaemon _queue_disarmLaterObserver]
+ -[SUOSUServiceDaemon _setMobileSoftwareUpdateDescriptorToInstallLater:withReason:stashState:]
+ -[SUOSUServiceDaemon appCloseNotificationTimerSource]
+ -[SUOSUServiceDaemon attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:completion:]
+ -[SUOSUServiceDaemon cacheDeletePurgeableSpaceWithCompletionHandler:]
+ -[SUOSUServiceDaemon cancelInstallTonight]
+ -[SUOSUServiceDaemon clientManager]
+ -[SUOSUServiceDaemon estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:completion:]
+ -[SUOSUServiceDaemon evaluateAndPostInstallTonightAppCloseNotification]
+ -[SUOSUServiceDaemon invalidAndRemoveOldDeclarations]
+ -[SUOSUServiceDaemon mobileKeyBagStashStateForUser:completion:]
+ -[SUOSUServiceDaemon queueAllUpdatesForAutoInstallTonightWithReason:]
+ -[SUOSUServiceDaemon refreshCachedLoginCredentialHarvestingMode]
+ -[SUOSUServiceDaemon scheduleUpdatesAvailableBSDNotification]
+ -[SUOSUServiceDaemon setAppCloseNotificationTimerSource:]
+ -[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]
+ -[SUOSUServiceDaemon setClientManager:]
+ -[SUOSUServiceDaemon setMobileSoftwareUpdateDescriptorToInstallLater:withReason:userId:]
+ -[SUOSUServiceDaemon setUpdatesAvailableNotificationTimerSource:]
+ -[SUOSUServiceDaemon suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:completion:]
+ -[SUOSUServiceDaemon updatesAvailableNotificationTimerSource]
+ -[SUOSUShimController _handleSuccessfullyCompletedScan]
+ -[SUOSUShimController _insufficientDiskSpaceErrorForProducts:spaceRequired:underlyingError:]
+ -[SUOSUShimController _promptAndSuspendMobileAssetIfNecessaryWithFreeSpaceRequired:suspendedMobileAsset:error:]
+ -[SUOSUShimController _promptAndSuspendMobileAssetIfNecessaryWithFreeSpaceRequired:suspendedMobileAsset:error:].cold.1
+ -[SUOSUShimController _reclaimDiskSpaceIfNecssaryWithBytesRequired:bytesReclaimed:error:]
+ -[SUOSUShimController _reclaimDiskSpaceIfNecssaryWithBytesRequired:bytesReclaimed:error:].cold.1
+ -[SUOSUShimController _refreshAllAvailableUpdatesAndNotifyDelegate]
+ -[SUOSUShimController _registerForScanCompletionNotification:outToken:]
+ -[SUOSUShimController _registerForScanCompletionNotification:outToken:].cold.1
+ -[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:].cold.1
+ -[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:].cold.2
+ -[SUOSUShimController backgroundScanNotifyToken]
+ -[SUOSUShimController cacheDeletePurgeableSpaceWithCompletionHandler:]
+ -[SUOSUShimController clientScanNotifyToken]
+ -[SUOSUShimController setBackgroundScanNotifyToken:]
+ -[SUOSUShimController setClientScanNotifyToken:]
+ -[SUOSUTelemetryDoItLaterEvent addCredentialHarvestingInfoWithStashState:]
+ -[SUOSUTelemetryDoItLaterEvent collectCredentialHarvestingInfo]
+ -[SUOSUTelemetryDoItLaterEvent setCollectCredentialHarvestingInfo:]
+ -[SUOSUTelemetryDoItLaterEvent setStashState:]
+ -[SUOSUTelemetryDoItLaterEvent stashState]
+ -[SUOSUTelemetryEvent appendCredentialHarvestingInfoWithSharedPrefs:stashState:toDict:]
+ -[SUOSUTelemetryQueueForInstallTonightEvent initWithProduct:reason:stashState:sharedPrefs:]
+ -[SUOSUTelemetryQueueForInstallTonightEvent setStashState:]
+ -[SUOSUTelemetryQueueForInstallTonightEvent stashState]
+ -[SUOSUUpdateController _commitStashOnlyForDescriptor:withError:]
+ -[SUOSUUpdateController _setIdleSleepPowerAssertion:]
+ -[SUOSUUpdateController attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:error:]
+ -[SUOSUUpdateController cacheDeletePurgeableSpaceWithCompletionHandler:]
+ -[SUOSUUpdateController cancelInstallTonight]
+ -[SUOSUUpdateController estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:outEvictableBytes:error:]
+ -[SUOSUUpdateController evaluateAndPostInstallTonightAppCloseNotification]
+ -[SUOSUUpdateController mobileKeyBagStashStateForUser:]
+ -[SUOSUUpdateController queueAllUpdatesForAutoInstallTonightWithReason:]
+ -[SUOSUUpdateController setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]
+ -[SUOSUUpdateController suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:error:]
+ -[SUOSUUpdatesAvailablePolicy .cxx_destruct]
+ -[SUOSUUpdatesAvailablePolicy _determineEligibleProducts]
+ -[SUOSUUpdatesAvailablePolicy _determineNotificationInterval]
+ -[SUOSUUpdatesAvailablePolicy _determineNotificationType]
+ -[SUOSUUpdatesAvailablePolicy _nowExceedsLastNotificationDate]
+ -[SUOSUUpdatesAvailablePolicy _shouldShowDeviceCompatibilityNotificationForDevice:]
+ -[SUOSUUpdatesAvailablePolicy _shouldShowNotificationWithReason:]
+ -[SUOSUUpdatesAvailablePolicy _shouldShowSecurityAdvisoryNotification]
+ -[SUOSUUpdatesAvailablePolicy _shouldShowSecurityAdvisoryNotification].cold.1
+ -[SUOSUUpdatesAvailablePolicy alignedCloudDevice]
+ -[SUOSUUpdatesAvailablePolicy alreadyPostedFinalNotification]
+ -[SUOSUUpdatesAvailablePolicy autoDownloadEnabled]
+ -[SUOSUUpdatesAvailablePolicy availableProductsDownloaded]
+ -[SUOSUUpdatesAvailablePolicy availableProducts]
+ -[SUOSUUpdatesAvailablePolicy cloudDevices]
+ -[SUOSUUpdatesAvailablePolicy currentOSVersion]
+ -[SUOSUUpdatesAvailablePolicy ddmEnforcedWithin24Hours]
+ -[SUOSUUpdatesAvailablePolicy eligibleProducts]
+ -[SUOSUUpdatesAvailablePolicy firstInstallTonightDates]
+ -[SUOSUUpdatesAvailablePolicy init]
+ -[SUOSUUpdatesAvailablePolicy installInProgress]
+ -[SUOSUUpdatesAvailablePolicy installTonightArmed]
+ -[SUOSUUpdatesAvailablePolicy lastNotificationDate]
+ -[SUOSUUpdatesAvailablePolicy lastNotificationProductKey]
+ -[SUOSUUpdatesAvailablePolicy majorOSUpdatesManaged]
+ -[SUOSUUpdatesAvailablePolicy majorProduct]
+ -[SUOSUUpdatesAvailablePolicy minimumNotificationIntervalOverride]
+ -[SUOSUUpdatesAvailablePolicy minimumNotificationInterval]
+ -[SUOSUUpdatesAvailablePolicy minorProduct]
+ -[SUOSUUpdatesAvailablePolicy notificationCount]
+ -[SUOSUUpdatesAvailablePolicy notificationsDisabled]
+ -[SUOSUUpdatesAvailablePolicy offerLater]
+ -[SUOSUUpdatesAvailablePolicy primaryProduct]
+ -[SUOSUUpdatesAvailablePolicy restartRequired]
+ -[SUOSUUpdatesAvailablePolicy setAlignedCloudDevice:]
+ -[SUOSUUpdatesAvailablePolicy setAlreadyPostedFinalNotification:]
+ -[SUOSUUpdatesAvailablePolicy setAutoDownloadEnabled:]
+ -[SUOSUUpdatesAvailablePolicy setAvailableProducts:]
+ -[SUOSUUpdatesAvailablePolicy setAvailableProductsDownloaded:]
+ -[SUOSUUpdatesAvailablePolicy setCloudDevices:]
+ -[SUOSUUpdatesAvailablePolicy setCurrentOSVersion:]
+ -[SUOSUUpdatesAvailablePolicy setDdmEnforcedWithin24Hours:]
+ -[SUOSUUpdatesAvailablePolicy setEligibleProducts:]
+ -[SUOSUUpdatesAvailablePolicy setFirstInstallTonightDates:]
+ -[SUOSUUpdatesAvailablePolicy setInstallInProgress:]
+ -[SUOSUUpdatesAvailablePolicy setInstallTonightArmed:]
+ -[SUOSUUpdatesAvailablePolicy setLastNotificationDate:]
+ -[SUOSUUpdatesAvailablePolicy setLastNotificationProductKey:]
+ -[SUOSUUpdatesAvailablePolicy setMajorOSUpdatesManaged:]
+ -[SUOSUUpdatesAvailablePolicy setMajorProduct:]
+ -[SUOSUUpdatesAvailablePolicy setMinimumNotificationInterval:]
+ -[SUOSUUpdatesAvailablePolicy setMinimumNotificationIntervalOverride:]
+ -[SUOSUUpdatesAvailablePolicy setMinorProduct:]
+ -[SUOSUUpdatesAvailablePolicy setNotificationCount:]
+ -[SUOSUUpdatesAvailablePolicy setNotificationsDisabled:]
+ -[SUOSUUpdatesAvailablePolicy setOfferLater:]
+ -[SUOSUUpdatesAvailablePolicy setRestartRequired:]
+ -[SUOSUUpdatesAvailablePolicy setSettingsIsActive:]
+ -[SUOSUUpdatesAvailablePolicy setSetupAssistantIsActive:]
+ -[SUOSUUpdatesAvailablePolicy setSplatAppliedRestartNow:]
+ -[SUOSUUpdatesAvailablePolicy setSplatProduct:]
+ -[SUOSUUpdatesAvailablePolicy settingsIsActive]
+ -[SUOSUUpdatesAvailablePolicy setupAssistantIsActive]
+ -[SUOSUUpdatesAvailablePolicy shouldShowNotification:]
+ -[SUOSUUpdatesAvailablePolicy splatAppliedRestartNow]
+ -[SUOSUUpdatesAvailablePolicy splatProduct]
+ -[SUOSUUserPrefs availableUpdatesNotificationMinimumIntervalOverride]
+ -[SUOSUUserPrefs fakeCloudDevices]
+ -[SUOSUUserPrefs fakeCloudDevices].cold.1
+ -[SUOSUUserPrefs fakeCurrentOperatingSystemVersion:]
+ -[SUOSUUserPrefs recordPostedUpdatesAvailableNotificationWithProduct:]
+ -[SUOSUUserPrefs updatesAvailableNotificationCount]
+ -[SUOSUUserPrefs updatesAvailableNotificationProductKey]
+ ACMContextGetExternalForm.cold.1
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table119
+ GCC_except_table123
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table140
+ GCC_except_table144
+ GCC_except_table152
+ GCC_except_table158
+ GCC_except_table160
+ GCC_except_table162
+ GCC_except_table164
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table183
+ GCC_except_table195
+ GCC_except_table197
+ GCC_except_table20
+ GCC_except_table200
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table227
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table254
+ GCC_except_table257
+ GCC_except_table265
+ GCC_except_table284
+ GCC_except_table30
+ GCC_except_table301
+ GCC_except_table312
+ GCC_except_table313
+ GCC_except_table385
+ GCC_except_table393
+ GCC_except_table411
+ GCC_except_table413
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table58
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table92
+ GCC_except_table94
+ GCC_except_table98
+ OBJC_IVAR_$_SUOSUCloudDevice._name
+ OBJC_IVAR_$_SUOSUCloudDevice._operatingSystemName
+ OBJC_IVAR_$_SUOSUCloudDevice._operatingSystemVersion
+ OBJC_IVAR_$_SUOSUCloudDeviceManager._cacheDate
+ OBJC_IVAR_$_SUOSUCloudDeviceManager._cachedDevices
+ OBJC_IVAR_$_SUOSUInactivityPredictor._client
+ OBJC_IVAR_$_SUOSUInactivityPredictor._endDate
+ OBJC_IVAR_$_SUOSUInactivityPredictor._startDate
+ OBJC_IVAR_$_SUOSULoginCredentialCacheInfo._descriptor
+ OBJC_IVAR_$_SUOSULoginCredentialCacheInfo._downloadedAndPrepared
+ OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._cachedInfo
+ OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._defaultRequiredInterval
+ OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._installTonightManager
+ OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._msuController
+ OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._staleUpdateInterval
+ OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._staleUpdateRequiredInterval
+ OBJC_IVAR_$_SUOSUMobileSoftwareUpdateController._clientID
+ OBJC_IVAR_$_SUOSUProduct._alignediOSMajorVersion
+ OBJC_IVAR_$_SUOSUProduct._deviceCompatibilityNotificationBodyString
+ OBJC_IVAR_$_SUOSUProduct._deviceCompatibilityNotificationTitleString
+ OBJC_IVAR_$_SUOSUProduct._disableDeviceCompatibilityNotification
+ OBJC_IVAR_$_SUOSUProduct._disableSecurityAdvisoryNotification
+ OBJC_IVAR_$_SUOSUProduct._securityAdvisoryNotificationBodyString
+ OBJC_IVAR_$_SUOSUProduct._securityAdvisoryNotificationTitleString
+ OBJC_IVAR_$_SUOSUProductStub._allowedToUseInstallTonight
+ OBJC_IVAR_$_SUOSUProductStub._isSplatCombo
+ OBJC_IVAR_$_SUOSUProductStub._postInstallAction
+ OBJC_IVAR_$_SUOSUProductStub._productVersionExtra
+ OBJC_IVAR_$_SUOSUProductStub._shortAttributedDescription
+ OBJC_IVAR_$_SUOSUProductStub._shortDescription
+ OBJC_IVAR_$_SUOSUProductStub._splatAppliedUpdateNow
+ OBJC_IVAR_$_SUOSUServiceClientManager._clients
+ OBJC_IVAR_$_SUOSUServiceClientManager._sunmClients
+ OBJC_IVAR_$_SUOSUServiceDaemon._appCloseNotificationTimerSource
+ OBJC_IVAR_$_SUOSUServiceDaemon._clientManager
+ OBJC_IVAR_$_SUOSUServiceDaemon._updatesAvailableNotificationTimerSource
+ OBJC_IVAR_$_SUOSUShimController._backgroundScanNotifyToken
+ OBJC_IVAR_$_SUOSUShimController._clientScanNotifyToken
+ OBJC_IVAR_$_SUOSUTelemetryDoItLaterEvent._collectCredentialHarvestingInfo
+ OBJC_IVAR_$_SUOSUTelemetryDoItLaterEvent._stashState
+ OBJC_IVAR_$_SUOSUTelemetryQueueForInstallTonightEvent._stashState
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._alignedCloudDevice
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._alreadyPostedFinalNotification
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._autoDownloadEnabled
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._availableProducts
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._availableProductsDownloaded
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._cloudDevices
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._currentOSVersion
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._ddmEnforcedWithin24Hours
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._eligibleProducts
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._firstInstallTonightDates
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._installInProgress
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._installTonightArmed
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._lastNotificationDate
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._lastNotificationProductKey
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._majorOSUpdatesManaged
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._majorProduct
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._minimumNotificationInterval
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._minimumNotificationIntervalOverride
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._minorProduct
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._notificationCount
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._notificationsDisabled
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._offerLater
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._restartRequired
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._settingsIsActive
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._setupAssistantIsActive
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._splatAppliedRestartNow
+ OBJC_IVAR_$_SUOSUUpdatesAvailablePolicy._splatProduct
+ _AKServiceNameiCloud
+ _MKBKeyBagKeyStashVerifyWithOpts
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_AKAppleIDAuthenticationController
+ _OBJC_CLASS_$_AKDeviceListRequestContext
+ _OBJC_CLASS_$_SUCoreSpace
+ _OBJC_CLASS_$_SUOSUCloudDevice
+ _OBJC_CLASS_$_SUOSUCloudDeviceManager
+ _OBJC_CLASS_$_SUOSUInactivityPredictor
+ _OBJC_CLASS_$_SUOSULoginCredentialCacheInfo
+ _OBJC_CLASS_$_SUOSUServiceClientManager
+ _OBJC_CLASS_$_SUOSUUpdatesAvailablePolicy
+ _OBJC_CLASS_$_SUTelemetryEventFormatter
+ _OBJC_CLASS_$__OSInactivityPredictionClient
+ _OBJC_METACLASS_$_SUOSUCloudDevice
+ _OBJC_METACLASS_$_SUOSUCloudDeviceManager
+ _OBJC_METACLASS_$_SUOSUInactivityPredictor
+ _OBJC_METACLASS_$_SUOSULoginCredentialCacheInfo
+ _OBJC_METACLASS_$_SUOSUServiceClientManager
+ _OBJC_METACLASS_$_SUOSUUpdatesAvailablePolicy
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _SUMacControllerStateCurrentClientIDKey
+ _SUNotificationApplicationsMayBlockRestartType
+ _SUNotificationInsufficientSpace
+ _SUOSUApplicationsMayBlockRestartIdentifier
+ _SUOSUAutomaticBackgroundScanFinishedNotification
+ _SUOSUClientInitiatedScanSucceeded
+ _SUOSUEventTypeInsufficientSpace
+ _SUOSUInsufficientSpaceIdentifier
+ _SUOSULoginCredentialPolicyModeString
+ _SUOSUMobileKeyBagStashStateString
+ _SUOSUNotificationOptionDictionaryCloudDeviceNameKey
+ _SUOSUNotificationOptionDictionaryCustomIconPathKey
+ _SUOSUNotificationOptionDictionaryUpdateTitleOverride
+ _SUOSUNotificationTypeString
+ _SUOSURemindMeLaterAction
+ _SUOSUUpdatesAvailableCustomTextIdentifier
+ _SUOSUUpdatesAvailableDeviceCompatibilityIdentifier
+ _SUOSUUpdatesAvailableGeneralIdentifier
+ _SUOSUUpdatesAvailableSecurityAdvisoryIdentifier
+ _SUOSUUserActionDetailsKeyBytesRequired
+ _SUTelemetryPayloadKeyLastLoginWindowHarvestMethod
+ _SUTelemetryPayloadKeyMinutesSinceLastHarvest
+ _SUTelemetryPayloadKeyMinutesSinceLastLoginWindowHarvest
+ _SUTelemetryPayloadKeyStashState
+ __101-[SUOSUManagedServiceDaemon scheduleEnforcedManagedUpdateWithVersion:forDate:withOptions:completion:]_block_invoke.340
+ __102-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]_block_invoke.503
+ __102-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]_block_invoke.506
+ __102-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]_block_invoke.506.cold.1
+ __102-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]_block_invoke.cold.1
+ __102-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]_block_invoke.cold.2
+ __103-[SUOSUNotificationManagerController postDoItLaterUpdatesFailedNotificationRestartRequired:offerLater:]_block_invoke.24
+ __105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke.333
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.460
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.460.cold.1
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.464
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.464.cold.1
+ __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.464.cold.2
+ __113-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptors:inBackground:mdmInitiated:completion:]_block_invoke.442
+ __113-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptors:inBackground:mdmInitiated:completion:]_block_invoke.445
+ __113-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptors:inBackground:mdmInitiated:completion:]_block_invoke_2.446
+ __116-[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:withProgressCompletion:withCompletion:]_block_invoke.314
+ __122-[SUOSUUpdateController estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:outEvictableBytes:error:]_block_invoke.449
+ __122-[SUOSUUpdateController estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:outEvictableBytes:error:]_block_invoke.cold.1
+ __123-[SUOSUShimController _startInstallingUpdatesRequiringNoPostInstallAction:inForeground:nowIsLater:mdmInitiated:completion:]_block_invoke.518
+ __129-[SUOSUNotificationManagerController postDDMNotificationForScheduledUpdate:updateVersion:ignoreDoNotDisturb:companyName:options:]_block_invoke.70
+ __132-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]_block_invoke.298
+ __132-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]_block_invoke.298.cold.1
+ __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.436
+ __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.441
+ __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.441.cold.1
+ __34-[SUOSUCloudDeviceManager devices]_block_invoke.cold.1
+ __39-[SUOSUServiceDaemon _laterDidNotOccur]_block_invoke.574
+ __41-[SUOSUServiceDaemon armClientsWithMode:]_block_invoke.494
+ __42-[SUOSUMDMController updateStatusForKeys:]_block_invoke.81
+ __42-[SUOSUServiceDaemon doPeriodicMDMActions]_block_invoke.313
+ __42-[SUOSUServiceDaemon doPeriodicMDMActions]_block_invoke.323
+ __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.550
+ __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.554
+ __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.555
+ __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.558
+ __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.cold.1
+ __49-[SUOSUServiceDaemon appQuitCompleteForObserver:]_block_invoke.561
+ __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.360
+ __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.360.cold.1
+ __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.361
+ __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.362
+ __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.367
+ __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.367.cold.1
+ __50-[SUOSUServiceDaemon armObserverWithMode:options:]_block_invoke.500
+ __50-[SUOSUServiceDaemon rollbackSplatWithCompletion:]_block_invoke.539
+ __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.351
+ __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.351.cold.1
+ __55-[SUOSUNotificationManagerController _connectToService]_block_invoke.85
+ __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.329
+ __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.329.cold.1
+ __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.329.cold.2
+ __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.343
+ __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.346
+ __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.346.cold.1
+ __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.580
+ __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.580.cold.1
+ __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.581
+ __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.581.cold.1
+ __57-[SUOSUShimController observeForegroundInstallInProgress]_block_invoke.446
+ __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke.394
+ __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_2.395
+ __61-[SUOSUServiceDaemon scheduleUpdatesAvailableBSDNotification]_block_invoke.357
+ __61-[SUOSUServiceDaemon scheduleUpdatesAvailableBSDNotification]_block_invoke.cold.1
+ __62-[SUOSUServiceDaemon _downloadAndPrepareMDMUpdateWithOptions:]_block_invoke.562
+ __62-[SUOSUServiceDaemon _downloadAndPrepareMDMUpdateWithOptions:]_block_invoke.562.cold.1
+ __62-[SUOSUServiceDaemon applyMobileSoftwareUpdateWithCompletion:]_block_invoke.467
+ __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.527
+ __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.527.cold.1
+ __65-[SUOSUNotificationManagerController _authorizeServiceForInstall]_block_invoke.90
+ __67-[SUOSUNotificationManagerController triggerAppleConnectWithError:]_block_invoke.66
+ __67-[SUOSUServiceDaemon performSemiSplatForDescriptor:withCompletion:]_block_invoke.540
+ __69-[SUOSUNotificationManagerController startInstallingDoItLaterUpdates]_block_invoke.40
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.494
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.495
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.506
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.507
+ __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.510
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.452
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.455
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.455.cold.1
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.455.cold.2
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.455.cold.3
+ __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.455.cold.4
+ __72-[SUOSUUpdateController cacheDeletePurgeableSpaceWithCompletionHandler:]_block_invoke.445
+ __72-[SUOSUUpdateController cacheDeletePurgeableSpaceWithCompletionHandler:]_block_invoke.cold.1
+ __79-[SUOSUServiceDaemon startInstallingExternalUpdateWithProductKeys:withOptions:]_block_invoke.543
+ __80-[SUOSUNotificationManagerController startInstallingUpdatesForKeys:withOptions:]_block_invoke.45
+ __81-[SUOSUNotificationManagerController postDoItLaterOtherUsersLoggedInNotification]_block_invoke.29
+ __83-[SUOSUServiceDaemon allAvailableMDMMobileSoftwareUpdateDescriptorsWithCompletion:]_block_invoke.396
+ __83-[SUOSUServiceDaemon allAvailableMDMMobileSoftwareUpdateDescriptorsWithCompletion:]_block_invoke.440
+ __85-[SUOSUNotificationManagerController queueAllUpdatesForAutoInstallTonightWithReason:]_block_invoke.cold.1
+ __86-[SUOSUUpdateController attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:error:]_block_invoke.441
+ __86-[SUOSUUpdateController attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:error:]_block_invoke.cold.1
+ __87-[SUOSUNotificationManagerController evaluateAndPostInstallTonightAppCloseNotification]_block_invoke.cold.1
+ __88-[SUOSUServiceDaemon triggerSplatRevokedNotificationWithVersion:options:withCompletion:]_block_invoke.509
+ __89-[SUOSUServiceDaemon startPostLogoutActionsForExternalUpdateWithProductKeys:withOptions:]_block_invoke.546
+ __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.527
+ __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.527.cold.1
+ __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.527.cold.2
+ __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.528
+ __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.528.cold.1
+ __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.529
+ __92-[SUOSUNotificationManagerController startInstallingMDMMajorOSUpdateWithBundleId:orVersion:]_block_invoke.51
+ __93-[SUOSUShimController _startShowingProgressForExternalUpdate:mdmInitiated:successCompletion:]_block_invoke.469
+ __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.546
+ __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.550
+ __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.553
+ __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke.322
+ __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke.328
+ __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_2.329
+ __95-[SUOSUUpdateController suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:error:]_block_invoke.451
+ __95-[SUOSUUpdateController suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:error:]_block_invoke.cold.1
+ __97-[SUOSUServiceDaemon suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:completion:]_block_invoke.382
+ __97-[SUOSUServiceDaemon suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:completion:]_block_invoke.382.cold.1
+ __97-[SUOSUServiceDaemon suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:completion:]_block_invoke.cold.1
+ __OBJC_$_CLASS_METHODS_SUOSUCloudDeviceManager
+ __OBJC_$_CLASS_METHODS_SUOSUUpdatesAvailablePolicy
+ __OBJC_$_CLASS_PROP_LIST_SUOSULoginCredentialPolicy
+ __OBJC_$_INSTANCE_METHODS_SUOSUCloudDevice
+ __OBJC_$_INSTANCE_METHODS_SUOSUCloudDeviceManager
+ __OBJC_$_INSTANCE_METHODS_SUOSUInactivityPredictor
+ __OBJC_$_INSTANCE_METHODS_SUOSULoginCredentialCacheInfo
+ __OBJC_$_INSTANCE_METHODS_SUOSUServiceClientManager
+ __OBJC_$_INSTANCE_METHODS_SUOSUUpdatesAvailablePolicy
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUCloudDevice
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUCloudDeviceManager
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUInactivityPredictor
+ __OBJC_$_INSTANCE_VARIABLES_SUOSULoginCredentialCacheInfo
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUServiceClientManager
+ __OBJC_$_INSTANCE_VARIABLES_SUOSUUpdatesAvailablePolicy
+ __OBJC_$_PROP_LIST_SUOSUCloudDevice
+ __OBJC_$_PROP_LIST_SUOSUCloudDeviceManager
+ __OBJC_$_PROP_LIST_SUOSUInactivityPredictor
+ __OBJC_$_PROP_LIST_SUOSULoginCredentialCacheInfo
+ __OBJC_$_PROP_LIST_SUOSUServiceClientManager
+ __OBJC_$_PROP_LIST_SUOSUUpdatesAvailablePolicy
+ __OBJC_CLASS_RO_$_SUOSUCloudDevice
+ __OBJC_CLASS_RO_$_SUOSUCloudDeviceManager
+ __OBJC_CLASS_RO_$_SUOSUInactivityPredictor
+ __OBJC_CLASS_RO_$_SUOSULoginCredentialCacheInfo
+ __OBJC_CLASS_RO_$_SUOSUServiceClientManager
+ __OBJC_CLASS_RO_$_SUOSUUpdatesAvailablePolicy
+ __OBJC_METACLASS_RO_$_SUOSUCloudDevice
+ __OBJC_METACLASS_RO_$_SUOSUCloudDeviceManager
+ __OBJC_METACLASS_RO_$_SUOSUInactivityPredictor
+ __OBJC_METACLASS_RO_$_SUOSULoginCredentialCacheInfo
+ __OBJC_METACLASS_RO_$_SUOSUServiceClientManager
+ __OBJC_METACLASS_RO_$_SUOSUUpdatesAvailablePolicy
+ ___102-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]_block_invoke
+ ___106-[SUOSUServiceDaemon estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:completion:]_block_invoke
+ ___122-[SUOSUUpdateController estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:outEvictableBytes:error:]_block_invoke
+ ___34-[SUOSUCloudDeviceManager devices]_block_invoke
+ ___37-[SUOSUServiceDaemon initializeState]_block_invoke
+ ___40+[SUOSUCloudDeviceManager sharedManager]_block_invoke
+ ___42-[SUOSUServiceDaemon cancelInstallTonight]_block_invoke
+ ___54-[SUOSULoginCredentialPolicyManager refreshCachedMode]_block_invoke
+ ___55-[SUOSUUpdateController mobileKeyBagStashStateForUser:]_block_invoke
+ ___57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke_3
+ ___60-[SUOSUManagedServiceDaemon invalidAndRemoveOldDeclarations]_block_invoke
+ ___61-[SUOSUServiceDaemon scheduleUpdatesAvailableBSDNotification]_block_invoke
+ ___62-[SUOSUClient cacheDeletePurgeableSpaceWithCompletionHandler:]_block_invoke
+ ___64-[SUOSUServiceDaemon refreshCachedLoginCredentialHarvestingMode]_block_invoke
+ ___65-[SUOSUUpdateController _commitStashOnlyForDescriptor:withError:]_block_invoke
+ ___67-[SUOSUMobileSoftwareUpdateController cancelUpdatesWithCompletion:]_block_invoke
+ ___67-[SUOSUShimController _refreshAllAvailableUpdatesAndNotifyDelegate]_block_invoke
+ ___69-[SUOSUServiceDaemon cacheDeletePurgeableSpaceWithCompletionHandler:]_block_invoke
+ ___70-[SUOSUShimController cacheDeletePurgeableSpaceWithCompletionHandler:]_block_invoke
+ ___70-[SUOSUShimController cacheDeletePurgeableSpaceWithCompletionHandler:]_block_invoke_2
+ ___71-[SUOSUShimController _registerForScanCompletionNotification:outToken:]_block_invoke
+ ___72-[SUOSUUpdateController cacheDeletePurgeableSpaceWithCompletionHandler:]_block_invoke
+ ___82-[SUOSULoginCredentialPolicyManager _isUpdateDownloadedAndPreparedWithCompletion:]_block_invoke
+ ___83-[SUOSULoginCredentialPolicyManager getCurrentLoginCredentialPolicyWithCompletion:]_block_invoke
+ ___85-[SUOSUNotificationManagerController queueAllUpdatesForAutoInstallTonightWithReason:]_block_invoke
+ ___86-[SUOSUUpdateController attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:error:]_block_invoke
+ ___87-[SUOSUNotificationManagerController evaluateAndPostInstallTonightAppCloseNotification]_block_invoke
+ ___88-[SUOSUServiceDaemon attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:completion:]_block_invoke
+ ___95-[SUOSUUpdateController suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:error:]_block_invoke
+ ___97-[SUOSUServiceDaemon suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:completion:]_block_invoke
+ ___block_descriptor_32_e8_v16?0Q8l
+ ___block_descriptor_40_e8_32bs_e23_v28?0B8Q12"NSError"20l
+ ___block_descriptor_40_e8_32bs_e30_v24?0"NSNumber"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e8_v16?0q8l
+ ___block_descriptor_48_e8_32s40bs_e23_v28?0B8Q12"NSError"20l
+ ___block_descriptor_48_e8_32s40bs_e38_v20?0"SUMacControllerDescriptor"8B16l
+ ___block_descriptor_48_e8_32s40s_e8_v12?0i8l
+ ___block_descriptor_56_e8_32bs40r48r_e18_v16?0"NSNumber"8l
+ ___block_descriptor_56_e8_32r40r48r_e23_v28?0B8Q12"NSError"20l
+ ___block_descriptor_56_e8_32s40bs_e23_v28?0B8Q12"NSError"20l
+ ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48s_e14_"NSArray"8?0l
+ ___block_descriptor_56_e8_32s40s48s_e42_v24?0"AKDeviceListResponse"8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
+ ___copy_helper_block_e8_32b40r48r
+ ___copy_helper_block_e8_32r40r48r
+ ___destroy_helper_block_e8_32r40r48r
+ __block_literal_global.23
+ __block_literal_global.28
+ __block_literal_global.316
+ __block_literal_global.325
+ __block_literal_global.33
+ __block_literal_global.35
+ __block_literal_global.364
+ __block_literal_global.37
+ __block_literal_global.39
+ __block_literal_global.399
+ __block_literal_global.44
+ __block_literal_global.454
+ __block_literal_global.48
+ __block_literal_global.482
+ __block_literal_global.484
+ __block_literal_global.486
+ __block_literal_global.497
+ __block_literal_global.50
+ __block_literal_global.505
+ __block_literal_global.512
+ __block_literal_global.545
+ __block_literal_global.548
+ __block_literal_global.55
+ __block_literal_global.557
+ __block_literal_global.57
+ __block_literal_global.59
+ __block_literal_global.61
+ __block_literal_global.63
+ __block_literal_global.65
+ __lastVendedPolicyMode
+ __lock
+ _dispatch_activate
+ _kAutoUpdatePolicyUpdateEligibilityPeriod
+ _kSUCoreDDMSoftwareUpdateStatusDidChangeNotificationValueTargetLocalDateTime
+ _objc_copyStruct
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$_allowedToRequireCredentialsForProductKey:
+ _objc_msgSend$_cancelScheduledAppCloseNotification
+ _objc_msgSend$_commitStashOnlyForDescriptor:withError:
+ _objc_msgSend$_configureOverridesForOptionalPSUSDownload:forDescriptor:
+ _objc_msgSend$_determineEligibleProducts
+ _objc_msgSend$_determineNotificationInterval
+ _objc_msgSend$_determineNotificationType
+ _objc_msgSend$_handleSuccessfullyCompletedScan
+ _objc_msgSend$_insufficientDiskSpaceErrorForProducts:spaceRequired:underlyingError:
+ _objc_msgSend$_isUpdateDownloadedAndPreparedWithCompletion:
+ _objc_msgSend$_mobileKeyBagStashStateForUser:
+ _objc_msgSend$_mobileSoftwareUpdatesForProducts:
+ _objc_msgSend$_modeFromCachedInfo:
+ _objc_msgSend$_nowExceedsLastNotificationDate
+ _objc_msgSend$_postAppCloseNotificationIfAppropriate
+ _objc_msgSend$_productNameForModel:
+ _objc_msgSend$_promptAndSuspendMobileAssetIfNecessaryWithFreeSpaceRequired:suspendedMobileAsset:error:
+ _objc_msgSend$_queue_disarmLaterObserver
+ _objc_msgSend$_reclaimDiskSpaceIfNecssaryWithBytesRequired:bytesReclaimed:error:
+ _objc_msgSend$_refreshAllAvailableUpdatesAndNotifyDelegate
+ _objc_msgSend$_registerForScanCompletionNotification:outToken:
+ _objc_msgSend$_reminderDaysForCount:finalNotification:
+ _objc_msgSend$_setIdleSleepPowerAssertion:
+ _objc_msgSend$_setMobileSoftwareUpdateDescriptorToInstallLater:withReason:stashState:
+ _objc_msgSend$_shouldIgnoreDescriptorFromScan:withOptions:
+ _objc_msgSend$_shouldShowDeviceCompatibilityNotificationForDevice:
+ _objc_msgSend$_shouldShowNotificationWithReason:
+ _objc_msgSend$_shouldShowSecurityAdvisoryNotification
+ _objc_msgSend$_willAutoInstallDescriptor:withProductKey:
+ _objc_msgSend$aa_altDSID
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$activeNotificationManagerClient
+ _objc_msgSend$addClient:
+ _objc_msgSend$addCredentialHarvestingInfoWithStashState:
+ _objc_msgSend$alignediOSMajorVersion
+ _objc_msgSend$allClients
+ _objc_msgSend$allowedToUseInstallTonight
+ _objc_msgSend$alreadyPostedFinalNotification
+ _objc_msgSend$appCloseNotificationDelay
+ _objc_msgSend$appCloseNotificationTimerSource
+ _objc_msgSend$appendCredentialHarvestingInfoWithSharedPrefs:stashState:toDict:
+ _objc_msgSend$appsThatWillPreventRestart
+ _objc_msgSend$attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:completion:
+ _objc_msgSend$attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:error:
+ _objc_msgSend$autoDownloadEnabled
+ _objc_msgSend$availableProducts
+ _objc_msgSend$availableProductsDownloaded
+ _objc_msgSend$buildVersion
+ _objc_msgSend$cacheDate
+ _objc_msgSend$cacheDeletePurgeableSpace
+ _objc_msgSend$cacheDeletePurgeableSpaceWithCompletionHandler:
+ _objc_msgSend$cachedDevices
+ _objc_msgSend$cachedInfo
+ _objc_msgSend$cachedMode
+ _objc_msgSend$cancelInstallTonight
+ _objc_msgSend$clientID
+ _objc_msgSend$clientManager
+ _objc_msgSend$cloudDevices
+ _objc_msgSend$collectCredentialHarvestingInfo
+ _objc_msgSend$confidenceLevel
+ _objc_msgSend$confidenceValue
+ _objc_msgSend$createUserActivityAssertionWithDescription:timeout:
+ _objc_msgSend$dataWithContentsOfURL:
+ _objc_msgSend$ddmEnforcedWithin24Hours
+ _objc_msgSend$defaultRequiredInterval
+ _objc_msgSend$defaultStore
+ _objc_msgSend$deviceList
+ _objc_msgSend$deviceListWithContext:completion:
+ _objc_msgSend$disableDeviceCompatibilityNotification
+ _objc_msgSend$disableMASuspension
+ _objc_msgSend$disableSecurityAdvisoryNotification
+ _objc_msgSend$documentationDeviceCompatibilityNotificationBodyString
+ _objc_msgSend$documentationDeviceCompatibilityNotificationTitleString
+ _objc_msgSend$documentationSecurityAdvisoryNotificationBodyString
+ _objc_msgSend$documentationSecurityAdvisoryNotificationTitleString
+ _objc_msgSend$doubleValue
+ _objc_msgSend$downloadedAndPrepared
+ _objc_msgSend$eligibleProducts
+ _objc_msgSend$enablePreSUStaging
+ _objc_msgSend$enablePreSUStagingForOptionalAssets
+ _objc_msgSend$endDate
+ _objc_msgSend$errorIsUserCancelledError:
+ _objc_msgSend$estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:completion:
+ _objc_msgSend$estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:outEvictableBytes:error:
+ _objc_msgSend$evaluateAndPostInstallTonightAppCloseNotification
+ _objc_msgSend$fakeMaxPreSUStagingSize
+ _objc_msgSend$fakeMobileAssetEstimateBytesReclaimedSuccess
+ _objc_msgSend$firstInstallTonightDates
+ _objc_msgSend$firstOfferDateForProductKey:
+ _objc_msgSend$initWithClient:startDate:endDate:
+ _objc_msgSend$initWithDescriptor:downloadedAndPrepared:
+ _objc_msgSend$initWithName:operatingSystemName:operatingSystemVersion:
+ _objc_msgSend$initWithProduct:reason:stashState:sharedPrefs:
+ _objc_msgSend$initWithSharedPrefs:msuController:installTonightManager:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$invalidAndRemoveOldDeclarations
+ _objc_msgSend$invalidateAllInvalidDeclarationsReturningAllInvalid
+ _objc_msgSend$isPortable
+ _objc_msgSend$lastLoginWindowHarvestDate
+ _objc_msgSend$lastLoginWindowHarvestMethod
+ _objc_msgSend$lastNotificationDate
+ _objc_msgSend$lastNotificationProductKey
+ _objc_msgSend$lastSuccessfulMSUBackgroundScanDate
+ _objc_msgSend$lastVendedPolicyMode
+ _objc_msgSend$loadLongSummary
+ _objc_msgSend$loadMajorIcon
+ _objc_msgSend$loadMinorIcon
+ _objc_msgSend$loadShortSummary
+ _objc_msgSend$localizedName
+ _objc_msgSend$longInactivityPredictionResultAtDate:withTimeSinceInactive:withOptions:withError:
+ _objc_msgSend$mainBundle
+ _objc_msgSend$majorOSUpdatesManaged
+ _objc_msgSend$maxPreSUStagingOptionalAssetSize
+ _objc_msgSend$minimumNotificationInterval
+ _objc_msgSend$minimumNotificationIntervalOverride
+ _objc_msgSend$minorProduct
+ _objc_msgSend$mobileAssetEstimateEvictable:completionQueue:completion:
+ _objc_msgSend$mobileAssetSuspend:completionQueue:completion:
+ _objc_msgSend$mobileKeyBagStashStateForUser:
+ _objc_msgSend$mobileKeyBagStashStateForUser:completion:
+ _objc_msgSend$model
+ _objc_msgSend$msuController
+ _objc_msgSend$notificationCount
+ _objc_msgSend$notificationsDisabled
+ _objc_msgSend$operatingSystemName
+ _objc_msgSend$optionUserId
+ _objc_msgSend$parseProductMarketingVersion:systemVersion:
+ _objc_msgSend$predictedInactivityDate
+ _objc_msgSend$primaryProduct
+ _objc_msgSend$queueAllUpdatesForAutoInstallTonightWithReason:
+ _objc_msgSend$queueDescriptorForInstallTonight:withReason:stashState:
+ _objc_msgSend$refreshCachedLoginCredentialHarvestingMode
+ _objc_msgSend$refreshCachedMode
+ _objc_msgSend$removeClient:
+ _objc_msgSend$roundToMB:
+ _objc_msgSend$setAlignedCloudDevice:
+ _objc_msgSend$setAllowedToUseInstallTonight:
+ _objc_msgSend$setAlreadyPostedFinalNotification:
+ _objc_msgSend$setAltDSID:
+ _objc_msgSend$setAppCloseNotificationTimerSource:
+ _objc_msgSend$setCacheDate:
+ _objc_msgSend$setCachedDevices:
+ _objc_msgSend$setCachedInfo:
+ _objc_msgSend$setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:
+ _objc_msgSend$setCollectCredentialHarvestingInfo:
+ _objc_msgSend$setEligibleProducts:
+ _objc_msgSend$setEnablePreSUStagingForOptionalAssets:
+ _objc_msgSend$setFirstInstallTonightDateForProductKey:
+ _objc_msgSend$setFirstOfferDateForProductKey:
+ _objc_msgSend$setIncludeUntrustedDevices:
+ _objc_msgSend$setIsAutoUpdateEligible:
+ _objc_msgSend$setIsCriticalProduct:
+ _objc_msgSend$setIsSplatCombo:
+ _objc_msgSend$setLastLoginWindowHarvestDate:
+ _objc_msgSend$setLastLoginWindowHarvestMethod:
+ _objc_msgSend$setLastPostedUpdatesAvailableNotificationDateToNow
+ _objc_msgSend$setLastSuccessfulMSUBackgroundScanDate:
+ _objc_msgSend$setLastVendedPolicyMode:
+ _objc_msgSend$setMajorProduct:
+ _objc_msgSend$setMaxPreSUStagingOptionalAssetSize:
+ _objc_msgSend$setMinimumNotificationInterval:
+ _objc_msgSend$setMinorProduct:
+ _objc_msgSend$setMobileSoftwareUpdateDescriptorToInstallLater:withReason:userId:
+ _objc_msgSend$setOfferLater:
+ _objc_msgSend$setOperatingSystems:
+ _objc_msgSend$setPostInstallAction:
+ _objc_msgSend$setProductVersionExtra:
+ _objc_msgSend$setRestartRequired:
+ _objc_msgSend$setServices:
+ _objc_msgSend$setShortAttributedDescription:
+ _objc_msgSend$setShortDescription:
+ _objc_msgSend$setSplatAppliedRestartNow:
+ _objc_msgSend$setSplatProduct:
+ _objc_msgSend$setStashState:
+ _objc_msgSend$setTimeRemainingBeforeCriticalAutoUpdate:
+ _objc_msgSend$setUpdateIconImage:
+ _objc_msgSend$setUpdatesAvailableNotificationTimerSource:
+ _objc_msgSend$settingsIsActive
+ _objc_msgSend$setupAssistantIsActive
+ _objc_msgSend$splatAppliedUpdateNow
+ _objc_msgSend$splatProduct
+ _objc_msgSend$staleUpdateInterval
+ _objc_msgSend$staleUpdateRequiredInterval
+ _objc_msgSend$startDate
+ _objc_msgSend$stashState
+ _objc_msgSend$stringForSystemVersion:
+ _objc_msgSend$sunmClients
+ _objc_msgSend$suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:completion:
+ _objc_msgSend$suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:error:
+ _objc_msgSend$uidFromCurrentAuditToken
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updatesAvailableNotificationCount
+ _objc_msgSend$updatesAvailableNotificationDelay
+ _objc_msgSend$updatesAvailableNotificationProductKey
+ _objc_msgSend$updatesAvailableNotificationTimerSource
+ get_aks_client_connection.cold.1
- +[SUOSUDDMConfiguration sharedInstance]
- +[SUOSUManagedGlobalSettings sharedInstance]
- +[SUOSUUtilities appNamesThatWillPreventRestart]
- -[SUOSUDDMConfiguration .cxx_destruct]
- -[SUOSUDDMConfiguration ddmConfiguration]
- -[SUOSUDDMConfiguration init]
- -[SUOSUDDMConfiguration setDdmConfiguration:]
- -[SUOSUExternalUpdateProvider postMajorOSUpdateMDMRequestedNotification]
- -[SUOSUInstallTonightManager queueDescriptorForInstallTonight:withReason:]
- -[SUOSULoginCredentialPolicyManager _allowedToRequireCredentials]
- -[SUOSULoginCredentialPolicyManager _changeCurrentPolicyMode:withReason:]
- -[SUOSULoginCredentialPolicyManager _willAutoInstallProduct:]
- -[SUOSULoginCredentialPolicyManager credentialsHarvested]
- -[SUOSULoginCredentialPolicyManager getCurrentLoginCredentialPolicy]
- -[SUOSULoginCredentialPolicyManager initWithSharedPrefs:intervalForRequiringCredentials:]
- -[SUOSULoginCredentialPolicyManager intervalForRequiringCredentials]
- -[SUOSULoginCredentialPolicyManager lock]
- -[SUOSULoginCredentialPolicyManager recommendedUpdatesDidChange]
- -[SUOSULoginCredentialPolicyManager setIntervalForRequiringCredentials:]
- -[SUOSULoginCredentialPolicyManager setLock:]
- -[SUOSULoginCredentialPolicyManager updatePolicyForDownloadedAndPreparedProduct:]
- -[SUOSULoginCredentialPolicyManager updatePolicyForInstallTonightWithProduct:]
- -[SUOSUMDMController doMDMMajorOSUpdateWithBundleId:withVersion:]
- -[SUOSUMDMController doMDMMajorOSUpdateWithBundleId:withVersion:withError:]
- -[SUOSUMDMController getMajorOSUpdateStatus:]
- -[SUOSUMDMController getUpdateStatus:]
- -[SUOSUMSUScanOptions fetchMajorUpdates]
- -[SUOSUMSUScanOptions fetchMinorUpdates]
- -[SUOSUMSUScanOptions setFetchMajorUpdates:]
- -[SUOSUMSUScanOptions setFetchMinorUpdates:]
- -[SUOSUManagedGlobalSettings .cxx_destruct]
- -[SUOSUManagedGlobalSettings adminInstallRequired]
- -[SUOSUManagedGlobalSettings automaticallyDownloadManaged]
- -[SUOSUManagedGlobalSettings automaticallyDownload]
- -[SUOSUManagedGlobalSettings automaticallyInstallOSUpdatesManaged]
- -[SUOSUManagedGlobalSettings automaticallyInstallOSUpdates]
- -[SUOSUManagedGlobalSettings automaticallyInstallSystemAndSecurityUpdatesManaged]
- -[SUOSUManagedGlobalSettings automaticallyInstallSystemAndSecurityUpdates]
- -[SUOSUManagedGlobalSettings daysToSeconds:]
- -[SUOSUManagedGlobalSettings ddmConfiguration]
- -[SUOSUManagedGlobalSettings enableGlobalNotifications]
- -[SUOSUManagedGlobalSettings enableRapidSecurityResponseRollback]
- -[SUOSUManagedGlobalSettings enableRapidSecurityResponse]
- -[SUOSUManagedGlobalSettings globalSettings]
- -[SUOSUManagedGlobalSettings init]
- -[SUOSUManagedGlobalSettings majorOSDeferralPeriod]
- -[SUOSUManagedGlobalSettings majorOSDeferralPeriod].cold.1
- -[SUOSUManagedGlobalSettings majorOSDeferralPeriod].cold.2
- -[SUOSUManagedGlobalSettings minorOSDeferralPeriod]
- -[SUOSUManagedGlobalSettings minorOSDeferralPeriod].cold.1
- -[SUOSUManagedGlobalSettings minorOSDeferralPeriod].cold.2
- -[SUOSUManagedGlobalSettings nonOSDeferralPeriod]
- -[SUOSUManagedGlobalSettings nonOSDeferralPeriod].cold.1
- -[SUOSUManagedGlobalSettings nonOSDeferralPeriod].cold.2
- -[SUOSUManagedGlobalSettings setDdmConfiguration:]
- -[SUOSUManagedServiceDaemon _convertTelemetryOverrideValueToDDMKey:]
- -[SUOSUMobileSoftwareUpdateController managedGlobalSettings]
- -[SUOSUMobileSoftwareUpdateController setManagedGlobalSettings:]
- -[SUOSUNotificationManagerController postMajorOSUpdateMDMRequestedNotification]
- -[SUOSUServiceClient postMajorOSUpdateMDMRequestedNotification]
- -[SUOSUServiceDaemon _queue_chooseActiveNotificationManagerClient]
- -[SUOSUServiceDaemon _scanForMobileSoftwareUpdateDescriptorsInBackground:getMinor:getMajor:mdmInitiated:requestedProductMarketingVersion:withCompletion:]
- -[SUOSUServiceDaemon _scanForMobileSoftwareUpdateDescriptorsInBackground:getMinor:getMajor:withCompletion:]
- -[SUOSUServiceDaemon attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:withCompletion:]
- -[SUOSUServiceDaemon availableUpdates]
- -[SUOSUServiceDaemon clients]
- -[SUOSUServiceDaemon majorOSUpdateStatus]
- -[SUOSUServiceDaemon notificationManagerClients]
- -[SUOSUServiceDaemon postMDMRequestedNotificationToAllLoggedInUsers]
- -[SUOSUServiceDaemon postMajorOSUpdateMDMRequestedNotification]
- -[SUOSUServiceDaemon removeMobileSoftwareUpdatesToInstallLater]
- -[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:withCompletion:]
- -[SUOSUServiceDaemon setClients:]
- -[SUOSUServiceDaemon setMajorOSUpdateStatus:]
- -[SUOSUServiceDaemon setMobileSoftwareUpdateDescriptorToInstallLater:withReason:]
- -[SUOSUShimController _availableUpdateForProductKey:]
- -[SUOSUShimController _handleAvailableUpdatesChangedWithNotificationNamed:]
- -[SUOSUShimController _handleAvailableUpdatesChangedWithNotificationNamed:updateClients:]
- -[SUOSUShimController _latestAvailableMajorOSProduct].cold.1
- -[SUOSUShimController _latestAvailableMajorOSProduct].cold.2
- -[SUOSUShimController _latestAvailableMajorOSProduct].cold.3
- -[SUOSUShimController _performDiskSpaceCheckForUpdates:mdmInitiated:]
- -[SUOSUShimController _performDiskSpaceCheckForUpdates:mdmInitiated:].cold.1
- -[SUOSUShimController _productKeysForAppStoreUpdates:]
- -[SUOSUShimController availableUpdatesObserverToken]
- -[SUOSUShimController currentlyFetchingMajorOSUpdateForURLScheme]
- -[SUOSUShimController forceFullInstaller]
- -[SUOSUShimController hasIgnoredUpdatesObserverToken]
- -[SUOSUShimController setAvailableUpdatesObserverToken:]
- -[SUOSUShimController setCurrentlyFetchingMajorOSUpdateForURLScheme:]
- -[SUOSUShimController setHasIgnoredUpdatesObserverToken:]
- -[SUOSUShimController userIsOwner]
- -[SUOSUShimController userIsOwner].cold.1
- -[SUOSUTelemetryInstallEvent _roundToMB:]
- -[SUOSUTelemetryQueueForInstallTonightEvent initWithProduct:reason:sharedPrefs:]
- -[SUOSUUpdateController _setIdleSleepPowerAssertion]
- -[SUOSUUpdateController attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:]
- -[SUOSUUpdateController commitStashOnlyForDescriptor:withError:]
- -[SUOSUUpdateController commitStashOnlyWithDescriptor:withError:]
- -[SUOSUUpdateController commitStashOnlyWithProduct:withError:]
- -[SUOSUUpdateController commitStashWithProduct:withError:]
- -[SUOSUUpdateController disarmLaterObserver]
- -[SUOSUUpdateController postMDMRequestedNotificationToAllLoggedInUsers]
- -[SUOSUUpdateController postMajorOSUpdateMDMRequestedNotification]
- -[SUOSUUpdateController postRestartRequiredNotificationWithOptions:completion:]
- -[SUOSUUpdateController removeAllMobileSoftwareUpdatesFromInstallLater]
- -[SUOSUUpdateController setClientExternalizedLocalAuthenticationContext:]
- -[SUOSUUpdateController setClientExternalizedLocalAuthenticationContextAsync:withCompletion:]
- -[SUOSUUserPrefs lastPostedMajorOSUpdatesAvailableNotificationDate]
- -[SUOSUUserPrefs setLastPostedMajorOSUpdatesAvailableNotificationDateToNow]
- -[SUOSUUserPrefs setLastPostedMajorOSUpdatesAvailableNotificationToDate:]
- GCC_except_table101
- GCC_except_table103
- GCC_except_table105
- GCC_except_table108
- GCC_except_table120
- GCC_except_table122
- GCC_except_table126
- GCC_except_table128
- GCC_except_table139
- GCC_except_table14
- GCC_except_table141
- GCC_except_table143
- GCC_except_table145
- GCC_except_table148
- GCC_except_table151
- GCC_except_table166
- GCC_except_table168
- GCC_except_table170
- GCC_except_table172
- GCC_except_table174
- GCC_except_table179
- GCC_except_table184
- GCC_except_table185
- GCC_except_table187
- GCC_except_table189
- GCC_except_table194
- GCC_except_table196
- GCC_except_table207
- GCC_except_table210
- GCC_except_table212
- GCC_except_table215
- GCC_except_table218
- GCC_except_table219
- GCC_except_table22
- GCC_except_table221
- GCC_except_table224
- GCC_except_table24
- GCC_except_table245
- GCC_except_table247
- GCC_except_table248
- GCC_except_table262
- GCC_except_table268
- GCC_except_table273
- GCC_except_table291
- GCC_except_table299
- GCC_except_table308
- GCC_except_table370
- GCC_except_table375
- GCC_except_table376
- GCC_except_table391
- GCC_except_table392
- GCC_except_table395
- GCC_except_table49
- GCC_except_table51
- GCC_except_table53
- GCC_except_table60
- GCC_except_table63
- GCC_except_table71
- GCC_except_table77
- GCC_except_table80
- GCC_except_table84
- GCC_except_table87
- GCC_except_table89
- GCC_except_table91
- GCC_except_table93
- GCC_except_table95
- GCC_except_table99
- OBJC_IVAR_$_SUOSUDDMConfiguration._ddmConfiguration
- OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._intervalForRequiringCredentials
- OBJC_IVAR_$_SUOSULoginCredentialPolicyManager._lock
- OBJC_IVAR_$_SUOSUMSUScanOptions._fetchMajorUpdates
- OBJC_IVAR_$_SUOSUMSUScanOptions._fetchMinorUpdates
- OBJC_IVAR_$_SUOSUManagedGlobalSettings._ddmConfiguration
- OBJC_IVAR_$_SUOSUMobileSoftwareUpdateController._managedGlobalSettings
- OBJC_IVAR_$_SUOSUServiceDaemon._availableUpdates
- OBJC_IVAR_$_SUOSUServiceDaemon._clients
- OBJC_IVAR_$_SUOSUServiceDaemon._majorOSUpdateStatus
- OBJC_IVAR_$_SUOSUShimController._availableUpdatesObserverToken
- OBJC_IVAR_$_SUOSUShimController._currentlyFetchingMajorOSUpdateForURLScheme
- OBJC_IVAR_$_SUOSUShimController._hasIgnoredUpdatesObserverToken
- _AutoDownloaded
- _AvailableForDownload
- _BundlePath
- _EvaluationDate
- _FreeSpaceRequired
- _IABundleIdentifier
- _NotificationDelay
- _OBJC_CLASS_$_ADMSystem
- _OBJC_CLASS_$_SUCorePolicyDDMConfiguration
- _OBJC_CLASS_$_SUOSUManagedGlobalSettings
- _OBJC_METACLASS_$_SUOSUDDMConfiguration
- _OBJC_METACLASS_$_SUOSUManagedGlobalSettings
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _RemainingReminders
- _ReminderIntervals
- _SUAppStoreAvailableUpdatesChangedNotification
- _SUAppStoreHasIgnoredUpdatesChangedNotification
- _SUNotificationMajorOSUpdateSource
- _SUOSUCloseAction
- _SUOSUMajorOSAction
- _SUOSUMajorOSOtherAction
- _SUOSUMajorOSUpdateAutoDownloadedType
- _SUOSUMajorOSUpdateAvailableForDownloadType
- _SUOSUMajorOSUpdateIdentifier
- _SUOSUMajorOSUpdateMSUType
- _SUOSUMajorOSUpdatePendingType
- _SUOSUMajorOSUpdateRequestedType
- _SUOSUMajorOSUpdateRestartingType
- _SUOSUNotificationUserInfoMajorOSTagsKey
- _SUOSUNotificationUserInfoMajorOSURLKey
- _SUOSUOkAction
- _SUOSUUpdatesAvailableOfferLaterIdentifier
- _SUOSUkDDMStatePersistencePath
- _SUTags
- __101-[SUOSUManagedServiceDaemon scheduleEnforcedManagedUpdateWithVersion:forDate:withOptions:completion:]_block_invoke.338
- __103-[SUOSUNotificationManagerController postDoItLaterUpdatesFailedNotificationRestartRequired:offerLater:]_block_invoke.27
- __105-[SUOSUShimController startScanningForLegacyUpdatesOnlyEvenIfUnchanged:background:withCompletionHandler:]_block_invoke.334
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.445
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.445.cold.1
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.449
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.449.cold.1
- __106-[SUOSUShimController _startShowingProgressForUpdates:mdmInitiated:cancellationHandler:successCompletion:]_block_invoke.449.cold.2
- __113-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptors:inBackground:mdmInitiated:completion:]_block_invoke.419
- __113-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptors:inBackground:mdmInitiated:completion:]_block_invoke.422
- __113-[SUOSUServiceDaemon downloadAndPrepareMobileSoftwareUpdateWithDescriptors:inBackground:mdmInitiated:completion:]_block_invoke_2.423
- __116-[SUOSUMobileSoftwareUpdateController commitStashForDescriptor:withOverrides:withProgressCompletion:withCompletion:]_block_invoke.310
- __123-[SUOSUShimController _startInstallingUpdatesRequiringNoPostInstallAction:inForeground:nowIsLater:mdmInitiated:completion:]_block_invoke.516
- __129-[SUOSUNotificationManagerController postDDMNotificationForScheduledUpdate:updateVersion:ignoreDoNotDisturb:companyName:options:]_block_invoke.71
- __132-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]_block_invoke.299
- __132-[SUOSUMobileSoftwareUpdateController downloadAndPrepareDescriptor:inBackground:mdmInitiated:withProgressCompletion:withCompletion:]_block_invoke.299.cold.1
- __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.424
- __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.426
- __165-[SUOSUShimController startInstallingMajorOSVersion:orWithMajorOSBundleIdentifier:majorOSVariant:shouldOpenIA:inForeground:isMDMInitiated:fromAvailableMajorUpdates:]_block_invoke.426.cold.1
- __39-[SUOSUServiceDaemon _laterDidNotOccur]_block_invoke.547
- __41-[SUOSUServiceDaemon armClientsWithMode:]_block_invoke.466
- __42-[SUOSUMDMController updateStatusForKeys:]_block_invoke.82
- __42-[SUOSUServiceDaemon doPeriodicMDMActions]_block_invoke.311
- __42-[SUOSUServiceDaemon doPeriodicMDMActions]_block_invoke.321
- __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.525
- __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.526
- __48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke.529
- __49-[SUOSUServiceDaemon appQuitCompleteForObserver:]_block_invoke.532
- __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.349
- __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.349.cold.1
- __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.350
- __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.351
- __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.356
- __50-[SUOSUServiceDaemon _handleBackgroundSplatApply:]_block_invoke.356.cold.1
- __50-[SUOSUServiceDaemon rollbackSplatWithCompletion:]_block_invoke.510
- __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.350
- __51-[SUOSUShimController _handleForegroundSplatApply:]_block_invoke.350.cold.1
- __55-[SUOSUNotificationManagerController _connectToService]_block_invoke.86
- __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.328
- __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.328.cold.1
- __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.335
- __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.338
- __56-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke.338.cold.1
- __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.553
- __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.554
- __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.554.cold.1
- __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.555
- __57-[SUOSUServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.555.cold.1
- __57-[SUOSUShimController observeForegroundInstallInProgress]_block_invoke.431
- __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke.376
- __59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_2.377
- __62-[SUOSUServiceDaemon _downloadAndPrepareMDMUpdateWithOptions:]_block_invoke.535
- __62-[SUOSUServiceDaemon _downloadAndPrepareMDMUpdateWithOptions:]_block_invoke.535.cold.1
- __62-[SUOSUServiceDaemon applyMobileSoftwareUpdateWithCompletion:]_block_invoke.445
- __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.525
- __63-[SUOSUShimController _installConfigDataUpdateWithProductKeys:]_block_invoke.525.cold.1
- __64-[SUOSUServiceDaemon _wakeUpAndWaitForNotificationManagerClient]_block_invoke.521
- __65-[SUOSUNotificationManagerController _authorizeServiceForInstall]_block_invoke.91
- __67-[SUOSUNotificationManagerController triggerAppleConnectWithError:]_block_invoke.67
- __67-[SUOSUServiceDaemon performSemiSplatForDescriptor:withCompletion:]_block_invoke.511
- __69-[SUOSUNotificationManagerController startInstallingDoItLaterUpdates]_block_invoke.43
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.492
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.493
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.502
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.505
- __70-[SUOSUShimController _startInstallingUpdates:withWindow:withOptions:]_block_invoke.508
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.437
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.440
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.440.cold.1
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.440.cold.2
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.440.cold.3
- __72-[SUOSUShimController _startShowingProgressForProductKeys:mdmInitiated:]_block_invoke.440.cold.4
- __76-[SUOSUMobileSoftwareUpdateController scanForUpdatesWithOptions:completion:]_block_invoke.cold.5
- __79-[SUOSUNotificationManagerController postMajorOSUpdateMDMRequestedNotification]_block_invoke.22
- __79-[SUOSUNotificationManagerController postMajorOSUpdateMDMRequestedNotification]_block_invoke.cold.1
- __79-[SUOSUServiceDaemon startInstallingExternalUpdateWithProductKeys:withOptions:]_block_invoke.514
- __80-[SUOSUNotificationManagerController startInstallingUpdatesForKeys:withOptions:]_block_invoke.48
- __81-[SUOSUNotificationManagerController postDoItLaterOtherUsersLoggedInNotification]_block_invoke.32
- __83-[SUOSUServiceDaemon allAvailableMDMMobileSoftwareUpdateDescriptorsWithCompletion:]_block_invoke.373
- __83-[SUOSUServiceDaemon allAvailableMDMMobileSoftwareUpdateDescriptorsWithCompletion:]_block_invoke.417
- __85-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:withCompletion:]_block_invoke.474
- __85-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:withCompletion:]_block_invoke.477
- __85-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:withCompletion:]_block_invoke.cold.1
- __88-[SUOSUServiceDaemon triggerSplatRevokedNotificationWithVersion:options:withCompletion:]_block_invoke.478
- __89-[SUOSUServiceDaemon startPostLogoutActionsForExternalUpdateWithProductKeys:withOptions:]_block_invoke.517
- __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.497
- __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.497.cold.1
- __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.497.cold.2
- __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.499
- __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.499.cold.1
- __91-[SUOSUServiceDaemon performMSUUpdateForProductKeys:orProductMarketingVersion:withOptions:]_block_invoke.500
- __92-[SUOSUNotificationManagerController startInstallingMDMMajorOSUpdateWithBundleId:orVersion:]_block_invoke.54
- __93-[SUOSUShimController _startShowingProgressForExternalUpdate:mdmInitiated:successCompletion:]_block_invoke.454
- __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.541
- __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.545
- __95-[SUOSUShimController _startRestartCountdownOperationForUpdates:options:downloadedAndPrepared:]_block_invoke.548
- __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke.323
- __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke.329
- __95-[SUOSUShimController startScanningForUpdatesEvenIfUnchanged:background:withCompletionHandler:]_block_invoke_2.330
- __OBJC_$_CLASS_METHODS_SUOSUDDMConfiguration
- __OBJC_$_CLASS_METHODS_SUOSUManagedGlobalSettings
- __OBJC_$_INSTANCE_METHODS_SUOSUDDMConfiguration
- __OBJC_$_INSTANCE_METHODS_SUOSUManagedGlobalSettings
- __OBJC_$_INSTANCE_VARIABLES_SUOSUDDMConfiguration
- __OBJC_$_INSTANCE_VARIABLES_SUOSUManagedGlobalSettings
- __OBJC_$_PROP_LIST_SUOSUDDMConfiguration
- __OBJC_$_PROP_LIST_SUOSUManagedGlobalSettings
- __OBJC_CLASS_RO_$_SUOSUDDMConfiguration
- __OBJC_CLASS_RO_$_SUOSUManagedGlobalSettings
- __OBJC_METACLASS_RO_$_SUOSUDDMConfiguration
- __OBJC_METACLASS_RO_$_SUOSUManagedGlobalSettings
- ___39+[SUOSUDDMConfiguration sharedInstance]_block_invoke
- ___44+[SUOSUManagedGlobalSettings sharedInstance]_block_invoke
- ___48-[SUOSUServiceDaemon invokeNowIsLaterWithReply:]_block_invoke_3
- ___54-[SUOSUServiceDaemon _activeNotificationManagerClient]_block_invoke
- ___59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_3
- ___59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_4
- ___59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_5
- ___59-[SUOSUShimController _registerForStateChangeNotifications]_block_invoke_6
- ___64-[SUOSUUpdateController commitStashOnlyForDescriptor:withError:]_block_invoke
- ___65-[SUOSUUpdateController commitStashOnlyWithDescriptor:withError:]_block_invoke
- ___68-[SUOSUServiceDaemon postMDMRequestedNotificationToAllLoggedInUsers]_block_invoke
- ___68-[SUOSUServiceDaemon postMDMRequestedNotificationToAllLoggedInUsers]_block_invoke_2
- ___69-[SUOSUShimController _performDiskSpaceCheckForUpdates:mdmInitiated:]_block_invoke
- ___73-[SUOSUUpdateController setClientExternalizedLocalAuthenticationContext:]_block_invoke
- ___79-[SUOSUNotificationManagerController postMajorOSUpdateMDMRequestedNotification]_block_invoke
- ___80-[SUOSUUpdateController attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:]_block_invoke
- ___85-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:withCompletion:]_block_invoke
- ___92-[SUOSUServiceDaemon attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:withCompletion:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e8_v12?0B8l
- __block_literal_global.24
- __block_literal_global.29
- __block_literal_global.314
- __block_literal_global.323
- __block_literal_global.34
- __block_literal_global.353
- __block_literal_global.36
- __block_literal_global.376
- __block_literal_global.38
- __block_literal_global.40
- __block_literal_global.439
- __block_literal_global.45
- __block_literal_global.460
- __block_literal_global.462
- __block_literal_global.464
- __block_literal_global.47
- __block_literal_global.476
- __block_literal_global.495
- __block_literal_global.51
- __block_literal_global.510
- __block_literal_global.516
- __block_literal_global.519
- __block_literal_global.528
- __block_literal_global.56
- __block_literal_global.58
- __block_literal_global.60
- __block_literal_global.62
- __block_literal_global.64
- __block_literal_global.66
- _objc_msgSend$_allowedToRequireCredentials
- _objc_msgSend$_changeCurrentPolicyMode:withReason:
- _objc_msgSend$_downloadAndPrepareInProgressForUpdate:withCompletion:
- _objc_msgSend$_handleAvailableUpdatesChangedWithNotificationNamed:
- _objc_msgSend$_handleAvailableUpdatesChangedWithNotificationNamed:updateClients:
- _objc_msgSend$_performDiskSpaceCheckForUpdates:mdmInitiated:
- _objc_msgSend$_queue_chooseActiveNotificationManagerClient
- _objc_msgSend$_reasonThatQuittingWillBeNoisyOrLoseData
- _objc_msgSend$_roundToMB:
- _objc_msgSend$_scanForMobileSoftwareUpdateDescriptorsInBackground:getMinor:getMajor:mdmInitiated:requestedProductMarketingVersion:withCompletion:
- _objc_msgSend$_willAutoInstallProduct:
- _objc_msgSend$allowScanForMajorMSUAsset
- _objc_msgSend$appNamesThatWillPreventRestart
- _objc_msgSend$arrayWithObject:
- _objc_msgSend$attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:withCompletion:
- _objc_msgSend$automaticallyDownload
- _objc_msgSend$automaticallyDownloadManaged
- _objc_msgSend$automaticallyInstallOSUpdates
- _objc_msgSend$automaticallyInstallOSUpdatesManaged
- _objc_msgSend$automaticallyInstallSystemAndSecurityUpdates
- _objc_msgSend$automaticallyInstallSystemAndSecurityUpdatesManaged
- _objc_msgSend$commitStashOnlyForDescriptor:withError:
- _objc_msgSend$credentialsHarvested
- _objc_msgSend$currentLoginCredentialPolicyMode
- _objc_msgSend$currentSystem
- _objc_msgSend$daysToSeconds:
- _objc_msgSend$defaultAdminDeferralPeriodOfType:
- _objc_msgSend$disableSoftwareUpdateNotifications
- _objc_msgSend$doMDMMajorOSUpdateWithBundleId:withVersion:withError:
- _objc_msgSend$enableGlobalNotifications
- _objc_msgSend$enableRapidSecurityResponse
- _objc_msgSend$enableRapidSecurityResponseRollback
- _objc_msgSend$fetchMajorOSInfoWithIconForProductKey:
- _objc_msgSend$fetchMajorUpdates
- _objc_msgSend$fetchMinorUpdates
- _objc_msgSend$formatter
- _objc_msgSend$getCurrentLoginCredentialPolicy
- _objc_msgSend$globalSettings
- _objc_msgSend$initWithArray:
- _objc_msgSend$initWithProduct:reason:sharedPrefs:
- _objc_msgSend$initWithSharedPrefs:intervalForRequiringCredentials:
- _objc_msgSend$initWithStatePersistencePath:
- _objc_msgSend$intervalForRequiringCredentials
- _objc_msgSend$isOwner
- _objc_msgSend$isSplatAssetType
- _objc_msgSend$localUserWithName:error:
- _objc_msgSend$majorOSVariant
- _objc_msgSend$managedGlobalSettings
- _objc_msgSend$postMDMRequestedNotificationToAllLoggedInUsers
- _objc_msgSend$postMajorOSUpdateMDMRequestedNotification
- _objc_msgSend$postMajorOSUpdateMDMRequestedNotificationWithCompletionHandler:
- _objc_msgSend$queueDescriptorForInstallTonight:withReason:
- _objc_msgSend$recommendedUpdatesDidChange
- _objc_msgSend$removeAllInvalidDeclarations
- _objc_msgSend$removeAllMobileSoftwareUpdatesFromInstallLater
- _objc_msgSend$removeMobileSoftwareUpdatesToInstallLater
- _objc_msgSend$requestMDMMajorOSDownloadAndUpdateWithBundleID:orVersion:withError:
- _objc_msgSend$setAvailableUpdatesObserverToken:
- _objc_msgSend$setClientExternalizedLocalAuthenticationContext:withCompletion:
- _objc_msgSend$setClientExternalizedLocalAuthenticationContextAsync:withCompletion:
- _objc_msgSend$setCurrentLoginCredentialPolicyMode:
- _objc_msgSend$setFetchMajorUpdates:
- _objc_msgSend$setFetchMinorUpdates:
- _objc_msgSend$setHasIgnoredUpdatesObserverToken:
- _objc_msgSend$setLastPostedMajorOSUpdatesAvailableNotificationToDate:
- _objc_msgSend$setMobileSoftwareUpdateDescriptorToInstallLater:withReason:
- _objc_msgSend$systemUpdatesDeferralPeriod
- _objc_msgSend$updateMajorProduct:
- _objc_msgSend$updatePolicyForDownloadedAndPreparedProduct:
- _objc_msgSend$updatePolicyForInstallTonightWithProduct:
- _objc_msgSend$userIsOwner
- _objc_msgSend$usernameForCurrentAuditTokenWithOutUID:
CStrings:
+ "#'"
+ "%@ (%@, %@)"
+ "%@: %@ is stale - using required interval %f"
+ "%@: %f since last harvest, allowed: %hhd"
+ "%@: %llu additional bytes of free space required, suspending MA can reclaim %llu."
+ "%@: %llu bytes free (%llu required) after suspending MobileAsset."
+ "%@: Allowed to require credentials, promoted mode to %@"
+ "%@: Cancelling existing scheduled app close notification."
+ "%@: Could not find client for installing DIL updates."
+ "%@: Create & persist stash failed with error: %@"
+ "%@: Create & persist stash succeeded"
+ "%@: Current client ID %@ does not match our client ID %@, assuming no update downloaded and prepared."
+ "%@: Current free space (%llu) <= required space (%llu), will disable optional PSUS assets."
+ "%@: Current free space (%llu) > required space (%llu), will limit optional PSUS assets to %@ bytes."
+ "%@: Deciding if we should suspend MobileAsset to reclaim %llu bytes."
+ "%@: Device already has sufficient free space. Required: %llu, free: %llu"
+ "%@: Download/prepare already in progress, skipping background scan."
+ "%@: Error querying current MSU state: %@"
+ "%@: Failed to check current free space, will disable optional PSUS assets. %@"
+ "%@: Failed to predict inactivity period: %@"
+ "%@: Failed to query current free space: %@"
+ "%@: Failed to query msu controller state, assuming no update downloaded and prepared"
+ "%@: Failed to re-query free space after suspending, assuming we have enough. Error: %@"
+ "%@: Failed to reclaim enough space. %llu bytes reclaimed, error: %@"
+ "%@: Failed to reclaim space with error: %@"
+ "%@: Failed to reclaim sufficient space."
+ "%@: Fake notification delay: %@ seconds."
+ "%@: Faking mobileAssetEstimateEvictable success."
+ "%@: Insufficient free space after suspending MobileAsset. Current: %llu, required: %llu"
+ "%@: MA was suspended, cancelling update."
+ "%@: No active client, will not fire notification for apps that may prevent logout/shutdown."
+ "%@: No contextUserID set, assuming stash is still required."
+ "%@: No predicted inactivity window, not scheduling app close notification."
+ "%@: No update downloaded and prepared."
+ "%@: No userID provided."
+ "%@: Posting %@ notification."
+ "%@: Predicting an inactivity between %@ and %@"
+ "%@: Refreshed available updates; new updates: [%@]; new major updates: [%@]"
+ "%@: Refreshing all available updates on behalf of %@ notification."
+ "%@: Refreshing available updates after startup."
+ "%@: Returning %@"
+ "%@: Scheduler is not armed, or no update is queued. Will not post app closer notification."
+ "%@: Scheduling app close notification for %@"
+ "%@: Should show updates available notification? no, %@"
+ "%@: Should show updates available notification? yes, %@"
+ "%@: Splat will auto install, using mode %@"
+ "%@: Successfully suspended MA."
+ "%@: Suspending MA reclaimed %llu bytes"
+ "%@: Suspending MA to reclaim at least %llu bytes."
+ "%@: Suspending MA would not reclaim enough enough space. Error: %@"
+ "%@: Unexpected user action requested: %@"
+ "%@: User-side stash during queue for later %s"
+ "%@: Using %@ as the latest qualifying product."
+ "%@: [internal only] last successful background scan was %@, skipping background scan."
+ "%@: additionalRequiredBytes: %llu, suspend estimate: %llu, error: %@"
+ "%@: fakeMaxPreSUStagingSize is set: %@"
+ "%@: no need to set properties b/c updates didn't change"
+ "%@: predicted date: %@"
+ "%@: product:%@, willAutoInstall:%hhd, autoUpdatesEnabled:%hhd, willAutoInstallThisProduct:%hhd, queuedForInstallTonight:%hhd"
+ "%@: queryDate: %@, confidence: %ld, confidence level: %.2f"
+ "%@: set externalized context with policy mode: %lu"
+ "%s is set, but can't read array from %@: %@"
+ "%s is set: %@"
+ "%s: Already posted final notification for %@"
+ "%s: Auto Install Tonight is no longer offered for %@"
+ "%s: Canceling updatesAvailableNotificationTimerSource"
+ "%s: Current major (%ld) and target major (%ld) don't match"
+ "%s: Detected managed portable mac & restarting now, taking User Activity assertion"
+ "%s: Detected non-supervised mac, taking Idle Sleep assertion"
+ "%s: Device (%@) is aligned to update (%@)"
+ "%s: Device list query failed: %@"
+ "%s: Disk space isn't sufficient (required = %llu, free = %llu), invoking CacheDelete"
+ "%s: Disk space isn't sufficient (total required = %llu, free = %llu, reclaimable space = %llu), posting insufficient space notification"
+ "%s: Failed to get iCloud account (not signed in?)"
+ "%s: Fetched device list: %@"
+ "%s: Fetching devices for %@"
+ "%s: Found device %@: %@"
+ "%s: Incrementing count for product %@: %lu"
+ "%s: Install Tonight isn't allowed for %@"
+ "%s: Invalid PMV: %@"
+ "%s: Invalid case - trying to set a version (%@) that's the same as current OS"
+ "%s: Invalid kKeyStashBagValidOnDisk value"
+ "%s: Legacy updates (%@) downloaded? %@, %@)"
+ "%s: MKBKeyBagKeyStashVerifyWithOpts returned nil"
+ "%s: MSU update is downloaded & prepared: %@"
+ "%s: MSU update is not yet downloaded & prepared: %@"
+ "%s: MSU update is revoked: %@"
+ "%s: Minimum notification interval override set: %0.1f"
+ "%s: No cloud devices"
+ "%s: No last notification date"
+ "%s: No major OS update"
+ "%s: No minor OS update"
+ "%s: No predicted inactivity date"
+ "%s: No product name for %@ (model = %@)"
+ "%s: Posting com.apple.SoftwareUpdate.updatesAvailable notification"
+ "%s: Predicted inactivity is in the past, posting now"
+ "%s: Removed %lu invalid declarations"
+ "%s: Resetting count for new product: %@ -> %@"
+ "%s: Restart required for %@"
+ "%s: Returning cached device list (fetched %@): %@"
+ "%s: Scheduling for %@ (%lld seconds)"
+ "%s: Should show security advisory? %@ (current = %@, target = %@)"
+ "%s: Skipping non-recommended update: %@"
+ "%s: Skipping ramped update: %@"
+ "%s: Skipping rolled back splat update: %@"
+ "%s: This is the final notification for %@, disabling Install Tonight"
+ "%s: Time interval since last notification: %0.1f (minimum: %0.1f)"
+ "%s: Timed out fetching devices"
+ "%s: Update eligible: %@"
+ "%s: Updates available notification already scheduled"
+ "%s: UpdatesAvailableNotificationDelay set, scheduling for %lld seconds"
+ "%s: Using minimum interval: %lu days (count: %lu)"
+ "%s: disableDeviceCompatibilityNotification is set"
+ "%s: disableSecurityAdvisoryNotification is set"
+ "%s: splat is disabled"
+ "%s: uid: %d, stashState: %d, result: %ld\n"
+ "(b)"
+ "+[SUOSUUtilities parseProductMarketingVersion:systemVersion:]"
+ "-[SUOSUCloudDeviceManager devices]"
+ "-[SUOSUCloudDeviceManager devices]_block_invoke"
+ "-[SUOSUManagedServiceDaemon invalidAndRemoveOldDeclarations]_block_invoke"
+ "-[SUOSUServiceDaemon _mobileKeyBagStashStateForUser:]"
+ "-[SUOSUServiceDaemon doBackgroundActionsWithCompletion:]_block_invoke"
+ "-[SUOSUServiceDaemon scheduleUpdatesAvailableBSDNotification]_block_invoke"
+ "-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:]_block_invoke"
+ "-[SUOSUShimController availableUpdatesDownloaded]"
+ "-[SUOSUUpdateController _setIdleSleepPowerAssertion:]"
+ "-[SUOSUUpdatesAvailablePolicy _determineEligibleProducts]"
+ "-[SUOSUUpdatesAvailablePolicy _determineNotificationInterval]"
+ "-[SUOSUUpdatesAvailablePolicy _nowExceedsLastNotificationDate]"
+ "-[SUOSUUpdatesAvailablePolicy _shouldShowDeviceCompatibilityNotificationForDevice:]"
+ "-[SUOSUUpdatesAvailablePolicy _shouldShowSecurityAdvisoryNotification]"
+ "-[SUOSUUserPrefs recordPostedUpdatesAvailableNotificationWithProduct:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "14.3"
+ "14.3.1"
+ "15.0"
+ "15.0.1"
+ "24A280"
+ "6.7"
+ "@\"NSArray\"8@?0"
+ "@\"SUOSUCloudDevice\""
+ "@\"SUOSULoginCredentialCacheInfo\""
+ "@\"SUOSUServiceClientManager\""
+ "@\"_OSInactivityPredictionClient\""
+ "@40@0:8{?=qqq}16"
+ "@48@0:8@16Q24q32@40"
+ "ApplicationsMayBlockRestart"
+ "AvailableUpdatesNotificationCountKey"
+ "AvailableUpdatesNotificationProductKey"
+ "B24@0:8^Q16"
+ "B24@0:8^{?=qqq}16"
+ "B32@0:8@16^{?=qqq}24"
+ "B32@0:8Q16^@24"
+ "Background=%hhd, MDMInitiated=%hhd, BuddyInitiated=%hhd, requestedPMV=%@)"
+ "BytesRequired"
+ "ConfirmDisableAppleIntelligence"
+ "Controller: Found Qualifying MajorOSProduct %@ - %@ (%@)"
+ "Controller: Not considering majorOS update (%@) as qualifying because it is not MSU-based."
+ "Controller: Not considering majorOS update (%@) as qualifying because it is not major."
+ "D"
+ "DDM declaration is scheduled within the next 24 hours"
+ "DeviceHandle"
+ "FakeCloudDevicesPlist"
+ "FakeCurrentOperatingSystemVersion"
+ "Install Tonight is armed"
+ "InsufficientSpace"
+ "LockScreen"
+ "NotReq"
+ "OfferInstallTonight"
+ "Opp"
+ "PRODUCT_SHORT_ATTRIBUTED_DESCRIPTION"
+ "PRODUCT_SHORT_DESCRIPTION"
+ "REMIND_ME_LATER"
+ "ReadMeLongSummaryPreview"
+ "ReadMeShortSummaryPreview"
+ "Req"
+ "SHOULDN'T DISPLAY REGULAR TITLE! THIS IS A MAJOR PRODUCT!"
+ "SHOULDN'T DISPLAY REGULAR VERSION! THIS IS A MAJOR PRODUCT!"
+ "SUOSUCloudDevice"
+ "SUOSUCloudDeviceManager"
+ "SUOSUInactivityPredictor"
+ "SUOSULoginCredentialCacheInfo"
+ "SUOSULoginCredentialPolicy: grabbed user ID %@"
+ "SUOSUServiceClientManager"
+ "SUOSUUpdatesAvailablePolicy"
+ "Settings is active"
+ "Setup Assistant is active"
+ "StashBagValidOnDisk"
+ "T@\"NSArray\",&,V_availableProducts"
+ "T@\"NSArray\",&,V_cachedDevices"
+ "T@\"NSArray\",&,V_cloudDevices"
+ "T@\"NSArray\",&,V_eligibleProducts"
+ "T@\"NSAttributedString\",&,V_shortAttributedDescription"
+ "T@\"NSDate\",&,V_cacheDate"
+ "T@\"NSDate\",&,V_endDate"
+ "T@\"NSDate\",&,V_lastNotificationDate"
+ "T@\"NSDate\",&,V_startDate"
+ "T@\"NSDictionary\",&,V_firstInstallTonightDates"
+ "T@\"NSMutableArray\",&,V_sunmClients"
+ "T@\"NSNumber\",&,V_alignediOSMajorVersion"
+ "T@\"NSNumber\",V_minimumNotificationIntervalOverride"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_appCloseNotificationTimerSource"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_updatesAvailableNotificationTimerSource"
+ "T@\"NSString\",&,V_clientID"
+ "T@\"NSString\",&,V_lastNotificationProductKey"
+ "T@\"NSString\",&,V_operatingSystemName"
+ "T@\"NSString\",&,V_operatingSystemVersion"
+ "T@\"NSString\",R,V_deviceCompatibilityNotificationBodyString"
+ "T@\"NSString\",R,V_deviceCompatibilityNotificationTitleString"
+ "T@\"NSString\",R,V_securityAdvisoryNotificationBodyString"
+ "T@\"NSString\",R,V_securityAdvisoryNotificationTitleString"
+ "T@\"SUOSUCloudDevice\",&,V_alignedCloudDevice"
+ "T@\"SUOSULoginCredentialCacheInfo\",&,V_cachedInfo"
+ "T@\"SUOSUMobileSoftwareUpdateController\",&,V_msuController"
+ "T@\"SUOSUProduct\",&,V_majorProduct"
+ "T@\"SUOSUProduct\",&,V_minorProduct"
+ "T@\"SUOSUProduct\",&,V_splatProduct"
+ "T@\"SUOSUProduct\",R"
+ "T@\"SUOSUServiceClientManager\",&,V_clientManager"
+ "T@\"_OSInactivityPredictionClient\",&,V_client"
+ "TB,R,V_disableDeviceCompatibilityNotification"
+ "TB,R,V_disableSecurityAdvisoryNotification"
+ "TB,V_allowedToUseInstallTonight"
+ "TB,V_alreadyPostedFinalNotification"
+ "TB,V_autoDownloadEnabled"
+ "TB,V_availableProductsDownloaded"
+ "TB,V_collectCredentialHarvestingInfo"
+ "TB,V_ddmEnforcedWithin24Hours"
+ "TB,V_downloadedAndPrepared"
+ "TB,V_majorOSUpdatesManaged"
+ "TB,V_notificationsDisabled"
+ "TB,V_offerLater"
+ "TB,V_restartRequired"
+ "TB,V_settingsIsActive"
+ "TB,V_setupAssistantIsActive"
+ "TB,V_splatAppliedRestartNow"
+ "TB,V_splatAppliedUpdateNow"
+ "TQ"
+ "TQ,V_notificationCount"
+ "Td,V_defaultRequiredInterval"
+ "Td,V_minimumNotificationInterval"
+ "Td,V_staleUpdateInterval"
+ "Td,V_staleUpdateRequiredInterval"
+ "Ti,V_backgroundScanNotifyToken"
+ "Ti,V_clientScanNotifyToken"
+ "Tonight"
+ "Tq,V_stashState"
+ "T{?=qqq},V_currentOSVersion"
+ "URLForResource:withExtension:"
+ "[CRITICAL] macOS Sonoma"
+ "[LEGACY] AppleConnect"
+ "[MAJOR] macOS Sequoia"
+ "[MINOR] macOS Sonoma"
+ "[SPLAT COMBO] macOS Sonoma"
+ "[SPLAT] macOS Security Response"
+ "_alignedCloudDevice"
+ "_alignediOSMajorVersion"
+ "_allowedToRequireCredentialsForProductKey:"
+ "_allowedToUseInstallTonight"
+ "_alreadyPostedFinalNotification"
+ "_appCloseNotificationTimerSource"
+ "_autoDownloadEnabled"
+ "_availableProducts"
+ "_availableProductsDownloaded"
+ "_backgroundScanNotifyToken"
+ "_cacheDate"
+ "_cachedDevices"
+ "_cachedInfo"
+ "_cancelScheduledAppCloseNotification"
+ "_clientID"
+ "_clientManager"
+ "_clientScanNotifyToken"
+ "_cloudDevices"
+ "_collectCredentialHarvestingInfo"
+ "_commitStashOnlyForDescriptor:withError:"
+ "_configureOverridesForOptionalPSUSDownload:forDescriptor:"
+ "_currentOSVersion"
+ "_ddmEnforcedWithin24Hours"
+ "_defaultRequiredInterval"
+ "_determineEligibleProducts"
+ "_determineNotificationInterval"
+ "_determineNotificationType"
+ "_deviceCompatibilityNotificationBodyString"
+ "_deviceCompatibilityNotificationTitleString"
+ "_disableDeviceCompatibilityNotification"
+ "_disableSecurityAdvisoryNotification"
+ "_downloadedAndPrepared"
+ "_eligibleProducts"
+ "_endDate"
+ "_firstInstallTonightDates"
+ "_handleSuccessfullyCompletedScan"
+ "_insufficientDiskSpaceErrorForProducts:spaceRequired:underlyingError:"
+ "_isUpdateDownloadedAndPreparedWithCompletion:"
+ "_lastNotificationDate"
+ "_lastNotificationProductKey"
+ "_majorOSUpdatesManaged"
+ "_minimumNotificationInterval"
+ "_minimumNotificationIntervalOverride"
+ "_minorProduct"
+ "_mobileKeyBagStashStateForUser:"
+ "_modeFromCachedInfo:"
+ "_msuController"
+ "_notificationCount"
+ "_notificationsDisabled"
+ "_nowExceedsLastNotificationDate"
+ "_offerLater"
+ "_operatingSystemName"
+ "_operatingSystemVersion"
+ "_postAppCloseNotificationIfAppropriate"
+ "_productNameForModel:"
+ "_promptAndSuspendMobileAssetIfNecessaryWithFreeSpaceRequired:suspendedMobileAsset:error:"
+ "_queue_disarmLaterObserver"
+ "_reclaimDiskSpaceIfNecssaryWithBytesRequired:bytesReclaimed:error:"
+ "_refreshAllAvailableUpdatesAndNotifyDelegate"
+ "_registerForScanCompletionNotification:outToken:"
+ "_reminderDaysForCount:"
+ "_reminderDaysForCount:finalNotification:"
+ "_restartRequired"
+ "_securityAdvisoryNotificationBodyString"
+ "_securityAdvisoryNotificationTitleString"
+ "_setIdleSleepPowerAssertion:"
+ "_setMobileSoftwareUpdateDescriptorToInstallLater:withReason:stashState:"
+ "_settingsIsActive"
+ "_setupAssistantIsActive"
+ "_shouldIgnoreDescriptorFromScan:withOptions:"
+ "_shouldShowDeviceCompatibilityNotificationForDevice:"
+ "_shouldShowNotificationWithReason:"
+ "_shouldShowSecurityAdvisoryNotification"
+ "_splatAppliedRestartNow"
+ "_splatAppliedUpdateNow"
+ "_splatProduct"
+ "_staleUpdateInterval"
+ "_staleUpdateRequiredInterval"
+ "_startDate"
+ "_stashState"
+ "_sunmClients"
+ "_updatesAvailableNotificationTimerSource"
+ "_willAutoInstallDescriptor:withProductKey:"
+ "a"
+ "aa_altDSID"
+ "aa_primaryAppleAccount"
+ "activeNotificationManagerClient"
+ "addClient:"
+ "addCredentialHarvestingInfoWithStashState:"
+ "alignedCloudDevice"
+ "alignediOSMajorVersion"
+ "allClients"
+ "allowedToUseInstallTonight"
+ "already posted final notification"
+ "alreadyPostedFinalNotification"
+ "appCloseNotificationDelay"
+ "appCloseNotificationTimerSource"
+ "appendCredentialHarvestingInfoWithSharedPrefs:stashState:toDict:"
+ "appsThatWillPreventRestart"
+ "attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:completion:"
+ "attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:error:"
+ "autoDownloadEnabled"
+ "autoInstalledCritical"
+ "availableProducts"
+ "availableProductsDownloaded"
+ "availableUpdatesNotificationMinimumIntervalOverride"
+ "backgroundScanNotifyToken"
+ "buildVersion"
+ "cacheDate"
+ "cacheDeletePurgeableSpace"
+ "cacheDeletePurgeableSpaceWithCompletionHandler:"
+ "cachedDevices"
+ "cachedInfo"
+ "cachedMode"
+ "cancelInstallTonight"
+ "clientID"
+ "clientManager"
+ "clientScanNotifyToken"
+ "cloudDeviceName"
+ "cloudDevices"
+ "collectCredentialHarvestingInfo"
+ "com.apple.SoftwareUpdateNotificationManager.ApplicationsMayBlockRestart"
+ "com.apple.SoftwareUpdateNotificationManager.InsufficientSpace"
+ "com.apple.SoftwareUpdateNotificationManager.UpdatesAvailableCustomText"
+ "com.apple.SoftwareUpdateNotificationManager.UpdatesAvailableDeviceCompatibility"
+ "com.apple.SoftwareUpdateNotificationManager.UpdatesAvailableGeneral"
+ "com.apple.SoftwareUpdateNotificationManager.UpdatesAvailableSecurityAdvisory"
+ "com.apple.softwareupdate.AutoBackgroundScanFinished"
+ "com.apple.softwareupdate.ClientInitiatedScanSucceeded"
+ "confidenceLevel"
+ "confidenceValue"
+ "createUserActivityAssertionWithDescription:timeout:"
+ "created"
+ "critical"
+ "criticalNow"
+ "customIconPath"
+ "customText"
+ "dataWithContentsOfURL:"
+ "ddmEnforcedWithin24Hours"
+ "defaultRequiredInterval"
+ "defaultStore"
+ "deviceCompatibility"
+ "deviceCompatibilityNotificationBodyString"
+ "deviceCompatibilityNotificationTitleString"
+ "deviceList"
+ "deviceListWithContext:completion:"
+ "devices"
+ "disableDeviceCompatibilityNotification"
+ "disableMASuspension"
+ "disableSecurityAdvisoryNotification"
+ "documentationDeviceCompatibilityNotificationBodyString"
+ "documentationDeviceCompatibilityNotificationTitleString"
+ "documentationSecurityAdvisoryNotificationBodyString"
+ "documentationSecurityAdvisoryNotificationTitleString"
+ "doubleValue"
+ "downloadedAndPrepared"
+ "eligibleProducts"
+ "enablePreSUStaging"
+ "enablePreSUStagingForOptionalAssets"
+ "endDate"
+ "estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:completion:"
+ "estimateBytesReclaimedBySuspendingMobileAssetWithAdditionalBytesRequired:outEvictableBytes:error:"
+ "evaluateAndPostInstallTonightAppCloseNotification"
+ "fakeCloudDevices"
+ "fakeCurrentOperatingSystemVersion:"
+ "fakeMaxPreSUStagingSize"
+ "fakeMobileAssetEstimateBytesReclaimedSuccess"
+ "firstInstallTonightDates"
+ "firstOfferDateForProductKey:"
+ "general"
+ "html"
+ "https://www.apple.com/macos/macos-sequoia/"
+ "iOS"
+ "iPad"
+ "iPhone"
+ "init:"
+ "initWithClient:startDate:endDate:"
+ "initWithDescriptor:downloadedAndPrepared:"
+ "initWithName:operatingSystemName:operatingSystemVersion:"
+ "initWithProduct:reason:stashState:sharedPrefs:"
+ "initWithSharedPrefs:msuController:installTonightManager:"
+ "initWithStartDate:endDate:"
+ "install in progress"
+ "invalidAndRemoveOldDeclarations"
+ "invalidateAllInvalidDeclarationsReturningAllInvalid"
+ "isPortable"
+ "lastLoginWindowHarvestDate"
+ "lastLoginWindowHarvestMethod"
+ "lastNotificationDate"
+ "lastNotificationProductKey"
+ "lastSuccessfulMSUBackgroundScanDate"
+ "lastVendedPolicyMode"
+ "loadLongSummary"
+ "loadMajorIcon"
+ "loadMinorIcon"
+ "loadShortSummary"
+ "localizedName"
+ "longInactivityPredictionResultAtDate:withTimeSinceInactive:withOptions:withError:"
+ "macOS Sonoma"
+ "mainBundle"
+ "major OS updates are managed"
+ "majorOSUpdatesManaged"
+ "maxPreSUStagingOptionalAssetSize"
+ "minimum interval hasn't been reached"
+ "minimumNotificationInterval"
+ "minimumNotificationIntervalOverride"
+ "minorProduct"
+ "mobileAssetEstimateEvictable:completionQueue:completion:"
+ "mobileAssetSuspend:completionQueue:completion:"
+ "mobileKeyBagStashStateForUser:"
+ "mobileKeyBagStashStateForUser:completion:"
+ "model"
+ "msuController"
+ "no"
+ "no eligible updates"
+ "none"
+ "notificationCount"
+ "notifications disabled"
+ "notificationsDisabled"
+ "operatingSystemName"
+ "optionUserId"
+ "parseProductMarketingVersion:systemVersion:"
+ "persisted"
+ "predictedInactivityDate"
+ "primaryProduct"
+ "q24@0:8Q16"
+ "q32@0:8Q16^B24"
+ "queueAllUpdatesForAutoInstallTonightWithReason:"
+ "queueDescriptorForInstallTonight:withReason:stashState:"
+ "recordPostedUpdatesAvailableNotificationWithProduct:"
+ "refreshCachedLoginCredentialHarvestingMode"
+ "refreshCachedMode"
+ "removeClient:"
+ "roundToMB:"
+ "scheduleUpdatesAvailableBSDNotification"
+ "securityAdvisory"
+ "securityAdvisoryNotificationBodyString"
+ "securityAdvisoryNotificationTitleString"
+ "setAlignedCloudDevice:"
+ "setAlignediOSMajorVersion:"
+ "setAllowedToUseInstallTonight:"
+ "setAlreadyPostedFinalNotification:"
+ "setAltDSID:"
+ "setAppCloseNotificationTimerSource:"
+ "setAutoDownloadEnabled:"
+ "setAvailableProducts:"
+ "setAvailableProductsDownloaded:"
+ "setBackgroundScanNotifyToken:"
+ "setCacheDate:"
+ "setCachedDevices:"
+ "setCachedInfo:"
+ "setClientExternalizedLocalAuthenticationContext:userId:forPolicyMode:completion:"
+ "setClientID:"
+ "setClientManager:"
+ "setClientScanNotifyToken:"
+ "setCloudDevices:"
+ "setCollectCredentialHarvestingInfo:"
+ "setCurrentOSVersion:"
+ "setDdmEnforcedWithin24Hours:"
+ "setDefaultRequiredInterval:"
+ "setDownloadedAndPrepared:"
+ "setEligibleProducts:"
+ "setEnablePreSUStagingForOptionalAssets:"
+ "setEndDate:"
+ "setFirstInstallTonightDateForProductKey:"
+ "setFirstInstallTonightDates:"
+ "setFirstOfferDateForProductKey:"
+ "setIncludeUntrustedDevices:"
+ "setLastLoginWindowHarvestDate:"
+ "setLastLoginWindowHarvestMethod:"
+ "setLastNotificationDate:"
+ "setLastNotificationProductKey:"
+ "setLastSuccessfulMSUBackgroundScanDate:"
+ "setLastVendedPolicyMode:"
+ "setMajorOSUpdatesManaged:"
+ "setMajorProduct:"
+ "setMaxPreSUStagingOptionalAssetSize:"
+ "setMinimumNotificationInterval:"
+ "setMinimumNotificationIntervalOverride:"
+ "setMinorProduct:"
+ "setMobileSoftwareUpdateDescriptorToInstallLater:withReason:userId:"
+ "setMsuController:"
+ "setNotificationCount:"
+ "setNotificationsDisabled:"
+ "setOfferLater:"
+ "setOperatingSystemName:"
+ "setOperatingSystemVersion:"
+ "setOperatingSystems:"
+ "setRestartRequired:"
+ "setServices:"
+ "setSettingsIsActive:"
+ "setSetupAssistantIsActive:"
+ "setSplatAppliedRestartNow:"
+ "setSplatAppliedUpdateNow:"
+ "setSplatProduct:"
+ "setStaleUpdateInterval:"
+ "setStaleUpdateRequiredInterval:"
+ "setStartDate:"
+ "setStashState:"
+ "setSunmClients:"
+ "setUpdatesAvailableNotificationTimerSource:"
+ "settingsIsActive"
+ "shouldShowNotification:"
+ "splatAppliedUpdateNow"
+ "splatAvailable"
+ "splatProduct"
+ "splatReady"
+ "staleUpdateInterval"
+ "staleUpdateRequiredInterval"
+ "startDate"
+ "stashState"
+ "stringForSystemVersion:"
+ "sunmClients"
+ "suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:completion:"
+ "suspendMobileAssetToReclaimDiskSpaceWithAdditionalBytesRequired:error:"
+ "uidFromCurrentAuditToken"
+ "unsignedIntValue"
+ "updateTitleOverride"
+ "updates not downloaded (auto download = %i, splat applied = %i)"
+ "updatesAvailableNotificationCount"
+ "updatesAvailableNotificationDelay"
+ "updatesAvailableNotificationProductKey"
+ "updatesAvailableNotificationTimerSource"
+ "v16@?0q8"
+ "v20@?0@\"SUMacControllerDescriptor\"8B16"
+ "v24@0:8@?<v@?@\"NSNumber\">16"
+ "v24@0:8@?<v@?@\"NSNumber\"@\"NSError\">16"
+ "v24@?0@\"AKDeviceListResponse\"8@\"NSError\"16"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "v28@?0B8Q12@\"NSError\"20"
+ "v32@0:8@16^i24"
+ "v32@0:8Q16@?<v@?B@\"NSError\">24"
+ "v32@0:8Q16@?<v@?BQ@\"NSError\">24"
+ "v36@0:8@\"SUMacControllerDescriptor\"16Q24I32"
+ "v36@0:8@16Q24I32"
+ "v36@0:8Q16Q24B32"
+ "v40@0:8@16Q24q32"
+ "v40@0:8@16q24@32"
+ "v40@0:8{?=qqq}16"
+ "v48@0:8@\"NSData\"16@\"NSNumber\"24Q32@?<v@?B>40"
+ "v48@0:8@16@24Q32@?40"
+ "yes"
+ "{?=\"majorVersion\"q\"minorVersion\"q\"patchVersion\"q}"
+ "{?=qqq}16@0:8"
- "\tmajorSecondaryDescriptor: %@"
- "\tminorSecondaryDescriptor: %@"
- "$Background=%hhd, GetMinor=%hhd, GetMajor=%hhd, MDMInitiated=%hhd, BuddyInitiated=%hhd, requestedPMV=%@)"
- "%@: Adding client: %@"
- "%@: Allowed to require credentials, bumping to ModeRequired."
- "%@: Changed credential harvesting policy from %@ to %@. Reason: %@"
- "%@: DDM deadline has passed, skipping notification interval checks"
- "%@: Download/prepare already in progress, don't issue an MSU background action"
- "%@: Error getting user: %@"
- "%@: Found external update: %@, always assume not downloaded b/c the client maintains their state"
- "%@: MSU update is a revoked splat: %@"
- "%@: MSU update is not yet downloaded & prepared: %@"
- "%@: Not allowed to require credentials, falling back to ModeOpportunistic."
- "%@: OSISClient did start prepping! Notifying user that we're going to do an MDM update"
- "%@: Removing client: %@"
- "%@: Scanning for major OS updates is disabled!"
- "%@: Update version (%@) doesn't match provided build version (%@)"
- "%@: Using custom majorOSVariant: CUSTOMER"
- "%@: Will auto-install MSU %@, new mode is %@"
- "%@: Will auto-install splat %@, new mode is %@"
- "%s: MDM conflicts with DDM, bailing (%@)"
- "%s: Major OS deferral is disabled"
- "%s: Minor OS deferral is disabled"
- "%s: Non OS deferral is disabled"
- "%s: Period: %@"
- "%s: Removing any invalid declarations"
- "%s: This system is managed and splat is disabled"
- "-[SUOSUMDMController doMDMMajorOSUpdateWithBundleId:withVersion:withError:]"
- "-[SUOSUMDMController getMajorOSUpdateStatus:]"
- "-[SUOSUMDMController getUpdateStatus:]"
- "-[SUOSUManagedGlobalSettings majorOSDeferralPeriod]"
- "-[SUOSUManagedGlobalSettings minorOSDeferralPeriod]"
- "-[SUOSUManagedGlobalSettings nonOSDeferralPeriod]"
- "-[SUOSUServiceDaemon setClientExternalizedLocalAuthenticationContext:withCompletion:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/var/db/softwareupdate/SoftwareUpdateDDMStatePersistence.plist"
- "@\"SUOSUManagedGlobalSettings\""
- "@32@0:8@16d24"
- "Allow scan for major MSU asset"
- "BundlePath"
- "CLOSE"
- "Controller: Found Qualifying MajorOSProduct %@ - %@ (%@) - Variant:%@, MSU: %hhd, Major: %hhd"
- "Controller: No MajorOSProducts are currently active, picking newest product %@ - %@ (%@)"
- "Controller: Received %@ notification; new updates: [%@]; new major updates: [%@]"
- "Controller: Received %@ notification; no need to set properties b/c updates didn't change"
- "Controller: Skipping majorOS update (%@) because the fetching of the MajorOSInfo failed.."
- "Create & persist stash finished. Error: %@"
- "Credentials harvested"
- "Downloaded and prepared: %@"
- "EvaluationDate"
- "Found UMA major non-MSU update which will not be presented in SUSettings: %@"
- "Found latest qualifying major MSU product: %@"
- "Free space is within 2 GB of space required for updates, attempt to free up extra space for additional padding"
- "FreeSpaceRequired"
- "IABundleIdentifier"
- "Install Tonight: %@"
- "LSDisplayName"
- "MAJOROS_ACTION"
- "MAJOROS_OTHER_ACTION"
- "MAJOR_OS_BUILD_VERSION"
- "MAJOR_OS_MORE_INFO_LINK"
- "MAJOR_OS_TITLE"
- "MAJOR_OS_VERSION"
- "MajorOSDetailsURL"
- "MajorOSSUTags"
- "MajorOSUpdateMSUNotification"
- "MajorOSUpdatePendingNotification"
- "MajorOSUpdateRequestedNotification"
- "MajorOSUpdateRestartingNotification"
- "MajorOSUserNotificationDate"
- "MaximumNotificationDelay"
- "Not updating clients"
- "OK"
- "PRODUCT_TITLE"
- "PRODUCT_VERSION"
- "Q24@0:8Q16"
- "Quitting %@ will be dirty for reason %@"
- "Recommended updates changed"
- "RemainingReminders"
- "ReminderIntervals"
- "Requesting additional padding for %llu bytes returned: %llu, %@"
- "SUOSUDDMConfiguration"
- "SUOSUManagedGlobalSettings"
- "SUScan: SPIInstallsStagedUpdatesOnly is set, only scanning for MajorOSUpdates that are staged!"
- "SUTags"
- "Set client externalized context with result: %hhd"
- "Successful call to postMajorOSUpdateMDMRequestedNotification"
- "T@\"NSArray\",R,V_availableUpdates"
- "T@\"NSMutableDictionary\",&,N,V_majorOSUpdateStatus"
- "T@\"SUOSUManagedGlobalSettings\",&,V_managedGlobalSettings"
- "T@\"SUSharedPrefs\",&,N,V_sharedPrefs"
- "T@,&,V_availableUpdatesObserverToken"
- "T@,&,V_hasIgnoredUpdatesObserverToken"
- "TB,V_currentlyFetchingMajorOSUpdateForURLScheme"
- "TB,V_fetchMajorUpdates"
- "TB,V_fetchMinorUpdates"
- "Td,V_intervalForRequiringCredentials"
- "T{os_unfair_lock_s=I},V_lock"
- "UpdateAutoDownloadedNotification"
- "UpdateAvailableForDownloadNotification"
- "_allowedToRequireCredentials"
- "_availableUpdateForProductKey:"
- "_availableUpdatesObserverToken"
- "_changeCurrentPolicyMode:withReason:"
- "_convertTelemetryOverrideValueToDDMKey:"
- "_currentlyFetchingMajorOSUpdateForURLScheme"
- "_fetchMajorUpdates"
- "_fetchMinorUpdates"
- "_handleAvailableUpdatesChangedWithNotificationNamed:"
- "_handleAvailableUpdatesChangedWithNotificationNamed:updateClients:"
- "_hasIgnoredUpdatesObserverToken"
- "_intervalForRequiringCredentials"
- "_lock"
- "_majorOSUpdateStatus"
- "_managedGlobalSettings"
- "_performDiskSpaceCheckForUpdates:mdmInitiated:"
- "_productKeysForAppStoreUpdates:"
- "_queue_chooseActiveNotificationManagerClient"
- "_reasonThatQuittingWillBeNoisyOrLoseData"
- "_roundToMB:"
- "_scanForMobileSoftwareUpdateDescriptorsInBackground:getMinor:getMajor:mdmInitiated:requestedProductMarketingVersion:withCompletion:"
- "_scanForMobileSoftwareUpdateDescriptorsInBackground:getMinor:getMajor:withCompletion:"
- "_willAutoInstallProduct:"
- "allowScanForMajorMSUAsset"
- "appNamesThatWillPreventRestart"
- "arrayWithObject:"
- "attemptToReclaimSpaceUsingCacheDeleteWithSpaceRequired:withCompletion:"
- "automaticallyDownload"
- "automaticallyDownloadManaged"
- "automaticallyInstallOSUpdates"
- "automaticallyInstallOSUpdatesManaged"
- "automaticallyInstallSystemAndSecurityUpdates"
- "automaticallyInstallSystemAndSecurityUpdatesManaged"
- "availableUpdatesObserverToken"
- "com.apple.SoftwareUpdateNotificationManager.MajorOSUpdate"
- "com.apple.SoftwareUpdateNotificationManager.UpdatesAvailableOfferLater"
- "commitStashOnlyForDescriptor:withError:"
- "commitStashOnlyWithDescriptor:withError:"
- "commitStashOnlyWithProduct:withError:"
- "commitStashWithProduct:withError:"
- "credentialsHarvested"
- "currentSystem"
- "currentlyFetchingMajorOSUpdateForURLScheme"
- "daysToSeconds:"
- "defaultAdminDeferralPeriodOfType:"
- "disableSoftwareUpdateNotifications"
- "doMDMMajorOSUpdateWithBundleId:withVersion:"
- "doMDMMajorOSUpdateWithBundleId:withVersion:withError:"
- "enableGlobalNotifications"
- "enableRapidSecurityResponse"
- "enableRapidSecurityResponseRollback"
- "fetchMajorUpdates"
- "fetchMinorUpdates"
- "formatter"
- "getCurrentLoginCredentialPolicy"
- "getMajorOSUpdateStatus:"
- "getMajorUpdates"
- "getMinorUpdates"
- "getUpdateStatus:"
- "globalSettings"
- "hasIgnoredUpdatesObserverToken"
- "initWithArray:"
- "initWithProduct:reason:sharedPrefs:"
- "initWithSharedPrefs:intervalForRequiringCredentials:"
- "initWithStatePersistencePath:"
- "intervalForRequiringCredentials"
- "isOwner"
- "isSplatAssetType"
- "lastPostedMajorOSUpdatesAvailableNotificationDate"
- "localUserWithName:error:"
- "majorOSUpdateStatus"
- "majorOSVariant"
- "managedGlobalSettings"
- "postMDMRequestedNotificationToAllLoggedInUsers"
- "postMajorOSUpdateMDMRequestedNotification"
- "postMajorOSUpdateMDMRequestedNotificationWithCompletionHandler:"
- "postRestartRequiredNotificationWithOptions:completion:"
- "queueDescriptorForInstallTonight:withReason:"
- "recommendedUpdatesDidChange"
- "removeAllInvalidDeclarations"
- "removeAllMobileSoftwareUpdatesFromInstallLater"
- "removeMobileSoftwareUpdatesToInstallLater"
- "setAvailableUpdatesObserverToken:"
- "setClientExternalizedLocalAuthenticationContext:withCompletion:"
- "setClientExternalizedLocalAuthenticationContextAsync:withCompletion:"
- "setCurrentlyFetchingMajorOSUpdateForURLScheme:"
- "setFetchMajorUpdates:"
- "setFetchMinorUpdates:"
- "setHasIgnoredUpdatesObserverToken:"
- "setIntervalForRequiringCredentials:"
- "setLastPostedMajorOSUpdatesAvailableNotificationDateToNow"
- "setLastPostedMajorOSUpdatesAvailableNotificationToDate:"
- "setLock:"
- "setMajorOSUpdateStatus:"
- "setManagedGlobalSettings:"
- "setMobileSoftwareUpdateDescriptorToInstallLater:withReason:"
- "startup"
- "systemUpdatesDeferralPeriod"
- "updatePolicyForDownloadedAndPreparedProduct:"
- "updatePolicyForInstallTonightWithProduct:"
- "userIsOwner"
- "usernameForCurrentAuditTokenWithOutUID:"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v32@0:8@\"SUMacControllerDescriptor\"16Q24"
- "v36@0:8B16B20B24@?28"
- "v40@0:8Q16Q24Q32"
- "v48@0:8B16B20B24B28@32@?40"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
