## AccessibilitySettings

> `/System/Library/PreferenceBundles/AccessibilitySettings.bundle/AccessibilitySettings`

```diff

-1726.2.3.0.0
-  __TEXT.__text: 0x142ddc
-  __TEXT.__auth_stubs: 0x3620
-  __TEXT.__objc_stubs: 0x20ea0
-  __TEXT.__objc_methlist: 0x1100c
+1726.2.16.0.0
+  __TEXT.__text: 0x143b78
+  __TEXT.__auth_stubs: 0x3610
+  __TEXT.__objc_stubs: 0x210c0
+  __TEXT.__objc_methlist: 0x110fc
   __TEXT.__const: 0xfa4
-  __TEXT.__gcc_except_tab: 0x2a4c
-  __TEXT.__objc_methname: 0x2e92d
-  __TEXT.__cstring: 0x14c98
-  __TEXT.__oslogstring: 0x2b7a
-  __TEXT.__objc_classname: 0x3dc8
-  __TEXT.__objc_methtype: 0x5b64
+  __TEXT.__gcc_except_tab: 0x2adc
+  __TEXT.__objc_methname: 0x2eb5f
+  __TEXT.__cstring: 0x14edd
+  __TEXT.__oslogstring: 0x2c9b
+  __TEXT.__objc_classname: 0x3de4
+  __TEXT.__objc_methtype: 0x5b7a
   __TEXT.__dlopen_cstrs: 0x186
   __TEXT.__ustring: 0x2e
   __TEXT.__constg_swiftt: 0x668

   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift5_proto: 0x64
   __TEXT.__swift5_types: 0x64
-  __TEXT.__unwind_info: 0x4a74
-  __DATA_CONST.__auth_got: 0x1b20
-  __DATA_CONST.__got: 0x1330
+  __TEXT.__unwind_info: 0x4adc
+  __DATA_CONST.__auth_got: 0x1b18
+  __DATA_CONST.__got: 0x1348
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x48a0
-  __DATA_CONST.__cfstring: 0x17200
-  __DATA_CONST.__objc_classlist: 0xce8
+  __DATA_CONST.__const: 0x4910
+  __DATA_CONST.__cfstring: 0x17600
+  __DATA_CONST.__objc_classlist: 0xcf0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x1578
+  __DATA_CONST.__objc_intobj: 0x15c0
   __DATA_CONST.__objc_arraydata: 0x11c0
   __DATA_CONST.__objc_arrayobj: 0x708
   __DATA_CONST.__objc_dictobj: 0x870
   __DATA_CONST.__objc_doubleobj: 0x1b0
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA.__objc_const: 0x1e580
-  __DATA.__objc_selrefs: 0xacc0
-  __DATA.__objc_classrefs: 0x1538
-  __DATA.__objc_superrefs: 0xa38
+  __DATA.__objc_const: 0x1e628
+  __DATA.__objc_selrefs: 0xad58
+  __DATA.__objc_classrefs: 0x1548
+  __DATA.__objc_superrefs: 0xa40
   __DATA.__objc_ivar: 0xce0
-  __DATA.__objc_data: 0x82c8
+  __DATA.__objc_data: 0x8318
   __DATA.__data: 0x259a
   __DATA.__bss: 0xf55
   __DATA.__common: 0x38

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7163
-  Symbols:   17650
-  CStrings:  11745
+  Functions: 7188
+  Symbols:   17705
+  CStrings:  11804
 
Symbols:
+ -[ASTBluetoothDevicesController axDeviceControllerType]
+ -[AXBluetoothDevicesController .cxx_destruct]
+ -[AXBluetoothDevicesController _addDevice:]
+ -[AXBluetoothDevicesController _brailleConfigMatch:withConfig:]
+ -[AXBluetoothDevicesController _cleanupPairing]
+ -[AXBluetoothDevicesController _isBluetoothPowerFooterShowing]
+ -[AXBluetoothDevicesController _peripheralDidCompletePairing:]
+ -[AXBluetoothDevicesController _pinRequestHandler:]
+ -[AXBluetoothDevicesController _removeDevice:]
+ -[AXBluetoothDevicesController _setupCentralScanning:]
+ -[AXBluetoothDevicesController _showBluetoothPowerFooter:]
+ -[AXBluetoothDevicesController _showScanningUI:]
+ -[AXBluetoothDevicesController _sspConfirmationHandler:]
+ -[AXBluetoothDevicesController _sspNumericComparisonHandler:]
+ -[AXBluetoothDevicesController _sspPasskeyDisplayHandler:]
+ -[AXBluetoothDevicesController _startConnectable]
+ -[AXBluetoothDevicesController _startDiscoverable]
+ -[AXBluetoothDevicesController _startScanning]
+ -[AXBluetoothDevicesController _stopConnectable]
+ -[AXBluetoothDevicesController _stopDiscoverable]
+ -[AXBluetoothDevicesController _stopScanning]
+ -[AXBluetoothDevicesController _updateDevicePosition:]
+ -[AXBluetoothDevicesController _updateDevicePosition:].cold.1
+ -[AXBluetoothDevicesController alertSheetDismissed:]
+ -[AXBluetoothDevicesController allowedServices]
+ -[AXBluetoothDevicesController applicationDidBecomeActive:]
+ -[AXBluetoothDevicesController applicationWillResignActive:]
+ -[AXBluetoothDevicesController applicationWillTerminate:]
+ -[AXBluetoothDevicesController authenticationRequestHandler:]
+ -[AXBluetoothDevicesController authorizedServices]
+ -[AXBluetoothDevicesController axDeviceControllerType]
+ -[AXBluetoothDevicesController bluetoothIsBusy]
+ -[AXBluetoothDevicesController bluetoothPowerAlertMessage]
+ -[AXBluetoothDevicesController bluetoothPoweredOffFooter]
+ -[AXBluetoothDevicesController centralManager:didDiscoverPeripheral:advertisementData:RSSI:]
+ -[AXBluetoothDevicesController centralManager:didFailToConnectPeripheral:error:]
+ -[AXBluetoothDevicesController centralManager:didFailToConnectPeripheral:error:].cold.1
+ -[AXBluetoothDevicesController centralManager:didUpdatePeripheralConnectionState:]
+ -[AXBluetoothDevicesController centralManagerDidUpdateState:]
+ -[AXBluetoothDevicesController centralManager]
+ -[AXBluetoothDevicesController currentSpecifier]
+ -[AXBluetoothDevicesController dealloc]
+ -[AXBluetoothDevicesController detailSpecifiersForDevice:withTarget:]
+ -[AXBluetoothDevicesController deviceConnected:]
+ -[AXBluetoothDevicesController deviceConnectedHandler:]
+ -[AXBluetoothDevicesController deviceDisconnectedHandler:]
+ -[AXBluetoothDevicesController deviceDiscoveredHandler:]
+ -[AXBluetoothDevicesController devicePairedHandler:]
+ -[AXBluetoothDevicesController deviceRemovedHandler:]
+ -[AXBluetoothDevicesController deviceUnpairedHandler:]
+ -[AXBluetoothDevicesController deviceUpdatedHandler:]
+ -[AXBluetoothDevicesController devicesGroupName]
+ -[AXBluetoothDevicesController getDeviceForPeripheral:]
+ -[AXBluetoothDevicesController handleReloadSpecifiers]
+ -[AXBluetoothDevicesController init]
+ -[AXBluetoothDevicesController mainSpecifiersGroup]
+ -[AXBluetoothDevicesController pairedDeviceSpecifiers]
+ -[AXBluetoothDevicesController pairingAgent:peerDidCompletePairing:]
+ -[AXBluetoothDevicesController pairingAgent:peerDidFailToCompletePairing:error:]
+ -[AXBluetoothDevicesController pairingAgent:peerDidUnpair:]
+ -[AXBluetoothDevicesController peripheralConnectionTimeout:]
+ -[AXBluetoothDevicesController peripheralDidUpdateName:]
+ -[AXBluetoothDevicesController peripheralMatchesUnadvertisedService:]
+ -[AXBluetoothDevicesController postDevicesSpecifiersGroup]
+ -[AXBluetoothDevicesController powerAlertCancelled]
+ -[AXBluetoothDevicesController powerChangedHandler:]
+ -[AXBluetoothDevicesController reloadSpecifiers]
+ -[AXBluetoothDevicesController scanningEnabled]
+ -[AXBluetoothDevicesController setAuthorizedServices:]
+ -[AXBluetoothDevicesController setBluetoothIsBusy:]
+ -[AXBluetoothDevicesController setCentralManager:]
+ -[AXBluetoothDevicesController setMainSpecifiersGroup:]
+ -[AXBluetoothDevicesController setScanningEnabled:]
+ -[AXBluetoothDevicesController shouldAddBTLEDevice:]
+ -[AXBluetoothDevicesController shouldAddClassicDevice:]
+ -[AXBluetoothDevicesController shouldReloadSpecifiersOnResume]
+ -[AXBluetoothDevicesController showBluetoothPowerAlert:]
+ -[AXBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]
+ -[AXBluetoothDevicesController specifierForDevice:]
+ -[AXBluetoothDevicesController specifierImmediatelyPrecedingDevices]
+ -[AXBluetoothDevicesController specifiers]
+ -[AXBluetoothDevicesController tableView:accessoryButtonTappedForRowWithIndexPath:]
+ -[AXBluetoothDevicesController tableView:cellForRowAtIndexPath:]
+ -[AXBluetoothDevicesController tableView:didSelectRowAtIndexPath:]
+ -[AXBluetoothDevicesController updatePairedDevices]
+ -[AXBluetoothDevicesController viewDidAppear:]
+ -[AXBluetoothDevicesController willBecomeActive]
+ -[AXBluetoothDevicesController willResignActive]
+ -[AXBluetoothDevicesController window]
+ -[AXLargeTextExplanationView categoryName]
+ -[AXLargeTextExplanationView setCategoryName:]
+ -[ClarityOnboardingController _clearOnboarding]
+ -[ClarityOnboardingController applicationWillTerminate:]
+ -[ClarityUIAdminPasscodeSetupController viewWillAppear:]
+ -[ClarityUIAppSelectionTableViewDataSource commitChangesToSelectedApplications]
+ -[ClarityUIController _setSilentModeToggleEnabled:specifier:]
+ -[ClarityUIController _silentModeToggleEnabled:]
+ -[HoverTextController largerTextEnabled:]
+ -[SCATAlertCoordinator showSwichAlreadyInUseAlert:]
+ -[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:]
+ -[SCATBluetoothDevicesController axDeviceControllerType]
+ -[SCATController firstLaunchScanningMode:]
+ -[SCATExternalSwitchSourceController _showSwitchAlreadyInUse]
+ -[SCATFirstLaunchScanningModeController init]
+ -[SCATFirstLaunchScanningModeController specifiers]
+ -[SCATFirstLaunchScanningModeController tableView:cellForRowAtIndexPath:]
+ -[SCATFirstLaunchScanningModeController tableView:didSelectRowAtIndexPath:]
+ -[UIViewController(ClarityUI) resetAllSettings]
+ -[VoiceOverBrailleController _coreBluetoothReady:]
+ -[VoiceOverBrailleController axDeviceControllerType]
+ -[VoiceOverBrailleController loadSettings]
+ -[VoiceOverController _coreBluetoothReady:]
+ -[VoiceOverController cachedBrailleDisplayIsPaired:]
+ GCC_except_table80
+ GCC_except_table82
+ OBJC_IVAR_$_AXBluetoothDevicesController._alert
+ OBJC_IVAR_$_AXBluetoothDevicesController._authorizedServices
+ OBJC_IVAR_$_AXBluetoothDevicesController._bluetoothInitialized
+ OBJC_IVAR_$_AXBluetoothDevicesController._bluetoothIsBusy
+ OBJC_IVAR_$_AXBluetoothDevicesController._centralManager
+ OBJC_IVAR_$_AXBluetoothDevicesController._currentDeviceSpecifier
+ OBJC_IVAR_$_AXBluetoothDevicesController._deviceSpecifiersGroup
+ OBJC_IVAR_$_AXBluetoothDevicesController._devicesDict
+ OBJC_IVAR_$_AXBluetoothDevicesController._mainSpecifiersGroup
+ OBJC_IVAR_$_AXBluetoothDevicesController._pairingPINDict
+ OBJC_IVAR_$_AXBluetoothDevicesController._power
+ OBJC_IVAR_$_AXBluetoothDevicesController._powerAlert
+ OBJC_IVAR_$_AXBluetoothDevicesController._scanningEnabled
+ OBJC_IVAR_$_AXBluetoothDevicesController._sspAlert
+ OBJC_IVAR_$_AXBluetoothDevicesController._togglingPower
+ OBJC_IVAR_$_AXLargeTextExplanationView._categoryName
+ _NSFileProtectionKey
+ _NSFileProtectionNone
+ _OBJC_CLASS_$_AXBluetoothDevicesController
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_SCATFirstLaunchScanningModeController
+ _OBJC_METACLASS_$_AXBluetoothDevicesController
+ _OBJC_METACLASS_$_SCATFirstLaunchScanningModeController
+ _UIContentSizeCategoryUnspecified
+ _VOSBluetoothCoreBluetoothManagerReadyNotification
+ __104-[AXVoiceOverImageDescriptionsController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.344
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.675
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.675.cold.1
+ __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.682
+ __53-[SCATController setSwitchScanningEnabled:specifier:]_block_invoke.618
+ __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke.317
+ __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke_2.319
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.267
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.279
+ __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.279.cold.1
+ __AXSPrefersHorizontalTextLayoutApp
+ __AXSPrefersHorizontalTextLayoutGlobal
+ __AXSSetPrefersHorizontalTextLayoutApp
+ __OBJC_$_INSTANCE_METHODS_AXBluetoothDevicesController
+ __OBJC_$_INSTANCE_METHODS_SCATFirstLaunchScanningModeController
+ __OBJC_$_INSTANCE_VARIABLES_AXBluetoothDevicesController
+ __OBJC_$_PROP_LIST_AXBluetoothDevicesController
+ __OBJC_CLASS_PROTOCOLS_$_AXBluetoothDevicesController
+ __OBJC_CLASS_RO_$_AXBluetoothDevicesController
+ __OBJC_CLASS_RO_$_SCATFirstLaunchScanningModeController
+ __OBJC_METACLASS_RO_$_AXBluetoothDevicesController
+ __OBJC_METACLASS_RO_$_SCATFirstLaunchScanningModeController
+ ___22-[SCATController init]_block_invoke_11
+ ___27-[VoiceOverController init]_block_invoke_10
+ ___45-[SCATFirstLaunchScanningModeController init]_block_invoke
+ ___51-[AXBluetoothDevicesController updatePairedDevices]_block_invoke
+ ___51-[SCATAlertCoordinator showSwichAlreadyInUseAlert:]_block_invoke
+ ___51-[SCATAlertCoordinator showSwichAlreadyInUseAlert:]_block_invoke_2
+ ___52-[VoiceOverBrailleController pairedDeviceSpecifiers]_block_invoke
+ ___52-[VoiceOverBrailleController pairedDeviceSpecifiers]_block_invoke_2
+ ___52-[VoiceOverController cachedBrailleDisplayIsPaired:]_block_invoke
+ ___56-[AXBluetoothDevicesController showBluetoothPowerAlert:]_block_invoke
+ ___56-[AXBluetoothDevicesController showBluetoothPowerAlert:]_block_invoke_2
+ ___61-[SCATExternalSwitchSourceController _showSwitchAlreadyInUse]_block_invoke
+ ___61-[SCATExternalSwitchSourceController _showSwitchAlreadyInUse]_block_invoke_2
+ ___64-[ClarityUIThingsToKnowOnboardingController initWithCompletion:]_block_invoke
+ ___70-[SCATExternalSwitchSourceController switchRegistrar:didUpdateSwitch:]_block_invoke_3
+ ___93-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:]_block_invoke
+ ___93-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:]_block_invoke_2
+ ___93-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:]_block_invoke_3
+ ___93-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:]_block_invoke_4
+ ___93-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:]_block_invoke_5
+ ___99-[AXBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke
+ ___99-[AXBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke_2
+ ___99-[AXBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke_3
+ ___99-[AXBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke_4
+ ___block_descriptor_40_e8_32s_e28_B16?0"VOSBluetoothDevice"8ls32l8
+ ___block_descriptor_48_e8_32bs40w_e23_v16?0"UIAlertAction"8ls32l8w40l8
+ ___block_descriptor_64_e8_32s40bs48bs56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64w_e23_v16?0"UIAlertAction"8ls32l8s40l8w64l8s48l8s56l8
+ __block_literal_global.270
+ __block_literal_global.282
+ __block_literal_global.286
+ __block_literal_global.314
+ __block_literal_global.336
+ __block_literal_global.340
+ __block_literal_global.359
+ __block_literal_global.361
+ __block_literal_global.368
+ __block_literal_global.370
+ __block_literal_global.374
+ __block_literal_global.383
+ __block_literal_global.393
+ __block_literal_global.395
+ __block_literal_global.405
+ __block_literal_global.407
+ __block_literal_global.431
+ __block_literal_global.436
+ __block_literal_global.441
+ __block_literal_global.458
+ __block_literal_global.460
+ __block_literal_global.479
+ __block_literal_global.481
+ __block_literal_global.485
+ __block_literal_global.678
+ _objc_msgSend$_clearOnboarding
+ _objc_msgSend$_learnMoreButtonTapped:
+ _objc_msgSend$_showSwitchAlreadyInUse
+ _objc_msgSend$addBulletedListItemWithTitle:description:symbolName:tintColor:linkButton:
+ _objc_msgSend$axDeviceControllerType
+ _objc_msgSend$cachedBrailleDisplayIsPaired:
+ _objc_msgSend$categoryName
+ _objc_msgSend$commitChangesToSelectedApplications
+ _objc_msgSend$configuration
+ _objc_msgSend$getDeviceForPeripheral:
+ _objc_msgSend$isPairedDeviceBrailleDisplay:
+ _objc_msgSend$loadSettings
+ _objc_msgSend$pairedBTLEDevices
+ _objc_msgSend$readPreferredContentSizeCategoryName
+ _objc_msgSend$resetAllSettings
+ _objc_msgSend$setCategoryName:
+ _objc_msgSend$setContentInsets:
+ _objc_msgSend$setSilentModeToggleEnabled:
+ _objc_msgSend$setSwitchControlFirstLaunchScanningMode:
+ _objc_msgSend$showSwichAlreadyInUseAlert:
+ _objc_msgSend$showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:
+ _objc_msgSend$silentModeToggleEnabled
+ _objc_msgSend$specifierForDevice:
+ _objc_msgSend$switchControlFirstLaunchScanningMode
+ _objc_msgSend$switchControlLocStringForFirstLaunchScanningMode:
- -[SCATAlertCoordinator showSwichAlreadyInUseAlert]
- -[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:]
- -[VoiceOverBluetoothDevicesController .cxx_destruct]
- -[VoiceOverBluetoothDevicesController _addDevice:]
- -[VoiceOverBluetoothDevicesController _brailleConfigMatch:withConfig:]
- -[VoiceOverBluetoothDevicesController _cleanupPairing]
- -[VoiceOverBluetoothDevicesController _getDeviceForPeripheral:]
- -[VoiceOverBluetoothDevicesController _isBluetoothPowerFooterShowing]
- -[VoiceOverBluetoothDevicesController _peripheralDidCompletePairing:]
- -[VoiceOverBluetoothDevicesController _pinRequestHandler:]
- -[VoiceOverBluetoothDevicesController _removeDevice:]
- -[VoiceOverBluetoothDevicesController _setupCentralScanning:]
- -[VoiceOverBluetoothDevicesController _showBluetoothPowerFooter:]
- -[VoiceOverBluetoothDevicesController _showScanningUI:]
- -[VoiceOverBluetoothDevicesController _specifierForDevice:]
- -[VoiceOverBluetoothDevicesController _sspConfirmationHandler:]
- -[VoiceOverBluetoothDevicesController _sspNumericComparisonHandler:]
- -[VoiceOverBluetoothDevicesController _sspPasskeyDisplayHandler:]
- -[VoiceOverBluetoothDevicesController _startConnectable]
- -[VoiceOverBluetoothDevicesController _startDiscoverable]
- -[VoiceOverBluetoothDevicesController _startScanning]
- -[VoiceOverBluetoothDevicesController _stopConnectable]
- -[VoiceOverBluetoothDevicesController _stopDiscoverable]
- -[VoiceOverBluetoothDevicesController _stopScanning]
- -[VoiceOverBluetoothDevicesController _updateDevicePosition:]
- -[VoiceOverBluetoothDevicesController alertSheetDismissed:]
- -[VoiceOverBluetoothDevicesController allowedServices]
- -[VoiceOverBluetoothDevicesController applicationDidBecomeActive:]
- -[VoiceOverBluetoothDevicesController applicationWillResignActive:]
- -[VoiceOverBluetoothDevicesController applicationWillTerminate:]
- -[VoiceOverBluetoothDevicesController authenticationRequestHandler:]
- -[VoiceOverBluetoothDevicesController authorizedServices]
- -[VoiceOverBluetoothDevicesController bluetoothIsBusy]
- -[VoiceOverBluetoothDevicesController bluetoothPowerAlertMessage]
- -[VoiceOverBluetoothDevicesController bluetoothPoweredOffFooter]
- -[VoiceOverBluetoothDevicesController centralManager:didDiscoverPeripheral:advertisementData:RSSI:]
- -[VoiceOverBluetoothDevicesController centralManager:didFailToConnectPeripheral:error:]
- -[VoiceOverBluetoothDevicesController centralManager:didFailToConnectPeripheral:error:].cold.1
- -[VoiceOverBluetoothDevicesController centralManager:didUpdatePeripheralConnectionState:]
- -[VoiceOverBluetoothDevicesController centralManagerDidUpdateState:]
- -[VoiceOverBluetoothDevicesController centralManager]
- -[VoiceOverBluetoothDevicesController currentSpecifier]
- -[VoiceOverBluetoothDevicesController dealloc]
- -[VoiceOverBluetoothDevicesController detailSpecifiersForDevice:withTarget:]
- -[VoiceOverBluetoothDevicesController deviceConnected:]
- -[VoiceOverBluetoothDevicesController deviceConnectedHandler:]
- -[VoiceOverBluetoothDevicesController deviceDisconnectedHandler:]
- -[VoiceOverBluetoothDevicesController deviceDiscoveredHandler:]
- -[VoiceOverBluetoothDevicesController devicePairedHandler:]
- -[VoiceOverBluetoothDevicesController deviceRemovedHandler:]
- -[VoiceOverBluetoothDevicesController deviceUnpairedHandler:]
- -[VoiceOverBluetoothDevicesController deviceUpdatedHandler:]
- -[VoiceOverBluetoothDevicesController devicesGroupName]
- -[VoiceOverBluetoothDevicesController handleReloadSpecifiers]
- -[VoiceOverBluetoothDevicesController init]
- -[VoiceOverBluetoothDevicesController mainSpecifiersGroup]
- -[VoiceOverBluetoothDevicesController pairedDeviceSpecifiers]
- -[VoiceOverBluetoothDevicesController pairingAgent:peerDidCompletePairing:]
- -[VoiceOverBluetoothDevicesController pairingAgent:peerDidFailToCompletePairing:error:]
- -[VoiceOverBluetoothDevicesController pairingAgent:peerDidUnpair:]
- -[VoiceOverBluetoothDevicesController peripheralConnectionTimeout:]
- -[VoiceOverBluetoothDevicesController peripheralDidUpdateName:]
- -[VoiceOverBluetoothDevicesController peripheralMatchesUnadvertisedService:]
- -[VoiceOverBluetoothDevicesController postDevicesSpecifiersGroup]
- -[VoiceOverBluetoothDevicesController powerAlertCancelled]
- -[VoiceOverBluetoothDevicesController powerChangedHandler:]
- -[VoiceOverBluetoothDevicesController reloadSpecifiers]
- -[VoiceOverBluetoothDevicesController scanningEnabled]
- -[VoiceOverBluetoothDevicesController setAuthorizedServices:]
- -[VoiceOverBluetoothDevicesController setBluetoothIsBusy:]
- -[VoiceOverBluetoothDevicesController setCentralManager:]
- -[VoiceOverBluetoothDevicesController setMainSpecifiersGroup:]
- -[VoiceOverBluetoothDevicesController setScanningEnabled:]
- -[VoiceOverBluetoothDevicesController shouldAddBTLEDevice:]
- -[VoiceOverBluetoothDevicesController shouldAddClassicDevice:]
- -[VoiceOverBluetoothDevicesController shouldReloadSpecifiersOnResume]
- -[VoiceOverBluetoothDevicesController showBluetoothPowerAlert:]
- -[VoiceOverBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]
- -[VoiceOverBluetoothDevicesController specifierImmediatelyPrecedingDevices]
- -[VoiceOverBluetoothDevicesController specifiers]
- -[VoiceOverBluetoothDevicesController tableView:accessoryButtonTappedForRowWithIndexPath:]
- -[VoiceOverBluetoothDevicesController tableView:cellForRowAtIndexPath:]
- -[VoiceOverBluetoothDevicesController tableView:didSelectRowAtIndexPath:]
- -[VoiceOverBluetoothDevicesController updatePairedDevices]
- -[VoiceOverBluetoothDevicesController viewDidAppear:]
- -[VoiceOverBluetoothDevicesController willBecomeActive]
- -[VoiceOverBluetoothDevicesController willResignActive]
- -[VoiceOverBluetoothDevicesController window]
- -[VoiceOverBrailleController _bluetoothDisplayAddressFromPreferences]
- -[VoiceOverBrailleController _isPairedDeviceBrailleDisplay:]
- -[VoiceOverBrailleController loadView]
- -[VoiceOverController centralManagerDidUpdateState:]
- -[VoiceOverController viewWillDisappear:]
- GCC_except_table22
- GCC_except_table30
- GCC_except_table78
- GCC_except_table81
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._alert
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._authorizedServices
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._bluetoothInitialized
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._bluetoothIsBusy
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._centralManager
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._currentDeviceSpecifier
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._deviceSpecifiersGroup
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._devicesDict
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._mainSpecifiersGroup
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._pairingPINDict
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._power
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._powerAlert
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._scanningEnabled
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._sspAlert
- OBJC_IVAR_$_VoiceOverBluetoothDevicesController._togglingPower
- OBJC_IVAR_$_VoiceOverController._centralManager
- _OBJC_CLASS_$_VoiceOverBluetoothDevicesController
- _OBJC_METACLASS_$_VoiceOverBluetoothDevicesController
- _VOTLogBraille
- __104-[AXVoiceOverImageDescriptionsController assetController:didFinishRefreshingAssets:wasSuccessful:error:]_block_invoke.341
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.664
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.664.cold.1
- __52-[SCATController setPayWithSwitchControl:specifier:]_block_invoke.671
- __53-[SCATController setSwitchScanningEnabled:specifier:]_block_invoke.607
- __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke.315
- __75-[ClarityUIAdminPasscodeSetupController _axShowDoneControllerWithPasscode:]_block_invoke_2.317
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.264
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.276
- __94-[AXVoiceOverImageDescriptionsController _installLanguageTranslationModelForLanguageIfNeeded:]_block_invoke.276.cold.1
- __AXSPrefersHorizontalTextLayout
- __AXSVoiceOverTouchCopyBrailleBluetoothDisplay
- __AXSVoiceOverTouchSetTactileGraphicsDisplay
- __OBJC_$_INSTANCE_METHODS_VoiceOverBluetoothDevicesController
- __OBJC_$_INSTANCE_VARIABLES_VoiceOverBluetoothDevicesController
- __OBJC_$_PROP_LIST_VoiceOverBluetoothDevicesController
- __OBJC_CLASS_PROTOCOLS_$_VoiceOverBluetoothDevicesController
- __OBJC_CLASS_RO_$_VoiceOverBluetoothDevicesController
- __OBJC_METACLASS_RO_$_VoiceOverBluetoothDevicesController
- ___106-[VoiceOverBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke
- ___106-[VoiceOverBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke_2
- ___106-[VoiceOverBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke_3
- ___106-[VoiceOverBluetoothDevicesController showPairingAlertForPairingAgent:peerDidRequestPairing:type:passkey:]_block_invoke_4
- ___27-[HoverTextController init]_block_invoke_4
- ___50-[SCATAlertCoordinator showSwichAlreadyInUseAlert]_block_invoke
- ___50-[SCATAlertCoordinator showSwichAlreadyInUseAlert]_block_invoke_2
- ___58-[VoiceOverBluetoothDevicesController updatePairedDevices]_block_invoke
- ___63-[VoiceOverBluetoothDevicesController showBluetoothPowerAlert:]_block_invoke
- ___63-[VoiceOverBluetoothDevicesController showBluetoothPowerAlert:]_block_invoke_2
- ___79-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:]_block_invoke
- ___79-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:]_block_invoke_2
- ___79-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:]_block_invoke_3
- ___79-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:]_block_invoke_4
- ___79-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:]_block_invoke_5
- ___84-[SCATExternalSwitchSourceController switchRegistrarMFIButtonAlreadyInUseForSwitch:]_block_invoke
- ___85-[SCATExternalSwitchSourceController switchRegistrarMIDISourceAlreadyInUseForSwitch:]_block_invoke
- ___86-[SCATExternalSwitchSourceController switchRegistrarKeyboardKeyAlreadyInUseForSwitch:]_block_invoke
- ___88-[SCATExternalSwitchSourceController switchRegistrarGamepadSourceAlreadyInUseForSwitch:]_block_invoke
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56w_e23_v16?0"UIAlertAction"8ls32l8s40l8w56l8s48l8
- __block_literal_global.267
- __block_literal_global.279
- __block_literal_global.283
- __block_literal_global.308
- __block_literal_global.316
- __block_literal_global.325
- __block_literal_global.327
- __block_literal_global.330
- __block_literal_global.332
- __block_literal_global.337
- __block_literal_global.344
- __block_literal_global.356
- __block_literal_global.358
- __block_literal_global.365
- __block_literal_global.367
- __block_literal_global.371
- __block_literal_global.377
- __block_literal_global.390
- __block_literal_global.392
- __block_literal_global.402
- __block_literal_global.404
- __block_literal_global.434
- __block_literal_global.439
- __block_literal_global.455
- __block_literal_global.457
- __block_literal_global.476
- __block_literal_global.478
- __block_literal_global.483
- __block_literal_global.667
- __bluetoothBrailleDisplayChange
- _kAXSVoiceOverTouchBrailleBluetoothDisplayChangedNotification
- _objc_msgSend$_getDeviceForPeripheral:
- _objc_msgSend$_isPairedDeviceBrailleDisplay:
- _objc_msgSend$_specifierForDevice:
- _objc_msgSend$addBulletedListItemWithTitle:description:image:linkButton:
- _objc_msgSend$peripheral
- _objc_msgSend$setDescriptionText:
- _objc_msgSend$showSwichAlreadyInUseAlert
- _objc_msgSend$showSwitchNamingAlertWithSwitch:message:successHandler:
- _unnamed_array_storage.415
CStrings:
+ " %@ setting cell %{public}@ paired %d and connected %d"
+ "-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:]"
+ "AXBluetoothDevicesController"
+ "AddNewLanguage"
+ "AdditionalLanguages"
+ "AllCommands"
+ "B16@?0@\"VOSBluetoothDevice\"8"
+ "BRAILLE DISPLAY CHANGE: "
+ "Clarity Onboarding was interrupted. Changes to CLFSettings should not persist"
+ "CreateNewCommand"
+ "Device"
+ "FIRST_LAUNCH_SCANNING_MODE_GLIDING_CURSOR"
+ "FIRST_LAUNCH_SCANNING_MODE_GLIDING_CURSOR_FOOTER"
+ "FIRST_LAUNCH_SCANNING_MODE_HEAD_TRACKING"
+ "FIRST_LAUNCH_SCANNING_MODE_HEAD_TRACKING_FOOTER"
+ "FIRST_LAUNCH_SCANNING_MODE_ITEM"
+ "FIRST_LAUNCH_SCANNING_MODE_ITEM_FOOTER"
+ "FIRST_LAUNCH_SCANNING_MODE_LABEL"
+ "FavoritePhrases"
+ "FirstLaunchScanningModeIdentifier"
+ "Gestures"
+ "Handling LE device: %@ %@"
+ "HoverTextActivationModifier"
+ "ImportCustomCommands"
+ "Item is paired, but not in list, check if valid: %@"
+ "KeyboardShortcuts"
+ "MediaControls"
+ "PITCH_HEADER"
+ "ResetVoiceOverCommands"
+ "SCATFirstLaunchScanningModeController"
+ "SILENT_MODE"
+ "SILENT_MODE_FOOTER_ACTION_BUTTON"
+ "SILENT_MODE_FOOTER_RINGER_SWITCH"
+ "ScanningMode"
+ "Settings"
+ "SystemNotifications"
+ "T@\"NSString\",&,N,V_categoryName"
+ "TopLevel"
+ "TouchGestures"
+ "VOSounds"
+ "WebRotor"
+ "_categoryName"
+ "_clearOnboarding"
+ "_coreBluetoothReady:"
+ "_setSilentModeToggleEnabled:specifier:"
+ "_showSwitchAlreadyInUse"
+ "_silentModeToggleEnabled:"
+ "addBulletedListItemWithTitle:description:symbolName:tintColor:linkButton:"
+ "axDeviceControllerType"
+ "cachedBrailleDisplayIsPaired:"
+ "categoryName"
+ "commitChangesToSelectedApplications"
+ "configuration"
+ "exampleText"
+ "firstLaunchScanningMode:"
+ "getDeviceForPeripheral:"
+ "isPairedDeviceBrailleDisplay:"
+ "loadSettings"
+ "pairedBTLEDevices"
+ "resetAllSettings"
+ "setCategoryName:"
+ "setContentInsets:"
+ "setSilentModeToggleEnabled:"
+ "setSwitchControlFirstLaunchScanningMode:"
+ "showSwichAlreadyInUseAlert:"
+ "showSwitchNamingAlertWithSwitch:message:successHandler:cancelHandler:"
+ "silentModeToggleEnabled"
+ "specifierForDevice:"
+ "switchControlFirstLaunchScanningMode"
+ "switchControlLocStringForFirstLaunchScanningMode:"
+ "v48@0:8@16@24@?32@?40"
+ "voiceOverActivePunctuationGroup"
- "\x04\x11"
- "%{public}@ setting cell %{public}@ paired %d and connected %d"
- "-[SCATAlertCoordinator showSwitchNamingAlertWithSwitch:message:successHandler:]"
- "ACMRequirement - ACMRequirementDataRatchet"
- "Autoloading BLE connected: %@"
- "Handling LE device: %@"
- "Skipping paired device %@ because did not match paired Braille devices"
- "VoiceOverBluetoothDevicesController"
- "_bluetoothDisplayAddressFromPreferences"
- "_getDeviceForPeripheral:"
- "_isPairedDeviceBrailleDisplay:"
- "_specifierForDevice:"
- "addBulletedListItemWithTitle:description:image:linkButton:"
- "peripheral"
- "showSwichAlreadyInUseAlert"
- "showSwitchNamingAlertWithSwitch:message:successHandler:"

```
