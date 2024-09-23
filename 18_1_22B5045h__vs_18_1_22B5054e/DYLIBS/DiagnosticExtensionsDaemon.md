## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-187.0.0.0.0
-  __TEXT.__text: 0x6e2e4
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x5e30
+189.0.0.0.0
+  __TEXT.__text: 0x6e5c0
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_methlist: 0x5d88
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x505f
-  __TEXT.__gcc_except_tab: 0x1c98
-  __TEXT.__oslogstring: 0x83d0
+  __TEXT.__cstring: 0x5116
+  __TEXT.__gcc_except_tab: 0x1dac
+  __TEXT.__oslogstring: 0x84f9
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x1960
-  __TEXT.__objc_classname: 0x875
-  __TEXT.__objc_methname: 0xeb7a
-  __TEXT.__objc_methtype: 0x230a
-  __TEXT.__objc_stubs: 0xbbc0
+  __TEXT.__unwind_info: 0x1998
+  __TEXT.__objc_classname: 0x873
+  __TEXT.__objc_methname: 0xeb73
+  __TEXT.__objc_methtype: 0x2316
+  __TEXT.__objc_stubs: 0xbae0
   __DATA_CONST.__got: 0x6c8
-  __DATA_CONST.__const: 0x1be8
+  __DATA_CONST.__const: 0x1c60
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3788
+  __DATA_CONST.__objc_selrefs: 0x3758
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0xbc0
+  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__const: 0xbe0
   __AUTH_CONST.__cfstring: 0x4ba0
-  __AUTH_CONST.__objc_const: 0x138b0
+  __AUTH_CONST.__objc_const: 0x137f0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0x5b0
+  __DATA.__objc_ivar: 0x5a0
   __DATA.__data: 0xa40
-  __DATA.__bss: 0x178
+  __DATA.__bss: 0x180
   __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__bss: 0x218
+  __DATA_DIRTY.__bss: 0x220
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/MultipeerConnectivity.framework/MultipeerConnectivity
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
-  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport
-  - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/CoreFollowUp
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2657
-  Symbols:   3337
-  CStrings:  4466
+  Functions: 2655
+  Symbols:   3334
+  CStrings:  4463
 
