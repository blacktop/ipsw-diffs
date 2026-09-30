## NeutrinoKit

> `/System/Library/PrivateFrameworks/NeutrinoKit.framework/Versions/A/NeutrinoKit`

```diff

-741.0.130.0.0
-  __TEXT.__text: 0x17428
+751.0.104.0.0
+  __TEXT.__text: 0x17388
   __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x1714
+  __TEXT.__objc_methlist: 0x19ec
   __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__gcc_except_tab: 0x220
   __TEXT.__cstring: 0x1188
   __TEXT.__oslogstring: 0x4a5
   __TEXT.__unwind_info: 0x6c0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1520
+  __DATA_CONST.__objc_selrefs: 0x15c0
   __DATA_CONST.__objc_superrefs: 0x70
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x6b0
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0x2d50
+  __AUTH_CONST.__objc_const: 0x2808
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x270

   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/Versions/A/PhotoFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D50DD0B-1C82-3B6C-BE41-99B74B8BA9C7
-  Functions: 576
+  UUID: C714DEAA-464E-3778-BB34-983DDE3B1D03
+  Functions: 575
   Symbols:   1714
   CStrings:  1362
 
Functions:
~ -[CALayer(NeutrinoUIDebugging) _nu_recursiveDescriptionWithLevel:result:] : 992 -> 988
~ -[NUAVPlayerController _addPlayerKVO] : 268 -> 276
~ -[NUAVPlayerController _removePlayerKVO] : 248 -> 256
~ -[NUAVPlayerController _removeTimeObserver] : 108 -> 100
~ -[NUAVPlayerController _addTimeObserver] : 508 -> 492
~ ___40-[NUAVPlayerController _addTimeObserver]_block_invoke : 316 -> 320
~ -[NUAVPlayerController seekForward] : 388 -> 392
~ -[NUAVPlayerController observeValueForKeyPath:ofObject:change:context:] : 2028 -> 2032
~ -[NUAVPlayerController prepareWithAVAsset:videoComposition:audioMix:loopsVideo:seekToTime:] : 1188 -> 1184
~ -[NUAVPlayerView _setReadyForDisplay:] : 112 -> 104
~ -[NUAVPlayerView _updateReadyForDisplayWithID:] : 120 -> 112
~ -[NUAVPlayerView observeValueForKeyPath:ofObject:change:context:] : 360 -> 356
~ -[NUAVPlayerView dispose] : 128 -> 120
~ -[NSView(NeutrinoUIDebugging) _nu_recursiveDescriptionWithLevel:result:] : 492 -> 488
~ -[NUClipView constrainBoundsRect:] : 572 -> 568
~ -[NUDebugRenderView mouseUp:] : 184 -> 188
~ +[NUMaskTransformer imageForComposition:size:completion:] : 764 -> 760
~ +[NUMaskTransformer imageForComposition:size:] : 1040 -> 1036
~ ___37-[NUTiledImageLayer _updateSublayers]_block_invoke_2 : 244 -> 280
~ -[NUMediaViewRenderer setMuted:] : 248 -> 232
~ -[NUMediaViewRenderer setPlaybackMode:] : 148 -> 136
~ -[NUMediaViewRenderer play] : 336 -> 332
~ -[NUMediaViewRenderer _coalesceUpdateLivePhotoComposition:] : 248 -> 244
~ -[NUMediaViewRenderer _coalesceUpdateVideoComposition:] : 248 -> 244
~ -[NUMediaViewRenderer _updateVideoViewLayoutWithGeometry:] : 468 -> 464
~ -[NUMediaViewRenderer _updateVideoWithResult:sourceChanged:] : 1744 -> 1748
~ -[NUMediaViewRenderer _setupAVPlayerController] : 660 -> 644
~ -[NUMediaViewRenderer _setDisplayType:] : 840 -> 836
~ -[NUMediaViewRenderer _coalesceBackfillRenderForComposition:] : 248 -> 244
~ -[NUMediaViewRenderer targetSize] : 372 -> 360
~ -[NUMediaViewRenderer canRenderVideoLive] : 52 -> 56
~ -[NUMediaViewRenderer pipelineFilersHaveChanged] : 56 -> 60
~ -[NUMediaViewRenderer updateComposition:] : 912 -> 900
- sub_2407ef2f4
~ +[NSView(NeutrinoAdditions) _recurseView:filter:] : 344 -> 340
~ -[_NUClipView proposedBoundsForBounds:inFrame:] : 864 -> 848
~ -[NUViewGeometry insetBoundsForCrop:inBounds:inFrame:] : 340 -> 332
~ -[NUViewGeometry proposedBoundsForBounds:inFrame:] : 972 -> 932
~ _NUEdgeInsetsInsetRect : 92 -> 84
~ -[NUMediaView playerControllerIsReadyForPlayback:] : 296 -> 300
~ -[NUMediaView playerControllerFailedToPlayToEnd:error:] : 336 -> 340
~ -[NUMediaView playerControllerDidFinishPlaying:duration:] : 320 -> 324
~ -[NUMediaView _livephotoPlaybackDidEnd] : 108 -> 104
~ -[NUMediaView _livephotoPlaybackWillBegin] : 108 -> 104
~ -[NUMediaView _rendererDidFinishPreparingVideo] : 108 -> 104
~ -[NUMediaView _rendererDidStartPreparingVideo] : 108 -> 104
~ -[NUMediaView _rendererDidUpdateLivePhoto] : 108 -> 104
~ -[NUMediaView _rendererDidFinishWithStatistics:] : 224 -> 232
~ -[NUMediaView _setupViews] : 420 -> 424
~ -[NUMediaView didZoom:] : 128 -> 132
~ -[NUMediaView didEndScrolling:] : 148 -> 152
~ -[NUMediaView didEndZooming:] : 164 -> 172
~ -[NUMediaView willBeginZooming:] : 128 -> 132
~ -[NUMediaView setDelegate:] : 444 -> 440
CStrings:
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMaskTransformer.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaViewRenderer.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewport.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewportRegionPolicy.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/macOS/NUMediaView.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMaskTransformer.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaViewRenderer.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewport.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUViewportRegionPolicy.m"
- "/AppleInternal/Library/BuildRoots/daece38d-cdcb-11ef-875a-d285688f7a47/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/macOS/NUMediaView.m"

```
