## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-43.0.0.0.0
-  __TEXT.__text: 0x50fb8
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_methlist: 0x3f3c
+46.0.0.0.0
+  __TEXT.__text: 0x53e60
+  __TEXT.__auth_stubs: 0xf00
+  __TEXT.__objc_methlist: 0x404c
   __TEXT.__const: 0x192
-  __TEXT.__gcc_except_tab: 0x10d4
-  __TEXT.__cstring: 0x5192
-  __TEXT.__oslogstring: 0x6089
+  __TEXT.__gcc_except_tab: 0x1110
+  __TEXT.__cstring: 0x5482
+  __TEXT.__oslogstring: 0x64f5
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1180
+  __TEXT.__unwind_info: 0x11c8
   __TEXT.__eh_frame: 0x150
   __TEXT.__objc_classname: 0x6af
-  __TEXT.__objc_methname: 0xe1c2
-  __TEXT.__objc_methtype: 0x1a9f
-  __TEXT.__objc_stubs: 0xb360
-  __DATA_CONST.__got: 0x1148
-  __DATA_CONST.__const: 0x1d60
+  __TEXT.__objc_methname: 0xe64c
+  __TEXT.__objc_methtype: 0x1b15
+  __TEXT.__objc_stubs: 0xb5a0
+  __DATA_CONST.__got: 0x1170
+  __DATA_CONST.__const: 0x1e78
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32f0
+  __DATA_CONST.__objc_selrefs: 0x3388
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x788
-  __AUTH_CONST.__const: 0x568
-  __AUTH_CONST.__cfstring: 0x4e80
-  __AUTH_CONST.__objc_const: 0x6840
+  __AUTH_CONST.__auth_got: 0x790
+  __AUTH_CONST.__const: 0x588
+  __AUTH_CONST.__cfstring: 0x4fe0
+  __AUTH_CONST.__objc_const: 0x68e0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH.__objc_data: 0xe80

   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libutil.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 912743C3-E4B3-34C0-B8AC-89F05A636FE9
-  Functions: 1571
-  Symbols:   6425
-  CStrings:  4089
+  UUID: 569109C1-ECED-317D-9BC7-5797489A09AD
+  Functions: 1616
+  Symbols:   6538
+  CStrings:  4159
 
