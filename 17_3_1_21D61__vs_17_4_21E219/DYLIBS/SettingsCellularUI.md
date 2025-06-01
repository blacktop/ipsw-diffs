## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-401.3.0.0.0
-  __TEXT.__text: 0x69024
+464.1.0.0.0
+  __TEXT.__text: 0x6f6f8
   __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_methlist: 0x65b8
+  __TEXT.__objc_methlist: 0x6c50
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x6681
-  __TEXT.__oslogstring: 0x576e
-  __TEXT.__gcc_except_tab: 0xcd8
-  __TEXT.__dlopen_cstrs: 0x4af
+  __TEXT.__cstring: 0x6abc
+  __TEXT.__oslogstring: 0x5a62
+  __TEXT.__gcc_except_tab: 0xda0
+  __TEXT.__dlopen_cstrs: 0x4fe
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x18f0
-  __TEXT.__objc_classname: 0x109f
-  __TEXT.__objc_methname: 0xf936
-  __TEXT.__objc_methtype: 0x22e7
-  __TEXT.__objc_stubs: 0xb120
-  __DATA_CONST.__got: 0x350
-  __DATA_CONST.__const: 0xc10
-  __DATA_CONST.__objc_classlist: 0x398
+  __TEXT.__unwind_info: 0x1ab4
+  __TEXT.__objc_classname: 0x114e
+  __TEXT.__objc_methname: 0x10614
+  __TEXT.__objc_methtype: 0x23fa
+  __TEXT.__objc_stubs: 0xb920
+  __DATA_CONST.__got: 0x380
+  __DATA_CONST.__const: 0xce8
+  __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x13ac8
-  __DATA_CONST.__objc_selrefs: 0x3b38
+  __DATA_CONST.__objc_const: 0x151d0
+  __DATA_CONST.__objc_selrefs: 0x3d88
+  __DATA_CONST.__objc_classrefs: 0x718
+  __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__cfstring: 0x56a0
-  __AUTH_CONST.__objc_const: 0x2a98
-  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x5a80
+  __AUTH_CONST.__objc_const: 0x2c48
+  __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x420
-  __AUTH.__objc_data: 0x1220
-  __DATA.__objc_classrefs: 0x6f0
-  __DATA.__objc_superrefs: 0x358
-  __DATA.__objc_ivar: 0x460
-  __DATA.__data: 0x8a0
+  __AUTH.__objc_data: 0x13b0
+  __DATA.__objc_ivar: 0x4ac
+  __DATA.__data: 0x900
   __DATA.__bss: 0x90
-  __DATA_DIRTY.__objc_ivar: 0x3b4
+  __DATA_DIRTY.__objc_ivar: 0x404
   __DATA_DIRTY.__objc_data: 0x11d0
-  __DATA_DIRTY.__bss: 0x1f8
+  __DATA_DIRTY.__bss: 0x208
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1088838A-3CE3-380C-B14D-7FDBC4F00CA4
-  Functions: 2303
-  Symbols:   8235
-  CStrings:  5231
+  UUID: 4880103C-1443-3626-9C06-9450D56ED5EC
+  Functions: 2455
+  Symbols:   8723
+  CStrings:  5447
 
