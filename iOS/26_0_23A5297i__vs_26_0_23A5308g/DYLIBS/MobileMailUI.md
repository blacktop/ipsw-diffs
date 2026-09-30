## MobileMailUI

> `/System/Library/PrivateFrameworks/MobileMailUI.framework/MobileMailUI`

```diff

-3860.100.5.2.1
-  __TEXT.__text: 0x4d9fc
+3863.100.1.2.5
+  __TEXT.__text: 0x4dcd0
   __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_methlist: 0x510c
-  __TEXT.__gcc_except_tab: 0x99d8
-  __TEXT.__cstring: 0x377c
+  __TEXT.__objc_methlist: 0x5124
+  __TEXT.__gcc_except_tab: 0x9a4c
+  __TEXT.__cstring: 0x376c
   __TEXT.__ustring: 0x318
   __TEXT.__const: 0x81b4
   __TEXT.__oslogstring: 0x1e77

   __TEXT.__swift5_types: 0x14
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x28b8
+  __TEXT.__unwind_info: 0x28d0
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_classname: 0xb90
-  __TEXT.__objc_methname: 0x11df3
+  __TEXT.__objc_methname: 0x11e6b
   __TEXT.__objc_methtype: 0x454e
-  __TEXT.__objc_stubs: 0xbfc0
+  __TEXT.__objc_stubs: 0xc040
   __DATA_CONST.__got: 0xb00
-  __DATA_CONST.__const: 0x12f0
+  __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4158
+  __DATA_CONST.__objc_selrefs: 0x4180
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x888
-  __AUTH_CONST.__const: 0x6f0
+  __AUTH_CONST.__const: 0x710
   __AUTH_CONST.__cfstring: 0x2ec0
-  __AUTH_CONST.__objc_const: 0x7da0
+  __AUTH_CONST.__objc_const: 0x7da8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0xa10
+  __AUTH.__objc_data: 0x9c0
   __AUTH.__data: 0xe8
   __DATA.__objc_ivar: 0x4b0
   __DATA.__data: 0x1168
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x70
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0xb38
+  __DATA_DIRTY.__objc_data: 0xb88
   __DATA_DIRTY.__data: 0x78
-  __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

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
-  UUID: 279A66B0-0576-3ACE-85DC-B8ABB27F8BC2
-  Functions: 1725
-  Symbols:   7092
-  CStrings:  4270
+  UUID: 199AAF11-BA58-36C1-9C4E-B1A576F0688E
+  Functions: 1728
+  Symbols:   7113
+  CStrings:  4278
 
Symbols:
+ +[MFMessageContentView _styleSheetWithPadding:useWideLayout:]
+ +[MFMessageContentView prewarmContent]
+ +[MFMessageContentView prewarmContent].cold.1
+ +[MFMessageContentView prewarmContent].cold.2
+ -[MFMessageContentView _reloadUserStyleSheets].cold.2
+ GCC_except_table356
+ GCC_except_table359
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table59
+ GCC_except_table65
+ ___60-[MFMessageContentView _webView:renderingProgressDidChange:]_block_invoke.432
+ ___60-[MFMessageContentView generateSnapshotImageWithCompletion:]_block_invoke.341
+ ___73-[MFMessageContentView _webView:webContentProcessDidTerminateWithReason:]_block_invoke.433
+ ____attachmentStyleSheet_block_invoke
+ ____notWideStyleSheet_block_invoke
+ ___block_literal_global.1558
+ ___block_literal_global.1566
+ ___block_literal_global.1571
+ __attachmentStyleSheet.onceToken
+ __attachmentStyleSheet.sInstance
+ __notWideStyleSheet.onceToken
+ __notWideStyleSheet.sInstance
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private_$_MobileMailUI
+ _objc_msgSend$mailQuoteColorLevelOne
+ _objc_msgSend$mailQuoteColorLevelThree
+ _objc_msgSend$mailQuoteColorLevelTwo
+ _objc_msgSend$mf_isPadIdiom
+ _objc_msgSend$prewarmContent
- -[MFMessageContentView _styleSheetWithPadding:useWideLayout:]
- GCC_except_table47
- GCC_except_table51
- GCC_except_table54
- GCC_except_table60
- GCC_except_table66
- GCC_except_table70
- ___46-[MFMessageContentView _reloadUserStyleSheets]_block_invoke
- ___60-[MFMessageContentView _webView:renderingProgressDidChange:]_block_invoke.437
- ___60-[MFMessageContentView generateSnapshotImageWithCompletion:]_block_invoke.346
- ___73-[MFMessageContentView _webView:webContentProcessDidTerminateWithReason:]_block_invoke.438
- ___block_literal_global.1565
- ___block_literal_global.327
- __reloadUserStyleSheets.attachmentStyleSheet
- __reloadUserStyleSheets.onceToken
- _objc_msgSend$mf_isPad
Functions:
+ +[MFMessageContentView prewarmContent]
~ -[MFMessageContentView _reloadUserStyleSheets] : 356 -> 320
- ___46-[MFMessageContentView _reloadUserStyleSheets]_block_invoke
~ -[MFMessageContentView _requestWebViewLoadWithRepresentation:] : 1488 -> 1832
+ ____attachmentStyleSheet_block_invoke
+ ___EMPrivacyStringifyRemoteContentURLStrings_block_invoke
~ ___41-[MFWKWebViewFactory preallocateWebViews]_block_invoke : 396 -> 408
+ -[MFMessageContentView _reloadUserStyleSheets].cold.2
CStrings:
+ "?"
+ "MobileMailUI/MFTimeSensitiveBannerView.swift"
+ "_webViewWillEnterFullscreen:"
+ "mailQuoteColorLevelOne"
+ "mailQuoteColorLevelThree"
+ "mailQuoteColorLevelTwo"
+ "mf_isPadIdiom"
+ "prewarmContent"
- "MobileMailUI/MFTimeSensitiveBannerView-BlackPearlUI.swift"
- "mf_isPad"

```
