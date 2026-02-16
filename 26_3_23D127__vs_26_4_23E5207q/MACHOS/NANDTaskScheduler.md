## NANDTaskScheduler

> `/usr/libexec/NANDTaskScheduler`

```diff

-653.80.5.0.0
-  __TEXT.__text: 0x1d7bc
-  __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x60
-  __TEXT.__cstring: 0x2c360
-  __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x4a7
-  __TEXT.__objc_methname: 0x59
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x130
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__cfstring: 0x100
+659.100.55.0.0
+  __TEXT.__text: 0x217f4
+  __TEXT.__auth_stubs: 0x510
+  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0xc4
+  __TEXT.__cstring: 0x2d6d5
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__oslogstring: 0x11fa
+  __TEXT.__objc_classname: 0x3f
+  __TEXT.__objc_methname: 0x62b
+  __TEXT.__objc_methtype: 0x116
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__auth_got: 0x298
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__cfstring: 0x420
+  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x18
-  __DATA.__data: 0x3d8
-  __DATA.__common: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA.__objc_const: 0x118
+  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_ivar: 0x8
+  __DATA.__objc_data: 0x50
+  __DATA.__data: 0x448
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/SidebarFileDispatcher
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D7ED15D-50A1-35C3-90AE-858C82989DC6
-  Functions: 82
-  Symbols:   50
-  CStrings:  3180
+  UUID: 5551FE51-8B9E-3884-800B-F1EB0A5D5247
+  Functions: 157
+  Symbols:   120
+  CStrings:  3486
 
Symbols:
+ _APFSPurgeExtentIteratorCreate
+ _APFSPurgeExtentIteratorDestroy
+ _APFSPurgeExtentIteratorIterate
+ _AnalyticsSendEventLazy
+ _CFDictionaryCreateMutable
+ _CFDictionarySetValue
+ _CFNumberCreate
+ _CFRelease
+ _NSLocalizedDescriptionKey
+ _NSSearchPathForDirectoriesInDomains
+ _NSUnderlyingErrorKey
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NSXPCConnection
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_METACLASS_$_NSObject
+ __Block_object_assign
+ __Block_object_dispose
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___objc_personality_v0
+ __objc_empty_cache
+ __os_log_debug_impl
+ __os_log_error_impl
+ _close
+ _dispatch_once
+ _dispatch_queue_create
+ _dispatch_sync
+ _fstat
+ _fsync
+ _ftruncate
+ _kAPFSPurgeExtentIteratorOptions
+ _kAPFSPurgeExtentIteratorUrgency
+ _kCFAllocatorDefault
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _lseek
+ _objc_alloc
+ _objc_alloc_init
+ _objc_autorelease
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeak
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_release_x19
+ _objc_release_x21
+ _objc_release_x22
+ _objc_setProperty_nonatomic
+ _open
+ _os_variant_has_factory_content
+ _os_variant_has_internal_content
+ _os_variant_is_darwinos
+ _strerror
+ _write
CStrings:
+ "\n"
+ "\n================================================\n"
+ "   entry %u: LBA=0x%llx, length=%llu, pos=%u"
+ "  offset= 0x%llx, length= %llu"
+ "%8llu "
+ ".dat"
+ "/private/var/"
+ "/private/var/mobile/"
+ "================================================\n\n"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSXPCConnection\""
+ "@16@0:8"
+ "ASPFTLParseBufferToCxt: IND_pool_avgTileSlackP(1703) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: IND_pool_tilesInUseP(1672) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: IND_pool_tilesSlackP(1673) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: dataLossHisto(1683): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: dataLossHisto(1683): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: extraSenseHisto(1676): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: extraSenseHisto(1676): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: formatNum(1654) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: formatNumOnSwitch(1658): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: formatNumOnSwitch(1658): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: huState(1660): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: huState(1660): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: massScanCurrentState(1347) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanForceStartWithPilot(1425) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanIgnoredRaidConversion(1477) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanNarrowBandsRefreshed(1476) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanPilotFailedContinuedToFull(1665) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanPilotIgnoredTooFrequent(1424) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanTotalRefreshedBands(1475) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: massScanTotalScannedBands(1474) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: mspSOCID(1688) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: numPaddingPfail(1480) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: pePrevStartSLC(1662): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: pePrevStartSLC(1662): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: pePrevStartTLC(1661): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: pePrevStartTLC(1661): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: peThresholdStart(1659): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: peThresholdStart(1659): Cannot add 4 elements to context"
+ "ASPFTLParseBufferToCxt: perfPOHisto(1675): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: perfPOHisto(1675): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: qualClassHisto(1680): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: qualClassHisto(1680): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: relClassHisto(1679): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: relClassHisto(1679): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: relPOHisto(1677): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: relPOHisto(1677): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: turboFailureHisto(1682): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: turboFailureHisto(1682): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: turboSuccessHisto(1681): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: turboSuccessHisto(1681): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: uncHisto(1678): (#10) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: uncHisto(1678): Cannot add 10 elements to context"
+ "ASPFTLParseBufferToCxt: unhLogIndex(1655) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: waAtTheRecordingPoint(1663): (#4) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: waAtTheRecordingPoint(1663): Cannot add 4 elements to context"
+ "ASPMSPParseBufferToCxt: fw_version_identifier(16384): Error adding 8 elements to context"
+ "ASPMSPParseBufferToCxt: fw_version_identifier(16384): cfg 8 elements; (8*1) cfg bytes != (%d) buffer bytes"
+ "Bucket %2d: %8llu\n"
+ "Cannot match entries: failed to get today's file path"
+ "Cannot match entries: failed to get yesterday's file path"
+ "Cannot match entries: failed to open file handles"
+ "Cannot match entries: today's file does not exist"
+ "Cannot match entries: yesterday's file does not exist (skipping match)"
+ "Cannot print entries: file not open"
+ "Cannot save histogram: failed to get directory"
+ "Cannot truncate: file not open"
+ "Cannot write entry: file not open"
+ "Could not create data iterator."
+ "Could not create user iterator."
+ "Created data iterator"
+ "Created user iterator"
+ "DATA iterator done"
+ "DIR ino=0x%llx"
+ "DIREND ino=0x%llx"
+ "Deleted old file: %s"
+ "Ending purge urgency %d"
+ "Established XPC connection to SidebarFileDispatcher service"
+ "Extent Size Histogram - %@\n"
+ "FILE ino=0x%llx"
+ "Failed to allocate extSizeHisto array"
+ "Failed to allocate purgeableShiftHisto array"
+ "Failed to communicate with XPC service"
+ "Failed to create CF number objects"
+ "Failed to create CFDictionary options"
+ "Failed to create purgeable buffer directory: %s"
+ "Failed to create purgeable buffer file"
+ "Failed to delete %s: %s"
+ "Failed to get file stats for sorting: %s"
+ "Failed to get purgeable buffer file path"
+ "Failed to initialize purgeable buffer file"
+ "Failed to list directory contents: %s"
+ "Failed to match purgeable entries."
+ "Failed to match purgeable entries: %s"
+ "Failed to open purgeable buffer file: %s"
+ "Failed to pre-allocate purgeable buffer file: %s"
+ "Failed to print purgeable entries: %s"
+ "Failed to process file: %s\n"
+ "Failed to seek in purgeable buffer file: %s"
+ "Failed to seek to beginning: %s"
+ "Failed to sort and deduplicate file."
+ "Failed to truncate purgeable buffer file: %s"
+ "Failed to write histogram file: %s"
+ "Failed to write purgeable entry to file"
+ "Failed to write purgeable entry to file: %s"
+ "Filling with dummy entries..."
+ "Hanging NANDTaskScheduler for leaks check"
+ "Histogram saved to: %s"
+ "IDSTK ping failed to send."
+ "IND_pool_avgTileSlackP"
+ "IND_pool_tilesInUseP"
+ "IND_pool_tilesSlackP"
+ "Idlestack should defer."
+ "Invalid purgeableShift data received"
+ "Keeping file: %s"
+ "Loaded persistent state: dStage=%u, dTestModes=%u"
+ "Match purgeable positions completed successfully"
+ "Match purgeable positions failed: %{public}@"
+ "Matching purgeable entries between today and yesterday..."
+ "Max entries reached: abort."
+ "Pre-allocating purgeable buffer file to %zu bytes (~24MB)"
+ "Print entries completed successfully"
+ "Print entries failed: %{public}@"
+ "Printing today's purgeable entries via XPC service..."
+ "Purgable processing completed successfully, status %d"
+ "Purgable processing failed: %{public}@, status %d"
+ "Purgeable Shift Histogram - %@\n"
+ "Purgeable buffer file closed"
+ "Purgeable buffer file created/opened: %s"
+ "Purgeable buffer file pre-allocated successfully"
+ "Purgeable buffer file truncated successfully"
+ "Purgeable iteration complete: found %u extents and total purgeable size %u MB."
+ "Received extent size histogram with %zu bytes"
+ "Row %2d: "
+ "Saved persistent state: dStage=%u, dTestModes=%u"
+ "SideBarFileDispatcherAPI"
+ "SideBarFileDispatcherAPI connection invalidated"
+ "SideBarFileDispatcherAPI initialized"
+ "SidebarFileDispatcherServiceProtocol"
+ "Starting purge urgency %d"
+ "Successfully matched purgeable entries, received %zu bytes"
+ "Successfully processed file at fd: %d, unique %u, overlaps %u\n"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connectionQueue"
+ "T@\"NSXPCConnection\",&,N,V_connectionToService"
+ "Today's purgeable file already exists (%llu bytes), skipping iteration"
+ "Total buckets: %d\n\n"
+ "Total buckets: %d, Overlaps: %u\n"
+ "Truncating purgeable buffer file to %zu bytes (%u entries)"
+ "USER iterator done."
+ "UTF8String"
+ "Urgency %d"
+ "XPC connection to SidebarFileDispatcher interrupted"
+ "XPC connection to SidebarFileDispatcher invalidated"
+ "XPC proxy error: %{public}@"
+ "_connectionQueue"
+ "_connectionToService"
+ "appendFormat:"
+ "appendString:"
+ "attributesOfItemAtPath:error:"
+ "closeFile"
+ "com.apple.massStorage.NANDInfo.purgeableReordering"
+ "com.apple.storage.SidebarFileDispatcherService"
+ "com.apple.storage.SidebarFileDispatcherService.connection"
+ "com.sidebar.filedispatchererror"
+ "connection"
+ "connectionQueue"
+ "connectionToService"
+ "contentsOfDirectoryAtPath:error:"
+ "countByEnumeratingWithState:objects:count:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "dStage"
+ "dTestModes"
+ "dataLossHisto"
+ "dataLossHisto_"
+ "date"
+ "dateByAddingTimeInterval:"
+ "defaultManager"
+ "dictionaryWithObjects:forKeys:count:"
+ "errorWithDomain:code:userInfo:"
+ "extraSenseHisto"
+ "extraSenseHisto_"
+ "fileExistsAtPath:"
+ "fileHandleForReadingAtPath:"
+ "fileSize"
+ "formatNum"
+ "formatNumOnSwitch"
+ "formatNumOnSwitch_"
+ "fw_version_identifier_"
+ "getBytes:length:"
+ "hasPrefix:"
+ "hasSuffix:"
+ "histogram_%@.txt"
+ "huState"
+ "huState_"
+ "i16@?0^{?=S^{?}IQS}8"
+ "idleStack_med task expiring"
+ "init"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "initWithFormat:"
+ "initWithServiceName:"
+ "integerForKey:"
+ "interfaceWithProtocol:"
+ "invalidate"
+ "isEqualToString:"
+ "length"
+ "localizedDescription"
+ "massScanCurrentState"
+ "massScanForceStartWithPilot"
+ "massScanIgnoredRaidConversion"
+ "massScanNarrowBandsRefreshed"
+ "massScanPilotFailedContinuedToFull"
+ "massScanPilotIgnoredTooFrequent"
+ "massScanTotalRefreshedBands"
+ "massScanTotalScannedBands"
+ "matchPurgeablePositionsToday:yesterdayF:reply:"
+ "mspSOCID"
+ "numDuplicateExtents"
+ "numPaddingPfail"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLongLong:"
+ "objectAtIndex:"
+ "pePrevStartSLC"
+ "pePrevStartSLC_"
+ "pePrevStartTLC"
+ "pePrevStartTLC_"
+ "peThresholdStart"
+ "peThresholdStart_"
+ "perfPOHisto"
+ "perfPOHisto_"
+ "printPurgeableFileEntries:reply:"
+ "purgeable iteration from idleStack_med not supported."
+ "purgeableExtentSizes_%d"
+ "purgeableShiftHisto_%d_%d"
+ "purgeable_"
+ "purgeable_%@.dat"
+ "qualClassHisto"
+ "qualClassHisto_"
+ "relClassHisto"
+ "relClassHisto_"
+ "relPOHisto"
+ "relPOHisto_"
+ "remoteObjectInterface"
+ "removeItemAtPath:error:"
+ "resume"
+ "running idleStack_med task (BGST) with purgeable iteration"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setConnectionQueue:"
+ "setConnectionToService:"
+ "setDateFormat:"
+ "setExpirationHandler:"
+ "setInteger:forKey:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setObject:forKey:"
+ "setRemoteObjectInterface:"
+ "setWithObject:"
+ "sharedDispatcher"
+ "sortAndDeduplicatePurgeableFile:reply:"
+ "standardUserDefaults"
+ "string"
+ "stringByAppendingPathComponent:"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "synchronize"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "turboFailureHisto"
+ "turboFailureHisto_"
+ "turboSuccessHisto"
+ "turboSuccessHisto_"
+ "uncHisto"
+ "uncHisto_"
+ "unhLogIndex"
+ "v16@0:8"
+ "v16@?0@\"NSError\"8"
+ "v24@0:8@16"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
+ "v28@?0I8@\"NSData\"12@\"NSError\"20"
+ "v32@0:8@\"NSFileHandle\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSFileHandle\"16@?<v@?I@\"NSData\"@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v40@0:8@\"NSFileHandle\"16@\"NSFileHandle\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v8@?0"
+ "waAtTheRecordingPoint"
+ "waAtTheRecordingPoint_"
+ "writeToFile:atomically:encoding:error:"
+ "yyyyMMdd"
- "ASPMSPParseBufferToCxt: fw_version_identifier(16384): Error adding 1 elements to context"
- "ASPMSPParseBufferToCxt: fw_version_identifier(16384): cfg 1 elements; (1*8) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8196): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: higher_die_temperature(8196): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8195): Error adding 16 elements to context"
- "ASPMSPParseBufferToCxt: lower_die_temperature(8195): cfg 16 elements; (16*4) cfg bytes != (%d) buffer bytes"
- "fw_version_identifier"
- "running idleStack_med task (BGST)"

```
