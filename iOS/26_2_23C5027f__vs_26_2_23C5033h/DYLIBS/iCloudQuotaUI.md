## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI`

```diff

-301.23.1.8.0
-  __TEXT.__text: 0x16f0ec
+301.23.2.1.0
+  __TEXT.__text: 0x16f53c
   __TEXT.__auth_stubs: 0x43c0
-  __TEXT.__objc_methlist: 0x9cf4
+  __TEXT.__objc_methlist: 0x9d04
   __TEXT.__const: 0xaf24
   __TEXT.__gcc_except_tab: 0xfe8
-  __TEXT.__cstring: 0xb7a6
-  __TEXT.__oslogstring: 0xb572
+  __TEXT.__cstring: 0xb7b6
+  __TEXT.__oslogstring: 0xb652
   __TEXT.__dlopen_cstrs: 0x691
   __TEXT.__swift5_typeref: 0x9bde
   __TEXT.__swift5_reflstr: 0x1ab0

   __TEXT.__swift_as_ret: 0x13c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x54e0
+  __TEXT.__unwind_info: 0x54f8
   __TEXT.__eh_frame: 0x3578
   __TEXT.__objc_classname: 0x1769
-  __TEXT.__objc_methname: 0x1a807
+  __TEXT.__objc_methname: 0x1a818
   __TEXT.__objc_methtype: 0x5ecf
-  __TEXT.__objc_stubs: 0x13e80
+  __TEXT.__objc_stubs: 0x13ea0
   __DATA_CONST.__got: 0x1cc8
   __DATA_CONST.__const: 0x2810
   __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6a50
+  __DATA_CONST.__objc_selrefs: 0x6a58
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x578
   __AUTH_CONST.__auth_got: 0x21f0
-  __AUTH_CONST.__const: 0x7000
-  __AUTH_CONST.__cfstring: 0x7a80
+  __AUTH_CONST.__const: 0x7020
+  __AUTH_CONST.__cfstring: 0x7aa0
   __AUTH_CONST.__objc_const: 0x22480
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x1b0

   __AUTH.__data: 0x24c8
   __DATA.__objc_ivar: 0xbd8
   __DATA.__data: 0x4110
-  __DATA.__bss: 0xd4e8
+  __DATA.__bss: 0xd4f8
   __DATA.__common: 0x2a8
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6AD2A285-DEA5-3216-A6FD-123671D5A5AA
-  Functions: 8048
-  Symbols:   15580
-  CStrings:  8814
+  UUID: 6405CDF5-D72D-37F3-9B7D-8D460380DD59
+  Functions: 8055
+  Symbols:   15598
+  CStrings:  8821
 
Symbols:
+ +[ICQBannerView debugBannerOffer]
+ +[ICQBannerView debugBannerOffer].cold.1
+ +[ICQBannerView shouldShowForDismissibleOffer:].cold.1
+ +[ICQBannerView shouldShowForOffer:].cold.1
+ -[ICQBannerView _initWithFrame:offer:dismissibility:].cold.1
+ ___33+[ICQBannerView debugBannerOffer]_block_invoke
+ ___33+[ICQBannerView debugBannerOffer]_block_invoke.cold.1
+ ___34-[ICQBackupController startBackup]_block_invoke.736
+ ___34-[ICQBackupController startBackup]_block_invoke.738
+ ___37-[ICQBackupController cancelRestore:]_block_invoke.733
+ ___37-[ICQBannerView handleBannerDismiss:]_block_invoke.69
+ ___38-[ICQBackupController updateBusyState]_block_invoke.720
+ ___39-[ICQUsageStorageController specifiers]_block_invoke.455
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.588
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.589
+ ___54-[ICQBackupController startListeningForThermalChanges]_block_invoke.517
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.597
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.597.cold.1
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.620
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.621
+ ___block_literal_global.741
+ _debugBannerOffer.cachedDebugOffer
+ _debugBannerOffer.onceToken
+ _objc_msgSend$debugBannerOffer
- ___34-[ICQBackupController startBackup]_block_invoke.727
- ___34-[ICQBackupController startBackup]_block_invoke.729
- ___37-[ICQBackupController cancelRestore:]_block_invoke.724
- ___37-[ICQBannerView handleBannerDismiss:]_block_invoke.63
- ___38-[ICQBackupController updateBusyState]_block_invoke.711
- ___39-[ICQUsageStorageController specifiers]_block_invoke.446
- ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.579
- ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.580
- ___54-[ICQBackupController startListeningForThermalChanges]_block_invoke.508
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.588
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.588.cold.1
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.611
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.612
- ___block_literal_global.732
CStrings:
+ "Debug banner override active for dismissible banner"
+ "Debug banner override active, forcing banner display for offer type: %@"
+ "Failed to unarchive debug banner offer: %@"
+ "Using debug banner offer instead of passed offer"
+ "debug-banner-override"
+ "debugBannerOffer"

```