Symbols:
+ +[MDMBootstrapTokenUtilities _generateBootstrapTokenContextFailed]
+ +[MDMBootstrapTokenUtilities deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:]
+ +[MDMBootstrapTokenUtilities deleteBootstrapTokenWithTokenContext:devicePasscodeContext:completionHandler:]
+ +[MDMBootstrapTokenUtilities generateBootstrapTokenWithDevicePasscodeContext:completionHandler:]
+ +[MDMBootstrapTokenUtilities validateBootstrapTokenContext:error:]
+ +[MDMInstalledApplicationListCommand expensiveItems]
+ -[MDMDEPPushTokenManager _migrationEligibilityChanged]
+ -[MDMDEPPushTokenManager _queue_isSyncNeededWithAppToken:eligibleForMigration:shouldForce:]
+ -[MDMDEPPushTokenManager _queue_lastSyncedEligibility]
+ -[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]
+ -[MDMDEPPushTokenManager _queue_retryPushTokenSync]
+ -[MDMDEPPushTokenManager _queue_scheduleAppTokenSync]
+ -[MDMDEPPushTokenManager _queue_scheduleMandatoryDEPPushTokenSyncWithDelay:reason:isRetry:]
+ -[MDMDEPPushTokenManager _queue_setLastSyncedEligibility:]
+ -[MDMDEPPushTokenManager _queue_startMonitoringDEPPushTokenChange]
+ -[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]
+ -[MDMMigrationManager _cancelMDMMigrationWithNewCloudConfig:]
+ -[MDMMigrationManager _handleNewCloudConfigIfNeeded:currentCloudConfig:didPollFromDEP:]
+ -[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]
+ -[MDMMigrationManager _scheduleMDMMigrationWithNewCloudConfigDetails:]
+ -[MDMMigrationManager _shouldMigrateWithNewCloudConfig:currentCloudConfig:isEligible:isMigrationNeeded:]
+ -[MDMMigrationManager nagWithCloudConfigDetails:]
+ -[MDMMigrationManager startMonitoringDEPServerPushIfNeeded]
+ -[MDMMigrationManager stopMonitoringDEPServerPush]
+ -[MDMServerCore _createServerMissingBootstrapTokenCapabilityError]
+ -[MDMServerCore deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:]
+ -[MDMServerCore deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:].cold.1
+ -[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]
+ -[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:].cold.1
+ -[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]
+ -[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:].cold.1
+ -[MDMServerCore generateBootstrapTokenWithDevicePasscodeContext:completionHandler:]
+ -[MDMServerCore generateBootstrapTokenWithDevicePasscodeContext:completionHandler:].cold.1
+ -[MDMServicerCore deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:]
+ -[MDMServicerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]
+ -[MDMServicerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]
+ -[MDMServicerCore generateBootstrapTokenWithDevicePasscodeContext:completionHandler:]
+ GCC_except_table134
+ GCC_except_table159
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table176
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table201
+ GCC_except_table204
+ GCC_except_table209
+ GCC_except_table225
+ GCC_except_table265
+ GCC_except_table272
+ GCC_except_table283
+ GCC_except_table320
+ GCC_except_table324
+ GCC_except_table340
+ _DMCCTTelephonyPropertiesForEnrollmentAuthentication
+ _DMCHangTracerDirectory
+ _MDMCreateLAContextWithPasscode
+ _MDMCreateLAContextWithPasscodeData
+ _MDMKeybagCopyEscrowWithACM
+ _MDMKeybagCreateMDMEscrowWithPasscodeContextData
+ _MDMMigrationEligibilityChangedNotification
+ _MDMSendMigrationEligibilityChangedNotification
+ _MKBKeyBagCreateEscrowWithACM
+ _OBJC_CLASS_$_DMCBacktraceLogger
+ _OBJC_CLASS_$_LAContext
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke.34
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke_2
+ ___118-[MDMDEPPushTokenManager _queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:]_block_invoke_2.35
+ ___125-[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]_block_invoke
+ ___125-[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]_block_invoke.80
+ ___125-[MDMDEPPushTokenManager _queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:]_block_invoke_2
+ ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1350
+ ___201+[MDMObliterationUtilities obliterateDeviceWithPreserveDataPlan:disallowProximitySetup:returnToServiceEnabled:exclusionPaths:revertToSnapshotName:bootstrapToken:preObliterationAction:completionHander:]_block_invoke.13
+ ___201+[MDMObliterationUtilities obliterateDeviceWithPreserveDataPlan:disallowProximitySetup:returnToServiceEnabled:exclusionPaths:revertToSnapshotName:bootstrapToken:preObliterationAction:completionHander:]_block_invoke_2
+ ___31-[MDMServerCore setMDMOptions:]_block_invoke.272
+ ___31-[MDMServerCore setMDMOptions:]_block_invoke_2.274
+ ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.146
+ ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.151
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1199
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1200
+ ___48-[MDMServerCore blockMDMCommandsWithCompletion:]_block_invoke.185
+ ___50-[MDMServerCore unblockMDMCommandsWithCompletion:]_block_invoke.186
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1495
+ ___54-[MDMDEPPushTokenManager _migrationEligibilityChanged]_block_invoke
+ ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.275
+ ___55-[MDMServerCore stopNaggingForMigrationWithCompletion:]_block_invoke_2
+ ___57+[MDMFindMyUtilities enableActivationLockWithCompletion:]_block_invoke.19
+ ___57+[MDMFindMyUtilities enableActivationLockWithCompletion:]_block_invoke.20
+ ___61-[MDMMigrationManager _cancelMDMMigrationWithNewCloudConfig:]_block_invoke
+ ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.251
+ ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.312
+ ___63-[MDMDEPPushTokenManager syncDEPPushTokenWithDelay:completion:]_block_invoke
+ ___66-[MDMServerCore nagForMigrationWithHardCodedValuesWithCompletion:]_block_invoke_2
+ ___67-[MDMDEPPushTokenManager schedulePeriodicMandatoryDEPPushTokenSync]_block_invoke
+ ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.980
+ ___68-[MDMServerCore syncBootstrapTokenToMDMWithToken:completionHandler:]_block_invoke.173
+ ___70-[MDMMigrationManager _scheduleMDMMigrationWithNewCloudConfigDetails:]_block_invoke
+ ___71-[MDMDEPPushTokenManager startMonitoringDEPPushTokenChangeShouldForce:]_block_invoke
+ ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.118
+ ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke.298
+ ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke_2.299
+ ___75-[MDMDEPPushTokenManager scheduleMandatoryDEPPushTokenSyncWithRandomDelay:]_block_invoke
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.103
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.104
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.109
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.175
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.176
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.177
+ ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.303
+ ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.305
+ ___87-[MDMMigrationManager _handleNewCloudConfigIfNeeded:currentCloudConfig:didPollFromDEP:]_block_invoke
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.76
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.77
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.84
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.95
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke_2.88
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.179
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.180
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.181
+ ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke
+ ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.11
+ ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.12
+ ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke.8
+ ___block_descriptor_32_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e17_v16?0"NSError"8ls40l8s32l8s48l8
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls48l8s32l8s40l8
+ ___block_descriptor_58_e8_32s40bs48w_e34_v16?0"DMCBackgroundTaskWrapper"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e28_v24?0"NSData"8"NSError"16ls48l8s56l8s32l8s40l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e37_v28?0B8"NSDictionary"12"NSError"20ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_91_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.1047
+ ___block_literal_global.1091
+ ___block_literal_global.1108
+ ___block_literal_global.1195
+ ___block_literal_global.1197
+ ___block_literal_global.1209
+ ___block_literal_global.1374
+ ___block_literal_global.1376
+ ___block_literal_global.1414
+ ___block_literal_global.1419
+ ___block_literal_global.1486
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.17
+ ___block_literal_global.188
+ ___block_literal_global.254
+ ___block_literal_global.315
+ ___block_literal_global.377
+ ___block_literal_global.945
+ ___block_literal_global.947
+ ___block_literal_global.949
+ ___block_literal_global.951
+ ___block_literal_global.953
+ ___block_literal_global.960
+ _kCCMDMMigrationDeadlineKey
+ _kCCMDMServerUIDKey
+ _objc_msgSend$_cancelMDMMigrationWithNewCloudConfig:
+ _objc_msgSend$_createServerMissingBootstrapTokenCapabilityError
+ _objc_msgSend$_generateBootstrapTokenContextFailed
+ _objc_msgSend$_handleNewCloudConfigIfNeeded:currentCloudConfig:didPollFromDEP:
+ _objc_msgSend$_queue_isSyncNeededWithAppToken:eligibleForMigration:shouldForce:
+ _objc_msgSend$_queue_lastSyncedEligibility
+ _objc_msgSend$_queue_retryPushTokenSync
+ _objc_msgSend$_queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:
+ _objc_msgSend$_queue_scheduleAppTokenSync
+ _objc_msgSend$_queue_scheduleMandatoryDEPPushTokenSyncWithDelay:reason:isRetry:
+ _objc_msgSend$_queue_setLastSyncedEligibility:
+ _objc_msgSend$_queue_startMonitoringDEPPushTokenChange
+ _objc_msgSend$_queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:
+ _objc_msgSend$_retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:
+ _objc_msgSend$_scheduleMDMMigrationWithNewCloudConfigDetails:
+ _objc_msgSend$_shouldMigrateWithNewCloudConfig:currentCloudConfig:isEligible:isMigrationNeeded:
+ _objc_msgSend$createBootstrapUserWithTokenInACMCredential:withDevicePasscodeInACMCredential:withError:
+ _objc_msgSend$currentEnrollmentStateSupportsMigration
+ _objc_msgSend$deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:
+ _objc_msgSend$deleteBootstrapTokenWithTokenContext:devicePasscodeContext:completionHandler:
+ _objc_msgSend$deleteBootstrapUserWithTokenInACMCredential:withDevicePasscodeInACMCredential:withError:
+ _objc_msgSend$dumpStackshotToPath:fileName:
+ _objc_msgSend$expensiveItems
+ _objc_msgSend$externalizedContext
+ _objc_msgSend$generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:
+ _objc_msgSend$generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:
+ _objc_msgSend$generateBootstrapTokenWithDevicePasscodeContext:completionHandler:
+ _objc_msgSend$imei
+ _objc_msgSend$isDeviceEligibleForMigrationWithExistingCloudConfig:outReason:
+ _objc_msgSend$isMigrationEligibilityReportEnabled
+ _objc_msgSend$makeEndMigrationRequestIfNeededWithCloudConfig:success:completionHandler:
+ _objc_msgSend$meid
+ _objc_msgSend$nagWithCloudConfigDetails:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$setCredential:type:
+ _objc_msgSend$startMonitoringDEPServerPushIfNeeded
+ _objc_msgSend$stopMonitoringDEPServerPush
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:
+ _objc_msgSend$validateBootstrapTokenContext:error:
+ _objc_msgSend$validateBootstrapUserWithTokenInACMCredential:withError:
- -[MDMDEPPushTokenManager _queue_appTokenNeedsToBeSynced]
- -[MDMDEPPushTokenManager _retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:]
- -[MDMDEPPushTokenManager _retryPushTokenSync]
- -[MDMDEPPushTokenManager _scheduleAppTokenSync]
- -[MDMDEPPushTokenManager _scheduleMandatoryDEPPushTokenSyncWithDelay:]
- -[MDMDEPPushTokenManager _startMonitoringDEPPushTokenChange]
- -[MDMDEPPushTokenManager _syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:]
- -[MDMMigrationManager _cancelMDMMigrationIfNeededWithNewCloudConfig:currentCloudConfig:]
- -[MDMMigrationManager _handleNewCloudConfigIfNeeded:currentCloudConfig:]
- -[MDMMigrationManager _isDeviceDEPEnrolled]
- -[MDMMigrationManager _scheduleMDMMigrationProcessWithNewCloudConfig:]
- -[MDMMigrationManager _shouldMigrateWithNewCloudConfig:currentCloudConfig:]
- -[MDMMigrationManager nagWithCloudConfig:]
- -[MDMMigrationManager startMonitoringDEPServerPush]
- GCC_except_table120
- GCC_except_table141
- GCC_except_table145
- GCC_except_table151
- GCC_except_table162
- GCC_except_table168
- GCC_except_table171
- GCC_except_table173
- GCC_except_table174
- GCC_except_table190
- GCC_except_table195
- GCC_except_table206
- GCC_except_table211
- GCC_except_table250
- GCC_except_table257
- GCC_except_table268
- GCC_except_table279
- GCC_except_table290
- GCC_except_table325
- _DMCCTIMEI
- _DMCCTMEID
- _MDMKeybagCopyEscrowWithAuth
- _MKBKeyBagCreateEscrowWithAuth
- ___105-[MDMDEPPushTokenManager _syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:]_block_invoke
- ___105-[MDMDEPPushTokenManager _syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:]_block_invoke.18
- ___105-[MDMDEPPushTokenManager _syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:]_block_invoke_2
- ___105-[MDMDEPPushTokenManager _syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:]_block_invoke_2.19
- ___105-[MDMDEPPushTokenManager _syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:]_block_invoke_3
- ___112-[MDMDEPPushTokenManager _retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:]_block_invoke
- ___112-[MDMDEPPushTokenManager _retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:]_block_invoke.58
- ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1347
- ___31-[MDMServerCore setMDMOptions:]_block_invoke.258
- ___31-[MDMServerCore setMDMOptions:]_block_invoke_2.260
- ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.140
- ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.144
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1196
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1197
- ___47-[MDMDEPPushTokenManager _scheduleAppTokenSync]_block_invoke
- ___48-[MDMServerCore blockMDMCommandsWithCompletion:]_block_invoke.168
- ___50-[MDMServerCore unblockMDMCommandsWithCompletion:]_block_invoke.169
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1492
- ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.261
- ___57+[MDMFindMyUtilities enableActivationLockWithCompletion:]_block_invoke.13
- ___57+[MDMFindMyUtilities enableActivationLockWithCompletion:]_block_invoke.14
- ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.236
- ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.298
- ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.977
- ___68-[MDMServerCore syncBootstrapTokenToMDMWithToken:completionHandler:]_block_invoke.162
- ___70-[MDMDEPPushTokenManager _scheduleMandatoryDEPPushTokenSyncWithDelay:]_block_invoke
- ___70-[MDMMigrationManager _scheduleMDMMigrationProcessWithNewCloudConfig:]_block_invoke
- ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.112
- ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke.284
- ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke_2.285
- ___76-[MDMMigrationManager _evaluateMigrationStatusShouldPoll:completionHandler:]_block_invoke.7
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.91
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.98
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.103
- ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.289
- ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.291
- ___88-[MDMMigrationManager _cancelMDMMigrationIfNeededWithNewCloudConfig:currentCloudConfig:]_block_invoke
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.70
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.71
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.78
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.89
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke_2.82
- ___block_descriptor_50_e8_32bs40w_e34_v16?0"DMCBackgroundTaskWrapper"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSError"8"NSDictionary"16ls48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56s64bs_e37_v28?0B8"NSDictionary"12"NSError"20ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_90_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.1044
- ___block_literal_global.1088
- ___block_literal_global.1105
- ___block_literal_global.1192
- ___block_literal_global.1194
- ___block_literal_global.1206
- ___block_literal_global.1371
- ___block_literal_global.1373
- ___block_literal_global.1411
- ___block_literal_global.1416
- ___block_literal_global.1483
- ___block_literal_global.160
- ___block_literal_global.162
- ___block_literal_global.171
- ___block_literal_global.239
- ___block_literal_global.301
- ___block_literal_global.360
- ___block_literal_global.942
- ___block_literal_global.944
- ___block_literal_global.946
- ___block_literal_global.948
- ___block_literal_global.950
- ___block_literal_global.957
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_MDM
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MDM
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MDM
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MDM
- _objc_msgSend$_cancelMDMMigrationIfNeededWithNewCloudConfig:currentCloudConfig:
- _objc_msgSend$_handleNewCloudConfigIfNeeded:currentCloudConfig:
- _objc_msgSend$_isDeviceDEPEnrolled
- _objc_msgSend$_queue_appTokenNeedsToBeSynced
- _objc_msgSend$_retryPushTokenSync
- _objc_msgSend$_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:
- _objc_msgSend$_scheduleAppTokenSync
- _objc_msgSend$_scheduleMDMMigrationProcessWithNewCloudConfig:
- _objc_msgSend$_scheduleMandatoryDEPPushTokenSyncWithDelay:
- _objc_msgSend$_shouldMigrateWithNewCloudConfig:currentCloudConfig:
- _objc_msgSend$_startMonitoringDEPPushTokenChange
- _objc_msgSend$_syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:
- _objc_msgSend$createBootstrapUserWithToken:withDevicePasscode:withError:
- _objc_msgSend$data
- _objc_msgSend$deleteBootstrapUserWithToken:withDevicePasscode:withError:
- _objc_msgSend$isADEProfile
- _objc_msgSend$isDEPPushEnabled
- _objc_msgSend$isMigrationSupportedWithExistingCloudConfig:
- _objc_msgSend$isStoredProfileInstalled
- _objc_msgSend$nagWithCloudConfig:
- _objc_msgSend$startMonitoringDEPServerPush
- _objc_msgSend$syncDEPPushToken:pushTopic:completionBlock:
- _objc_msgSend$validateBootstrapUserWithToken:withError:
CStrings:
+ "-[MDMServerCore deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:]"
+ "-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]"
+ "-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]"
+ "-[MDMServerCore generateBootstrapTokenWithDevicePasscodeContext:completionHandler:]"
+ "-[MDMServerCore nagForMigrationWithHardCodedValuesWithCompletion:]_block_invoke"
+ "-[MDMServerCore stopNaggingForMigrationWithCompletion:]_block_invoke"
+ "B32@0:8@16B24B28"
+ "B36@0:8@16@24B32"
+ "B48@0:8@16@24^B32^B40"
+ "Bootstrap token synced."
+ "Bootstrap user exists."
+ "Device is on seed build. Skip the random delay"
+ "Enrollment authentication info: %{public}@"
+ "Failed to create bootstrap token with error: %{public}@"
+ "Failed to generate LAContext for bootstrap token"
+ "Failed to generate token data context"
+ "Failed to get lastSyncedEligibility with error: %{public}@"
+ "Failed to set credential for context"
+ "Failed to set lastSyncedEligibility with error: %{public}@"
+ "Failed to sync bootstrap token with error: %{public}@"
+ "LastSyncedEligibility"
+ "MDMDEPPushTokenManager: DEP push token sync is not necessary."
+ "MDMDEPPushTokenManager: Nothing has changed since last sync"
+ "MDMDEPPushTokenManager: Syncing DEP push token... reason: \"%{public}@\", eligible for migration: %d"
+ "MDMDEPPushTokenManager: _scheduleAppTokenSync schedule forced sync due to deadline"
+ "MDMDEPPushTokenManager: _scheduleAppTokenSync schedule sync with random delay due to no deadline"
+ "MDMDEPPushTokenManager: migration eligibility might have changed, will check if we need to sync push token again..."
+ "MDMMigrationManager: Retry retrieving cloud config..."
+ "MDMMigrationManager: Sending EndMigrationRequest"
+ "MDMMigrationManager: Stop monitoring DEP push notification"
+ "MDMServerCore failed to clear test nag cloud config with error: %{public}@"
+ "MDMServerCore failed to store test nag cloud config with error: %{public}@"
+ "MKBKeyBagCopyData finished with result: %d %@"
+ "MKBKeyBagCreateEscrowWithACM finished with result: %d"
+ "Migration eligibility changed"
+ "No bootstrap token was created. Continue..."
+ "Push token received"
+ "Push token sync failed"
+ "Task %s hasn't finished within %.1f seconds"
+ "_cancelMDMMigrationWithNewCloudConfig:"
+ "_createServerMissingBootstrapTokenCapabilityError"
+ "_generateBootstrapTokenContextFailed"
+ "_handleNewCloudConfigIfNeeded:currentCloudConfig:didPollFromDEP:"
+ "_migrationEligibilityChanged"
+ "_queue_isSyncNeededWithAppToken:eligibleForMigration:shouldForce:"
+ "_queue_lastSyncedEligibility"
+ "_queue_retryPushTokenSync"
+ "_queue_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:reason:"
+ "_queue_scheduleAppTokenSync"
+ "_queue_scheduleMandatoryDEPPushTokenSyncWithDelay:reason:isRetry:"
+ "_queue_setLastSyncedEligibility:"
+ "_queue_startMonitoringDEPPushTokenChange"
+ "_queue_syncPushTokenShouldForce:shouldScheduleRetry:reason:backgroundTask:completionHandler:"
+ "_retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:"
+ "_scheduleMDMMigrationWithNewCloudConfigDetails:"
+ "_shouldMigrateWithNewCloudConfig:currentCloudConfig:isEligible:isMigrationNeeded:"
+ "_stackshot.ips"
+ "checkBootstrapUserExistsWithError failed with error: %{public}@."
+ "createBootstrapUserWithTokenInACMCredential:withDevicePasscodeInACMCredential:withError:"
+ "currentEnrollmentStateSupportsMigration"
+ "ddr_erase_device"
+ "ddr_erase_device_queue"
+ "deleteBootstrapTokenWithToken:devicePasscodeContext:completionHandler:"
+ "deleteBootstrapTokenWithTokenContext:devicePasscodeContext:completionHandler:"
+ "deleteBootstrapUserWithTokenInACMCredential:withDevicePasscodeInACMCredential:withError:"
+ "dumpStackshotToPath:fileName:"
+ "expensiveItems"
+ "externalizedContext"
+ "generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:"
+ "generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:"
+ "generateBootstrapTokenWithDevicePasscodeContext:completionHandler:"
+ "imei"
+ "isDeviceEligibleForMigrationWithExistingCloudConfig:outReason:"
+ "isMigrationEligibilityReportEnabled"
+ "makeEndMigrationRequestIfNeededWithCloudConfig:success:completionHandler:"
+ "meid"
+ "nagWithCloudConfigDetails:"
+ "removeObserver:name:object:"
+ "rundmc.MDMMigration.Nag"
+ "scheduleMandatoryDEPPushTokenSyncWithRandomDelay called"
+ "schedulePeriodicMandatoryDEPPushTokenSync called"
+ "setCredential:type:"
+ "startMonitoringDEPServerPushIfNeeded"
+ "stopMonitoringDEPServerPush"
+ "stringByAppendingString:"
+ "syncDEPPushToken:pushTopic:eligibleForMigration:eligibilityDescription:completionBlock:"
+ "syncDEPPushTokenWithDelay:completion: called"
+ "v32@0:8@\"NSData\"16@?<v@?B@\"NSError\">24"
+ "v36@0:8d16@24B32"
+ "v44@0:8d16B24B28B32@36"
+ "v48@0:8B16B20@24@32@?40"
+ "validateBootstrapTokenContext:error:"
+ "validateBootstrapUserWithTokenInACMCredential:withError:"
- "-[MDMServerCore nagForMigrationWithHardCodedValuesWithCompletion:]"
- "-[MDMServerCore stopNaggingForMigrationWithCompletion:]"
- "MDMDEPPushTokenManager: Push token has been synced."
- "MDMDEPPushTokenManager: Syncing DEP push token..."
- "MDMMigrationManager: Device has incomplete MDM enrollment!"
- "MDMMigrationManager: Device has incomplete migration!"
- "MDMMigrationManager: Device is not DEP enrolled."
- "MDMMigrationManager: Device is not MDM enrolled."
- "MDMMigrationManager: Migration from non DEP enrolled device is not supported"
- "_cancelMDMMigrationIfNeededWithNewCloudConfig:currentCloudConfig:"
- "_handleNewCloudConfigIfNeeded:currentCloudConfig:"
- "_isDeviceDEPEnrolled"
- "_queue_appTokenNeedsToBeSynced"
- "_retryPushTokenSync"
- "_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:"
- "_scheduleAppTokenSync"
- "_scheduleMDMMigrationProcessWithNewCloudConfig:"
- "_scheduleMandatoryDEPPushTokenSyncWithDelay:"
- "_shouldMigrateWithNewCloudConfig:currentCloudConfig:"
- "_startMonitoringDEPPushTokenChange"
- "_syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:"
- "createBootstrapUserWithToken:withDevicePasscode:withError:"
- "data"
- "deleteBootstrapUserWithToken:withDevicePasscode:withError:"
- "isADEProfile"
- "isDEPPushEnabled"
- "isMigrationSupportedWithExistingCloudConfig:"
- "isStoredProfileInstalled"
- "nagWithCloudConfig:"
- "startMonitoringDEPServerPush"
- "syncDEPPushToken:pushTopic:completionBlock:"
- "v36@0:8d16B24B28B32"
- "v40@0:8B16B20@24@?32"
- "validateBootstrapUserWithToken:withError:"

```
