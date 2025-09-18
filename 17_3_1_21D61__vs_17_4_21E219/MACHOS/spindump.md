## spindump

> `/usr/sbin/spindump`

```diff

-341.1.0.0.0
-  __TEXT.__text: 0x8a274
-  __TEXT.__auth_stubs: 0x1210
-  __TEXT.__objc_stubs: 0x2dc0
-  __TEXT.__objc_methlist: 0x89c
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0x118aa
-  __TEXT.__oslogstring: 0x1fe6b
-  __TEXT.__objc_classname: 0xc9
-  __TEXT.__gcc_except_tab: 0x1510
-  __TEXT.__objc_methname: 0x31c7
-  __TEXT.__objc_methtype: 0x483
-  __TEXT.__unwind_info: 0xa64
-  __DATA_CONST.__auth_got: 0x918
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x10c0
-  __DATA_CONST.__cfstring: 0x7e00
-  __DATA_CONST.__objc_classlist: 0x58
+357.0.0.0.0
+  __TEXT.__text: 0x8d700
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_stubs: 0x3bc0
+  __TEXT.__objc_methlist: 0x9f4
+  __TEXT.__const: 0xb8
+  __TEXT.__cstring: 0x116b0
+  __TEXT.__oslogstring: 0x1f509
+  __TEXT.__objc_classname: 0xe5
+  __TEXT.__gcc_except_tab: 0x1a34
+  __TEXT.__objc_methname: 0x3f1f
+  __TEXT.__objc_methtype: 0x52a
+  __TEXT.__unwind_info: 0xa9c
+  __DATA_CONST.__auth_got: 0x900
+  __DATA_CONST.__got: 0x100
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x11b8
+  __DATA_CONST.__cfstring: 0x7f00
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1928
-  __DATA.__objc_selrefs: 0xcd0
-  __DATA.__objc_classrefs: 0x130
-  __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x1d4
-  __DATA.__objc_data: 0x370
+  __DATA_CONST.__objc_classrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x1d68
+  __DATA.__objc_selrefs: 0x1048
+  __DATA.__objc_ivar: 0x214
+  __DATA.__objc_data: 0x410
   __DATA.__data: 0x18
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x7d0
+  __DATA.__bss: 0x7c0
   __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FF01B15E-4163-3E60-A86E-EF4F598D0854
-  Functions: 1684
-  Symbols:   377
-  CStrings:  4826
+  UUID: 363926B3-64D8-36B8-B7EE-954D58588CEE
+  Functions: 1690
+  Symbols:   361
+  CStrings:  5000
 
Symbols:
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDecimalNumber
+ _OBJC_CLASS_$_WRWorkflowEventTracker
+ _WRErrorDomain
+ _WRSanitizeForCA
+ ___exp10
+ _objc_release_x27
+ _objc_retain_x19
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x7
- _OBJC_CLASS_$_NSJSONSerialization
- _TSPDumpOptions_ReasonString
- _WRWorkflowEndMachContTimeNSKey
- _WRWorkflowEndThreadIDKey
- _WRWorkflowNameKey
- _WRWorkflowSignpostDurationSecondsKey
- _WRWorkflowSignpostIntervalBeginMachContTimeNSKey
- _WRWorkflowSignpostIntervalBeginThreadIDKey
- _WRWorkflowSignpostIntervalEndMachContTimeNSKey
- _WRWorkflowSignpostIntervalEndThreadIDKey
- _WRWorkflowSignpostIntervalsListKey
- _WRWorkflowSignpostListKey
- _WRWorkflowSignpostNameKey
- _WRWorkflowSignpostThresholdDurationSecondsKey
- _WRWorkflowStartMachContTimeNSKey
- _WRWorkflowStartThreadIDKey
- _WRWorkflowThresholdDurationSecondsKey
- _ktrace_chunk_map_data
- _ktrace_chunk_size
- _ktrace_chunk_tag
- _ktrace_chunk_unmap_data
- _ktrace_chunk_version_major
- _ktrace_config_create
- _ktrace_config_destroy
- _ktrace_config_get_reason
- _ktrace_file_close
- _ktrace_file_iterate
- _ktrace_file_open
- _tailspin_currently_running
CStrings:
+ "\n\n"
+ " (fatal)"
+ "$"
+ "%@, %@.%@.%@, %@"
+ "%@-%@"
+ "%llu allocated, exceeding limit of %llu%@"
+ "%s [%d]: %s: Unable to set target dispatch queue"
+ "%s [%d]: %s: Unable to set target thread"
+ "%s [%d]: file descriptor exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "%s [%d]: kqworkloop exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "%s [%d]: port exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "%s: No thread nor dispatch queue"
+ "%s: TidToPidDictPromise called with no sample store"
+ "%s: Unable to set target dispatch queue"
+ "%s: Unable to set target thread"
+ "%{public}s [%d]: file descriptor exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "%{public}s [%d]: kqworkloop exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "%{public}s [%d]: port exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "-BS"
+ "-[SPWRReport initWithReportReason:reportedSignpostTracker:task:timeRange:thread:dispatchQueue:]"
+ "-bulkSymbolication"
+ "-forceOneBasedTimeIndexes"
+ "/var/mobile/stackshots."
+ "<entire workflow>"
+ "@\"SADispatchQueue\""
+ "@\"SASampleStore\"8@?0"
+ "@\"SATask\""
+ "@\"SAThread\""
+ "@\"SPWRReportReason\""
+ "@\"WRDiagnostic\""
+ "@\"WRSignpostTracker\""
+ "@\"WRWorkflowEventTracker\""
+ "@40@0:8@16@24@32"
+ "@64@0:8@16@24@32@40@48@56"
+ "Both -dsymForUUID and -noSymbolicate provided"
+ "Both -noBulkSymbolication and -bulkSymbolication provided"
+ "DPFailure"
+ "DoWorkflowResponsivenessDelay_block_invoke"
+ "Forcing one-based time indexes"
+ "GenerateWorkflowResponsivenessReport"
+ "Process killed"
+ "SPWRReport"
+ "SPWRReportReason"
+ "Submit resource reports cpu:%d io:%d due to suppression:%d"
+ "T@\"SADispatchQueue\",R,V_dispatchQueue"
+ "T@\"SATask\",R,V_task"
+ "T@\"SAThread\",R,V_thread"
+ "T@\"SATimeRange\",R,V_timeRange"
+ "T@\"SPWRReportReason\",R,V_reportReason"
+ "T@\"WRDiagnostic\",R,V_diagnostic"
+ "T@\"WRSignpostTracker\",R,V_reportedSignpostTracker"
+ "T@\"WRSignpostTracker\",R,V_signpostTracker"
+ "T@\"WRWorkflowEventTracker\",R,V_workflowTracker"
+ "TB,V_workflowEventTimedOut"
+ "TQ,V_signpostCount"
+ "Td,V_signpostDurationSingle"
+ "Td,V_signpostDurationSum"
+ "Td,V_signpostDurationUnion"
+ "Td,V_workflowDuration"
+ "Td,V_workflowDurationOmittingNetworkBoundIntervals"
+ "Unable to encode workflow event tracked into a string: %@"
+ "Unable to format: %s [%d]: %s: Unable to set target dispatch queue"
+ "Unable to format: %s [%d]: %s: Unable to set target thread"
+ "Unable to format: %s [%d]: file descriptor exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Unable to format: %s [%d]: kqworkloop exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Unable to format: %s [%d]: port exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Unable to format: %s: No thread nor dispatch queue"
+ "Unable to format: %s: TidToPidDictPromise called with no sample store"
+ "Unable to format: %s: Unable to set target dispatch queue"
+ "Unable to format: %s: Unable to set target thread"
+ "Unable to format: Both -dsymForUUID and -noSymbolicate provided"
+ "Unable to format: Both -noBulkSymbolication and -bulkSymbolication provided"
+ "Unable to format: Forcing one-based time indexes"
+ "Unable to format: Submit resource reports cpu:%d io:%d due to suppression:%d"
+ "Unable to format: Unable to encode workflow event tracked into a string: %@"
+ "Unable to format: UseDsymForUUID:%d"
+ "Unable to format: Using BulkSymbolication"
+ "Unable to format: WR: %@ generating overall workflow report for %@ [%d]"
+ "Unable to format: WR: %@ generating report for %@ due to %@ for %@ [%d]"
+ "Unable to format: WR: %@ generating report for %@ due to overall workflow for %@ [%d]"
+ "Unable to format: WR: %@: %@: %@ -> %@, conflicts with existing entry"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports dispatch queue %@, but %@ [%d] has no such dispatch queue"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports dispatch queue %@, but regex failed to compile: %@"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports main thread, but %@ [%d] has no main thread"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports this dispatch queue, but neither start %llu@%@ nor end %llu@%@ are on a dispatch queue"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports this dispatch queue, but signpost starts on %@ and ends on %@, neither at the exact right time, so not reporting"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports this dispatch queue, but signpost starts on %@ and ends on %@, so not reporting"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports this dispatch queue, signpost starts on %@ and ends on %@, and end is at the exact time, so using that"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports this dispatch queue, signpost starts on %@ and ends on %@, and start is at the exact time, so using that"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports this thread, but signpost starts on 0x%llx and ends on 0x%llx"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports thread %@, but %@ [%d] has no thread with that name during the interval %@ - %@"
+ "Unable to format: WR: %@: %@: diagnostic %@ reports thread %@, but regex failed to compile: %@"
+ "Unable to format: WR: %@: %@: diagnostic %@: %@ [%d] has no thread 0x%llx, cannot generate report"
+ "Unable to format: WR: %@: %@: diagnostic %@: Reporting spindump for this signpost due to %@, but no intervals to report"
+ "Unable to format: WR: %@: %@: diagnostic %@: Reporting spindump for this signpost due to count threshold, but no intervals to report"
+ "Unable to format: WR: %@: %@: diagnostic %@: Reporting spindump for this signpost due to overall workflow, but no intervals to report"
+ "Unable to format: WR: %@: %@: diagnostic %@: Unable to find task with thread 0x%llx at %llu, cannot generate report"
+ "Unable to format: WR: %@: DRShouldGatherLog return false, not submitting tailspin"
+ "Unable to format: WR: %@: No workflow event end"
+ "Unable to format: WR: %@: No workflow event start"
+ "Unable to format: WR: %@: Not generating any spindump reports, unable to create sample store for %s: %@\n"
+ "Unable to format: WR: %@: Received tailspin path %s"
+ "Unable to format: WR: %@: Unable to compare timesamps with tailspin data (%@)"
+ "Unable to format: WR: %@: WARNING trying to create sample store from %s: %@\n"
+ "Unable to format: WR: %@: Workflow event has error %@, not considering for diagnostics"
+ "Unable to format: WR: %@: Workflow event has error %@, still considering for diagnostics"
+ "Unable to format: WR: %@: Workflow event has invalid duration %.3f"
+ "Unable to format: WR: %@: error in DRShouldGatherLog call: %@"
+ "Unable to format: WR: %@: error trying to provide tailspin to Diagnostic Pipeline: %@"
+ "Unable to format: WR: %@: generating %lu spindump reports"
+ "Unable to format: WR: %@: no spindump reports to generate"
+ "Unable to format: WR: %@: submitted tailspin to Diagnostic Pipeline"
+ "Unable to format: WR: %@: submitting tailspin to Diagnostic Pipeline"
+ "Unable to format: WR: Unable to decode workflow event tracker: %@"
+ "Unable to format: WR: WorkflowResponsivness unavailable, not generating spindump report(s) for %s"
+ "Unable to format: WR: have %lu reports, but no sampleStore"
+ "Unable to format: file descriptor exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Unable to format: kqworkloop exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Unable to format: port exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "Use spindump -i to generate textual report\n\n"
+ "UseDsymForUUID:%d"
+ "Using BulkSymbolication"
+ "WR: %@ generating overall workflow report for %@ [%d]"
+ "WR: %@ generating report for %@ due to %@ for %@ [%d]"
+ "WR: %@ generating report for %@ due to overall workflow for %@ [%d]"
+ "WR: %@: %@: %@ -> %@, conflicts with existing entry"
+ "WR: %@: %@: diagnostic %@ reports dispatch queue %@, but %@ [%d] has no such dispatch queue"
+ "WR: %@: %@: diagnostic %@ reports dispatch queue %@, but regex failed to compile: %@"
+ "WR: %@: %@: diagnostic %@ reports main thread, but %@ [%d] has no main thread"
+ "WR: %@: %@: diagnostic %@ reports this dispatch queue, but neither start %llu@%@ nor end %llu@%@ are on a dispatch queue"
+ "WR: %@: %@: diagnostic %@ reports this dispatch queue, but signpost starts on %@ and ends on %@, neither at the exact right time, so not reporting"
+ "WR: %@: %@: diagnostic %@ reports this dispatch queue, but signpost starts on %@ and ends on %@, so not reporting"
+ "WR: %@: %@: diagnostic %@ reports this dispatch queue, signpost starts on %@ and ends on %@, and end is at the exact time, so using that"
+ "WR: %@: %@: diagnostic %@ reports this dispatch queue, signpost starts on %@ and ends on %@, and start is at the exact time, so using that"
+ "WR: %@: %@: diagnostic %@ reports this thread, but signpost starts on 0x%llx and ends on 0x%llx"
+ "WR: %@: %@: diagnostic %@ reports thread %@, but %@ [%d] has no thread with that name during the interval %@ - %@"
+ "WR: %@: %@: diagnostic %@ reports thread %@, but regex failed to compile: %@"
+ "WR: %@: %@: diagnostic %@: %@ [%d] has no thread 0x%llx, cannot generate report"
+ "WR: %@: %@: diagnostic %@: Reporting spindump for this signpost due to %@, but no intervals to report"
+ "WR: %@: %@: diagnostic %@: Reporting spindump for this signpost due to count threshold, but no intervals to report"
+ "WR: %@: %@: diagnostic %@: Reporting spindump for this signpost due to overall workflow, but no intervals to report"
+ "WR: %@: %@: diagnostic %@: Unable to find task with thread 0x%llx at %llu, cannot generate report"
+ "WR: %@: DRShouldGatherLog return false, not submitting tailspin"
+ "WR: %@: No workflow event end"
+ "WR: %@: No workflow event start"
+ "WR: %@: Not generating any spindump reports, unable to create sample store for %s: %@\n"
+ "WR: %@: Received tailspin path %s"
+ "WR: %@: Unable to compare timesamps with tailspin data (%@)"
+ "WR: %@: Unable to compare timesamps with tailspin data (%{public}@)"
+ "WR: %@: WARNING trying to create sample store from %s: %@\n"
+ "WR: %@: Workflow event has error %@, not considering for diagnostics"
+ "WR: %@: Workflow event has error %@, still considering for diagnostics"
+ "WR: %@: Workflow event has invalid duration %.3f"
+ "WR: %@: error in DRShouldGatherLog call: %@"
+ "WR: %@: error trying to provide tailspin to Diagnostic Pipeline: %@"
+ "WR: %@: generating %lu spindump reports"
+ "WR: %@: no spindump reports to generate"
+ "WR: %@: submitted tailspin to Diagnostic Pipeline"
+ "WR: %@: submitting tailspin to Diagnostic Pipeline"
+ "WR: Unable to decode workflow event tracker: %@"
+ "WR: WorkflowResponsivness unavailable, not generating spindump report(s) for %s"
+ "WR: have %lu reports, but no sampleStore"
+ "Workflow:%{signpost.telemetry:string1,public}@ error:%{signpost.telemetry:string2,public}@ contextDictionarySize:%{signpost.telemetry:number1,public}lu enableTelemetry=YES "
+ "^"
+ "_diagnostic"
+ "_dispatchQueue"
+ "_reportReason"
+ "_reportedSignpostTracker"
+ "_signpostCount"
+ "_signpostDurationSingle"
+ "_signpostDurationSum"
+ "_signpostDurationUnion"
+ "_signpostTracker"
+ "_task"
+ "_thread"
+ "_timeRange"
+ "_workflowDuration"
+ "_workflowDurationOmittingNetworkBoundIntervals"
+ "_workflowEventTimedOut"
+ "_workflowTracker"
+ "allKeys"
+ "allSignpostTrackers"
+ "category"
+ "code"
+ "dataWithPropertyList:format:options:error:"
+ "decimalNumberWithMantissa:exponent:isNegative:"
+ "deltaSecondsTo:timeDomainPriorityList:timeDomainUsed:"
+ "diagnostic"
+ "diagnostics"
+ "dispatchQueue"
+ "dispatchQueueLabel"
+ "dispatchQueues"
+ "distributorID"
+ "distributor_id"
+ "domain"
+ "encodedStringWithError:"
+ "end"
+ "endTimestamp"
+ "enumerateTasks:"
+ "enumerateThreadStatesBetweenStartTime:startSampleIndex:endTime:endSampleIndex:reverseOrder:block:"
+ "env_%@"
+ "environment"
+ "error"
+ "eventEnd"
+ "eventStart"
+ "exceededThresholds"
+ "file descriptor exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "firstThreadStateOnOrAfterTime:sampleIndex:"
+ "ge:"
+ "hasAnySpindumpReports"
+ "hasSuffix:"
+ "hasTriggerThresholdCount"
+ "hasTriggerThresholdDurationSingle"
+ "hasTriggerThresholdDurationSum"
+ "hasTriggerThresholdDurationUnion"
+ "identifier"
+ "incompleteIntervalStarts"
+ "individuationFieldName"
+ "individuationIdentifier"
+ "initWithReportReason:reportedSignpostTracker:task:timeRange:thread:dispatchQueue:"
+ "initWithTailspin:error:"
+ "initWithWorkflowTracker:signpostTracker:diagnostic:"
+ "intervals"
+ "kqworkloop exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "lastThreadStateOnOrBeforeTime:sampleIndex:"
+ "le:"
+ "lt:"
+ "machContTimeNs"
+ "mainThread"
+ "maxS"
+ "maximumEventDuration"
+ "monitor-WorkflowResponsiveness.m"
+ "nonNetworkS"
+ "num"
+ "numIncomplete"
+ "numberOfMatchesInString:options:range:"
+ "numberWithInteger:"
+ "overall"
+ "port exhaustion: deallocating fatal port, allowing process to exit due to fatal resource exhaustion"
+ "reportOmittingNetworkBoundIntervals"
+ "reportOtherSignpostWithName"
+ "reportProcessesWithName"
+ "reportReason"
+ "reportSpindumpForDispatchQueueWithLabel"
+ "reportSpindumpForMainThread"
+ "reportSpindumpForThisDispatchQueue"
+ "reportSpindumpForThisThread"
+ "reportSpindumpForThreadWithName"
+ "report_type == DID_SYSTEM_STATS || report_type == DID_SYSTEM_STATS_IO || report_type == DID_MANUAL_MICROSTACKSHOTS || report_type == DID_MANUAL_MICROSTACKSHOTS_IO || report_type == DID_CPU_RESOURCE || report_type == DID_DISK_WRITES_RESOURCE"
+ "reportedSignpostTracker"
+ "sampleStore.targetDispatchQueueId == report.dispatchQueue.identifier"
+ "setObject:atIndexedSubscript:"
+ "setSignpostCount:"
+ "setSignpostDurationSingle:"
+ "setSignpostDurationSum:"
+ "setSignpostDurationUnion:"
+ "setTargetDispatchQueueId:"
+ "setTargetProcess:"
+ "setWorkflowDuration:"
+ "setWorkflowDurationOmittingNetworkBoundIntervals:"
+ "setWorkflowEventTimedOut:"
+ "setWrError:"
+ "setWrSignpostCategory:"
+ "setWrSignpostCount:"
+ "setWrSignpostCountThreshold:"
+ "setWrSignpostDurationSingle:"
+ "setWrSignpostDurationSingleThreshold:"
+ "setWrSignpostDurationSum:"
+ "setWrSignpostDurationSumThreshold:"
+ "setWrSignpostDurationUnion:"
+ "setWrSignpostDurationUnionThreshold:"
+ "setWrSignpostName:"
+ "setWrSignpostSubsystem:"
+ "setWrTriggeringSignpostCategory:"
+ "setWrTriggeringSignpostName:"
+ "setWrTriggeringSignpostSubsystem:"
+ "setWrWorkflowDuration:"
+ "setWrWorkflowDurationOmittingNetworkBoundIntervals:"
+ "setWrWorkflowDurationOmittingNetworkBoundIntervalsThreshold:"
+ "setWrWorkflowDurationThreshold:"
+ "setWrWorkflowName:"
+ "setWrWorkflowTimeoutDuration:"
+ "signpost"
+ "signpostCount"
+ "signpostDurationSingle"
+ "signpostDurationSum"
+ "signpostDurationUnion"
+ "signpostTracker"
+ "start"
+ "startTimestamp"
+ "stats"
+ "statsWithEventEndNs:"
+ "subsystem"
+ "sumS"
+ "targetDispatchQueueId"
+ "task"
+ "thread"
+ "thread || dispatchQueue"
+ "threadID"
+ "threadId"
+ "tidToPidDict"
+ "timeRange"
+ "triggerEventTimeout"
+ "triggerThresholdCount"
+ "triggerThresholdDurationSingle"
+ "triggerThresholdDurationSum"
+ "triggerThresholdDurationUnion"
+ "unionS"
+ "untrackedS"
+ "v16@?0@\"NSNumber\"8"
+ "v24@?0@\"SATask\"8^B16"
+ "v32@?0@\"NSNumber\"8@\"SADispatchQueue\"16^B24"
+ "v32@?0@\"NSNumber\"8@\"SAThread\"16^B24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v32@?0@\"SAThreadState\"8Q16^B24"
+ "workflowDiagnostics"
+ "workflowDuration"
+ "workflowDurationOmittingNetworkBoundIntervals"
+ "workflowEventTimedOut"
+ "workflowTracker"
+ "zero"
- "%@.wakeups_resource"
- "%llu allocated, exceeding limit of %llu"
- "%s [%d]: Deallocating fatal port for exhaustion report"
- "%s [%d]: wakeups resource: %lld wakeups over the last %.0f seconds with flags %#llx"
- "%s [%d]: wakeups resource: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "%s [%d]: wakeups resource: done reporting (%#llx)"
- "%s [%d]: wakeups resource: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "%s [%d]: wakeups resource: not monitoring due to conditions %#llx"
- "%s [%d]: wakeups resource: not monitoring due to suppression cookie file"
- "%s [%d]: wakeups resource: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "%{public}s [%d]: Deallocating fatal port for exhaustion report"
- "%{public}s [%d]: wakeups resource: %lld wakeups over the last %.0f seconds with flags %#llx"
- "%{public}s [%d]: wakeups resource: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "%{public}s [%d]: wakeups resource: done reporting (%#llx)"
- "%{public}s [%d]: wakeups resource: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "%{public}s [%d]: wakeups resource: not monitoring due to conditions %#llx"
- "%{public}s [%d]: wakeups resource: not monitoring due to suppression cookie file"
- "%{public}s [%d]: wakeups resource: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "/var/tmp/stackshots."
- "142"
- "B16@?0^{ktrace_chunk=}8"
- "BundleIdOverride=%{public, signpost.description:attribute}@ %{public, signpost.description:begin_time}llu cid=%{public,name=cid}llu pid=%{public,name=pid}u numWakeups=%{public,name=numWakeups}llu conditionsPreventingSubmission=%{public,name=conditionsPreventingSubmission}#llx otherConditions=%{public,name=otherConditions}#llx enableTelemetry=YES "
- "Could not open tailspin file %s for parsing reason string"
- "Deallocating fatal port for exhaustion report"
- "Error %@ deserializing JSON"
- "Error creating JSON data from reason string '%@'"
- "Error iterating over tailspin file %s: %d (%s)"
- "Error reporting wakeups resource: bad duration (%f)"
- "Error reporting wakeups resource: bad duration_limit (%f)"
- "Error reporting wakeups resource: no duration provided"
- "Error reporting wakeups resource: no duration_limit provided"
- "Error reporting wakeups resource: no endtime provided"
- "Error reporting wakeups resource: no num wakeups provided"
- "Error reporting wakeups resource: no pid provided"
- "Generating workflow responsiveness report for delay: %@, %@, [%@], threadID %llu, duration %.2f(s) > threshold %.2f(s)"
- "JSONObjectWithData:options:error:"
- "Ktrace/tailspin not available, unable to get reason dict for workflow responsiveness delay"
- "Mutiple intervals present for signpost %@, considering only the first interval"
- "No begin timestamp available for signpost %@, skipping spindump report"
- "No beginThreadID for signpost %@, duration %.2f(s) > threshold %.2f(s), skipping spindump report"
- "No bug type for fatal cpu wakeups reports, using non-fatal bug type"
- "No duration for signpost %@, though we have a threshold of %.2f, continuing..."
- "No end timestamp available for signpost %@, skipping spindump report"
- "No endThreadID for signpost %@, duration %.2f(s) > threshold %.2f(s), skipping spindump report"
- "No name for signpost, continuing..."
- "No reason string in tailspin files %s"
- "No signposts present in tailspin reason dictionary, not generating any spindump report(s)"
- "No threadID/interval info available for signpost %@, skipping spindump report, continuing..."
- "No timestamps in sample store from file %s, not generating overall workflow spindump report"
- "No timestamps in sample store from file %s, not generating signpost spindump report"
- "No workflow end threadID present in reason dictionary from file %s, not generating overall workflow spindump report"
- "No workflow end timestamp present in reason dictionary from file %s, not generating overall workflow spindump report"
- "No workflow name present in reason dictionary from file %s, not generating any spindump report(s)"
- "No workflow start threadID present in reason dictionary from file %s, not generating overall workflow spindump report"
- "No workflow start timestamp present in reason dictionary from file %s, not generating overall workflow spindump report"
- "No workflow threshold duration present in reason dictionary from file %s, not generating overall workflow spindump report"
- "Not generating any spindump reports, unable to create sample store for %s: %@\n"
- "NumWakeups"
- "Received tailspin path %s for Workflow Responsiveness Delay %@"
- "Submit resource reports cpu:%d wakeups:%d io:%d due to suppression:%d"
- "Unable to format: %s [%d]: Deallocating fatal port for exhaustion report"
- "Unable to format: %s [%d]: wakeups resource: %lld wakeups over the last %.0f seconds with flags %#llx"
- "Unable to format: %s [%d]: wakeups resource: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "Unable to format: %s [%d]: wakeups resource: done reporting (%#llx)"
- "Unable to format: %s [%d]: wakeups resource: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "Unable to format: %s [%d]: wakeups resource: not monitoring due to conditions %#llx"
- "Unable to format: %s [%d]: wakeups resource: not monitoring due to suppression cookie file"
- "Unable to format: %s [%d]: wakeups resource: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "Unable to format: Could not open tailspin file %s for parsing reason string"
- "Unable to format: Deallocating fatal port for exhaustion report"
- "Unable to format: Error %@ deserializing JSON"
- "Unable to format: Error creating JSON data from reason string '%@'"
- "Unable to format: Error iterating over tailspin file %s: %d (%s)"
- "Unable to format: Error reporting wakeups resource: bad duration (%f)"
- "Unable to format: Error reporting wakeups resource: bad duration_limit (%f)"
- "Unable to format: Error reporting wakeups resource: no duration provided"
- "Unable to format: Error reporting wakeups resource: no duration_limit provided"
- "Unable to format: Error reporting wakeups resource: no endtime provided"
- "Unable to format: Error reporting wakeups resource: no num wakeups provided"
- "Unable to format: Error reporting wakeups resource: no pid provided"
- "Unable to format: Generating workflow responsiveness report for delay: %@, %@, [%@], threadID %llu, duration %.2f(s) > threshold %.2f(s)"
- "Unable to format: Ktrace/tailspin not available, unable to get reason dict for workflow responsiveness delay"
- "Unable to format: Mutiple intervals present for signpost %@, considering only the first interval"
- "Unable to format: No begin timestamp available for signpost %@, skipping spindump report"
- "Unable to format: No beginThreadID for signpost %@, duration %.2f(s) > threshold %.2f(s), skipping spindump report"
- "Unable to format: No bug type for fatal cpu wakeups reports, using non-fatal bug type"
- "Unable to format: No duration for signpost %@, though we have a threshold of %.2f, continuing..."
- "Unable to format: No end timestamp available for signpost %@, skipping spindump report"
- "Unable to format: No endThreadID for signpost %@, duration %.2f(s) > threshold %.2f(s), skipping spindump report"
- "Unable to format: No name for signpost, continuing..."
- "Unable to format: No reason string in tailspin files %s"
- "Unable to format: No signposts present in tailspin reason dictionary, not generating any spindump report(s)"
- "Unable to format: No threadID/interval info available for signpost %@, skipping spindump report, continuing..."
- "Unable to format: No timestamps in sample store from file %s, not generating overall workflow spindump report"
- "Unable to format: No timestamps in sample store from file %s, not generating signpost spindump report"
- "Unable to format: No workflow end threadID present in reason dictionary from file %s, not generating overall workflow spindump report"
- "Unable to format: No workflow end timestamp present in reason dictionary from file %s, not generating overall workflow spindump report"
- "Unable to format: No workflow name present in reason dictionary from file %s, not generating any spindump report(s)"
- "Unable to format: No workflow start threadID present in reason dictionary from file %s, not generating overall workflow spindump report"
- "Unable to format: No workflow start timestamp present in reason dictionary from file %s, not generating overall workflow spindump report"
- "Unable to format: No workflow threshold duration present in reason dictionary from file %s, not generating overall workflow spindump report"
- "Unable to format: Not generating any spindump reports, unable to create sample store for %s: %@\n"
- "Unable to format: Received tailspin path %s for Workflow Responsiveness Delay %@"
- "Unable to format: Submit resource reports cpu:%d wakeups:%d io:%d due to suppression:%d"
- "Unable to format: Unable to read tailspin reason dictionary from file %s, not generating spindump report(s)"
- "Unable to format: WARNING trying to create sample store from %s: %@\n"
- "Unable to format: Workflow overall duration %.2f(s) did not exceed threshold %.2f(s) from file %s, not generating overall workflow spindump report"
- "Unable to format: Workflow startThreadID (%llu) != endThreadID(%llu) in reason dictionary from file %s, not generating overall workflow spindump report"
- "Unable to format: WorkflowResponsivness unavailable, not generating spindump report(s) for %s"
- "Unable to format: duration %.2f(s) < threshold %.2f(s) for signpost %@, skipping spindump report and continuing..."
- "Unable to format: startThreadID (%llu) != endThreadID(%llu) for signpost %@, skipping spindump report"
- "Unable to format: wakeups resource: %lld wakeups over the last %.0f seconds with flags %#llx"
- "Unable to format: wakeups resource: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "Unable to format: wakeups resource: done reporting (%#llx)"
- "Unable to format: wakeups resource: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "Unable to format: wakeups resource: not monitoring due to conditions %#llx"
- "Unable to format: wakeups resource: not monitoring due to suppression cookie file"
- "Unable to format: wakeups resource: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "Unable to format: workflow responsiveness %@: DRShouldGatherLog return false, not submitting tailspin"
- "Unable to format: workflow responsiveness %@: error in DRShouldGatherLog call: %@"
- "Unable to format: workflow responsiveness %@: error trying to provide tailspin to Diagnostic Pipeline: %@"
- "Unable to format: workflow responsiveness %@: submitted tailspin to Diagnostic Pipeline"
- "Unable to format: workflow responsiveness %@: submitting tailspin to Diagnostic Pipeline"
- "Unable to read tailspin reason dictionary from file %s, not generating spindump report(s)"
- "WARNING trying to create sample store from %s: %@\n"
- "Wakeups resource for [%d]"
- "WakeupsResource"
- "WakeupsResourceTelemetry"
- "Workflow overall duration %.2f(s) did not exceed threshold %.2f(s) from file %s, not generating overall workflow spindump report"
- "Workflow startThreadID (%llu) != endThreadID(%llu) in reason dictionary from file %s, not generating overall workflow spindump report"
- "WorkflowResponsivness unavailable, not generating spindump report(s) for %s"
- "com.apple.spindump.wakeupsresource"
- "dataUsingEncoding:"
- "duration %.2f(s) < threshold %.2f(s) for signpost %@, skipping spindump report and continuing..."
- "enableImmediateCleanupOfCSSymbolOwners"
- "nil"
- "propertyListWithData:options:format:error:"
- "report_type == DID_SYSTEM_STATS || report_type == DID_SYSTEM_STATS_IO || report_type == DID_MANUAL_MICROSTACKSHOTS || report_type == DID_MANUAL_MICROSTACKSHOTS_IO || report_type == DID_CPU_RESOURCE || report_type == DID_WAKEUPS_RESOURCE || report_type == DID_DISK_WRITES_RESOURCE"
- "setNumWakeups:"
- "setNumWakeupsLimit:"
- "setWakeupsDuration:"
- "setWakeupsLimitDuration:"
- "startThreadID (%llu) != endThreadID(%llu) for signpost %@, skipping spindump report"
- "starttime"
- "wakeups"
- "wakeups resource"
- "wakeups resource: %lld wakeups over the last %.0f seconds with flags %#llx"
- "wakeups resource: all microstackshots without errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "wakeups resource: done reporting (%#llx)"
- "wakeups resource: no microstackshots: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "wakeups resource: not monitoring due to conditions %#llx"
- "wakeups resource: not monitoring due to suppression cookie file"
- "wakeups resource: some microstackshots with errors: %llu out-of-order microstackshots, %llu microstackshots missing load infos, %llu bytes invalid"
- "wakeups-lite"
- "wakeups_limit"
- "workflow responsiveness %@: DRShouldGatherLog return false, not submitting tailspin"
- "workflow responsiveness %@: error in DRShouldGatherLog call: %@"
- "workflow responsiveness %@: error trying to provide tailspin to Diagnostic Pipeline: %@"
- "workflow responsiveness %@: submitted tailspin to Diagnostic Pipeline"
- "workflow responsiveness %@: submitting tailspin to Diagnostic Pipeline"

```
