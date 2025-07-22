## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-48.0.0.0.0
-  __TEXT.__text: 0x540a4
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x404c
-  __TEXT.__const: 0x19a
+49.0.0.0.0
+  __TEXT.__text: 0x55ccc
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x417c
+  __TEXT.__const: 0x1a2
   __TEXT.__gcc_except_tab: 0x1110
-  __TEXT.__cstring: 0x5482
-  __TEXT.__oslogstring: 0x64f5
+  __TEXT.__cstring: 0x5592
+  __TEXT.__oslogstring: 0x6ca5
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x11d0
+  __TEXT.__unwind_info: 0x1210
   __TEXT.__eh_frame: 0x178
-  __TEXT.__objc_classname: 0x6af
-  __TEXT.__objc_methname: 0xe64c
-  __TEXT.__objc_methtype: 0x1b15
-  __TEXT.__objc_stubs: 0xb5a0
-  __DATA_CONST.__got: 0x1170
-  __DATA_CONST.__const: 0x1e78
+  __TEXT.__objc_classname: 0x6c4
+  __TEXT.__objc_methname: 0xeb1e
+  __TEXT.__objc_methtype: 0x1b90
+  __TEXT.__objc_stubs: 0xb980
+  __DATA_CONST.__got: 0x11a8
+  __DATA_CONST.__const: 0x1f10
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3388
+  __DATA_CONST.__objc_selrefs: 0x3490
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0x4fe0
-  __AUTH_CONST.__objc_const: 0x68e0
+  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__const: 0x610
+  __AUTH_CONST.__cfstring: 0x5080
+  __AUTH_CONST.__objc_const: 0x6a40
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH.__objc_data: 0xe80
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x27c
-  __DATA.__data: 0x790
+  __DATA.__objc_ivar: 0x294
+  __DATA.__data: 0x7f0
   __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x140
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F8251329-2222-3203-8FD4-9ECE9ABB3168
-  Functions: 1619
-  Symbols:   6539
-  CStrings:  4159
+  UUID: 9B6A3236-94E8-375D-8D2A-EC8C6A68DCFD
+  Functions: 1647
+  Symbols:   6658
+  CStrings:  4261
 
