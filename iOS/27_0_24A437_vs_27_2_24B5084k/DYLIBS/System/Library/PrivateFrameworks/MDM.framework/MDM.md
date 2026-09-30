## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-113.2.5.0.0
-  __TEXT.__text: 0x53b24
-  __TEXT.__objc_methlist: 0x42d4
+113.40.17.0.0
+  __TEXT.__text: 0x548e4
+  __TEXT.__objc_methlist: 0x43d4
   __TEXT.__const: 0x1c2
-  __TEXT.__gcc_except_tab: 0xf08
-  __TEXT.__cstring: 0x532d
-  __TEXT.__oslogstring: 0x70a5
+  __TEXT.__gcc_except_tab: 0xf34
+  __TEXT.__cstring: 0x5439
+  __TEXT.__oslogstring: 0x727e
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x1870
+  __TEXT.__unwind_info: 0x18c0
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3478
+  __DATA_CONST.__objc_selrefs: 0x34f0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__got: 0x1230
+  __DATA_CONST.__got: 0x11f8
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x4bc0
-  __AUTH_CONST.__objc_const: 0x6c58
+  __AUTH_CONST.__cfstring: 0x4c40
+  __AUTH_CONST.__objc_const: 0x6dd0
   __AUTH_CONST.__objc_arrayobj: 0x8d0
   __AUTH_CONST.__objc_intobj: 0x660
-  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__auth_got: 0x7e8
   __AUTH.__objc_data: 0x638
-  __DATA.__objc_ivar: 0x2ac
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x7f0
   __DATA_DIRTY.__objc_data: 0xa28
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1687
-  Symbols:   4897
-  CStrings:  1271
+  Functions: 1718
+  Symbols:   4941
+  CStrings:  1282
 
