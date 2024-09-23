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
+ _OBJC_CLASS_$_DEAnnotation
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _CKErrorDomain
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
- _xpc_equal
- _OBJC_CLASS_$_CPNetworkObserver
- _ELSEventTypeFailedSavingRecord
- _CPNetworkObserverReachableFlags
- _CPNetworkObserverReachable
- _xpc_activity_set_state
- _xpc_activity_copy_criteria
CStrings:
+ "itemWithURL:shouldCheckURLAttributes:"
+ "Failed to annotate [%!{(MISSING)public}@] with [%!{(MISSING)public}@] error: [%!{(MISSING)public}@]"
+ "setNetworkUploadSize:"
+ "collectAnnotatedGroupWithIdentifier:parameters:"
+ "setTaskCompleted"
+ "initWithPathURL:shouldCheckURLAttributes:"
+ "Task %!{(MISSING)public}@ completed"
+ "_combineParametersWithParameters:extension:identifier:"
+ "-[DEDDiagnosticCollector collectAnnotatedGroupWithIdentifier:parameters:]"
+ "com.apple.diagnosticextensionsd.%!@(MISSING).CloudKitMarkAttachmentUploadComplete"
+ "v16@?0@\"BGSystemTask\"8"
+ "Task %!{(MISSING)public}@ is running"
+ "%!@(MISSING),%!l(MISSING)d"
+ "CloudKit failed to save record: %!@(MISSING) with error: %!@(MISSING)"
+ "setExpirationHandler:"
+ "\x04"
+ "-[DEDAttachmentHandler _processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:rootDir:annotatedGroup:]"
+ "Uploading %!l(MISSING)u records: %!@(MISSING)"
+ "1\x17"
+ "v64@0:8@16@24@32@?40@?48@?56"
+ "submitTaskRequest:error:"
+ "additionalInfo"
+ "iconType"
+ "v16@?0@\"DEAnnotatedGroup\"8"
+ "Feedback Assistant"
+ "annotateURL:displayName:description:iconType:additionalInfo:error:"
+ "CloudKit successfully saved record: %!@(MISSING)"
+ "uploadAttachments:inAttachmentGroup:completionHandler:"
+ "finished collecting annotated attachments for %!{(MISSING)public}@"
+ "items"
+ "Failed to submit task %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "Expiring task %!{(MISSING)public}@"
+ "Operation failed with error: %!@(MISSING)"
+ "createAttachmentGroupStatusForAttachmentGroup:completionHandler:"
+ "Failed to expire task %!{(MISSING)public}@"
+ "Upload progress is %!f(MISSING) for asset: %!@(MISSING)"
+ "annotated"
+ "_processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:rootDir:annotatedGroup:"
+ "initWithIdentifier:"
+ "setTaskExpiredWithRetryAfter:error:"
+ "collected annotated group %!@(MISSING)"
+ "processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:annotatedGroup:"
+ "Annotated Group returned is nil. Will try attachmentForParameters:"
+ "setSystemTask:"
+ "setPriority:"
+ "Created record %!@(MISSING) for %!{(MISSING)public}@ with queue destination %!{(MISSING)public}@"
+ "annotatedAttachmentsForParameters:andHandler:"
+ "Operation completed successfully: %!@(MISSING)"
+ "Task %!{(MISSING)public}@ was expired by DAS"
+ "setRequiresNetworkConnectivity:"
+ "Annotated [%!{(MISSING)public}@] with [%!{(MISSING)public}@]"
+ "sharedScheduler"
+ "@60@0:8@16@24@32B40@44@52"
+ "com.apple.diagnosticextensionsd.%!@(MISSING).CloudKitUploadAttachments"
+ "Submitted task %!{(MISSING)public}@"
- "v48@0:8@16@?24@?32@?40"
- "addObserver:selector:forHostname:"
- "createAttachmentGroupStatusForAttachmentGroup:"
- "_successfulUploads"
- "operationCount"
- "Failed to set XPC_ACTIVITY_STATE_CONTINUE for [%!{(MISSING)public}@]"
- "setRecordsQueue:"
- "All Uploads Failed and iCloud is not retrying anymore"
- "%!@(MISSING),%!@(MISSING),%!l(MISSING)d"
- "_recordsQueue"
- "%!f(MISSING)"
- "setFailedUploads:"
- "flushQueue"
- "Saved %!@(MISSING) for ID: %!{(MISSING)public}@"
- "A\x17"
- "removeObserver:"
- "stillHaveOperationsInQueue"
- "setPreviousRecordsQueue:"
- "apple.com"
- "Failed to create AttachmentGroup record and iCloud is not retrying anymore"
- "performCloudKitOperations"
- "setSuccessfulUploads:"
- "failedUploads"
- "recordType"
- "sharedNetworkObserver"
- "recordID"
- "recordsQueue"
- "setXPCActivity:"
- "Error saving %!@(MISSING): %!{(MISSING)public}@"
- "com.apple.diagnosticextensionsd.commit-record-%!@(MISSING)-%!@(MISSING)"
- "T@\"NSMutableArray\",&,N,V_recordsQueue"
- "Uploaded File: %!@(MISSING) successfully"
- "CloudKit upload progress percentage: %!f(MISSING)"
- "restoreQueue"
- "com.apple.diagnosticextensionsd.commit-file-%!@(MISSING)-%!@(MISSING)"
- "T@\"NSArray\",&,N,V_previousRecordsQueue"
- "previousRecordsQueue"
- "addRawRecordToQueueFromModel:"
- "scheduleOperationsOnAvailability"
- "-[DEDAttachmentHandler _processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:rootDir:]"
- "Ti,N,V_failedUploads"
- "logError:forRecord:"
- "executeRecord:atomicallyWithProgressHandler:completionHandler:finalHandler:"
- "_previousRecordsQueue"
- "Ti,N,V_successfulUploads"
- "Total Uploads: %!l(MISSING)d Successful: %!d(MISSING) Failed: %!d(MISSING)"
- "\x06"
- "processAttachments:withSessionIdentifier:extension:shouldAddClassBDataProtection:"
- "1"
- "successfulUploads"
- "_reachabilityChanged:"
- "unscheduleOperationsOnAvailability"
- "postProcessRecord:withError:attachmentGroup:"
- "userInfo"
- "executeOperationsAtomicallyWithProgressHandler:completionHandler:finalHandler:"
- "_failedUploads"
- "operationQueue"
- "Creating CKRecord for %!{(MISSING)public}@ with queue destination %!@(MISSING)"
- "XPC_ACTIVITY_STATE_CONTINUE is set for [%!{(MISSING)public}@]"
- "v40@0:8@?16@?24@?32"

```
