## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-835.13.1.11.1
-  __TEXT.__text: 0x709b4
+835.16.1.0.0
+  __TEXT.__text: 0x71818
   __TEXT.__auth_stubs: 0x2c60
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0xcc8
   __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x1d4ea
+  __TEXT.__cstring: 0x1d597
   __TEXT.__oslogstring: 0x6c
-  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__unwind_info: 0x12e8
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x68f
+  __TEXT.__objc_methname: 0x689
   __TEXT.__objc_methtype: 0x25
   __TEXT.__objc_stubs: 0x880
   __DATA_CONST.__got: 0x600
-  __DATA_CONST.__const: 0x1a98
+  __DATA_CONST.__const: 0x1a80
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220

   __AUTH.__data: 0x188
   __DATA.__objc_ivar: 0xc
   __DATA.__data: 0x1a38
-  __DATA.__bss: 0x908
+  __DATA.__bss: 0x8f0
   __DATA_DIRTY.__data: 0x780
-  __DATA_DIRTY.__bss: 0x4b0
+  __DATA_DIRTY.__bss: 0x4c8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1584
-  Symbols:   2654
-  CStrings:  2911
+  Functions: 1590
+  Symbols:   2655
+  CStrings:  2913
 
Symbols:
+ _kAPSEndpointStreamAudioHoseSBARNotification_AudioFormatChanged
+ _kAPSRadarLoggingComponent_AirPlayAudioBuffered
+ _kAPSRadarLoggingComponent_AirPlayAudioStreaming
+ _kAPSRadarLoggingComponent_CoreMediaBufferedAirPlay
- _kAPSEndpointStreamAudioHoseSBARNotification_EnqueuedAudioFormatChanged
- _kAPSRadarLoggingComponent_AirPlayAudio
- _kAPSRadarLoggingComponent_CoreMediaAPMusic
CStrings:
+ "1158817"
+ "1158818"
+ "AirPlay Audio - Buffered"
+ "AirPlay Audio - Streaming"
+ "CoreMedia Buffered AirPlay"
+ "NewAudioFormat"
+ "[%!{(MISSING)ptr}] TimedManagerTimerTriggerNotification: AudioFormat changed to %!s(MISSING)"
+ "[%!{(MISSING)ptr}] hoseSBAR_scheduleHandlingFormatChangeForAudioSessionOnTimer synchronizerTimebase=%!f(MISSING), OPTS=%!f(MISSING), newAudioFormat=%!s(MISSING)"
+ "componentEntryWithName:version:ID:"
+ "hoseSBAR_handleFormatChangeForAudioSession"
+ "hoseSBAR_scheduleFormatChangeHandlingForAudioSessionOnTimer"
+ "hoseSBAR_timedManagerTimerTriggerNotification"
+ "setObject:forKeyedSubscript:"
+ "void hoseSBAR_scheduleFormatChangeHandlingForAudioSessionOnTimer(APSEndpointStreamAudioHoseSBARRef, CMTime, Boolean)"
- "855786"
- "AirPlay Audio"
- "ChannelCount"
- "CoreMedia AP Music"
- "PrefersMultiChannel"
- "SampleRate"
- "[%!{(MISSING)ptr}] TimedManagerTimerTriggerNotification"
- "[%!{(MISSING)ptr}] scheduleSetPreferencesOnAudioSessionOnTimer synchronizerTimebase=%!f(MISSING), OPTS=%!f(MISSING), ChannelCount=%!u(MISSING)"
- "componentEntryWithName:componentVersion:componentID:"
- "hoseSBAR_scheduleSetPreferencesOnAudioSessionOnTimer"
- "setValue:forKey:"
- "void hoseSBAR_scheduleSetPreferencesOnAudioSessionOnTimer(APSEndpointStreamAudioHoseSBARRef, CMTime, Boolean)"

```
