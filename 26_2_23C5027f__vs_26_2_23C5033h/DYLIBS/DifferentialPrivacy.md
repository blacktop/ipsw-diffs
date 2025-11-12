## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-684.60.1.0.5
-  __TEXT.__text: 0x5fc30
+684.60.3.0.5
+  __TEXT.__text: 0x5fda4
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x588c
+  __TEXT.__objc_methlist: 0x591c
   __TEXT.__const: 0x9e8
-  __TEXT.__cstring: 0x4a0c
-  __TEXT.__oslogstring: 0x431f
-  __TEXT.__gcc_except_tab: 0xd14
+  __TEXT.__cstring: 0x4b7c
+  __TEXT.__oslogstring: 0x42ba
+  __TEXT.__gcc_except_tab: 0xcfc
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__constg_swiftt: 0x300

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x18c0
+  __TEXT.__unwind_info: 0x1898
   __TEXT.__eh_frame: 0x858
-  __TEXT.__objc_classname: 0xd7f
-  __TEXT.__objc_methname: 0x9d45
-  __TEXT.__objc_methtype: 0x12be
-  __TEXT.__objc_stubs: 0x7ee0
-  __DATA_CONST.__got: 0x810
-  __DATA_CONST.__const: 0x1210
-  __DATA_CONST.__objc_classlist: 0x4a0
+  __TEXT.__objc_classname: 0xdbf
+  __TEXT.__objc_methname: 0x9da2
+  __TEXT.__objc_methtype: 0x12de
+  __TEXT.__objc_stubs: 0x7ea0
+  __DATA_CONST.__got: 0x818
+  __DATA_CONST.__const: 0x1238
+  __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2510
+  __DATA_CONST.__objc_selrefs: 0x2518
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x8d8
   __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x40c0
-  __AUTH_CONST.__objc_const: 0xae28
+  __AUTH_CONST.__cfstring: 0x4200
+  __AUTH_CONST.__objc_const: 0xafd8
   __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0x3a8
+  __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xe70
+  __AUTH.__objc_data: 0xf60
   __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0x534
   __DATA.__data: 0x9d0
-  __DATA.__bss: 0x950
+  __DATA.__bss: 0x940
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x24e8
   __DATA_DIRTY.__data: 0xc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 60CB0D08-5717-3A23-A951-CF31D9C248B5
-  Functions: 2441
-  Symbols:   7731
-  CStrings:  3564
+  UUID: 8FBD65B7-194D-3EBE-8DFD-2E059F9E578A
+  Functions: 2446
+  Symbols:   7756
+  CStrings:  3586
 
