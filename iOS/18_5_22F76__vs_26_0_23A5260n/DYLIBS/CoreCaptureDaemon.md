## CoreCaptureDaemon

> `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

```diff

-1255.32.0.0.0
-  __TEXT.__text: 0x39a6c
-  __TEXT.__auth_stubs: 0xf60
+1301.62.0.0.0
+  __TEXT.__text: 0x40284
+  __TEXT.__auth_stubs: 0x1110
   __TEXT.__const: 0x4f0
-  __TEXT.__gcc_except_tab: 0xcc
-  __TEXT.__oslogstring: 0x6377
-  __TEXT.__cstring: 0x7638
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__gcc_except_tab: 0x1d4
+  __TEXT.__oslogstring: 0x729e
+  __TEXT.__cstring: 0x86a5
+  __TEXT.__unwind_info: 0x618
   __TEXT.__objc_classname: 0x1
-  __TEXT.__objc_methname: 0x9f
-  __TEXT.__objc_stubs: 0x100
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x210
+  __TEXT.__objc_methname: 0x107
+  __TEXT.__objc_stubs: 0x180
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH_CONST.__const: 0xff8
-  __AUTH_CONST.__cfstring: 0x960
+  __DATA_CONST.__objc_selrefs: 0x60
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__const: 0x1088
+  __AUTH_CONST.__cfstring: 0xa00
   __DATA.__data: 0x1
-  __DATA.__common: 0x4c
-  __DATA.__bss: 0x11b
+  __DATA.__common: 0x3c
+  __DATA.__bss: 0x132
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC
   - /usr/lib/libIOReport.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1A5DBB47-DB36-3C8B-AFAF-3845C227A22A
-  Functions: 470
-  Symbols:   976
-  CStrings:  1173
+  UUID: A461C3A7-1E3D-348C-B8A9-3F4147CABBD8
+  Functions: 499
+  Symbols:   1063
+  CStrings:  1334
 
