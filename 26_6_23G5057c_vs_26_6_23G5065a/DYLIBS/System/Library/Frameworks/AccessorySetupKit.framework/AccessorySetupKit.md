## AccessorySetupKit

> `/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`

```diff

-  __TEXT.__text: 0x231ec
-  __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x20e8
-  __TEXT.__const: 0x5d2
-  __TEXT.__gcc_except_tab: 0x47c
-  __TEXT.__cstring: 0x3a91
+  __TEXT.__text: 0x258e0
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_methlist: 0x2160
+  __TEXT.__const: 0x668
+  __TEXT.__gcc_except_tab: 0x49c
+  __TEXT.__cstring: 0x3be1
   __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0x14e
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
-  __TEXT.__unwind_info: 0x858
-  __TEXT.__eh_frame: 0x78
-  __TEXT.__objc_classname: 0x452
-  __TEXT.__objc_methname: 0x6491
-  __TEXT.__objc_methtype: 0x1493
-  __TEXT.__objc_stubs: 0x45a0
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x760
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__oslogstring: 0x32b
+  __TEXT.__swift5_capture: 0xfc
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__eh_frame: 0x1c0
+  __TEXT.__objc_classname: 0x492
+  __TEXT.__objc_methname: 0x6651
+  __TEXT.__objc_methtype: 0x14b3
+  __TEXT.__objc_stubs: 0x4680
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0x788
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19d8
+  __DATA_CONST.__objc_selrefs: 0x1a20
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x470
-  __AUTH_CONST.__cfstring: 0x1620
-  __AUTH_CONST.__objc_const: 0x2dd8
+  __AUTH_CONST.__auth_got: 0x820
+  __AUTH_CONST.__const: 0x4e8
+  __AUTH_CONST.__cfstring: 0x16e0
+  __AUTH_CONST.__objc_const: 0x2e90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xad0
-  __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x990
+  __AUTH_CONST.__objc_doubleobj: 0x10
+  __AUTH.__objc_data: 0xb80
+  __AUTH.__data: 0xb0
+  __DATA.__objc_ivar: 0x1d8
+  __DATA.__data: 0x9c0
   __DATA.__bss: 0x640
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

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
-  Symbols:   2743
-  CStrings:  1853
+  Functions: 858
+  Symbols:   2789
+  CStrings:  1887
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
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
- _OBJC_IVAR_$_ASAccessoryInfoViewController._companionAppLoaded
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
+ "@32@0:8@16^q24"
+ "@76@0:8@16@24@32@40@48B56@60@68"
+ "ASAccessoryCompanionAppResolved"
+ "AccessorySetupKit/ASAccessoryAltMarketplace.swift"
+ "Companion app browser fallback: invalid manufacturer URL: %@"
+ "Failed to convert adamID to UInt64: %s"
+ "Failed to open alt marketplace product page: %s"
+ "Opening alt marketplace product page: distributor=%s, adamID=%s"
+ "T@\"NSString\",R,N,V_distributorBundleID"
+ "T@\"NSString\",R,N,V_distributorName"
+ "View in Browser"
+ "_TtC17AccessorySetupKit25ASAccessoryAltMarketplace"
+ "_companionResolution"
+ "_companionResolutionStarted"
+ "_distributorBundleID"
+ "_distributorName"
+ "_resolvedCompanionAppInfo"
+ "buildSpecifiers"
+ "com.apple.AccessorySetupKit"
+ "com.apple.AppStore"
+ "companionApp"
+ "companionAppBrowser_"
+ "companionAppInfo"
+ "companionSpecifiersFromList:insertIndex:"
+ "distributorBundleID"
+ "distributorName"
+ "initWithBundleID:appInfo:"
+ "initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:distributorBundleID:distributorName:"
+ "insertContiguousSpecifiers:atIndex:animated:"
+ "manufacturerURL"
+ "openProductPageWithDistributorBundleID:adamID:"
+ "postNotificationName:object:"
+ "resolveCompanionAppIfNeeded:"
+ "revealCompanionSectionAnimated"
+ "setPriority:"
+ "subarrayWithRange:"
+ "viewCompanionAppInBrowser:"
- "@60@0:8@16@24@32@40@48B56"
- "T@?,C,N,V_loadingCompletionHandler"
- "_companionAppLoaded"
- "_loadingCompletionHandler"
- "beginUpdates"
- "endUpdates"
- "hasPrefix:"
- "initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:"
- "loadingCompletionHandler"
- "setLoadingCompletionHandler:"

```
