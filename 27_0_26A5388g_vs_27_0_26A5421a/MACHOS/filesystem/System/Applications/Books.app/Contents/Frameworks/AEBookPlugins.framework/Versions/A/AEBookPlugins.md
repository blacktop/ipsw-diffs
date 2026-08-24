## AEBookPlugins

> `/System/Applications/Books.app/Contents/Frameworks/AEBookPlugins.framework/Versions/A/AEBookPlugins`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-6647.0.0.0.0
-  __TEXT.__text: 0x132988
-  __TEXT.__auth_stubs: 0x26a0
-  __TEXT.__objc_stubs: 0x29600
-  __TEXT.__objc_methlist: 0x1852c
+6655.0.0.0.0
+  __TEXT.__text: 0x132b50
+  __TEXT.__auth_stubs: 0x2690
+  __TEXT.__objc_stubs: 0x29580
+  __TEXT.__objc_methlist: 0x18534
   __TEXT.__cstring: 0x95e7
-  __TEXT.__objc_classname: 0x2c0d
+  __TEXT.__objc_classname: 0x2bed
   __TEXT.__objc_methtype: 0xa44d
-  __TEXT.__const: 0x17c8
-  __TEXT.__gcc_except_tab: 0x3e68
-  __TEXT.__objc_methname: 0x38439
-  __TEXT.__oslogstring: 0x5827
+  __TEXT.__const: 0x17e8
+  __TEXT.__gcc_except_tab: 0x3eec
+  __TEXT.__objc_methname: 0x38379
+  __TEXT.__oslogstring: 0x5ba7
   __TEXT.__ustring: 0x342
   __TEXT.__swift5_typeref: 0x702
   __TEXT.__swift5_capture: 0x26c

   __DATA_CONST.__cfstring: 0x92a0
   __DATA_CONST.__objc_classlist: 0x800
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x528
+  __DATA_CONST.__objc_protolist: 0x518
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x528

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x60
-  __DATA_CONST.__auth_got: 0x1368
-  __DATA_CONST.__got: 0x16c0
+  __DATA_CONST.__auth_got: 0x1360
+  __DATA_CONST.__got: 0x16b8
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA.__objc_const: 0x204a8
-  __DATA.__objc_selrefs: 0xd7f8
-  __DATA.__objc_ivar: 0x1448
+  __DATA.__objc_const: 0x203f8
+  __DATA.__objc_selrefs: 0xd7e0
+  __DATA.__objc_ivar: 0x143c
   __DATA.__objc_data: 0x5c90
-  __DATA.__data: 0x42d8
+  __DATA.__data: 0x4218
   __DATA.__bss: 0xb30
   __DATA.__common: 0x38
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
-  - /System/Library/Frameworks/Symbols.framework/Versions/A/Symbols
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AXRuntime.framework/Versions/A/AXRuntime
   - /System/Library/PrivateFrameworks/AppAnalytics.framework/Versions/A/AppAnalytics

   - @rpath/BookCore.framework/Versions/A/BookCore
   - @rpath/BookEPUB.framework/Versions/A/BookEPUB
   - @rpath/TemplateUI.framework/Versions/A/TemplateUI
-  Functions: 8453
-  Symbols:   2303
-  CStrings:  12227
+  Functions: 8454
+  Symbols:   2299
+  CStrings:  12228
 
Symbols:
+ _OBJC_CLASS_$_BKSafeAreaInsetRemovingView
+ _OBJC_CLASS_$_BUBag
+ _OBJC_METACLASS_$_BKSafeAreaInsetRemovingView
- OBJC_IVAR_$_BKThumbnailBookViewController._bookmarkButton
- OBJC_IVAR_$_BKThumbnailBookViewController._topToolbar
- _BCReaderEnhancedLandscapeEnabled
- _OBJC_CLASS_$_BCUIFullHeightNavWrapper
- _OBJC_CLASS_$_BKBottomSafeAreaInsetRemovingView
- _OBJC_CLASS_$_NSSymbolReplaceContentTransition
- _OBJC_METACLASS_$_BKBottomSafeAreaInsetRemovingView
CStrings:
+ "BKSafeAreaInsetRemovingView"
+ "T@\"UINavigationBar\",R,N"
+ "[DRMTrace][open] -> silent keybag refetch dsid=%{private}@ logID:%{public}@"
+ "[DRMTrace][open] Auth needed due to non-existing account for asset at url, username: %@ -- %@, logID:%{public}@"
+ "[DRMTrace][open] DRM/Keybag failure for book at URL: %@ -- %@ logID:%{public}@"
+ "[DRMTrace][open] Error authenticating account: %@ -- %@, logID:%{public}@"
+ "[DRMTrace][open] Error refetching bag for dsid: %@ -- %@, logID:%{public}@"
+ "[DRMTrace][open] confirmBagContents ENTER sinfCount=%lu"
+ "[DRMTrace][open] confirmBagContents keybag-refetch-required; underlying=%{public}@ familyRemoval=%{BOOL}d"
+ "[DRMTrace][open] gate(AE): accountNil=%{BOOL}d credentialEmpty=%{BOOL}d credential=%{private}@ logID:%{public}@"
+ "[DRMTrace][open] identity: usernamePresent=%{BOOL}d dsid=%{private}@ logID:%{public}@"
+ "[DRMTrace][open] interactive auth result ok=%{BOOL}d err=%{public}@ logID:%{public}@"
+ "[DRMTrace][open] open failed err=%{public}@ underlying=%{public}@ refetchRequired=%{BOOL}d canRefetch=%{BOOL}d logID:%{public}@"
+ "[DRMTrace][open] parse decrypt keybag-refetch-required; underlying FairPlay status=%d"
+ "[DRMTrace][open] vcWithOptions ENTER url=%@ canRefetch=%{BOOL}d logID:%{public}@"
+ "[DRMTrace][read] SMIL FairPlay decrypt failed: %{public}@ Path: %{public}@ refetch:%d"
+ "_configuredBuyButtonItem"
+ "assetViewController:updateBuyButton:setIsDark:"
+ "defaultBag"
+ "isLoaded"
+ "isNavigationBarHidden"
+ "setSharesBackground:"
+ "shouldHideSearchItem"
+ "storeFront"
+ "supportsAlernativeBarLayout"
+ "updateBookmarkItem:"
+ "wantsBottomScrubber"
- "Auth needed due to non-existing account for asset at url, username: %@ -- %@, logID:%{public}@"
- "BCToolbarDelegate"
- "BKBottomSafeAreaInsetRemovingView"
- "DRM/Keybag failure for book at URL: %@ -- %@ logID:%{public}@"
- "Error authenticating account: %@ -- %@, logID:%{public}@"
- "Error refetching bag for dsid: %@ -- %@, logID:%{public}@"
- "SMIL FairPlay decrypt failed: %{public}@ Path: %{public}@ refetch:%d"
- "T@\"BCNavigationBar\",R,N,V_topToolbar"
- "T@\"NSLayoutConstraint\",&,N,V_pageNumberHUDTopConstraint"
- "UIToolbarDelegate"
- "_bookmarkButton"
- "_pageNumberHUDTopConstraint"
- "_topToolbar"
- "pageNumberHUDTopConstraint"
- "setAdditionalSafeAreaInsets:"
- "setCursorInsets:"
- "setPageNumberHUDTopConstraint:"
- "setSpecifiedWidth:"
- "setSymbolImage:withContentTransition:"
- "specifiedWidth"
- "stylizeBCNavigationBarTranslucent:"
- "systemRedColor"
- "toolbarItems"
- "transition"
- "updateBookmarkButton"
- "updateBookmarkButton:"
```
