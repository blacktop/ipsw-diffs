## assistantd

> `/System/Library/PrivateFrameworks/AssistantServices.framework/assistantd`

```diff

-3500.97.4.1.2
-  __TEXT.__text: 0x36fcdc
+3500.104.2.0.0
+  __TEXT.__text: 0x37075c
   __TEXT.__auth_stubs: 0x34b0
-  __TEXT.__objc_stubs: 0x445c0
-  __TEXT.__objc_methlist: 0x221c8
+  __TEXT.__objc_stubs: 0x44600
+  __TEXT.__objc_methlist: 0x22220
   __TEXT.__const: 0x109c8
   __TEXT.__dlopen_cstrs: 0xafa
-  __TEXT.__gcc_except_tab: 0x48c8
-  __TEXT.__cstring: 0x511ad
-  __TEXT.__oslogstring: 0x3fe02
-  __TEXT.__objc_classname: 0x5158
-  __TEXT.__objc_methname: 0x5c3b6
-  __TEXT.__objc_methtype: 0xf0af
+  __TEXT.__gcc_except_tab: 0x49a0
+  __TEXT.__cstring: 0x51272
+  __TEXT.__oslogstring: 0x3fd1a
+  __TEXT.__objc_classname: 0x517c
+  __TEXT.__objc_methname: 0x5c3b4
+  __TEXT.__objc_methtype: 0xf108
   __TEXT.__ustring: 0x2b0
-  __TEXT.__unwind_info: 0xa118
+  __TEXT.__unwind_info: 0xa150
   __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0x1a68
   __DATA_CONST.__got: 0x3a58
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x14ce8
-  __DATA_CONST.__cfstring: 0x127a0
-  __DATA_CONST.__objc_classlist: 0xd18
+  __DATA_CONST.__const: 0x14d38
+  __DATA_CONST.__cfstring: 0x127c0
+  __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x620
   __DATA_CONST.__objc_protolist: 0x6d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xb00
+  __DATA_CONST.__objc_superrefs: 0xb08
   __DATA_CONST.__objc_arraydata: 0x388
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_intobj: 0x828
   __DATA_CONST.__objc_dictobj: 0x2d0
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0x33400
-  __DATA.__objc_selrefs: 0x14500
-  __DATA.__objc_ivar: 0x2544
-  __DATA.__objc_data: 0x82f0
+  __DATA.__objc_const: 0x33550
+  __DATA.__objc_selrefs: 0x14520
+  __DATA.__objc_ivar: 0x2558
+  __DATA.__objc_data: 0x8340
   __DATA.__data: 0x5630
   __DATA.__bss: 0xe08
   __DATA.__common: 0xa18

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D72F2A00-44AE-37D5-B07A-46E63756947D
-  Functions: 14242
+  UUID: 661C325D-054A-3DB5-B11A-A47EE7EE872B
+  Functions: 14255
   Symbols:   2862
-  CStrings:  29280
+  CStrings:  29299
 
CStrings:
+ "%s #callstate _callStateChanged notification name=%@"
+ "%s %@ Sampling: Aborting further sampling upload due to permit monitor relay status."
+ "%s Failed to fetch value for key: (%@) (%@)"
+ "%s Failed to fetch values for keys: (%@) - (%@)"
+ "%s Filtering out command %@ for {session type: %d}"
+ "%s Ignoring FindMy update notification on a FullUOD device"
+ "%s Sending SACommandSucceeded for local session %@"
+ "%s passThrough for isCommandAllowedToBeHandledOnClient %@"
+ "-[ADArbitrationFeedbackManager _createDeviceInfoOperationForParticipation:]_block_invoke_2"
+ "-[ADArbitrationFeedbackManager _createRequestInfoUpdateOperationForParticipation:forTurnId:withExecutionContxt:]_block_invoke"
+ "-[ADCallObserver _callStateChanged:]"
+ "-[ADSpeechSamplingDictationAudioDataHandler initWithFilePaths:ignoreMinimumSampleAge:permitMonitor:completionHandler:]"
+ "45"
+ "@\"<ADSoundAnalysisPredicate>\""
+ "@\"ADSpeechSamplingRelayPermitMonitor\""
+ "@44@0:8@16B24@28@?36"
+ "ADSpeechSamplingRelayPermitMonitor"
+ "MobileAssistantDaemons-3500.104.2"
+ "TB,V_shouldAbort"
+ "_buildLaunchHandlerWithFunction_block_invoke_3"
+ "_completionHandler"
+ "_createRequestInfoUpdateOperationForParticipation:forTurnId:withExecutionContxt:"
+ "_permitMonitor"
+ "_shouldAbort"
+ "_soundAnalysisPredicate"
+ "com.apple.icloud.fmip.siri_data_changed"
+ "findSettingWithKeyPath:group:"
+ "initWithFilePaths:ignoreMinimumSampleAge:permitMonitor:completionHandler:"
+ "initWithMotionManager:soundAnalysisPredicate:"
+ "isBluetoothHeadset"
+ "isCommandAllowedToBeHandledOnClient:"
+ "setGenAIAccountType:"
+ "setIsGenAIConfirmationAlwaysRequired:"
+ "setIsGenAISetUpPrompts:"
+ "setShouldAbort:"
+ "shouldAbort"
- "%s Failed to fetch value for key: (%@)"
- "%s Failed to fetch values for keys: (%@)"
- "%s Filtering out all commandsfor {session type: %d}"
- "%s SRD has not implemented cancelRequestWithAssistantId:requestId:reason: yet, failing back to cancelRequestWithAssistantId:requestId:"
- "%s SRD has not implemented requestFailedWithAssistantId:requestId: yet, failling back to cancelRequestWithAssistantId:requestId:reason"
- "%s SRD has not implemented updateConversationContextForRemoteResponseWithAssistantId:requestId:fullSpeak:redactedFullSpeak:fullPrint:redactedFullPrint:listenAfterSpeaking yet. Falling back to previous implementation"
- "%s Updated settings for user on ATV but not part of same home."
- "-[ADArbitrationFeedbackManager _createRequestInfoUpdateOperationForParticipation:forTurnId:]_block_invoke"
- "-[ADRequestDispatcherService requestFailedWithAssistantId:requestId:]"
- "-[ADSpeechSamplingDictationAudioDataHandler initWithFilePaths:ignoreMinimumSampleAge:]"
- "MobileAssistantDaemons-3500.97.4.1.2"
- "_createRequestInfoUpdateOperationForParticipation:forTurnId:"
- "cancelRequestWithAssistantId:requestId:"
- "initWithFilePaths:ignoreMinimumSampleAge:"
- "initWithMotionManager:"
- "setCompletionBlock:"
- "updateConversationContextForRemoteResponseWithAssistantId:requestId:fullSpeak:redactedFullSpeak:fullPrint:redactedFullPrint:"
- "updateVoiceCommandContextWithAssistantId:requestId:prefixText:postfixText:selectedText:disambiguationActive:cursorInVisibleText:favorCommandSuppression:abortCommandSuppression:"

```
