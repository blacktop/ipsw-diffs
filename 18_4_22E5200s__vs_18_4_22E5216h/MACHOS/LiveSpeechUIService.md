## LiveSpeechUIService

> `/System/Library/AccessibilityBundles/LiveSpeechUIService.axuiservice/LiveSpeechUIService`

```diff

-3148.15.5.2.0
-  __TEXT.__text: 0x9439c
-  __TEXT.__auth_stubs: 0x2c80
+3148.15.9.0.0
+  __TEXT.__text: 0x946a4
+  __TEXT.__auth_stubs: 0x2c20
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__objc_methlist: 0x8a8
-  __TEXT.__const: 0x4c30
+  __TEXT.__objc_methlist: 0x8b8
+  __TEXT.__const: 0x4cd0
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__cstring: 0x23ba
-  __TEXT.__oslogstring: 0x101b
+  __TEXT.__cstring: 0x247a
+  __TEXT.__oslogstring: 0x129d
   __TEXT.__objc_classname: 0xb5
-  __TEXT.__objc_methname: 0x1d0c
+  __TEXT.__objc_methname: 0x1d95
   __TEXT.__objc_methtype: 0x89b
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__swift5_typeref: 0x10639
-  __TEXT.__constg_swiftt: 0x1c04
+  __TEXT.__swift5_typeref: 0x10641
+  __TEXT.__constg_swiftt: 0x1c20
   __TEXT.__swift5_builtin: 0x104
-  __TEXT.__swift5_reflstr: 0x1777
-  __TEXT.__swift5_fieldmd: 0x15a8
-  __TEXT.__swift5_assocty: 0x5d8
-  __TEXT.__swift5_proto: 0x1e8
+  __TEXT.__swift5_reflstr: 0x17c7
+  __TEXT.__swift5_fieldmd: 0x15dc
+  __TEXT.__swift5_assocty: 0x5f0
+  __TEXT.__swift5_proto: 0x1f0
   __TEXT.__swift5_types: 0x148
-  __TEXT.__swift5_capture: 0xae4
+  __TEXT.__swift5_capture: 0xa84
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1b50
-  __TEXT.__eh_frame: 0x1308
-  __DATA_CONST.__auth_got: 0x1650
-  __DATA_CONST.__got: 0xc00
-  __DATA_CONST.__auth_ptr: 0xcc0
-  __DATA_CONST.__const: 0x3778
+  __TEXT.__unwind_info: 0x1b58
+  __TEXT.__eh_frame: 0x1300
+  __DATA_CONST.__auth_got: 0x1620
+  __DATA_CONST.__got: 0xc20
+  __DATA_CONST.__auth_ptr: 0xcb0
+  __DATA_CONST.__const: 0x3640
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA.__objc_const: 0x1c20
-  __DATA.__objc_selrefs: 0x918
+  __DATA.__objc_const: 0x1c60
+  __DATA.__objc_selrefs: 0x940
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x1388
-  __DATA.__data: 0x3a58
+  __DATA.__objc_data: 0x13c0
+  __DATA.__data: 0x3a98
   __DATA.__objc_stublist: 0x18
-  __DATA.__bss: 0x4210
+  __DATA.__bss: 0x4310
   __DATA.__common: 0x180
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/LiveSpeechServices.framework/LiveSpeechServices
   - /System/Library/PrivateFrameworks/LiveSpeechUI.framework/LiveSpeechUI
   - /System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription
-  - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
+  - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2875
-  Symbols:   352
-  CStrings:  764
+  Functions: 2859
+  Symbols:   353
+  CStrings:  780
 
Symbols:
+ _AVSystemController_PlayingSessionsDescriptionAttribute
+ _AVSystemController_SomeSessionIsPlayingDidChangeNotification
+ _AVSystemController_SubscribeToNotificationsAttribute
+ _OBJC_CLASS_$_AVSystemController
+ _OBJC_CLASS_$_AXSpringBoardServer
+ _OBJC_CLASS_$_NSDictionary
+ _kAXSContinuityDisplayStateChangedNotification
+ _swift_cvw_allocateGenericValueMetadataWithLayoutString
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _MRMediaRemoteGetLocalOrigin
- _MRMediaRemoteGetNowPlayingApplicationPlaybackStateForOrigin
- _MRMediaRemoteSetWantsNowPlayingNotifications
- _kMRMediaRemoteNowPlayingApplicationDisplayNameUserInfoKey
- _kMRMediaRemoteNowPlayingApplicationIsPlayingDidChangeNotification
- _kMRMediaRemoteNowPlayingApplicationIsPlayingUserInfoKey
- _swift_allocateGenericValueMetadataWithLayoutString
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "CaptionsProvider AudioSession client pid: %s session: %s"
+ "CaptionsProvider AudioSession isMediaPlaying: %s"
+ "CaptionsProvider AudioSession mediaPlayingDidChange Timer isMediaPlaying: %{bool}d"
+ "CaptionsProvider AudioSession mediaPlayingDidChange isMediaPlaying: %{bool}d"
+ "CaptionsProvider AudioSession mediaPlayingDidChange: %s"
+ "CaptionsProvider AudioSession mediaPlayingDidChange: no data"
+ "CaptionsProvider not starting transcription due to Oneness"
+ "Could not subscribe to AVSystemController_SomeSessionIsPlayingDidChange: %s"
+ "H: %{bool}d, V: %{bool}d fast H: %{bool}d, fast V: %{bool}d, long H: %{bool}d"
+ "StartTranscribing for type: %ld, pid: %ld"
+ "StartTranscribing skip isTranscribing: TRUE, for type: %ld, pid: %ld"
+ "__swift_objectForKeyedSubscript:"
+ "attributeForKey:"
+ "blockAudioTranscriptionForOneness"
+ "continuityDisplayStateChanged"
+ "handleFastSwipe velocity: %s, translation: %s"
+ "isContinuitySessionActive"
+ "setAttribute:forKey:error:"
+ "updateLiveCaptionsStateForOneness"
+ "updateLiveCaptionsStateForOneness continuitySessionActive: %{bool}d"
+ "updateMicOnState new: %{bool}d, old %{bool}d"
- "CaptionsProvider AudioSession Client: %s isMediaPlaying: %s"
- "handleFastSwipe velocity: %s, tranclsation: %s"
- "startTranscribing for type: %ld, pid: %ld"
- "updateMicOnState: %{bool}d"
- "v12@?0I8"

```