Symbols:
+ +[PSUICarrierItemTableCell cellStyle]
+ +[SettingsCellularUtils noDataConnectivityAvailable]
+ -[CTCapability acceptCapabilityforSlotID:status:canSet:info:]
+ -[CTCapability getCapabilityInfoObject:forSlotID:]
+ -[CTCapability setCapabilityInfoObject:forKey:forSlotID:]
+ -[PSUIAddNewPlanController .cxx_destruct]
+ -[PSUIAddNewPlanController QRCodeGroupSpecifier]
+ -[PSUIAddNewPlanController QRCodeGroup]
+ -[PSUIAddNewPlanController addCancelButton]
+ -[PSUIAddNewPlanController addOnGroupSpecifier]
+ -[PSUIAddNewPlanController addOnPlanGroup]
+ -[PSUIAddNewPlanController cancelButton]
+ -[PSUIAddNewPlanController carrierItemGroupSpecifier]
+ -[PSUIAddNewPlanController carrierItemGroup]
+ -[PSUIAddNewPlanController cellularPlanChanged:]
+ -[PSUIAddNewPlanController createAddOnGroupIfNeeded:]
+ -[PSUIAddNewPlanController createCarrierItemGroupIfNeeded:]
+ -[PSUIAddNewPlanController createPendingInstallGroupIfNeeded:]
+ -[PSUIAddNewPlanController createQRCodeGroupIfNeeded:]
+ -[PSUIAddNewPlanController createTransferablePlanGroupIfNeeded:]
+ -[PSUIAddNewPlanController dismiss]
+ -[PSUIAddNewPlanController getLogger]
+ -[PSUIAddNewPlanController init]
+ -[PSUIAddNewPlanController pendingInstallGroupSpecifier]
+ -[PSUIAddNewPlanController pendingInstallGroup]
+ -[PSUIAddNewPlanController setAddOnPlanGroup:]
+ -[PSUIAddNewPlanController setCancelButton:]
+ -[PSUIAddNewPlanController setCarrierItemGroup:]
+ -[PSUIAddNewPlanController setPendingInstallGroup:]
+ -[PSUIAddNewPlanController setQRCodeGroup:]
+ -[PSUIAddNewPlanController setTransferablePlanGroup:]
+ -[PSUIAddNewPlanController shouldShowPendingInstallPlan]
+ -[PSUIAddNewPlanController specifiers]
+ -[PSUIAddNewPlanController transferablePlanGroupSpecifier]
+ -[PSUIAddNewPlanController transferablePlanGroup]
+ -[PSUIAddNewPlanController viewDidLoad]
+ -[PSUIAddOnPlanGroup _addOnPlanOptionPressed:]
+ -[PSUIAddOnPlanGroup _addWiFiOffFooter]
+ -[PSUIAddOnPlanGroup _shouldShowWiFiOffFooter]
+ -[PSUIAddOnPlanGroup _turnOnWifiPressed:]
+ -[PSUIAddOnPlanGroup groupSpecifier]
+ -[PSUIAddOnPlanGroup initWithListController:groupSpecifier:planManager:ctPlanManager:showAddOnPlans:]
+ -[PSUIAddOnPlanGroup initWithListController:groupSpecifier:showAddOnPlans:]
+ -[PSUIAddOnPlanGroup setGroupSpecifier:]
+ -[PSUIAddOnPlanGroup specifiersForRemotePlans:]
+ -[PSUICarrierItemGroup carrierItemOptionPressed:]
+ -[PSUICarrierItemGroup initWithListController:groupSpecifier:planManager:ctPlanManager:showCarrierItems:]
+ -[PSUICarrierItemGroup initWithListController:groupSpecifier:showCarrierItems:]
+ -[PSUICarrierItemGroup isCellNetworkSearchAuthorized]
+ -[PSUICarrierItemGroup isFlowRunning]
+ -[PSUICarrierItemTableCell .cxx_destruct]
+ -[PSUICarrierItemTableCell _setTitle:]
+ -[PSUICarrierItemTableCell canBeChecked]
+ -[PSUICarrierItemTableCell canReload]
+ -[PSUICarrierItemTableCell initWithStyle:reuseIdentifier:]
+ -[PSUICarrierItemTableCell refreshCellContentsWithSpecifier:]
+ -[PSUICarrierItemTableCell setSpinner:]
+ -[PSUICarrierItemTableCell setTitleLabel:]
+ -[PSUICarrierItemTableCell spinner]
+ -[PSUICarrierItemTableCell titleLabel]
+ -[PSUICarrierListController getLogger]
+ -[PSUICarrierListController initWithOptions:showCarrierItemGroup:]
+ -[PSUICellularController QRCodeGroupSpecifier]
+ -[PSUICellularController QRCodeGroup]
+ -[PSUICellularController _createESIMCardDataAlert:]
+ -[PSUICellularController _shouldShowCarrierItemGroup]
+ -[PSUICellularController addOnPlanGroupSpecifier]
+ -[PSUICellularController createAddOnPlanGroupIfNeeded:showAddOnPlans:]
+ -[PSUICellularController createCarrierItemGroupIfNeeded:showCarrierItems:]
+ -[PSUICellularController createQRCodeGroupIfNeeded:]
+ -[PSUICellularController createTransferPlanGroupIfNeeded:]
+ -[PSUICellularController handleURL:withCompletion:]
+ -[PSUICellularController otherOptionsGroup]
+ -[PSUICellularController pendingInstallPlanGroup]
+ -[PSUICellularController setOtherOptionsGroup:]
+ -[PSUICellularController setPendingInstallPlanGroup:]
+ -[PSUICellularController setQRCodeGroup:]
+ -[PSUICellularController shouldShowPendingInstallPlan]
+ -[PSUICellularController transferPlanGroupSpecifier]
+ -[PSUICellularPlanManagerCache cachedPendingInstallPlans]
+ -[PSUICellularPlanManagerCache isBootstrapRecommended]
+ -[PSUICellularPlanManagerCache isCarrierItemBeingFetched]
+ -[PSUICellularPlanManagerCache pendingInstallPlanFetchInProgress]
+ -[PSUICellularPlanManagerCache pendingInstallPlans]
+ -[PSUICellularPlanManagerCache plansDidUpdate:]
+ -[PSUICellularPlanManagerCache setCachedPendingInstallPlans:]
+ -[PSUICellularPlanManagerCache setPendingInstallPlanFetchInProgress:]
+ -[PSUICoreTelephonyCapabilitiesCache fetchCanSetCapabilityWithCache:forContext:]
+ -[PSUICoreTelephonyCapabilitiesCache fetchCapabilityEnabledWithCache:forContext:]
+ -[PSUICoreTelephonyCapabilitiesCache getCapabilityInfoObject:forContext:cache:]
+ -[PSUICoreTelephonyCapabilitiesCache networkSlicingCategories:]
+ -[PSUICoreTelephonyCapabilitiesCache setCapabilityEnabledForContext:cache:enabled:info:]
+ -[PSUICoreTelephonyCapabilitiesCache setCapabilityInfoObject:forKey:forContext:cache:]
+ -[PSUICoreTelephonyCapabilitiesCache setNetworkSlicing:enabled:category:]
+ -[PSUICoreTelephonyCapabilitiesCache setNetworkSlicingCategories:forContext:]
+ -[PSUICoreTelephonyDataCache fetchPrivateNetworkCapabilities:]
+ -[PSUICoreTelephonyDataCache hideDataRoaming:]
+ -[PSUICoreTelephonyDataCache preferPrivateNetworkCellularOverWiFiDidChange]
+ -[PSUICoreTelephonyDataCache privateNetworkCapabilities]
+ -[PSUICoreTelephonyDataCache setPrivateNetworkCapabilities:]
+ -[PSUINetworkSlicingController _enableNetworkSlicing:categoryID:]
+ -[PSUINetworkSlicingController fCategories]
+ -[PSUINetworkSlicingController setFCategories:]
+ -[PSUIOtherOptionsGroup .cxx_destruct]
+ -[PSUIOtherOptionsGroup getLogger]
+ -[PSUIOtherOptionsGroup initWithListController:groupSpecifier:]
+ -[PSUIOtherOptionsGroup init]
+ -[PSUIOtherOptionsGroup listController]
+ -[PSUIOtherOptionsGroup otherOptionsPressed:]
+ -[PSUIOtherOptionsGroup setListController:]
+ -[PSUIOtherOptionsGroup specifiers]
+ -[PSUIPendingInstallPlanGroup .cxx_destruct]
+ -[PSUIPendingInstallPlanGroup coreTelephonyClient]
+ -[PSUIPendingInstallPlanGroup getLogger]
+ -[PSUIPendingInstallPlanGroup initWithListController:groupSpecifier:]
+ -[PSUIPendingInstallPlanGroup initWithListController:groupSpecifier:planManager:]
+ -[PSUIPendingInstallPlanGroup init]
+ -[PSUIPendingInstallPlanGroup listController]
+ -[PSUIPendingInstallPlanGroup pendingInstallPlanPressed:]
+ -[PSUIPendingInstallPlanGroup setCoreTelephonyClient:]
+ -[PSUIPendingInstallPlanGroup setListController:]
+ -[PSUIPendingInstallPlanGroup simSetupFlowCompleted:]
+ -[PSUIPendingInstallPlanGroup specifiersForPendingInstallPlans]
+ -[PSUIPendingInstallPlanGroup specifiers]
+ -[PSUIPlanPendingTransferListGroup .cxx_destruct]
+ -[PSUIPlanPendingTransferListGroup _isChinaRegionCellularDevice]
+ -[PSUIPlanPendingTransferListGroup _isInChina]
+ -[PSUIPlanPendingTransferListGroup _showSpinner:]
+ -[PSUIPlanPendingTransferListGroup getLogger]
+ -[PSUIPlanPendingTransferListGroup groupSpecifier]
+ -[PSUIPlanPendingTransferListGroup listController]
+ -[PSUIPlanPendingTransferListGroup setGroupSpecifier:]
+ -[PSUIPlanPendingTransferListGroup setListController:]
+ -[PSUIPlanPendingTransferListGroup setTransferPlanSpecifier:]
+ -[PSUIPlanPendingTransferListGroup simSetupFlowCompleted:]
+ -[PSUIPlanPendingTransferListGroup transferPlanSpecifier]
+ -[PSUIPlanPendingTransferListGroup transferablePlanPressed:]
+ -[PSUIQRCodeGroup .cxx_destruct]
+ -[PSUIQRCodeGroup flow]
+ -[PSUIQRCodeGroup getLogger]
+ -[PSUIQRCodeGroup groupSpecifier]
+ -[PSUIQRCodeGroup initWithListController:groupSpecifier:]
+ -[PSUIQRCodeGroup init]
+ -[PSUIQRCodeGroup listController]
+ -[PSUIQRCodeGroup scanQRCodePressed:]
+ -[PSUIQRCodeGroup setFlow:]
+ -[PSUIQRCodeGroup setGroupSpecifier:]
+ -[PSUIQRCodeGroup setListController:]
+ -[PSUIQRCodeGroup simSetupFlowCompleted:]
+ -[PSUIQRCodeGroup specifiers]
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table48
+ GCC_except_table65
+ _OBJC_CLASS_$_PSUIAddNewPlanController
+ _OBJC_CLASS_$_PSUICarrierItemTableCell
+ _OBJC_CLASS_$_PSUIOtherOptionsGroup
+ _OBJC_CLASS_$_PSUIPendingInstallPlanGroup
+ _OBJC_CLASS_$_PSUIQRCodeGroup
+ _OBJC_IVAR_$_PSUIAddOnPlanGroup._showAddOnPlans
+ _OBJC_IVAR_$_PSUICarrierItemGroup._showCarrierItems
+ _OBJC_IVAR_$_PSUICellularPlanManagerCache._cachedPendingInstallPlans
+ _OBJC_IVAR_$_PSUICellularPlanManagerCache._pendingInstallPlanFetchInProgress
+ _OBJC_IVAR_$_PSUICoreTelephonyDataCache._privateNetworkCapabilities
+ _OBJC_IVAR_$_PSUIOtherOptionsGroup._groupSpecifier
+ _OBJC_IVAR_$_PSUIOtherOptionsGroup._listController
+ _OBJC_IVAR_$_PSUIPendingInstallPlanGroup._carrierName
+ _OBJC_IVAR_$_PSUIPendingInstallPlanGroup._cellularPlanManager
+ _OBJC_IVAR_$_PSUIPendingInstallPlanGroup._coreTelephonyClient
+ _OBJC_IVAR_$_PSUIPendingInstallPlanGroup._flow
+ _OBJC_IVAR_$_PSUIPendingInstallPlanGroup._groupSpecifier
+ _OBJC_IVAR_$_PSUIPendingInstallPlanGroup._listController
+ _OBJC_IVAR_$_PSUIPlanPendingTransferListGroup._flow
+ _OBJC_IVAR_$_PSUIPlanPendingTransferListGroup._groupSpecifier
+ _OBJC_IVAR_$_PSUIPlanPendingTransferListGroup._listController
+ _OBJC_IVAR_$_PSUIPlanPendingTransferListGroup._originAccessoryView
+ _OBJC_IVAR_$_PSUIPlanPendingTransferListGroup._spinner
+ _OBJC_IVAR_$_PSUIPlanPendingTransferListGroup._transferPlanSpecifier
+ _OBJC_IVAR_$_PSUIQRCodeGroup._flow
+ _OBJC_IVAR_$_PSUIQRCodeGroup._groupSpecifier
+ _OBJC_IVAR_$_PSUIQRCodeGroup._listController
+ _OBJC_METACLASS_$_PSUIAddNewPlanController
+ _OBJC_METACLASS_$_PSUICarrierItemTableCell
+ _OBJC_METACLASS_$_PSUIOtherOptionsGroup
+ _OBJC_METACLASS_$_PSUIPendingInstallPlanGroup
+ _OBJC_METACLASS_$_PSUIQRCodeGroup
+ __OBJC_$_CLASS_METHODS_PSUICarrierItemTableCell
+ __OBJC_$_INSTANCE_METHODS_PSUIAddNewPlanController
+ __OBJC_$_INSTANCE_METHODS_PSUICarrierItemTableCell
+ __OBJC_$_INSTANCE_METHODS_PSUIOtherOptionsGroup
+ __OBJC_$_INSTANCE_METHODS_PSUIPendingInstallPlanGroup
+ __OBJC_$_INSTANCE_METHODS_PSUIQRCodeGroup
+ __OBJC_$_INSTANCE_VARIABLES_PSUIAddNewPlanController
+ __OBJC_$_INSTANCE_VARIABLES_PSUICarrierItemTableCell
+ __OBJC_$_INSTANCE_VARIABLES_PSUIOtherOptionsGroup
+ __OBJC_$_INSTANCE_VARIABLES_PSUIPendingInstallPlanGroup
+ __OBJC_$_INSTANCE_VARIABLES_PSUIPlanPendingTransferListGroup
+ __OBJC_$_INSTANCE_VARIABLES_PSUIQRCodeGroup
+ __OBJC_$_PROP_LIST_PSUIAddNewPlanController
+ __OBJC_$_PROP_LIST_PSUICarrierItemTableCell
+ __OBJC_$_PROP_LIST_PSUIOtherOptionsGroup
+ __OBJC_$_PROP_LIST_PSUIPendingInstallPlanGroup
+ __OBJC_$_PROP_LIST_PSUIQRCodeGroup
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CoreTelephonyClientCellularPlanManagementDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreTelephonyClientCellularPlanManagementDelegate
+ __OBJC_$_PROTOCOL_REFS_CoreTelephonyClientCellularPlanManagementDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PSUIOtherOptionsGroup
+ __OBJC_CLASS_PROTOCOLS_$_PSUIPendingInstallPlanGroup
+ __OBJC_CLASS_PROTOCOLS_$_PSUIQRCodeGroup
+ __OBJC_CLASS_RO_$_PSUIAddNewPlanController
+ __OBJC_CLASS_RO_$_PSUICarrierItemTableCell
+ __OBJC_CLASS_RO_$_PSUIOtherOptionsGroup
+ __OBJC_CLASS_RO_$_PSUIPendingInstallPlanGroup
+ __OBJC_CLASS_RO_$_PSUIQRCodeGroup
+ __OBJC_LABEL_PROTOCOL_$_CoreTelephonyClientCellularPlanManagementDelegate
+ __OBJC_METACLASS_RO_$_PSUIAddNewPlanController
+ __OBJC_METACLASS_RO_$_PSUICarrierItemTableCell
+ __OBJC_METACLASS_RO_$_PSUIOtherOptionsGroup
+ __OBJC_METACLASS_RO_$_PSUIPendingInstallPlanGroup
+ __OBJC_METACLASS_RO_$_PSUIQRCodeGroup
+ __OBJC_PROTOCOL_$_CoreTelephonyClientCellularPlanManagementDelegate
+ ___37-[PSUIQRCodeGroup scanQRCodePressed:]_block_invoke
+ ___41-[PSUIQRCodeGroup simSetupFlowCompleted:]_block_invoke
+ ___43-[PSUICarrierItemGroup carrierItemPressed:]_block_invoke.60
+ ___43-[PSUICellularPlanManagerCache remotePlans]_block_invoke.99
+ ___44-[PSUICellularPlanManagerCache carrierItems]_block_invoke.101
+ ___47-[PSUICellularPlanManagerCache plansDidUpdate:]_block_invoke
+ ___48-[PSUIAddNewPlanController cellularPlanChanged:]_block_invoke
+ ___49-[PSUIPlanPendingTransferListGroup _showSpinner:]_block_invoke
+ ___51-[PSUICellularController _createESIMCardDataAlert:]_block_invoke
+ ___51-[PSUICellularController handleURL:withCompletion:]_block_invoke
+ ___51-[PSUICellularController handleURL:withCompletion:]_block_invoke.81
+ ___51-[PSUICellularController handleURL:withCompletion:]_block_invoke_2
+ ___51-[PSUICellularPlanManagerCache pendingInstallPlans]_block_invoke
+ ___51-[PSUICellularPlanManagerCache pendingInstallPlans]_block_invoke.94
+ ___53-[PSUIPendingInstallPlanGroup simSetupFlowCompleted:]_block_invoke
+ ___57-[PSUIPendingInstallPlanGroup pendingInstallPlanPressed:]_block_invoke
+ ___58-[PSUIPlanPendingTransferListGroup simSetupFlowCompleted:]_block_invoke
+ ___60-[PSUIPlanPendingTransferListGroup transferablePlanPressed:]_block_invoke
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.315
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.316
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.321
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32s_e20_v24?0Q8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e48_v24?0"CTCellularPlanQRCodeAction"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40w_e39_v24?0"CTDisplayPlanList"8"NSError"16lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e26_v16?0"UIViewController"8lw48l8s32l8s40l8
+ ___block_literal_global.108
+ ___block_literal_global.125
+ ___block_literal_global.53
+ _kCTCapabilityCanSet
+ _kCTCapabilityStatus
+ _kCTNetworkSlicingCategories
+ _kCTNetworkSlicingCategoryID
+ _kCTNetworkSlicingCategoryName
+ _kCTNetworkSlicingCategoryState
+ _objc_msgSend$QRCodeGroup
+ _objc_msgSend$QRCodeGroupSpecifier
+ _objc_msgSend$_addWiFiOffFooter
+ _objc_msgSend$_createESIMCardDataAlert:
+ _objc_msgSend$_enableNetworkSlicing:categoryID:
+ _objc_msgSend$_isChinaRegionCellularDevice
+ _objc_msgSend$_isInChina
+ _objc_msgSend$_setTitle:
+ _objc_msgSend$_shouldShowCarrierItemGroup
+ _objc_msgSend$_shouldShowWiFiOffFooter
+ _objc_msgSend$acceptCapabilityforSlotID:status:canSet:info:
+ _objc_msgSend$addOnPlanGroupSpecifier
+ _objc_msgSend$bootstrapStatus
+ _objc_msgSend$cachedPendingInstallPlans
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$createAddOnGroupIfNeeded:
+ _objc_msgSend$createAddOnPlanGroupIfNeeded:showAddOnPlans:
+ _objc_msgSend$createCarrierItemGroupIfNeeded:showCarrierItems:
+ _objc_msgSend$createPendingInstallGroupIfNeeded:
+ _objc_msgSend$createQRCodeGroupIfNeeded:
+ _objc_msgSend$createTransferPlanGroupIfNeeded:
+ _objc_msgSend$createTransferablePlanGroupIfNeeded:
+ _objc_msgSend$fCategories
+ _objc_msgSend$fetchCanSetCapabilityWithCache:forContext:
+ _objc_msgSend$fetchCapabilityEnabledWithCache:forContext:
+ _objc_msgSend$fetchPrivateNetworkCapabilities:
+ _objc_msgSend$getActionForCardData:completionHandler:
+ _objc_msgSend$getBootstrapState:
+ _objc_msgSend$getCapabilityInfoObject:forContext:cache:
+ _objc_msgSend$getCapabilityInfoObject:forSlotID:
+ _objc_msgSend$getNetworkSlicingAppCategory:
+ _objc_msgSend$getPrivateNetworkCapabilitiesForContext:error:
+ _objc_msgSend$hideDataRoaming
+ _objc_msgSend$hideDataRoaming:
+ _objc_msgSend$init
+ _objc_msgSend$initWithListController:groupSpecifier:planManager:
+ _objc_msgSend$initWithListController:groupSpecifier:planManager:ctPlanManager:showAddOnPlans:
+ _objc_msgSend$initWithListController:groupSpecifier:planManager:ctPlanManager:showCarrierItems:
+ _objc_msgSend$initWithListController:groupSpecifier:showAddOnPlans:
+ _objc_msgSend$initWithListController:groupSpecifier:showCarrierItems:
+ _objc_msgSend$initWithOptions:showCarrierItemGroup:
+ _objc_msgSend$isBootstrapRecommended
+ _objc_msgSend$isCarrierItemBeingFetched
+ _objc_msgSend$isCellNetworkSearchAuthorized
+ _objc_msgSend$networkSlicingCategories:
+ _objc_msgSend$noDataConnectivityAvailable
+ _objc_msgSend$otherOptionsGroup
+ _objc_msgSend$pendingInstallGroup
+ _objc_msgSend$pendingInstallGroupSpecifier
+ _objc_msgSend$pendingInstallPlanGroup
+ _objc_msgSend$pendingInstallPlans
+ _objc_msgSend$performWithCompletionHandler:
+ _objc_msgSend$planPendingTransferGroup
+ _objc_msgSend$plansPendingInstallWithCompletion:
+ _objc_msgSend$privateNetworkCapabilities
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$setCachedPendingInstallPlans:
+ _objc_msgSend$setCapabilityEnabledForContext:cache:enabled:info:
+ _objc_msgSend$setCapabilityInfoObject:forKey:forContext:cache:
+ _objc_msgSend$setCapabilityInfoObject:forKey:forSlotID:
+ _objc_msgSend$setFCategories:
+ _objc_msgSend$setNetworkSlicing:enabled:category:
+ _objc_msgSend$setNetworkSlicingCategories:forContext:
+ _objc_msgSend$setOtherOptionsGroup:
+ _objc_msgSend$setPendingInstallGroup:
+ _objc_msgSend$setPendingInstallPlanFetchInProgress:
+ _objc_msgSend$setPendingInstallPlanGroup:
+ _objc_msgSend$setPlanPendingTransferGroup:
+ _objc_msgSend$setQRCodeGroup:
+ _objc_msgSend$setTransferablePlanGroup:
+ _objc_msgSend$shouldShowPendingInstallPlan
+ _objc_msgSend$specifiersForPendingInstallPlans
+ _objc_msgSend$specifiersForRemotePlans:
+ _objc_msgSend$startPendingPlanInstallationForPlan:carrierName:completionHandler:
+ _objc_msgSend$transferPlanGroupSpecifier
+ _objc_msgSend$transferPlanSpecifier
+ _objc_msgSend$transferablePlanGroup
+ _objc_msgSend$transferablePlanGroupSpecifier
- -[PSUIAddOnPlanGroup initWithListController:groupSpecifier:planManager:ctPlanManager:]
- -[PSUIAddOnPlanGroup specifiersForRemotePlans]
- -[PSUICarrierItemGroup initWithListController:groupSpecifier:planManager:ctPlanManager:]
- -[PSUICellularController createCarrierItemGroupIfNeeded:]
- -[PSUICoreTelephonyCapabilitiesCache fetchCanSetCapabilityWithCache:]
- -[PSUICoreTelephonyCapabilitiesCache fetchCapabilityEnabledWithCache:]
- -[PSUICoreTelephonyCapabilitiesCache isNetworkSlicingManagedForContext:]
- -[PSUICoreTelephonyCapabilitiesCache setCapabilityEnabledForContext:cache:enabled:]
- -[PSUICoreTelephonyCapabilitiesCache setNetworkSlicing:enabled:]
- -[PSUICoreTelephonyDataCache fetchIsPrivateNetworkSIM:]
- -[PSUICoreTelephonyDataCache isPrivateNetworkSIM]
- -[PSUICoreTelephonyDataCache setIsPrivateNetworkSIM:]
- -[PSUINetworkSlicingController _enableNetworkSlicing:]
- -[PSUINetworkSlicingController networkSlicingOn]
- -[PSUINetworkSlicingController setNetworkSlicingOn:]
- GCC_except_table27
- GCC_except_table28
- GCC_except_table32
- GCC_except_table52
- _OBJC_IVAR_$_PSUICoreTelephonyDataCache._isPrivateNetworkSIM
- _OBJC_IVAR_$_PSUINetworkSlicingController._capabilityCache
- _OBJC_IVAR_$_PSUINetworkSlicingController._networkSlicingOn
- ___43-[PSUICarrierItemGroup carrierItemPressed:]_block_invoke.49
- ___43-[PSUICellularPlanManagerCache remotePlans]_block_invoke.95
- ___44-[PSUICellularPlanManagerCache carrierItems]_block_invoke.97
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.264
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.265
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.271
- ___block_literal_global.47
- _objc_msgSend$_enableNetworkSlicing:
- _objc_msgSend$configureAddOnPlanTurnOnWifi:
- _objc_msgSend$fetchCanSetCapabilityWithCache:
- _objc_msgSend$fetchCapabilityEnabledWithCache:
- _objc_msgSend$fetchIsPrivateNetworkSIM:
- _objc_msgSend$getCapabilityInfo:forSlotID:
- _objc_msgSend$initWithListController:groupSpecifier:planManager:ctPlanManager:
- _objc_msgSend$isNetworkSlicingManagedForContext:
- _objc_msgSend$isPrivateNetworkSIM:error:
- _objc_msgSend$networkSlicingOn
- _objc_msgSend$setCapabilityEnabledForContext:cache:enabled:
- _objc_msgSend$setNetworkSlicing:enabled:
- _objc_msgSend$setNetworkSlicingOn:
- _objc_msgSend$specifiersForRemotePlans
CStrings:
+ "\x02\x13"
+ "\x02\x13\x1d"
+ "\x04\x11\x11"
+ "\v"
+ "\x15$"
+ "%s No carrier items available for ChinaRegionCellularDevice"
+ "%s: DONOTHING, not fetched"
+ "-[CTCapability setCapabilityInfoObject:forKey:forSlotID:]"
+ "-[PSUICellularController _shouldShowCarrierItemGroup]"
+ "-[PSUICellularPlanManagerCache pendingInstallPlans]"
+ "-[PSUICellularPlanManagerCache pendingInstallPlans]_block_invoke"
+ "-[PSUINetworkSlicingController _enableNetworkSlicing:categoryID:]"
+ "-[PSUIPendingInstallPlanGroup simSetupFlowCompleted:]"
+ "-[PSUIQRCodeGroup simSetupFlowCompleted:]"
+ "@\"PSUIOtherOptionsGroup\""
+ "@\"PSUIPendingInstallPlanGroup\""
+ "@\"PSUIQRCodeGroup\""
+ "@24@0:8B16B20"
+ "@32@0:8@16q24"
+ "@36@0:8@16@24B32"
+ "ADD_ON_PLAN"
+ "ADD_ON_PLAN_FOOTER_NEW"
+ "AddNewPlanController"
+ "CARRIER"
+ "CARRIER_ITEM"
+ "CARRIER_ITEM_FOOTER"
+ "CARRIER_ITEM_GROUP"
+ "CTDisplayPlanList: %@"
+ "Can set fetch for %@, Allowed: %@, Enabled: %@, %@"
+ "CarrierListController"
+ "Checking Private Network capabilities failed: %@"
+ "Clearing Private network SIM infos due to profile update"
+ "CoreTelephonyClientCellularPlanManagementDelegate"
+ "ESIM_ACTIVATION_DEVICE_NOT_SUPPORTED_MESSAGE"
+ "ESIM_ACTIVATION_FAILED_ACTION_MESSAGE"
+ "ESIM_ACTIVATION_FAILED_ACTION_TITLE"
+ "ESIM_ACTIVATION_FAILED_PARSE_MESSAGE"
+ "ESIM_ACTIVATION_POLICY_MISMATCH_MESSAGE"
+ "Emtpy eSIM QR code data"
+ "Executing can set capability fetch for %@"
+ "Failed getActionForCardData with error %@"
+ "Failed to fetch pending install items with error: %@"
+ "Failed to install pending plan"
+ "Fetch for capability for %@, Allowed: %@, Enabled: %@, %@"
+ "Invalid PSUIQRCodeGroup"
+ "Invalid specifier"
+ "Location Services is off"
+ "No add-on plan(s) is available"
+ "No carrier item(s) is available in this location"
+ "OTHER_OPTIONS"
+ "OTHER_OPTIONS_FOOTER"
+ "OTHER_OPTIONS_GROUP"
+ "OtherOptions"
+ "PENDING_INSTALL_FOOTER"
+ "PENDING_INSTALL_GROUP"
+ "PENDING_INSTALL_NAME_%@"
+ "PSUIAddNewPlanController"
+ "PSUICarrierItemTableCell"
+ "PSUIOtherOptionsGroup"
+ "PSUIPendingInstallPlanGroup"
+ "PSUIQRCodeGroup"
+ "Pending install group specifiers: %@"
+ "PendingInstall"
+ "PendingXferListGroup"
+ "Private Network Capabilities for context slot id [%@]: %@"
+ "QRCodeGroup"
+ "QRCodeGroupSpecifier"
+ "QR_CODE_GROUP"
+ "Slicing: %s category=%@ ->%@"
+ "Slicing: %s category=%@ STATE=%d"
+ "Slicing: %s context=%@, UDPATE=%@"
+ "Slicing: reload, context=%@"
+ "Slicing: reload, context=%@, categories:%@"
+ "Slicing: skipped"
+ "T@\"CTDisplayPlanList\",&,V_cachedPendingInstallPlans"
+ "T@\"NSArray\",&,N,V_fCategories"
+ "T@\"NSMutableDictionary\",&,V_capabilityFetched"
+ "T@\"NSMutableDictionary\",&,V_enabledFetched"
+ "T@\"NSMutableDictionary\",&,V_privateNetworkCapabilities"
+ "T@\"NSString\",?,R,C"
+ "T@\"PSSpecifier\",&,N,V_transferPlanSpecifier"
+ "T@\"PSUIOtherOptionsGroup\",&,N,V_otherOptionsGroup"
+ "T@\"PSUIPendingInstallPlanGroup\",&,N,V_pendingInstallGroup"
+ "T@\"PSUIPendingInstallPlanGroup\",&,N,V_pendingInstallPlanGroup"
+ "T@\"PSUIPlanPendingTransferListGroup\",&,N,V_transferablePlanGroup"
+ "T@\"PSUIQRCodeGroup\",&,N,V_QRCodeGroup"
+ "TB,V_pendingInstallPlanFetchInProgress"
+ "TRANSFER_PLAN"
+ "TRANSFER_PLAN_FOOTER"
+ "TRANSFER_PLAN_GROUP"
+ "TURN_ON_LOCATION_SERVICES_FAUX_CARD_SCANNER_FOOTER_NEW_UI"
+ "USE_QR_CODE"
+ "USE_QR_CODE_FOOTER"
+ "WiFi/Cellular is off while iCloud signed in"
+ "_QRCodeGroup"
+ "_QRCodeGroupSpecifier"
+ "_addOnPlanOptionPressed:"
+ "_addWiFiOffFooter"
+ "_cachedPendingInstallPlans"
+ "_carrierListFetchInProgress: %@"
+ "_createESIMCardDataAlert:"
+ "_enableNetworkSlicing:categoryID:"
+ "_fCategories"
+ "_isChinaRegionCellularDevice"
+ "_isInChina"
+ "_otherOptionsGroup"
+ "_pendingInstallGroup"
+ "_pendingInstallGroupSpecifier"
+ "_pendingInstallPlanFetchInProgress"
+ "_pendingInstallPlanGroup"
+ "_privateNetworkCapabilities"
+ "_setTitle:"
+ "_shouldShowCarrierItemGroup"
+ "_shouldShowWiFiOffFooter"
+ "_showAddOnPlanGroup"
+ "_showAddOnPlans"
+ "_showCarrierItemGroup"
+ "_showCarrierItems"
+ "_transferPlanSpecifier"
+ "_transferablePlanGroup"
+ "_transferablePlanGroupSpecifier"
+ "_turnOnWifiPressed:"
+ "acceptCapabilityforSlotID:status:canSet:info:"
+ "addOnPlanGroupSpecifier"
+ "bootstrapStatus"
+ "cachedPendingInstallPlans"
+ "capabilitiesChanged: %@, %@"
+ "carddata"
+ "carrier name empty"
+ "carrierItemOptionPressed:"
+ "caseInsensitiveCompare:"
+ "createAddOnGroupIfNeeded:"
+ "createAddOnPlanGroupIfNeeded:showAddOnPlans:"
+ "createCarrierItemGroupIfNeeded:showCarrierItems:"
+ "createPendingInstallGroupIfNeeded:"
+ "createQRCodeGroupIfNeeded:"
+ "createTransferPlanGroupIfNeeded:"
+ "createTransferablePlanGroupIfNeeded:"
+ "esim_qrcode_provisioning"
+ "fCategories"
+ "fetchCanSetCapabilityWithCache:forContext:"
+ "fetchCapabilityEnabledWithCache:forContext:"
+ "fetchPrivateNetworkCapabilities:"
+ "flow is still running"
+ "getActionForCardData callback: Success - %@"
+ "getActionForCardData:completionHandler:"
+ "getBootstrapState:"
+ "getCapabilityInfoObject:forContext:cache:"
+ "getCapabilityInfoObject:forSlotID:"
+ "getPrivateNetworkCapabilitiesForContext:error:"
+ "handleURL:withCompletion:"
+ "hideDataRoaming"
+ "hideDataRoaming:"
+ "iPadUIPolish"
+ "initWithListController:groupSpecifier:planManager:"
+ "initWithListController:groupSpecifier:planManager:ctPlanManager:showAddOnPlans:"
+ "initWithListController:groupSpecifier:planManager:ctPlanManager:showCarrierItems:"
+ "initWithListController:groupSpecifier:showAddOnPlans:"
+ "initWithListController:groupSpecifier:showCarrierItems:"
+ "initWithOptions:showCarrierItemGroup:"
+ "isBootstrapRecommended"
+ "isBootstrapRecommended failed:%@"
+ "isCarrierItemBeingFetched"
+ "isCellNetworkSearchAuthorized"
+ "launchSecureIntentUI:isLocalConvertFlow:completion:"
+ "launchWebsheet:completion:"
+ "networkSlicingCategories:"
+ "noDataConnectivityAvailable"
+ "otherOptionsGroup"
+ "otherOptionsPressed:"
+ "pendingInstallGroup"
+ "pendingInstallGroupSpecifier"
+ "pendingInstallPlanFetchInProgress"
+ "pendingInstallPlanGroup"
+ "pendingInstallPlanPressed:"
+ "pendingInstallPlans"
+ "performWithCompletionHandler:"
+ "plansDidUpdate:"
+ "plansPendingInstallWithCompletion:"
+ "preferPrivateNetworkCellularOverWiFiDidChange"
+ "privateNetworkCapabilities"
+ "proxSetupAuthEventUpdate:"
+ "replaceObjectAtIndex:withObject:"
+ "scanQRCodePressed:"
+ "setCachedPendingInstallPlans:"
+ "setCapabilityEnabledForContext:cache:enabled:info:"
+ "setCapabilityInfoObject:forKey:forContext:cache:"
+ "setCapabilityInfoObject:forKey:forSlotID:"
+ "setFCategories:"
+ "setNetworkSlicing:enabled:category:"
+ "setNetworkSlicingCategories:forContext:"
+ "setOtherOptionsGroup:"
+ "setPendingInstallGroup:"
+ "setPendingInstallPlanFetchInProgress:"
+ "setPendingInstallPlanGroup:"
+ "setPrivateNetworkCapabilities:"
+ "setQRCodeGroup:"
+ "setTransferPlanSpecifier:"
+ "setTransferablePlanGroup:"
+ "shouldShowPendingInstallPlan"
+ "specifiersForPendingInstallPlans"
+ "specifiersForRemotePlans:"
+ "startPendingPlanInstallationForPlan:carrierName:completionHandler:"
+ "transferEventUpdate:"
+ "transferPlanGroupSpecifier"
+ "transferPlanSpecifier"
+ "transferablePlanGroup"
+ "transferablePlanGroupSpecifier"
+ "transferablePlanPressed:"
+ "updateSourceProxCardState:"
+ "v24@0:8@\"CTDisplayPlanList\"16"
+ "v24@?0@\"CTCellularPlanQRCodeAction\"8@\"NSError\"16"
+ "v24@?0@\"CTDisplayPlanList\"8@\"NSError\"16"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B>24"
+ "v36@0:8@\"NSData\"16B24@?<v@?B>28"
+ "v36@0:8@16B24@?28"
+ "v40@0:8q16B24B28@32"
+ "v44@0:8@16@24B32@36"
- "\x02\x13\x1a"
- "\x15#"
- "%s _enableNetworkSlicing %d subscriptionContext=%@"
- "%s enterpriseSlicing=%d"
- "%s subscriptionContext=%@"
- "%s subscriptionContext=%@, networkSliceingOn=%d"
- "-[PSUINetworkSlicingController _enableNetworkSlicing:]"
- "-[PSUINetworkSlicingController specifiers]"
- "COMMUNICATION_APP"
- "Can set fetch for %@ succeeded: %@, %{public}@"
- "Checking Private Network SIM failed: %@"
- "Checking Private Network SIM: %@"
- "ENTERPRISE_SLICING_FOOTER"
- "Executing can set capability fetch"
- "Fetch for capability enabled %@ succeeded: %@"
- "MANAGED_APP"
- "T@\"NSMutableDictionary\",&,V_isPrivateNetworkSIM"
- "TB,N,V_networkSlicingOn"
- "TB,V_capabilityFetched"
- "TB,V_enabledFetched"
- "Updating: %@"
- "_enableNetworkSlicing:"
- "_isPrivateNetworkSIM"
- "_networkSlicingOn"
- "fetchCanSetCapabilityWithCache:"
- "fetchCapabilityEnabledWithCache:"
- "fetchIsPrivateNetworkSIM:"
- "initWithListController:groupSpecifier:planManager:ctPlanManager:"
- "invalid carrier name"
- "isNetworkSlicingManagedForContext:"
- "isPrivateNetworkSIM: %@"
- "isPrivateNetworkSIM:error:"
- "kCTCapabilityNetworkSlicingManaged"
- "networkSlicingOn"
- "setCapabilityEnabledForContext:cache:enabled:"
- "setIsPrivateNetworkSIM:"
- "setNetworkSlicing:enabled:"
- "setNetworkSlicingOn:"
- "specifiersForRemotePlans"

```