Symbols:
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _CKErrorDomain
+ _OBJC_CLASS_$_DEAnnotation
- _CPNetworkObserverReachableFlags
- _xpc_activity_copy_criteria
- _CPNetworkObserverReachable
- _ELSEventTypeFailedSavingRecord
- _xpc_equal
- _OBJC_CLASS_$_CPNetworkObserver
- _xpc_activity_set_state
CStrings:
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setTaskCompleted"
+ "Operation completed successfully: %!@(MISSING)"
+ "Task %!{(MISSING)public}@ was expired by DAS"
+ "Submitted task %!{(MISSING)public}@"
+ "collectAnnotatedGroupWithIdentifier:parameters:"
+ "%!@(MISSING),%!l(MISSING)d"
+ "Annotated Group returned is nil. Will try attachmentForParameters:"
+ "uploadAttachments:inAttachmentGroup:completionHandler:"
+ "setRequiresNetworkConnectivity:"
+ "items"
+ "setSystemTask:"
+ "processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:annotatedGroup:"
+ "_combineParametersWithParameters:extension:identifier:"
+ "CloudKit failed to save record: %!@(MISSING) with error: %!@(MISSING)"
+ "Failed to submit task %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "1\x17"
+ "collected annotated group %!@(MISSING)"
+ "setNetworkUploadSize:"
+ "finished collecting annotated attachments for %!{(MISSING)public}@"
+ "setPriority:"
+ "annotateURL:displayName:description:iconType:additionalInfo:error:"
+ "_processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:rootDir:annotatedGroup:"
+ "submitTaskRequest:error:"
+ "Task %!{(MISSING)public}@ completed"
+ "Uploading %!l(MISSING)u records: %!@(MISSING)"
+ "Annotated [%!{(MISSING)public}@] with [%!{(MISSING)public}@]"
+ "uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "com.apple.diagnosticextensionsd.%!@(MISSING).CloudKitMarkAttachmentUploadComplete"
+ "itemWithURL:shouldCheckURLAttributes:"
+ "v16@?0@\"DEAnnotatedGroup\"8"
+ "Feedback Assistant"
+ "-[DEDDiagnosticCollector collectAnnotatedGroupWithIdentifier:parameters:]"
+ "iconType"
+ "sharedScheduler"
+ "initWithPathURL:shouldCheckURLAttributes:"
+ "additionalInfo"
+ "annotatedAttachmentsForParameters:andHandler:"
+ "@60@0:8@16@24@32B40@44@52"
+ "v64@0:8@16@24@32@?40@?48@?56"
+ "-[DEDAttachmentHandler _processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:rootDir:annotatedGroup:]"
+ "Created record %!@(MISSING) for %!{(MISSING)public}@ with queue destination %!{(MISSING)public}@"
+ "v16@?0@\"BGSystemTask\"8"
+ "Upload progress is %!f(MISSING) for asset: %!@(MISSING)"
+ "CloudKit successfully saved record: %!@(MISSING)"
+ "Expiring task %!{(MISSING)public}@"
+ "Failed to annotate [%!{(MISSING)public}@] with [%!{(MISSING)public}@] error: [%!{(MISSING)public}@]"
+ "annotated"
+ "Task %!{(MISSING)public}@ is running"
+ "Operation failed with error: %!@(MISSING)"
+ "com.apple.diagnosticextensionsd.%!@(MISSING).CloudKitUploadAttachments"
+ "\x04"
+ "initWithIdentifier:"
+ "Failed to expire task %!{(MISSING)public}@"
+ "setExpirationHandler:"
+ "createAttachmentGroupStatusForAttachmentGroup:completionHandler:"
+ "setTaskExpiredWithRetryAfter:error:"
- "setPreviousRecordsQueue:"
- "removeObserver:"
- "unscheduleOperationsOnAvailability"
- "_previousRecordsQueue"
- "recordType"
- "v48@0:8@16@?24@?32@?40"
- "scheduleOperationsOnAvailability"
- "%!f(MISSING)"
- "Total Uploads: %!l(MISSING)d Successful: %!d(MISSING) Failed: %!d(MISSING)"
- "Uploaded File: %!@(MISSING) successfully"
- "A\x17"
- "addRawRecordToQueueFromModel:"
- "CloudKit upload progress percentage: %!f(MISSING)"
- "flushQueue"
- "Failed to set XPC_ACTIVITY_STATE_CONTINUE for [%!{(MISSING)public}@]"
- "_recordsQueue"
- "restoreQueue"
- "apple.com"
- "stillHaveOperationsInQueue"
- "Ti,N,V_successfulUploads"
- "performCloudKitOperations"
- "T@\"NSMutableArray\",&,N,V_recordsQueue"
- "All Uploads Failed and iCloud is not retrying anymore"
- "postProcessRecord:withError:attachmentGroup:"
- "recordsQueue"
- "_reachabilityChanged:"
- "addObserver:selector:forHostname:"
- "setSuccessfulUploads:"
- "recordID"
- "\x06"
- "Creating CKRecord for %!{(MISSING)public}@ with queue destination %!@(MISSING)"
- "-[DEDAttachmentHandler _processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:rootDir:]"
- "sharedNetworkObserver"
- "setFailedUploads:"
- "Saved %!@(MISSING) for ID: %!{(MISSING)public}@"
- "Failed to create AttachmentGroup record and iCloud is not retrying anymore"
- "operationCount"
- "setRecordsQueue:"
- "previousRecordsQueue"
- "XPC_ACTIVITY_STATE_CONTINUE is set for [%!{(MISSING)public}@]"
- "processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:"
- "executeRecord:atomicallyWithProgressHandler:completionHandler:finalHandler:"
- "successfulUploads"
- "operationQueue"
- "v40@0:8@?16@?24@?32"
- "setXPCActivity:"
- "T@\"NSArray\",&,N,V_previousRecordsQueue"
- "Error saving %!@(MISSING): %!{(MISSING)public}@"
- "createAttachmentGroupStatusForAttachmentGroup:"
- "_failedUploads"
- "userInfo"
- "executeOperationsAtomicallyWithProgressHandler:completionHandler:finalHandler:"
- "com.apple.diagnosticextensionsd.commit-record-%!@(MISSING)-%!@(MISSING)"
- "Ti,N,V_failedUploads"
- "1"
- "logError:forRecord:"
- "_successfulUploads"
- "com.apple.diagnosticextensionsd.commit-file-%!@(MISSING)-%!@(MISSING)"
- "failedUploads"
- "%!@(MISSING),%!@(MISSING),%!l(MISSING)d"

```
