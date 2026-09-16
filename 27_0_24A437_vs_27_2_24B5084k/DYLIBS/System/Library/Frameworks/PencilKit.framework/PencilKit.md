## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-616.100.0.0.0
-  __TEXT.__text: 0x344b00
-  __TEXT.__objc_methlist: 0x26074
-  __TEXT.__const: 0x8ef4
+621.0.0.0.0
+  __TEXT.__text: 0x346338
+  __TEXT.__objc_methlist: 0x2620c
+  __TEXT.__const: 0x8f54
   __TEXT.__dlopen_cstrs: 0x563
   __TEXT.__constg_swiftt: 0x1f2c
   __TEXT.__swift5_typeref: 0x1f06

   __TEXT.__swift5_assocty: 0x728
   __TEXT.__swift5_proto: 0x398
   __TEXT.__swift5_types: 0x1dc
-  __TEXT.__swift5_capture: 0xa9c
-  __TEXT.__cstring: 0xf962
-  __TEXT.__oslogstring: 0xed2f
+  __TEXT.__swift5_capture: 0xacc
+  __TEXT.__cstring: 0xf959
+  __TEXT.__oslogstring: 0xee56
   __TEXT.__swift_as_entry: 0xf0
   __TEXT.__swift_as_cont: 0x218
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x254b8
+  __TEXT.__gcc_except_tab: 0x254f8
   __TEXT.__ustring: 0x23a
-  __TEXT.__unwind_info: 0x128b8
+  __TEXT.__unwind_info: 0x12948
   __TEXT.__eh_frame: 0x2af8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x7010
-  __DATA_CONST.__objc_classlist: 0x1180
+  __DATA_CONST.__objc_classlist: 0x1190
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x7e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x135b0
+  __DATA_CONST.__objc_selrefs: 0x13688
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0xda8
+  __DATA_CONST.__objc_superrefs: 0xdb8
   __DATA_CONST.__objc_arraydata: 0x920
   __DATA_CONST.__got: 0x22c8
-  __AUTH_CONST.__const: 0x85d0
+  __AUTH_CONST.__const: 0x8648
   __AUTH_CONST.__cfstring: 0xe780
-  __AUTH_CONST.__objc_const: 0x48df0
+  __AUTH_CONST.__objc_const: 0x49260
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x460
   __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__auth_got: 0x1e28
-  __AUTH.__objc_data: 0xa698
+  __AUTH_CONST.__auth_got: 0x1e30
+  __AUTH.__objc_data: 0xa738
   __AUTH.__data: 0xc20
-  __DATA.__objc_ivar: 0x2cb8
+  __DATA.__objc_ivar: 0x2cec
   __DATA.__data: 0x6d68
   __DATA.__common: 0x160
-  __DATA_DIRTY.__objc_ivar: 0x115c
+  __DATA_DIRTY.__objc_ivar: 0x116c
   __DATA_DIRTY.__objc_data: 0x1810
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x7c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18461
-  Symbols:   40882
-  CStrings:  3595
+  Functions: 18501
+  Symbols:   40968
+  CStrings:  3600
 
