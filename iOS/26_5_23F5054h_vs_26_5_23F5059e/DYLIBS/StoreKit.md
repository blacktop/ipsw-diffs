## StoreKit

> `/System/Library/Frameworks/StoreKit.framework/StoreKit`

```diff

-815.5.4.0.0
-  __TEXT.__text: 0x1cc4a0
+815.5.6.0.0
+  __TEXT.__text: 0x1cceb0
   __TEXT.__auth_stubs: 0x31e0
-  __TEXT.__objc_methlist: 0x5bfc
-  __TEXT.__gcc_except_tab: 0x1028
+  __TEXT.__objc_methlist: 0x5c44
+  __TEXT.__gcc_except_tab: 0x1038
   __TEXT.__const: 0x16be4
-  __TEXT.__cstring: 0x7c61
+  __TEXT.__cstring: 0x7cb1
   __TEXT.__oslogstring: 0x3140
   __TEXT.__dlopen_cstrs: 0x498
   __TEXT.__constg_swiftt: 0x42a8

   __TEXT.__swift_as_ret: 0x66c
   __TEXT.__swift5_mpenum: 0x38
   __TEXT.__swift5_protos: 0x2c
-  __TEXT.__unwind_info: 0x8ae0
+  __TEXT.__unwind_info: 0x8b18
   __TEXT.__eh_frame: 0xfa3c
   __TEXT.__objc_classname: 0x1aa7
-  __TEXT.__objc_methname: 0xd407
+  __TEXT.__objc_methname: 0xd587
   __TEXT.__objc_methtype: 0x33e4
-  __TEXT.__objc_stubs: 0x9240
-  __DATA_CONST.__got: 0xb88
-  __DATA_CONST.__const: 0x1880
+  __TEXT.__objc_stubs: 0x9420
+  __DATA_CONST.__got: 0xb90
+  __DATA_CONST.__const: 0x18b0
   __DATA_CONST.__objc_classlist: 0x3f8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30e0
+  __DATA_CONST.__objc_selrefs: 0x3158
   __DATA_CONST.__objc_protorefs: 0x1c0
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x1900
-  __AUTH_CONST.__const: 0x11b88
-  __AUTH_CONST.__cfstring: 0x3740
-  __AUTH_CONST.__objc_const: 0x16410
+  __AUTH_CONST.__const: 0x11b68
+  __AUTH_CONST.__cfstring: 0x3780
+  __AUTH_CONST.__objc_const: 0x16440
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x2728
   __AUTH.__data: 0x3068
-  __DATA.__objc_ivar: 0x59c
+  __DATA.__objc_ivar: 0x5a0
   __DATA.__data: 0x6dc0
   __DATA.__bss: 0x25a30
   __DATA.__common: 0xc0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7EFAB2ED-5A16-343E-ACCA-20BFA71C295C
-  Functions: 14425
-  Symbols:   19069
-  CStrings:  4477
+  UUID: F0624A83-976D-3832-ADA9-2A19D44B21FD
+  Functions: 14442
+  Symbols:   19122
+  CStrings:  4500
 
Symbols:
+ -[SKAccountPageSpecifierProvider _shouldShowActionSheet]
+ -[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]
+ -[SKAccountPageViewController _removeSignOutButton]
+ -[SKAccountPageViewController _signOutButtonTapped:]
+ -[SKAccountPageViewController setShowsSignOutButton:]
+ -[SKAccountPageViewController showsSignOutButton]
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table6
+ GCC_except_table63
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table81
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table94
+ _AppleMediaServicesLibrary
+ _OBJC_CLASS_$_UIAction
+ _OBJC_IVAR_$_SKAccountPageViewController._showsSignOutButton
+ ___50-[SKPaymentQueue(Package) checkServerQueueForced:]_block_invoke.162
+ ___51-[SKAccountPageViewController _setupNavigationItem]_block_invoke
+ ___52-[SKAccountPageViewController _signOutButtonTapped:]_block_invoke
+ ___52-[SKAccountPageViewController _signOutButtonTapped:]_block_invoke_2
+ ___52-[SKAccountPageViewController _signOutButtonTapped:]_block_invoke_3
+ ___54-[SKAccountPageViewController _setupWebViewController]_block_invoke.132
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke_2
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke_3
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke_4
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke_5
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke_6
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke_7
+ ___63-[SKAccountPageSpecifierProvider _showActionSheetForSpecifier:]_block_invoke_8
+ ___70-[SKPaymentQueue restoreCompletedTransactionsWithApplicationUsername:]_block_invoke_3
+ ___70-[SKPaymentQueue restoreCompletedTransactionsWithApplicationUsername:]_block_invoke_4
+ ___block_descriptor_40_e8_32s_e18_v16?0"UIAction"8ls32l8
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___getAMSBagClass_block_invoke
+ ___getAMSBagClass_block_invoke.cold.1
+ _getAMSBagClass.softClass
+ _objc_msgSend$_removeSignOutButton
+ _objc_msgSend$_shouldShowActionSheet
+ _objc_msgSend$_showActionSheetForSpecifier:
+ _objc_msgSend$_signOutButtonTapped:
+ _objc_msgSend$actionWithTitle:image:identifier:handler:
+ _objc_msgSend$bagForProfile:profileVersion:
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$initWithPrimaryAction:
+ _objc_msgSend$popViewControllerAnimated:
+ _objc_msgSend$resultWithError:
+ _objc_msgSend$setAttributes:
+ _objc_msgSend$setRightBarButtonItem:animated:
+ _objc_msgSend$setShowsSignOutButton:
+ _objc_msgSend$showsSignOutButton
+ _objc_msgSend$valuePromise
- GCC_except_table49
- GCC_except_table52
- GCC_except_table55
- GCC_except_table58
- GCC_except_table61
- GCC_except_table65
- GCC_except_table69
- GCC_except_table77
- GCC_except_table85
- GCC_except_table88
- GCC_except_table90
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke_2
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke_3
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke_4
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke_5
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke_6
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke_7
- ___65-[SKAccountPageSpecifierProvider _accountPageSpecifierWasTapped:]_block_invoke_8
- ___block_descriptor_32_e20_v20?0B8"NSError"12l
CStrings:
+ "00:03:11"
+ "AMSBag"
+ "Accounts"
+ "Apr 15 2026"
+ "TB,N,V_showsSignOutButton"
+ "_removeSignOutButton"
+ "_shouldShowActionSheet"
+ "_showActionSheetForSpecifier:"
+ "_showsSignOutButton"
+ "_signOutButtonTapped:"
+ "account-page-shows-action-sheet"
+ "actionWithTitle:image:identifier:handler:"
+ "bagForProfile:profileVersion:"
+ "boolForKey:"
+ "initWithPrimaryAction:"
+ "popViewControllerAnimated:"
+ "resultWithError:"
+ "setAttributes:"
+ "setRightBarButtonItem:animated:"
+ "setShowsSignOutButton:"
+ "showsSignOutButton"
+ "v16@?0@\"UIAction\"8"
+ "valuePromise"
- "01:22:59"
- "Apr  6 2026"

```
