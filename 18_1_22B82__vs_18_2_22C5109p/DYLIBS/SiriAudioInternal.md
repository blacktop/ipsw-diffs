## SiriAudioInternal

> `/System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal`

```diff

-3401.22.2.0.0
-  __TEXT.__text: 0x4c5b4
-  __TEXT.__auth_stubs: 0x1c30
-  __TEXT.__objc_methlist: 0x114
-  __TEXT.__const: 0xf78
-  __TEXT.__cstring: 0x1501
-  __TEXT.__constg_swiftt: 0x66c
-  __TEXT.__swift5_typeref: 0xd03
-  __TEXT.__swift5_fieldmd: 0x550
+3402.51.1.1.2
+  __TEXT.__text: 0x4aaa4
+  __TEXT.__auth_stubs: 0x1ab0
+  __TEXT.__objc_methlist: 0x120
+  __TEXT.__const: 0xc78
+  __TEXT.__cstring: 0x14a1
+  __TEXT.__swift5_typeref: 0xc1d
+  __TEXT.__swift5_fieldmd: 0x514
+  __TEXT.__constg_swiftt: 0x5ac
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_reflstr: 0x547
-  __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0x78
-  __TEXT.__swift5_types: 0x64
+  __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__oslogstring: 0x68b9
-  __TEXT.__swift5_capture: 0x7cc
-  __TEXT.__unwind_info: 0x8f8
-  __TEXT.__eh_frame: 0xe68
+  __TEXT.__swift5_proto: 0x4c
+  __TEXT.__swift5_types: 0x58
+  __TEXT.__oslogstring: 0x6809
+  __TEXT.__swift5_capture: 0x7c8
+  __TEXT.__unwind_info: 0x860
+  __TEXT.__eh_frame: 0xbd0
   __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0xbc8
+  __TEXT.__objc_methname: 0xbb5
   __TEXT.__objc_methtype: 0x494
   __TEXT.__objc_stubs: 0x20
-  __DATA_CONST.__got: 0x550
-  __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x340
   __DATA_CONST.__objc_protorefs: 0x30
-  __AUTH_CONST.__auth_got: 0xe20
-  __AUTH_CONST.__auth_ptr: 0x498
+  __AUTH_CONST.__auth_got: 0xd60
+  __AUTH_CONST.__auth_ptr: 0x330
   __AUTH_CONST.__const: 0x18d0
-  __AUTH_CONST.__objc_const: 0x1a48
-  __AUTH.__objc_data: 0x5b0
-  __AUTH.__data: 0x3f8
-  __DATA.__data: 0x950
-  __DATA.__common: 0x440
-  __DATA.__bss: 0xd00
+  __AUTH_CONST.__objc_const: 0x1968
+  __AUTH.__objc_data: 0x578
+  __AUTH.__data: 0x2e8
+  __DATA.__data: 0x880
+  __DATA.__bss: 0x780
+  __DATA.__common: 0x400
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/MediaPlayer.framework/MediaPlayer
   - /System/Library/PrivateFrameworks/AppIntentsServices.framework/AppIntentsServices
-  - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
   - /System/Library/PrivateFrameworks/PodcastsKit.framework/PodcastsKit
   - /System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils

   - /System/Library/PrivateFrameworks/SiriKitFlow.framework/SiriKitFlow
   - /System/Library/PrivateFrameworks/SiriPlaybackControlSupport.framework/SiriPlaybackControlSupport
   - /System/Library/PrivateFrameworks/SiriReferenceResolution.framework/SiriReferenceResolution
+  - /System/Library/PrivateFrameworks/SiriSignals.framework/SiriSignals
   - /System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI
   - /System/Library/PrivateFrameworks/SiriSuggestionsKit.framework/SiriSuggestionsKit
   - /System/Library/PrivateFrameworks/SiriUtilities.framework/SiriUtilities

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
-  Functions: 757
-  Symbols:   241
-  CStrings:  598
+  Functions: 715
+  Symbols:   240
+  CStrings:  591
 
Symbols:
+ _OBJC_CLASS_$_INUpdateMediaAffinityMediaItemResolutionResult
+ __swift_FORCE_LOAD_$_swiftAppleArchive
- _LNConnectionOperationRequestTimeout
- _OBJC_CLASS_$_LNEnvironment
- _swift_getSingletonMetadata
- _swift_initClassMetadata2
CStrings:
+ "INSearchForMediaAppIntentHandler#handle invoking OpenPodcastEpisodeAppIntent with identifier: %!s(MISSING)"
+ "INSearchForMediaAppIntentHandler#handle invoking OpenPodcastShowAppIntent with identifier: %!s(MISSING)"
+ "INSearchForMediaAppIntentHandler#handle mediaType is not podcastShow or podcastEpisode, defaulting to invoke OpenPodcastShowAppIntent with identifier: %!s(MISSING)"
+ "INSearchForMediaAppIntentHandler#handle using Podcasts open intent"
+ "INSearchForMediaAppIntentHandler#resolveMediaItems failed to get MusicSiriRepresentation"
+ "INSearchForMediaAppIntentHandler#resolveMediaItems missing search results"
+ "INSearchForMediaAppIntentHandler#resolveMediaItems resolving podcast item: %!s(MISSING)"
+ "INUpdateMediaAffinityIntentHandler#handle failed to convert identifier: %!s(MISSING) into Int64 entityId"
+ "INUpdateMediaAffinityIntentHandler#handle missing mediaItem"
+ "INUpdateMediaAffinityIntentHandler#handle model object is %!s(MISSING)"
+ "INUpdateMediaAffinityIntentHandler#resolveMediaItems missing albumId from nowPlayingInfo: %!s(MISSING)"
+ "INUpdateMediaAffinityIntentHandler#resolveMediaItems missing artistId from nowPlayingInfo: %!s(MISSING)"
+ "INUpdateMediaAffinityIntentHandler#resolveMediaItems missing songId from nowPlayingInfo: %!s(MISSING)"
+ "INUpdateMediaAffinityIntentHandler#resolveMediaItems resolveNowPlayingMediaItem nowPlaying item error: %!{(MISSING)public}s"
+ "INUpdateMediaAffinityIntentHandler#resolveMediaItems resolved mediaItem: %!@(MISSING)"
+ "INUpdateMediaAffinityIntentHandler#resolveMediaItems..."
- "AppIntentInvoker#invokeOpenMusicItemIntent calling showResultIntent: %!s(MISSING)"
- "AppIntentInvoker#invokeOpenMusicItemIntent calling showResultIntentResponse: %!s(MISSING)"
- "AppIntentInvoker#invokeOpenMusicItemIntent response: %!s(MISSING)"
- "AppIntentInvoker#invokeSearchMusicAppIntent calling showResultIntent: %!s(MISSING)"
- "AppIntentInvoker#invokeSearchMusicAppIntent calling showResultIntentResponse: %!s(MISSING)"
- "AppIntentInvoker#invokeSearchMusicAppIntent response: %!s(MISSING)"
- "AppIntentInvoker#invokeSearchMusicAppIntent with criteria: %!s(MISSING), searchSource: %!s(MISSING), and mediaType: %!s(MISSING)"
- "INSearchForMediaAppIntentHandler#resolveMediaItems failed to create musicSiriRepresentation from source: %!s(MISSING), type: %!s(MISSING), and identifier: %!s(MISSING)"
- "INSearchForMediaAppIntentHandler#resolveMediaItems resolving item from user default: openMusicKitId=%!s(MISSING)"
- "INUpdateMediaAffinityIntentHandler#handle missing albumId from nowPlayingInfo: %!s(MISSING)"
- "INUpdateMediaAffinityIntentHandler#handle missing artistId from nowPlayingInfo: %!s(MISSING)"
- "INUpdateMediaAffinityIntentHandler#handle missing songId from nowPlayingInfo: %!s(MISSING)"
- "INUpdateMediaAffinityIntentHandler#handle resolveNowPlayingMediaItem nowPlaying item error: %!{(MISSING)public}s"
- "INUpdateMediaAffinityIntentHandler#model object is %!s(MISSING)"
- "MusicSiriRepresentation#from Failed to create valid URL for library content"
- "MusicSiriRepresentation#from Failed to create valid URL for store content"
- "MusicSiriRepresentation#from called with source = %!s(MISSING), type = %!s(MISSING), and identifier = %!s(MISSING)"
- "MusicSiriRepresentation#from returning %!s(MISSING)"
- "MusicSiriRepresentation#from unknown source type, returning nil"
- "_TtC17SiriAudioInternal16AppIntentInvoker"
- "_TtC17SiriAudioInternal22GenericMusicItemEntity"
- "defaultEnvironment"
- "localDispatcher"

```
