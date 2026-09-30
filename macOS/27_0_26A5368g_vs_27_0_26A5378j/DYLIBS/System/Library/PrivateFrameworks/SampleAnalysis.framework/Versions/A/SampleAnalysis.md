## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis`

```diff

-  __TEXT.__text: 0x11d398
-  __TEXT.__objc_methlist: 0x5e04
+  __TEXT.__text: 0x11db84
+  __TEXT.__objc_methlist: 0x5e34
   __TEXT.__const: 0x328
   __TEXT.__dlopen_cstrs: 0x1ca
-  __TEXT.__cstring: 0x1994f
-  __TEXT.__oslogstring: 0xd0e2
-  __TEXT.__gcc_except_tab: 0x21878
-  __TEXT.__unwind_info: 0x3df8
+  __TEXT.__cstring: 0x19ae0
+  __TEXT.__oslogstring: 0xd1c4
+  __TEXT.__gcc_except_tab: 0x21950
+  __TEXT.__unwind_info: 0x3e08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x12d0
-  __DATA_CONST.__objc_classlist: 0x3a8
+  __DATA_CONST.__objc_classlist: 0x3b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2de0
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_selrefs: 0x2df0
+  __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x218
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x3f30
   __AUTH_CONST.__cfstring: 0xd060
-  __AUTH_CONST.__objc_const: 0xff78
+  __AUTH_CONST.__objc_const: 0x100f0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__auth_got: 0xcc0
+  __AUTH.__objc_data: 0x230
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xe08
+  __DATA.__objc_ivar: 0xe20
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x28
   __DATA.__common: 0x4b0
   __DATA_DIRTY.__objc_ivar: 0x10
-  __DATA_DIRTY.__objc_data: 0x2490
-  __DATA_DIRTY.__bss: 0x4e0
+  __DATA_DIRTY.__objc_data: 0x22b0
+  __DATA_DIRTY.__bss: 0x4f0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2994
-  Symbols:   7982
-  CStrings:  5941
+  Functions: 2998
+  Symbols:   8000
+  CStrings:  5948
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
Symbols:
+ -[SAMakeRunnableInfo .cxx_destruct]
+ -[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:]
+ -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]
+ -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]
+ -[SASampleStore backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:hasExclaveInKernelStack:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:threadExclavesInfo:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:lastMadeRunnableScheduledPriority:tidThatMadeRunnable:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]
+ -[SAThreadState scheduledPriorityWhenLastMadeRunnable]
+ -[SAThreadState tidThatMadeRunnable]
+ GCC_except_table122
+ GCC_except_table217
+ GCC_except_table296
+ GCC_except_table355
+ GCC_except_table361
+ GCC_except_table367
+ GCC_except_table368
+ GCC_except_table379
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table399
+ GCC_except_table400
+ OBJC_IVAR_$_SAKPerfState._mostRecentMakeRunnableInfoByTid
+ OBJC_IVAR_$_SAMakeRunnableInfo._scheduledPriority
+ OBJC_IVAR_$_SAMakeRunnableInfo._tidThatMadeRunnable
+ OBJC_IVAR_$_SAMakeRunnableInfo._timestamp
+ OBJC_IVAR_$_SAThreadState._scheduledPriorityWhenLastMadeRunnable
+ OBJC_IVAR_$_SAThreadState._tidThatMadeRunnable
+ _OBJC_CLASS_$_SAMakeRunnableInfo
+ _OBJC_METACLASS_$_SAMakeRunnableInfo
+ __149-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:]_block_invoke
+ __149-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:]_block_invoke_2
+ __303-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_SAMakeRunnableInfo
+ __OBJC_$_INSTANCE_VARIABLES_SAMakeRunnableInfo
+ __OBJC_CLASS_RO_$_SAMakeRunnableInfo
+ __OBJC_METACLASS_RO_$_SAMakeRunnableInfo
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_9
+ ___149-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:]_block_invoke
+ ___149-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:]_block_invoke_2
+ ___149-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:]_block_invoke_3
+ ___303-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
+ ___303-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_2
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_2
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_3
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_4
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_5
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_6
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_7
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_8
+ ___367-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_9
+ ___670-[SASampleStore(KPerfPrivate) backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:hasExclaveInKernelStack:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:threadExclavesInfo:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:lastMadeRunnableScheduledPriority:tidThatMadeRunnable:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]_block_invoke
+ ___block_descriptor_129_ea8_32s40s48s56s64s72s80r88r96r104r112r_e5_v8?0l
+ ___block_descriptor_282_ea8_32s40s48s56s64s72s80s88s96s104s112s120s128s136r144r152r160r168r176r184r192r200r_e30_v32?0"SAThreadState"8Q16^B24l
+ ___copy_helper_block_ea8_32s40s48s56s64s72s80r88r96r104r112r
+ ___destroy_helper_block_ea8_32s40s48s56s64s72s80r88r96r104r112r
+ _objc_msgSend$scheduledPriorityWhenLastMadeRunnable
+ _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:kperfState:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:.next_fake_unique_pid
- -[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]
- -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]
- -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]
- -[SASampleStore backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:hasExclaveInKernelStack:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:threadExclavesInfo:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]
- GCC_except_table153
- GCC_except_table214
- GCC_except_table215
- GCC_except_table348
- GCC_except_table351
- GCC_except_table357
- GCC_except_table369
- GCC_except_table371
- GCC_except_table378
- GCC_except_table383
- GCC_except_table384
- GCC_except_table385
- GCC_except_table386
- GCC_except_table391
- GCC_except_table392
- __138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke
- __138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_2
- __292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
- ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke
- ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_2
- ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_3
- ___292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
- ___292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_2
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_2
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_3
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_4
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_5
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_6
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_7
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_8
- ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_9
- ___616-[SASampleStore(KPerfPrivate) backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:hasExclaveInKernelStack:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:threadExclavesInfo:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]_block_invoke
- ___block_descriptor_121_ea8_32s40s48s56s64s72r80r88r96r104r_e5_v8?0l
- ___block_descriptor_270_ea8_32s40s48s56s64s72s80s88s96s104s112s120s128s136r144r152r160r168r176r184r192r200r_e30_v32?0"SAThreadState"8Q16^B24l
- ___copy_helper_block_ea8_32s40s48s56s64s72r80r88r96r104r
- ___destroy_helper_block_ea8_32s40s48s56s64s72r80r88r96r104r
- _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:.next_fake_unique_pid
CStrings:
+ "%'llu Thread 0x%llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s pri %d by tid 0x%llx) backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu Thread 0x%llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s pri %d by tid 0x%llx) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%s: after serializing (with %lu vmRangeLocks), ended with length %ld, should be %lu"
+ "((void*)(additions + 1)) - ((void*)serializedThreadState) == (long)[self sizeInBytesForSerializedVersion]"
+ "bufferLength %lu < serialized SAThreadState v13 struct %lu"
+ "bufferLength %lu < serialized SAThreadState v14 struct plus %u vm range locks %llu"
+ "bufferLength >= sizeofV14"
- "%'llu Thread 0x%llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s) backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu Thread 0x%llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "Ws"

```
