## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9127.1.6.0.0
-  __TEXT.__text: 0x138f58
-  __TEXT.__objc_methlist: 0x10604
+9127.1.7.2.101
+  __TEXT.__text: 0x139794
+  __TEXT.__objc_methlist: 0x107cc
   __TEXT.__dlopen_cstrs: 0x3f1
-  __TEXT.__const: 0x3c7e
+  __TEXT.__const: 0x3c9e
   __TEXT.__swift5_typeref: 0x1dee
   __TEXT.__swift5_capture: 0x624
-  __TEXT.__cstring: 0xd935
-  __TEXT.__constg_swiftt: 0x19c0
+  __TEXT.__cstring: 0xd977
+  __TEXT.__constg_swiftt: 0x1868
   __TEXT.__swift5_reflstr: 0xd95
   __TEXT.__swift5_assocty: 0x370
   __TEXT.__swift5_fieldmd: 0xe38

   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__ustring: 0x258
-  __TEXT.__unwind_info: 0x5308
-  __TEXT.__eh_frame: 0x1c14
+  __TEXT.__unwind_info: 0x52c8
+  __TEXT.__eh_frame: 0x1bfc
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7ab8
-  __DATA_CONST.__objc_classlist: 0x720
+  __DATA_CONST.__const: 0x7b00
+  __DATA_CONST.__objc_classlist: 0x730
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x2b8
+  __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa830
+  __DATA_CONST.__objc_selrefs: 0xa990
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x468
-  __DATA_CONST.__objc_arraydata: 0xae0
-  __DATA_CONST.__got: 0x15e8
-  __AUTH_CONST.__const: 0x2fe8
-  __AUTH_CONST.__cfstring: 0xebe0
-  __AUTH_CONST.__objc_const: 0x1a1c0
+  __DATA_CONST.__objc_arraydata: 0xb10
+  __DATA_CONST.__got: 0x1628
+  __AUTH_CONST.__const: 0x3028
+  __AUTH_CONST.__cfstring: 0xec40
+  __AUTH_CONST.__objc_const: 0x1a608
   __AUTH_CONST.__objc_intobj: 0x3d8
-  __AUTH_CONST.__objc_arrayobj: 0x288
-  __AUTH_CONST.__objc_doubleobj: 0x170
+  __AUTH_CONST.__objc_arrayobj: 0x2b8
+  __AUTH_CONST.__objc_doubleobj: 0x1a0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_floatobj: 0xe0
   __AUTH_CONST.__auth_got: 0x1da8
-  __AUTH.__objc_data: 0x3c38
+  __AUTH.__objc_data: 0x3b58
   __AUTH.__data: 0xb80
-  __DATA.__objc_ivar: 0x1220
-  __DATA.__data: 0x2ca8
+  __DATA.__objc_ivar: 0x1258
+  __DATA.__data: 0x2d28
   __DATA.__common: 0x288
-  __DATA_DIRTY.__objc_data: 0x20d0
+  __DATA_DIRTY.__objc_data: 0x20f8
   __DATA_DIRTY.__data: 0x2e8
-  __DATA_DIRTY.__bss: 0x4e0
+  __DATA_DIRTY.__bss: 0x500
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7070
-  Symbols:   15344
-  CStrings:  2750
+  Functions: 7073
+  Symbols:   15504
+  CStrings:  2753
 
