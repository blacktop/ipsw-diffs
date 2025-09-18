## com.apple.SpeechRecognitionCore.speechrecognitiond

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/XPCServices/com.apple.SpeechRecognitionCore.brokerd.xpc/XPCServices/com.apple.SpeechRecognitionCore.speechrecognitiond.xpc/com.apple.SpeechRecognitionCore.speechrecognitiond`

```diff

-6.2.82.3.0
-  __TEXT.__text: 0xa6cf4
-  __TEXT.__auth_stubs: 0x18b0
-  __TEXT.__objc_stubs: 0x2e00
+6.2.83.3.0
+  __TEXT.__text: 0xa9798
+  __TEXT.__auth_stubs: 0x18c0
+  __TEXT.__objc_stubs: 0x2f00
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xad8
-  __TEXT.__cstring: 0x2ed4
-  __TEXT.__objc_methname: 0x3576
-  __TEXT.__objc_classname: 0x1b6
-  __TEXT.__objc_methtype: 0xb52
+  __TEXT.__objc_methlist: 0xc18
+  __TEXT.__cstring: 0x2f19
+  __TEXT.__objc_methname: 0x3756
+  __TEXT.__objc_classname: 0x1ce
+  __TEXT.__objc_methtype: 0xb6d
   __TEXT.__const: 0x5605
-  __TEXT.__oslogstring: 0x3919
-  __TEXT.__gcc_except_tab: 0x6d88
+  __TEXT.__oslogstring: 0x3ccf
+  __TEXT.__gcc_except_tab: 0x6d60
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x3e9c
+  __TEXT.__unwind_info: 0x3e58
   __TEXT.__eh_frame: 0x1a0
-  __DATA_CONST.__auth_got: 0xc70
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_got: 0xc78
+  __DATA_CONST.__got: 0x3a0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x6340
-  __DATA_CONST.__cfstring: 0x1ae0
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0x63a0
+  __DATA_CONST.__cfstring: 0x1b40
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x80
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x2228
-  __DATA.__objc_selrefs: 0xd60
-  __DATA.__objc_classrefs: 0x1e8
-  __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__objc_data: 0x3c0
+  __DATA.__objc_const: 0x2428
+  __DATA.__objc_selrefs: 0xdb0
+  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_data: 0x410
   __DATA.__data: 0x790
-  __DATA.__bss: 0x9d8
+  __DATA.__bss: 0x9e0
   __DATA.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2AC5BA09-3134-342B-8298-FC645F04ACC4
-  Functions: 3203
-  Symbols:   1110
-  CStrings:  1936
+  UUID: 8B7ED7BD-FB5E-356B-9096-A686D4136725
+  Functions: 3258
+  Symbols:   1116
+  CStrings:  1986
 
Symbols:
+ _AVAudioSessionCategoryRecord
+ _CFPreferencesSetAppValue
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_AVAudioSessionRouteControl
+ _OBJC_CLASS_$_AVIndependentSoundInput
+ _OBJC_METACLASS_$_AVIndependentSoundInput
+ _RXIsUseIndependentVADEnabled
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_
+ _kCFBooleanFalse
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strERKNS_12basic_stringIcS2_S4_EE
CStrings:
+ "@\"AVIndependentSoundInput\""
+ "AVI::Audio configuration changed = %@"
+ "AVI:AV activateNotifications"
+ "AVI:AV deactivateNotifications"
+ "AVI:AV is already running"
+ "AVI:AVAudioSession set active failed with error code:{%@}, error message: {%@}"
+ "AVI:Audio Session already active"
+ "AVI:Could not drain converter %@"
+ "AVI:Could not run audio converter %@"
+ "AVI:ERROR in setting up the audio session"
+ "AVI:Error Starting engine: %@"
+ "AVI:Error setting audio session category: %@"
+ "AVI:Error setting haptics and sounds during recording: %@"
+ "AVI:Error setting preffered route: %@"
+ "AVI:No audio input available, channel count 0"
+ "AVI:Started Recording from AV"
+ "AVI:StopRecording from AV"
+ "AVI:System is sleeping, so don't start recording"
+ "AVI:no independent route"
+ "AVI:releasing audio engine"
+ "AVI:startRecording"
+ "AVI:stopRecording : error stopping AVAudioSession: %@"
+ "AVI:stopRunningAudioEngine"
+ "AVIndependentSoundInput"
+ "Device supports independent route"
+ "ExclaveCapability"
+ "RDSoundInputImpl_iOS_Independent_AV.m"
+ "RDSoundInputiOS::Dealloc"
+ "RDSoundInputiOS::Init"
+ "RDSoundInputiOS::StartRecording"
+ "RDSoundInputiOS::StopRecording"
+ "RXUsingIndependentVAD"
+ "T@\"AVIndependentSoundInput\",&,N,V_avIndependenRouteSoundInput"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,V_audioSessionSetupCompleted"
+ "TB,R,N,V_hasIndependentRouteCapability"
+ "_audioSessionSetupCompleted"
+ "_avIndependenRouteSoundInput"
+ "_hasIndependentRouteCapability"
+ "audioSessionSetupCompleted"
+ "avIndependenRouteSoundInput"
+ "availableInputs"
+ "hasIndependentRouteCapability"
+ "init:delegate:silenceLookback:silenceExpect:batchDecode:enableAudioDebugging:"
+ "preferredRouteControlConfig"
+ "routeControlOptions"
+ "setAvIndependenRouteSoundInput:"
+ "setPreferredRouteControlConfig:error:"
+ "setRouteControlOptions:"
+ "stopRunningAudioEngine"
- "_compact"
- "initWithConfig:keywordsWithPhonemes:delegate:silenceLookback:silenceExpect:batchDecode:enableAudioDebugging:"
- "~Stop recording"

```
