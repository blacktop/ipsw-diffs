## Pegasus

> `/System/Library/PrivateFrameworks/Pegasus.framework/Pegasus`

```diff

-299.102.0.0.0
-  __TEXT.__text: 0x43604
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x44a4
-  __TEXT.__const: 0x212
-  __TEXT.__cstring: 0x469e
+301.0.0.0.0
+  __TEXT.__text: 0x4336c
+  __TEXT.__auth_stubs: 0x9d0
+  __TEXT.__objc_methlist: 0x44b4
+  __TEXT.__const: 0x20a
+  __TEXT.__cstring: 0x46ae
   __TEXT.__oslogstring: 0x1acc
   __TEXT.__gcc_except_tab: 0x5e4
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__swift5_typeref: 0x1c
-  __TEXT.__swift5_capture: 0x24
-  __TEXT.__unwind_info: 0x1440
+  __TEXT.__unwind_info: 0x1428
   __TEXT.__objc_classname: 0x8d7
-  __TEXT.__objc_methname: 0xdcfd
-  __TEXT.__objc_methtype: 0x281d
-  __TEXT.__objc_stubs: 0x9240
-  __DATA_CONST.__got: 0x440
+  __TEXT.__objc_methname: 0xdcfc
+  __TEXT.__objc_methtype: 0x27ed
+  __TEXT.__objc_stubs: 0x92c0
+  __DATA_CONST.__got: 0x448
   __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c10
+  __DATA_CONST.__objc_selrefs: 0x2c30
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__auth_got: 0x558
-  __AUTH_CONST.__const: 0x458
+  __AUTH_CONST.__auth_got: 0x4f8
+  __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x2e40
-  __AUTH_CONST.__objc_const: 0xaaf0
+  __AUTH_CONST.__objc_const: 0xaa68
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x5a8
-  __DATA.__data: 0x970
+  __DATA.__objc_ivar: 0x5ac
+  __DATA.__data: 0x968
   __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 61E2B880-47E7-30A7-B760-8CACF7B247CC
-  Functions: 1724
-  Symbols:   6564
-  CStrings:  3330
+  UUID: 0EC3D335-ED05-309A-971C-597AFC960584
+  Functions: 1718
+  Symbols:   6556
+  CStrings:  3334
 
Symbols:
+ +[PGCABackdropLayerView baseFilters]
+ +[PGCABackdropLayerView baseFilters].cold.1
+ +[PGControlsViewLayoutMetrics concentricCornerRadiusForViewSize:]
+ +[PGControlsViewLayoutMetrics defaultActionButtonGlyphSize]
+ +[PGControlsViewLayoutMetrics defaultActionButtonSize]
+ +[PGControlsViewLayoutMetrics defaultControlsViewPadding]
+ +[PGControlsViewLayoutMetrics defaultPrerollIndicatorHeight]
+ +[PGControlsViewLayoutMetrics defaultPrerollLiveIndicatorPadding]
+ +[PGControlsViewLayoutMetrics defaultProgressIndicatorCompleteTrackPadding]
+ +[PGControlsViewLayoutMetrics defaultProgressIndicatorHeight]
+ +[PGControlsViewLayoutMetrics defaultRestoreCancelButtonsGlyphSize]
+ +[PGControlsViewLayoutMetrics defaultRestoreCancelButtonsSize]
+ +[PGControlsViewLayoutMetrics defaultSkipButtonsGlyphSize]
+ +[PGControlsViewLayoutMetrics defaultSkipButtonsSize]
+ +[PGControlsViewLayoutMetrics scaleForViewSize:]
+ +[PGControlsViewLayoutMetrics spacingScaleForViewSize:]
+ -[PGCABackdropLayerView initWithFrame:captureOnly:]
+ -[PGCABackdropLayerView initWithFrame:wantsGlassBackground:]
+ -[PGCABackdropLayerView setWantsBlur:]
+ -[PGCABackdropLayerView wantsBlur]
+ GCC_except_table23
+ _OBJC_IVAR_$_PGCABackdropLayerView._wantsBlur
+ ___36+[PGCABackdropLayerView baseFilters]_block_invoke
+ ___block_literal_global.25
+ ___block_literal_global.4
+ _baseFilters.baseFilters
+ _baseFilters.onceToken
+ _kCAFilterSDRNormalize
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$baseFilters
+ _objc_msgSend$initWithFrame:captureOnly:
+ _objc_msgSend$scaleForViewSize:
+ _objc_msgSend$setOpacity:
+ _objc_msgSend$setWantsBlur:
+ _objc_msgSend$spacingScaleForViewSize:
+ _objc_msgSend$wantsBlur
- +[PGControlsViewLayoutMetrics sharedInstance]
- -[PGCABackdropLayerView initWithFrame:captureOnly:wantsGlassBackground:]
- -[PGControlsViewLayoutMetrics _currentScaleForViewSize:]
- -[PGControlsViewLayoutMetrics adjustedControlsAndPaddingScaleForViewSize:]
- -[PGControlsViewLayoutMetrics adjustedSpacingScaleForViewSize:]
- -[PGControlsViewLayoutMetrics concentricCornerRadiusForViewSize:]
- -[PGControlsViewLayoutMetrics defaultActionButtonGlyphSize]
- -[PGControlsViewLayoutMetrics defaultActionButtonSize]
- -[PGControlsViewLayoutMetrics defaultControlsViewPadding]
- -[PGControlsViewLayoutMetrics defaultPrerollIndicatorHeight]
- -[PGControlsViewLayoutMetrics defaultPrerollLiveIndicatorPadding]
- -[PGControlsViewLayoutMetrics defaultProgressIndicatorCompleteTrackPadding]
- -[PGControlsViewLayoutMetrics defaultProgressIndicatorHeight]
- -[PGControlsViewLayoutMetrics defaultRestoreCancelButtonsGlyphSize]
- -[PGControlsViewLayoutMetrics defaultRestoreCancelButtonsSize]
- -[PGControlsViewLayoutMetrics defaultSkipButtonsGlyphSize]
- -[PGControlsViewLayoutMetrics defaultSkipButtonsSize]
- GCC_except_table19
- __Block_copy
- __Block_release
- __OBJC_$_INSTANCE_METHODS_PGControlsViewLayoutMetrics
- __OBJC_$_PROP_LIST_PGControlsViewLayoutMetrics
- ___45+[PGControlsViewLayoutMetrics sharedInstance]_block_invoke
- ___block_literal_global.21
- ___swift_instantiateConcreteTypeFromMangledName
- _block_copy_helper
- _block_descriptor
- _block_destroy_helper
- _objc_msgSend$_currentScaleForViewSize:
- _objc_msgSend$adjustedControlsAndPaddingScaleForViewSize:
- _objc_msgSend$adjustedSpacingScaleForViewSize:
- _objc_msgSend$initWithFrame:captureOnly:wantsGlassBackground:
- _objc_opt_self
- _sharedInstance.onceToken
- _sharedInstance.sharedInstance
- _swift_allocObject
- _swift_deallocObject
- _swift_getTypeByMangledNameInContext2
- _swift_isEscapingClosureAtFileLocation
- _swift_retain
- _symbolic Ig_
- _symbolic Sb
- _symbolic So6UIViewC
- _symbolic _____Sg 5UIKit29_UICornerMaskingConfigurationV
CStrings:
+ "TB,N,V_wantsBlur"
+ "_wantsBlur"
+ "addObjectsFromArray:"
+ "baseFilters"
+ "initWithFrame:captureOnly:"
+ "scaleForViewSize:"
+ "setOpacity:"
+ "setWantsBlur:"
+ "spacingScaleForViewSize:"
+ "wantsBlur"
- "@56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16B48B52"
- "T{CGSize=dd},R,N"
- "_currentScaleForViewSize:"
- "adjustedControlsAndPaddingScaleForViewSize:"
- "adjustedSpacingScaleForViewSize:"
- "initWithFrame:captureOnly:wantsGlassBackground:"

```
