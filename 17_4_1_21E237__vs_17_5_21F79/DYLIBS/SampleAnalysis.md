## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-347.0.1.0.0
-  __TEXT.__text: 0xcb34c
-  __TEXT.__auth_stubs: 0x1570
-  __TEXT.__objc_methlist: 0x4d54
-  __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x143f3
-  __TEXT.__oslogstring: 0xa20d
-  __TEXT.__gcc_except_tab: 0x655c
+347.3.0.0.0
+  __TEXT.__text: 0xd3364
+  __TEXT.__auth_stubs: 0x15a0
+  __TEXT.__objc_methlist: 0x505c
+  __TEXT.__const: 0x168
+  __TEXT.__cstring: 0x14e02
+  __TEXT.__oslogstring: 0xa658
+  __TEXT.__gcc_except_tab: 0x66bc
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x1dc0
-  __TEXT.__objc_classname: 0x910
-  __TEXT.__objc_methname: 0xbbe6
-  __TEXT.__objc_methtype: 0x1515
-  __TEXT.__objc_stubs: 0x6f40
+  __TEXT.__unwind_info: 0x1e94
+  __TEXT.__objc_classname: 0x9c7
+  __TEXT.__objc_methname: 0xbf3e
+  __TEXT.__objc_methtype: 0x164d
+  __TEXT.__objc_stubs: 0x70a0
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x30f8
-  __DATA_CONST.__objc_classlist: 0x350
+  __DATA_CONST.__const: 0x31b8
+  __DATA_CONST.__objc_classlist: 0x398
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xacb8
-  __DATA_CONST.__objc_selrefs: 0x2428
+  __DATA_CONST.__objc_const: 0xb4b8
+  __DATA_CONST.__objc_selrefs: 0x24a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x448
-  __DATA_CONST.__objc_superrefs: 0x208
-  __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__cfstring: 0xa3a0
-  __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__const: 0x620
-  __AUTH_CONST.__objc_intobj: 0x150
-  __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH_CONST.__auth_got: 0xad0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xad4
+  __DATA_CONST.__objc_classrefs: 0x490
+  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_arraydata: 0x80
+  __AUTH_CONST.__cfstring: 0xa6e0
+  __AUTH_CONST.__objc_const: 0x480
+  __AUTH_CONST.__const: 0x680
+  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__auth_got: 0xae8
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0xb40
   __DATA.__data: 0x5c4
   __DATA.__thread_vars: 0x48
   __DATA.__crash_info: 0x40
   __DATA.__thread_bss: 0x11
   __DATA.__common: 0x498
   __DATA.__bss: 0x38
-  __DATA_DIRTY.__const: 0x3e0
-  __DATA_DIRTY.__objc_const: 0x2be8
-  __DATA_DIRTY.__objc_ivar: 0x34
-  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA_DIRTY.__const: 0x380
+  __DATA_DIRTY.__objc_const: 0x2ba0
+  __DATA_DIRTY.__objc_ivar: 0x44
+  __DATA_DIRTY.__objc_data: 0x1f40
   __DATA_DIRTY.__bss: 0x410
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 236B250D-2090-3C91-A059-FE29AD02B278
-  Functions: 2468
-  Symbols:   8335
-  CStrings:  7103
+  UUID: 79E1B31E-6FB2-321A-A488-E56383C1283C
+  Functions: 2549
+  Symbols:   8601
+  CStrings:  7298
 
