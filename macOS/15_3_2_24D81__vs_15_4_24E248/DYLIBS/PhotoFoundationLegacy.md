## PhotoFoundationLegacy

> `/System/Library/PrivateFrameworks/PhotoFoundationLegacy.framework/Versions/A/PhotoFoundationLegacy`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x520d8
+751.0.104.0.0
+  __TEXT.__text: 0x51ef0
   __TEXT.__auth_stubs: 0xe50
-  __TEXT.__objc_methlist: 0x5e54
+  __TEXT.__objc_methlist: 0x662c
   __TEXT.__const: 0x2c8
   __TEXT.__gcc_except_tab: 0xdf0
-  __TEXT.__cstring: 0x8eae
+  __TEXT.__cstring: 0x8eab
   __TEXT.__oslogstring: 0x219
   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0x1d20

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3350
+  __DATA_CONST.__objc_selrefs: 0x33c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x738
   __AUTH_CONST.__const: 0x18c0
   __AUTH_CONST.__cfstring: 0x3880
-  __AUTH_CONST.__objc_const: 0xaa90
+  __AUTH_CONST.__objc_const: 0x9c40
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2440

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D9694400-1C64-313B-93D9-F3519634E060
-  Functions: 2498
+  UUID: 573545A8-DCA0-30C1-A2D2-6F32FE9F78BF
+  Functions: 2496
   Symbols:   5741
-  CStrings:  4150
+  CStrings:  4149
 
