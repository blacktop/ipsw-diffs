## Photo Booth

> `/System/Library/AccessibilityBundles/Photo Booth.axbundle/Photo Booth`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x13e4
-  __TEXT.__objc_methlist: 0x1e4
+3048.0.0.0.0
+  __TEXT.__text: 0x1cbc
+  __TEXT.__objc_methlist: 0x248
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x6ce
-  __TEXT.__unwind_info: 0xe0
+  __TEXT.__gcc_except_tab: 0x44
+  __TEXT.__cstring: 0x7fe
+  __TEXT.__unwind_info: 0x120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__objc_selrefs: 0x228
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__cfstring: 0x8e0
   __AUTH_CONST.__objc_const: 0x550
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 37
-  Symbols:   175
-  CStrings:  72
+  Functions: 50
+  Symbols:   213
+  CStrings:  89
 
Symbols:
+ +[PBShelfTileAccessibility _accessibilityPerformValidations:]
+ -[PBControllerAccessibility _axInstallPhotoActionLabelBlocks]
+ -[PBControllerAccessibility _axLabelForPhotoActionWithFormatKey:]
+ -[PBControllerAccessibility _axValueForFlipButton]
+ -[PBControllerAccessibility _removeTilesAtIndices:animated:]
+ -[PBShelfTileAccessibility _axIsPhotoSelected]
+ -[PBShelfTileAccessibility accessibilityHint]
+ -[PBShelfTileAccessibility animatePrinting:]
+ GCC_except_table15
+ GCC_except_table19
+ _AXPerformBlockOnMainThreadAfterDelay
+ _UIAccessibilitySpeakAndDoNotBeInterrupted
+ __Unwind_Resume
+ ___42-[PBControllerAccessibility toggleCamera:]_block_invoke
+ ___44-[PBShelfTileAccessibility animatePrinting:]_block_invoke
+ ___61-[PBControllerAccessibility _axInstallPhotoActionLabelBlocks]_block_invoke
+ ___61-[PBControllerAccessibility _axInstallPhotoActionLabelBlocks]_block_invoke_2
+ ___71-[PBControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e15_"NSString"8?0lw32l8
+ ___objc_personality_v0
+ __dispatch_main_q
+ _dispatch_after
+ _dispatch_time
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_axInstallPhotoActionLabelBlocks
+ _objc_msgSend$_axIsPhotoSelected
+ _objc_msgSend$_axLabelForPhotoActionWithFormatKey:
+ _objc_msgSend$_axValueForFlipButton
+ _objc_msgSend$_setAccessibilityLabelBlock:
+ _objc_msgSend$_setAccessibilityValueBlock:
+ _objc_msgSend$accessibilityLabel
+ _objc_msgSend$lastObject
+ _objc_msgSend$length
+ _objc_msgSend$safeArrayForKey:
+ _objc_msgSend$safeBoolForKey:
- _objc_msgSend$boolValue
CStrings:
+ "@\"NSString\"8@?0"
+ "NSMutableArray"
+ "_deleteButton"
+ "_highlightedTile"
+ "_removeTilesAtIndices:animated:"
+ "_shareButton"
+ "_tiles"
+ "animatePrinting:"
+ "camera.chooser.back.value"
+ "camera.chooser.button.label"
+ "camera.chooser.front.value"
+ "delete.photo.label"
+ "isReviewed"
+ "photo.select.hint"
+ "photo.unselect.hint"
+ "share.photo.label"
+ "v8@?0"
```
