## NeutrinoKit

> `/System/Library/PrivateFrameworks/NeutrinoKit.framework/NeutrinoKit`

```diff

-760.6.150.0.0
-  __TEXT.__text: 0x173c4
+800.14.111.0.0
+  __TEXT.__text: 0x1829c
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x191c
+  __TEXT.__objc_methlist: 0x1a04
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__cstring: 0x103a
-  __TEXT.__oslogstring: 0xa87
-  __TEXT.__unwind_info: 0x6d0
-  __TEXT.__objc_classname: 0x260
-  __TEXT.__objc_methname: 0x4d0d
-  __TEXT.__objc_methtype: 0x11f2
-  __TEXT.__objc_stubs: 0x4780
+  __TEXT.__gcc_except_tab: 0x244
+  __TEXT.__cstring: 0x1011
+  __TEXT.__oslogstring: 0xa99
+  __TEXT.__unwind_info: 0x6e8
+  __TEXT.__objc_classname: 0x27a
+  __TEXT.__objc_methname: 0x4f65
+  __TEXT.__objc_methtype: 0x126d
+  __TEXT.__objc_stubs: 0x4980
   __DATA_CONST.__got: 0x360
-  __DATA_CONST.__const: 0x5d8
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__const: 0x560
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15f8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0x1698
+  __DATA_CONST.__objc_superrefs: 0x68
   __AUTH_CONST.__auth_got: 0x4c0
   __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0xb00
-  __AUTH_CONST.__objc_const: 0x2878
+  __AUTH_CONST.__cfstring: 0xac0
+  __AUTH_CONST.__objc_const: 0x2a00
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x210
-  __DATA.__data: 0x330
+  __DATA.__objc_ivar: 0x22c
+  __DATA.__data: 0x338
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x5f0
+  __DATA_DIRTY.__objc_data: 0x640
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 925BE5E0-399A-3766-BE81-E7633B247F00
-  Functions: 540
-  Symbols:   2274
-  CStrings:  1397
+  UUID: A093FB85-4016-3DD5-8345-BE30479ED3B9
+  Functions: 559
+  Symbols:   2339
+  CStrings:  1431
 
Symbols:
+ -[NUMediaView addOverlay:withIdentifier:style:]
+ -[NUMediaView hasOverlayWithIdentifier:]
+ -[NUMediaView media]
+ -[NUMediaView playerRateDidChange:rate:]
+ -[NUMediaView removeOverlayWithIdentifier:]
+ -[NUMediaView setMedia:]
+ -[NUMediaView setMedia:displayType:]
+ -[NUMediaViewRenderer _backfillRenderRequestForMedia:]
+ -[NUMediaViewRenderer _isVideoSourceChangedInComposition:]
+ -[NUMediaViewRenderer _livePhotoRenderResponseHandler]
+ -[NUMediaViewRenderer _roiRenderRequestForComposition:]
+ -[NUMediaViewRenderer _roiRenderRequestForMedia:]
+ -[NUMediaViewRenderer _roiRenderResponseHandler]
+ -[NUMediaViewRenderer _setupRenderRequest:]
+ -[NUMediaViewRenderer _updateLivePhotoViewWithLatestRenderResponse]
+ -[NUMediaViewRenderer _updateLivePhotoViewWithRenderResponse:]
+ -[NUMediaViewRenderer _updateVideoPlayerWithLatestRenderResponse]
+ -[NUMediaViewRenderer _updateVideoPlayerWithRenderResponse:]
+ -[NUMediaViewRenderer _videoRenderRequestForMedia:]
+ -[NUMediaViewRenderer _videoRenderResponseHandler]
+ -[NUMediaViewRenderer updateMedia:]
+ -[NUMediaViewRenderer updateMedia:displayType:]
+ -[NUMediaViewRenderer(Private) sweep:withBlock:]
+ -[_NUTiledBackfillLayer setBounds:]
+ -[_NUTiledBackfillLayer setFrame:]
+ GCC_except_table246
+ GCC_except_table250
+ GCC_except_table348
+ GCC_except_table378
+ GCC_except_table380
+ GCC_except_table392
+ GCC_except_table403
+ GCC_except_table407
+ GCC_except_table410
+ GCC_except_table490
+ _CAToneMapModeIfSupported
+ _NUAssertLogger.444
+ _NUAssertLogger.799
+ _NUAssertLogger.852
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NUVideoRenderRequest
+ _OBJC_CLASS_$__NUMediaViewOverlayView
+ _OBJC_IVAR_$_NUMediaView._media
+ _OBJC_IVAR_$_NUMediaView._overlayViews
+ _OBJC_IVAR_$_NUMediaViewRenderer._backfillRenderRequest
+ _OBJC_IVAR_$_NUMediaViewRenderer._livePhotoRenderRequest
+ _OBJC_IVAR_$_NUMediaViewRenderer._livePhotoRenderResponse
+ _OBJC_IVAR_$_NUMediaViewRenderer._log
+ _OBJC_IVAR_$_NUMediaViewRenderer._mediaType
+ _OBJC_IVAR_$_NUMediaViewRenderer._roiRenderRequest
+ _OBJC_IVAR_$_NUMediaViewRenderer._videoRenderRequest
+ _OBJC_IVAR_$_NUMediaViewRenderer._videoRenderResponse
+ _OBJC_IVAR_$_NUTiledImageLayer._log
+ _OBJC_METACLASS_$__NUMediaViewOverlayView
+ _PlayerObservationContext
+ __OBJC_$_INSTANCE_METHODS__NUTiledBackfillLayer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NUAVPlayerViewDelegate
+ __OBJC_CLASS_RO_$__NUMediaViewOverlayView
+ __OBJC_METACLASS_RO_$__NUMediaViewOverlayView
+ ___48-[NUMediaViewRenderer _roiRenderResponseHandler]_block_invoke
+ ___48-[NUMediaViewRenderer _roiRenderResponseHandler]_block_invoke_2
+ ___50-[NUMediaViewRenderer _videoRenderResponseHandler]_block_invoke
+ ___50-[NUMediaViewRenderer _videoRenderResponseHandler]_block_invoke_2
+ ___54-[NUMediaViewRenderer _livePhotoRenderResponseHandler]_block_invoke
+ ___54-[NUMediaViewRenderer _livePhotoRenderResponseHandler]_block_invoke_2
+ ___65-[NUMediaViewRenderer _updateVideoPlayerWithLatestRenderResponse]_block_invoke
+ ___67-[NUMediaViewRenderer _updateLivePhotoViewWithLatestRenderResponse]_block_invoke
+ ___Block_byref_object_copy_.262
+ ___Block_byref_object_copy_.506
+ ___Block_byref_object_dispose_.263
+ ___Block_byref_object_dispose_.507
+ ___NUAssertLogger_block_invoke.170
+ ___NUAssertLogger_block_invoke.452
+ ___NUAssertLogger_block_invoke.819
+ ___NUAssertLogger_block_invoke.870
+ ___NUUILogger_block_invoke.466
+ ___NUUILogger_block_invoke.632
+ ___NUUILogger_block_invoke.71
+ ___block_descriptor_89_e8_32s40s48s_e29_v24?0"<NUSurfaceTile>"8^B16ls32l8s40l8s48l8
+ ___block_literal_global.159
+ ___block_literal_global.434
+ ___block_literal_global.436
+ ___block_literal_global.46
+ ___block_literal_global.462
+ ___block_literal_global.464
+ ___block_literal_global.485
+ ___block_literal_global.627
+ ___block_literal_global.73
+ ___block_literal_global.816
+ ___block_literal_global.867
+ _objc_msgSend$_backfillRenderRequestForMedia:
+ _objc_msgSend$_isVideoSourceChangedInComposition:
+ _objc_msgSend$_livePhotoRenderResponseHandler
+ _objc_msgSend$_roiRenderRequestForComposition:
+ _objc_msgSend$_roiRenderRequestForMedia:
+ _objc_msgSend$_roiRenderResponseHandler
+ _objc_msgSend$_setupRenderRequest:
+ _objc_msgSend$_updateLivePhotoViewWithLatestRenderResponse
+ _objc_msgSend$_updateLivePhotoViewWithRenderResponse:
+ _objc_msgSend$_updateVideoPlayerWithLatestRenderResponse
+ _objc_msgSend$_updateVideoPlayerWithRenderResponse:
+ _objc_msgSend$_videoRenderRequestForMedia:
+ _objc_msgSend$_videoRenderResponseHandler
+ _objc_msgSend$cancelAllRequests
+ _objc_msgSend$constraintEqualToAnchor:
+ _objc_msgSend$initWithMedia:
+ _objc_msgSend$media
+ _objc_msgSend$mediaViewDidEndPlayback:
+ _objc_msgSend$mediaViewDidStartPlayback:
+ _objc_msgSend$playerRateDidChange:rate:
+ _objc_msgSend$renderContext
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setActive:
+ _objc_msgSend$setMedia:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setResponseQueue:
+ _objc_msgSend$setToneMapMode:
+ _objc_msgSend$updateMedia:
+ _objc_msgSend$updateMedia:displayType:
+ _os_log_create
- -[NUMediaView _withComposition:visitRenderClient:]
- -[NUMediaViewRenderer _coalesceBackfillRenderForComposition:]
- -[NUMediaViewRenderer _updateCoalescedBackfillRenderWithComposition:]
- -[NUMediaViewRenderer _zoomRenderRequestForComposition:]
- -[NUMediaViewRenderer _zoomRenderResponseHandler]
- -[NUMediaViewRenderer newRenderRequestForComposition:scalePolicy:regionPolicy:]
- -[NUMediaViewRenderer renderClient]
- -[NUMediaViewRenderer(Private) _withComposition:visitRenderClient:]
- GCC_except_table240
- GCC_except_table244
- GCC_except_table342
- GCC_except_table369
- GCC_except_table371
- GCC_except_table384
- GCC_except_table389
- GCC_except_table397
- GCC_except_table401
- GCC_except_table471
- _NUAssertLogger.418
- _NUAssertLogger.749
- _NUAssertLogger.802
- _OBJC_CLASS_$_NULivePhotoRenderClient
- _OBJC_CLASS_$_NUSurfaceRenderClient
- _OBJC_CLASS_$_NUVideoRenderClient
- _OBJC_IVAR_$_NUMediaViewRenderer._backfillClient
- _OBJC_IVAR_$_NUMediaViewRenderer._livePhotoClient
- _OBJC_IVAR_$_NUMediaViewRenderer._videoClient
- _OBJC_IVAR_$_NUMediaViewRenderer._zoomClient
- ___39-[NUMediaViewRenderer _setDisplayType:]_block_invoke
- ___47-[NUMediaViewRenderer _updateVideoComposition:]_block_invoke
- ___47-[NUMediaViewRenderer _updateVideoComposition:]_block_invoke.80
- ___49-[NUMediaViewRenderer _zoomRenderResponseHandler]_block_invoke
- ___49-[NUMediaViewRenderer _zoomRenderResponseHandler]_block_invoke_2
- ___61-[NUMediaViewRenderer _coalesceBackfillRenderForComposition:]_block_invoke
- ___Block_byref_object_copy_.273
- ___Block_byref_object_copy_.477
- ___Block_byref_object_dispose_.274
- ___Block_byref_object_dispose_.478
- ___NUAssertLogger_block_invoke.177
- ___NUAssertLogger_block_invoke.428
- ___NUAssertLogger_block_invoke.769
- ___NUAssertLogger_block_invoke.820
- ___NUUILogger_block_invoke.437
- ___NUUILogger_block_invoke.594
- ___NUUILogger_block_invoke.81
- ___block_descriptor_40_e8_32w_e20_v16?0"NUResponse"8lw32l8
- ___block_descriptor_58_e8_32s40s48s_e20_v16?0"NUResponse"8ls32l8s40l8s48l8
- ___block_descriptor_70_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_97_e8_32s40s48s56s_e29_v24?0"<NUSurfaceTile>"8^B16ls32l8s40l8s48l8s56l8
- ___block_literal_global.162
- ___block_literal_global.411
- ___block_literal_global.413
- ___block_literal_global.451
- ___block_literal_global.459
- ___block_literal_global.461
- ___block_literal_global.589
- ___block_literal_global.59
- ___block_literal_global.766
- ___block_literal_global.817
- ___block_literal_global.84
- _objc_msgSend$CGColorSpace
- _objc_msgSend$_coalesceBackfillRenderForComposition:
- _objc_msgSend$_updateCoalescedBackfillRenderWithComposition:
- _objc_msgSend$_withComposition:visitRenderClient:
- _objc_msgSend$_zoomRenderRequestForComposition:
- _objc_msgSend$_zoomRenderResponseHandler
- _objc_msgSend$cancel
- _objc_msgSend$initWithName:
- _objc_msgSend$initWithName:responseQueue:
- _objc_msgSend$newRenderRequestForComposition:scalePolicy:regionPolicy:
- _objc_msgSend$setIsOneShot:
- _objc_msgSend$submitGenericRequest:completion:
- _objc_msgSend$submitRequest:
- _objc_msgSend$submitRequestForComposition:completion:
- _objc_retain_x10
CStrings:
+ "%s transform = %@"
+ "-[NUTiledImageLayer setGeometry:]"
+ "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/Common/NUMediaView.m"
+ "@\"<NUMedia>\""
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_os_log>\""
+ "@\"NULivePhotoRenderRequest\""
+ "@\"NUSurfaceRenderRequest\""
+ "@\"NUVideoRenderRequest\""
+ "NUMediaViewRenderer-livePhoto"
+ "T@\"<NUMedia>\",&,N,V_media"
+ "_NUMediaViewOverlayView"
+ "_backfillRenderRequest"
+ "_backfillRenderRequestForMedia:"
+ "_isVideoSourceChangedInComposition:"
+ "_livePhotoRenderRequest"
+ "_livePhotoRenderResponse"
+ "_livePhotoRenderResponseHandler"
+ "_log"
+ "_media"
+ "_mediaType"
+ "_overlayViews"
+ "_roiRenderRequest"
+ "_roiRenderRequestForComposition:"
+ "_roiRenderRequestForMedia:"
+ "_roiRenderResponseHandler"
+ "_setupRenderRequest:"
+ "_updateLivePhotoViewWithLatestRenderResponse"
+ "_updateLivePhotoViewWithRenderResponse:"
+ "_updateVideoPlayerWithLatestRenderResponse"
+ "_updateVideoPlayerWithRenderResponse:"
+ "_videoRenderRequest"
+ "_videoRenderRequestForMedia:"
+ "_videoRenderResponse"
+ "_videoRenderResponseHandler"
+ "addOverlay:withIdentifier:style:"
+ "cancelAllRequests"
+ "constraintEqualToAnchor:"
+ "hasOverlayWithIdentifier:"
+ "initWithMedia:"
+ "media"
+ "mediaViewDidEndPlayback:"
+ "mediaViewDidStartPlayback:"
+ "mvr"
+ "playerRateDidChange:rate:"
+ "removeOverlayWithIdentifier:"
+ "renderContext"
+ "renderView"
+ "setAccessibilityIdentifier:"
+ "setActive:"
+ "setMedia:"
+ "setMedia:displayType:"
+ "setObject:forKey:"
+ "setObject:forKeyedSubscript:"
+ "setResponseQueue:"
+ "setToneMapMode:"
+ "sweep:withBlock:"
+ "updateMedia:"
+ "updateMedia:displayType:"
+ "v28@0:8@\"NUAVPlayerView\"16f24"
+ "v28@0:8@16f24"
+ "v40@0:8@16@24q32"
+ "\xf0\xb1"
+ "\xf0\xf0A"
- "/Library/Caches/com.apple.xbs/Sources/Photos/workspaces/neutrino/Kit/iOS/NUMediaView.m"
- "@\"NULivePhotoRenderClient\""
- "@\"NUSurfaceRenderClient\""
- "@\"NUVideoRenderClient\""
- "CGColorSpace"
- "NUMediaViewRenderer-LivePhotoClient"
- "NUMediaViewRenderer-NUVideoRenderRequest"
- "NUMediaViewRenderer-zoomedToFit"
- "_backfillClient"
- "_coalesceBackfillRenderForComposition:"
- "_livePhotoClient"
- "_updateCoalescedBackfillRenderWithComposition:"
- "_videoClient"
- "_withComposition:visitRenderClient:"
- "_zoomClient"
- "_zoomRenderRequestForComposition:"
- "_zoomRenderResponseHandler"
- "cancel"
- "initWithName:"
- "initWithName:responseQueue:"
- "newRenderRequestForComposition:scalePolicy:regionPolicy:"
- "renderClient"
- "setIsOneShot:"
- "submitGenericRequest:completion:"
- "submitRequest:"
- "submitRequestForComposition:completion:"
- "\xf0\xa1"
- "\xf0\xe1"

```
