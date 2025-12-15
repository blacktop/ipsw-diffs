## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/DiagnosticExtensionsDaemon`

```diff

-205.2.0.0.0
-  __TEXT.__text: 0x726e8
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x6b0c
+205.4.0.0.0
+  __TEXT.__text: 0x758d8
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x6c3c
   __TEXT.__const: 0x31a
-  __TEXT.__cstring: 0x5305
-  __TEXT.__gcc_except_tab: 0x1db0
-  __TEXT.__oslogstring: 0x87d9
+  __TEXT.__cstring: 0x54d5
+  __TEXT.__gcc_except_tab: 0x1f7c
+  __TEXT.__oslogstring: 0x8ce9
   __TEXT.__ustring: 0xc
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_typeref: 0x42

   __TEXT.__swift5_reflstr: 0x80
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x1b10
+  __TEXT.__unwind_info: 0x1c18
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x894
-  __TEXT.__objc_methname: 0xf215
-  __TEXT.__objc_methtype: 0x2454
-  __TEXT.__objc_stubs: 0xbf20
-  __DATA_CONST.__got: 0x6d0
-  __DATA_CONST.__const: 0x20b0
+  __TEXT.__objc_classname: 0x895
+  __TEXT.__objc_methname: 0xf471
+  __TEXT.__objc_methtype: 0x24b3
+  __TEXT.__objc_stubs: 0xc1a0
+  __DATA_CONST.__got: 0x6e8
+  __DATA_CONST.__const: 0x2100
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39c0
+  __DATA_CONST.__objc_selrefs: 0x3a40
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__auth_got: 0x678
   __AUTH_CONST.__const: 0xc40
-  __AUTH_CONST.__cfstring: 0x4d00
-  __AUTH_CONST.__objc_const: 0x129c0
+  __AUTH_CONST.__cfstring: 0x4e00
+  __AUTH_CONST.__objc_const: 0x12f68
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0xfb0
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x5b8
+  __DATA.__objc_ivar: 0x5b4
   __DATA.__data: 0xa70
   __DATA.__bss: 0x260
   __DATA_DIRTY.__objc_data: 0x8c0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DDF93775-2652-3BB1-BA86-38E5FCA710B1
-  Functions: 2769
-  Symbols:   9618
-  CStrings:  5159
+  UUID: F16850B6-609E-36C2-8561-6296149074B5
+  Functions: 2817
+  Symbols:   9783
+  CStrings:  5221
 
Symbols:
+ +[DEDCloudKitBaseModel archivedClasses]
+ +[DEDCloudKitBaseModel recordClasses]
+ +[DEDCloudKitBaseModel supportsSecureCoding]
+ +[DEDCloudKitClient archivedClasses]
+ +[DEDCloudKitClient recordClasses]
+ +[DEDCloudKitClient supportsSecureCoding]
+ -[DEDCloudKitBaseModel encodeWithCoder:]
+ -[DEDCloudKitBaseModel initWithCoder:]
+ -[DEDCloudKitBaseModel initWithCoder:].cold.1
+ -[DEDCloudKitClient createOperationWithRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]
+ -[DEDCloudKitClient encodeWithCoder:]
+ -[DEDCloudKitClient handleOtherFailure:task:completionBlock:]
+ -[DEDCloudKitClient handleOtherFailure:task:completionBlock:].cold.1
+ -[DEDCloudKitClient handleOtherFailure:task:completionBlock:].cold.2
+ -[DEDCloudKitClient handleOtherFailure:task:completionBlock:].cold.3
+ -[DEDCloudKitClient handlePartialFailure:records:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]
+ -[DEDCloudKitClient handlePartialFailure:records:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:].cold.1
+ -[DEDCloudKitClient handlePartialFailure:records:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:].cold.2
+ -[DEDCloudKitClient handlePartialFailure:records:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:].cold.3
+ -[DEDCloudKitClient initWithCoder:]
+ -[DEDCloudKitClient initWithCoder:].cold.1
+ -[DEDCloudKitClient initWithConfiguration:taskIdentifier:]
+ -[DEDCloudKitClient isBackgroundTaskExpiredError:]
+ -[DEDCloudKitClient pendingRecords]
+ -[DEDCloudKitClient registerForTaskWithIdentifier:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]
+ -[DEDCloudKitClient resumeUploadWithPerRecordProgressBlock:perRecordSaveBlock:completionBlock:]
+ -[DEDCloudKitClient retryDelayForError:]
+ -[DEDCloudKitClient setPendingRecords:]
+ -[DEDCloudKitClient setTaskIdentifier:]
+ -[DEDCloudKitClient shouldRetryError:]
+ -[DEDCloudKitClient taskIdentifier]
+ -[DEDCloudKitClient uploadRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]
+ -[DEDCloudKitClient uploadRecords:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]
+ -[DEDCloudKitClient uploadRecords:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:].cold.1
+ -[DEDCloudKitClient uploadRecords:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:].cold.2
+ -[DEDCloudKitFinisher advanceState]
+ -[DEDCloudKitFinisher endWithError:]
+ -[DEDCloudKitFinisher endWithError:].cold.1
+ -[DEDCloudKitFinisher initWithCoder:].cold.1
+ -[DEDCloudKitFinisher resumeUploadingAttachmentGroupStatus]
+ -[DEDCloudKitFinisher resumeUploadingAttachmentGroupStatus].cold.1
+ -[DEDCloudKitFinisher resumeUploadingAttachments]
+ -[DEDCloudKitFinisher resumeUploadingAttachments].cold.1
+ -[DEDCloudKitFinisher resume]
+ -[DEDCloudKitFinisher startCompressing]
+ -[DEDCloudKitFinisher startUploadingAttachmentGroupStatus]
+ -[DEDCloudKitFinisher startUploadingAttachmentGroupStatus].cold.1
+ -[DEDCloudKitFinisher startUploadingAttachments]
+ -[DEDCloudKitFinisher startUploadingAttachments].cold.1
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table27
+ GCC_except_table81
+ _CKAcceptableValueClasses
+ _CKErrorRetryAfterKey
+ _CKPartialErrorsByItemIDKey
+ _OBJC_CLASS_$_CKRecordID
+ _OBJC_IVAR_$_DEDCloudKitClient._pendingRecords
+ _OBJC_IVAR_$_DEDCloudKitClient._taskIdentifier
+ __OBJC_$_CLASS_METHODS_DEDCloudKitBaseModel
+ __OBJC_$_CLASS_METHODS_DEDCloudKitClient
+ __OBJC_$_CLASS_PROP_LIST_DEDCloudKitBaseModel
+ __OBJC_$_CLASS_PROP_LIST_DEDCloudKitClient
+ __OBJC_CLASS_PROTOCOLS_$_DEDCloudKitClient
+ ___109-[DEDCloudKitClient registerForTaskWithIdentifier:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke
+ ___109-[DEDCloudKitClient registerForTaskWithIdentifier:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.35
+ ___109-[DEDCloudKitClient registerForTaskWithIdentifier:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke_2
+ ___111-[DEDCloudKitClient createOperationWithRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke
+ ___111-[DEDCloudKitClient createOperationWithRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.42
+ ___111-[DEDCloudKitClient createOperationWithRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.42.cold.1
+ ___111-[DEDCloudKitClient createOperationWithRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.cold.1
+ ___39-[DEDCloudKitFinisher startCompressing]_block_invoke
+ ___39-[DEDCloudKitFinisher startCompressing]_block_invoke_2
+ ___48-[DEDCloudKitFinisher startUploadingAttachments]_block_invoke
+ ___49-[DEDCloudKitFinisher resumeUploadingAttachments]_block_invoke
+ ___49-[DEDCloudKitFinisher resumeUploadingAttachments]_block_invoke_2
+ ___49-[DEDCloudKitFinisher resumeUploadingAttachments]_block_invoke_3
+ ___58-[DEDCloudKitFinisher startUploadingAttachmentGroupStatus]_block_invoke
+ ___59-[DEDCloudKitFinisher resumeUploadingAttachmentGroupStatus]_block_invoke
+ ___59-[DEDCloudKitFinisher resumeUploadingAttachmentGroupStatus]_block_invoke_2
+ ___87-[DEDCloudKitFinisher createAttachmentGroupStatusForAttachmentGroup:completionHandler:]_block_invoke
+ ___98-[DEDCloudKitClient uploadRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke
+ ___block_descriptor_40_e8_32s_e34_v32?0"NSString"8"NSArray"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_40_e8_32w_e45_v32?0"CKRecordID"8"CKRecord"16"NSError"24lw32l8
+ ___block_descriptor_56_e8_32s40s48bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64bs_e22_v16?0"BGSystemTask"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48bs56bs64bs72w_e17_v16?0"NSError"8lw72l8s32l8s48l8s40l8s56l8s64l8
+ _objc_msgSend$advanceState
+ _objc_msgSend$containerID
+ _objc_msgSend$createOperationWithRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$endWithError:
+ _objc_msgSend$handleOtherFailure:task:completionBlock:
+ _objc_msgSend$handlePartialFailure:records:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:
+ _objc_msgSend$initWithConfiguration:taskIdentifier:
+ _objc_msgSend$isBackgroundTaskExpiredError:
+ _objc_msgSend$operationID
+ _objc_msgSend$pendingRecords
+ _objc_msgSend$recordClasses
+ _objc_msgSend$recordID
+ _objc_msgSend$registerForTaskWithIdentifier:perRecordProgressBlock:perRecordSaveBlock:completionBlock:
+ _objc_msgSend$resumeUploadWithPerRecordProgressBlock:perRecordSaveBlock:completionBlock:
+ _objc_msgSend$resumeUploadingAttachmentGroupStatus
+ _objc_msgSend$resumeUploadingAttachments
+ _objc_msgSend$retryDelayForError:
+ _objc_msgSend$setModifyRecordsCompletionBlock:
+ _objc_msgSend$setPendingRecords:
+ _objc_msgSend$setSandboxEnvironment:
+ _objc_msgSend$shouldRetryError:
+ _objc_msgSend$startCompressing
+ _objc_msgSend$startUploadingAttachmentGroupStatus
+ _objc_msgSend$startUploadingAttachments
+ _objc_msgSend$uploadRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:
+ _objc_msgSend$uploadRecords:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:
+ _objc_msgSend$userInfo
- -[DEDCloudKitBaseModel addDependency:]
- -[DEDCloudKitBaseModel dependencies]
- -[DEDCloudKitBaseModel setDependencies:]
- -[DEDCloudKitClient bugSessionConfig]
- -[DEDCloudKitClient bugSession]
- -[DEDCloudKitClient initWithBugSession:configuration:]
- -[DEDCloudKitClient setBugSession:]
- -[DEDCloudKitClient setBugSessionConfig:]
- -[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]
- -[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:].cold.1
- GCC_except_table10
- _OBJC_IVAR_$_DEDCloudKitBaseModel._dependencies
- _OBJC_IVAR_$_DEDCloudKitClient._bugSession
- _OBJC_IVAR_$_DEDCloudKitClient._bugSessionConfig
- ___124-[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke
- ___124-[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.17
- ___124-[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.17.cold.1
- ___124-[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.19
- ___124-[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.19.cold.1
- ___124-[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke.19.cold.2
- ___124-[DEDCloudKitClient uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:]_block_invoke_2
- ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke
- ___55-[DEDCloudKitFinisher finishSession:withConfiguration:]_block_invoke.125
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48bs56w_e17_v16?0"NSError"8ls48l8s32l8s40l8w56l8
- ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs72bs_e22_v16?0"BGSystemTask"8ls32l8s40l8s48l8s56l8s64l8s72l8
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$dependencies
- _objc_msgSend$error
- _objc_msgSend$initWithBugSession:configuration:
- _objc_msgSend$setCloudKitModel:
- _objc_msgSend$setCompletionBlock:
- _objc_msgSend$setDependencies:
- _objc_msgSend$uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:
CStrings:
+ "%s error: %@"
+ "-[DEDCloudKitFinisher endWithError:]"
+ "-[DEDCloudKitFinisher resumeUploadingAttachmentGroupStatus]"
+ "-[DEDCloudKitFinisher resumeUploadingAttachments]"
+ "-[DEDCloudKitFinisher startCompressing]"
+ "-[DEDCloudKitFinisher startUploadingAttachmentGroupStatus]"
+ "-[DEDCloudKitFinisher startUploadingAttachments]"
+ "@56@0:8@16@24@?32@?40@?48"
+ "A"
+ "Created attachmentGroupModel with recordID %@"
+ "Creating retry operation for %lu failed records with delay of %.1f seconds"
+ "Executing operation %{public}@"
+ "Failed to expire task: %{public}@"
+ "Failed to save record: %@ with error: %{public}@"
+ "Finishing session with state %ld"
+ "Missing one or more required keys to decode (attachments: %@ uploadedBytes: %@)"
+ "Missing one or more required keys to decode (cloudKitModel: %@)"
+ "Missing one or more required keys to decode (container: %@ pendingRecords: %@)"
+ "No pending records to upload"
+ "No records to retry - all failures are non-retryable"
+ "Operation %{public}@ failed with error: %{public}@"
+ "Operation %{public}@ succeeded"
+ "Operation failed for record %@ with error: %{public}@"
+ "Operation failed with error: %{public}@. Scheduling retry after %{public}.1f seconds"
+ "Partial failure reported but no failed records found"
+ "Partial failure: %{public}lu records failed"
+ "Required properties are nil (attachmentGroupModel: %@)"
+ "Required properties are nil (attachments: %@, attachmentGroupModel: %@)"
+ "Required properties are nil (cloudKitClient: %@)"
+ "Starting CloudKit finishSession for session: %{public}@"
+ "State changed from %ld to %ld"
+ "Successfully saved %{public}lu records"
+ "Successfully saved record: %@"
+ "T@\"DEDCloudKitClient\",&"
+ "T@\"NSArray\",&,V_pendingRecords"
+ "T@\"NSString\",&,N,V_taskIdentifier"
+ "Task %{public}@ completed successfully"
+ "Task %{public}@ completed with error %{public}@; will not retry"
+ "Task %{public}@ expired; retry after %{public}.2f seconds"
+ "Task %{public}@ expired; retry after %{public}.2f seconds with %{public}lu records to retry"
+ "Tq"
+ "Upload request rejected; another upload is already in progress with %{public}lu pending records"
+ "Uploading %lu pending records for task %{public}@"
+ "Uploading %{public}lu records: %@"
+ "_pendingRecords"
+ "advanceState"
+ "com.apple.diagnosticextensionsd.CloudKitClient"
+ "container: %{public}@"
+ "containerID"
+ "createOperationWithRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "endWithError:"
+ "handleOtherFailure:task:completionBlock:"
+ "handlePartialFailure:records:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "initWithConfiguration:taskIdentifier:"
+ "isBackgroundTaskExpiredError:"
+ "operationID"
+ "pendingRecords"
+ "record"
+ "recordClasses"
+ "recordID"
+ "registerForTaskWithIdentifier:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "resumeUploadWithPerRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "resumeUploadingAttachmentGroupStatus"
+ "resumeUploadingAttachments"
+ "retryDelayForError:"
+ "setModifyRecordsCompletionBlock:"
+ "setPendingRecords:"
+ "shouldRetryError:"
+ "startCompressing"
+ "startUploadingAttachmentGroupStatus"
+ "startUploadingAttachments"
+ "taskID"
+ "uploadRecords:task:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "uploadRecords:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"
+ "userInfo"
+ "v32@?0@\"NSArray\"8@\"NSArray\"16@\"NSError\"24"
+ "v40@0:8@?16@?24@?32"
+ "v48@0:8@16@?24@?32@?40"
+ "v56@0:8@16@24@?32@?40@?48"
- "1"
- "CloudKit failed to save record: %@ with error: %@"
- "CloudKit successfully saved record: %@"
- "Expiring task %{public}@"
- "Failed to expire task %{public}@"
- "No additional CloudKit data was provided"
- "Operation completed successfully: %@"
- "Operation failed with error: %@"
- "Starting CloudKit finishSession with container: %{public}@"
- "T@\"DEDBugSession\",&,N,V_bugSession"
- "T@\"DEDBugSessionConfiguration\",&,N,V_bugSessionConfig"
- "T@\"DEDCloudKitClient\",&,N,V_cloudKitClient"
- "T@\"NSMutableArray\",&,N,V_dependencies"
- "Task %{public}@ completed"
- "Tq,N,V_state"
- "Uploading %lu records: %@"
- "_bugSession"
- "_bugSessionConfig"
- "_dependencies"
- "addDependency:"
- "bugSession"
- "bugSessionConfig"
- "cloudkitData: %{public}@"
- "decodeObjectForKey:"
- "dependencies"
- "initWithBugSession:configuration:"
- "setBugSession:"
- "setBugSessionConfig:"
- "setCompletionBlock:"
- "setDependencies:"
- "uploadRecords:taskIdentifier:totalUploadSize:perRecordProgressBlock:perRecordSaveBlock:completionBlock:"

```
