## LinkPresentation

> `/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`

```diff

-235.2.0.0.0
-  __TEXT.__text: 0xcc1bc
+240.1.0.0.0
+  __TEXT.__text: 0xce19c
   __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0xddc4
-  __TEXT.__cstring: 0x7fa5
-  __TEXT.__gcc_except_tab: 0x1cc68
-  __TEXT.__const: 0x708
-  __TEXT.__ustring: 0x474
+  __TEXT.__objc_methlist: 0xdf0c
+  __TEXT.__cstring: 0x806f
+  __TEXT.__gcc_except_tab: 0x1d340
+  __TEXT.__const: 0x778
+  __TEXT.__ustring: 0x484
   __TEXT.__oslogstring: 0x29ed
   __TEXT.__dlopen_cstrs: 0x96f
-  __TEXT.__unwind_info: 0x6c58
+  __TEXT.__unwind_info: 0x6cc4
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x220e
-  __TEXT.__objc_methname: 0x1c82c
-  __TEXT.__objc_methtype: 0x3e69
-  __TEXT.__objc_stubs: 0x160a0
+  __TEXT.__objc_classname: 0x2217
+  __TEXT.__objc_methname: 0x1cc32
+  __TEXT.__objc_methtype: 0x3e86
+  __TEXT.__objc_stubs: 0x16400
   __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x2090
+  __DATA_CONST.__const: 0x20f0
   __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x24040
-  __DATA_CONST.__objc_selrefs: 0x63f0
-  __DATA_CONST.__objc_arraydata: 0x1470
-  __AUTH_CONST.__const: 0xcc0
-  __AUTH_CONST.__objc_const: 0x6db0
-  __AUTH_CONST.__cfstring: 0xcd80
-  __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH_CONST.__objc_arrayobj: 0x3f0
+  __DATA_CONST.__objc_const: 0x24268
+  __DATA_CONST.__objc_selrefs: 0x64b0
+  __DATA_CONST.__objc_arraydata: 0x1490
+  __AUTH_CONST.__const: 0xce0
+  __AUTH_CONST.__objc_const: 0x6d68
+  __AUTH_CONST.__cfstring: 0xce80
+  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__objc_arrayobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x60

   __DATA.__objc_protorefs: 0x70
   __DATA.__objc_classrefs: 0xc40
   __DATA.__objc_superrefs: 0x650
-  __DATA.__objc_ivar: 0x15e4
-  __DATA.__data: 0x1848
-  __DATA.__bss: 0x580
+  __DATA.__objc_ivar: 0x1608
+  __DATA.__data: 0x1840
+  __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x2828
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5243
-  Symbols:   20530
-  CStrings:  7721
+  Functions: 5279
+  Symbols:   20659
+  CStrings:  7767
 
Symbols:
+ +[LPPresentationSpecializations isAppleBookSeriesURL:]
+ +[LPSettings useLightweightMaterials]
+ +[LPTheme defaultBackgroundColorForPlatform:]
+ -[LPButtonStyle prefersBehavioralStylePad]
+ -[LPButtonStyle setPrefersBehavioralStylePad:]
+ -[LPCaptionBarButtonView hasAnyText]
+ -[LPCaptionBarPresentationProperties collaborationFooter]
+ -[LPCaptionBarPresentationProperties setCollaborationFooter:]
+ -[LPCaptionButtonPresentationProperties setShape:]
+ -[LPCaptionButtonPresentationProperties shape]
+ -[LPCollaborationFooterPresentationProperties .cxx_destruct]
+ -[LPCollaborationFooterPresentationProperties action]
+ -[LPCollaborationFooterPresentationProperties glyphAttachmentImage]
+ -[LPCollaborationFooterPresentationProperties initiatorNameComponents]
+ -[LPCollaborationFooterPresentationProperties initiatorName]
+ -[LPCollaborationFooterPresentationProperties setAction:]
+ -[LPCollaborationFooterPresentationProperties setGlyphAttachmentImage:]
+ -[LPCollaborationFooterPresentationProperties setInitiatorName:]
+ -[LPCollaborationFooterPresentationProperties setInitiatorNameComponents:]
+ -[LPCollaborationFooterPresentationProperties setSubtitle:]
+ -[LPCollaborationFooterPresentationProperties setTitle:]
+ -[LPCollaborationFooterPresentationProperties subtitle]
+ -[LPCollaborationFooterPresentationProperties title]
+ -[LPCollaborationFooterView initWithHost:properties:style:]
+ -[LPImageViewStyle fixedFallbackImageFontTextStyle]
+ -[LPImageViewStyle setFixedFallbackImageFontTextStyle:]
+ -[LPLinkMetadataPresentationTransformer allowsOpaqueBackgroundColors]
+ -[LPLinkMetadataPresentationTransformer setAllowsOpaqueBackgroundColors:]
+ -[LPLinkView _backgroundColorSupportsVibrancy:]
+ -[LPLinkView _resolveBackgroundColor]
+ -[LPLinkView _shouldUseBlur]
+ -[LPLinkView themePlatformForComponentView:]
+ -[LPMediaPlaybackManager _volumeChanged]
+ -[LPTextView _needsColoredGlyphsView]
+ -[LPVerticalTextStackViewStyle applyToLowerTextRowStyles:]
+ -[LPiCloudSharingMetadata(Transformer) _bottomLeadingCaptionStringWithApplicationName:originalURL:]
+ -[LPiCloudSharingMetadata(Transformer) isSafariTabGroupLinkWithURL:]
+ GCC_except_table104
+ GCC_except_table114
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table135
+ GCC_except_table144
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table161
+ GCC_except_table171
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table186
+ GCC_except_table188
+ GCC_except_table199
+ GCC_except_table205
+ GCC_except_table209
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table283
+ GCC_except_table300
+ GCC_except_table317
+ GCC_except_table396
+ GCC_except_table398
+ GCC_except_table399
+ GCC_except_table400
+ GCC_except_table413
+ GCC_except_table414
+ GCC_except_table415
+ GCC_except_table417
+ GCC_except_table422
+ GCC_except_table423
+ GCC_except_table431
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table436
+ GCC_except_table446
+ GCC_except_table447
+ GCC_except_table451
+ GCC_except_table452
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table497
+ GCC_except_table498
+ GCC_except_table88
+ _OBJC_CLASS_$_LPCollaborationFooterPresentationProperties
+ _OBJC_IVAR_$_LPButtonStyle._prefersBehavioralStylePad
+ _OBJC_IVAR_$_LPCaptionBarPresentationProperties._collaborationFooter
+ _OBJC_IVAR_$_LPCaptionButtonPresentationProperties._shape
+ _OBJC_IVAR_$_LPCollaborationFooterPresentationProperties._action
+ _OBJC_IVAR_$_LPCollaborationFooterPresentationProperties._glyphAttachmentImage
+ _OBJC_IVAR_$_LPCollaborationFooterPresentationProperties._initiatorName
+ _OBJC_IVAR_$_LPCollaborationFooterPresentationProperties._initiatorNameComponents
+ _OBJC_IVAR_$_LPCollaborationFooterPresentationProperties._subtitle
+ _OBJC_IVAR_$_LPCollaborationFooterPresentationProperties._title
+ _OBJC_IVAR_$_LPCollaborationFooterView._action
+ _OBJC_IVAR_$_LPCollaborationFooterView._subtitleView
+ _OBJC_IVAR_$_LPImageViewStyle._fixedFallbackImageFontTextStyle
+ _OBJC_IVAR_$_LPLinkMetadataPresentationTransformer._allowsOpaqueBackgroundColors
+ _OBJC_IVAR_$_LPLinkView._backgroundColorSupportsVibrancy
+ _OBJC_IVAR_$_LPLinkView._collaborationFooter
+ _OBJC_METACLASS_$_LPCollaborationFooterPresentationProperties
+ __OBJC_$_INSTANCE_METHODS_LPCollaborationFooterPresentationProperties
+ __OBJC_$_INSTANCE_VARIABLES_LPCollaborationFooterPresentationProperties
+ __OBJC_$_PROP_LIST_LPCollaborationFooterPresentationProperties
+ __OBJC_CLASS_RO_$_LPCollaborationFooterPresentationProperties
+ __OBJC_METACLASS_RO_$_LPCollaborationFooterPresentationProperties
+ ___25-[LPTheme adjustForStyle]_block_invoke.1015
+ ___25-[LPTheme adjustForStyle]_block_invoke.1025
+ ___25-[LPTheme adjustForStyle]_block_invoke_2.1018
+ ___25-[LPTheme adjustForStyle]_block_invoke_2.1028
+ ___25-[LPTheme adjustForStyle]_block_invoke_3.1021
+ ___25-[LPTheme adjustForStyle]_block_invoke_4.1022
+ ___37+[LPSettings useLightweightMaterials]_block_invoke
+ ___40-[LPMediaPlaybackManager volumeChanged:]_block_invoke
+ ___45-[LPCaptionBarButtonView layoutComponentView]_block_invoke
+ ___59-[LPCollaborationFooterView initWithHost:properties:style:]_block_invoke
+ ___59-[LPCollaborationFooterView initWithHost:properties:style:]_block_invoke_2
+ ___applyCommonCardHeadingCaptionBarProperties_block_invoke
+ ___block_descriptor_40_ea8_32s_e24_v16?0"LPTextRowStyle"8ls32l8
+ ___block_descriptor_40_ea8_32s_e5_i8?0ls32l8
+ ___block_literal_global.1000
+ ___block_literal_global.1002
+ ___block_literal_global.1004
+ ___block_literal_global.1006
+ ___block_literal_global.1012
+ ___block_literal_global.1017
+ ___block_literal_global.1020
+ ___block_literal_global.1027
+ ___block_literal_global.11
+ ___block_literal_global.1181
+ ___block_literal_global.1186
+ ___block_literal_global.1188
+ ___block_literal_global.988
+ __unnamed_array_storage.274
+ __unnamed_array_storage.277
+ __unnamed_array_storage.295
+ __unnamed_array_storage.360
+ _cardHeadingIconSize.normalSize.1189
+ _cardHeadingVerticalIconMargin
+ _cardHeadingVerticalIconMargin.normalMargin
+ _cardHeadingVerticalIconMargin.visionMargin
+ _cardHeadingVerticalIconMargin.watchMargin
+ _defaultCornerRadius.normalSize
+ _defaultCornerRadius.tinyVisionSize
+ _defaultCornerRadius.visionSize
+ _faceTimeIconSize.visionSize
+ _fallbackIconSize.normalSize.1174
+ _objc_msgSend$_backgroundColorSupportsVibrancy:
+ _objc_msgSend$_bottomLeadingCaptionStringWithApplicationName:originalURL:
+ _objc_msgSend$_needsColoredGlyphsView
+ _objc_msgSend$_resolveBackgroundColor
+ _objc_msgSend$_shouldUseBlur
+ _objc_msgSend$_volumeChanged
+ _objc_msgSend$allowsOpaqueBackgroundColors
+ _objc_msgSend$applyToLowerTextRowStyles:
+ _objc_msgSend$configurationWithTextStyle:
+ _objc_msgSend$defaultBackgroundColorForPlatform:
+ _objc_msgSend$effectForBlurEffect:
+ _objc_msgSend$fixedFallbackImageFontTextStyle
+ _objc_msgSend$glyphAttachmentImage
+ _objc_msgSend$hasAnyText
+ _objc_msgSend$ignoreSafeAreaInset
+ _objc_msgSend$initiatorName
+ _objc_msgSend$isAppleBookSeriesURL:
+ _objc_msgSend$isSafariTabGroupLinkWithURL:
+ _objc_msgSend$prefersBehavioralStylePad
+ _objc_msgSend$secondarySystemBackgroundColor
+ _objc_msgSend$setAllowsOpaqueBackgroundColors:
+ _objc_msgSend$setFixedFallbackImageFontTextStyle:
+ _objc_msgSend$setGlyphAttachmentImage:
+ _objc_msgSend$setIconOffset:
+ _objc_msgSend$setInitiatorName:
+ _objc_msgSend$setInitiatorNameComponents:
+ _objc_msgSend$setPadding:
+ _objc_msgSend$setPreferredVibrancy:
+ _objc_msgSend$setPrefersBehavioralStylePad:
+ _objc_msgSend$setTraitCollection:
+ _objc_msgSend$shape
+ _objc_msgSend$themePlatformForComponentView:
+ _objc_msgSend$useLightweightMaterials
+ _sharedObjectAutomaticIconOuterMargin.normalSize
+ _sharedObjectAutomaticIconOuterMargin.visionSize
+ _sharedObjectAutomaticIconOuterMargin.watchSize
+ _sizeClassAllowsCollaborationFooter
+ _sizeClassAllowsInsetMedia
+ _transcriptBoldTextFont.contentSizeCategory.166
+ _transcriptBoldTextFont.font.167
+ _updateFromDefaults.hasEverUpdated
+ _useLightweightMaterials.lightweightMaterialsEnabled
+ _useLightweightMaterials.onceToken
+ _visionPtAdjusted
- +[LPCollaborationFooterConfiguration configurationWithViewModel:action:]
- -[LPCollaborationFooterConfiguration .cxx_destruct]
- -[LPCollaborationFooterConfiguration action]
- -[LPCollaborationFooterConfiguration setAction:]
- -[LPCollaborationFooterConfiguration setViewModel:]
- -[LPCollaborationFooterConfiguration viewModel]
- -[LPCollaborationFooterView initWithHost:configuration:style:]
- -[LPLinkView resolveBackgroundColor]
- -[LPiCloudSharingMetadata(Transformer) _bottomLeadingCaptionStringWithApplicationName:]
- GCC_except_table116
- GCC_except_table128
- GCC_except_table136
- GCC_except_table146
- GCC_except_table149
- GCC_except_table150
- GCC_except_table157
- GCC_except_table163
- GCC_except_table170
- GCC_except_table173
- GCC_except_table187
- GCC_except_table191
- GCC_except_table202
- GCC_except_table255
- GCC_except_table256
- GCC_except_table278
- GCC_except_table295
- GCC_except_table301
- GCC_except_table312
- GCC_except_table335
- GCC_except_table378
- GCC_except_table389
- GCC_except_table391
- GCC_except_table393
- GCC_except_table395
- GCC_except_table411
- GCC_except_table412
- GCC_except_table424
- GCC_except_table425
- GCC_except_table426
- GCC_except_table427
- GCC_except_table439
- GCC_except_table445
- GCC_except_table448
- GCC_except_table450
- GCC_except_table482
- GCC_except_table487
- GCC_except_table488
- GCC_except_table489
- GCC_except_table76
- GCC_except_table90
- _OBJC_CLASS_$_LPCollaborationFooterConfiguration
- _OBJC_IVAR_$_LPCollaborationFooterConfiguration._action
- _OBJC_IVAR_$_LPCollaborationFooterConfiguration._viewModel
- _OBJC_IVAR_$_LPCollaborationFooterView._configuration
- _OBJC_IVAR_$_LPCollaborationFooterView._handleView
- _OBJC_IVAR_$_LPLinkView._backgroundColorIsClear
- _OBJC_IVAR_$_LPLinkView._collaborationFooterConfiguration
- _OBJC_METACLASS_$_LPCollaborationFooterConfiguration
- __OBJC_$_CLASS_METHODS_LPCollaborationFooterConfiguration
- __OBJC_$_INSTANCE_METHODS_LPCollaborationFooterConfiguration
- __OBJC_$_INSTANCE_VARIABLES_LPCollaborationFooterConfiguration
- __OBJC_$_PROP_LIST_LPCollaborationFooterConfiguration
- __OBJC_CLASS_RO_$_LPCollaborationFooterConfiguration
- __OBJC_METACLASS_RO_$_LPCollaborationFooterConfiguration
- ___25-[LPTheme adjustForStyle]_block_invoke.1007
- ___25-[LPTheme adjustForStyle]_block_invoke_14
- ___25-[LPTheme adjustForStyle]_block_invoke_15
- ___25-[LPTheme adjustForStyle]_block_invoke_16
- ___62-[LPCollaborationFooterView initWithHost:configuration:style:]_block_invoke
- ___62-[LPCollaborationFooterView initWithHost:configuration:style:]_block_invoke_2
- ___block_literal_global.1001
- ___block_literal_global.1003
- ___block_literal_global.1009
- ___block_literal_global.1160
- ___block_literal_global.1165
- ___block_literal_global.1167
- ___block_literal_global.1169
- ___block_literal_global.977
- ___block_literal_global.989
- ___block_literal_global.991
- ___block_literal_global.993
- ___block_literal_global.995
- ___defaultBackgroundColor_block_invoke_2
- __unnamed_array_storage.283
- __unnamed_array_storage.348
- _adjustForStyle.outerMargin.1004
- _cardHeadingIconMargin
- _cardHeadingIconMargin.normalMargin
- _cardHeadingIconMargin.watchMargin
- _cardHeadingIconSize.normalSize.1170
- _cardHeadingLeadingTextPadding
- _fallbackIconSize.normalSize.1153
- _objc_msgSend$_bottomLeadingCaptionStringWithApplicationName:
- _objc_msgSend$configurationWithViewModel:action:
- _objc_msgSend$initWithHost:configuration:style:
- _objc_msgSend$resolveBackgroundColor
- _objc_msgSend$setViewModel:
- _objc_msgSend$viewModel
- _transcriptBoldTextFont.contentSizeCategory.141
- _transcriptBoldTextFont.font.142
CStrings:
+ "\x04\x1a#"
+ "\x04$\x11"
+ "\x15$/\x03\x11\x17\x14q\x17!"
+ "\x1a3\x13\x12"
+ "\"\x13\x11"
+ "@\"LPCollaborationFooterPresentationProperties\""
+ "@\"NSPersonNameComponents\""
+ "Anyone with the link will be able to add, delete, and reorder songs."
+ "AppleBookSeries"
+ "AppleMusicCollaborativePlaylist"
+ "Collaborate"
+ "Join Playlist"
+ "LPCollaborationFooterPresentationProperties"
+ "T@\"LPCollaborationFooterPresentationProperties\",&,N,V_collaborationFooter"
+ "T@\"NSPersonNameComponents\",C,N,V_initiatorNameComponents"
+ "T@\"NSString\",&,N,V_fixedFallbackImageFontTextStyle"
+ "T@\"NSString\",C,N,V_initiatorName"
+ "T@\"UIImage\",C,N,V_glyphAttachmentImage"
+ "TB,N,V_allowsOpaqueBackgroundColors"
+ "TB,N,V_prefersBehavioralStylePad"
+ "Tq,N,V_shape"
+ "_allowsOpaqueBackgroundColors"
+ "_backgroundColorSupportsVibrancy"
+ "_backgroundColorSupportsVibrancy:"
+ "_bottomLeadingCaptionStringWithApplicationName:originalURL:"
+ "_fixedFallbackImageFontTextStyle"
+ "_glyphAttachmentImage"
+ "_initiatorName"
+ "_initiatorNameComponents"
+ "_needsColoredGlyphsView"
+ "_prefersBehavioralStylePad"
+ "_resolveBackgroundColor"
+ "_shape"
+ "_shouldUseBlur"
+ "_subtitleView"
+ "_volumeChanged"
+ "allowsOpaqueBackgroundColors"
+ "applyToLowerTextRowStyles:"
+ "audiobook-series"
+ "book-series"
+ "configurationWithTextStyle:"
+ "defaultBackgroundColorForPlatform:"
+ "effectForBlurEffect:"
+ "fixedFallbackImageFontTextStyle"
+ "glyphAttachmentImage"
+ "hasAnyText"
+ "initiatorName"
+ "isAppleBookSeriesURL:"
+ "isSafariTabGroupLinkWithURL:"
+ "join"
+ "prefersBehavioralStylePad"
+ "q24@0:8@\"LPComponentView\"16"
+ "secondarySystemBackgroundColor"
+ "setAllowsOpaqueBackgroundColors:"
+ "setFixedFallbackImageFontTextStyle:"
+ "setGlyphAttachmentImage:"
+ "setInitiatorName:"
+ "setInitiatorNameComponents:"
+ "setPreferredVibrancy:"
+ "setPrefersBehavioralStylePad:"
+ "setTraitCollection:"
+ "shape"
+ "themePlatformForComponentView:"
+ "useLightweightMaterials"
+ "v16@?0@\"LPTextRowStyle\"8"
- "\x04\x14\x11"
- "\x04\x1a\""
- "\x12\x13\x11"
- "\x15$/\x03\x11\x16\x15q\x17!"
- "\x193\x13\x12"
- "@\"LPCollaborationFooterConfiguration\""
- "@\"SLCollaborationFooterViewModel\""
- "LPCollaborationFooterConfiguration"
- "T@\"SLCollaborationFooterViewModel\",&,N,V_viewModel"
- "_backgroundColorIsClear"
- "_bottomLeadingCaptionStringWithApplicationName:"
- "_collaborationFooterConfiguration"
- "_handleView"
- "_viewModel"
- "configurationWithViewModel:action:"
- "initWithHost:configuration:style:"
- "resolveBackgroundColor"
- "setViewModel:"
- "viewModel"

```
