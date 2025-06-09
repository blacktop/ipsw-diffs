## profiled

> `/usr/libexec/profiled`

```diff

-2400.5.2.0.0
-  __TEXT.__text: 0x9f4f0
-  __TEXT.__auth_stubs: 0x2230
-  __TEXT.__objc_stubs: 0xfbe0
-  __TEXT.__objc_methlist: 0x56e4
-  __TEXT.__const: 0x1fc
-  __TEXT.__gcc_except_tab: 0x1940
-  __TEXT.__oslogstring: 0xce1c
-  __TEXT.__cstring: 0x8d0c
-  __TEXT.__objc_methname: 0x13640
-  __TEXT.__objc_classname: 0xb36
-  __TEXT.__objc_methtype: 0x205a
-  __TEXT.__unwind_info: 0x16b0
-  __DATA_CONST.__auth_got: 0x1128
+2420.1.1.0.0
+  __TEXT.__text: 0xa0064
+  __TEXT.__auth_stubs: 0x20e0
+  __TEXT.__objc_stubs: 0x10520
+  __TEXT.__objc_methlist: 0x5a9c
+  __TEXT.__const: 0x20e
+  __TEXT.__gcc_except_tab: 0x1bf8
+  __TEXT.__oslogstring: 0xd717
+  __TEXT.__cstring: 0x89c2
+  __TEXT.__objc_methname: 0x14470
+  __TEXT.__objc_classname: 0xb59
+  __TEXT.__objc_methtype: 0x224b
+  __TEXT.__unwind_info: 0x16f8
+  __DATA_CONST.__auth_got: 0x1080
   __DATA_CONST.__got: 0x1bb8
-  __DATA_CONST.__const: 0x1b50
-  __DATA_CONST.__cfstring: 0x8540
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __DATA_CONST.__const: 0x1b90
+  __DATA_CONST.__cfstring: 0x85c0
+  __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_intobj: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6088
-  __DATA.__objc_selrefs: 0x45d0
-  __DATA.__objc_ivar: 0x1c0
-  __DATA.__objc_data: 0x1bd0
+  __DATA.__objc_const: 0x6568
+  __DATA.__objc_selrefs: 0x48d0
+  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x540
   __DATA.__common: 0x20
-  __DATA.__bss: 0x268
+  __DATA.__bss: 0x240
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/ClassroomKit.framework/ClassroomKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DataAccess.framework/DataAccess

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C9D9208C-65C9-3AA1-8B35-84E9E12D43A3
-  Functions: 2025
-  Symbols:   1480
-  CStrings:  5989
+  UUID: 3719F0A3-AC1C-3603-B13C-F2CF88AFF8A3
+  Functions: 2038
+  Symbols:   1459
+  CStrings:  6129
 
Symbols:
+ _CFErrorCopyDescription
+ _MAEDeactivateDeviceWithError
+ _MCKeybagCreateMDMEscrowWithPasscodeContext
+ _MCPostSetupAutoInstallProfilePathNF
+ _MDMSendSkipkeyChangedNotification
+ _MKBDeviceUnlockedSinceBoot
+ _MKBKeyBagChangeSystemSecretWithACM
+ _MKBKeyBagChangeSystemSecretWithEscrowWithACM
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_CWFInterface
+ _OBJC_CLASS_$_DMCReturnToServiceHelper
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_MCExtractablePasscodeContextWrapper
+ _OBJC_CLASS_$_MCSecurePasscodeContextWrapper
+ _OBJC_CLASS_$_MDMUserConfiguration
+ _kCCHasUndergoneMigrationKey
+ _kCCIgnoreMDMFromBackupKey
+ _kCCIsRapidReturnToServiceKey
+ _kCCMDMServerUIDKey
+ _kDMCProfileInstallationSourceMDMMigration
+ _kMCMDMProfileIdentifierToWiFiRecoveryNetworkPayloadUUIDDependencyKey
+ _kSecAttrAccessibleAlways
- _CFRunLoopGetCurrent
- _IOConnectCallScalarMethod
- _IOConnectCallStructMethod
- _MCKeybagCreateMDMEscrowWithPasscode
- _MCPostSetupAutoInstallProfilePath
- _MCUMUserManagerClass
- _MDMUserFilePath
- _MKBKeyBagChangeSystemSecret
- _MKBKeyBagChangeSystemSecretOpts
- _MKBKeyBagChangeSystemSecretWithEscrow
- _OBJC_CLASS_$_LSApplicationProxy
- _SecKeyGeneratePair
- _SecTrustGetCertificateAtIndex
- _WiFiDeviceClientGetInterfaceName
- _WiFiManagerClientGetPower
- _WiFiManagerClientScheduleWithRunLoop
- _WiFiManagerClientSetPower
- _WiFiManagerClientUnscheduleFromRunLoop
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- _XPC_ACTIVITY_INTERVAL_1_MIN
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRES_CLASS_A
- _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
- __os_log_default
- _dispatch_queue_attr_make_with_qos_class
- _kCFRunLoopDefaultMode
- _memcpy
- _printf
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_state
- _xpc_activity_should_defer
- _xpc_activity_unregister
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_int64
- _xpc_dictionary_set_string
CStrings:
+ "%s waking up mdmd"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "+"
+ "-[MCInteractionClient requestCurrentPasscodeOutPasscodeContextWrapper:]"
+ "-[MCProfileServiceServer changePasscodeWithOldPasscodeContext:newPasscodeContext:isRecovery:skipRecovery:senderBundleID:completion:]_block_invoke"
+ "-[MCProfileServiceServer clearPasscodeWithEscrowKeybagData:secretContext:senderBundleID:completion:]_block_invoke"
+ "-[MCProfileServiceServer createMDMUnlockTokenIfNeededWithPasscodeContext:completion:]_block_invoke"
+ "-[MCProfileServiceServer setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:senderPID:sender:completion:]_block_invoke"
+ "-[MCProfileServiceServer start]_block_invoke_4"
+ "@\"BGSystemTask\""
+ "@\"MCBackgroundTask\""
+ "@\"MCBackgroundTaskManager\""
+ "@\"NSData\"36@0:8Q16Q24B32"
+ "@\"NSDictionary\"16@0:8"
+ "@36@0:8Q16Q24B32"
+ "@40@0:8@16@24@?32"
+ "@40@0:8d16d24Q32"
+ "@48@0:8@16d24d32Q40"
+ "B56@0:8@16@24B32B36@40@48"
+ "Could not enable WiFi: %{public}@"
+ "Could not generate public/private key pair: %{public}@"
+ "ERROR_WIFI_ONLY_ALLOWED_IN_RTS_MODE"
+ "ERROR_WIFI_ONLY_ONE_RECOVERY_NETWORK"
+ "Failed to initialize application record for %{public}@ with error %{public}@"
+ "MCBackgroundTask"
+ "MCBackgroundTask %{public}@ already exists, attempting to cancel before submitting again"
+ "MCBackgroundTask canceled task: %{public}@"
+ "MCBackgroundTask canceling task %{public}@..."
+ "MCBackgroundTask deallocated task: %{public}@"
+ "MCBackgroundTask expiration handler called for task: %{public}@"
+ "MCBackgroundTask failed to cancel task %{public}@ with error: %{public}@"
+ "MCBackgroundTask failed to register task: %{public}@"
+ "MCBackgroundTask failed to submit task %{public}@ with error: %{public}@"
+ "MCBackgroundTask failed to update task %{public}@ with error: %{public}@"
+ "MCBackgroundTask ignoring cancellation for inactive task %{public}@"
+ "MCBackgroundTask initialized task: %{public}@"
+ "MCBackgroundTask launch handler called for task: %{public}@"
+ "MCBackgroundTask submitted task %{public}@ to run in %{public}f (+%{public}f) seconds"
+ "MCBackgroundTask submitting task %{public}@..."
+ "MCBackgroundTask updated task %{public}@ to run in %{public}f (+%{public}f) seconds"
+ "MCBackgroundTask updating task %{public}@..."
+ "MCBackgroundTaskManager"
+ "MCBackgroundTaskManager cannot debug schedule invalid task: '%{public}@'"
+ "MCBackgroundTaskManager failed to clear recovery passcode opaque data with error: %{public}@"
+ "MCBackgroundTaskManager failed to clear recovery passcode with error: %{public}@"
+ "MCBackgroundTaskManager has no recovery passcode, clearing associated data if necessary"
+ "MCBackgroundTaskManager log level is heightened. Checking MDM installation status..."
+ "MCBackgroundTaskManager schedule queue"
+ "MCBackgroundTaskManager scheduling activation lock cleanup task because activation lock bypass code was stored"
+ "MCBackgroundTaskManager scheduling managed app validation & MIS trust update because managed applications changed"
+ "MCBackgroundTaskManager scheduling passcode and recovery passcode expiry checks because passcode changed"
+ "MCBackgroundTaskManager scheduling passcode expiry check because passcode policy changed"
+ "MCBackgroundTaskManager scheduling profile janitor tasks because profile list changed"
+ "MCBackgroundTaskManager start"
+ "MCBackgroundTaskManager stop"
+ "MCBackgroundTaskWrapper"
+ "MCBackgroundTaskWrapper dealloc called with an incomplete task: %{public}@"
+ "MCCleanupMigrator Profile Removal for same device restore"
+ "MCCleanupMigrator: Cleaning up MDM profile for Return to Service."
+ "MCCleanupMigrator: Cleaning up cloud config for Return to Service."
+ "MCCleanupMigrator: Cleaning up for Rapid Return to Service..."
+ "MCCleanupMigrator: Deactivated the device"
+ "MCCleanupMigrator: Failed to deactivate the device"
+ "MCCleanupMigrator: Not doing Rapid Return to Service, returning..."
+ "MCCleanupMigrator: Removed Return to Service MDM profile"
+ "MCCleanupMigrator: Removing cloud config details."
+ "MCCleanupMigrator: Removing data separated (PDUE/ADUE/ADDE) MDM profile"
+ "MCCleanupMigrator: ServerUID has changed. New ServerUID: %{public}@, backup ServerUID: %{public}@"
+ "MCCleanupMigrator: cloud config indicates that we should ignore the MDM from backup."
+ "MCCleanupMigrator: preserveAppsWithCompletion timed out"
+ "MCMigrator: _checkValidUserEnrollment Failed to update MDM config with error: %{public}@"
+ "MCMigrator: _correctMDMConfigurationFile Failed to update MDM config with error: %{public}@"
+ "MCNewWiFiPayloadHandler AutoJoinBeforeFirstUnlock not supported outside of RTS mode"
+ "MCNewWiFiPayloadHandler unable to remove %{public}@WiFi payload with UUID: %{public}@ - before first unlock"
+ "MCNewWiFiPayloadHandler: another WiFi payload (%{public}@) in profile with identifier: %{public}@ already has auto join before first unlock set"
+ "MCProvisioningProfileJanitor maintaining MC signers: %@"
+ "MCProvisioningProfileJanitor skipping signer sync after MIS enumeration failed. Maintaining MC signers: %@"
+ "MCProvisioningProfileJanitor syncing MIS signers to MC: %@"
+ "MCProvisioningProfileJanitor updating MIS trust with MC signers: %@"
+ "MCProvisioningProfileJanitor.syncMCTrustedCodeSigningIdentities:"
+ "MCRestrictionManagerWriter cannot recompute nag metadata because the device is locked."
+ "Not taking over unmanaged profiles during MDM migration"
+ "Return to Service Enrollment Profile Removal"
+ "T@\"BGSystemTask\",&,N,V_task"
+ "T@\"MCBackgroundTask\",&,N,V_activationLockCleanupTask"
+ "T@\"MCBackgroundTask\",&,N,V_dailyAnalyticsTask"
+ "T@\"MCBackgroundTask\",&,N,V_managedAppValidationTask"
+ "T@\"MCBackgroundTask\",&,N,V_orphanedRestrictionsCleanupTask"
+ "T@\"MCBackgroundTask\",&,N,V_passcodeExpiryTask"
+ "T@\"MCBackgroundTask\",&,N,V_profileEventsJanitorTask"
+ "T@\"MCBackgroundTask\",&,N,V_profileJanitorTask"
+ "T@\"MCBackgroundTask\",&,N,V_recomputeNagMetadataTask"
+ "T@\"MCBackgroundTask\",&,N,V_recoveryPasscodeExpiryTask"
+ "T@\"MCBackgroundTaskManager\",&,N,V_workerQueueBackgroundTaskManager"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_scheduleQueue"
+ "T@\"NSString\",&,N,V_name"
+ "T@?,C,N,V_completion"
+ "TB,N,V_active"
+ "TB,N,V_completed"
+ "TB,N,V_firstActionAfterInit"
+ "_activationLockBypassCodeWasStored:"
+ "_activationLockCleanupTask"
+ "_active"
+ "_aks_set_configuration"
+ "_applyEnforcedCloudConfigRules:"
+ "_cancelTask:"
+ "_cleanupCloudConfigForReturnToService"
+ "_cleanupForReturnToServiceIfNeeded"
+ "_completed"
+ "_completion"
+ "_dailyAnalyticsTask"
+ "_debug_scheduleBackgroundTask:interval:tolerance:"
+ "_debug_scheduleBackgroundTask:interval:tolerance:completion:"
+ "_defaultTolerance"
+ "_firstActionAfterInit"
+ "_infuseRequest:interval:tolerance:requirements:"
+ "_intervalForDate:normalize:"
+ "_intervalForInterval:normalize:"
+ "_managedAppValidationTask"
+ "_name"
+ "_orphanedRestrictionsCleanupTask"
+ "_passcodeExpiryTask"
+ "_profileEventsJanitorTask"
+ "_profileJanitorTask"
+ "_promptUserForComplianceWithRestrictions:handler:interactionClient:outPasscodeContextWrapper:outError:"
+ "_recomputeNagMetadataTask"
+ "_recoveryPasscodeExpiryTask"
+ "_removeCloudConfigAndMDMProfileIfNeeded"
+ "_removeNetworkWithUUID:isAllowedBeforeFirstUnlock:"
+ "_scheduleActivationLockCleanupTask"
+ "_scheduleDailyAnalyticsTask"
+ "_scheduleOrphanedRestrictionsCleanupTask"
+ "_schedulePasscodeExpiryTask"
+ "_scheduleQueue"
+ "_shouldIgnoreCloudConfigFromBackup"
+ "_submitNewRequestWithInterval:tolerance:requirements:"
+ "_submitTask:interval:tolerance:requirements:"
+ "_task"
+ "_updateCDPWithNewPasscodeContextWrapper:passcodeType:"
+ "_updateExistingRequest:interval:tolerance:requirements:"
+ "_workerQueueBackgroundTaskManager"
+ "_workerQueue_setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:senderPID:sender:assertion:completion:"
+ "activate"
+ "activationLockCleanup"
+ "activationLockCleanupTask"
+ "activationRecordIndicatesCloudConfigurationIsAvailable"
+ "active"
+ "allowJoinBeforeFirstUnlock"
+ "appSignerIdentityForBundleID:"
+ "applyEffectiveSettings:toOtherSubsystemsWithCredentialSet:"
+ "applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
+ "applyRestrictionDictionary:toSystem:overrideRestrictions:appsAndOptions:clientType:clientUUID:sender:localizedClientDescription:localizedWarningMessage:completion:"
+ "awaitPendingApplicationInstallationWithObserver:completionHandler:"
+ "awaitSystemDeletableAppsInstallationWithCompletionHandler:"
+ "blockMDMCommandsWithCompletionHandler:"
+ "canInstallPayloadWithJoinBeforeFirstUnlock:error:"
+ "cancel"
+ "cancelTaskRequestWithIdentifier:error:"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:isRecovery:skipRecovery:completion:"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:isRecovery:skipRecovery:senderBundleID:completion:"
+ "changePasscodeWithOldPasscodeContext:newPasscodeContext:skipRecovery:senderBundleID:outError:"
+ "changePasscodeWithRecoveryPasscodeContext:newPasscodeContext:skipRecovery:senderBundleID:outError:"
+ "characteristicsDictionaryFromPasscodeContext:"
+ "cleanupOrphanedAppsWithCompletionHandler:"
+ "clearPasscodeWithEscrowKeybagData:secretContext:completion:"
+ "clearPasscodeWithEscrowKeybagData:secretContext:senderBundleID:completion:"
+ "clearPasscodeWithEscrowKeybagData:secretContext:senderBundleID:outError:"
+ "completed"
+ "completion"
+ "contextWrapperForExtractablePasscode:outError:"
+ "contextWrapperForSecureSecretData:outError:"
+ "contextWrapperFromExternalizedContext:outError:"
+ "copyBundleLocation:bundleType:completion:"
+ "copyLeafCertificateFromTrust:"
+ "createBootstrapTokenIfNeededWithPasscode:completionHandler:"
+ "createMDMUnlockTokenIfNeededWithPasscodeContext:completion:"
+ "credentialSetForPasscode:outError:"
+ "d28@0:8@16B24"
+ "d28@0:8d16B24"
+ "dailyAnalytics"
+ "dailyAnalyticsTask"
+ "deleteBootstrapTokenWithBootstrapToken:passcode:completionHandler:"
+ "deregisterTaskWithIdentifier:"
+ "disablePushWakeWithCompletionHandler:"
+ "enablePushWakeWithCompletionHandler:"
+ "evaluateMigrationStatusWithPollFromServer:completionHandler:"
+ "existingCloudConfigOnDisk"
+ "externalizedContext"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "firstActionAfterInit"
+ "getMachineInfoForEnrollmentType:enrollmentMethod:canRequestSoftwareUpdate:"
+ "getWatchPairingTokenForPhoneID:watchID:securityToken:completionHandler:"
+ "hashForPasscodeContext:usingMethod:salt:customIterations:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithIdentifier:"
+ "initWithName:queue:completion:"
+ "initWithTask:"
+ "installedMDMProfileIdentifier"
+ "interfaceName"
+ "isAccountModificationAllowed"
+ "isRapidReturnToService"
+ "managedAppValidation"
+ "managedAppValidationTask"
+ "managingProfileIdentifier"
+ "memberQueueRecomputeEffectiveUserSettingsWithCredentialSet:"
+ "memberQueueSetParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:sender:"
+ "name"
+ "now"
+ "organizationInfo"
+ "orphanedRestrictionsCleanup"
+ "orphanedRestrictionsCleanupTask"
+ "passcode"
+ "passcodeContext:compliesWithPolicyFromRestrictions:checkHistory:outError:"
+ "passcodeExists"
+ "passcodeExpiry"
+ "passcodeExpiryTask"
+ "passcodeLength"
+ "powerOn"
+ "preserveAppsWithCompletion:"
+ "profileEventsJanitor"
+ "profileEventsJanitorTask"
+ "profileJanitor"
+ "profileJanitorTask"
+ "profiled-DebugScheduleBackgroundTask"
+ "recomputeEffectiveUserSettings"
+ "recomputeNagMetadataTask"
+ "recoveryPasscodeExpiry"
+ "recoveryPasscodeExpiryTask"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "removeApplicationWithBundleID:personaID:completionHandler:"
+ "removeCloudConfigWithCompletionHandler:"
+ "removeMDMConfigurationWithError:"
+ "removeProtectedProfileWithIdentifier:completionHandler:"
+ "removeSetAsideCloudConfigWithCompletionHandler:"
+ "requestCurrentPasscodeOutPasscodeContextWrapper:"
+ "scheduleManagedAppValidationTask:"
+ "scheduleProfileJanitorTask"
+ "scheduleQueue"
+ "scheduleRecomputeNagMetadataTask"
+ "scheduleRecoveryPasscodeExpiryTask"
+ "sendMDMAuthenticationRequestWithCompletionHandler:"
+ "sendMDMCheckOutRequestWithCompletionHandler:"
+ "serverURL"
+ "setActivationLockCleanupTask:"
+ "setActive:"
+ "setCompleted:"
+ "setCompletion:"
+ "setDailyAnalyticsTask:"
+ "setExpirationHandler:"
+ "setFirstActionAfterInit:"
+ "setManagedAppValidationTask:"
+ "setOrphanedRestrictionsCleanupTask:"
+ "setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:completion:"
+ "setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:sender:"
+ "setParametersForSettingsByType:configurationUUID:toSystem:user:credentialSet:senderPID:sender:completion:"
+ "setPasscodeExpiryTask:"
+ "setPersonaIdentifier:"
+ "setPower:error:"
+ "setPriority:"
+ "setProfileEventsJanitorTask:"
+ "setProfileJanitorTask:"
+ "setRecomputeNagMetadataTask:"
+ "setRecoveryPasscodeExpiryTask:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setRequiresProtectionClass:"
+ "setRequiresUserInactivity:"
+ "setScheduleAfter:"
+ "setScheduleQueue:"
+ "setTask:"
+ "setTaskCompleted"
+ "setTrySchedulingBefore:"
+ "setWorkerQueueBackgroundTaskManager:"
+ "sharedScheduler"
+ "shouldDoRapidReturnToService"
+ "signerIdentityForBundleID:completion:"
+ "skipKeys"
+ "submitRequestWithInterval:tolerance:requirements:"
+ "submitTaskRequest:error:"
+ "syncBootstrapToken:completionHandler:"
+ "syncMCTrustedCodeSigningIdentities:"
+ "syncTrustedCodeSigningIdentitiesWithCompletion:"
+ "task"
+ "taskRequestForIdentifier:"
+ "timeIntervalSinceDate:"
+ "trustedCodeSigningIdentitiesWithCompletion:"
+ "unblockMDMCommandsWithCompletionHandler:"
+ "unlockDeviceWithPasscodeContext:outError:"
+ "updateMDMConfigurationWithCreateIfNeeded:updateBlock:error:"
+ "updateMDMConfigurationWithUpdateBlock:error:"
+ "updatePasscodeHistoryWithOldPasscodeContext:oldPasscodeExists:oldPasscodeLength:newPrivateDictionary:"
+ "updateTaskRequest:error:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"MCBackgroundTaskWrapper\"8"
+ "v16@?0@\"NSMutableDictionary\"8"
+ "v28@0:8B16@?<v@?B@\"NSError\">20"
+ "v32@0:8@\"<DMCEnrollmentFlowAppInstallationObserver>\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16d24d32"
+ "v44@0:8@16B24Q28@36"
+ "v48@0:8@\"NSData\"16@\"NSData\"24B32B36@?<v@?B@\"NSError\">40"
+ "v48@0:8@\"NSString\"16d24d32@?<v@?@\"NSError\">40"
+ "v48@0:8@16d24d32@?40"
+ "v48@0:8@16d24d32Q40"
+ "v56@0:8@\"NSDictionary\"16@\"NSString\"24B32B36@\"NSData\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24B32B36@40@?48"
+ "v68@0:8@16@24B32B36@40i48@52@?60"
+ "v76@0:8@16@24B32B36@40i48@52@60@?68"
+ "v80@0:8@\"NSDictionary\"16B24B28@\"NSArray\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@?<v@?BB@\"NSError\">72"
+ "v80@0:8@16B24B28@32@40@48@56@64@?72"
+ "v88@0:8@16B24B28@32@40@48@56@64@72@?80"
+ "waitForDDMAppsToBeRegisteredForMDMProfile:completionHandler:"
+ "workerQueueBackgroundTaskManager"
- "!"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s: %s: CS[%u] %s.\n"
- "%s: %s: CS[%u] created.\n"
- "%s: %s: called.\n"
- "%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n"
- "%s: %s: cmd(%u) on CS[%u] -> ok.\n"
- "%s: %s: log level set to %d.\n"
- "%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n"
- "%s: %s: returning, err = %ld.\n"
- "%s: %s: returning.\n"
- "%{public}@"
- ", Repeat Interval: %@"
- ", Require Network: true"
- ", Require Unlock: true"
- "-[MCInteractionClient requestCurrentPasscodeOutPasscode:]"
- "-[MCProfileServiceServer addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:sender:completion:]_block_invoke"
- "-[MCProfileServiceServer changePasscode:oldPasscode:skipRecovery:senderBundleID:completion:]_block_invoke"
- "-[MCProfileServiceServer changePasscode:recoveryPasscode:skipRecovery:senderBundleID:completion:]_block_invoke"
- "-[MCProfileServiceServer clearPasscodeWithEscrowKeybagData:secret:senderBundleID:completion:]_block_invoke"
- "-[MCProfileServiceServer createMDMUnlockTokenIfNeededWithPasscode:completion:]_block_invoke"
- "-[MCProfileServiceServer setParametersForSettingsByType:configurationUUID:toSystem:user:passcode:credentialSet:senderPID:sender:completion:]_block_invoke"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "1"
- "<data>"
- "@\"MCBackgroundActivityManager\""
- "@\"MCProfileServiceServer\""
- "@24@0:8q16"
- "ACM"
- "ACMContextCreate"
- "ACMContextDelete"
- "ACMContextGetExternalForm"
- "ACMHandleWithPayload"
- "ACMLib"
- "Activation lock bypass code was stored. Rescheduling activation lock cleanup."
- "AddTrusted"
- "AppleCredentialManager"
- "B64@0:8@16@24B32B36@40@48@56"
- "Background activity fired but deferred. name %s result %i"
- "Cancelling %{public}@"
- "Cannot check out because the Check-In URL is invalid."
- "Cannot check out because the MDM identity cannot be retrieved."
- "Changing passcode with no options"
- "Couldn't create auth context: ACM err %d"
- "Couldn't verify input passcode: MKB err %d"
- "DMCSafePropertyListWithData:options:format:error:"
- "Failed to clear recovery passcode opaque data: %{public}@"
- "LibCall_ACMContextCreate"
- "LibCall_ACMContextDelete"
- "LibCall_BuildCommand"
- "Log level is heightened. Checking MDM installation status."
- "MCBackgroundActivityManager"
- "MCBackgroundActivityManager work queue"
- "MCCleanupMigrator: Removed data separated (PDUE/ADUE/ADDE) MDM profile"
- "MCProfileServiceServer missing code signing identities for provisioning profile UUID: %{public}@"
- "MCProvisioningProfileJanitor skipping MCFeatureTrustedCodeSigningIdentities update after MIS enumeration failed"
- "MCProvisioningProfileJanitor updating MIS trust..."
- "MCProvisioningProfileJanitor._syncMCTrustedCodeSigningIdentities"
- "Managed applications changed. Rescheduling managed app validation & MIS trust update"
- "NULL"
- "No new code signing identities for provisioning profile UUID: %{public}@"
- "No recovery passcode, clearing associated data if necessary"
- "PROVISIONING_ERROR_NO_SIGNING_IDENTITIES"
- "Passcode changed. Rescheduling passcode and recovery passcode expiry checks"
- "Passcode policy changed. Rescheduling passcode expiry check"
- "Performing %{public}@ (Nil self? %d)…"
- "Profile list changed. Rescheduling profile janitor."
- "Scheduling %@ at %@. Priority: %s, Grace Period: %@%@%@%@"
- "T@\"MCBackgroundActivityManager\",&,N,V_workerQueueBackgroundActivityManager"
- "T@\"MCProfileServiceServer\",W,N,V_server"
- "Trusting %{public}d new code signing identities for provisioning profile UUID: %{public}@"
- "Unable to clear recovery passcode. Error: %{public}@"
- "User Enrollment Profile Removal"
- "_aks_verify_password"
- "_handleXPCActivity:proposedStartDate:normalizeStartDate:proposedGracePeriod:proposedPriority:repeatingInterval:requireNetwork:requireUnlock:"
- "_jobDescriptionForBackgroundActivityType:"
- "_jobNameForBackgroundActivityType:"
- "_newZStringWithString:"
- "_nextActivationLockCleanupDate"
- "_nextManagedAppValidationDateWithOverride:"
- "_promptUserForComplianceWithRestrictions:handler:interactionClient:outPasscode:outError:"
- "_removeMDMProfileIfDataSeparated"
- "_removeNetworkWithUUID:"
- "_rescheduleBackgroundActivity:startDate:gracePeriod:priority:repeatingInterval:"
- "_server"
- "_syncMCTrustedCodeSigningIdentities:"
- "_updateCDPWithNewPasscode:passcodeType:"
- "_workQueueReschedule:startDate:gracePeriod:priority:repeatingInterval:"
- "_workQueueReschedulePasscodeExpiryJob"
- "_workQueueRescheduleRecoveryPasscodeExpiryJob"
- "_workerQueueBackgroundActivityManager"
- "_workerQueue_setParametersForSettingsByType:configurationUUID:toSystem:user:passcode:credentialSet:senderPID:sender:assertion:completion:"
- "acm_mem_alloc_info"
- "acm_mem_free_info"
- "activation lock token cleanup"
- "activationLockBypassCodeWasStored:"
- "addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:completion:"
- "addTrustedCodeSigningIdentitiesForProvisioningProfileUUID:sender:completion:"
- "aks_set_configuration"
- "applicationProxyForIdentifier:"
- "applyEffectiveSettings:toOtherSubsystemsPasscode:credentialSet:"
- "applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:localizedClientDescription:localizedWarningMessage:completion:"
- "applyRestrictionDictionary:overrideRestrictions:appsAndOptions:clientType:clientUUID:sender:localizedClientDescription:localizedWarningMessage:completion:"
- "authenticateWithCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:topic:useDevelopmentAPNS:signMessage:isUserEnrollment:enrollmentID:outError:"
- "changePasscode:oldPasscode:skipRecovery:senderBundleID:completion:"
- "changePasscode:recoveryPasscode:skipRecovery:senderBundleID:completion:"
- "changePasscodeFrom:to:skipRecovery:senderBundleID:outError:"
- "changePasscodeWithRecoveryPasscode:to:skipRecovery:senderBundleID:outError:"
- "characteristicsDictionaryFromPasscode:"
- "checkOutCheckInURL:identity:pinnedSecCertificateRefs:pinningRevocationCheckRequired:topic:signMessage:isUserEnrollment:enrollmentID:outError:"
- "clearPasscodeWithEscrowKeybagData:secret:senderBundleID:completion:"
- "clearPasscodeWithEscrowKeybagData:secret:senderBundleID:outError:"
- "copyCarrierBundleLocation:completion:"
- "copyCertificatesWithPersistentIDs:useSystemKeychain:"
- "core analytics daily status event"
- "debugRescheduleBackgroundActivity:startDate:gracePeriod:repeatingInterval:completion:"
- "deleted"
- "destroyed"
- "earliestRequiredManagedAppValidationDate"
- "failed to open connection to %s\n"
- "getWatchPairingTokenForPhoneID:watchID:securityToken:outError:"
- "hashForPasscode:usingMethod:salt:customIterations:"
- "ioKitTransport"
- "laterDate:"
- "managed app validation"
- "memberQueueManagingProfileIdentifier"
- "memberQueueOrganizationInfo"
- "memberQueueRecomputeEffectiveUserSettingsPasscode:credentialSet:"
- "memberQueueServerURL"
- "memberQueueSetParametersForSettingsByType:configurationUUID:toSystem:user:passcode:credentialSet:sender:"
- "numberWithLongLong:"
- "orphaned restrictions cleanup"
- "passcode expiry check"
- "performCommand"
- "profile events janitor cleanup"
- "profile janitor cleanup"
- "profiled-AddTrustedProvisioningProfile"
- "profiled-ChangePasscodeWithRecovery"
- "profiled-DebugRescheduleBackgroundActivity"
- "r*24@0:8q16"
- "recompute nag metadata"
- "recomputeEffectiveUserSettingsPasscode:"
- "recovery passcode expiry check"
- "removeApplicationWithBundleID:completionHandler:"
- "requestCurrentPasscodeOutPasscode:"
- "rescheduleManagedAppValidationJob"
- "rescheduleManagedAppValidationJob:"
- "reschedulePasscodeExpiryJob"
- "rescheduleProfileJanitorJob"
- "rescheduleRecoveryPasscodeExpiryJob"
- "revalidateManagedApps"
- "scheduleRecomputeNagMetadataJob"
- "server"
- "setParametersForSettingsByType:configurationUUID:toSystem:user:passcode:credentialSet:sender:"
- "setParametersForSettingsByType:configurationUUID:toSystem:user:passcode:credentialSet:senderPID:sender:completion:"
- "setServer:"
- "setWorkerQueueBackgroundActivityManager:"
- "signerIdentitiesFromProvisioningProfileUUID:"
- "timeIntervalSinceNow"
- "unlockDeviceWithPasscode:outError:"
- "updateLogLevelFromKext"
- "updatePasscodeHistoryWithOldPasscode:oldPasscodeData:newPrivateDictionary:"
- "v24@?0r^v8Q16"
- "v52@0:8@16@24B32@36@?44"
- "v56@0:8q16@\"NSDate\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSError\">48"
- "v56@0:8q16@24@32@40@?48"
- "v56@0:8q16@24@32r*40@48"
- "v68@0:8q16@24B32@36r*44@52B60B64"
- "v76@0:8@\"NSDictionary\"16B24@\"NSArray\"28@\"NSString\"36@\"NSString\"44@\"NSString\"52@\"NSString\"60@?<v@?BB@\"NSError\">68"
- "v76@0:8@16@24B32B36@40@48i56@60@?68"
- "v76@0:8@16B24@28@36@44@52@60@?68"
- "v84@0:8@16@24B32B36@40@48i56@60@68@?76"
- "v84@0:8@16B24@28@36@44@52@60@68@?76"
- "workerQueueBackgroundActivityManager"
- "workerQueueRemoveExpiredProfiles"
- "workerQueueRevalidateManagedApps"

```
