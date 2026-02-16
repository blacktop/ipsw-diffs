## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-634.2.2.0.0
-  __TEXT.__text: 0xf053c
-  __TEXT.__auth_stubs: 0x2da0
-  __TEXT.__objc_methlist: 0x12178
+634.4.6.1.0
+  __TEXT.__text: 0xfc41c
+  __TEXT.__auth_stubs: 0x2e40
+  __TEXT.__objc_methlist: 0x121e0
   __TEXT.__const: 0x3754
-  __TEXT.__cstring: 0x4787
+  __TEXT.__cstring: 0x38d8
   __TEXT.__oslogstring: 0x272f
-  __TEXT.__gcc_except_tab: 0xa34
+  __TEXT.__gcc_except_tab: 0x9d8
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160
-  __TEXT.__constg_swiftt: 0x1318
-  __TEXT.__swift5_typeref: 0x2eb8
+  __TEXT.__swift5_typeref: 0x2f5e
+  __TEXT.__constg_swiftt: 0x139c
   __TEXT.__swift5_reflstr: 0x6d0
   __TEXT.__swift5_fieldmd: 0x8a4
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__swift5_proto: 0x140
+  __TEXT.__swift5_proto: 0x144
   __TEXT.__swift5_types: 0xdc
-  __TEXT.__swift5_capture: 0x748
+  __TEXT.__swift5_capture: 0x75c
   __TEXT.__swift_as_entry: 0x12c
   __TEXT.__swift_as_ret: 0x110
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x47f8
-  __TEXT.__eh_frame: 0x220c
-  __TEXT.__objc_classname: 0x313a
-  __TEXT.__objc_methname: 0x2a5cc
-  __TEXT.__objc_methtype: 0x7762
-  __TEXT.__objc_stubs: 0x206c0
-  __DATA_CONST.__got: 0x2488
-  __DATA_CONST.__const: 0x2840
+  __TEXT.__unwind_info: 0x4f50
+  __TEXT.__eh_frame: 0x21e4
+  __TEXT.__objc_classname: 0x36c7
+  __TEXT.__objc_methname: 0x2ad31
+  __TEXT.__objc_methtype: 0x7df8
+  __TEXT.__objc_stubs: 0x21140
+  __DATA_CONST.__got: 0x24a0
+  __DATA_CONST.__const: 0x2868
   __DATA_CONST.__objc_classlist: 0xad0
   __DATA_CONST.__objc_catlist: 0x408
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f58
+  __DATA_CONST.__objc_selrefs: 0x9f98
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x16e0
-  __AUTH_CONST.__const: 0x28d8
-  __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0x1df18
+  __AUTH_CONST.__auth_got: 0x1730
+  __AUTH_CONST.__const: 0x2900
+  __AUTH_CONST.__cfstring: 0x3300
+  __AUTH_CONST.__objc_const: 0x1df20
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x41e8
+  __AUTH.__objc_data: 0x40e8
   __AUTH.__data: 0x7a0
   __DATA.__objc_ivar: 0xcb0
-  __DATA.__data: 0x32e0
-  __DATA.__bss: 0x1ad8
+  __DATA.__data: 0x3258
+  __DATA.__bss: 0x1b90
   __DATA.__common: 0xd8
-  __DATA_DIRTY.__objc_data: 0x36f0
-  __DATA_DIRTY.__data: 0x430
-  __DATA_DIRTY.__bss: 0xd28
+  __DATA_DIRTY.__objc_data: 0x37f0
+  __DATA_DIRTY.__data: 0x4a0
+  __DATA_DIRTY.__bss: 0xd10
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore
   - /System/Library/PrivateFrameworks/PhotosUIPrivate.framework/PhotosUIPrivate
   - /System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting
+  - /System/Library/PrivateFrameworks/RenderBox.framework/RenderBox
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DAD26B1E-17F9-3167-A2EF-94F1B86C1222
-  Functions: 6828
-  Symbols:   21127
-  CStrings:  9167
+  UUID: D0837596-D9FC-33DB-BE00-00C7862CE933
+  Functions: 6857
+  Symbols:   21310
+  CStrings:  9153
 