Functions:
~ _PF_QOSClassOfName : 296 -> 268
~ +[PFDispatchQueueClearingExtension alloc] : 100 -> 88
~ -[PFDispatchQueueClearingExtension queue:didDequeue:skipExecution:] : 204 -> 200
~ -[PFDispatchQueueClearingExtension doPurge:wait:] : 228 -> 224
~ -[PFDispatchQueueClearingExtension countOfPurgingQueues] : 84 -> 88
~ ___24-[PFWorkContext nextJob]_block_invoke : 216 -> 212
~ -[PFWorkContext _updateDisplayForcing:] : 292 -> 288
~ -[PFWorkContext setControlState:] : 184 -> 188
~ -[PFWorkContext setStage:] : 184 -> 188
~ -[PFWorkContext setState:] : 184 -> 188
~ -[PFWorkContext initWithName:delegate:qosServiceType:concurrency:] : 848 -> 804
~ -[PFWorkContext(BackgroundServiceManager) dispatchWorkContextResumedFromStallWithReply:] : 644 -> 640
~ -[PFWorkContext(BackgroundServiceManager) dispatchWorkContextStalled:reply:] : 688 -> 684
~ -[PFWorkContext(BackgroundServiceManager) dispatchResumeWorkWithReply:] : 644 -> 640
~ -[PFWorkContext(BackgroundServiceManager) dispatchSuspendWorkWithReply:] : 644 -> 640
~ -[PFWorkContext(BackgroundServiceManager) dispatchCancelWorkWithReply:] : 668 -> 664
~ -[PFWorkContext(BackgroundServiceManager) dispatchEndWorkWithReply:] : 668 -> 664
~ -[PFWorkContext(BackgroundServiceManager) dispatchEndBatch:withReply:] : 688 -> 684
~ -[PFWorkContext(BackgroundServiceManager) dispatchPerformJob:withReply:] : 1092 -> 1088
~ __72-[PFWorkContext(BackgroundServiceManager) dispatchPerformJob:withReply:]_block_invoke.40 : 216 -> 212
~ -[PFWorkContext(BackgroundServiceManager) dispatchBeginBatch:withReply:] : 688 -> 684
~ -[PFWorkContext(BackgroundServiceManager) dispatchCreateBatchWithReply:] : 800 -> 796
~ ___72-[PFWorkContext(BackgroundServiceManager) dispatchCreateBatchWithReply:]_block_invoke_2 : 224 -> 220
~ -[PFWorkContext(BackgroundServiceManager) dispatchBeginWorkWithReply:] : 712 -> 708
~ ___44-[PFPriorityQueueExtension resumeScheduling]_block_invoke : 116 -> 104
~ -[PFPriorityQueueExtension _scheduleNextBlock] : 1056 -> 1060
~ -[PFPriorityQueueExtension installOnQueue:] : 428 -> 424
~ -[PFPriorityQueueExtension initWithPriorityLevels:concurrentScheduling:] : 420 -> 428
~ -[PFURLEventHandler retryPendingURLs] : 416 -> 412
~ -[PFURLEventHandler hasPendingURLs] : 216 -> 212
~ ___54-[PFBSMResourceIdentifier _reportUnresponsiveClients:]_block_invoke : 560 -> 564
~ -[PFBSMResourceIdentifier tryResourceShutdownIgnoringClients:whenComplete:] : 1296 -> 1276
~ __75-[PFBSMResourceIdentifier tryResourceShutdownIgnoringClients:whenComplete:]_block_invoke.138 : 96 -> 100
~ -[PFBSMResourceIdentifier _clientsBlockingShutdown] : 408 -> 404
~ -[PFJobTimer start] : 100 -> 92
~ -[PFTimeIntervalCoalescer dispatch_after:queue:block:] : 632 -> 628
~ -[PFDispatchQueueOSTransactionExtension _blockCompleted] : 116 -> 112
~ -[PFDispatchQueueOSTransactionExtension newBlockInfo] : 288 -> 284
~ -[PFDispatchQueueOSTransactionExtension installOnQueue:] : 108 -> 104
~ -[PFFileIStream streamData:] : 204 -> 200
~ +[PFFile createEmptyTempFileInBaseDirectory:withSubDirectoryNamed:filenamePrefix:pathExtension:error:] : 972 -> 968
~ +[PFFile uniqueFileSystemNameForName:inDirectory:] : 1240 -> 1256
~ +[PFFile fileExists:] : 88 -> 92
~ -[PFDirectoryEnumerator nextObject] : 1216 -> 1232
- sub_243d55448
~ -[PFFolder setFolders:] : 124 -> 120
~ -[PFFile fileType] : 140 -> 100
~ -[PFFile cachedStat] : 152 -> 156
~ -[PFLoggerBackendAppleArchive logFromCodeLocation:facility:subsystem:level:message:format:args:] : 576 -> 568
~ -[PFLoggerBackendAppleArchive close] : 116 -> 112
~ -[PFLoggerBackendAppleArchive flushWithCompletionHandler:] : 140 -> 136
~ -[PFWeakContainer stopTrackingWeakObjectDealloc:] : 96 -> 84
~ -[PFWeakContainer trackWeakObjectDealloc:] : 96 -> 84
~ -[PFWeakContainer isTrackingWeakObjectDealloc:] : 96 -> 84
~ ___31-[PFWeakHash payloadForObject:]_block_invoke : 132 -> 136
~ ___35-[PFWeakHash setPayload:forObject:]_block_invoke : 112 -> 116
~ -[PFWeakHash allObjects] : 200 -> 196
~ ___21-[PFWeakHash member:]_block_invoke : 148 -> 152
~ -[PFWeakHash removeObject:] : 352 -> 356
~ ___27-[PFWeakHash removeObject:]_block_invoke : 388 -> 392
~ -[PFWeakHash _processNilledWeakReferences] : 312 -> 316
~ -[PFWeakHash _purgeOrphanedPayloads] : 264 -> 276
~ -[PFWeakHash _resize] : 384 -> 380
~ -[PFWeakHash _bucketForObject:foundInHash:] : 536 -> 516
~ -[PFWeakHash _rehashWithNewCapacity:] : 664 -> 676
~ -[PFWeakHash removeAllObjects] : 200 -> 204
~ -[PFWeakHash _serialize:] : 224 -> 220
~ -[PFBackgroundServiceManager processNextJobInBatch:forWorkContext:] : 732 -> 728
~ -[PFBackgroundServiceManager performNextStepForContext:] : 1284 -> 1312
- sub_243d5d368
~ -[_PFDQRBEThreadStack .cxx_destruct] : 84 -> 96
~ +[PFDispatchQueueRunBlockExtension alloc] : 100 -> 88
~ -[PFDispatchQueueDebugExtension recordBlockInfo:] : 192 -> 188
~ +[PFBase64Codec encodeUuid:] : 116 -> 120
~ +[PFBase64Codec encodeData:] : 116 -> 120
~ +[PFBase64Codec decodeString:with:] : 624 -> 600
~ +[PFBase64Codec encodeBytes:withLength:] : 1080 -> 1056
~ -[PFStateMachine _handleEvent:] : 608 -> 588
~ -[PFLogger flush] : 196 -> 200
~ -[PFLogger logFromCodeLocation:subsystem:level:format:arguments:] : 884 -> 892
~ +[PFLogger logCrashReporterMessageFromCodeLocation:format:] : 232 -> 236
~ ___53+[PFLogger logCrashReporterMessage:fromCodeLocation:]_block_invoke_2 : 368 -> 364
~ -[PFCanceler addObserver:] : 296 -> 300
~ ___26-[PFCanceler addObserver:]_block_invoke : 140 -> 144
~ -[PFCanceler cancel] : 244 -> 248
~ ___20-[PFCanceler cancel]_block_invoke : 40 -> 36
~ -[_PFDeferredInitializationTriggerWorkItem init] : 252 -> 248
~ -[_PFTriggeredWorkItem doAllWorkItems] : 304 -> 300
~ -[_PFTriggeredWorkItem doOneWorkItem] : 248 -> 244
~ -[_PFTriggeredWorkItem addTriggeredWorkItem:] : 128 -> 124
~ _PFInitializationSetAdditionalClasses : 96 -> 88
~ -[_PFMulticasterReceiverList .cxx_destruct] : 68 -> 76
~ -[PFMulticaster distributeSelector:distributionBlock:] : 784 -> 780
~ -[PFMulticaster weakHashBecameEmpty:] : 104 -> 100
~ -[PFMulticaster invalidate] : 96 -> 92
~ -[PFMulticaster stopAcceptingReceivers] : 96 -> 92
~ -[PFMulticaster removeReceiver:] : 336 -> 332
~ -[PFMulticaster addWeakReceiver:] : 288 -> 280
~ -[PFMulticaster addReceiver:] : 284 -> 276
~ __assignImpsForMethods : 392 -> 396
~ +[PFMulticaster _multicasterClassForProtocolNamed:] : 444 -> 436
~ +[_PFPlaceholderMulticaster placeholderSubclassOfClass:named:] : 424 -> 420
~ -[PFAction canRedo] : 80 -> 84
~ -[PFAction canUndo] : 72 -> 80
~ -[PFAction implementsUndo] : 68 -> 72
~ +[PFSerialQueue _newQueueWithLabel:qos:targetQueue:] : 236 -> 232
~ +[PFConcurrentQueue _newQueueWithLabel:qos:targetQueue:] : 268 -> 264
~ -[PFLoggerBackendOSLog _logFromCodeLocation:subsystem:type:] : 280 -> 272
~ -[PFLoggerBackendOSLog logFromCodeLocation:facility:subsystem:level:message:format:args:] : 248 -> 252
~ -[PFActionGroup canUndo] : 264 -> 256
~ ___24-[PFActionGroup canUndo]_block_invoke : 132 -> 128
~ -[PFActionGroup _usingAction:performBlock:] : 352 -> 348
~ -[PFWorkBatch unprocessedJobs] : 124 -> 120
~ -[PFWorkBatch unprocessedJobCount] : 76 -> 72
~ -[PFWorkBatch nextJob] : 172 -> 168
~ -[PFWorkBatch removeAllJobs] : 144 -> 132
~ -[PFWorkBatch removeJob:] : 276 -> 272
~ -[PFWorkBatch jobForUuid:] : 124 -> 120
~ -[PFWorkBatch addJob:] : 172 -> 160
~ -[PFWorkBatch jobCount] : 68 -> 64
~ ___38-[PFCache _removeObjectForKey:notify:]_block_invoke_2 : 120 -> 116
~ -[PFCacheApproximateLRUMaximumCountPolicy willAddOrReplaceEntry:add:contents:] : 436 -> 440
~ -[PFCacheApproximateLRUMaximumCountPolicy _rebuildConsiderationKeys:] : 504 -> 492
~ ___28-[PFPurgeableData endAccess]_block_invoke : 220 -> 228
~ ___31-[PFPurgeableData beginAccess:]_block_invoke : 296 -> 304
~ ___30-[PFPurgeableData beginAccess]_block_invoke : 152 -> 160
~ -[PFPurgeableData resetLRUValue] : 224 -> 216
~ ___32-[PFPurgeableData resetLRUValue]_block_invoke : 104 -> 108
~ ___33-[PFPurgeableData setPurgeLevel:]_block_invoke : 104 -> 108
~ -[PFPurgeableData purgeState] : 212 -> 208
~ -[PFPurgeableData _markBlockUnpurgeable] : 200 -> 192
~ -[PFPurgeableData _checkAccess] : 168 -> 152
~ +[PFUuidData isCanonicalUuidString:] : 192 -> 188
~ __localizedStringForDateRange : 680 -> 676
~ _pf_time_string : 376 -> 368
~ +[PFStringUtilities dataForHexString:] : 336 -> 332
~ +[PFStringUtilities hexStringForData:] : 260 -> 256
~ -[NSDictionary(PFStringUtilities) _uniquedDictionary:] : 452 -> 456
~ -[PFTemporaryBuffer .cxx_destruct] : 148 -> 176
~ -[PFTemporaryBuffer _retireRecent] : 700 -> 696
~ -[PFTemporaryBuffer _enforceRetiredMaximum:] : 232 -> 228
~ -[PFTemporaryBuffer _scheduleEnforceRetiredMaximum:] : 184 -> 188
~ -[PFTemporaryBuffer _scheduleRetireRecent] : 156 -> 160
~ -[PFTemporaryBuffer _pruneRetired:] : 308 -> 304
~ -[PFTemporaryBuffer initWithName:maximumSize:maximumRetiredCount:roundTo:maximumWaste:] : 312 -> 308
~ -[PFDispatchQueueExtensionManager .cxx_destruct] : 60 -> 92
~ -[PFDispatchQueueExtensionManager queueWillResume:] : 88 -> 92
~ -[PFDispatchQueueExtensionManager queueDidSuspend:] : 88 -> 92
~ -[PFDispatchQueueExtensionManager addExtensions:queue:] : 428 -> 424
~ +[PFUtilities hasInternalPhotosDiagnosticsCapability] : 68 -> 72
~ +[PFUtilities runningUnderDebugger] : 68 -> 72
~ _pf_dispatch_seconds : 116 -> 104
~ -[PFDateRangeStringRepresentationController stopAutoUpdating] : 100 -> 88
~ +[PFSingletonInitialization _sharedConditionLock] : 828 -> 824
~ -[PFLimitedConcurrencySlotQueue initWithConcurrentQueue:targetQueue:slotIndex:] : 412 -> 408
~ ___61-[PFLimitedConcurrencyQueueClass dispatchAsyncWithQOS:block:]_block_invoke : 644 -> 640
~ ___48-[PFLimitedConcurrencyQueueClass dispatchAsync:]_block_invoke : 628 -> 624
~ __47-[PFLimitedConcurrencyQueueClass dispatchSync:]_block_invoke.73 : 724 -> 708
~ -[PFLimitedConcurrencyQueueClass enqueueDelayedDrop] : 280 -> 276
~ +[PFLimitedConcurrencyQueue _newQueueWithLabel:qos:targetQueue:] : 268 -> 264
~ _PFTextRingBufferCreate : 100 -> 108
~ _PFTextRingBufferDestroy : 52 -> 56
~ _PFTextRingBufferCopy : 196 -> 204
~ -[PFBlockControl groupNotify:] : 260 -> 256
~ -[PFBlockControl enqueueWithDelay:] : 296 -> 292
~ -[PFBlockControl enqueue] : 288 -> 284
~ -[PFBlockControl dequeue] : 164 -> 168
~ -[PFBlockControl tryCancelBlock] : 140 -> 144
~ -[PFBlockControl invoke:] : 240 -> 244
~ -[PFBlockControl dealloc] : 116 -> 120
~ -[PFLoggerBackendAdapter beginTransaction] : 104 -> 96
~ -[PFDispatchQueueBlockOnDemandExtension installOnQueue:] : 116 -> 112
~ -[PFChecksum initWithChecksumAsData:] : 200 -> 196
~ -[PFChecksum initWithData:] : 200 -> 196
~ -[PFLoggerBackendFile writeOpenFileAtURL:] : 872 -> 868
~ -[PFLoggerBackendFile initWithFileHandle:] : 244 -> 240
~ -[PFLoggerBackendFile dealloc] : 116 -> 120
~ -[PFInitializationWorkItem _targetQueue] : 80 -> 84
~ -[PFInitializationWorkItem addInitializationCompletionCallbackBlock_no_lock:] : 216 -> 220
~ -[PFInitializationWorkItem waitForInitialization] : 296 -> 300
~ ___42-[PFInitializationWorkItem addDependency:]_block_invoke : 144 -> 148
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/actions/PFAction.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/actions/PFResourceAccessAction.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/appleevents/PFURLEventHandler.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/cache/PFChecksum.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/initialization/PFInitialization.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/initialization/PFInitializationWorkItem.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/initialization/PFSingletonInitialization.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/logging/PFLoggerBackend.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/BackgroundProcessingManager/PFBackgroundServiceManager+Resource.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/Job/PFJob.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/PFBackgroundServiceManager.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/PFWorkBatch.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/PFWorkContext.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/string/PFString.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFAsyncTaskBarrier.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFBlockControl.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFBookmarkCoordinator.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFCache.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFCanceler.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDateRangeStringRepresentationController.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueue.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueDebugExtension.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueExtending.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueExtensionManager.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueStatisticsExtension.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFLimitedConcurrencyQueue.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFPriorityQueueExtension.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFFile.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFMulticaster.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFNotification.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFOnce.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFPropertyListUtilities.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFQOSUtilities.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFTemporaryBuffer.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFUtilities.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/containers/PFWeakContainer.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/containers/PFWeakHash.m"
- ".."
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/actions/PFAction.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/actions/PFResourceAccessAction.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/appleevents/PFURLEventHandler.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/cache/PFChecksum.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/initialization/PFInitialization.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/initialization/PFInitializationWorkItem.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/initialization/PFSingletonInitialization.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/logging/PFLoggerBackend.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/BackgroundProcessingManager/PFBackgroundServiceManager+Resource.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/Job/PFJob.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/PFBackgroundServiceManager.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/PFWorkBatch.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/services/JobControl/PFWorkContext.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/string/PFString.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFAsyncTaskBarrier.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFBlockControl.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFBookmarkCoordinator.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFCache.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFCanceler.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDateRangeStringRepresentationController.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueue.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueDebugExtension.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueExtending.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueExtensionManager.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFDispatchQueueStatisticsExtension.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFLimitedConcurrencyQueue.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFDispatchQueue/PFPriorityQueueExtension.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFFile.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFMulticaster.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFNotification.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFOnce.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFPropertyListUtilities.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFQOSUtilities.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFTemporaryBuffer.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/PFUtilities.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/containers/PFWeakContainer.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos_Apps/lib/photofoundationlegacy/source/util/containers/PFWeakHash.m"

```
