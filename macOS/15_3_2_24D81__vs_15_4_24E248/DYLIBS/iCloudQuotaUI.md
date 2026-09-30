## iCloudQuotaUI

> `/System/Library/PrivateFrameworks/iCloudQuotaUI.framework/Versions/A/iCloudQuotaUI`

```diff

-301.22.3.0.0
-  __TEXT.__text: 0xb1d18
+301.22.4.7.0
+  __TEXT.__text: 0xb0728
   __TEXT.__auth_stubs: 0x25d0
-  __TEXT.__objc_methlist: 0x1824
-  __TEXT.__const: 0x5ec4
-  __TEXT.__gcc_except_tab: 0x65c
-  __TEXT.__cstring: 0x4c2a
-  __TEXT.__oslogstring: 0x301b
+  __TEXT.__objc_methlist: 0x1c54
+  __TEXT.__const: 0x5e94
+  __TEXT.__gcc_except_tab: 0x670
+  __TEXT.__cstring: 0x4b4a
+  __TEXT.__oslogstring: 0x311b
   __TEXT.__dlopen_cstrs: 0x218
-  __TEXT.__swift5_typeref: 0x744c
+  __TEXT.__swift5_typeref: 0x7420
   __TEXT.__swift5_reflstr: 0x14f2
   __TEXT.__swift5_assocty: 0x8b8
   __TEXT.__constg_swiftt: 0x20e0

   __TEXT.__swift5_capture: 0x7c0
   __TEXT.__swift5_proto: 0x3bc
   __TEXT.__swift5_types: 0x1d4
+  __TEXT.__swift_as_entry: 0x90
+  __TEXT.__swift_as_ret: 0x78
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x2cb0
-  __TEXT.__eh_frame: 0x1660
+  __TEXT.__unwind_info: 0x2b38
+  __TEXT.__eh_frame: 0x1668
   __TEXT.__objc_classname: 0x2ec
-  __TEXT.__objc_methname: 0x5d6f
-  __TEXT.__objc_methtype: 0xd56
-  __TEXT.__objc_stubs: 0x4520
-  __DATA_CONST.__got: 0xa20
-  __DATA_CONST.__const: 0x488
+  __TEXT.__objc_methname: 0x5fc1
+  __TEXT.__objc_methtype: 0xd84
+  __TEXT.__objc_stubs: 0x4680
+  __DATA_CONST.__got: 0xa10
+  __DATA_CONST.__const: 0x4a0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1858
+  __DATA_CONST.__objc_selrefs: 0x1a58
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x478
   __AUTH_CONST.__auth_got: 0x12f8
-  __AUTH_CONST.__const: 0x4510
-  __AUTH_CONST.__cfstring: 0x29a0
-  __AUTH_CONST.__objc_const: 0x52e8
+  __AUTH_CONST.__const: 0x45f8
+  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__objc_const: 0x4c48
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x398
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH.__objc_data: 0xc60
-  __AUTH.__data: 0x19f8
-  __DATA.__objc_ivar: 0x1c8
-  __DATA.__data: 0x1f18
-  __DATA.__bss: 0x84b0
+  __AUTH.__data: 0x1a00
+  __DATA.__objc_ivar: 0x1d0
+  __DATA.__data: 0x1ef8
+  __DATA.__bss: 0x8490
   __DATA.__common: 0x270
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: DCD04684-EF92-30A0-8591-12DEEECED2B1
-  Functions: 3965
-  Symbols:   3209
-  CStrings:  2428
+  UUID: 6CF50981-CD0E-326B-92D3-B0673285A020
+  Functions: 3923
+  Symbols:   3273
+  CStrings:  2454
 
Symbols:
+ +[ICQInAppMessage(Examples) dataRecoveryAlert]
+ +[ICQInAppMessaging shared].cold.1
+ -[ICQInAppMessage initWithContentType:identifier:reason:title:subTitle:sfSymbolName:accountId:bundleID:actions:dismissAction:iconSpecification:serverGenerated:]
+ -[ICQInAppMessage serverGenerated]
+ -[ICQInAppMessaging _fetchBRCellularConstraintState]
+ -[ICQInAppMessaging _handleBRCellularConstraintChanged:]
+ -[ICQInAppMessaging _shouldShowBRCellularConstraintMessage]
+ -[ICQInAppMessaging cellularConstraintMessageFromDefaultOffer:]
+ -[ICQInAppMessaging isCellularConstraintReached]
+ -[ICQInAppMessaging setIsCellularConstraintReached:]
+ -[ICQLinkInAppAction _performOverrideUploadOnCellularConstraints]
+ GCC_except_table26
+ GCC_except_table40
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table50
+ GCC_except_table66
+ OBJC_IVAR_$_ICQInAppMessage._serverGenerated
+ OBJC_IVAR_$_ICQInAppMessaging._isCellularConstraintReached
+ _BRCellularConstraintChangedNotification
+ _BRCellularConstraintReachedKey
+ _BROverrideUploadOnCellularConstraints
+ _ICQManageStoragePreferencesURL
+ _ICQUIBRCellularConstraintStateDisabled
+ _ICQUIBRCellularConstraintStateEnabled
+ _ICQUIInAppMessageReasonCellularConstraintReached
+ _ICQUIInAppMessageReasonManageStorageDeleteAlert
+ __39-[ICQInAppMessaging _fetchDefaultOffer]_block_invoke.95
+ __39-[ICQInAppMessaging _fetchPremiumOffer]_block_invoke.91
+ __39-[ICQInAppMessaging _fetchRegularOffer]_block_invoke.89
+ __48-[ICQInAppMessaging fetchMessageWithCompletion:]_block_invoke.83
+ __52-[ICQInAppMessaging _fetchBRCellularConstraintState]_block_invoke.82
+ __76-[ICQInAppMessaging fetchMessageForReason:pendingItemsCount:withCompletion:]_block_invoke.85
+ ___52-[ICQInAppMessaging _fetchBRCellularConstraintState]_block_invoke
+ ___56-[ICQInAppMessaging _handleBRCellularConstraintChanged:]_block_invoke
+ ___57-[ICQInAppMessaging observeUpdatesForBundleID:placement:]_block_invoke
+ ___block_descriptor_48_e8_32s_e5_v8?0l
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e5_v8?0l
+ ___copy_helper_block_e8_32s40r48r56r64r72r
+ ___destroy_helper_block_e8_32s40r48r56r64r72r
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_boxed_opaque_existential_1Tm
+ __isOSVersionAtLeast.cold.1
+ __isPlatformOrVariantPlatformVersionAtLeast.cold.2
+ __isPlatformOrVariantPlatformVersionAtLeast.cold.3
+ __isPlatformOrVariantPlatformVersionAtLeast.cold.4
+ __isPlatformVersionAtLeast.cold.1
+ __isPlatformVersionAtLeast.cold.2
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_iCloudQuotaUI
+ _notify_cancel
+ _notify_get_state
+ _notify_register_check
+ _objc_msgSend$UTF8String
+ _objc_msgSend$_performOverrideUploadOnCellularConstraints
+ _objc_msgSend$_shouldShowBRCellularConstraintMessage
+ _objc_msgSend$boolValue
+ _objc_msgSend$cellularConstraintMessageFromDefaultOffer:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$initWithContentType:identifier:reason:title:subTitle:sfSymbolName:accountId:bundleID:actions:dismissAction:iconSpecification:serverGenerated:
+ _objc_msgSend$isCellularConstraintReached
+ _objc_msgSend$serverGenerated
+ _objc_msgSend$setIsCellularConstraintReached:
+ _symbolic SccySo20NSRunningApplicationC______pG s5ErrorP
+ block_copy_helper.101
+ block_copy_helper.73
+ block_copy_helper.83
+ block_copy_helper.87
+ block_copy_helper.97
+ block_descriptor.103
+ block_descriptor.75
+ block_descriptor.85
+ block_descriptor.89
+ block_descriptor.99
+ block_destroy_helper.102
+ block_destroy_helper.74
+ block_destroy_helper.84
+ block_destroy_helper.88
+ block_destroy_helper.98
- GCC_except_table20
- GCC_except_table34
- GCC_except_table35
- GCC_except_table42
- GCC_except_table44
- GCC_except_table45
- GCC_except_table59
- _OUTLINED_FUNCTION_5
- __39-[ICQInAppMessaging _fetchDefaultOffer]_block_invoke.90
- __39-[ICQInAppMessaging _fetchPremiumOffer]_block_invoke.86
- __39-[ICQInAppMessaging _fetchRegularOffer]_block_invoke.84
- __76-[ICQInAppMessaging fetchMessageForReason:pendingItemsCount:withCompletion:]_block_invoke.80
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_iCloudQuotaUI
- __swift_FORCE_LOAD_$_swiftWebKit
- __swift_FORCE_LOAD_$_swiftWebKit_$_iCloudQuotaUI
- _symbolic _____Sg 13iCloudQuotaUI21PrivateRelayViewModelC6BannerV
- _symbolic _____ySbGSg 7SwiftUI11AnyLocationC
- _symbolic _____y_Qo_ 13iCloudQuotaUI20ManageStorageTipViewV4bodyQrvpQO
- _symbolic _____y_Qo_ 13iCloudQuotaUI26PrivateRelayDataclassSheetV4bodyQrvpQO
- _symbolic _____y_____y__________GABy_____ADG_G 7SwiftUI19_ConditionalContentV7StorageO AA08ModifiedD0V AA6SpacerV AA16_FlexFrameLayoutV 011iCloudQuotaB018UpsellCardItemViewV
- block_copy_helper.100
- block_copy_helper.42
- block_copy_helper.76
- block_copy_helper.86
- block_copy_helper.96
- block_descriptor.102
- block_descriptor.44
- block_descriptor.78
- block_descriptor.88
- block_descriptor.98
- block_destroy_helper.101
- block_destroy_helper.43
- block_destroy_helper.77
- block_destroy_helper.87
- block_destroy_helper.97
CStrings:
+ "%s %d %@"
+ "%s isCellularConstraintReached: %d"
+ "%s, success: %d, error: %@"
+ "%s: BRCellularConstraintChangedNotification status is %d, bailing"
+ "%s: Set cellular constraint state %d. Received %llu"
+ ","
+ "-[ICQInAppMessaging _fetchBRCellularConstraintState]"
+ "-[ICQInAppMessaging _fetchBRCellularConstraintState]_block_invoke"
+ "-[ICQInAppMessaging _handleBRCellularConstraintChanged:]_block_invoke"
+ "-[ICQInAppMessaging _shouldShowBRCellularConstraintMessage]"
+ "-[ICQLinkInAppAction _performOverrideUploadOnCellularConstraints]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/iCloudQuota/iCloudQuotaUI/ICQiCloudPurchaseStorageController.m"
+ "@108@0:8Q16@24@32@40@48@56@64@72@80@88@96B104"
+ "CellularConstraintReached"
+ "ManageStorageDeleteAlert"
+ "No message content found for Cellular Constraint using default message"
+ "TB,N,V_isCellularConstraintReached"
+ "TB,R,N,V_serverGenerated"
+ "UTF8String"
+ "[icqctl] iCloud Notes Are Available For 30 Days"
+ "_fetchBRCellularConstraintState"
+ "_handleBRCellularConstraintChanged:"
+ "_isCellularConstraintReached"
+ "_performOverrideUploadOnCellularConstraints"
+ "_serverGenerated"
+ "_shouldShowBRCellularConstraintMessage"
+ "boolValue"
+ "cellularConstraintMessageFromDefaultOffer:"
+ "dataRecoveryAlert"
+ "decodeBoolForKey:"
+ "encodeBool:forKey:"
+ "iCloud Notes are available for 30 days. After that time, notes will be permanently deleted."
+ "initWithContentType:identifier:reason:title:subTitle:sfSymbolName:accountId:bundleID:actions:dismissAction:iconSpecification:serverGenerated:"
+ "isCellularConstraintReached"
+ "mockDataRecoveryAlert"
+ "serverGenerated"
+ "setIsCellularConstraintReached:"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/iCloudQuota/iCloudQuotaUI/ICQiCloudPurchaseStorageController.m"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
