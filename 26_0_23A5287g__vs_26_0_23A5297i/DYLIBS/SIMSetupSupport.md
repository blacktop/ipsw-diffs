## SIMSetupSupport

> `/System/Library/PrivateFrameworks/SIMSetupSupport.framework/SIMSetupSupport`

```diff

-858.2.0.0.0
-  __TEXT.__text: 0xaa7e0
+862.0.0.0.0
+  __TEXT.__text: 0xab9d4
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x97cc
+  __TEXT.__objc_methlist: 0x9954
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x1bdc
-  __TEXT.__cstring: 0xf07f
-  __TEXT.__oslogstring: 0x61f4
+  __TEXT.__gcc_except_tab: 0x1bf8
+  __TEXT.__cstring: 0xf37a
+  __TEXT.__oslogstring: 0x620a
   __TEXT.__dlopen_cstrs: 0x2be
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x2410
-  __TEXT.__objc_classname: 0x14d1
-  __TEXT.__objc_methname: 0x150ed
-  __TEXT.__objc_methtype: 0x334a
-  __TEXT.__objc_stubs: 0xd940
-  __DATA_CONST.__got: 0xa28
-  __DATA_CONST.__const: 0x1d00
-  __DATA_CONST.__objc_classlist: 0x458
+  __TEXT.__unwind_info: 0x2430
+  __TEXT.__objc_classname: 0x14fd
+  __TEXT.__objc_methname: 0x15504
+  __TEXT.__objc_methtype: 0x350d
+  __TEXT.__objc_stubs: 0xda40
+  __DATA_CONST.__got: 0xa40
+  __DATA_CONST.__const: 0x1d10
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d48
+  __DATA_CONST.__objc_selrefs: 0x4df0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x428
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0x6ee0
-  __AUTH_CONST.__objc_const: 0x3ade8
+  __AUTH_CONST.__const: 0x880
+  __AUTH_CONST.__cfstring: 0x70c0
+  __AUTH_CONST.__objc_const: 0x3b388
   __AUTH_CONST.__objc_intobj: 0x4e0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x2b20
-  __DATA.__objc_ivar: 0xdd8
-  __DATA.__data: 0xb50
+  __AUTH.__objc_data: 0x2b70
+  __DATA.__objc_ivar: 0xdf8
+  __DATA.__data: 0xbb0
   __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF183810-9B65-382C-823D-9FE376B4240A
-  Functions: 3681
-  Symbols:   13419
-  CStrings:  7032
+  UUID: AFCF5CF9-FCA5-3B7D-A5DE-B57DF9B089C4
+  Functions: 3712
+  Symbols:   13519
+  CStrings:  7112
 
Symbols:
+ +[TSFlowHelper showBluetoothOffAlertForCrossPlatformTransfer:withCloseHandler:]
+ -[BluetoothChecker .cxx_destruct]
+ -[BluetoothChecker centralManagerDidUpdateState:]
+ -[BluetoothChecker isBluetoothOff:]
+ -[CTDisplayPlan(SimSetup) isRegulatoryRestrictedForCurrentLocationPlan]
+ -[SSInstallPlanInformation isSIMTypeSelectionShown]
+ -[SSInstallPlanInformation maybeUpdateTimeoutStatus]
+ -[SSInstallPlanInformation setIsSIMTypeSelectionShown:]
+ -[SSInstallPlanInformation setUseGMVNOAsTravelSIM:]
+ -[SSInstallPlanInformation useGMVNOAsTravelSIM]
+ -[TSCellularPlanActivatingFlow initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:isLocalConvert:]
+ -[TSCellularPlanActivatingFlow isLocalConvert]
+ -[TSCellularPlanActivatingFlow setIsLocalConvert:]
+ -[TSCellularPlanLabelsViewController tableView:heightForFooterInSection:]
+ -[TSCrossPlatformSourceTransferFlow _startBackgroundTask]
+ -[TSCrossPlatformSourceTransferFlow _stopBackgroundTask]
+ -[TSCrossPlatformSourceTransferFlow backgroundTask]
+ -[TSCrossPlatformSourceTransferFlow dealloc]
+ -[TSCrossPlatformSourceTransferFlow setBackgroundTask:]
+ -[TSDeviceInfoViewController initWithOptions:].cold.2
+ -[TSEnableTableViewController _updateButtonStatus]
+ -[TSEnableTableViewController continueButton]
+ -[TSEnableTableViewController setContinueButton:]
+ -[TSEnableTableViewController setSkipButton:]
+ -[TSEnableTableViewController skipButton]
+ -[TSTravelModeIntroViewController initWithOptions:extractionSource:reduceEducation:]
+ -[TSTravelSimTypeSelectionViewController prepare:].cold.1
+ -[TSWebsheetViewController currentTitle]
+ -[TSWebsheetViewController setCurrentTitle:]
+ GCC_except_table124
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table153
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table200
+ GCC_except_table226
+ _CBCentralManagerOptionShowPowerAlertKey
+ _OBJC_CLASS_$_BluetoothChecker
+ _OBJC_CLASS_$_CBCentralManager
+ _OBJC_IVAR_$_BluetoothChecker._completion
+ _OBJC_IVAR_$_BluetoothChecker._manager
+ _OBJC_IVAR_$_SSInstallPlanInformation._isSIMTypeSelectionShown
+ _OBJC_IVAR_$_SSInstallPlanInformation._useGMVNOAsTravelSIM
+ _OBJC_IVAR_$_TSCellularPlanActivatingFlow._isLocalConvert
+ _OBJC_IVAR_$_TSCellularPlanIntroViewController.bluetoothChecker
+ _OBJC_IVAR_$_TSCrossPlatformSourceTransferFlow._backgroundTask
+ _OBJC_IVAR_$_TSDeviceInfoViewController._isSharingIdentitySupported
+ _OBJC_IVAR_$_TSTravelModeIntroViewController._reduceEducation
+ _OBJC_METACLASS_$_BluetoothChecker
+ _TSTravelActionTappedLearnMoreReducedEducation
+ _TSTravelReduceEducation
+ __OBJC_$_INSTANCE_METHODS_BluetoothChecker
+ __OBJC_$_INSTANCE_VARIABLES_BluetoothChecker
+ __OBJC_$_PROP_LIST_BluetoothChecker
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBCentralManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBCentralManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBCentralManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CBCentralManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BluetoothChecker
+ __OBJC_CLASS_RO_$_BluetoothChecker
+ __OBJC_LABEL_PROTOCOL_$_CBCentralManagerDelegate
+ __OBJC_METACLASS_RO_$_BluetoothChecker
+ __OBJC_PROTOCOL_$_CBCentralManagerDelegate
+ ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.497
+ ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke.81
+ ___53-[TSCrossPlatformSourceAuthFlow transferEventUpdate:]_block_invoke
+ ___53-[TSCrossPlatformTargetAuthFlow transferEventUpdate:]_block_invoke_3
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.218
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.220
+ ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.219
+ ___57-[TSCrossPlatformSourceTransferFlow _startBackgroundTask]_block_invoke
+ ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.71
+ ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.71.cold.1
+ ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.166
+ ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.203
+ ___71-[TSCellularPlanIntroViewController tableView:didSelectRowAtIndexPath:]_block_invoke
+ ___71-[TSCellularPlanIntroViewController tableView:didSelectRowAtIndexPath:]_block_invoke_2
+ ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.543
+ ___79+[TSFlowHelper showBluetoothOffAlertForCrossPlatformTransfer:withCloseHandler:]_block_invoke
+ ___79+[TSFlowHelper showBluetoothOffAlertForCrossPlatformTransfer:withCloseHandler:]_block_invoke_2
+ ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.606
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.555
+ ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.555.cold.1
+ ___block_literal_global.123
+ ___block_literal_global.222
+ ___block_literal_global.294
+ ___block_literal_global.310
+ ___block_literal_global.406
+ ___block_literal_global.496
+ ___block_literal_global.499
+ ___block_literal_global.55
+ ___block_literal_global.557
+ ___block_literal_global.672
+ ___block_literal_global.702
+ ___block_literal_global.762
+ ___block_literal_global.83
+ ___block_literal_global.84
+ ___block_literal_global.88
+ _objc_msgSend$_updateButtonStatus
+ _objc_msgSend$initWithDelegate:queue:options:
+ _objc_msgSend$initWithOptions:extractionSource:reduceEducation:
+ _objc_msgSend$initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:isLocalConvert:
+ _objc_msgSend$isBluetoothOff:
+ _objc_msgSend$isRegulatoryRestrictedForCurrentLocationPlan
+ _objc_msgSend$isSIMTypeSelectionShown
+ _objc_msgSend$maybeUpdateTimeoutStatus
+ _objc_msgSend$setIsSIMTypeSelectionShown:
+ _objc_msgSend$setUseGMVNOAsTravelSIM:
+ _objc_msgSend$showBluetoothOffAlertForCrossPlatformTransfer:withCloseHandler:
+ _objc_msgSend$state
+ _objc_msgSend$useGMVNOAsTravelSIM
- -[SSInstallPlanInformation maybeUpdateTimeoutStatus:]
- -[TSCellularPlanActivatingFlow initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:]
- -[TSCellularPlanIntroViewController getCellTextAt:]
- -[TSCellularPlanIntroViewController tableView:heightForRowAtIndexPath:]
- -[TSEnableTableViewController _refreshContinueButton]
- -[TSTravelModeIntroViewController initWithOptions:extractionSource:]
- GCC_except_table120
- GCC_except_table126
- GCC_except_table131
- GCC_except_table139
- GCC_except_table140
- GCC_except_table151
- GCC_except_table185
- GCC_except_table188
- GCC_except_table196
- GCC_except_table224
- _OBJC_IVAR_$_TSTravelModeIntroViewController._roamingSwitchEnabled
- ___115-[TSCellularPlanActivatingFlow(CoreTelephonyClientCellularPlanManagementDelegate) handleWaitingOnWifiStatusUpdate:]_block_invoke.492
- ___52-[TSCrossPlatformSourceAuthFlow _findEligiblePlans:]_block_invoke.79
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.212
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke.214
- ___53-[TSTransferListViewController _startPendingInstall:]_block_invoke_2.213
- ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.68
- ___59-[TSCrossPlatformSourceAuthFlow onCodeDetected:completion:]_block_invoke.68.cold.1
- ___61-[TSTransferListViewController _installMultipleSelectedPlans]_block_invoke.160
- ___64-[TSTransferListViewController _startPlanTransfer:withDeviceID:]_block_invoke.197
- ___74-[TSCellularPlanActivatingFlow(TSSIMSetupDelegate) simSetupFlowCompleted:]_block_invoke.538
- ___82-[TSCellularPlanActivatingFlow(InteractiveUI) _displayIntermediateViewController:]_block_invoke.601
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.550
- ___82-[TSCellularPlanActivatingFlow(TSSIMSetupFlowDelegate) viewControllerDidComplete:]_block_invoke.550.cold.1
- ___block_literal_global.119
- ___block_literal_global.122
- ___block_literal_global.216
- ___block_literal_global.285
- ___block_literal_global.301
- ___block_literal_global.401
- ___block_literal_global.491
- ___block_literal_global.494
- ___block_literal_global.552
- ___block_literal_global.660
- ___block_literal_global.690
- ___block_literal_global.750
- ___block_literal_global.82
- _objc_msgSend$_refreshContinueButton
- _objc_msgSend$host
- _objc_msgSend$initWithOptions:extractionSource:
- _objc_msgSend$initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:
- _objc_msgSend$maybeUpdateTimeoutStatus:
CStrings:
+ "-[SSInstallPlanInformation maybeUpdateTimeoutStatus]"
+ "-[TSCrossPlatformSourceTransferFlow _startBackgroundTask]_block_invoke"
+ "-[TSTravelSimTypeSelectionViewController prepare:]"
+ "@\"BluetoothChecker\""
+ "@\"CBCentralManager\""
+ "@40@0:8Q16@24Q32"
+ "@88@0:8B16q20@28Q36@44B52@56B64@68@76B84"
+ "AR"
+ "BluetoothChecker"
+ "CBCentralManagerDelegate"
+ "CROSSTRANSFER_CONN_BLUETOOTH_OFF"
+ "CROSSTRANSFER_CONN_BLUETOOTH_OFF_CLOSE_ACTION"
+ "CROSSTRANSFER_CONN_BLUETOOTH_OFF_MSG"
+ "CROSSTRANSFER_CONN_BLUETOOTH_OFF_SETTINGS_ACTION"
+ "PSIM_IN_STORE_SIGNUP_DETAIL"
+ "SINGLE_INELIGIBLE_ESIM_TRANSFER_CAPABILITY_UNREGULATORY_RESTRICTED"
+ "T@\"NSString\",&,V_currentTitle"
+ "T@\"SSOBLinkTrayButton\",&,V_skipButton"
+ "TB,V_isLocalConvert"
+ "TB,V_isSIMTypeSelectionShown"
+ "TB,V_useGMVNOAsTravelSIM"
+ "TRANSFER_INELIGIBLE_FOR_NOW_PLAN"
+ "TRANSFER_INELIGIBLE_FOR_NOW_PLAN_DETAIL_%@"
+ "TRANSFER_PLAN_ITEM_DETAIL_REGULATORY_RESTRICTED_FOR_CURRENT_LOCATION"
+ "TRANSFER_PLAN_ITEM_DETAIL_UNAVAILABLE"
+ "TRAVEL_MODE_REDUCED_EDU_PRE_DEPARTURE_BODY_%@"
+ "TRAVEL_MODE_REDUCED_EDU_PRE_DEPARTURE_BODY_ABROAD"
+ "[E]ICCID is empty @%s"
+ "_completion"
+ "_isLocalConvert"
+ "_isSIMTypeSelectionShown"
+ "_isSharingIdentitySupported"
+ "_manager"
+ "_reduceEducation"
+ "_updateButtonStatus"
+ "_useGMVNOAsTravelSIM"
+ "a"
+ "bluetoothChecker"
+ "centralManager:connectionEventDidOccur:forPeripheral:"
+ "centralManager:didConnectPeripheral:"
+ "centralManager:didDisconnectPeripheral:error:"
+ "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
+ "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
+ "centralManager:didFailToConnectPeripheral:error:"
+ "centralManager:didUpdateANCSAuthorizationForPeripheral:"
+ "centralManager:willRestoreState:"
+ "centralManagerDidUpdateState:"
+ "currentTitle"
+ "initWithDelegate:queue:options:"
+ "initWithOptions:extractionSource:reduceEducation:"
+ "initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:isLocalConvert:"
+ "isBluetoothOff:"
+ "isLocalConvert"
+ "isRegulatoryRestrictedForCurrentLocationPlan"
+ "isSIMTypeSelectionShown"
+ "maybeUpdateTimeoutStatus"
+ "reduceEducation"
+ "setCurrentTitle:"
+ "setIsLocalConvert:"
+ "setIsSIMTypeSelectionShown:"
+ "setUseGMVNOAsTravelSIM:"
+ "settings-navigation://com.apple.Settings.Bluetooth"
+ "showBluetoothOffAlertForCrossPlatformTransfer:withCloseHandler:"
+ "tapped_learn_more_reduced_education"
+ "useGMVNOAsTravelSIM"
+ "v24@0:8@\"CBCentralManager\"16"
+ "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
+ "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
+ "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
+ "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
+ "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
+ "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
+ "v52@0:8@16@24d32B40@44"
+ "\xd4\xd1"
- "-[SSInstallPlanInformation maybeUpdateTimeoutStatus:]"
- "@84@0:8B16q20@28Q36@44B52@56B64@68@76"
- "Ab"
- "_refreshContinueButton"
- "_roamingSwitchEnabled"
- "host"
- "initWithOptions:extractionSource:"
- "initWithSkipActivatingPane:timerType:transferBackPlan:setupType:carrierName:maybeShowConfirmationCodePane:plan:isForCrossPlatformTransfer:session:sourceOsVersion:"
- "maybeUpdateTimeoutStatus:"
- "\xc4\xd1"

```
