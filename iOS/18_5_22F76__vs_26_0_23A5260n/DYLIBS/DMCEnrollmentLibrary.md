## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-20.5.1.2.0
-  __TEXT.__text: 0x1ea44
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0x1160
-  __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x25b5
-  __TEXT.__cstring: 0x1ad4
-  __TEXT.__gcc_except_tab: 0x820
+43.0.0.0.0
+  __TEXT.__text: 0x28b7c
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x19ec
+  __TEXT.__const: 0xf0
+  __TEXT.__oslogstring: 0x3b58
+  __TEXT.__cstring: 0x21a2
+  __TEXT.__gcc_except_tab: 0x8c0
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x6c8
-  __TEXT.__objc_classname: 0xf5
-  __TEXT.__objc_methname: 0x623c
-  __TEXT.__objc_methtype: 0x5e5
-  __TEXT.__objc_stubs: 0x4b20
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0xd58
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__objc_classname: 0x210
+  __TEXT.__objc_methname: 0x8228
+  __TEXT.__objc_methtype: 0x936
+  __TEXT.__objc_stubs: 0x6040
+  __DATA_CONST.__got: 0x440
+  __DATA_CONST.__const: 0x1188
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f0
-  __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x2f0
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x10a0
-  __AUTH_CONST.__objc_const: 0x1040
-  __AUTH_CONST.__objc_intobj: 0x6a8
-  __AUTH_CONST.__objc_arrayobj: 0x2e8
+  __DATA_CONST.__objc_selrefs: 0x1a48
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_arraydata: 0x3e0
+  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x1600
+  __AUTH_CONST.__objc_const: 0x1d20
+  __AUTH_CONST.__objc_intobj: 0x960
+  __AUTH_CONST.__objc_arrayobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0xf4
-  __DATA.__bss: 0x1c8
-  __DATA_DIRTY.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x168
+  __DATA.__data: 0x1f0
+  __DATA.__bss: 0x1f8
+  __DATA_DIRTY.__objc_data: 0x370
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
+  - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C56AB9D3-1423-3DB0-AF5B-FC229585FA40
-  Functions: 540
-  Symbols:   2169
-  CStrings:  1356
+  UUID: D71B6E51-6ECC-3FD8-B060-CC5DC698795A
+  Functions: 756
+  Symbols:   2929
+  CStrings:  1852
 
