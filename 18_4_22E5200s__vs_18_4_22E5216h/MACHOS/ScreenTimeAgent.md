## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

```diff

-537.4.14.0.0
-  __TEXT.__text: 0x24d084
-  __TEXT.__auth_stubs: 0x2a80
-  __TEXT.__objc_stubs: 0x111c0
-  __TEXT.__objc_methlist: 0x9d90
+537.4.18.2.0
+  __TEXT.__text: 0x2507ac
+  __TEXT.__auth_stubs: 0x2a90
+  __TEXT.__objc_stubs: 0x10d00
+  __TEXT.__objc_methlist: 0x9a18
   __TEXT.__const: 0x3e50
-  __TEXT.__gcc_except_tab: 0x21a4
-  __TEXT.__cstring: 0xd99c
-  __TEXT.__oslogstring: 0x1b83b
-  __TEXT.__objc_methname: 0x1b979
-  __TEXT.__objc_classname: 0x2015
-  __TEXT.__objc_methtype: 0x540c
+  __TEXT.__gcc_except_tab: 0x2140
+  __TEXT.__cstring: 0xd87c
+  __TEXT.__oslogstring: 0x1b2cb
+  __TEXT.__objc_methname: 0x1b326
+  __TEXT.__objc_classname: 0x1f9a
+  __TEXT.__objc_methtype: 0x517a
   __TEXT.__constg_swiftt: 0x2b80
   __TEXT.__swift5_typeref: 0x293a
   __TEXT.__swift5_builtin: 0x1b8

   __TEXT.__swift_as_ret: 0x3dc
   __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_protos: 0x70
-  __TEXT.__unwind_info: 0x6d58
-  __TEXT.__eh_frame: 0xebf0
-  __DATA_CONST.__auth_got: 0x1550
-  __DATA_CONST.__got: 0x1460
-  __DATA_CONST.__auth_ptr: 0x9b8
-  __DATA_CONST.__const: 0xe6e8
-  __DATA_CONST.__cfstring: 0x4940
-  __DATA_CONST.__objc_classlist: 0x638
+  __TEXT.__unwind_info: 0x7108
+  __TEXT.__eh_frame: 0xef10
+  __DATA_CONST.__auth_got: 0x1558
+  __DATA_CONST.__got: 0x1530
+  __DATA_CONST.__auth_ptr: 0x6e8
+  __DATA_CONST.__const: 0xe680
+  __DATA_CONST.__cfstring: 0x48c0
+  __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x548
+  __DATA_CONST.__objc_protolist: 0x538
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x170
-  __DATA_CONST.__objc_superrefs: 0x3b0
+  __DATA_CONST.__objc_superrefs: 0x398
   __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1d888
-  __DATA.__objc_selrefs: 0x5660
-  __DATA.__objc_ivar: 0x834
-  __DATA.__objc_data: 0x43d0
-  __DATA.__data: 0x8788
-  __DATA.__bss: 0x49b0
+  __DATA.__objc_const: 0x1d078
+  __DATA.__objc_selrefs: 0x5508
+  __DATA.__objc_ivar: 0x7fc
+  __DATA.__objc_data: 0x4330
+  __DATA.__data: 0x86c8
+  __DATA.__bss: 0x49a0
   __DATA.__common: 0x128
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7939
-  Symbols:   1502
-  CStrings:  7956
+  Functions: 7848
+  Symbols:   1501
+  CStrings:  7831
 
Symbols:
+ _OBJC_CLASS_$_CTCategory
+ _OBJC_CLASS_$_NSConditionLock
+ _exit
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
- _NSPersistentStoreMirroringOptionsKey
- _OBJC_CLASS_$_NSCloudKitMirroringExportRequest
- _OBJC_CLASS_$_STReconciler
- __os_activity_none
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initEnumMetadataMultiPayloadWithLayoutString
- _swift_initStructMetadataWithLayoutString
- _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
- _swift_multiPayloadEnumGeneric_getEnumTag
CStrings:
+ "Exiting ScreenTimeAgent with reason: %s"
+ "Expiring One More Minute for %{public}@"
+ "Failed to apply One More Minute For appIdentifier: %{public}@ with error: %{public}@"
+ "Failed to apply One More Minute For category identifier: %{public}@ with error: %{public}@"
+ "Failed to apply One More Minute For webDomain: %{public}@ with error: %{public}@"
+ "Failed to fetch categories for resourceIDs: %{public}@ with error: %{public}@"
+ "Failed to fetch user with dsid: %{public}@, %{public}@"
+ "Failed to find any usageLimits with error: %{public}@"
+ "One More Minute problem finding category for %{public}@ with error %{public}@"
+ "STOneMoreMinute"
+ "SafariStore"
+ "_applyOneMoreMinuteForBlueprint:timeGranted:toUser:managedObjectContext:error:"
+ "_categoriesForIdentifiers:ofUsageType:completionHandler:"
+ "_doesNotHaveBlueprints:predicate:"
+ "_shouldAllowOneMoreMinuteForBundleIdentifier:configuration:"
+ "_shouldAllowOneMoreMinuteForCategoryIdentifier:configuration:"
+ "_shouldAllowOneMoreMinuteForWebDomain:configuration:"
+ "array"
+ "categoriesForBundleIDs:completionHandler:"
+ "categoriesForDomainNames:completionHandler:"
+ "dateWithTimeIntervalSinceNow:"
+ "equivalentBundleIdentifiers"
+ "equivalentIdentifiersForBundleID:"
+ "failed to apply downtime OMM with error: %{public}@"
+ "fetchCategoryForBundleIdentifier:error:"
+ "fetchOneMoreMinuteBlueprintsWithMoc:error:"
+ "initWithCondition:"
+ "lock"
+ "lockWhenCondition:beforeDate:"
+ "oneMoreMinuteManager"
+ "one_more_minute"
+ "safari"
+ "set"
+ "setDenyHistoryClearing:"
+ "setDenyPrivateBrowsing:"
+ "shouldAllowOneMoreMinuteForBundleIdentifier:oneMoreMinuteBlueprints:"
+ "shouldAllowOneMoreMinuteForCategoryIdentifier:oneMoreMinuteBlueprints:"
+ "shouldAllowOneMoreMinuteForWebDomain:oneMoreMinuteBlueprints:"
+ "unlock"
+ "unlockWithCondition:"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v56@0:8@16@24@32@40^@48"
+ "webDomains"
- "...Local changes should be mirrored, so starting a sync"
- "...Local changes should not be mirrored"
- "...The check to see if local changes should be mirrored failed: %@"
- "@\"APSConnection\""
- "@\"STDaemonPersistenceController\""
- "@32@0:8@?16^@24"
- "APSConnectionDelegate"
- "B24@?0@\"NSPersistentStore\"8@\"NSDictionary\"16"
- "Canceling old history analyzer timer and scheduling a new one"
- "Canceling old safety sync timer and scheduling a new one for %{public}@ seconds from now"
- "Checking to see if local changes should be mirrored..."
- "Connect -> APNS"
- "Crashing ScreenTimeAgent"
- "Error scheduling mirror sync(export): %{public}@"
- "Error scheduling mirror sync(import): %{public}@"
- "Failed to load cloud store: %{public}@"
- "Failed to remove cloud store: %{public}@"
- "Failed to unload cloud store: %{public}@"
- "KVOContextSTCloudMirroringMonitor"
- "Killing ScreenTimeAgent with reason: %s"
- "Last mirroring operation hasn't had a chance to run, ignoring new request"
- "Loading CloudKit mirroring persistent store and CKContainer"
- "Migrate failed: %{public}@"
- "Mirror sync(export) completed; success: %d, madeChanges: %d, error: %{public}@"
- "Mirror sync(import) completed; success: %d, madeChanges: %d, error: %{public}@"
- "Mirroring failed: %{public}@"
- "No persistent stores support mirroring"
- "No safety sync needed, last sync attempt was at: %{public}@"
- "Notification <- APNS"
- "Notification from unknown store %@ named %@"
- "Performing safety sync, last sync attempt was at: %{public}@"
- "Push notification received for topic: '%@'"
- "Received NSCloudKitMirroringDelegateRequestAbortedError, attempting to recover by removing and re-adding cloud persistent store"
- "Received push token notification"
- "Received push token, ignoring"
- "Received store change notification: %@"
- "Reconcile finished; changes: %d, error: %{public}@"
- "Removing CloudKit mirroring persistent store and CKContainer"
- "STCloudMirroringMonitor"
- "STCoreDataCloudKitMirroringSyncOperation"
- "STCoreDataCloudKitMirroringSyncOperation start"
- "STNotificationManager"
- "STNotificationManagerDelegate"
- "Safety sync initiated"
- "Safety sync terminated"
- "Scheduling history analyzer timer..."
- "Scheduling safety sync timer for %{public}@ seconds from now"
- "ScreenTimeAgent/DiagnosticsService.swift"
- "Skipping export, there are no persistent stores that support mirroring."
- "Skipping import, there are no persistent stores that support mirroring."
- "Starting iCloud mirroring"
- "Stopping iCloud mirroring"
- "T@\"APSConnection\",&,N,V_connection"
- "T@\"NSData\",&,N,V_pushToken"
- "T@\"NSMutableDictionary\",&,N,V_delegates"
- "T@\"NSMutableSet\",&,N,V_topics"
- "T@\"NSObject<OS_os_transaction>\",&,V_historyAnalyzerTransaction"
- "T@\"NSOperationQueue\",&,N,V_syncOperationQueue"
- "T@\"NSTimer\",&,N,V_historyAnalyzerTimer"
- "T@\"NSTimer\",&,N,V_safetySyncTimer"
- "T@\"STDaemonPersistenceController\",R,N,V_persistenceController"
- "T@,&,N,V_storeChangeNotificationToken"
- "TB,GisCloudKitSyncingEnabled"
- "TestMirroringStaleSeconds"
- "Token <- APNS"
- "Triggering mirroring operation"
- "Unloading CloudKit mirroring persistent store and CKContainer"
- "_analyzeLocalChanges"
- "_checkForNextSync"
- "_cloudKitSyncingEnabled"
- "_cloudKitTopicName"
- "_connectToAPNS"
- "_delegates"
- "_doesNotHaveOneMoreMinuteBlueprintPassingTest:error:"
- "_executingSyncOperations"
- "_exportWithCompletionHandler:"
- "_historyAnalyzerTimer"
- "_historyAnalyzerTransaction"
- "_importWithCompletionHandler:"
- "_loadCloudPersistentStore"
- "_migrateWithExportNeeded:completionHandler:"
- "_nextSafetySyncInterval"
- "_persistentStoreDidChange:"
- "_pushToken"
- "_queuedSyncOperations"
- "_reconcileWithCompletionHandler:"
- "_registerForNotificationsThatTriggerCloudKitSyncs"
- "_removeCloudPersistentStore"
- "_safetySyncNeeded"
- "_safetySyncStaleSeconds"
- "_safetySyncTimer"
- "_scheduleHistoryAnalyzerTimer"
- "_setEnabledTopics:"
- "_setSafetySyncTimer"
- "_startSafetySyncChecks"
- "_stopSafetySyncChecks"
- "_storeChangeNotificationToken"
- "_syncOperationQueue"
- "_syncingEnabledLock"
- "_topics"
- "_unloadCloudPersistentStore"
- "_unregisterForNotificationsThatTriggerCloudKitSyncs"
- "_updateAPNSConnection"
- "apns"
- "areLocalChangesInterestingWithError:"
- "cloudKitSyncingEnabled"
- "com.apple.ScreenTimeAgent.analyze"
- "com.apple.ScreenTimeAgent.cloudkit"
- "com.apple.icloud-container.%@"
- "connection:channelSubscriptionsFailedWithFailures:"
- "connection:didChangeConnectedStatus:"
- "connection:didFailToSendOutgoingMessage:error:"
- "connection:didReceiveIncomingMessage:"
- "connection:didReceiveMessageForTopic:userInfo:"
- "connection:didReceivePublicToken:"
- "connection:didReceiveToken:forInfo:"
- "connection:didReceiveToken:forTopic:identifier:"
- "connection:didReceiveURLToken:forInfo:"
- "connection:didReceiveURLTokenError:forInfo:"
- "connection:didSendOutgoingMessage:"
- "connectionDidReconnect:"
- "delegates"
- "historyAnalyzerTimer"
- "historyAnalyzerTransaction"
- "isCancelled"
- "isCloudKitSyncingEnabled"
- "madeChanges"
- "migrateWithError:"
- "mirroring"
- "publicToken"
- "pushToken"
- "receivedNotification:"
- "receivedToken:"
- "reconcileWithManagedObjectContext:completion:"
- "registerWithTopic:delegate:"
- "safetySyncTimer"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "setCloudKitSyncingEnabled:"
- "setConnection:"
- "setContainerOptions:"
- "setDelegates:"
- "setHistoryAnalyzerTimer:"
- "setHistoryAnalyzerTransaction:"
- "setPushToken:"
- "setSafetySyncTimer:"
- "setStoreChangeNotificationToken:"
- "setSyncOperationQueue:"
- "setTopics:"
- "sharedNotificationManager"
- "storeChangeNotificationToken"
- "syncOperationQueue"
- "synchronizeWithCompletionHandler:"
- "topic"
- "topics"
- "v24@0:8@\"APSConnection\"16"
- "v24@0:8@\"APSIncomingMessage\"16"
- "v24@?0B8B12@\"NSError\"16"
- "v28@0:8@\"APSConnection\"16B24"
- "v32@0:8@\"APSConnection\"16@\"APSIncomingMessage\"24"
- "v32@0:8@\"APSConnection\"16@\"APSOutgoingMessage\"24"
- "v32@0:8@\"APSConnection\"16@\"NSArray\"24"
- "v32@0:8@\"APSConnection\"16@\"NSData\"24"
- "v40@0:8@\"APSConnection\"16@\"APSOutgoingMessage\"24@\"NSError\"32"
- "v40@0:8@\"APSConnection\"16@\"APSURLToken\"24@\"APSURLTokenInfo\"32"
- "v40@0:8@\"APSConnection\"16@\"NSData\"24@\"APSAppTokenInfo\"32"
- "v40@0:8@\"APSConnection\"16@\"NSError\"24@\"APSURLTokenInfo\"32"
- "v40@0:8@\"APSConnection\"16@\"NSString\"24@\"NSDictionary\"32"
- "v48@0:8@\"APSConnection\"16@\"NSData\"24@\"NSString\"32@\"NSString\"40"

```
