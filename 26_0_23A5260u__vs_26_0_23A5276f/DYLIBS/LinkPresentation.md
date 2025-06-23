## LinkPresentation

> `/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`

```diff

-284.1.0.0.0
-  __TEXT.__text: 0xfd68c
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x107c4
-  __TEXT.__cstring: 0x9320
-  __TEXT.__gcc_except_tab: 0x21dcc
+285.0.0.0.0
+  __TEXT.__text: 0xfe078
+  __TEXT.__auth_stubs: 0x1c00
+  __TEXT.__objc_methlist: 0x1085c
+  __TEXT.__cstring: 0x9350
+  __TEXT.__gcc_except_tab: 0x21eec
   __TEXT.__const: 0x1db4
   __TEXT.__ustring: 0x3cc
-  __TEXT.__oslogstring: 0x3aab
+  __TEXT.__oslogstring: 0x3aeb
   __TEXT.__dlopen_cstrs: 0x9c7
   __TEXT.__swift5_typeref: 0x880
   __TEXT.__constg_swiftt: 0x748

   __TEXT.__swift5_capture: 0x1f8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
-  __TEXT.__unwind_info: 0x7a08
+  __TEXT.__unwind_info: 0x7a48
   __TEXT.__eh_frame: 0x5b0
-  __TEXT.__objc_classname: 0x2425
-  __TEXT.__objc_methname: 0x21b14
-  __TEXT.__objc_methtype: 0x48b2
-  __TEXT.__objc_stubs: 0x17e80
+  __TEXT.__objc_classname: 0x2426
+  __TEXT.__objc_methname: 0x21d13
+  __TEXT.__objc_methtype: 0x48c9
+  __TEXT.__objc_stubs: 0x17fc0
   __DATA_CONST.__got: 0xdb0
-  __DATA_CONST.__const: 0x2550
+  __DATA_CONST.__const: 0x2558
   __DATA_CONST.__objc_classlist: 0x8d0
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7668
+  __DATA_CONST.__objc_selrefs: 0x76b8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x670
   __DATA_CONST.__objc_arraydata: 0x1538
-  __AUTH_CONST.__auth_got: 0xe10
-  __AUTH_CONST.__const: 0x1a80
-  __AUTH_CONST.__cfstring: 0xda40
-  __AUTH_CONST.__objc_const: 0x2da80
+  __AUTH_CONST.__auth_got: 0xe18
+  __AUTH_CONST.__const: 0x1aa0
+  __AUTH_CONST.__cfstring: 0xdaa0
+  __AUTH_CONST.__objc_const: 0x2db50
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH.__objc_data: 0x3138
   __AUTH.__data: 0x458
-  __DATA.__objc_ivar: 0x179c
+  __DATA.__objc_ivar: 0x17b0
   __DATA.__data: 0x1cd8
-  __DATA.__bss: 0x1580
+  __DATA.__bss: 0x1590
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x2968
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 53719FE1-CC97-3AFE-837C-7EE1490670A5
-  Functions: 6415
-  Symbols:   22616
-  CStrings:  10425
+  UUID: BA1D50FE-290D-3C91-B6E5-D27CE1FCFD6D
+  Functions: 6433
+  Symbols:   22667
+  CStrings:  10450
 
Symbols:
+ +[LPImage _optionalSystemImageNamed:withSymbolConfiguration:]
+ +[NSItemProvider(LPExtras) _lp_itemProviderWithData:MIMEType:].cold.1
+ -[LPCaptionButtonCollapsedPresentationProperties attributedText]
+ -[LPCaptionButtonCollapsedPresentationProperties setAttributedText:]
+ -[LPCaptionButtonCollapsedPresentationProperties setShouldCollapseWhenCompressed:]
+ -[LPCaptionButtonCollapsedPresentationProperties setShouldHideIconsWhenCollapsed:]
+ -[LPCaptionButtonCollapsedPresentationProperties shouldCollapseWhenCompressed]
+ -[LPCaptionButtonCollapsedPresentationProperties shouldHideIconsWhenCollapsed]
+ -[LPLinkView _URLToOpen]
+ -[LPLinkView _computeCollapsedButtonPropertiesForAttributedString:]
+ -[LPLinkView _hasMedia]
+ -[LPLinkView _setPresentationPropertiesInternal:]
+ -[LPVideo _mediaServicesWereReset]
+ -[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]
+ -[LPiCloudSharingMetadataProviderSpecialization completeUsingApplication:kind:title:thumbnail:icon:]
+ -[LPiCloudSharingMetadataProviderSpecialization completeUsingApplication:kind:title:thumbnail:icon:].cold.1
+ -[UIColor(LPExtras) _lp_isDynamicColor]
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table156
+ GCC_except_table166
+ GCC_except_table173
+ GCC_except_table179
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table200
+ GCC_except_table215
+ GCC_except_table216
+ GCC_except_table221
+ GCC_except_table233
+ GCC_except_table236
+ GCC_except_table310
+ GCC_except_table312
+ GCC_except_table314
+ _LPLogChannelTypes
+ _LPLogChannelTypes.cold.1
+ _LPLogChannelTypes.log
+ _LPLogChannelTypes.onceToken
+ _OBJC_IVAR_$_LPCaptionButtonCollapsedPresentationProperties._attributedText
+ _OBJC_IVAR_$_LPCaptionButtonCollapsedPresentationProperties._shouldCollapseWhenCompressed
+ _OBJC_IVAR_$_LPCaptionButtonCollapsedPresentationProperties._shouldHideIconsWhenCollapsed
+ _OBJC_IVAR_$_LPImage._placeholderProperties
+ _OBJC_IVAR_$_LPLinkView._overrideURLFromProperties
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke.50
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke.53
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke.59
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke.cold.1
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke_2
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke_2.57
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke_2.57.cold.1
+ ___121-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:]_block_invoke_2.cold.1
+ ___67-[LPLinkView _computeCollapsedButtonPropertiesForAttributedString:]_block_invoke
+ ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.274
+ ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.277
+ ___LPLogChannelTypes_block_invoke
+ ___block_descriptor_145_ea8_32s_e5_B8?0ls32l8
+ ___block_descriptor_48_ea8_32r40r_e27_v40?08{_NSRange=QQ}16^B32lr32l8r40l8
+ ___block_descriptor_72_ea8_32s40s48s56s64s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_ea8_32s40s48s56s64s72s_e47_v24?0"QLThumbnailRepresentation"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_ea8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_ea8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s80l8
+ ___block_literal_global.104
+ ___block_literal_global.130
+ ___block_literal_global.213
+ ___block_literal_global.218
+ ___block_literal_global.245
+ ___block_literal_global.28
+ ___block_literal_global.340
+ _dispatch_assert_queue$V2
+ _objc_msgSend$_URLToOpen
+ _objc_msgSend$_computeCollapsedButtonPropertiesForAttributedString:
+ _objc_msgSend$_lp_isDynamicColor
+ _objc_msgSend$_mediaServicesWereReset
+ _objc_msgSend$_optionalSystemImageNamed:withSymbolConfiguration:
+ _objc_msgSend$_setPresentationPropertiesInternal:
+ _objc_msgSend$completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:
+ _objc_msgSend$completeUsingApplication:kind:title:thumbnail:icon:
+ _objc_msgSend$setShouldCollapseWhenCompressed:
+ _objc_msgSend$setShouldHideIconsWhenCollapsed:
+ _objc_msgSend$shouldCollapseWhenCompressed
+ _objc_msgSend$shouldHideIconsWhenCollapsed
- -[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]
- -[LPiCloudSharingMetadataProviderSpecialization completeUsingApplication:kind:title:thumbnail:]
- -[LPiCloudSharingMetadataProviderSpecialization completeUsingApplication:kind:title:thumbnail:].cold.1
- GCC_except_table128
- GCC_except_table136
- GCC_except_table145
- GCC_except_table159
- GCC_except_table184
- GCC_except_table193
- GCC_except_table195
- GCC_except_table203
- GCC_except_table204
- GCC_except_table213
- GCC_except_table220
- GCC_except_table231
- GCC_except_table305
- GCC_except_table307
- GCC_except_table308
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke.50
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke.53
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke.59
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke.cold.1
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke_2
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke_2.57
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke_2.57.cold.1
- ___116-[LPiCloudSharingMetadataProviderSpecialization completeRetrievingThumbnailForShareMetadata:application:kind:title:]_block_invoke_2.cold.1
- ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.270
- ___78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.273
- ___block_descriptor_40_ea8_32s_e24_v16?0"NSNotification"8ls32l8
- ___block_descriptor_64_ea8_32s40s48s56s_e27_v24?0"NSURL"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_ea8_32s40s48s56s64s_e47_v24?0"QLThumbnailRepresentation"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_ea8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
- ___block_descriptor_97_ea8_32s_e5_B8?0ls32l8
- ___block_literal_global.124
- ___block_literal_global.214
- ___block_literal_global.241
- ___block_literal_global.335
- ___block_literal_global.338
- ___block_literal_global.98
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_LinkPresentation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_LinkPresentation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_LinkPresentation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_LinkPresentation
- _objc_msgSend$completeRetrievingThumbnailForShareMetadata:application:kind:title:
- _objc_msgSend$completeUsingApplication:kind:title:thumbnail:
CStrings:
+ "Creating item provider for dynamic UTI, from unknown MIME type '%@'"
+ "TB,N,V_shouldCollapseWhenCompressed"
+ "TB,N,V_shouldHideIconsWhenCollapsed"
+ "Types"
+ "_URLToOpen"
+ "_computeCollapsedButtonPropertiesForAttributedString:"
+ "_lp_isDynamicColor"
+ "_mediaServicesWereReset"
+ "_optionalSystemImageNamed:withSymbolConfiguration:"
+ "_overrideURLFromProperties"
+ "_placeholderProperties"
+ "_setPresentationPropertiesInternal:"
+ "_shouldCollapseWhenCompressed"
+ "_shouldHideIconsWhenCollapsed"
+ "com.microsoft.ico"
+ "completeRetrievingThumbnailForShareMetadata:application:kind:title:icon:"
+ "completeUsingApplication:kind:title:thumbnail:icon:"
+ "dyn."
+ "ico"
+ "messages://open"
+ "setShouldCollapseWhenCompressed:"
+ "setShouldHideIconsWhenCollapsed:"
+ "shouldCollapseWhenCompressed"
+ "shouldHideIconsWhenCollapsed"
+ "v56@0:8@16@24@32@40@48"
+ "\xf0\xf0\xf0\xe1"
- "completeRetrievingThumbnailForShareMetadata:application:kind:title:"
- "completeUsingApplication:kind:title:thumbnail:"
- "sms://open"
- "\xf0\xf0\xf0\xd1"

```
