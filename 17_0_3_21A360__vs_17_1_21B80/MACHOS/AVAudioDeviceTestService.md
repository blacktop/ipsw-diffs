## AVAudioDeviceTestService

> `/System/Library/Frameworks/AVFAudio.framework/XPCServices/AVAudioDeviceTestService.xpc/AVAudioDeviceTestService`

```diff

-629.1.6.0.0
-  __TEXT.__text: 0xd2e4
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_stubs: 0x1a60
-  __TEXT.__objc_methlist: 0x774
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x192c
-  __TEXT.__objc_methname: 0x1eaa
-  __TEXT.__cstring: 0x498
-  __TEXT.__objc_classname: 0x10e
-  __TEXT.__objc_methtype: 0x481
-  __TEXT.__oslogstring: 0xdaf
-  __TEXT.__unwind_info: 0x390
+629.2.7.0.0
+  __TEXT.__text: 0xdbbc
+  __TEXT.__auth_stubs: 0x630
+  __TEXT.__objc_stubs: 0x1ac0
+  __TEXT.__objc_methlist: 0x784
+  __TEXT.__const: 0xe0
+  __TEXT.__gcc_except_tab: 0x1a24
+  __TEXT.__cstring: 0x567
+  __TEXT.__oslogstring: 0xe48
+  __TEXT.__objc_methname: 0x1f00
+  __TEXT.__objc_classname: 0x10f
+  __TEXT.__objc_methtype: 0x4ae
+  __TEXT.__unwind_info: 0x3b4
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x418
-  __DATA_CONST.__cfstring: 0x620
+  __DATA_CONST.__auth_got: 0x330
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__cfstring: 0x6a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x12f8
-  __DATA.__objc_selrefs: 0x828
+  __DATA.__objc_selrefs: 0x848
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0xe0
   __DATA.__objc_superrefs: 0x28
   __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 192
-  Symbols:   164
-  CStrings:  600
+  Functions: 195
+  Symbols:   169
+  CStrings:  619
 
Symbols:
+ _AVAudioSessionCategoryPlayback
+ _CFPreferencesCopyAppValue
+ _CFRelease
+ ___assert_rtn
+ _kCFBooleanTrue
CStrings:
+ "%25s:%-5d Playing tone above amplitude of 1.0. { amplitude=%f }"
+ "%25s:%-5d Updating current audio session category to playback only."
+ "%25s:%-5d Volume not as expected, updating volume. { current=%f, expected=%f }"
+ "%25s:%-5d collecting input tap data %@"
+ "-\x14"
+ "-[AVAudioDeviceTestService playbackTone:completion:]_block_invoke_3"
+ "/tmp/multichannel_mixer_out.caf"
+ "@\"NSNumber\""
+ "PulseTone.mm"
+ "T@\"NSNumber\",&,N,V_userVolumeBeforeHearingTest"
+ "Td,N,V_startDelay"
+ "_startDelay"
+ "_userVolumeBeforeHearingTest"
+ "atpt"
+ "averagePowerPerChannel"
+ "com.apple.coreaudio.avaudiodevicetest"
+ "didWrite"
+ "err == nil"
+ "initWithFloat:"
+ "isMixerOutputEnabled"
+ "mixer_output_enable"
+ "setCategory:error:"
+ "setStartDelay:"
+ "setUserVolumeBeforeHearingTest:"
+ "setupAudioSessionFor:playbackOnly:completion:"
+ "setupVolumeObserverForVolume:completion:"
+ "startDelay"
+ "userVolumeBeforeHearingTest"
+ "v28@0:8f16@?20"
+ "v36@0:8@16B24@?28"
- "%25s:%-5d Volume was changed and not as expected, updating volume. { changedTo=%f, expected=%f }"
- "=\x13"
- "Tf,N,V_hearingTestToneVolume"
- "Tf,N,V_originalHearingTestVolume"
- "_hearingTestToneVolume"
- "_originalHearingTestVolume"
- "hearingTestToneVolume"
- "originalHearingTestVolume"
- "setHearingTestToneVolume:"
- "setOriginalHearingTestVolume:"
- "setupAudioSessionFor:completion:"
- "setupVolumeObserver:"

```
