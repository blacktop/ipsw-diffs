## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-55.80.4.0.0
-  __TEXT.__text: 0x55ca4
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x4194
+59.100.16.0.0
+  __TEXT.__text: 0x59540
+  __TEXT.__auth_stubs: 0xf10
+  __TEXT.__objc_methlist: 0x41cc
   __TEXT.__const: 0x1aa
-  __TEXT.__gcc_except_tab: 0x1130
-  __TEXT.__cstring: 0x55a2
-  __TEXT.__oslogstring: 0x6ccc
+  __TEXT.__gcc_except_tab: 0x10b4
+  __TEXT.__cstring: 0x56d9
+  __TEXT.__oslogstring: 0x6e76
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
-  __TEXT.__unwind_info: 0x1210
+  __TEXT.__unwind_info: 0x1450
   __TEXT.__eh_frame: 0x178
-  __TEXT.__objc_classname: 0x6c4
-  __TEXT.__objc_methname: 0xeb2a
-  __TEXT.__objc_methtype: 0x1b90
-  __TEXT.__objc_stubs: 0xb980
-  __DATA_CONST.__got: 0x11a8
-  __DATA_CONST.__const: 0x1ec8
+  __TEXT.__objc_classname: 0x6e3
+  __TEXT.__objc_methname: 0xedc4
+  __TEXT.__objc_methtype: 0x1b8a
+  __TEXT.__objc_stubs: 0xbb20
+  __DATA_CONST.__got: 0x11d0
+  __DATA_CONST.__const: 0x1f10
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3490
+  __DATA_CONST.__objc_selrefs: 0x34d8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x5f0
-  __AUTH_CONST.__cfstring: 0x50a0
-  __AUTH_CONST.__objc_const: 0x6a40
+  __AUTH_CONST.__auth_got: 0x798
+  __AUTH_CONST.__const: 0x610
+  __AUTH_CONST.__cfstring: 0x5140
+  __AUTH_CONST.__objc_const: 0x6a90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH.__objc_data: 0xe80
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x294
+  __DATA.__objc_ivar: 0x29c
   __DATA.__data: 0x7f0
   __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D38B8F6F-99F1-37B1-AB64-287B07D7AA42
-  Functions: 1646
-  Symbols:   6652
-  CStrings:  4264
+  UUID: F35839F0-A46D-30CF-80CA-49B4463B790C
+  Functions: 1660
+  Symbols:   6701
+  CStrings:  4294
 
