## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI`

```diff

-301.23.0.19.0
-  __TEXT.__text: 0x163614
+301.23.0.21.0
+  __TEXT.__text: 0x163a34
   __TEXT.__auth_stubs: 0x4390
-  __TEXT.__objc_methlist: 0x9ba4
+  __TEXT.__objc_methlist: 0x9bbc
   __TEXT.__const: 0x91a4
   __TEXT.__gcc_except_tab: 0xfe8
-  __TEXT.__cstring: 0xb426
+  __TEXT.__cstring: 0xb466
   __TEXT.__oslogstring: 0xb442
   __TEXT.__dlopen_cstrs: 0x691
   __TEXT.__swift5_typeref: 0x9a2a

   __TEXT.__unwind_info: 0x5368
   __TEXT.__eh_frame: 0x34c0
   __TEXT.__objc_classname: 0x175b
-  __TEXT.__objc_methname: 0x1a470
-  __TEXT.__objc_methtype: 0x5ded
-  __TEXT.__objc_stubs: 0x13b20
+  __TEXT.__objc_methname: 0x1a551
+  __TEXT.__objc_methtype: 0x5e4b
+  __TEXT.__objc_stubs: 0x13d20
   __DATA_CONST.__got: 0x1ca8
   __DATA_CONST.__const: 0x26b0
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6938
+  __DATA_CONST.__objc_selrefs: 0x69a0
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x578
   __AUTH_CONST.__auth_got: 0x21d8
   __AUTH_CONST.__const: 0x6a90
-  __AUTH_CONST.__cfstring: 0x76c0
-  __AUTH_CONST.__objc_const: 0x22288
+  __AUTH_CONST.__cfstring: 0x7920
+  __AUTH_CONST.__objc_const: 0x22290
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x40

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 267CE467-B803-3BD5-A20A-9351A85809EF
-  Functions: 7888
-  Symbols:   15449
-  CStrings:  8699
+  UUID: 9B30C084-ED0D-324A-A1DA-C172F5982CF5
+  Functions: 7889
+  Symbols:   15467
+  CStrings:  8736
 
Symbols:
+ +[UIColor(ICQUI) colorFromString:]
+ ___34-[ICQBackupController startBackup]_block_invoke.724
+ ___34-[ICQBackupController startBackup]_block_invoke.726
+ ___37-[ICQBackupController cancelRestore:]_block_invoke.721
+ ___38-[ICQBackupController updateBusyState]_block_invoke.708
+ ___39-[ICQUsageStorageController specifiers]_block_invoke.443
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.576
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.577
+ ___54-[ICQBackupController startListeningForThermalChanges]_block_invoke.505
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.585
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.585.cold.1
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.608
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.609
+ ___block_literal_global.729
+ _objc_msgSend$blueColor
+ _objc_msgSend$brownColor
+ _objc_msgSend$colorNamed:
+ _objc_msgSend$cyanColor
+ _objc_msgSend$greenColor
+ _objc_msgSend$orangeColor
+ _objc_msgSend$purpleColor
+ _objc_msgSend$quaternaryLabelColor
+ _objc_msgSend$sfSymbolId
+ _objc_msgSend$symbolSpecification
+ _objc_msgSend$systemIndigoColor
+ _objc_msgSend$systemMintColor
+ _objc_msgSend$systemPinkColor
+ _objc_msgSend$systemTealColor
+ _objc_msgSend$tintColor
+ _objc_msgSend$yellowColor
- ___34-[ICQBackupController startBackup]_block_invoke.727
- ___34-[ICQBackupController startBackup]_block_invoke.729
- ___37-[ICQBackupController cancelRestore:]_block_invoke.724
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
Functions:
~ -[ICQInAppMessaging quotaMessageForOffer:] : 744 -> 932
+ +[UIColor(ICQUI) colorFromString:]
CStrings:
+ "accent"
+ "blueColor"
+ "brownColor"
+ "colorFromString:"
+ "colorNamed:"
+ "cyanColor"
+ "dynamicViewController:contentViewControllerWithDictionary:completionHandler:"
+ "greenColor"
+ "orangeColor"
+ "primary"
+ "purpleColor"
+ "quaternary"
+ "sfSymbolId"
+ "symbolSpecification"
+ "tertiary"
+ "tintColor"
+ "v40@0:8@\"AMSUIDynamicViewController\"16@\"NSDictionary\"24@?<v@?@\"UIViewController\"@\"NSError\">32"
+ "yellowColor"

```
