## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1270.80.1.0.0
-  __TEXT.__text: 0x2d3b4
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_stubs: 0xce0
-  __TEXT.__objc_methlist: 0x274
+1295.100.44.0.0
+  __TEXT.__text: 0x2ef5c
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0xf4
-  __TEXT.__gcc_except_tab: 0x38c
-  __TEXT.__oslogstring: 0x156f
-  __TEXT.__cstring: 0x285ab
-  __TEXT.__objc_classname: 0x35
-  __TEXT.__objc_methname: 0xbc8
-  __TEXT.__objc_methtype: 0x115
-  __TEXT.__unwind_info: 0x39c
-  __DATA_CONST.__auth_got: 0x4d0
+  __TEXT.__gcc_except_tab: 0x400
+  __TEXT.__oslogstring: 0x179d
+  __TEXT.__cstring: 0x292db
+  __TEXT.__objc_classname: 0x37
+  __TEXT.__objc_methname: 0xd5a
+  __TEXT.__objc_methtype: 0x159
+  __TEXT.__unwind_info: 0x408
+  __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__auth_ptr: 0x70
-  __DATA_CONST.__const: 0x480
-  __DATA_CONST.__cfstring: 0x13a0
+  __DATA_CONST.__auth_ptr: 0x80
+  __DATA_CONST.__const: 0x4c8
+  __DATA_CONST.__cfstring: 0x14e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x120
-  __DATA.__objc_selrefs: 0x340
-  __DATA.__objc_classrefs: 0xb0
+  __DATA.__objc_const: 0x190
+  __DATA.__objc_selrefs: 0x390
+  __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3f8
   __DATA.__bss: 0x10

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreCaptureControl.framework/CoreCaptureControl
+  - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NearField.framework/NearField

   - /System/Library/PrivateFrameworks/ProactiveInputPredictions.framework/ProactiveInputPredictions
   - /System/Library/PrivateFrameworks/Proximity.framework/Proximity
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: 77DA0668-7F2C-3C73-89C1-53E6B30EB806
-  Functions: 211
-  Symbols:   207
-  CStrings:  3438
+  UUID: 625BECD1-10FF-3714-8BC5-6B60263A8D0D
+  Functions: 237
+  Symbols:   215
+  CStrings:  3588
 
