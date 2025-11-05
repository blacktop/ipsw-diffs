## PhotosPlayer

> `/System/iOSSupport/System/Library/PrivateFrameworks/PhotosPlayer.framework/Versions/A/PhotosPlayer`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x2993c
-  __TEXT.__auth_stubs: 0x800
-  __TEXT.__objc_methlist: 0x3c64
+751.0.104.0.0
+  __TEXT.__text: 0x29770
+  __TEXT.__auth_stubs: 0x7f0
+  __TEXT.__objc_methlist: 0x410c
   __TEXT.__const: 0x208
-  __TEXT.__gcc_except_tab: 0x8e4
+  __TEXT.__gcc_except_tab: 0x8e0
   __TEXT.__cstring: 0xfb3
   __TEXT.__oslogstring: 0x81c
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x1228
+  __TEXT.__unwind_info: 0x1218
   __TEXT.__objc_classname: 0x64c
   __TEXT.__objc_methname: 0xb053
   __TEXT.__objc_methtype: 0x198e

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24f0
+  __DATA_CONST.__objc_selrefs: 0x25b0
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x410
+  __AUTH_CONST.__auth_got: 0x408
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x7b88
+  __AUTH_CONST.__objc_const: 0x7330
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 25181DC0-EE0F-38FE-B79C-E7B08A925DC9
-  Functions: 1571
-  Symbols:   3967
+  UUID: F5355297-5BB4-3F66-815C-FCDDE5C814FB
+  Functions: 1570
+  Symbols:   3966
   CStrings:  2574
 