Symbols:
+ -[MDMMigrationManager _isDeviceEligibleForMigration]
+ -[MDMMigrationManager _queue_clearConfigFetchRetryState]
+ -[MDMMigrationManager _queue_isConfigFetchPending]
+ -[MDMMigrationManager _queue_retryConfigFetchFromReason:backgroundTask:]
+ -[MDMMigrationManager _queue_scheduleConfigFetchRetry]
+ -[MDMMigrationManager _queue_setConfigFetchPending:]
+ -[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithCompletionHandler:]
+ -[MDMMigrationManager configFetchPending]
+ -[MDMMigrationManager configFetchRetryInterval]
+ -[MDMMigrationManager configFetchRetryTask]
+ -[MDMMigrationManager initWithNetworkMonitor:]
+ -[MDMMigrationManager isFetchingConfig]
+ -[MDMMigrationManager networkMonitor]
+ -[MDMMigrationManager retryInfoPlist]
+ -[MDMMigrationManager setConfigFetchPending:]
+ -[MDMMigrationManager setConfigFetchRetryInterval:]
+ -[MDMMigrationManager setConfigFetchRetryTask:]
+ -[MDMMigrationManager setIsFetchingConfig:]
+ -[MDMMigrationManager setNetworkMonitor:]
+ -[MDMMigrationManager setRetryInfoPlist:]
+ -[MDMMigrationManager setWorkerQueue:]
+ -[MDMMigrationManager workerQueue]
+ -[MDMServerCore _errorFromTransaction:assertion:rmAccountID:enrollmentMode:reauthQueue:outHandling:]
+ -[MDMServerCore _executionQueueErrorFromTransactionHandlingError:assertion:rmAccountID:enrollmentMode:reauthQueue:]
+ -[MDMServerCore _processAccountDrivenUnauthorizedFromTransaction:rmAccountID:reauthQueue:outHandling:]
+ -[MDMServerCore _processUnauthorizedFromTransaction:authParams:rmAccountID:rmAccountUsername:reauthQueue:outHandling:]
+ -[MDMServerCore _triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:outHandling:]
+ -[MDMServerCore executeDeclarativeManagementRequestForEndpoint:requestData:completion:]
+ -[MDMServicerCore executeDeclarativeManagementRequestForEndpoint:requestData:completion:]
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table25
+ GCC_except_table258
+ GCC_except_table292
+ GCC_except_table299
+ GCC_except_table310
+ GCC_except_table323
+ GCC_except_table335
+ GCC_except_table339
+ GCC_except_table350
+ GCC_except_table354
+ GCC_except_table37
+ GCC_except_table370
+ _DMCMigrationErrorDomain
+ _MDMMigrationConfigFetchRetryInfoFilePath
+ _MDMShouldAllowEscrowCreationForPasscode
+ _OBJC_CLASS_$_DMCDeviceEligibility
+ _OBJC_IVAR_$_MDMMigrationManager._configFetchPending
+ _OBJC_IVAR_$_MDMMigrationManager._configFetchRetryInterval
+ _OBJC_IVAR_$_MDMMigrationManager._configFetchRetryTask
+ _OBJC_IVAR_$_MDMMigrationManager._isFetchingConfig
+ _OBJC_IVAR_$_MDMMigrationManager._networkMonitor
+ _OBJC_IVAR_$_MDMMigrationManager._retryInfoPlist
+ _OBJC_IVAR_$_MDMMigrationManager._workerQueue
+ ___100-[MDMServerCore _errorFromTransaction:assertion:rmAccountID:enrollmentMode:reauthQueue:outHandling:]_block_invoke
+ ___100-[MDMServerCore _errorFromTransaction:assertion:rmAccountID:enrollmentMode:reauthQueue:outHandling:]_block_invoke_2
+ ___131-[MDMServerCore _triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:outHandling:]_block_invoke
+ ___131-[MDMServerCore _triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:outHandling:]_block_invoke_2
+ ___131-[MDMServerCore _triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:outHandling:]_block_invoke_3
+ ___50-[MDMMigrationManager stopMonitoringDEPServerPush]_block_invoke
+ ___54-[MDMMigrationManager _queue_scheduleConfigFetchRetry]_block_invoke
+ ___59-[MDMMigrationManager startMonitoringDEPServerPushIfNeeded]_block_invoke
+ ___59-[MDMMigrationManager startMonitoringDEPServerPushIfNeeded]_block_invoke_2
+ ___87-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithCompletionHandler:]_block_invoke
+ ___87-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithCompletionHandler:]_block_invoke_2
+ ___87-[MDMServerCore executeDeclarativeManagementRequestForEndpoint:requestData:completion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ _kMDMDataKey
+ _kMDMEndpointKey
+ _kMDMMessageTypeDeclarativeManagement
+ _objc_msgSend$_errorFromTransaction:assertion:rmAccountID:enrollmentMode:reauthQueue:outHandling:
+ _objc_msgSend$_executionQueueErrorFromTransactionHandlingError:assertion:rmAccountID:enrollmentMode:reauthQueue:
+ _objc_msgSend$_isDeviceEligibleForMigration
+ _objc_msgSend$_processAccountDrivenUnauthorizedFromTransaction:rmAccountID:reauthQueue:outHandling:
+ _objc_msgSend$_processUnauthorizedFromTransaction:authParams:rmAccountID:rmAccountUsername:reauthQueue:outHandling:
+ _objc_msgSend$_queue_clearConfigFetchRetryState
+ _objc_msgSend$_queue_isConfigFetchPending
+ _objc_msgSend$_queue_retryConfigFetchFromReason:backgroundTask:
+ _objc_msgSend$_queue_scheduleConfigFetchRetry
+ _objc_msgSend$_queue_setConfigFetchPending:
+ _objc_msgSend$_retrieveAndStorePendingCloudConfigurationWithCompletionHandler:
+ _objc_msgSend$_triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:outHandling:
+ _objc_msgSend$configFetchPending
+ _objc_msgSend$configFetchRetryInterval
+ _objc_msgSend$configFetchRetryTask
+ _objc_msgSend$executeDeclarativeManagementRequestForEndpoint:requestData:completion:
+ _objc_msgSend$initWithNetworkMonitor:
+ _objc_msgSend$isEligibleForNoninteractiveEnhancedLogCollection
+ _objc_msgSend$isFetchingConfig
+ _objc_msgSend$responseFromTransaction:
+ _objc_msgSend$retryInfoPlist
+ _objc_msgSend$setConfigFetchPending:
+ _objc_msgSend$setConfigFetchRetryInterval:
+ _objc_msgSend$setConfigFetchRetryTask:
+ _objc_msgSend$setIsFetchingConfig:
- -[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]
- -[MDMMigrationManager init]
- -[MDMRequestTriggerEnhancedLogCollectionCommand(Handler) _areAccountsPresentWithAccountTypeIdentifiers:]
- -[MDMRequestTriggerEnhancedLogCollectionCommand(Handler) _isDeviceWithoutUserData]
- -[MDMRequestTriggerEnhancedLogCollectionCommand(Handler) _isPasscodePresent]
- -[MDMServerCore _httpErrorFromTransaction:assertion:rmAccountID:enrollmentMode:reauthQueue:]
- -[MDMServerCore _processAccountDrivenUnauthorizedFromTransaction:rmAccountID:reauthQueue:]
- -[MDMServerCore _processUnauthorizedFromTransaction:authParams:rmAccountID:rmAccountUsername:reauthQueue:]
- -[MDMServerCore _triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:]
- -[MDMUserParser _originator]
- GCC_except_table227
- GCC_except_table232
- GCC_except_table24
- GCC_except_table253
- GCC_except_table287
- GCC_except_table294
- GCC_except_table305
- GCC_except_table318
- GCC_except_table329
- GCC_except_table333
- GCC_except_table344
- GCC_except_table348
- GCC_except_table36
- GCC_except_table364
- _ACAccountTypeIdentifierAppleAccount
- _ACAccountTypeIdentifierCalDAV
- _ACAccountTypeIdentifierCardDAV
- _ACAccountTypeIdentifierExchange
- _ACAccountTypeIdentifierGmail
- _ACAccountTypeIdentifierHotmail
- _ACAccountTypeIdentifierIMAP
- _ACAccountTypeIdentifierIMAPMail
- _ACAccountTypeIdentifierIMAPNotes
- _ACAccountTypeIdentifierPOP
- _ACAccountTypeIdentifierYahoo
- _ACAccountTypeIdentifieriTunesStore
- ___119-[MDMServerCore _triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:]_block_invoke
- ___119-[MDMServerCore _triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:]_block_invoke_2
- ___95-[MDMServerCore _sendCheckInRequestAndHandleErrorForMessageType:requestDict:completionHandler:]_block_invoke_3
- ___98-[MDMMigrationManager _retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:]_block_invoke
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8
- ___block_descriptor_56_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- _objc_msgSend$_areAccountsPresentWithAccountTypeIdentifiers:
- _objc_msgSend$_httpErrorFromTransaction:assertion:rmAccountID:enrollmentMode:reauthQueue:
- _objc_msgSend$_isDeviceWithoutUserData
- _objc_msgSend$_isPasscodePresent
- _objc_msgSend$_processAccountDrivenUnauthorizedFromTransaction:rmAccountID:reauthQueue:
- _objc_msgSend$_processUnauthorizedFromTransaction:authParams:rmAccountID:rmAccountUsername:reauthQueue:
- _objc_msgSend$_retrieveAndStorePendingCloudConfigurationWithRetryCount:completionHandler:
- _objc_msgSend$_triggerRefreshTokenForTransaction:authenticator:authParams:rmAccountID:rmAccountUsername:reauthQueue:
- _objc_msgSend$accountType
- _objc_msgSend$accountsWithAccountTypeIdentifiers:error:
- _objc_msgSend$ams_isLocalAccount
CStrings:
+ "-[MDMServerCore executeDeclarativeManagementRequestForEndpoint:requestData:completion:]"
+ "A cloud config fetch is already in progress"
+ "Device is on seed build. Skip the random delay"
+ "MDMMigrationManager: A cloud config fetch is still pending, re-attempting when network is available"
+ "MDMMigrationManager: Cloud config fetch already in progress, coalescing"
+ "MDMMigrationManager: Cloud config fetch already in progress, skipping retry (%{public}@)"
+ "MDMMigrationManager: Device no longer eligible for migration, stopping cloud config fetch retry"
+ "MDMMigrationManager: Failed to read pending config fetch flag with error: %{public}@"
+ "MDMMigrationManager: Failed to write pending config fetch flag with error: %{public}@"
+ "MDMMigrationManager: Retrying cloud config fetch (%{public}@)"
+ "MDMMigrationManager: Scheduling cloud config fetch retry after %.1f seconds"
+ "MDMMigrationManager_worker_queue"
+ "Pending fetch on daemon start"
+ "PendingConfigFetchNeeded"
+ "Scheduled retry"
+ "com.apple.mdmd.MDMMigrationManager.configFetchRetry"
- "Account found - Type: %{public}@, Username: %{private}@, Description: %{private}@"
- "Checking for accounts with type identifiers: %{public}@"
- "Failed to fetch accounts with error: %{public}@"
- "MDMMigrationManager: Retry retrieving cloud config..."
- "ORGANIZATION_QUOTED_%@"
```
