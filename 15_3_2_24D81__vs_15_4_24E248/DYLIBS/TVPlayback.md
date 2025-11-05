## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/Versions/A/TVPlayback`

```diff

-563.30.1.0.0
-  __TEXT.__text: 0x5f12c
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x4ac4
-  __TEXT.__const: 0x218
-  __TEXT.__cstring: 0x623a
-  __TEXT.__oslogstring: 0x3d3d
-  __TEXT.__gcc_except_tab: 0x2078
-  __TEXT.__unwind_info: 0x1418
-  __TEXT.__objc_classname: 0x6d4
-  __TEXT.__objc_methname: 0x10702
-  __TEXT.__objc_methtype: 0x1f04
-  __TEXT.__objc_stubs: 0xa0c0
-  __DATA_CONST.__got: 0x658
-  __DATA_CONST.__const: 0xc68
+563.40.18.0.0
+  __TEXT.__text: 0x61bf8
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x5540
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0x62dc
+  __TEXT.__oslogstring: 0x41b9
+  __TEXT.__gcc_except_tab: 0x2210
+  __TEXT.__unwind_info: 0x1490
+  __TEXT.__objc_classname: 0x6ff
+  __TEXT.__objc_methname: 0x109aa
+  __TEXT.__objc_methtype: 0x1fa9
+  __TEXT.__objc_stubs: 0xa2e0
+  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x70
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3690
+  __DATA_CONST.__objc_selrefs: 0x3898
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x318
-  __AUTH_CONST.__const: 0x1c40
-  __AUTH_CONST.__cfstring: 0x6140
-  __AUTH_CONST.__objc_const: 0x95c8
+  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__const: 0x1c70
+  __AUTH_CONST.__cfstring: 0x6200
+  __AUTH_CONST.__objc_const: 0x8360
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x664
-  __DATA.__data: 0x848
+  __DATA.__objc_ivar: 0x660
+  __DATA.__data: 0x8c0
   __DATA.__bss: 0x288
   __DATA.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 77AD69FB-5DFC-393B-A7FB-73C42471BE7F
-  Functions: 1972
-  Symbols:   5264
-  CStrings:  4863
+  UUID: 032A41DB-4A1A-33D3-AEC0-B646660C19AA
+  Functions: 2025
+  Symbols:   5358
+  CStrings:  4920
 
Symbols:
+ +[NSDateFormatter(TVPlaybackAdditions) tvp_ISO8601CombinedDateAndTimeFormatter].cold.1
+ +[NSDateFormatter(TVPlaybackAdditions) tvp_RFC1123DateFormatter].cold.1
+ +[NSDateFormatter(TVPlaybackAdditions) tvp_RFC850DateFormatter].cold.1
+ +[NSDateFormatter(TVPlaybackAdditions) tvp_asctimeDateFormatter].cold.1
+ +[TVPContentKeyRequest initialize].cold.1
+ +[TVPContentKeySession initialize].cold.1
+ +[TVPMPPlaybackQueueManager _mediaItemPropertyToMediaRemotePropertyMapping].cold.1
+ +[TVPMPPlaybackQueueManager _mediaPlayerMediaTypeForMediaItemMediaType:].cold.1
+ +[TVPMediaItemLoader initialize].cold.1
+ +[TVPMediaItemLoader loaderForMediaItem:].cold.1
+ +[TVPMediaRemoteManager sharedInstance].cold.1
+ +[TVPPlaybackReportingEventCollection initialize].cold.1
+ +[TVPPlaybackState loading].cold.1
+ +[TVPPlaybackState paused].cold.1
+ +[TVPPlaybackState playing].cold.1
+ +[TVPPlaybackState scanning].cold.1
+ +[TVPPlaybackState stopped].cold.1
+ +[TVPPlayer _audioSelectionCriteriaForPreferredAudioLanguageCodes:prefersAudioDescriptions:]
+ +[TVPPlayer _configureAutoSubtitlesForPlayer:]
+ +[TVPPlayer _updateAudioSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:preferredAudioLanguageCodes:prefersAudioDescriptions:]
+ +[TVPPlayer automaticallyNotifiesObserversForKey:].cold.1
+ +[TVPPlayer initialize].cold.1
+ +[TVPPlayer(TVPlaybackAdditions) _initConstants].cold.1
+ +[TVPPlayerReporter initialize].cold.1
+ +[TVPReachabilityMonitor sharedInstance].cold.1
+ +[TVPReportingSession initialize].cold.1
+ +[TVPVideoView initialize].cold.1
+ -[NSArray(TVPlaybackAdditions) tvp_randomizedArray].cold.1
+ -[TVPBoundaryTimeObserverInfo init]
+ -[TVPBoundaryTimeObserverInfo setTokensFromIntegratedTimeline:]
+ -[TVPBoundaryTimeObserverInfo tokensFromIntegratedTimeline]
+ -[TVPMediaItemLoader _avAssetOptions].cold.1
+ -[TVPMediaRemoteCommandHandler _allAudioMediaTypes].cold.1
+ -[TVPPlayer _activePlayerItem]
+ -[TVPPlayer _activePlayerTimeControlStatus]
+ -[TVPPlayer _activePlayer]
+ -[TVPPlayer _addBoundaryTimeObserversToIntegratedTimeline:]
+ -[TVPPlayer _addObserversToInterstitialEventMonitor:]
+ -[TVPPlayer _addPeriodicTimeObserverToIntegratedTimeline:]
+ -[TVPPlayer _avPlayer:timeControlStatusDidChangeTo:oldStatusNum:]
+ -[TVPPlayer _currentMediaItemMetadataDidChange:].cold.1
+ -[TVPPlayer _currentTimeDidChangeTo:]
+ -[TVPPlayer _durationDidChangeTo:isTimeline:]
+ -[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]
+ -[TVPPlayer _interstitialInProgress]
+ -[TVPPlayer _interstitialsEnabled]
+ -[TVPPlayer _notifyOfMediaSelectionOptionChanges]
+ -[TVPPlayer _playerItemMediaSelectionDidChange:]
+ -[TVPPlayer _removeBoundaryTimeObserversFromIntegratedTimeline:]
+ -[TVPPlayer _removeObserversFromInterstitialEventMonitor:]
+ -[TVPPlayer _removePeriodicTimeObserverFromIntegratedTimeline:]
+ -[TVPPlayer _statesThatReturnAVPlayerTime].cold.1
+ -[TVPPlayer _statesThatReturnSeekTime].cold.1
+ -[TVPPlayer _statesThatReturnStartTime].cold.1
+ -[TVPPlayer integratedTimeline:willSeekToTime:currentTime:]
+ -[TVPPlayer interstitialEventMonitor]
+ -[TVPPlayer isPlayingInterstitial]
+ -[TVPPlayer setInterstitialEventMonitor:]
+ -[TVPPlayer setIsPlayingInterstitial:]
+ GCC_except_table123
+ GCC_except_table129
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table291
+ GCC_except_table323
+ GCC_except_table335
+ GCC_except_table362
+ GCC_except_table366
+ GCC_except_table381
+ GCC_except_table405
+ GCC_except_table413
+ GCC_except_table418
+ GCC_except_table422
+ GCC_except_table423
+ GCC_except_table425
+ GCC_except_table428
+ GCC_except_table429
+ GCC_except_table435
+ GCC_except_table439
+ GCC_except_table444
+ GCC_except_table448
+ GCC_except_table453
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table492
+ GCC_except_table494
+ GCC_except_table510
+ GCC_except_table513
+ GCC_except_table518
+ GCC_except_table522
+ GCC_except_table53
+ GCC_except_table536
+ GCC_except_table539
+ GCC_except_table551
+ GCC_except_table553
+ GCC_except_table556
+ GCC_except_table560
+ GCC_except_table62
+ GCC_except_table63
+ GCC_except_table722
+ OBJC_IVAR_$_TVPBoundaryTimeObserverInfo._tokensFromIntegratedTimeline
+ OBJC_IVAR_$_TVPPlayer._interstitialEventMonitor
+ OBJC_IVAR_$_TVPPlayer._isPlayingInterstitial
+ _AVMediaCharacteristicIsOriginalContent
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncNotification
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonKey
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonLoadedTimeRangesChanged
+ _AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonSegmentsChanged
+ _AVPlayerWaitingDuringInterstitialEventReason
+ _OBJC_CLASS_$_AVPlayerInterstitialEventMonitor
+ _TVPMediaItemMetadataHapticsURLString
+ __23-[TVPPlayer invalidate]_block_invoke.394
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1001
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1002
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1011
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1017
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1024
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1031
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1036
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1042
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1052
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1056
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.748
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.754
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.758
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.766
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.770
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.772
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.775
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.791
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.794.cold.1
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.806
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.815
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.816
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.824
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.826
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.833
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.834
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.835
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.842
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.843
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.849
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.850
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.861
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.864
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.884
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.894
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.900
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.905
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.914
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.915
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.922
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.924
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.928
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.937
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.943
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.945
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.948
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.950
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.952
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.956
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.968
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.977
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.978
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.979
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.981
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.988
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.990
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.992
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.996
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1003
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1012
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1018
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1025
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1032
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1037
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1057
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.749
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.776
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.798
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.874
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.895
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.906
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.944
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.946
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.949
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.953
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.957
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.959
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.980
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.984
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.989
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.993
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.997
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1004
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1013
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1019
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1026
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1033
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1038
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1060
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.777
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.799
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.875
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.880
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.896
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.954
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.960
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.994
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.998
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1005
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1014
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1020
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1027
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1041
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1041.cold.1
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1041.cold.2
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1041.cold.3
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1041.cold.4
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1061
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.800
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.881
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.955
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.961
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.995
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.1006
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.1021
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.1028
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.1062
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.1007
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.1029
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.1008
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.1030
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.1009
+ __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.1010
+ __43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.595
+ __48-[TVPPlayer _playerItemMediaSelectionDidChange:]_block_invoke.cold.1
+ __48-[TVPPlayer _updateVideoViewsWithAVQueuePlayer:]_block_invoke.652
+ __51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke.606
+ __53-[TVPPlayer _addPeriodicTimeObserverToAVQueuePlayer:]_block_invoke.520
+ __56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.422
+ __56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.423
+ __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.491
+ __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.495
+ __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.499
+ __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.500
+ __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.506
+ __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.507
+ __58-[TVPPlayer _addPeriodicTimeObserverToIntegratedTimeline:]_block_invoke.523
+ __58-[TVPPlayer _addPeriodicTimeObserverToIntegratedTimeline:]_block_invoke_2.524
+ __58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.411
+ __58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.418
+ __60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke.405
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_$_PROTOCOL_REFS_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_LABEL_PROTOCOL_$_AVPlayerItemIntegratedTimelineSeekDelegate
+ __OBJC_PROTOCOL_$_AVPlayerItemIntegratedTimelineSeekDelegate
+ ___48-[TVPPlayer _playerItemMediaSelectionDidChange:]_block_invoke
+ ___51-[TVPPlayer _integratedTimelineSnapshotsOutOfSync:]_block_invoke
+ ___53-[TVPPlayer _addHighFrequencyTimeObserverIfNecessary]_block_invoke_2
+ ___53-[TVPPlayer _addHighFrequencyTimeObserverIfNecessary]_block_invoke_3
+ ___54-[TVPPlayer _addBoundaryTimeObserversToAVQueuePlayer:]_block_invoke_3
+ ___58-[TVPPlayer _addPeriodicTimeObserverToIntegratedTimeline:]_block_invoke
+ ___58-[TVPPlayer _addPeriodicTimeObserverToIntegratedTimeline:]_block_invoke_2
+ ___59-[TVPPlayer _addBoundaryTimeObserversToIntegratedTimeline:]_block_invoke
+ ___59-[TVPPlayer _addBoundaryTimeObserversToIntegratedTimeline:]_block_invoke_2
+ ___59-[TVPPlayer integratedTimeline:willSeekToTime:currentTime:]_block_invoke
+ ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___60-[TVPPlayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
+ ___AVInterstitialPlayerCurrentItemKVOContext
+ ___AVInterstitialPlayerItemStatusKVOContext
+ ___AVInterstitialPlayerTimeControlStatusKVOContext
+ ___block_descriptor_280_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s272s_e5_v8?0l
+ ___block_descriptor_312_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248r256r264r272r280r288r296r304w_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e43_v24?0"AVMediaSelectionGroup"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_64_e8_32w_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64s72w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248r256r264r272r280r288r296r304w
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s272s
+ ___copy_helper_block_e8_32s40s48s56s64s72w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248r256r264r272r280r288r296r304w
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s272s
+ __block_literal_global.1040
+ __block_literal_global.2029
+ __block_literal_global.228
+ __block_literal_global.428
+ __block_literal_global.431
+ __block_literal_global.609
+ __block_literal_global.627
+ __block_literal_global.629
+ __block_literal_global.631
+ __block_literal_global.934
+ __os_feature_enabled_impl
+ _objc_msgSend$_activePlayer
+ _objc_msgSend$_activePlayerItem
+ _objc_msgSend$_activePlayerTimeControlStatus
+ _objc_msgSend$_addBoundaryTimeObserversToIntegratedTimeline:
+ _objc_msgSend$_addObserversToInterstitialEventMonitor:
+ _objc_msgSend$_addPeriodicTimeObserverToIntegratedTimeline:
+ _objc_msgSend$_audioSelectionCriteriaForPreferredAudioLanguageCodes:prefersAudioDescriptions:
+ _objc_msgSend$_avPlayer:timeControlStatusDidChangeTo:oldStatusNum:
+ _objc_msgSend$_configureAutoSubtitlesForPlayer:
+ _objc_msgSend$_currentTimeDidChangeTo:
+ _objc_msgSend$_durationDidChangeTo:isTimeline:
+ _objc_msgSend$_interstitialInProgress
+ _objc_msgSend$_interstitialsEnabled
+ _objc_msgSend$_notifyOfMediaSelectionOptionChanges
+ _objc_msgSend$_removeBoundaryTimeObserversFromIntegratedTimeline:
+ _objc_msgSend$_removeObserversFromInterstitialEventMonitor:
+ _objc_msgSend$_removePeriodicTimeObserverFromIntegratedTimeline:
+ _objc_msgSend$_updateAudioSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:preferredAudioLanguageCodes:prefersAudioDescriptions:
+ _objc_msgSend$addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:
+ _objc_msgSend$currentSegment
+ _objc_msgSend$currentSnapshot
+ _objc_msgSend$initWithPremiumMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:
+ _objc_msgSend$initWithPrimaryPlayer:
+ _objc_msgSend$integratedTimeline
+ _objc_msgSend$interstitialEventMonitor
+ _objc_msgSend$interstitialPlayer
+ _objc_msgSend$isPlayingInterstitial
+ _objc_msgSend$loadMediaSelectionGroupForMediaCharacteristic:completionHandler:
+ _objc_msgSend$mapTime:toSegment:atSegmentOffset:
+ _objc_msgSend$premiumMediaCharacteristics
+ _objc_msgSend$segments
+ _objc_msgSend$setExternalPlaybackInterstitialSchedulingStrategy:
+ _objc_msgSend$setInterstitialEventMonitor:
+ _objc_msgSend$setIsPlayingInterstitial:
+ _objc_msgSend$setSeekDelegate:
+ _objc_msgSend$tokensFromIntegratedTimeline
- +[TVPPlayer _audioSelectionCriteriaForPreferredAudioLanguageCodes:mediaItemLoader:prefersAudioDescriptions:]
- +[TVPPlayer _updateAudioSelectionCriteriaForAVQueuePlayer:mediaItemLoader:preferredAudioLanguageCodes:prefersAudioDescriptions:]
- -[TVPPlayer _addPlaybackEndTimeBoundaryObservers]
- -[TVPPlayer _avPlayerTimeDidChangeTo:]
- -[TVPPlayer _currentPlayerItemDurationDidChangeTo:]
- -[TVPPlayer _currentPlayerItemMediaSelectionDidChange:]
- -[TVPPlayer _isPlaybackLikelyToKeepUp]
- -[TVPPlayer _removePlaybackEndTimeBoundaryObservers]
- -[TVPPlayer _timeControlStatusDidChangeTo:oldStatusNum:]
- -[TVPPlayer playbackEndTimeBoundaryObserverTokens]
- -[TVPPlayer sceneCompletelyBuffered]
- -[TVPPlayer setAudioOptions:]
- -[TVPPlayer setPlaybackEndTimeBoundaryObserverTokens:]
- -[TVPPlayer setSceneCompletelyBuffered:]
- -[TVPPlayer setSubtitleOptions:]
- -[TVPPlayer updateSubtitleOptionsAndSelection]
- GCC_except_table115
- GCC_except_table121
- GCC_except_table215
- GCC_except_table219
- GCC_except_table223
- GCC_except_table29
- GCC_except_table299
- GCC_except_table311
- GCC_except_table339
- GCC_except_table343
- GCC_except_table352
- GCC_except_table377
- GCC_except_table384
- GCC_except_table385
- GCC_except_table389
- GCC_except_table390
- GCC_except_table394
- GCC_except_table395
- GCC_except_table397
- GCC_except_table398
- GCC_except_table400
- GCC_except_table401
- GCC_except_table408
- GCC_except_table421
- GCC_except_table434
- GCC_except_table436
- GCC_except_table438
- GCC_except_table467
- GCC_except_table470
- GCC_except_table476
- GCC_except_table483
- GCC_except_table487
- GCC_except_table493
- GCC_except_table511
- GCC_except_table514
- GCC_except_table526
- GCC_except_table531
- GCC_except_table535
- GCC_except_table55
- GCC_except_table690
- OBJC_IVAR_$_TVPPlayer._audioOptions
- OBJC_IVAR_$_TVPPlayer._playbackEndTimeBoundaryObserverTokens
- OBJC_IVAR_$_TVPPlayer._sceneCompletelyBuffered
- OBJC_IVAR_$_TVPPlayer._subtitleOptions
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- __23-[TVPPlayer invalidate]_block_invoke.393
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1005
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1010
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1016
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1026
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.1030
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.710
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.716
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.721
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.725
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.729
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.733
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.737
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.739
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.759
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.762.cold.1
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.771
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.774
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.777
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.783
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.784
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.785
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.792
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.793
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.801
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.802
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.810
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.811
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.818
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.819
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.829
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.832
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.846
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.867
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.874
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.883
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.887
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.888
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.891
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.895
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.897
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.898
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.902
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.904
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.913
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.916
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.921
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.923
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.935
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.936
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.939
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.949
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.951
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.953
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.961
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.965
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.970
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.975
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.976
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.985
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke.998
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1006
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1011
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.1031
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.711
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.717
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.766
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.847
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.852
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.868
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.892
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.903
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.905
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.917
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.922
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.926
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.952
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.956
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.962
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.968
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.971
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.977
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.986
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.992
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_2.999
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1000
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1007
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1012
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.1034
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.744
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.767
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.848
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.853
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.869
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.927
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.933
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.957
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.969
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.972
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.978
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.987
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_3.993
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1001
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1015
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1015.cold.1
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1015.cold.2
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1015.cold.3
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1015.cold.4
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.1035
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.768
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.854
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.928
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.934
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.979
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.988
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_4.994
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.1002
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.1036
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.980
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_5.995
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.1003
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_6.981
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.1004
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_7.982
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_8.983
- __42-[TVPPlayer _registerStateMachineHandlers]_block_invoke_9.984
- __43-[TVPPlayer _currentPlayerItemDidChangeTo:]_block_invoke.564
- __48-[TVPPlayer _updateVideoViewsWithAVQueuePlayer:]_block_invoke.624
- __49-[TVPPlayer _addPlaybackEndTimeBoundaryObservers]_block_invoke.522
- __53-[TVPPlayer _addPeriodicTimeObserverToAVQueuePlayer:]_block_invoke.500
- __56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.411
- __56-[TVPPlayer changeToMediaAtIndex:reason:ignoreDelegate:]_block_invoke.412
- __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.488
- __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.492
- __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.496
- __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.497
- __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke.503
- __58-[TVPMediaItemLoader _loadMediaItemMetadataAsynchronously]_block_invoke_2.504
- __58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.400
- __58-[TVPPlayer changeMediaInDirection:reason:ignoreDelegate:]_block_invoke.407
- ___49-[TVPPlayer _addPlaybackEndTimeBoundaryObservers]_block_invoke
- ___block_descriptor_272_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s_e5_v8?0l
- ___block_descriptor_304_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240r248r256r264r272r280r288r296w_e5_v8?0l
- ___block_descriptor_40_e8_32w_e27_"TVPChapterCollection"8?0l
- ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0l
- ___block_descriptor_80_e8_32s40bs48bs56bs64bs72w_e68_"NSString"40?0"TVPStateMachine"8"NSString"1624"NSDictionary"32l
- ___copy_helper_block_e8_32s40b48b56b64b72w
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240r248r256r264r272r280r288r296w
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s
- ___copy_helper_block_e8_32s40s48s56s64w
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240r248r256r264r272r280r288r296w
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152s160s168s176s184s192s200s208s216s224s232s240s248s256s264s
- __block_literal_global.1014
- __block_literal_global.1994
- __block_literal_global.226
- __block_literal_global.417
- __block_literal_global.420
- __block_literal_global.581
- __block_literal_global.599
- __block_literal_global.601
- __block_literal_global.603
- __block_literal_global.907
- _objc_msgSend$_addPlaybackEndTimeBoundaryObservers
- _objc_msgSend$_audioSelectionCriteriaForPreferredAudioLanguageCodes:mediaItemLoader:prefersAudioDescriptions:
- _objc_msgSend$_avPlayerTimeDidChangeTo:
- _objc_msgSend$_currentPlayerItemDurationDidChangeTo:
- _objc_msgSend$_isPlaybackLikelyToKeepUp
- _objc_msgSend$_removePlaybackEndTimeBoundaryObservers
- _objc_msgSend$_timeControlStatusDidChangeTo:oldStatusNum:
- _objc_msgSend$_updateAudioSelectionCriteriaForAVQueuePlayer:mediaItemLoader:preferredAudioLanguageCodes:prefersAudioDescriptions:
- _objc_msgSend$defaultOption
- _objc_msgSend$initWithPrincipalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:
- _objc_msgSend$isPlaybackBufferFull
- _objc_msgSend$isPlaybackLikelyToKeepUp
- _objc_msgSend$playbackEndTimeBoundaryObserverTokens
- _objc_msgSend$sceneCompletelyBuffered
- _objc_msgSend$setAudioOptions:
- _objc_msgSend$setPlaybackEndTimeBoundaryObserverTokens:
- _objc_msgSend$setSceneCompletelyBuffered:
- _objc_msgSend$setSubtitleOptions:
- _objc_msgSend$updateSubtitleOptions
CStrings:
+ "?:FP"
+ "?>"
+ "@\"AVPlayerInterstitialEventMonitor\""
+ "@28@0:8@16B24"
+ "AVPlayer %@ %@ player timeControlStatus did change to %@.  reasonForWaiting is %@"
+ "AVPlayerItemIntegratedTimelineSeekDelegate"
+ "Active player is %@"
+ "Active player item is %@"
+ "After becoming ready to play, AVPlayer %@ %@ player timeControlStatus is %@."
+ "DisableInterstitials"
+ "Ignoring media selection change for non-active player item %@"
+ "Ignoring status change from non-active player item %@.  Active player item is %@"
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
+ "Player item status did become ready to play"
+ "Primary player item media selection did change"
+ "Prior to enqueueing item, seeking integrated timeline to %@"
+ "Selected audio option: %@"
+ "Setting audible media selection criteria on %@ (is interstitial player: %@) to %@"
+ "Setting cached audio option from active player item %@ to %@."
+ "T@\"AVPlayerInterstitialEventMonitor\",&,N,V_interstitialEventMonitor"
+ "T@\"NSMutableArray\",&,N,V_tokensFromIntegratedTimeline"
+ "TB,N,V_isPlayingInterstitial"
+ "TVApp"
+ "TVPMediaItemMetadataHapticsURLString"
+ "Unable to add boundary time observer to timeline.  Desired time is %@, segments are %@, currentSegment is %@"
+ "Unable to load audible media selection group due to error %@"
+ "Using interstitial player's time control status since an interstitial is in progress"
+ "Will perform automatic re-selection of audio for player item %@ in player %@"
+ "_activePlayer"
+ "_activePlayerItem"
+ "_activePlayerTimeControlStatus"
+ "_addBoundaryTimeObserversToIntegratedTimeline:"
+ "_addObserversToInterstitialEventMonitor:"
+ "_addPeriodicTimeObserverToIntegratedTimeline:"
+ "_audioSelectionCriteriaForPreferredAudioLanguageCodes:prefersAudioDescriptions:"
+ "_avPlayer:timeControlStatusDidChangeTo:oldStatusNum:"
+ "_configureAutoSubtitlesForPlayer:"
+ "_currentTimeDidChangeTo:"
+ "_durationDidChangeTo:isTimeline:"
+ "_integratedTimelineSnapshotsOutOfSync:"
+ "_interstitialEventMonitor"
+ "_interstitialInProgress"
+ "_interstitialsEnabled"
+ "_isPlayingInterstitial"
+ "_notifyOfMediaSelectionOptionChanges"
+ "_playerItemMediaSelectionDidChange:"
+ "_removeBoundaryTimeObserversFromIntegratedTimeline:"
+ "_removeObserversFromInterstitialEventMonitor:"
+ "_removePeriodicTimeObserverFromIntegratedTimeline:"
+ "_tokensFromIntegratedTimeline"
+ "_updateAudioSelectionCriteriaForAVQueuePlayer:isInterstitialPlayer:preferredAudioLanguageCodes:prefersAudioDescriptions:"
+ "addBoundaryTimeObserverForSegment:offsetsIntoSegment:queue:usingBlock:"
+ "com.apple.amp.tv.is-default"
+ "com.apple.hls.haptics.url"
+ "currentSegment"
+ "currentSnapshot"
+ "initWithPremiumMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:"
+ "initWithPrimaryPlayer:"
+ "integratedTimeline"
+ "integratedTimeline %@ willSeekToTime:%@ currentTime:%@ currentDate:%@"
+ "integratedTimeline:willSeekToTime:currentTime:"
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
+ "segments"
+ "setExternalPlaybackInterstitialSchedulingStrategy:"
+ "setInterstitialEventMonitor:"
+ "setIsPlayingInterstitial:"
+ "setSeekDelegate:"
+ "setTokensFromIntegratedTimeline:"
+ "tokensFromIntegratedTimeline"
+ "v24@?0@\"AVMediaSelectionGroup\"8@\"NSError\"16"
+ "v40@0:8@16B24@28B36"
+ "v40@0:8@16q24@32"
+ "v44@0:8{?=qiIq}16B40"
+ "v72@0:8@\"AVPlayerItemIntegratedTimeline\"16{?=qiIq}24{?=qiIq}48"
+ "v72@0:8@16{?=qiIq}24{?=qiIq}48"
- "?9FP"
- "?="
- "@\"TVPChapterCollection\"8@?0"
- "@36@0:8@16@24B32"
- "AVPlayer timeControlStatus did change to %@.  reasonForWaiting is %@"
- "Assuming likelyToKeepUp is YES because playback has started"
- "Boundary time observer for forward playback end time fired."
- "Boundary time observer for reverse playback end time fired."
- "Current player item status did become ready to play"
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
- "_audioSelectionCriteriaForPreferredAudioLanguageCodes:mediaItemLoader:prefersAudioDescriptions:"
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
- "com.apple.tv.nevergonnagiveyouup"
- "defaultOption"
- "initWithPrincipalMediaCharacteristics:preferredLanguages:preferredMediaCharacteristics:"
- "isPlaybackBufferFull"
- "isPlaybackLikelyToKeepUp"
- "playbackEndTimeBoundaryObserverTokens"
- "playerItem shouldSeekToTime:%@ currentTime:%@ currentDate:%@"
- "sceneCompletelyBuffered"
- "setAudioOptions:"
- "setPlaybackEndTimeBoundaryObserverTokens:"
- "setSceneCompletelyBuffered:"
- "setSubtitleOptions:"
- "updateSubtitleOptionsAndSelection"
- "v44@0:8@16@24@32B40"

```
