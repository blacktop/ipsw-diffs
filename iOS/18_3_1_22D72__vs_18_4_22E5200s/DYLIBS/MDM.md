## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x44c1c
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x2f88
-  __TEXT.__const: 0x108
-  __TEXT.__gcc_except_tab: 0xf80
-  __TEXT.__cstring: 0x4427
-  __TEXT.__oslogstring: 0x4cff
+20.4.13.0.0
+  __TEXT.__text: 0x47c6c
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x399c
+  __TEXT.__const: 0x138
+  __TEXT.__gcc_except_tab: 0x10f0
+  __TEXT.__cstring: 0x45b6
+  __TEXT.__oslogstring: 0x5553
   __TEXT.__dlopen_cstrs: 0x55
-  __TEXT.__unwind_info: 0xed8
-  __TEXT.__objc_classname: 0x61d
-  __TEXT.__objc_methname: 0xc482
-  __TEXT.__objc_methtype: 0x1666
-  __TEXT.__objc_stubs: 0xa260
-  __DATA_CONST.__got: 0x1000
-  __DATA_CONST.__const: 0x1988
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__unwind_info: 0xf98
+  __TEXT.__objc_classname: 0x640
+  __TEXT.__objc_methname: 0xcce7
+  __TEXT.__objc_methtype: 0x16d3
+  __TEXT.__objc_stubs: 0xa920
+  __DATA_CONST.__got: 0x1040
+  __DATA_CONST.__const: 0x1a20
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b90
+  __DATA_CONST.__objc_selrefs: 0x2ff0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0x6668
+  __AUTH_CONST.__cfstring: 0x4ac0
+  __AUTH_CONST.__objc_const: 0x5cd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0xf0
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0x238
+  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH.__objc_data: 0xdc0
+  __DATA.__objc_ivar: 0x268
   __DATA.__data: 0x6c0
   __DATA.__bss: 0x1f8
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/Catalyst.framework/Catalyst

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 1293
-  Symbols:   2216
-  CStrings:  3105
+  Functions: 1372
+  Symbols:   2316
+  CStrings:  3245
 
