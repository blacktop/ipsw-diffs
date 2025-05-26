## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-1703.42.2.0.0
-  __TEXT.__text: 0xb80b8
-  __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_methlist: 0x49c4
-  __TEXT.__cstring: 0xab86
-  __TEXT.__oslogstring: 0xc0aa
+1703.62.4.0.0
+  __TEXT.__text: 0xb9f38
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_methlist: 0x4a44
+  __TEXT.__cstring: 0xae18
+  __TEXT.__oslogstring: 0xc062
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xbb08
+  __TEXT.__gcc_except_tab: 0xbf0c
   __TEXT.__ustring: 0x1796
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3354
+  __TEXT.__unwind_info: 0x33f8
   __TEXT.__objc_classname: 0x867
-  __TEXT.__objc_methname: 0x127a9
+  __TEXT.__objc_methname: 0x12aaf
   __TEXT.__objc_methtype: 0x49c5
-  __TEXT.__objc_stubs: 0xc8a0
-  __DATA_CONST.__got: 0x2f0
+  __TEXT.__objc_stubs: 0xcaa0
+  __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x34d0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xede0
-  __DATA_CONST.__objc_selrefs: 0x3b40
+  __DATA_CONST.__objc_const: 0xef60
+  __DATA_CONST.__objc_selrefs: 0x3c00
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__cfstring: 0x4c00
+  __AUTH_CONST.__cfstring: 0x4c20
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__objc_const: 0x1778
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x858
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH.__objc_data: 0x730
   __DATA.__objc_protorefs: 0x38
   __DATA.__objc_classrefs: 0x528

   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/FileProviderTelemetry.framework/FileProviderTelemetry
   - /System/Library/PrivateFrameworks/GenerationalStorage.framework/GenerationalStorage
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3788
-  Symbols:   11988
-  CStrings:  5203
+  Functions: 3815
+  Symbols:   12077
+  CStrings:  5238
 
