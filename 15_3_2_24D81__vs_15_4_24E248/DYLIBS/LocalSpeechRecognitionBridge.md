## LocalSpeechRecognitionBridge

> `/System/Library/PrivateFrameworks/LocalSpeechRecognitionBridge.framework/Versions/A/LocalSpeechRecognitionBridge`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0xbca4
+3404.82.3.0.0
+  __TEXT.__text: 0xbf04
   __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_methlist: 0x7f8
+  __TEXT.__objc_methlist: 0xbfc
+  __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__const: 0x1b0
   __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__cstring: 0x1f82
+  __TEXT.__cstring: 0x1fb4
   __TEXT.__oslogstring: 0xacf
-  __TEXT.__dlopen_cstrs: 0xb0
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_classname: 0x14b
-  __TEXT.__objc_methname: 0x40e6
-  __TEXT.__objc_methtype: 0xe10
-  __TEXT.__objc_stubs: 0x1320
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__objc_methname: 0x43db
+  __TEXT.__objc_methtype: 0xee9
+  __TEXT.__objc_stubs: 0x1360
+  __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x738
+  __DATA_CONST.__objc_selrefs: 0x7f0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__auth_got: 0x138
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0xae0
-  __AUTH_CONST.__objc_const: 0x1798
+  __AUTH_CONST.__cfstring: 0xb00
+  __AUTH_CONST.__objc_const: 0x10c8
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0xc8
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x370
   __DATA.__bss: 0x48
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 731A03AA-3D6B-37FC-971F-5C6E202122E7
-  Functions: 233
-  Symbols:   639
-  CStrings:  768
+  UUID: 9B3D216C-73E5-3AC4-AB94-4B6417733371
+  Functions: 237
+  Symbols:   647
+  CStrings:  778
 
Symbols:
+ -[LBLocalSpeechRecognitionSettings activeUserInfo]
+ -[LBLocalSpeechRecognitionSettings initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:]
+ -[LBLocalSpeechRecognizerClient sendVisualContextAndCorrectionsInfo:interactionIdentifier:]
+ GCC_except_table108
+ GCC_except_table161
+ GCC_except_table228
+ OBJC_IVAR_$_LBLocalSpeechRecognitionSettings._activeUserInfo
+ _OBJC_CLASS_$_AFSpeechVisualContextAndCorrectionsInfo
+ ___91-[LBLocalSpeechRecognizerClient sendVisualContextAndCorrectionsInfo:interactionIdentifier:]_block_invoke
+ _objc_msgSend$initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:
+ _objc_msgSend$sendVisualContextAndCorrectionsInfo:interactionIdentifier:
- GCC_except_table106
- GCC_except_table159
- GCC_except_table224
CStrings:
+ "@\"AFASRSharedUserInfo\""
+ "@236@0:8@16@24Q32Q40@48@56@64@72B80B84B88B92d96@104B112B116B120B124@128B136@140@148@156@164@172@180B188Q192q200@208B216@220@228"
+ "LBLocalSpeechRecognitionSettings:::activeUserInfo"
+ "T@\"AFASRSharedUserInfo\",R,N,V_activeUserInfo"
+ "Vv32@0:8@\"AFSpeechVisualContextAndCorrectionsInfo\"16@\"NSString\"24"
+ "_activeUserInfo"
+ "activeUserInfo"
+ "initWithRequestId:inputOrigin:speechRecognitionTaskName:speechRecognitionMode:location:jitGrammar:overrideModelPath:applicationName:detectUtterances:continuousListening:shouldHandleCapitalization:secureOfflineOnly:maximumRecognitionDuration:recognitionOverrides:shouldStoreAudioOnDevice:deliverEagerPackage:enableEmojiRecognition:enableAutoPunctuation:UILanguage:enableVoiceCommands:dictationUIInteractionId:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:shouldStartAudioCapture:audioCaptureStartHostTime:audioRecordType:audioRecordDeviceId:shouldGenerateVoiceCommandCandidates:asrLocale:activeUserInfo:"
+ "sendVisualContextAndCorrectionsInfo:interactionIdentifier:"

```