Symbols:
+ _CFDictionaryAddValue
+ _CFDictionaryCreateMutable
+ _LSDefaultAppCategoryMaskForCategory
+ _MDMDEPPushReceivedNotification
+ _MDMDEPPushServiceDirectory
+ _MDMDEPTokenSyncPropertiesFilePath
+ _MDMMigrationDirectory
+ _MDMSendDEPPushReceivedNotification
+ _OBJC_CLASS_$_DMCPropertyListStorage
+ _aks_set_configuration
+ _arc4random_uniform
+ _kAKSConfigInactivityRebootEnabled
+ _kCFAllocatorDefault
+ _kCFBooleanFalse
+ _kCFBooleanTrue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kMDMOptionIdleRebootAllowed
+ _objc_retain_x10
- _OBJC_CLASS_$_DMCBackgroundActivityManager
CStrings:
+ "\x14\x14"
+ "-[MDMServerCore _backgroundPollFromTask:]_block_invoke"
+ "-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRNFromBackgroundTask:]"
+ "-[MDMServerCore monitorDEPPushTokenIfNeededWithCompletion:]"
+ "-[MDMServerCore monitorDEPPushTokenWithCompletion:]"
+ "-[MDMServerCore simulateDEPPushWithCompletion:]"
+ "-[MDMServerCore syncDEPPushTokenWithDelay:completion:]"
+ "@\"BGSystemTask\""
+ "@\"DMCPropertyListStorage\""
+ "@\"MDMBackgroundTask\""
+ "@\"MDMMigrationManager\""
+ "App Push Token Sync Scheduled"
+ "Calling"
+ "CustomSetDefaultAppErrorDomain"
+ "DeadlineToSync"
+ "Error calling aks_set_configuration with kAKSConfigInactivityRebootEnabled config! Error code:  %x\n"
+ "Failed to get deadlineToSync with error: %{public}@"
+ "Failed to get lastestPushTokenHash with error: %{public}@"
+ "Failed to set deadlineToSync with error: %{public}@"
+ "Failed to set default calling app to: %{public}@ with error code: %{public}@"
+ "Failed to set default messaging app to: %{public}@ with error code: %{public}@"
+ "Failed to set lastestPushTokenHash with error: %{public}@"
+ "Interval"
+ "Localized Target Sync Date"
+ "MDMBGSystemTaskWrapper"
+ "MDMBackgroundTask"
+ "MDMBackgroundTask canceled task: %{public}@"
+ "MDMBackgroundTask deallocated task: %{public}@"
+ "MDMBackgroundTask expiration handler called for task: %{public}@"
+ "MDMBackgroundTask failed to cancel task '%{public}@' with error: %{public}@"
+ "MDMBackgroundTask failed to register task: %{public}@"
+ "MDMBackgroundTask failed to submit task '%{public}@' with error: %{public}@"
+ "MDMBackgroundTask failed to update task '%{public}@' with error: %{public}@"
+ "MDMBackgroundTask ignoring cancellation for inactive task: %{public}@"
+ "MDMBackgroundTask initialized task: %{public}@"
+ "MDMBackgroundTask launch handler called for task: %{public}@"
+ "MDMBackgroundTask submitted task '%{public}@' to run in %{public}f (+%{public}f) seconds"
+ "MDMBackgroundTask updated task '%{public}@' to run in %{public}f (+%{public}f) seconds"
+ "MDMDEPPushTokenManager: Scheduling push token sync after %.1f seconds"
+ "MDMDEPPushTokenManager: Syncing DEP push token..."
+ "MDMDEPPushTokenManager: scheduling mandatory DEP push token sync with delay: %.1f"
+ "MDMDEPPushTokenManager: shouldSyncToken is NO."
+ "MDMMigrationManager"
+ "MDMMigrationManager: DEP Push received"
+ "MDMMigrationManager: Device is not supervised"
+ "MDMMigrationManager: Failed to retrieve & store cloud config with error: %{public}@"
+ "MDMMigrationManager: Migration of ABE devices is not supported"
+ "MDMMigrationManager: Migration of Shared iPad devices is not supported"
+ "MDMMigrationManager: New pending cloud config stored."
+ "MDMMigrationManager: Retrieved new cloud config"
+ "MDMMigrationManager: Start monitoring DEP push notification"
+ "MDMMigrationManager: Storing new cloud config"
+ "MDMMigrationManager: server UID did not change."
+ "MDMServerCore HRN polling now..."
+ "MDMServerCore HRN scheduling next poll..."
+ "MDMServerCore ignoring excessive poll scheduling (in %{public}f seconds). Next poll expected at: %{public}@."
+ "MDMServerCore retried token update enough. Aborting..."
+ "MDMServerCore scheduling poll in %{public}f (+%{public}f) seconds."
+ "MDMServerCore subscribing to locale changes."
+ "MDMServerCore uproot failed to stop managing app: '%{public}@' with error: %{public}@"
+ "MDMServerCore uproot successfully stopped managing app: '%{public}@'"
+ "MDMServerCore will retry token update..."
+ "Messaging"
+ "SERVER CORE: CONFIG IS BEING SET TO FALSE: %@"
+ "SERVER CORE: CONFIG IS BEING SET TO TRUE: %@"
+ "Setting default app: %{public}@ for category: %lu"
+ "Successfully set kAKSConfigInactivityRebootEnabled config with value: %@"
+ "Successfully set the default calling app."
+ "Successfully set the default messaging app."
+ "T@\"BGSystemTask\",&,N,V_task"
+ "T@\"DMCPropertyListStorage\",&,N,V_syncActivityPlist"
+ "T@\"DMCPropertyListStorage\",&,N,V_syncInfoPlist"
+ "T@\"MDMBackgroundTask\",&,N,V_pollTask"
+ "T@\"MDMBackgroundTask\",&,N,V_retryPushTokenSyncTask"
+ "T@\"MDMMigrationManager\",&,N,V_mdmMigrationManager"
+ "T@\"NSDate\",R,N,V_targetDate"
+ "T@\"NSString\",&,N,V_name"
+ "T@?,C,N,V_callback"
+ "T@?,C,N,V_syncRequestCompletionHandler"
+ "TB,N,V_active"
+ "TB,N,V_isMonitoringTokenChanges"
+ "Target Sync Date"
+ "X\x1f\x06#"
+ "_active"
+ "_backgroundPollFromTask:"
+ "_callback"
+ "_depPushReceived"
+ "_isMigrationNeededWithExistingCloudConfig:newCloudConfig:"
+ "_isMigrationSupportedWithExistingCloudConfig:"
+ "_isMonitoringTokenChanges"
+ "_mdmMigrationManager"
+ "_memberQueuePollOrScheduleNextPollForHRNFromBackgroundTask:"
+ "_name"
+ "_performSetDefaultApp:forCategory:completion:"
+ "_pollTask"
+ "_queue_deadlineToSync"
+ "_queue_lastestPushTokenHashToSync"
+ "_queue_setDeadlineToSync:"
+ "_queue_setLastestPushTokenHashToSync:"
+ "_randomDelay"
+ "_retryPushTokenSyncAfterInterval:shouldForce:shouldScheduleRetry:shouldCallCompletion:"
+ "_retryPushTokenSyncTask"
+ "_scheduleAppTokenSync"
+ "_scheduleMDMMigrationProcessWithNewCloudConfig:"
+ "_startMonitoringDEPPushTokenChange"
+ "_submitNewRequestWithInterval:tolerance:"
+ "_syncActivityPlist"
+ "_syncInfoPlist"
+ "_syncPushTokenShouldForce:shouldScheduleRetry:backgroundTask:completionHandler:"
+ "_syncRequestCompletionHandler"
+ "_targetDate"
+ "_task"
+ "_updateExistingRequest:interval:tolerance:"
+ "active"
+ "callback"
+ "clearAllKeyValueStorageWithError:"
+ "com.apple.mdmd.MDMDEPPushTokenManager.sync"
+ "dateByAddingTimeInterval:"
+ "deregisterTaskWithIdentifier:"
+ "initWithCloudConfigDetails:"
+ "initWithFilePath:"
+ "initWithName:queue:"
+ "initWithTask:"
+ "isMDMMigrationEnabled"
+ "isMonitoringTokenChanges"
+ "isSetDefaultCallingAndMessagingAppsEnabled"
+ "isoLocalTimeZoneDateFormatter"
+ "mdmMigrationManager"
+ "mdmServerUID"
+ "monitorDEPPushTokenIfNeededWithCompletion:"
+ "monitorDEPPushTokenWithCompletion:"
+ "now"
+ "pollTask"
+ "retrieveValueForKey:error:"
+ "retryPushTokenSyncTask"
+ "saveKeyValuePairs:error:"
+ "saveValue:forKey:error:"
+ "scheduleMandatoryDEPPushTokenSyncWithRandomDelay:"
+ "setActive:"
+ "setCallback:"
+ "setDefaultApplicationForCategory:toApplicationRecord:completionHandler:"
+ "setExpirationHandler:"
+ "setIsMonitoringTokenChanges:"
+ "setMdmMigrationManager:"
+ "setPollTask:"
+ "setPriority:"
+ "setRetryPushTokenSyncTask:"
+ "setSyncActivityPlist:"
+ "setSyncInfoPlist:"
+ "setSyncRequestCompletionHandler:"
+ "setTask:"
+ "simulateDEPPush"
+ "simulateDEPPushWithCompletion:"
+ "startMonitoringDEPPushTokenChangeShouldForce:"
+ "startMonitoringDEPServerPush"
+ "storePendingCloudConfigurationDetailsForMigration:completionHandler:"
+ "submitRequestWithInterval:tolerance:callback:"
+ "supportedDefaultAppCategories"
+ "syncActivityPlist"
+ "syncDEPPushTokenWithDelay:completion:"
+ "syncInfoPlist"
+ "syncRequestCompletionHandler"
+ "targetDate"
+ "task"
+ "updateTaskRequest:error:"
+ "v16@?0@\"MDMBGSystemTaskWrapper\"8"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v32@0:8d16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8d16d24"
+ "v36@0:8d16B24B28B32"
+ "v40@0:8@16Q24@?32"
+ "v40@0:8@16d24d32"
+ "v40@0:8B16B20@24@?32"
+ "v40@0:8d16d24@?32"
- "\x04"
- "-[MDMServerCore _memberQueuePollOrScheduleNextPollForHRN]"
- "-[MDMServerCore _scheduleNextPollWithInterval:]_block_invoke"
- "-[MDMServerCore syncDEPPushTokenWithCompletion:]"
- "DMCBackgroundActivityManager: Failed to cancel task (%{public}@) with error: %{public}@"
- "DMCBackgroundActivityManager: Failed to register for task with name: %{public}@"
- "DMCBackgroundActivityManager: Failed to submit task with error: %@"
- "DMCBackgroundActivityManager: Task has been submitted. Abort..."
- "DMCBackgroundActivityManager: launchHandler called!"
- "DMCBackgroundActivityManager: request submmited"
- "MDMBackgroundTaskUtilities"
- "MDMDEPPushTokenManager: Failed to remove DEP token sync activity file with error: %{public}@"
- "MDMDEPPushTokenManager: Failed to retrieve & store cloud config with error: %{public}@"
- "MDMServerCore failed to stop managing app '%{public}@' with error: %{public}@"
- "Scheduling poll in %f seconds, tolerance %f."
- "Subscribing to locale changes."
- "V\x1f\x06#"
- "We've retried enough. Abort..."
- "Will retry token update..."
- "_memberQueuePollOrScheduleNextPollForHRN"
- "_queue_lastestPushTokenToSync"
- "_queue_setLastestPushTokenToSync:"
- "_syncPushTokenShouldForce:shouldScheduleRetry:completionHandler:"
- "cancelBackgroundTask:"
- "com.apple.mdmd.MDMDEPPushTokenManager"
- "manager:didFinishDeviceTransferPreflight:error:"
- "retrieveAndStoreCloudConfigurationDetailsCompletionBlock:"
- "scheduleOneShotActivity:interval:gracePeriod:callback:"
- "scheduleOneShotBackgroundTask:usingQueue:interval:gracePeriod:callback:"
- "startMonitoringDEPPushTokenChange"
- "syncDEPPushTokenWithCompletion:"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v40@0:8@\"MBManager\"16@\"MBDeviceTransferPreflight\"24@\"NSError\"32"
- "v56@0:8@16@24d32d40@?48"

```
