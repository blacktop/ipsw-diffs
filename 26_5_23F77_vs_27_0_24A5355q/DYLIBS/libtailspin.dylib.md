## libtailspin.dylib

> `/usr/lib/libtailspin.dylib`

```diff

-250.2.0.0.0
-  __TEXT.__text: 0x275e0
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x191
-  __TEXT.__cstring: 0x2fce
-  __TEXT.__oslogstring: 0x2baa
-  __TEXT.__gcc_except_tab: 0x1b68
-  __TEXT.__dlopen_cstrs: 0x9e
+262.0.0.0.0
+  __TEXT.__text: 0x2862c
+  __TEXT.__objc_methlist: 0x254
+  __TEXT.__const: 0x181
+  __TEXT.__cstring: 0x34cd
+  __TEXT.__oslogstring: 0x2cbe
+  __TEXT.__gcc_except_tab: 0x1c08
+  __TEXT.__dlopen_cstrs: 0x11a
   __TEXT.__ustring: 0x6
-  __TEXT.__unwind_info: 0xa60
-  __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methname: 0x11cd
-  __TEXT.__objc_methtype: 0xfb
-  __TEXT.__objc_stubs: 0x1240
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0xa70
+  __TEXT.__unwind_info: 0xa80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xad0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x538
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x858
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x1cc0
-  __AUTH_CONST.__objc_const: 0x300
-  __DATA.__objc_ivar: 0x34
+  __AUTH_CONST.__cfstring: 0x1e20
+  __AUTH_CONST.__objc_const: 0x3c0
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x858
+  __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x10
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x6b8
+  __DATA.__bss: 0x720
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x21b8
+  __DATA_DIRTY.__bss: 0x21b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20A06CD7-2C7E-37D8-887A-601E410E8910
-  Functions: 679
-  Symbols:   543
-  CStrings:  1055
+  UUID: 27ED7F49-C302-3C60-BEE8-A30BD51F691E
+  Functions: 706
+  Symbols:   552
+  CStrings:  881
 
Symbols:
+ _OBJC_CLASS_$_NSCountedSet
+ _TSPCPUTraceOptions_PidFilters
+ _TSPConfiguration_CPUTraceOptionsKey
+ _TSPConfiguration_CPUTraceOptions_PidFiltersKey
+ _TSPMetadata_RunawayMitigationHistoryKey
+ _ktrace_events_all
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_retain_x9
+ _tailspin_cputrace_enabled_get_with_options
- ___cxa_end_catch
- ___cxa_rethrow
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ " for pids [%@]"
+ ", "
+ "<empty>"
+ "A2!"
+ "Augment failed (see augment subphase signposts for specific reason)"
+ "CPUTraceOptions"
+ "CPUTraceOptions_PidFilters"
+ "Class getComputeSafeguardsManagingClientClass(void)_block_invoke"
+ "ComputeSafeguardsManagingClient"
+ "Configuring CPUTrace on pid: %d"
+ "Enabling on-device decoding"
+ "Error getting runaway mitigation history: %@"
+ "FAILED with error: %{public}@.\nFile path: %{public}@"
+ "Invalid pid filter value: %d (must be >= 0), skipping"
+ "Phase_Augment"
+ "Phase_Augment_LoggingData"
+ "Phase_Augment_Symbolicate"
+ "Phase_KdebugBufferWriteout"
+ "Phase_PostProcessing_Libktrace"
+ "Phase_PostProcessing_Tailspin"
+ "Phase_SaveStandardChunks"
+ "Phase_SaveStandardChunks_WithoutPostProcessing"
+ "RunawayMitigationHistory"
+ "Unable to configure more than %d pids, skipping %d"
+ "Unable to use existing ktrace buffer: %s"
+ "hwtrace_error_t soft_hwtrace_recording_save(hwtrace_recording_t, hwtrace_recording_save_options_t)"
+ "hwtrace_live_recording_system_options_add_context_target_filtered"
+ "hwtrace_recording_save"
+ "hwtrace_recording_save_options_deinit"
+ "hwtrace_recording_save_options_init"
+ "hwtrace_recording_save_options_set_decode_trace"
+ "hwtrace_recording_save_options_set_ktrace_file"
+ "hwtrace_recording_save_options_t soft_hwtrace_recording_save_options_init()"
+ "ktrace_start_writing_fd() failed for original fd %d (dup %d) for client %s [%d]: with errno %d"
+ "softlink:o:path:/System/Library/PrivateFrameworks/PowerExceptions_ClientFramework.framework/PowerExceptions_ClientFramework"
+ "tailspin_cputrace_option_pid_filters"
+ "void *PowerExceptions_ClientFrameworkLibrary(void)"
+ "void soft_hwtrace_live_recording_system_options_add_context_target_filtered(hwtrace_live_recording_system_options_t, uint64_t)"
+ "void soft_hwtrace_recording_save_options_deinit(hwtrace_recording_save_options_t)"
+ "void soft_hwtrace_recording_save_options_set_decode_trace(hwtrace_recording_save_options_t, bool)"
+ "void soft_hwtrace_recording_save_options_set_ktrace_file(hwtrace_recording_save_options_t, ktrace_file_t)"
- ".cxx_destruct"
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@16@0:8"
- "Augment"
- "Augment_LoggingData"
- "Augment_Symbolicate"
- "B"
- "B16@0:8"
- "FAILED due to reason: %{public}@.\nFile path: %{public}@"
- "PostProcessing_Libktrace"
- "PostProcessing_Tailspin"
- "Q"
- "Q16@0:8"
- "Q24@0:8r*16"
- "SaveStandardChunks"
- "SaveStandardChunks_WithoutPostProcessing"
- "T@\"NSMutableDictionary\",R,N,V_timeSpentByPhases"
- "T@\"NSString\",&,N,V_filePath"
- "T@\"NSString\",&,N,V_prevExecName"
- "TB,N,V_didClientRequestEndTimestamp"
- "TB,N,V_didPrevClientSaveOverlapWithEndTimestamp"
- "TQ,N,V_numEvents"
- "TQ,R,N,V_request_id"
- "TSPSaveMeasurements"
- "Td,R,N,V_lostTimePeriodAtStartSecs"
- "Td,R,N,V_ratioTimePeriodCovered"
- "Td,R,N,V_requestProcessingLatencySecs"
- "Td,R,N,V_tailspinDurationSecs"
- "Tq,N,V_fileSizeBytes"
- "UTF8String"
- "UUIDString"
- "_didClientRequestEndTimestamp"
- "_didPrevClientSaveOverlapWithEndTimestamp"
- "_filePath"
- "_fileSizeBytes"
- "_lostTimePeriodAtStartSecs"
- "_numEvents"
- "_prevExecName"
- "_ratioTimePeriodCovered"
- "_requestProcessingLatencySecs"
- "_request_id"
- "_saveStandardChunksStartTimestampMCT"
- "_startRecordingTimeForPhase:"
- "_stopRecordingTimeForPhase:"
- "_tailspinDurationSecs"
- "_timeSpentByPhases"
- "addIndex:"
- "addObject:"
- "allInstalledRootsAndReturnError:"
- "appendFormat:"
- "appendString:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "argumentAtIndex:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "automatedDeviceGroup"
- "binaryLoadInfoForLiveProcessWithPid:dataGatheringOptions:"
- "binaryVersion"
- "binaryWithUUID:absolutePath:"
- "boolForKey:"
- "boolValue"
- "bundleIdentifier"
- "bundleShortVersion"
- "bundleVersion"
- "bytes"
- "category"
- "clearSymbolCaches"
- "closeAndReturnError:"
- "compare:"
- "compatibilityVersion"
- "containsObject:"
- "containsString:"
- "copy"
- "copyCurrentMitigationInfoForClientIdentifier:"
- "copyPathForPersonalizedData:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentHandler"
- "d"
- "d16@0:8"
- "dataUsingEncoding:"
- "dataWithContentsOfFile:"
- "dataWithPropertyList:format:options:error:"
- "debugDescription"
- "decomposedMessage"
- "defaultManager"
- "defaultProvider"
- "defaultStateForFeature:domain:"
- "deploymentId"
- "description"
- "dictionary"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjects:forKeys:count:"
- "didClientRequestEndTimestamp"
- "didPrevClientSaveOverlapWithEndTimestamp"
- "domains"
- "enumerateActiveExperimentsForEnvironment:error:block:"
- "enumerateActiveRolloutsWithError:block:"
- "enumerateKeysAndObjectsUsingBlock:"
- "experimentId"
- "factorPackIds"
- "featuresForDomain:"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "filePath"
- "fileSizeBytes"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "fileURLWithPath:isDirectory:"
- "firstObject"
- "gatherInfoWithDataGatheringOptions:pid:"
- "getUUIDBytes:"
- "handleFailureInFunction:file:lineNumber:description:"
- "hwtrace_error_t soft_hwtrace_recording_save_to_ktrace(hwtrace_recording_t, ktrace_file_t)"
- "hwtrace_recording_save_to_ktrace"
- "indexSetWithIndex:"
- "init"
- "initWithCapacity:"
- "initWithData:encoding:"
- "initWithFormat:"
- "initWithObjectsAndKeys:"
- "initWithSuiteName:"
- "initWithTimeIntervalSince1970:"
- "initWithUUIDBytes:"
- "initWithUUIDString:"
- "intValue"
- "invalidateCache"
- "invalidateConnection"
- "lastPathComponent"
- "length"
- "localStore"
- "localeWithLocaleIdentifier:"
- "lostTimePeriodAtStartSecs"
- "lowercaseString"
- "mitigationLevel"
- "name"
- "namespaces"
- "numEvents"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectRepresentation"
- "openAndReturnError:"
- "path"
- "placeholderCount"
- "preferredLanguages"
- "prevExecName"
- "q"
- "q16@0:8"
- "rampId"
- "ratioTimePeriodCovered"
- "recordLostTimePeriodAtStart:"
- "recordRatioTimePeriodCovered:"
- "recordRequestProcessingLatencySecsWithStartMCT:endMCT:"
- "recordTailspinDurationWithStartMCT:endMCT:"
- "recordTimeForSaveStandardChunksWithoutPostProcessing:"
- "requestProcessingLatencySecs"
- "request_id"
- "rolloutId"
- "segmentWithName:"
- "setDidClientRequestEndTimestamp:"
- "setDidPrevClientSaveOverlapWithEndTimestamp:"
- "setFilePath:"
- "setFileSizeBytes:"
- "setNumEvents:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setPrevExecName:"
- "shared"
- "sharedDataAccessor"
- "sharedInstance"
- "signpostName"
- "startRecordingTimeForAugmentLoggingPhase:collectOSLog:scrubData:"
- "startRecordingTimeForAugmentPhase:pid:originalFd:dupFd:"
- "startRecordingTimeForAugmentSymbolicatePhase"
- "startRecordingTimeForDumpRequestPhase:pid:"
- "startRecordingTimeForLibktracePostProcessing"
- "startRecordingTimeForSaveStandardChunksPhase:pid:"
- "startRecordingTimeForTailspinPostProcessing"
- "stateForFeature:domain:level:"
- "stopRecordingTimeForAugmentLoggingPhase:"
- "stopRecordingTimeForAugmentPhase:finalSizeBytes:"
- "stopRecordingTimeForAugmentSymbolicatePhase"
- "stopRecordingTimeForDumpRequestPhase:"
- "stopRecordingTimeForLibktracePostProcessing"
- "stopRecordingTimeForSaveStandardChunksPhase:"
- "stopRecordingTimeForTailspinPostProcessing"
- "storeWithArchiveURL:"
- "string"
- "stringByAppendingString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "subsystem"
- "symbolicateUUID:pid:path:offsets:options:"
- "tailspinDurationSecs"
- "timeIntervalSinceDate:"
- "timeIntervalSinceReferenceDate"
- "timeSpentByPhases"
- "treatmentId"
- "unsignedLongLongValue"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v24@0:8r*16"
- "v28@0:8B16B20B24"
- "v28@0:8B16q20"
- "v28@0:8r*16i24"
- "v32@0:8Q16Q24"
- "v36@0:8r*16i24i28i32"
- "value"
- "writeToFile:atomically:"

```
