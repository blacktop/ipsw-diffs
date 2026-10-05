## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/LocalSpeechRecognitionBridge`

```diff

-3605.25.1.0.0
-  __TEXT.__text: 0x1d3d0
-  __TEXT.__objc_methlist: 0x2514
+3605.31.3.0.0
+  __TEXT.__text: 0x1d498
+  __TEXT.__objc_methlist: 0x2524
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__const: 0xb0
   __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__cstring: 0x4a7f
+  __TEXT.__cstring: 0x4b12
   __TEXT.__oslogstring: 0x2d3e
   __TEXT.__unwind_info: 0x900
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x860
+  __DATA_CONST.__const: 0x870
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_selrefs: 0x1368
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x1e8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x3d58
+  __AUTH_CONST.__cfstring: 0x1b80
+  __AUTH_CONST.__objc_const: 0x3d88
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0x8b0
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x58

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 744
-  Symbols:   1485
-  CStrings:  612
+  Functions: 745
+  Symbols:   1487
+  CStrings:  617
 
Symbols:
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:applicationProcessIdentifier:isAudioSourceRemote:]
+ -[LBLocalSpeechRecognitionSettings isAudioSourceRemote]
+ GCC_except_table668
+ GCC_except_table703
+ GCC_except_table708
+ GCC_except_table713
+ _OBJC_IVAR_$_LBLocalSpeechRecognitionSettings._isAudioSourceRemote
- +[LBLocalSpeechRecognitionSettings companionSettingsWithRequestId:inputOrigin:]
- GCC_except_table667
- GCC_except_table702
- GCC_except_table707
- GCC_except_table712
Functions:
~ -[LBLocalSpeechRecognitionSettings description] : 1088 -> 1120
~ -[LBLocalSpeechRecognitionSettings encodeWithCoder:] : 1240 -> 1284
~ -[LBLocalSpeechRecognitionSettings initWithCoder:] : 2200 -> 2256
- +[LBLocalSpeechRecognitionSettings companionSettingsWithRequestId:inputOrigin:]
~ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:applicationProcessIdentifier:] : 1088 -> 260
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:messagesContext:sessionId:isLinwoodEnabled:applicationProcessIdentifier:isAudioSourceRemote:]
+ -[LBLocalSpeechRecognitionSettings applicationProcessIdentifier]
CStrings:
+ "ContinuityEndReceived"
+ "LBLocalSpeechRecognitionSettings:::isAudioSourceRemote"
+ "NoTRPArrived"
+ "SpeechRecognitionDelayedStart"
+ "[isAudioSourceRemote = %@]"
```
