## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/Versions/A/LocalSpeechRecognitionBridge`

```diff

-3600.70.47.0.0
-  __TEXT.__text: 0x1fe24
+3605.32.1.14.1
+  __TEXT.__text: 0x20110
   __TEXT.__objc_methlist: 0x25a4
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x4bf2
-  __TEXT.__oslogstring: 0x2d90
-  __TEXT.__unwind_info: 0x760
+  __TEXT.__cstring: 0x4d13
+  __TEXT.__oslogstring: 0x2eb9
+  __TEXT.__unwind_info: 0x750
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x240
-  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__const: 0x258
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1350
+  __DATA_CONST.__objc_selrefs: 0x13b0
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x1b00
-  __AUTH_CONST.__objc_const: 0x3ec8
+  __AUTH_CONST.__cfstring: 0x1bc0
+  __AUTH_CONST.__objc_const: 0x3e28
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_ivar: 0x2d8
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x2dc
   __DATA.__data: 0x8b0
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x58
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 786
-  Symbols:   1910
-  CStrings:  617
+  Symbols:   1904
+  CStrings:  628
 
Symbols:
+ -[LBAudioStreamProvider _anchorHostTimeForPacketIndex:inHostTimes:baseIndex:]
+ -[LBAudioStreamProvider _forwardUserSpeakingEndWithSecondsFromEnd:lastPacketIndex:forStreamId:]
+ -[LBAudioStreamProvider forwardUserSpeakingEndWithSecondsFromEnd:lastPacketIndex:forStreamId:]
+ -[LBAudioStreamProvider previousPacketHostTimesBaseIndex]
+ -[LBAudioStreamProvider previousPacketHostTimes]
+ -[LBAudioStreamProvider previousStreamId]
+ -[LBAudioStreamProvider setPreviousPacketHostTimes:]
+ -[LBAudioStreamProvider setPreviousPacketHostTimesBaseIndex:]
+ -[LBAudioStreamProvider setPreviousStreamId:]
+ -[LBLocalSpeechRecognitionSettings applicationProcessIdentifier]
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:applicationProcessIdentifier:]
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:applicationProcessIdentifier:]
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:applicationProcessIdentifier:isAudioSourceRemote:]
+ -[LBLocalSpeechRecognitionSettings isAudioSourceRemote]
+ GCC_except_table185
+ GCC_except_table338
+ GCC_except_table355
+ GCC_except_table480
+ GCC_except_table484
+ GCC_except_table493
+ GCC_except_table503
+ GCC_except_table587
+ OBJC_IVAR_$_LBAudioStreamProvider._previousPacketHostTimes
+ OBJC_IVAR_$_LBAudioStreamProvider._previousPacketHostTimesBaseIndex
+ OBJC_IVAR_$_LBAudioStreamProvider._previousStreamId
+ OBJC_IVAR_$_LBLocalSpeechRecognitionSettings._applicationProcessIdentifier
+ OBJC_IVAR_$_LBLocalSpeechRecognitionSettings._isAudioSourceRemote
+ ___94-[LBAudioStreamProvider forwardUserSpeakingEndWithSecondsFromEnd:lastPacketIndex:forStreamId:]_block_invoke
+ _objc_msgSend$_anchorHostTimeForPacketIndex:inHostTimes:baseIndex:
+ _objc_msgSend$_forwardUserSpeakingEndWithSecondsFromEnd:lastPacketIndex:forStreamId:
+ _objc_msgSend$forwardUserSpeakingEndAtHostTime:forStreamId:
+ _objc_msgSend$initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:applicationProcessIdentifier:
+ _objc_msgSend$initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:applicationProcessIdentifier:
+ _objc_msgSend$initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:applicationProcessIdentifier:isAudioSourceRemote:
+ _objc_msgSend$isEqual:
- +[LBLocalSpeechRecognitionSettings companionSettingsWithRequestId:inputOrigin:]
- +[LBLocalSpeechRecognizerTurnFinalizedContext supportsSecureCoding]
- -[LBAudioStreamProvider _anchorHostTimeForPacketIndex:]
- -[LBLocalSpeechRecognizerClient turnFinalizedwithContext:]
- -[LBLocalSpeechRecognizerTurnFinalizedContext .cxx_destruct]
- -[LBLocalSpeechRecognizerTurnFinalizedContext copyWithZone:]
- -[LBLocalSpeechRecognizerTurnFinalizedContext description]
- -[LBLocalSpeechRecognizerTurnFinalizedContext encodeWithCoder:]
- -[LBLocalSpeechRecognizerTurnFinalizedContext initWithCoder:]
- -[LBLocalSpeechRecognizerTurnFinalizedContext initWithRequestId:selectedTrpId:runtimeType:selectedRuntime:]
- -[LBLocalSpeechRecognizerTurnFinalizedContext requestId]
- -[LBLocalSpeechRecognizerTurnFinalizedContext runtimeType]
- -[LBLocalSpeechRecognizerTurnFinalizedContext selectedRuntime]
- -[LBLocalSpeechRecognizerTurnFinalizedContext selectedTrpId]
- GCC_except_table187
- GCC_except_table334
- GCC_except_table348
- GCC_except_table473
- GCC_except_table477
- GCC_except_table486
- GCC_except_table496
- GCC_except_table591
- OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._requestId
- OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._runtimeType
- OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._selectedRuntime
- OBJC_IVAR_$_LBLocalSpeechRecognizerTurnFinalizedContext._selectedTrpId
- _OBJC_CLASS_$_LBLocalSpeechRecognizerTurnFinalizedContext
- _OBJC_METACLASS_$_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_$_CLASS_METHODS_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_$_CLASS_PROP_LIST_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_$_INSTANCE_METHODS_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_$_INSTANCE_VARIABLES_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_$_PROP_LIST_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_CLASS_PROTOCOLS_$_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_CLASS_RO_$_LBLocalSpeechRecognizerTurnFinalizedContext
- __OBJC_METACLASS_RO_$_LBLocalSpeechRecognizerTurnFinalizedContext
- ___58-[LBLocalSpeechRecognizerClient turnFinalizedwithContext:]_block_invoke
- _objc_msgSend$_anchorHostTimeForPacketIndex:
- _objc_msgSend$forwardUserSpeakingEndAtHostTime:
- _objc_msgSend$initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:
- _objc_msgSend$turnFinalizedwithContext:
CStrings:
+ "%s #stream LBAudioStreamProvider DROP legacy USE, no live stream to attribute it to"
+ "%s #stream LBAudioStreamProvider DROP nil streamId"
+ "%s #stream LBAudioStreamProvider DROP no packet hostTimes tracked for streamId=%@ (stream may not have produced packets yet)"
+ "%s #stream LBAudioStreamProvider DROP unknown streamId=%@ (current=%@, previous=%@)"
+ "%s #stream LBAudioStreamProvider ENTRY (legacy, no streamId) secondsFromEnd=%f lastPacketIndex=%llu"
+ "%s #stream LBAudioStreamProvider ENTRY secondsFromEnd=%f lastPacketIndex=%llu streamId=%@"
+ "%s #stream LBAudioStreamProvider XPC SEND useHostTime=%llu (anchorHostTime=%llu, secondsFromEnd=%f, streamId=%@, stream=%{public}@)"
+ "-[LBAudioStreamProvider _anchorHostTimeForPacketIndex:inHostTimes:baseIndex:]"
+ "-[LBAudioStreamProvider _forwardUserSpeakingEndWithSecondsFromEnd:lastPacketIndex:forStreamId:]"
+ "-[LBAudioStreamProvider forwardUserSpeakingEndWithSecondsFromEnd:lastPacketIndex:forStreamId:]"
+ "-[LBAudioStreamProvider forwardUserSpeakingEndWithSecondsFromEnd:lastPacketIndex:forStreamId:]_block_invoke"
+ "ContinuityEndReceived"
+ "Dismissal"
+ "LBLocalSpeechRecognitionSettings:::applicationProcessIdentifier"
+ "LBLocalSpeechRecognitionSettings:::isAudioSourceRemote"
+ "NoTRPArrived"
+ "SpeechRecognitionDelayedStart"
+ "[applicationProcessIdentifier = %ld]"
+ "[isAudioSourceRemote = %@]"
+ "current"
+ "previous"
- "%s #stream LBAudioStreamProvider DROP no packet hostTimes tracked (stream may not have produced packets yet)"
- "%s #stream LBAudioStreamProvider ENTRY secondsFromEnd=%f lastPacketIndex=%llu"
- "%s #stream LBAudioStreamProvider XPC SEND useHostTime=%llu (anchorHostTime=%llu, secondsFromEnd=%f)"
- "%s LBLocalSpeechRecognizerClient[%@], xpcConnection[%@]:TurnFinalizedContext : %@"
- "-[LBAudioStreamProvider _anchorHostTimeForPacketIndex:]"
- "-[LBLocalSpeechRecognizerClient turnFinalizedwithContext:]_block_invoke"
- "LBLocalSpeechRecognizerTurnFinalizedContext:::requestId"
- "LBLocalSpeechRecognizerTurnFinalizedContext:::runtimeType"
- "LBLocalSpeechRecognizerTurnFinalizedContext:::selectedRuntime"
- "LBLocalSpeechRecognizerTurnFinalizedContext:::selectedTrpId"
```
