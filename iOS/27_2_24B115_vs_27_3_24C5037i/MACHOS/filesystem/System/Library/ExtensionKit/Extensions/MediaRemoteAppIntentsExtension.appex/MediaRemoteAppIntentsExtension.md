## MediaRemoteAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/MediaRemoteAppIntentsExtension.appex/MediaRemoteAppIntentsExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`

```diff

-4026.210.3.0.0
-  __TEXT.__text: 0xa214
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_stubs: 0x40
-  __TEXT.__swift5_typeref: 0x8f3
-  __TEXT.__const: 0x1c38
-  __TEXT.__swift5_reflstr: 0x404
-  __TEXT.__swift5_assocty: 0x320
-  __TEXT.__constg_swiftt: 0x180
-  __TEXT.__swift5_fieldmd: 0x3bc
-  __TEXT.__objc_methtype: 0x12
-  __TEXT.__swift5_proto: 0x1a8
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift_as_entry: 0x68
-  __TEXT.__swift_as_ret: 0x58
-  __TEXT.__swift_as_cont: 0x2c
+4026.300.11.0.0
+  __TEXT.__text: 0x1fbd4
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__const: 0x5f00
+  __TEXT.__swift5_typeref: 0x1a1b
+  __TEXT.__swift5_reflstr: 0x6b2
+  __TEXT.__swift5_assocty: 0x9b0
+  __TEXT.__constg_swiftt: 0x934
+  __TEXT.__swift5_fieldmd: 0x934
+  __TEXT.__objc_methtype: 0x95
+  __TEXT.__oslogstring: 0x28
+  __TEXT.__cstring: 0x54e
+  __TEXT.__swift5_proto: 0x570
+  __TEXT.__swift5_types: 0xb8
+  __TEXT.__swift_as_entry: 0x164
+  __TEXT.__swift_as_ret: 0x14c
+  __TEXT.__swift_as_cont: 0x104
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x28a
-  __TEXT.__objc_methname: 0x67
-  __TEXT.__unwind_info: 0x6d8
-  __TEXT.__eh_frame: 0x4a0
-  __DATA_CONST.__const: 0xa08
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__objc_methname: 0x362
+  __TEXT.__unwind_info: 0x14d0
+  __TEXT.__eh_frame: 0x11f8
+  __DATA_CONST.__const: 0x1f80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x138
-  __DATA_CONST.__auth_ptr: 0x508
-  __DATA.__objc_selrefs: 0x10
-  __DATA.__data: 0x788
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__auth_ptr: 0x6a8
+  __DATA.__objc_selrefs: 0xc8
+  __DATA.__data: 0x12d8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
+  - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 501
-  Symbols:   89
-  CStrings:  47
+  Functions: 1528
+  Symbols:   139
+  CStrings:  106
 
Symbols:
+ _MRMediaRemoteCopyCommandDescription
+ _MRRequestDetailsInitiatorIntent
+ _OBJC_CLASS_$_MPCAssistantGetVolume
+ _OBJC_CLASS_$_MPCAssistantSetVolume
+ _OBJC_CLASS_$_MRAVEndpoint
+ _OBJC_CLASS_$_MRDestination
+ _OBJC_CLASS_$_MRLanguageOption
+ _OBJC_CLASS_$_MRNowPlayingController
+ _OBJC_CLASS_$_MRRequestDetails
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSUnitDuration
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_OS_os_log
+ __Block_copy
+ __Block_release
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_impl
+ __swiftEmptySetSingleton
+ _kMRMediaRemoteOptionLanguageOptionData
+ _kMRMediaRemoteOptionPlaybackPosition
+ _kMRMediaRemoteOptionPlaybackRate
+ _kMRMediaRemoteOptionRepeatMode
+ _kMRMediaRemoteOptionRequestDefermentToPlaybackQueuePosition
+ _kMRMediaRemoteOptionShuffleMode
+ _kMRMediaRemoteOptionSkipInterval
+ _objc_opt_self
+ _objc_release
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x8
+ _os_log_type_enabled
+ _swift_continuation_resume
+ _swift_deallocObject
+ _swift_dynamicCast
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_release_x23
+ _swift_release_x8
+ _swift_retain_x2
+ _swift_slowDealloc
CStrings:
+ "Disable Subtitles"
+ "MRNPC sent %@ %u to %@;\n got result: %@"
+ "MediaRemote"
+ "add speaker intent"
+ "addOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:"
+ "app_intents_proactive_destination"
+ "appex_getVolumeLevel(forUID:)"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "backward"
+ "beginning"
+ "closedCaptions"
+ "container"
+ "contentItemWithOffset:"
+ "decrease"
+ "decreaseVolumeBy:withUIDs:completion:"
+ "default"
+ "duration"
+ "end"
+ "error"
+ "faster"
+ "forward"
+ "getVolumeLevelForUID:completion:"
+ "increase"
+ "increaseVolumeBy:withUIDs:completion:"
+ "init"
+ "initWithInitiator:requestID:reason:"
+ "initWithOutputDeviceUID:"
+ "initWithType:languageTag:characteristics:displayName:identifier:"
+ "initWithUID:"
+ "localDestination"
+ "metadata"
+ "move speaker intent"
+ "moveOutputDevicesWithUIDs:toGroupContainingOutputDeviceWithUID:details:queue:completion:"
+ "normal"
+ "off"
+ "one"
+ "pauseOutputDeviceUIDs:details:queue:completion:"
+ "performRequestWithCompletion:"
+ "playbackControls.audioLanguage"
+ "playbackControls.mediaSkipDirection"
+ "playbackControls.relativeVolumeLevel"
+ "playbackControls.repeatState"
+ "playbackControls.seekLocation"
+ "playbackControls.setPlaybackSpeedQualifier"
+ "playbackControls.subtitleLanguage"
+ "playbackControls.subtitleType"
+ "playbackQueue"
+ "proactiveDestination"
+ "qualifier"
+ "remove speaker intent"
+ "seconds"
+ "sendCommand:toDestination:options:appOptions:withCompletion:"
+ "setVolume:withUIDs:completion:"
+ "slower"
+ "subtitlesForTheDeafAndHardOfHearing"
+ "v16@?0@\"MRCommandResult\"8"
+ "v20@?0f8@\"NSError\"12"
+ "v24@?0@\"MRNowPlayingPlayerResponse\"8@\"NSError\"16"
+ "value"
```
