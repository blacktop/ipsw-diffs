## SiriPlaybackControlIntents

> `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents`

```diff

-3401.14.1.0.0
-  __TEXT.__text: 0x266400
-  __TEXT.__auth_stubs: 0x44c0
+3402.39.1.0.0
+  __TEXT.__text: 0x26c0b8
+  __TEXT.__auth_stubs: 0x4780
   __TEXT.__objc_methlist: 0x1e44
-  __TEXT.__const: 0x17ac0
-  __TEXT.__cstring: 0x8038
-  __TEXT.__constg_swiftt: 0x67a0
-  __TEXT.__swift5_typeref: 0x5aa8
+  __TEXT.__const: 0x181a0
+  __TEXT.__cstring: 0x8238
+  __TEXT.__constg_swiftt: 0x6940
+  __TEXT.__swift5_typeref: 0x5c12
   __TEXT.__swift5_builtin: 0x500
-  __TEXT.__swift5_reflstr: 0x4c33
-  __TEXT.__swift5_fieldmd: 0x58a4
-  __TEXT.__swift5_assocty: 0x1b10
-  __TEXT.__swift5_proto: 0x14f4
-  __TEXT.__swift5_types: 0x69c
-  __TEXT.__swift5_protos: 0xbc
+  __TEXT.__swift5_reflstr: 0x4cd3
+  __TEXT.__swift5_fieldmd: 0x5970
+  __TEXT.__swift5_assocty: 0x1b40
+  __TEXT.__swift5_proto: 0x1550
+  __TEXT.__swift5_types: 0x6b0
+  __TEXT.__swift5_protos: 0xc0
   __TEXT.__swift5_capture: 0x42d0
-  __TEXT.__oslogstring: 0x1a456
+  __TEXT.__oslogstring: 0x1a856
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x6ef0
-  __TEXT.__eh_frame: 0x4be4
+  __TEXT.__unwind_info: 0x70b8
+  __TEXT.__eh_frame: 0x4f2c
   __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methname: 0x2c35
+  __TEXT.__objc_methname: 0x2c5f
   __TEXT.__objc_methtype: 0x1d0
-  __DATA_CONST.__got: 0xe00
-  __DATA_CONST.__const: 0xb30
-  __DATA_CONST.__objc_classlist: 0x598
+  __DATA_CONST.__got: 0xe40
+  __DATA_CONST.__const: 0xb60
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd58
+  __DATA_CONST.__objc_selrefs: 0xd68
   __DATA_CONST.__objc_protorefs: 0x100
-  __AUTH_CONST.__auth_got: 0x2260
-  __AUTH_CONST.__auth_ptr: 0x2068
-  __AUTH_CONST.__const: 0x12538
-  __AUTH_CONST.__objc_const: 0x12030
-  __AUTH.__objc_data: 0x62a8
-  __AUTH.__data: 0x6cb8
-  __DATA.__data: 0x4230
-  __DATA.__bss: 0x22e80
-  __DATA.__common: 0x2f8
+  __AUTH_CONST.__auth_got: 0x23c0
+  __AUTH_CONST.__auth_ptr: 0x2400
+  __AUTH_CONST.__const: 0x12618
+  __AUTH_CONST.__objc_const: 0x122e8
+  __AUTH.__objc_data: 0x62f0
+  __AUTH.__data: 0x6f38
+  __DATA.__data: 0x4380
+  __DATA.__bss: 0x23880
+  __DATA.__common: 0x308
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine
+  - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 13761
-  Symbols:   4615
-  CStrings:  2786
+  Functions: 13930
+  Symbols:   4644
+  CStrings:  2812
 
Symbols:
+ _CATDefaultMode
+ _OBJC_CLASS_$_CATDialog
+ _OBJC_CLASS_$_DialogElement
+ _OBJC_CLASS_$_DialogExecutionResult
+ _OBJC_CLASS_$_LNEnvironment
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ _swift_deletedAsyncMethodErrorTu
- _OBJC_CLASS_$_CAT
- _OBJC_CLASS_$_CATResult
CStrings:
+ "AppIntentInvoker#invokeOpenAccessoryItemAppIntentForLyrics"
+ "AppIntentInvoker#invokeOpenAccessoryItemAppIntentForLyrics response: %!s(MISSING)"
+ "BaseDialogProvider#executeDialog Error while executing dialog: %!{(MISSING)public}s"
+ "BaseDialogProvider#executeDialog Successfully evaluated CAT: catId:%!{(MISSING)public}s, result.speak:%!{(MISSING)public}s, result.print:%!{(MISSING)public}s"
+ "BaseDialogProvider#executeDialog is executing a dialog with responseMode = %!s(MISSING)"
+ "BaseDialogProvider#executeDialog..."
+ "ControlsDialogParameters#update deviceType: %!s(MISSING) doesn't have dialog parameter"
+ "Initializing showLyricsFlow"
+ "PlaybackControlling#filterOptionsByCharacteristic options empty after filtering by subtitles, returning all options"
+ "PlaybackControlling#filterOptionsByCharacteristic returning options filtered by CC/SDH"
+ "PlaybackControlling#filterOptionsByCharacteristic returning options filtered by subtitles"
+ "PlaybackControlling#filterOptionsByCharacteristic unknown characteristic, returning all options"
+ "PlaybackControlling#filterOptionsByCharacteristic using characteristic: %!{(MISSING)public}s to filter language options: %!{(MISSING)public}s"
+ "PlaybackControls#ShowLyricsFailed"
+ "ShowLyricsFlow#execute"
+ "ShowLyricsFlow#execute sent dismiss command"
+ "ShowLyricsFlow#execute threw an error: %!s(MISSING)"
+ "Source device doesn't support add command, sending a move command instead"
+ "UsoTask_request_common_MediaItem#shouldHandle not a lyrics request. Not handling in controls"
+ "UsoTask_summarise_common_MediaItem#shouldHandle not a lyrics request. Not handling in controls"
+ "_TtC26SiriPlaybackControlIntents14ShowLyricsFlow"
+ "_TtC26SiriPlaybackControlIntents16AppIntentInvoker"
+ "_TtC26SiriPlaybackControlIntents19AccessoryItemEntity"
+ "_TtC26SiriPlaybackControlIntents23AppIntentInvokerContext"
+ "appIntentInvoker"
+ "com.apple.nowplaying"
+ "defaultEnvironment"
+ "dialog"
+ "execute:catId:parameters:globals:callback:options:completion:"
+ "fullPrint"
+ "fullSpeak"
+ "localDispatcher"
+ "request"
+ "sirikit.intents.custom.com.apple.siri.SiriPlaybackControlIntents.ShowLyricsIntent"
+ "summarise"
+ "v24@?0@\"DialogExecutionResult\"8@\"NSError\"16"
- "BaseDialogProvider#executeCatResult Error while executing dialog: %!{(MISSING)public}s"
- "BaseDialogProvider#executeCatResult Successfully evaluated CAT: catId:%!{(MISSING)public}s, result.speak:%!{(MISSING)public}s, result.print:%!{(MISSING)public}s"
- "BaseDialogProvider#executeCatResult is executing a dialog with responseMode = %!s(MISSING)"
- "BaseDialogProvider#executeCatResult..."
- "Source device is is not TV or HomePod. Sending a move command instead of add"
- "Unsupported deviceType for native playback controls!"
- "execute:catId:parameters:globals:callback:completion:"
- "print"
- "speak"
- "v24@?0@\"CATResult\"8@\"NSError\"16"

```
