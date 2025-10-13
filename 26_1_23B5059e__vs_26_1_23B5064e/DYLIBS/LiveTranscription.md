## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription`

```diff

-545.3.1.0.0
-  __TEXT.__text: 0x2ea90
+545.3.2.0.0
+  __TEXT.__text: 0x2ea80
   __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_methlist: 0x156c
   __TEXT.__const: 0x800
   __TEXT.__cstring: 0xf7a
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__oslogstring: 0x2634
+  __TEXT.__oslogstring: 0x2694
   __TEXT.__dlopen_cstrs: 0x6a
   __TEXT.__swift5_typeref: 0x444
   __TEXT.__swift5_reflstr: 0x1fa

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D4E7F56-4457-30EC-A7F7-47C0E07EDAE9
+  UUID: BD717D3C-18CA-3A23-8F7B-43A481CD9ED7
   Functions: 1022
   Symbols:   1987
   CStrings:  1166
Functions:
~ -[AXLTLiveTranscription startTranscribing:targetPID:excludingPIDs:callbackBlock:audioInfoBlock:error:] : 1248 -> 1240
~ -[AXLTLiveTranscription stopTranscribing:targetPID:error:] : 696 -> 684
~ +[AXLTAudioOutManager isCoreMediaNotificationsSupportedForPid:] : 12 -> 16
CStrings:
+ "AudioTranscriber: Recognized text for app: %@"
+ "AudioTranscriber: Transcribed text: %@ for app: %@"
+ "MicTranscriber: Error starting audio engine: %@"
+ "MicTranscriber: Media Services reset notification: %@"
+ "MicTranscriber: Transcribed text: %@ for Mic"
- "Media Services notification: %@"
- "Recognized text for app: %@"
- "Transcribed text: %@ for Mic"
- "Transcribed text: %@ for app: %@"
- "error starting audioengine: %@"

```