Symbols:
+ +[_DPCoreAnalyticsCollector reportCoreAnalyticsExecutionStage:error:key:count:isTelemetryAllowed:]
+ +[_DPCoreAnalyticsCollector reportCoreAnalyticsExecutionStageWithCollector:executionStage:error:key:count:isTelemetryAllowed:]
+ +[_DPCoreAnalyticsCollector telemetryTaskIdFromKey:]
+ +[_DPDatabaseRecorderError errorWithCode:description:]
+ +[_DPDatabaseRecorderError errorWithCode:underlyingError:description:]
+ +[_DPDediscoReporterError errorWithCode:description:]
+ +[_DPDediscoReporterError errorWithCode:underlyingError:description:]
+ +[_DPServer missingEntitlementError]
+ +[_DPServerError errorWithCode:description:]
+ +[_DPServerError errorWithCode:underlyingError:description:]
+ -[_DPDatabaseRecorder reportCoreAnalyticsExecutionStage:key:error:count:]
+ -[_DPDediscoReporter reportCoreAnalyticsExecutionStage:error:key:count:]
+ -[_DPServer reportCoreAnalyticsExecutionStage:error:key:count:]
+ -[_DPServer shouldNotRecord:forKey:count:]
+ -[_DPServer shouldNotRecord:forKey:count:].cold.1
+ -[_DPServer shouldNotRecord:forKey:count:].cold.2
+ _OBJC_CLASS_$__DPDatabaseRecorderError
+ _OBJC_CLASS_$__DPDediscoReporterError
+ _OBJC_CLASS_$__DPServerError
+ _OBJC_METACLASS_$__DPDatabaseRecorderError
+ _OBJC_METACLASS_$__DPDediscoReporterError
+ _OBJC_METACLASS_$__DPServerError
+ __DPCoreAnalyticsCommonKey
+ __DPCoreAnalyticsEvent_Reach
+ __DPCoreAnalyticsField_Count
+ __DPCoreAnalyticsField_ErrorCode
+ __DPCoreAnalyticsField_ErrorDomain
+ __DPCoreAnalyticsField_ExecutionStage
+ __DPCoreAnalyticsField_TaskId
+ __DPDatabaseRecorderErrorDomain
+ __DPDediscoReporterErrorDomain
+ __DPServerErrorDomain
+ __OBJC_$_CLASS_METHODS__DPDatabaseRecorderError
+ __OBJC_$_CLASS_METHODS__DPDediscoReporterError
+ __OBJC_$_CLASS_METHODS__DPServerError
+ __OBJC_CLASS_RO_$__DPDatabaseRecorderError
+ __OBJC_CLASS_RO_$__DPDediscoReporterError
+ __OBJC_CLASS_RO_$__DPServerError
+ __OBJC_METACLASS_RO_$__DPDatabaseRecorderError
+ __OBJC_METACLASS_RO_$__DPDediscoReporterError
+ __OBJC_METACLASS_RO_$__DPServerError
+ ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.56
+ ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.56.cold.1
+ ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.52
+ ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.52.cold.1
+ ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.52.cold.2
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$missingEntitlementError
+ _objc_msgSend$reportCoreAnalyticsExecutionStage:error:key:count:
+ _objc_msgSend$reportCoreAnalyticsExecutionStage:error:key:count:isTelemetryAllowed:
+ _objc_msgSend$reportCoreAnalyticsExecutionStage:key:error:count:
+ _objc_msgSend$reportCoreAnalyticsExecutionStageWithCollector:executionStage:error:key:count:isTelemetryAllowed:
+ _objc_msgSend$telemetryTaskIdFromKey:
- +[_DPLHBitacoraLogger donateEventToBitacoraForKey:eventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:telemetryAllowed:].cold.1
- +[_DPServer shouldNotRecord:forKey:count:]
- +[_DPServer shouldNotRecord:forKey:count:].cold.1
- +[_DPServer shouldNotRecord:forKey:count:].cold.2
- -[_DPDatabaseRecorder donateRandomizationEventToBitacoraForKey:succeeded:errorCode:count:]
- -[_DPServer donateDonationReceivedEventToBitacoraForKey:succeeded:count:]
- -[_DPServer donateEventToCoreAnalytics:succeeded:count:]
- GCC_except_table0
- __DPCoreAnalyticsEvent_PhaseCount
- __DPCoreAnalyticsField_Counts
- __DPCoreAnalyticsField_Phase
- __DPCoreAnalyticsField_Status
- __DPCoreAnalyticsField_TaskName
- ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.33
- ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.33.cold.1
- ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.53
- ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.53.cold.1
- ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.53.cold.2
- ___74-[_DPDediscoReporter reportToDediscoRecords:forKey:keyProperties:storage:]_block_invoke.cold.1
- ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___getLBFEventManagerClass_block_invoke
- ___getLBFEventManagerClass_block_invoke.cold.1
- _getLBFEventManagerClass.softClass
- _objc_msgSend$addDprivacydEvent:identifiers:error:
- _objc_msgSend$bitacoraDprivacydEventWithEventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:
- _objc_msgSend$donateDonationReceivedEventToBitacoraForKey:succeeded:count:
- _objc_msgSend$donateEventToBitacoraForKey:eventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:telemetryAllowed:
- _objc_msgSend$donateEventToCoreAnalytics:succeeded:count:
- _objc_msgSend$donateRandomizationEventToBitacoraForKey:succeeded:errorCode:count:
- _objc_msgSend$keyName
- _objc_msgSend$numberWithInt:
- _objc_msgSend$trialIdentifiersForKey:
CStrings:
+ "%@: metadata is not provided, and method that should accept values without metadata is not supported"
+ "%@: metadata is not provided, and method=(%@) not supported"
+ "%@_%@_%@"
+ "Blacklisted values filtered"
+ "CK_FS_"
+ "Failed to create randomizer for recording bit values"
+ "Failed to create randomizer for recording bit vectors"
+ "Failed to create randomizer for recording float vectors"
+ "Failed to create randomizer for recording number vectors"
+ "Failed to create randomizer for recording numbers"
+ "Failed to create randomizer for recording strings"
+ "_DPDatabaseRecorderError"
+ "_DPDediscoReporterError"
+ "_DPServerError"
+ "com.apple.DifferentialPrivacy.DPServerError"
+ "com.apple.DifferentialPrivacy.DatabaseRecorderError"
+ "com.apple.DifferentialPrivacy.DediscoReporterError"
+ "com.apple.priml.DifferentialPrivacyReach"
+ "donationCount"
+ "errorCode"
+ "executionStage"
+ "fedstats"
+ "missingEntitlementError"
+ "pfl"
+ "reportCoreAnalyticsExecutionStage:error:key:count:"
+ "reportCoreAnalyticsExecutionStage:error:key:count:isTelemetryAllowed:"
+ "reportCoreAnalyticsExecutionStage:key:error:count:"
+ "reportCoreAnalyticsExecutionStageWithCollector:executionStage:error:key:count:isTelemetryAllowed:"
+ "taskId"
+ "telemetryTaskIdFromKey:"
+ "unknown"
+ "v48@0:8Q16@24@32Q40"
+ "v52@0:8Q16@24@32Q40B48"
+ "v60@0:8@16Q24@32@40Q48B56"
- "%@: metadata is not provided, but method that should accepts values without metadata is not supported"
- "%@: metadata is not provided, but method=(%@) not supported"
- "Could not create connection to %@ : error=%@"
- "Counts"
- "Failed to create randomizer"
- "Failed to donate to Bitacora for key %@ with error: %@"
- "LBFEventManager"
- "Malformed metadata provided"
- "Metadata methods not allowed"
- "Phase"
- "Privatization Failed"
- "Status"
- "TaskName"
- "XPCConnectionRejectedWithoutEntitlement"
- "addDprivacydEvent:identifiers:error:"
- "com.apple.DifferentialPrivacy.PhaseCount"
- "donateDonationReceivedEventToBitacoraForKey:succeeded:count:"
- "donateEventToCoreAnalytics:succeeded:count:"
- "donateRandomizationEventToBitacoraForKey:succeeded:errorCode:count:"
- "fedstats:com.apple.dedisco.telemetry"
- "numberWithInt:"
- "v32@0:8@16B24i28"
- "v36@0:8@16B24i28i32"

```
