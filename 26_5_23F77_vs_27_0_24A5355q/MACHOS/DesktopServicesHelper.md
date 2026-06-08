## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/DesktopServicesHelper`

```diff

-1827.5.1.0.0
-  __TEXT.__text: 0x6e06c
-  __TEXT.__auth_stubs: 0x17a0
-  __TEXT.__objc_stubs: 0x1d20
-  __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x78c
-  __TEXT.__const: 0x17f8
-  __TEXT.__gcc_except_tab: 0x8d78
-  __TEXT.__cstring: 0x1b77
-  __TEXT.__oslogstring: 0x13c8
-  __TEXT.__objc_classname: 0x12b
+1848.0.0.0.0
+  __TEXT.__text: 0x7f670
+  __TEXT.__auth_stubs: 0x1900
+  __TEXT.__objc_stubs: 0x1e80
+  __TEXT.__init_offsets: 0x8
+  __TEXT.__objc_methlist: 0x904
+  __TEXT.__gcc_except_tab: 0xa114
+  __TEXT.__const: 0x2fe0
+  __TEXT.__objc_methname: 0x1dcd
+  __TEXT.__objc_classname: 0x14c
+  __TEXT.__cstring: 0x27f4
+  __TEXT.__objc_methtype: 0x1448
+  __TEXT.__oslogstring: 0x3507
   __TEXT.__ustring: 0x1a
-  __TEXT.__objc_methname: 0x1c0b
-  __TEXT.__objc_methtype: 0xe9b
-  __TEXT.__unwind_info: 0x3190
-  __DATA_CONST.__auth_got: 0xbe0
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__const: 0x1bb0
-  __DATA_CONST.__cfstring: 0x7c0
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__unwind_info: 0x37d0
+  __DATA_CONST.__const: 0x2840
+  __DATA_CONST.__cfstring: 0x1420
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0xce8
-  __DATA.__objc_selrefs: 0x8f0
-  __DATA.__objc_ivar: 0x78
-  __DATA.__objc_data: 0x230
-  __DATA.__data: 0x448
-  __DATA.__bss: 0x8c0
-  __DATA.__common: 0x1be
+  __DATA_CONST.__auth_got: 0xc90
+  __DATA_CONST.__got: 0x500
+  __DATA.__objc_const: 0xfc0
+  __DATA.__objc_selrefs: 0x990
+  __DATA.__objc_ivar: 0x88
+  __DATA.__objc_data: 0x320
+  __DATA.__data: 0x4d1
+  __DATA.__bss: 0x900
+  __DATA.__common: 0x1a2
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/FileProvider.framework/FileProvider

   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
-  - /System/Library/PrivateFrameworks/CloudDocs.framework/CloudDocs
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2F4037DE-0B2E-3A83-9C7B-9F3F7A36613D
-  Functions: 1813
-  Symbols:   557
-  CStrings:  954
+  UUID: D938DCC6-29BA-3788-B647-DE12367029C6
+  Functions: 2140
+  Symbols:   577
+  CStrings:  1381
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFDataGetTypeID
+ _FPCopyLocalStorageDirectoryLocation
+ _IOBSDNameMatching
+ _IOObjectRelease
+ _IORegistryEntrySearchCFProperty
+ _IOServiceGetMatchingService
+ _NSURLLocalizedNameKey
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEl
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEm
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEy
+ __ZNSt3__120__libcpp_atomic_waitEPVKvx
+ __ZNSt3__123__cxx_atomic_notify_allEPVKv
+ __ZNSt3__123__libcpp_atomic_monitorEPVKv
+ __ZNSt3__19to_stringEm
+ __ZNSt3__19to_stringEx
+ __ZNSt3__19to_stringEy
+ __os_signpost_emit_with_name_impl
+ _getenv
+ _kIOMainPortDefault
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
+ _os_signpost_enabled
+ _os_signpost_id_generate
+ _os_signpost_id_make_with_pointer
+ _pthread_get_qos_class_np
+ _pthread_self
+ _pthread_set_qos_class_self_np
+ _xpc_connection_get_audit_token
- _CFDataAppendBytes
- _CFDataCreateMutable
- _CFDataCreateWithBytesNoCopy
- _CFStringCreateWithBytesNoCopy
- _NSKeyValueChangeNewKey
- _OBJC_CLASS_$_NSByteCountFormatter
- __ZNSt3__119piecewise_constructE
- ___assert_rtn
- ___cxa_rethrow
- _kCFAllocatorNull
- _objc_autorelease
- _objc_release_x1
- _objc_retainAutoreleasedReturnValue
- _objc_setProperty_nonatomic_copy
CStrings:
+ "%d write threads still active - %{public}@"
+ "%lu clone actions have not completed yet, bailing out."
+ "%zd = pread(%d, %{public}s, %llu, %llu) errno=%{errno}d fp_pos=%lld"
+ "%zd = pwrite(%d, %{public}s, %llu, %llu) errno=%{errno}d fp_pos=%lld"
+ "%{public}s\n\t Units: %lld / %lld -> %lld / %lld\n\t All Children Have Totals: %{bool}d\n\t Any Child Running: %{bool}d\n\t Parent Was Running: %{bool}d\n\t progress: %{public}@"
+ "%{public}s - childProgress isn't known yet. It should be.\n\t childProgress: %{public}@\n\t knownChildProgresses: %{public}@"
+ "%{public}s - count decreased from %lld to %lld"
+ "%{public}s - localStatus: %{public}s\n\t destination: %{public}@\n\t source: %{public}@\n\t name: %{public}@\n\t operationUUID: %{public}@"
+ "%{public}s - localStatus: %{public}s, source: %{public}@"
+ "%{public}s - operationUUID: %{public}@"
+ "%{public}s - source: %{public}@,\n\t dest: %{public}@,\n\t targetName: %{public}@\n\t operationUUID: %{public}@\n\t localStatus: %{public}s\n\t status: %{public}s"
+ "%{public}s - status: %{public}s\n\t destination: %{public}@\n\t source: %{public}@\n\t name: %{public}@"
+ "%{public}s not ready to clone, no source url ready yet"
+ "%{public}s not ready to clone, source still being written"
+ "%{public}s progress record for op UUID: %{public}@, op ID: %d for url: %{public}@\n\t totalItemCount: %lld, totalFSItemCount: %lld, totalByteCount: %lld"
+ "%{public}s: group progress: %{public}@\n\t _continuedUITask: %{public}@"
+ "%{public}s: read complete"
+ "%{public}s: sourcePath: %{public}s\n\t destinationPath: %{public}s\n\t targetName: %{public}s\n\t operationUUID: %{public}@\n\t status: %{public}s"
+ "-[DSFileServiceProgressGroup dealloc]"
+ "-[DSFileServiceProgressGroup observeChildProgress:]"
+ "-[DSFileServiceProgressGroup sumChildUnitCounts]"
+ ".resolve"
+ "/System/Library/LaunchDaemons/com.apple.DesktopServicesHelper-libgmalloc.plist"
+ ": "
+ "@\"NSMutableDictionary\"8@?0"
+ "Action Queue: %{public}@, count: %lu"
+ "Adding"
+ "Adding progress record for op UUID: %{public}@, op ID: %d for srcURL: %{public}@\n\t destURL: %{public}@\n\t progress: %{public}@"
+ "AlertMsg"
+ "BGContinuedProcessingTaskContext"
+ "BackgroundQOSClass"
+ "Begin%{public}s%{public}s"
+ "Cancel"
+ "Canceling progress group %{public}@ after copyError=%{public}s"
+ "Cancelled - %{public}@"
+ "Ciao"
+ "Clone Queue: %{public}@, count: %lu"
+ "Cloning %{public}s"
+ "CompletedBytes"
+ "CompletedFSItems"
+ "CompletedVisibleItems"
+ "CopyClientActive"
+ "CopyReader"
+ "CopyReader_Drain"
+ "CopyWriter"
+ "CopyWriter: pwrite failed. status: %{public}s errno: %{errno}d"
+ "CopyWriter_Drain"
+ "CopyXattrNamesForCompare: xattr name is not valid UTF-8: %{public}s"
+ "DSEnumeration_SMB"
+ "DSEnumeration_USB"
+ "DSFileService -- Error fetching display name. Falling back to raw name: %{public}@, error: %{public}@"
+ "DSFileServiceProgressGroup -cancel: %{public}@"
+ "DSFileServiceProgressGroup -cancellationHandler: children: %lu, progress: %{public}@"
+ "DSFileServiceProgressGroup -pausingHandler: children: %lu, progress: %{public}@"
+ "DSFileServiceProgressGroup -publish: %{public}@"
+ "DSFileServiceProgressGroup -resumingHandler: children: %lu, progress: %{public}@"
+ "DSFileServiceProgressGroup -unpublish: %{public}@"
+ "DSFileServiceProgressGroup childProgress -cancellationHandler: %{public}@\n\t group progress: %{public}@"
+ "DSFileServiceProgressGroup childProgress -pausingHandler: %{public}@\n\t group progress: %{public}@"
+ "DSFileServiceProgressGroup childProgress -resumingHandler: %{public}@\n\t group progress: %{public}@"
+ "DSFileServiceProgressGroup received BGTask: %{public}@\n\t %{public}@"
+ "DSFileServiceProgressGroup requesting BGTask: %{public}@"
+ "DSProgress registerChildProgress: Added child to %{public}@ - new count: %lu"
+ "DSProgress: unregisterChildProgress from %{public}@ - new count: %lu"
+ "DYLD_INSERT_LIBRARIES"
+ "DstFS"
+ "DstIsICloud"
+ "DstPathMultiByteChars"
+ "End"
+ "Error %{public}s at path: %{public}@ on %{public}s\n\t url: %{public}@\n\t Backtrace: %{public}@"
+ "Error fetching realpath \"%{public}@\" errno=%{errno}d"
+ "Error fetching realpath \"%{public}@\" while resolving '%{public}@' errno=%{errno}d"
+ "Error(%{errno}d) removing xattr %{public}s from %{public}@"
+ "ErrorMessage"
+ "Exiting write, error %{public}s"
+ "FIAnalytics"
+ "FIAnalyticsOperationRecord"
+ "FIAnalyticsRecord"
+ "FIOperationUUID"
+ "Failed client clone. status: %{public}s"
+ "Failed client move. status: %{public}s"
+ "Failed clone %{public}s, cloneID %llu, %{public}s"
+ "Failed copying extent from %{public}@ to %{public}@, error: %{public}s"
+ "Failed link. status: %{public}s"
+ "Failed preserved clone link. status: %{public}s"
+ "Failed to fetch local storage domain %{public}@"
+ "Failed to get operation UUID"
+ "File %{public}s -- deferring creation onto secondary copy thread"
+ "FileSystemItemsCompleted"
+ "FileSystemItemsTotal"
+ "ForceAppearsAsDestinationHighThroughputSSDOptimization"
+ "ForceDiskAppearAsSameDevice"
+ "ForceDisksToAppearAsSSD"
+ "ForceSourceAppearsAsHighThroughputSSDOptimization"
+ "ForegroundQOSClass"
+ "Found two progress objects with the same UUID.\t\n Knonwn: %{public}@\n\n\t new: %{public}@"
+ "Got Request '%{public}@'"
+ "HandleChildCreateLockMsgAsync_block_invoke"
+ "HandleOperationSizingMsgAsync_block_invoke"
+ "HandleRunCopyMoveOperationMsgAsync_block_invoke_2"
+ "High Throughput Options"
+ "IOService"
+ "Ignoring failed clone from %{public}@ to %{public}@, file already exists."
+ "IsCopyExactly"
+ "IsSystemRestore"
+ "IsVolumeRestore"
+ "ItemType"
+ "Items left for cleanup: %{public}s"
+ "LastStage"
+ "Notifying: copy done: %{public}@"
+ "Notifying: end of record: %{public}@"
+ "NumRootItems"
+ "OperationRootItemCount"
+ "OperationUUID"
+ "Progress"
+ "Publishing progress for srcURL: %{public}@\n\t destURL: %{public}@\n\t progress: %{public}@"
+ "R"
+ "Read Queue: %{public}@"
+ "Reader Finalizing"
+ "Reader GetNextItem Setup: %{public}s"
+ "Reader GetNextItem: %{public}s"
+ "Reader closed data fork for %{public}s, done. source info %p %{public}s"
+ "Reader error %{public}s: %{public}s"
+ "Reader failed to get next item: %{public}s, item: %{public}s"
+ "Reading (%lu) - source: '%{public}s', dest: '%{public}s'"
+ "RunCopyMove"
+ "SetFSItemsCompletedCount"
+ "SetFSItemsTotalCount"
+ "SetReadCompleted"
+ "SetVisibleFSItemsCompletedCount"
+ "SetVisibleFSItemsTotalCount"
+ "Signaling writer work batch changed. %d writes left, %ld batched left"
+ "Signalling reader work batch changed. %ld batched left"
+ "SrcFS"
+ "SrcIsICloud"
+ "SrcNameMultiByteChars"
+ "SrcPathMultiByteChars"
+ "Status"
+ "SubKind"
+ "T@\"BGContinuedProcessingTask\",&"
+ "T@\"FIProviderDomain\",R"
+ "T@\"NSMutableDictionary\",R,N,V_eventDict"
+ "T@\"NSString\",R,N,V_displayName"
+ "T@\"NSString\",R,N,V_eventName"
+ "T@?,C,D,N"
+ "TCFURLInfo::TranslateCFError -- status: %{public}s\n\t CFError: %{public}@\n\t Backtrace:\n%{public}@"
+ "TCFURLInfo::TranslateRawPOSIXError %{errno}d -> %{public}s, path: %{public}@\n%{public}@"
+ "TCopyReader::Read: Got to unknown read step"
+ "TCopyWriter::UpdateStatusBytesCompleted - amount: %llu, fAmountWritten: %llu, fRootItemAmountWritten: %llu, fBytesCompleted: %llu, fBytesTotal: %llu, %{public}@"
+ "TCopyWriter::UpdateStatusItemsCompleted - userVisibleItemsCount: %llu, fileSystemItemsCount: %llu, fFSItemsCompleted: %llu, fItemsTotal: %llu, fFSItemsCompleted: %llu, fFSItemsTotal: %llu, %{public}@"
+ "THelperOperationStateMap adding op ID: %d"
+ "THelperOperationStateMap already contains op ID: %d"
+ "THelperProgressMap -- Error fetching display name. Falling back to raw name: %{public}@, error: %{public}@"
+ "THelperProgressMap removing: %{public}@ (%{public}@ / %d / %lu)"
+ "THelperProgressMap::Finalize unpublish: %{public}@"
+ "THelperProgressMap::UpdateProgressPriv - url: %{public}@\n\t Unit: %lld / %lld -> %lld / %lld\n\t Byte: %lld / %lld -> %lld / %lld\n\t File: %lld / %lld -> %lld / %lld\n\t Items: %lld / %lld -> %lld / %lld\n\t Visible Items: %lld / %lld -> %lld / %lld\n\t progress: %{public}@"
+ "Tags"
+ "Timed out waiting for the write queue to drain after %llu usec"
+ "TotalBytes"
+ "TotalFSItems"
+ "TotalVisibleItems"
+ "Unable to CopyLocalStorageDirectoryLocation"
+ "Unable to find progress group for cancelling group %{public}@"
+ "Unable to get local storage domain creating placeholder with root url %{public}@"
+ "Unable to get local storage path"
+ "Unexpected copy span: %p, type: %d"
+ "Unpublishing progress for srcURL: %{public}@\n\t destURL: %{public}@\n\t old progress: %{public}@"
+ "Unpublishing progress for url: %{public}@\n\t progress: %{public}@"
+ "Updating"
+ "Updating progress record for op UUID: %{public}@, op ID: %d for srcURL: %{public}@\n\t destURL: %{public}@\n\t old progress: %{public}@\n\t new progress: %{public}@"
+ "Updating published progress for op UUID: %{public}@, op ID: %d for url: %{public}@\n\t totalItemCount: %lld, totalFSItemCount: %lld, totalByteCount: %lld\n\t progress: %{public}@"
+ "VisibleFileSystemItemsCompleted"
+ "VisibleFileSystemItemsTotal"
+ "Waiting: copy done: %{public}@"
+ "Waiting: end of record: %{public}@"
+ "Write Queue: '%{public}@', timeout: %{public}s"
+ "Write completed, notify write threads to exit: %{public}@"
+ "Write finishing but copy queue still contains unprocessed items - %{public}@"
+ "Write thread complete: %{public}@"
+ "Writer closed data fork for %{public}s, done"
+ "Writer could not find cached clone for preservation. status: %{public}s"
+ "Writer exiting with status %{public}s"
+ "Writing: %{public}@"
+ "^([[:alpha:]][[:alpha:][:digit:].+-]*)://"
+ "_auditTokensByOperationUUID"
+ "_displayName"
+ "_eventDict"
+ "_eventName"
+ "_pendingChildProgressCount"
+ "_unitCountObservers"
+ "_uuidToChildProgressMap"
+ "active"
+ "after using with item %llu, recycled buffer %p"
+ "backupCaseSensitivityErr"
+ "backupInvalidFormatErr"
+ "backupOwnershipIgnoredErr"
+ "backupProtectedErr"
+ "bufferTooSmallErr"
+ "busyApplicationErr"
+ "cannotCoerceErr"
+ "cannotResolveAliasErr"
+ "cantCopyAliasOrSymLinkErr"
+ "caseInsensitivityCopyErr"
+ "childProgressCount"
+ "childProgressesLocked"
+ "com.apple.DesktopServicesHelper-libgmalloc"
+ "com.apple.DesktopServicesHelper-libgmalloc.plist is not present - falling back"
+ "com.apple.finder.copymove.result"
+ "com.apple.finder.emptytrash.result"
+ "compareFailedErr"
+ "copy done: %{public}@"
+ "copyErr"
+ "createNewRequestForOperationUUID:"
+ "created new file %{public}s, %{public}s"
+ "creating item %{public}s at %{public}s"
+ "dataUnavailableErr"
+ "delayed clone of %{public}s"
+ "dequeue error %{public}s"
+ "destinationInvisibleNameConflictErr"
+ "destinationLockedErr"
+ "destinationOwnershipIgnoredErr"
+ "destinationPermissionsErr"
+ "directoryChangedErr"
+ "disk"
+ "displayName"
+ "dsHelperCrashedErr"
+ "end"
+ "end of record: %{public}@"
+ "error %{public}s closing reading fork, item: %{public}s"
+ "error %{public}s getting next item, bailing"
+ "error %{public}s opening data fork %{public}s"
+ "error %{public}s reading data fork, item: %{public}s"
+ "error %{public}s unexpected"
+ "error %{public}s, item %{public}s"
+ "error reading from %{public}@ to %{errno}d"
+ "error writing from %{public}@ to %{errno}d"
+ "estimatedTimeRemaining"
+ "eventDict"
+ "eventName"
+ "executing %ld queued up actions"
+ "executing %lu queued clone actions"
+ "failed opening %{public}@ for reading, %{public}s"
+ "failed opening %{public}@ for writing, %{public}s"
+ "failed to clone from %{public}@ to %{public}@, %d, %{public}s"
+ "failed to fcntl at offset %lld, file %{public}@, %{errno}d\n"
+ "fatal read error %{public}s, cancelling: %{public}s"
+ "fileHasConflictsErr"
+ "forkOpenAlreadyErr"
+ "fpItemFaultNeedsToBeDownloaded"
+ "fpItemNameConflictErr"
+ "got %{public}s while handling %{public}s"
+ "got %{public}s while trying to create %{public}s, child: %{public}s, destination %{public}s"
+ "handleContinuousProcessingTask:withOperationUUID:"
+ "iCloudFaultConflictErr"
+ "immediate creation of clone %{public}s"
+ "inconsistentRegistrationErr"
+ "indefinitely"
+ "initWithEventName:"
+ "initWithIdentifier:title:subtitle:context:"
+ "initWithUUID:operationKind:opRootItemCount:publishingURL:displayName:dateStarted:utType:"
+ "internalError"
+ "invalidNameErr"
+ "invalidNodeErr"
+ "invalidParameterErr"
+ "invalidPathErr"
+ "invalidSearchErr"
+ "invalidSearchQueueErr"
+ "invalidVRefNumErr"
+ "isCancellable"
+ "isFinished"
+ "isSMBDomain"
+ "isSMBFPv2Domain"
+ "isUSBDomain"
+ "isUSBFPv2Domain"
+ "isUSBOrSMBDeviceDomain"
+ "isUSBOrSMBDeviceFPv2Domain"
+ "item %{public}s DONE WRITING"
+ "item %{public}s marked as failed, deleting"
+ "item %{public}s not copied because error %{public}s"
+ "itemLockedInParentErr"
+ "iteratorPostOrderSuccessErr"
+ "kCopyBuffer id: %d"
+ "kEndOfCopy"
+ "kEndOfFailedItem"
+ "kEndOfFolderCopyItem"
+ "kEndOfRecordItem"
+ "kExtendedAttributeItem"
+ "kFileCloneAndDeltaItem"
+ "kFileCopyItem %{public}s, id: %d"
+ "kFolderCopyItem %{public}s"
+ "kWriterCloseDataFork failed: %{public}s - %{public}s"
+ "kWriterCreateItem failed: %{public}s - %{public}s"
+ "kWriterWriteDataFork failed: %{public}s - %{public}s"
+ "kWriterWriteExtendedAttributes failed: %{public}s - %{public}s"
+ "libgmalloc"
+ "localStorageDomain"
+ "mixedSelectionErr"
+ "needsRecalculationErr"
+ "no clone ID for %{public}s"
+ "noChangeErr"
+ "notABackupErr"
+ "notAClippingErr"
+ "notAContainerErr"
+ "notAFileSystemObjectErr"
+ "notAVolumeErr"
+ "notAnAliasErr"
+ "notFoundErr"
+ "notavailableErr"
+ "nothingToDoErr"
+ "nullptr"
+ "numberWithBool:"
+ "numberWithUnsignedInteger:"
+ "observeChildProgress:"
+ "operationCompletedErr"
+ "operationDestinationLockFailedErr"
+ "operationInProgressErr"
+ "operationLockFailedErr"
+ "operationSourceLockFailedErr"
+ "operator()"
+ "pread failed %{errno}d"
+ "propertyStoreNotOpenErr"
+ "propertyTooLargeErr"
+ "proxyContextForAuditToken:"
+ "pwrite failed %{errno}d"
+ "q"
+ "queue cancelled"
+ "queue drained"
+ "queue not drained"
+ "queued action failed: %{public}s"
+ "queued clone action failed: %{public}s"
+ "read failed for %{public}s, recovering: %{public}s"
+ "read not completed - %{public}@"
+ "readOnlyPropertyErr"
+ "reader thread done"
+ "reader thread queueing up reads of item %{public}s"
+ "reader thread reading data fork for %{public}s"
+ "registerAuditToken:forOperationUUID:"
+ "requiredBySystemErr"
+ "reusing buffer %p, queue size %ld"
+ "running copy metadata on %{public}s\n"
+ "scheduling a write on secondary thread"
+ "secondary thread batch not empty: %lu - %{public}@"
+ "selfRepairErr"
+ "sendAnalytics:"
+ "sendEvent:eventDictionary:"
+ "setBool:forKey:"
+ "setFileSystem:forKey:"
+ "setItemType:"
+ "setObject:forKey:"
+ "sharedAnalytics"
+ "skipChildErr"
+ "sourcePermissionsErr"
+ "srcNotDeletedAfterForceMoveErr"
+ "status %s, thread status %s"
+ "still have pending queued up actions: %lu - %{public}@"
+ "stringByRemovingPercentEncoding"
+ "submitTaskRequest:completionHandler:"
+ "sumChildUnitCounts"
+ "temporaryDirectory"
+ "threaded (4 reader threads, 4 writer threads, 2 extra)"
+ "too many open file descriptors open, waiting for queue to drain before opening %{public}s"
+ "too many open file descriptors open, waiting for queue to drain before opening %{public}s, %{public}s"
+ "too many open file descriptors open, waiting for queue to drain before opening next item"
+ "unableToAcquireReservationErr"
+ "unknownPropertyErr"
+ "unregisterChildProgress:"
+ "userCanceledErr"
+ "usesDSCopyEngine"
+ "using a custom value %lld for MaxActiveReadThreads"
+ "using a custom value %lld for MaxActiveWriteThreads"
+ "using a custom value %lld for MaxReadThreads"
+ "using a custom value %lld for MaxWriteThreads"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8Q16"
+ "v28@0:8B16@20"
+ "v32@0:8@16@?24"
+ "v32@0:8Q16@24"
+ "v56@0:8{?=[8I]}16@48"
+ "validate"
+ "waiting for write and action queues to drain"
+ "willCauseNetworkIOErr"
+ "write complete or canceled, exiting"
+ "write complete: %{public}@"
+ "write done for %{public}s, buffer %p"
+ "writer about to write data for for %{public}s"
+ "writer cancelled"
+ "{unordered_map<NSProgress *, std::pair<TKeyValueObserver, TKeyValueObserver>, std::hash<NSProgress *>, std::equal_to<NSProgress *>, std::allocator<std::pair<NSProgress *const, std::pair<TKeyValueObserver, TKeyValueObserver>>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSProgress *, std::pair<TKeyValueObserver, TKeyValueObserver>>, std::__unordered_map_hasher<NSProgress *, std::pair<NSProgress *const, std::pair<TKeyValueObserver, TKeyValueObserver>>, std::hash<NSProgress *>, std::equal_to<NSProgress *>>, std::__unordered_map_equal<NSProgress *, std::pair<NSProgress *const, std::pair<TKeyValueObserver, TKeyValueObserver>>, std::equal_to<NSProgress *>, std::hash<NSProgress *>>, std::allocator<std::pair<NSProgress *const, std::pair<TKeyValueObserver, TKeyValueObserver>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, std::pair<TKeyValueObserver, TKeyValueObserver>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, std::pair<TKeyValueObserver, TKeyValueObserver>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, std::pair<TKeyValueObserver, TKeyValueObserver>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, std::pair<TKeyValueObserver, TKeyValueObserver>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_map<NSUUID *, audit_token_t, std::hash<NSUUID *>, std::equal_to<NSUUID *>, std::allocator<std::pair<NSUUID *const, audit_token_t>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSUUID *, audit_token_t>, std::__unordered_map_hasher<NSUUID *, std::pair<NSUUID *const, audit_token_t>, std::hash<NSUUID *>, std::equal_to<NSUUID *>>, std::__unordered_map_equal<NSUUID *, std::pair<NSUUID *const, audit_token_t>, std::equal_to<NSUUID *>, std::hash<NSUUID *>>, std::allocator<std::pair<NSUUID *const, audit_token_t>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSUUID *, audit_token_t>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSUUID *, audit_token_t>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSUUID *, audit_token_t>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSUUID *, audit_token_t>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "\x83e"
- "%zd = pread(%d, %s, %llu, %llu) errno=%d fp_pos=%lld"
- "%zd = pwrite(%d, %s, %llu, %llu) errno=%d fp_pos=%lld"
- "1 0"
- "B8@?0"
- "Canceling progress group %{public}@ after copyError=%d"
- "CopyWriter: pwrite failed. status=%d errno=%d"
- "DSProgress setUpGroupForChildProgress: Added child to %{public}@ - new count: %lu"
- "DSProgress: addChildProgress: final total count: %{public}@"
- "DSProgress: removeChildProgress from %{public}@ - new count: %lu"
- "DefeatSSDOptimization"
- "DesktopServicesHelperMain.mm"
- "DesktopServicesHelper_connection_handler"
- "Error %d at path: %{public}@ on %{public}s"
- "Error %d with no path"
- "Error fetching realpath \"%{public}@\" errno=%d"
- "Error fetching realpath \"%{public}@\" while resolving '%{public}@' errno=%d"
- "Error(%d) removing xattr %{public}s from %{public}@"
- "Failed client clone. status=%d"
- "Failed client move. status=%d"
- "Failed clone. status=%d"
- "Failed link. status=%d"
- "Failed preserved clone link. status=%d"
- "Got Request %{public}@"
- "GroupCount"
- "GroupUUID"
- "HelperProgressMap removing: %{public}@ (%d)"
- "HelperProgressMap::Finalize unpublish"
- "Other error "
- "T@\"BGContinuedProcessingTask\",&,V_continuedUITask"
- "T@\"NSMutableDictionary\",R,N,V_childProgresses"
- "T@\"NSString\",R,N,V_firstChildName"
- "T@?,C,N,V_requestBGTask"
- "TCFURLInfo::TranslateCFError -- status: %{public}@, CFError = %@"
- "TCFURLInfo::TranslateRawPOSIXError %d (%{public}s) -> %{public}s, path: %{public}@"
- "THelperOperationStateMap adding: %d"
- "THelperOperationStateMap already contains: %d"
- "Unable to find progress group for %{public}@"
- "Writer could not find cached clone for preservation. status=%d"
- "_childProgresses"
- "_completedUnitCountObservers"
- "_firstChildName"
- "_hasRequestedBGTask"
- "addChildProgress:"
- "com.apple.DocumentsApp"
- "completedUnitCountDidChange:forProgress:"
- "createNewRequestForGroupUUID:"
- "emoji"
- "firstChildName"
- "folderEmpty"
- "h"
- "handleContinuousProcessingTask:withGroupUUID:"
- "initWithIdentifier:title:subtitle:onBehalfOf:"
- "initWithUUID:operationKind:groupCount:publishingURL:firstChildName:dateStarted:utType:"
- "isExternalDeviceDomain"
- "numberWithInt:"
- "peerEventQueue != nullptr"
- "removeChildProgress:"
- "setFolderEmpty:"
- "setSystemTintColor:"
- "setUpGroupForChildProgress:"
- "stringFromByteCount:countStyle:"
- "submitTaskRequest:error:"
- "symbolName"
- "systemTintColor"
- "threaded"
- "using a custom value %lld for MaxActiveReadThreads\n"
- "using a custom value %lld for MaxActiveWriteThreads\n"
- "using a custom value %lld for MaxReadThreads\n"
- "using a custom value %lld for MaxWriteThreads\n"
- "v44@?0r^v8q16q24q32B40"
- "{atomic<bool>=\"__a_\"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>=\"__a_value\"AB}}"
- "{unordered_map<NSProgress *, TKeyValueObserver, std::hash<NSProgress *>, std::equal_to<NSProgress *>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSProgress *, TKeyValueObserver>, std::__unordered_map_hasher<NSProgress *, std::pair<NSProgress *const, TKeyValueObserver>, std::hash<NSProgress *>, std::equal_to<NSProgress *>>, std::__unordered_map_equal<NSProgress *, std::pair<NSProgress *const, TKeyValueObserver>, std::equal_to<NSProgress *>, std::hash<NSProgress *>>, std::allocator<std::pair<NSProgress *const, TKeyValueObserver>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSProgress *, TKeyValueObserver>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"

```
