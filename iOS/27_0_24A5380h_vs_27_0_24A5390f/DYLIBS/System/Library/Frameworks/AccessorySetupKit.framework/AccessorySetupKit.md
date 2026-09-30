## AccessorySetupKit

> `/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`

```diff

-2700.27.0.0.0
-  __TEXT.__text: 0x22544
-  __TEXT.__objc_methlist: 0x20f0
-  __TEXT.__const: 0x5d2
-  __TEXT.__gcc_except_tab: 0x4d0
-  __TEXT.__cstring: 0x3ab1
+2700.30.0.0.0
+  __TEXT.__text: 0x24958
+  __TEXT.__objc_methlist: 0x2168
+  __TEXT.__const: 0x658
+  __TEXT.__gcc_except_tab: 0x4e4
+  __TEXT.__cstring: 0x3c01
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0x15a
-  __TEXT.__swift5_typeref: 0x2ca
+  __TEXT.__swift5_typeref: 0x2f6
   __TEXT.__swift5_reflstr: 0x119
   __TEXT.__swift5_assocty: 0x60
-  __TEXT.__constg_swiftt: 0x2dc
+  __TEXT.__constg_swiftt: 0x308
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_fieldmd: 0xe8
+  __TEXT.__swift5_fieldmd: 0xf8
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__oslogstring: 0x28b
-  __TEXT.__swift5_capture: 0xc0
-  __TEXT.__unwind_info: 0x7b8
-  __TEXT.__eh_frame: 0x78
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__oslogstring: 0x32b
+  __TEXT.__swift5_capture: 0xec
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0x8
+  __TEXT.__unwind_info: 0x848
+  __TEXT.__eh_frame: 0x198
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x758
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__const: 0x780
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19e0
+  __DATA_CONST.__objc_selrefs: 0x1a28
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x4d0
-  __AUTH_CONST.__const: 0x470
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x2de0
+  __DATA_CONST.__got: 0x4f8
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x16e0
+  __AUTH_CONST.__objc_const: 0x2eb8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x810
-  __AUTH.__objc_data: 0xad0
-  __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x990
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH_CONST.__auth_got: 0x898
+  __AUTH.__objc_data: 0x188
+  __AUTH.__data: 0x30
+  __DATA.__objc_ivar: 0x1dc
+  __DATA.__data: 0x9c0
   __DATA.__bss: 0x640
   __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x9f8
+  __DATA_DIRTY.__data: 0x90
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 821
-  Symbols:   1973
-  CStrings:  421
+  Functions: 853
+  Symbols:   2015
+  CStrings:  434
 
Symbols:
+ +[ASAccessoryInfoViewController companionSpecifiersFromList:insertIndex:]
+ -[ASAccessoryCompanionAppInfo distributorBundleID]
+ -[ASAccessoryCompanionAppInfo distributorName]
+ -[ASAccessoryCompanionAppInfo initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:distributorBundleID:distributorName:]
+ -[ASAccessoryCompanionAppView initWithBundleID:appInfo:]
+ -[ASAccessoryInfoViewController buildSpecifiers]
+ -[ASAccessoryInfoViewController resolveCompanionAppIfNeeded:]
+ -[ASAccessoryInfoViewController revealCompanionSectionAnimated]
+ -[ASAccessoryInfoViewController viewCompanionAppInBrowser:]
+ GCC_except_table1
+ GCC_except_table10
+ GCC_except_table12
+ GCC_except_table65
+ GCC_except_table70
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$__TtC17AccessorySetupKit25ASAccessoryAltMarketplace
+ _OBJC_IVAR_$_ASAccessoryCompanionAppInfo._distributorBundleID
+ _OBJC_IVAR_$_ASAccessoryCompanionAppInfo._distributorName
+ _OBJC_IVAR_$_ASAccessoryInfoViewController._companionResolution
+ _OBJC_IVAR_$_ASAccessoryInfoViewController._companionResolutionStarted
+ _OBJC_IVAR_$_ASAccessoryInfoViewController._resolvedCompanionAppInfo
+ _OBJC_METACLASS_$__TtC17AccessorySetupKit25ASAccessoryAltMarketplace
+ _PSTableCellHeightKey
+ __CLASS_METHODS__TtC17AccessorySetupKit25ASAccessoryAltMarketplace
+ __DATA__TtC17AccessorySetupKit25ASAccessoryAltMarketplace
+ __INSTANCE_METHODS__TtC17AccessorySetupKit25ASAccessoryAltMarketplace
+ __METACLASS_DATA__TtC17AccessorySetupKit25ASAccessoryAltMarketplace
+ __OBJC_$_CLASS_METHODS_ASAccessoryInfoViewController
+ ___56-[ASAccessoryCompanionAppView initWithBundleID:appInfo:]_block_invoke
+ ___56-[ASAccessoryCompanionAppView initWithBundleID:appInfo:]_block_invoke_2
+ ___61-[ASAccessoryInfoViewController resolveCompanionAppIfNeeded:]_block_invoke
+ ___61-[ASAccessoryInfoViewController resolveCompanionAppIfNeeded:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e49_v24?0"ASAccessoryCompanionAppInfo"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _objc_msgSend$buildSpecifiers
+ _objc_msgSend$companionSpecifiersFromList:insertIndex:
+ _objc_msgSend$distributorBundleID
+ _objc_msgSend$distributorName
+ _objc_msgSend$initWithBundleID:appInfo:
+ _objc_msgSend$initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:distributorBundleID:distributorName:
+ _objc_msgSend$insertContiguousSpecifiers:atIndex:animated:
+ _objc_msgSend$manufacturerURL
+ _objc_msgSend$openProductPageWithDistributorBundleID:adamID:
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$resolveCompanionAppIfNeeded:
+ _objc_msgSend$revealCompanionSectionAnimated
+ _objc_msgSend$setPriority:
+ _objc_msgSend$subarrayWithRange:
+ _swift_getErrorValue
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _symbolic SS
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic _____ 17AccessorySetupKit25ASAccessoryAltMarketplaceC
+ _symbolic _____XMT 17AccessorySetupKit25ASAccessoryAltMarketplaceC
+ _symbolic ytIeAgHr_
- -[ASAccessoryCompanionAppInfo initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:]
- -[ASAccessoryCompanionAppView loadingCompletionHandler]
- -[ASAccessoryCompanionAppView setLoadingCompletionHandler:]
- -[ASAccessoryInfoViewController tableView:heightForRowAtIndexPath:]
- GCC_except_table0
- GCC_except_table64
- GCC_except_table9
- _OBJC_IVAR_$_ASAccessoryCompanionAppView._loadingCompletionHandler
- ___48-[ASAccessoryCompanionAppView initWithBundleID:]_block_invoke
- ___48-[ASAccessoryCompanionAppView initWithBundleID:]_block_invoke_2
- ___65-[ASAccessoryInfoViewController tableView:cellForRowAtIndexPath:]_block_invoke_2
- ___65-[ASAccessoryInfoViewController tableView:cellForRowAtIndexPath:]_block_invoke_3
- ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
- _objc_msgSend$beginUpdates
- _objc_msgSend$endUpdates
- _objc_msgSend$hasPrefix:
- _objc_msgSend$initWithBundleID:
- _objc_msgSend$initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:
- _objc_msgSend$loadingCompletionHandler
- _objc_msgSend$setLoadingCompletionHandler:
CStrings:
+ "-[ASAccessoryInfoViewController viewCompanionAppInBrowser:]"
+ "ASAccessoryCompanionAppResolved"
+ "AccessorySetupKit/ASAccessoryAltMarketplace.swift"
+ "Companion app browser fallback: invalid manufacturer URL: %@"
+ "Failed to convert adamID to UInt64: %s"
+ "Failed to open alt marketplace product page: %s"
+ "Opening alt marketplace product page: distributor=%s, adamID=%s"
+ "View in Browser"
+ "com.apple.AccessorySetupKit"
+ "com.apple.AppStore"
+ "companionApp"
+ "companionAppBrowser_"
+ "companionAppInfo"
```
