## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-563.30.1.0.0
-  __TEXT.__text: 0x62d30
-  __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__objc_methlist: 0x52e0
-  __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x660b
-  __TEXT.__oslogstring: 0x5bef
-  __TEXT.__gcc_except_tab: 0x2458
-  __TEXT.__unwind_info: 0x15d8
+563.40.15.0.0
+  __TEXT.__text: 0x648e4
+  __TEXT.__auth_stubs: 0x800
+  __TEXT.__objc_methlist: 0x5dc8
+  __TEXT.__const: 0x260
+  __TEXT.__cstring: 0x66b4
+  __TEXT.__oslogstring: 0x5eb1
+  __TEXT.__gcc_except_tab: 0x2584
+  __TEXT.__unwind_info: 0x1670
   __TEXT.__objc_classname: 0x80c
-  __TEXT.__objc_methname: 0x12a2d
-  __TEXT.__objc_methtype: 0x23a2
-  __TEXT.__objc_stubs: 0xb100
-  __DATA_CONST.__got: 0x850
-  __DATA_CONST.__const: 0x23e0
+  __TEXT.__objc_methname: 0x12c5f
+  __TEXT.__objc_methtype: 0x23ef
+  __TEXT.__objc_stubs: 0xb2c0
+  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__const: 0x2438
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a80
+  __DATA_CONST.__objc_selrefs: 0x3c50
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x408
+  __AUTH_CONST.__auth_got: 0x410
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x67e0
-  __AUTH_CONST.__objc_const: 0xabe8
+  __AUTH_CONST.__cfstring: 0x68a0
+  __AUTH_CONST.__objc_const: 0x9838
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x7b0
-  __DATA.__data: 0xa48
+  __DATA.__objc_ivar: 0x7ac
+  __DATA.__data: 0xa60
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__bss: 0x1f8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2172
-  Symbols:   3032
-  CStrings:  4582
+  Functions: 2220
+  Symbols:   3088
+  CStrings:  4619
 