Symbols:
+ +[SABinaryLoadInfo binaryLoadInfoWithBinary:loadAddress:isInKernelAddressSpace:exclave:]
+ +[SABinaryLoadInfo binaryLoadInfoWithSegment:loadAddress:isInKernelAddressSpace:exclave:]
+ +[SABinaryLoadInfo loadInfosForSegmentsInBinary:binaryBaseAddress:isInKernelAddressSpace:exclave:]
+ +[SAExclave(Serialization) classDictionaryKey]
+ +[SAExclave(Serialization) newInstanceWithoutReferencesFromSerializedBuffer:bufferLength:]
+ +[SAExclaveCallstack(Serialization) classDictionaryKey]
+ +[SAExclaveCallstack(Serialization) newInstanceWithoutReferencesFromSerializedBuffer:bufferLength:]
+ +[SAThreadExclavesInfo(Serialization) classDictionaryKey]
+ +[SAThreadExclavesInfo(Serialization) newInstanceWithoutReferencesFromSerializedBuffer:bufferLength:]
+ -[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:]
+ -[SABinary symbolicateAllInstructionsWithOptions:pid:checkExclave:onlyDsym:]
+ -[SABinaryLoadInfo exclave]
+ -[SABinaryLoadInfoToDisplay .cxx_destruct]
+ -[SABinaryLoadInfoToDisplay debugDescription]
+ -[SABinaryLoadInfoToDisplay exclave]
+ -[SABinaryLoadInfoToDisplay highestOffset]
+ -[SABinaryLoadInfoToDisplay isInKernelAddressSpace]
+ -[SABinaryLoadInfoToDisplay isZerothAndOnlySegment]
+ -[SABinaryLoadInfoToDisplay setHighestOffset:]
+ -[SABinaryLoadInfoToDisplay setIsZerothAndOnlySegment:]
+ -[SAExclave .cxx_destruct]
+ -[SAExclave debugDescription]
+ -[SAExclave enumerateFrames:]
+ -[SAExclave fixupFrameInstructionsWithDataGatheringOptions:foundNewBinaryInfo:uuidsWithNewInstructions:]
+ -[SAExclave identifier]
+ -[SAExclave initWithKCData:name:textLayout:]
+ -[SAExclave loadInfos]
+ -[SAExclave matches:name:textLayout:]
+ -[SAExclave name]
+ -[SAExclave synthetic]
+ -[SAExclave unslid]
+ -[SAExclave(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:]
+ -[SAExclave(Serialization) addSelfToSerializationDictionary:]
+ -[SAExclave(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:]
+ -[SAExclave(Serialization) sizeInBytesForSerializedVersion]
+ -[SAExclaveBinaryLoadInfo .cxx_destruct]
+ -[SAExclaveBinaryLoadInfo exclave]
+ -[SAExclaveBinaryLoadInfo initWithBinary:segment:loadAddress:exclave:]
+ -[SAExclaveCallstack .cxx_destruct]
+ -[SAExclaveCallstack debugDescription]
+ -[SAExclaveCallstack initWithKCData:exclave:leafFrame:]
+ -[SAExclaveCallstack(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:]
+ -[SAExclaveCallstack(Serialization) addSelfToSerializationDictionary:]
+ -[SAExclaveCallstack(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:]
+ -[SAExclaveCallstack(Serialization) sizeInBytesForSerializedVersion]
+ -[SAExclaveFrame .cxx_destruct]
+ -[SAExclaveFrame exclave]
+ -[SAExclaveFrame initCopyingFrame:withParent:]
+ -[SAExclaveFrame initWithExclave:]
+ -[SAExclaveFrame isExclave]
+ -[SAExclaveFrame reset]
+ -[SAFrame _addChildFrame:]
+ -[SAFrame copyWithNewParent:]
+ -[SAFrame exclave]
+ -[SAFrame isExclave]
+ -[SAFrameIterator exclaveInsertionIndex]
+ -[SAFrameIterator setExclaveInsertionIndex:]
+ -[SAKCDataExclaveAddressSpace initWithInfo:name:]
+ -[SAKCDataExclaveCallstack .cxx_destruct]
+ -[SAKCDataExclaveCallstack initWithInfo:addresses:]
+ -[SAKCDataExclaveSCResult .cxx_destruct]
+ -[SAKCDataExclaveSCResult initWithInfo:callstacks:]
+ -[SAKCDataExclaveTextLayout .cxx_destruct]
+ -[SAKCDataExclaveTextLayout initWithInfo:textSegments:]
+ -[SAKCDataExclaveTextLayoutSegment initWithInfo:]
+ -[SASamplePrintOptions displayExclaveFrames]
+ -[SASamplePrintOptions setDisplayExclaveFrames:]
+ -[SASamplePrinter avoidOverlapInBinaryLoadInfos:onlyExclaves:inTask:]
+ -[SASamplePrinter displayedBinaryLoadInfoForBinary:segment:desiredLoadAddress:offsetIntoLoadInfo:isInKernelAddressSpace:exclave:binariesToDisplay:extraBinariesToDisplay:]
+ -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]
+ -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]
+ -[SASampleStore addKCDataThreadV4:threadV2:deltaThreadV3:deltaThreadV2:timestamp:sampleIndex:stack:threadExclavesInfo:threadName:dispatchQueueLabel:waitInfo:waitInfoPortLabelInfo:turnstileInfo:turnstileInfoPortLabelInfo:instructionCycles:task:kernelTask:taskIsSuspended:]
+ -[SASampleStore backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:threadExclavesInfo:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]
+ -[SASampleStore exclaves]
+ -[SASampleStore fixupAllFrames]
+ -[SASampleStore kPerfPETParsePastLastStackshot]
+ -[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]
+ -[SASampleStore setKPerfPETParsePastLastStackshot:]
+ -[SATask fixupFrameInstructionsWithDataGatheringOptions:mightBeAlive:foundNewBinaryInfo:uuidsWithNewInstructions:]
+ -[SAThreadExclavesInfo .cxx_destruct]
+ -[SAThreadExclavesInfo debugDescription]
+ -[SAThreadExclavesInfo initWithKCData:callstacks:]
+ -[SAThreadExclavesInfo matchesStack:]
+ -[SAThreadExclavesInfo(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:]
+ -[SAThreadExclavesInfo(Serialization) addSelfToSerializationDictionary:]
+ -[SAThreadExclavesInfo(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:]
+ -[SAThreadExclavesInfo(Serialization) sizeInBytesForSerializedVersion]
+ GCC_except_table101
+ GCC_except_table106
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table133
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table156
+ GCC_except_table168
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table180
+ GCC_except_table194
+ GCC_except_table198
+ GCC_except_table202
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table213
+ GCC_except_table214
+ GCC_except_table233
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table42
+ GCC_except_table452
+ GCC_except_table455
+ GCC_except_table458
+ GCC_except_table51
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table93
+ GCC_except_table95
+ _.str.464
+ _.str.684
+ _CSSymbolicatorCreateWithExclaveUUIDAndFlags
+ _CreateSymbolOwnerForExclaveUUID
+ _OBJC_CLASS_$_SABinaryLoadInfoToDisplay
+ _OBJC_CLASS_$_SAExclave
+ _OBJC_CLASS_$_SAExclaveBinaryLoadInfo
+ _OBJC_CLASS_$_SAExclaveCallstack
+ _OBJC_CLASS_$_SAExclaveFrame
+ _OBJC_CLASS_$_SAKCDataExclaveAddressSpace
+ _OBJC_CLASS_$_SAKCDataExclaveCallstack
+ _OBJC_CLASS_$_SAKCDataExclaveSCResult
+ _OBJC_CLASS_$_SAKCDataExclaveTextLayout
+ _OBJC_CLASS_$_SAKCDataExclaveTextLayoutSegment
+ _OBJC_CLASS_$_SAThreadExclavesInfo
+ _OBJC_IVAR_$_SAExclave._identifier
+ _OBJC_IVAR_$_SAExclave._loadInfos
+ _OBJC_IVAR_$_SAExclave._name
+ _OBJC_IVAR_$_SAExclave._rootFrames
+ _OBJC_IVAR_$_SAExclave._textlayout_flags
+ _OBJC_IVAR_$_SAExclaveBinaryLoadInfo._exclave
+ _OBJC_IVAR_$_SAExclaveCallstack._exclave
+ _OBJC_IVAR_$_SAExclaveCallstack._invocationID
+ _OBJC_IVAR_$_SAExclaveCallstack._leafFrame
+ _OBJC_IVAR_$_SAExclaveCallstack._threadNumericID
+ _OBJC_IVAR_$_SAExclaveFrame._exclave
+ _OBJC_IVAR_$_SAFrameIterator._exclaveFrame
+ _OBJC_IVAR_$_SAFrameIterator._exclaveInsertionIndex
+ _OBJC_IVAR_$_SAKCDataExclaveAddressSpace._exclave_addressspace_info
+ _OBJC_IVAR_$_SAKCDataExclaveAddressSpace._name
+ _OBJC_IVAR_$_SAKCDataExclaveCallstack._addresses
+ _OBJC_IVAR_$_SAKCDataExclaveCallstack._exclave_ipcstackentry_info
+ _OBJC_IVAR_$_SAKCDataExclaveSCResult._callstacks
+ _OBJC_IVAR_$_SAKCDataExclaveSCResult._exclave_scresult_info
+ _OBJC_IVAR_$_SAKCDataExclaveTextLayout._exclave_textlayout_info
+ _OBJC_IVAR_$_SAKCDataExclaveTextLayout._textSegments
+ _OBJC_IVAR_$_SAKCDataExclaveTextLayoutSegment._exclave_textlayout_segment
+ _OBJC_IVAR_$_SASamplePrintOptions._displayExclaveFrames
+ _OBJC_IVAR_$_SASampleStore._exclaves
+ _OBJC_IVAR_$_SASampleStore._kPerfPETParsePastLastStackshot
+ _OBJC_IVAR_$_SAThreadExclavesInfo._callstacks
+ _OBJC_IVAR_$_SAThreadExclavesInfo._flags
+ _OBJC_IVAR_$_SAThreadState._exclavesInfo
+ _OBJC_IVAR_$_SAUUIDToSymbolicate._isInExclave
+ _OBJC_METACLASS_$_SABinaryLoadInfoToDisplay
+ _OBJC_METACLASS_$_SAExclave
+ _OBJC_METACLASS_$_SAExclaveBinaryLoadInfo
+ _OBJC_METACLASS_$_SAExclaveCallstack
+ _OBJC_METACLASS_$_SAExclaveFrame
+ _OBJC_METACLASS_$_SAKCDataExclaveAddressSpace
+ _OBJC_METACLASS_$_SAKCDataExclaveCallstack
+ _OBJC_METACLASS_$_SAKCDataExclaveSCResult
+ _OBJC_METACLASS_$_SAKCDataExclaveTextLayout
+ _OBJC_METACLASS_$_SAKCDataExclaveTextLayoutSegment
+ _OBJC_METACLASS_$_SAThreadExclavesInfo
+ __OBJC_$_CLASS_METHODS_SAExclave(Serialization)
+ __OBJC_$_CLASS_METHODS_SAExclaveCallstack(Serialization)
+ __OBJC_$_CLASS_METHODS_SAThreadExclavesInfo(Serialization)
+ __OBJC_$_INSTANCE_METHODS_SABinaryLoadInfoToDisplay
+ __OBJC_$_INSTANCE_METHODS_SAExclave(Serialization)
+ __OBJC_$_INSTANCE_METHODS_SAExclaveBinaryLoadInfo
+ __OBJC_$_INSTANCE_METHODS_SAExclaveCallstack(Serialization)
+ __OBJC_$_INSTANCE_METHODS_SAExclaveFrame
+ __OBJC_$_INSTANCE_METHODS_SAKCDataExclaveCallstack
+ __OBJC_$_INSTANCE_METHODS_SAKCDataExclaveSCResult
+ __OBJC_$_INSTANCE_METHODS_SAKCDataExclaveTextLayout
+ __OBJC_$_INSTANCE_METHODS_SAThreadExclavesInfo(Serialization)
+ __OBJC_$_INSTANCE_VARIABLES_SABinaryLoadInfoToDisplay
+ __OBJC_$_INSTANCE_VARIABLES_SAExclave
+ __OBJC_$_INSTANCE_VARIABLES_SAExclaveBinaryLoadInfo
+ __OBJC_$_INSTANCE_VARIABLES_SAExclaveCallstack
+ __OBJC_$_INSTANCE_VARIABLES_SAExclaveFrame
+ __OBJC_$_INSTANCE_VARIABLES_SAKCDataExclaveAddressSpace
+ __OBJC_$_INSTANCE_VARIABLES_SAKCDataExclaveCallstack
+ __OBJC_$_INSTANCE_VARIABLES_SAKCDataExclaveSCResult
+ __OBJC_$_INSTANCE_VARIABLES_SAKCDataExclaveTextLayout
+ __OBJC_$_INSTANCE_VARIABLES_SAKCDataExclaveTextLayoutSegment
+ __OBJC_$_INSTANCE_VARIABLES_SAThreadExclavesInfo
+ __OBJC_$_PROP_LIST_SABinaryLoadInfoToDisplay
+ __OBJC_CLASS_PROTOCOLS_$_SAExclave(Serialization)
+ __OBJC_CLASS_PROTOCOLS_$_SAExclaveCallstack(Serialization)
+ __OBJC_CLASS_PROTOCOLS_$_SAThreadExclavesInfo(Serialization)
+ __OBJC_CLASS_RO_$_SABinaryLoadInfoToDisplay
+ __OBJC_CLASS_RO_$_SAExclave
+ __OBJC_CLASS_RO_$_SAExclaveBinaryLoadInfo
+ __OBJC_CLASS_RO_$_SAExclaveCallstack
+ __OBJC_CLASS_RO_$_SAExclaveFrame
+ __OBJC_CLASS_RO_$_SAKCDataExclaveAddressSpace
+ __OBJC_CLASS_RO_$_SAKCDataExclaveCallstack
+ __OBJC_CLASS_RO_$_SAKCDataExclaveSCResult
+ __OBJC_CLASS_RO_$_SAKCDataExclaveTextLayout
+ __OBJC_CLASS_RO_$_SAKCDataExclaveTextLayoutSegment
+ __OBJC_CLASS_RO_$_SAThreadExclavesInfo
+ __OBJC_METACLASS_RO_$_SABinaryLoadInfoToDisplay
+ __OBJC_METACLASS_RO_$_SAExclave
+ __OBJC_METACLASS_RO_$_SAExclaveBinaryLoadInfo
+ __OBJC_METACLASS_RO_$_SAExclaveCallstack
+ __OBJC_METACLASS_RO_$_SAExclaveFrame
+ __OBJC_METACLASS_RO_$_SAKCDataExclaveAddressSpace
+ __OBJC_METACLASS_RO_$_SAKCDataExclaveCallstack
+ __OBJC_METACLASS_RO_$_SAKCDataExclaveSCResult
+ __OBJC_METACLASS_RO_$_SAKCDataExclaveTextLayout
+ __OBJC_METACLASS_RO_$_SAKCDataExclaveTextLayoutSegment
+ __OBJC_METACLASS_RO_$_SAThreadExclavesInfo
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1210
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1214
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1217
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1211
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1218
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1572
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1574
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.247
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.249
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.250
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1990
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1998
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2003
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2019
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1950
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1959
+ ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke
+ ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.296
+ ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.306
+ ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.310
+ ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke_2
+ ___28-[SASampleStore postprocess]_block_invoke.165
+ ___28-[SASampleStore postprocess]_block_invoke_2.166
+ ___28-[SASampleStore postprocess]_block_invoke_3.169
+ ___28-[SASampleStore symbolicate]_block_invoke.377
+ ___29-[SASamplePrinter preprocess]_block_invoke_2
+ ___29-[SASamplePrinter preprocess]_block_invoke_3
+ ___30-[SASamplePrinter printHeader]_block_invoke.1056
+ ___30-[SASamplePrinter printHeader]_block_invoke.1087
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1057
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1100
+ ___31+[SASharedCache addDSCSymData:]_block_invoke.493
+ ___31-[SASampleStore fixupAllFrames]_block_invoke
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_2
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_3
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_4
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_5
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_6
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_7
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_8
+ ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_9
+ ___37-[SASamplePrinter checkForBadOptions]_block_invoke.337
+ ___38-[SASamplePrinter printTasksByProcess]_block_invoke.1154
+ ___41-[SASamplePrinter printTasksByExecutable]_block_invoke.1161
+ ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.484
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1622
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.1623
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.1624
+ ___59-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:]_block_invoke
+ ___59-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:]_block_invoke.137
+ ___59-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:]_block_invoke.139
+ ___59-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:]_block_invoke_2
+ ___592-[SASampleStore(KPerfPrivate) backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:threadExclavesInfo:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]_block_invoke
+ ___65-[SASampleStore parseKCDataExclavesIPCStackContainer:callstacks:]_block_invoke
+ ___68-[SASampleStore parseKCDataExclavesTextLayoutContainer:textLayouts:]_block_invoke
+ ___76-[SABinary symbolicateAllInstructionsWithOptions:pid:checkExclave:onlyDsym:]_block_invoke
+ ___77-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]_block_invoke
+ ___77-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]_block_invoke.332
+ ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.350
+ ___ReadAheadTaskLevelInfo_block_invoke.1609
+ ___ReadAheadTaskLevelInfo_block_invoke.1614
+ ___ReadAheadTaskLevelInfo_block_invoke.1617
+ ___SAKCDataReadAheadDonatingUniquePids_block_invoke
+ ___SAKCDataReadAheadJetsamCoalitionInfo_block_invoke
+ ___SAKCDataReadAheadJetsamCoalitionInfo_block_invoke_2
+ ___block_descriptor_147_ea8_32s40s48s56r64r72r80r_e28_v32?0"SATaskState"8Q16^B24ls32l8s40l8r56l8r64l8r72l8r80l8s48l8
+ ___block_descriptor_277_e8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
+ ___block_descriptor_32_e65_q24?0"SABinaryLoadInfoToDisplay"8"SABinaryLoadInfoToDisplay"16l
+ ___block_descriptor_40_e21_B24?0"SAFrame"8^B16l
+ ___block_descriptor_40_e8_32s_e13_v20?0I8r^Q12ls32l8
+ ___block_descriptor_40_e8_32s_e47_v20?0I8r^{exclave_textlayout_segment=[16C]Q}12ls32l8
+ ___block_descriptor_45_e8_32bs_e24_v32?0"SAFrame"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40s_e24_v32?0"SAFrame"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e27_v28?0"SABinary"8i16B20B24ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e20_v24?0"SATask"8^B16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e24_v32?0"SAFrame"8Q16^B24ls40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls40l8s32l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1060
+ ___block_literal_global.1503
+ ___block_literal_global.154
+ ___block_literal_global.1546
+ ___block_literal_global.1549
+ ___block_literal_global.1584
+ ___block_literal_global.1597
+ ___block_literal_global.1635
+ ___block_literal_global.1637
+ ___block_literal_global.178
+ ___block_literal_global.1947
+ ___block_literal_global.1962
+ ___block_literal_global.1983
+ ___block_literal_global.1992
+ ___block_literal_global.203
+ ___block_literal_global.205
+ ___block_literal_global.2050
+ ___block_literal_global.224
+ ___block_literal_global.2284
+ ___block_literal_global.291
+ ___block_literal_global.298
+ ___block_literal_global.353
+ ___block_literal_global.355
+ ___block_literal_global.380
+ ___block_literal_global.382
+ ___block_literal_global.386
+ ___block_literal_global.388
+ ___block_literal_global.396
+ ___block_literal_global.412
+ ___block_literal_global.414
+ ___block_literal_global.415
+ ___block_literal_global.429
+ ___block_literal_global.433
+ ___block_literal_global.455
+ ___block_literal_global.457
+ ___block_literal_global.459
+ ___block_literal_global.471
+ ___block_literal_global.483
+ ___block_literal_global.760
+ __parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:.next_fake_unique_pid
+ __unnamed_array_storage.1638
+ __unnamed_array_storage.2072
+ __unnamed_array_storage.2078
+ __unnamed_array_storage.2084
+ __unnamed_array_storage.435
+ __unnamed_array_storage.441
+ _objc_msgSend$copyWithNewParent:
+ _objc_msgSend$displayExclaveFrames
+ _objc_msgSend$exclave
+ _objc_msgSend$exclaves
+ _objc_msgSend$isExclave
+ _objc_msgSend$isZerothAndOnlySegment
+ _objc_msgSend$kPerfPETParsePastLastStackshot
+ _objc_msgSend$loadInfos
+ _objc_msgSend$reset
+ _objc_msgSend$setDisplayExclaveFrames:
+ _objc_msgSend$setExclaveInsertionIndex:
+ _objc_msgSend$setIsZerothAndOnlySegment:
+ _objc_release_x10
+ _objc_release_x4
- +[SABinaryLoadInfo binaryLoadInfoWithBinary:loadAddress:isInKernelAddressSpace:]
- +[SABinaryLoadInfo binaryLoadInfoWithSegment:loadAddress:isInKernelAddressSpace:]
- +[SABinaryLoadInfo loadInfosForSegmentsInBinary:binaryBaseAddress:isInKernelAddressSpace:]
- -[SABinary symbolOwnerWrapperWithOptions:pid:]
- -[SABinaryLoadInfoTrackingHighestOffset highestOffset]
- -[SABinaryLoadInfoTrackingHighestOffset isInKernelAddressSpace]
- -[SABinaryLoadInfoTrackingHighestOffset setHighestOffset:]
- -[SASamplePrinter displayedBinaryLoadInfoForBinary:segment:desiredLoadAddress:offsetIntoLoadInfo:isInKernelAddressSpace:binariesToDisplay:extraBinariesToDisplay:]
- -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]
- -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]
- -[SASampleStore addKCDataThreadV4:threadV2:deltaThreadV3:deltaThreadV2:timestamp:sampleIndex:stack:threadName:dispatchQueueLabel:waitInfo:waitInfoPortLabelInfo:turnstileInfo:turnstileInfoPortLabelInfo:instructionCycles:task:kernelTask:taskIsSuspended:]
- -[SASampleStore backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]
- -[SASampleStore fixupAllTasksFrames]
- -[SATask fixupFrameInstructionsWithDataGatheringOptions:mightBeAlive:inspectedLiveTask:uuidsWithNewInstructions:]
- GCC_except_table113
- GCC_except_table116
- GCC_except_table125
- GCC_except_table127
- GCC_except_table128
- GCC_except_table150
- GCC_except_table161
- GCC_except_table167
- GCC_except_table170
- GCC_except_table172
- GCC_except_table178
- GCC_except_table188
- GCC_except_table196
- GCC_except_table199
- GCC_except_table205
- GCC_except_table208
- GCC_except_table227
- GCC_except_table260
- GCC_except_table261
- GCC_except_table448
- GCC_except_table451
- GCC_except_table454
- GCC_except_table82
- GCC_except_table85
- GCC_except_table88
- GCC_except_table89
- GCC_except_table91
- GCC_except_table94
- GCC_except_table96
- _.str.446
- _.str.676
- _CopyDonatingUniquePids
- _CopyJetsamCoalitionInfo
- _OBJC_CLASS_$_SABinaryLoadInfoTrackingHighestOffset
- _OBJC_CLASS_$_SABinaryLoadInfoZerothSegmentOnly
- _OBJC_IVAR_$_SABinaryLoadInfoTrackingHighestOffset._highestOffset
- _OBJC_IVAR_$_SABinaryLoadInfoTrackingHighestOffset._isInKernelAddressSpace
- _OBJC_METACLASS_$_SABinaryLoadInfoTrackingHighestOffset
- _OBJC_METACLASS_$_SABinaryLoadInfoZerothSegmentOnly
- __OBJC_$_INSTANCE_METHODS_SABinaryLoadInfoTrackingHighestOffset
- __OBJC_$_INSTANCE_VARIABLES_SABinaryLoadInfoTrackingHighestOffset
- __OBJC_$_PROP_LIST_SABinaryLoadInfoTrackingHighestOffset
- __OBJC_CLASS_RO_$_SABinaryLoadInfoTrackingHighestOffset
- __OBJC_CLASS_RO_$_SABinaryLoadInfoZerothSegmentOnly
- __OBJC_METACLASS_RO_$_SABinaryLoadInfoTrackingHighestOffset
- __OBJC_METACLASS_RO_$_SABinaryLoadInfoZerothSegmentOnly
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1199
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1203
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1206
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1200
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1207
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1558
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1560
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.248
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.250
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.251
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1978
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1986
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1991
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2007
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1938
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1947
- ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke
- ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke.297
- ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke.307
- ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke.311
- ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke_2
- ___28-[SASampleStore postprocess]_block_invoke.163
- ___28-[SASampleStore postprocess]_block_invoke_2.164
- ___28-[SASampleStore postprocess]_block_invoke_3.167
- ___30-[SASamplePrinter printHeader]_block_invoke.1045
- ___30-[SASamplePrinter printHeader]_block_invoke.1076
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1046
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1089
- ___31+[SASharedCache addDSCSymData:]_block_invoke.475
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_2
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_3
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_4
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_5
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_6
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_7
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_8
- ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_9
- ___36-[SASampleStore fixupAllTasksFrames]_block_invoke
- ___37-[SASamplePrinter checkForBadOptions]_block_invoke.326
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke.1143
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke.1150
- ___46-[SABinary symbolOwnerWrapperWithOptions:pid:]_block_invoke
- ___46-[SABinary symbolOwnerWrapperWithOptions:pid:]_block_invoke.137
- ___46-[SABinary symbolOwnerWrapperWithOptions:pid:]_block_invoke.139
- ___46-[SABinary symbolOwnerWrapperWithOptions:pid:]_block_invoke_2
- ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.466
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1608
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.1609
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.1610
- ___573-[SASampleStore(KPerfPrivate) backfillThread:inTask:lastSampleIndex:timestamp:haveName:name:haveDispatchQueueId:dispatchQueueId:dispatchQueueLabel:leafKernelFrame:haveUserStack:leafUserFrame:swiftTaskId:leafOfCRootFramesReplacedBySwiftAsync:haveSched:systemCpuTimeNs:userCpuTimeNs:basePriority:scheduledPriority:state:threadQos:threadRequestedQos:threadRequestedQosOverride:threadQosPromote:haveCycIns:instructions:cycles:haveSnap:ioTier:isIOPassive:isDarwinBG:isSuspended:isGlobalForcedIdle:isIdleWorkQueue:lastMadeRunnableTime:isOnCore:isOnCoreForLastSampleIndex:cpuNum:]_block_invoke
- ___63-[SABinary symbolicateAllInstructionsWithOptions:pid:onlyDsym:]_block_invoke
- ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.336
- ___CopyDonatingUniquePids_block_invoke
- ___CopyJetsamCoalitionInfo_block_invoke
- ___CopyJetsamCoalitionInfo_block_invoke_2
- ___ReadAheadTaskLevelInfo_block_invoke.1574
- ___ReadAheadTaskLevelInfo_block_invoke.1579
- ___ReadAheadTaskLevelInfo_block_invoke.1582
- ___block_descriptor_147_ea8_32s40s48s56r64r72r80r_e28_v32?0"SATaskState"8Q16^B24lr56l8s32l8s40l8r64l8r72l8r80l8s48l8
- ___block_descriptor_276_e8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
- ___block_descriptor_32_e89_q24?0"SABinaryLoadInfoTrackingHighestOffset"8"SABinaryLoadInfoTrackingHighestOffset"16l
- ___block_descriptor_44_e8_32bs_e24_v32?0"SAFrame"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32s40bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e20_v24?0"SATask"8^B16ls32l8s40l8
- ___block_descriptor_49_e8_32s40s_e21_v20?0"SABinary"8i16ls32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56s64s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1049
- ___block_literal_global.1493
- ___block_literal_global.152
- ___block_literal_global.1532
- ___block_literal_global.1535
- ___block_literal_global.1552
- ___block_literal_global.1563
- ___block_literal_global.1568
- ___block_literal_global.1600
- ___block_literal_global.172
- ___block_literal_global.191
- ___block_literal_global.1935
- ___block_literal_global.1950
- ___block_literal_global.1971
- ___block_literal_global.1980
- ___block_literal_global.199
- ___block_literal_global.2038
- ___block_literal_global.2245
- ___block_literal_global.225
- ___block_literal_global.292
- ___block_literal_global.299
- ___block_literal_global.334
- ___block_literal_global.339
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.362
- ___block_literal_global.364
- ___block_literal_global.372
- ___block_literal_global.390
- ___block_literal_global.394
- ___block_literal_global.397
- ___block_literal_global.405
- ___block_literal_global.409
- ___block_literal_global.437
- ___block_literal_global.439
- ___block_literal_global.441
- ___block_literal_global.453
- ___block_literal_global.465
- ___block_literal_global.739
- __parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:.next_fake_unique_pid
- __unnamed_array_storage.1624
- __unnamed_array_storage.2048
- __unnamed_array_storage.2054
- __unnamed_array_storage.424
- __unnamed_array_storage.430
- _objc_msgSend$symbolicateAllInstructionsWithOptions:pid:
CStrings:
+ "\x01\x11\x11"
+ "\x02SA"
+ "\x03\x1e\x11\xa2A\x81\x11\x1e\x15\x11\xc5\x12\x13V\x82C"
+ " exclave %-*s"
+ "!exclave || isInKernelAddressSpace"
+ "%#18llx"
+ "%'llu Created %s-core threadState (index %lu) for thread 0x%llx (sample index %ld-%ld, machabs %llu-%llu) with kernel stack (leaf frame 0x%llx) exclaves:%d\n"
+ "%'llu task [%d] ran into non-kperf state at index %lu, stopping\n"
+ "%*s%s: asid %llu, tnid %llu, invocationid %llu, flags 0x%llx%s\n"
+ "%*s%s: id %llu, flags 0x%llx%s\n"
+ "%*s%s: id %llu, flags 0x%llx, layoutid %llu, slide 0x%llx, %s\n"
+ "%*s%s: layoutid %llu, flags 0x%llx%s\n"
+ "%*s%s: scid %llu, thread offset %u, flags 0x%x%s\n"
+ "%@ + %llu%@"
+ "%@ + %llu%@)"
+ "%@ [0x%llx] (swift:%d kernel:%d exclave:%@ offByOne:%d trunc:%d anotherCallTree:%d)"
+ "%@ callstack with leaf %@"
+ "%@, ho:0x%llx, z:%d"
+ "%s has exclave %s in user space"
+ "%s segment %s has exclave %s in user space"
+ "%s: %lu callstacks"
+ "%s: %lu loadInfos"
+ "((void*)(additions + 1)) - ((void*)serializedFrame) == (long) [self sizeInBytesForSerializedVersion]"
+ "0 frame in exclave stack, ignoring"
+ "<exclave %@>"
+ "<exclave 0x%llx>"
+ "<exclave UNKNOWN>"
+ "??? (%@ + %llu%@)"
+ "??? (%@)"
+ "@\"SAExclave\""
+ "@\"SAExclaveFrame\""
+ "@\"SAThreadExclavesInfo\""
+ "A"
+ "B40@0:8^{?=CCII}16Q24@32"
+ "B40@0:8^{?=CCQQ(?=C{?=b1})QQ}16Q24@32"
+ "B40@0:8^{?=CCQQIQ(?=C{?=b1b1b1b1})}16Q24@32"
+ "B40@0:8^{?=CCQQQII}16Q24@32"
+ "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQiiQ}16Q24@32"
+ "B40@0:8^{?=CCQQQQ}16Q24@32"
+ "Frame exclave:%d has exclave %s, is class %s, not SAExclaveFrame"
+ "No exclave address space %llu in stackshot"
+ "No exclave_addressspace_info in addressspace container"
+ "No exclave_ipcstackentry_info in ipcstackentry container"
+ "No exclave_scresult_info in scresult container"
+ "No exclave_textlayout_info in textlayout container"
+ "SABinaryLoadInfoToDisplay"
+ "SAExclave"
+ "SAExclaveBinaryLoadInfo"
+ "SAExclaveCallstack"
+ "SAExclaveFrame"
+ "SAKCDataExclaveAddressSpace"
+ "SAKCDataExclaveCallstack"
+ "SAKCDataExclaveSCResult"
+ "SAKCDataExclaveTextLayout"
+ "SAKCDataExclaveTextLayoutSegment"
+ "SAThreadExclavesInfo"
+ "T@\"NSArray\",R,V_exclaves"
+ "T@\"NSArray\",R,V_loadInfos"
+ "T@\"SAExclave\",R"
+ "T@\"SAExclave\",R,W"
+ "TB,V_displayExclaveFrames"
+ "TB,V_isZerothAndOnlySegment"
+ "TI,V_exclaveInsertionIndex"
+ "Unknown SAExclave version"
+ "Unknown SAExclaveCallstack version"
+ "Unknown SAThreadExclavesInfo version"
+ "WARNING: exclave address space name non NULL-terminated"
+ "Xr"
+ "[self isKindOfClass:SAExclaveFrame.class]"
+ "_addresses"
+ "_callstacks"
+ "_displayExclaveFrames"
+ "_exclave"
+ "_exclaveFrame"
+ "_exclaveInsertionIndex"
+ "_exclave_addressspace_info"
+ "_exclave_ipcstackentry_info"
+ "_exclave_scresult_info"
+ "_exclave_textlayout_info"
+ "_exclave_textlayout_segment"
+ "_exclaves"
+ "_exclavesInfo"
+ "_invocationID"
+ "_isInExclave"
+ "_isZerothAndOnlySegment"
+ "_kPerfPETParsePastLastStackshot"
+ "_leafFrame"
+ "_loadInfos"
+ "_textSegments"
+ "_textlayout_flags"
+ "_threadNumericID"
+ "buffer + bufferLength >= ((void*)(additions + 1))"
+ "bufferLength %lu < serialized SABinaryLoadInfo v3 struct %lu"
+ "bufferLength %lu < serialized SAExclave struct %lu"
+ "bufferLength %lu < serialized SAExclave struct with %u root frames, %u image infos"
+ "bufferLength %lu < serialized SAExclaveCallstack struct %lu"
+ "bufferLength %lu < serialized SAFrame struct v4 with %u children"
+ "bufferLength %lu < serialized SAThreadExclavesInfo struct %lu"
+ "bufferLength %lu < serialized SAThreadExclavesInfo struct with %u callstacks"
+ "bufferLength %lu < serialized SAThreadState v8 struct %lu"
+ "bufferLength >= sizeof(*serializedBinaryLoadInfo_v3)"
+ "bufferLength >= sizeof(*serializedExclave)"
+ "bufferLength >= sizeof(*serializedExclaveCallstack)"
+ "bufferLength >= sizeof(*serializedThreadExclavesInfo)"
+ "bufferLength >= sizeof(*serializedThreadState_v8)"
+ "callstacks.count < UINT32_MAX"
+ "containerType == STACKSHOT_KCCONTAINER_EXCLAVES"
+ "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_ADDRESSSPACE"
+ "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_IPCSTACKENTRY"
+ "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_SCRESULT"
+ "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_TEXTLAYOUT"
+ "copyWithNewParent:"
+ "displayExclaveFrames"
+ "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayExclaveFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\naggregateProcessesByExecutable: %d\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
+ "exclave"
+ "exclave %#18llx"
+ "exclave %@"
+ "exclave 0x%llx %@"
+ "exclave UNKNOWN"
+ "exclave address space container"
+ "exclave address space info"
+ "exclave address space name"
+ "exclave container"
+ "exclaveInsertionIndex"
+ "exclaves"
+ "exclaves ipc stack entry container"
+ "exclaves ipc stack entry info"
+ "exclaves ipc stack entry info ecstack"
+ "exclaves scresult container"
+ "exclaves scresult info"
+ "exclaves text layout container"
+ "exclaves text layout info"
+ "exclaves text layout segments"
+ "exclaves thread info"
+ "isExclave"
+ "isKernelFrame"
+ "isZerothAndOnlySegment"
+ "kPerfPETParsePastLastStackshot"
+ "loadInfos"
+ "loadInfos.count < UINT32_MAX"
+ "no kernel task, though there are exclaves"
+ "q24@?0@\"SABinaryLoadInfoToDisplay\"8@\"SABinaryLoadInfoToDisplay\"16"
+ "r*"
+ "r^{exclave_addressspace_info=QQQQQ}"
+ "r^{exclave_ipcstackentry_info=QQQQ}"
+ "r^{exclave_scresult_info=QQ}"
+ "r^{exclave_textlayout_info=QQ}"
+ "r^{exclave_textlayout_segment=[16C]Q}"
+ "reset"
+ "rootFrames.count < UINT32_MAX"
+ "setDisplayExclaveFrames:"
+ "setExclaveInsertionIndex:"
+ "setIsZerothAndOnlySegment:"
+ "setKPerfPETParsePastLastStackshot:"
+ "stack with %d kernel frames (leaf 0x%llx), %d user (leaf 0x%llx), %d swift async (leaf 0x%llx), backtracer %llu, exclave@%u"
+ "synthetic"
+ "thread exclave info with %lu callstacks"
+ "threadQos %d"
+ "threadQosKEventOverride %d"
+ "threadQosPromote %d"
+ "threadQosWorkQueueOverride %d"
+ "threadQosWorkloopServicerOverride %d"
+ "threadRequestedQos %d"
+ "threadRequestedQosOverride %d"
+ "unslid"
+ "v20@?0I8r^{exclave_textlayout_segment=[16C]Q}12"
+ "v28@?0@\"SABinary\"8i16B20B24"
+ "yes"
+ "\xa5\x12"
- "\x01CA"
- "\x03\x1d\x11\x92A\x81\x11\x1e\x15\x11\xc5\x12\x13V\x82C"
- "%'llu Created %s-core threadState (index %lu) for thread 0x%llx (sample index %ld-%ld, machabs %llu-%llu) with kernel stack (leaf frame 0x%llx)\n"
- "%@ + %llu)"
- "%@ [0x%llx] (swift:%d kernel:%d offByOne:%d trunc:%d anotherCallTree:%d"
- "((void*)(childFrameIndexes + serializedFrame->numChildFrames)) - ((void*)serializedFrame) == (long) [self sizeInBytesForSerializedVersion]"
- "2"
- "??? (%@ + %llu)"
- "B40@0:8^{?=CCQQ(?=C{?=b1})Q}16Q24@32"
- "B40@0:8^{?=CCQQIQ(?=C{?=b1b1b1})}16Q24@32"
- "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQii}16Q24@32"
- "SABinaryLoadInfoTrackingHighestOffset"
- "SABinaryLoadInfoZerothSegmentOnly"
- "Xq"
- "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\naggregateProcessesByExecutable: %d\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
- "firstSegment"
- "q24@?0@\"SABinaryLoadInfoTrackingHighestOffset\"8@\"SABinaryLoadInfoTrackingHighestOffset\"16"
- "stack with %d kernel frames (leaf 0x%llx), %d user (leaf 0x%llx), %d swift async (leaf 0x%llx), backtracer %llu"
- "thread ## name %d"
- "threadState.endSampleIndex %lu != taskState.endSampleIndex %lu"
- "threadState.endSampleIndex == taskState.endSampleIndex"
- "v20@?0@\"SABinary\"8i16"
- "zerothSegmentOnly load info with no segment at offset 0: %s (first segment %s)"
- "\x95\x12"

```