Symbols:
+ -[FPDSharedScheduler _contextForActivity:]
+ -[FPDSharedScheduler dasContext]
+ -[FPDSharedScheduler isRegistered]
+ -[FPDSharedScheduler isRunning]
+ -[FPDSharedScheduler lastRegistrationDate]
+ -[FPDSharedScheduler lastTriggerDate]
+ -[FPDSharedScheduler lastUsageDate]
+ -[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]
+ -[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:].cold.1
+ -[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:].cold.2
+ -[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:].cold.3
+ -[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]
+ -[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:].cold.1
+ -[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:].cold.2
+ -[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:].cold.3
+ -[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]
+ -[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:].cold.1
+ -[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:].cold.2
+ -[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:].cold.3
+ GCC_except_table276
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table279
+ GCC_except_table280
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table283
+ GCC_except_table284
+ _FPClearImportCookieForDomainURL
+ _FPGetImportCookieForURL
+ _OBJC_CLASS_$__DASScheduler
+ __DASSchedulingPriorityBackground
+ __DASSchedulingPriorityDefault
+ __DASSchedulingPriorityMaintenance
+ __DASSchedulingPriorityUserInitiated
+ __DASSchedulingPriorityUserInitiatedOvercommit
+ __DASSchedulingPriorityUtility
+ ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke
+ ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.382
+ ___100-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke.cold.1
+ ___117-[FPDDomain _provideItemAtURL:withReaderID:withProcessID:withAuditToken:kernelInfo:readingOptions:completionHandler:]_block_invoke.155
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.100
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.100.cold.1
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.114
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.120
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.98
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.98.cold.1
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke_2.115
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke_2.127
+ ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke_3
+ ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.135
+ ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.135.cold.1
+ ___50-[FPDDomain _writerWithID:didFinishWritingForURL:]_block_invoke.157
+ ___55-[FPDDomain didChangeItemID:request:completionHandler:]_block_invoke.192
+ ___59-[FPDProvider removeDomain:mode:request:completionHandler:]_block_invoke.155
+ ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.324
+ ___64-[FPDDomain downloadVersionThumbnail:version:completionHandler:]_block_invoke.204
+ ___65-[FPDDomain _registerFileCoordinatorAndSpaceForceWithCompletion:]_block_invoke.176
+ ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.322
+ ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.314
+ ___70-[FPDXPCServicer reindexAllSearchableItemsWithAcknowledgementHandler:]_block_invoke.319
+ ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.318
+ ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.318.cold.1
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.317
+ ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.317.cold.1
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.334
+ ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.334.cold.1
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.365
+ ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.365.cold.1
+ ___82-[FPDXPCServicer dumpStateTo:limitNumberOfItems:providerFilter:completionHandler:]_block_invoke.296
+ ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.341
+ ___96-[FPDProvider _setEnabledOrHiddenByUser:forDomainIdentifier:newValue:request:completionHandler:]_block_invoke.174
+ ___96-[FPDProvider _setEnabledOrHiddenByUser:forDomainIdentifier:newValue:request:completionHandler:]_block_invoke.174.cold.1
+ ___96-[FPDProvider _setEnabledOrHiddenByUser:forDomainIdentifier:newValue:request:completionHandler:]_block_invoke.177
+ ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke
+ ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.379
+ ___96-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke.cold.1
+ ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke
+ ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.376
+ ___98-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke.cold.1
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96bs104bs112bs120bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s96l8s104l8s72l8s80l8s112l8s88l8s120l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88bs_e20_v20?0B8"NSError"12ls80l8s32l8s40l8s48l8s56l8s64l8s72l8s88l8
+ ___block_literal_global.132
+ ___block_literal_global.141
+ ___block_literal_global.157
+ ___block_literal_global.160
+ ___block_literal_global.165
+ ___block_literal_global.176
+ ___block_literal_global.181
+ ___block_literal_global.206
+ ___block_literal_global.327
+ ___block_literal_global.654
+ ___block_literal_global.657
+ __unnamed_array_storage.150
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_contextForActivity:
+ _objc_msgSend$cancelAfterDeadline
+ _objc_msgSend$cpuIntensive
+ _objc_msgSend$delayedStart
+ _objc_msgSend$entries
+ _objc_msgSend$importProgressForItemsPendingReconciliationWithCompletionHandler:
+ _objc_msgSend$importProgressForItemsPendingScanningDiskWithCompletionHandler:
+ _objc_msgSend$importProgressForItemsPendingScanningProviderWithCompletionHandler:
+ _objc_msgSend$isUpload
+ _objc_msgSend$memoryIntensive
+ _objc_msgSend$preventDeviceSleep
+ _objc_msgSend$requiresNetwork
+ _objc_msgSend$runningActivities
+ _objc_msgSend$schedulingPriority
+ _objc_msgSend$sessionForProviderID:version:
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$submittedActivities
+ _objc_msgSend$timeIntervalSinceReferenceDate
- _OBJC_CLASS_$_FPImportCookie
- ___117-[FPDDomain _provideItemAtURL:withReaderID:withProcessID:withAuditToken:kernelInfo:readingOptions:completionHandler:]_block_invoke.156
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.101
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.101.cold.1
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.115
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.121
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.128
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.99
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.99.cold.1
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke.cold.7
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke_2.116
- ___146-[FPDProvider addDomain:byImportingDirectoryAtURL:knownFolders:unableToStartup:needsReimport:startupError:reloadDomain:request:completionHandler:]_block_invoke_2.129
- ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.136
- ___35-[FPDDomain cleanupDomainWithMode:]_block_invoke.136.cold.1
- ___50-[FPDDomain _writerWithID:didFinishWritingForURL:]_block_invoke.158
- ___55-[FPDDomain didChangeItemID:request:completionHandler:]_block_invoke.193
- ___59-[FPDProvider removeDomain:mode:request:completionHandler:]_block_invoke.157
- ___63-[FPDXPCServicer fetchDaemonOperationIDsWithCompletionHandler:]_block_invoke.318
- ___64-[FPDDomain downloadVersionThumbnail:version:completionHandler:]_block_invoke.205
- ___65-[FPDDomain _registerFileCoordinatorAndSpaceForceWithCompletion:]_block_invoke.179
- ___68-[FPDXPCServicer scheduleActionOperationWithInfo:completionHandler:]_block_invoke.316
- ___70-[FPDXPCServicer copyDatabaseForFPCKStartingAtPath:completionHandler:]_block_invoke.308
- ___70-[FPDXPCServicer reindexAllSearchableItemsWithAcknowledgementHandler:]_block_invoke.313
- ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.312
- ___71-[FPDXPCServicer waitForStabilizationOfDomainWithID:completionHandler:]_block_invoke.312.cold.1
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.311
- ___73-[FPDXPCServicer waitForChangesOnItemsBelowItemWithID:completionHandler:]_block_invoke.311.cold.1
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.328
- ___74-[FPDXPCServicer startAccessingServiceWithName:itemURL:completionHandler:]_block_invoke.328.cold.1
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.359
- ___78-[FPDXPCServicer _test_callRemoveTrashedItemsOlderThanDate:completionHandler:]_block_invoke.359.cold.1
- ___82-[FPDXPCServicer dumpStateTo:limitNumberOfItems:providerFilter:completionHandler:]_block_invoke.290
- ___82-[FPDXPCServicer fetchAndStartEnumeratingWithSettings:observer:completionHandler:]_block_invoke.335
- ___96-[FPDProvider _setEnabledOrHiddenByUser:forDomainIdentifier:newValue:request:completionHandler:]_block_invoke.176
- ___96-[FPDProvider _setEnabledOrHiddenByUser:forDomainIdentifier:newValue:request:completionHandler:]_block_invoke.176.cold.1
- ___96-[FPDProvider _setEnabledOrHiddenByUser:forDomainIdentifier:newValue:request:completionHandler:]_block_invoke.179
- ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96bs104bs112bs120bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s96l8s104l8s72l8s80l8s112l8s88l8s120l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88bs_e17_v16?0"NSError"8ls80l8s32l8s40l8s48l8s56l8s64l8s72l8s88l8
- ___block_literal_global.133
- ___block_literal_global.145
- ___block_literal_global.146
- ___block_literal_global.161
- ___block_literal_global.167
- ___block_literal_global.178
- ___block_literal_global.182
- ___block_literal_global.207
- ___block_literal_global.321
- ___block_literal_global.655
- ___block_literal_global.658
- __unnamed_array_storage.152
- _objc_msgSend$clearCookieForDomainURL:error:
- _objc_msgSend$sessionForProvider:version:
- _objc_msgSend$writeCookieForDomainURL:error:
CStrings:
+ "-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]"
+ "-[FPDXPCServicer _test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:]_block_invoke"
+ "-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]"
+ "-[FPDXPCServicer _test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:]_block_invoke"
+ "-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]"
+ "-[FPDXPCServicer _test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:]_block_invoke"
+ "Date/Time:         %s, (%f)\n"
+ "Import Cookie: %@\n"
+ "T@\"NSDate\",R"
+ "TB,R,GisRegistered"
+ "TB,R,GisRunning"
+ "Tq,R"
+ "URLWithString:"
+ "[DEBUG] Found domain %@ with fast path for %@"
+ "_contextForActivity:"
+ "_test_importItemsPendingReconciliationProgressForDomainWithID:completionHandler:"
+ "_test_importItemsPendingScanningDiskProgressForDomainWithID:completionHandler:"
+ "_test_importItemsPendingScanningProviderProgressForDomainWithID:completionHandler:"
+ "cancelAfterDeadline"
+ "cpuIntensive"
+ "dasContext"
+ "delayedStart"
+ "entries"
+ "importProgressForItemsPendingReconciliationWithCompletionHandler:"
+ "importProgressForItemsPendingScanningDiskWithCompletionHandler:"
+ "importProgressForItemsPendingScanningProviderWithCompletionHandler:"
+ "isRunning"
+ "isUpload"
+ "lastRegistrationDate"
+ "lastTriggerDate"
+ "lastUsageDate"
+ "memoryIntensive"
+ "preventDeviceSleep"
+ "requiresNetwork"
+ "running"
+ "runningActivities"
+ "schedulingPriority"
+ "sessionForProviderID:version:"
+ "sharedScheduler"
+ "submittedActivities"
+ "timeIntervalSinceReferenceDate"
- "Date/Time:         %s\n"
- "[DEBUG] Found domain %{public}@ with fast path for %{public}@"
- "[ERROR] failed to write import cookie for domain %@: %@"
- "clearCookieForDomainURL:error:"
- "sessionForProvider:version:"
- "writeCookieForDomainURL:error:"

```
