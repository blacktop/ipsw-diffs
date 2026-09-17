## PencilKit

> `/System/iOSSupport/System/Library/Frameworks/PencilKit.framework/Versions/A/PencilKit`

```diff

-616.0.0.0.0
-  __TEXT.__text: 0x3193dc
-  __TEXT.__objc_methlist: 0x2e3a4
-  __TEXT.__const: 0x8a44
+621.0.0.0.0
+  __TEXT.__text: 0x31aa60
+  __TEXT.__objc_methlist: 0x2e53c
+  __TEXT.__const: 0x8a94
   __TEXT.__dlopen_cstrs: 0x351
   __TEXT.__constg_swiftt: 0x1d40
   __TEXT.__swift5_typeref: 0x1e02

   __TEXT.__swift5_assocty: 0x6e0
   __TEXT.__swift5_proto: 0x388
   __TEXT.__swift5_types: 0x1c0
-  __TEXT.__cstring: 0xc943
+  __TEXT.__cstring: 0xc93a
   __TEXT.__swift5_capture: 0xa30
-  __TEXT.__oslogstring: 0xc94c
+  __TEXT.__oslogstring: 0xca71
   __TEXT.__swift_as_entry: 0xf0
   __TEXT.__swift_as_cont: 0x218
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x260f8
+  __TEXT.__gcc_except_tab: 0x26138
   __TEXT.__ustring: 0x23a
-  __TEXT.__unwind_info: 0x12c38
+  __TEXT.__unwind_info: 0x12cc0
   __TEXT.__eh_frame: 0x2af8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x6860
-  __DATA_CONST.__objc_classlist: 0x1008
+  __DATA_CONST.__objc_classlist: 0x1018
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x770
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x17df0
+  __DATA_CONST.__objc_selrefs: 0x17ec8
   __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0xc60
+  __DATA_CONST.__objc_superrefs: 0xc70
   __DATA_CONST.__objc_arraydata: 0x918
   __DATA_CONST.__got: 0x2058
   __AUTH_CONST.__const: 0x7e80
   __AUTH_CONST.__cfstring: 0xe000
-  __AUTH_CONST.__objc_const: 0x476e0
+  __AUTH_CONST.__objc_const: 0x47b40
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x8b8
   __AUTH_CONST.__objc_arrayobj: 0x6a8
   __AUTH_CONST.__objc_dictobj: 0x460
   __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__auth_got: 0x1c78
-  __AUTH.__objc_data: 0x97d8
+  __AUTH_CONST.__auth_got: 0x1c80
+  __AUTH.__objc_data: 0x9878
   __AUTH.__data: 0xb80
-  __DATA.__objc_ivar: 0x2808
+  __DATA.__objc_ivar: 0x283c
   __DATA.__data: 0x6540
   __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_ivar: 0x10c0
+  __DATA_DIRTY.__objc_ivar: 0x10d0
   __DATA_DIRTY.__objc_data: 0x1630
   __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0x900

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 19483
-  Symbols:   43219
-  CStrings:  3293
+  Functions: 19518
+  Symbols:   43304
+  CStrings:  3298
 
Symbols:
+ +[PKInkingTool _convertColorFromLight:toAppearance:]
+ +[PKInkingTool _isPureBlackOrWhite:]
+ -[PKColorMatrixView colorAppearance]
+ -[PKColorMatrixView setColorAppearance:]
+ -[PKColorPicker colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKColorPicker setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[PKDeviceLockStateObserver dealloc]
+ -[PKDeviceLockStateObserver initWithHandler:]
+ -[PKDrawingPaletteView colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKDrawingPaletteView setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[PKInkAttributesPicker colorAppearance]
+ -[PKInkAttributesPicker setColorAppearance:]
+ -[PKPaletteBaseColorPickerController colorAppearance]
+ -[PKPaletteBaseColorPickerController setColorAppearance:]
+ -[PKPaletteColorPickerView colorAppearance]
+ -[PKPaletteColorPickerView setColorAppearance:]
+ -[PKPaletteColorSwatch colorAppearance]
+ -[PKPaletteColorSwatch setColorAppearance:]
+ -[PKPaletteHostView _updateContextMenuAvoidanceRect]
+ -[PKPaletteStandardColorPickerController colorAppearance]
+ -[PKPaletteSystemColorPickerController _shouldConvertColorPickerColorFromDarkToLight:]
+ -[PKPaletteSystemColorPickerController colorAppearance]
+ -[PKPaletteSystemColorPickerController setColorAppearance:]
+ -[PKPaletteToolPickerView _isAllToolsColorAppearanceEqualsTo:]
+ -[PKPaletteToolPickerView colorAppearance]
+ -[PKPaletteToolPickerView setColorAppearance:]
+ -[PKPaletteToolPreview colorAppearance]
+ -[PKPaletteToolPreview setColorAppearance:]
+ -[PKPaletteToolReorderController .cxx_destruct]
+ -[PKPaletteToolReorderController _allowedCenterRectForVisibleToolsRect:liftedSize:]
+ -[PKPaletteToolReorderController _beginDraggingToolView:atLocation:]
+ -[PKPaletteToolReorderController _containerLocationOfRecognizer:]
+ -[PKPaletteToolReorderController _draggedToolCenter]
+ -[PKPaletteToolReorderController _endDragAnimated:]
+ -[PKPaletteToolReorderController _endReordering]
+ -[PKPaletteToolReorderController _longPressGestureHandler:]
+ -[PKPaletteToolReorderController _reorderableToolViewAtLocationOfRecognizer:]
+ -[PKPaletteToolReorderController _updateDragAtLocation:]
+ -[PKPaletteToolReorderController beginReordering]
+ -[PKPaletteToolReorderController delegate]
+ -[PKPaletteToolReorderController endReorderingAnimated:]
+ -[PKPaletteToolReorderController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[PKPaletteToolReorderController gestureRecognizerShouldBegin:]
+ -[PKPaletteToolReorderController initWithDelegate:]
+ -[PKPaletteToolReorderController isActive]
+ -[PKPaletteToolReorderController isDragging]
+ -[PKPaletteToolReorderController longPressGestureRecognizer]
+ -[PKPaletteToolView colorAppearance]
+ -[PKPaletteToolView setColorAppearance:]
+ -[PKToolPicker _colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKToolPicker _setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[_PKColorAlphaSliderIOS colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[_PKColorAlphaSliderIOS setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[_PKInkAttributesPickerView colorAppearance]
+ -[_PKInkAttributesPickerView setColorAppearance:]
+ OBJC_IVAR_$_PKColorMatrixView._colorAppearance
+ OBJC_IVAR_$_PKDeviceLockStateObserver._notifyToken
+ OBJC_IVAR_$_PKMetalRendererController._updateCycleRendererReadySemaphore
+ OBJC_IVAR_$_PKPaletteBaseColorPickerController._colorAppearance
+ OBJC_IVAR_$_PKPaletteColorPickerView._colorAppearance
+ OBJC_IVAR_$_PKPaletteColorSwatch._colorAppearance
+ OBJC_IVAR_$_PKPaletteSystemColorPickerController._onlyConvertsBlackAndWhiteInDark
+ OBJC_IVAR_$_PKPaletteToolPickerView._colorAppearance
+ OBJC_IVAR_$_PKPaletteToolPreview._colorAppearance
+ OBJC_IVAR_$_PKPaletteToolReorderController._active
+ OBJC_IVAR_$_PKPaletteToolReorderController._delegate
+ OBJC_IVAR_$_PKPaletteToolReorderController._dragAllowedCenterRect
+ OBJC_IVAR_$_PKPaletteToolReorderController._dragDesiredCenter
+ OBJC_IVAR_$_PKPaletteToolReorderController._dragLiftedSize
+ OBJC_IVAR_$_PKPaletteToolReorderController._dragTouchOffset
+ OBJC_IVAR_$_PKPaletteToolReorderController._draggedSnapshotView
+ OBJC_IVAR_$_PKPaletteToolReorderController._draggedToolView
+ OBJC_IVAR_$_PKPaletteToolReorderController._longPressGestureRecognizer
+ OBJC_IVAR_$_PKPaletteToolView._colorAppearance
+ OBJC_IVAR_$_PKToolPicker.__colorUserInterfaceStyleOnlyConvertsBlackAndWhite
+ _OBJC_CLASS_$_PKDeviceLockStateObserver
+ _OBJC_CLASS_$_PKPaletteToolReorderController
+ _OBJC_METACLASS_$_PKDeviceLockStateObserver
+ _OBJC_METACLASS_$_PKPaletteToolReorderController
+ __OBJC_$_INSTANCE_METHODS_PKDeviceLockStateObserver
+ __OBJC_$_INSTANCE_METHODS_PKPaletteToolReorderController
+ __OBJC_$_INSTANCE_VARIABLES_PKDeviceLockStateObserver
+ __OBJC_$_INSTANCE_VARIABLES_PKPaletteToolReorderController
+ __OBJC_$_PROP_LIST_PKPaletteToolReorderController
+ __OBJC_CLASS_PROTOCOLS_$_PKPaletteToolReorderController
+ __OBJC_CLASS_RO_$_PKDeviceLockStateObserver
+ __OBJC_CLASS_RO_$_PKPaletteToolReorderController
+ __OBJC_METACLASS_RO_$_PKDeviceLockStateObserver
+ __OBJC_METACLASS_RO_$_PKPaletteToolReorderController
+ ___51-[PKPaletteToolReorderController _endDragAnimated:]_block_invoke
+ ___51-[PKPaletteToolReorderController _endDragAnimated:]_block_invoke_2
+ ___51-[PKPaletteToolReorderController _endDragAnimated:]_block_invoke_3
+ ___62-[PKMetalRendererController updateCyclePreCACommit:isDrawing:]_block_invoke_5
+ ___68-[PKPaletteToolReorderController _beginDraggingToolView:atLocation:]_block_invoke
+ _notify_cancel
+ _objc_msgSend$_allowedCenterRectForVisibleToolsRect:liftedSize:
+ _objc_msgSend$_beginDraggingToolView:atLocation:
+ _objc_msgSend$_colorUserInterfaceStyleOnlyConvertsBlackAndWhite
+ _objc_msgSend$_containerLocationOfRecognizer:
+ _objc_msgSend$_convertColorFromLight:toAppearance:
+ _objc_msgSend$_endDragAnimated:
+ _objc_msgSend$_endReordering
+ _objc_msgSend$_isPureBlackOrWhite:
+ _objc_msgSend$_reorderableToolViewAtLocationOfRecognizer:
+ _objc_msgSend$_shouldConvertColorPickerColorFromDarkToLight:
+ _objc_msgSend$_updateContextMenuAvoidanceRect
+ _objc_msgSend$_updateDragAtLocation:
+ _objc_msgSend$beginReordering
+ _objc_msgSend$colorAppearance
+ _objc_msgSend$colorUserInterfaceStyleOnlyConvertsBlackAndWhite
+ _objc_msgSend$dragContainerViewForReorderController:
+ _objc_msgSend$reorderControllerDidChangeActive:
+ _objc_msgSend$reorderControllerShouldBeginReordering:
+ _objc_msgSend$reorderableToolViewsForReorderController:
+ _objc_msgSend$setColorAppearance:
+ _objc_msgSend$setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:
+ _objc_msgSend$snapshotViewAfterScreenUpdates:
+ _objc_msgSend$visibleToolsRectForReorderController:
- -[PKColorMatrixView _uiColorUserInterfaceStyle]
- -[PKColorMatrixView colorUserInterfaceStyle]
- -[PKColorMatrixView setColorUserInterfaceStyle:]
- -[PKInkAttributesPicker colorUserInterfaceStyle]
- -[PKInkAttributesPicker setColorUserInterfaceStyle:]
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
- -[PKPaletteToolPickerView _isAllToolsColorUserInterfaceStyleEqualsTo:]
- -[PKPaletteToolPickerView colorUserInterfaceStyle]
- -[PKPaletteToolPickerView setColorUserInterfaceStyle:]
- -[PKPaletteToolPreview colorUserInterfaceStyle]
- -[PKPaletteToolPreview setColorUserInterfaceStyle:]
- -[PKPaletteToolView colorUserInterfaceStyle]
- -[PKPaletteToolView setColorUserInterfaceStyle:]
- -[_PKInkAttributesPickerView colorUserInterfaceStyle]
- -[_PKInkAttributesPickerView setColorUserInterfaceStyle:]
- OBJC_IVAR_$_PKColorMatrixView._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteBaseColorPickerController._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteColorPickerView._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteColorSwatch._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteToolPickerView._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteToolPreview._colorUserInterfaceStyle
- OBJC_IVAR_$_PKPaletteToolView._colorUserInterfaceStyle
- _objc_msgSend$_uiColorUserInterfaceStyle
CStrings:
+ "Couldn't snapshot the tool being dragged; falling back to a placeholder."
+ "Did begin dragging a tool."
+ "Did begin reordering tools."
+ "Did end reordering tools."
+ "Reordering refused by the delegate."
+ "Skip updating opacity label constraints, vertical offset: %{private}.2f, scaling factor: %{private}.2f"
+ "\xf0!"
+ "\xf0\xf0\xf0\xf0Q\x92"
- "Graphing"
- "Notes"
- "\xf0\xf0\xf0\xf0A\x92"
```
