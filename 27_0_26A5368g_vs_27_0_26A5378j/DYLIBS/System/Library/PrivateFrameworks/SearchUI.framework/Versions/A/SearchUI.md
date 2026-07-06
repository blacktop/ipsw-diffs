## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/Versions/A/SearchUI`

```diff

-  __TEXT.__text: 0xcefe8
-  __TEXT.__objc_methlist: 0xf59c
-  __TEXT.__const: 0x2c04
+  __TEXT.__text: 0xcf958
+  __TEXT.__objc_methlist: 0xf5dc
+  __TEXT.__const: 0x2c84
   __TEXT.__cstring: 0x3343
-  __TEXT.__oslogstring: 0x25b5
-  __TEXT.__gcc_except_tab: 0x73c
+  __TEXT.__oslogstring: 0x25f5
+  __TEXT.__gcc_except_tab: 0x788
   __TEXT.__ustring: 0xa8
   __TEXT.__dlopen_cstrs: 0xb2
-  __TEXT.__swift5_typeref: 0x25a8
-  __TEXT.__constg_swiftt: 0x112c
+  __TEXT.__swift5_typeref: 0x25ea
+  __TEXT.__constg_swiftt: 0x114c
   __TEXT.__swift5_reflstr: 0x535
-  __TEXT.__swift5_fieldmd: 0x740
+  __TEXT.__swift5_fieldmd: 0x750
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0x248
-  __TEXT.__swift5_proto: 0x100
+  __TEXT.__swift5_proto: 0x104
   __TEXT.__swift5_types: 0xc4
   __TEXT.__swift5_capture: 0x440
-  __TEXT.__swift5_protos: 0x1c
+  __TEXT.__swift5_protos: 0x20
   __TEXT.__swift_as_entry: 0xec
   __TEXT.__swift_as_ret: 0xd4
   __TEXT.__swift_as_cont: 0x164
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3a10
+  __TEXT.__unwind_info: 0x3a20
   __TEXT.__eh_frame: 0x19f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x408
   __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8528
+  __DATA_CONST.__objc_selrefs: 0x8580
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x5c8
   __DATA_CONST.__objc_arraydata: 0xac0
-  __DATA_CONST.__got: 0x1da0
-  __AUTH_CONST.__const: 0x3b20
+  __DATA_CONST.__got: 0x1de8
+  __AUTH_CONST.__const: 0x3b28
   __AUTH_CONST.__cfstring: 0x3640
-  __AUTH_CONST.__objc_const: 0x1ac28
+  __AUTH_CONST.__objc_const: 0x1ac68
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_arrayobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__auth_got: 0x1300
   __AUTH.__objc_data: 0x35e8
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xb90
-  __DATA.__data: 0x2588
+  __DATA.__objc_ivar: 0xb94
+  __DATA.__data: 0x2598
   __DATA.__bss: 0x9c8
   __DATA.__common: 0xd8
-  __DATA_DIRTY.__objc_data: 0x3820
+  __DATA_DIRTY.__objc_data: 0x3828
   __DATA_DIRTY.__data: 0xac0
   __DATA_DIRTY.__bss: 0x1760
   __DATA_DIRTY.__common: 0x58

   - /System/Library/PrivateFrameworks/CalculateUI.framework/Versions/A/CalculateUI
   - /System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/CalendarUI
   - /System/Library/PrivateFrameworks/CalendarUIKit.framework/Versions/A/CalendarUIKit
+  - /System/Library/PrivateFrameworks/Categories.framework/Versions/A/Categories
   - /System/Library/PrivateFrameworks/ContactsUICore.framework/Versions/A/ContactsUICore
   - /System/Library/PrivateFrameworks/DeviceManagement.framework/Versions/A/DeviceManagement
   - /System/Library/PrivateFrameworks/FMF.framework/Versions/A/FMF

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5847
-  Symbols:   13697
-  CStrings:  1207
+  Functions: 5856
+  Symbols:   13726
+  CStrings:  1208
 
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
~ __AUTH_CONST.__objc_dictobj : content changed
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
+ -[SearchUISwitchAccessoryViewController awaitingTimeoutBlock]
+ -[SearchUISwitchAccessoryViewController setAwaitingTimeoutBlock:]
+ -[SearchUIVerticalLayoutCardSectionView viewWillMoveToWindow:]
+ OBJC_IVAR_$_SearchUISwitchAccessoryViewController._awaitingTimeoutBlock
+ _CTOSPlatformCurrent
+ _CTOSPlatformiOS
+ _CTOSPlatformtvOS
+ _CTOSPlatformvisionOS
+ _CTOSPlatformwatchOS
+ _OBJC_CLASS_$_CTCategories
+ _SearchUITopHitContentHorizontalInset
+ _SearchUITopHitContentVerticalInset
+ ___54-[SearchUISwitchAccessoryViewController buttonPressed]_block_invoke
+ _instanceIdentifierCodingKey
+ _objc_msgSend$applyImageConstraintsToImageView:isCompact:preventThumbnailScaling:usesCompactWidth:isTopHit:
+ _objc_msgSend$awaitingTimeoutBlock
+ _objc_msgSend$bundleIDForPlatform:fromBundleID:platform:
+ _objc_msgSend$bundleWithURL:
+ _objc_msgSend$expectedUpdateState
+ _objc_msgSend$isIOS
+ _objc_msgSend$mouseLocation
+ _objc_msgSend$resolvedBundleIDForCurrentPlatform:
+ _objc_msgSend$setAwaitingTimeoutBlock:
+ _objc_msgSend$sharedCategories
+ _objc_msgSend$urlForDefaultAppToOpenURL:
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