Symbols:
+ +[MDMMigrationManager _bootUUID]
+ -[MDMDEPPushTokenManager initWithPushServiceManager:networkMonitor:]
+ -[MDMMigrationManager _isFirstBoot]
+ -[MDMMigrationManager bootUUID]
+ -[MDMMigrationManager handleDeadlineActionForNagItem:]
+ -[MDMServerCore _listenForCleanupMigrationFinishedNotificationAndRetryTokenUpdate]
+ -[MDMServerCore _memberQueueDeviceDidBecomeActive]
+ -[MDMServerCore _memberQueueDeviceDidBecomeIdleWithTimeoutInterval:]
+ -[MDMServerCore _memberQueueInactivityTaskFired:]
+ -[MDMServerCore _memberQueueRRTSTimeoutReached]
+ -[MDMServerCore _memberQueueScheduleRRTSInactivityTaskWithInterval:]
+ -[MDMServerCore isRRTSInactivityTaskScheduled]
+ -[MDMServerCore networkMonitor]
+ -[MDMServerCore prepareToObliterationWithCompletionHandler:]
+ -[MDMServerCore rrtsController]
+ -[MDMServerCore rrtsIdleTimeout]
+ -[MDMServerCore rrtsLastInactivityTime]
+ -[MDMServerCore setNetworkMonitor:]
+ -[MDMServerCore setRrtsController:]
+ -[MDMServerCore setRrtsIdleTimeout:]
+ -[MDMServerCore setRrtsInactivityTaskScheduled:]
+ -[MDMServerCore setRrtsLastInactivityTime:]
+ GCC_except_table12
+ GCC_except_table137
+ GCC_except_table151
+ GCC_except_table158
+ GCC_except_table162
+ GCC_except_table168
+ GCC_except_table172
+ GCC_except_table179
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table207
+ GCC_except_table212
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table276
+ GCC_except_table29
+ GCC_except_table316
+ GCC_except_table331
+ GCC_except_table335
+ GCC_except_table351
+ GCC_except_table41
+ GCC_except_table46
+ GCC_except_table71
+ GCC_except_table85
+ _DMCLocalizedStringByDevice
+ _IOPMScheduleUserActivityLevelNotificationWithTimeout
+ _IOPMUnregisterNotification
+ _MCRapidReturnToServiceNotification
+ _OBJC_CLASS_$_DMCRapidReturnToServiceFlowController
+ _OBJC_CLASS_$_DMCSystemAlert
+ _OBJC_CLASS_$_DMCSystemAlertManager
+ _OBJC_IVAR_$_MDMMigrationManager._bootUUID
+ _OBJC_IVAR_$_MDMServerCore._networkMonitor
+ _OBJC_IVAR_$_MDMServerCore._rrtsController
+ _OBJC_IVAR_$_MDMServerCore._rrtsIdleTimeout
+ _OBJC_IVAR_$_MDMServerCore._rrtsInactivityTaskScheduled
+ _OBJC_IVAR_$_MDMServerCore._rrtsLastInactivityTime
+ __OBJC_$_CLASS_METHODS_MDMMigrationManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DMCRRTSFlowDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_DMCRRTSFlowDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DMCRRTSFlowDelegate
+ __OBJC_$_PROTOCOL_REFS_DMCRRTSFlowDelegate
+ __OBJC_LABEL_PROTOCOL_$_DMCRRTSFlowDelegate
+ __OBJC_PROTOCOL_$_DMCRRTSFlowDelegate
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke.33
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke_2.34
+ ___125-[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]_block_invoke.79
+ ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1348
+ ___31-[MDMServerCore setMDMOptions:]_block_invoke.276
+ ___31-[MDMServerCore setMDMOptions:]_block_invoke_2.278
+ ___37-[MDMServerCore initWithChannelType:]_block_invoke
+ ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.148
+ ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.153
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1197
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1198
+ ___47-[MDMServerCore _memberQueueRRTSTimeoutReached]_block_invoke
+ ___47-[MDMServerCore _memberQueueRRTSTimeoutReached]_block_invoke.372
+ ___48-[MDMServerCore blockMDMCommandsWithCompletion:]_block_invoke.188
+ ___50-[MDMParser _performSetSharedDeviceConfiguration:]_block_invoke
+ ___50-[MDMServerCore unblockMDMCommandsWithCompletion:]_block_invoke.189
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1493
+ ___54-[MDMMigrationManager handleDeadlineActionForNagItem:]_block_invoke
+ ___54-[MDMMigrationManager handleDeadlineActionForNagItem:]_block_invoke_2
+ ___54-[MDMServerCore _memberQueueRegisterForRRTSIdleEvents]_block_invoke
+ ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.279
+ ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.255
+ ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.316
+ ___66-[MDMServerCore nagForMigrationWithHardCodedValuesWithCompletion:]_block_invoke_2.169
+ ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.977
+ ___68-[MDMServerCore _memberQueueScheduleRRTSInactivityTaskWithInterval:]_block_invoke
+ ___68-[MDMServerCore syncBootstrapTokenToMDMWithToken:completionHandler:]_block_invoke.176
+ ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.120
+ ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke.302
+ ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke_2.303
+ ___80-[MDMServerCore _syncBootstrapTokenToMDMWithToken:retryCount:completionHandler:]_block_invoke_2
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.105
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.99
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.106
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.111
+ ___82-[MDMServerCore _listenForCleanupMigrationFinishedNotificationAndRetryTokenUpdate]_block_invoke
+ ___82-[MDMServerCore _listenForCleanupMigrationFinishedNotificationAndRetryTokenUpdate]_block_invoke_2
+ ___82-[MDMServerCore _listenForCleanupMigrationFinishedNotificationAndRetryTokenUpdate]_block_invoke_3
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.178
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.179
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.180
+ ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.307
+ ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.309
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.78
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.79
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.86
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.97
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke_2.90
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.182
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.183
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.184
+ ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.10
+ ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.13
+ ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.14
+ ___block_descriptor_32_e8_v16?0Q8l
+ ___block_descriptor_40_e8_32s_e11_v24?0Q8Q16ls32l8
+ ___block_descriptor_40_e8_32s_e34_v16?0"DMCBackgroundTaskWrapper"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_literal_global.1044
+ ___block_literal_global.1088
+ ___block_literal_global.1105
+ ___block_literal_global.1193
+ ___block_literal_global.1207
+ ___block_literal_global.1372
+ ___block_literal_global.1412
+ ___block_literal_global.1417
+ ___block_literal_global.1484
+ ___block_literal_global.19
+ ___block_literal_global.191
+ ___block_literal_global.258
+ ___block_literal_global.319
+ ___block_literal_global.35
+ ___block_literal_global.37
+ ___block_literal_global.374
+ ___block_literal_global.385
+ ___block_literal_global.942
+ ___block_literal_global.944
+ ___block_literal_global.946
+ ___block_literal_global.948
+ ___block_literal_global.950
+ ___block_literal_global.957
+ _clock_gettime_nsec_np
+ _kCCConfigurationSourceKey
+ _kCCIsSupervisedKey
+ _kMDMActivityIdleTimeout
+ _objc_msgSend$_bootUUID
+ _objc_msgSend$_isFirstBoot
+ _objc_msgSend$_listenForCleanupMigrationFinishedNotificationAndRetryTokenUpdate
+ _objc_msgSend$_memberQueueDeviceDidBecomeActive
+ _objc_msgSend$_memberQueueDeviceDidBecomeIdleWithTimeoutInterval:
+ _objc_msgSend$_memberQueueInactivityTaskFired:
+ _objc_msgSend$_memberQueueRRTSTimeoutReached
+ _objc_msgSend$_memberQueueScheduleRRTSInactivityTaskWithInterval:
+ _objc_msgSend$_notInRRTSModeError
+ _objc_msgSend$bootUUID
+ _objc_msgSend$bootstrapTokenOverrideWithDefaultValue:
+ _objc_msgSend$deadline
+ _objc_msgSend$displayAlert:
+ _objc_msgSend$extendForInterval:error:
+ _objc_msgSend$initWithPushServiceManager:networkMonitor:
+ _objc_msgSend$isMigrationNag
+ _objc_msgSend$isRRTSInactivityTaskScheduled
+ _objc_msgSend$isRRTSMDMTimeoutEnabled
+ _objc_msgSend$isRRTSUEATimeoutEnabled
+ _objc_msgSend$launchMigrationApplicationWithError:
+ _objc_msgSend$minimumExtensionInterval
+ _objc_msgSend$nagMigrationGracePeriod
+ _objc_msgSend$requestRapidReturnToServiceWithCompletion:
+ _objc_msgSend$rrtsController
+ _objc_msgSend$rrtsIdleTimeout
+ _objc_msgSend$rrtsIdleTimeoutTask
+ _objc_msgSend$rrtsLastInactivityTime
+ _objc_msgSend$setDefaultButtonText:
+ _objc_msgSend$setDisplayOnLockScreen:
+ _objc_msgSend$setRrtsController:
+ _objc_msgSend$setRrtsIdleTimeout:
+ _objc_msgSend$setRrtsInactivityTaskScheduled:
+ _objc_msgSend$setRrtsLastInactivityTime:
+ _objc_msgSend$shouldSuppressRRTSOnIdleTimeout
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$waitForNetworkWithCompletionHandler:timeout:
+ _sysctlbyname
- -[MDMDEPPushTokenManager initWithPushServiceManager:]
- -[MDMMigrationManager initWithNagScheduluer:]
- -[MDMServerCore _listenForCleanupMigrationFinishedNotificaitonAndRetryTokenUpdate]
- -[MDMServerCore _memberQueueRRTSTimeoutFired]
- GCC_except_table134
- GCC_except_table14
- GCC_except_table150
- GCC_except_table155
- GCC_except_table159
- GCC_except_table165
- GCC_except_table169
- GCC_except_table176
- GCC_except_table182
- GCC_except_table187
- GCC_except_table19
- GCC_except_table201
- GCC_except_table209
- GCC_except_table220
- GCC_except_table225
- GCC_except_table265
- GCC_except_table272
- GCC_except_table28
- GCC_except_table309
- GCC_except_table324
- GCC_except_table340
- GCC_except_table40
- GCC_except_table45
- GCC_except_table70
- GCC_except_table84
- ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke.34
- ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke_2.35
- ___125-[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]_block_invoke.80
- ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1350
- ___31-[MDMServerCore setMDMOptions:]_block_invoke.272
- ___31-[MDMServerCore setMDMOptions:]_block_invoke_2.274
- ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.146
- ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.151
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1199
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1200
- ___48-[MDMServerCore blockMDMCommandsWithCompletion:]_block_invoke.185
- ___50-[MDMServerCore unblockMDMCommandsWithCompletion:]_block_invoke.186
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1495
- ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.275
- ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.251
- ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.312
- ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.980
- ___68-[MDMServerCore syncBootstrapTokenToMDMWithToken:completionHandler:]_block_invoke.173
- ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.118
- ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke.298
- ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke_2.299
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.103
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.97
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.104
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.109
- ___82-[MDMServerCore _listenForCleanupMigrationFinishedNotificaitonAndRetryTokenUpdate]_block_invoke
- ___82-[MDMServerCore _listenForCleanupMigrationFinishedNotificaitonAndRetryTokenUpdate]_block_invoke_2
- ___82-[MDMServerCore _listenForCleanupMigrationFinishedNotificaitonAndRetryTokenUpdate]_block_invoke_3
- ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.175
- ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.176
- ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.177
- ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.303
- ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.305
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.76
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.77
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.84
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.95
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke_2.88
- ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.179
- ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.180
- ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.181
- ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.11
- ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.12
- ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.8
- ___block_literal_global.1047
- ___block_literal_global.1091
- ___block_literal_global.1108
- ___block_literal_global.1197
- ___block_literal_global.1209
- ___block_literal_global.1376
- ___block_literal_global.1414
- ___block_literal_global.1419
- ___block_literal_global.1486
- ___block_literal_global.17
- ___block_literal_global.188
- ___block_literal_global.254
- ___block_literal_global.315
- ___block_literal_global.377
- ___block_literal_global.945
- ___block_literal_global.947
- ___block_literal_global.949
- ___block_literal_global.951
- ___block_literal_global.953
- ___block_literal_global.960
- _objc_msgSend$_listenForCleanupMigrationFinishedNotificaitonAndRetryTokenUpdate
- _objc_msgSend$bootstrapTokenOverride
- _objc_msgSend$init
- _objc_msgSend$initWithNagScheduluer:
- _objc_msgSend$initWithPushServiceManager:
CStrings:
+ "-[MDMServerCore _listenForCleanupMigrationFinishedNotificationAndRetryTokenUpdate]_block_invoke"
+ "-[MDMServerCore _memberQueueRRTSTimeoutReached]"
+ "@\"DMCRapidReturnToServiceFlowController\""
+ "B24@0:8@\"DMCNagItem\"16"
+ "Begin processing of Rapid Return to Service Task"
+ "Cancelling idle timeout task; there's no longer a timeout in place!"
+ "Clearing last inactivity date"
+ "Current active timeout task is significantly longer than the current timeout; cancelling. This may result in extended timeout delays"
+ "DMCNagMigrationLastBootUUID"
+ "DMCRRTSFlowDelegate"
+ "Deregistering keep-alive"
+ "Device has become active."
+ "Device has become inactive, but no temporary session timeout is set"
+ "Device has become inactive."
+ "Elapsed idle time: %llus; target idle time: %fs"
+ "End processing of Rapid Return to Service Task"
+ "Extending idle timeout for additional %fs"
+ "Failed to extend idle timeout task: %{public}@"
+ "Ignoring idle timeout, as no temporary session timeout is set"
+ "Invoking RRTS flow controller"
+ "Invoking idle timer handler"
+ "Last idle time: %llus; now: %llus"
+ "MDMMigrationManager: Applying %{public}f grace period (%{public}@) to MDM migration nag: %{public}@"
+ "MDMMigrationManager: Cannot start nagging without a nag scheduler"
+ "MDMMigrationManager: Cannot stop nagging without a nag scheduler"
+ "MDMMigrationManager: Failed to get boot UUID"
+ "MDMMigrationManager: Ignoring grace period because we already checked this boot: %{public}@"
+ "MDMMigrationManager: Ignoring grace period for far out MDM migration nag: %{public}@"
+ "MDMMigrationManager: Launching post-deadline system migration action for nag: %{public}@"
+ "MDMParser: bundleID for the current installation is: %{public}@"
+ "MDMServerCore proceeding with obliteration"
+ "MDM_MIGRATION_OPTION_RESTART"
+ "MDM_MIGRATION_RESTART_WARNING_TEXT"
+ "MDM_MIGRATION_RESTART_WARNING_TITLE"
+ "Processing Rapid Return to Service idle timeout task"
+ "RRTS process failed: %{public}@"
+ "RRTS timeout fired but we're not in RRTS mode!?"
+ "Rapid Return to Service has been initiated."
+ "Recording last inactivity date"
+ "Registered IOPMActivityLevelNotifications"
+ "Registering for IOKit power notifications"
+ "Registering for Rapid Return to Service notification."
+ "Registering to keep mdmd alive"
+ "Scheduling idle timeout task with interval: %f"
+ "Skipping RRTS machinery because default is set!"
+ "T@\"DMCRapidReturnToServiceFlowController\",&,N,V_rrtsController"
+ "T@\"NSString\",R,N,V_bootUUID"
+ "TB,N,GisRRTSInactivityTaskScheduled,V_rrtsInactivityTaskScheduled"
+ "TQ,N,V_rrtsLastInactivityTime"
+ "Td,N,V_rrtsIdleTimeout"
+ "Timeout task fired early with %fs remaining"
+ "Unregistering Rapid Return to Service Background tasks."
+ "Unregistering for IOKit power notifications."
+ "_bootUUID"
+ "_isFirstBoot"
+ "_listenForCleanupMigrationFinishedNotificationAndRetryTokenUpdate"
+ "_memberQueueDeviceDidBecomeActive"
+ "_memberQueueDeviceDidBecomeIdleWithTimeoutInterval:"
+ "_memberQueueInactivityTaskFired:"
+ "_memberQueueRRTSTimeoutReached"
+ "_memberQueueScheduleRRTSInactivityTaskWithInterval:"
+ "_rrtsController"
+ "_rrtsIdleTimeout"
+ "_rrtsInactivityTaskScheduled"
+ "_rrtsLastInactivityTime"
+ "bootUUID"
+ "bootstrapTokenOverrideWithDefaultValue:"
+ "checkInRequestFailedWithError:"
+ "com.apple.devicemanagementclient.mdmd.rrts"
+ "deadline"
+ "displayAlert:"
+ "extendForInterval:error:"
+ "handleDeadlineActionForNagItem:"
+ "initWithPushServiceManager:networkMonitor:"
+ "isMigrationNag"
+ "isRRTSInactivityTaskScheduled"
+ "isRRTSMDMTimeoutEnabled"
+ "isRRTSUEATimeoutEnabled"
+ "kern.bootsessionuuid"
+ "launchMigrationApplicationWithError:"
+ "minimumExtensionInterval"
+ "nagMigrationGracePeriod"
+ "prepareToObliterationWithCompletionHandler:"
+ "requestRapidReturnToServiceWithCompletion:"
+ "rrtsController"
+ "rrtsIdleTimeout"
+ "rrtsInactivityTaskScheduled"
+ "rrtsLastInactivityTime"
+ "setDefaultButtonText:"
+ "setDisplayOnLockScreen:"
+ "setRrtsController:"
+ "setRrtsIdleTimeout:"
+ "setRrtsInactivityTaskScheduled:"
+ "setRrtsLastInactivityTime:"
+ "shouldSuppressRRTSOnIdleTimeout"
+ "stringForKey:"
+ "v16@?0Q8"
+ "v24@0:8@\"NSError\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@?<v@?B>16"
+ "v24@?0Q8Q16"
+ "v32@?0@8@16^B24"
+ "waitForNetworkWithCompletionHandler:timeout:"
+ "wifiAutoJoinFailedWithReason:"
- "-[MDMServerCore _listenForCleanupMigrationFinishedNotificaitonAndRetryTokenUpdate]_block_invoke"
- "MDMParser: bundleID for the current installtion is: %{public}@"
- "_listenForCleanupMigrationFinishedNotificaitonAndRetryTokenUpdate"
- "_memberQueueRRTSTimeoutFired"
- "bootstrapTokenOverride"
- "initWithNagScheduluer:"
- "initWithPushServiceManager:"

```
