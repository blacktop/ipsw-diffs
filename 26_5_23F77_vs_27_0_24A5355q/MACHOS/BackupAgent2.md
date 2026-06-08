## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2969.120.2.0.0
-  __TEXT.__text: 0x9da2c
-  __TEXT.__auth_stubs: 0x18a0
-  __TEXT.__objc_stubs: 0xd020
-  __TEXT.__objc_methlist: 0x6730
-  __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x18e91
-  __TEXT.__oslogstring: 0xdf4b
-  __TEXT.__objc_methname: 0xf4c5
-  __TEXT.__objc_classname: 0xa9f
-  __TEXT.__objc_methtype: 0x1f94
-  __TEXT.__gcc_except_tab: 0x25c8
-  __TEXT.__unwind_info: 0x1bf0
-  __DATA_CONST.__auth_got: 0xc60
-  __DATA_CONST.__got: 0x528
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1550
-  __DATA_CONST.__cfstring: 0x9940
-  __DATA_CONST.__objc_classlist: 0x3a0
-  __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0xa0
+3033.0.0.0.0
+  __TEXT.__text: 0x906c4
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_stubs: 0xc900
+  __TEXT.__objc_methlist: 0x5fa4
+  __TEXT.__const: 0x4b8
+  __TEXT.__cstring: 0x18e7c
+  __TEXT.__oslogstring: 0xde37
+  __TEXT.__objc_methname: 0xe7b4
+  __TEXT.__objc_classname: 0x9ee
+  __TEXT.__objc_methtype: 0x1e71
+  __TEXT.__gcc_except_tab: 0x2104
+  __TEXT.__unwind_info: 0x1950
+  __DATA_CONST.__const: 0x1428
+  __DATA_CONST.__cfstring: 0x9520
+  __DATA_CONST.__objc_classlist: 0x378
+  __DATA_CONST.__objc_catlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__objc_arrayobj: 0xc0
+  __DATA_CONST.__objc_arraydata: 0x110
+  __DATA_CONST.__objc_arrayobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xa430
-  __DATA.__objc_selrefs: 0x4078
-  __DATA.__objc_ivar: 0x5e0
-  __DATA.__objc_data: 0x2440
-  __DATA.__data: 0x878
+  __DATA_CONST.__auth_got: 0xc38
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__objc_const: 0x9820
+  __DATA.__objc_selrefs: 0x3c88
+  __DATA.__objc_ivar: 0x54c
+  __DATA.__objc_data: 0x22b0
+  __DATA.__data: 0x818
   __DATA.__bss: 0x220
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3664D154-79C0-3CC7-A114-613903A4FF3D
-  Functions: 2595
-  Symbols:   574
-  CStrings:  8519
+  UUID: F70CBF9B-D135-37A8-81AA-6412D714FC04
+  Functions: 2446
+  Symbols:   558
+  CStrings:  8237
 
