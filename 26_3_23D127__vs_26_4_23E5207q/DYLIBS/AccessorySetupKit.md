## AccessorySetupKit

> `/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`

```diff

-323.7.0.0.0
-  __TEXT.__text: 0x1d2a4
-  __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x1d90
-  __TEXT.__const: 0x4e2
-  __TEXT.__cstring: 0x366a
-  __TEXT.__gcc_except_tab: 0x3d0
+324.20.1.1.1
+  __TEXT.__text: 0x2123c
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__objc_methlist: 0x1e90
+  __TEXT.__const: 0x4f2
+  __TEXT.__gcc_except_tab: 0x47c
+  __TEXT.__cstring: 0x35e1
+  __TEXT.__dlopen_cstrs: 0x47
   __TEXT.__ustring: 0x14e
   __TEXT.__constg_swiftt: 0x284
-  __TEXT.__swift5_typeref: 0x29e
+  __TEXT.__swift5_typeref: 0x2aa
   __TEXT.__swift5_reflstr: 0x109
   __TEXT.__swift5_fieldmd: 0xcc
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_types: 0x10
   __TEXT.__oslogstring: 0x28b
   __TEXT.__swift5_capture: 0xc0
-  __TEXT.__unwind_info: 0x6e8
+  __TEXT.__unwind_info: 0x7e8
   __TEXT.__eh_frame: 0x78
-  __TEXT.__objc_classname: 0x356
-  __TEXT.__objc_methname: 0x55c2
-  __TEXT.__objc_methtype: 0x1293
-  __TEXT.__objc_stubs: 0x3620
-  __DATA_CONST.__got: 0x3d8
-  __DATA_CONST.__const: 0x5a0
+  __TEXT.__objc_classname: 0x3e2
+  __TEXT.__objc_methname: 0x5ecb
+  __TEXT.__objc_methtype: 0x13f3
+  __TEXT.__objc_stubs: 0x4480
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__const: 0x738
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1660
+  __DATA_CONST.__objc_selrefs: 0x1868
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH_CONST.__const: 0x410
-  __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0x2a80
+  __AUTH_CONST.__auth_got: 0x6f8
+  __AUTH_CONST.__const: 0x430
+  __AUTH_CONST.__cfstring: 0x1500
+  __AUTH_CONST.__objc_const: 0x2bb8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xa08
   __AUTH.__data: 0x68
-  __DATA.__objc_ivar: 0x1a8
-  __DATA.__data: 0x890
-  __DATA.__bss: 0x4a0
+  __DATA.__objc_ivar: 0x1c4
+  __DATA.__data: 0x8a0
+  __DATA.__bss: 0x4c0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0F6AB3C2-0D83-32B0-B28F-1A1BB6CC6CE5
-  Functions: 727
-  Symbols:   2397
-  CStrings:  1654
+  UUID: 8823701C-0A6B-3949-AC02-26CF7463815D
+  Functions: 773
+  Symbols:   2646
+  CStrings:  1760
 
Symbols:
+ +[ASAccessoryCompanionAppInfo appInfoWithBundleID:completion:]
+ -[ASAccessoryCompanionAppCell isLoaded]
+ -[ASAccessoryCompanionAppCell markAsLoaded]
+ -[ASAccessoryCompanionAppInfo adamID]
+ -[ASAccessoryCompanionAppInfo appIsInstalled]
+ -[ASAccessoryCompanionAppInfo initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:]
+ -[ASAccessoryCompanionAppView _presentStoreProductViewController]
+ -[ASAccessoryCompanionAppView _presentStoreProductViewController].cold.1
+ -[ASAccessoryCompanionAppView _refreshAppInfo]
+ -[ASAccessoryCompanionAppView _updateUIWithAppInfo:]
+ -[ASAccessoryCompanionAppView hasUpdatedUI]
+ -[ASAccessoryCompanionAppView loadingCompletionHandler]
+ -[ASAccessoryCompanionAppView productViewControllerDidFinish:]
+ -[ASAccessoryCompanionAppView setHasUpdatedUI:]
+ -[ASAccessoryCompanionAppView setLoadingCompletionHandler:]
+ -[ASAccessoryCompanionAppView setStoreProductViewHandler:]
+ -[ASAccessoryCompanionAppView storeProductViewHandler]
+ -[ASAccessoryInfoViewController notificationsAuthString:]
+ -[ASAccessoryInfoViewController openNotificationsSettings:]
+ -[ASAccessoryInfoViewController specifiersForNotificationsSection]
+ -[ASAccessoryInfoViewController tableView:heightForRowAtIndexPath:]
+ -[ASPickerDisplayItem(DADiscoveryConfigurationConversion) discoveryConfigurationWithBundleID:]
+ GCC_except_table0
+ GCC_except_table6
+ GCC_except_table62
+ GCC_except_table8
+ _NSLog
+ _NSSelectorFromString
+ _OBJC_CLASS_$_DAAppAssetManager
+ _OBJC_CLASS_$_DADiscoveryConfiguration
+ _OBJC_CLASS_$_DAPropertyCompareString
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_IVAR_$_ASAccessoryCompanionAppCell._isLoaded
+ _OBJC_IVAR_$_ASAccessoryCompanionAppInfo._adamID
+ _OBJC_IVAR_$_ASAccessoryCompanionAppInfo._appIsInstalled
+ _OBJC_IVAR_$_ASAccessoryCompanionAppView._hasUpdatedUI
+ _OBJC_IVAR_$_ASAccessoryCompanionAppView._loadingCompletionHandler
+ _OBJC_IVAR_$_ASAccessoryCompanionAppView._storeProductViewHandler
+ _OBJC_IVAR_$_ASAccessoryInfoViewController._companionAppLoaded
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _StoreKitLibrary
+ _StoreKitLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_ASAccessoryCompanionAppInfo
+ __OBJC_$_CLASS_METHODS_ASPickerDisplayItem(NSDataConversion|DADiscoveryConfigurationConversion)
+ __OBJC_$_INSTANCE_METHODS_ASPickerDisplayItem(NSDataConversion|DADiscoveryConfigurationConversion)
+ ___46-[ASAccessoryCompanionAppView _refreshAppInfo]_block_invoke
+ ___46-[ASAccessoryCompanionAppView _refreshAppInfo]_block_invoke_2
+ ___48-[ASAccessoryCompanionAppView initWithBundleID:]_block_invoke
+ ___52-[ASAccessoryCompanionAppView _updateUIWithAppInfo:]_block_invoke
+ ___62+[ASAccessoryCompanionAppInfo appInfoWithBundleID:completion:]_block_invoke
+ ___62+[ASAccessoryCompanionAppInfo appInfoWithBundleID:completion:]_block_invoke_2
+ ___62+[ASAccessoryCompanionAppInfo appInfoWithBundleID:completion:]_block_invoke_3
+ ___62+[ASAccessoryCompanionAppInfo appInfoWithBundleID:completion:]_block_invoke_4
+ ___62-[ASAccessoryCompanionAppView productViewControllerDidFinish:]_block_invoke
+ ___62-[ASAccessoryInfoViewController specifiersForAppAccessSection]_block_invoke_2
+ ___65-[ASAccessoryCompanionAppView _presentStoreProductViewController]_block_invoke
+ ___65-[ASAccessoryInfoViewController tableView:cellForRowAtIndexPath:]_block_invoke
+ ___65-[ASAccessoryInfoViewController tableView:cellForRowAtIndexPath:]_block_invoke_2
+ ___65-[ASAccessoryInfoViewController tableView:cellForRowAtIndexPath:]_block_invoke_3
+ ___65-[ASAccessoryInfoViewController tableView:cellForRowAtIndexPath:]_block_invoke_4
+ ___67-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke.cold.1
+ ___67-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke.cold.2
+ ___67-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke.cold.3
+ ___StoreKitLibraryCore_block_invoke
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e25_B24?08"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32w_e26_v16?0"UIViewController"8lw32l8
+ ___block_descriptor_40_e8_32w_e49_v24?0"ASAccessoryCompanionAppInfo"8"NSError"16lw32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_49_e8_32s40bs_e32_v24?0"DAAppAsset"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e36_v32?0"ASPickerDisplayItem"8Q16^B24lr40l8r48l8r56l8s32l8r64l8r72l8
+ ___block_literal_global.109
+ ___block_literal_global.366
+ ___block_literal_global.415
+ ___block_literal_global.439
+ ___block_literal_global.443
+ ___block_literal_global.587
+ ___block_literal_global.98
+ ___getSKStoreProductParameterITunesItemIdentifierSymbolLoc_block_invoke
+ ___getSKStoreProductViewControllerClass_block_invoke
+ ___getSKStoreProductViewControllerClass_block_invoke.cold.1
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringStoreKit
+ _block_copy_helper.72
+ _block_copy_helper.78
+ _block_copy_helper.82
+ _block_copy_helper.89
+ _block_descriptor.74
+ _block_descriptor.80
+ _block_descriptor.84
+ _block_descriptor.91
+ _block_destroy_helper.73
+ _block_destroy_helper.79
+ _block_destroy_helper.83
+ _block_destroy_helper.90
+ _dispatch_get_global_queue
+ _dlerror
+ _dlsym
+ _getSKStoreProductParameterITunesItemIdentifierSymbolLoc.ptr
+ _getSKStoreProductViewControllerClass.softClass
+ _kTCCServiceAccessoryNotifications
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_msgSend$_presentStoreProductViewController
+ _objc_msgSend$_refreshAppInfo
+ _objc_msgSend$_updateUIWithAppInfo:
+ _objc_msgSend$activateConnectionWithSession:with:pickerSettings:for:requiresUI:completionHandler:
+ _objc_msgSend$adamID
+ _objc_msgSend$animateWithDuration:animations:
+ _objc_msgSend$appInfoWithBundleID:completion:
+ _objc_msgSend$appIsInstalled
+ _objc_msgSend$appName
+ _objc_msgSend$appView
+ _objc_msgSend$arrayToData:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$beginUpdates
+ _objc_msgSend$companionAppBundleID
+ _objc_msgSend$companionAppSpecifiers:
+ _objc_msgSend$compare:
+ _objc_msgSend$configureConnection:
+ _objc_msgSend$connectionWithEndpoint:
+ _objc_msgSend$developerName
+ _objc_msgSend$deviceRegistry
+ _objc_msgSend$discoveryConfigurationWithBundleID:
+ _objc_msgSend$endDiscoveryInPicker
+ _objc_msgSend$endUpdates
+ _objc_msgSend$endpointForMachName:service:instance:
+ _objc_msgSend$failAccessory:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$getAppAssetForBundleID:completion:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$iconData
+ _objc_msgSend$iconView
+ _objc_msgSend$imageAsset
+ _objc_msgSend$initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$installedLabel
+ _objc_msgSend$integerValue
+ _objc_msgSend$interfaceWithIdentifier:
+ _objc_msgSend$invalidateIntrinsicContentSize
+ _objc_msgSend$invocationWithMethodSignature:
+ _objc_msgSend$invoke
+ _objc_msgSend$isKindOfClass:
+ _objc_msgSend$isLoaded
+ _objc_msgSend$loadingCompletionHandler
+ _objc_msgSend$markAsLoaded
+ _objc_msgSend$methodSignatureForSelector:
+ _objc_msgSend$migrateSilentlyWithOverrideBundleID:
+ _objc_msgSend$nameLabel
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$openSensitiveURL:withOptions:
+ _objc_msgSend$pickerDidReport:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$preflightMigrationWithConfigurations:session:error:
+ _objc_msgSend$protocolForProtocol:
+ _objc_msgSend$publisherLabel
+ _objc_msgSend$queue
+ _objc_msgSend$relayPickerEvent:
+ _objc_msgSend$remoteTargetWithLaunchingAssertionAttributes:
+ _objc_msgSend$renameAccessory:currentName:updateSSID:overrideBundleID:
+ _objc_msgSend$setActivationHandler:
+ _objc_msgSend$setAllowsRename:
+ _objc_msgSend$setAlpha:
+ _objc_msgSend$setAppInfo:
+ _objc_msgSend$setArgument:atIndex:
+ _objc_msgSend$setAssociationIdentifier:
+ _objc_msgSend$setBluetoothCompanyIdentifiers:
+ _objc_msgSend$setBluetoothCompanyPayload:
+ _objc_msgSend$setBluetoothCompanyPayloadMask:
+ _objc_msgSend$setBluetoothIdentifier:
+ _objc_msgSend$setBluetoothNameSubstring:
+ _objc_msgSend$setBluetoothNameSubstringCompareOptions:
+ _objc_msgSend$setBluetoothRange:
+ _objc_msgSend$setBluetoothServicePayload:
+ _objc_msgSend$setBluetoothServicePayloadMask:
+ _objc_msgSend$setBluetoothServices:
+ _objc_msgSend$setClient:
+ _objc_msgSend$setClientMessagingExpectation:
+ _objc_msgSend$setExistingDeviceIdentifier:
+ _objc_msgSend$setFlags:
+ _objc_msgSend$setHasUpdatedUI:
+ _objc_msgSend$setHidden:
+ _objc_msgSend$setHotspotSSIDPrefixes:
+ _objc_msgSend$setHotspotSSIDs:
+ _objc_msgSend$setInterface:
+ _objc_msgSend$setInterfaceTarget:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setLoadingCompletionHandler:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$setNetworkHotspotSSID:
+ _objc_msgSend$setSelector:
+ _objc_msgSend$setServer:
+ _objc_msgSend$setServiceQuality:
+ _objc_msgSend$setStoreProductViewHandler:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$setTargetQueue:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setWifiAwareModelNameMatch:
+ _objc_msgSend$setWifiAwarePairingID:
+ _objc_msgSend$setWifiAwareServiceName:
+ _objc_msgSend$setWifiAwareServiceType:
+ _objc_msgSend$setWifiAwareVendorNameMatch:
+ _objc_msgSend$sharedManager
+ _objc_msgSend$showMigrationPickerWithOverrideBundleID:
+ _objc_msgSend$showPermissionPrompt:accessoryIdentifier:accessoryName:authorizationLevel:overrideBundleID:
+ _objc_msgSend$showPickerWithOverrideBundleID:shouldRetrieveDisplayItems:needsBluetooth:needsWiFi:needsDeviceOTANameBroadcast:discoveryTimeout:filterInApp:
+ _objc_msgSend$size
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$specifiersForNotificationsSection
+ _objc_msgSend$storeItemIdentifier
+ _objc_msgSend$storeProductViewHandler
+ _objc_msgSend$stringValue
+ _objc_msgSend$updateMigrationDisplayCount:
+ _objc_msgSend$updatePickerWith:
+ _objc_msgSend$upgradeAccessory:needsBluetooth:needsWiFi:needsDeviceOTANameBroadcast:discoveryTimeout:overrideBundleID:
+ _objc_msgSend$userInitiated
+ _objc_msgSend$viewButton
+ _objc_opt_respondsToSelector
+ _swift_bridgeObjectRelease_n
+ _symbolic _____Sg_ABt 10Foundation4UUIDV
- -[ASAccessoryCompanionAppInfo initWithBundleID:]
- -[ASAccessorySession updateAuthorization:descriptor:completionHandler:].cold.5
- __OBJC_$_CLASS_METHODS_ASPickerDisplayItem(NSDataConversion)
- __OBJC_$_INSTANCE_METHODS_ASPickerDisplayItem(NSDataConversion)
- ___67-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke_2.cold.1
- ___67-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke_2.cold.2
- ___67-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke_2.cold.3
- ___block_descriptor_72_e8_32s40r48r56r64r_e36_v32?0"ASPickerDisplayItem"8Q16^B24lr40l8r48l8s32l8r56l8r64l8
- ___block_literal_global.23
- ___block_literal_global.270
- ___block_literal_global.315
- ___block_literal_global.329
- ___block_literal_global.333
- ___block_literal_global.34
- ___block_literal_global.474
- _block_copy_helper.71
- _block_copy_helper.77
- _block_copy_helper.81
- _block_copy_helper.88
- _block_descriptor.73
- _block_descriptor.79
- _block_descriptor.83
- _block_descriptor.90
- _block_destroy_helper.72
- _block_destroy_helper.78
- _block_destroy_helper.82
- _block_destroy_helper.89
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$activateConnectionWithSession:with:pickerSettings:for:completionHandler:
- _objc_retain_x3
CStrings:
+ "%s"
+ "-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke"
+ "@60@0:8@16@24@32@40@48B56"
+ "Allow this accessory to receive iPhone notifications."
+ "B24@?0@8@\"NSDictionary\"16"
+ "DADiscoveryConfigurationConversion"
+ "Error loading product: %@"
+ "FORWARDING"
+ "Notifications"
+ "Off"
+ "On"
+ "SKStoreProductParameterITunesItemIdentifier"
+ "SKStoreProductViewController"
+ "StoreKit framework is not available"
+ "T@\"NSString\",R,N,V_adamID"
+ "T@?,C,N,V_loadingCompletionHandler"
+ "T@?,C,N,V_storeProductViewHandler"
+ "TB,N,V_hasUpdatedUI"
+ "TB,R,N,V_appIsInstalled"
+ "Unable to find class %s"
+ "VIEW"
+ "_adamID"
+ "_appIsInstalled"
+ "_companionAppLoaded"
+ "_hasUpdatedUI"
+ "_isLoaded"
+ "_loadingCompletionHandler"
+ "_presentStoreProductViewController"
+ "_refreshAppInfo"
+ "_storeProductViewHandler"
+ "_updateUIWithAppInfo:"
+ "activateConnectionWithSession:with:pickerSettings:for:requiresUI:completionHandler:"
+ "adamID"
+ "animateWithDuration:animations:"
+ "appInfoWithBundleID:completion:"
+ "appIsInstalled"
+ "appName"
+ "beginUpdates"
+ "companionAppBundleID"
+ "compare:"
+ "delegate"
+ "developerName"
+ "deviceRegistry"
+ "discoveryConfigurationWithBundleID:"
+ "endUpdates"
+ "filteredArrayUsingPredicate:"
+ "getAppAssetForBundleID:completion:"
+ "hasPrefix:"
+ "hasUpdatedUI"
+ "iconData"
+ "initWithBundleID:name:publisherName:adamID:icon:appIsInstalled:"
+ "invalidateIntrinsicContentSize"
+ "invocationWithMethodSignature:"
+ "invoke"
+ "isLoaded"
+ "loadProductWithParameters:completionBlock:"
+ "loadingCompletionHandler"
+ "markAsLoaded"
+ "methodSignatureForSelector:"
+ "migrateSilentlyWithOverrideBundleID:"
+ "notifications"
+ "notificationsAuthString:"
+ "numberWithUnsignedShort:"
+ "openNotificationsSettings:"
+ "openSensitiveURL:withOptions:"
+ "predicateWithBlock:"
+ "preflightMigrationWithConfigurations:session:error:"
+ "productViewControllerDidFinish:"
+ "setAlpha:"
+ "setArgument:atIndex:"
+ "setAssociationIdentifier:"
+ "setBluetoothCompanyIdentifiers:"
+ "setBluetoothCompanyPayload:"
+ "setBluetoothCompanyPayloadMask:"
+ "setBluetoothServicePayload:"
+ "setBluetoothServicePayloadMask:"
+ "setBluetoothServices:"
+ "setExistingDeviceIdentifier:"
+ "setFlags:"
+ "setHasUpdatedUI:"
+ "setHidden:"
+ "setHotspotSSIDPrefixes:"
+ "setHotspotSSIDs:"
+ "setLoadingCompletionHandler:"
+ "setNeedsLayout"
+ "setNetworkHotspotSSID:"
+ "setSelector:"
+ "setStoreProductViewHandler:"
+ "setTarget:"
+ "setValue:forKey:"
+ "setWifiAwareServiceType:"
+ "settings-navigation://com.apple.Settings.Notifications/NOTIFICATION_FORWARDING_ID"
+ "sharedManager"
+ "showPickerWithOverrideBundleID:device:assetDescriptorData:targetBundleType:"
+ "softlink:r:path:/System/Library/Frameworks/StoreKit.framework/StoreKit"
+ "sortUsingComparator:"
+ "specifiersForNotificationsSection"
+ "storeItemIdentifier"
+ "storeProductViewHandler"
+ "stringValue"
+ "v16@?0@\"UIViewController\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@\"ASAccessoryCompanionAppInfo\"8@\"NSError\"16"
+ "v24@?0@\"DAAppAsset\"8@\"NSError\"16"
+ "v48@0:8@\"NSString\"16@\"DADevice\"24@\"NSData\"32@\"NSNumber\"40"
+ "v60@0:8@16@24@32@40B48@?52"
- "-[ASAccessorySession _showPickerForDisplayItems:completionHandler:]_block_invoke_2"
- "activateConnectionWithSession:with:pickerSettings:for:completionHandler:"
- "showPickerWithOverrideBundleID:device:assetDescriptorData:"
- "v40@0:8@\"NSString\"16@\"DADevice\"24@\"NSData\"32"
- "v56@0:8@16@24@32@40@?48"

```
