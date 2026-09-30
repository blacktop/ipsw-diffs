## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-  __TEXT.__text: 0xf3198
-  __TEXT.__objc_methlist: 0x12208
-  __TEXT.__const: 0x3824
+  __TEXT.__text: 0xf3c28
+  __TEXT.__objc_methlist: 0x12258
+  __TEXT.__const: 0x38a4
   __TEXT.__cstring: 0x3998
-  __TEXT.__oslogstring: 0x2885
-  __TEXT.__gcc_except_tab: 0x99c
+  __TEXT.__oslogstring: 0x28c5
+  __TEXT.__gcc_except_tab: 0x9e8
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160
-  __TEXT.__swift5_typeref: 0x3336
-  __TEXT.__constg_swiftt: 0x13f8
+  __TEXT.__swift5_typeref: 0x3378
+  __TEXT.__constg_swiftt: 0x1418
   __TEXT.__swift5_reflstr: 0x6d5
-  __TEXT.__swift5_fieldmd: 0x8b0
+  __TEXT.__swift5_fieldmd: 0x8c0
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__swift5_proto: 0x144
+  __TEXT.__swift5_proto: 0x148
   __TEXT.__swift5_types: 0xdc
   __TEXT.__swift5_capture: 0x7ec
   __TEXT.__swift_as_entry: 0x130
   __TEXT.__swift_as_ret: 0x114
   __TEXT.__swift_as_cont: 0x1c8
-  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x47e0
+  __TEXT.__unwind_info: 0x4800
   __TEXT.__eh_frame: 0x230c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x410
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa198
+  __DATA_CONST.__objc_selrefs: 0xa1f0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x24e8
-  __AUTH_CONST.__const: 0x2a20
+  __DATA_CONST.__got: 0x2538
+  __AUTH_CONST.__const: 0x2a28
   __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x1dd58
+  __AUTH_CONST.__objc_const: 0x1dd98
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x1878
   __AUTH.__objc_data: 0x5ca8
   __AUTH.__data: 0x908
-  __DATA.__objc_ivar: 0xcd8
-  __DATA.__data: 0x3430
+  __DATA.__objc_ivar: 0xcdc
+  __DATA.__data: 0x3440
   __DATA.__bss: 0x27e0
   __DATA.__common: 0xd8
-  __DATA_DIRTY.__objc_data: 0x1c38
+  __DATA_DIRTY.__objc_data: 0x1c40
   __DATA_DIRTY.__data: 0x180
   __DATA_DIRTY.__bss: 0xc0
   __DATA_DIRTY.__common: 0x40

   - /System/Library/PrivateFrameworks/Calculate.framework/Calculate
   - /System/Library/PrivateFrameworks/CalculateUI.framework/CalculateUI
   - /System/Library/PrivateFrameworks/CalendarUIKit.framework/CalendarUIKit
+  - /System/Library/PrivateFrameworks/Categories.framework/Categories
   - /System/Library/PrivateFrameworks/ClipServices.framework/ClipServices
   - /System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore
   - /System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6933
-  Symbols:   21663
-  CStrings:  1218
+  Functions: 6943
+  Symbols:   21702
+  CStrings:  1219
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[SearchUIThumbnailViewController applyImageConstraintsToImageView:isCompact:preventThumbnailScaling:usesCompactWidth:isTopHit:]
+ +[SearchUIUtilities bundleIdentifierForDefaultAppToOpenURL:]
+ +[SearchUIUtilities defaultRecordForURL:]
+ +[SearchUIUtilities urlForDefaultAppToOpenURL:]
+ -[SearchUIAppIconImage resolvedBundleIDForCurrentPlatform:]
+ -[SearchUICollectionViewCell _applyIntrinsicContentHeightToAttributes:]
+ -[SearchUICollectionViewCell _shouldUseIntrinsicContentHeight]
+ -[SearchUISwitchAccessoryViewController awaitingTimeoutBlock]
+ -[SearchUISwitchAccessoryViewController setAwaitingTimeoutBlock:]
+ _CTOSPlatformCurrent
+ _CTOSPlatformmacOS
+ _CTOSPlatformtvOS
+ _CTOSPlatformvisionOS
+ _CTOSPlatformwatchOS
+ _OBJC_CLASS_$_CTCategories
+ _OBJC_IVAR_$_SearchUISwitchAccessoryViewController._awaitingTimeoutBlock
+ _SearchUITopHitContentHorizontalInset
+ _SearchUITopHitContentVerticalInset
+ ___54-[SearchUISwitchAccessoryViewController buttonPressed]_block_invoke
+ _instanceIdentifierCodingKey
+ _objc_msgSend$_applyIntrinsicContentHeightToAttributes:
+ _objc_msgSend$_shouldUseIntrinsicContentHeight
+ _objc_msgSend$applyImageConstraintsToImageView:isCompact:preventThumbnailScaling:usesCompactWidth:isTopHit:
+ _objc_msgSend$awaitingTimeoutBlock
+ _objc_msgSend$bundleIDForPlatform:fromBundleID:platform:
+ _objc_msgSend$bundleIdentifierForDefaultAppToOpenURL:
+ _objc_msgSend$expectedUpdateState
+ _objc_msgSend$isIOS
+ _objc_msgSend$prefersIntrinsicContentHeight
+ _objc_msgSend$resolvedBundleIDForCurrentPlatform:
+ _objc_msgSend$setAwaitingTimeoutBlock:
+ _objc_msgSend$sharedCategories
+ _symbolic $s8SearchUI0A30UIIntrinsicHeightRFCardSectionP
+ _symbolic ______p 8SearchUI0A30UIIntrinsicHeightRFCardSectionP
+ _symbolic ______pSg 8SearchUI0A30UIIntrinsicHeightRFCardSectionP
+ _typeIdentifierCodingKey
- +[SearchUIDefaultPunchoutAppIconImage defaultRecordForURL:]
- +[SearchUIThumbnailViewController applyImageConstraintsToImageView:isCompact:preventThumbnailScaling:usesCompactWidth:]
- __OBJC_$_CLASS_METHODS_SearchUIDefaultPunchoutAppIconImage
- _instanceIdentifier
- _objc_msgSend$applyImageConstraintsToImageView:isCompact:preventThumbnailScaling:usesCompactWidth:
- _typeIdentifier
CStrings:
+ "Ignoring stale event for BiomeStream (%@) — expected %d, got %d"

```