Symbols:
+ GCC_except_table11
+ GCC_except_table146
+ GCC_except_table202
+ GCC_except_table217
+ GCC_except_table355
+ GCC_except_table430
+ GCC_except_table494
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table69
+ _CFStringGetMaximumSizeForEncoding
+ _MGCopyAnswer
+ _OBJC_CLASS_$_MCProfileConnection
+ __Block_object_dispose
+ __ZL13osTransaction
+ __ZL15gBootArgsParsed.0
+ __ZN10CCDataFile13sendTelemetryEv
+ __ZN10CCDataFile24resetTelemetryParametersEv
+ __ZN13CCPipeMonitor22withDictionaryAndQueueEP14__CFDictionaryP16dispatch_queue_s
+ __ZN13CCPipeMonitor26initWithDictionaryAndQueueEP14__CFDictionaryP16dispatch_queue_s
+ __ZN15CCPipeInterface26getBackgroundDispatchQueueEv
+ __ZN16CCServiceMonitor26initWithDictionaryAndQueueEP14__CFDictionaryP16dispatch_queue_s
+ __ZN19CCIOReportDumpQueue19cancelableBlockFuncEv
+ __ZN19CCIOReportDumpQueue21initInstanceWithQueueEP16dispatch_queue_s
+ __ZN19CCIOReportDumpQueue23createInstanceWithQueueEP16dispatch_queue_s
+ __ZN5CCTap11setQuiescedEv
+ __ZN5CCTap19isDumpToDiskAllowedEv
+ __ZN6CCFile18setFileCloseReasonE21CCLogFileCloseReasons
+ __ZN6CCFile33populateCommonTelemetryDictionaryEPv
+ __ZN6CCFile8copyFileEPKcb
+ __ZN8CCDaemon11getInstanceEv
+ __ZN8CCDaemon11initializedE
+ __ZN8CCDaemon16startPipeMonitorEv
+ __ZN8CCDaemon29fEnableDumpToDiskinRecoveryOSE
+ __ZN8CCDaemon8instanceE
+ __ZN8CCDaemon9onceTokenE
+ __ZN9CCLogFile13sendTelemetryEv
+ __ZN9CCLogFile24resetTelemetryParametersEv
+ __ZNSt13runtime_errorC1EPKc
+ __ZNSt13runtime_errorD1Ev
+ __ZSt9terminatev
+ __ZTISt13runtime_error
+ __ZTISt9exception
+ __ZZ16isCarrierReleaseE17gIsCarrierRelease
+ __ZZ16isCarrierReleaseE9onceToken
+ __ZZ23deviceUnlockedSinceBootE18deviceUnlockedOnce
+ __ZZ24shouldReduceLogRetentionE15reduceRetention
+ __ZZ24shouldReduceLogRetentionE16parseChipsetInfo
+ ____ZN10CCDataFile13sendTelemetryEv_block_invoke
+ ____ZN19CCIOReportDumpQueue19cancelableBlockFuncEv_block_invoke
+ ____ZN6CCFile13captureLogRunEv_block_invoke
+ ____ZN8CCDaemon11getInstanceEv_block_invoke
+ ____ZN8CCDaemon13freeResourcesEv_block_invoke
+ ____ZN9CCLogFile13sendTelemetryEv_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_tmp.1541
+ ___block_descriptor_tmp.160
+ ___block_descriptor_tmp.1754
+ ___block_descriptor_tmp.1846
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.2102
+ ___block_descriptor_tmp.2221
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.37
+ ___block_descriptor_tmp.391
+ ___block_descriptor_tmp.53
+ ___block_descriptor_tmp.605
+ ___block_descriptor_tmp.62
+ ___block_descriptor_tmp.816
+ ___block_literal_global.1250
+ ___block_literal_global.1752
+ ___block_literal_global.2060
+ ___block_literal_global.25
+ ___block_literal_global.810
+ ___clang_call_terminate
+ ___cxa_allocate_exception
+ ___cxa_begin_catch
+ ___cxa_end_catch
+ ___cxa_free_exception
+ ___cxa_rethrow
+ ___cxa_throw
+ ___isCarrierRelease_block_invoke
+ _addSystemInformationToDict
+ _analytics_send_event_lazy
+ _cleanCaptureDirectory
+ _cleanupLogFile
+ _compressFile
+ _copyCFStringRefToXPCDictionary
+ _deleteDirectory
+ _deviceUnlockedSinceBoot
+ _dispatch_block_cancel
+ _dispatch_block_create
+ _dispatch_block_testcancel
+ _dispatch_once
+ _dispatch_queue_attr_make_with_qos_class
+ _feof
+ _ferror
+ _getMaxPreservedCaptures
+ _getPossibleSaveLocation
+ _getSaveLocation
+ _getgBootArgsParsed
+ _ifSeedCreateClassCProtectedFile
+ _ifSeedCreateClassCProtectedFileAtCFStringPath
+ _isBTLoggingProfileInstalled
+ _isCarrierRelease
+ _isClientBT
+ _isClientMultiFunctionManager
+ _isClientValid
+ _isClientWiFi
+ _isMegaWiFiProfileInstalled
+ _isSeedAndiOS
+ _lowPriorityActivities
+ _mkdirRecursive
+ _objc_enumerationMutation
+ _objc_msgSend$containsString:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$installedProfileIdentifiers
+ _objc_msgSend$sharedConnection
+ _objc_opt_class
+ _os_release
+ _os_transaction_create
+ _os_variant_is_recovery
+ _pruneDirectoryOnOSUpgrade
+ _setgBootArgsParsed
+ _shouldReduceLogRetention
+ _sleep
+ _sortByDirectoryName
+ _strncmp
+ _strstr
+ _strtok
+ _validCFObjectReference
+ _writeMetadataFiles
+ _xpc_dictionary_create
+ _xpc_dictionary_set_uint64
+ _xpc_transaction_try_exit_clean
- GCC_except_table191
- GCC_except_table205
- GCC_except_table331
- GCC_except_table403
- GCC_except_table465
- GCC_except_table55
- GCC_except_table56
- GCC_except_table59
- _CFMakeCollectable
- __Z12isSeedAndiOSv
- __Z14mkdirRecursivePK10__CFString
- __Z15deleteDirectoryP10__CFString
- __Z15getSaveLocationv
- __Z18writeMetadataFilesPK10__CFStringPKc11CCTimestamp
- __Z19sortByDirectoryNamexPP10__CFString
- __Z21cleanCaptureDirectoryPK10__CFString
- __Z21lowPriorityActivitiesv
- __Z22validCFObjectReferencePKcPKvm
- __Z23deviceUnlockedSinceBootv
- __Z23getMaxPreservedCapturesv
- __Z23getPossibleSaveLocationv
- __Z25pruneDirectoryOnOSUpgradev
- __Z26addSystemInformationToDictP14__CFDictionaryy
- __Z31ifSeedCreateClassCProtectedFilePc
- __Z45ifSeedCreateClassCProtectedFileAtCFStringPathPK10__CFString
- __ZL15gBootArgsParsed
- __ZN13CCPipeMonitor14withDictionaryEP14__CFDictionary
- __ZN13CCPipeMonitor18initWithDictionaryEP14__CFDictionary
- __ZN16CCServiceMonitor18initWithDictionaryEP14__CFDictionary
- __ZN19CCIOReportDumpQueue12initInstanceEv
- __ZN19CCIOReportDumpQueue14createInstanceEv
- __ZN6CCFile8copyFileEPKc
- __ZN8CCObjectdlEPvm
- __ZN8CCObjectnwEm
- __ZN9CCLogFile6lockedEv
- __ZZ12isSeedAndiOSvE10bootArgSet
- __ZZ23deviceUnlockedSinceBootvE18deviceUnlockedOnce
- ____ZN19CCIOReportDumpQueue16_processorThreadEv_block_invoke
- ___block_descriptor_tmp
- ___block_descriptor_tmp.1327
- ___block_descriptor_tmp.1531
- ___block_descriptor_tmp.1634
- ___block_descriptor_tmp.18
- ___block_descriptor_tmp.1864
- ___block_descriptor_tmp.22
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.510
- ___block_descriptor_tmp.707
- ___block_literal_global.1529
- ___block_literal_global.1825
- __gQueuePrivate
- __gQueuePrivateServNotify
- _daemonGlbl
- _exit
- _pthread_mutex_trylock
- _shutDownPending
- _startCalled
CStrings:
+ " "
+ "%s Duplicate Owner:%s Name:%s entry:%u\n"
+ "%s%s"
+ "%s@%d: fCancelableBlock bailing out\n"
+ "%s@%d: fExitNextIteration bailing out\n"
+ "CCDaemon received power notification (0x%x) \n"
+ "CCDaemon received system wake or will not sleep (0x%x), all cctap resumed from quiesced state\n"
+ "CCDaemon will calling shutdown()\n"
+ "CCDaemon:: Num of matching CCPipe %ld\n"
+ "CCDaemon::%s CCDaemon::getInstance().isShutdownPending() == true, skipping activityCheck()"
+ "CCDaemon::%s:%d Compressed file with name %s and resulting length %lld bytes\n"
+ "CCDaemon::%s:%d Deleting compressed file %s"
+ "CCDaemon::%s:%d Error reading from source buffer %s\n"
+ "CCDaemon::%s:%d Error writing to destination buffer %s: %s\n"
+ "CCDaemon::%s:%d Trying to compress file %s%s\n"
+ "CCDaemon::%s:%d dirPath is invalid"
+ "CCDaemon::%s:%d dirPath is invalid\n"
+ "CCDaemon::%s:%d failed to open dest buffer %s\n"
+ "CCDaemon::%s:%d failed to open source buffer %s\n"
+ "CCDaemon::%s:%d fileName %s is already compressed...\n"
+ "CCDaemon::%s:%d fileName is invalid"
+ "CCDaemon::%s:%d fileName is invalid\n"
+ "CCDaemon::%s:%d filePath may get truncated. Returning..."
+ "CCDaemon::%s:%d unable to allocate destination buffer\n"
+ "CCDaemon::%s:%d unable to allocate source buffer\n"
+ "CCDaemon::%s:%d unable to create class with protection flag\n"
+ "CCDaemon::%s:%d unable to create filePathRef\n"
+ "CCDaemon::%s:%d unable to stat dest path\n"
+ "CCDaemon::ccstart to create CCDaemon"
+ "CCDaemon::getInstance failed with exception: %s"
+ "CCDaemon::getInstance isInitialized false"
+ "CCDaemon::init failed to create com.apple.corecaptured.background_queue\n"
+ "CCDaemon::runShutdownThread Cannot xpc_transaction_try_exit_clean, still outstanding transactions, will call xpc_transaction_try_exit_clean again later"
+ "CCDaemon::runShutdownThread Exiting via xpc_transaction_try_exit_clean"
+ "CCDaemon::setupDirectInstance failed with exception: %s"
+ "CCDaemon::setupDirectInstance success"
+ "CCDaemon::startPipeMonitor CCDaemon not yet initialized, exiting"
+ "CCDataFile::sendTelemetry analytics_send_event_lazy weak link import failed"
+ "CCDataFile::sendTelemetry returned %d"
+ "CCFile::copyFile  Error writing to destination buffer %s: %s\n"
+ "CCFile::copyFile Error reading from source buffer %s\n"
+ "CCFile::copyFile Error writing to destination buffer: %s \n"
+ "CCFile::copyFile unable to allocate destination buffer"
+ "CCFile::copyFile unable to allocate source buffer"
+ "CCFile::copyFile: Unable to stat source path errno %d, reason %s\n"
+ "CCFile::mkdirRecursive Unable to create path '%s' as '%s' is not a directory errno %d\n"
+ "CCFile::mkdirRecursive Unable to mkdir on '%s', errno %d\n"
+ "CCLogFile::deleteFile name: %s\n"
+ "CCLogFile::sendTelemetry analytics_send_event_lazy weak link import failed"
+ "CCLogFile::sendTelemetry returned %d"
+ "CCPipeMonitor::%s:%d Release Tap i %zu"
+ "CCPipeMonitor::%s:%d Tap corresponding to Pipe not found"
+ "CCProfileMonitor::applyConfiguration  shutdown pending, dropping request and exiting\n"
+ "CCProfileMonitor::profileCallback during shutdown (1) CCDaemon::getInstance().isShutdownPending() == true \n"
+ "CCProfileMonitor::profileCallback during shutdown (2) CCDaemon::getInstance().isShutdownPending() == true \n"
+ "CCProfileMonitor::profileCallback exiting states CCDaemon::getInstance().isShutdownPending() %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::profileCallback starting states CCDaemon::getInstance().isShutdownPending() %d fProfileLoaded %d fProfileRemoveApplied %d\n"
+ "CCProfileMonitor::setStreamEventHandler CCDaemon::getInstance().isShutdownPending() == true, dropping event and exiting\n"
+ "CCServiceMonitor::servicesPublished ignoring processing servicePublished due to isShutdownPending"
+ "CCTerminate"
+ "CCXPCService::handleConnectionEvent CCDaemon::getInstance().isShutdownPending() true, dropping xpc event and exiting\n"
+ "CCXPCService::handleIncomingMessage CCDaemon::getInstance().isShutdownPending() true, dropping message and exiting\n"
+ "Capture"
+ "CaptureEvent"
+ "Carrier"
+ "Circular"
+ "Continuous"
+ "CoreCaptureStart called when CCDaemon already running, returning existing instance"
+ "CoreCaptureStart called with bad args, crashing"
+ "CoreCaptureStop called when isShutdownPending true, ignoring"
+ "CoreCaptureStop called when no CCDaemon running, CCDaemon::isInitialized() returned false, ignoring"
+ "CoreCaptureStop complete\n"
+ "CoreCaptureStop failed with exception: %s"
+ "CoreCaptureStop non daemon cleanup, calling ccfree\n"
+ "CoreCaptureStop non daemon stopping, calling quiesceAllTaps()\n"
+ "CoreCaptureStop setShutdownAlreadyTrue, exiting without doing anything"
+ "CrashTracerLog"
+ "FileCloseReason"
+ "Log"
+ "LogEvents"
+ "LogFileSize"
+ "LogTimeSpan"
+ "MaxFileSize"
+ "MaxNumberOfFiles"
+ "MultiFunctionManager"
+ "OSSerialize"
+ "OSSerializeWithIOReporter"
+ "Pcapng"
+ "PipeSize"
+ "Raw"
+ "ReleaseType"
+ "Rollover"
+ "Stream"
+ "Text"
+ "Unknown"
+ "WiFi"
+ "^v8@?0"
+ "_dataTapInterestCallback_dext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"
+ "_dataTapInterestCallback_kext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"
+ "_logTapInterestCallback_dext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"
+ "_logTapInterestCallback_kext called when CCDaemon::getInstance().isShutdownPending() == true, ignoring\n"
+ "bluetooth.logging"
+ "can reduce logging: %d\n"
+ "cancelableBlockFunc_block_invoke"
+ "cc.recovery.allow"
+ "cleanupLogFile"
+ "com.apple.corecapture.fileclose"
+ "com.apple.corecaptured.background_queue"
+ "compressFile"
+ "containsString:"
+ "countByEnumeratingWithState:objects:count:"
+ "installedProfileIdentifiers"
+ "marconi-wifi"
+ "previous and current sequence numbers are same %u entry %u\n"
+ "sharedConnection"
+ "stopPipeMonitor"
+ "wifi.megawifi"
+ "wlan"
- "CCDaemon received system wake, all cctap resumed from quiesced state\n"
- "CCDaemon::No of matching CCPipe %ld\n"
- "CCDaemon::init Failed to create CCXPCService\n"
- "CCDaemon::non daemon cleanup is in progress\n"
- "CCFIle::copyFile: Unable to stat source path errno %d, reason %s\n"
- "CCFile::copyFile written bytes 0 \n"
- "CCFile::mkdirRecursive Unable to create path '%s' as '%s' is not a directory\n"
- "CCFile::mkdirRecursive Unable to mkdir on '%s'\n"
- "CCLogFile::deleteFile name: %s \n"
- "CCProfileMonitor::applyConfiguration  shutdown pending\n"
- "CCProfileMonitor::profileCallback during shutdown (1) \n"
- "CCProfileMonitor::profileCallback during shutdown (2) \n"
- "CCProfileMonitor::profileCallback exiting states shutDownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
- "CCProfileMonitor::profileCallback starting states shutDownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n"
- "previous and current sequence numbers are same %u\n"

```
