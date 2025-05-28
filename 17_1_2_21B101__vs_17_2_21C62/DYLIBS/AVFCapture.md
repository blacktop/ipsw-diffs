## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-465.15.2.0.0
-  __TEXT.__text: 0xd7be4
-  __TEXT.__auth_stubs: 0x1810
-  __TEXT.__objc_methlist: 0xb628
+470.16.1.0.0
+  __TEXT.__text: 0xd8f08
+  __TEXT.__auth_stubs: 0x1820
+  __TEXT.__objc_methlist: 0xb6f0
   __TEXT.__const: 0x868
-  __TEXT.__gcc_except_tab: 0x1c54
-  __TEXT.__cstring: 0x16e6c
+  __TEXT.__gcc_except_tab: 0x1c98
+  __TEXT.__cstring: 0x16f34
   __TEXT.__oslogstring: 0x3e0e
   __TEXT.__dlopen_cstrs: 0x178
-  __TEXT.__unwind_info: 0x37d4
+  __TEXT.__unwind_info: 0x3834
   __TEXT.__objc_classname: 0x1548
-  __TEXT.__objc_methname: 0x204ce
-  __TEXT.__objc_methtype: 0x351d
-  __TEXT.__objc_stubs: 0x130e0
-  __DATA_CONST.__got: 0x1e48
-  __DATA_CONST.__const: 0x62a0
+  __TEXT.__objc_methname: 0x207e8
+  __TEXT.__objc_methtype: 0x3529
+  __TEXT.__objc_stubs: 0x132a0
+  __DATA_CONST.__got: 0x1e50
+  __DATA_CONST.__const: 0x62a8
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf448
-  __DATA_CONST.__objc_selrefs: 0x5e60
+  __DATA_CONST.__objc_const: 0xf4e8
+  __DATA_CONST.__objc_selrefs: 0x5ed8
   __DATA_CONST.__objc_arraydata: 0x348
   __AUTH_CONST.__objc_const: 0x3f40
-  __AUTH_CONST.__cfstring: 0xf1c0
-  __AUTH_CONST.__objc_intobj: 0x7c8
+  __AUTH_CONST.__cfstring: 0xf200
+  __AUTH_CONST.__objc_intobj: 0x7b0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __AUTH_CONST.__auth_got: 0xc18
+  __AUTH_CONST.__auth_got: 0xc20
   __AUTH.__objc_data: 0x230
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x780
   __DATA.__objc_superrefs: 0x418
-  __DATA.__objc_ivar: 0x137c
+  __DATA.__objc_ivar: 0x1390
   __DATA.__data: 0xca0
   __DATA.__common: 0x60
   __DATA.__bss: 0x2d8
   __DATA_DIRTY.__objc_data: 0x2e40
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__common: 0x120
+  __DATA_DIRTY.__common: 0x140
   __DATA_DIRTY.__bss: 0x370
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4613
-  Symbols:   16796
-  CStrings:  7448
+  Functions: 4634
+  Symbols:   16863
+  CStrings:  7473
 
