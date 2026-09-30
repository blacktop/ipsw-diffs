## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-  __TEXT.__text: 0x3534ec
-  __TEXT.__objc_methlist: 0x25f9c
-  __TEXT.__const: 0x8ec4
+  __TEXT.__text: 0x354664
+  __TEXT.__objc_methlist: 0x25fcc
+  __TEXT.__const: 0x8ee4
   __TEXT.__dlopen_cstrs: 0x563
-  __TEXT.__constg_swiftt: 0x1eb8
-  __TEXT.__swift5_typeref: 0x1ee4
+  __TEXT.__constg_swiftt: 0x1f24
+  __TEXT.__swift5_typeref: 0x1ef4
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x1683
-  __TEXT.__swift5_fieldmd: 0x1a9c
+  __TEXT.__swift5_fieldmd: 0x1aac
   __TEXT.__swift5_assocty: 0x728
   __TEXT.__swift5_proto: 0x398
-  __TEXT.__swift5_types: 0x1d8
+  __TEXT.__swift5_types: 0x1dc
   __TEXT.__swift5_capture: 0xa9c
-  __TEXT.__cstring: 0xf917
-  __TEXT.__oslogstring: 0xebad
+  __TEXT.__cstring: 0xf918
+  __TEXT.__oslogstring: 0xed2f
   __TEXT.__swift_as_entry: 0xf0
   __TEXT.__swift_as_cont: 0x218
   __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x2520c
+  __TEXT.__gcc_except_tab: 0x25338
   __TEXT.__ustring: 0x23a
-  __TEXT.__unwind_info: 0x106b0
+  __TEXT.__unwind_info: 0x10738
   __TEXT.__eh_frame: 0x2ae8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x7e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x13538
+  __DATA_CONST.__objc_selrefs: 0x13530
   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0xda8
   __DATA_CONST.__objc_arraydata: 0x920
   __DATA_CONST.__got: 0x22a0
-  __AUTH_CONST.__const: 0x8538
-  __AUTH_CONST.__cfstring: 0xe740
-  __AUTH_CONST.__objc_const: 0x48d18
+  __AUTH_CONST.__const: 0x85d0
+  __AUTH_CONST.__cfstring: 0xe720
+  __AUTH_CONST.__objc_const: 0x48d88
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_arrayobj: 0x6c0
   __AUTH_CONST.__objc_dictobj: 0x460
   __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__auth_got: 0x1df8
-  __AUTH.__objc_data: 0xa730
+  __AUTH_CONST.__auth_got: 0x1e10
+  __AUTH.__objc_data: 0xa690
   __AUTH.__data: 0xc20
