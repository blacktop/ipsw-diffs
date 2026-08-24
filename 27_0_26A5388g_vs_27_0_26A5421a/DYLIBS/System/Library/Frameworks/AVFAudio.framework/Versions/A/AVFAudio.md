## AVFAudio

> `/System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio`

```diff

-794.0.0.0.0
-  __TEXT.__text: 0xeecf0
+794.106.0.0.0
+  __TEXT.__text: 0xef2bc
   __TEXT.__realtime: 0x1d80
   __TEXT.__objc_methlist: 0x4eb4
   __TEXT.__const: 0xd20
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x255
-  __TEXT.__cstring: 0xe794
+  __TEXT.__cstring: 0xe7aa
   __TEXT.__constg_swiftt: 0x218
   __TEXT.__swift5_reflstr: 0x102
   __TEXT.__swift5_fieldmd: 0x1c0

   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x14
-  __TEXT.__gcc_except_tab: 0xd70c
-  __TEXT.__oslogstring: 0x141e5
-  __TEXT.__unwind_info: 0x53e0
+  __TEXT.__gcc_except_tab: 0xd7c8
+  __TEXT.__oslogstring: 0x144a9
+  __TEXT.__unwind_info: 0x53e8
   __TEXT.__eh_frame: 0x2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3765
-  Symbols:   8036
-  CStrings:  2868
+  Symbols:   8037
+  CStrings:  2877
 
Symbols:
+ GCC_except_table1863
+ GCC_except_table1865
+ GCC_except_table1867
+ GCC_except_table1874
+ GCC_except_table1878
+ GCC_except_table1883
+ GCC_except_table1885
+ GCC_except_table1889
+ GCC_except_table1891
- GCC_except_table1864
- GCC_except_table1866
- GCC_except_table1868
- GCC_except_table1877
- GCC_except_table1881
- GCC_except_table1884
- GCC_except_table1887
- GCC_except_table1890
Functions:
~ __ZN15AUGraphNodeIOV320DeallocateInputBlockEv : 464 -> 668
~ -[AVAudioBuffer initWithFormat:byteCapacity:] : 496 -> 596
~ -[AVAudioBuffer mutableCopyWithZone:] : 212 -> 216
~ -[AVAudioPCMBuffer mutableCopyWithZone:] : 232 -> 236
~ -[AVVoiceTriggerClient enableVoiceTriggerListening:completionBlock:] : 2800 -> 3148
~ __ZN24AVVoiceTriggerClientImpl42registerAOPVoiceTriggerNotificationHandlerEjb : 372 -> 644
~ __ZN17AVAudioEngineImpl5PauseEPP7NSError : 364 -> 640
~ __ZN17AVAudioEngineImpl4StopEPP7NSError : 592 -> 868
CStrings:
+ "%25s:%-5d Engine@%p: error pausing engine, was running %d, is running %d, error = %d"
+ "%25s:%-5d Engine@%p: error stopping engine, was running %d, is running %d, error = %d"
+ "%25s:%-5d Error: allowing deallocation despite running state mismatch between engine (%d) and underlying device (%d)"
+ "%25s:%-5d enableVoiceTriggerListening: Attempt to (%s) voice trigger failed. AOP unconfigured"
+ "%25s:%-5d enableVoiceTriggerListening: Failed to (%s) voice trigger on device (%d) [err1 (%s) err2 (%s)]"
+ "%25s:%-5d enableVoiceTriggerListening: Voice Trigger is already (%s). Skipping HAL property set"
+ "%25s:%-5d enableVoiceTriggerListening: Voice Trigger successfully (%s) on device (%d)"
+ "%25s:%-5d failed to allocate ExtendedAudioBufferList (numBuffers=%d, byteCapacity=%u)"
+ "%25s:%-5d failure to %s voice trigger on device %d [err (%s)]"
+ "%25s:%-5d registerAOPVoiceTriggerNotificationHandler: AOP voice trigger notifications (%s) on device (%u)"
+ "%25s:%-5d registerAOPVoiceTriggerNotificationHandler: Failed to (%s) AOP voice trigger listener on device (%u). error %s"
+ "enableVoiceTriggerListening"
+ "false == isEngineRunning"
+ "register"
+ "registered"
+ "unregister"
+ "unregistered"
- "%25s:%-5d %s AOP trigger notifications"
- "%25s:%-5d Attempt to %s voice trigger when AOP unconfigured"
- "%25s:%-5d Voice Trigger %s already - ignoring"
- "%25s:%-5d enableVoiceTriggerListening (%s) on device %d"
- "%25s:%-5d failure to %s voice trigger on device %d [err (%d)]"
- "%25s:%-5d failure to %s voice trigger on device %d [err1 (%d) err2 (%d)]"
- "ExtendedAudioBufferList_CreateWithFormat failed"
- "false == AUI().IsRunning()"
```
