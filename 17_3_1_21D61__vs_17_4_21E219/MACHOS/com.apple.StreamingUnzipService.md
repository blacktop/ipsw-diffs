## com.apple.StreamingUnzipService

> `/System/Library/PrivateFrameworks/StreamingZip.framework/XPCServices/com.apple.StreamingUnzipService.xpc/com.apple.StreamingUnzipService`

```diff

-206.40.2.0.0
-  __TEXT.__text: 0x1b5d8
+216.0.0.0.0
+  __TEXT.__text: 0x16a60
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_stubs: 0x1cc0
-  __TEXT.__objc_methlist: 0x7b0
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x463d
-  __TEXT.__oslogstring: 0x2e9d
-  __TEXT.__objc_classname: 0x113
-  __TEXT.__objc_methname: 0x246e
-  __TEXT.__objc_methtype: 0xa48
-  __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__objc_stubs: 0x22e0
+  __TEXT.__objc_methlist: 0xb14
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__cstring: 0x2b22
+  __TEXT.__oslogstring: 0x33fe
+  __TEXT.__objc_classname: 0x1d0
+  __TEXT.__objc_methname: 0x2f1a
+  __TEXT.__objc_methtype: 0xd4a
+  __TEXT.__unwind_info: 0x37c
   __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6b8
-  __DATA_CONST.__cfstring: 0x2400
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x600
+  __DATA_CONST.__cfstring: 0x1640
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1ae0
-  __DATA.__objc_selrefs: 0x818
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x538
-  __DATA.__bss: 0x70
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA.__objc_const: 0x2058
+  __DATA.__objc_selrefs: 0x9d0
+  __DATA.__objc_ivar: 0x15c
+  __DATA.__objc_data: 0x2d0
+  __DATA.__data: 0x4a8
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 503
-  Symbols:   331
-  CStrings:  1134
+  Functions: 311
+  Symbols:   222
+  CStrings:  1192
 
Symbols:
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSValue
+ __dispatch_queue_attr_concurrent
+ __os_log_fault_impl
+ _dispatch_group_async
+ _dispatch_group_wait
+ _objc_retain_x28
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _read
- _CDRecordHasZip64ExtraField
- _CDRecordIsDirectory
- _CFRelease
- _CFStringCreateWithFormatAndArguments
- _CFStringGetCString
- _CompressionAlgorithmIDForCompressionMethod
- _CompressionMethodUsesLibrary
- _CopyFileNameFromCDRecord
- _CopyFileNameFromLocalFileRecord
- _CopyLocalFileRecord
- _CreateCDRecord
- _CreateLocalFileRecord
- _DOS2UNIXTime
- _GenericHashFinal
- _GenericHashInit
- _GenericHashUpdate
- _GetCDRecordCompressedSize
- _GetCDRecordUncompressedSize
- _GetDiskNumberFromCDRecord
- _GetExtraFieldFromCDRecord
- _GetExtraFieldFromLocalFileRecord
- _GetExtraFieldWithSignature
- _GetFileCommentFromCDRecord
- _GetInfoZipExtraFieldFromCDRecord
- _GetInfoZipExtraFieldFromLF
- _GetLFCompressedSize
- _GetLFOffsetFromCDRecord
- _GetLFSizes
- _GetLFUncompressedSize
- _GetPOSIXFileModeFromCDRecord
- _GetSizeOfCDRecord
- _GetSizeOfLocalFileRecord
- _GetSizeOfZip64EndRecord
- _GetStreamingZipExtraFieldFromLF
- _GetUnixAccessTimestampFromCDRecord
- _GetUnixAccessTimestampFromLocalFileRecord
- _GetUnixModTimestampFromCDRecord
- _GetUnixModTimestampFromLocalFileRecord
- _GetUnixTimestampFromCDRecord
- _GetUnixTimestampFromLocalFileRecord
- _GetZip64ExtraFieldDataFromLF
- _GetZip64ExtraFieldFromCDRecord
- _GetZip64ExtraFieldFromLF
- _IsSupportedCompressionMethod
- _LocalFileRecordHasZip64ExtraField
- _LocalFileRecordIsDirectory
- _LocalFileRecordNameIsUTF8
- _LocalFileRecordRequiresDataDescriptor
- _OBJC_CLASS_$_SZExtractor
- _OBJC_CLASS_$_StreamingUnzipServiceDelegate
- _OBJC_CLASS_$_StreamingUnzipper
- _OBJC_METACLASS_$_SZExtractor
- _OBJC_METACLASS_$_StreamingUnzipServiceDelegate
- _OBJC_METACLASS_$_StreamingUnzipper
- _SZConfiguredStreamingUnzipDelegateProtocolInterface
- _SZConfiguredStreamingUnzipProtocolInterface
- _SZExtractorActualHashValueErrorKey
- _SZExtractorCompressionLibErrorKey
- _SZExtractorEntitlementPrivileged
- _SZExtractorErrorDomain
- _SZExtractorFileOffsetErrorKey
- _SZExtractorFunctionNameErrorKey
- _SZExtractorHashChunkIndexErrorKey
- _SZExtractorHashTypeMD5
- _SZExtractorHashTypeSHA1
- _SZExtractorHashTypeSHA224
- _SZExtractorHashTypeSHA256
- _SZExtractorHashTypeSHA384
- _SZExtractorHashTypeSHA512
- _SZExtractorOptionsAssertQOS
- _SZExtractorOptionsDenyInvalidSymlinks
- _SZExtractorOptionsHashType
- _SZExtractorOptionsHashedChunkSize
- _SZExtractorOptionsHashesArray
- _SZExtractorOptionsOwnerGroupID
- _SZExtractorOptionsOwnerUserID
- _SZExtractorOptionsPerformCachedWrites
- _SZExtractorOptionsQuarantineInfo
- _SZExtractorSourceFileLineErrorKey
- _SZExtractorZlibErrorKey
- _SZGetLoggingHandle
- _SZGetTraceHandle
- _SZWrite
- _UNIX2DOSTime
- __SZLog
- ___stderrp
- _gHashContextSizes
- _gHashDigestSizes
- _gHashStringNames
- _gSZDefaultLogLevel
- _gSZLogPrefix
- _gSZLogToSyslog
- _kCDRecordSignature
- _kCFAllocatorDefault
- _kDataDescriptorSignature
- _kEndRecordSignature
- _kFixedMetadataMagic
- _kInfoZipExtraFieldSignature
- _kInfoZipNewUnixExtraFieldSignature
- _kInfoZipTimestampExtraFieldSignature
- _kLocalFileRecordSignature
- _kStreamingZipLFExtraFieldSignature
- _kZip64EndRecordLocatorSignature
- _kZip64EndRecordSignature
- _kZip64ExtraFieldSignature
- _kZipFixedMetadataFilePath
- _kZipMetadataCreatorToolCommandLineKey
- _kZipMetadataCreatorToolUUIDKey
- _kZipMetadataDirectory
- _kZipMetadataFilePath
- _kZipMetadataRecordCountKey
- _kZipMetadataStandardDirectoryPermsKey
- _kZipMetadataStandardFilePermsKey
- _kZipMetadataTotalUncompressedBytesKey
- _kZipMetadataVersionKey
- _objc_release_x2
- _objc_retain_x4
- _pthread_self
- _vfprintf
- _vsyslog
CStrings:
+ "\x11R"
+ "!"
+ "!_currentState.fileWriter"
+ "-[AsyncStreamingFileWriter currentOffsetWithError:]"
+ "-[AsyncStreamingFileWriter readIntoBuffer:length:error:]"
+ "-[AsyncStreamingFileWriter setCurrentOffset:error:]"
+ "-[StreamingFileWriter _openCurrentOutputFDForPath:withOpenFlags:mode:performCachedWrites:quarantineInfo:error:]"
+ "-[StreamingFileWriter currentOffsetWithError:]"
+ "-[StreamingFileWriter readIntoBuffer:length:error:]"
+ "-[StreamingFileWriter setCurrentOffset:error:]"
+ "-[StreamingFileWriter writeBuffer:length:error:]"
+ "-[StreamingFileWriterQueue insertAsyncFileOperation:error:]"
+ "20:57:12"
+ "3"
+ "<%@: path=%@>"
+ "@\"<StreamingFileWriterErrorDelegate>\""
+ "@\"NSMutableArray\""
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSObject<OS_dispatch_group>\"16@0:8"
+ "@\"StreamingFileWriter\""
+ "@\"StreamingFileWriterQueueReservation\""
+ "@\"StreamingFileWriterQueueReservation\"16@0:8"
+ "@24@0:8q16"
+ "@48@0:8q16@24@32^B40"
+ "@52@0:8@16i24S28^v32B40^@44"
+ "@60@0:8@16i24S28^v32B40q44^@52"
+ "@76@0:8@16i24S28^v32B40q44@52@60^@68"
+ "@84@0:8@16i24S28^v32B40q44@52@60@68^@76"
+ "ASYNC_ENQUEUE"
+ "ASYNC_FILE_QUEUE_FULL"
+ "ASYNC_FILE_RESERVED"
+ "ASYNC_OP_EXISTS"
+ "ASYNC_WRITE"
+ "Added async operation for size %lld; queue count: %lu"
+ "Advisory preallocation of %lld bytes for %@ failed: %s"
+ "Async op exists for %@"
+ "Async op reserved for %@ size %lld (cur total: %lld)"
+ "Async operation for %@ failed: %@"
+ "AsyncStreamingFileWriter"
+ "B24@0:8^@16"
+ "B32@0:8@16^@24"
+ "B32@0:8q16^@24"
+ "B36@0:8r^{timeval=qi}16S24^@28"
+ "B40@0:8r^v16Q24^@32"
+ "B52@0:8@16i24S28B32^v36^@44"
+ "CONCURRENCY_LIMIT"
+ "End async operation for %@ size %lld"
+ "Enqueueing async operation for %@ size %lld"
+ "FILE_TOO_BIG"
+ "Failed to fchown %@ to (%d:%d) : %d (%s)"
+ "Failed to read bytes from %@ : %d (%s)"
+ "Failed to seek to current offset in output file at path %@ : %s"
+ "Failed to seek to offset %llu in output file at path %@ : %s"
+ "Failed to set times on %@ : %s"
+ "Failed to write data to output file at %@: %s"
+ "Failed to write initial data to passthrough output file"
+ "Failed to write remaining initial data to passthrough output file"
+ "Feb 16 2024"
+ "Getting current output offset not available on async file operation for %@"
+ "I"
+ "I16@0:8"
+ "Insufficient buffer avilable for %@ size %lld"
+ "Max async item size limit is %lld"
+ "Max async operation size limit is %lld"
+ "Max concurrency is %lu"
+ "MaxAsyncItemSize"
+ "MaxAsyncOperationSize"
+ "MaxConcurrency"
+ "No pending operation paths found for group %@ when trying to remove path %@"
+ "Overriding max async item size limit to %lld"
+ "Overriding max async operation size limit to %lld"
+ "Overriding max concurrency to %lu"
+ "PerformAllWritesSynchronously"
+ "Read not available on async file operation for %@"
+ "Rejecting insert of file operation because the reservation for size %llu was not valid"
+ "Returning async file error %@"
+ "Setting current output offset not available on async file operation for %@"
+ "Setting incomplete extraction attribute not available on this async file operation for %@"
+ "Setting initial mode on %@ failed: %s"
+ "Start async operation for %@ size %lld"
+ "StreamingFileWriter"
+ "StreamingFileWriter %@ encountered error %@"
+ "StreamingFileWriterErrorDelegate"
+ "StreamingFileWriterQueue"
+ "StreamingFileWriterQueueAsyncOperation"
+ "StreamingFileWriterQueueReservation"
+ "T@\"<StreamingFileWriterErrorDelegate>\",W,N,V_errorDelegate"
+ "T@\"NSMutableArray\",R,N,V_pendingOperations"
+ "T@\"NSMutableData\",&,N,V_fileData"
+ "T@\"NSMutableDictionary\",R,N,V_pendingOperationPathsByGroupPointer"
+ "T@\"NSObject<OS_dispatch_group>\",R,N"
+ "T@\"NSObject<OS_dispatch_group>\",R,N,V_trackingGroup"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_fileWriterQueue"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C,N"
+ "T@\"NSString\",R,C,N,V_path"
+ "T@\"StreamingFileWriter\",&,N,V_fileWriter"
+ "T@\"StreamingFileWriterQueueReservation\",R,N"
+ "T@\"StreamingFileWriterQueueReservation\",R,N,V_reservation"
+ "TB,?,R,D,N"
+ "TB,?,R,N"
+ "TB,N,GisValid,V_valid"
+ "TB,N,V_setOwnership"
+ "TB,R,N,V_performCachedWrites"
+ "TI,N,V_gid"
+ "TI,N,V_uid"
+ "TQ,N,V_executeFileOperationFlags"
+ "TQ,N,V_runningOperationCount"
+ "TQ,R,N,V_maxConcurrency"
+ "TS,N,V_mode"
+ "TS,R,N,V_omode"
+ "Ti,R,N,V_oflag"
+ "Too large for async: %@ size %lld"
+ "Tq,N,V_pendingOperationSize"
+ "Tq,R,N,V_fileSize"
+ "Tq,R,N,V_maxPendingItemSize"
+ "Tq,R,N,V_maxPendingOperationSize"
+ "Tq,R,N,V_reservedSize"
+ "Tr^{timeval=qi},N,V_time"
+ "T{os_unfair_lock_s=I},N,V_pendingStateLock"
+ "Unable to get current output offset from current output file"
+ "Writing %@ asynchronously"
+ "_asyncError"
+ "_asyncErrorLock"
+ "_asyncWorkTrackingGroup"
+ "_currentState.fileWriter"
+ "_errorDelegate"
+ "_executeFileOperationFlags"
+ "_executeWithError:"
+ "_fileData"
+ "_fileSize"
+ "_fileWriter"
+ "_fileWriterQueue"
+ "_gid"
+ "_initForWritingToPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:reservation:error:"
+ "_initForWritingToPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:error:"
+ "_maxConcurrency"
+ "_maxPendingItemSize"
+ "_maxPendingOperationSize"
+ "_mode"
+ "_oflag"
+ "_omode"
+ "_openCurrentOutputFDForPath:withOpenFlags:mode:performCachedWrites:quarantineInfo:error:"
+ "_path"
+ "_pendingOperationPathsByGroupPointer"
+ "_pendingOperationSize"
+ "_pendingOperations"
+ "_pendingStateLock"
+ "_reservation"
+ "_reservedSize"
+ "_runOperation:"
+ "_runningOperationCount"
+ "_setOwnership"
+ "_time"
+ "_trackingGroup"
+ "_uid"
+ "_valid"
+ "closeCurrentOutputFD"
+ "com.apple.StreamingZip.StreamingFileWriterQueue"
+ "configureFileAndSetOwnership:toUID:GID:"
+ "currentOffsetWithError:"
+ "errorDelegate"
+ "executeAsyncOperation"
+ "executeFileOperationFlags"
+ "fileData"
+ "fileSize"
+ "fileWriter"
+ "fileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:error:"
+ "fileWriterQueue"
+ "finalizeFileWithTimestamp:mode:error:"
+ "gid"
+ "initWithReservationSize:"
+ "insertAsyncFileOperation:error:"
+ "integerForKey:"
+ "isValid"
+ "maxConcurrency"
+ "maxPendingItemSize"
+ "maxPendingOperationSize"
+ "mode"
+ "oflag"
+ "omode"
+ "pendingOperationPathsByGroupPointer"
+ "pendingOperationSize"
+ "pendingOperations"
+ "pendingStateLock"
+ "q16@0:8"
+ "q24@0:8^@16"
+ "q40@0:8^v16Q24^@32"
+ "r\"1"
+ "r^{timeval=qi}"
+ "r^{timeval=qi}16@0:8"
+ "readIntoBuffer:length:error:"
+ "removeObject:"
+ "removeObjectForKey:"
+ "reservation"
+ "reserveAsyncOperationForFileSize:path:group:operationPendingForPath:"
+ "reservedSize"
+ "runningOperationCount"
+ "setCurrentOffset:error:"
+ "setErrorDelegate:"
+ "setExecuteFileOperationFlags:"
+ "setFileData:"
+ "setFileWriter:"
+ "setGid:"
+ "setIncompleteExtractionAttribute"
+ "setMode:"
+ "setOwnership"
+ "setPendingOperationSize:"
+ "setPendingStateLock:"
+ "setRunningOperationCount:"
+ "setSetOwnership:"
+ "setTime:"
+ "setUid:"
+ "setValid:"
+ "sharedInstance"
+ "streamingFileWriter:didEncounterError:"
+ "suspendWithError:"
+ "synchronousFileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:error:"
+ "time"
+ "trackingGroup"
+ "uid"
+ "v20@0:8I16"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8q16"
+ "v24@0:8r^{timeval=qi}16"
+ "v28@0:8B16I20I24"
+ "v32@0:8@\"StreamingFileWriter\"16@\"NSError\"24"
+ "valid"
+ "valueWithNonretainedObject:"
+ "writeBuffer:length:error:"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
+ "\x81"
+ "\xa4\xf0\xd4!q"
+ "\xe2"
- "%s: %s:%d (0x%p): %s\n"
- "+[SZExtractor(Testing) servicePIDWithError:]_block_invoke"
- "-[SZExtractor _invalidateObject]"
- "-[SZExtractor _setUpWithPath:options:]"
- "-[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:]_block_invoke"
- "-[SZExtractor _synchronouslyPrepareForExtractionAtOffset:]_block_invoke"
- "-[SZExtractor encodeWithCoder:]"
- "-[SZExtractor encodeWithCoder:]_block_invoke"
- "-[SZExtractor finishStreamWithCompletionBlock:]_block_invoke"
- "-[SZExtractor initWithCoder:]"
- "-[SZExtractor prepareForExtractionToPath:completionBlock:]"
- "-[SZExtractor setActiveExtractorDelegateMethods:]"
- "-[SZExtractor setActiveExtractorDelegateMethods:]_block_invoke"
- "-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke"
- "-[SZExtractor terminateStreamWithError:completionBlock:]_block_invoke"
- "-[StreamingUnzipServiceDelegate listener:shouldAcceptNewConnection:]"
- "-[StreamingUnzipState openCurrentOutputFDForPath:withOpenFlags:mode:error:]"
- "-[StreamingUnzipper _setErrorState]"
- "-[StreamingUnzipper dealloc]"
- "-[StreamingUnzipper setActiveDelegateMethods:]"
- "-[StreamingUnzipper supplyBytes:withReply:]_block_invoke"
- "17:52:38"
- "@24@0:8Q16"
- "@32@0:8r^v16Q24"
- "B40@0:8@16i24S28^@32"
- "CreateLocalFileRecord"
- "CreatorToolCommandLine"
- "CreatorToolUUID"
- "Dec 20 2023"
- "Failed to create log string"
- "Failed to fchown %s to (%d:%d) : %d (%s)"
- "Failed to seek to offset %llu in output file at path %@: %s"
- "Failed to write data to output file %@: %s"
- "Failed to write data to passthrough output file: %s"
- "Failed to write decompressed data to output file %@ : %s"
- "Failed to write initial data to passthrough output file: %s"
- "Failed to write remaining initial data to passthrough output file: %s"
- "GetFileNameStringFromLocalFileRecord"
- "SZExtractorZlibErrorKey"
- "StreamingZip"
- "T@\"<SZExtractorDelegate>\",W,Vdelegate"
- "TB,R,D,N"
- "TB,R,N"
- "UREAD(cdRecord->thirty_two_bit_compressed_size) < UINT32_MAX && UREAD(cdRecord->thirty_two_bit_uncompressed_size) < UINT32_MAX"
- "ZipStructure.c"
- "_HashTypeForString"
- "_RemoveAndRecreateDirectoryAtPath"
- "_ValidateDictionaryKeyValueType"
- "_beginNonStreamablePassthroughWithRemainingBytes:length:"
- "_checkHashForOffset:"
- "_currentState.currentOutputFD < 0"
- "_currentState.currentOutputFD >= 0"
- "_extractionEnteredPassThroughMode"
- "_sendExtractionCompleteAtArchivePath:"
- "_sendExtractionProgress:"
- "_setErrorState"
- "_supplyBytes:length:withReply:"
- "advisory preallocation of %lld bytes for %@ failed: %s"
- "initWithPath:options:error:"
- "main"
- "main_block_invoke"
- "openCurrentOutputFDForPath:withOpenFlags:mode:error:"
- "rA"
- "v40@0:8r*16Q24@?32"
- "\xa4\xf0ԡ"
- "\xb2"

```