-  __DATA.__objc_ivar: 0x2cac
-  __DATA.__data: 0x6cb8
-  __DATA.__bss: 0x7038
-  __DATA.__common: 0x150
-  __DATA_DIRTY.__objc_ivar: 0x1154
-  __DATA_DIRTY.__objc_data: 0x1770
+  __DATA.__objc_ivar: 0x2cb4
+  __DATA.__data: 0x6d68
+  __DATA.__bss: 0x7030
+  __DATA.__common: 0x160
+  __DATA_DIRTY.__objc_ivar: 0x115c
+  __DATA_DIRTY.__objc_data: 0x1810
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x7b8
+  __DATA_DIRTY.__bss: 0x7c0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 18429
-  Symbols:   60729
-  CStrings:  5423
+  Functions: 18446
+  Symbols:   60785
+  CStrings:  5429
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
Symbols:
+ +[PKRendererVSyncController deviceNameForScreen:]
+ +[PKRendererVSyncController sharedControllerForDeviceName:]
+ +[PKRendererVSyncController sharedControllerForScreen:]
+ -[PKMetalRendererController _updateVSyncController]
+ -[PKMetalRendererController setVSyncDeviceName:]
+ -[PKPaletteContainerView _shouldHideAccessoryView]
+ -[PKPaletteContainerView layoutSubviews]
+ -[PKPaletteHostView _updatePaletteViewLayoutGuideInsets]
+ -[PKPencilShadowView didMoveToWindow]
+ -[PKSelectionView _startWritingToolsWithDictionary:]
+ -[PKTiledCanvasView _updateVSyncController]
+ GCC_except_table286
+ GCC_except_table290
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table303
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table321
+ GCC_except_table328
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table336
+ GCC_except_table340
+ GCC_except_table342
+ GCC_except_table349
+ GCC_except_table352
+ GCC_except_table354
+ GCC_except_table359
+ GCC_except_table366
+ GCC_except_table372
+ GCC_except_table377
+ GCC_except_table381
+ GCC_except_table386
+ GCC_except_table390
+ GCC_except_table394
+ GCC_except_table400
+ GCC_except_table408
+ GCC_except_table478
+ _$s7SwiftUI19UIHostingControllerC5coder8rootViewACyxGSgSo7NSCoderC_xtcfCTq
+ _$s7SwiftUI19UIHostingControllerC5coder8rootViewACyxGSgSo7NSCoderC_xtcfc
+ _$s7SwiftUI19UIHostingControllerC8rootViewACyxGx_tcfCTq
+ _$s9PencilKit23SecureHostingControllerC19_canShowWhileLockedSbyFTo
+ _$s9PencilKit23SecureHostingControllerC5coder8rootViewACyxGSgSo7NSCoderC_xtcfC
+ _$s9PencilKit23SecureHostingControllerC5coder8rootViewACyxGSgSo7NSCoderC_xtcfc
+ _$s9PencilKit23SecureHostingControllerC5coderACyxGSgSo7NSCoderC_tcfc
+ _$s9PencilKit23SecureHostingControllerC5coderACyxGSgSo7NSCoderC_tcfcTo
+ _$s9PencilKit23SecureHostingControllerC8rootViewACyxGx_tcfC
+ _$s9PencilKit23SecureHostingControllerC8rootViewACyxGx_tcfcTf4gn_n
+ _$s9PencilKit23SecureHostingControllerCMF
+ _$s9PencilKit23SecureHostingControllerCMI
+ _$s9PencilKit23SecureHostingControllerCMP
+ _$s9PencilKit23SecureHostingControllerCMa
+ _$s9PencilKit23SecureHostingControllerCMi
+ _$s9PencilKit23SecureHostingControllerCMn
+ _$s9PencilKit23SecureHostingControllerCMo
+ _$s9PencilKit23SecureHostingControllerCMr
+ _$s9PencilKit23SecureHostingControllerCfD
+ _$s9PencilKit23SecureHostingControllerCyAA28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLVGMR
+ _$s9PencilKit23SecureHostingControllerCyAA28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLVGMd
+ _$s9PencilKit35PKSqueezePaletteGlassBackgroundViewC17hostingController33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLAA013SecureHostingI0CyAA0cde3ArcG0AELLVGSgvpWvd
+ _OBJC_IVAR_$_PKMetalRendererController._currentVSyncController
+ _OBJC_IVAR_$_PKMetalRendererController._vSyncDeviceName
+ _OBJC_IVAR_$_PKRendererVSyncController._deviceName
+ _PKPaletteDockedEdgeMargin
+ __INSTANCE_METHODS__TtC9PencilKit23SecureHostingController
+ __UIMap
+ ___44-[PKPaletteHostView safeAreaInsetsDidChange]_block_invoke_2
+ ___48-[PKMetalRendererController setVSyncDeviceName:]_block_invoke
+ ___48-[PKRendererVSyncController initWithDeviceName:]_block_invoke
+ ___unnamed_4
+ _objc_msgSend$_updatePaletteViewLayoutGuideInsets
+ _objc_msgSend$_updateVSyncController
+ _objc_msgSend$deviceName
+ _objc_msgSend$topViewController
+ _swift_allocateGenericClassMetadata
+ _swift_initClassMetadata2
+ _symbolic _____ 9PencilKit23SecureHostingControllerC
+ _symbolic _____y_____G 9PencilKit23SecureHostingControllerC AA28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLV
+ _symbolic _____y_____GSg 9PencilKit23SecureHostingControllerC AA28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLV
+ _symbolic _____yxG 7SwiftUI19UIHostingControllerC
- +[PKRendererVSyncController sharedController]
- -[PKRendererVSyncController init]
- -[PKToolPicker _directionalLayoutMargins]
- -[PKToolPicker _setDirectionalLayoutMargins:]
- GCC_except_table289
- GCC_except_table294
- GCC_except_table297
- GCC_except_table302
- GCC_except_table309
- GCC_except_table311
- GCC_except_table318
- GCC_except_table331
- GCC_except_table334
- GCC_except_table337
- GCC_except_table341
- GCC_except_table344
- GCC_except_table351
- GCC_except_table353
- GCC_except_table357
- GCC_except_table361
- GCC_except_table369
- GCC_except_table376
- GCC_except_table380
- GCC_except_table385
- GCC_except_table389
- GCC_except_table392
- GCC_except_table399
- GCC_except_table406
- GCC_except_table412
- GCC_except_table479
- _$s7SwiftUI19UIHostingControllerCy9PencilKit28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLVGMR
- _$s7SwiftUI19UIHostingControllerCy9PencilKit28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLVGMd
- _$s9PencilKit35PKSqueezePaletteGlassBackgroundViewC17hostingController33_E0003CBE58FBC3EFB8AF3A591FBDBD72LL7SwiftUI09UIHostingI0CyAA0cde3ArcG0AELLVGSgvpWvd
- _NSStringFromDirectionalEdgeInsets
- _OBJC_IVAR_$_PKToolPicker.__directionalLayoutMargins
- _PKPaletteTopLayoutMarginIgnoringSafeArea
- __ZL13timebase_info
- __ZNSt3__14sortB9foe220106INS_11__wrap_iterIP18AttachmentTileInfoEEZ86-[PKTiledView updateTilesForVisibleRectRendering:offscreen:overrideAdditionalStrokes:]E3$_0EEvT_S6_T0_
- ___33-[PKRendererVSyncController init]_block_invoke
- ___45+[PKRendererVSyncController sharedController]_block_invoke
- _objc_msgSend$_directionalLayoutMargins
- _objc_msgSend$layoutMargins
- _objc_msgSend$setDirectionalLayoutMargins:
- _objc_msgSend$setInsetsLayoutMarginsFromSafeArea:
- _symbolic _____y_____G 7SwiftUI19UIHostingControllerC 9PencilKit28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLV
- _symbolic _____y_____GSg 7SwiftUI19UIHostingControllerC 9PencilKit28PKSqueezePaletteGlassArcView33_E0003CBE58FBC3EFB8AF3A591FBDBD72LLV
CStrings:
+ "Adding renderer controller to '%@': %p"
+ "Did configure mobile framebuffer by name: '%@' => %p"
+ "Removing renderer controller from '%@': %p"
+ "Skipping tile generation: non-finite attachment visible rect."
+ "Skipping tile generation: tile span out of range (%ld x %ld)."
+ "Skipping updateTilesForVisibleRectRendering: tileSize=%g frame=%@ zoomScale=%g tileScale=%g scrollBounds=%@"
+ "Tile span: %lu, %lu"
+ "Unable to open mobile framebuffer"
+ "VSync"
+ "_startWritingToolsWithDictionary: - PKSelectionView"
+ "\xf0\xf0\xf0\xf0q\x92"
- "Unable to open primary mobile framebuffer"
- "primary"
- "set directional layout margins to %{public}@"
- "\xf0\xf0\xf0\xf0Q\x82"

```
