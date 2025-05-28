## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-609.0.0.0.0
-  __TEXT.__text: 0x6cd94
+668.0.0.0.0
+  __TEXT.__text: 0x70e4c
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x5834
+  __TEXT.__objc_methlist: 0x5c8c
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x8de2
-  __TEXT.__oslogstring: 0x3dd9
-  __TEXT.__gcc_except_tab: 0xd50
+  __TEXT.__cstring: 0x936b
+  __TEXT.__oslogstring: 0x3f71
+  __TEXT.__gcc_except_tab: 0xd98
   __TEXT.__dlopen_cstrs: 0x1b6
-  __TEXT.__unwind_info: 0x1810
-  __TEXT.__objc_classname: 0xdcf
-  __TEXT.__objc_methname: 0xf805
-  __TEXT.__objc_methtype: 0x2da9
-  __TEXT.__objc_stubs: 0xa380
+  __TEXT.__unwind_info: 0x1908
+  __TEXT.__objc_classname: 0xe80
+  __TEXT.__objc_methname: 0xfd51
+  __TEXT.__objc_methtype: 0x2df6
+  __TEXT.__objc_stubs: 0xa600
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x12a0
-  __DATA_CONST.__objc_classlist: 0x2e8
+  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x216d8
-  __DATA_CONST.__objc_selrefs: 0x34e0
+  __DATA_CONST.__objc_const: 0x247e8
+  __DATA_CONST.__objc_selrefs: 0x35e0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x658
-  __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x3e60
-  __AUTH_CONST.__const: 0x560
-  __AUTH_CONST.__objc_const: 0x20f0
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__objc_intobj: 0x3d8
+  __DATA_CONST.__objc_classrefs: 0x688
+  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_arraydata: 0x50
+  __AUTH_CONST.__cfstring: 0x4220
+  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__objc_const: 0x2258
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH.__objc_data: 0x1cc0
-  __DATA.__objc_ivar: 0x900
+  __AUTH.__objc_data: 0x1e50
+  __DATA.__objc_ivar: 0x958
   __DATA.__data: 0xa90
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2474
-  Symbols:   9042
-  CStrings:  4358
+  Functions: 2576
+  Symbols:   9408
+  CStrings:  4472
 
