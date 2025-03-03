## NowPlaying-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/NowPlaying-iOS.feature/NowPlaying-iOS`

```diff

-1025.82.1.0.0
-  __TEXT.__text: 0xf908
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x968
-  __TEXT.__cstring: 0xae5
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x528
-  __TEXT.__oslogstring: 0x2632
+1043.100.29.0.0
+  __TEXT.__text: 0x109ac
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_methlist: 0xbf8
+  __TEXT.__cstring: 0xece
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__oslogstring: 0x2793
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x328
+  __TEXT.__unwind_info: 0x318
   __TEXT.__objc_classname: 0x161
-  __TEXT.__objc_methname: 0x2067
-  __TEXT.__objc_methtype: 0x403
-  __TEXT.__objc_stubs: 0x1840
-  __DATA_CONST.__got: 0x410
-  __DATA_CONST.__const: 0x370
+  __TEXT.__objc_methname: 0x226d
+  __TEXT.__objc_methtype: 0x41e
+  __TEXT.__objc_stubs: 0x1980
+  __DATA_CONST.__got: 0x408
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x780
+  __DATA_CONST.__objc_selrefs: 0x878
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x380
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x680
-  __AUTH_CONST.__objc_const: 0x1b08
+  __AUTH_CONST.__objc_const: 0x1880
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xf4
+  __DATA.__objc_ivar: 0x10c
   __DATA.__data: 0x240
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 299
-  Symbols:   679
-  CStrings:  666
+  Functions: 311
+  Symbols:   694
+  CStrings:  716
 
Symbols:
+ _MRMediaRemoteSetWantsNowPlayingNotifications
- _CFStringCreateCopy
- _MRMediaRemoteRegisterForNowPlayingNotifications
- _MRMediaRemoteUnregisterForNowPlayingNotifications
- _dispatch_get_global_queue
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _kCFAllocatorDefault
- _objc_release_x9
CStrings:
+ "%s: %d"
+ "%s: -> new ArtworkData: %lu bytes / hash %@"
+ "%s: -> new nowPlayingInfo: %@"
+ "%s: Notification received: %@, debounce=%ld"
+ "%s: artwork: %p"
+ "%s: artwork: %p, nowPlayingInfo: %@"
+ "%s: clientRef: %@, errorRef: %@"
+ "%s: commands: %@"
+ "%s: delay(%f ms) -> new supportedCommands: %@"
+ "%s: delay(%f ms) old supportedCommands: %@"
+ "%s: delay(%f ms), -> new ArtworkData: %lu bytes / hash %@"
+ "%s: delay(%f ms), appBundleID %@ -> %@"
+ "%s: delay(%f ms), appName %@ -> %@"
+ "%s: delay(%f ms), artwork: %p (%lu bytes), nowPlayingInfo: %@"
+ "%s: delay(%f ms), old ArtworkData: %lu bytes / hash %@"
+ "%s: delay(%f ms), playbackState %d -> %d"
+ "%s: mrNowPlayingInfo: %@"
+ "%s: old ArtworkData: %lu bytes / hash %@"
+ "%s: old nowPlayingInfo: %@"
+ "%s: playbackState %d"
+ "-[ACCNowPlayingFeaturePlugin currentPlaybackAttributes]"
+ "-[ACCNowPlayingFeaturePlugin currentPlaybackStateMR]"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingAppDidChange:]_block_invoke"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingAppDidChange:]_block_invoke_2"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingArtworkDidChange:]_block_invoke"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingArtworkDidChange:]_block_invoke_2"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingInfoDidChange:]"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingInfoDidChange:]_block_invoke"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingInfoDidChange:]_block_invoke_2"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingStateDidChange:]"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingStateDidChange:]_block_invoke"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingStateDidChange:]_block_invoke_2"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingSupportedCommandsDidChange:]"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingSupportedCommandsDidChange:]_block_invoke"
+ "-[ACCNowPlayingFeaturePlugin nowPlayingSupportedCommandsDidChange:]_block_invoke_2"
+ "/\a"
+ "@\"NSArray\""
+ "@\"NSDictionary\""
+ "ACCNowPlayingMRCompletionQ"
+ "T@\"NSArray\",&,N,V_mrSupportedCommands"
+ "T@\"NSData\",&,N,V_mrArtworkData"
+ "T@\"NSData\",&,N,V_mrArtworkDataHash"
+ "T@\"NSDictionary\",&,N,V_mrNowPlayingInfo"
+ "T@\"NSString\",&,N,V_mrNowPlayingAppBundleID"
+ "T@\"NSString\",&,N,V_mrNowPlayingAppName"
+ "TI,N,V_mrPlaybackState"
+ "_mrArtworkData"
+ "_mrArtworkDataHash"
+ "_mrNowPlayingAppBundleID"
+ "_mrNowPlayingAppName"
+ "_mrNowPlayingInfo"
+ "_mrPlaybackState"
+ "_mrSupportedCommands"
+ "mrArtworkData"
+ "mrArtworkDataHash"
+ "mrNowPlayingAppBundleID"
+ "mrNowPlayingAppName"
+ "mrNowPlayingInfo"
+ "mrPlaybackState"
+ "mrSupportedCommands"
+ "nowPlayingInfoDidChange nowPlayingInfo: \nnowPlayingInfo Item Info \n    PID: %@ \n    Title: %@ \n    Album: %@ \n    Artist: %@ \n    Genre: %@ \n    Composer: %@ \n    Duration: %@ \n    Album Index/Count: %@ / %@ \n    Disc Index/Count: %@ / %@ \n    Chapter Count: %@ \n    Liked / Banned: %@ / %@ \n    artworkID; %@ \n"
+ "nowPlayingInfoDidChange nowPlayingInfo: \nnowPlayingInfoInfo Playback Info \n    Timestamp: %@ (%f) \n    ElapsedTime: %@ / %@ \n    PlaybackRate: %@ (%@) \n    Index / Count: %@ / %@ \n    Chapter: %@ / %@ \n    IsAd: %@ \n    RadioStation: %@ (%@)\n    IsMusicApp: %@\n"
+ "nowPlayingSupportedCommandsDidChange:"
+ "setMrArtworkData:"
+ "setMrArtworkDataHash:"
+ "setMrNowPlayingAppBundleID:"
+ "setMrNowPlayingAppName:"
+ "setMrNowPlayingInfo:"
+ "setMrPlaybackState:"
+ "setMrSupportedCommands:"
- "\x1f\x02"
- "#Artwork Requesting artwork for current now playing item..."
- "#Artwork Timed out waiting %dms for MRMediaRemoteRequestNowPlayingPlaybackQueueSync completion handler!"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_mpMusicPlayerControllerQueue"
- "[WARNING] currentMediaItemAttributes: timed out (%d ms) waiting for MR nowPlayingInfo"
- "[WARNING] currentMediaItemAttributes: timed out (%d ms) waiting for MR supportedCommands"
- "[WARNING] currentPlaybackAppBundleID: timed out (%d ms) waiting for MR nowPlaying clientRef"
- "[WARNING] currentPlaybackAppName: timed out (%d ms) waiting for MR nowPlaying clientRef"
- "[WARNING] currentPlaybackAttributes: timed out (%d ms) waiting for MR supportedCommands"
- "[WARNING] currentPlaybackStateMR: timed out (%d ms) waiting for MR PlaybackState"
- "_mpMusicPlayerControllerQueue"
- "com.apple.accessoryd.MediaPlayerMPQ"
- "currentMediaItemArtworkOriginal"
- "currentPlaybackAttributes nowPlayingInfo: %@"
- "currentPlaybackAttributes playbackAttributes: %@"
- "currentPlaybackStateMR: %d"
- "mpMusicPlayerControllerQueue"
- "nowPlayingInfoDidChange: Notification received: %@, debounce=%ld"
- "nowPlayingStateDidChange: Notification received: %@, debounce=%ld"
- "setMpMusicPlayerControllerQueue:"

```