Symbols:
+ +[PKInkingTool _convertColorFromLight:toAppearance:]
+ +[PKInkingTool _isPureBlackOrWhite:]
+ -[PKColorMatrixView colorAppearance]
+ -[PKColorMatrixView setColorAppearance:]
+ -[PKColorPicker colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKColorPicker setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[PKDeviceLockStateObserver dealloc]
+ -[PKDrawingPaletteView colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKDrawingPaletteView setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[PKInkAttributesPicker colorAppearance]
+ -[PKInkAttributesPicker setColorAppearance:]
+ -[PKPaletteBaseColorPickerController colorAppearance]
+ -[PKPaletteBaseColorPickerController setColorAppearance:]
+ -[PKPaletteColorPickerView colorAppearance]
+ -[PKPaletteColorPickerView setColorAppearance:]
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
+ -[PKSqueezePaletteView setColorAppearance:]
+ -[PKSqueezePaletteViewExpandedColorsLayout colorAppearanceDidChange]
+ -[PKSqueezePaletteViewExpandedInkingToolLayout colorAppearanceDidChange]
+ -[PKSqueezePaletteViewExpandedToolsLayout colorAppearanceDidChange]
+ -[PKSqueezePaletteViewMiniPaletteLayout colorAppearanceDidChange]
+ -[PKToolPicker _colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[PKToolPicker _setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[_PKColorAlphaSliderIOS colorUserInterfaceStyleOnlyConvertsBlackAndWhite]
+ -[_PKColorAlphaSliderIOS setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:]
+ -[_PKInkAttributesPickerView colorAppearance]
+ -[_PKInkAttributesPickerView setColorAppearance:]
+ OBJC_IVAR_$_PKPaletteSystemColorPickerController._onlyConvertsBlackAndWhiteInDark
+ _$s9PencilKit33PKSqueezeVisualIntelligenceButton33_37F59D7289F7B321309FA7D662ED2685LLC22updateInteractionStateyyF
+ _$s9PencilKit33PKSqueezeVisualIntelligenceButton33_37F59D7289F7B321309FA7D662ED2685LLC22updateInteractionStateyyFyyXEfU_
+ _$s9PencilKit33PKSqueezeVisualIntelligenceButton33_37F59D7289F7B321309FA7D662ED2685LLC22updateInteractionStateyyFyyXEfU_TA
+ _$sIg_Ieg_TR
+ _OBJC_CLASS_$_PKDeviceLockStateObserver
+ _OBJC_CLASS_$_PKPaletteToolReorderController
+ _OBJC_IVAR_$_PKColorMatrixView._colorAppearance
+ _OBJC_IVAR_$_PKDeviceLockStateObserver._notifyToken
+ _OBJC_IVAR_$_PKMetalRendererController._updateCycleRendererReadySemaphore
+ _OBJC_IVAR_$_PKPaletteBaseColorPickerController._colorAppearance
+ _OBJC_IVAR_$_PKPaletteColorPickerView._colorAppearance
+ _OBJC_IVAR_$_PKPaletteColorSwatch._colorAppearance
+ _OBJC_IVAR_$_PKPaletteToolPickerView._colorAppearance
+ _OBJC_IVAR_$_PKPaletteToolPreview._colorAppearance
+ _OBJC_IVAR_$_PKPaletteToolReorderController._active
+ _OBJC_IVAR_$_PKPaletteToolReorderController._delegate
+ _OBJC_IVAR_$_PKPaletteToolReorderController._dragAllowedCenterRect
+ _OBJC_IVAR_$_PKPaletteToolReorderController._dragDesiredCenter
+ _OBJC_IVAR_$_PKPaletteToolReorderController._dragLiftedSize
+ _OBJC_IVAR_$_PKPaletteToolReorderController._dragTouchOffset
+ _OBJC_IVAR_$_PKPaletteToolReorderController._draggedSnapshotView
+ _OBJC_IVAR_$_PKPaletteToolReorderController._draggedToolView
+ _OBJC_IVAR_$_PKPaletteToolReorderController._longPressGestureRecognizer
+ _OBJC_IVAR_$_PKPaletteToolView._colorAppearance
+ _OBJC_IVAR_$_PKSqueezePaletteColorSwatchButton._colorAppearance
+ _OBJC_IVAR_$_PKSqueezePaletteDrawingTool._colorAppearance
+ _OBJC_IVAR_$_PKSqueezePaletteMulticolorSwatchButton._colorAppearance
+ _OBJC_IVAR_$_PKSqueezePaletteView._colorAppearance
+ _OBJC_IVAR_$_PKToolPicker.__colorUserInterfaceStyleOnlyConvertsBlackAndWhite
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
+ _objc_msgSend$colorAppearanceDidChange
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
- -[PKSqueezePaletteView setColorUserInterfaceStyle:]
- -[PKSqueezePaletteViewExpandedColorsLayout colorUserInterfaceStyleDidChange]
- -[PKSqueezePaletteViewExpandedInkingToolLayout colorUserInterfaceStyleDidChange]
- -[PKSqueezePaletteViewExpandedToolsLayout colorUserInterfaceStyleDidChange]
- -[PKSqueezePaletteViewMiniPaletteLayout colorUserInterfaceStyleDidChange]
- -[_PKInkAttributesPickerView colorUserInterfaceStyle]
- -[_PKInkAttributesPickerView setColorUserInterfaceStyle:]
- _$s9PencilKit33PKSqueezeVisualIntelligenceButton33_37F59D7289F7B321309FA7D662ED2685LLC13isHighlightedSbvs
- _$s9PencilKit33PKSqueezeVisualIntelligenceButton33_37F59D7289F7B321309FA7D662ED2685LLC22updateInteractionStateyyFyycfU_
- _$s9PencilKit33PKSqueezeVisualIntelligenceButton33_37F59D7289F7B321309FA7D662ED2685LLC22updateInteractionStateyyFyycfU_TA
- _OBJC_IVAR_$_PKColorMatrixView._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKPaletteBaseColorPickerController._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKPaletteColorPickerView._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKPaletteColorSwatch._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKPaletteToolPickerView._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKPaletteToolPreview._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKPaletteToolView._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKSqueezePaletteColorSwatchButton._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKSqueezePaletteDrawingTool._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKSqueezePaletteMulticolorSwatchButton._colorUserInterfaceStyle
- _OBJC_IVAR_$_PKSqueezePaletteView._colorUserInterfaceStyle
- _objc_msgSend$_uiColorUserInterfaceStyle
- _objc_msgSend$colorUserInterfaceStyleDidChange
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:419: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:442: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:446: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:509: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/list:1500: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "Couldn't snapshot the tool being dragged; falling back to a placeholder."
+ "Did begin dragging a tool."
+ "Did begin reordering tools."
+ "Did end reordering tools."
+ "Reordering refused by the delegate."
+ "Skip updating opacity label constraints, vertical offset: %{private}.2f, scaling factor: %{private}.2f"
+ "Update palette UI style: %{private}ld, color appearance: %{private}ld"
+ "\xf0!"
+ "\xf0\xf0\xf0\xf0\x81\x92"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:419: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:442: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:446: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:509: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:1500: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "Graphing"
- "Notes"
- "Update palette UI style: %{private}ld, color UI style: %{private}ld"
- "\xf0\xf0\xf0\xf0q\x92"
```
