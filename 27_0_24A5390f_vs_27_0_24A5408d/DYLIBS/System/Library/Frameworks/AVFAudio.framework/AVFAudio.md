## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/AVFAudio`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-794.0.0.0.0
-  __TEXT.__text: 0x113af0
+794.106.0.0.0
+  __TEXT.__text: 0x113d98
   __TEXT.__realtime: 0x1d20
   __TEXT.__objc_methlist: 0x5b1c
   __TEXT.__dlopen_cstrs: 0xa9
   __TEXT.__const: 0xb80
-  __TEXT.__cstring: 0xfe95
+  __TEXT.__cstring: 0xfe65
   __TEXT.__swift5_typeref: 0x256
   __TEXT.__swift5_reflstr: 0x109
   __TEXT.__swift5_assocty: 0x78

   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x12560
-  __TEXT.__oslogstring: 0x180ed
+  __TEXT.__gcc_except_tab: 0x12568
+  __TEXT.__oslogstring: 0x18210
   __TEXT.__unwind_info: 0x6318
   __TEXT.__eh_frame: 0x2e0
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 4136
   Symbols:   9070
-  CStrings:  3368
+  CStrings:  3370
 
Functions:
~ -[AVVCSessionManager setSessionCategoryModeOptionsForActivationMode:withOptions:] : 3844 -> 3852
~ -[AVVCSessionManager setSessionAudioHWControlFlagsForActivationMode:withOptions:] : 3228 -> 3232
~ -[AVAudioBuffer initWithFormat:byteCapacity:] : 492 -> 588
~ -[AVVCSessionManager setDuckOthers:mixWithOthers:error:] : 1216 -> 1224
~ -[AVAudioBuffer mutableCopyWithZone:] : 212 -> 216
~ -[AVAudioPCMBuffer mutableCopyWithZone:] : 232 -> 236
~ ___68-[AVVoiceTriggerClient enableSpeakerStateListening:completionBlock:]_block_invoke.205 : 364 -> 368
~ __ZN17AVAudioEngineImpl5PauseEPP7NSError : 364 -> 640
~ __ZN17AVAudioEngineImpl4StopEPP7NSError : 592 -> 868
CStrings:
+ "%25s:%-5d AVVCSessionManager::setSessionAudioHWControlFlags: HW control flags will be set implicitly as per MX policy on ATV"
+ "%25s:%-5d Engine@%p: error pausing engine, was running %d, is running %d, error = %d"
+ "%25s:%-5d Engine@%p: error stopping engine, was running %d, is running %d, error = %d"
+ "%25s:%-5d failed to allocate ExtendedAudioBufferList (numBuffers=%d, byteCapacity=%u)"
+ "false == isDeviceIORunning"
- "%25s:%-5d AVVCSessionManager::setSessionAudioHWControlFlags: Take Audio HW control on tvOS"
- "ExtendedAudioBufferList_CreateWithFormat failed"
- "false == AUI().IsRunning()"
```
