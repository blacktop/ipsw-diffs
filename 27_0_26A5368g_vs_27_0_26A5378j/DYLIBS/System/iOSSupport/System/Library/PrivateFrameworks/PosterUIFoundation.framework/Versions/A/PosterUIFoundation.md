## PosterUIFoundation

> `/System/iOSSupport/System/Library/PrivateFrameworks/PosterUIFoundation.framework/Versions/A/PosterUIFoundation`

```diff

-  __TEXT.__text: 0x931bc
-  __TEXT.__objc_methlist: 0xaae4
+  __TEXT.__text: 0x93234
+  __TEXT.__objc_methlist: 0xaaec
   __TEXT.__const: 0xdc4
   __TEXT.__oslogstring: 0x38c1
   __TEXT.__cstring: 0x6553
-  __TEXT.__gcc_except_tab: 0x1648
+  __TEXT.__gcc_except_tab: 0x163c
   __TEXT.__dlopen_cstrs: 0x1c0
   __TEXT.__swift5_typeref: 0x7f2
   __TEXT.__constg_swiftt: 0x69c

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x26f0
+  __DATA_CONST.__const: 0x2710
   __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5888
+  __DATA_CONST.__objc_selrefs: 0x5890
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x18e0

   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0xff0
-  __AUTH.__objc_data: 0x23c0
+  __AUTH_CONST.__auth_got: 0x1010
+  __AUTH.__objc_data: 0x2320
   __AUTH.__data: 0x1a0
   __DATA.__objc_ivar: 0xbe0
   __DATA.__data: 0x17a8
   __DATA.__bss: 0x8b0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xd70
+  __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4124
-  Symbols:   10669
+  Functions: 4126
+  Symbols:   10677
   CStrings:  2498
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
Symbols:
+ -[PUIPosterLevelSet copyByFilteringLevels:]
+ __UIClamp
+ __UILerp
+ __UIMap
+ __UIUnlerp
+ ___52+[PUICodableImage dataRepresentationForImage:error:]_block_invoke
+ ___block_descriptor_40_e9_16?0^8l
+ _objc_msgSend$copyByFilteringLevels:
Functions:
~ ___48-[PUIStyleDiscreteColors variationAppliedColors]_block_invoke : 40 -> 116
~ +[PUIDiscreteGradientVariatedCustomStyle variatedColorForVariation:fromColors:usingSaturation:alpha:] : 560 -> 580
~ +[PUIDiscreteGradientVariatedCustomStyle luminanceForLegacyLuminance:] : 28 -> 20
~ -[PUIStylePickerHomeScreenComponentViewController updateHomeScreenCustomTintColorToColor:] : 300 -> 284
~ -[PUIStylePickerHomeScreenComponentViewController _createTintSourceHorizontalStackViewForHomeScreenConfiguration:] : 896 -> 880
~ -[PUIStylePickerHomeScreenComponentViewController _accentColorSlidersDidChangeValue:] : 452 -> 436
~ -[_PUIStylePickerHomeScreenLumaSliderUICoordinatorImpl initWithStyle:] : 268 -> 252
~ -[_PUIStylePickerHomeScreenLumaSliderUICoordinatorImpl setVariation:] : 328 -> 324
~ -[_PUIStylePickerHomeScreenLumaSliderUICoordinatorImpl gradientSliderDidChange:] : 552 -> 536
~ -[_PUIStylePickerHomeScreenLumaSliderUICoordinatorImpl _updateSliderThumbView] : 236 -> 212
~ -[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:finalizedMutator:error:] : 2176 -> 2180
~ ___74-[PUIFontPickerComponentViewController configureFontPickerViewIfNecessary]_block_invoke : 388 -> 384
~ +[UIColor(PosterUIFoundation) pui_determineVarianceAndLuminanceForColor:amongstColors:minLuminance:maxLuminance:outVariance:outLuminance:outSaturation:] : 100 -> 96
~ +[UIColor(PosterUIFoundation) pui_determineVarianceAndLuminanceForColor:amongstColors:minLuminance:maxLuminance:outHue:outSaturation:outLuminance:] : 404 -> 412
~ +[UIColor(PosterUIFoundation) pui_determineVarianceForHue:forColors:] : 492 -> 508
~ ___44+[PUIPosterLevelSet allLevelsExceptFloating]_block_invoke : 120 -> 92
~ -[PUIPosterLevelSet initWithSet:] : 156 -> 256
~ -[PUIPosterLevelSet initWithNumberOfLevels:] : 208 -> 172
~ -[PUIPosterLevelSet initWithLevel:] : 152 -> 116
~ -[PUIPosterLevelSet init] : 100 -> 76
~ -[PUIPosterLevelSet initWithCoder:] : 224 -> 200
~ -[PUIPosterLevelSet copyWithZone:] : 76 -> 64
+ -[PUIPosterLevelSet copyByFilteringLevels:]
~ -[PUIPosterLevelSet sortedLevels] : 192 -> 8
~ -[PUIStyleColorPickerVibrantMonotoneColor colorWithVariation:] : 68 -> 76
~ -[PUIStyleColorPickerVibrantMonotoneColor variationForAlpha:] : 16 -> 20
~ +[PUIStyleColorPickerVibrantColor luminanceForPosterColor:withAppliedVariation:] : 124 -> 148
~ -[PUIStyleColorPickerVibrantColor colorWithVariation:] : 68 -> 76
~ -[PUIStyleColorPickerVibrantColor variationForAlpha:] : 16 -> 20
~ -[PUIStyleColorPickerConstantColor variationForLuminance:] : 280 -> 316
~ +[PUICodableImage dataRepresentationForImage:error:] : 868 -> 300
+ ___52+[PUICodableImage dataRepresentationForImage:error:]_block_invoke
~ ___86-[PUIStylePickerViewController fontPickerComponentViewController:didChangeFontWeight:]_block_invoke : 152 -> 140
~ ___80-[PUIStylePickerViewController fontPickerComponentViewController:didSelectItem:]_block_invoke : 436 -> 428
~ -[PUIStylePickerViewController _setupComponentViewControllersIfNeeded] : 2620 -> 2612

```
