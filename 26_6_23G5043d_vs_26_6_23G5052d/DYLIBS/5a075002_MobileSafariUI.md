## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-  __TEXT.__text: 0x27e6f8
+  __TEXT.__text: 0x27e9b0
   __TEXT.__auth_stubs: 0x3f80
   __TEXT.__objc_methlist: 0x23154
   __TEXT.__const: 0x2418
-  __TEXT.__gcc_except_tab: 0x1d684
+  __TEXT.__gcc_except_tab: 0x1d674
   __TEXT.__cstring: 0xed70
   __TEXT.__dlopen_cstrs: 0x83a
   __TEXT.__oslogstring: 0x9e38

   __TEXT.__unwind_info: 0xe398
   __TEXT.__eh_frame: 0x1768
   __TEXT.__objc_classname: 0x496d
-  __TEXT.__objc_methname: 0x6ffd0
+  __TEXT.__objc_methname: 0x6fff0
   __TEXT.__objc_methtype: 0x15ad7
-  __TEXT.__objc_stubs: 0x493e0
-  __DATA_CONST.__got: 0x2f28
+  __TEXT.__objc_stubs: 0x49440
+  __DATA_CONST.__got: 0x2f30
   __DATA_CONST.__const: 0x8c78
   __DATA_CONST.__objc_classlist: 0x980
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xb00
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16f38
+  __DATA_CONST.__objc_selrefs: 0x16f48
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0x6a8
   __DATA_CONST.__objc_arraydata: 0x370

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 13955
-  Symbols:   45155
-  CStrings:  22380
+  Symbols:   45159
+  CStrings:  22382
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __TEXT.__objc_classname : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__objc_ivar : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[CompletionListTableViewCell updateIconAppearanceAndConfiguration]
+ _OBJC_CLASS_$_CALayer
+ _OBJC_IVAR_$_BrowserRootViewController._suppressBannerContentOffsetAdjustment
+ ___114-[BrowserRootViewController capsuleNavigationBarViewController:selectedItemWillChangeToState:options:coordinator:]_block_invoke.285
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"UIImage"8lw40l8s32l8
+ ___block_literal_global.1135
+ ___block_literal_global.178
+ ___block_literal_global.184
+ _objc_msgSend$iconForSystemImageName:iconConfiguration:
+ _objc_msgSend$mask
+ _objc_msgSend$setDisableActions:
+ _objc_msgSend$setMask:
+ _objc_msgSend$updateIconAppearanceAndConfiguration
- -[CompletionListTableViewCell _updateIconForCurrentAppearance]
- _OBJC_IVAR_$_CompletionList._urlStringsForInProgressSearchSuggestionImageLoads
- ___114-[BrowserRootViewController capsuleNavigationBarViewController:selectedItemWillChangeToState:options:coordinator:]_block_invoke.283
- ___block_descriptor_56_e8_32s40s48w_e17_v16?0"UIImage"8lw48l8s32l8s40l8
- ___block_literal_global.179
- ___block_literal_global.185
- _objc_msgSend$filenameWithoutExtension
- _objc_msgSend$iconForSystemImageName:isDarkMode:
Functions:
~ ___46-[BrowserRootViewController _layOutTopBanners]_block_invoke.181 : 804 -> 1348
~ -[BrowserRootViewController _transitionFromBanner:toBanner:animated:] : 1096 -> 1128
~ -[BrowserRootViewController tabDocumentView:contentOffsetAdjustmentEdgeWithPreviousContentInset:] : 336 -> 364
~ -[SearchSuggestion _configureImageForTableViewCellIfNeeded:completionList:usingBottomCapsule:] : 956 -> 928
~ -[TabDocument _setAppBannerWhenPainted:] : 272 -> 280
~ -[TabDocument _webView:renderingProgressDidChange:] : 872 -> 896
~ -[TabDocument didFindAppBannerWithContent:] : 348 -> 360
~ -[TabDocument currentSearchQuery] : 244 -> 192
~ -[TabDocument currentSearchQueryAllowingQueryThatLooksLikeURL] : 248 -> 192
~ ___138+[CompletionListTableViewController configureCell:backgroundMode:separatorStyle:shouldHaveTopPadding:configurationStateDidChangeCallback:]_block_invoke : 412 -> 528
~ -[CompletionList _updateCompletionListing] : 1820 -> 1816
~ -[CompletionList _requestSearchSuggestionImages] : 748 -> 600
~ ___48-[CompletionList _requestSearchSuggestionImages]_block_invoke : 192 -> 184
~ -[CompletionList .cxx_destruct] : 584 -> 572
~ -[CompletionListTableViewCell _updateIconForCurrentAppearance] -> -[CompletionListTableViewCell updateIconAppearanceAndConfiguration] : 424 -> 652
~ -[DownloadTableViewCell initWithStyle:reuseIdentifier:] : 2324 -> 2336
CStrings:
+ "_suppressBannerContentOffsetAdjustment"
+ "iconForSystemImageName:iconConfiguration:"
+ "setDisableActions:"
+ "setMask:"
+ "updateIconAppearanceAndConfiguration"
- "_updateIconForCurrentAppearance"
- "_urlStringsForInProgressSearchSuggestionImageLoads"
- "filenameWithoutExtension"
- "iconForSystemImageName:isDarkMode:"

```