Symbols:
+ +[SearchUIAppIconUtilities gridSectionLayoutMarginsFittingSize:shouldFillAvailableSpace:]
+ +[SearchUIHomeScreenAppIconView cacheForVariant:requiresCircleShape:]
+ +[SearchUIHomeScreenAppIconView cacheForVariant:requiresCircleShape:].cold.1
+ +[SearchUIHomeScreenAppIconView cacheKeyForVariant:requiresCircleShape:]
+ -[SearchUIAppIconCardSectionView layoutSubviews]
+ -[SearchUIHomeScreenAppIconView focusHighlightChicletCornerRadius]
+ -[SearchUIHomeScreenAppIconView updateFocusHighlightCornerRadius]
+ -[SearchUIPhotosAlbumImage debugIdentifier]
+ -[SearchUIPhotosImage debugIdentifier]
+ -[SearchUIPhotosLibraryImage debugIdentifier]
+ -[SearchUIPhotosMemoryImage debugIdentifier]
+ _OBJC_CLASS_$_RBDevice
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _RBImageRendererScale
+ __MergedGlobals
+ ___69+[SearchUIHomeScreenAppIconView cacheForVariant:requiresCircleShape:]_block_invoke
+ ___79-[SearchUIClockImage finishSnapshottingClockImageView:scale:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e23_v16?0"RBDisplayList"8ls32l8
+ ___block_descriptor_68_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___isPlatformVersionAtLeast
+ ___isPlatformVersionAtLeast.cold.1
+ ___isPlatformVersionAtLeast.cold.2
+ __availability_version_check
+ __initializeAvailabilityCheck
+ _cacheForVariant:requiresCircleShape:.iconCache
+ _cacheForVariant:requiresCircleShape:.onceToken
+ _compatibilityInitializeAvailabilityCheck
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _get_underlying_type_ref 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOQr.1
+ _get_underlying_witness 7SwiftUI4ViewPAAEAcAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOqd__AaBHC.2
+ _get_witness_table 7SwiftUI15NavigationStackVyAA0C4PathVAA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQOyAgAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaFRd_0_r0_lFQOyAgAE7toolbarAQQrqd__yXE_tAA14ToolbarContentRd__lFQOyAgAE18navigationBarTitle_11displayModeQrqd___AA0cW4ItemV0x7DisplayZ0OtSyRd__lFQOyAgAE9listStyleyQrqd__AA9ListStyleRd__lFQOyAA4ListVys5NeverOAA05TupleF0Vy06SearchB040SearchUIUserReportRequestSelectorSectionV_A12_37SearchUIUserReportRequestImageSectionVtGG_AA21InsetGroupedListStyleVQo__SSQo__AA05TupletU0VyAA0T4ItemVyytAA6ButtonVyAA4TextVGG_A26_yytAgAE4boldyQrSbFQOyAA08ModifiedU0VyA31_AA32_EnvironmentKeyTransformModifierVySbGG_Qo_GtGQo__A12_0R9ContainerVySSGA12_015SearchUIPrivacyF0VQo__Qo_GAaFHPyHC.30
+ _initializeAvailabilityCheck
+ _malloc
+ _objc_autorelease
+ _objc_msgSend$_layoutSizeThatFits:fixedAxes:
+ _objc_msgSend$_timeZoneAtLocation:
+ _objc_msgSend$addAnimation:forKey:
+ _objc_msgSend$addCompletion:
+ _objc_msgSend$animationWith:
+ _objc_msgSend$archive
+ _objc_msgSend$attachmentSectionTitle
+ _objc_msgSend$audioBuffer
+ _objc_msgSend$beginBackgroundTaskWithExpirationHandler:
+ _objc_msgSend$beginCGContextWithAlpha:
+ _objc_msgSend$bitsPerChannel
+ _objc_msgSend$bytesPerFrame
+ _objc_msgSend$bytesPerPacket
+ _objc_msgSend$cacheForVariant:requiresCircleShape:
+ _objc_msgSend$cacheKeyForVariant:requiresCircleShape:
+ _objc_msgSend$channelsPerFrame
+ _objc_msgSend$cloudCover
+ _objc_msgSend$cloudCoverHighAltPct
+ _objc_msgSend$cloudCoverLowAltPct
+ _objc_msgSend$cloudCoverMidAltPct
+ _objc_msgSend$contactForIdentifier:
+ _objc_msgSend$coreAnimation
+ _objc_msgSend$customViewForCardSection:withPlacement:
+ _objc_msgSend$dataProviderTypeIdentifiers
+ _objc_msgSend$debugIdentifier
+ _objc_msgSend$delay
+ _objc_msgSend$didEngageSection:
+ _objc_msgSend$directionalLayoutMargins
+ _objc_msgSend$disclaimerLearnMorePunchout
+ _objc_msgSend$disclaimerText
+ _objc_msgSend$duration
+ _objc_msgSend$endBackgroundTask:
+ _objc_msgSend$endCGContext
+ _objc_msgSend$entityIdentifer
+ _objc_msgSend$fetchPreviewImageForResult:completion:
+ _objc_msgSend$fileProviderTypeIdentifiers
+ _objc_msgSend$flow
+ _objc_msgSend$focusHighlightChicletCornerRadius
+ _objc_msgSend$formatFlags
+ _objc_msgSend$formatID
+ _objc_msgSend$formatted_text
+ _objc_msgSend$framesPerPacket
+ _objc_msgSend$gridSectionLayoutMarginsFittingSize:shouldFillAvailableSpace:
+ _objc_msgSend$headerDelegate
+ _objc_msgSend$initWithAnimationCurve:
+ _objc_msgSend$initWithCGImage:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithPerceptualDuration:bounce:
+ _objc_msgSend$initWithResult:
+ _objc_msgSend$initWithSection:triggerEvent:
+ _objc_msgSend$isAppIntentsSupportEnabled
+ _objc_msgSend$isExpandedForSectionModel:
+ _objc_msgSend$isVisionOS
+ _objc_msgSend$itemProviderForContact:withContactStore:
+ _objc_msgSend$linkWithBundleIdentifier:
+ _objc_msgSend$localizedButtonTitle
+ _objc_msgSend$moreResultsPunchout
+ _objc_msgSend$opaqueSessionID
+ _objc_msgSend$propertyAnimator
+ _objc_msgSend$provideDataForBundle:itemIdentifier:typeIdentifier:options:completionHandler:
+ _objc_msgSend$provideFileURLForBundle:itemIdentifier:typeIdentifier:options:completionHandler:
+ _objc_msgSend$providerLogoWithCompletionHandler:
+ _objc_msgSend$providerNameWithCompletionHandler:
+ _objc_msgSend$recycleCustomView:forCardSection:withPlacement:
+ _objc_msgSend$registerDataRepresentationForTypeIdentifier:visibility:loadHandler:
+ _objc_msgSend$renderImageInRect:options:renderer:
+ _objc_msgSend$reportOptionsSectionTitle
+ _objc_msgSend$reserved
+ _objc_msgSend$respondsToSelector:
+ _objc_msgSend$sampleRate
+ _objc_msgSend$scrollButtonDelegate
+ _objc_msgSend$scrollSection:direction:
+ _objc_msgSend$secondarySystemGroupedBackgroundColor
+ _objc_msgSend$setActive:withOptions:error:
+ _objc_msgSend$setAnimations:
+ _objc_msgSend$setCategory:mode:options:error:
+ _objc_msgSend$setDuration:
+ _objc_msgSend$setFromValue:
+ _objc_msgSend$setIsSelected:
+ _objc_msgSend$setKeyPath:
+ _objc_msgSend$setToValue:
+ _objc_msgSend$sharedDefaultDevice
+ _objc_msgSend$supportsConfiguration
+ _objc_msgSend$symbolImage
+ _objc_msgSend$text_1
+ _objc_msgSend$text_2
+ _objc_msgSend$text_3
+ _objc_msgSend$text_elements
+ _objc_msgSend$typeIdentifer
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateFocusHighlightCornerRadius
+ _objectdestroy.13Tm
+ _objectdestroy.5Tm
+ _rewind
+ _sscanf
+ _swift_bridgeObjectRelease_n
+ _symbolic _____y__________y_____y_____y_____y_____y_____y__________y___________tGG______Qo__SSQo_______y_____yyt_____y_____GG_ANyyt_____y_____yAQ_____ySbGG_Qo_GtGQo_______ySSG_____Qo__Qo_G 7SwiftUI15NavigationStackV AA0C4PathV AA4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AgAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaFRd_0_r0_lFQO AgAE7toolbarAQQrqd__yXE_tAA14ToolbarContentRd__lFQO AgAE18navigationBarTitle_11displayModeQrqd___AA0cW4ItemV0x7DisplayZ0OtSyRd__lFQO AgAE9listStyleyQrqd__AA9ListStyleRd__lFQO AA4ListV s5NeverO AA05TupleF0V 06SearchB040SearchUIUserReportRequestSelectorSectionV A12_37SearchUIUserReportRequestImageSectionV AA21InsetGroupedListStyleV AA05TupletU0V AA0T4ItemV AA6ButtonV AA4TextV AgAE4boldyQrSbFQO AA08ModifiedU0V AA32_EnvironmentKeyTransformModifierV A12_0R9ContainerV A12_015SearchUIPrivacyF0V
+ _symbolic _____y_____y_____y_____y_____y_____y__________y___________tGG______Qo__SSQo_______y_____yyt_____y_____GG_ALyyt_____y_____yAO_____ySbGG_Qo_GtGQo_______ySSG_____Qo__Qo_ 7SwiftUI4ViewPAAE4task4name8priority4file4line_QrSSSg_ScPSSSiyyYaYAcntFQO AcAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaBRd_0_r0_lFQO AcAE7toolbarAMQrqd__yXE_tAA14ToolbarContentRd__lFQO AcAE18navigationBarTitle_11displayModeQrqd___AA010NavigationT4ItemV0u7DisplayW0OtSyRd__lFQO AcAE9listStyleyQrqd__AA9ListStyleRd__lFQO AA4ListV s5NeverO AA05TupleC0V 06SearchB040SearchUIUserReportRequestSelectorSectionV A8_37SearchUIUserReportRequestImageSectionV AA21InsetGroupedListStyleV AA05TupleqR0V AA0qY0V AA6ButtonV AA4TextV AcAE4boldyQrSbFQO AA08ModifiedR0V AA32_EnvironmentKeyTransformModifierV A8_0O9ContainerV A8_015SearchUIPrivacyC0V
+ _symbolic _____y_____y_____y_____y_____y_____y__________y___________tGG______Qo__SSQo_______y_____yyt_____y_____GG_AMyyt_____yAAyAP_____ySbGG_Qo_GtGQo_______ySSG_____Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaDRd_0_r0_lFQO AeAE7toolbarAIQrqd__yXE_tAA07ToolbarD0Rd__lFQO AeAE18navigationBarTitle_11displayModeQrqd___AA010NavigationP4ItemV0q7DisplayS0OtSyRd__lFQO AeAE9listStyleyQrqd__AA04ListX0Rd__lFQO AA0Y0V s5NeverO AA05TupleE0V 06SearchB040SearchUIUserReportRequestSelectorSectionV A4_37SearchUIUserReportRequestImageSectionV AA012InsetGroupedyX0V AA05TuplenD0V AA0nU0V AA6ButtonV AA4TextV AeAE4boldyQrSbFQO AA32_EnvironmentKeyTransformModifierV A4_0L9ContainerV A4_015SearchUIPrivacyE0V AA14_TaskModifier2V
- +[SearchUIHomeScreenAppIconView cacheForVariant:]
- +[SearchUIHomeScreenAppIconView cacheForVariant:].cold.1
- -[SearchUIHomeScreenAppIconView focusHighlightCornerRadius]
- _OBJC_CLASS_$_UIGraphicsImageRenderer
- _OBJC_CLASS_$_UIGraphicsImageRendererFormat
- ___49+[SearchUIHomeScreenAppIconView cacheForVariant:]_block_invoke
- ___block_descriptor_40_e8_32s_e40_v16?0"UIGraphicsImageRendererContext"8ls32l8
- ___block_descriptor_67_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- _cacheForVariant:.iconCache
- _cacheForVariant:.onceToken
- _get_witness_table 7SwiftUI15NavigationStackVyAA0C4PathVAA15ModifiedContentVyAA4ViewPAAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaHRd_0_r0_lFQOyAiAE7toolbarAMQrqd__yXE_tAA07ToolbarG0Rd__lFQOyAiAE18navigationBarTitle_11displayModeQrqd___AA0cS4ItemV0t7DisplayV0OtSyRd__lFQOyAiAE9listStyleyQrqd__AA04ListZ0Rd__lFQOyAA4ListVys5NeverOAA05TupleH0Vy06SearchB040SearchUIUserReportRequestSelectorSectionV_A8_37SearchUIUserReportRequestImageSectionVtGG_AA016InsetGroupedListZ0VQo__SSQo__AA05TupleqG0VyAA0qW0VyytAA6ButtonVyAA4TextVGG_A22_yytAiAE4boldyQrSbFQOyAGyA27_AA32_EnvironmentKeyTransformModifierVySbGG_Qo_GtGQo__A8_0O9ContainerVySSGA8_015SearchUIPrivacyH0VQo_AA13_TaskModifierVGGAaHHPyHC.25
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$CGContext
- _objc_msgSend$_setFocusStyle:
- _objc_msgSend$cacheForVariant:
- _objc_msgSend$focusHighlightCornerRadius
- _objc_msgSend$imageWithActions:
- _objc_msgSend$initWithSize:format:
- _objc_msgSend$isXROS
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _objectdestroy.4Tm
- _symbolic _____y______Qo_ 7SwiftUI4ViewPAAE10fontWeightyQrAA4FontV0E0VSgFQO AA5ImageV
- _symbolic _____y__________y_____y_____y_____y_____y_____y__________y___________tGG______Qo__SSQo_______y_____yyt_____y_____GG_AOyyt_____yACyAR_____ySbGG_Qo_GtGQo_______ySSG_____Qo______GG 7SwiftUI15NavigationStackV AA0C4PathV AA15ModifiedContentV AA4ViewPAAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaHRd_0_r0_lFQO AiAE7toolbarAMQrqd__yXE_tAA07ToolbarG0Rd__lFQO AiAE18navigationBarTitle_11displayModeQrqd___AA0cS4ItemV0t7DisplayV0OtSyRd__lFQO AiAE9listStyleyQrqd__AA04ListZ0Rd__lFQO AA4ListV s5NeverO AA05TupleH0V 06SearchB040SearchUIUserReportRequestSelectorSectionV A8_37SearchUIUserReportRequestImageSectionV AA016InsetGroupedListZ0V AA05TupleqG0V AA0qW0V AA6ButtonV AA4TextV AiAE4boldyQrSbFQO AA32_EnvironmentKeyTransformModifierV A8_0O9ContainerV A8_015SearchUIPrivacyH0V AA13_TaskModifierV
- _symbolic _____y_____y_____y_____y_____y_____y__________y___________tGG______Qo__SSQo_______y_____yyt_____y_____GG_AMyyt_____yAAyAP_____ySbGG_Qo_GtGQo_______ySSG_____Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaDRd_0_r0_lFQO AeAE7toolbarAIQrqd__yXE_tAA07ToolbarD0Rd__lFQO AeAE18navigationBarTitle_11displayModeQrqd___AA010NavigationP4ItemV0q7DisplayS0OtSyRd__lFQO AeAE9listStyleyQrqd__AA04ListX0Rd__lFQO AA0Y0V s5NeverO AA05TupleE0V 06SearchB040SearchUIUserReportRequestSelectorSectionV A4_37SearchUIUserReportRequestImageSectionV AA012InsetGroupedyX0V AA05TuplenD0V AA0nU0V AA6ButtonV AA4TextV AeAE4boldyQrSbFQO AA32_EnvironmentKeyTransformModifierV A4_0L9ContainerV A4_015SearchUIPrivacyE0V AA13_TaskModifierV
CStrings:
+ "%@-Unknown"
+ "%d.%d.%d"
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "@28@0:8Q16B24"
+ "Album-%@"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "Library-%@"
+ "Memory-%@"
+ "ProductVersion"
+ "SearchUIArchivedRowModel"
+ "SearchUIContentConfigurator"
+ "SearchUICustomViewCardSectionView"
+ "SearchUICustomViewRowModel"
+ "SearchUIMusicUtilities"
+ "SearchUIRFCardSectionRowModel"
+ "SearchUIRFCardSectionRowModelProvider"
+ "SearchUISupplementaryIdentifiers"
+ "SearchUIWeatherColor"
+ "T@\"SFCopyItem\",&,N"
+ "View.task @ SearchUI/SearchUIUserReportRequestView.swift:"
+ "beginCGContextWithAlpha:"
+ "cacheForVariant:requiresCircleShape:"
+ "cacheKeyForVariant:requiresCircleShape:"
+ "com.apple.mobilemail"
+ "debugIdentifier"
+ "directionalLayoutMargins"
+ "endCGContext"
+ "focusHighlightChicletCornerRadius"
+ "gridSectionLayoutMarginsFittingSize:shouldFillAvailableSpace:"
+ "initWithCGImage:"
+ "initWithResult:"
+ "isVisionOS"
+ "kCFAllocatorNull"
+ "r"
+ "renderImageInRect:options:renderer:"
+ "requestDismissal"
+ "sharedDefaultDevice"
+ "updateFocusHighlightCornerRadius"
+ "v16@?0@\"RBDisplayList\"8"
+ "{NSDirectionalEdgeInsets=dddd}36@0:8{CGSize=dd}16B32"
- "CGContext"
- "T@\"SFCopyItem\",N"
- "_setFocusStyle:"
- "cacheForVariant:"
- "focusHighlightCornerRadius"
- "imageWithActions:"
- "initWithSize:format:"
- "isXROS"
- "v16@?0@\"UIGraphicsImageRendererContext\"8"

```
