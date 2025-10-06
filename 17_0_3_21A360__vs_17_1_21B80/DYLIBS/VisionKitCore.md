## VisionKitCore

> `/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore`

```diff

-247.1.0.0.0
-  __TEXT.__text: 0xc24bc
-  __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_methlist: 0xcb40
+251.2.0.0.0
+  __TEXT.__text: 0xc2f10
+  __TEXT.__auth_stubs: 0x14a0
+  __TEXT.__objc_methlist: 0xcb30
   __TEXT.__const: 0x804
-  __TEXT.__gcc_except_tab: 0x21dc
-  __TEXT.__cstring: 0x7763
-  __TEXT.__oslogstring: 0x2f8c
+  __TEXT.__gcc_except_tab: 0x222c
+  __TEXT.__cstring: 0x7720
+  __TEXT.__oslogstring: 0x3004
   __TEXT.__dlopen_cstrs: 0x419
   __TEXT.__ustring: 0xa0
-  __TEXT.__unwind_info: 0x3c20
+  __TEXT.__unwind_info: 0x3c5c
   __TEXT.__eh_frame: 0x74
-  __TEXT.__objc_classname: 0x1725
-  __TEXT.__objc_methname: 0x25aaa
-  __TEXT.__objc_methtype: 0x5e06
-  __TEXT.__objc_stubs: 0x19e00
+  __TEXT.__objc_classname: 0x1740
+  __TEXT.__objc_methname: 0x25b88
+  __TEXT.__objc_methtype: 0x5df9
+  __TEXT.__objc_stubs: 0x19e80
   __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x3858
-  __DATA_CONST.__objc_classlist: 0x530
+  __DATA_CONST.__const: 0x38b0
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b308
-  __DATA_CONST.__objc_selrefs: 0x7ff0
+  __DATA_CONST.__objc_const: 0x1b3f8
+  __DATA_CONST.__objc_selrefs: 0x8018
   __DATA_CONST.__objc_arraydata: 0x220
   __AUTH_CONST.__cfstring: 0x63c0
-  __AUTH_CONST.__objc_const: 0x3ff8
+  __AUTH_CONST.__objc_const: 0x4040
   __AUTH_CONST.__const: 0xdb0
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xa60
-  __AUTH.__objc_data: 0x2170
+  __AUTH_CONST.__auth_got: 0xa68
+  __AUTH.__objc_data: 0x2210
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0xa50
-  __DATA.__objc_superrefs: 0x378
-  __DATA.__objc_ivar: 0x1028
+  __DATA.__objc_classrefs: 0xa58
+  __DATA.__objc_superrefs: 0x380
+  __DATA.__objc_ivar: 0x1030
   __DATA.__data: 0x1670
   __DATA.__bss: 0x3a8
   __DATA_DIRTY.__objc_data: 0x1270

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
   - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RevealCore.framework/RevealCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E54548E4-49B4-3501-84A3-0F7FE1F2D54F
-  Functions: 5873
-  Symbols:   19467
-  CStrings:  9252
+  UUID: F0FFEE37-8C1A-3F37-AB4F-18BADC776D8F
+  Functions: 5893
+  Symbols:   19526
+  CStrings:  9262
 
Symbols:
+ +[VKCPreDeclare cropRectForMatteResult:]
+ -[VKAVCapture setVideoRotationAngle:completion:]
+ -[VKAVCapture videoRotationAngle]
+ -[VKAVCaptureFrameProvider _avCapturePreparationComplete].cold.1
+ -[VKAVCaptureFrameProvider previewView:didMoveToWindow:]
+ -[VKAVCapturePreviewView didMoveToWindow]
+ -[VKAVCapturePreviewView setVideoRotationAngle:]
+ -[VKAVCapturePreviewView videoRotationAngle]
+ -[VKCImageAnalysisResult cachedCustomImageForRemoveBackground]
+ -[VKCImageAnalysisResult setCachedCustomImageForRemoveBackground:]
+ -[VKCImageSubjectHighlightView addSticker]
+ -[VKCStickerEffectView didMoveToWindow]
+ -[VKCStickerEffectView displayLinkFired:]
+ -[VKCStickerEffectView startPlaybackIfNecessary]
+ -[VKCStickerVideoDecoder duration]
+ -[VKCStickerVideoDecoder frameForTargetTimestamp:]
+ -[VKCStickerVideoDecoder frameRanges]
+ -[VKCStickerVideoDecoder previousFrameIndex]
+ -[VKCStickerVideoDecoder setDuration:]
+ -[VKCStickerVideoDecoder setFrameRanges:]
+ -[VKCStickerVideoDecoder setPreviousFrameIndex:]
+ -[VKCTimeRange contains:]
+ -[VKCTimeRange duration]
+ -[VKCTimeRange end]
+ -[VKCTimeRange initWithStart:duration:]
+ -[VKCTimeRange setDuration:]
+ -[VKCTimeRange setStart:]
+ -[VKCTimeRange start]
+ GCC_except_table118
+ _MKBGetDeviceLockState
+ _OBJC_CLASS_$_VKCPreDeclare
+ _OBJC_CLASS_$_VKCTimeRange
+ _OBJC_IVAR_$_VKCImageAnalysisResult._cachedCustomImageForRemoveBackground
+ _OBJC_IVAR_$_VKCStickerEffectView._displayLink
+ _OBJC_IVAR_$_VKCStickerEffectView._startTimeInterval
+ _OBJC_IVAR_$_VKCStickerVideoDecoder._duration
+ _OBJC_IVAR_$_VKCStickerVideoDecoder._frameRanges
+ _OBJC_IVAR_$_VKCStickerVideoDecoder._previousFrameIndex
+ _OBJC_IVAR_$_VKCTimeRange._duration
+ _OBJC_IVAR_$_VKCTimeRange._start
+ _OBJC_METACLASS_$_VKCPreDeclare
+ _OBJC_METACLASS_$_VKCTimeRange
+ __OBJC_$_CLASS_METHODS_VKCPreDeclare
+ __OBJC_$_INSTANCE_VARIABLES_VKCTimeRange
+ __OBJC_CLASS_RO_$_VKCPreDeclare
+ __OBJC_CLASS_RO_$_VKCTimeRange
+ __OBJC_METACLASS_RO_$_VKCPreDeclare
+ __OBJC_METACLASS_RO_$_VKCTimeRange
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke.216
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke.216.cold.1
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke.217
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke.227
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke.cold.1
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke_2
+ ___42-[VKCImageSubjectHighlightView addSticker]_block_invoke_2.cold.1
+ ___48-[VKAVCapture setVideoRotationAngle:completion:]_block_invoke
+ ___48-[VKAVCapture setVideoRotationAngle:completion:]_block_invoke_2
+ ___57-[VKAVCaptureFrameProvider _avCapturePreparationComplete]_block_invoke
+ ___66-[VKCImageSubjectBaseView loadImageSubjectWithIndexes:completion:]_block_invoke.106
+ ___66-[VKCImageSubjectBaseView loadImageSubjectWithIndexes:completion:]_block_invoke.106.cold.1
+ ___66-[VKCImageSubjectBaseView loadImageSubjectWithIndexes:completion:]_block_invoke.108
+ ___69-[VKCImageSubjectBaseView _loadSubjectMaskIfNecessaryWithCompletion:]_block_invoke.101
+ ___69-[VKCImageSubjectBaseView _loadSubjectMaskIfNecessaryWithCompletion:]_block_invoke.101.cold.1
+ ___69-[VKCImageSubjectBaseView _loadSubjectMaskIfNecessaryWithCompletion:]_block_invoke.103
+ ___75-[VKAVCaptureFrameProvider observeValueForKeyPath:ofObject:change:context:]_block_invoke_3
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___vk_requestDeviceUnlockIfNecessaryWithCompletion_block_invoke
+ _objc_msgSend$addSticker
+ _objc_msgSend$addToRunLoop:forMode:
+ _objc_msgSend$cachedCustomImageForRemoveBackground
+ _objc_msgSend$cropRectForMatteResult:
+ _objc_msgSend$displayLinkWithTarget:selector:
+ _objc_msgSend$duration
+ _objc_msgSend$frameRanges
+ _objc_msgSend$previewView:didMoveToWindow:
+ _objc_msgSend$previousFrameIndex
+ _objc_msgSend$requestPasscodeUnlockUIWithOptions:withCompletion:
+ _objc_msgSend$setCachedCustomImageForRemoveBackground:
+ _objc_msgSend$setFrameRanges:
+ _objc_msgSend$setPreviousFrameIndex:
+ _objc_msgSend$startPlaybackIfNecessary
+ _objc_msgSend$targetTimestamp
+ _objc_msgSend$videoRotationAngle
- -[VKAVCapturePreviewView interfaceOrientation]
- -[VKCImageSubjectContext customImageForRemoveBackground]
- -[VKCImageSubjectContext setCustomImageForRemoveBackground:]
- -[VKCStickerEffectView decoder:displayFrame:forIndex:]
- -[VKCStickerVideoDecoder beginPlayback]
- -[VKCStickerVideoDecoder currentFrameIndex]
- -[VKCStickerVideoDecoder displayNextFrame]
- -[VKCStickerVideoDecoder frames]
- -[VKCStickerVideoDecoder isPaused]
- -[VKCStickerVideoDecoder setCurrentFrameIndex:]
- -[VKCStickerVideoDecoder setFrames:]
- -[VKCStickerVideoDecoder setPaused:]
- -[VKCStickerVideoDecoder setTimer:]
- -[VKCStickerVideoDecoder timer]
- GCC_except_table115
- GCC_except_table116
- _OBJC_CLASS_$_NSNull
- _OBJC_IVAR_$_VKAVCapturePreviewView._interfaceOrientation
- _OBJC_IVAR_$_VKCImageSubjectContext._customImageForRemoveBackground
- _OBJC_IVAR_$_VKCStickerVideoDecoder._currentFrameIndex
- _OBJC_IVAR_$_VKCStickerVideoDecoder._frames
- _OBJC_IVAR_$_VKCStickerVideoDecoder._paused
- _OBJC_IVAR_$_VKCStickerVideoDecoder._timer
- ___66-[VKCImageSubjectBaseView loadImageSubjectWithIndexes:completion:]_block_invoke.105
- ___66-[VKCImageSubjectBaseView loadImageSubjectWithIndexes:completion:]_block_invoke.105.cold.1
- ___66-[VKCImageSubjectBaseView loadImageSubjectWithIndexes:completion:]_block_invoke.107
- ___66-[VKCImageSubjectHighlightView stickerPickerViewControllerDidLoad]_block_invoke.216
- ___66-[VKCImageSubjectHighlightView stickerPickerViewControllerDidLoad]_block_invoke.216.cold.1
- ___66-[VKCImageSubjectHighlightView stickerPickerViewControllerDidLoad]_block_invoke.217
- ___66-[VKCImageSubjectHighlightView stickerPickerViewControllerDidLoad]_block_invoke.227
- ___66-[VKCImageSubjectHighlightView stickerPickerViewControllerDidLoad]_block_invoke.cold.1
- ___66-[VKCImageSubjectHighlightView stickerPickerViewControllerDidLoad]_block_invoke_2
- ___66-[VKCImageSubjectHighlightView stickerPickerViewControllerDidLoad]_block_invoke_2.cold.1
- ___69-[VKCImageSubjectBaseView _loadSubjectMaskIfNecessaryWithCompletion:]_block_invoke.100
- ___69-[VKCImageSubjectBaseView _loadSubjectMaskIfNecessaryWithCompletion:]_block_invoke.100.cold.1
- ___69-[VKCImageSubjectBaseView _loadSubjectMaskIfNecessaryWithCompletion:]_block_invoke.102
- _objc_msgSend$addTimer:forMode:
- _objc_msgSend$beginPlayback
- _objc_msgSend$currentFrameIndex
- _objc_msgSend$decoder:displayFrame:forIndex:
- _objc_msgSend$displayNextFrame
- _objc_msgSend$frameDelays
- _objc_msgSend$null
- _objc_msgSend$setCurrentFrameIndex:
- _objc_msgSend$setFrames:
- _objc_msgSend$setTimer:
- _objc_msgSend$timer
- _objc_msgSend$timerWithTimeInterval:target:selector:userInfo:repeats:
CStrings:
+ "\x12\x11\x11"
+ "\"\x12"
+ "%@ - AVCapturePreviewView doesn't have a window. Can't start running"
+ "@\"CADisplayLink\""
+ "AddSticker"
+ "Setting custom image for remove background: %@, %@"
+ "T@\"NSMutableArray\",&,N,V_frameRanges"
+ "T@\"UIImage\",&,N,V_cachedCustomImageForRemoveBackground"
+ "Td,N,V_duration"
+ "Tq,N,V_previousFrameIndex"
+ "Trying to perform a remove background request with performInPlace and cropToFit set to true, this is not support, falling back to just cropToFit"
+ "VKCPreDeclare"
+ "VKCTimeRange"
+ "_cachedCustomImageForRemoveBackground"
+ "_displayLink"
+ "_duration"
+ "_frameRanges"
+ "_previousFrameIndex"
+ "_start"
+ "_startTimeInterval"
+ "addSticker"
+ "addToRunLoop:forMode:"
+ "cachedCustomImageForRemoveBackground"
+ "cropRectForMatteResult:"
+ "displayLinkFired:"
+ "displayLinkWithTarget:selector:"
+ "duration"
+ "frameRanges"
+ "previewView:didMoveToWindow:"
+ "previousFrameIndex"
+ "requestPasscodeUnlockUIWithOptions:withCompletion:"
+ "setCachedCustomImageForRemoveBackground:"
+ "setFrameRanges:"
+ "setPreviousFrameIndex:"
+ "startPlaybackIfNecessary"
+ "targetTimestamp"
+ "v32@0:8@\"VKAVCapturePreviewView\"16@\"UIWindow\"24"
+ "videoRotationAngle"
- "\x17"
- "!\x11\x11\x12"
- "-[VKCStickerVideoDecoder displayNextFrame]"
- "T@\"<VKCStickerVideoDecoderDelegate>\",W,N,V_delegate"
- "T@\"NSData\",&,N,V_videoData"
- "T@\"NSMutableArray\",&,N,V_frames"
- "T@\"NSTimer\",&,N,V_timer"
- "TB,N,GisPaused,V_paused"
- "Tq,N,V_currentFrameIndex"
- "Trying to perform a remove backgroudn request with performInPlace and cropToFit set to true, this is not support, falling back to just cropToFit"
- "Unable to get frame for index: %ld"
- "_currentFrameIndex"
- "_frames"
- "_paused"
- "_timer"
- "addTimer:forMode:"
- "beginPlayback"
- "currentFrameIndex"
- "decoder:displayFrame:forIndex:"
- "displayNextFrame"
- "null"
- "setCurrentFrameIndex:"
- "setFrames:"
- "setTimer:"
- "timer"
- "timerWithTimeInterval:target:selector:userInfo:repeats:"
- "v40@0:8@\"VKCStickerVideoDecoder\"16^{CGImage=}24q32"
- "v40@0:8@16^{CGImage=}24q32"

```
