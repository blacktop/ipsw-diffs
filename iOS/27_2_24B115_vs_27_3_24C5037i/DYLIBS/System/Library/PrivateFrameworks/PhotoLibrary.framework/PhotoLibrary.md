## PhotoLibrary

> `/System/Library/PrivateFrameworks/PhotoLibrary.framework/PhotoLibrary`

```diff

-916.57.153.0.0
-  __TEXT.__text: 0x355f0
+920.7.110.0.0
+  __TEXT.__text: 0x3586c
   __TEXT.__objc_methlist: 0x4f6c
-  __TEXT.__const: 0x378
+  __TEXT.__const: 0x360
   __TEXT.__dlopen_cstrs: 0x1f4
   __TEXT.__gcc_except_tab: 0x310
   __TEXT.__cstring: 0x261c
-  __TEXT.__oslogstring: 0x90d
-  __TEXT.__unwind_info: 0x14e8
+  __TEXT.__oslogstring: 0xa75
+  __TEXT.__unwind_info: 0x14f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1635
-  Symbols:   3439
-  CStrings:  396
+  Symbols:   3440
+  CStrings:  397
 
Symbols:
+ GCC_except_table1063
+ GCC_except_table1068
+ GCC_except_table1086
+ GCC_except_table1089
+ GCC_except_table1090
+ GCC_except_table1091
+ GCC_except_table1092
+ GCC_except_table1093
+ GCC_except_table1291
+ GCC_except_table1304
+ GCC_except_table131
+ GCC_except_table1366
+ GCC_except_table1472
+ GCC_except_table1537
+ GCC_except_table527
+ GCC_except_table528
+ GCC_except_table637
+ GCC_except_table750
+ GCC_except_table885
+ GCC_except_table942
+ _PLCurrentLibraryLogTag
- GCC_except_table1048
- GCC_except_table1053
- GCC_except_table106
- GCC_except_table1071
- GCC_except_table1074
- GCC_except_table1075
- GCC_except_table1076
- GCC_except_table1077
- GCC_except_table1078
- GCC_except_table1284
- GCC_except_table1297
- GCC_except_table1359
- GCC_except_table1465
- GCC_except_table1530
- GCC_except_table511
- GCC_except_table512
- GCC_except_table605
- GCC_except_table734
- GCC_except_table870
- GCC_except_table927
CStrings:
+ "%{public}s(streamed-video-playback) already have a cachedNonPersistedVideoPlaybackURL %@"
+ "%{public}s(streamed-video-playback) will play streamed video using original video at path %@"
+ "%{public}s(streamed-video-playback) will play video for %@"
+ "%{public}s(video-playback) %@ observeValueForKeyPath %@ %@"
+ "%{public}s(video-playback) _playerRateDidChange %@"
+ "%{public}s(video-playback) _verifyOrRestartPlayback playing %u didBuffer %u"
+ "%{public}s(video-playback) _verifyOrRestartPlayback rate > 0"
+ "%{public}s(video-playback) _verifyOrRestartPlayback telling movie player to play"
+ "%{public}s(video-playback) buffering state changed from %lu to %lu"
+ "%{public}s(video-playback) calling _player pause in pause"
+ "%{public}s(video-playback) calling _player pause in stop"
+ "%{public}s(video-playback) calling _player play"
+ "%{public}s(video-playback) calling _player play in playFromBeginning"
+ "%{public}s(video-playback) calling _player playDueToEnoughData"
+ "%{public}s(video-playback) moviePlayerPlaybackRateDidChange to 0"
+ "%{public}s(video-playback) moviePlayerPlaybackRateDidChange to 1"
+ "%{public}s(video-playback) network reachability changes. Clears out cached video URL."
+ "%{public}s(video-playback) pause due to reset"
+ "%{public}s(video-playback) pause due to stop"
+ "%{public}s(video-playback) pause due to video view pause"
+ "%{public}s(video-playback) pauseDueToInsufficientData due to buffer state change"
+ "%{public}s(video-playback) play due to buffer state change"
+ "%{public}s(video-playback) play in %@"
+ "%{public}s(video-playback) setting buffering state to %lu"
+ "%{public}s(video-playback) update poster frame visibility to %d"
+ "%{public}sCompleted cleanupForStoreDemoMode successfully"
+ "%{public}sFailed to fetch playback objects for %@"
+ "%{public}sFailed to perform cleanupForStoreDemoMode: %{public}@"
+ "%{public}sMarked temp file (%@) as purgeable."
+ "%{public}sMis-matched image size and/or orientation for asset %@. PhotoKit: %.0f x %.0f (%ld). Data: %.0f x %.0f (%ld)"
+ "%{public}sNo PHAsset for committing pending adjustment changes"
+ "%{public}sPlaying 360p video for cellular connection."
+ "%{public}sRequesting cleanupForStoreDemoMode"
+ "%{public}sSent cleanupForStoreDemoMode"
+ "%{public}sUnable to mark temp file (%@) purgeable."
+ "%{public}sVideo export failed for asset %@: %@"
- "(streamed-video-playback) already have a cachedNonPersistedVideoPlaybackURL %@"
- "(streamed-video-playback) will play streamed video using original video at path %@"
- "(streamed-video-playback) will play video for %@"
- "(video-playback) %@ observeValueForKeyPath %@ %@"
- "(video-playback) _playerRateDidChange %@"
- "(video-playback) _verifyOrRestartPlayback playing %u didBuffer %u"
- "(video-playback) _verifyOrRestartPlayback rate > 0"
- "(video-playback) _verifyOrRestartPlayback telling movie player to play"
- "(video-playback) buffering state changed from %lu to %lu"
- "(video-playback) calling _player pause in pause"
- "(video-playback) calling _player pause in stop"
- "(video-playback) calling _player play"
- "(video-playback) calling _player play in playFromBeginning"
- "(video-playback) calling _player playDueToEnoughData"
- "(video-playback) moviePlayerPlaybackRateDidChange to 0"
- "(video-playback) moviePlayerPlaybackRateDidChange to 1"
- "(video-playback) network reachability changes. Clears out cached video URL."
- "(video-playback) pause due to reset"
- "(video-playback) pause due to stop"
- "(video-playback) pause due to video view pause"
- "(video-playback) pauseDueToInsufficientData due to buffer state change"
- "(video-playback) play due to buffer state change"
- "(video-playback) play in %@"
- "(video-playback) setting buffering state to %lu"
- "(video-playback) update poster frame visibility to %d"
- "Completed cleanupForStoreDemoMode successfully"
- "Failed to fetch playback objects for %@"
- "Failed to perform cleanupForStoreDemoMode: %{public}@"
- "Marked temp file (%@) as purgeable."
- "Mis-matched image size and/or orientation for asset %@. PhotoKit: %.0f x %.0f (%ld). Data: %.0f x %.0f (%ld)"
- "No PHAsset for committing pending adjustment changes"
- "Playing 360p video for cellular connection."
- "Requesting cleanupForStoreDemoMode"
- "Sent cleanupForStoreDemoMode"
- "Unable to mark temp file (%@) purgeable."
```
