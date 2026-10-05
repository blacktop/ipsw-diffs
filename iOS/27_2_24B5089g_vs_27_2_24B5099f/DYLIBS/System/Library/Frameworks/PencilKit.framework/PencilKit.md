## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-621.0.0.0.0
-  __TEXT.__text: 0x346338
-  __TEXT.__objc_methlist: 0x2620c
-  __TEXT.__const: 0x8f54
+622.1.1.0.0
+  __TEXT.__text: 0x345d50
+  __TEXT.__objc_methlist: 0x26184
+  __TEXT.__const: 0x8f64
   __TEXT.__dlopen_cstrs: 0x563
   __TEXT.__constg_swiftt: 0x1f2c
   __TEXT.__swift5_typeref: 0x1f06

   __TEXT.__swift5_proto: 0x398
   __TEXT.__swift5_types: 0x1dc
   __TEXT.__swift5_capture: 0xacc
-  __TEXT.__cstring: 0xf959
-  __TEXT.__oslogstring: 0xee56
+  __TEXT.__cstring: 0xf96b
+  __TEXT.__oslogstring: 0xedff
   __TEXT.__swift_as_entry: 0xf0
   __TEXT.__swift_as_cont: 0x218
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x254f8
+  __TEXT.__gcc_except_tab: 0x2559c
   __TEXT.__ustring: 0x23a
-  __TEXT.__unwind_info: 0x12948
+  __TEXT.__unwind_info: 0x12910
   __TEXT.__eh_frame: 0x2af8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7010
-  __DATA_CONST.__objc_classlist: 0x1190
+  __DATA_CONST.__const: 0x6fe8
+  __DATA_CONST.__objc_classlist: 0x1188
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x7e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x13688
+  __DATA_CONST.__objc_selrefs: 0x13648
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0xdb8
-  __DATA_CONST.__objc_arraydata: 0x920
+  __DATA_CONST.__objc_superrefs: 0xdb0
+  __DATA_CONST.__objc_arraydata: 0x958
   __DATA_CONST.__got: 0x22c8
-  __AUTH_CONST.__const: 0x8648
-  __AUTH_CONST.__cfstring: 0xe780
-  __AUTH_CONST.__objc_const: 0x49260
+  __AUTH_CONST.__const: 0x8668
+  __AUTH_CONST.__cfstring: 0xe7c0
+  __AUTH_CONST.__objc_const: 0x490c0
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x918
-  __AUTH_CONST.__objc_arrayobj: 0x6c0
-  __AUTH_CONST.__objc_dictobj: 0x460
+  __AUTH_CONST.__objc_arrayobj: 0x6d8
+  __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__auth_got: 0x1e30
-  __AUTH.__objc_data: 0xa6d0
+  __AUTH.__objc_data: 0xa680
   __AUTH.__data: 0xbf8
-  __DATA.__objc_ivar: 0x2cec
+  __DATA.__objc_ivar: 0x2cd0
   __DATA.__data: 0x6d90
   __DATA.__common: 0x160
-  __DATA_DIRTY.__objc_ivar: 0x116c
+  __DATA_DIRTY.__objc_ivar: 0x1170
   __DATA_DIRTY.__objc_data: 0x1878
   __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x7c0
+  __DATA_DIRTY.__bss: 0x7e0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18501
-  Symbols:   33163
-  CStrings:  3600
+  Functions: 18484
+  Symbols:   33130
+  CStrings:  3599
 
