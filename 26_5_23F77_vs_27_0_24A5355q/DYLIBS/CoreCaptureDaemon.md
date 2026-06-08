## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1330.5.0.0.0
-  __TEXT.__text: 0x471cc
-  __TEXT.__auth_stubs: 0x1270
-  __TEXT.__const: 0x518
-  __TEXT.__gcc_except_tab: 0x2cc
-  __TEXT.__oslogstring: 0x7ad7
-  __TEXT.__cstring: 0x91c1
-  __TEXT.__unwind_info: 0x688
-  __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x131
-  __TEXT.__objc_stubs: 0x1c0
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x388
+1355.39.0.0.0
+  __TEXT.__text: 0x5b220
+  __TEXT.__const: 0x538
+  __TEXT.__gcc_except_tab: 0x4ec
+  __TEXT.__oslogstring: 0xb554
+  __TEXT.__cstring: 0xb956
+  __TEXT.__unwind_info: 0x7d0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
+  __DATA_CONST.__const: 0x3d0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x948
-  __AUTH_CONST.__const: 0x1168
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1230
   __AUTH_CONST.__cfstring: 0xc40
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x9c0
   __DATA.__data: 0x1
-  __DATA.__common: 0x3c
-  __DATA.__bss: 0x188
+  __DATA.__common: 0x24
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__common: 0x11
+  __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libIOReport.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6A74EE66-2985-3061-9803-B182E43EF548
-  Functions: 532
-  Symbols:   1164
-  CStrings:  1463
+  UUID: A00482C8-77C2-39C6-9D6D-1539A166D4B7
+  Functions: 613
+  Symbols:   1321
+  CStrings:  2011
 
