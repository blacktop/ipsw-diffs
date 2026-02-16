## SiriPowerInstrumentation

> `/System/Library/PrivateFrameworks/SiriPowerInstrumentation.framework/SiriPowerInstrumentation`

```diff

 3500.3.1.0.0
-  __TEXT.__text: 0x420c
-  __TEXT.__auth_stubs: 0x230
+  __TEXT.__text: 0x4548
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_methlist: 0xf64
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0x908
-  __TEXT.__unwind_info: 0x300
+  __TEXT.__unwind_info: 0x328
   __TEXT.__objc_classname: 0x866
   __TEXT.__objc_methname: 0xc27
   __TEXT.__objc_methtype: 0x2bb

   __DATA_CONST.__objc_selrefs: 0x3e0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__cfstring: 0xa00
   __AUTH_CONST.__objc_const: 0x2950
   __AUTH_CONST.__objc_intobj: 0xd8

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7022386D-67C0-3EAC-BCD6-2438C7B7030F
+  UUID: C2B75008-093B-3341-B7EE-E285ED5B3CBD
   Functions: 222
-  Symbols:   980
+  Symbols:   978
   CStrings:  432
 
Symbols:
+ _objc_release_x8
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ +[SPIProcessStartedEventContext context] : 76 -> 80
~ +[SPIProcessEndedEventContext context] : 76 -> 80
~ +[SPITestingEventContext context] : 76 -> 80
~ +[SPIAsrInitializationStartedOrChangedEventContext context] : 76 -> 80
~ +[SPIAsrInitializationEndedEventContext context] : 76 -> 80
~ +[SPIAsrAssetLoadStartedOrChangedEventContext context] : 76 -> 80
~ +[SPIAsrAssetLoadEndedEventContext context] : 76 -> 80
~ +[SPIAsrAudioPacketArrivalStartedOrChangedEventContext context] : 76 -> 80
~ +[SPIAsrAudioPacketArrivalEndedEventContext context] : 76 -> 80
~ +[SPIAsrFirstAudioPacketProcessedEventContext context] : 76 -> 80
~ +[SPIAsrRequestStartedOrChangedEventContext context] : 76 -> 80
~ +[SPIAsrPartialResultGeneratedEventContext context] : 76 -> 80
~ +[SPIAsrFinalResultGeneratedEventContext context] : 76 -> 80
~ +[SPIAsrRequestEndedOrFailedOrCancelledEventContext context] : 76 -> 80
~ +[SPIAsrPreheatStartedOrChangedEventContext context] : 76 -> 80
~ +[SPIAsrPreheatFailedEventContext context] : 76 -> 80
~ +[SPIAsrPreheatEndedAlreadyDoneEventContext context] : 76 -> 80
~ +[SPIAsrPreheatEndedSuccessEventContext context] : 76 -> 80
~ +[SPIOrchRequestStartedEventContext context] : 76 -> 80
~ +[SPIOrchRequestEndedEventContext context] : 76 -> 80
~ +[SPIOrchRequestFailedEventContext context] : 76 -> 80
~ +[SPIOrchRequestCancelledEventContext context] : 76 -> 80
~ +[SPIOrchAsrCallStartedEventContext context] : 76 -> 80
~ +[SPIOrchAsrCallEndedEventContext context] : 76 -> 80
~ +[SPIOrchAsrCallFailedEventContext context] : 76 -> 80
~ +[SPIOrchCdmRequestStartedEventContext context] : 76 -> 80
~ +[SPIOrchCdmRequestEndedEventContext context] : 76 -> 80
~ +[SPIOrchCdmRequestFailedEventContext context] : 76 -> 80
~ +[SPIOrchExecutionRequestReceivedEventContext context] : 76 -> 80
~ +[SPIOrchExecutionEndedEventContext context] : 76 -> 80
~ +[SPIOrchExecutionFailedEventContext context] : 76 -> 80
~ +[SPIOrchPommesRequestStartedEventContext context] : 76 -> 80
~ +[SPIOrchPommesRequestEndedEventContext context] : 76 -> 80
~ +[SPIOrchPommesRequestFailedEventContext context] : 76 -> 80
~ +[SPISiriUUFRShownEventContext context] : 76 -> 80
~ +[SPISiriStateTransitionEventContext context] : 76 -> 80
~ +[SPISiriActivatedEventContext context] : 76 -> 80
~ +[SPISiriDismissedEventContext context] : 76 -> 80
~ +[SPITtsRequestReceivedEventContext context] : 76 -> 80
~ +[SPITtsSpeechStartedOrChangedEventContext context] : 76 -> 80
~ +[SPITtsSpeechEndedEventContext context] : 76 -> 80
~ +[SPITtsSpeechFailedEventContext context] : 76 -> 80
~ +[SPITtsSpeechCancelledEventContext context] : 76 -> 80
~ +[SPIUeiLaunchEndedEventContext context] : 76 -> 80
~ +[SPIUeiInvocationEventContext context] : 76 -> 80
~ +[SPIUeiUiStateTransitionEventContext context] : 76 -> 80
~ +[SPIUeiUufrSaidEventContext context] : 76 -> 80
~ +[SPIUeiRequestCategorizationEventContext context] : 76 -> 80
~ +[SPIUeiTextToSpeechBeginEventContext context] : 76 -> 80
~ +[SPIUeiTextToSpeechEndEventContext context] : 76 -> 80
~ +[SPIProcessUtils getProcessNameForPid:] : 148 -> 152
~ +[SPIProcessUtils getProcessForPid:] : 128 -> 140
~ -[SPISELFMessageBuilder addProcess:] : 100 -> 104
~ -[SPISELFMessageBuilder addProcessUsage:] : 140 -> 144
~ -[SPISELFMessageBuilder addContext:] : 100 -> 104
~ -[SPISELFMessageBuilder addRequestLinkInfoForComponent:identifier:] : 180 -> 184
~ -[SPISELFMessageBuilder buildMessage] : 108 -> 116
~ -[SPISELFMessageBuilder setPowClientEventMsg:] : 12 -> 64
~ -[SPISELFMessageBuilder setUsageMsg:] : 12 -> 64
~ -[SPISELFMessageBuilder setProcUsageMsg:] : 12 -> 64
~ -[SPISELFMessageBuilder setEventContextMsg:] : 12 -> 64
~ -[POWSchemaProvisionalPOWClientEvent setUsage:] : 44 -> 96
~ -[POWSchemaProvisionalPOWClientEvent writeTo:] : 188 -> 204
~ -[POWSchemaProvisionalPOWClientEvent isEqual:] : 472 -> 512
~ -[POWSchemaProvisionalPOWClientEvent dictionaryRepresentation] : 348 -> 376
~ -[POWSchemaProvisionalPOWClientEvent jsonData] : 120 -> 128
~ -[POWSchemaProvisionalPOWClientEvent initWithDictionary:] : 304 -> 312
~ -[POWSchemaProvisionalPOWClientEvent setLink:] : 20 -> 80
~ -[POWSchemaProvisionalPOWProcessUsage dictionaryRepresentation] : 384 -> 404
~ -[POWSchemaProvisionalPOWProcessUsage jsonData] : 120 -> 128
~ -[POWSchemaProvisionalPOWProcessUsage initWithDictionary:] : 416 -> 432
~ -[POWSchemaProvisionalPOWUsage writeTo:] : 208 -> 216
~ -[POWSchemaProvisionalPOWUsage isEqual:] : 408 -> 428
~ -[POWSchemaProvisionalPOWUsage dictionaryRepresentation] : 368 -> 384
~ -[POWSchemaProvisionalPOWUsage jsonData] : 120 -> 128
~ -[POWSchemaProvisionalPOWUsage initWithDictionary:] : 360 -> 372
~ -[POWSchemaProvisionalPOWUsage setProcessUsage:] : 20 -> 80
~ -[SPIPowerLoggerSnapshot initWithPowerLogger:usage:captureTimestamp:] : 152 -> 144
~ -[SPIPowerLoggerSnapshot logWithEventContext:componentName:identifier:] : 152 -> 148
~ -[SPIPowerLoggerSnapshot buildAndEmitWithMessageBuilder:eventContext:] : 216 -> 224
~ -[SPIPowerLogger initWithCurrentProcess] : 96 -> 100

```
