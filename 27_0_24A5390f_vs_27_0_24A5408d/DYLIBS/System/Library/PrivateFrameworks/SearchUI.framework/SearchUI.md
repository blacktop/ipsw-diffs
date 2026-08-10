## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__data`

```diff

-673.0.6.0.0
-  __TEXT.__text: 0xf58a0
+673.0.12.102.0
+  __TEXT.__text: 0xf587c
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x123d8
-  __TEXT.__const: 0x3a74
-  __TEXT.__cstring: 0x3aa9
+  __TEXT.__objc_methlist: 0x12430
+  __TEXT.__const: 0x3a84
+  __TEXT.__cstring: 0x3a79
   __TEXT.__oslogstring: 0x2915
-  __TEXT.__gcc_except_tab: 0xa00
+  __TEXT.__gcc_except_tab: 0xa18
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160
   __TEXT.__swift5_typeref: 0x3992

   __TEXT.__swift_as_cont: 0x1c8
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4870
+  __TEXT.__unwind_info: 0x48b8
   __TEXT.__eh_frame: 0x2334
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x28a0
-  __DATA_CONST.__objc_classlist: 0xae0
+  __DATA_CONST.__objc_classlist: 0xad8
   __DATA_CONST.__objc_catlist: 0x410
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6f8
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x2578
+  __DATA_CONST.__got: 0x2568
   __AUTH_CONST.__const: 0x2ab0
-  __AUTH_CONST.__cfstring: 0x33c0
-  __AUTH_CONST.__objc_const: 0x1e028
+  __AUTH_CONST.__cfstring: 0x3360
+  __AUTH_CONST.__objc_const: 0x1dff8
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__auth_got: 0x1900
   __AUTH.__objc_data: 0x4750
   __AUTH.__data: 0x7c8
-  __DATA.__objc_ivar: 0xcf4
-  __DATA.__data: 0x3384
+  __DATA.__objc_ivar: 0xcfc
+  __DATA.__data: 0x3374
   __DATA.__bss: 0x1c60
   __DATA.__common: 0xe8
-  __DATA_DIRTY.__objc_data: 0x3258
+  __DATA_DIRTY.__objc_data: 0x3208
   __DATA_DIRTY.__data: 0x4b0
-  __DATA_DIRTY.__bss: 0xce8
+  __DATA_DIRTY.__bss: 0xcd8
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6996
-  Symbols:   15787
-  CStrings:  826
+  Functions: 7004
+  Symbols:   15785
+  CStrings:  824
 
Symbols:
+ +[SearchUIAppIconUtilities idealHorizontalSpacingBetweenAppIconsForWidth:]
+ +[SearchUIAppIconUtilities numberOfAppIconsPerRowForWidth:]
+ +[SearchUIHomeScreenAppIconView iconImageInfoForVariant:requiresCircleShape:]
+ +[SearchUIUtilities isCampoProcess]
+ +[SearchUIUtilities openApplicationOptionsSpotlightSource:]
+ +[SearchUIUtilities openPunchout:presentationSource:]
+ +[SearchUIUtilities openPunchout:presentationSource:completion:]
+ +[SearchUIUtilities openURL:presentationSource:withCompletion:]
+ +[SearchUIUtilities requestClipInstallWithURL:presentationSource:completion:]
+ -[SFAppIconCardSection(SearchUILeadingTrailingSectionModel) searchUILeadingTrailingSectionModel_leadingFractionalWidthForContainerWidth:]
+ -[SFCardSection(SearchUILeadingTrailingSectionModel) searchUILeadingTrailingSectionModel_leadingFractionalWidthForContainerWidth:]
+ -[SearchUIBackgroundColorView currentColorRequestId]
+ -[SearchUIBackgroundColorView setCurrentColorRequestId:]
+ -[SearchUICollectionViewController searchui_contentColumnWidthForContainerWidth:]
+ -[SearchUIColorRequest requestId]
+ -[SearchUIColorRequest setRequestId:]
+ -[SearchUICommandEnvironment presentationSource]
+ -[SearchUICommandEnvironment setPresentationSource:]
+ -[SearchUIMultiResultCollectionView updateVisibleCountForWidthIfNeeded]
+ -[SearchUIResultsViewController frameForChildViewControllers]
+ GCC_except_table105
+ GCC_except_table22
+ _OBJC_IVAR_$_SearchUIBackgroundColorView._currentColorRequestId
+ _OBJC_IVAR_$_SearchUIColorRequest._requestId
+ _OBJC_IVAR_$_SearchUICommandEnvironment._presentationSource
+ _SearchUIAppIconsPerRowForWidth
+ _SearchUISpotlightColumnTopMargin
+ _SearchUISpotlightContentColumnWidth
+ _SearchUISpotlightMaxContentWidth
+ ___35+[SearchUIUtilities isCampoProcess]_block_invoke
+ ___63+[SearchUIUtilities openURL:presentationSource:withCompletion:]_block_invoke
+ ___67-[SearchUIPhotoAssetCache computeObjectsForKeys:completionHandler:]_block_invoke
+ ___67-[SearchUIPhotoAssetCache computeObjectsForKeys:completionHandler:]_block_invoke_2
+ ___77+[SearchUIUtilities requestClipInstallWithURL:presentationSource:completion:]_block_invoke
+ ___block_descriptor_64_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56r_e44_v16?0"SearchUIResolvedBackgroundColoring"8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_73_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ _computeObjectsForKeys:completionHandler:.onceToken
+ _computeObjectsForKeys:completionHandler:.queue
+ _isCampoProcess.isCampoProcess
+ _isCampoProcess.onceToken
+ _objc_msgSend$currentColorRequestId
+ _objc_msgSend$frameForChildViewControllers
+ _objc_msgSend$iconImageInfoForVariant:requiresCircleShape:
+ _objc_msgSend$idealHorizontalSpacingBetweenAppIconsForWidth:
+ _objc_msgSend$isCampoProcess
+ _objc_msgSend$numberOfAppIconsPerRowForWidth:
+ _objc_msgSend$openApplicationOptionsSpotlightSource:
+ _objc_msgSend$openPunchout:presentationSource:
+ _objc_msgSend$openPunchout:presentationSource:completion:
+ _objc_msgSend$openURL:presentationSource:withCompletion:
+ _objc_msgSend$presentationSource
+ _objc_msgSend$requestClipInstallWithURL:presentationSource:completion:
+ _objc_msgSend$requestId
+ _objc_msgSend$searchUILeadingTrailingSectionModel_leadingFractionalWidthForContainerWidth:
+ _objc_msgSend$setPresentationSource:
+ _objc_msgSend$setRequestId:
+ _objc_msgSend$updateVisibleCountForWidthIfNeeded
- +[SearchUIAppIconUtilities idealHorizontalSpacingBetweenAppIconsForContainerWidth:insets:]
- +[SearchUIHomeScreenAppIconView cacheForVariant:requiresCircleShape:]
- +[SearchUIHomeScreenAppIconView cacheKeyForVariant:requiresCircleShape:]
- +[SearchUIUtilities openApplicationOptions]
- -[SearchUIBackgroundColorView currentColorRequest]
- -[SearchUIHomeScreenAppIconView currentIconIsPlaceholder]
- -[SearchUIHomeScreenAppIconView hidePlaceholder:]
- -[SearchUIHomeScreenAppIconView iconImageViewDidChangeContents:forIcon:]
- -[SearchUIHomeScreenAppIconView imageLoadingBehavior]
- -[SearchUIHomeScreenAppIconView placeholderView]
- -[SearchUIHomeScreenAppIconView removePlaceholderAndSetShadowAnimated:]
- -[SearchUIHomeScreenAppIconView setPlaceholderView:]
- -[SearchUIIconImageCache genericImage]
- GCC_except_table103
- GCC_except_table21
- _OBJC_CLASS_$_SBHClockApplicationIcon
- _OBJC_CLASS_$_SBHIconImageCache
- _OBJC_CLASS_$_SearchUIIconImageCache
- _OBJC_IVAR_$_SearchUIHomeScreenAppIconView._placeholderView
- _OBJC_METACLASS_$_SBHIconImageCache
- _OBJC_METACLASS_$_SearchUIIconImageCache
- _SearchUIPlaceholderIconIdentifier
- __OBJC_$_INSTANCE_METHODS_SearchUIIconImageCache
- __OBJC_CLASS_RO_$_SearchUIIconImageCache
- __OBJC_METACLASS_RO_$_SearchUIIconImageCache
- ___43+[SearchUIUtilities openApplicationOptions]_block_invoke
- ___44+[SearchUIUtilities openURL:withCompletion:]_block_invoke
- ___58+[SearchUIUtilities requestClipInstallWithURL:completion:]_block_invoke
- ___69+[SearchUIHomeScreenAppIconView cacheForVariant:requiresCircleShape:]_block_invoke
- ___71-[SearchUIHomeScreenAppIconView removePlaceholderAndSetShadowAnimated:]_block_invoke
- ___76+[SearchUILaunchAppHandler openApplicationWithBundleIdentifier:environment:]_block_invoke_2
- ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_65_e8_32s40s48s56s_e44_v16?0"SearchUIResolvedBackgroundColoring"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_66_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- _cacheForVariant:requiresCircleShape:.iconCache
- _cacheForVariant:requiresCircleShape:.onceToken
- _idealHorizontalSpacingBetweenAppIcons.spacing
- _objc_msgSend$_iconImageView
- _objc_msgSend$cacheForVariant:requiresCircleShape:
- _objc_msgSend$cacheKeyForVariant:requiresCircleShape:
- _objc_msgSend$currentIconIsPlaceholder
- _objc_msgSend$hidePlaceholder:
- _objc_msgSend$idealHorizontalSpacingBetweenAppIcons
- _objc_msgSend$idealHorizontalSpacingBetweenAppIconsForContainerWidth:insets:
- _objc_msgSend$initWithName:iconImageInfo:
- _objc_msgSend$leafIdentifier
- _objc_msgSend$openApplicationOptions
- _objc_msgSend$openURL:withCompletion:
- _objc_msgSend$placeholderView
- _objc_msgSend$removePlaceholderAndSetShadowAnimated:
- _objc_msgSend$requestClipInstallWithURL:completion:
- _objc_msgSend$setContentsScale:
- _objc_msgSend$setIconImageCache:
- _objc_msgSend$setImageLoadingBehavior:
- _objc_msgSend$setPlaceholderView:
- _objc_msgSend$setPunchoutShadow:
- _openApplicationOptions.onceToken
- _openApplicationOptions.options
- _openApplicationWithBundleIdentifier:environment:.onceToken
- _openApplicationWithBundleIdentifier:environment:.openApplicationService
CStrings:
+ "Campo"
+ "com.apple.searchui.SearchUIPhotoAssetCache"
- "-%@"
- "Identifier:AppIconButton,AppName:%@"
- "SearchUIIconImageCache"
- "searchUIPlaceholderIcon"
```