Symbols:
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncNotification
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonKey
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonLoadedTimeRangesChanged
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonSegmentsChanged
+ _AVPlayerWaitingDuringInterstitialEventReason
+ _OBJC_CLASS_$_AVPlayerInterstitialEventMonitor
+ _TVPMediaItemMetadataHapticsURLString
+ __os_feature_enabled_impl
CStrings:
+ "?:FP"
+ "?>"
+ "@\"AVPlayerInterstitialEventMonitor\""
+ "AVPlayer %@ %@ player timeControlStatus did change to %@.  reasonForWaiting is %@"
+ "Active player is %@"
+ "Active player item is %@"
+ "EnableInterstitials"
+ "Ignoring media selection change for non-active player item %@"
+ "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToDate on current player item"
+ "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToDate on integrated timeline"
+ "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToTime on current player item"
+ "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToTime on integrated timeline"
+ "Integrated timeline duration did change to %@"
+ "Integrated timeline snapshots out of sync with reason %@"
+ "Integrated timeline time did jump"
+ "Interstitial in progress: %@"
+ "Interstitial player item did change to %@"
+ "Interstitial player item media selection did change"
+ "Interstitial player item status did change to %@"
+ "Interstitial player's time control status changed while an interstitial is not in progress.  Ignoring"
+ "Not the same show; setting preferred audio language to nil"
+ "Performing automatic re-selection of audio for player item %@ in player %@"
+ "Primary player item media selection did change"
+ "Prior to enqueueing item, seeking integrated timeline to %@"
+ "Selected audio option: %@"
+ "Setting audible media selection criteria on %@ (is interstitial player: %@) to %@"
+ "T@\"AVPlayerInterstitialEventMonitor\",&,N,V_interstitialEventMonitor"
+ "T@\"NSMutableArray\",&,N,V_tokensFromIntegratedTimeline"
+ "TB,N,V_isPlayingInterstitial"
+ "TVApp"
+ "TVPMediaItemMetadataHapticsURLString"
+ "Unable to add boundary time observer to timeline.  Desired time is %@, segments are %@, currentSegment is %@"
+ "Unable to load audible media selection group due to error %@"
+ "Using interstitial player's time control status since an interstitial is in progress"
+ "Will perform automatic re-selection of audio for player item %@ in player %@"
+ "_activePlayerItem"
+ "_addBoundaryTimeObserversToIntegratedTimeline:"
+ "_addObserversToInterstitialEventMonitor:"
+ "_addPeriodicTimeObserverToIntegratedTimeline:"
+ "_avPlayer:timeControlStatusDidChangeTo:oldStatusNum:"
+ "_configureAutoSubtitlesForPlayer:"
+ "_currentTimeControlStatus"
+ "_currentTimeDidChangeTo:"
+ "_durationDidChangeTo:isTimeline:"
+ "_integratedTimelineSnapshotsOutOfSync:"
+ "_interstitialEventMonitor"
+ "_interstitialsEnabled"
+ "_isPlayingInterstitial"
+ "_notifyOfMediaSelectionOptionChanges"
+ "_playerItemMediaSelectionDidChange:"
+ "_removeBoundaryTimeObserversFromIntegratedTimeline:"
+ "_removeObserversFromInterstitialEventMonitor:"
+ "_removePeriodicTimeObserverFromIntegratedTimeline:"
+ "_tokensFromIntegratedTimeline"
+ "_updateAudioSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:mediaItemLoader:preferredAudioLanguageCodes:prefersAudioDescriptions:"
+ "addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:"
+ "com.apple.amp.tv.is-default"
+ "com.apple.hls.haptics.url"
+ "currentSegment"
+ "currentSnapshot"
+ "initWithPremiumMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:"
+ "initWithPrimaryPlayer:"
+ "integratedTimeline"
+ "interstitial"
+ "interstitialEventMonitor"
+ "interstitialPlayer"
+ "interstitialPlayer.currentItem"
+ "interstitialPlayer.currentItem.status"
+ "interstitialPlayer.timeControlStatus"
+ "isPlayingInterstitial"
+ "loadMediaSelectionGroupForMediaCharacteristic:completionHandler:"
+ "main"
+ "mapTime:toSegment:atSegmentOffset:"
+ "playerItem %@ shouldSeekToTime:%@ currentTime:%@ currentDate:%@"
+ "premiumMediaCharacteristics"
+ "segmentType"
+ "segments"
+ "setExternalPlaybackInterstitialSchedulingStrategy:"
+ "setInterstitialEventMonitor:"
+ "setIsPlayingInterstitial:"
+ "setTokensFromIntegratedTimeline:"
+ "tokensFromIntegratedTimeline"
+ "v24@?0@\"AVMediaSelectionGroup\"8@\"NSError\"16"
+ "v40@0:8@16q24@32"
+ "v44@0:8{?=qiIq}16B40"
+ "v48@0:8@16B24@28@36B44"
+ "\x82E\x1e\x127\x1e\x13"
- "?9FP"
- "?="
- "@\"TVPChapterCollection\"8@?0"
- "AVPlayer timeControlStatus did change to %@.  reasonForWaiting is %@"
- "Assuming likelyToKeepUp is YES because playback has started"
- "Boundary time observer for forward playback end time fired."
- "Boundary time observer for reverse playback end time fired."
- "Default audio option is downloaded.  Will pick default audio option"
- "Default audio option is not downloaded.  Will let Core Media pick whatever it wants"
- "Ignoring forward playback boundary time observer since player isn't playing or scanning."
- "Ignoring reverse playback boundary time observer since player isn't scanning."
- "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToDate"
- "In _setElapsedTimeOrDateOnCurrentPlayerItem, calling seekToTime"
- "Sending \"Sufficient Buffer Did Become Available\" since entire scene is loaded"
- "Setting audible media selection criteria to %@"
- "Setting player's preferred audio language code to nil since selected language option, %@, is the default"
- "Sufficient buffer did become available"
- "T@\"NSArray\",&,N,V_audioOptions"
- "T@\"NSArray\",&,N,V_playbackEndTimeBoundaryObserverTokens"
- "T@\"NSArray\",&,N,V_subtitleOptions"
- "TB,N,V_sceneCompletelyBuffered"
- "Waiting for sufficient buffer"
- "_addPlaybackEndTimeBoundaryObservers"
- "_audioOptions"
- "_avPlayerTimeDidChangeTo:"
- "_currentPlayerItemDurationDidChangeTo:"
- "_currentPlayerItemMediaSelectionDidChange:"
- "_isPlaybackLikelyToKeepUp"
- "_playbackEndTimeBoundaryObserverTokens"
- "_removePlaybackEndTimeBoundaryObservers"
- "_sceneCompletelyBuffered"
- "_subtitleOptions"
- "_timeControlStatusDidChangeTo:oldStatusNum:"
- "_updateAudioSelectionCriteriaForAVQueuePlayer:mediaItemLoader:preferredAudioLanguageCodes:prefersAudioDescriptions:"
- "assetCache"
- "com.apple.tv.nevergonnagiveyouup"
- "defaultOption"
- "initWithPrincipalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:"
- "isPlaybackBufferFull"
- "isPlaybackLikelyToKeepUp"
- "mediaSelectionOptionsInMediaSelectionGroup:"
- "playbackEndTimeBoundaryObserverTokens"
- "playerItem shouldSeekToTime:%@ currentTime:%@ currentDate:%@"
- "sceneCompletelyBuffered"
- "setAudioOptions:"
- "setPlaybackEndTimeBoundaryObserverTokens:"
- "setSceneCompletelyBuffered:"
- "setSubtitleOptions:"
- "updateSubtitleOptionsAndSelection"
- "v44@0:8@16@24@32B40"
- "\x82G\x1e\x127\x1e\x13"

```