Symbols:
+ +[DMCEnrollmentFlowController(Utilities) _createFailedToCaptureSnapshotError]
+ +[DMCEnrollmentFlowController(Utilities) _createFailedToDeleteSnapshotError]
+ +[DMCMigrationFlowController isMigrationNeeded]
+ +[DMCMigrationFlowController shouldShowMigrationUI]
+ +[DMCMigrationHelper _createStartMigrationRequestFailedErrorWithDEPResponse:]
+ +[DMCMigrationHelper _migrationConfigFilePath]
+ +[DMCMigrationHelper hasIncompleteMigration]
+ +[DMCMigrationHelper isMigrationMandatoryWithPendingCloudConfig:]
+ +[DMCMigrationHelper isMigrationNeededWithExistingCloudConfig:newCloudConfig:]
+ +[DMCMigrationHelper isMigrationSupportedWithExistingCloudConfig:]
+ +[DMCMigrationHelper launchMigrationApplicationWithError:]
+ +[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:]
+ +[DMCMigrationHelper makeStartMigrationRequestWithCloudConfig:completionHandler:]
+ +[DMCMigrationHelper readPendingCloudConfigDetails]
+ +[DMCMigrationHelper setMigrationIncomplete:]
+ +[DMCMigrationHelper setUserInititiatedMigration:]
+ +[DMCMigrationHelper userInititiatedMigration]
+ +[DMCReturnToServiceHelper _userDefaultsToPreserve]
+ +[DMCReturnToServiceHelper preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:]
+ -[DMCEnrollmentFlowController _analyzeCloudConfig:enrollmentType:isDoingReturnToService:obliterationShelter:]
+ -[DMCEnrollmentFlowController _analyzeProfileData:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isRapidReturnToService:]
+ -[DMCEnrollmentFlowController _awaitApplicationInstallation]
+ -[DMCEnrollmentFlowController _awaitDDMAppConfigurationWithProfileIdentifier:]
+ -[DMCEnrollmentFlowController _blockMDMCommands]
+ -[DMCEnrollmentFlowController _cleanupOrphanedAppsIfNeededIsDoingRRTS:]
+ -[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]
+ -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentMethod:isReturnToService:]
+ -[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]
+ -[DMCEnrollmentFlowController _takeSnapshot]
+ -[DMCEnrollmentFlowController _trackDirtyAppBundleIDs:personaID:]
+ -[DMCEnrollmentFlowController _unblockMDMCommandsIfNeededHasBlocked:]
+ -[DMCEnrollmentFlowController cloudConfigIndicatesRapidReturnToService]
+ -[DMCEnrollmentFlowController hasBlockedMDMCommands]
+ -[DMCEnrollmentFlowController hasEnabledPushWake]
+ -[DMCEnrollmentFlowController isDoingReturnToService]
+ -[DMCEnrollmentFlowController migrationDelegate]
+ -[DMCEnrollmentFlowController setCloudConfigIndicatesRapidReturnToService:]
+ -[DMCEnrollmentFlowController setHasBlockedMDMCommands:]
+ -[DMCEnrollmentFlowController setHasEnabledPushWake:]
+ -[DMCEnrollmentFlowController setIsDoingReturnToService:]
+ -[DMCEnrollmentFlowController setMigrationDelegate:]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_RRTS_snapshotSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_bootstrapTokenSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_cleanupOrphanedAppsSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADE_migration_cleanupSteps]
+ -[DMCEnrollmentFlowController(Utilities) _disablePushWake]
+ -[DMCEnrollmentFlowController(Utilities) _enablePushWake]
+ -[DMCEnrollmentFlowController(Utilities) _machineInfoWithEnrollmentType:enrollmentMethod:isDoingReturnToService:isRapidReturnToService:]
+ -[DMCEnrollmentFlowController(Utilities) _unblockMDMCommands]
+ -[DMCEnrollmentFlowController(Utilities) _verifyPropertiesFromProfileData:enrollmentMethod:isRapidReturnToService:isESSO:essoAppITunesStoreID:enrollmentMode:managedAppleID:assignedManagedAppleID:serverCapabilities:error:]
+ -[DMCEnrollmentFlowController(Utilities) appInstallationStatusUpdatedForType:totalNumber:finishedNumber:]
+ -[DMCMigrationFlowController .cxx_destruct]
+ -[DMCMigrationFlowController _cleanupDirtyState]
+ -[DMCMigrationFlowController _convertErrorToHumanReadableError:]
+ -[DMCMigrationFlowController _createEnrollmentTypeNotSupportedError]
+ -[DMCMigrationFlowController _createUnenrollmentFailedError]
+ -[DMCMigrationFlowController _finalizeMigration]
+ -[DMCMigrationFlowController _flowTerminatedWithError:canceled:]
+ -[DMCMigrationFlowController _formalizePendingCloudConfig:]
+ -[DMCMigrationFlowController _performEnrollmentFlow]
+ -[DMCMigrationFlowController _performUnenrollmentFlow]
+ -[DMCMigrationFlowController _preflightMigration]
+ -[DMCMigrationFlowController _preserveManagedAppsIfNeededWithPendingCloudConfig:]
+ -[DMCMigrationFlowController _promptForMigrationConsentWithEnrollmentType:pendingCloudConfig:]
+ -[DMCMigrationFlowController _removeExistingCloudConfigProfile]
+ -[DMCMigrationFlowController _removePendingCloudConfigIfNeededWithEnrollmentCloudConfig:]
+ -[DMCMigrationFlowController _resetToInitialSteps]
+ -[DMCMigrationFlowController _sendEndMigrationRequestWithCloudConfig:]
+ -[DMCMigrationFlowController _sendStartMigrationRequestWithPendingCloudConfig:]
+ -[DMCMigrationFlowController _trustedErrors]
+ -[DMCMigrationFlowController _trustedErrors].cold.1
+ -[DMCMigrationFlowController _workerQueue_cleanupCachedValues]
+ -[DMCMigrationFlowController _workerQueue_flowCompleted]
+ -[DMCMigrationFlowController _workerQueue_performFlowStep:]
+ -[DMCMigrationFlowController canUsePendingCloudConfig]
+ -[DMCMigrationFlowController delegate]
+ -[DMCMigrationFlowController enrollmentCloudConfig]
+ -[DMCMigrationFlowController enrollmentFlowController:appInstallationStatusUpdatedForType:totalNumber:finishedNumber:]
+ -[DMCMigrationFlowController enrollmentFlowController:didReceiveCloudConfiguration:]
+ -[DMCMigrationFlowController enrollmentFlowController:performingEnrollmentStepWithName:status:]
+ -[DMCMigrationFlowController enrollmentFlowControllerIsDoingMigration:]
+ -[DMCMigrationFlowController enrollmentFlowController]
+ -[DMCMigrationFlowController initWithPresenter:managedConfigurationHelper:]
+ -[DMCMigrationFlowController managedConfigurationHelper]
+ -[DMCMigrationFlowController migrationCompletionHandler]
+ -[DMCMigrationFlowController originEnrollmentType]
+ -[DMCMigrationFlowController pendingCloudConfig]
+ -[DMCMigrationFlowController presenter]
+ -[DMCMigrationFlowController setCanUsePendingCloudConfig:]
+ -[DMCMigrationFlowController setDelegate:]
+ -[DMCMigrationFlowController setEnrollmentCloudConfig:]
+ -[DMCMigrationFlowController setEnrollmentFlowController:]
+ -[DMCMigrationFlowController setManagedConfigurationHelper:]
+ -[DMCMigrationFlowController setMigrationCompletionHandler:]
+ -[DMCMigrationFlowController setOriginEnrollmentType:]
+ -[DMCMigrationFlowController setPendingCloudConfig:]
+ -[DMCMigrationFlowController setPresenter:]
+ -[DMCMigrationFlowController setUnenrollmentFlowController:]
+ -[DMCMigrationFlowController startMDMMigrationWithCompletionHandler:]
+ -[DMCMigrationFlowController unenrollmentFlowController:willUninstallProfile:]
+ -[DMCMigrationFlowController unenrollmentFlowController]
+ -[DMCMigrationFlowController(Sequence) _migration_commonSteps]
+ -[DMCMigrationFlowController(Sequence) _migration_enrollmentSteps]
+ -[DMCMigrationFlowController(Sequence) _migration_unenrollmentSteps]
+ -[DMCMigrationFlowController(Sequence) _nameForStep:]
+ -[DMCRapidReturnToServiceFlowController .cxx_destruct]
+ -[DMCRapidReturnToServiceFlowController bootstrapToken]
+ -[DMCRapidReturnToServiceFlowController delegate]
+ -[DMCRapidReturnToServiceFlowController errorWithCode:message:]
+ -[DMCRapidReturnToServiceFlowController init]
+ -[DMCRapidReturnToServiceFlowController mdmProfileData]
+ -[DMCRapidReturnToServiceFlowController requestCheckInWithRetryCount:completion:]
+ -[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]
+ -[DMCRapidReturnToServiceFlowController setBootstrapToken:]
+ -[DMCRapidReturnToServiceFlowController setDelegate:]
+ -[DMCRapidReturnToServiceFlowController setMdmProfileData:]
+ -[DMCRapidReturnToServiceFlowController setStateMachine:]
+ -[DMCRapidReturnToServiceFlowController setTimeoutTimer:]
+ -[DMCRapidReturnToServiceFlowController setWifiProfileData:]
+ -[DMCRapidReturnToServiceFlowController setWorkerQueue:]
+ -[DMCRapidReturnToServiceFlowController startObliterationWithCompletion:]
+ -[DMCRapidReturnToServiceFlowController stateMachine]
+ -[DMCRapidReturnToServiceFlowController timeoutTimer]
+ -[DMCRapidReturnToServiceFlowController wifiProfileData]
+ -[DMCRapidReturnToServiceFlowController wifi]
+ -[DMCRapidReturnToServiceFlowController workerQueue]
+ -[DMCReturnToServiceHelper .cxx_destruct]
+ -[DMCReturnToServiceHelper languageStrings]
+ -[DMCReturnToServiceHelper localeString]
+ -[DMCReturnToServiceHelper obliterationShelter]
+ -[DMCReturnToServiceHelper returnToServiceFlowCompleted]
+ -[DMCReturnToServiceHelper setObliterationShelter:]
+ -[DMCReturnToServiceHelper shouldDoRapidReturnToService]
+ -[DMCReturnToServiceHelper shouldDoReturnToService]
+ -[DMCUnenrollmentFlowController _preflightUnenrollmentWithUnenrollmentType:accoutAltDSID:]
+ -[DMCUnenrollmentFlowController _uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:unenrollmentType:]
+ -[DMCUnenrollmentFlowController migrationDelegate]
+ -[DMCUnenrollmentFlowController setMigrationDelegate:]
+ -[DMCUnenrollmentFlowController setUnenrollmentType:]
+ -[DMCUnenrollmentFlowController unenrollADEWithCompletionHandler:]
+ -[DMCUnenrollmentFlowController unenrollmentType]
+ -[DMCUnenrollmentFlowController(Sequence) _interactiveUnenrollmentSteps]
+ -[DMCUnenrollmentFlowController(Sequence) _nameForStep:]
+ -[DMCUnenrollmentFlowController(Sequence) _silentUnenrollmentSteps]
+ -[DMCWiFiAutoJoinStateMachine .cxx_destruct]
+ -[DMCWiFiAutoJoinStateMachine _invalidStateTransitionError]
+ -[DMCWiFiAutoJoinStateMachine controller]
+ -[DMCWiFiAutoJoinStateMachine currentState]
+ -[DMCWiFiAutoJoinStateMachine init]
+ -[DMCWiFiAutoJoinStateMachine obliterationInfo]
+ -[DMCWiFiAutoJoinStateMachine processWiFiAutoJoinStateRequest:reason:completion:]
+ -[DMCWiFiAutoJoinStateMachine progressToDisableWiFiWithReason:]
+ -[DMCWiFiAutoJoinStateMachine progressToHaveNetworkWithCompletion:]
+ -[DMCWiFiAutoJoinStateMachine progressToPowerOnWithCompletion:]
+ -[DMCWiFiAutoJoinStateMachine progressToState:reason:completion:]
+ -[DMCWiFiAutoJoinStateMachine resetToState:]
+ -[DMCWiFiAutoJoinStateMachine setController:]
+ -[DMCWiFiAutoJoinStateMachine setObliterationInfo:]
+ -[DMCWiFiAutoJoinStateMachine wifi]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table108
+ GCC_except_table114
+ GCC_except_table12
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table135
+ GCC_except_table172
+ GCC_except_table175
+ GCC_except_table178
+ GCC_except_table18
+ GCC_except_table182
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table192
+ GCC_except_table198
+ GCC_except_table7
+ GCC_except_table77
+ GCC_except_table89
+ GCC_except_table9
+ GCC_except_table92
+ GCC_except_table95
+ _DMCEnrollmentFlowAppTypeMDMManaged
+ _DMCEnrollmentFlowAppTypeSystemDeletable
+ _DMCErrorTypeRetryable
+ _DMCMigrationErrorDomain
+ _DMCReturnToServiceErrorDomain
+ _DMCWiFiAutoJoinFailedReasonNone
+ _DMCWiFiAutoJoinFailedReasonUnableToJoinNetwork
+ _DMCWiFiAutoJoinFailedReasonUnableToTurnOnPower
+ _MDMCloudConfigurationPendingMigrationDetailsFilePath
+ _MDMMigrationConfigFilePath
+ _OBJC_CLASS_$_DEPClient
+ _OBJC_CLASS_$_DMCAppIdentifier
+ _OBJC_CLASS_$_DMCMigrationFlowController
+ _OBJC_CLASS_$_DMCMigrationHelper
+ _OBJC_CLASS_$_DMCMultiUserModeUtilities
+ _OBJC_CLASS_$_DMCPropertyListStorage
+ _OBJC_CLASS_$_DMCRapidReturnToServiceFlowController
+ _OBJC_CLASS_$_DMCSnapshotUtilities
+ _OBJC_CLASS_$_DMCWiFiAutoJoinStateMachine
+ _OBJC_CLASS_$_DMCWiFiUtilities
+ _OBJC_CLASS_$_FBSShutdownOptions
+ _OBJC_CLASS_$_FBSSystemService
+ _OBJC_CLASS_$_MDMClient
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._cloudConfigIndicatesRapidReturnToService
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._hasBlockedMDMCommands
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._hasEnabledPushWake
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._isDoingReturnToService
+ _OBJC_IVAR_$_DMCEnrollmentFlowController._migrationDelegate
+ _OBJC_IVAR_$_DMCMigrationFlowController._canUsePendingCloudConfig
+ _OBJC_IVAR_$_DMCMigrationFlowController._delegate
+ _OBJC_IVAR_$_DMCMigrationFlowController._enrollmentCloudConfig
+ _OBJC_IVAR_$_DMCMigrationFlowController._enrollmentFlowController
+ _OBJC_IVAR_$_DMCMigrationFlowController._managedConfigurationHelper
+ _OBJC_IVAR_$_DMCMigrationFlowController._migrationCompletionHandler
+ _OBJC_IVAR_$_DMCMigrationFlowController._originEnrollmentType
+ _OBJC_IVAR_$_DMCMigrationFlowController._pendingCloudConfig
+ _OBJC_IVAR_$_DMCMigrationFlowController._presenter
+ _OBJC_IVAR_$_DMCMigrationFlowController._unenrollmentFlowController
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._bootstrapToken
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._delegate
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._mdmProfileData
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._stateMachine
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._timeoutTimer
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._wifi
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._wifiProfileData
+ _OBJC_IVAR_$_DMCRapidReturnToServiceFlowController._workerQueue
+ _OBJC_IVAR_$_DMCReturnToServiceHelper._obliterationShelter
+ _OBJC_IVAR_$_DMCUnenrollmentFlowController._migrationDelegate
+ _OBJC_IVAR_$_DMCUnenrollmentFlowController._unenrollmentType
+ _OBJC_IVAR_$_DMCWiFiAutoJoinStateMachine._controller
+ _OBJC_IVAR_$_DMCWiFiAutoJoinStateMachine._currentState
+ _OBJC_IVAR_$_DMCWiFiAutoJoinStateMachine._obliterationInfo
+ _OBJC_IVAR_$_DMCWiFiAutoJoinStateMachine._wifi
+ _OBJC_METACLASS_$_DMCMigrationFlowController
+ _OBJC_METACLASS_$_DMCMigrationHelper
+ _OBJC_METACLASS_$_DMCRapidReturnToServiceFlowController
+ _OBJC_METACLASS_$_DMCWiFiAutoJoinStateMachine
+ __ADE_RRTS_snapshotSteps.onceToken
+ __ADE_RRTS_snapshotSteps.ret
+ __ADE_migration_cleanupSteps.onceToken
+ __ADE_migration_cleanupSteps.ret
+ __OBJC_$_CLASS_METHODS_DMCMigrationFlowController
+ __OBJC_$_CLASS_METHODS_DMCMigrationHelper
+ __OBJC_$_INSTANCE_METHODS_DMCMigrationFlowController(Sequence)
+ __OBJC_$_INSTANCE_METHODS_DMCRapidReturnToServiceFlowController
+ __OBJC_$_INSTANCE_METHODS_DMCReturnToServiceHelper
+ __OBJC_$_INSTANCE_METHODS_DMCUnenrollmentFlowController(Sequence)
+ __OBJC_$_INSTANCE_METHODS_DMCWiFiAutoJoinStateMachine
+ __OBJC_$_INSTANCE_VARIABLES_DMCMigrationFlowController
+ __OBJC_$_INSTANCE_VARIABLES_DMCRapidReturnToServiceFlowController
+ __OBJC_$_INSTANCE_VARIABLES_DMCReturnToServiceHelper
+ __OBJC_$_INSTANCE_VARIABLES_DMCWiFiAutoJoinStateMachine
+ __OBJC_$_PROP_LIST_DMCMigrationFlowController
+ __OBJC_$_PROP_LIST_DMCRapidReturnToServiceFlowController
+ __OBJC_$_PROP_LIST_DMCReturnToServiceHelper
+ __OBJC_$_PROP_LIST_DMCWiFiAutoJoinStateMachine
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCEnrollmentFlowAppInstallationObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCEnrollmentFlowMigrationDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCEnrollmentFlowMigrationDelegateBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCUnenrollmentFlowMigrationDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentFlowAppInstallationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentFlowMigrationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCEnrollmentFlowMigrationDelegateBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCUnenrollmentFlowMigrationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_DMCEnrollmentFlowAppInstallationObserver
+ __OBJC_$_PROTOCOL_REFS_DMCEnrollmentFlowMigrationDelegate
+ __OBJC_$_PROTOCOL_REFS_DMCEnrollmentFlowMigrationDelegateBase
+ __OBJC_$_PROTOCOL_REFS_DMCUnenrollmentFlowMigrationDelegate
+ __OBJC_CLASS_PROTOCOLS_$_DMCEnrollmentFlowController(Sequence|Utilities)
+ __OBJC_CLASS_PROTOCOLS_$_DMCMigrationFlowController
+ __OBJC_CLASS_RO_$_DMCMigrationFlowController
+ __OBJC_CLASS_RO_$_DMCMigrationHelper
+ __OBJC_CLASS_RO_$_DMCRapidReturnToServiceFlowController
+ __OBJC_CLASS_RO_$_DMCWiFiAutoJoinStateMachine
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentFlowAppInstallationObserver
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentFlowMigrationDelegate
+ __OBJC_LABEL_PROTOCOL_$_DMCEnrollmentFlowMigrationDelegateBase
+ __OBJC_LABEL_PROTOCOL_$_DMCUnenrollmentFlowMigrationDelegate
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_DMCMigrationFlowController
+ __OBJC_METACLASS_RO_$_DMCMigrationHelper
+ __OBJC_METACLASS_RO_$_DMCRapidReturnToServiceFlowController
+ __OBJC_METACLASS_RO_$_DMCWiFiAutoJoinStateMachine
+ __OBJC_PROTOCOL_$_DMCEnrollmentFlowAppInstallationObserver
+ __OBJC_PROTOCOL_$_DMCEnrollmentFlowMigrationDelegate
+ __OBJC_PROTOCOL_$_DMCEnrollmentFlowMigrationDelegateBase
+ __OBJC_PROTOCOL_$_DMCUnenrollmentFlowMigrationDelegate
+ __OBJC_PROTOCOL_$_NSObject
+ ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.77
+ ___122-[DMCUnenrollmentFlowController _uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:unenrollmentType:]_block_invoke
+ ___122-[DMCUnenrollmentFlowController _uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:unenrollmentType:]_block_invoke_2
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.86
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.94
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.88
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.95
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.112
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.113
+ ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.114
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.115
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.117
+ ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.116
+ ___149-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentMethod:isReturnToService:]_block_invoke
+ ___149-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentMethod:isReturnToService:]_block_invoke_2
+ ___44-[DMCEnrollmentFlowController _takeSnapshot]_block_invoke
+ ___44-[DMCMigrationFlowController _trustedErrors]_block_invoke
+ ___48-[DMCEnrollmentFlowController _blockMDMCommands]_block_invoke
+ ___48-[DMCEnrollmentFlowController _blockMDMCommands]_block_invoke_2
+ ___48-[DMCMigrationFlowController _finalizeMigration]_block_invoke
+ ___48-[DMCMigrationFlowController _finalizeMigration]_block_invoke_2
+ ___49-[DMCEnrollmentFlowController _storeCloudConfig:]_block_invoke_2
+ ___52-[DMCMigrationFlowController _performEnrollmentFlow]_block_invoke
+ ___52-[DMCMigrationFlowController _performEnrollmentFlow]_block_invoke_2
+ ___54-[DMCMigrationFlowController _performUnenrollmentFlow]_block_invoke
+ ___54-[DMCMigrationFlowController _performUnenrollmentFlow]_block_invoke_2
+ ___59-[DMCMigrationFlowController _formalizePendingCloudConfig:]_block_invoke
+ ___59-[DMCMigrationFlowController _formalizePendingCloudConfig:]_block_invoke_2
+ ___60-[DMCEnrollmentFlowController _awaitApplicationInstallation]_block_invoke
+ ___60-[DMCEnrollmentFlowController _awaitApplicationInstallation]_block_invoke_2
+ ___61-[DMCEnrollmentFlowController(Utilities) _unblockMDMCommands]_block_invoke
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke.33
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke_2
+ ___63-[DMCMigrationFlowController _removeExistingCloudConfigProfile]_block_invoke_2.34
+ ___64-[DMCEnrollmentFlowController(Sequence) _ADE_RRTS_snapshotSteps]_block_invoke
+ ___64-[DMCMigrationFlowController _flowTerminatedWithError:canceled:]_block_invoke
+ ___67-[DMCWiFiAutoJoinStateMachine progressToHaveNetworkWithCompletion:]_block_invoke
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.149
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.150
+ ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.151
+ ___68-[DMCEnrollmentFlowController(Sequence) _ADE_migration_cleanupSteps]_block_invoke
+ ___70-[DMCMigrationFlowController _sendEndMigrationRequestWithCloudConfig:]_block_invoke
+ ___70-[DMCMigrationFlowController _sendEndMigrationRequestWithCloudConfig:]_block_invoke_2
+ ___71-[DMCEnrollmentFlowController _cleanupOrphanedAppsIfNeededIsDoingRRTS:]_block_invoke
+ ___71-[DMCEnrollmentFlowController _cleanupOrphanedAppsIfNeededIsDoingRRTS:]_block_invoke_2
+ ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke
+ ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke.171
+ ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke.173
+ ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke_2
+ ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke_2.172
+ ___72-[DMCEnrollmentFlowController _createAndSyncBootstrapTokenWithPasscode:]_block_invoke_2.174
+ ___73-[DMCRapidReturnToServiceFlowController startObliterationWithCompletion:]_block_invoke
+ ___73-[DMCRapidReturnToServiceFlowController startObliterationWithCompletion:]_block_invoke_2
+ ___78-[DMCEnrollmentFlowController _awaitDDMAppConfigurationWithProfileIdentifier:]_block_invoke
+ ___78-[DMCEnrollmentFlowController _awaitDDMAppConfigurationWithProfileIdentifier:]_block_invoke_2
+ ___79-[DMCMigrationFlowController _sendStartMigrationRequestWithPendingCloudConfig:]_block_invoke
+ ___79-[DMCMigrationFlowController _sendStartMigrationRequestWithPendingCloudConfig:]_block_invoke.25
+ ___79-[DMCMigrationFlowController _sendStartMigrationRequestWithPendingCloudConfig:]_block_invoke_2
+ ___81+[DMCMigrationHelper makeStartMigrationRequestWithCloudConfig:completionHandler:]_block_invoke
+ ___81-[DMCMigrationFlowController _preserveManagedAppsIfNeededWithPendingCloudConfig:]_block_invoke
+ ___81-[DMCMigrationFlowController _preserveManagedAppsIfNeededWithPendingCloudConfig:]_block_invoke_2
+ ___81-[DMCRapidReturnToServiceFlowController requestCheckInWithRetryCount:completion:]_block_invoke
+ ___81-[DMCRapidReturnToServiceFlowController requestCheckInWithRetryCount:completion:]_block_invoke_2
+ ___81-[DMCRapidReturnToServiceFlowController requestCheckInWithRetryCount:completion:]_block_invoke_3
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.2
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.4
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke.8
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.3
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.6
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_2.9
+ ___83-[DMCRapidReturnToServiceFlowController requestRapidReturnToServiceWithCompletion:]_block_invoke_3
+ ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.135
+ ___87+[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:]_block_invoke
+ ___87+[DMCMigrationHelper makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:]_block_invoke.16
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.124
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.127
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.125
+ ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.128
+ ___89-[DMCMigrationFlowController _removePendingCloudConfigIfNeededWithEnrollmentCloudConfig:]_block_invoke
+ ___89-[DMCMigrationFlowController _removePendingCloudConfigIfNeededWithEnrollmentCloudConfig:]_block_invoke_2
+ ___94-[DMCMigrationFlowController _promptForMigrationConsentWithEnrollmentType:pendingCloudConfig:]_block_invoke
+ ___94-[DMCMigrationFlowController _promptForMigrationConsentWithEnrollmentType:pendingCloudConfig:]_block_invoke_2
+ ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke
+ ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke.163
+ ___96-[DMCEnrollmentFlowController _processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e37_v28?0B8"NSDictionary"12"NSError"20ls32l8
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e23_v24?0B8B12"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e33_v28?0"NSString"8B16"NSError"20lw40l8s32l8
+ ___block_descriptor_48_e8_32bs_e37_v28?0B8"NSDictionary"12"NSError"20ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSTimer"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e32_v28?0B8"NSArray"12"NSError"20lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e50_v40?0"NSData"8"NSData"16"NSData"24"NSError"32ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_literal_global.151
+ ___block_literal_global.180
+ ___block_literal_global.199
+ ___block_literal_global.89
+ __dispatch_main_q
+ _dispatch_async
+ _kCCIsRapidReturnToServiceKey
+ _kCCMDMServerUIDKey
+ _kCCPostSetupProfileWasInstalledKey
+ _kDEPResponseErrorReasonKey
+ _kDEPResponseStatusKey
+ _kDEPResponseSuccess
+ _kDMCProfileInstallationSourceMDMMigration
+ _kDMCRapidReturntoServiceSnapshotName
+ _kMDMBootstrapTokenCapability
+ _kMDMMigrationHasIncompleteMigrationKey
+ _kMDMMigrationUserInitiatedMigrationKey
+ _objc_msgSend$DMCErrorType
+ _objc_msgSend$_ADE_RRTS_snapshotSteps
+ _objc_msgSend$_ADE_bootstrapTokenSteps
+ _objc_msgSend$_ADE_cleanupOrphanedAppsSteps
+ _objc_msgSend$_ADE_migration_cleanupSteps
+ _objc_msgSend$_allOverrides
+ _objc_msgSend$_analyzeCloudConfig:enrollmentType:isDoingReturnToService:obliterationShelter:
+ _objc_msgSend$_analyzeProfileData:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isRapidReturnToService:
+ _objc_msgSend$_awaitApplicationInstallation
+ _objc_msgSend$_awaitDDMAppConfigurationWithProfileIdentifier:
+ _objc_msgSend$_blockMDMCommands
+ _objc_msgSend$_cleanupDirtyState
+ _objc_msgSend$_cleanupOrphanedAppsIfNeededIsDoingRRTS:
+ _objc_msgSend$_createAndSyncBootstrapTokenWithPasscode:
+ _objc_msgSend$_createEnrollmentTypeNotSupportedError
+ _objc_msgSend$_createFailedToCaptureSnapshotError
+ _objc_msgSend$_createFailedToDeleteSnapshotError
+ _objc_msgSend$_createStartMigrationRequestFailedErrorWithDEPResponse:
+ _objc_msgSend$_createUnenrollmentFailedError
+ _objc_msgSend$_disablePushWake
+ _objc_msgSend$_enablePushWake
+ _objc_msgSend$_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentMethod:isReturnToService:
+ _objc_msgSend$_finalizeMigration
+ _objc_msgSend$_formalizePendingCloudConfig:
+ _objc_msgSend$_invalidStateTransitionError
+ _objc_msgSend$_machineInfoWithEnrollmentType:enrollmentMethod:isDoingReturnToService:isRapidReturnToService:
+ _objc_msgSend$_migrationConfigFilePath
+ _objc_msgSend$_migration_commonSteps
+ _objc_msgSend$_migration_enrollmentSteps
+ _objc_msgSend$_migration_unenrollmentSteps
+ _objc_msgSend$_performEnrollmentFlow
+ _objc_msgSend$_performUnenrollmentFlow
+ _objc_msgSend$_preflightMigration
+ _objc_msgSend$_preflightUnenrollmentWithUnenrollmentType:accoutAltDSID:
+ _objc_msgSend$_preserveManagedAppsIfNeededWithPendingCloudConfig:
+ _objc_msgSend$_processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:
+ _objc_msgSend$_promptForMigrationConsentWithEnrollmentType:pendingCloudConfig:
+ _objc_msgSend$_removeExistingCloudConfigProfile
+ _objc_msgSend$_removePendingCloudConfigIfNeededWithEnrollmentCloudConfig:
+ _objc_msgSend$_sendEndMigrationRequestWithCloudConfig:
+ _objc_msgSend$_sendStartMigrationRequestWithPendingCloudConfig:
+ _objc_msgSend$_takeSnapshot
+ _objc_msgSend$_trackDirtyAppBundleIDs:personaID:
+ _objc_msgSend$_unblockMDMCommands
+ _objc_msgSend$_unblockMDMCommandsIfNeededHasBlocked:
+ _objc_msgSend$_uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:unenrollmentType:
+ _objc_msgSend$_userDefaultsToPreserve
+ _objc_msgSend$_verifyPropertiesFromProfileData:enrollmentMethod:isRapidReturnToService:isESSO:essoAppITunesStoreID:enrollmentMode:managedAppleID:assignedManagedAppleID:serverCapabilities:error:
+ _objc_msgSend$activationRecordIndicatesCloudConfigurationIsAvailable
+ _objc_msgSend$awaitPendingApplicationInstallationWithObserver:completionHandler:
+ _objc_msgSend$blockMDMCommandsWithCompletionHandler:
+ _objc_msgSend$bootstrapToken
+ _objc_msgSend$bundleID
+ _objc_msgSend$canUsePendingCloudConfig
+ _objc_msgSend$captureSystemVolumeSnapshotWithName:
+ _objc_msgSend$checkInRequestFailedWithError:
+ _objc_msgSend$cleanupOrphanedAppsWithCompletionHandler:
+ _objc_msgSend$cloudConfigIndicatesRapidReturnToService
+ _objc_msgSend$compare:
+ _objc_msgSend$createBootstrapTokenIfNeededWithPasscode:completionHandler:
+ _objc_msgSend$currentEnrollmentType
+ _objc_msgSend$currentPendingCloudConfigOnDisk
+ _objc_msgSend$currentState
+ _objc_msgSend$deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:
+ _objc_msgSend$deleteSystemVolumeSnapshotWithName:
+ _objc_msgSend$dismissMigrationScene
+ _objc_msgSend$dismissUnenrollmentSceneWithError:
+ _objc_msgSend$enableAutoJoinIfNeededWithTimeout:completionHandler:
+ _objc_msgSend$enrollmentCloudConfig
+ _objc_msgSend$enrollmentFlowController:appInstallationStatusUpdatedForType:totalNumber:finishedNumber:
+ _objc_msgSend$enrollmentFlowController:performingEnrollmentStepWithName:status:
+ _objc_msgSend$enrollmentFlowControllerIsDoingMigration:
+ _objc_msgSend$enrollmentServerInfo
+ _objc_msgSend$errorWithCode:message:
+ _objc_msgSend$evaluateMigrationStatusWithPollFromServer:completionHandler:
+ _objc_msgSend$existingCloudConfigOnDisk
+ _objc_msgSend$getMachineInfoForEnrollmentType:enrollmentMethod:canRequestSoftwareUpdate:
+ _objc_msgSend$hasBlockedMDMCommands
+ _objc_msgSend$hasEnabledPushWake
+ _objc_msgSend$hasIncompleteMigration
+ _objc_msgSend$haveNetwork
+ _objc_msgSend$initWithBundleID:personaID:
+ _objc_msgSend$initWithCloudConfigDetails:
+ _objc_msgSend$initWithFilePath:
+ _objc_msgSend$initWithPresenter:managedConfigurationHelper:
+ _objc_msgSend$initWithReason:
+ _objc_msgSend$installedMDMProfileIdentifier
+ _objc_msgSend$invalidate
+ _objc_msgSend$isAwaitingConfiguration
+ _objc_msgSend$isDoingReturnToService
+ _objc_msgSend$isMigrationMandatoryWithPendingCloudConfig:
+ _objc_msgSend$isMigrationNeeded
+ _objc_msgSend$isMigrationNeededWithExistingCloudConfig:newCloudConfig:
+ _objc_msgSend$isMigrationSupportedWithExistingCloudConfig:
+ _objc_msgSend$isRapidReturnToService
+ _objc_msgSend$isSharediPad
+ _objc_msgSend$makeEndMDMMigrationRequestWithServerUID:status:completionBlock:
+ _objc_msgSend$makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:
+ _objc_msgSend$makeStartMDMMigrationRequestWithCompletionBlock:
+ _objc_msgSend$makeStartMigrationRequestWithCloudConfig:completionHandler:
+ _objc_msgSend$managingProfileIdentifier
+ _objc_msgSend$mdmServerUID
+ _objc_msgSend$migrationCompletionHandler
+ _objc_msgSend$migrationDeadline
+ _objc_msgSend$migrationDelegate
+ _objc_msgSend$migrationFlowController:appInstallationStatusUpdatedForType:totalNumber:finishedNumber:
+ _objc_msgSend$migrationFlowController:performingEnrollmentStepWithName:status:
+ _objc_msgSend$migrationFlowController:performingMigrationStepWithName:status:
+ _objc_msgSend$newAppIdentifierWithIdentifier:
+ _objc_msgSend$now
+ _objc_msgSend$objectForKey:inDomain:
+ _objc_msgSend$originEnrollmentType
+ _objc_msgSend$pendingCloudConfig
+ _objc_msgSend$powerOn
+ _objc_msgSend$prepareToObliterationWithCompletionHandler:
+ _objc_msgSend$presentUnenrollmentActivityPageIsAppleMAID:
+ _objc_msgSend$preserveManagedAppsWithCompletionHandler:
+ _objc_msgSend$preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:
+ _objc_msgSend$processWiFiAutoJoinStateRequest:reason:completion:
+ _objc_msgSend$progressToDisableWiFiWithReason:
+ _objc_msgSend$progressToHaveNetworkWithCompletion:
+ _objc_msgSend$progressToPowerOnWithCompletion:
+ _objc_msgSend$progressToState:reason:completion:
+ _objc_msgSend$readPendingCloudConfigDetails
+ _objc_msgSend$refreshDetailsFromDisk
+ _objc_msgSend$removeApplicationWithBundleID:personaID:completionHandler:
+ _objc_msgSend$removeCloudConfigWithCompletionHandler:
+ _objc_msgSend$removePendingCloudConfigWithCompletionHandler:
+ _objc_msgSend$removeProtectedProfileWithIdentifier:completionHandler:
+ _objc_msgSend$removeSetAsideCloudConfigWithCompletionHandler:
+ _objc_msgSend$requestCheckInWithRetryCount:completion:
+ _objc_msgSend$requestRRTSCheckInAndValidationWithCompletionHandler:
+ _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:
+ _objc_msgSend$requestUserConsentForMigrationWithPendingCloudConfig:originalEnrollmentType:isMandatory:deadline:completionHandler:
+ _objc_msgSend$retrieveDictionaryWithError:
+ _objc_msgSend$retrieveValueForKey:error:
+ _objc_msgSend$saveValue:forKey:error:
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$setAdditionalDetails:
+ _objc_msgSend$setBootstrapToken:
+ _objc_msgSend$setCanUsePendingCloudConfig:
+ _objc_msgSend$setCloudConfigIndicatesRapidReturnToService:
+ _objc_msgSend$setController:
+ _objc_msgSend$setEnrollmentCloudConfig:
+ _objc_msgSend$setEnrollmentFlowController:
+ _objc_msgSend$setHasBlockedMDMCommands:
+ _objc_msgSend$setHasEnabledPushWake:
+ _objc_msgSend$setIsDoingReturnToService:
+ _objc_msgSend$setIsRapidReturnToService:
+ _objc_msgSend$setIsSharediPad:
+ _objc_msgSend$setMigrationCompletionHandler:
+ _objc_msgSend$setMigrationDelegate:
+ _objc_msgSend$setMigrationIncomplete:
+ _objc_msgSend$setOriginEnrollmentType:
+ _objc_msgSend$setPendingCloudConfig:
+ _objc_msgSend$setPower:error:
+ _objc_msgSend$setRebootType:
+ _objc_msgSend$setTimeoutTimer:
+ _objc_msgSend$setUnenrollmentFlowController:
+ _objc_msgSend$setUnenrollmentType:
+ _objc_msgSend$setUserDefaults:
+ _objc_msgSend$setUserInititiatedMigration:
+ _objc_msgSend$sharedClient
+ _objc_msgSend$sharedService
+ _objc_msgSend$shouldDoReturnToService
+ _objc_msgSend$shouldPreserveUserDefaultsForReturnToService
+ _objc_msgSend$showMigrationCompletionScene
+ _objc_msgSend$showMigrationFailure:
+ _objc_msgSend$shutdownWithOptions:
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$startInBuddyEnrollmentFlowRestartIfFail:completionHandler:
+ _objc_msgSend$startObliterationWithCompletion:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$syncBootstrapToken:completionHandler:
+ _objc_msgSend$timeoutTimer
+ _objc_msgSend$unblockMDMCommandsWithCompletionHandler:
+ _objc_msgSend$unenrollADEWithCompletionHandler:
+ _objc_msgSend$unenrollmentFlowController:willUninstallProfile:
+ _objc_msgSend$unenrollmentType
+ _objc_msgSend$userInititiatedMigration
+ _objc_msgSend$userMode
+ _objc_msgSend$waitForDDMAppsToBeRegisteredForMDMProfile:completionHandler:
+ _objc_msgSend$wifiAutoJoinFailedWithReason:
+ _objc_retain_x10
- -[DMCEnrollmentFlowController _analyzeCloudConfig:enrollmentType:isReturnToService:obliterationShelter:]
- -[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]
- -[DMCEnrollmentFlowController _trackDirtyAppBundleIDs:]
- -[DMCEnrollmentFlowController isReturnToService]
- -[DMCEnrollmentFlowController setIsReturnToService:]
- -[DMCEnrollmentFlowController(Utilities) _extractAndVerifyPropertiesFromProfileData:enrollmentMethod:isESSO:essoAppITunesStoreID:error:]
- -[DMCUnenrollmentFlowController _interactiveUnenrollmentSteps]
- -[DMCUnenrollmentFlowController _nameForStep:]
- -[DMCUnenrollmentFlowController _preflightUnenrollmentWithAccoutAltDSID:]
- -[DMCUnenrollmentFlowController _silentUnenrollmentSteps]
- -[DMCUnenrollmentFlowController _uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:]
- GCC_except_table10
- GCC_except_table104
- GCC_except_table107
- GCC_except_table113
- GCC_except_table120
- GCC_except_table123
- GCC_except_table126
- GCC_except_table13
- GCC_except_table134
- GCC_except_table17
- GCC_except_table170
- GCC_except_table173
- GCC_except_table176
- GCC_except_table180
- GCC_except_table184
- GCC_except_table189
- GCC_except_table6
- GCC_except_table76
- GCC_except_table88
- GCC_except_table91
- GCC_except_table94
- GCC_except_table99
- _OBJC_IVAR_$_DMCEnrollmentFlowController._isReturnToService
- __OBJC_$_INSTANCE_METHODS_DMCUnenrollmentFlowController
- __OBJC_$_PROP_LIST_DMCEnrollmentFlowController
- ___115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.70
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.75
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.83
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.77
- ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.84
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.101
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.102
- ___127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke_2.103
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.104
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.106
- ___137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke_2.105
- ___192-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]_block_invoke
- ___192-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]_block_invoke_2
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.137
- ___68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.138
- ___85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.123
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.113
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke.115
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.114
- ___87-[DMCEnrollmentFlowController _installEnterpriseApplication:debuggingAppIDs:personaID:]_block_invoke_2.116
- ___block_descriptor_40_e8_32w_e33_v28?0"NSString"8B16"NSError"20lw32l8
- ___block_descriptor_56_e8_32s40bs48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
- ___block_descriptor_65_e8_32s40w_e28_v24?0"NSData"8"NSError"16lw40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s64l8s56l8
- ___block_literal_global.146
- ___block_literal_global.175
- ___block_literal_global.90
- _objc_msgSend$_analyzeCloudConfig:enrollmentType:isReturnToService:obliterationShelter:
- _objc_msgSend$_extractAndVerifyPropertiesFromProfileData:enrollmentMethod:isESSO:essoAppITunesStoreID:error:
- _objc_msgSend$_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:
- _objc_msgSend$_preflightUnenrollmentWithAccoutAltDSID:
- _objc_msgSend$_trackDirtyAppBundleIDs:
- _objc_msgSend$_uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:
- _objc_msgSend$dismissUnenrollmentScene
- _objc_msgSend$getMachineInfoForEnrollmentType:enrollmentMethod:
- _objc_msgSend$isReturnToService
- _objc_msgSend$memberQueueManagingProfileIdentifier
- _objc_msgSend$presentActivityPageForAppleMAID:
- _objc_msgSend$removeApplicationWithBundleID:completionHandler:
- _objc_msgSend$serverCapabilities
- _objc_msgSend$setIsReturnToService:
CStrings:
+ "\""
+ "#16@0:8"
+ "%@"
+ "%s %@"
+ "%s enrollmentType: %lu, deadline: %@, isMandatory: %d"
+ "%s is migration mandatory: %d. Deadline: %{public}@."
+ "%s preserving user defaults: %{public}@"
+ "+[DMCMigrationHelper hasIncompleteMigration]"
+ "+[DMCMigrationHelper isMigrationMandatoryWithPendingCloudConfig:]"
+ "+[DMCReturnToServiceHelper preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:]"
+ "-[DMCEnrollmentFlowController _analyzeProfileData:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isRapidReturnToService:]"
+ "-[DMCEnrollmentFlowController _ensureDeviceActivation]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentMethod:isReturnToService:]_block_invoke_2"
+ "-[DMCMigrationFlowController _promptForMigrationConsentWithEnrollmentType:pendingCloudConfig:]"
+ "-[DMCMigrationFlowController _workerQueue_performFlowStep:]"
+ "@\"<DMCEnrollmentFlowMigrationDelegate>\""
+ "@\"<DMCMigrationFlowDelegate>\""
+ "@\"<DMCMigrationFlowMCBridge>\""
+ "@\"<DMCMigrationFlowPresenter>\""
+ "@\"<DMCRRTSFlowDelegate>\""
+ "@\"<DMCUnenrollmentFlowMigrationDelegate>\""
+ "@\"DMCEnrollmentFlowController\""
+ "@\"DMCRapidReturnToServiceFlowController\""
+ "@\"DMCUnenrollmentFlowController\""
+ "@\"DMCWiFiAutoJoinStateMachine\""
+ "@\"DMCWiFiUtilities\""
+ "@\"NSString\"16@0:8"
+ "@\"NSTimer\""
+ "@24@0:8:16"
+ "@28@0:8i16@20"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8Q16Q24B32B36"
+ "@48@0:8@16@24@32^@40"
+ "Activation record indicates cloud configuration is available, will fetch..."
+ "AnalyzeEnrollmentProfile"
+ "Apple Global Domain"
+ "AwaitApplicationInstallation"
+ "AwaitDDMAppConfiguration"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"DMCEnrollmentFlowControllerBase\"16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8^@16"
+ "B88@0:8@16Q24B32B36@40@48@56@64@72^@80"
+ "BlockMDMCommands"
+ "Can not use the pending cloud config, continue..."
+ "Cleaning up dirty application with bundle ID: %{public}@, persona ID: %{public}@..."
+ "CleanupOrphanedAppsIfNeeded"
+ "Cloud Configuration is available locally, returning..."
+ "Couldn't find profile identifier. Continuing..."
+ "CreateAndSyncBootstrapToken"
+ "DMCEnrollmentFlowAppInstallationObserver"
+ "DMCEnrollmentFlowContrller: App type: %@, %lu of %lu completed"
+ "DMCEnrollmentFlowMigrationDelegate"
+ "DMCEnrollmentFlowMigrationDelegateBase"
+ "DMCErrorType"
+ "DMCMigrationFlowController"
+ "DMCMigrationHelper"
+ "DMCMigrationHelper: Device is not supervised"
+ "DMCMigrationHelper: Migration of ABE devices is not supported"
+ "DMCMigrationHelper: Migration of RRTS devices is not supported"
+ "DMCMigrationHelper: Migration of Shared iPad devices is not supported"
+ "DMCMigrationHelper: Migration of non DEP enrolled devices is not supported"
+ "DMCMigrationHelper: Migration to ABE is not supported"
+ "DMCMigrationHelper: new cloud config does not exist."
+ "DMCMigrationHelper: new cloud config does not have a migration deadline."
+ "DMCMigrationHelper: server UID has changed from %{public}@ to %{public}@."
+ "DMCMigrationHelper: server UID hasn't changed: %{public}@."
+ "DMCRapidReturnToServiceFlowController"
+ "DMCUnenrollmentFlowMigrationDelegate"
+ "DMCWiFiAutoJoinStateMachine"
+ "DMC_MDM_MIGRATION_FAILED"
+ "Device is doing Rapid Return to Service"
+ "Device is not doing migration nor Rapid Return to Service, continue..."
+ "Doing RTS on non-ADE enrolled device, need to preserve the cloud config"
+ "Doing Rapid Return to Service but server does not support bootstrap token. Aborting..."
+ "Doing migration flow... Skip consent during unenrollment."
+ "ERROR_PROFILE_MISSING_BOOTSTRAP_TOKEN_CAPABILITY"
+ "End MDM migration request returned with response: %{public}@, error: %{public}@"
+ "End Migration request came back with response: %{public}@"
+ "Enrollment canceled"
+ "Enrollment failed with error: %{public}@"
+ "Enrollment succeeded"
+ "Enrollment type is None!"
+ "EnrollmentFlow"
+ "Error turnning WiFi power off: %{public}@"
+ "Evaluation returned with migration needed: %d, error: %{public}@"
+ "Failed to block MDM commands with error: %{public}@"
+ "Failed to capture snapshot"
+ "Failed to clean up orphaned apps with error: %{public}@"
+ "Failed to create bootstrap token with error: %{public}@"
+ "Failed to delete bootstrap token with error: %{public}@"
+ "Failed to delete snapshot"
+ "Failed to make end migration request with error: %{public}@"
+ "Failed to make start migration request with error: %{public}@"
+ "Failed to preserve managed apps with error: %{public}@"
+ "Failed to re-evaluate migration status with error: %{public}@"
+ "Failed to read pending cloud config details with error: %{public}@"
+ "Failed to remove pending cloud config with error: %{public}@!"
+ "Failed to retrieve HasIncompleteMigration info with error: %{public}@"
+ "Failed to retrieve UserInitiatedMigration info with error: %{public}@"
+ "Failed to save HasIncompleteMigration info with error: %{public}@"
+ "Failed to save UserInitiatedMigration info with error: %{public}@"
+ "Failed to save the pending cloud configuration as the formal cloud configuration with error:%{public}@"
+ "Failed to sync bootstrap token with error: %{public}@"
+ "Failed to unblock MDM commands with error: %{public}@"
+ "Failed to wait for DDM apps configuration with error: %{public}@"
+ "Failed to wait for app installation with error: %{public}@"
+ "FinializeMigration"
+ "FormalizePendingCloudConfig"
+ "Formalizing pending cloud config..."
+ "Has incomplete migration"
+ "HasIncompleteMigration"
+ "LockdownActivationIndicatesCloudConfigurationAvailable"
+ "MDM Migration restarting device"
+ "MDM managed"
+ "MDM payload removed..."
+ "MDM profile installed."
+ "MDM_ERROR_MIGRATION_NOT_SUPPORTED"
+ "MDM_MIGRATION_FAILED_TO_UNENROLL"
+ "Maximum retry count reached."
+ "Migration flow completed!"
+ "Migration flow terminated with error: %{public}@, canceled: %d"
+ "Migration is not supported with current enrollment type: %lu"
+ "NSObject"
+ "No bootstrap token was created. Continue..."
+ "No cloud config or the cloud config does not have the deadline key for MDM migration."
+ "No need to ask for consent again during migration"
+ "No pending cloud config on disk. Abort..."
+ "No profile identifier, continue..."
+ "No server UID from existing cloud config. Continue..."
+ "None"
+ "ORGO enrollment during MDM Migration is not supported"
+ "Pending cloud config does not require await configuration. Do not presrve apps."
+ "PreflightMigration"
+ "PreserveApps"
+ "ProcessPotentialMigration"
+ "PromptForMigrationConsent"
+ "Rapid Return to Service during MDM Migration is not supported"
+ "Rebooting the device"
+ "RemoveExistingCloudConfig"
+ "RemovePendingCloudConfig"
+ "Removing existing cloud config profile..."
+ "Removing set aside cloud config profile..."
+ "RequestEndMigration"
+ "RequestStartMigration"
+ "Retry sending checkin request..."
+ "Server UID has changed from %{public}@ to %{public}@."
+ "Server returned fail response for the StartMigration request, re-evaluating migration status"
+ "Snapshot created with name: %{public}@"
+ "Start MDM migration request failed with server error: %@"
+ "Start migration got back with failed response"
+ "Start migration got back with response: %{public}@"
+ "State machine reset requested"
+ "System deletable"
+ "T#,R"
+ "T@\"<DMCEnrollmentFlowMigrationDelegate>\",W,V_migrationDelegate"
+ "T@\"<DMCMigrationFlowDelegate>\",W,V_delegate"
+ "T@\"<DMCMigrationFlowMCBridge>\",&,N,V_managedConfigurationHelper"
+ "T@\"<DMCMigrationFlowPresenter>\",&,N,V_presenter"
+ "T@\"<DMCRRTSFlowDelegate>\",W,N,V_delegate"
+ "T@\"<DMCUnenrollmentFlowMigrationDelegate>\",W,V_migrationDelegate"
+ "T@\"DMCEnrollmentFlowController\",&,N,V_enrollmentFlowController"
+ "T@\"DMCRapidReturnToServiceFlowController\",W,N,V_controller"
+ "T@\"DMCUnenrollmentFlowController\",&,N,V_unenrollmentFlowController"
+ "T@\"DMCWiFiAutoJoinStateMachine\",&,N,V_stateMachine"
+ "T@\"DMCWiFiUtilities\",R,N,V_wifi"
+ "T@\"NSData\",&,N,V_bootstrapToken"
+ "T@\"NSData\",&,N,V_mdmProfileData"
+ "T@\"NSData\",&,N,V_wifiProfileData"
+ "T@\"NSDictionary\",&,N,V_enrollmentCloudConfig"
+ "T@\"NSDictionary\",&,N,V_pendingCloudConfig"
+ "T@\"NSMutableDictionary\",N,V_obliterationInfo"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"NSTimer\",&,N,V_timeoutTimer"
+ "T@?,C,N,V_migrationCompletionHandler"
+ "TB,N,V_canUsePendingCloudConfig"
+ "TB,N,V_cloudConfigIndicatesRapidReturnToService"
+ "TB,N,V_hasBlockedMDMCommands"
+ "TB,N,V_hasEnabledPushWake"
+ "TB,N,V_isDoingReturnToService"
+ "TQ,N,V_originEnrollmentType"
+ "TQ,N,V_unenrollmentType"
+ "TQ,R"
+ "TQ,R,N,V_currentState"
+ "TakeSnapshot"
+ "The Server UID in the existing cloud configuration matches the serverUID in the pending cloud configuration. Skipping unenrollment..."
+ "Unable to join network"
+ "Unable to turn on WiFi power"
+ "UnblockMDMCommands"
+ "Unblocked MDM commands"
+ "Unblocking MDM commands..."
+ "Unenrollment canceled"
+ "Unenrollment failed with error: %{public}@"
+ "Unenrollment succeeded"
+ "UnenrollmentFlow"
+ "User has initiated migration"
+ "UserInitiatedMigration"
+ "Vv16@0:8"
+ "WiFi Auto Join invalid state transition"
+ "WiFi profile is not available."
+ "WiFiAutoJoinState: [%ld]"
+ "Will perform migration step: %{public}@"
+ "[DMCRapidReturnToServiceFlowController] Failed to process WiFi Auto Join with error: %{public}@"
+ "[DMCRapidReturnToServiceFlowController] Failed to request RRTS checkin with error: %{public}@"
+ "[DMCRapidReturnToServiceFlowController] Failed to request RRTS obliteration with error: %{public}@"
+ "[DMCRapidReturnToServiceFlowController] start obliteration"
+ "[DMCRapidReturnToServiceFlowController] start timer"
+ "[DMCWiFiAutoJoinStateMachine] Failed to complete the flow and disabled WiFi"
+ "[DMCWiFiAutoJoinStateMachine] Failed to turn on WiFi: %{public}@"
+ "[DMCWiFiAutoJoinStateMachine] Invalid state"
+ "[DMCWiFiAutoJoinStateMachine] Invalid transition: %{public}@ -> %{public}@"
+ "[DMCWiFiAutoJoinStateMachine] Perform valid state transition: %@ -> %@"
+ "[DMCWiFiAutoJoinStateMachine] Transition to Power On state from %{public}@"
+ "^{_NSZone=}16@0:8"
+ "_ADE_RRTS_snapshotSteps"
+ "_ADE_bootstrapTokenSteps"
+ "_ADE_cleanupOrphanedAppsSteps"
+ "_ADE_migration_cleanupSteps"
+ "_allOverrides"
+ "_analyzeCloudConfig:enrollmentType:isDoingReturnToService:obliterationShelter:"
+ "_analyzeProfileData:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isRapidReturnToService:"
+ "_awaitApplicationInstallation"
+ "_awaitDDMAppConfigurationWithProfileIdentifier:"
+ "_blockMDMCommands"
+ "_bootstrapToken"
+ "_canUsePendingCloudConfig"
+ "_cleanupDirtyState"
+ "_cleanupOrphanedAppsIfNeededIsDoingRRTS:"
+ "_cloudConfigIndicatesRapidReturnToService"
+ "_controller"
+ "_createAndSyncBootstrapTokenWithPasscode:"
+ "_createEnrollmentTypeNotSupportedError"
+ "_createFailedToCaptureSnapshotError"
+ "_createFailedToDeleteSnapshotError"
+ "_createStartMigrationRequestFailedErrorWithDEPResponse:"
+ "_createUnenrollmentFailedError"
+ "_currentState"
+ "_disablePushWake"
+ "_enablePushWake"
+ "_enrollmentCloudConfig"
+ "_enrollmentFlowController"
+ "_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentMethod:isReturnToService:"
+ "_finalizeMigration"
+ "_formalizePendingCloudConfig:"
+ "_hasBlockedMDMCommands"
+ "_hasEnabledPushWake"
+ "_invalidStateTransitionError"
+ "_isDoingReturnToService"
+ "_machineInfoWithEnrollmentType:enrollmentMethod:isDoingReturnToService:isRapidReturnToService:"
+ "_mdmProfileData"
+ "_migrationCompletionHandler"
+ "_migrationConfigFilePath"
+ "_migrationDelegate"
+ "_migration_commonSteps"
+ "_migration_enrollmentSteps"
+ "_migration_unenrollmentSteps"
+ "_obliterationInfo"
+ "_originEnrollmentType"
+ "_pendingCloudConfig"
+ "_performEnrollmentFlow"
+ "_performUnenrollmentFlow"
+ "_preflightMigration"
+ "_preflightUnenrollmentWithUnenrollmentType:accoutAltDSID:"
+ "_preserveManagedAppsIfNeededWithPendingCloudConfig:"
+ "_processPotentialMigrationIfNeededWithEnrollmentType:cloudConfig:"
+ "_promptForMigrationConsentWithEnrollmentType:pendingCloudConfig:"
+ "_removeExistingCloudConfigProfile"
+ "_removePendingCloudConfigIfNeededWithEnrollmentCloudConfig:"
+ "_sendEndMigrationRequestWithCloudConfig:"
+ "_sendStartMigrationRequestWithPendingCloudConfig:"
+ "_stateMachine"
+ "_takeSnapshot"
+ "_timeoutTimer"
+ "_trackDirtyAppBundleIDs:personaID:"
+ "_unblockMDMCommands"
+ "_unblockMDMCommandsIfNeededHasBlocked:"
+ "_unenrollmentFlowController"
+ "_unenrollmentType"
+ "_uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:unenrollmentType:"
+ "_userDefaultsToPreserve"
+ "_verifyPropertiesFromProfileData:enrollmentMethod:isRapidReturnToService:isESSO:essoAppITunesStoreID:enrollmentMode:managedAppleID:assignedManagedAppleID:serverCapabilities:error:"
+ "_wifi"
+ "_wifiProfileData"
+ "activationRecordIndicatesCloudConfigurationIsAvailable"
+ "appInstallationStatusUpdatedForType:totalNumber:finishedNumber:"
+ "autorelease"
+ "awaitPendingApplicationInstallationWithObserver:completionHandler:"
+ "blockMDMCommandsWithCompletionHandler:"
+ "bootstrapToken"
+ "bundleID"
+ "canUsePendingCloudConfig"
+ "captureSystemVolumeSnapshotWithName:"
+ "checkInRequestFailedWithError:"
+ "class"
+ "cleanupOrphanedAppsWithCompletionHandler done"
+ "cleanupOrphanedAppsWithCompletionHandler:"
+ "cloudConfigIndicatesRapidReturnToService"
+ "com.apple.managedconfiguration.notbackedup"
+ "compare:"
+ "conformsToProtocol:"
+ "controller"
+ "createBootstrapTokenIfNeededWithPasscode:completionHandler:"
+ "currentEnrollmentType"
+ "currentPendingCloudConfigOnDisk"
+ "currentState"
+ "debugDescription"
+ "deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:"
+ "deleteSystemVolumeSnapshotWithName:"
+ "description"
+ "dismissMigrationScene"
+ "dismissUnenrollmentSceneWithError:"
+ "enableAutoJoinIfNeededWithTimeout:completionHandler:"
+ "enrollmentCloudConfig"
+ "enrollmentFlowController:appInstallationStatusUpdatedForType:totalNumber:finishedNumber:"
+ "enrollmentFlowController:performingEnrollmentStepWithName:status:"
+ "enrollmentFlowControllerIsDoingMigration:"
+ "enrollmentServerInfo"
+ "errorWithCode:message:"
+ "evaluateMigrationStatusWithPollFromServer came back with error: %{public}@"
+ "evaluateMigrationStatusWithPollFromServer:completionHandler:"
+ "existingCloudConfigOnDisk"
+ "getMachineInfoForEnrollmentType:enrollmentMethod:canRequestSoftwareUpdate:"
+ "hasBlockedMDMCommands"
+ "hasEnabledPushWake"
+ "hasIncompleteMigration"
+ "hash"
+ "haveNetwork"
+ "initWithBundleID:personaID:"
+ "initWithCloudConfigDetails:"
+ "initWithFilePath:"
+ "initWithReason:"
+ "installedMDMProfileIdentifier"
+ "invalidate"
+ "isAwaitingConfiguration"
+ "isDoingReturnToService"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isMigrationMandatoryWithPendingCloudConfig:"
+ "isMigrationNeeded"
+ "isMigrationNeededWithExistingCloudConfig:newCloudConfig:"
+ "isMigrationSupportedWithExistingCloudConfig:"
+ "isProxy"
+ "isRapidReturnToService"
+ "isSharediPad"
+ "launchMigrationApplicationWithError:"
+ "makeEndMDMMigrationRequestWithServerUID:status:completionBlock:"
+ "makeEndMigrationRequestIfNeededWithCloudConfig:completionHandler:"
+ "makeStartMDMMigrationRequestWithCompletionBlock:"
+ "makeStartMigrationRequestWithCloudConfig:completionHandler:"
+ "managedConfigurationHelper didn't implement the unblockMDMCommandsWithCompletionHandler method"
+ "managingProfileIdentifier"
+ "mdmServerUID"
+ "migrationCompletionHandler"
+ "migrationDeadline"
+ "migrationDelegate"
+ "migrationFlowController:appInstallationStatusUpdatedForType:totalNumber:finishedNumber:"
+ "migrationFlowController:performingEnrollmentStepWithName:status:"
+ "migrationFlowController:performingMigrationStepWithName:status:"
+ "newAppIdentifierWithIdentifier:"
+ "now"
+ "objectForKey:inDomain:"
+ "obliterationInfo"
+ "originEnrollmentType"
+ "pendingCloudConfig"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "powerOn"
+ "prepareToObliterationWithCompletionHandler:"
+ "presentUnenrollmentActivityPageIsAppleMAID:"
+ "preserveManagedAppsWithCompletionHandler:"
+ "preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:"
+ "processWiFiAutoJoinStateRequest:reason:completion:"
+ "progressToDisableWiFiWithReason:"
+ "progressToHaveNetworkWithCompletion:"
+ "progressToPowerOnWithCompletion:"
+ "progressToState:reason:completion:"
+ "readPendingCloudConfigDetails"
+ "refreshDetailsFromDisk"
+ "release"
+ "removeApplicationWithBundleID:personaID:completionHandler:"
+ "removeCloudConfigWithCompletionHandler:"
+ "removePendingCloudConfigWithCompletionHandler:"
+ "removeProtectedProfileWithIdentifier:completionHandler:"
+ "removeSetAsideCloudConfigWithCompletionHandler:"
+ "requestCheckInWithRetryCount:completion:"
+ "requestRRTSCheckInAndValidationWithCompletionHandler:"
+ "requestRapidReturnToServiceWithCompletion:"
+ "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:"
+ "requestUserConsentForMigrationWithPendingCloudConfig:originalEnrollmentType:isMandatory:deadline:completionHandler:"
+ "resetToState:"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "retrieveDictionaryWithError:"
+ "retrieveValueForKey:error:"
+ "returnToServiceFlowCompleted"
+ "saveValue:forKey:error:"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "self"
+ "server_uid"
+ "setAdditionalDetails:"
+ "setBootstrapToken:"
+ "setCanUsePendingCloudConfig:"
+ "setCloudConfigIndicatesRapidReturnToService:"
+ "setController:"
+ "setEnrollmentCloudConfig:"
+ "setEnrollmentFlowController:"
+ "setHasBlockedMDMCommands:"
+ "setHasEnabledPushWake:"
+ "setIsDoingReturnToService:"
+ "setIsRapidReturnToService:"
+ "setIsSharediPad:"
+ "setMigrationCompletionHandler:"
+ "setMigrationDelegate:"
+ "setMigrationIncomplete:"
+ "setObliterationInfo:"
+ "setOriginEnrollmentType:"
+ "setPendingCloudConfig:"
+ "setPower:error:"
+ "setRebootType:"
+ "setStateMachine:"
+ "setTimeoutTimer:"
+ "setUnenrollmentFlowController:"
+ "setUnenrollmentType:"
+ "setUserDefaults:"
+ "setUserInititiatedMigration:"
+ "sharedClient"
+ "sharedService"
+ "shouldDoRapidReturnToService"
+ "shouldDoReturnToService"
+ "shouldPreserveUserDefaultsForReturnToService"
+ "shouldShowMigrationUI"
+ "showMigrationCompletionScene"
+ "showMigrationFailure:"
+ "shutdownWithOptions:"
+ "standardUserDefaults"
+ "startMDMMigrationWithCompletionHandler:"
+ "startObliterationWithCompletion:"
+ "stateMachine"
+ "stringWithFormat:"
+ "success"
+ "superclass"
+ "syncBootstrapToken:completionHandler:"
+ "timeoutTimer"
+ "unblockMDMCommandsWithCompletionHandler:"
+ "unenrollADEWithCompletionHandler:"
+ "unenrollmentFlowController"
+ "unenrollmentFlowController:willUninstallProfile:"
+ "unenrollmentType"
+ "userInititiatedMigration"
+ "userMode"
+ "v16@?0@\"NSTimer\"8"
+ "v28@?0B8@\"NSArray\"12@\"NSError\"20"
+ "v28@?0B8@\"NSDictionary\"12@\"NSError\"20"
+ "v32@0:8@\"DMCEnrollmentFlowController\"16@\"NSDictionary\"24"
+ "v32@0:8@\"DMCUnenrollmentFlowController\"16@\"NSString\"24"
+ "v32@0:8Q16@24"
+ "v32@0:8q16@?24"
+ "v40@0:8@\"NSString\"16Q24Q32"
+ "v40@0:8@16Q24Q32"
+ "v40@0:8Q16@24@?32"
+ "v40@?0@\"NSData\"8@\"NSData\"16@\"NSData\"24@\"NSError\"32"
+ "v48@0:8@16@24Q32Q40"
+ "v56@0:8@16Q24Q32B40@44B52"
+ "v60@0:8@16@24@32@40Q48B56"
+ "waitForDDMAppsToBeRegisteredForMDMProfile:completionHandler:"
+ "wifi"
+ "wifiAutoJoinFailedWithReason:"
+ "zone"
- "-[DMCEnrollmentFlowController _fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:]_block_invoke_2"
- "B52@0:8@16Q24B32@36^@44"
- "Cleaning up dirty application with bundle ID %{public}@..."
- "Doing RRTS on non-ADE enrolled device, need to preserve the cloud config"
- "TB,N,V_isReturnToService"
- "_analyzeCloudConfig:enrollmentType:isReturnToService:obliterationShelter:"
- "_extractAndVerifyPropertiesFromProfileData:enrollmentMethod:isESSO:essoAppITunesStoreID:error:"
- "_fetchEnrollmentProfileFromServiceURL:authTokens:machineInfo:anchorCertificateRefs:enrollmentType:enrollmentMethod:isESSO:essoAppITunesStoreID:isReturnToService:"
- "_isReturnToService"
- "_preflightUnenrollmentWithAccoutAltDSID:"
- "_trackDirtyAppBundleIDs:"
- "_uninstallEnrollmentProfileWithIdentifier:personaID:altDSID:isAppleMAID:"
- "dismissUnenrollmentScene"
- "getMachineInfoForEnrollmentType:enrollmentMethod:"
- "isReturnToService"
- "memberQueueManagingProfileIdentifier"
- "presentActivityPageForAppleMAID:"
- "removeApplicationWithBundleID:completionHandler:"
- "setIsReturnToService:"
- "v44@0:8@16@24@32B40"
- "v80@0:8@16@24@32@40Q48Q56B64@68B76"

```