Symbols:
- _objc_retain_x28
Functions:
~ -[ISRateCurveRequest _stopObservingPlayer] : 100 -> 92
~ -[ISRateCurveRequest _stepDownRate] : 492 -> 468
~ -[ISRateCurveRequest start] : 568 -> 564
~ -[ISAVPlayer init] : 124 -> 120
~ +[ISAVPlayer isSpringBoard] : 68 -> 72
~ +[ISAVPlayer isAppleInternal] : 68 -> 72
~ -[ISAsset initWithVideoAsset:UIImage:photoTime:photoEXIFOrientation:options:] : 160 -> 164
~ -[ISBasePlayer _newWrappedPlayer] : 208 -> 216
~ -[ISBasePlayer _mainQueue_resetAVObjectsWithResetCount:] : 244 -> 240
~ -[ISBasePlayer _mainQueue_handleMediaServicesReset] : 220 -> 216
~ -[ISBasePlayer _updateVideoPlayerVolumeIfNeeded] : 196 -> 180
~ -[ISBasePlayer _needsUpdate] : 76 -> 96
~ ___43-[ISBasePlayer _setForwardPlaybackEndTime:]_block_invoke : 200 -> 188
~ -[ISBasePlayer _setStatus:] : 96 -> 88
~ -[ISBasePlayer _updateStatusIfNeeded] : 272 -> 276
~ -[ISBasePlayer _updateWillPlayToPhotoObserverIfNeeded] : 840 -> 836
~ ___54-[ISBasePlayer _updateWillPlayToPhotoObserverIfNeeded]_block_invoke : 156 -> 160
~ -[ISBasePlayer _updateWillPlayToEndObserverIfNeeded] : 788 -> 780
~ ___52-[ISBasePlayer _updateWillPlayToEndObserverIfNeeded]_block_invoke : 156 -> 160
~ -[ISBasePlayer _updateContentFromPlayerItemIfNeeded] : 484 -> 456
~ ___78-[ISBasePlayer applyOutputInfo:fromBehavior:withTransitionOptions:completion:]_block_invoke : 224 -> 252
~ ___78-[ISBasePlayer applyOutputInfo:fromBehavior:withTransitionOptions:completion:]_block_invoke_3 : 32 -> 28
~ ___60-[ISBasePlayer applyScale:withTransitionOptions:completion:]_block_invoke_2 : 32 -> 28
~ -[ISBasePlayer setActiveBehavior:] : 280 -> 276
~ -[ISBasePlayer setAudioVolume:] : 132 -> 140
~ -[ISBasePlayer setAudioEnabled:] : 132 -> 136
~ -[ISBasePlayer addOutput:] : 324 -> 316
~ -[ISBasePlayer setDelegate:] : 212 -> 208
~ -[ISBasePlayerUIView setOverrideImage:] : 136 -> 132
~ -[ISBasePlayerUIView generateSnapshotImage] : 616 -> 612
~ -[ISBasePlayerUIView setContent:] : 456 -> 452
~ -[ISBasePlayerUIView _signalChange:withAnimationDuration:] : 140 -> 128
~ -[ISBasePlayerUIView _updateAudioSession] : 212 -> 216
~ ___41-[ISBasePlayerUIView _updateAudioSession]_block_invoke : 200 -> 196
~ -[ISBasePlayerUIView setPlayer:] : 196 -> 192
~ -[ISBasePlayerUIView _setWrappedAudioSession:] : 116 -> 112
~ -[ISBasePlayerUIView setCustomPhotoView:] : 132 -> 128
~ -[ISBasePlayerUIView setVideoFilter:] : 188 -> 192
~ -[ISBasePlayerUIView _setChangeObserver:] : 160 -> 156
~ -[ISBasePlayerUIView _performCommonInitialization] : 1028 -> 996
~ +[ISDeferredDealloc sharedInstance] : 68 -> 72
~ -[ISDisplayLink _callUpdateHandler] : 100 -> 104
~ -[ISLivePhotoAutoplayVitalityFilter _setState:] : 64 -> 56
~ -[ISLivePhotoAutoplayVitalityFilter updateOutput] : 324 -> 328
~ -[ISKVOProxyManager addProxyWithTarget:queue:keyPaths:delegate:] : 416 -> 412
~ -[ISKVOProxy initWithTarget:keyPaths:identifier:delegate:] : 232 -> 224
~ ___64-[ISLivePhotoPlaybackBehavior _transitionToVideoWithPlaybackID:]_block_invoke : 104 -> 108
~ -[ISLivePhotoPlaybackBehavior _handleDidSeekToBeginning] : 192 -> 188
~ -[ISLivePhotoPlaybackBehavior _prepareVideoForPlaybackIfNeeded] : 520 -> 516
~ -[ISLivePhotoPlaybackBehavior startPlayback] : 132 -> 128
~ -[ISLivePhotoPlaybackBehavior _handleDidFinish] : 124 -> 116
~ -[ISLivePhotoPlaybackBehavior videoWillPlayToEnd] : 344 -> 340
~ ___50-[ISLivePhotoPlayer observable:didChange:context:]_block_invoke : 92 -> 84
~ -[ISLivePhotoPlayer _fadeInAudioIfNeeded] : 476 -> 472
~ -[ISLivePhotoPlayer setIsAttemptingToPlayback:] : 132 -> 136
~ -[ISLivePhotoPlayer _setCurrentPlaybackStyle:] : 128 -> 132
~ -[ISLivePhotoPlayer _updateApertureModeIfNeeded] : 156 -> 144
~ -[ISLivePhotoPlayer setVitalityFilter:] : 248 -> 244
~ -[ISLivePhotoSeekBehavior _handleDidSeekToSeekTime:] : 200 -> 204
~ ___40-[ISLivePhotoSeekBehavior _seekIfNeeded]_block_invoke : 264 -> 248
~ -[ISLivePhotoSettleBehavior settle:] : 308 -> 304
~ -[ISLivePhotoUIView gestureRecognizer:shouldReceiveTouch:] : 184 -> 188
~ -[ISLivePhotoUIView gestureRecognizerShouldBegin:] : 88 -> 92
~ -[ISLivePhotoUIView _showOverlayLabel] : 748 -> 744
~ -[ISLivePhotoUIView _setPlaybackFilter:] : 156 -> 152
~ -[ISLivePhotoUIView setVitalityTransform:] : 144 -> 140
~ -[ISLivePhotoUIView setDelegate:] : 216 -> 212
~ -[ISLivePhotoVitalityBehavior _didReachTransitionToPhotoTime] : 472 -> 468
~ -[ISLivePhotoVitalityBehavior _startObservingVideo] : 896 -> 888
~ -[ISLivePhotoVitalityBehavior prepareForVitality] : 580 -> 576
~ ___49-[ISLivePhotoVitalityBehavior prepareForVitality]_block_invoke : 160 -> 164
~ -[ISLiveWallpaperPlayer _seekVideoToEnd] : 320 -> 316
~ -[ISLiveWallpaperPlayer _seekVideoToBeginning] : 292 -> 288
~ -[ISLiveWallpaperPlayer _updatePlayer] : 488 -> 480
~ -[ISLiveWallpaperPlayer _setActive:] : 552 -> 548
~ -[ISLiveWallpaperUIView willMoveToWindow:] : 320 -> 316
~ -[ISAnimatedImagePlayer setDisplayedFrameIndex:] : 136 -> 124
~ -[ISAnimatedImagePlayer setPlaying:] : 84 -> 76
~ -[ISAnimatedImagePlayer _setCurrentFrame:] : 100 -> 92
~ -[ISObservable _observersQueue_copyChangeObserversForWriteIfNeeded] : 352 -> 356
~ -[ISObservable enumerateObserversUsingBlock:] : 756 -> 752
~ ___49-[ISObservable unregisterChangeObserver:context:]_block_invoke : 196 -> 208
~ -[ISObservable performChanges:] : 232 -> 236
~ -[ISPlayerContent isEqual:] : 468 -> 460
~ -[ISPlayerItem _performWork:sync:] : 368 -> 364
~ ___91-[ISPlayerItem _handleVideoPlayerItemLoadResultWithSuccess:playerItem:videoDuration:error:]_block_invoke : 312 -> 316
~ ___46-[ISPlayerItem _updateVideoPlayerItemIfNeeded]_block_invoke_2 : 424 -> 420
~ ___43-[ISPlayerItem setContentSupportsVitality:]_block_invoke : 224 -> 228
~ ___54-[ISPlayerItem _updateContentSupportsVitalityIfNeeded]_block_invoke_2 : 744 -> 740
~ ___40-[ISPlayerItem _setVariationIdentifier:]_block_invoke : 248 -> 252
~ ___58-[ISPlayerItem setDecodesAllFramesDuringOrdinaryPlayback:]_block_invoke : 44 -> 40
~ ___51-[ISPlayerItem setReversesMoreVideoFramesInMemory:]_block_invoke : 44 -> 40
~ ___48-[ISPlayerItem setAggressivelyCacheVideoFrames:]_block_invoke : 44 -> 40
~ ___48-[ISPlayerItem discardContentBelowLoadingTarget]_block_invoke_2 : 100 -> 108
~ -[_ISPlayerItemChefOperation _preparePlayerItem] : 2004 -> 2000
~ -[_ISPlayerItemChefOperation main] : 216 -> 212
~ -[ISPlayerView _updateReadyForDisplayIfNeeded] : 136 -> 124
~ -[ISPlayerView _updatePlaybackStateIfNeeded] : 260 -> 248
~ -[ISPlayerView _updateStatusIfNeeded] : 172 -> 160
~ -[ISPlayerView _updatePlayerMutedIfNeeded] : 152 -> 140
~ -[ISPlayerView _updatePlayerPlayerItemIfNeeded] : 160 -> 148
~ -[ISPlayerView _updatePlayerItemLoadingTargetIfNeeded] : 144 -> 132
~ -[ISPlayerView _updatePlayerViewIfNeeded] : 188 -> 176
~ -[ISPlayerView _needsUpdate] : 84 -> 108
~ -[ISPlayerView _setGestureRecognizer:] : 156 -> 160
~ -[ISPlayerView _setPlayerView:] : 680 -> 676
~ -[ISPlayerView _setPlaybackState:] : 144 -> 148
~ -[ISPlayerView _setInteracting:] : 144 -> 148
~ -[ISPlayerView _setPlayerItem:] : 196 -> 192
~ -[ISPlayerView setDelegate:] : 212 -> 208
~ -[ISPlayerView setAudioMuted:] : 92 -> 84
~ -[ISPlayerView setPlaybackStyle:] : 100 -> 92
~ ___56-[ISScrollViewVitalityController _updateVitalityFilters]_block_invoke : 548 -> 552
~ -[ISScrollViewVitalityController setEnabled:] : 124 -> 128
~ -[ISAnimatedImageView setImage:] : 164 -> 160
~ -[ISAnimatedImageView setPlayer:] : 204 -> 200
~ -[ISAnimatedImageView initWithAnimatedImagePlayer:] : 128 -> 124
~ -[ISTouchLivePhotoPlaybackFilter setTouchActive:] : 408 -> 404
~ ___76-[ISTransitionApplier _applyScale:toLayer:withTransitionOptions:completion:]_block_invoke : 32 -> 28
~ ___87-[ISTransitionApplier _applyAlpha:blurRadius:toLayer:withTransitionOptions:completion:]_block_invoke : 32 -> 28
~ ___87-[ISTransitionApplier _applyAlpha:blurRadius:toLayer:withTransitionOptions:completion:]_block_invoke_2 : 32 -> 28
~ ___91-[ISTransitionApplier applyScale:withTransitionOptions:toPhotoLayer:videoLayer:completion:]_block_invoke : 32 -> 28
~ ___91-[ISTransitionApplier applyScale:withTransitionOptions:toPhotoLayer:videoLayer:completion:]_block_invoke_2 : 32 -> 28
~ ___96-[ISTransitionApplier applyOutputInfo:withTransitionOptions:toPhotoLayer:videoLayer:completion:]_block_invoke : 32 -> 28
~ ___96-[ISTransitionApplier applyOutputInfo:withTransitionOptions:toPhotoLayer:videoLayer:completion:]_block_invoke_2 : 32 -> 28
~ ___76-[ISUIScrollViewVitalityController scrollViewDidEndDragging:willDecelerate:]_block_invoke : 152 -> 156
~ -[ISVideoPlayerUIView setVideoPlayer:] : 152 -> 148
~ -[ISVisibilityOffsetHelper getVisibility:offset:targetVisibilityOffset:forView:] : 532 -> 536
~ -[ISVisibilityOffsetHelper _visibilityRangeForRect:] : 320 -> 316
- sub_1d17355e0
~ ___81-[ISWrappedAVPlayer seekToTime:toleranceBefore:toleranceAfter:completionHandler:]_block_invoke_2 : 156 -> 140
~ ___39-[ISWrappedAVPlayer setLoopingEnabled:]_block_invoke_2 : 256 -> 260
~ -[ISWrappedAVPlayer addBoundaryTimeObserverForTimes:queue:usingBlock:] : 288 -> 284
~ -[ISWrappedAVPlayer addPeriodicTimeObserverForInterval:queue:usingBlock:] : 268 -> 264
~ -[ISWrappedAVPlayer _initWithAVPlayer:] : 960 -> 928
~ ___39-[ISWrappedAVPlayer _initWithAVPlayer:]_block_invoke_2 : 200 -> 196
~ -[ISWrappedAVPlayer _performPlayerTransaction:] : 216 -> 212
~ -[ISWrappedAVPlayer unregisterChangeObserver:context:] : 224 -> 220
~ -[ISWrappedAVPlayer registerChangeObserver:context:] : 224 -> 220

```
