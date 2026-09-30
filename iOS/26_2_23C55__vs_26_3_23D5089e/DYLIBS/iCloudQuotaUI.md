## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI`

```diff

-301.23.2.2.0
-  __TEXT.__text: 0x16f808
+301.23.3.1.0
+  __TEXT.__text: 0x16f4cc
   __TEXT.__auth_stubs: 0x43c0
   __TEXT.__objc_methlist: 0x9d04
   __TEXT.__const: 0xaf24
-  __TEXT.__gcc_except_tab: 0x1024
-  __TEXT.__cstring: 0xb7e6
-  __TEXT.__oslogstring: 0xb652
+  __TEXT.__gcc_except_tab: 0xfe8
+  __TEXT.__cstring: 0xb836
+  __TEXT.__oslogstring: 0xb632
   __TEXT.__dlopen_cstrs: 0x691
   __TEXT.__swift5_typeref: 0x9bde
   __TEXT.__swift5_reflstr: 0x1ab0

   __TEXT.__swift_as_ret: 0x13c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x54f8
+  __TEXT.__unwind_info: 0x54e8
   __TEXT.__eh_frame: 0x3578
   __TEXT.__objc_classname: 0x1769
   __TEXT.__objc_methname: 0x1a818

   __DATA_CONST.__objc_arraydata: 0x578
   __AUTH_CONST.__auth_got: 0x21f0
   __AUTH_CONST.__const: 0x7020
-  __AUTH_CONST.__cfstring: 0x7ac0
+  __AUTH_CONST.__cfstring: 0x7aa0
   __AUTH_CONST.__objc_const: 0x22480
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x1b0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2D81413B-D051-3A09-9B66-FFBE4B67698F
-  Functions: 8056
-  Symbols:   15600
-  CStrings:  8823
+  UUID: 5D8AA87C-F2FD-3927-934F-4ECBF120B69C
+  Functions: 8055
+  Symbols:   15598
+  CStrings:  8824
 
Symbols:
+ -[ICQUpgradeFlowManager dismissUpgradeFlowWithSuccess:].cold.1
+ GCC_except_table55
+ ___34-[ICQBackupController startBackup]_block_invoke.727
+ ___34-[ICQBackupController startBackup]_block_invoke.729
+ ___37-[ICQBackupController cancelRestore:]_block_invoke.724
+ ___38-[ICQBackupController updateBusyState]_block_invoke.711
+ ___39-[ICQUsageStorageController specifiers]_block_invoke.446
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.579
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.580
+ ___54-[ICQBackupController startListeningForThermalChanges]_block_invoke.508
+ ___61-[ICQInternetPrivacyViewModel _fetchBannerModelsForPaidTier:]_block_invoke.181
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.588
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.588.cold.1
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.611
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.612
+ ___block_literal_global.732
- -[ICQBundlesHook dynamicViewController:didFinishPurchaseWithResult:error:].cold.2
- GCC_except_table58
- ___34-[ICQBackupController startBackup]_block_invoke.736
- ___34-[ICQBackupController startBackup]_block_invoke.738
- ___37-[ICQBackupController cancelRestore:]_block_invoke.733
- ___38-[ICQBackupController updateBusyState]_block_invoke.720
- ___39-[ICQUsageStorageController specifiers]_block_invoke.455
- ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.588
- ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.589
- ___54-[ICQBackupController startListeningForThermalChanges]_block_invoke.517
- ___60-[ICQInternetPrivacyDetailSpecifierProvider _switchOffAlert]_block_invoke_3
- ___61-[ICQInternetPrivacyViewModel _fetchBannerModelsForPaidTier:]_block_invoke.187
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.597
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.597.cold.1
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.620
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.621
- ___block_literal_global.741
Functions:
~ -[ICQUpgradeFlowManager dismissUpgradeFlowWithSuccess:] : 132 -> 180
~ ___55-[ICQUpgradeFlowManager dismissUpgradeFlowWithSuccess:]_block_invoke : 24 -> 240
~ -[ICQInternetPrivacyDetailSpecifierProvider _switchOffAlert] : 780 -> 632
- ___60-[ICQInternetPrivacyDetailSpecifierProvider _switchOffAlert]_block_invoke_3
~ -[ICQBundlesHook dynamicViewController:didFinishPurchaseWithResult:error:] : 1424 -> 1164
~ -[ICQInternetPrivacyViewModel _fetchBannerModelsForPaidTier:] : 6024 -> 5464
+ -[ICQUpgradeFlowManager dismissUpgradeFlowWithSuccess:].cold.1
~ -[ICQBundlesHook dynamicViewController:didFinishPurchaseWithResult:error:].cold.1 : 248 -> 68
- -[ICQInternetPrivacyViewModel setStatusStringForPrefPane:].cold.1
CStrings:
+ "%s Dismissed with success signal: %@"
+ "%s Unable to find _hostingNavigationController! Cannot dismiss"
+ "-[ICQUpgradeFlowManager dismissUpgradeFlowWithSuccess:]"
+ "-[ICQUpgradeFlowManager dismissUpgradeFlowWithSuccess:]_block_invoke"
- "%s: failed to present with _flowManager.hostingNavigationController: %@, _presentingViewController.presentedViewController: %@"
- "INTERNET_PRIVACY_OPEN_SYSTEM_STATUS_BUTTON_TITLE"

```
