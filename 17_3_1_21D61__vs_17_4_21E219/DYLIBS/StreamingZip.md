## StreamingZip

> `/System/Library/PrivateFrameworks/StreamingZip.framework/StreamingZip`

```diff

-206.40.2.0.0
-  __TEXT.__text: 0x2cea4
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_methlist: 0x7a0
-  __TEXT.__cstring: 0x7dce
-  __TEXT.__oslogstring: 0x5557
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x1b0
-  __TEXT.__unwind_info: 0x660
-  __TEXT.__objc_classname: 0xf4
-  __TEXT.__objc_methname: 0x2436
-  __TEXT.__objc_methtype: 0xa0c
-  __TEXT.__objc_stubs: 0x1c40
+216.0.0.0.0
+  __TEXT.__text: 0x217c4
+  __TEXT.__auth_stubs: 0xe50
+  __TEXT.__objc_methlist: 0xb04
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__cstring: 0x3a9d
+  __TEXT.__oslogstring: 0x5a93
+  __TEXT.__unwind_info: 0x3ec
+  __TEXT.__objc_classname: 0x1b1
+  __TEXT.__objc_methname: 0x2f04
+  __TEXT.__objc_methtype: 0xd0e
+  __TEXT.__objc_stubs: 0x2280
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0xc10
-  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__const: 0xc40
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x14e8
-  __DATA_CONST.__objc_selrefs: 0x800
-  __AUTH_CONST.__cfstring: 0x42c0
-  __AUTH_CONST.__objc_const: 0x0
+  __DATA_CONST.__objc_const: 0x1b88
+  __DATA_CONST.__objc_selrefs: 0x9c8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__objc_const: 0x1b0
+  __AUTH_CONST.__cfstring: 0x1d60
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x730
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xc0
-  __DATA.__objc_superrefs: 0x18
-  __DATA.__objc_ivar: 0xe4
-  __DATA.__data: 0x3f0
-  __DATA.__bss: 0x40
-  __DATA_DIRTY.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x738
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x15c
+  __DATA.__data: 0x3c0
+  __DATA.__bss: 0x58
+  __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_const: 0x1f0
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 828
-  Symbols:   2450
-  CStrings:  1654
+  Functions: 358
+  Symbols:   1617
+  CStrings:  1501
 
Symbols:
+ +[StreamingFileWriter fileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:error:]
+ +[StreamingFileWriter synchronousFileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:error:]
+ +[StreamingFileWriterQueue sharedInstance]
+ -[AsyncStreamingFileWriter .cxx_destruct]
+ -[AsyncStreamingFileWriter _executeWithError:]
+ -[AsyncStreamingFileWriter _initForWritingToPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:reservation:error:]
+ -[AsyncStreamingFileWriter _openCurrentOutputFDForPath:withOpenFlags:mode:performCachedWrites:quarantineInfo:error:]
+ -[AsyncStreamingFileWriter closeCurrentOutputFD]
+ -[AsyncStreamingFileWriter configureFileAndSetOwnership:toUID:GID:]
+ -[AsyncStreamingFileWriter currentOffsetWithError:]
+ -[AsyncStreamingFileWriter dealloc]
+ -[AsyncStreamingFileWriter errorDelegate]
+ -[AsyncStreamingFileWriter executeAsyncOperation]
+ -[AsyncStreamingFileWriter executeFileOperationFlags]
+ -[AsyncStreamingFileWriter fileData]
+ -[AsyncStreamingFileWriter finalizeFileWithTimestamp:mode:error:]
+ -[AsyncStreamingFileWriter gid]
+ -[AsyncStreamingFileWriter mode]
+ -[AsyncStreamingFileWriter oflag]
+ -[AsyncStreamingFileWriter omode]
+ -[AsyncStreamingFileWriter performCachedWrites]
+ -[AsyncStreamingFileWriter readIntoBuffer:length:error:]
+ -[AsyncStreamingFileWriter reservation]
+ -[AsyncStreamingFileWriter setCurrentOffset:error:]
+ -[AsyncStreamingFileWriter setErrorDelegate:]
+ -[AsyncStreamingFileWriter setExecuteFileOperationFlags:]
+ -[AsyncStreamingFileWriter setFileData:]
+ -[AsyncStreamingFileWriter setGid:]
+ -[AsyncStreamingFileWriter setIncompleteExtractionAttribute]
+ -[AsyncStreamingFileWriter setMode:]
+ -[AsyncStreamingFileWriter setOwnership]
+ -[AsyncStreamingFileWriter setSetOwnership:]
+ -[AsyncStreamingFileWriter setTime:]
+ -[AsyncStreamingFileWriter setUid:]
+ -[AsyncStreamingFileWriter suspendWithError:]
+ -[AsyncStreamingFileWriter time]
+ -[AsyncStreamingFileWriter trackingGroup]
+ -[AsyncStreamingFileWriter uid]
+ -[AsyncStreamingFileWriter writeBuffer:length:error:]
+ -[StreamingFileWriter .cxx_destruct]
+ -[StreamingFileWriter _initForWritingToPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:error:]
+ -[StreamingFileWriter _openCurrentOutputFDForPath:withOpenFlags:mode:performCachedWrites:quarantineInfo:error:]
+ -[StreamingFileWriter closeCurrentOutputFD]
+ -[StreamingFileWriter configureFileAndSetOwnership:toUID:GID:]
+ -[StreamingFileWriter currentOffsetWithError:]
+ -[StreamingFileWriter currentOutputFD]
+ -[StreamingFileWriter dealloc]
+ -[StreamingFileWriter description]
+ -[StreamingFileWriter fileSize]
+ -[StreamingFileWriter finalizeFileWithTimestamp:mode:error:]
+ -[StreamingFileWriter path]
+ -[StreamingFileWriter readIntoBuffer:length:error:]
+ -[StreamingFileWriter setCurrentOffset:error:]
+ -[StreamingFileWriter setCurrentOutputFD:]
+ -[StreamingFileWriter setIncompleteExtractionAttribute]
+ -[StreamingFileWriter suspendWithError:]
+ -[StreamingFileWriter writeBuffer:length:error:]
+ -[StreamingFileWriterQueue .cxx_destruct]
+ -[StreamingFileWriterQueue _runOperation:]
+ -[StreamingFileWriterQueue fileWriterQueue]
+ -[StreamingFileWriterQueue init]
+ -[StreamingFileWriterQueue insertAsyncFileOperation:error:]
+ -[StreamingFileWriterQueue maxConcurrency]
+ -[StreamingFileWriterQueue maxPendingItemSize]
+ -[StreamingFileWriterQueue maxPendingOperationSize]
+ -[StreamingFileWriterQueue pendingOperationPathsByGroupPointer]
+ -[StreamingFileWriterQueue pendingOperationSize]
+ -[StreamingFileWriterQueue pendingOperations]
+ -[StreamingFileWriterQueue pendingStateLock]
+ -[StreamingFileWriterQueue reserveAsyncOperationForFileSize:path:group:operationPendingForPath:]
+ -[StreamingFileWriterQueue runningOperationCount]
+ -[StreamingFileWriterQueue setPendingOperationSize:]
+ -[StreamingFileWriterQueue setPendingStateLock:]
+ -[StreamingFileWriterQueue setRunningOperationCount:]
+ -[StreamingFileWriterQueueReservation initWithReservationSize:]
+ -[StreamingFileWriterQueueReservation isValid]
+ -[StreamingFileWriterQueueReservation reservedSize]
+ -[StreamingFileWriterQueueReservation setValid:]
+ -[StreamingUnzipState fileWriter]
+ -[StreamingUnzipState setFileWriter:]
+ -[StreamingUnzipper _waitForAsyncFileWriterCompletionAndGetAsyncError]
+ -[StreamingUnzipper streamingFileWriter:didEncounterError:]
+ GCC_except_table104
+ GCC_except_table111
+ GCC_except_table146
+ GCC_except_table242
+ GCC_except_table323
+ GCC_except_table329
+ GCC_except_table349
+ _OBJC_CLASS_$_AsyncStreamingFileWriter
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_StreamingFileWriter
+ _OBJC_CLASS_$_StreamingFileWriterQueue
+ _OBJC_CLASS_$_StreamingFileWriterQueueReservation
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._errorDelegate
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._executeFileOperationFlags
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._fileData
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._gid
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._mode
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._oflag
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._omode
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._performCachedWrites
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._reservation
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._setOwnership
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._time
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._trackingGroup
+ _OBJC_IVAR_$_AsyncStreamingFileWriter._uid
+ _OBJC_IVAR_$_StreamingFileWriter._currentOutputFD
+ _OBJC_IVAR_$_StreamingFileWriter._fileSize
+ _OBJC_IVAR_$_StreamingFileWriter._path
+ _OBJC_IVAR_$_StreamingFileWriterQueue._fileWriterQueue
+ _OBJC_IVAR_$_StreamingFileWriterQueue._maxConcurrency
+ _OBJC_IVAR_$_StreamingFileWriterQueue._maxPendingItemSize
+ _OBJC_IVAR_$_StreamingFileWriterQueue._maxPendingOperationSize
+ _OBJC_IVAR_$_StreamingFileWriterQueue._pendingOperationPathsByGroupPointer
+ _OBJC_IVAR_$_StreamingFileWriterQueue._pendingOperationSize
+ _OBJC_IVAR_$_StreamingFileWriterQueue._pendingOperations
+ _OBJC_IVAR_$_StreamingFileWriterQueue._pendingStateLock
+ _OBJC_IVAR_$_StreamingFileWriterQueue._runningOperationCount
+ _OBJC_IVAR_$_StreamingFileWriterQueueReservation._reservedSize
+ _OBJC_IVAR_$_StreamingFileWriterQueueReservation._valid
+ _OBJC_IVAR_$_StreamingUnzipState._fileWriter
+ _OBJC_IVAR_$_StreamingUnzipper._asyncError
+ _OBJC_IVAR_$_StreamingUnzipper._asyncErrorLock
+ _OBJC_IVAR_$_StreamingUnzipper._asyncWorkTrackingGroup
+ _OBJC_METACLASS_$_AsyncStreamingFileWriter
+ _OBJC_METACLASS_$_StreamingFileWriter
+ _OBJC_METACLASS_$_StreamingFileWriterQueue
+ _OBJC_METACLASS_$_StreamingFileWriterQueueReservation
+ __OBJC_$_CLASS_METHODS_StreamingFileWriter
+ __OBJC_$_CLASS_METHODS_StreamingFileWriterQueue
+ __OBJC_$_INSTANCE_METHODS_AsyncStreamingFileWriter
+ __OBJC_$_INSTANCE_METHODS_StreamingFileWriter
+ __OBJC_$_INSTANCE_METHODS_StreamingFileWriterQueue
+ __OBJC_$_INSTANCE_METHODS_StreamingFileWriterQueueReservation
+ __OBJC_$_INSTANCE_VARIABLES_AsyncStreamingFileWriter
+ __OBJC_$_INSTANCE_VARIABLES_StreamingFileWriter
+ __OBJC_$_INSTANCE_VARIABLES_StreamingFileWriterQueue
+ __OBJC_$_INSTANCE_VARIABLES_StreamingFileWriterQueueReservation
+ __OBJC_$_PROP_LIST_AsyncStreamingFileWriter
+ __OBJC_$_PROP_LIST_StreamingFileWriter
+ __OBJC_$_PROP_LIST_StreamingFileWriterQueue
+ __OBJC_$_PROP_LIST_StreamingFileWriterQueueAsyncOperation
+ __OBJC_$_PROP_LIST_StreamingFileWriterQueueReservation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_StreamingFileWriterErrorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_StreamingFileWriterQueueAsyncOperation
+ __OBJC_$_PROTOCOL_METHOD_TYPES_StreamingFileWriterErrorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_StreamingFileWriterQueueAsyncOperation
+ __OBJC_$_PROTOCOL_REFS_StreamingFileWriterErrorDelegate
+ __OBJC_$_PROTOCOL_REFS_StreamingFileWriterQueueAsyncOperation
+ __OBJC_CLASS_PROTOCOLS_$_AsyncStreamingFileWriter
+ __OBJC_CLASS_RO_$_AsyncStreamingFileWriter
+ __OBJC_CLASS_RO_$_StreamingFileWriter
+ __OBJC_CLASS_RO_$_StreamingFileWriterQueue
+ __OBJC_CLASS_RO_$_StreamingFileWriterQueueReservation
+ __OBJC_LABEL_PROTOCOL_$_StreamingFileWriterErrorDelegate
+ __OBJC_LABEL_PROTOCOL_$_StreamingFileWriterQueueAsyncOperation
+ __OBJC_METACLASS_RO_$_AsyncStreamingFileWriter
+ __OBJC_METACLASS_RO_$_StreamingFileWriter
+ __OBJC_METACLASS_RO_$_StreamingFileWriterQueue
+ __OBJC_METACLASS_RO_$_StreamingFileWriterQueueReservation
+ __OBJC_PROTOCOL_$_StreamingFileWriterErrorDelegate
+ __OBJC_PROTOCOL_$_StreamingFileWriterQueueAsyncOperation
+ ___147+[StreamingFileWriter fileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:error:]_block_invoke
+ ___42-[StreamingFileWriterQueue _runOperation:]_block_invoke
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.182
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.189
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.195
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.196
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.223
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.224
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.228
+ ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke_2.191
+ ___59-[StreamingFileWriterQueue insertAsyncFileOperation:error:]_block_invoke
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.119
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.135
+ ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.140
+ ___Block_byref_object_copy_.457
+ ___Block_byref_object_dispose_.458
+ ___block_descriptor_32_e5_v8?0l.955
+ ___block_literal_global.3
+ ___block_literal_global.934
+ __dispatch_queue_attr_concurrent
+ __os_log_fault_impl
+ _dispatch_group_async
+ _dispatch_group_wait
+ _fileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:error:.onceToken
+ _fileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:error:.performAllWritesSynchronously
+ _objc_msgSend$_executeWithError:
+ _objc_msgSend$_initForWritingToPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:reservation:error:
+ _objc_msgSend$_initForWritingToPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:error:
+ _objc_msgSend$_openCurrentOutputFDForPath:withOpenFlags:mode:performCachedWrites:quarantineInfo:error:
+ _objc_msgSend$_runOperation:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$closeCurrentOutputFD
+ _objc_msgSend$configureFileAndSetOwnership:toUID:GID:
+ _objc_msgSend$currentOffsetWithError:
+ _objc_msgSend$errorDelegate
+ _objc_msgSend$executeAsyncOperation
+ _objc_msgSend$executeFileOperationFlags
+ _objc_msgSend$fileData
+ _objc_msgSend$fileSize
+ _objc_msgSend$fileWriter
+ _objc_msgSend$fileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:expectedSize:asyncTrackingGroup:errorDelegate:error:
+ _objc_msgSend$fileWriterQueue
+ _objc_msgSend$finalizeFileWithTimestamp:mode:error:
+ _objc_msgSend$gid
+ _objc_msgSend$initWithReservationSize:
+ _objc_msgSend$insertAsyncFileOperation:error:
+ _objc_msgSend$integerForKey:
+ _objc_msgSend$isValid
+ _objc_msgSend$maxConcurrency
+ _objc_msgSend$maxPendingItemSize
+ _objc_msgSend$maxPendingOperationSize
+ _objc_msgSend$mode
+ _objc_msgSend$oflag
+ _objc_msgSend$omode
+ _objc_msgSend$pendingOperationPathsByGroupPointer
+ _objc_msgSend$pendingOperationSize
+ _objc_msgSend$pendingOperations
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$reservation
+ _objc_msgSend$reserveAsyncOperationForFileSize:path:group:operationPendingForPath:
+ _objc_msgSend$reservedSize
+ _objc_msgSend$runningOperationCount
+ _objc_msgSend$setCurrentOffset:error:
+ _objc_msgSend$setExecuteFileOperationFlags:
+ _objc_msgSend$setFileWriter:
+ _objc_msgSend$setGid:
+ _objc_msgSend$setIncompleteExtractionAttribute
+ _objc_msgSend$setMode:
+ _objc_msgSend$setOwnership
+ _objc_msgSend$setPendingOperationSize:
+ _objc_msgSend$setRunningOperationCount:
+ _objc_msgSend$setSetOwnership:
+ _objc_msgSend$setTime:
+ _objc_msgSend$setUid:
+ _objc_msgSend$setValid:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$standardUserDefaults
+ _objc_msgSend$streamingFileWriter:didEncounterError:
+ _objc_msgSend$suspendWithError:
+ _objc_msgSend$synchronousFileWriterForPath:withOpenFlags:mode:quarantineInfo:performCachedWrites:error:
+ _objc_msgSend$time
+ _objc_msgSend$trackingGroup
+ _objc_msgSend$uid
+ _objc_msgSend$valueWithNonretainedObject:
+ _objc_msgSend$writeBuffer:length:error:
+ _objc_retain_x28
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _sharedInstance.sharedInstance
- -[SZExtractor _prepareForExtractionSynchronously:withCompletionBlock:].cold.1
- -[SZExtractor _prepareForExtractionSynchronously:withCompletionBlock:].cold.2
- -[SZExtractor _serviceConnectionWithError:].cold.1
- -[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:].cold.1
- -[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:].cold.2
- -[SZExtractor _suspendStreamWithCompletionBlockSynchronously:completion:].cold.3
- -[SZExtractor finishStreamWithCompletionBlock:].cold.1
- -[SZExtractor finishStreamWithCompletionBlock:].cold.2
- -[SZExtractor finishStreamWithCompletionBlock:].cold.3
- -[SZExtractor setExtractorDelegate:].cold.1
- -[SZExtractor setExtractorDelegate:].cold.2
- -[SZExtractor supplyBytes:withCompletionBlock:].cold.1
- -[SZExtractor supplyBytes:withCompletionBlock:].cold.2
- -[SZExtractor supplyBytes:withCompletionBlock:].cold.3
- -[SZExtractor terminateStreamWithError:completionBlock:].cold.1
- -[SZExtractor terminateStreamWithError:completionBlock:].cold.2
- -[SZExtractor terminateStreamWithError:completionBlock:].cold.3
- -[SZExtractorInternalDelegate delegate]
- -[SZExtractorInternalDelegate setDelegate:]
- -[StreamingUnzipState _checkHashForOffset:].cold.1
- -[StreamingUnzipState checkLastChunkPartialHash].cold.1
- -[StreamingUnzipState checkLastChunkPartialHash].cold.2
- -[StreamingUnzipState currentOutputFD]
- -[StreamingUnzipState finishStream].cold.1
- -[StreamingUnzipState initWithPath:options:error:].cold.1
- -[StreamingUnzipState initWithPath:options:error:].cold.10
- -[StreamingUnzipState initWithPath:options:error:].cold.11
- -[StreamingUnzipState initWithPath:options:error:].cold.12
- -[StreamingUnzipState initWithPath:options:error:].cold.13
- -[StreamingUnzipState initWithPath:options:error:].cold.14
- -[StreamingUnzipState initWithPath:options:error:].cold.15
- -[StreamingUnzipState initWithPath:options:error:].cold.16
- -[StreamingUnzipState initWithPath:options:error:].cold.17
- -[StreamingUnzipState initWithPath:options:error:].cold.18
- -[StreamingUnzipState initWithPath:options:error:].cold.19
- -[StreamingUnzipState initWithPath:options:error:].cold.2
- -[StreamingUnzipState initWithPath:options:error:].cold.20
- -[StreamingUnzipState initWithPath:options:error:].cold.21
- -[StreamingUnzipState initWithPath:options:error:].cold.22
- -[StreamingUnzipState initWithPath:options:error:].cold.23
- -[StreamingUnzipState initWithPath:options:error:].cold.24
- -[StreamingUnzipState initWithPath:options:error:].cold.25
- -[StreamingUnzipState initWithPath:options:error:].cold.26
- -[StreamingUnzipState initWithPath:options:error:].cold.27
- -[StreamingUnzipState initWithPath:options:error:].cold.28
- -[StreamingUnzipState initWithPath:options:error:].cold.3
- -[StreamingUnzipState initWithPath:options:error:].cold.4
- -[StreamingUnzipState initWithPath:options:error:].cold.5
- -[StreamingUnzipState initWithPath:options:error:].cold.6
- -[StreamingUnzipState initWithPath:options:error:].cold.7
- -[StreamingUnzipState initWithPath:options:error:].cold.8
- -[StreamingUnzipState initWithPath:options:error:].cold.9
- -[StreamingUnzipState openCurrentOutputFDForPath:withOpenFlags:mode:error:]
- -[StreamingUnzipState openCurrentOutputFDForPath:withOpenFlags:mode:error:].cold.1
- -[StreamingUnzipState openCurrentOutputFDForPath:withOpenFlags:mode:error:].cold.2
- -[StreamingUnzipState openCurrentOutputFDForPath:withOpenFlags:mode:error:].cold.3
- -[StreamingUnzipState openCurrentOutputFDForPath:withOpenFlags:mode:error:].cold.4
- -[StreamingUnzipState serializeState].cold.1
- -[StreamingUnzipState serializeState].cold.2
- -[StreamingUnzipState serializeState].cold.3
- -[StreamingUnzipState serializeState].cold.4
- -[StreamingUnzipState serializeState].cold.5
- -[StreamingUnzipState serializeState].cold.6
- -[StreamingUnzipState setCurrentOutputFD:]
- -[StreamingUnzipState setStreamState:].cold.1
- -[StreamingUnzipState setStreamState:].cold.2
- -[StreamingUnzipState setStreamState:].cold.3
- -[StreamingUnzipState setStreamState:].cold.4
- -[StreamingUnzipState setStreamState:].cold.5
- -[StreamingUnzipState setStreamState:].cold.6
- -[StreamingUnzipState updateHashFromOffset:withBytes:length:onlyFinishCurrentChunk:].cold.1
- -[StreamingUnzipState updateHashFromOffset:withBytes:length:onlyFinishCurrentChunk:].cold.2
- -[StreamingUnzipState updateHashFromOffset:withBytes:length:onlyFinishCurrentChunk:].cold.3
- -[StreamingUnzipper _beginNonStreamablePassthroughWithRemainingBytes:length:].cold.1
- -[StreamingUnzipper _beginNonStreamablePassthroughWithRemainingBytes:length:].cold.2
- -[StreamingUnzipper _beginNonStreamablePassthroughWithRemainingBytes:length:].cold.3
- -[StreamingUnzipper _beginNonStreamablePassthroughWithRemainingBytes:length:].cold.4
- -[StreamingUnzipper _extractionEnteredPassThroughMode]
- -[StreamingUnzipper _sendExtractionCompleteAtArchivePath:]
- -[StreamingUnzipper _setErrorState].cold.1
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.1
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.10
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.11
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.12
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.13
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.14
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.15
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.16
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.17
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.18
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.19
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.2
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.20
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.21
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.22
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.23
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.24
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.25
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.26
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.27
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.28
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.29
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.3
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.30
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.31
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.32
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.33
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.34
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.35
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.36
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.37
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.38
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.39
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.4
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.40
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.41
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.42
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.43
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.44
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.45
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.46
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.47
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.5
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.6
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.7
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.8
- -[StreamingUnzipper _supplyBytes:length:withReply:].cold.9
- -[StreamingUnzipper finishStreamWithReply:].cold.1
- -[StreamingUnzipper finishStreamWithReply:].cold.2
- -[StreamingUnzipper finishStreamWithReply:].cold.3
- -[StreamingUnzipper finishStreamWithReply:].cold.4
- -[StreamingUnzipper finishStreamWithReply:].cold.5
- -[StreamingUnzipper finishStreamWithReply:].cold.6
- -[StreamingUnzipper finishStreamWithReply:].cold.7
- -[StreamingUnzipper setupUnzipperWithOutputPath:sandboxExtensionToken:options:withReply:].cold.1
- -[StreamingUnzipper setupUnzipperWithOutputPath:sandboxExtensionToken:options:withReply:].cold.2
- -[StreamingUnzipper setupUnzipperWithOutputPath:sandboxExtensionToken:options:withReply:].cold.3
- -[StreamingUnzipper setupUnzipperWithOutputPath:sandboxExtensionToken:options:withReply:].cold.4
- -[StreamingUnzipper setupUnzipperWithOutputPath:sandboxExtensionToken:options:withReply:].cold.5
- -[StreamingUnzipper suspendStreamWithReply:].cold.1
- -[StreamingUnzipper terminateStreamWithReply:].cold.1
- GCC_except_table19
- GCC_except_table22
- GCC_except_table26
- GCC_except_table40
- GCC_except_table47
- GCC_except_table95
- _CDRecordHasZip64ExtraField
- _CDRecordIsDirectory
- _CFStringCreateWithFormatAndArguments
- _CanSetUIDAndGID
- _CloseLocalFile.cold.1
- _CompressionAlgorithmIDForCompressionMethod
- _CompressionMethodUsesLibrary
- _ConvertZipToStream
- _ConvertZipToStream.cold.1
- _ConvertZipToStream.cold.10
- _ConvertZipToStream.cold.11
- _ConvertZipToStream.cold.12
- _ConvertZipToStream.cold.13
- _ConvertZipToStream.cold.14
- _ConvertZipToStream.cold.15
- _ConvertZipToStream.cold.2
- _ConvertZipToStream.cold.3
- _ConvertZipToStream.cold.4
- _ConvertZipToStream.cold.5
- _ConvertZipToStream.cold.6
- _ConvertZipToStream.cold.7
- _ConvertZipToStream.cold.8
- _ConvertZipToStream.cold.9
- _CopyFileNameFromCDRecord
- _CopyFileNameFromLocalFileRecord
- _CopyLocalFileRecord
- _CopyMutableCDRecord
- _CopyMutableLocalFileRecord
- _CopyNextCDRecord
- _CopyNextCDRecord.cold.1
- _CopyNextCDRecord.cold.2
- _CopyNextCDRecord.cold.3
- _CopyNextCDRecord.cold.4
- _CopyNextCDRecord.cold.5
- _CopyNextCDRecord.cold.6
- _CopyNextCDRecord.cold.7
- _CopyRawLocalFileHeader
- _CreateAndWriteCDRecord
- _CreateCDRecordFromMutable
- _CreateCDRecordFromMutable.cold.1
- _CreateLocalFileRecord.cold.1
- _CreateLocalFileRecordFromMutable
- _CreateLocalFileRecordFromMutable.cold.1
- _CreateMutableCDRecordFromMutableLFRecord
- _CreateZipStream
- _CreateZipStream.cold.1
- _CreateZipStream.cold.10
- _CreateZipStream.cold.11
- _CreateZipStream.cold.12
- _CreateZipStream.cold.13
- _CreateZipStream.cold.14
- _CreateZipStream.cold.15
- _CreateZipStream.cold.16
- _CreateZipStream.cold.17
- _CreateZipStream.cold.18
- _CreateZipStream.cold.19
- _CreateZipStream.cold.2
- _CreateZipStream.cold.20
- _CreateZipStream.cold.21
- _CreateZipStream.cold.22
- _CreateZipStream.cold.23
- _CreateZipStream.cold.24
- _CreateZipStream.cold.25
- _CreateZipStream.cold.26
- _CreateZipStream.cold.27
- _CreateZipStream.cold.3
- _CreateZipStream.cold.4
- _CreateZipStream.cold.5
- _CreateZipStream.cold.6
- _CreateZipStream.cold.7
- _CreateZipStream.cold.8
- _CreateZipStream.cold.9
- _ExtractFileToStream
- _ExtractFileToStream.cold.1
- _ExtractFileToStream.cold.2
- _ExtractFileToStream.cold.3
- _ExtractFileToStream.cold.4
- _ExtractFileToStream.cold.5
- _ExtractFileToStream.cold.6
- _ExtractFileToStream.cold.7
- _ExtractFileToStream.cold.8
- _ExtractFileToStream.cold.9
- _FetchGroupIDs.cold.1
- _GetCDRecordCompressedSize
- _GetCDRecordUncompressedSize
- _GetDiskNumberFromCDRecord
- _GetExtraFieldFromCDRecord
- _GetExtraFieldFromLocalFileRecord
- _GetFileCommentFromCDRecord
- _GetFileNameStringFromLocalFileRecord.cold.1
- _GetInfoZipExtraFieldFromCDRecord
- _GetInfoZipExtraFieldFromLF
- _GetLFCompressedSize
- _GetLFOffsetFromCDRecord
- _GetLFSizes
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
- _OBJC_IVAR_$_StreamingUnzipState._currentOutputFD
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _OpenLocalFileRaw
- _OpenZipFile.cold.1
- _OpenZipFile.cold.10
- _OpenZipFile.cold.11
- _OpenZipFile.cold.12
- _OpenZipFile.cold.13
- _OpenZipFile.cold.14
- _OpenZipFile.cold.15
- _OpenZipFile.cold.16
- _OpenZipFile.cold.17
- _OpenZipFile.cold.18
- _OpenZipFile.cold.19
- _OpenZipFile.cold.2
- _OpenZipFile.cold.20
- _OpenZipFile.cold.21
- _OpenZipFile.cold.22
- _OpenZipFile.cold.23
- _OpenZipFile.cold.24
- _OpenZipFile.cold.25
- _OpenZipFile.cold.26
- _OpenZipFile.cold.27
- _OpenZipFile.cold.28
- _OpenZipFile.cold.3
- _OpenZipFile.cold.4
- _OpenZipFile.cold.5
- _OpenZipFile.cold.6
- _OpenZipFile.cold.7
- _OpenZipFile.cold.8
- _OpenZipFile.cold.9
- _ReadLocalFileData.cold.1
- _ReadLocalFileData.cold.2
- _ReadLocalFileData.cold.3
- _ReadLocalFileData.cold.4
- _ReadLocalFileData.cold.5
- _ReadLocalFileData.cold.6
- _ReadLocalFileData.cold.7
- _ReadLocalFileData.cold.8
- _ReadLocalFileData.cold.9
- _SZConfiguredStreamingUnzipDelegateProtocolInterface
- _SZConfiguredStreamingUnzipProtocolInterface
- _SZCountedSetAddValue
- _SZCountedSetCreateMutable
- _SZCountedSetGetValueWithHighestCount
- _SZWrite
- _ZipStreamAddStatisticsForCDRecord.cold.1
- _ZipStreamAddStatisticsForCDRecord.cold.2
- _ZipStreamCallFlushCallback
- _ZipStreamCallProgressCallback
- _ZipStreamCallReadCallback
- _ZipStreamCallSeekCallback
- _ZipStreamCallTellCallback
- _ZipStreamCallTruncateCallback
- _ZipStreamCallWriteCallback
- _ZipStreamConcoctStreamData.cold.1
- _ZipStreamConcoctStreamData.cold.2
- _ZipStreamConfigureOutput.cold.1
- _ZipStreamConfigureOutput.cold.2
- _ZipStreamFILEReadCallback.cold.1
- _ZipStreamFILEWriteCallback.cold.1
- _ZipStreamModeIsNonStandard
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.1
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.10
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.11
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.12
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.13
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.14
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.2
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.3
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.4
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.5
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.6
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.7
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.8
- _ZipStreamWriteCentralDirectoryAndEndRecords.cold.9
- _ZipStreamWriteDictionaryToFile
- _ZipStreamWriteDictionaryToFile.cold.1
- _ZipStreamWriteDictionaryToFile.cold.2
- _ZipStreamWriteLocalFile.cold.1
- _ZipStreamWriteLocalFile.cold.10
- _ZipStreamWriteLocalFile.cold.11
- _ZipStreamWriteLocalFile.cold.12
- _ZipStreamWriteLocalFile.cold.13
- _ZipStreamWriteLocalFile.cold.14
- _ZipStreamWriteLocalFile.cold.15
- _ZipStreamWriteLocalFile.cold.16
- _ZipStreamWriteLocalFile.cold.17
- _ZipStreamWriteLocalFile.cold.18
- _ZipStreamWriteLocalFile.cold.19
- _ZipStreamWriteLocalFile.cold.2
- _ZipStreamWriteLocalFile.cold.20
- _ZipStreamWriteLocalFile.cold.21
- _ZipStreamWriteLocalFile.cold.22
- _ZipStreamWriteLocalFile.cold.23
- _ZipStreamWriteLocalFile.cold.24
- _ZipStreamWriteLocalFile.cold.25
- _ZipStreamWriteLocalFile.cold.26
- _ZipStreamWriteLocalFile.cold.3
- _ZipStreamWriteLocalFile.cold.4
- _ZipStreamWriteLocalFile.cold.5
- _ZipStreamWriteLocalFile.cold.6
- _ZipStreamWriteLocalFile.cold.7
- _ZipStreamWriteLocalFile.cold.8
- _ZipStreamWriteLocalFile.cold.9
- _ZipStreamWritePartialHashForLastChunk
- _ZipStreamWritePartialHashForLastChunk.cold.1
- _ZipStreamWritePartialHashForLastChunk.cold.10
- _ZipStreamWritePartialHashForLastChunk.cold.11
- _ZipStreamWritePartialHashForLastChunk.cold.12
- _ZipStreamWritePartialHashForLastChunk.cold.13
- _ZipStreamWritePartialHashForLastChunk.cold.2
- _ZipStreamWritePartialHashForLastChunk.cold.3
- _ZipStreamWritePartialHashForLastChunk.cold.4
- _ZipStreamWritePartialHashForLastChunk.cold.5
- _ZipStreamWritePartialHashForLastChunk.cold.6
- _ZipStreamWritePartialHashForLastChunk.cold.7
- _ZipStreamWritePartialHashForLastChunk.cold.8
- _ZipStreamWritePartialHashForLastChunk.cold.9
- __AddIndexToDictionary.cold.1
- __CheckRealpathHasBasePrefix.cold.1
- __CopyRawLocalFileHeaderAtOffset
- __CopyRawLocalFileHeaderAtOffset.cold.1
- __CopyRawLocalFileHeaderAtOffset.cold.2
- __CopyRawLocalFileHeaderAtOffset.cold.3
- __CopyRawLocalFileHeaderAtOffset.cold.4
- __CopyRawLocalFileHeaderAtOffset.cold.5
- __CopyRawLocalFileHeaderAtOffset.cold.6
- __CreateErrorV
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.1
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.10
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.11
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.12
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.13
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.14
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.2
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.3
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.4
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.5
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.6
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.7
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.8
- __GetCDIndexOfBundleExecutableForInfoPlist.cold.9
- __GetCRC32.cold.1
- __GetCRC32.cold.2
- __GetCompressedSize.cold.1
- __GetCompressedSize.cold.2
- __GetExtraFieldOfLength.cold.1
- __GetUncompressedSize.cold.1
- __GetUncompressedSize.cold.2
- __IsExcludedFileName.cold.1
- __IsOrderedEarly.cold.1
- __LogOutput
- __MutableZipStructureWrite
- __OBJC_$_PROP_LIST_SZExtractorInternalDelegate
- __OpenLocalFile
- __OpenLocalFile.cold.1
- __OpenLocalFile.cold.2
- __OpenLocalFile.cold.3
- __Prescan.cold.1
- __Prescan.cold.2
- __Prescan.cold.3
- __Prescan.cold.4
- __Prescan.cold.5
- __Prescan.cold.6
- __Prescan.cold.7
- __ReadOriginalCentralDirectory.cold.1
- __ReadOriginalCentralDirectory.cold.2
- __ReadOriginalCentralDirectory.cold.3
- __ReadOriginalCentralDirectory.cold.4
- __RemoveAndRecreateDirectoryAtPath.cold.1
- __RemoveAndRecreateDirectoryAtPath.cold.2
- __RemoveAndRecreateDirectoryAtPath.cold.3
- __RemoveAndRecreateDirectoryAtPath.cold.4
- __RemoveAndRecreateDirectoryAtPath.cold.5
- __SZLog
- __UpgradeCallbacksToCurrent.cold.1
- __WriteLocalFile.cold.1
- __WriteLocalFile.cold.2
- __WriteLocalFile.cold.3
- __WriteLocalFile.cold.4
- __WriteLocalFile.cold.5
- __WriteLocalFile.cold.6
- __WriteLocalFile.cold.7
- ___31-[SZExtractor encodeWithCoder:]_block_invoke.cold.1
- ___42-[SZExtractor _prepareForLocalExtraction:]_block_invoke.cold.1
- ___43-[StreamingUnzipper supplyBytes:withReply:]_block_invoke.cold.1
- ___44+[SZExtractor(Testing) servicePIDWithError:]_block_invoke.cold.1
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.185
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.185.cold.1
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.185.cold.2
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.192
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.199
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.201
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.201.cold.1
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.201.cold.2
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.201.cold.3
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.226
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.227
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke.231
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke_2.194
- ___47-[SZExtractor supplyBytes:withCompletionBlock:]_block_invoke_2.194.cold.1
- ___49-[SZExtractor setActiveExtractorDelegateMethods:]_block_invoke_2.cold.1
- ___58-[SZExtractor _synchronouslyPrepareForExtractionAtOffset:]_block_invoke.cold.1
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke.cold.1
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke.cold.2
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.122
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.138
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.138.cold.1
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.143
- ___76-[SZExtractor _prepareForRemoteExtractionSynchronously:withCompletionBlock:]_block_invoke_2.cold.1
- ___stderrp
- _gSZDefaultLogLevel
- _gSZLogPrefix
- _gSZLogToSyslog
- _kEndRecordSignature
- _kFixedMetadataMagic
- _kInfoZipNewUnixExtraFieldSignature
- _kInfoZipTimestampExtraFieldSignature
- _kLocalFileRecordSignature
- _kZip64EndRecordLocatorSignature
- _kZip64EndRecordSignature
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
- _objc_msgSend$_beginNonStreamablePassthroughWithRemainingBytes:length:
- _objc_msgSend$_checkHashForOffset:
- _objc_msgSend$_extractionEnteredPassThroughMode
- _objc_msgSend$_sendExtractionCompleteAtArchivePath:
- _objc_msgSend$_sendExtractionProgress:
- _objc_msgSend$_setErrorState
- _objc_msgSend$_supplyBytes:length:withReply:
- _objc_msgSend$delegate
- _objc_msgSend$initWithPath:options:error:
- _objc_msgSend$openCurrentOutputFDForPath:withOpenFlags:mode:error:
- _objc_msgSend$setDelegate:
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
+ "Failed to create path from %s/%s : %s"
+ "Failed to fchown %@ to (%d:%d) : %d (%s)"
+ "Failed to read bytes from %@ : %d (%s)"
+ "Failed to seek to current offset in output file at path %@ : %s"
+ "Failed to seek to offset %llu in output file at path %@ : %s"
+ "Failed to set times on %@ : %s"
+ "Failed to write data to output file at %@: %s"
+ "Failed to write initial data to passthrough output file"
+ "Failed to write remaining initial data to passthrough output file"
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
+ "boolForKey:"
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
+ "standardUserDefaults"
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
- "+[SZExtractor(KnownImplementations) knownSZExtractorImplementations]_block_invoke"
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
- "-[StreamingUnzipState openCurrentOutputFDForPath:withOpenFlags:mode:error:]"
- "-[StreamingUnzipper _setErrorState]"
- "-[StreamingUnzipper dealloc]"
- "-[StreamingUnzipper setActiveDelegateMethods:]"
- "-[StreamingUnzipper supplyBytes:withReply:]_block_invoke"
- "@24@0:8Q16"
- "@32@0:8r^v16Q24"
- "B40@0:8@16i24S28^@32"
- "CloseLocalFile"
- "ConvertZipToStream"
- "CopyNextCDRecord returned NULL and status %d"
- "CreateZipStream"
- "ExtractFileToStream"
- "Failed to create log string"
- "Failed to fchown %s to (%d:%d) : %d (%s)"
- "Failed to seek to offset %llu in output file at path %@: %s"
- "Failed to write data to output file %@: %s"
- "Failed to write data to passthrough output file: %s"
- "Failed to write decompressed data to output file %@ : %s"
- "Failed to write initial data to passthrough output file: %s"
- "Failed to write remaining initial data to passthrough output file: %s"
- "GetFileNameStringFromLocalFileRecord"
- "Malloc failed for path buffer"
- "OpenZipFile"
- "ReadLocalFileData"
- "StreamingZip"
- "T@\"<SZExtractorDelegate>\",W,Vdelegate"
- "TB,R,D,N"
- "TB,R,N"
- "ZipStreamAddStatisticsForCDRecord"
- "ZipStreamConfigureOutput"
- "ZipStreamFILEReadCallback"
- "ZipStreamFILEWriteCallback"
- "ZipStreamWriteDictionaryToFile"
- "_AddIndexToDictionary"
- "_CopyRawLocalFileHeaderAtOffset"
- "_ExtractFile"
- "_GetCDEndRecord"
- "_GetCDIndexOfBundleExecutableForInfoPlist"
- "_HashTypeForString"
- "_IsExcludedFileName"
- "_IsOrderedEarly"
- "_OpenLocalFile"
- "_OrderEarlyExecutable"
- "_Prescan"
- "_ProcessZipFile"
- "_ReadZip64Records"
- "_RemoveAndRecreateDirectoryAtPath"
- "_UpgradeCallbacksToCurrent"
- "_ValidateDictionaryKeyValueType"
- "_WriteFileToDisk"
- "_WriteLocalFile"
- "_WriteLocalFileData"
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
- "bufLen <= UINT32_MAX"
- "initWithPath:options:error:"
- "openCurrentOutputFDForPath:withOpenFlags:mode:error:"
- "rA"
- "v40@0:8r*16Q24@?32"
- "\xa4\xf0ԡ"
- "\xb2"

```
