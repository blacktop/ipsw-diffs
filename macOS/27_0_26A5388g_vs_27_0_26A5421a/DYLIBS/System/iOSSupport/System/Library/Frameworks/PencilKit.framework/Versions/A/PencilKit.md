## PencilKit

> `/System/iOSSupport/System/Library/Frameworks/PencilKit.framework/Versions/A/PencilKit`

```diff

-613.0.0.0.0
-  __TEXT.__text: 0x329680
-  __TEXT.__objc_methlist: 0x2e2f4
-  __TEXT.__const: 0x8a34
+616.0.0.0.0
+  __TEXT.__text: 0x32a360
+  __TEXT.__objc_methlist: 0x2e394
+  __TEXT.__const: 0x8a44
   __TEXT.__dlopen_cstrs: 0x351
   __TEXT.__constg_swiftt: 0x1d40
   __TEXT.__swift5_typeref: 0x1e02

   __TEXT.__swift5_assocty: 0x6e0
   __TEXT.__swift5_proto: 0x388
   __TEXT.__swift5_types: 0x1c0
-  __TEXT.__cstring: 0xc8f9
+  __TEXT.__cstring: 0xc943
   __TEXT.__swift5_capture: 0xa30
   __TEXT.__oslogstring: 0xc94c
   __TEXT.__swift_as_entry: 0xf0

   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x26018
+  __TEXT.__gcc_except_tab: 0x260f8
   __TEXT.__ustring: 0x23a
-  __TEXT.__unwind_info: 0x10cb0
+  __TEXT.__unwind_info: 0x10cd8
   __TEXT.__eh_frame: 0x2ae8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x770
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x17da0
+  __DATA_CONST.__objc_selrefs: 0x17de8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0xc60
   __DATA_CONST.__objc_arraydata: 0x918
-  __DATA_CONST.__got: 0x2040
+  __DATA_CONST.__got: 0x2058
   __AUTH_CONST.__const: 0x7e80
-  __AUTH_CONST.__cfstring: 0xdfa0
+  __AUTH_CONST.__cfstring: 0xe000
   __AUTH_CONST.__objc_const: 0x476c8
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x8b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19472
-  Symbols:   43194
-  CStrings:  3290
+  Functions: 19483
+  Symbols:   43218
+  CStrings:  3293
 
Symbols:
+ +[PKTextInputElementsFinder _isExcludedTargetedWorkaroundView:]
+ -[PKDrawing(Slicing) sliceWithEraseStroke:honoringErasable:]
+ -[PKGroupQuery isAnyStrokeInMathGroup:]
+ -[PKImageView setBounds:]
+ -[PKMetalRenderer copyFromAddMultiplyLayersUsingRenderEncoder:clearIfMissing:setupClipping:]
+ -[PKPaletteHostView _compactHorizontalEdgePosition]
+ -[PKPaletteHostView _fixToHorizontalEdge:]
+ -[PKPaletteHostView _updateConstraintsToFixToHorizontalEdge:]
+ -[PKPaletteToolPickerAndColorPickerView _compactToolsContainerMaximumWidth]
+ -[PKPaletteToolPickerAndColorPickerView didMoveToWindow]
+ -[PKPaletteToolPickerAndColorPickerView safeAreaInsetsDidChange]
+ -[PKRecognitionController isAnyStrokeInMathGroup:]
+ -[PKRecognitionSessionManager isAnyStrokeInMathGroup:]
+ -[PKStroke _isErasable]
+ -[PKTiledView onScreenRotationForDrawing:]
+ -[_PKInkThicknessButton _applyColorsForSelected:highlighted:animated:]
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table316
+ GCC_except_table325
+ GCC_except_table328
+ GCC_except_table330
+ GCC_except_table332
+ GCC_except_table335
+ GCC_except_table342
+ GCC_except_table349
+ GCC_except_table351
+ GCC_except_table356
+ GCC_except_table359
+ GCC_except_table367
+ GCC_except_table374
+ GCC_except_table378
+ GCC_except_table383
+ GCC_except_table389
+ GCC_except_table395
+ GCC_except_table402
+ GCC_except_table408
+ GCC_except_table565
+ _$sSo19PKStrokeRenderStateC9PencilKitEyAbC0A0V0bC0VcfC
+ _OBJC_CLASS_$_CATransition
+ _PKPaletteContentTopInset
+ __60-[PKDrawing(Slicing) sliceWithEraseStroke:honoringErasable:]_block_invoke
+ ___52-[PKTiledCanvasView eraseStrokesForPoint:prevPoint:]_block_invoke
+ ___60-[PKDrawing(Slicing) sliceWithEraseStroke:honoringErasable:]_block_invoke
+ ___60-[PKDrawing(Slicing) sliceWithEraseStroke:honoringErasable:]_block_invoke_2
+ _kCAMediaTimingFunctionDefault
+ _kCATransitionFade
+ _objc_msgSend$_applyColorsForSelected:highlighted:animated:
+ _objc_msgSend$_compactHorizontalEdgePosition
+ _objc_msgSend$_compactToolsContainerMaximumWidth
+ _objc_msgSend$_fixToHorizontalEdge:
+ _objc_msgSend$_isErasable
+ _objc_msgSend$_isExcludedTargetedWorkaroundView:
+ _objc_msgSend$_updateConstraintsToFixToHorizontalEdge:
+ _objc_msgSend$copyFromAddMultiplyLayersUsingRenderEncoder:clearIfMissing:setupClipping:
+ _objc_msgSend$flush
+ _objc_msgSend$isAnyStrokeInMathGroup:
+ _objc_msgSend$onScreenRotationForDrawing:
+ _objc_msgSend$presentationLayer
+ _objc_msgSend$sliceWithEraseStroke:honoringErasable:
- -[PKMetalRenderer copyFromAddMultiplyLayersUsingRenderEncoder:clearIfMissing:]
- -[PKPaletteHostView _fixToBottomEdge]
- -[PKPaletteHostView _updateConstraintsToFixToBottomEdge]
- GCC_except_table302
- GCC_except_table308
- GCC_except_table311
- GCC_except_table319
- GCC_except_table326
- GCC_except_table329
- GCC_except_table331
- GCC_except_table334
- GCC_except_table338
- GCC_except_table347
- GCC_except_table350
- GCC_except_table352
- GCC_except_table357
- GCC_except_table364
- GCC_except_table370
- GCC_except_table375
- GCC_except_table379
- GCC_except_table384
- GCC_except_table390
- GCC_except_table396
- GCC_except_table404
- GCC_except_table564
- _$s9PencilKit8PKStrokeV11RenderStateV012asObjCRenderE0So0cdE0CyF
- _PKIsPhoneLandscape
- __43-[PKDrawing(Slicing) sliceWithEraseStroke:]_block_invoke
- ___43-[PKDrawing(Slicing) sliceWithEraseStroke:]_block_invoke
- ___43-[PKDrawing(Slicing) sliceWithEraseStroke:]_block_invoke_2
- ___46-[_PKInkThicknessButton setSelected:animated:]_block_invoke
- ___52-[_PKInkThicknessButton _animateToHighlightedState:]_block_invoke
- ___52-[_PKInkThicknessButton _animateToHighlightedState:]_block_invoke_2
- _objc_msgSend$_fixToBottomEdge
- _objc_msgSend$_updateConstraintsToFixToBottomEdge
- _objc_msgSend$copyFromAddMultiplyLayersUsingRenderEncoder:clearIfMissing:
CStrings:
+ "PaperKit.WritingToolsTextInputView"
+ "backgroundColorFade"
+ "tintColorCrossfade"
```
