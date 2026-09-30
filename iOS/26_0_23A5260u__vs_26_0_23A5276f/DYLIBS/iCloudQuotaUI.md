## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/iCloudQuotaUI`

```diff

-301.23.0.16.0
-  __TEXT.__text: 0x16286c
+301.23.0.17.0
+  __TEXT.__text: 0x162ec4
   __TEXT.__auth_stubs: 0x4350
-  __TEXT.__objc_methlist: 0x9b8c
+  __TEXT.__objc_methlist: 0x9bac
   __TEXT.__const: 0x9184
   __TEXT.__gcc_except_tab: 0xfe8
-  __TEXT.__cstring: 0xb3b6
+  __TEXT.__cstring: 0xb466
   __TEXT.__oslogstring: 0xb442
   __TEXT.__dlopen_cstrs: 0x691
   __TEXT.__swift5_typeref: 0x97da

   __TEXT.__unwind_info: 0x5340
   __TEXT.__eh_frame: 0x34c0
   __TEXT.__objc_classname: 0x175b
-  __TEXT.__objc_methname: 0x1a374
-  __TEXT.__objc_methtype: 0x5db7
-  __TEXT.__objc_stubs: 0x13b40
+  __TEXT.__objc_methname: 0x1a4d1
+  __TEXT.__objc_methtype: 0x5ded
+  __TEXT.__objc_stubs: 0x13bc0
   __DATA_CONST.__got: 0x1ca8
-  __DATA_CONST.__const: 0x26b8
+  __DATA_CONST.__const: 0x26b0
   __DATA_CONST.__objc_classlist: 0x5a0
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6938
+  __DATA_CONST.__objc_selrefs: 0x6960
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0x578
   __AUTH_CONST.__auth_got: 0x21b8
   __AUTH_CONST.__const: 0x69f0
-  __AUTH_CONST.__cfstring: 0x7600
-  __AUTH_CONST.__objc_const: 0x22228
+  __AUTH_CONST.__cfstring: 0x76c0
+  __AUTH_CONST.__objc_const: 0x22288
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH.__objc_data: 0x3b10
   __AUTH.__data: 0x2408
-  __DATA.__objc_ivar: 0xbc0
+  __DATA.__objc_ivar: 0xbc8
   __DATA.__data: 0x3fd0
   __DATA.__bss: 0xc978
   __DATA.__common: 0x2a8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CC3D4372-16B3-373A-9BCA-F6295CA6D59B
-  Functions: 7881
-  Symbols:   15439
-  CStrings:  8684
+  UUID: 36B8D681-CBF1-32D1-A535-8E40948F3447
+  Functions: 7884
+  Symbols:   15448
+  CStrings:  8706
 
Symbols:
+ -[ICQInAppMessage conciseTitle]
+ -[ICQInAppMessage initWithContentType:identifier:reason:title:subTitle:conciseTitle:sfSymbolName:sfSymbolColor:accountId:bundleID:actions:dismissAction:iconSpecification:serverGenerated:]
+ -[ICQInAppMessage sfSymbolColor]
+ _ICQUIMessagePlacementInAppConcise
+ _OBJC_IVAR_$_ICQInAppMessage._conciseTitle
+ _OBJC_IVAR_$_ICQInAppMessage._sfSymbolColor
+ ___34-[ICQBackupController startBackup]_block_invoke.727
+ ___34-[ICQBackupController startBackup]_block_invoke.729
+ ___37-[ICQBackupController cancelRestore:]_block_invoke.724
+ ___38-[ICQBackupController updateBusyState]_block_invoke.711
+ ___39-[ICQUsageStorageController specifiers]_block_invoke.446
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.579
+ ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.580
+ ___50-[ICQUpgradeFlowManager sender:action:parameters:]_block_invoke.161
+ ___50-[ICQUpgradeFlowManager sender:action:parameters:]_block_invoke.168
+ ___50-[ICQUpgradeFlowManager sender:action:parameters:]_block_invoke.169
+ ___54-[ICQBackupController startListeningForThermalChanges]_block_invoke.508
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.588
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.588.cold.1
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.611
+ ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.612
+ ___67-[ICQUpgradeFlowManager remoteUIController:didFinishLoadWithError:]_block_invoke.177
+ ___block_literal_global.127
+ ___block_literal_global.133
+ ___block_literal_global.185
+ ___block_literal_global.732
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftMetalKit_$_iCloudQuotaUI
+ __swift_FORCE_LOAD_$_swiftModelIO
+ __swift_FORCE_LOAD_$_swiftModelIO_$_iCloudQuotaUI
+ _objc_msgSend$conciseTitle
+ _objc_msgSend$conciseTitleWithKey:
+ _objc_msgSend$initWithContentType:identifier:reason:title:subTitle:conciseTitle:sfSymbolName:sfSymbolColor:accountId:bundleID:actions:dismissAction:iconSpecification:serverGenerated:
+ _objc_msgSend$initWithImage:style:target:action:
+ _objc_msgSend$sfSymbolColor
- ___34-[ICQBackupController startBackup]_block_invoke.724
- ___34-[ICQBackupController startBackup]_block_invoke.726
- ___37-[ICQBackupController cancelRestore:]_block_invoke.721
- ___38-[ICQBackupController updateBusyState]_block_invoke.708
- ___39-[ICQUsageStorageController specifiers]_block_invoke.443
- ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.576
- ___50-[ICQBackupController _setBackupEnabled:passcode:]_block_invoke.577
- ___50-[ICQUpgradeFlowManager sender:action:parameters:]_block_invoke.157
- ___50-[ICQUpgradeFlowManager sender:action:parameters:]_block_invoke.164
- ___50-[ICQUpgradeFlowManager sender:action:parameters:]_block_invoke.165
- ___54-[ICQBackupController startListeningForThermalChanges]_block_invoke.505
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.585
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.585.cold.1
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.608
- ___62-[ICQBackupController _persistBackupEnablementState:passcode:]_block_invoke.609
- ___67-[ICQUpgradeFlowManager remoteUIController:didFinishLoadWithError:]_block_invoke.173
- ___block_literal_global.123
- ___block_literal_global.181
- ___block_literal_global.729
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_iCloudQuotaUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_iCloudQuotaUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_iCloudQuotaUI
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_iCloudQuotaUI
- _objc_msgSend$_symbolNameForQuotaOffer:
CStrings:
+ "."
+ "@124@0:8Q16@24@32@40@48@56@64@72@80@88@96@104@112B120"
+ "In-App Message for bundle ID %@ with title: %@, subTitle: %@, conciseTitle:%@, sfSymbolID:%@ sfSymbolColor:%@, actions:\n%@"
+ "InAppConcise"
+ "T@\"NSString\",R,C,N,V_conciseTitle"
+ "T@\"UIColor\",R,C,N,V_sfSymbolColor"
+ "[icqctl] iCloud Storage Almost Full"
+ "[icqctl] iCloud Storage Full"
+ "_conciseTitle"
+ "_sfSymbolColor"
+ "conciseTitle"
+ "conciseTitleWithKey:"
+ "exclamationmark.icloud.fill"
+ "initWithContentType:identifier:reason:title:subTitle:conciseTitle:sfSymbolName:sfSymbolColor:accountId:bundleID:actions:dismissAction:iconSpecification:serverGenerated:"
+ "initWithImage:style:target:action:"
+ "sfSymbolColor"
- "In-App Message for bundle ID %@ with title: %@, subTitle: %@, actions:\n%@"

```