Symbols:
+ GCC_except_table210
+ GCC_except_table225
+ GCC_except_table274
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table410
+ GCC_except_table411
+ GCC_except_table413
+ GCC_except_table415
+ GCC_except_table416
+ GCC_except_table452
+ GCC_except_table459
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table466
+ GCC_except_table468
+ GCC_except_table470
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table479
+ GCC_except_table483
+ GCC_except_table493
+ GCC_except_table531
+ GCC_except_table559
+ GCC_except_table568
+ GCC_except_table580
+ GCC_except_table581
+ GCC_except_table596
+ GCC_except_table607
+ GCC_except_table608
+ GCC_except_table72
+ GCC_except_table75
+ _CFDictionaryRemoveAllValues
+ _CFNotificationCenterRemoveObserver
+ _CFStringCreateCopy
+ __Z14getCCLogHandlev
+ __ZGVZN10CCDatabase11getInstanceEvE8instance
+ __ZL16cacheDeleteQueue
+ __ZL20cleanupXPCConnectionRP17_xpc_connection_s
+ __ZL23cleanupCacheDeleteQueuev
+ __ZN10CCDatabase10findStreamEP11CCPipeEntryPK10__CFString
+ __ZN10CCDatabase10getStreamsEPK10__CFStringS2_
+ __ZN10CCDatabase10removePipeEPK10__CFStringS2_
+ __ZN10CCDatabase11getInstanceEv
+ __ZN10CCDatabase11removeOwnerEPK10__CFString
+ __ZN10CCDatabase12getPipeEntryEPK10__CFStringS2_
+ __ZN10CCDatabase12removeStreamEPK10__CFStringS2_S2_
+ __ZN10CCDatabase13getPipeConfigEPK10__CFStringS2_
+ __ZN10CCDatabase14getStreamEntryEPK10__CFStringS2_S2_
+ __ZN10CCDatabase15getPipePropertyEPK10__CFStringS2_S2_
+ __ZN10CCDatabase15getStreamConfigEPK10__CFStringS2_S2_
+ __ZN10CCDatabase15setPipePropertyEPK10__CFStringS2_S2_S2_
+ __ZN10CCDatabase17getStreamPropertyEPK10__CFStringS2_S2_S2_
+ __ZN10CCDatabase17setStreamPropertyEPK10__CFStringS2_S2_S2_S2_
+ __ZN10CCDatabase18removePipePropertyEPK10__CFStringS2_S2_
+ __ZN10CCDatabase19getPipePropertyKeysEPK10__CFStringS2_
+ __ZN10CCDatabase20removeStreamPropertyEPK10__CFStringS2_S2_S2_
+ __ZN10CCDatabase21getStreamPropertyKeysEPK10__CFStringS2_S2_
+ __ZN10CCDatabase5resetEv
+ __ZN10CCDatabase7addPipeEPK10__CFStringS2_PK12CCPipeConfig
+ __ZN10CCDatabase7hasPipeEPK10__CFStringS2_
+ __ZN10CCDatabase8addOwnerEPK10__CFString
+ __ZN10CCDatabase8findPipeEP12CCOwnerEntryPK10__CFString
+ __ZN10CCDatabase8getPipesEPK10__CFString
+ __ZN10CCDatabase8hasOwnerEPK10__CFString
+ __ZN10CCDatabase9addStreamEPK10__CFStringS2_S2_PK14CCStreamConfig
+ __ZN10CCDatabase9findOwnerEPK10__CFString
+ __ZN10CCDatabase9getOwnersEv
+ __ZN10CCDatabase9hasStreamEPK10__CFStringS2_S2_
+ __ZN10CCDatabaseC1Ev
+ __ZN10CCDatabaseC2Ev
+ __ZN10CCDatabaseD1Ev
+ __ZN10CCDatabaseD2Ev
+ __ZN11CCPipeEntryC1ERKS_
+ __ZN11CCPipeEntryC1Ev
+ __ZN11CCPipeEntryC2ERKS_
+ __ZN11CCPipeEntryC2Ev
+ __ZN11CCPipeEntryD1Ev
+ __ZN11CCPipeEntryD2Ev
+ __ZN11CCPipeEntryaSERKS_
+ __ZN12CCOwnerEntryC1ERKS_
+ __ZN12CCOwnerEntryC1Ev
+ __ZN12CCOwnerEntryC2ERKS_
+ __ZN12CCOwnerEntryC2Ev
+ __ZN12CCOwnerEntryD1Ev
+ __ZN12CCOwnerEntryD2Ev
+ __ZN12CCOwnerEntryaSERKS_
+ __ZN12CCXPCService23cancelActiveConnectionsEv
+ __ZN12CCXPCService27cleanupAndUntrackConnectionERP17_xpc_connection_s
+ __ZN13CCStreamEntryC1ERKS_
+ __ZN13CCStreamEntryC1Ev
+ __ZN13CCStreamEntryC2ERKS_
+ __ZN13CCStreamEntryC2Ev
+ __ZN13CCStreamEntryD1Ev
+ __ZN13CCStreamEntryD2Ev
+ __ZN13CCStreamEntryaSERKS_
+ __ZN15CCTextFormatter16setLogIdentifierEPK10__CFString
+ __ZN16CCProfileMonitor15cancelObserversEv
+ __ZN16CCProfileMonitor15profileCallbackE21CCProfileChangeSource
+ __ZN16CCProfileMonitor29sendProfileChangeNotificationE21CCProfileChangeSource
+ __ZN17CCPcapngFormatter4initEv
+ __ZN6CCFile17setCaptureDirPathEPK10__CFString
+ __ZN6CCFile8moveFileEPKc
+ __ZN8CCDaemon29sendProfileChangeNotificationE21CCProfileChangeSource
+ __ZN9CCLogFile10withConfigEPK12CCPipeConfigPK10__CFStringS5_
+ __ZN9CCLogFile14initWithConfigEPK12CCPipeConfigPK10__CFStringS5_
+ __ZN9CCLogFile9closeMMAPERNS_12WriteContextEi
+ __ZNKSt11logic_error4whatEv
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt12length_errorD0Ev
+ __ZNSt12length_errorD1Ev
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__15dequeI14StackshotEntryNS_9allocatorIS1_EEED2B9fqe220100Ev
+ __ZNSt3__16vectorIP17_xpc_connection_sNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIP17_xpc_connection_sNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__19allocatorIP14StackshotEntryE17allocate_at_leastB9fqe220100Em
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZTISt12length_error
+ __ZTVSt12length_error
+ __ZZ12isSeedAndiOSE3ret
+ __ZZ12isSeedAndiOSE9onceToken
+ __ZZ14getCCLogHandlevE9logHandle
+ __ZZ14getCCLogHandlevE9onceToken
+ __ZZ18isForceCopyEnabledE3ret
+ __ZZ18isForceCopyEnabledE9onceToken
+ __ZZ21isCacheDeleteDisabledE3ret
+ __ZZ21isCacheDeleteDisabledE9onceToken
+ __ZZL18initializeBootArgsvE9onceToken
+ __ZZN10CCDatabase11getInstanceEvE8instance
+ ___CCCacheDeleteEnablePurgeNotification_block_invoke.18
+ ___CCCacheDeleteEnablePurgeNotification_block_invoke_2.21
+ ____Z14getCCLogHandlev_block_invoke
+ ____ZL18initializeBootArgsv_block_invoke
+ ____ZL20cleanupXPCConnectionRP17_xpc_connection_s_block_invoke
+ ____ZL23cleanupCacheDeleteQueuev_block_invoke
+ ____ZN12CCXPCService13freeResourcesEv_block_invoke
+ ____ZN12CCXPCService23cancelActiveConnectionsEv_block_invoke
+ ____ZN16CCProfileMonitor15cancelObserversEv_block_invoke
+ ____ZN9CCLogFile9closeFileEv_block_invoke
+ ____ZN9CCLogFile9closeFileEv_block_invoke_2
+ ___block_descriptor_32_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_tmp.150
+ ___block_descriptor_tmp.1812
+ ___block_descriptor_tmp.2188
+ ___block_descriptor_tmp.2415
+ ___block_descriptor_tmp.2690
+ ___block_descriptor_tmp.377
+ ___block_descriptor_tmp.54
+ ___block_descriptor_tmp.55
+ ___block_descriptor_tmp.56
+ ___block_descriptor_tmp.59
+ ___block_descriptor_tmp.69
+ ___block_descriptor_tmp.78
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.867
+ ___block_literal_global.10
+ ___block_literal_global.103
+ ___block_literal_global.1189
+ ___block_literal_global.1221
+ ___block_literal_global.15
+ ___block_literal_global.165
+ ___block_literal_global.170
+ ___block_literal_global.1728
+ ___block_literal_global.23
+ ___block_literal_global.25
+ ___block_literal_global.2500
+ ___block_literal_global.4
+ ___block_literal_global.43
+ ___block_literal_global.55
+ ___block_literal_global.7
+ ___block_literal_global.75
+ ___block_literal_global.868
+ ___block_literal_global.93
+ ___cxa_atexit
+ ___cxa_guard_abort
+ ___cxa_guard_acquire
+ ___cxa_guard_release
+ ___isCacheDeleteDisabled_block_invoke
+ ___isForceCopyEnabled_block_invoke
+ ___isSeedAndiOS_block_invoke
+ ___triggerStackshot_block_invoke.97
+ __os_signpost_emit_with_name_impl
+ _access
+ _dispatch_assert_queue_not$V2
+ _exit
+ _fcntl
+ _ifSeedSetClassCProtectionOnMovedFile
+ _isCacheDeleteDisabled
+ _isForceCopyEnabled
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _os_signpost_enabled
+ _os_signpost_id_make_with_pointer
+ _proc_name
+ _rename
+ _xpc_connection_get_pid
- GCC_except_table208
- GCC_except_table223
- GCC_except_table272
- GCC_except_table339
- GCC_except_table340
- GCC_except_table385
- GCC_except_table396
- GCC_except_table397
- GCC_except_table401
- GCC_except_table402
- GCC_except_table462
- GCC_except_table527
- GCC_except_table70
- GCC_except_table73
- __ZL15gBootArgsParsed.0
- __ZN16CCProfileMonitor15profileCallbackEi
- __ZN16CCProfileMonitor29sendProfileChangeNotificationEi
- __ZN8CCDaemon29sendProfileChangeNotificationEi
- __ZN9CCLogFile9closeMMAPEv
- __ZNSt3__15dequeI14StackshotEntryNS_9allocatorIS1_EEED2B9nqe210106Ev
- __ZNSt3__19allocatorIP14StackshotEntryE17allocate_at_leastB9nqe210106Em
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZZ12isSeedAndiOSE10bootArgSet
- ___CCCacheDeleteEnablePurgeNotification_block_invoke.15
- ____ZN12CCXPCService21handleIncomingMessageEP17_xpc_connection_sPv_block_invoke
- ____ZN12CCXPCService21handleIncomingMessageEP17_xpc_connection_sPv_block_invoke.26
- ____ZN12CCXPCService21handleIncomingMessageEP17_xpc_connection_sPv_block_invoke_2
- ___block_descriptor_tmp.168
- ___block_descriptor_tmp.1878
- ___block_descriptor_tmp.2030
- ___block_descriptor_tmp.2303
- ___block_descriptor_tmp.2422
- ___block_descriptor_tmp.27
- ___block_descriptor_tmp.32
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.401
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.6
- ___block_descriptor_tmp.841
- ___block_literal_global.1154
- ___block_literal_global.13
- ___block_literal_global.1300
- ___block_literal_global.151
- ___block_literal_global.156
- ___block_literal_global.17
- ___block_literal_global.2244
- ___block_literal_global.29
- ___block_literal_global.63
- ___block_literal_global.8
- ___block_literal_global.81
- ___block_literal_global.842
- ___triggerStackshot_block_invoke.85
- _coreCaptureOsLog
- _fsync
- _getgBootArgsParsed
- _msync
- _setgBootArgsParsed
CStrings:
+ "%02x "
+ "%s:%d processEvent for entry:%u Owner:%s Name:%s"
+ "(CCLogTap) CFNumberGetValue failed for LogPolicy\n"
+ "(CCLogTap) IORegistryEntryCreateCFProperty failed for LogPolicy\n"
+ "... (%ld more bytes)"
+ "?"
+ "ALL"
+ "CCCacheDelete: failed to create dispatch queue\n"
+ "CCDaemon"
+ "CCDaemon purge notification enabled\n"
+ "CCDaemon: CacheDelete disabled via boot-arg\n"
+ "CCDaemon::%s Compressed '%s%s' -> %lld bytes"
+ "CCDaemon::%s Compression successful, deleting uncompressed file %s"
+ "CCDaemon::%s Failed to compress '%s%s'"
+ "CCDaemon::%s Failed to delete file %s errno: %d"
+ "CCDaemon::%s unable to stat compressed file '%s'"
+ "CCDaemon::freeResources: clearing working directory on shutdown"
+ "CCDaemon::init: clearing working directory on startup"
+ "CCDaemon::runShutdownThread Cannot xpc_transaction_try_exit_clean, still outstanding transactions (attempt %d/%d)"
+ "CCDaemon::runShutdownThread Failed to exit cleanly after %d attempts, forcing exit"
+ "CCDaemon_ActivityCheck"
+ "CCDaemon_DisablePowerNotification"
+ "CCDaemon_EnablePowerNotification"
+ "CCDaemon_PowerEvent"
+ "CCDaemon_QuiesceAll"
+ "CCDaemon_ResumeAll"
+ "CCDaemon_initWithOptions"
+ "CCDaemon_shutdown"
+ "CCDataFile::sendTelemetry failed"
+ "CCDataFile_closeFile"
+ "CCDataFile_openCaptureFile"
+ "CCDataFile_openFile"
+ "CCDataFile_sendTelemetry"
+ "CCDataPipeInterface_capture"
+ "CCDataPipeInterface_profileLoaded"
+ "CCDataPipeInterface_profileRemoved"
+ "CCDataPipeInterface_queryMetaData"
+ "CCDataPipeInterface_readData"
+ "CCDataTap: Unable to create CCFile. entry:%u Owner:%s Name:%s\n"
+ "CCDataTap::processEvent already quiesced entry:%u Owner:%s Name:%s\n"
+ "CCDataTap::processEvent quiesce pending entry:%u Owner:%s Name:%s\n"
+ "CCDataTap::processEvent() seed build and device hasn't been unlocked since boot - not processing event and waiting for the next. entry:%u Owner:%s Name:%s\n"
+ "CCDataTap::tapLoopImpl exit entry:%u Owner:%s Name:%s Exiting taploop\n"
+ "CCDataTap_initWithRegistryEntry"
+ "CCDataTap_withRegistryEntry"
+ "CCDatabase::addOwner: CFStringCreateCopy failed\n"
+ "CCDatabase::addOwner: ownerName is NULL\n"
+ "CCDatabase::addPipe: CFStringCreateCopy failed\n"
+ "CCDatabase::addPipe: failed to find/create owner\n"
+ "CCDatabase::addPipe: ownerName is NULL\n"
+ "CCDatabase::addPipe: pipeName is NULL\n"
+ "CCDatabase::addStream: CFStringCreateCopy failed\n"
+ "CCDatabase::addStream: owner not found\n"
+ "CCDatabase::addStream: ownerName is NULL\n"
+ "CCDatabase::addStream: pipe not found\n"
+ "CCDatabase::addStream: pipeName is NULL\n"
+ "CCDatabase::addStream: streamName is NULL\n"
+ "CCDatabase::findOwner: database is NULL\n"
+ "CCDatabase::findOwner: ownerName is NULL\n"
+ "CCDatabase::findPipe: owner is NULL\n"
+ "CCDatabase::findPipe: owner->pipes is NULL\n"
+ "CCDatabase::findPipe: pipeName is NULL\n"
+ "CCDatabase::findStream: pipe is NULL\n"
+ "CCDatabase::findStream: pipe->streams is NULL\n"
+ "CCDatabase::findStream: streamName is NULL\n"
+ "CCDatabase::getOwners: malloc failed for %zu bytes\n"
+ "CCDatabase::getOwners: no owners in database\n"
+ "CCDatabase::getPipeConfig: owner not found\n"
+ "CCDatabase::getPipeConfig: pipe not found\n"
+ "CCDatabase::getPipeEntry: owner not found\n"
+ "CCDatabase::getPipeProperty: entry->properties is NULL\n"
+ "CCDatabase::getPipeProperty: owner not found\n"
+ "CCDatabase::getPipeProperty: pipe not found\n"
+ "CCDatabase::getPipePropertyKeys: entry->properties is NULL\n"
+ "CCDatabase::getPipePropertyKeys: malloc failed for %zu bytes\n"
+ "CCDatabase::getPipePropertyKeys: no properties in pipe\n"
+ "CCDatabase::getPipePropertyKeys: owner not found\n"
+ "CCDatabase::getPipePropertyKeys: pipe not found\n"
+ "CCDatabase::getPipes: malloc failed for %zu bytes\n"
+ "CCDatabase::getPipes: no pipes in owner\n"
+ "CCDatabase::getPipes: owner not found\n"
+ "CCDatabase::getPipes: owner->pipes is NULL\n"
+ "CCDatabase::getStreamConfig: owner not found\n"
+ "CCDatabase::getStreamConfig: pipe not found\n"
+ "CCDatabase::getStreamConfig: stream not found\n"
+ "CCDatabase::getStreamEntry: owner not found\n"
+ "CCDatabase::getStreamEntry: pipe not found\n"
+ "CCDatabase::getStreamProperty: entry->properties is NULL\n"
+ "CCDatabase::getStreamProperty: owner not found\n"
+ "CCDatabase::getStreamProperty: pipe not found\n"
+ "CCDatabase::getStreamProperty: stream not found\n"
+ "CCDatabase::getStreamPropertyKeys: entry->properties is NULL\n"
+ "CCDatabase::getStreamPropertyKeys: malloc failed for %zu bytes\n"
+ "CCDatabase::getStreamPropertyKeys: no properties in stream\n"
+ "CCDatabase::getStreamPropertyKeys: owner not found\n"
+ "CCDatabase::getStreamPropertyKeys: pipe not found\n"
+ "CCDatabase::getStreamPropertyKeys: stream not found\n"
+ "CCDatabase::getStreams: malloc failed for %zu bytes\n"
+ "CCDatabase::getStreams: no streams in pipe\n"
+ "CCDatabase::getStreams: owner not found\n"
+ "CCDatabase::getStreams: pipe not found\n"
+ "CCDatabase::getStreams: pipe->streams is NULL\n"
+ "CCDatabase::hasOwner: ownerName is NULL\n"
+ "CCDatabase::hasPipe: owner not found\n"
+ "CCDatabase::hasPipe: ownerName is NULL\n"
+ "CCDatabase::hasPipe: pipeName is NULL\n"
+ "CCDatabase::hasStream: owner not found\n"
+ "CCDatabase::hasStream: ownerName is NULL\n"
+ "CCDatabase::hasStream: pipe not found\n"
+ "CCDatabase::hasStream: pipeName is NULL\n"
+ "CCDatabase::hasStream: streamName is NULL\n"
+ "CCDatabase::removeOwner: owner not found\n"
+ "CCDatabase::removeOwner: ownerName is NULL\n"
+ "CCDatabase::removePipe: owner not found\n"
+ "CCDatabase::removePipe: ownerName is NULL\n"
+ "CCDatabase::removePipe: pipe not found\n"
+ "CCDatabase::removePipe: pipeName is NULL\n"
+ "CCDatabase::removePipeProperty: owner not found\n"
+ "CCDatabase::removePipeProperty: pipe not found\n"
+ "CCDatabase::removePipeProperty: property key not found\n"
+ "CCDatabase::removeStream: owner not found\n"
+ "CCDatabase::removeStream: ownerName is NULL\n"
+ "CCDatabase::removeStream: pipe not found\n"
+ "CCDatabase::removeStream: pipeName is NULL\n"
+ "CCDatabase::removeStream: stream not found\n"
+ "CCDatabase::removeStream: streamName is NULL\n"
+ "CCDatabase::removeStreamProperty: owner not found\n"
+ "CCDatabase::removeStreamProperty: pipe not found\n"
+ "CCDatabase::removeStreamProperty: property key not found\n"
+ "CCDatabase::removeStreamProperty: stream not found\n"
+ "CCDatabase::reset: malloc failed for %zu bytes\n"
+ "CCDatabase::setPipeProperty: key is NULL\n"
+ "CCDatabase::setPipeProperty: owner not found\n"
+ "CCDatabase::setPipeProperty: pipe not found\n"
+ "CCDatabase::setStreamProperty: key is NULL\n"
+ "CCDatabase::setStreamProperty: owner not found\n"
+ "CCDatabase::setStreamProperty: pipe not found\n"
+ "CCDatabase::setStreamProperty: stream not found\n"
+ "CCDatabase::~CCDatabase: malloc failed for %zu bytes\n"
+ "CCFile::captureLog Failed to create directory %s (reason: %s)\n"
+ "CCFile::captureLogRun Current File %s (reason: %s) Owner:%s Pipe:%s\n"
+ "CCFile::captureLogRun Failed to stat file %s%s, errno: %d Owner:%s Pipe:%s\n"
+ "CCFile::captureLogRun Skipping current file Dir file %s, Current File %s Owner:%s Pipe:%s\n"
+ "CCFile::captureLogRun copying files took %f seconds (reason: %s) Owner:%s Pipe:%s\n"
+ "CCFile::captureLogRun moving files took %f seconds (reason: %s) Owner:%s Pipe:%s\n"
+ "CCFile::captureLogRun() Exiting CCFile::captureLogRun (reason: %s) Owner:%s Pipe:%s\n"
+ "CCFile::copyFile Unable to stat dest path '%s' errno: %d reason: %s prevErr: %s\n"
+ "CCFile::copyFile Wrote '%s' source length: %lld archive length: %lld (reason: %s) Owner:%s Pipe:%s\n"
+ "CCFile::copyFile failed: %s file: '%s' Owner:%s Pipe:%s\n"
+ "CCFile::copyFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n"
+ "CCFile::copyFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n"
+ "CCFile::copyFile gzwrite error: %s\n"
+ "CCFile::moveFile Failed to delete source file after copy: '%s', errno: %d\n"
+ "CCFile::moveFile Moved '%s' -> '%s' (reason: %s) Owner:%s Pipe:%s\n"
+ "CCFile::moveFile failed: %s file: '%s' Owner:%s Pipe:%s\n"
+ "CCFile::moveFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n"
+ "CCFile::moveFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n"
+ "CCFile::populateCommonTelemetryDictionary - Failed to get config from database for owner/pipe\n"
+ "CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe missing owner or name\n"
+ "CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe, getting config from database\n"
+ "CCFile::writeDataFiles memory allocation failed (reason: %s)\n"
+ "CCFile_captureLog"
+ "CCFile_captureLogRun"
+ "CCFile_copyFile"
+ "CCFile_initWithRegistryEntry"
+ "CCFile_moveFile"
+ "CCFile_writeDataFiles"
+ "CCIOReportDumpQueue"
+ "CCIOReportDumpQueue::_processorThread bail - !keysTypeRef\n"
+ "CCIOReportDumpQueue_DoSaveChannels"
+ "CCIOReportDumpQueue_ProcessorThread"
+ "CCIOReportDumpQueue_SaveChannels"
+ "CCLogDisable"
+ "CCLogEnable"
+ "CCLogFile::deleteFile failed to delete: %s, errno: %d\n"
+ "CCLogFile::deleteFile file already deleted: %s\n"
+ "CCLogFile::deleteFile successfully deleted: %s\n"
+ "CCLogFile::initWithConfig\n"
+ "CCLogFile::initWithConfig: CFNumberCreate failed for logDataType\n"
+ "CCLogFile::initWithConfig: CFNumberCreate failed for pipeType\n"
+ "CCLogFile::initWithConfig: Failed to create directory/file name strings\n"
+ "CCLogFile::initWithConfig: Failed to create formatter\n"
+ "CCLogFile::initWithConfig: Failed to create log directory\n"
+ "CCLogFile::initWithConfig: Failed to create log directory path\n"
+ "CCLogFile::initWithConfig: Failed to create working directory string\n"
+ "CCLogFile::initWithConfig: Failed to initialize PCAP formatter\n"
+ "CCLogFile::initWithConfig: Invalid arguments\n"
+ "CCLogFile::initWithConfig: Number of files cannot be 0\n"
+ "CCLogFile::initWithConfig: Successfully initialized for non-IORegistry pipe\n"
+ "CCLogFile::initWithConfig: Unsupported log data type %d\n"
+ "CCLogFile::initWithConfig: buildFileTables failed\n"
+ "CCLogFile::initWithConfig: pthread_mutex_init failed\n"
+ "CCLogFile::initWithConfig: pthread_mutexattr_init failed\n"
+ "CCLogFile::initWithConfig: pthread_mutexattr_settype failed\n"
+ "CCLogFile::sendTelemetry failed"
+ "CCLogFile::withConfig()\n"
+ "CCLogFile::withConfig() Invalid log type %d\n"
+ "CCLogFile::withConfig() Invalid parameters\n"
+ "CCLogFile::writeLog - File roll needed\n"
+ "CCLogFile_addFile"
+ "CCLogFile_buildFileTables"
+ "CCLogFile_closeFile"
+ "CCLogFile_closeMMAP"
+ "CCLogFile_openFile"
+ "CCLogFile_sendTelemetry"
+ "CCLogPipeInterface_capture"
+ "CCLogPipeInterface_dumpToDiskComplete"
+ "CCLogPipeInterface_mapPipe"
+ "CCLogPipeInterface_profileLoaded"
+ "CCLogPipeInterface_profileRemoved"
+ "CCLogPipeInterface_setConsoleLogFlags"
+ "CCLogPipeInterface_setConsoleLogLevel"
+ "CCLogPipeInterface_setLogFlags"
+ "CCLogPipeInterface_setLogLevel"
+ "CCLogPipeInterface_setNotifyTimeout"
+ "CCLogPipeInterface_setPolicy"
+ "CCLogPipeInterface_setWatermarkLevel"
+ "CCLogPipeInterface_unmapPipe"
+ "CCLogPipeInterface_updateConsoleLogFlags"
+ "CCLogPipeInterface_updateLogFlags"
+ "CCLogTap::freeResources() entry:%u failed to unmap pipe with rc[0x%08x]\n"
+ "CCLogTap::isActive idle < duration, Owner:%s Name:%s entry:%u duration:%f\n"
+ "CCLogTap::isActive policy is %d, Owner:%s Name:%s entry:%u\n"
+ "CCLogTap::isActive tap is busy, Owner:%s Name:%s entry:%u\n"
+ "CCLogTap::pipeEvent EXIT Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d),prevread offset %u, new read offset %u, prev seq %u, expected seq %u entry %u, ring state readoff %u, write offset %u, Owner:%s Name:%s\n"
+ "CCLogTap_initWithRegistryEntry"
+ "CCLogTap_withRegistryEntry"
+ "CCOwnerEntry copy constructor: malloc failed for %zu bytes\n"
+ "CCOwnerEntry operator=: malloc failed for %zu bytes\n"
+ "CCOwnerEntry operator=: malloc failed for cleanup, %zu bytes\n"
+ "CCOwnerEntry::~CCOwnerEntry: malloc failed for %zu bytes\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable Failed to convert stream name\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get CCFile object\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get stream entry for stream %ld\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Found %ld streams in database\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Found stream header (%ld bytes) for stream\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Missing owner or pipe name\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe initialized with %u total interfaces\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe, querying database\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Stream header bytes: %s\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: Stream[%u]: name=%s, id=%u, dlt=%u\n"
+ "CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.\n"
+ "CCPcapngFormatter::searchStreamIdInRegistry: Found %ld streams in database\n"
+ "CCPcapngFormatter::searchStreamIdInRegistry: Found matching stream in database\n"
+ "CCPcapngFormatter::searchStreamIdInRegistry: Non-IORegistry pipe, querying CCDatabase for streamId=%u\n"
+ "CCPcapngFormatter::searchStreamIdInRegistry: Stream not found in database\n"
+ "CCPcapngFormatter::writeFileHeader: Empty pipeOwner or pipeName string\n"
+ "CCPcapngFormatter::writeFileHeader: Failed to cast fWriteObject to CCFile\n"
+ "CCPcapngFormatter::writeFileHeader: Missing pipeOwner or pipeName\n"
+ "CCPcapngFormatter::writeFileHeader: Non-IORegistry pipe - owner=%s, name=%s\n"
+ "CCPipeEntry copy constructor: malloc failed for %zu bytes\n"
+ "CCPipeEntry operator=: malloc failed for %zu bytes\n"
+ "CCPipeEntry operator=: malloc failed for cleanup, %zu bytes\n"
+ "CCPipeEntry::~CCPipeEntry: malloc failed for %zu bytes\n"
+ "CCPipeInterface_setNotificationPort"
+ "CCPipeInterface_wakeupTapLoop"
+ "CCPipeMonitor"
+ "CCPipeMonitor::isActive: recent serviceTerminated, staying active\n"
+ "CCPipeMonitor_CleanCaptureDirectories"
+ "CCPipeMonitor_ProfileLoaded"
+ "CCPipeMonitor_ProfileRemoved"
+ "CCPipeMonitor_QuiesceAllTaps"
+ "CCPipeMonitor_ResumeAllTaps"
+ "CCPipeMonitor_ServicePublished"
+ "CCPipeMonitor_ServiceTerminated"
+ "CCProfileMonitor"
+ "CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback to check for installed profiles\n"
+ "CCProfileMonitor::cancelObservers removing event stream handler and Darwin observer\n"
+ "CCProfileMonitor::profileCallback Entered source:%d token:%d\n"
+ "CCProfileMonitor::profileCallback Loaded\n"
+ "CCProfileMonitor::profileCallback during shutdown at %d\n"
+ "CCProfileMonitor::profileCallback starting states -> source %d fProfileToken %d isShutdownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::setStreamEventHandler calling profileCallback(CCProfileChangeSourceXPCStream)\n"
+ "CCProfileMonitor_ApplyConfiguration"
+ "CCProfileMonitor_ApplyProfile"
+ "CCProfileMonitor_MergeProfilePlist"
+ "CCProfileMonitor_ProfileCallback"
+ "CCProfileMonitor_ProfileRemoved"
+ "CCTap_cleanCaptureDirectories"
+ "CCTap_freeResources"
+ "CCTap_initWithRegistryEntry"
+ "CCXPCService"
+ "CCXPCService: logging command received but not supported on this platform\n"
+ "CCXPCService::cancelActiveConnections cancelling %lu connections\n"
+ "CCXPCService::handleIncomingMessage shutdown pending true, dropping message and exiting\n"
+ "CCXPCService::handleIncomingMessage: incoming, incomingConnection from '%s' with pid '%d', XPC_TYPE_CONNECTION, %d, XPC_TYPE_ERROR, %d, XPC_TYPE_DICTIONARY, %d\n"
+ "CCXPCService_FreeResources"
+ "CCXPCService_HandleConnectionEvent"
+ "CCXPCService_HandleIncomingMessage"
+ "CCXPCService_InitWithConfigureAndPipeMonitor"
+ "CCXPCService_StartXPCService"
+ "CoreCaptureStart: ENTRY - workingDir=%p, saveDir=%p, isCCDaemon=%d, isInitialized=%d\n"
+ "CoreCapture_Start"
+ "CoreCapture_Stop"
+ "NULL"
+ "Received Capture Event entry:%u Owner:%s Name:%s\n"
+ "Session Name: %s, Blob Name: %s %llu.%llu Owner:%s Name:%s\n"
+ "Unable to initialize logging subsystem for corecapture"
+ "applied"
+ "buffer_alloc_fail"
+ "cc.cachedelete.disable"
+ "cc.file.forcecopy"
+ "cleanCaptureDirectory: count %lld exceeds max %lld, deleting %lld oldest"
+ "com.apple.corecaptured.cachedelete"
+ "config_alloc_fail"
+ "configure=%p pipeMonitor=%p"
+ "connection=%p type=%s"
+ "create_protected_file_failed"
+ "default"
+ "deleteDirectory: deleting '%s' reason: %s"
+ "dest_buffer_alloc_failed"
+ "dest_open_failed"
+ "dest_stat_failed"
+ "dest_write_failed"
+ "empty_configuration"
+ "event_type=%s"
+ "failed"
+ "false"
+ "fileCount=%ld"
+ "fileCount=%ld timeTaken=%f"
+ "filePath=%s"
+ "filesSaved=%ld"
+ "getInstance result=%s"
+ "gzopen_failed"
+ "gzwrite_failed"
+ "invalid_plist"
+ "invalid_plist_format"
+ "invalid_plist_type"
+ "invalid_reference"
+ "message=0x%x"
+ "mutex_lock_failed"
+ "newInstance result=%s"
+ "no_config_string"
+ "no_keys"
+ "no_profiles_installed"
+ "no_remote_connection"
+ "none"
+ "owner=%s pipe=%s"
+ "owner=%s pipe=%s dirName=%s"
+ "owner=%s pipe=%s entry=%u"
+ "owner=%s pipe=%s fileName=%s"
+ "owner=%s pipe=%s fileName=%s captureId=%u.%06u reason=%s logSize=%zu"
+ "owner=%s pipe=%s fileName=%s doCompress=%d"
+ "owner=%s pipe=%s fileName=%s fileSize=%ld"
+ "owner=%s pipe=%s fileName=%s fileSize=%ld logEvents=%u"
+ "owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=async"
+ "owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=fileWillClose"
+ "owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=rollover"
+ "owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=shutdown"
+ "owner=%s pipe=%s fileName=%s reason=%s"
+ "owner=%s pipe=%s keyCount=%ld"
+ "owner=%s pipe=%s level=%u"
+ "owner=%s pipe=%s nextFileIndex=%u logType=%d fileSize=%u"
+ "owner=%s pipe=%s policy=%u"
+ "owner=%s pipe=%s profileLoaded=%d"
+ "owner=%s pipe=%s reason=%s"
+ "owner=%s pipe=%s reason=prepareQuiescing"
+ "owner=%s pipe=%s reason=resumeFromQuiesced"
+ "owner=%s pipe=%s registryEntry=%u"
+ "owner=%s pipe=%s streamName=%s"
+ "owner=%s pipe=%s streamName=%s flagName=%s"
+ "owner=%s pipe=%s timeout=%u"
+ "owners_extraction_failed"
+ "plist1=%s plist2=%s"
+ "present"
+ "previousProfileLoaded=%d"
+ "profile_loaded_notification"
+ "profile_removed_notification"
+ "pruneDirectoryNDaysDo: older than %ld days (age=%.0fs)"
+ "pruneDirectoryOnOSUpgrade: upgraded from %s to %s"
+ "rename_failed"
+ "result=%s"
+ "result=%s fileD=%d"
+ "result=%s logDataType=%d"
+ "result=%s sourceSize=%lld destSize=%lld"
+ "result=0x%x"
+ "result=0x%x bytesRead=%llu"
+ "result=0x%x ringSize=%llu"
+ "result=active"
+ "result=already_running"
+ "result=already_set"
+ "result=already_shutdown"
+ "result=both_null"
+ "result=cannot_acquire_lock"
+ "result=complete"
+ "result=connection_established"
+ "result=duplicate"
+ "result=exception exception=%s"
+ "result=failed"
+ "result=failed reason=IORegisterForSystemPower_failed"
+ "result=failed reason=already_called"
+ "result=failed reason=bad_args"
+ "result=failed reason=device_locked"
+ "result=failed reason=dict_alloc_failed"
+ "result=failed reason=directory_creation_failed"
+ "result=failed reason=filePath_failed"
+ "result=failed reason=file_creation_failed"
+ "result=failed reason=formatter_creation_failed"
+ "result=failed reason=invalid_args"
+ "result=failed reason=keys_alloc_failed"
+ "result=failed reason=log_dir_path_invalid"
+ "result=failed reason=log_directory_creation_failed"
+ "result=failed reason=malloc_failed"
+ "result=failed reason=memory_allocation_failed"
+ "result=failed reason=mkdir_failed"
+ "result=failed reason=mutex_init_failed error=%d"
+ "result=failed reason=mutex_lock_failed"
+ "result=failed reason=no_keys"
+ "result=failed reason=no_profile_loaded"
+ "result=failed reason=not_entitled"
+ "result=failed reason=null_allChannels"
+ "result=failed reason=null_saveDir"
+ "result=failed reason=profile_removed"
+ "result=failed reason=property_creation_failed"
+ "result=failed reason=property_value_failed"
+ "result=failed reason=tap_creation_failed"
+ "result=failed reason=values_alloc_failed"
+ "result=failed reason=working_directory_creation_failed"
+ "result=failed reason=xpc_service_creation_failed"
+ "result=malloc_failed"
+ "result=mutex_failed"
+ "result=no_taps"
+ "result=not_dictionary_types"
+ "result=not_enabled"
+ "result=not_initialized"
+ "result=profile_active"
+ "result=retain_plist1"
+ "result=retain_plist2"
+ "result=shutdown_pending"
+ "result=shutdown_triggered"
+ "result=success"
+ "result=success configurationsApplied=%ld"
+ "result=success finalProfileLoaded=%d keyCount=%ld"
+ "result=success mergedKeys=%ld"
+ "result=success numberOfFiles=%u maxFiles=%u"
+ "result=success profile=%s"
+ "result=success profile=skipped"
+ "result=success state=%d"
+ "result=success tap=released"
+ "result=success tapCount=%ld"
+ "result=success tapCount=%zu"
+ "result=tap_not_found"
+ "result=timeout tapCount=%ld notQuiescedTap=%ld"
+ "result=unexpected_event_type type=%s"
+ "result=xpc_active"
+ "result=xpc_error"
+ "result=xpc_error error=%s"
+ "set_protection_class_failed"
+ "shutdown_pending"
+ "source=%d previousState=%d fProfileToken=%d"
+ "source_buffer_alloc_failed"
+ "source_open_failed"
+ "source_read_failed"
+ "success"
+ "success=%s"
+ "true"
+ "unchanged"
+ "vector"
+ "workingDir=%s saveDir=%s isDaemon=%s"
- "%s:%d processEvent for entry:%u"
- "CCDaemon::%s:%d Compressed file with name %s and resulting length %lld bytes\n"
- "CCDaemon::%s:%d Deleting compressed file %s"
- "CCDaemon::%s:%d unable to stat dest path\n"
- "CCDaemon::runShutdownThread Cannot xpc_transaction_try_exit_clean, still outstanding transactions, will call xpc_transaction_try_exit_clean again later"
- "CCDataFile::sendTelemetry returned %d"
- "CCDataTap: Unable to create CCFile.\n"
- "CCDataTap::processEvent() seed build and device hasn't been unlocked since boot - not processing event and waiting for the next.\n"
- "CCDataTap::tapLoopImpl exit :%u Exiting taploop\n"
- "CCFile::captureLog Failed to create directory %s\n"
- "CCFile::captureLogRun Current File %s\n"
- "CCFile::captureLogRun Failed to stat file %s%s, errno: %d\n"
- "CCFile::captureLogRun Skipping current file Dir file %s, Current File %s\n"
- "CCFile::captureLogRun copying files took %f seconds\n"
- "CCFile::captureLogRun() Exiting CCFile::captureLogRun \n"
- "CCFile::copyFile  Error writing to destination buffer %s: %s\n"
- "CCFile::copyFile Attempt to write fileName %s, source path:%s, dest path:%s, length: %lld\n"
- "CCFile::copyFile Error reading from source buffer %s\n"
- "CCFile::copyFile Error writing to destination buffer: %s \n"
- "CCFile::copyFile Failed to open source file:%s errno %d, reason %s\n"
- "CCFile::copyFile Unable to stat dest path errno = %d, reason %s\n"
- "CCFile::copyFile Wrote fileName %s with source length: %lld archive length: %lld\n"
- "CCFile::copyFile unable to allocate destination buffer"
- "CCFile::copyFile unable to allocate source buffer"
- "CCFile::writeDataFiles memory allocation failed\n"
- "CCLogFile::cleanupCapturedFiles() deleting file[%u]: %s\n"
- "CCLogFile::deleteFile name: %s\n"
- "CCLogFile::sendTelemetry returned %d"
- "CCLogTap::isActive idle < duration  3 entry:%u duration:%f\n"
- "CCLogTap::isActive policy is %d entry:%u\n"
- "CCLogTap::isActive tap is fBusy Active 2 entry:%u\n"
- "CCLogTap::pipeEvent EXIT Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d),prevread offset %u, new read offset %u, prev seq %u, expected seq %u entry %u, ring state readoff %u, write offset %u\n"
- "CCPcapngFormatter::buildStreamToInterfaceTable MISSING STREAM NAME\n"
- "CCPipeMonitor::CCPipeMonitor Failed to create OS LOG.\n"
- "CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback(1) to check for installed profiles\n"
- "CCProfileMonitor::profileCallback Entered token:%d\n"
- "CCProfileMonitor::profileCallback Loaded \n"
- "CCProfileMonitor::profileCallback during shutdown (1)\n"
- "CCProfileMonitor::profileCallback during shutdown (2)\n"
- "CCProfileMonitor::profileCallback starting states -> isShutdownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
- "CCProfileMonitor::setStreamEventHandler CCDaemon::getInstance().isShutdownPending() == true, dropping event and exiting\n"
- "CCProfileMonitor::setStreamEventHandler Woken up by notifyd.\n"
- "CCProfileMonitor::setStreamEventHandler calling profileCallback(1)\n"
- "CCXPCService::handleIncomingMessage CCDaemon::getInstance().isShutdownPending() true, dropping message and exiting\n"
- "CCXPCService::handleIncomingMessage: incoming, incomingConnection, XPC_TYPE_CONNECTION, %d, XPC_TYPE_ERROR, %d, XPC_TYPE_DICTIONARY, %d\n"
- "Received Capture Event %u\n"
- "Session Name: %s, Blob Name: %s %llu.%llu\n"
- "UTF8String"
- "containsString:"
- "countByEnumeratingWithState:objects:count:"
- "dataWithBytes:length:"
- "dataWithJSONObject:options:error:"
- "descriptionWithCalendarFormat:"
- "fopen failed errno = %d, reason : %s\n"
- "gzopen failed errno = %d, reason : %s\n"
- "initWithUTF8String:"
- "installedProfileIdentifiers"
- "length"
- "numberOfDirArrayEntries: %lld, readIndex %lld\n"
- "objectForKeyedSubscript:"
- "pruneDirectoryNDaysDo %s\n"
- "pruneDirectoryOnOSUpgrade %s\n"
- "pruneDirectoryOnOSUpgrade: activity enabled; upgraded from %s to %s\n"
- "sharedConnection"
- "stringWithFormat:"
- "unsignedLongLongValue"
- "writeData:"

```