Symbols:
+ +[PKTextInputLanguageSelectionController _scriptQualifiedLocaleIdentifiers]
+ +[PKTextInputLanguageSelectionController _transliterationInputModeRules]
+ -[PKDrawingPaletteView _contentViewForTesting]
+ -[PKDrawingPaletteView _toolPickerViewForTesting]
+ -[PKMetalRenderer newComputeVertexBufferWithLength:outOffset:commandBuffer:]
+ -[PKMetalResourceHandlerBuffer deallocateReusableBuffers]
+ -[PKMetalResourceHandlerBuffer initWithSize:options:device:purgeable:initialReusableBufferCount:]
+ -[PKPaletteHostView _usesCompactPaletteWidth]
+ -[PKPaletteHostView compactPaletteAvailableWidth]
+ -[PKPaletteToolPickerAndColorPickerView compactPaletteWidth]
+ -[PKPaletteToolPickerAndColorPickerView setCompactPaletteWidth:]
+ -[PKPaletteToolPickerView _ensureFirstToolVisibleForRTLIfNeeded]
+ -[PKPaletteView compactPaletteWidth]
+ -[PKTextInputLanguageSelectionController ensureKeyboardLanguageConsistencyIfNeededWhileWriting:]
+ _OBJC_IVAR_$_PKMetalRenderer._computeVertexBuffer
+ _OBJC_IVAR_$_PKMetalResourceHandlerBuffer._lock
+ _OBJC_IVAR_$_PKPaletteToolPickerAndColorPickerView._compactPaletteWidth
+ ___72+[PKTextInputLanguageSelectionController _transliterationInputModeRules]_block_invoke
+ ___75+[PKTextInputLanguageSelectionController _scriptQualifiedLocaleIdentifiers]_block_invoke
+ ___76-[PKMetalRenderer newComputeVertexBufferWithLength:outOffset:commandBuffer:]_block_invoke
+ ___block_descriptor_48_ea8_32s40s_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
- -[PKMetalResourceHandler deallocateReusableBuffers]
- -[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]
- -[PKPaletteToolPickerAndColorPickerView didMoveToWindow]
- -[PKPaletteToolPickerAndColorPickerView safeAreaInsetsDidChange]
- -[PKPaletteToolPickerView _ensureCorrectToolSelectionForRTLIfNeeded]
- -[PKPaletteToolReorderController .cxx_destruct]
- -[PKPaletteToolReorderController _allowedCenterRectForVisibleToolsRect:liftedSize:]
- -[PKPaletteToolReorderController _beginDraggingToolView:atLocation:]
- -[PKPaletteToolReorderController _containerLocationOfRecognizer:]
- -[PKPaletteToolReorderController _draggedToolCenter]
- -[PKPaletteToolReorderController _endDragAnimated:]
- -[PKPaletteToolReorderController _endReordering]
- -[PKPaletteToolReorderController _longPressGestureHandler:]
- -[PKPaletteToolReorderController _reorderableToolViewAtLocationOfRecognizer:]
- -[PKPaletteToolReorderController _updateDragAtLocation:]
- -[PKPaletteToolReorderController beginReordering]
- -[PKPaletteToolReorderController delegate]
- -[PKPaletteToolReorderController endReorderingAnimated:]
- -[PKPaletteToolReorderController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
- -[PKPaletteToolReorderController gestureRecognizerShouldBegin:]
- -[PKPaletteToolReorderController initWithDelegate:]
- -[PKPaletteToolReorderController isActive]
- -[PKPaletteToolReorderController isDragging]
- -[PKPaletteToolReorderController longPressGestureRecognizer]
- -[PKTextInputLanguageSelectionController ensureKeyboardLanguageConsistencyIfNeeded]
- _OBJC_CLASS_$_PKPaletteToolReorderController
- _OBJC_IVAR_$_PKMetalResourceHandler._gpuResourceBuffer
- _OBJC_IVAR_$_PKPaletteToolReorderController._active
- _OBJC_IVAR_$_PKPaletteToolReorderController._delegate
- _OBJC_IVAR_$_PKPaletteToolReorderController._dragAllowedCenterRect
- _OBJC_IVAR_$_PKPaletteToolReorderController._dragDesiredCenter
- _OBJC_IVAR_$_PKPaletteToolReorderController._dragLiftedSize
- _OBJC_IVAR_$_PKPaletteToolReorderController._dragTouchOffset
- _OBJC_IVAR_$_PKPaletteToolReorderController._draggedSnapshotView
- _OBJC_IVAR_$_PKPaletteToolReorderController._draggedToolView
- _OBJC_IVAR_$_PKPaletteToolReorderController._longPressGestureRecognizer
- _OBJC_METACLASS_$_PKPaletteToolReorderController
- __OBJC_$_INSTANCE_METHODS_PKPaletteToolReorderController
- __OBJC_$_INSTANCE_VARIABLES_PKPaletteToolReorderController
- __OBJC_$_PROP_LIST_PKPaletteToolReorderController
- __OBJC_CLASS_PROTOCOLS_$_PKPaletteToolReorderController
- __OBJC_CLASS_RO_$_PKPaletteToolReorderController
- __OBJC_METACLASS_RO_$_PKPaletteToolReorderController
- ___51-[PKMetalResourceHandler deallocateReusableBuffers]_block_invoke
- ___51-[PKPaletteToolReorderController _endDragAnimated:]_block_invoke
- ___51-[PKPaletteToolReorderController _endDragAnimated:]_block_invoke_2
- ___51-[PKPaletteToolReorderController _endDragAnimated:]_block_invoke_3
- ___68-[PKPaletteToolPickerView _ensureCorrectToolSelectionForRTLIfNeeded]_block_invoke
- ___68-[PKPaletteToolReorderController _beginDraggingToolView:atLocation:]_block_invoke
- ___73-[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]_block_invoke
- ___73-[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]_block_invoke_2
- ___73-[PKMetalResourceHandler newGPUBufferWithLength:outOffset:commandBuffer:]_block_invoke_3
- ___block_descriptor_48_ea8_32s40w_e28_v16?0"<MTLCommandBuffer>"8lw40l8s32l8
- ___block_descriptor_72_ea8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
CStrings:
+ "Campo not supported on phone"
+ "LanguageController: Skipping keyboard language propagation while writing."
+ "mr-Translit"
+ "mr_Latn"
+ "\xf0a"
- "Couldn't snapshot the tool being dragged; falling back to a placeholder."
- "Did begin dragging a tool."
- "Did begin reordering tools."
- "Did end reordering tools."
- "Reordering refused by the delegate."
- "\xf0!"
```
