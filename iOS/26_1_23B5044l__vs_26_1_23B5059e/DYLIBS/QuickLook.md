## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-1016.201.1.2.0
-  __TEXT.__text: 0xd5b10
+1016.201.4.0.0
+  __TEXT.__text: 0xd5d64
   __TEXT.__auth_stubs: 0x2580
   __TEXT.__delay_helper: 0x7cc
   __TEXT.__objc_methlist: 0xb57c
   __TEXT.__const: 0x2d94
   __TEXT.__gcc_except_tab: 0x19e8
   __TEXT.__oslogstring: 0x5537
-  __TEXT.__cstring: 0x6370
+  __TEXT.__cstring: 0x6470
   __TEXT.__ustring: 0x1c
   __TEXT.__swift5_typeref: 0x1a86
   __TEXT.__swift5_reflstr: 0x7e7

   __TEXT.__swift_as_ret: 0x1c0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x48d8
+  __TEXT.__unwind_info: 0x48e0
   __TEXT.__eh_frame: 0x4734
   __TEXT.__objc_classname: 0x1727
-  __TEXT.__objc_methname: 0x20741
+  __TEXT.__objc_methname: 0x2076f
   __TEXT.__objc_methtype: 0x6ed1
-  __TEXT.__objc_stubs: 0x15b40
+  __TEXT.__objc_stubs: 0x15b60
   __DATA_CONST.__got: 0xf28
   __DATA_CONST.__const: 0x2610
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x398
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x72e8
+  __DATA_CONST.__objc_selrefs: 0x72f0
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x12d0
   __AUTH_CONST.__const: 0x36d0
-  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__cfstring: 0x32a0
   __AUTH_CONST.__objc_const: 0x11720
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0CAE4BE1-5E22-3EB2-A9DD-244561D79D54
+  UUID: 6C2ED8D9-3AF4-3F7B-B50B-FE586305AF8B
   Functions: 5522
-  Symbols:   14034
-  CStrings:  7265
+  Symbols:   14035
+  CStrings:  7280
 
Symbols:
+ ___46-[QLMovieItemViewController loadAssetMetadata]_block_invoke.228
+ ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke.187
+ ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke_2.188
+ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.108
+ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.121
+ ___block_descriptor_56_e8_32bs_e20_v24?0Q8"NSArray"16ls32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8s40l8
+ ___block_literal_global.171
+ ___block_literal_global.175
+ ___block_literal_global.199
+ _objc_msgSend$setAutomaticallyAdjustsScrollIndicatorInsets:
- ___46-[QLMovieItemViewController loadAssetMetadata]_block_invoke.216
- ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke.178
- ___52-[QLPreviewController(Overlay) _openInButtonTapped:]_block_invoke_2.179
- ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.106
- ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.119
- ___block_descriptor_56_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_64_e8_32bs_e12_v24?0Q8^d16ls32l8
- ___block_descriptor_64_e8_32s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8
- ___block_literal_global.162
- ___block_literal_global.166
- ___block_literal_global.190
Functions:
~ ___48-[QLPreviewController updatePreferredTransition]_block_invoke : 1620 -> 1624
~ -[UIToolbar(_UIToolbarConfiguration) configureWithConfiguration:] : 392 -> 400
~ -[QLTextItemViewController setupTextView:] : 704 -> 716
~ -[QLTextItemViewController _updateTextViewInsets] : 204 -> 208
~ _QLWaveformWithPowerLevels : 256 -> 292
~ ___QLWaveformWithPowerLevels_block_invoke : 292 -> 316
~ +[QLWaveformScrubberViewProvider generateWaveformForSize:asset:updateHandler:] : 416 -> 412
~ ___78+[QLWaveformScrubberViewProvider generateWaveformForSize:asset:updateHandler:]_block_invoke : 412 -> 560
~ ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.106 -> ___QLWaveformDeterminePowerLevelsForAsset_block_invoke.108 : 1412 -> 1584
~ -[QLMovieItemViewController toolbarButtonsForTraitCollection:] : 484 -> 576
~ -[QLPreviewController(Overlay) _actionButton] : 416 -> 516
CStrings:
+ "Rotate right"
+ "Share"
+ "Title of Rotate right button displayed in Quick Look's toolbar for videos."
+ "Title of Share button displayed in Quick Look's navigation bar."
+ "Title of Trim button displayed in Quick Look's toolbar for videos."
+ "Trim"
+ "setAutomaticallyAdjustsScrollIndicatorInsets:"
+ "square.and.arrow.up"
+ "v24@?0Q8@\"NSArray\"16"
- "v24@?0Q8^d16"

```