Symbols:
+ _fchownat
+ _fcopyfile
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x2
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _NSURLAuthenticationMethodClientCertificate
- _NSURLAuthenticationMethodServerTrust
- _NSURLErrorDomain
- _OBJC_CLASS_$_AKAppleIDSession
- _OBJC_CLASS_$_NSHTTPURLResponse
- _OBJC_CLASS_$_NSMutableURLRequest
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$_NSURLConnection
- _OBJC_CLASS_$_PBCodable
- _OBJC_METACLASS_$_PBCodable
- _PBDataWriterWriteDataField
- _PBDataWriterWriteInt32Field
- _PBDataWriterWriteStringField
- _PBDataWriterWriteSubmessage
- _PBDataWriterWriteUint32Field
- _PBDataWriterWriteUint64Field
- _PBReaderPlaceMark
- _PBReaderReadData
- _PBReaderReadString
- _PBReaderRecallMark
- _PBReaderSkipValueWithTag
- _dispatch_release
- _kCFURLRequestPreAuthXMMeAuthToken
- _objc_setProperty_nonatomic
CStrings:
+ "!_isPerformingBatch || _lastCommitFailed"
+ "%{public}@, uploadBatchSize:%lu, concurrentUploadBatchCount:%lu usingSemaphore:%d"
+ "(flags & O_CREAT) == 0"
+ "+[MBFileOperation createDirectories:permissions:owner:group:error:]"
+ "+[MBFileOperation createOrOpenFD:baseFD:rpath:flags:mode:error:]"
+ "+[MBFileOperation createOrOpenFD:path:flags:mode:error:]"
+ "-[MBFileScanner _foundFile:snapshotPath:context:stats:]"
+ "-[MBFileScanner _performSinglePassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:direntCount:directoryPathStack:directoryCountStack:context:stats:]"
+ "-[MBFileScanner _shouldNotBackupFile:domain:context:]"
+ "-[MBPQLBatchTracker dealloc]"
+ "-[MBPQLBatchTracker incrementCountWithError:]"
+ "-[MBSuspendingClock clockByAddingPositiveTimeInterval:]"
+ "/private/var/installd/Library/MobileInstallation/BackedUpState/BackupSystemAppInstallState.plist"
+ "/private/var/installd/Library/MobileInstallation/BackedUpState/SystemAppInstallState.plist"
+ "/private/var/mobile/Library/Caches/Backup/DT"
+ "/private/var/mobile/tmp/com.apple.backup.testing"
+ "/private/var/root/Library/Caches/Backup"
+ "/private/var/tmp/backupd-XXXXXXXXXXXXXXX"
+ "/private/var/tmp/com.apple.backup"
+ "/private/var/tmp/com.apple.backup.testing"
+ "=restorable= Creating missing parent directories at %@ (0%3o)"
+ "=restorable= Failed to check if parent of %@ exists: %@"
+ "=scanning= Failed scanning domain %{public}@ - %@: %@"
+ "=scanning= Finished scanning domain %{public}@ - %@"
+ "@\"NSError\"40@0:8@\"MBFileScanner\"16@\"MBFile\"24@32"
+ "@24@0:8d16"
+ "@32@0:8^i16r^*24"
+ "@48@0:8@16@24@32^{_MBFileScannerDomainStats=qqqQQQQQQ}40"
+ "@72@0:8@16@24@32@40@48@56^{_MBFileScannerDomainStats=qqqQQQQQQ}64"
+ "@88@0:8@16@24@32@40i48I52@56@64@72^{_MBFileScannerDomainStats=qqqQQQQQQ}80"
+ "B32@0:8^{?=IIIIqqqqQIQSC{?=b1b1b1}}16^@24"
+ "B32@?0@\"MBFileSystemSnapshot\"8Q16^B24"
+ "B40@0:8@\"MBFileScanner\"16@\"MBFile\"24@32"
+ "B44@0:8@\"MBFileScanner\"16@\"MBFile\"24i32@36"
+ "B44@0:8@16@24i32@36"
+ "B44@0:8@16S24I28I32^@36"
+ "B48@0:8^i16@24i32S36^@40"
+ "B52@0:8^i16i24@28i36S40^@44"
+ "BEGIN TRANSACTION"
+ "COMMIT"
+ "CREATE INDEX IF NOT EXISTS FilesDomainsRelativePathIdx ON Files(domain, relativePath);"
+ "Cannot call copyfile() on root dir"
+ "Copied system app plist from %@ to %@"
+ "DROP INDEX IF EXISTS FilesDomainIdx;"
+ "Error opening SQLite file to calculate freelist ratio: %s (%d/0x%x)"
+ "Failed to copy system app plist: %@"
+ "Failed to open %@ when trying restore parent of %@"
+ "Failed to validate backup"
+ "Fetched xattrs for %@:%{public}@ count:%llu"
+ "MBNodeForFD"
+ "MBPQLBatchTracker"
+ "MBSuspendingClock.m"
+ "Only annotating domains with system files to always remove on restore"
+ "Q24@0:8^@16"
+ "Skipped rename from %@ to %@: %@"
+ "Snapshot %@ not found for volume %@"
+ "TQ,R,N,V_completedBatchCount"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
+ "Unable to create /private/var/tmp/backupd-XXXXXXXXXX directory (strdup)"
+ "_batchCount"
+ "_completedBatchCount"
+ "_currentCount"
+ "_delegateRespondsToIsFileAddedOrModified"
+ "_failedToCompactSQLiteDatabase:"
+ "_foundFile:snapshotPath:context:stats:"
+ "_initWithStartTime:"
+ "_isPerformingBatch"
+ "_lastCommitFailed"
+ "_lastModifiedDateBySQLiteFileIDLock"
+ "_mb_openatWithMode failed for directory"
+ "_mb_openatWithMode failed for invalid file type"
+ "_mb_openatWithMode failed for regular file"
+ "_mb_openatWithMode failed for symlink"
+ "_mb_splitIntoBase failed (long path)"
+ "_mb_splitIntoBase failed to call malloc"
+ "_mb_splitIntoBase:andRelativePath:"
+ "_openFD:baseFD:rpath:flags:mode:error:"
+ "_openFD:path:flags:mode:error:"
+ "_performSinglePassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:direntCount:directoryPathStack:directoryCountStack:context:stats:"
+ "_performTwoPassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:direntCount:directoryPathStack:directoryCountStack:context:stats:"
+ "_scanDomain:snapshotPath:context:stats:"
+ "_scanFilesForDomain:fds:snapshotPath:relativePath:context:stats:"
+ "_scanFilesUsingGetattrlistbulkForDomain:fds:snapshotPath:relativePath:context:stats:"
+ "_scanTree:forDomain:fds:snapshotPath:relativePath:context:stats:"
+ "_shouldNotBackupFile:domain:context:"
+ "_totalStatsLock"
+ "clockByAddingPositiveTimeInterval:"
+ "completedBatchCount"
+ "copyRegularFileFrom:to:replaceDestination:error:"
+ "countOfSnapshotsForAllPersonae:"
+ "createDirectories:permissions:owner:group:error:"
+ "createOrOpenFD:baseFD:rpath:flags:mode:error:"
+ "createOrOpenFD:path:flags:mode:error:"
+ "domainsWithSystemFilesToAlwaysRemoveOnRestore"
+ "fchownat failed at %@ for %@/%@"
+ "fcopyfile failed"
+ "fgetattrlist() error"
+ "fileScanner:didFindFile:context:"
+ "fileScanner:failedToOpenFile:withErrno:context:"
+ "fileScanner:failedToStatFile:withErrno:context:"
+ "fileScanner:isFileAddedOrModified:context:"
+ "fileScanner:shouldExcludeFile:context:"
+ "findSnapshotWithName:forVolume:error:"
+ "finishBatchWithError:"
+ "incrementCountWithError:"
+ "indexesOfObjectsPassingTest:"
+ "initWithPQLConnection:batchCount:"
+ "interval >= 0"
+ "mb_splitIntoBase failed"
+ "mkdirat failed at %@ for %@/%@"
+ "nodeWithBuffer:error:"
+ "path.length > 0 && [path characterAtIndex:0] == '/'"
+ "rename from %s to %s failed: %@"
+ "scanDomain:snapshotMountPoint:context:error:"
+ "startBatchWithError:"
+ "v40@0:8q16q24@?32"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "!_done && \"Received connection:didFailWithError: when already done\""
- "!_done && \"Received connection:didFinishLoading: when already done\""
- "%@ %@"
- "%@ rename error"
- "%@/%@ (%@; %@)"
- "%@: canceling"
- "%@: data received (%lu bytes)"
- "%@: failure: %@"
- "%@: finished loading"
- "%@: response received: %ld (%@)"
- "%@: starting: %@ %@ (%lu)"
- "%{public}@, uploadBatchSize:%lu, concurrentUploadBatchCount:%lu"
- "(unknown: %i)"
- "-[MBFileScanner _foundFile:snapshotPath:stats:]"
- "-[MBFileScanner _performSinglePassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:direntCount:directoryPathStack:directoryCountStack:stats:]"
- "-[MBFileScanner _shouldNotBackupFile:domain:]"
- "-[MBURLConnection connection:didFailWithError:]"
- "-[MBURLConnection connectionDidFinishLoading:]"
- "/var/installd/Library/MobileInstallation/BackedUpState/BackupSystemAppInstallState.plist"
- "/var/installd/Library/MobileInstallation/BackedUpState/SystemAppInstallState.plist"
- "/var/mobile/Library/Caches/Backup/DT"
- "/var/mobile/tmp/com.apple.backup.testing"
- "/var/root/Library/Caches/Backup"
- "/var/tmp/backupd-XXXXXXXXXXXXXXX"
- "/var/tmp/com.apple.backup"
- "/var/tmp/com.apple.backup.testing"
- "2@ `"
- "<%@: %p>"
- "=restore-policy= lstat failed at %@: %{errno}d"
- "=scanning= Deleted while scanning: %@"
- "=scanning= Finished scanning domain %{public}@ - %@: %@"
- "=scanning= Ignoring path modified while scanning: %@ (startTime:%ld, lastModified:%ld)"
- "=scanning= Modified while scanning: %@ (startTime:%ld, lastModified:%ld)"
- "?%@"
- "@\"MBSBackupAttributes\""
- "@\"MBSSnapshotAttributes\""
- "@\"MBURLRequest\""
- "@\"NSError\"32@0:8@\"MBFileScanner\"16@\"MBFile\"24"
- "@\"NSOperationQueue\""
- "@\"NSURL\""
- "@\"NSURLConnection\""
- "@40@0:8#16@?24@32"
- "@40@0:8@16@24^{_MBFileScannerDomainStats=qqqQQQQQQ}32"
- "@56@0:8@16@24@32@40^{_MBFileScannerDomainStats=qqqQQQQQQ}48"
- "@56@0:8@16@24^@32^@40^@48"
- "@80@0:8@16@24@32@40i48I52@56@64^{_MBFileScannerDomainStats=qqqQQQQQQ}72"
- "Authorization"
- "Automatic"
- "B24@0:8@\"NSURLConnection\"16"
- "B32@0:8@\"MBFileScanner\"16@\"MBFile\"24"
- "B32@0:8@\"NSURLConnection\"16@\"NSURLProtectionSpace\"24"
- "B32@0:8q16^@24"
- "B36@0:8@\"MBFileScanner\"16@\"MBFile\"24i32"
- "B36@0:8@16@24i32"
- "Basic %@"
- "Error opening SQLite file to calculate freelist ratio: %s (%d)"
- "Error stat'ing file descriptor: %{errno}d"
- "Failed to copy system app plist: %{errno}d"
- "File modified while being uploaded"
- "File modified while being uploaded (%@): %@ (%@)"
- "File removed before being uploaded: %@ (%ld, %@)"
- "FileDeletedWhileScanning"
- "FileModifiedWhileScanning"
- "Full"
- "GET"
- "Incremental"
- "Initial"
- "MBSBackup"
- "MBSBackupAttributes"
- "MBSSnapshot"
- "MBSSnapshotAttributes"
- "MBURLConnection"
- "MBURLConnection.m"
- "MBURLRequest"
- "MMePreAuth"
- "Manual"
- "NSURLAuthenticationMethodXMobileMeAuthToken"
- "NSURLConnectionDelegate"
- "NSURLRequest"
- "Not annotating"
- "Removed while getting metadata: %@ (%@)"
- "Request cancelled"
- "Response body too large"
- "Response from the server is too large. Bailing."
- "Restore path parent directory is a symlink"
- "Setup"
- "Skipped rename from %@ to %@: %{errno}d"
- "T@\"MBSBackupAttributes\",&,N,V_attributes"
- "T@\"MBSSnapshotAttributes\",&,N,V_attributes"
- "T@\"NSData\",&,N,V_backupUDID"
- "T@\"NSData\",&,N,V_data"
- "T@\"NSData\",&,N,V_keybagUUID"
- "T@\"NSDictionary\",C,N"
- "T@\"NSMutableArray\",&,N,V_snapshots"
- "T@\"NSSet\",R,N"
- "T@\"NSString\",&,N,V_buildVersion"
- "T@\"NSString\",&,N,V_deviceClass"
- "T@\"NSString\",&,N,V_deviceColor"
- "T@\"NSString\",&,N,V_deviceEnclosureColor"
- "T@\"NSString\",&,N,V_deviceName"
- "T@\"NSString\",&,N,V_hardwareModel"
- "T@\"NSString\",&,N,V_marketingName"
- "T@\"NSString\",&,N,V_method"
- "T@\"NSString\",&,N,V_productType"
- "T@\"NSString\",&,N,V_productVersion"
- "T@\"NSString\",&,N,V_serialNumber"
- "T@\"NSURL\",&,N,V_URL"
- "T@?,C,N,V_dataReceived"
- "T@?,C,N,V_failure"
- "T@?,C,N,V_finishedLoading"
- "T@?,C,N,V_responseReceived"
- "TB,N,GshouldLog,V_log"
- "TB,N,GuseMMePreAuth,V_MMePreAuth"
- "TI,N,V_snapshotID"
- "TQ,N,V_committed"
- "TQ,N,V_keysLastModified"
- "TQ,N,V_lastModified"
- "TQ,N,V_quotaReserved"
- "TQ,N,V_quotaUsed"
- "Ti,N,V_backupReason"
- "Ti,N,V_backupType"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (mkdtemp)"
- "Unable to create /var/tmp/backupd-XXXXXXXXXX directory (strdup)"
- "User-Agent"
- "_MMePreAuth"
- "_URL"
- "_backupReason"
- "_backupType"
- "_backupUDID"
- "_buildVersion"
- "_bytesReadSinceLastModificationCheck"
- "_dataReceived"
- "_detectModifiedDomain:relativePath:lastModified:"
- "_deviceClass"
- "_deviceColor"
- "_deviceEnclosureColor"
- "_deviceName"
- "_done"
- "_enumerateObjectsOfClass:withCallback:format:"
- "_failure"
- "_finishedLoading"
- "_foundFile:snapshotPath:stats:"
- "_hardwareModel"
- "_has"
- "_headers"
- "_initWithRequest:delegate:usesCache:maxContentLength:startImmediately:connectionProperties:"
- "_isModifiedSince:error:"
- "_isModifiedWithFileDescriptor:reason:"
- "_keybagUUID"
- "_keysLastModified"
- "_lastModified"
- "_log"
- "_marketingName"
- "_method"
- "_operationQueue"
- "_performSinglePassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:direntCount:directoryPathStack:directoryCountStack:stats:"
- "_performTwoPassEnumerationForDomain:snapshotPath:relativePath:buffer:dirFd:direntCount:directoryPathStack:directoryCountStack:stats:"
- "_productType"
- "_productVersion"
- "_quotaReserved"
- "_quotaUsed"
- "_request"
- "_responseReceived"
- "_scanDomain:snapshotPath:stats:"
- "_scanFilesForDomain:fds:snapshotPath:relativePath:stats:"
- "_scanFilesUsingGetattrlistbulkForDomain:fds:snapshotPath:relativePath:stats:"
- "_scanTree:forDomain:fds:snapshotPath:relativePath:stats:"
- "_serialNumber"
- "_setError"
- "_setProperty:forKey:"
- "_shouldCheckForModifications"
- "_shouldNotBackupFile:domain:"
- "_snapshots"
- "_startTime"
- "addSnapshot:"
- "allHeaderFields"
- "appleIDHeadersForRequest:"
- "authenticationMethod"
- "backupReason"
- "backupUDID"
- "cancelAuthenticationChallenge:"
- "clearSnapshots"
- "connection:canAuthenticateAgainstProtectionSpace:"
- "connection:didCancelAuthenticationChallenge:"
- "connection:didFailWithError:"
- "connection:didReceiveAuthenticationChallenge:"
- "connection:didReceiveData:"
- "connection:didReceiveResponse:"
- "connection:willSendRequestForAuthenticationChallenge:"
- "connectionDidFinishLoading:"
- "connectionShouldUseCredentialStorage:"
- "connectionWithRequest:properties:"
- "copyTo:"
- "dataReceived"
- "destinationBaseFD != 1"
- "deviceColor"
- "deviceEnclosureColor"
- "enumerateObjectsOfClass:"
- "failure"
- "fileModifiedWhileUploadingFile:reason:"
- "fileScanner:didFindFile:"
- "fileScanner:failedToOpenFile:withErrno:"
- "fileScanner:failedToStatFile:withErrno:"
- "fileScanner:isFileAddedOrModified:"
- "fileScanner:shouldExcludeFile:"
- "finishedLoading"
- "hard link error: %@"
- "hardwareModel"
- "hasAttributes"
- "hasBackupReason"
- "hasBackupType"
- "hasBackupUDID"
- "hasBuildVersion"
- "hasCommitted"
- "hasDeviceClass"
- "hasDeviceColor"
- "hasDeviceEnclosureColor"
- "hasDeviceName"
- "hasError"
- "hasHardwareModel"
- "hasKeybagID"
- "hasKeybagUUID"
- "hasKeysLastModified"
- "hasLastModified"
- "hasMarketingName"
- "hasProductType"
- "hasProductVersion"
- "hasQuotaReserved"
- "hasQuotaUsed"
- "hasSerialNumber"
- "hasSnapshotID"
- "headers"
- "initWithIdentifier:"
- "initWithRequest:properties:"
- "isModifiedSince:reason:"
- "keysLastModified"
- "link error to \"%@\""
- "localizedStringForStatusCode:"
- "lstat error"
- "marketingName"
- "mb_splitIntoBase:andRelativePath:"
- "mergeFrom:"
- "method"
- "mod time changed"
- "modifiedDomains"
- "objectAtIndex:"
- "openat() error"
- "openat_dprotected_np() error"
- "performCallbackOnQueue:"
- "performDefaultHandlingForAuthenticationChallenge:"
- "position"
- "previousFailureCount"
- "proposedCredential"
- "protectionSpace"
- "query"
- "quotaReserved"
- "quotaUsed"
- "readFrom:"
- "relativePathsNotToCheckIfModifiedDuringBackup"
- "rename from %s to %s failed: %{errno}d"
- "request"
- "requestWithMethod:URL:"
- "requestWithURL:"
- "responseReceived"
- "scanDomain:snapshotMountPoint:"
- "sendAsyncRequest:properties:block:"
- "sendSyncRequest:properties:connection:response:error:"
- "sender"
- "setAllHTTPHeaderFields:"
- "setAttributes:"
- "setBackupReason:"
- "setBackupType:"
- "setBackupUDID:"
- "setBuildVersion:"
- "setCachePolicy:"
- "setData:"
- "setDataReceived:"
- "setDelegateQueue:"
- "setDeviceClass:"
- "setDeviceColor:"
- "setDeviceEnclosureColor:"
- "setFailure:"
- "setFinishedLoading:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHTTPShouldUsePipelining:"
- "setHardwareModel:"
- "setHasBackupReason:"
- "setHasBackupType:"
- "setHasCommitted:"
- "setHasKeybagID:"
- "setHasKeysLastModified:"
- "setHasLastModified:"
- "setHasQuotaReserved:"
- "setHasQuotaUsed:"
- "setHasSnapshotID:"
- "setHeaders:"
- "setKeybagUUID:"
- "setKeysLastModified:"
- "setLog:"
- "setMMePreAuth:"
- "setMarketingName:"
- "setMaxConcurrentOperationCount:"
- "setMethod:"
- "setPosition:"
- "setProductType:"
- "setProductVersion:"
- "setQuotaReserved:"
- "setQuotaUsed:"
- "setResponseReceived:"
- "setSerialNumber:"
- "setSnapshots:"
- "setTimeoutInterval:"
- "setURL:"
- "setUnderlyingQueue:"
- "setValue:forHTTPHeaderField:"
- "setValue:forHeader:"
- "shouldLog"
- "snapshot"
- "snapshotAtIndex:"
- "snapshots"
- "snapshotsCount"
- "statusCode"
- "useCredential:forAuthenticationChallenge:"
- "useMMePreAuth"
- "v16@?0@\"NSData\"8"
- "v16@?0@\"NSHTTPURLResponse\"8"
- "v32@0:8@\"NSURLConnection\"16@\"NSError\"24"
- "v32@0:8@\"NSURLConnection\"16@\"NSURLAuthenticationChallenge\"24"
- "v32@0:8^i16r^*24"
- "v32@?0@\"NSHTTPURLResponse\"8@\"NSData\"16@\"NSError\"24"
- "v40@0:8@16@24q32"
- "writeTo:"
- "{?=\"backupReason\"b1\"backupType\"b1\"keybagID\"b1}"
- "{?=\"committed\"b1\"lastModified\"b1\"quotaReserved\"b1\"snapshotID\"b1}"
- "{?=\"keysLastModified\"b1\"quotaUsed\"b1}"

```