Symbols:
+ _CRGenerateRepairReport
+ _OBJC_CLASS_$_SBSStateDumpService
+ ___NSDictionary0__struct
+ __os_crash_msg
+ __os_log_send_and_compose_impl
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_sync
+ _objc_getProperty
+ _objc_msgSendSuper2
+ _objc_setProperty_atomic
+ _os_eligibility_dump_sysdiagnose_data_to_dir
+ _pthread_setugid_np
- _OBJC_CLASS_$_NSMutableDictionary
- _getuid
- _kCFPreferencesAnyUser
- _seteuid
CStrings:
+ "\x02"
+ ".cxx_destruct"
+ "@\"NSObject<OS_dispatch_queue>\""
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: GCReadSequential(1106): Cannot add 14 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): (#15) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsReadSectors(1042): Cannot add 15 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsSnapshot(1041): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): (#31) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: bandsAgeBinsV2(1040): Cannot add 31 elements to context"
+ "ASPFTLParseBufferToCxt: cbdrAborts(696) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrFullyDone(699) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrResumeSent(689) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: cbdrSkippedBlocks(758) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterDestinations(721) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcPDusterWrites(722) cannot add 1 element to context"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): (#32) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: gcwamp(1116): Cannot add 32 elements to context"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): (#14) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: hostReadSequential(1105): Cannot add 14 elements to context"
+ "B40@0:8@?16d24@32"
+ "CoreRepair SPI not found"
+ "CoreRepair SPI returned nil plist"
+ "CoreRepair SPI timed out"
+ "CoreRepair: failed to write report to disk: %{public}s"
+ "Creating helper shared instance"
+ "DirectManagerState"
+ "Err: Finding internal NAND exporter failed.\n"
+ "Error fetching the tunnel output buffer for opcode [%d], Result [0x%X]\n"
+ "Error querying Wifi Velocity configuration for peer due to %@. Assuming WiFiVelocity MegaProfile is not enabled"
+ "Error: Cannot Extract Band Stats for ASP3\n"
+ "Error: must provide valid pointer for output value"
+ "Failed to generate repair report. Success: %d, error: %{public}s"
+ "GCReadSequential"
+ "GCReadSequential_"
+ "GCSlcToTlcRVFails"
+ "GCTlcToTlcRVFails"
+ "Got error from os_eligibility_dump_sysdiagnose_data_to_dir (%d): %{public}s"
+ "RepairReport.plist"
+ "SBOGcMusted"
+ "SBOGcMustedValid"
+ "SBOMaxWaited"
+ "SBONumAccomplished"
+ "SBONumCanceled"
+ "SBOSumWaited"
+ "SBSStateDumpService SPI not available"
+ "SBSStateDumpService SPI timed out"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_serialQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_userModeQueue"
+ "TASK_TYPE_COREREPAIR_DIAGNOSTIC"
+ "TASK_TYPE_OS_ELIGIBILITY"
+ "TASK_TYPE_SPRING_BOARD_STATE_DUMP"
+ "TASK_TYPE_UID"
+ "Unable to open %@: %s"
+ "Unable to set root mode with error: %s. Aborting because this thread is in a bad state."
+ "Unable to set user mode. Not running block"
+ "_runBlockForCurrentUser:withTimeout:"
+ "_runDispatchBlock:withTimeout:onQueue:"
+ "_serialQueue"
+ "_userModeQueue"
+ "band_rbo_allocated"
+ "bandsAgeBinsReadSectors"
+ "bandsAgeBinsReadSectors_"
+ "bandsAgeBinsSnapshot"
+ "bandsAgeBinsSnapshot_"
+ "bandsAgeBinsV2"
+ "bandsAgeBinsV2_"
+ "bandsUeccTempHisto"
+ "blockErases"
+ "boListHighwatermark"
+ "cacheSegCombines"
+ "com.apple.MobileAsset"
+ "com.apple.sysdiagnose.sysdiagnose_helper.serialQueue"
+ "com.apple.sysdiagnose_helper.userModeQueue"
+ "com.apple.voiceservices"
+ "coreRepairDiagnosticTaskWithDir:withTimeout:"
+ "dictionaryWithDictionary:"
+ "dmArtificialNeighborFormat"
+ "dmArtificialNeighborGbb"
+ "flushNwToOslc"
+ "fullRVFails"
+ "gcVerticalDepthLimitFragments"
+ "gcVerticalDepthLimitSectors"
+ "gc_concurrent_vert_gc1"
+ "gc_concurrent_vert_gc12"
+ "gc_concurrent_vert_gc2"
+ "gc_cur_vert_gc1"
+ "gc_cur_vert_gc2"
+ "gc_cur_vert_gc3"
+ "gc_tot_vert_gc1"
+ "gc_tot_vert_gc2"
+ "gcwamp"
+ "gcwamp_"
+ "hostExcessiveZeroTP"
+ "hostReadSequential"
+ "hostReadSequential_"
+ "hostReadsByFlow"
+ "hostReadsVerticalByFlow"
+ "hostSlcRVFails"
+ "hostTlcRVFails"
+ "init"
+ "intermediateBlockErases"
+ "isUnhappy"
+ "ldefragActivations"
+ "ldefragDroppedSegs"
+ "ldefragHostTotalReadSectors"
+ "ldefragHostTrimSectors"
+ "ldefragOnlyTrollingOnChoke"
+ "ldefragTrollChains"
+ "ldefragTrollFragments"
+ "ldefragTrollSectors"
+ "ldefragTrollTotalReadSectors"
+ "ldefragTrollTrimSectors"
+ "maxUeccsDuringBoot"
+ "nandGeomErrorSkippedErrors"
+ "nil"
+ "numOfToHappySwitches"
+ "numOfToUnhappySwitches"
+ "os eligibility SPI not found"
+ "os eligibility task timed out"
+ "osEligibilityDumpToDir:withTimeout:"
+ "pgCompactNum"
+ "pgCompactPGIndxs"
+ "pgCompressionBlocksInDip"
+ "pgCompressionBlocksInPG"
+ "pgCompressionBlocksRelease"
+ "pgCompressionNum"
+ "pgCompressionPmxSecWrites"
+ "pgGCpmxSecWrites"
+ "pushWrittenSegCombines"
+ "raidForceClogLoad"
+ "reducedRVFails"
+ "rxBurnBlocksProbe"
+ "serialQueue"
+ "setSerialQueue:"
+ "slcHostPadSamsungV8"
+ "slcParityPadSamsungV8"
+ "slowHwToOslc"
+ "springBoardStateDumpTaskWithTimeout:"
+ "subscribedAssets"
+ "supportsUnhappy"
+ "turboRaidFailedSkip"
+ "turboRaidQualityGBBs"
+ "turboRaidSkipTooManyFailuresFailRec"
+ "turboRaidSuccssfulSkip"
+ "userModeQueue"
+ "utilFastResetCnt"
+ "v16@0:8"
+ "v24@0:8@16"
+ "writeStateDump:toTextFileAtPath:"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): (#10) cfg elements != (%d) buffer elements"
- "ASPFTLParseBufferToCxt: fwaHistogram(913): Cannot add 10 elements to context"
- "Error querying Wifi Velocity configuration for peer due to %@"
- "Unable to create empty file '%s' with error: %s"
- "Unable to set root mode with error: %s."
- "addEntriesFromDictionary:"
- "dictionary"
- "fwaHistogram_"
- "gcLonlyDroppedT1s"
- "gcLonlyTimeSpentUs"
- "lFullLaps"

```
