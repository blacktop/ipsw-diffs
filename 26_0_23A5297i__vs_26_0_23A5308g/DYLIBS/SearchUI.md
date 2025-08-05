## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-630.0.0.0.0
-  __TEXT.__text: 0xec140
-  __TEXT.__auth_stubs: 0x2d30
-  __TEXT.__objc_methlist: 0x12030
+633.0.0.0.0
+  __TEXT.__text: 0xec9fc
+  __TEXT.__auth_stubs: 0x2d40
+  __TEXT.__objc_methlist: 0x120c0
   __TEXT.__const: 0x2f04
-  __TEXT.__gcc_except_tab: 0x9e0
+  __TEXT.__gcc_except_tab: 0xa1c
   __TEXT.__cstring: 0x45c7
   __TEXT.__oslogstring: 0x25e8
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160
   __TEXT.__constg_swiftt: 0x12f8
-  __TEXT.__swift5_typeref: 0x2dfa
+  __TEXT.__swift5_typeref: 0x2e0a
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_reflstr: 0x6b8
   __TEXT.__swift5_fieldmd: 0x87c

   __TEXT.__swift_as_entry: 0x120
   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x46b0
+  __TEXT.__unwind_info: 0x46f0
   __TEXT.__eh_frame: 0x1ef0
   __TEXT.__objc_classname: 0x30e3
-  __TEXT.__objc_methname: 0x2a1ee
-  __TEXT.__objc_methtype: 0x76dc
-  __TEXT.__objc_stubs: 0x20360
-  __DATA_CONST.__got: 0x2460
-  __DATA_CONST.__const: 0x2790
+  __TEXT.__objc_methname: 0x2a321
+  __TEXT.__objc_methtype: 0x76ed
+  __TEXT.__objc_stubs: 0x20460
+  __DATA_CONST.__got: 0x2468
+  __DATA_CONST.__const: 0x27c0
   __DATA_CONST.__objc_classlist: 0xab8
   __DATA_CONST.__objc_catlist: 0x400
   __DATA_CONST.__objc_protolist: 0x368
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e68
+  __DATA_CONST.__objc_selrefs: 0x9eb8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x6e8
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x16a8
-  __AUTH_CONST.__const: 0x26d0
+  __AUTH_CONST.__auth_got: 0x16b0
+  __AUTH_CONST.__const: 0x2728
   __AUTH_CONST.__cfstring: 0x3120
-  __AUTH_CONST.__objc_const: 0x1dc18
+  __AUTH_CONST.__objc_const: 0x1dc70
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x40f8
   __AUTH.__data: 0x7a0
-  __DATA.__objc_ivar: 0xc9c
+  __DATA.__objc_ivar: 0xca4
   __DATA.__data: 0x3228
   __DATA.__bss: 0x1ac0
   __DATA.__common: 0xd8

   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
+  - /System/Library/Frameworks/Symbols.framework/Symbols
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/Vision.framework/Vision

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BDFC3C1B-30FF-35F6-A760-2B8C6D8A481F
-  Functions: 6751
-  Symbols:   20975
-  CStrings:  9090
+  UUID: D1981598-39FE-3EF9-92E7-75B0AA7E52FB
+  Functions: 6766
+  Symbols:   21019
+  CStrings:  9105
 
Symbols:
+ +[SearchUICopyButtonItem offsetSinceLastPasteboardUpdate]
+ +[SearchUICopyButtonItem pasteboardWasUpdatedWithObject:]
+ -[SearchUIButtonItem stateSymbolTransition]
+ -[SearchUIButtonItemView setSfImage:animateTransition:symbolTransition:]
+ -[SearchUICollectionViewCell _updateHighlightColorsForView:highlight:]
+ -[SearchUICollectionViewDataSource registerAllViewsForSnapshot:]
+ -[SearchUICopyButtonItem .cxx_destruct]
+ -[SearchUICopyButtonItem pasteboardStringMatches]
+ -[SearchUICopyButtonItem setStatus:]
+ -[SearchUICopyButtonItem stateSymbolTransition]
+ -[SearchUIHomeScreenAppIconView setTintView:]
+ -[SearchUIHomeScreenAppIconView tintView]
+ -[SearchUIHomeScreenAppIconView updateCorners]
+ GCC_except_table25
+ _OBJC_CLASS_$_NSSymbolReplaceContentTransition
+ _OBJC_IVAR_$_SearchUICopyButtonItem._statusTimer
+ _OBJC_IVAR_$_SearchUIHomeScreenAppIconView._tintView
+ __OBJC_$_CLASS_METHODS_SearchUICopyButtonItem
+ __OBJC_$_INSTANCE_VARIABLES_SearchUICopyButtonItem
+ ___36-[SearchUICopyButtonItem setStatus:]_block_invoke
+ ___84-[SearchUIQuickLookThumbnailImage loadImageWithScale:isDarkStyle:completionHandler:]_block_invoke_3
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSTimer"8lw40l8s32l8
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_SearchUI
+ _objc_msgSend$offsetSinceLastPasteboardUpdate
+ _objc_msgSend$pasteboardStringMatches
+ _objc_msgSend$pasteboardWasUpdatedWithObject:
+ _objc_msgSend$replaceUpUpTransition
+ _objc_msgSend$setSfImage:animateTransition:symbolTransition:
+ _objc_msgSend$setTransition:
+ _objc_msgSend$stateSymbolTransition
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$updateCorners
+ _sLastCopyTimestamp
+ _symbolic ______pSgXw So28SearchUIScrollButtonDelegateP
- -[SFVerticalLayoutCardSection(SearchUIGridSectionModel) searchUIGridSectionModel_useEstimatedHeight]
- -[SearchUIButtonItemView setSfImage:animateTransition:]
- GCC_except_table11
- GCC_except_table23
- ___84-[SearchUIQuickLookThumbnailImage loadImageWithScale:isDarkStyle:completionHandler:]_block_invoke.15
- _objc_msgSend$setSfImage:animateTransition:
- _symbolic ______pSg So28SearchUIScrollButtonDelegateP
CStrings:
+ "?"
+ "T@\"UIView\",&,V_tintView"
+ "_statusTimer"
+ "_updateHighlightColorsForView:highlight:"
+ "offsetSinceLastPasteboardUpdate"
+ "pasteboardStringMatches"
+ "pasteboardWasUpdatedWithObject:"
+ "registerAllViewsForSnapshot:"
+ "replaceUpUpTransition"
+ "setSfImage:animateTransition:symbolTransition:"
+ "setTransition:"
+ "stateSymbolTransition"
+ "timeIntervalSince1970"
+ "updateCorners"
+ "v36@0:8@16B24@28"
- "setSfImage:animateTransition:"

```
