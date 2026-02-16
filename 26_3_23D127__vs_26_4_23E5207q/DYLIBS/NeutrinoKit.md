## NeutrinoKit

> `/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit`

```diff

-832.0.107.0.0
-  __TEXT.__text: 0x18370
-  __TEXT.__auth_stubs: 0x960
+840.1.220.0.0
+  __TEXT.__text: 0x190f0
+  __TEXT.__auth_stubs: 0x920
   __TEXT.__objc_methlist: 0x1a14
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0x244
-  __TEXT.__cstring: 0x1011
+  __TEXT.__cstring: 0x114c
   __TEXT.__oslogstring: 0xa99
-  __TEXT.__unwind_info: 0x6e0
+  __TEXT.__unwind_info: 0x720
   __TEXT.__objc_classname: 0x27a
   __TEXT.__objc_methname: 0x4f9d
   __TEXT.__objc_methtype: 0x1284

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x16b0
   __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x4c0
+  __AUTH_CONST.__auth_got: 0x4a0
   __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0xac0
   __AUTH_CONST.__objc_const: 0x2a00

   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2B1A39A-482A-31D7-BE72-CC53E1870B43
+  UUID: EC3B7200-3927-378C-821F-D9DA2431BC55
   Functions: 561
-  Symbols:   2346
+  Symbols:   2342
   CStrings:  1434
 
Symbols:
+ _dispatch_assert_queue$V2
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x8
Functions:
~ -[NUScrollView description] : 156 -> 164
~ -[CALayer(NeutrinoUIDebugging) _nu_recursiveDescriptionWithLevel:result:] : 924 -> 960
~ -[_NUAVPlayerItemObservation setPlayerItem:] : 12 -> 64
~ -[NUAVPlayerController setPlayer:] : 12 -> 64
~ -[NUAVPlayerController _addPlayerItemKVO:] : 516 -> 524
~ -[NUAVPlayerController _removePlayerItemKVO:removeFromArray:] : 484 -> 492
~ -[NUAVPlayerController _addPlayerKVO] : 244 -> 260
~ -[NUAVPlayerController _removePlayerKVO] : 224 -> 240
~ -[NUAVPlayerController _setRate:] : 96 -> 100
~ -[NUAVPlayerController playerItemFailedToPlayToEnd:] : 136 -> 148
~ -[NUAVPlayerController playerItemDidReachEnd:] : 160 -> 172
~ -[NUAVPlayerController _removeTimeObserver] : 92 -> 96
~ -[NUAVPlayerController currentTime] : 172 -> 176
~ -[NUAVPlayerController _addTimeObserver] : 464 -> 480
~ ___40-[NUAVPlayerController _addTimeObserver]_block_invoke : 304 -> 308
~ -[NUAVPlayerController step:] : 104 -> 112
~ -[NUAVPlayerController seek:toleranceBefore:toleranceAfter:forceSeek:completionHandler:] : 856 -> 860
~ -[NUAVPlayerController seekBack] : 300 -> 312
~ -[NUAVPlayerController seekForward] : 368 -> 380
~ -[NUAVPlayerController setLoopsVideo:] : 552 -> 564
~ -[NUAVPlayerController observeValueForKeyPath:ofObject:change:context:] : 1888 -> 1932
~ -[NUAVPlayerController updateAppliesPerFrameHDRDisplayMetadata:] : 488 -> 496
~ _AlwaysApplyPerFrameHDRDisplayMetadata : 80 -> 84
~ -[NUAVPlayerController updateAudioMix:] : 520 -> 528
~ -[NUAVPlayerController updateWithVideoPrepareNodeFromVideoComposition:] : 564 -> 592
~ -[NUAVPlayerController updateVideoComposition:] : 520 -> 528
~ -[NUAVPlayerController _playerItemsWithVideoAsset:videoComposition:audioMix:loopsVideo:] : 536 -> 544
~ -[NUAVPlayerController prepareWithAVAsset:videoComposition:audioMix:loopsVideo:seekToTime:] : 1224 -> 1228
~ -[NUAVPlayerController dealloc] : 320 -> 324
~ -[NUAVPlayerView _setReadyForDisplay:] : 108 -> 112
~ -[NUAVPlayerView _updateReadyForDisplayWithID:] : 116 -> 120
~ -[NUAVPlayerView dispose] : 168 -> 176
~ __commonInit : 108 -> 116
~ -[NUAVPlayerView setPlayer:] : 172 -> 192
~ -[NUMediaView playerControllerIsReadyForPlayback:] : 284 -> 288
~ -[NUMediaView playerControllerDidFinishPlaying:duration:] : 308 -> 312
~ -[NUMediaView playerRateDidChange:rate:] : 152 -> 156
~ -[NUMediaView hasOverlayWithIdentifier:] : 64 -> 68
~ -[NUMediaView removeOverlayWithIdentifier:] : 132 -> 140
~ -[NUMediaView addOverlay:withIdentifier:style:] : 492 -> 544
~ -[NUMediaView _visibleImageRectOverlayView] : 16 -> 64
~ -[NUMediaView _updateContentInsets] : 592 -> 600
~ -[NUMediaView _imageSize] : 300 -> 304
~ -[NUMediaView _rendererDidFinishWithStatistics:] : 784 -> 788
~ -[NUMediaView _rendererDidCreateAVPlayerController:] : 352 -> 348
~ -[NUMediaView _transitionToInsets:duration:animationCurve:updateRenderContent:] : 1364 -> 1372
~ _NUMediaTimingFunctionForUIAnimationCurve : 96 -> 100
~ -[NUMediaView _videoPlayerView] : 236 -> 256
~ -[NUMediaView _livePhotoView] : 244 -> 264
~ -[NUMediaView _setupViews] : 948 -> 992
~ ___26-[NUMediaView _setupViews]_block_invoke : 120 -> 112
~ -[NUMediaView _updateRenderContent] : 312 -> 336
~ -[NUMediaView viewForZoomingInScrollView:] : 16 -> 64
~ -[NUMediaView scrollViewDidEndDecelerating:] : 184 -> 188
~ -[NUMediaView scrollViewDidEndDragging:willDecelerate:] : 196 -> 200
~ -[NUMediaView scrollViewDidScroll:] : 184 -> 188
~ -[NUMediaView scrollViewWillBeginDragging:] : 140 -> 144
~ -[NUMediaView scrollViewDidEndZooming:withView:atScale:] : 184 -> 188
~ -[NUMediaView scrollViewWillBeginZooming:withView:] : 160 -> 164
~ -[NUMediaView scrollViewDidZoom:] : 156 -> 160
~ -[NUMediaView convertViewRect:fromSpace:] : 1280 -> 1312
~ _NUAssertLogger : 92 -> 108
~ -[NUMediaView convertPoint:fromSpace:toView:] : 1796 -> 1784
~ -[NUMediaView convertPoint:fromView:toSpace:] : 1796 -> 1788
~ -[NUMediaView _monitorDisplayEDRHeadroom:] : 484 -> 492
~ -[NUMediaView _scheduleDisplayEDRHeadroomMonitor] : 208 -> 216
~ -[NUMediaView didMoveToWindow] : 384 -> 416
~ -[NUMediaView _setLayerFilters:] : 144 -> 152
~ -[NUMediaView snapshotImage] : 88 -> 96
~ -[NUMediaView _layerRecursiveDescription] : 76 -> 84
~ -[NUMediaView _stopVideoPlayback] : 64 -> 68
~ -[NUMediaView _startVideoPlayback] : 64 -> 68
~ -[NUMediaView setMuted:] : 80 -> 84
~ -[NUMediaView isMuted] : 56 -> 60
~ -[NUMediaView loopsVideoPlayback] : 60 -> 64
~ -[NUMediaView setLoopsVideoPlayback:] : 80 -> 84
~ -[NUMediaView _livephotoPlaybackDidEnd] : 108 -> 112
~ -[NUMediaView _livephotoPlaybackWillBegin] : 108 -> 112
~ -[NUMediaView _rendererDidFinishPreparingVideo] : 108 -> 112
~ -[NUMediaView _rendererDidStartPreparingVideo] : 108 -> 112
~ -[NUMediaView _rendererDidUpdateLivePhoto] : 108 -> 112
~ -[NUMediaView _videoPlayerController] : 76 -> 84
~ -[NUMediaView _renderer] : 16 -> 64
~ -[NUMediaView _renderView] : 16 -> 64
~ -[NUMediaView _scrollView] : 16 -> 64
~ -[NUMediaView setZoomScaleToFit] : 112 -> 116
~ -[NUMediaView geometryUpdated] : 108 -> 112
~ -[NUMediaView setAngle:] : 148 -> 152
~ -[NUMediaView imageFrame] : 116 -> 120
~ -[NUMediaView player] : 16 -> 64
~ -[NUMediaView setMedia:] : 92 -> 96
~ -[NUMediaView setMedia:displayType:] : 136 -> 148
~ -[NUMediaView setComposition:] : 172 -> 184
~ -[NUMediaView setDelegate:] : 568 -> 572
~ +[NUMediaView _proposedInsetsForInsets:contentSize:inFrame:centerContent:] : 956 -> 968
~ -[NUMaskTransformerResult setGeometry:] : 12 -> 64
~ -[NUMaskTransformerResult setImage:] : 12 -> 64
~ -[NUMaskTransformerResult setError:] : 12 -> 64
~ +[NUMaskTransformer transformedImage:forComposition:imageSize:error:] : 1220 -> 1256
~ _NUAssertLogger.155 : 92 -> 108
~ ___57+[NUMaskTransformer imageForComposition:size:completion:]_block_invoke : 280 -> 292
~ +[NUMaskTransformer imageForComposition:size:] : 976 -> 996
~ ___46+[NUMaskTransformer imageForComposition:size:]_block_invoke : 260 -> 272
~ +[NUMaskTransformer maskedImageBackgroundImage:source:] : 256 -> 264
~ +[NUMaskTransformer applyRenderedOutputGeometryFromSpace:toInputImage:geometry:composition:error:] : 1860 -> 1952
~ +[NUMaskTransformer createImageIsolatedToMask:mediaView:] : 168 -> 176
~ +[NUMaskTransformer createImageIsolatedToMask:source:geometry:composition:] : 492 -> 500
~ -[NUTiledImageLayer debugDescription] : 488 -> 520
~ -[NUTiledImageLayer snapshotImage] : 388 -> 392
~ ___34-[NUTiledImageLayer snapshotImage]_block_invoke : 440 -> 456
~ -[NUTiledImageLayer _updateSublayers] : 696 -> 724
~ ___37-[NUTiledImageLayer _updateSublayers]_block_invoke : 468 -> 472
~ ___37-[NUTiledImageLayer _updateSublayers]_block_invoke_2 : 280 -> 252
~ ___37-[NUTiledImageLayer _updateSublayers]_block_invoke_3 : 392 -> 400
~ -[NUTileLayer dealloc] : 148 -> 152
~ -[NUTileLayer initWithImage:tile:] : 248 -> 244
~ ___34-[NUTiledImageLayer _recycleTiles]_block_invoke : 268 -> 276
~ -[NUTiledImageLayer setGeometry:] : 492 -> 496
~ -[NUTiledImageLayer setImage:] : 132 -> 140
~ -[NUTiledImageLayer dealloc] : 108 -> 112
~ -[NUTiledImageLayer init] : 248 -> 252
~ -[NUMediaViewRenderer setPixelFormat:] : 12 -> 64
~ -[NUMediaViewRenderer setColorSpace:] : 12 -> 64
~ -[NUMediaViewRenderer livePhotoViewDidEndScrubbing:] : 104 -> 108
~ -[NUMediaViewRenderer livePhotoViewDidBeginScrubbing:] : 104 -> 108
~ -[NUMediaViewRenderer livePhotoView:didEndPlaybackWithStyle:] : 100 -> 104
~ -[NUMediaViewRenderer livePhotoView:willBeginPlaybackWithStyle:] : 100 -> 104
~ -[NUMediaViewRenderer removeObserver:] : 604 -> 632
~ _NUAssertLogger.467 : 92 -> 108
~ -[NUMediaViewRenderer addPlaybackTimeObserver:] : 620 -> 648
~ -[NUMediaViewRenderer addExternalPlaybackObserver:] : 620 -> 648
~ -[NUMediaViewRenderer addPlaybackStateObserver:] : 620 -> 648
~ -[NUMediaViewRenderer setMuted:] : 212 -> 228
~ -[NUMediaViewRenderer setPlaybackMode:] : 128 -> 132
~ -[NUMediaViewRenderer setPlaybackRate:] : 152 -> 164
~ -[NUMediaViewRenderer playbackRate] : 96 -> 104
~ -[NUMediaViewRenderer play] : 324 -> 328
~ -[NUMediaViewRenderer stepByCount:] : 84 -> 88
~ -[NUMediaViewRenderer currentSeekTime] : 96 -> 100
~ -[NUMediaViewRenderer seekToTime:toleranceBefore:toleranceAfter:forceSeek:] : 160 -> 164
~ -[NUMediaViewRenderer loadedTimeRanges] : 120 -> 136
~ -[NUMediaViewRenderer currentTime] : 112 -> 116
~ -[NUMediaViewRenderer playbackState] : 148 -> 160
~ -[NUMediaViewRenderer mediaDuration] : 132 -> 140
~ -[NUMediaViewRenderer cancelPendingRenders] : 152 -> 168
~ -[NUMediaViewRenderer _addFullExtentConstraintsForView:] : 324 -> 344
~ -[NUMediaViewRenderer _videoRenderRequestForMedia:] : 176 -> 204
~ -[NUMediaViewRenderer _roiRenderRequestForMedia:] : 332 -> 360
~ -[NUMediaViewRenderer _roiRenderRequestForComposition:] : 332 -> 360
~ -[NUMediaViewRenderer _backfillRenderRequestForMedia:] : 316 -> 340
~ -[NUMediaViewRenderer _backfillRenderRequestForComposition:] : 316 -> 340
~ -[NUMediaViewRenderer _zoomTargetRect] : 552 -> 556
~ -[NUMediaViewRenderer _targetZoomScale] : 112 -> 116
~ -[NUMediaViewRenderer _updateLivePhotoWithResponse:] : 612 -> 668
~ -[NUMediaViewRenderer _livePhotoFromResponse:] : 220 -> 232
~ -[NUMediaViewRenderer _coalesceUpdateLivePhotoComposition:] : 232 -> 228
~ -[NUMediaViewRenderer _coalesceUpdateVideoComposition:] : 232 -> 228
~ -[NUMediaViewRenderer _updateVideoViewLayoutWithGeometry:] : 428 -> 440
~ -[NUMediaViewRenderer _updateVideoComposition:] : 428 -> 464
~ -[NUMediaViewRenderer _isVideoSourceChangedInComposition:] : 140 -> 148
~ -[NUMediaViewRenderer _scalePolicyForVideoCompositionRender] : 648 -> 644
~ -[NUMediaViewRenderer _updateVideoWithResult:sourceChanged:] : 1600 -> 1676
~ -[NUMediaViewRenderer cacheVideoRenderFilter] : 84 -> 100
~ -[NUMediaViewRenderer _playerStatusDidChange:] : 144 -> 152
~ -[NUMediaViewRenderer _setDisplayType:] : 616 -> 656
~ -[NUMediaViewRenderer _updateDisplayForMediaType:] : 564 -> 580
~ -[NUMediaViewRenderer _updateImageLayer:withRenderResponse:] : 952 -> 984
~ -[NUMediaViewRenderer _updateBackfillLayerWithRenderResponse:] : 232 -> 252
~ -[NUMediaViewRenderer _updateROILayerWithRenderResponse:] : 164 -> 176
~ ___67-[NUMediaViewRenderer _updateBackfillLayerWithLatestRenderResponse]_block_invoke : 80 -> 96
~ ___62-[NUMediaViewRenderer _updateROILayerWithLatestRenderResponse]_block_invoke : 80 -> 96
~ -[NUMediaViewRenderer _updateVideoPlayerWithRenderResponse:] : 528 -> 544
~ ___65-[NUMediaViewRenderer _updateVideoPlayerWithLatestRenderResponse]_block_invoke : 80 -> 96
~ ___67-[NUMediaViewRenderer _updateLivePhotoViewWithLatestRenderResponse]_block_invoke : 80 -> 96
~ ___50-[NUMediaViewRenderer _videoRenderResponseHandler]_block_invoke : 160 -> 184
~ ___54-[NUMediaViewRenderer _livePhotoRenderResponseHandler]_block_invoke : 160 -> 184
~ ___60-[NUMediaViewRenderer _videoFrameImageRenderResponseHandler]_block_invoke : 160 -> 184
~ ___53-[NUMediaViewRenderer _backfillRenderResponseHandler]_block_invoke : 160 -> 184
~ ___48-[NUMediaViewRenderer _roiRenderResponseHandler]_block_invoke : 160 -> 184
~ -[NUMediaViewRenderer _updateImageRenderForComposition:] : 200 -> 196
~ ___56-[NUMediaViewRenderer _updateImageRenderForComposition:]_block_invoke : 332 -> 356
~ -[NUMediaViewRenderer _renderFinishedWithGeometry:layer:] : 1608 -> 1648
~ -[NUMediaViewRenderer _regionPolicyForZoomTargetRect:] : 416 -> 432
~ -[NUMediaViewRenderer _scrollBounds] : 116 -> 120
~ -[NUMediaViewRenderer targetSize] : 288 -> 296
~ -[NUMediaViewRenderer convertRect:fromImageToView:] : 216 -> 228
~ -[NUMediaViewRenderer convertRect:toImageFromView:] : 216 -> 228
~ -[NUMediaViewRenderer convertPoint:fromImageToView:] : 176 -> 188
~ -[NUMediaViewRenderer convertPoint:toImageFromView:] : 176 -> 188
~ -[NUMediaViewRenderer isReady] : 92 -> 104
~ -[NUMediaViewRenderer isZoomedToFit] : 100 -> 104
~ -[NUMediaViewRenderer beginZooming] : 108 -> 112
~ -[NUMediaViewRenderer updateMedia:displayType:] : 492 -> 540
~ -[NUMediaViewRenderer updateComposition:] : 840 -> 860
~ -[NUMediaViewRenderer _setupRenderRequest:] : 348 -> 372
~ -[NUMediaViewRenderer init] : 768 -> 784
~ -[NUMediaViewRenderer initWithMediaView:] : 376 -> 384
~ +[NUMediaViewRenderer _forceUpdateForNewVideoComposition:previousComposition:newAsset:previousAsset:isPlaying:] : 248 -> 236
~ -[NUMediaViewRenderer(Private) sweep:withBlock:] : 252 -> 268
~ -[NUMediaViewRenderer(Private) _releaseAVObjects] : 1040 -> 1060
~ +[UIView(NeutrinoAdditions) _recurseView:filter:] : 320 -> 328
~ -[NURenderView animationDidStop:finished:] : 508 -> 512
~ -[NURenderView animationDidStart:] : 136 -> 140
~ -[NURenderView transitionToSize:offset:duration:animationCurve:completion:] : 864 -> 868
~ -[NURenderView transitionToSize:duration:animationCurve:completion:] : 176 -> 168
~ -[NURenderView willMoveToWindow:] : 256 -> 264
~ -[NURenderView convertRectToImage:] : 144 -> 148
~ -[NURenderView renderFrameReachedTargetSize] : 784 -> 788
~ -[NURenderView hasTransitionAnimation] : 72 -> 76
~ -[NURenderView setGeometry:] : 352 -> 364
~ -[NURenderView geometry] : 16 -> 64
~ -[NURenderView layoutSubviews] : 188 -> 192
~ -[NURenderView _containerLayer] : 16 -> 64
~ -[NURenderView _roiLayer] : 16 -> 64
~ -[NURenderView _backfillLayer] : 16 -> 64
~ __NUViewCommonInit : 520 -> 548
~ -[NUDebugRenderView _setupDeviceMotion] : 388 -> 392
~ -[NUDebugRenderView _resetOrientation:] : 200 -> 208
~ -[NUDebugRenderView _orientWithX:andY:] : 596 -> 604
~ -[NUDebugRenderView setDebugMode:] : 244 -> 252
~ -[NUViewport initWithSize:backingScaleFactor:] : 1560 -> 1632
~ _NUAssertLogger.821 : 92 -> 108
~ -[NUViewport init] : 768 -> 784
~ -[NUViewportRegionPolicy regionForGeometry:] : 400 -> 404
~ -[NUViewportRegionPolicy initWithViewport:] : 628 -> 652
~ _NUAssertLogger.873 : 92 -> 108
~ -[NUViewportRegionPolicy init] : 768 -> 784
CStrings:
+ "/Library/Caches/com.apple.xbs/E829230E-D49E-44C5-8D18-3164B5B57967/TemporaryDirectory.vaxqgC/Sources/Photos/workspaces/neutrino/Kit/Common/NUMaskTransformer.m"
+ "/Library/Caches/com.apple.xbs/E829230E-D49E-44C5-8D18-3164B5B57967/TemporaryDirectory.vaxqgC/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaView.m"
+ "/Library/Caches/com.apple.xbs/E829230E-D49E-44C5-8D18-3164B5B57967/TemporaryDirectory.vaxqgC/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaViewRenderer.m"
+ "/Library/Caches/com.apple.xbs/E829230E-D49E-44C5-8D18-3164B5B57967/TemporaryDirectory.vaxqgC/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewport.m"
+ "/Library/Caches/com.apple.xbs/E829230E-D49E-44C5-8D18-3164B5B57967/TemporaryDirectory.vaxqgC/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewportRegionPolicy.m"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMaskTransformer.m"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaView.m"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaViewRenderer.m"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewport.m"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewportRegionPolicy.m"

```
