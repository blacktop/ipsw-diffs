## PencilKit

> `/System/iOSSupport/System/Library/Frameworks/PencilKit.framework/Versions/A/PencilKit`

```diff

-616.0.0.0.0
-  __TEXT.__text: 0x32a5e4
-  __TEXT.__objc_methlist: 0x2e3a4
-  __TEXT.__const: 0x8a44
+622.1.2.0.0
+  __TEXT.__text: 0x32bbb8
+  __TEXT.__objc_methlist: 0x2e5ec
+  __TEXT.__const: 0x8ad4
   __TEXT.__dlopen_cstrs: 0x351
   __TEXT.__constg_swiftt: 0x1d40
   __TEXT.__swift5_typeref: 0x1e02

   __TEXT.__swift5_assocty: 0x6e0
   __TEXT.__swift5_proto: 0x388
   __TEXT.__swift5_types: 0x1c0
-  __TEXT.__cstring: 0xc943
+  __TEXT.__cstring: 0xc95e
   __TEXT.__swift5_capture: 0xa30
-  __TEXT.__oslogstring: 0xc94c
+  __TEXT.__oslogstring: 0xc9fd
   __TEXT.__swift_as_entry: 0xf0
   __TEXT.__swift_as_cont: 0x218
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x260f8
+  __TEXT.__gcc_except_tab: 0x2619c
   __TEXT.__ustring: 0x23a
-  __TEXT.__unwind_info: 0x10cd8
+  __TEXT.__unwind_info: 0x10d30
   __TEXT.__eh_frame: 0x2ae8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6860
-  __DATA_CONST.__objc_classlist: 0x1008
+  __DATA_CONST.__const: 0x6838
+  __DATA_CONST.__objc_classlist: 0x1018
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x770
+  __DATA_CONST.__objc_protolist: 0x778
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x17df0
+  __DATA_CONST.__objc_selrefs: 0x17ee8
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0xc60
-  __DATA_CONST.__objc_arraydata: 0x918
-  __DATA_CONST.__got: 0x2058
-  __AUTH_CONST.__const: 0x7e80
-  __AUTH_CONST.__cfstring: 0xe000
-  __AUTH_CONST.__objc_const: 0x476e0
+  __DATA_CONST.__objc_superrefs: 0xc68
+  __DATA_CONST.__objc_arraydata: 0x950
+  __DATA_CONST.__got: 0x2068
+  __AUTH_CONST.__const: 0x7ee0
+  __AUTH_CONST.__cfstring: 0xe040
+  __AUTH_CONST.__objc_const: 0x47c30
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x8b8
-  __AUTH_CONST.__objc_arrayobj: 0x6a8
-  __AUTH_CONST.__objc_dictobj: 0x460
+  __AUTH_CONST.__objc_arrayobj: 0x6c0
+  __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__auth_got: 0x1c78
+  __AUTH_CONST.__auth_got: 0x1c88
   __AUTH_CONST.__auth_ptr: 0x880
-  __AUTH.__objc_data: 0x97d8
+  __AUTH.__objc_data: 0x9878
   __AUTH.__data: 0xb80
-  __DATA.__objc_ivar: 0x2808
-  __DATA.__data: 0x6540
+  __DATA.__objc_ivar: 0x282c
+  __DATA.__data: 0x65b0
   __DATA.__bss: 0x6c70
   __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_ivar: 0x10c0
+  __DATA_DIRTY.__objc_ivar: 0x10dc
   __DATA_DIRTY.__objc_data: 0x1630
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x900
+  __DATA_DIRTY.__bss: 0x948
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19483
-  Symbols:   43219
-  CStrings:  3293
+  Functions: 19520
+  Symbols:   43312
+  CStrings:  3297
 
Symbols:
+ +[PKDataDetectorRevealHighlighter sharedHighlighter]
+ +[PKInkingTool _convertColorFromLight:toAppearance:]
+ +[PKInkingTool _isPureBlackOrWhite:]
+ +[PKTextInputLanguageSelectionController _scriptQualifiedLocaleIdentifiers]
+ +[PKTextInputLanguageSelectionController _transliterationInputModeRules]
+ -[PKColorMatrixView colorAppearance]
+ -[PKColorMatrixView setColorAppearance:]
+ -[PKColorPicker colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKColorPicker setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[PKDataDetectorRevealHighlighter completeHighlightingItem:]
+ -[PKDataDetectorRevealHighlighter highlightItem:withProgress:]
+ -[PKDataDetectorRevealHighlighter highlightRangeChangedForItem:]
+ -[PKDataDetectorRevealHighlighter highlightRectsForItem:]
+ -[PKDataDetectorRevealHighlighter highlighting]
+ -[PKDataDetectorRevealHighlighter startHighlightingItem:]
+ -[PKDataDetectorRevealHighlighter stopHighlightingItem:]
+ -[PKDeviceLockStateObserver dealloc]
+ -[PKDeviceLockStateObserver initWithHandler:]
+ -[PKDeviceLockStateObserver isDeviceLocked]
+ -[PKDrawingPaletteView _contentViewForTesting]
+ -[PKDrawingPaletteView _toolPickerViewForTesting]
+ -[PKDrawingPaletteView colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKDrawingPaletteView setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[PKInkAttributesPicker colorAppearance]
+ -[PKInkAttributesPicker setColorAppearance:]
+ -[PKMetalRenderer newComputeVertexBufferWithLength:outOffset:commandBuffer:]
+ -[PKMetalResourceHandlerBuffer initWithSize:options:device:purgeable:initialReusableBufferCount:]
+ -[PKPaletteBaseColorPickerController colorAppearance]
+ -[PKPaletteBaseColorPickerController setColorAppearance:]
+ -[PKPaletteColorPickerView colorAppearance]
+ -[PKPaletteColorPickerView setColorAppearance:]
+ -[PKPaletteColorSwatch colorAppearance]
+ -[PKPaletteColorSwatch setColorAppearance:]
+ -[PKPaletteHostView _setPaletteDockedToHorizontalEdge:]
+ -[PKPaletteHostView _updateContextMenuAvoidanceRect]
+ -[PKPaletteHostView _usesCompactPaletteWidth]
+ -[PKPaletteHostView compactPaletteAvailableWidth]
+ -[PKPaletteMoreOptionsViewController cornerLocation]
+ -[PKPaletteMoreOptionsViewController edgeLocation]
+ -[PKPaletteMoreOptionsViewController preferredContentSize]
+ -[PKPaletteMoreOptionsViewController setCornerLocation:]
+ -[PKPaletteMoreOptionsViewController setEdgeLocation:]
+ -[PKPaletteStandardColorPickerController colorAppearance]
+ -[PKPaletteSystemColorPickerController _shouldConvertColorPickerColorFromDarkToLight:]
+ -[PKPaletteSystemColorPickerController colorAppearance]
+ -[PKPaletteSystemColorPickerController setColorAppearance:]
+ -[PKPaletteToolPickerAndColorPickerView compactPaletteWidth]
+ -[PKPaletteToolPickerAndColorPickerView setCompactPaletteWidth:]
+ -[PKPaletteToolPickerView _ensureFirstToolVisibleForRTLIfNeeded]
+ -[PKPaletteToolPickerView _isAllToolsColorAppearanceEqualsTo:]
+ -[PKPaletteToolPickerView colorAppearance]
+ -[PKPaletteToolPickerView setColorAppearance:]
+ -[PKPaletteToolPreview colorAppearance]
+ -[PKPaletteToolPreview setColorAppearance:]
+ -[PKPaletteToolView colorAppearance]
+ -[PKPaletteToolView setColorAppearance:]
+ -[PKPaletteView compactPaletteWidth]
+ -[PKPaletteView minimizedPaletteSizeScaleFactor]
+ -[PKTextInputLanguageSelectionController ensureKeyboardLanguageConsistencyIfNeededWhileWriting:]
+ -[PKToolPicker _colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKToolPicker _setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[_PKColorAlphaSliderIOS colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[_PKColorAlphaSliderIOS setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[_PKInkAttributesPickerView colorAppearance]
+ -[_PKInkAttributesPickerView setColorAppearance:]
+ OBJC_IVAR_$_PKColorMatrixView._colorAppearance
+ OBJC_IVAR_$_PKDeviceLockStateObserver._notifyToken
+ OBJC_IVAR_$_PKMetalRenderer._computeVertexBuffer
+ OBJC_IVAR_$_PKMetalRendererController._updateCycleRendererReadySemaphore
+ OBJC_IVAR_$_PKMetalResourceHandlerBuffer._lock
+ OBJC_IVAR_$_PKPaletteBaseColorPickerController._colorAppearance
+ OBJC_IVAR_$_PKPaletteColorPickerView._colorAppearance
+ OBJC_IVAR_$_PKPaletteColorSwatch._colorAppearance
+ OBJC_IVAR_$_PKPaletteMoreOptionsViewController._cornerLocation
+ OBJC_IVAR_$_PKPaletteMoreOptionsViewController._edgeLocation
+ OBJC_IVAR_$_PKPaletteSystemColorPickerController._onlyConvertsBlackAndWhiteInDark
+ OBJC_IVAR_$_PKPaletteToolPickerAndColorPickerView._compactPaletteWidth
+ OBJC_IVAR_$_PKPaletteToolPickerView._colorAppearance
+ OBJC_IVAR_$_PKPaletteToolPreview._colorAppearance
+ OBJC_IVAR_$_PKPaletteToolView._colorAppearance
+ OBJC_IVAR_$_PKSelectionInteraction._keyboardSuppressionPolicyDelegate
+ OBJC_IVAR_$_PKToolPicker.__colorUserInterfaceStyleOnlyConvertsBlackAndWhite
+ _$s7SwiftUI25_AppearanceActionModifierVAA04ViewE0AAMc
+ _$s7SwiftUI25_AppearanceActionModifierVAcA04ViewE0AAWL
+ _$s7SwiftUI25_AppearanceActionModifierVAcA04ViewE0AAWl
+ _$s7SwiftUI25_AppearanceActionModifierVN
+ _$ss5NeverO7SwiftUI4ViewACMc
+ _$ss5NeverOAB7SwiftUI4ViewACWL
+ _$ss5NeverOAB7SwiftUI4ViewACWl
+ _OBJC_CLASS_$_PKDataDetectorRevealHighlighter
+ _OBJC_CLASS_$_PKDeviceLockStateObserver
+ _OBJC_METACLASS_$_PKDataDetectorRevealHighlighter
+ _OBJC_METACLASS_$_PKDeviceLockStateObserver
+ _PKPaletteCompactCornerRadius
+ _PKPaletteCompactToolPickerTopMargin
+ _PKPaletteDragHandleTopMargin
+ _PKPaletteStatusBarEdgeMargin
+ _PKPaletteVerticalBarEdgeMargin
+ _PKPaletteVerticalBarEdgeMarginInHorizontal
+ _PKSmallButtonImageSymbolConfiguration
+ __OBJC_$_CLASS_METHODS_PKDataDetectorRevealHighlighter
+ __OBJC_$_CLASS_PROP_LIST_PKDataDetectorRevealHighlighter
+ __OBJC_$_INSTANCE_METHODS_PKDataDetectorRevealHighlighter
+ __OBJC_$_INSTANCE_METHODS_PKDeviceLockStateObserver
+ __OBJC_$_INSTANCE_VARIABLES_PKDeviceLockStateObserver
+ __OBJC_$_PROP_LIST_PKDataDetectorRevealHighlighter
+ __OBJC_$_PROP_LIST_PKDeviceLockStateObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIRVPresenterHighlightDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UIRVPresenterHighlightDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIRVPresenterHighlightDelegate
+ __OBJC_$_PROTOCOL_REFS_UIRVPresenterHighlightDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PKDataDetectorRevealHighlighter
+ __OBJC_CLASS_PROTOCOLS_$_PKPaletteMoreOptionsViewController
+ __OBJC_CLASS_RO_$_PKDataDetectorRevealHighlighter
+ __OBJC_CLASS_RO_$_PKDeviceLockStateObserver
+ __OBJC_LABEL_PROTOCOL_$_UIRVPresenterHighlightDelegate
+ __OBJC_METACLASS_RO_$_PKDataDetectorRevealHighlighter
+ __OBJC_METACLASS_RO_$_PKDeviceLockStateObserver
+ __OBJC_PROTOCOL_$_UIRVPresenterHighlightDelegate
+ ___52+[PKDataDetectorRevealHighlighter sharedHighlighter]_block_invoke
+ ___62-[PKMetalRendererController updateCyclePreCACommit:isDrawing:]_block_invoke_5
+ ___72+[PKTextInputLanguageSelectionController _transliterationInputModeRules]_block_invoke
+ ___75+[PKTextInputLanguageSelectionController _scriptQualifiedLocaleIdentifiers]_block_invoke
+ ___76-[PKMetalRenderer newComputeVertexBufferWithLength:outOffset:commandBuffer:]_block_invoke
+ ___PKBodyRegularFontSizeInPoints_block_invoke
+ ___block_descriptor_48_ea8_32s40s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
+ ___getkDDHighlighterKeySymbolLoc_block_invoke
+ _notify_cancel
+ _notify_get_state
+ _objc_msgSend$_colorUserInterfaceStyleOnlyConvertsBlackAndWhite
+ _objc_msgSend$_convertColorFromLight:toAppearance:
+ _objc_msgSend$_ensureFirstToolVisibleForRTLIfNeeded
+ _objc_msgSend$_isPureBlackOrWhite:
+ _objc_msgSend$_scriptQualifiedLocaleIdentifiers
+ _objc_msgSend$_setPaletteDockedToHorizontalEdge:
+ _objc_msgSend$_shouldConvertColorPickerColorFromDarkToLight:
+ _objc_msgSend$_transliterationInputModeRules
+ _objc_msgSend$_updateContextMenuAvoidanceRect
+ _objc_msgSend$_usesCompactPaletteWidth
+ _objc_msgSend$colorAppearance
+ _objc_msgSend$colorUserInterfaceStyleOnlyConvertsBlackAndWhite
+ _objc_msgSend$compactPaletteAvailableWidth
+ _objc_msgSend$compactPaletteWidth
+ _objc_msgSend$constant
+ _objc_msgSend$ensureKeyboardLanguageConsistencyIfNeededWhileWriting:
+ _objc_msgSend$groupingLevel
+ _objc_msgSend$initWithSize:options:device:purgeable:initialReusableBufferCount:
+ _objc_msgSend$minimizedPaletteSizeScaleFactor
+ _objc_msgSend$newComputeVertexBufferWithLength:outOffset:commandBuffer:
+ _objc_msgSend$setColorAppearance:
+ _objc_msgSend$setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:
+ _objc_msgSend$setCompactPaletteWidth:
+ _objc_msgSend$setGroupsByEvent:
+ _objc_msgSend$sharedHighlighter
- -[PKColorMatrixView _uiColorUserInterfaceStyle]
- -[PKColorMatrixView colorUserInterfaceStyle]
- -[PKColorMatrixView setColorUserInterfaceStyle:]
- -[PKDrawingPaletteView bottomLineDividerView]
- -[PKDrawingPaletteView setBottomLineDividerView:]
- -[PKInkAttributesPicker colorUserInterfaceStyle]
- -[PKInkAttributesPicker setColorUserInterfaceStyle:]
- -[PKMetalResourceHandler deallocateReusableBuffers]
- -[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]
- -[PKPaletteBaseColorPickerController colorUserInterfaceStyle]
- -[PKPaletteBaseColorPickerController setColorUserInterfaceStyle:]
- -[PKPaletteColorPickerView colorUserInterfaceStyle]
- -[PKPaletteColorPickerView setColorUserInterfaceStyle:]
- -[PKPaletteColorSwatch _uiColorUserInterfaceStyle]
- -[PKPaletteColorSwatch colorUserInterfaceStyle]
- -[PKPaletteColorSwatch setColorUserInterfaceStyle:]
- -[PKPaletteInkingToolView _uiColorUserInterfaceStyle]
- -[PKPaletteStandardColorPickerController colorUserInterfaceStyle]
- -[PKPaletteSystemColorPickerController colorUserInterfaceStyle]
- -[PKPaletteSystemColorPickerController setColorUserInterfaceStyle:]
- -[PKPaletteToolPickerAndColorPickerView didMoveToWindow]
- -[PKPaletteToolPickerAndColorPickerView safeAreaInsetsDidChange]
- -[PKPaletteToolPickerView _ensureCorrectToolSelectionForRTLIfNeeded]
- -[PKPaletteToolPickerView _isAllToolsColorUserInterfaceStyleEqualsTo:]
- -[PKPaletteToolPickerView colorUserInterfaceStyle]
- -[PKPaletteToolPickerView setColorUserInterfaceStyle:]
- -[PKPaletteToolPreview colorUserInterfaceStyle]
- -[PKPaletteToolPreview setColorUserInterfaceStyle:]
- -[PKPaletteToolView colorUserInterfaceStyle]
- -[PKPaletteToolView setColorUserInterfaceStyle:]
- -[PKTextInputLanguageSelectionController ensureKeyboardLanguageConsistencyIfNeeded]
- -[_PKInkAttributesPickerView colorUserInterfaceStyle]
- -[_PKInkAttributesPickerView setColorUserInterfaceStyle:]
- OBJC_IVAR_$_PKColorMatrixView._colorUserInterfaceStyle
- OBJC_IVAR_$_PKMetalResourceHandler._gpuResourceBuffer
- OBJC_IVAR_$_PKPaletteBaseColorPickerController._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteColorPickerView._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteColorSwatch._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteToolPickerView._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteToolPreview._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteToolView._colorUserInterfaceStyle
- _$s7SwiftUI25_AppearanceActionModifierVAA04ViewE0AAWP
- _$ss5NeverO7SwiftUI4ViewACWP
- _PKPaletteCompactHardwareRatio
- _PKToolPickerCompactPillLayoutEnabled
- ___51-[PKMetalResourceHandler deallocateReusableBuffers]_block_invoke
- ___68-[PKPaletteToolPickerView _ensureCorrectToolSelectionForRTLIfNeeded]_block_invoke
- ___73-[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]_block_invoke
- ___73-[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]_block_invoke_2
- ___73-[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]_block_invoke_3
- ___block_descriptor_48_ea8_32s40w_e28_v16?0"<MTLCommandBuffer>"8lw40l8s32l8
- ___block_descriptor_72_ea8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- _objc_msgSend$_ensureCorrectToolSelectionForRTLIfNeeded
- _objc_msgSend$_uiColorUserInterfaceStyle
- _objc_msgSend$bottomLineDividerView
- _objc_msgSend$displayCornerRadius
- _objc_msgSend$ensureKeyboardLanguageConsistencyIfNeeded
- _objc_msgSend$ignoresSafeAreaInsetsInCompactSize
- _objc_msgSend$newGPUBufferWithLength:outOffset:commandBuffer:
- _objc_msgSend$setBottomLineDividerView:
- _objc_msgSend$wantsBottomLineDividerVisibleInCompactSize
CStrings:
+ "LanguageController: Skipping keyboard language propagation while writing."
+ "Skip updating opacity label constraints, vertical offset: %{private}.2f, scaling factor: %{private}.2f"
+ "kDDHighlighterKey"
+ "mr-Translit"
+ "mr_Latn"
+ "\xf0a1"
+ "\xf0q"
+ "\xf0\xe2\x81"
+ "\xf0\xf0\xf0\xf0Q\x92"
- "Graphing"
- "Notes"
- "\xf0q1"
- "\xf0ҁ"
- "\xf0\xf0\xf0\xf0A\x92"
```
