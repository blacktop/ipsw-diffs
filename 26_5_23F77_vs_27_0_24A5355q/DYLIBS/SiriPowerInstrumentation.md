## SiriPowerInstrumentation

> `/System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation`

```diff

 3500.3.1.0.0
-  __TEXT.__text: 0x4548
-  __TEXT.__auth_stubs: 0x210
+  __TEXT.__text: 0x4364
   __TEXT.__objc_methlist: 0xf64
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x908
-  __TEXT.__unwind_info: 0x328
-  __TEXT.__objc_classname: 0x866
-  __TEXT.__objc_methname: 0xc27
-  __TEXT.__objc_methtype: 0x2bb
-  __TEXT.__objc_stubs: 0x940
-  __DATA_CONST.__got: 0x98
+  __TEXT.__cstring: 0x910
+  __TEXT.__unwind_info: 0x300
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x98
   __AUTH_CONST.__cfstring: 0xa00
   __AUTH_CONST.__objc_const: 0x2950
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x60
   __DATA.__data: 0x8
   __DATA_DIRTY.__objc_data: 0x1400

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 70CC1DF4-DB19-390E-A44C-692EF759661C
+  UUID: 8BA523A5-18B9-3E89-AD1D-54BFD77607F7
   Functions: 222
-  Symbols:   978
-  CStrings:  432
+  Symbols:   979
+  CStrings:  163
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release_x1
- _objc_release_x8
- _objc_retain_x19
Functions:
~ +[SPIProcessStartedEventContext context] : 80 -> 76
~ +[SPIProcessEndedEventContext context] : 80 -> 76
~ +[SPITestingEventContext context] : 80 -> 76
~ +[SPIAsrInitializationStartedOrChangedEventContext context] : 80 -> 76
~ +[SPIAsrInitializationEndedEventContext context] : 80 -> 76
~ +[SPIAsrAssetLoadStartedOrChangedEventContext context] : 80 -> 76
~ +[SPIAsrAssetLoadEndedEventContext context] : 80 -> 76
~ +[SPIAsrAudioPacketArrivalStartedOrChangedEventContext context] : 80 -> 76
~ +[SPIAsrAudioPacketArrivalEndedEventContext context] : 80 -> 76
~ +[SPIAsrFirstAudioPacketProcessedEventContext context] : 80 -> 76
~ +[SPIAsrRequestStartedOrChangedEventContext context] : 80 -> 76
~ +[SPIAsrPartialResultGeneratedEventContext context] : 80 -> 76
~ +[SPIAsrFinalResultGeneratedEventContext context] : 80 -> 76
~ +[SPIAsrRequestEndedOrFailedOrCancelledEventContext context] : 80 -> 76
~ +[SPIAsrPreheatStartedOrChangedEventContext context] : 80 -> 76
~ +[SPIAsrPreheatFailedEventContext context] : 80 -> 76
~ +[SPIAsrPreheatEndedAlreadyDoneEventContext context] : 80 -> 76
~ +[SPIAsrPreheatEndedSuccessEventContext context] : 80 -> 76
~ +[SPIOrchRequestStartedEventContext context] : 80 -> 76
~ +[SPIOrchRequestEndedEventContext context] : 80 -> 76
~ +[SPIOrchRequestFailedEventContext context] : 80 -> 76
~ +[SPIOrchRequestCancelledEventContext context] : 80 -> 76
~ +[SPIOrchAsrCallStartedEventContext context] : 80 -> 76
~ +[SPIOrchAsrCallEndedEventContext context] : 80 -> 76
~ +[SPIOrchAsrCallFailedEventContext context] : 80 -> 76
~ +[SPIOrchCdmRequestStartedEventContext context] : 80 -> 76
~ +[SPIOrchCdmRequestEndedEventContext context] : 80 -> 76
~ +[SPIOrchCdmRequestFailedEventContext context] : 80 -> 76
~ +[SPIOrchExecutionRequestReceivedEventContext context] : 80 -> 76
~ +[SPIOrchExecutionEndedEventContext context] : 80 -> 76
~ +[SPIOrchExecutionFailedEventContext context] : 80 -> 76
~ +[SPIOrchPommesRequestStartedEventContext context] : 80 -> 76
~ +[SPIOrchPommesRequestEndedEventContext context] : 80 -> 76
~ +[SPIOrchPommesRequestFailedEventContext context] : 80 -> 76
~ +[SPISiriUUFRShownEventContext context] : 80 -> 76
~ +[SPISiriStateTransitionEventContext context] : 80 -> 76
~ +[SPISiriActivatedEventContext context] : 80 -> 76
~ +[SPISiriDismissedEventContext context] : 80 -> 76
~ +[SPITtsRequestReceivedEventContext context] : 80 -> 76
~ +[SPITtsSpeechStartedOrChangedEventContext context] : 80 -> 76
~ +[SPITtsSpeechEndedEventContext context] : 80 -> 76
~ +[SPITtsSpeechFailedEventContext context] : 80 -> 76
~ +[SPITtsSpeechCancelledEventContext context] : 80 -> 76
~ +[SPIUeiLaunchEndedEventContext context] : 80 -> 76
~ +[SPIUeiInvocationEventContext context] : 80 -> 76
~ +[SPIUeiUiStateTransitionEventContext context] : 80 -> 76
~ +[SPIUeiUufrSaidEventContext context] : 80 -> 76
~ +[SPIUeiRequestCategorizationEventContext context] : 80 -> 76
~ +[SPIUeiTextToSpeechBeginEventContext context] : 80 -> 76
~ +[SPIUeiTextToSpeechEndEventContext context] : 80 -> 76
~ +[SPIProcessUtils getProcessNameForPid:] : 152 -> 148
~ +[SPIProcessUtils getProcessForPid:] : 140 -> 128
~ -[SPISELFMessageBuilder addProcess:] : 104 -> 100
~ -[SPISELFMessageBuilder addProcessUsage:] : 144 -> 140
~ -[SPISELFMessageBuilder addContext:] : 104 -> 100
~ -[SPISELFMessageBuilder addRequestLinkInfoForComponent:identifier:] : 184 -> 180
~ -[SPISELFMessageBuilder buildMessage] : 116 -> 108
~ -[SPISELFMessageBuilder setPowClientEventMsg:] : 64 -> 12
~ -[SPISELFMessageBuilder setUsageMsg:] : 64 -> 12
~ -[SPISELFMessageBuilder setProcUsageMsg:] : 64 -> 12
~ -[SPISELFMessageBuilder setEventContextMsg:] : 64 -> 12
~ -[POWSchemaProvisionalPOWClientEvent hasLink] : 24 -> 28
~ -[POWSchemaProvisionalPOWClientEvent setUsage:] : 96 -> 48
~ -[POWSchemaProvisionalPOWClientEvent usage] : 92 -> 100
~ -[POWSchemaProvisionalPOWClientEvent deleteUsage] : 48 -> 56
~ _POWSchemaProvisionalPOWClientEventReadFrom : 596 -> 592
~ _POWSchemaProvisionalPOWUsageReadFrom : 980 -> 1008
~ -[POWSchemaProvisionalPOWClientEvent writeTo:] : 204 -> 188
~ -[POWSchemaProvisionalPOWClientEvent isEqual:] : 512 -> 476
~ -[POWSchemaProvisionalPOWClientEvent hash] : 72 -> 80
~ -[POWSchemaProvisionalPOWClientEvent dictionaryRepresentation] : 376 -> 356
~ -[POWSchemaProvisionalPOWClientEvent jsonData] : 128 -> 120
~ -[POWSchemaProvisionalPOWClientEvent initWithDictionary:] : 312 -> 304
~ -[POWSchemaProvisionalPOWClientEvent whichEvent_Type] : 16 -> 20
~ -[POWSchemaProvisionalPOWClientEvent link] : 16 -> 20
~ -[POWSchemaProvisionalPOWClientEvent setLink:] : 80 -> 20
~ -[POWSchemaProvisionalPOWClientEvent setHasLink:] : 16 -> 20
~ -[POWSchemaProvisionalPOWClientEvent hasUsage] : 16 -> 20
~ -[POWSchemaProvisionalPOWClientEvent setHasUsage:] : 16 -> 20
~ -[POWSchemaProvisionalPOWProcessUsage setCpuCycles:] : 36 -> 44
~ -[POWSchemaProvisionalPOWProcessUsage hasCpuCycles] : 20 -> 24
~ -[POWSchemaProvisionalPOWProcessUsage setHasCpuCycles:] : 28 -> 32
~ -[POWSchemaProvisionalPOWProcessUsage deleteCpuCycles] : 60 -> 64
~ -[POWSchemaProvisionalPOWProcessUsage setCpuInstructions:] : 36 -> 44
~ -[POWSchemaProvisionalPOWProcessUsage hasCpuInstructions] : 20 -> 24
~ -[POWSchemaProvisionalPOWProcessUsage setHasCpuInstructions:] : 40 -> 44
~ -[POWSchemaProvisionalPOWProcessUsage deleteCpuInstructions] : 60 -> 64
~ -[POWSchemaProvisionalPOWProcessUsage setGpuCycles:] : 36 -> 44
~ -[POWSchemaProvisionalPOWProcessUsage hasGpuCycles] : 20 -> 24
~ -[POWSchemaProvisionalPOWProcessUsage setHasGpuCycles:] : 40 -> 44
~ -[POWSchemaProvisionalPOWProcessUsage deleteGpuCycles] : 60 -> 64
~ -[POWSchemaProvisionalPOWProcessUsage setMemoryFootprint:] : 36 -> 44
~ -[POWSchemaProvisionalPOWProcessUsage hasMemoryFootprint] : 20 -> 24
~ -[POWSchemaProvisionalPOWProcessUsage setHasMemoryFootprint:] : 40 -> 44
~ -[POWSchemaProvisionalPOWProcessUsage deleteMemoryFootprint] : 60 -> 64
~ _POWSchemaProvisionalPOWProcessUsageReadFrom : 1328 -> 1308
~ -[POWSchemaProvisionalPOWProcessUsage writeTo:] : 220 -> 240
~ -[POWSchemaProvisionalPOWProcessUsage isEqual:] : 316 -> 340
~ -[POWSchemaProvisionalPOWProcessUsage hash] : 148 -> 168
~ -[POWSchemaProvisionalPOWProcessUsage dictionaryRepresentation] : 404 -> 388
~ -[POWSchemaProvisionalPOWProcessUsage jsonData] : 128 -> 120
~ -[POWSchemaProvisionalPOWProcessUsage initWithDictionary:] : 432 -> 416
~ -[POWSchemaProvisionalPOWProcessUsage cpuCycles] : 16 -> 20
~ -[POWSchemaProvisionalPOWProcessUsage cpuInstructions] : 16 -> 20
~ -[POWSchemaProvisionalPOWProcessUsage gpuCycles] : 16 -> 20
~ -[POWSchemaProvisionalPOWProcessUsage memoryFootprint] : 16 -> 20
~ -[POWSchemaProvisionalPOWUsage setProcess:] : 36 -> 44
~ -[POWSchemaProvisionalPOWUsage hasProcess] : 20 -> 24
~ -[POWSchemaProvisionalPOWUsage setHasProcess:] : 28 -> 32
~ -[POWSchemaProvisionalPOWUsage deleteProcess] : 60 -> 64
~ -[POWSchemaProvisionalPOWUsage hasProcessUsage] : 24 -> 28
~ -[POWSchemaProvisionalPOWUsage setContext:] : 36 -> 44
~ -[POWSchemaProvisionalPOWUsage hasContext] : 20 -> 24
~ -[POWSchemaProvisionalPOWUsage setHasContext:] : 40 -> 44
~ -[POWSchemaProvisionalPOWUsage deleteContext] : 60 -> 64
~ -[POWSchemaProvisionalPOWUsage writeTo:] : 216 -> 220
~ -[POWSchemaProvisionalPOWUsage isEqual:] : 428 -> 424
~ -[POWSchemaProvisionalPOWUsage hash] : 144 -> 160
~ -[POWSchemaProvisionalPOWUsage dictionaryRepresentation] : 384 -> 376
~ -[POWSchemaProvisionalPOWUsage jsonData] : 128 -> 120
~ -[POWSchemaProvisionalPOWUsage initWithDictionary:] : 372 -> 360
~ -[POWSchemaProvisionalPOWUsage process] : 16 -> 20
~ -[POWSchemaProvisionalPOWUsage processUsage] : 16 -> 20
~ -[POWSchemaProvisionalPOWUsage setProcessUsage:] : 80 -> 20
~ -[POWSchemaProvisionalPOWUsage context] : 16 -> 20
~ -[POWSchemaProvisionalPOWUsage setHasProcessUsage:] : 16 -> 20
~ -[SPIPowerLoggerSnapshot initWithPowerLogger:usage:captureTimestamp:] : 144 -> 152
~ -[SPIPowerLoggerSnapshot logWithEventContext:componentName:identifier:] : 148 -> 152
~ -[SPIPowerLoggerSnapshot buildAndEmitWithMessageBuilder:eventContext:] : 224 -> 216
~ -[SPIPowerLogger initWithCurrentProcess] : 100 -> 96
CStrings:
- ".cxx_destruct"
- "@\"POWSchemaProvisionalPOWClientEvent\""
- "@\"POWSchemaProvisionalPOWProcessUsage\""
- "@\"POWSchemaProvisionalPOWUsage\""
- "@\"SISchemaInstrumentationMessage\""
- "@\"SISchemaRequestLinkInfo\""
- "@\"SPIPowerLogger\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8@16"
- "@56@0:8@16{SPIResourceUsage=QQQ}24Q48"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "C16@0:8"
- "C20@0:8i16"
- "InstrumentationAdditions"
- "JSONObjectWithData:options:error:"
- "POWSchemaProvisionalPOWClientEvent"
- "POWSchemaProvisionalPOWProcessUsage"
- "POWSchemaProvisionalPOWUsage"
- "Q"
- "Q16@0:8"
- "SPIAsrAssetLoadEndedEventContext"
- "SPIAsrAssetLoadStartedOrChangedEventContext"
- "SPIAsrAudioPacketArrivalEndedEventContext"
- "SPIAsrAudioPacketArrivalStartedOrChangedEventContext"
- "SPIAsrEventContext"
- "SPIAsrFinalResultGeneratedEventContext"
- "SPIAsrFirstAudioPacketProcessedEventContext"
- "SPIAsrInitializationEndedEventContext"
- "SPIAsrInitializationStartedOrChangedEventContext"
- "SPIAsrPartialResultGeneratedEventContext"
- "SPIAsrPreheatEndedAlreadyDoneEventContext"
- "SPIAsrPreheatEndedSuccessEventContext"
- "SPIAsrPreheatFailedEventContext"
- "SPIAsrPreheatStartedOrChangedEventContext"
- "SPIAsrRequestEndedOrFailedOrCancelledEventContext"
- "SPIAsrRequestStartedOrChangedEventContext"
- "SPIEventContext"
- "SPIOrchAsrCallEndedEventContext"
- "SPIOrchAsrCallFailedEventContext"
- "SPIOrchAsrCallStartedEventContext"
- "SPIOrchCdmRequestEndedEventContext"
- "SPIOrchCdmRequestFailedEventContext"
- "SPIOrchCdmRequestStartedEventContext"
- "SPIOrchEventContext"
- "SPIOrchExecutionEndedEventContext"
- "SPIOrchExecutionFailedEventContext"
- "SPIOrchExecutionRequestReceivedEventContext"
- "SPIOrchPommesRequestEndedEventContext"
- "SPIOrchPommesRequestFailedEventContext"
- "SPIOrchPommesRequestStartedEventContext"
- "SPIOrchRequestCancelledEventContext"
- "SPIOrchRequestEndedEventContext"
- "SPIOrchRequestFailedEventContext"
- "SPIOrchRequestStartedEventContext"
- "SPIPowerLogger"
- "SPIPowerLoggerSnapshot"
- "SPIProcessEndedEventContext"
- "SPIProcessStartedEventContext"
- "SPIProcessUtils"
- "SPISELFMessageBuilder"
- "SPISELFProcessAdapter"
- "SPISiriActivatedEventContext"
- "SPISiriDismissedEventContext"
- "SPISiriEventContext"
- "SPISiriStateTransitionEventContext"
- "SPISiriUUFRShownEventContext"
- "SPITestingEventContext"
- "SPITtsEventContext"
- "SPITtsRequestReceivedEventContext"
- "SPITtsSpeechCancelledEventContext"
- "SPITtsSpeechEndedEventContext"
- "SPITtsSpeechFailedEventContext"
- "SPITtsSpeechStartedOrChangedEventContext"
- "SPIUeiEventContext"
- "SPIUeiInvocationEventContext"
- "SPIUeiLaunchEndedEventContext"
- "SPIUeiRequestCategorizationEventContext"
- "SPIUeiTextToSpeechBeginEventContext"
- "SPIUeiTextToSpeechEndEventContext"
- "SPIUeiUiStateTransitionEventContext"
- "SPIUeiUufrSaidEventContext"
- "T@\"NSData\",R,N"
- "T@\"POWSchemaProvisionalPOWClientEvent\",&,N,V_powClientEventMsg"
- "T@\"POWSchemaProvisionalPOWProcessUsage\",&,N,V_procUsageMsg"
- "T@\"POWSchemaProvisionalPOWProcessUsage\",&,N,V_processUsage"
- "T@\"POWSchemaProvisionalPOWUsage\",&,N,V_usage"
- "T@\"POWSchemaProvisionalPOWUsage\",&,N,V_usageMsg"
- "T@\"SISchemaInstrumentationMessage\",&,N,V_eventContextMsg"
- "T@\"SISchemaRequestLinkInfo\",&,N,V_link"
- "T@\"SPIPowerLogger\",R,N,V_powerLogger"
- "TB,N"
- "TB,N,V_hasLink"
- "TB,N,V_hasProcessUsage"
- "TB,N,V_hasUsage"
- "TC,R,N,Vprocess"
- "TQ,N,V_cpuCycles"
- "TQ,N,V_cpuInstructions"
- "TQ,N,V_gpuCycles"
- "TQ,N,V_memoryFootprint"
- "TQ,R,N,V_captureTimestamp"
- "TQ,R,N,V_whichEvent_Type"
- "Ti,N,V_context"
- "Ti,N,V_process"
- "Ti,R,N,Vpid"
- "T{SPIResourceUsage=QQQ},R,N,V_usage"
- "_captureTimestamp"
- "_context"
- "_cpuCycles"
- "_cpuInstructions"
- "_eventContextMsg"
- "_gpuCycles"
- "_has"
- "_hasLink"
- "_hasProcessUsage"
- "_hasUsage"
- "_link"
- "_memoryFootprint"
- "_powClientEventMsg"
- "_powerLogger"
- "_procUsageMsg"
- "_process"
- "_processUsage"
- "_setError"
- "_staticWrappedInitWithCurrentProcess"
- "_staticWrappedInitWithProcessIdentifier:"
- "_usage"
- "_usageMsg"
- "_whichEvent_Type"
- "addContext:"
- "addProcess:"
- "addProcessUsage:"
- "addRequestLinkInfoForComponent:identifier:"
- "buildAndEmitWithMessageBuilder:eventContext:"
- "buildMessage"
- "captureSnapshot"
- "captureTimestamp"
- "data"
- "dataWithJSONObject:options:error:"
- "deleteContext"
- "deleteCpuCycles"
- "deleteCpuInstructions"
- "deleteGpuCycles"
- "deleteLink"
- "deleteMemoryFootprint"
- "deleteProcess"
- "deleteProcessUsage"
- "deleteUsage"
- "dictionary"
- "dictionaryRepresentation"
- "emitMessage:timestamp:"
- "eventContextMsg"
- "getAnyEventType"
- "getBytes:range:"
- "getProcessForPid:"
- "getProcessNameForPid:"
- "getTypeId"
- "getUsageForPid:withOutput:"
- "getVersion"
- "hasContext"
- "hasCpuCycles"
- "hasCpuInstructions"
- "hasError"
- "hasGpuCycles"
- "hasLink"
- "hasMemoryFootprint"
- "hasProcess"
- "hasProcessUsage"
- "hasUsage"
- "hash"
- "i16@0:8"
- "i20@0:8C16"
- "i28@0:8i16^{SPIResourceUsage=QQQ}20"
- "init"
- "initWithCurrentProcess"
- "initWithDictionary:"
- "initWithJSON:"
- "initWithNSUUID:"
- "initWithPowerLogger:usage:captureTimestamp:"
- "initWithProcessIdentifier:"
- "intValue"
- "isEqual:"
- "isMemberOfClass:"
- "isProvisional"
- "isValidJSONObject:"
- "jsonData"
- "length"
- "logWithEventContext:"
- "logWithEventContext:asrIdentifier:"
- "logWithEventContext:componentName:identifier:"
- "logWithEventContext:requestIdentifier:"
- "logWithEventContext:ttsIdentifier:"
- "logWithEventContext:turnIdentifier:"
- "null"
- "numberWithUnsignedLongLong:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "pid"
- "position"
- "powClientEventMsg"
- "powerLogger"
- "procUsageMsg"
- "processIdentifier"
- "processInfo"
- "qualifiedMessageName"
- "readFrom:"
- "setComponent:"
- "setContext:"
- "setContextForUsage:"
- "setCpuCycles:"
- "setCpuInstructions:"
- "setEventContextMsg:"
- "setGpuCycles:"
- "setHasContext:"
- "setHasCpuCycles:"
- "setHasCpuInstructions:"
- "setHasGpuCycles:"
- "setHasLink:"
- "setHasMemoryFootprint:"
- "setHasProcess:"
- "setHasProcessUsage:"
- "setHasUsage:"
- "setLink:"
- "setMemoryFootprint:"
- "setObject:forKeyedSubscript:"
- "setPosition:"
- "setPowClientEventMsg:"
- "setProcUsageMsg:"
- "setProcess:"
- "setProcessUsage:"
- "setUsage:"
- "setUsageMsg:"
- "setUuid:"
- "sharedStream"
- "stringWithUTF8String:"
- "translateProcess:"
- "unsignedLongLongValue"
- "unsignedShortValue"
- "usageMsg"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v28@0:8i16@20"
- "v32@0:8@16@24"
- "v36@0:8@16i24@28"
- "v40@0:8{SPIResourceUsage=QQQ}16"
- "whichEvent_Type"
- "willProduceDictionaryRepresentation:"
- "writeTo:"
- "{?=\"cpuCycles\"b1\"cpuInstructions\"b1\"gpuCycles\"b1\"memoryFootprint\"b1}"
- "{?=\"process\"b1\"context\"b1}"
- "{SPIResourceUsage=\"cpuCycles\"Q\"cpuInstructions\"Q\"memPhysFootprint\"Q}"
- "{SPIResourceUsage=QQQ}16@0:8"

```
