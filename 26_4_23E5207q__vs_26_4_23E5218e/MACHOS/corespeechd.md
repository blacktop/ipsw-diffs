## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3520.87.3.1.5
-  __TEXT.__text: 0x196b28
+3520.89.1.0.0
+  __TEXT.__text: 0x1973a8
   __TEXT.__auth_stubs: 0x1690
-  __TEXT.__objc_stubs: 0x20840
-  __TEXT.__objc_methlist: 0x19f94
+  __TEXT.__objc_stubs: 0x208e0
+  __TEXT.__objc_methlist: 0x1a064
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0x3bb8
-  __TEXT.__objc_methname: 0x429e1
-  __TEXT.__cstring: 0x2da03
-  __TEXT.__oslogstring: 0x23c58
-  __TEXT.__objc_classname: 0x3722
-  __TEXT.__objc_methtype: 0x8fce
-  __TEXT.__unwind_info: 0x76c0
+  __TEXT.__gcc_except_tab: 0x3bcc
+  __TEXT.__objc_methname: 0x42d56
+  __TEXT.__cstring: 0x2daae
+  __TEXT.__oslogstring: 0x23da8
+  __TEXT.__objc_classname: 0x3747
+  __TEXT.__objc_methtype: 0x900f
+  __TEXT.__unwind_info: 0x76f8
   __DATA_CONST.__auth_got: 0xb60
   __DATA_CONST.__got: 0x1410
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6248
+  __DATA_CONST.__const: 0x62d8
   __DATA_CONST.__cfstring: 0x8fe0
   __DATA_CONST.__objc_classlist: 0x9a0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x530
+  __DATA_CONST.__objc_protolist: 0x538
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf8
   __DATA_CONST.__objc_superrefs: 0x7e8

   __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x560
-  __DATA.__objc_const: 0x29110
-  __DATA.__objc_selrefs: 0xc3b8
-  __DATA.__objc_ivar: 0x1fa8
+  __DATA.__objc_const: 0x29268
+  __DATA.__objc_selrefs: 0xc418
+  __DATA.__objc_ivar: 0x1fb8
   __DATA.__objc_data: 0x6040
-  __DATA.__data: 0x3e40
+  __DATA.__data: 0x3ea0
   __DATA.__bss: 0x710
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 9C516C69-6A74-31B1-A774-6E0F8AF438C9
-  Functions: 9931
+  UUID: 93BC2DAB-B9C0-39B8-85A0-6D2CB018407D
+  Functions: 9949
   Symbols:   1022
-  CStrings:  17652
+  CStrings:  17681
 
CStrings:
+ "%s FirstPassHearstAP doesn't meet listening condition, audioProviderUUID is being set to nil"
+ "%s Forcing speech update event delivery on TRP arrival"
+ "%s Resetting speechUpdateEvent"
+ "%s Unexpected! There are %lu non-VoiceTrigger stream audio providers"
+ "%s VoiceTrigger HearstAP start policy changed : %{public}@, audioProviderUUID: %@"
+ "%s _isFirstTrpDelivered:%u, _firstSpeechEventPostTCUTimestamp:%f"
+ "-[CSAttSiriSpeechPresenceAnalyzer(SpeechDetection) _forceSpeechUpdateOnTRPArrival]"
+ "-[CSVoiceTriggerHearstAPEnabledPolicy _fetchAudioProviderUUID]"
+ "/AppleInternal/Library/BuildRoots/4~CJJLugCDjKLbI_EJpFjkQMMY4OjjUXo5ylB-604/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJJLugCDjKLbI_EJpFjkQMMY4OjjUXo5ylB-604/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "@\"CSVoiceTriggerHearstAPEnabledPolicy\""
+ "CSAudioStreamActivityMonitorDelegate"
+ "CSAudioStreamActivityMonitorDelegate:hasNonVoiceTriggerStreamsActive:audioProviderUUID:"
+ "CSAudioStreamActivityMonitorDelegate:hasNonVoiceTriggerStreamsActive:audioProviderUUIDs:"
+ "T@\"CSVoiceTriggerHearstAPEnabledPolicy\",&,N,V_voiceTriggerHearstAPEnabledPolicy"
+ "T@\"NSArray\",&,N,V_nonVoiceTriggerStreamAudioProviderUUIDs"
+ "TB,N,V_hasNonVoiceTriggerStreamsActive"
+ "TB,N,V_hasNonVoiceTriggerStreamsOrStreamHoldersActive"
+ "_fetchAudioProviderUUID"
+ "_forceSpeechUpdateOnTRPArrival"
+ "_hasNonVoiceTriggerStreamsActive"
+ "_hasNonVoiceTriggerStreamsOrStreamHoldersActive"
+ "_nonVoiceTriggerStreamAudioProviderUUIDs"
+ "_transitHearstAPEnable:withAudioProviderUUID:"
+ "hasNonVoiceTriggerStreamsActive"
+ "isEnabledAndFetchAudioProviderUUID"
+ "nonVoiceTriggerStreamAudioProviderUUIDs"
+ "nonVoiceTriggerStreamsActiveAudioProviderUUIDs"
+ "setHasNonVoiceTriggerStreamsActive:"
+ "setHasNonVoiceTriggerStreamsOrStreamHoldersActive:"
+ "setNonVoiceTriggerStreamAudioProviderUUIDs:"
+ "setVoiceTriggerHearstAPEnabledPolicyCallback:"
+ "v28@?0B8Q12@\"NSString\"20"
+ "v36@0:8@16B24@\"NSArray\"28"
- "%s VoiceTrigger HearstAP start policy changed : %{public}@"
- "/AppleInternal/Library/BuildRoots/4~CIZYugD20eIkpebSvXZVuYZEcjRFrhTqJ5EdxDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIZYugD20eIkpebSvXZVuYZEcjRFrhTqJ5EdxDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "T@\"CSPolicy\",&,N,V_voiceTriggerHearstAPEnabledPolicy"
- "_transitHearstAPEnable:"

```
