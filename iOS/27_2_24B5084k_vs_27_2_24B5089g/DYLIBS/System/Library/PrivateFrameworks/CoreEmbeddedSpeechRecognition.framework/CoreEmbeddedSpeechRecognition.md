## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`

```diff

-3605.10.1.0.0
-  __TEXT.__text: 0x33893c
-  __TEXT.__objc_methlist: 0x4ec0
-  __TEXT.__const: 0x8d48
-  __TEXT.__cstring: 0xe7ad
+3605.12.1.0.0
+  __TEXT.__text: 0x33ac9c
+  __TEXT.__objc_methlist: 0x4ee8
+  __TEXT.__const: 0x8d28
+  __TEXT.__cstring: 0xe80d
   __TEXT.__gcc_except_tab: 0xd80
-  __TEXT.__oslogstring: 0xd065
+  __TEXT.__oslogstring: 0xd0c5
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0xdc
-  __TEXT.__swift5_typeref: 0x43ae
+  __TEXT.__swift5_typeref: 0x43a6
   __TEXT.__constg_swiftt: 0x27f4
   __TEXT.__swift5_reflstr: 0x2b93
   __TEXT.__swift5_fieldmd: 0x2910

   __TEXT.__swift5_assocty: 0x528
   __TEXT.__swift5_proto: 0x4e4
   __TEXT.__swift5_types: 0x2b0
-  __TEXT.__swift5_capture: 0xc994
+  __TEXT.__swift5_capture: 0xc9e4
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0x260
   __TEXT.__swift_as_ret: 0x2dc
   __TEXT.__swift_as_cont: 0x6e4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xb4e0
+  __TEXT.__unwind_info: 0xb500
   __TEXT.__eh_frame: 0x5dec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d88
+  __DATA_CONST.__const: 0x1d90
   __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3878
+  __DATA_CONST.__objc_selrefs: 0x3890
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x478
-  __DATA_CONST.__got: 0x1ae0
-  __AUTH_CONST.__const: 0x233d8
-  __AUTH_CONST.__cfstring: 0x5140
-  __AUTH_CONST.__objc_const: 0xb978
+  __DATA_CONST.__got: 0x1ac0
+  __AUTH_CONST.__const: 0x234a0
+  __AUTH_CONST.__cfstring: 0x51a0
+  __AUTH_CONST.__objc_const: 0xb9d0
   __AUTH_CONST.__objc_intobj: 0xeb8
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x2360
-  __AUTH.__objc_data: 0x12b8
-  __AUTH.__data: 0xd98
-  __DATA.__objc_ivar: 0x528
-  __DATA.__data: 0x27b0
+  __AUTH_CONST.__auth_got: 0x2358
+  __AUTH.__objc_data: 0x1128
+  __AUTH.__data: 0xb60
+  __DATA.__objc_ivar: 0x530
+  __DATA.__data: 0x2620
   __DATA.__common: 0x108
-  __DATA_DIRTY.__objc_data: 0x1b78
-  __DATA_DIRTY.__data: 0x3e70
-  __DATA_DIRTY.__bss: 0x3f38
+  __DATA_DIRTY.__objc_data: 0x1d08
+  __DATA_DIRTY.__data: 0x42d0
+  __DATA_DIRTY.__bss: 0x4068
   __DATA_DIRTY.__common: 0x188
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11201
-  Symbols:   6428
-  CStrings:  2504
+  Functions: 11211
+  Symbols:   6434
+  CStrings:  2508
 
Symbols:
+ -[CESRSpeechParameters initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:disableEagerLimit:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:messagesContext:sessionIdentifier:applicationProcessIdentifier:isAudioSourceRemote:]
+ -[CESRSpeechParameters isAudioSourceRemote]
+ -[CESRSpeechParameters(InterfaceCompatibility) initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:disableEagerLimit:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:messagesContext:sessionIdentifier:applicationProcessIdentifier:]
+ -[_CESRSpeechParametersMutation setIsAudioSourceRemote:]
+ _OBJC_IVAR_$_CESRSpeechParameters._isAudioSourceRemote
+ _OBJC_IVAR_$__CESRSpeechParametersMutation._isAudioSourceRemote
+ _objc_msgSend$initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:disableEagerLimit:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:messagesContext:sessionIdentifier:applicationProcessIdentifier:isAudioSourceRemote:
+ _objc_msgSend$isAudioSourceRemote
- -[CESRSpeechParameters initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:disableEagerLimit:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:messagesContext:sessionIdentifier:applicationProcessIdentifier:]
- _symbolic _____Sg 6Speech26FoundationModelTranscriberC15ReportingOptionO
CStrings:
+ "CESRSpeechParameters::isAudioSourceRemote"
+ "Skipping on-screen context entity retrieval — audio source is remote for requestId %s"
+ "isAudioSourceRemote"
+ "isAudioSourceRemote = %@"
```