Symbols:
+ -[AVCaptureDevice _setContinuousZoomWithDepthDisallowed:]
+ -[AVCaptureDeviceFormat isStereoVideoCaptureSupported]
+ -[AVCaptureFigVideoDevice _initializeContinuousZoomWithDepthActiveWithEnabled:]
+ -[AVCaptureFigVideoDevice _setContinuousZoomWithDepthActiveWithEnabled:disallowed:isActiveDepthDataFormatChangingOut:]
+ -[AVCaptureFigVideoDevice _setContinuousZoomWithDepthDisallowed:]
+ -[AVCaptureFigVideoDevice _setStereoVideoCaptureStatus:]
+ -[AVCaptureFigVideoDevice _updateActiveDepthDataFormatForContinuousZoomWithDepth]
+ -[AVCaptureFigVideoDevice _updateContinuousZoomWithDepthActiveWithEnabled:disallowed:isActiveDepthDataFormatChangingOut:]
+ -[AVCaptureFigVideoDevice stereoVideoCaptureStatus]
+ -[AVCaptureMovieFileOutput _totalNANDBandwidthAllowed:videoCodecType:]
+ -[AVCaptureMovieFileOutput isStereoVideoCaptureEnabled]
+ -[AVCaptureMovieFileOutput isStereoVideoCaptureSupported]
+ -[AVCaptureMovieFileOutput setStereoVideoCaptureEnabled:]
+ -[AVCaptureMovieFileOutput stereoVideoCaptureStatus]
+ -[AVCaptureSession _getMovieFileOutputNANDDataRate:]
+ -[AVCaptureSession _informSessionMembersOfChangedActiveFormat:forDevice:mediaType:]
+ -[AVCaptureSession _nandCostWithDataRate:]
+ -[AVCaptureSession movieFileOutputStoppedRecording:]
+ -[AVCaptureSession requestNANDBandwidthToStartMovieFileRecording:outputFileURL:videoCodecType:]
+ GCC_except_table104
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table132
+ GCC_except_table134
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table183
+ GCC_except_table197
+ GCC_except_table206
+ GCC_except_table218
+ GCC_except_table221
+ GCC_except_table240
+ GCC_except_table246
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table254
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table285
+ GCC_except_table296
+ GCC_except_table298
+ GCC_except_table300
+ GCC_except_table306
+ GCC_except_table320
+ GCC_except_table343
+ GCC_except_table353
+ GCC_except_table365
+ GCC_except_table380
+ GCC_except_table383
+ GCC_except_table410
+ GCC_except_table414
+ GCC_except_table423
+ GCC_except_table425
+ GCC_except_table438
+ GCC_except_table444
+ GCC_except_table449
+ GCC_except_table460
+ GCC_except_table470
+ GCC_except_table479
+ GCC_except_table500
+ GCC_except_table511
+ GCC_except_table521
+ GCC_except_table539
+ GCC_except_table558
+ GCC_except_table571
+ GCC_except_table574
+ GCC_except_table595
+ GCC_except_table597
+ GCC_except_table599
+ GCC_except_table622
+ GCC_except_table634
+ GCC_except_table636
+ GCC_except_table638
+ GCC_except_table644
+ GCC_except_table646
+ GCC_except_table687
+ GCC_except_table69
+ GCC_except_table691
+ GCC_except_table738
+ GCC_except_table94
+ _AVGQCaptureDepthWithDeepFusionSupported
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._continuousZoomWithDepthDisallowed
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._stereoVideoCaptureStatus
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.stereoVideoCaptureEnabled
+ _OBJC_IVAR_$_AVCaptureSessionInternal.recordingMovieFileOutputs
+ _OBJC_IVAR_$_AVCaptureSessionInternal.recordingMovieFileOutputsLock
+ __FigIsNotCurrentDispatchQueue
+ ___51-[AVCaptureFigVideoDevice stereoVideoCaptureStatus]_block_invoke
+ ___56-[AVCaptureFigVideoDevice _setStereoVideoCaptureStatus:]_block_invoke
+ ___65-[AVCaptureFigVideoDevice _setContinuousZoomWithDepthDisallowed:]_block_invoke
+ ___81-[AVCaptureFigVideoDevice _updateActiveDepthDataFormatForContinuousZoomWithDepth]_block_invoke
+ ___block_literal_global.1195
+ ___block_literal_global.1202
+ ___block_literal_global.659
+ _gAVCaptureConnectionTrace
+ _kFigCaptureSourceNotification_StereoVideoCaptureStatusChanged
+ _objc_msgSend$_getMovieFileOutputNANDDataRate:
+ _objc_msgSend$_informSessionMembersOfChangedActiveFormat:forDevice:mediaType:
+ _objc_msgSend$_initializeContinuousZoomWithDepthActiveWithEnabled:
+ _objc_msgSend$_nandCostWithDataRate:
+ _objc_msgSend$_setContinuousZoomWithDepthActiveWithEnabled:disallowed:isActiveDepthDataFormatChangingOut:
+ _objc_msgSend$_setContinuousZoomWithDepthDisallowed:
+ _objc_msgSend$_setStereoVideoCaptureStatus:
+ _objc_msgSend$_totalNANDBandwidthAllowed:videoCodecType:
+ _objc_msgSend$_updateActiveDepthDataFormatForContinuousZoomWithDepth
+ _objc_msgSend$_updateContinuousZoomWithDepthActiveWithEnabled:disallowed:isActiveDepthDataFormatChangingOut:
+ _objc_msgSend$isStereoVideoCaptureEnabled
+ _objc_msgSend$isStereoVideoCaptureSupported
+ _objc_msgSend$movieFileOutputStoppedRecording:
+ _objc_msgSend$requestNANDBandwidthToStartMovieFileRecording:outputFileURL:videoCodecType:
+ _objc_msgSend$setStereoVideoCaptureEnabled:
+ _objc_msgSend$stereoVideoCaptureEnabled
- -[AVCaptureSession _nandCostWithFormatWidth:height:maxFrameRate:]
- -[AVCaptureSession informSessionMembersOfChangedActiveFormat:forDevice:]
- GCC_except_table101
- GCC_except_table112
- GCC_except_table113
- GCC_except_table119
- GCC_except_table120
- GCC_except_table121
- GCC_except_table122
- GCC_except_table131
- GCC_except_table137
- GCC_except_table176
- GCC_except_table190
- GCC_except_table199
- GCC_except_table211
- GCC_except_table214
- GCC_except_table233
- GCC_except_table239
- GCC_except_table242
- GCC_except_table245
- GCC_except_table247
- GCC_except_table255
- GCC_except_table258
- GCC_except_table278
- GCC_except_table289
- GCC_except_table291
- GCC_except_table293
- GCC_except_table299
- GCC_except_table313
- GCC_except_table336
- GCC_except_table346
- GCC_except_table358
- GCC_except_table373
- GCC_except_table376
- GCC_except_table403
- GCC_except_table407
- GCC_except_table416
- GCC_except_table424
- GCC_except_table437
- GCC_except_table442
- GCC_except_table446
- GCC_except_table463
- GCC_except_table472
- GCC_except_table493
- GCC_except_table504
- GCC_except_table514
- GCC_except_table532
- GCC_except_table551
- GCC_except_table560
- GCC_except_table563
- GCC_except_table584
- GCC_except_table586
- GCC_except_table588
- GCC_except_table611
- GCC_except_table623
- GCC_except_table625
- GCC_except_table627
- GCC_except_table633
- GCC_except_table635
- GCC_except_table676
- GCC_except_table68
- GCC_except_table680
- GCC_except_table727
- GCC_except_table82
- GCC_except_table84
- GCC_except_table91
- ___block_literal_global.1194
- ___block_literal_global.1201
- ___block_literal_global.650
- _objc_msgSend$_nandCostWithFormatWidth:height:maxFrameRate:
- _objc_msgSend$informSessionMembersOfChangedActiveFormat:forDevice:
CStrings:
+ "-[AVCaptureSession _setRunning:]"
+ "AVGQCaptureDepthWithDeepFusionSupported"
+ "B32@0:8B16B20^B24"
+ "Not supported - use isStereoVideoCaptureSupported"
+ "_FigIsNotCurrentDispatchQueue( _devicePropsQueue )"
+ "_continuousZoomWithDepthDisallowed"
+ "_getMovieFileOutputNANDDataRate:"
+ "_informSessionMembersOfChangedActiveFormat:forDevice:mediaType:"
+ "_initializeContinuousZoomWithDepthActiveWithEnabled:"
+ "_nandCostWithDataRate:"
+ "_setContinuousZoomWithDepthActiveWithEnabled:disallowed:isActiveDepthDataFormatChangingOut:"
+ "_setContinuousZoomWithDepthDisallowed:"
+ "_setStereoVideoCaptureStatus:"
+ "_stereoVideoCaptureStatus"
+ "_totalNANDBandwidthAllowed:videoCodecType:"
+ "_updateActiveDepthDataFormatForContinuousZoomWithDepth"
+ "_updateContinuousZoomWithDepthActiveWithEnabled:disallowed:isActiveDepthDataFormatChangingOut:"
+ "avcaptureconnection_trace"
+ "description=CameraCapture_AVF-470.16.1"
+ "f20@0:8i16"
+ "isStereoVideoCaptureEnabled"
+ "isStereoVideoCaptureSupported"
+ "movieFileOutputStoppedRecording:"
+ "recordingMovieFileOutputs"
+ "recordingMovieFileOutputsLock"
+ "requestNANDBandwidthToStartMovieFileRecording:outputFileURL:videoCodecType:"
+ "setStereoVideoCaptureEnabled:"
+ "stereoVideoCaptureEnabled"
+ "stereoVideoCaptureStatus"
- "_nandCostWithFormatWidth:height:maxFrameRate:"
- "description=CameraCapture_AVF-465.15.2"
- "f28@0:8i16i20f24"
- "informSessionMembersOfChangedActiveFormat:forDevice:"

```