Symbols:
+ +[TSFlowHelper getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:]
+ +[TSFlowHelper hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:]
+ +[TSFlowHelper sortIndexesInDescending:]
+ -[CTDisplayPlan(SimSetup) isAccountMemberTransferablePlan]
+ -[TSCarrierItemListViewController .cxx_destruct]
+ -[TSCarrierItemListViewController _cancelButtonTapped]
+ -[TSCarrierItemListViewController _fetchCarrierListWithCompletion:]
+ -[TSCarrierItemListViewController carrierItems]
+ -[TSCarrierItemListViewController client]
+ -[TSCarrierItemListViewController delegate]
+ -[TSCarrierItemListViewController footer]
+ -[TSCarrierItemListViewController getCellTextAt:]
+ -[TSCarrierItemListViewController init]
+ -[TSCarrierItemListViewController numberOfSectionsInTableView:]
+ -[TSCarrierItemListViewController prepare:]
+ -[TSCarrierItemListViewController selectedCarrierItem]
+ -[TSCarrierItemListViewController setCarrierItems:]
+ -[TSCarrierItemListViewController setClient:]
+ -[TSCarrierItemListViewController setDelegate:]
+ -[TSCarrierItemListViewController setFooter:]
+ -[TSCarrierItemListViewController setSelectedCarrierItem:]
+ -[TSCarrierItemListViewController tableView:cellForRowAtIndexPath:]
+ -[TSCarrierItemListViewController tableView:didSelectRowAtIndexPath:]
+ -[TSCarrierItemListViewController tableView:didSelectRowAtIndexPath:].cold.1
+ -[TSCarrierItemListViewController tableView:heightForRowAtIndexPath:]
+ -[TSCarrierItemListViewController tableView:numberOfRowsInSection:]
+ -[TSCarrierItemListViewController tableView:viewForFooterInSection:]
+ -[TSCarrierItemListViewController updateFooterView]
+ -[TSCarrierItemListViewController viewDidLayoutSubviews]
+ -[TSCarrierItemListViewController viewDidLoad]
+ -[TSCarrierItemListViewController viewWillAppear:]
+ -[TSCarrierSignupFlow initWithPlan:queriableFirstViewController:hostViewController:]
+ -[TSCarrierSignupFlow initWithPlan:queriableFirstViewController:hostViewController:].cold.1
+ -[TSCarrierSignupFlow initWithPlan:queriableFirstViewController:hostViewController:].cold.2
+ -[TSCellularPlanScanViewController startScanning]
+ -[TSSIMSetupFlow isBootstrapAssertionRequired]
+ -[TSSubFlowViewController setUsingFirstViewControllerParadigm:]
+ -[TSSubFlowViewController usingFirstViewControllerParadigm]
+ -[TSTravelEducationExistingPlanViewController .cxx_destruct]
+ -[TSTravelEducationExistingPlanViewController _cancelButtonTapped]
+ -[TSTravelEducationExistingPlanViewController _doneButtonTapped]
+ -[TSTravelEducationExistingPlanViewController client]
+ -[TSTravelEducationExistingPlanViewController delegate]
+ -[TSTravelEducationExistingPlanViewController init]
+ -[TSTravelEducationExistingPlanViewController setClient:]
+ -[TSTravelEducationExistingPlanViewController setDelegate:]
+ -[TSTravelEducationExistingPlanViewController viewDidLoad]
+ -[TSTravelEducationFlow .cxx_destruct]
+ -[TSTravelEducationFlow firstViewController:]
+ -[TSTravelEducationFlow firstViewController]
+ -[TSTravelEducationFlow firstViewController].cold.1
+ -[TSTravelEducationFlow initWithOptions:]
+ -[TSTravelEducationFlow isBootstrapAssertionRequired]
+ -[TSTravelEducationFlow nextViewControllerFrom:]
+ -[TSTravelEducationFlow options]
+ -[TSTravelEducationFlow returnHome]
+ -[TSTravelEducationFlow setOptions:]
+ -[TSTravelEducationFlow setReturnHome:]
+ -[TSTravelEducationIntroViewController .cxx_destruct]
+ -[TSTravelEducationIntroViewController _cancelButtonTapped]
+ -[TSTravelEducationIntroViewController client]
+ -[TSTravelEducationIntroViewController delegate]
+ -[TSTravelEducationIntroViewController getCellTextAt:]
+ -[TSTravelEducationIntroViewController getDisplayOptions]
+ -[TSTravelEducationIntroViewController initWithOptions:]
+ -[TSTravelEducationIntroViewController isExistingPlanTapped]
+ -[TSTravelEducationIntroViewController isPurchaseLocalPlanTapped]
+ -[TSTravelEducationIntroViewController isRoamingTapped]
+ -[TSTravelEducationIntroViewController numberOfSectionsInTableView:]
+ -[TSTravelEducationIntroViewController options]
+ -[TSTravelEducationIntroViewController setClient:]
+ -[TSTravelEducationIntroViewController setDelegate:]
+ -[TSTravelEducationIntroViewController setIsExistingPlanTapped:]
+ -[TSTravelEducationIntroViewController setIsPurchaseLocalPlanTapped:]
+ -[TSTravelEducationIntroViewController setIsRoamingTapped:]
+ -[TSTravelEducationIntroViewController setOptions:]
+ -[TSTravelEducationIntroViewController setText:]
+ -[TSTravelEducationIntroViewController tableView:cellForRowAtIndexPath:]
+ -[TSTravelEducationIntroViewController tableView:didSelectRowAtIndexPath:]
+ -[TSTravelEducationIntroViewController tableView:heightForRowAtIndexPath:]
+ -[TSTravelEducationIntroViewController tableView:numberOfRowsInSection:]
+ -[TSTravelEducationIntroViewController text]
+ -[TSTravelEducationIntroViewController viewDidLayoutSubviews]
+ -[TSTravelEducationIntroViewController viewDidLoad]
+ -[TSTravelEducationIntroViewController viewWillAppear:]
+ -[TSTravelEducationRoamingViewController .cxx_destruct]
+ -[TSTravelEducationRoamingViewController _cancelButtonTapped]
+ -[TSTravelEducationRoamingViewController _doneButtonTapped]
+ -[TSTravelEducationRoamingViewController _openRoamingSettings]
+ -[TSTravelEducationRoamingViewController client]
+ -[TSTravelEducationRoamingViewController delegate]
+ -[TSTravelEducationRoamingViewController init]
+ -[TSTravelEducationRoamingViewController setClient:]
+ -[TSTravelEducationRoamingViewController setDelegate:]
+ -[TSTravelEducationRoamingViewController viewDidLoad]
+ _OBJC_CLASS_$_TSCarrierItemListViewController
+ _OBJC_CLASS_$_TSTravelEducationExistingPlanViewController
+ _OBJC_CLASS_$_TSTravelEducationFlow
+ _OBJC_CLASS_$_TSTravelEducationIntroViewController
+ _OBJC_CLASS_$_TSTravelEducationRoamingViewController
+ _OBJC_CLASS_$_UITableViewHeaderFooterView
+ _OBJC_IVAR_$_TSCarrierItemListViewController._carrierItems
+ _OBJC_IVAR_$_TSCarrierItemListViewController._client
+ _OBJC_IVAR_$_TSCarrierItemListViewController._delegate
+ _OBJC_IVAR_$_TSCarrierItemListViewController._footer
+ _OBJC_IVAR_$_TSCarrierItemListViewController._selectedCarrierItem
+ _OBJC_IVAR_$_TSCarrierSignupFlow._hostViewController
+ _OBJC_IVAR_$_TSCarrierSignupFlow._isQueriableFirstViewController
+ _OBJC_IVAR_$_TSCarrierSignupFlow._signUpViewController
+ _OBJC_IVAR_$_TSSubFlowViewController._usingFirstViewControllerParadigm
+ _OBJC_IVAR_$_TSTravelEducationExistingPlanViewController._client
+ _OBJC_IVAR_$_TSTravelEducationExistingPlanViewController._delegate
+ _OBJC_IVAR_$_TSTravelEducationFlow._options
+ _OBJC_IVAR_$_TSTravelEducationFlow._returnHome
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._client
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._delegate
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._isExistingPlanTapped
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._isPurchaseLocalPlanTapped
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._isRoamingTapped
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._options
+ _OBJC_IVAR_$_TSTravelEducationIntroViewController._text
+ _OBJC_IVAR_$_TSTravelEducationRoamingViewController._client
+ _OBJC_IVAR_$_TSTravelEducationRoamingViewController._delegate
+ _OBJC_METACLASS_$_TSCarrierItemListViewController
+ _OBJC_METACLASS_$_TSTravelEducationExistingPlanViewController
+ _OBJC_METACLASS_$_TSTravelEducationFlow
+ _OBJC_METACLASS_$_TSTravelEducationIntroViewController
+ _OBJC_METACLASS_$_TSTravelEducationRoamingViewController
+ _TSHasLocalPlanKey
+ _TSHostViewControllerKey
+ _TSUserInfoTravelOptionsKey
+ __OBJC_$_INSTANCE_METHODS_TSCarrierItemListViewController
+ __OBJC_$_INSTANCE_METHODS_TSTravelEducationExistingPlanViewController
+ __OBJC_$_INSTANCE_METHODS_TSTravelEducationFlow
+ __OBJC_$_INSTANCE_METHODS_TSTravelEducationIntroViewController
+ __OBJC_$_INSTANCE_METHODS_TSTravelEducationRoamingViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSCarrierItemListViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelEducationExistingPlanViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelEducationFlow
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelEducationIntroViewController
+ __OBJC_$_INSTANCE_VARIABLES_TSTravelEducationRoamingViewController
+ __OBJC_$_PROP_LIST_TSCarrierItemListViewController
+ __OBJC_$_PROP_LIST_TSTravelEducationExistingPlanViewController
+ __OBJC_$_PROP_LIST_TSTravelEducationFlow
+ __OBJC_$_PROP_LIST_TSTravelEducationIntroViewController
+ __OBJC_$_PROP_LIST_TSTravelEducationRoamingViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSCarrierItemListViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelEducationExistingPlanViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelEducationFlow
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelEducationIntroViewController
+ __OBJC_CLASS_PROTOCOLS_$_TSTravelEducationRoamingViewController
+ __OBJC_CLASS_RO_$_TSCarrierItemListViewController
+ __OBJC_CLASS_RO_$_TSTravelEducationExistingPlanViewController
+ __OBJC_CLASS_RO_$_TSTravelEducationFlow
+ __OBJC_CLASS_RO_$_TSTravelEducationIntroViewController
+ __OBJC_CLASS_RO_$_TSTravelEducationRoamingViewController
+ __OBJC_METACLASS_RO_$_TSCarrierItemListViewController
+ __OBJC_METACLASS_RO_$_TSTravelEducationExistingPlanViewController
+ __OBJC_METACLASS_RO_$_TSTravelEducationFlow
+ __OBJC_METACLASS_RO_$_TSTravelEducationIntroViewController
+ __OBJC_METACLASS_RO_$_TSTravelEducationRoamingViewController
+ ___35-[TSSubFlowViewController prepare:]_block_invoke_2
+ ___40+[TSFlowHelper sortIndexesInDescending:]_block_invoke
+ ___43-[TSCarrierItemListViewController prepare:]_block_invoke
+ ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.153
+ ___67-[TSCarrierItemListViewController _fetchCarrierListWithCompletion:]_block_invoke
+ ___67-[TSCarrierItemListViewController _fetchCarrierListWithCompletion:]_block_invoke_2
+ ___67-[TSCarrierItemListViewController _fetchCarrierListWithCompletion:]_block_invoke_2.cold.1
+ ___67-[TSCarrierItemListViewController _fetchCarrierListWithCompletion:]_block_invoke_3
+ ___67-[TSCarrierItemListViewController _fetchCarrierListWithCompletion:]_block_invoke_4
+ ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.279
+ ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.283
+ ___block_descriptor_32_e11_q24?0816l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e20_v24?0Q8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e23_v16?0"UIAlertAction"8lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSArray"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
+ ___block_literal_global.254
+ ___block_literal_global.285
+ ___block_literal_global.292
+ ___block_literal_global.431
+ ___block_literal_global.484
+ _objc_msgSend$_fetchCarrierListWithCompletion:
+ _objc_msgSend$_openRoamingSettings
+ _objc_msgSend$carrierItemsShouldUpdate:completion:
+ _objc_msgSend$getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:
+ _objc_msgSend$getDisplayOptions
+ _objc_msgSend$getSupportedFlowTypes:
+ _objc_msgSend$hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithOptions:
+ _objc_msgSend$initWithPlan:queriableFirstViewController:hostViewController:
+ _objc_msgSend$isAccountMemberTransferablePlan
+ _objc_msgSend$isBootstrapAssertionRequired
+ _objc_msgSend$isExistingPlanTapped
+ _objc_msgSend$isPurchaseLocalPlanTapped
+ _objc_msgSend$isRoamingTapped
+ _objc_msgSend$primaryAccount
+ _objc_msgSend$selectedCarrierItem
+ _objc_msgSend$sendTravelBuddyCAEvent:carrierName:error:
+ _objc_msgSend$showFirstViewControllerWithHostController:completion:
+ _objc_msgSend$sortIndexesInDescending:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$startScanning
- +[TSFlowHelper hasTransferablePlanWithSameCarrier:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:]
- -[TSSIMSetupFlow getRootFlow]
- -[TSSIMSetupFlow getRootFlow].cold.1
- ___62-[TSSIMSetupFlow navigateToNextPaneFrom:navigationController:]_block_invoke.143
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.276
- ___82-[TSSinglePlanTransferViewController _maybeDisplayConsent:phoneNumber:completion:]_block_invoke.280
- ___block_descriptor_48_e8_32s40w_e23_v16?0"UIAlertAction"8ls32l8w40l8
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.251
- ___block_literal_global.282
- ___block_literal_global.289
- ___block_literal_global.422
- ___block_literal_global.475
- _objc_msgSend$getRootFlow
- _objc_msgSend$hasTransferablePlanWithSameCarrier:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:
CStrings:
+ "\x06\x11"
+ "+[TSFlowHelper getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:]"
+ "+[TSFlowHelper hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:]"
+ "-[TSActivationFlowWithSimSetupFlow _filterCarrierSetupItems:]"
+ "-[TSCarrierItemListViewController _fetchCarrierListWithCompletion:]_block_invoke_2"
+ "-[TSCarrierItemListViewController tableView:didSelectRowAtIndexPath:]"
+ "-[TSCarrierSignupFlow initWithPlan:queriableFirstViewController:hostViewController:]"
+ "-[TSSIMSetupFlow appBackgrounded]"
+ "-[TSSIMSetupFlow appForegrounded]"
+ "-[TSTransferCloudFlowModel filterCarrierSetupItems:]"
+ "-[TSTravelEducationFlow firstViewController:]"
+ "-[TSTravelEducationFlow firstViewController]"
+ "-[TSTravelEducationRoamingViewController _openRoamingSettings]"
+ "@\"CTCellularPlanCarrierItem\""
+ "@\"UITableViewHeaderFooterView\""
+ "@36@0:8@16B24@28"
+ "Account member has a transferrable plan with a SODA tether @%s"
+ "Account member plan %@ will be removed from transfer list @%s"
+ "Core Analytics"
+ "Existing Plan View Controller_Cancel"
+ "Existing Plan View Controller_Done"
+ "HasLocalPlan"
+ "HostViewController"
+ "Intro View Controller_Cancel"
+ "NOT_CONNECTED_TO_WLAN"
+ "PRIVACY_FOOTER"
+ "Roaming View Controller_Cancel"
+ "Roaming View Controller_Done"
+ "SINGLE_ESIM_CROSSPLATFORM_TRANSFER_DETAIL_NO_NUMBER_%@"
+ "STAY_CONNECTED_TRAVEL_BODY"
+ "STAY_CONNECTED_TRAVEL_TITLE"
+ "Skip querying SODA plans on iPad! @%s"
+ "T@\"CTCellularPlanCarrierItem\",&,N,V_selectedCarrierItem"
+ "T@\"NSArray\",&,N,V_carrierItems"
+ "T@\"NSDictionary\",&,V_options"
+ "T@\"NSDictionary\",&,V_text"
+ "T@\"UITableViewHeaderFooterView\",&,V_footer"
+ "TB,V_isExistingPlanTapped"
+ "TB,V_isPurchaseLocalPlanTapped"
+ "TB,V_isRoamingTapped"
+ "TB,V_returnHome"
+ "TB,V_usingFirstViewControllerParadigm"
+ "TRAVEL_DATA_ROAMING_LIST_ITEM"
+ "TRAVEL_EXISTING_PLAN_BODY"
+ "TRAVEL_EXISTING_PLAN_LIST_ITEM"
+ "TRAVEL_EXISTING_PLAN_TITLE"
+ "TRAVEL_OPEN_ROAMING_URL"
+ "TRAVEL_PURCHASE_PLAN_BODY"
+ "TRAVEL_PURCHASE_PLAN_LIST_ITEM"
+ "TRAVEL_PURCHASE_PLAN_TITLE"
+ "TRAVEL_ROAMING_BODY"
+ "TRAVEL_ROAMING_TITLE"
+ "TSCarrierItemListViewController"
+ "TSTravelEducationExistingPlanViewController"
+ "TSTravelEducationFlow"
+ "TSTravelEducationIntroViewController"
+ "TSTravelEducationRoamingViewController"
+ "TURN_ON_WLAN_TO_PURCHASE_PLAN"
+ "TravelOptionsKey"
+ "[E]CarrierPlanItemFlow is unsupprted @%s"
+ "[E]invalid row selection @%s"
+ "[I] app in background, deassert bootstrap @%s"
+ "[I] app in foreground, assert bootstrap @%s"
+ "_carrierItems"
+ "_fetchCarrierListWithCompletion:"
+ "_footer"
+ "_hostViewController"
+ "_isExistingPlanTapped"
+ "_isPurchaseLocalPlanTapped"
+ "_isQueriableFirstViewController"
+ "_isRoamingTapped"
+ "_openRoamingSettings"
+ "_options"
+ "_returnHome"
+ "_selectedCarrierItem"
+ "_signUpViewController"
+ "_text"
+ "_usingFirstViewControllerParadigm"
+ "carrier item at %@: %@ @%s"
+ "carrierItems"
+ "carrierItemsShouldUpdate:completion:"
+ "flow %@ presents ViewController by itself @%s"
+ "footer"
+ "getAccountMemberTransferablePlanWithSameCarrierName:transferablePlans:"
+ "getDisplayOptions"
+ "getSupportedFlowTypes:"
+ "hasTransferablePlanWithSameCarrierName:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:"
+ "initWithArray:"
+ "initWithPlan:queriableFirstViewController:hostViewController:"
+ "isAccountMemberTransferablePlan"
+ "isBootstrapAssertionRequired"
+ "isExistingPlanTapped"
+ "isPurchaseLocalPlanTapped"
+ "isRoamingTapped"
+ "launching data roaming settings failed with error: %s, isOpened:%d\n @%s"
+ "options"
+ "options: %@ @%s"
+ "primaryAccount"
+ "purchase local plan"
+ "purchase local plan_Cancel"
+ "q24@?0@8@16"
+ "returnHome"
+ "selectedCarrierItem"
+ "sendTravelBuddyCAEvent:carrierName:error:"
+ "setCarrierItems:"
+ "setFooter:"
+ "setIsExistingPlanTapped:"
+ "setIsPurchaseLocalPlanTapped:"
+ "setIsRoamingTapped:"
+ "setOptions:"
+ "setReturnHome:"
+ "setSelectedCarrierItem:"
+ "setUsingFirstViewControllerParadigm:"
+ "showLocalPlanOption"
+ "showPurchaseOption"
+ "showRoamingOption"
+ "sortIndexesInDescending:"
+ "sortUsingComparator:"
+ "startScanning"
+ "usingFirstViewControllerParadigm"
- "+[TSFlowHelper hasTransferablePlanWithSameCarrier:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:]"
- "-[TSSIMSetupFlow getRootFlow]"
- "Device is on WiFi and skip querying SODA plans! @%s"
- "[Db] Root flow : %@ @%s"
- "getRootFlow"
- "hasTransferablePlanWithSameCarrier:transferablePlans:inBuddy:matchingSODACarrierWebsheetTransferPlanIndex:"

```