Symbols:
+ +[TUICandidateCell candidateFontForCandidate:style:]
+ +[TUIKeyboardHitDebugTouchChannel _deliverSample:]
+ +[TUIKeyboardHitDebugTouchChannel _isRepeatOfRecentSample:]
+ +[TUIKeyboardHitDebugTouchChannel _observers]
+ +[TUIKeyboardHitDebugTouchChannel addObserver:]
+ +[TUIKeyboardHitDebugTouchChannel publishTouchEvent:]
+ +[TUIKeyboardHitDebugTouchChannel removeObserver:]
+ -[TUIKeyboardHitDebugOverlay _applyMarkerPathForSample:trail:toMarker:]
+ -[TUIKeyboardHitDebugOverlay _beginTapMarkerAtSample:pathKey:]
+ -[TUIKeyboardHitDebugOverlay _closeOutTapMarkerForPathKey:]
+ -[TUIKeyboardHitDebugOverlay _evictableTapMarker]
+ -[TUIKeyboardHitDebugOverlay _extendTapMarkerWithSample:pathKey:isFinal:]
+ -[TUIKeyboardHitDebugOverlay _removeAllTapMarkers]
+ -[TUIKeyboardHitDebugOverlay _removeTapMarker:]
+ -[TUIKeyboardHitDebugOverlay _restartFadeForMarker:]
+ -[TUIKeyboardHitDebugOverlay _startObservingEngineChannels]
+ -[TUIKeyboardHitDebugOverlay _stopObservingEngineChannels]
+ -[TUIKeyboardHitDebugOverlay _updateTapMarkerColors]
+ -[TUIKeyboardHitDebugOverlay didReceiveTouchSample:]
+ -[TUIKeyboardHitDebugOverlay setShowsKeyHitGeometry:]
+ -[TUIKeyboardHitDebugOverlay setShowsTouchPointMarkers:]
+ -[TUIKeyboardHitDebugOverlay setTapMarkerContainerLayer:]
+ -[TUIKeyboardHitDebugOverlay setTapMarkerFadeGeneration:]
+ -[TUIKeyboardHitDebugOverlay setTapMarkerReferenceSize:]
+ -[TUIKeyboardHitDebugOverlay setTapMarkers:]
+ -[TUIKeyboardHitDebugOverlay setTapMarkersByPathIndex:]
+ -[TUIKeyboardHitDebugOverlay setTapTrailsByPathIndex:]
+ -[TUIKeyboardHitDebugOverlay showsKeyHitGeometry]
+ -[TUIKeyboardHitDebugOverlay showsTouchPointMarkers]
+ -[TUIKeyboardHitDebugOverlay stopObserving]
+ -[TUIKeyboardHitDebugOverlay tapMarkerContainerLayer]
+ -[TUIKeyboardHitDebugOverlay tapMarkerFadeGeneration]
+ -[TUIKeyboardHitDebugOverlay tapMarkerReferenceSize]
+ -[TUIKeyboardHitDebugOverlay tapMarkersByPathIndex]
+ -[TUIKeyboardHitDebugOverlay tapMarkers]
+ -[TUIKeyboardHitDebugOverlay tapTrailsByPathIndex]
+ -[_TUITapMarkerTrail .cxx_destruct]
+ -[_TUITapMarkerTrail lastDotLocation]
+ -[_TUITapMarkerTrail lastFadeRestartTimestamp]
+ -[_TUITapMarkerTrail linePath]
+ -[_TUITapMarkerTrail sampleLayer]
+ -[_TUITapMarkerTrail samplePath]
+ -[_TUITapMarkerTrail setLastDotLocation:]
+ -[_TUITapMarkerTrail setLastFadeRestartTimestamp:]
+ -[_TUITapMarkerTrail setLinePath:]
+ -[_TUITapMarkerTrail setSampleLayer:]
+ -[_TUITapMarkerTrail setSamplePath:]
+ -[_TUITapMarkerTrail setStartLocation:]
+ -[_TUITapMarkerTrail startLocation]
+ _OBJC_CLASS_$_CAKeyframeAnimation
+ _OBJC_CLASS_$_CALayer
+ _OBJC_CLASS_$_TUIKeyboardHitDebugTouchChannel
+ _OBJC_CLASS_$__TUITapMarkerTrail
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._showsKeyHitGeometry
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._showsTouchPointMarkers
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._tapMarkerContainerLayer
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._tapMarkerFadeGeneration
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._tapMarkerReferenceSize
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._tapMarkers
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._tapMarkersByPathIndex
+ _OBJC_IVAR_$_TUIKeyboardHitDebugOverlay._tapTrailsByPathIndex
+ _OBJC_IVAR_$__TUITapMarkerTrail._lastDotLocation
+ _OBJC_IVAR_$__TUITapMarkerTrail._lastFadeRestartTimestamp
+ _OBJC_IVAR_$__TUITapMarkerTrail._linePath
+ _OBJC_IVAR_$__TUITapMarkerTrail._sampleLayer
+ _OBJC_IVAR_$__TUITapMarkerTrail._samplePath
+ _OBJC_IVAR_$__TUITapMarkerTrail._startLocation
+ _OBJC_METACLASS_$_TUIKeyboardHitDebugTouchChannel
+ _OBJC_METACLASS_$__TUITapMarkerTrail
+ _TIGetShowTouchPointDebugUIValue.onceToken
+ _TUICandidateFont
+ _TUICandidateRowHeight
+ _TUIKeyboardHitDebugTouchChannelHasObservers
+ _TUIMinimumCandidateLabelHeight
+ __OBJC_$_CLASS_METHODS_TUIKeyboardHitDebugTouchChannel
+ __OBJC_$_INSTANCE_METHODS__TUITapMarkerTrail
+ __OBJC_$_INSTANCE_VARIABLES__TUITapMarkerTrail
+ __OBJC_$_PROP_LIST__TUITapMarkerTrail
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TUIKeyboardHitDebugTouchObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TUIKeyboardHitDebugTouchObserver
+ __OBJC_$_PROTOCOL_REFS_TUIKeyboardHitDebugTouchObserver
+ __OBJC_CLASS_PROTOCOLS_$_TUIKeyboardHitDebugOverlay
+ __OBJC_CLASS_RO_$_TUIKeyboardHitDebugTouchChannel
+ __OBJC_CLASS_RO_$__TUITapMarkerTrail
+ __OBJC_LABEL_PROTOCOL_$_TUIKeyboardHitDebugTouchObserver
+ __OBJC_METACLASS_RO_$_TUIKeyboardHitDebugTouchChannel
+ __OBJC_METACLASS_RO_$__TUITapMarkerTrail
+ __OBJC_PROTOCOL_$_TUIKeyboardHitDebugTouchObserver
+ __TUITapMarkerTrailColor
+ ___44-[TUIKeyboardHitDebugOverlay initWithFrame:]_block_invoke
+ ___45+[TUIKeyboardHitDebugTouchChannel _observers]_block_invoke
+ ___52-[TUIKeyboardHitDebugOverlay _restartFadeForMarker:]_block_invoke
+ ___53+[TUIKeyboardHitDebugTouchChannel publishTouchEvent:]_block_invoke
+ ___59-[TUIKeyboardHitDebugOverlay _startObservingEngineChannels]_block_invoke
+ ___59-[TUIKeyboardHitDebugOverlay _startObservingEngineChannels]_block_invoke_2
+ ___TIGetShowTouchPointDebugUIValue_block_invoke
+ ___block_descriptor_56_8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_88_e5_v8?0l
+ __isRepeatOfRecentSample:.nextSlot
+ __isRepeatOfRecentSample:.recentPathIndices
+ __isRepeatOfRecentSample:.recentTimestamps
+ __observers.observers
+ __observers.onceToken
+ _kCAFillRuleEvenOdd
+ _kCALineCapRound
+ _kCALineJoinRound
+ _kCAMediaTimingFunctionEaseIn
+ _objc_msgSend$_applyMarkerPathForSample:trail:toMarker:
+ _objc_msgSend$_beginTapMarkerAtSample:pathKey:
+ _objc_msgSend$_closeOutTapMarkerForPathKey:
+ _objc_msgSend$_deliverSample:
+ _objc_msgSend$_evictableTapMarker
+ _objc_msgSend$_extendTapMarkerWithSample:pathKey:isFinal:
+ _objc_msgSend$_isRepeatOfRecentSample:
+ _objc_msgSend$_observers
+ _objc_msgSend$_removeAllTapMarkers
+ _objc_msgSend$_removeTapMarker:
+ _objc_msgSend$_restartFadeForMarker:
+ _objc_msgSend$_startObservingEngineChannels
+ _objc_msgSend$_stopObservingEngineChannels
+ _objc_msgSend$_updateTapMarkerColors
+ _objc_msgSend$addObserver:
+ _objc_msgSend$allKeysForObject:
+ _objc_msgSend$candidateFontForCandidate:style:
+ _objc_msgSend$didReceiveTouchSample:
+ _objc_msgSend$lastDotLocation
+ _objc_msgSend$lastFadeRestartTimestamp
+ _objc_msgSend$linePath
+ _objc_msgSend$location
+ _objc_msgSend$publishTouchEvent:
+ _objc_msgSend$radius
+ _objc_msgSend$removeObjectIdenticalTo:
+ _objc_msgSend$sampleLayer
+ _objc_msgSend$samplePath
+ _objc_msgSend$setFillRule:
+ _objc_msgSend$setKeyTimes:
+ _objc_msgSend$setLastDotLocation:
+ _objc_msgSend$setLastFadeRestartTimestamp:
+ _objc_msgSend$setLineCap:
+ _objc_msgSend$setLineJoin:
+ _objc_msgSend$setLinePath:
+ _objc_msgSend$setSampleLayer:
+ _objc_msgSend$setSamplePath:
+ _objc_msgSend$setShowsKeyHitGeometry:
+ _objc_msgSend$setShowsTouchPointMarkers:
+ _objc_msgSend$setStartLocation:
+ _objc_msgSend$setTapMarkerContainerLayer:
+ _objc_msgSend$setTapMarkerFadeGeneration:
+ _objc_msgSend$setTapMarkerReferenceSize:
+ _objc_msgSend$setTapMarkers:
+ _objc_msgSend$setTapMarkersByPathIndex:
+ _objc_msgSend$setTapTrailsByPathIndex:
+ _objc_msgSend$setTimingFunctions:
+ _objc_msgSend$setValues:
+ _objc_msgSend$showsKeyHitGeometry
+ _objc_msgSend$showsTouchPointMarkers
+ _objc_msgSend$stage
+ _objc_msgSend$startLocation
+ _objc_msgSend$stopObserving
+ _objc_msgSend$tapMarkerContainerLayer
+ _objc_msgSend$tapMarkerFadeGeneration
+ _objc_msgSend$tapMarkerReferenceSize
+ _objc_msgSend$tapMarkers
+ _objc_msgSend$tapMarkersByPathIndex
+ _objc_msgSend$tapTrailsByPathIndex
+ _sHasObservers
+ _type_layout_string So7CGPointV
- -[TUIKeyboardHitDebugOverlay startObservingEngineChannels]
- -[TUIKeyboardHitDebugOverlay stopObservingEngineChannels]
- ___58-[TUIKeyboardHitDebugOverlay startObservingEngineChannels]_block_invoke
- ___58-[TUIKeyboardHitDebugOverlay startObservingEngineChannels]_block_invoke_2
- _objc_msgSend$startObservingEngineChannels
- _objc_msgSend$stopObservingEngineChannels
- _type_layout_string So6CGSizeV
CStrings:
+ "8"
+ "ShowTouchPointDebugUI"
+ "TUITapMarkerFade"
+ "TUITapMarkerFadeGeneration"
- "4"
```
