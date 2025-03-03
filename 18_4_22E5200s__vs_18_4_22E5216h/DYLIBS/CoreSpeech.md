## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3404.71.4.1.1
-  __TEXT.__text: 0x157f10
+3404.79.2.0.0
+  __TEXT.__text: 0x158404
   __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x15444
+  __TEXT.__objc_methlist: 0x15494
   __TEXT.__const: 0x5e0
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__gcc_except_tab: 0x3fc8
-  __TEXT.__cstring: 0x2710c
-  __TEXT.__oslogstring: 0x1f8cd
-  __TEXT.__unwind_info: 0x5028
-  __TEXT.__objc_classname: 0x2e97
-  __TEXT.__objc_methname: 0x383ea
-  __TEXT.__objc_methtype: 0x7c61
-  __TEXT.__objc_stubs: 0x1c500
-  __DATA_CONST.__got: 0x1ab0
-  __DATA_CONST.__const: 0x4130
+  __TEXT.__gcc_except_tab: 0x3fd4
+  __TEXT.__cstring: 0x27205
+  __TEXT.__oslogstring: 0x1f90f
+  __TEXT.__unwind_info: 0x5030
+  __TEXT.__objc_classname: 0x2e98
+  __TEXT.__objc_methname: 0x3855c
+  __TEXT.__objc_methtype: 0x7c6c
+  __TEXT.__objc_stubs: 0x1c580
+  __DATA_CONST.__got: 0x1aa8
+  __DATA_CONST.__const: 0x4190
   __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaa10
+  __DATA_CONST.__objc_selrefs: 0xaa38
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x450
   __AUTH_CONST.__auth_got: 0xe10
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1e20
-  __AUTH_CONST.__cfstring: 0x8f40
-  __AUTH_CONST.__objc_const: 0x21b68
+  __AUTH_CONST.__const: 0x1e00
+  __AUTH_CONST.__cfstring: 0x9000
+  __AUTH_CONST.__objc_const: 0x21b98
   __AUTH_CONST.__objc_intobj: 0xa20
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_floatobj: 0x4c0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1a7c
+  __DATA.__objc_ivar: 0x1a80
   __DATA.__data: 0x3650
-  __DATA.__bss: 0x668
-  __DATA.__common: 0x18
+  __DATA.__bss: 0x660
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x5050
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x180

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8265
-  Symbols:   10078
-  CStrings:  14559
+  Functions: 8273
+  Symbols:   10084
+  CStrings:  14570
 
Symbols:
+ _AVAudioSessionModeSpeechRecognition
+ _CSSiriSpeechRecordingRecordedAudioAppContainerName
- _CSLogContextFacilityCoreSpeechExclave
- _CSSecureLogInitIfNeeded
- _OBJC_CLASS_$_AFMyriadGoodnessScoreOverrideState
- _OBJC_CLASS_$_SCDAGoodnessScoreOverrideState
CStrings:
+ "%s Detected 2nd-pass trigger at %{public}llu, KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s Rejected 2nd-pass KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s Unable to access app container group"
+ "-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke_3"
+ "-[CSVoiceIdXPCClient _notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke_2"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke"
+ ".\x11"
+ "Detected"
+ "NearMiss"
+ "Rejected"
+ "StrongAccept"
+ "StrongReject"
+ "URLByAppendingPathComponent:isDirectory:"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSURL\">24"
+ "WeakAccept"
+ "WeakReject"
+ "_handleImplicitUtteranceMessage:client:"
+ "_notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "_processSecondPassInExclave:rejectBlock:"
+ "_siriLanguageCode"
+ "appContainerName"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "convertSecureVoiceTriggerKeywordDetectionResultTypeToString:"
+ "convertSecureVoiceTriggerSpeakerDetectionResultTypeToString:"
+ "getBestSupportedSiriLanguageWithFallback:"
+ "group.com.apple.siri.recorded-audio"
+ "notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "setCategory:mode:options:error:"
+ "v24@?0@\"NSString\"8@\"NSURL\"16"
+ "v60@?0Q8d16I24Q28Q36Q44Q52"
+ "v68@?0Q8Q16d24I32Q36Q44Q52Q60"
- "%s ::: CoreSpeech Secure logging initialized"
- "%s Detected 2nd-pass trigger at %{public}llu"
- "%s Overriding Myriad state as request was made during a ringtone"
- "-[CSVoiceIdXPCClient _notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke_2"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke"
- "CSSecureLogInitIfNeeded_block_invoke"
- "ExclaveKit"
- "Trigger was during a ringtone"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSURL\">24"
- "_notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
- "_processSecondPassInExclave:"
- "bestSupportedLanguageCodeForLanguageCode:"
- "com.apple.corespeech"
- "exclave-built-in"
- "initWithOverrideOption:reason:"
- "setCategory:withOptions:error:"
- "setOverrideState:"
- "v16@?0@\"NSURL\"8"
- "v44@?0Q8d16I24Q28Q36"
- "v52@?0Q8Q16d24I32Q36Q44"

```
