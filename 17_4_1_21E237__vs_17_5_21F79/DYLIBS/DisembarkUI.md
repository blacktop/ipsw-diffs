## DisembarkUI

> `/System/Library/PrivateFrameworks/DisembarkUI.framework/DisembarkUI`

```diff

-226.0.0.0.0
-  __TEXT.__text: 0x16400
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x184c
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x1466
-  __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__oslogstring: 0xad9
-  __TEXT.__unwind_info: 0x594
-  __TEXT.__objc_classname: 0x4ed
-  __TEXT.__objc_methname: 0x5b88
+226.4.0.0.0
+  __TEXT.__text: 0x17bd0
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_methlist: 0x1954
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x15f6
+  __TEXT.__gcc_except_tab: 0x174
+  __TEXT.__oslogstring: 0xc2f
+  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__objc_classname: 0x50d
+  __TEXT.__objc_methname: 0x5f3c
   __TEXT.__objc_methtype: 0x1240
-  __TEXT.__objc_stubs: 0x4580
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0xb20
-  __DATA_CONST.__objc_classlist: 0x110
+  __TEXT.__objc_stubs: 0x48a0
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0xbb8
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3d48
-  __DATA_CONST.__objc_selrefs: 0x1480
-  __DATA_CONST.__objc_classrefs: 0x338
-  __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__cfstring: 0x1120
-  __AUTH_CONST.__objc_const: 0xaf0
+  __DATA_CONST.__objc_const: 0x3eb0
+  __DATA_CONST.__objc_selrefs: 0x1558
+  __DATA_CONST.__objc_classrefs: 0x348
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__cfstring: 0x1200
+  __AUTH_CONST.__objc_const: 0xb38
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__auth_got: 0x278
-  __AUTH.__objc_data: 0xaa0
-  __DATA.__objc_ivar: 0x22c
+  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x240
   __DATA.__data: 0x8a0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/StorageData.framework/StorageData
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 659
-  Symbols:   2641
-  CStrings:  1474
+  Functions: 691
+  Symbols:   2753
+  CStrings:  1528
 
Symbols:
+ -[DKAccountProvider primaryAppleAccountAllowsOfflineEraseWithCompletion:]
+ -[DKConfiguration presentsNetworkSettingsModally]
+ -[DKConfiguration setPresentsNetworkSettingsModally:]
+ -[DKEraseFlow _advanceFromInternetWarningAfterPresentedNetworkSettingsDismisses:]
+ -[DKEraseFlow _advanceFromInternetWarningAfterPresentedNetworkSettingsDismisses:].cold.1
+ -[DKEraseFlow _signOutAndEraseDevice]
+ -[DKEraseFlow _signOutAndEraseDevice].cold.1
+ -[DKEraseFlow _signOutAndEraseDevice].cold.2
+ -[DKEraseFlow _signOutAndEraseDevice].cold.3
+ -[DKEraseFlow continueWithoutInternet]
+ -[DKEraseFlow setContinueWithoutInternet:]
+ -[DKInternetWarningViewController .cxx_destruct]
+ -[DKInternetWarningViewController _continueWithoutInternetTapped:]
+ -[DKInternetWarningViewController _createNotableUserDataCardForFindMy:]
+ -[DKInternetWarningViewController _requireInternetTapped:]
+ -[DKInternetWarningViewController continueWithoutInternetBlock]
+ -[DKInternetWarningViewController init]
+ -[DKInternetWarningViewController notableUserData]
+ -[DKInternetWarningViewController requireInternetBlock]
+ -[DKInternetWarningViewController setContinueWithoutInternetBlock:]
+ -[DKInternetWarningViewController setNotableUserData:]
+ -[DKInternetWarningViewController setRequireInternetBlock:]
+ -[DKInternetWarningViewController showAvailable]
+ -[DKInternetWarningViewController showBusy]
+ -[DKInternetWarningViewController viewDidLoad]
+ GCC_except_table13
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table43
+ GCC_except_table49
+ GCC_except_table8
+ _OBJC_CLASS_$_DKInternetWarningViewController
+ _OBJC_CLASS_$_NSDate
+ _OBJC_IVAR_$_DKConfiguration._presentsNetworkSettingsModally
+ _OBJC_IVAR_$_DKEraseFlow._continueWithoutInternet
+ _OBJC_IVAR_$_DKInternetWarningViewController._continueWithoutInternetBlock
+ _OBJC_IVAR_$_DKInternetWarningViewController._notableUserData
+ _OBJC_IVAR_$_DKInternetWarningViewController._requireInternetBlock
+ _OBJC_METACLASS_$_DKInternetWarningViewController
+ _UIFontTextStyleBody
+ __Block_object_dispose
+ __OBJC_$_INSTANCE_METHODS_DKInternetWarningViewController
+ __OBJC_$_INSTANCE_VARIABLES_DKInternetWarningViewController
+ __OBJC_$_PROP_LIST_DKAccountProvider.245
+ __OBJC_$_PROP_LIST_DKInternetWarningViewController
+ __OBJC_CLASS_RO_$_DKInternetWarningViewController
+ __OBJC_METACLASS_RO_$_DKInternetWarningViewController
+ ___37-[DKEraseFlow _signOutAndEraseDevice]_block_invoke
+ ___37-[DKEraseFlow _signOutAndEraseDevice]_block_invoke_2
+ ___37-[DKEraseFlow _signOutAndEraseDevice]_block_invoke_2.cold.1
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke.124
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke.125
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_2.126
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_3.127
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_4.128
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_5.129
+ ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_6.133
+ ___46-[DKEraseFlow _nextStateFromState:completion:]_block_invoke.134
+ ___46-[DKEraseFlow _nextStateFromState:completion:]_block_invoke_2
+ ___66-[DKInternetWarningViewController _continueWithoutInternetTapped:]_block_invoke
+ ___73-[DKAccountProvider primaryAppleAccountAllowsOfflineEraseWithCompletion:]_block_invoke
+ ___81-[DKEraseFlow _advanceFromInternetWarningAfterPresentedNetworkSettingsDismisses:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56w_e5_v8?0lw56l8r48l8s32l8s40l8
+ __dispatch_source_type_timer
+ _dispatch_activate
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _objc_msgSend$_advanceFromInternetWarningAfterPresentedNetworkSettingsDismisses:
+ _objc_msgSend$_signOutAndEraseDevice
+ _objc_msgSend$arrangedSubviews
+ _objc_msgSend$continueWithoutInternet
+ _objc_msgSend$continueWithoutInternetBlock
+ _objc_msgSend$labelColor
+ _objc_msgSend$lastObject
+ _objc_msgSend$now
+ _objc_msgSend$preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:
+ _objc_msgSend$presentedViewController
+ _objc_msgSend$presentsNetworkSettingsModally
+ _objc_msgSend$primaryAppleAccountAllowsOfflineEraseWithCompletion:
+ _objc_msgSend$requireInternetBlock
+ _objc_msgSend$setContinueWithoutInternet:
+ _objc_msgSend$setContinueWithoutInternetBlock:
+ _objc_msgSend$setCustomSpacing:afterView:
+ _objc_msgSend$setPresentsNetworkSettingsModally:
+ _objc_msgSend$setRequireInternetBlock:
+ _objc_msgSend$setTextAlignment:
+ _objc_msgSend$showAvailable
+ _objc_msgSend$showBusy
+ _objc_msgSend$showButtonsAvailable
+ _objc_msgSend$showButtonsBusy
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$traitCollection
- -[DKEraseFlow _eraseDevice].cold.1
- -[DKEraseFlow _eraseDevice].cold.2
- -[DKEraseFlow _eraseDevice].cold.3
- GCC_except_table31
- GCC_except_table35
- GCC_except_table39
- GCC_except_table6
- __OBJC_$_PROP_LIST_DKAccountProvider.243
- ___27-[DKEraseFlow _eraseDevice]_block_invoke
- ___27-[DKEraseFlow _eraseDevice]_block_invoke_2
- ___27-[DKEraseFlow _eraseDevice]_block_invoke_2.cold.1
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_11
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_12
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_13
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_14
- ___39-[DKEraseFlow _viewControllerForState:]_block_invoke_15
CStrings:
+ "-[DKEraseFlow _advanceFromInternetWarningAfterPresentedNetworkSettingsDismisses:]"
+ "-[DKEraseFlow _signOutAndEraseDevice]"
+ "Allows offline erase %d"
+ "Continuing without internet"
+ "DKInternetWarningViewController"
+ "Detected internet warning release"
+ "Detected network settings connectivity"
+ "Detected network settings dismissal"
+ "INTERNET_WARNING_CONFIRMATION_CONTINUE_WITHOUT_INTERNET_BUTTON"
+ "INTERNET_WARNING_CONFIRMATION_TITLE"
+ "INTERNET_WARNING_CONTINUE_WITHOUT_INTERNET_BUTTON"
+ "INTERNET_WARNING_DETAIL"
+ "INTERNET_WARNING_REQUIRE_INTERNET_BUTTON"
+ "INTERNET_WARNING_TITLE"
+ "Internet Warning"
+ "Network settings did not change connectivity after delay"
+ "Requiring internet and presenting network settings"
+ "T@?,C,N,V_continueWithoutInternetBlock"
+ "T@?,C,N,V_requireInternetBlock"
+ "TB,N,V_continueWithoutInternet"
+ "TB,N,V_presentsNetworkSettingsModally"
+ "Waiting for network settings dismissal"
+ "_advanceFromInternetWarningAfterPresentedNetworkSettingsDismisses:"
+ "_continueWithoutInternet"
+ "_continueWithoutInternetBlock"
+ "_continueWithoutInternetTapped:"
+ "_presentsNetworkSettingsModally"
+ "_requireInternetBlock"
+ "_requireInternetTapped:"
+ "_signOutAndEraseDevice"
+ "arrangedSubviews"
+ "continueWithoutInternet"
+ "continueWithoutInternetBlock"
+ "internetWarningViewController.presentedViewController"
+ "labelColor"
+ "lastObject"
+ "now"
+ "preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:"
+ "presentedViewController"
+ "presentsNetworkSettingsModally"
+ "primaryAppleAccountAllowsOfflineEraseWithCompletion:"
+ "requireInternetBlock"
+ "setContinueWithoutInternet:"
+ "setContinueWithoutInternetBlock:"
+ "setCustomSpacing:afterView:"
+ "setPresentsNetworkSettingsModally:"
+ "setRequireInternetBlock:"
+ "setTextAlignment:"
+ "showAvailable"
+ "showBusy"
+ "showButtonsAvailable"
+ "showButtonsBusy"
+ "timeIntervalSinceDate:"
+ "traitCollection"
+ "viewController.notableUserData %@"
- "-[DKEraseFlow _eraseDevice]"

```