Symbols:
+ +[MDMBootstrapTokenUtilities _generateBootstrapTokenVerificationFailedErrorWithUnderlayingError:]
+ +[MDMRequestEraseDeviceCommand_ReturnToService buildWithEnabled:wiFiProfileData:mdmProfileData:bootstrapToken:shouldRetryEnrollment:]
+ +[MDMReturnToServiceUtilities triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:bootstrapToken:shouldRetryEnrollment:preObliterationAction:completionHandler:]
+ +[MDMReturnToServiceUtilities triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:preObliterationAction:completionHandler:]
+ -[MDMRequestEraseDeviceCommand_ReturnToService commandShouldRetryEnrollment]
+ -[MDMRequestEraseDeviceCommand_ReturnToService setCommandShouldRetryEnrollment:]
+ -[MDMServerCore _memberQueueEvaluateSessionTimeoutForRRTS]
+ -[MDMServerCore configuredTimeoutInterval]
+ -[MDMServerCore handleXPCStream]
+ -[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:]
+ -[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:].cold.1
+ -[MDMServerCore rrtsScheduledIdleTimeout]
+ -[MDMServerCore setConfiguredTimeoutInterval:]
+ -[MDMServerCore setRrtsScheduledIdleTimeout:]
+ -[MDMServicerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:]
+ GCC_except_table139
+ GCC_except_table159
+ GCC_except_table162
+ GCC_except_table168
+ GCC_except_table17
+ GCC_except_table172
+ GCC_except_table179
+ GCC_except_table185
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table212
+ GCC_except_table22
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table249
+ GCC_except_table279
+ GCC_except_table286
+ GCC_except_table297
+ GCC_except_table308
+ GCC_except_table31
+ GCC_except_table319
+ GCC_except_table323
+ GCC_except_table334
+ GCC_except_table338
+ GCC_except_table354
+ GCC_except_table43
+ GCC_except_table48
+ GCC_except_table73
+ GCC_except_table87
+ _DMCSessionTimeoutChangedNotification
+ _OBJC_CLASS_$_DMCSnapshotUtilities
+ _OBJC_CLASS_$_DMFFetchAppsResultObject
+ _OBJC_IVAR_$_MDMRequestEraseDeviceCommand_ReturnToService._commandShouldRetryEnrollment
+ _OBJC_IVAR_$_MDMServerCore._configuredTimeoutInterval
+ _OBJC_IVAR_$_MDMServerCore._rrtsScheduledIdleTimeout
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1358
+ ___202-[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:]_block_invoke
+ ___202-[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:]_block_invoke_2
+ ___31-[MDMServerCore setMDMOptions:]_block_invoke.275
+ ___31-[MDMServerCore setMDMOptions:]_block_invoke_2.277
+ ___32-[MDMServerCore handleXPCStream]_block_invoke
+ ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.150
+ ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.155
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1207
+ ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1208
+ ___47-[MDMServerCore _memberQueueRRTSTimeoutReached]_block_invoke.372
+ ___48-[MDMServerCore blockMDMCommandsWithCompletion:]_block_invoke.192
+ ___50-[MDMServerCore unblockMDMCommandsWithCompletion:]_block_invoke.193
+ ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1503
+ ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.278
+ ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.315
+ ___63-[MDMServerCore _memberQueueStartListeningForInterestingEvents]_block_invoke_3
+ ___63-[MDMServerCore _memberQueueStartListeningForInterestingEvents]_block_invoke_4
+ ___66-[MDMServerCore nagForMigrationWithHardCodedValuesWithCompletion:]_block_invoke_2.173
+ ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.986
+ ___68-[MDMServerCore syncBootstrapTokenToMDMWithToken:completionHandler:]_block_invoke.180
+ ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.122
+ ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke.301
+ ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke_2.302
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.102
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.108
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.109
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.113
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.182
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.183
+ ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.184
+ ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.306
+ ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.308
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.100
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.81
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.82
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.89
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke_2.93
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.186
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.187
+ ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.188
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
+ ___block_descriptor_48_e8_32bs40bs_e59_v52?0B8"NSData"12"NSData"20"NSData"28B36B40"NSError"44ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e20_v24?08"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_75_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1054
+ ___block_literal_global.1099
+ ___block_literal_global.1116
+ ___block_literal_global.1203
+ ___block_literal_global.1205
+ ___block_literal_global.1217
+ ___block_literal_global.1382
+ ___block_literal_global.1384
+ ___block_literal_global.1422
+ ___block_literal_global.1427
+ ___block_literal_global.1494
+ ___block_literal_global.158
+ ___block_literal_global.195
+ ___block_literal_global.318
+ ___block_literal_global.374
+ ___block_literal_global.385
+ ___block_literal_global.955
+ ___block_literal_global.957
+ ___block_literal_global.959
+ ___block_literal_global.966
+ __xpc_event_key_name
+ _kMDMPQueryAuthenticatedTemporarySession
+ _kMDMPQueryDirectUserSwitch
+ _objc_msgSend$_generateBootstrapTokenVerificationFailedErrorWithUnderlayingError:
+ _objc_msgSend$_memberQueueEvaluateSessionTimeoutForRRTS
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$authenticatedTemporarySession
+ _objc_msgSend$commandShouldRetryEnrollment
+ _objc_msgSend$configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:
+ _objc_msgSend$configuredTimeoutInterval
+ _objc_msgSend$directUserSwitch
+ _objc_msgSend$handleXPCStream
+ _objc_msgSend$hasSystemVolumeSnapshotWithName:
+ _objc_msgSend$init
+ _objc_msgSend$initWithAppsByBundleIdentifier:
+ _objc_msgSend$isAuthenticatedTemporarySessionEnabled
+ _objc_msgSend$preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:shouldRetryEnrollment:error:
+ _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:
+ _objc_msgSend$rrtsScheduledIdleTimeout
+ _objc_msgSend$setCommandShouldRetryEnrollment:
+ _objc_msgSend$setConfiguredTimeoutInterval:
+ _objc_msgSend$setRrtsScheduledIdleTimeout:
+ _objc_msgSend$triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:bootstrapToken:shouldRetryEnrollment:preObliterationAction:completionHandler:
+ _objc_msgSend$triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:preObliterationAction:completionHandler:
+ _objc_msgSend$userActivityHandle
+ _xpc_dictionary_get_string
+ _xpc_set_event_stream_handler
- +[MDMRequestEraseDeviceCommand_ReturnToService buildWithEnabled:wiFiProfileData:mdmProfileData:bootstrapToken:]
- +[MDMReturnToServiceUtilities triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:bootstrapToken:preObliterationAction:completionHandler:]
- +[MDMReturnToServiceUtilities triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:preObliterationAction:completionHandler:]
- -[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]
- -[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:].cold.1
- -[MDMServerCore rrtsIdleTimeout]
- -[MDMServerCore setRrtsIdleTimeout:]
- -[MDMServicerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]
- GCC_except_table12
- GCC_except_table137
- GCC_except_table15
- GCC_except_table157
- GCC_except_table160
- GCC_except_table166
- GCC_except_table170
- GCC_except_table177
- GCC_except_table183
- GCC_except_table186
- GCC_except_table189
- GCC_except_table202
- GCC_except_table205
- GCC_except_table210
- GCC_except_table226
- GCC_except_table236
- GCC_except_table274
- GCC_except_table281
- GCC_except_table29
- GCC_except_table292
- GCC_except_table303
- GCC_except_table314
- GCC_except_table318
- GCC_except_table329
- GCC_except_table333
- GCC_except_table349
- GCC_except_table41
- GCC_except_table46
- GCC_except_table71
- GCC_except_table85
- _OBJC_IVAR_$_MDMServerCore._rrtsIdleTimeout
- ___180-[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]_block_invoke
- ___180-[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]_block_invoke_2
- ___184-[MDMParser _performInstallApplicationRequestWithManifestURL:iTunesStoreIDObj:bundleId:flagsObj:attributes:configuration:manageChangeStr:purchaseMethodValue:personaID:completionBlock:]_block_invoke.1352
- ___31-[MDMServerCore setMDMOptions:]_block_invoke.271
- ___31-[MDMServerCore setMDMOptions:]_block_invoke_2.273
- ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.148
- ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.153
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1201
- ___44-[MDMParser _performSetDefaultApplications:]_block_invoke.1202
- ___47-[MDMServerCore _memberQueueRRTSTimeoutReached]_block_invoke.367
- ___48-[MDMServerCore blockMDMCommandsWithCompletion:]_block_invoke.188
- ___50-[MDMServerCore unblockMDMCommandsWithCompletion:]_block_invoke.189
- ___53-[MDMParser _installMedia:assertion:completionBlock:]_block_invoke.1497
- ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.274
- ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.311
- ___66-[MDMServerCore nagForMigrationWithHardCodedValuesWithCompletion:]_block_invoke_2.169
- ___68-[MDMParser _processRequest:accessRights:assertion:completionBlock:]_block_invoke.980
- ___68-[MDMServerCore syncBootstrapTokenToMDMWithToken:completionHandler:]_block_invoke.176
- ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.120
- ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke.297
- ___73-[MDMServerCore pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke_2.298
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.105
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.99
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.106
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.111
- ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.178
- ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.179
- ___83-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscode:completionHandler:]_block_invoke.180
- ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.302
- ___83-[MDMServerCore pushServiceManager:didReceiveMessageForTopic:userInfo:environment:]_block_invoke.304
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.78
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.79
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.86
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.97
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke_2.90
- ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.182
- ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.183
- ___90-[MDMServerCore generateAndSyncBootstrapTokenWithDevicePasscodeContext:completionHandler:]_block_invoke.184
- ___block_descriptor_48_e8_32bs40bs_e53_v44?0B8"NSData"12"NSData"20"NSData"28"NSError"36ls32l8s40l8
- ___block_descriptor_56_e8_32s40r_e20_v24?08"NSError"16lr40l8s32l8
- ___block_descriptor_74_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1048
- ___block_literal_global.1092
- ___block_literal_global.1109
- ___block_literal_global.1197
- ___block_literal_global.1199
- ___block_literal_global.1211
- ___block_literal_global.1376
- ___block_literal_global.1378
- ___block_literal_global.1416
- ___block_literal_global.1421
- ___block_literal_global.1488
- ___block_literal_global.191
- ___block_literal_global.314
- ___block_literal_global.369
- ___block_literal_global.380
- ___block_literal_global.945
- ___block_literal_global.947
- ___block_literal_global.949
- ___block_literal_global.960
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:preferenceDomain:
- _objc_msgSend$initWithName:reason:userInfo:
- _objc_msgSend$preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:
- _objc_msgSend$raise
- _objc_msgSend$requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:
- _objc_msgSend$rrtsIdleTimeout
- _objc_msgSend$setRrtsIdleTimeout:
- _objc_msgSend$triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:bootstrapToken:preObliterationAction:completionHandler:
- _objc_msgSend$triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:preObliterationAction:completionHandler:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x5
- _objc_retain_x6
CStrings:
+ "-[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:]"
+ "/Library/Caches/com.apple.xbs/8034402B-B4E4-48BD-9085-738E874DF78C/TemporaryDirectory.cSTShA/Sources/DeviceManagementClientTools/DeviceManagementClientTools/MDM Framework/Parsers/MDMAbstractTunnelParser.m"
+ "/Library/Caches/com.apple.xbs/8034402B-B4E4-48BD-9085-738E874DF78C/TemporaryDirectory.cSTShA/Sources/DeviceManagementClientTools/DeviceManagementClientTools/MDM Framework/Utilities/MDMServerCore.m"
+ "AuthenticatedTemporarySession"
+ "Bootstrap token verification failed with error: %{public}@"
+ "Configured timeout interval has changed. old: %f, new: %f"
+ "Creating empty result object for fetched response."
+ "DMFFetchAppsResultObject is nil with error: %{public}@."
+ "Device has an idle timeout task scheduled already. Avoid scheduling a new one."
+ "Device is on seed build. Skip the random delay"
+ "DirectUserSwitch"
+ "MDM_BOOTSTRAP_ERROR_FAILED_TO_VERIFY"
+ "Received %{public}@ notification from notifyd"
+ "ShouldRetryEnrollment"
+ "System Snapshot Exists"
+ "System snapshot doesn't exist"
+ "T@\"NSNumber\",C,N,V_commandShouldRetryEnrollment"
+ "Td,N,V_configuredTimeoutInterval"
+ "Td,N,V_rrtsScheduledIdleTimeout"
+ "_commandShouldRetryEnrollment"
+ "_configuredTimeoutInterval"
+ "_generateBootstrapTokenVerificationFailedErrorWithUnderlayingError:"
+ "_memberQueueEvaluateSessionTimeoutForRRTS"
+ "_rrtsScheduledIdleTimeout"
+ "addObserverForName:object:queue:usingBlock:"
+ "authenticatedTemporarySession"
+ "buildWithEnabled:wiFiProfileData:mdmProfileData:bootstrapToken:shouldRetryEnrollment:"
+ "com.apple.notifyd.matching"
+ "commandShouldRetryEnrollment"
+ "configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:directUserSwitch:authenticatedTemporarySession:preferenceDomain:"
+ "configuredTimeoutInterval"
+ "directUserSwitch"
+ "handleXPCStream"
+ "hasSystemVolumeSnapshotWithName:"
+ "initWithAppsByBundleIdentifier:"
+ "isAuthenticatedTemporarySessionEnabled"
+ "preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:shouldRetryEnrollment:error:"
+ "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:completionHandler:"
+ "rrtsScheduledIdleTimeout"
+ "setCommandShouldRetryEnrollment:"
+ "setConfiguredTimeoutInterval:"
+ "setRrtsScheduledIdleTimeout:"
+ "triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:bootstrapToken:shouldRetryEnrollment:preObliterationAction:completionHandler:"
+ "triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:shouldRetryEnrollment:preObliterationAction:completionHandler:"
+ "v16@?0@\"NSNotification\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"BB@\"NSError\">16"
+ "v52@?0B8@\"NSData\"12@\"NSData\"20@\"NSData\"28B36B40@\"NSError\"44"
+ "v68@0:8B16B20@\"NSData\"24@\"NSData\"32@\"NSString\"40@\"NSData\"48B56@?<v@?@\"NSError\">60"
+ "v68@0:8B16B20@24@32@40@48B56@?60"
+ "v68@0:8B16B20@24@32@40B48@?52@?60"
+ "v76@0:8B16B20@24@32@40@48B56@?60@?68"
- "-[MDMServerCore requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:]"
- "/Library/Caches/com.apple.xbs/Sources/DeviceManagementClientTools/DeviceManagementClientTools/MDM Framework/Parsers/MDMAbstractTunnelParser.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceManagementClientTools/DeviceManagementClientTools/MDM Framework/Utilities/MDMServerCore.m"
- "@48@0:8@16@24@32@40"
- "Td,N,V_rrtsIdleTimeout"
- "_rrtsIdleTimeout"
- "buildWithEnabled:wiFiProfileData:mdmProfileData:bootstrapToken:"
- "configureTemporarySessionOnly:useDynamicQuotaSize:restoreQuotaSizeWhenDisabled:preferenceDomain:"
- "initWithName:reason:userInfo:"
- "manager:didFailVerificationWithError:"
- "managerDidFinishVerification:"
- "preseveReturnToServiceDataWithMDMProfileData:wifiProfileData:additionalDetails:error:"
- "raise"
- "request for app items failed: %@"
- "requestReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:completionHandler:"
- "rrtsIdleTimeout"
- "setRrtsIdleTimeout:"
- "triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:bootstrapToken:preObliterationAction:completionHandler:"
- "triggerReturnToServiceObliterationWithPreserveDataPlan:disallowProximitySetup:mdmProfileData:wifiProfileData:revertToSnapshotName:bootstrapToken:preObliterationAction:completionHandler:"
- "v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSData\"@\"NSError\">16"
- "v44@?0B8@\"NSData\"12@\"NSData\"20@\"NSData\"28@\"NSError\"36"
- "v64@0:8B16B20@\"NSData\"24@\"NSData\"32@\"NSString\"40@\"NSData\"48@?<v@?@\"NSError\">56"
- "v64@0:8B16B20@24@32@40@48@?56"
- "v64@0:8B16B20@24@32@40@?48@?56"
- "v72@0:8B16B20@24@32@40@48@?56@?64"

```
