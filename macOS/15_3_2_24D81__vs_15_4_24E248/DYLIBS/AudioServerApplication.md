## AudioServerApplication

> `/System/Library/PrivateFrameworks/AudioServerApplication.framework/Versions/A/AudioServerApplication`

```diff

-1020.3.0.0.0
-  __TEXT.__text: 0x11368
+1040.10.0.0.0
+  __TEXT.__text: 0x1114c
   __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_methlist: 0x11ac
   __TEXT.__const: 0x40

   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/Versions/A/AudioToolboxCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7AE76BD9-7A38-3940-9DEA-2D9976DB91D2
+  UUID: 69C25866-1806-3779-B48F-7F6CA7ECE643
   Functions: 385
   Symbols:   796
   CStrings:  893
Functions:
~ -[ASAPlaythrough start] : 668 -> 684
~ _InputOutputProc : 980 -> 972
~ -[ASAPlaythrough _createIOContext] : 2788 -> 2776
~ -[ASAPlaythrough dealloc] : 268 -> 272
~ _CheckAudioBufferList : 104 -> 112
~ _OUTLINED_FUNCTION_1 : 28 -> 16
~ _OUTLINED_FUNCTION_2 : 16 -> 12
~ -[ASAAudioDevice diagnosticDescriptionWithIndent:walkTree:] : 3380 -> 3276
~ -[ASAAudioDevice inputStreamUsageForAudioProc:] : 336 -> 340
~ -[ASAAudioDevice setInputStreamUsage:forAudioProc:] : 256 -> 264
~ -[ASAAudioDevice outputStreamUsageForAudioProc:] : 336 -> 340
~ -[ASAAudioDevice setOutputStreamUsage:forAudioProc:] : 256 -> 264
~ -[ASAObject diagnosticDescriptionWithIndent:walkTree:] : 784 -> 732
~ -[ASAPlugin diagnosticDescriptionWithIndent:walkTree:] : 1488 -> 1476
~ -[ASAControl diagnosticDescriptionWithIndent:walkTree:] : 412 -> 348
~ -[ASABox diagnosticDescriptionWithIndent:walkTree:] : 1896 -> 1840
~ -[ASACoreAudio _setupDeathSource] : 284 -> 280
~ -[ASACoreAudio diagnosticDescriptionWithIndent:walkTree:] : 1860 -> 1844
~ -[ASAClockDevice diagnosticDescriptionWithIndent:walkTree:] : 1780 -> 1688
~ -[ASAStream diagnosticDescriptionWithIndent:walkTree:] : 3932 -> 3808
~ -[ASAAudioFormat audioStreamBasicDescription] : 140 -> 132
~ -[ASAAudioFormat audioStreamRangedDescription] : 112 -> 68
~ -[ASAAudioFormat description] : 556 -> 552
~ -[ASAPlaythrough initWithDevices:usingMainDevice:andClockDevice:withName:isPrivate:usingChannelMapping:].cold.1 : 128 -> 124
~ InputOutputProc.cold.1 : 112 -> 120
~ InputOutputProc.cold.2 : 112 -> 120
~ InputOutputProc.cold.3 : 112 -> 120
~ InputOutputProc.cold.4 : 112 -> 120
~ -[ASAPlaythrough dealloc].cold.1 : 144 -> 140

```
