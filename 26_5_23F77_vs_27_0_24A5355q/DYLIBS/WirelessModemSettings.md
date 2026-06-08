## WirelessModemSettings

> `/System/Library/PreferenceBundles/WirelessModemSettings.bundle/WirelessModemSettings`

```diff

-815.1.0.0.0
-  __TEXT.__text: 0x1245c
-  __TEXT.__auth_stubs: 0xc10
-  __TEXT.__objc_methlist: 0xcac
+840.20.0.0.0
+  __TEXT.__text: 0x13668
+  __TEXT.__objc_methlist: 0xe04
   __TEXT.__const: 0x1c2
-  __TEXT.__cstring: 0x148f
-  __TEXT.__oslogstring: 0x9d6
-  __TEXT.__gcc_except_tab: 0x1cc
+  __TEXT.__cstring: 0x160f
+  __TEXT.__oslogstring: 0xb16
+  __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__swift5_typeref: 0xdc
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_reflstr: 0x14

   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__swift_as_cont: 0x4
+  __TEXT.__unwind_info: 0x4d0
   __TEXT.__eh_frame: 0x70
-  __TEXT.__objc_classname: 0x22f
-  __TEXT.__objc_methname: 0x2a16
-  __TEXT.__objc_methtype: 0xafe
-  __TEXT.__objc_stubs: 0x26e0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x3f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x418
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd30
+  __DATA_CONST.__objc_selrefs: 0xdd8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x618
-  __AUTH_CONST.__const: 0x218
-  __AUTH_CONST.__cfstring: 0x1520
-  __AUTH_CONST.__objc_const: 0x1900
+  __DATA_CONST.__got: 0x430
+  __AUTH_CONST.__const: 0x1d8
+  __AUTH_CONST.__cfstring: 0x1680
+  __AUTH_CONST.__objc_const: 0x1f18
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x640
   __AUTH.__objc_data: 0x320
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x10c
+  __DATA.__objc_ivar: 0x124
   __DATA.__data: 0x248
-  __DATA.__bss: 0x150
+  __DATA.__bss: 0x130
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x18

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
+  - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/Netrb.framework/Netrb

   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/SettingsFoundation.framework/SettingsFoundation
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
+  - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7A1C029F-1D5B-3EA9-9B83-CC2D53CB8194
-  Functions: 382
-  Symbols:   1560
-  CStrings:  1063
+  UUID: D1BEFDF9-AF34-31FF-B481-46DCC42EC8E5
+  Functions: 409
+  Symbols:   1654
+  CStrings:  473
 
Symbols:
+ -[MISManager hasConnectedClients]
+ -[WMSPersonalHotspotDataUsageCache fetchHotspotClientsUsage]
+ -[WMSPersonalHotspotDataUsageCache fetchHotspotClientsUsage].cold.1
+ -[WMSPersonalHotspotDataUsageCache fetchHotspotClientsUsage].cold.2
+ -[WMSPersonalHotspotDataUsageCache hotspotClientIDsForPeriod:mruMap:]
+ -[WMSPersonalHotspotDataUsageCache hotspotClientsUsage]
+ -[WMSPersonalHotspotDataUsageCache phClientInfoForID:]
+ -[WMSPersonalHotspotDataUsageCache setHotspotClientsUsage:]
+ -[WiFiNetworkNameController applyNetworkName:]
+ -[WiFiNetworkNameController applyNetworkName:].cold.1
+ -[WiFiNetworkNameController cancelButtonClicked:]
+ -[WiFiNetworkNameController doneButtonClicked:]
+ -[WiFiNetworkNameController doneButtonClicked:].cold.1
+ -[WiFiNetworkNameController emptySetter:specifier:]
+ -[WiFiNetworkNameController showDisconnectAlertWithName:]
+ -[WiFiNetworkNameController specifiers]
+ -[WiFiNetworkNameController tableView:cellForRowAtIndexPath:]
+ -[WiFiNetworkNameController textDidChange:]
+ -[WiFiNetworkNameController textField:shouldChangeCharactersInRange:replacementString:]
+ -[WiFiNetworkNameController textFieldShouldReturn:]
+ -[WiFiNetworkNameController utf8ByteLength:]
+ -[WiFiNetworkNameController viewDidAppear:]
+ -[WiFiNetworkNameController viewDidLoad]
+ -[WiFiNetworkNameController wifiNetworkName:]
+ -[WiFiSetupView .cxx_destruct]
+ -[WiFiSetupView setNetworkName:]
+ -[WirelessModemController _findInsertionPointForConnectedDevices]
+ -[WirelessModemController _hasConnectedClients]
+ -[WirelessModemController _restartMISDiscovery]
+ -[WirelessModemController _restartMISDiscovery].cold.1
+ -[WirelessModemController _setWiFiNetworkName:]
+ -[WirelessModemController _setWiFiNetworkName:].cold.1
+ -[WirelessModemController _setWiFiNetworkName:].cold.2
+ -[WirelessModemController _updateConnectedDevicesSection]
+ -[WirelessModemController _updateConnectedDevicesSection].cold.1
+ -[WirelessModemController _wiFiNetworkName]
+ -[WirelessModemController nameSpec]
+ -[WirelessModemController wifiNetworkName:]
+ GCC_except_table24
+ GCC_except_table4
+ GCC_except_table46
+ GCC_except_table67
+ _OBJC_CLASS_$_CWFInterface
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_WiFiNetworkNameController
+ _OBJC_IVAR_$_MISManager._ctConnection
+ _OBJC_IVAR_$_WMSPersonalHotspotDataUsageCache._hotspotClientsUsage
+ _OBJC_IVAR_$_WiFiSetupView._networkName
+ _OBJC_IVAR_$_WiFiSetupView._step1Label
+ _OBJC_IVAR_$_WirelessModemController._cachedNetworkName
+ _OBJC_IVAR_$_WirelessModemController._cwfInterface
+ _OBJC_IVAR_$_WirelessModemController._nameSpec
+ _OBJC_METACLASS_$_WiFiNetworkNameController
+ _UITextContentTypeNickname
+ _WiFiManagerClientSetMISState
+ __CTServerConnectionAddToRunLoop
+ __CTServerConnectionCreate
+ __CTServerConnectionRegisterForNotification
+ __OBJC_$_INSTANCE_METHODS_WiFiNetworkNameController
+ __OBJC_$_INSTANCE_VARIABLES_WiFiSetupView
+ __OBJC_$_PROP_LIST_WiFiNetworkNameController
+ __OBJC_CLASS_PROTOCOLS_$_WiFiNetworkNameController
+ __OBJC_CLASS_RO_$_WiFiNetworkNameController
+ __OBJC_METACLASS_RO_$_WiFiNetworkNameController
+ ___47-[WirelessModemController _restartMISDiscovery]_block_invoke
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.17
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.19
+ ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.19.cold.1
+ ___57-[WiFiNetworkNameController showDisconnectAlertWithName:]_block_invoke
+ ___57-[WiFiNetworkNameController showDisconnectAlertWithName:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e23_v16?0"UIAlertAction"8lw40l8s32l8
+ ___block_literal_global.21
+ ___block_literal_global.75
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.6
+ _coreTelephonyNotificationCallback
+ _coreTelephonyNotificationCallback.cold.1
+ _kPSWirelessDataUsageOtherDevicesKey
+ _kWiFiDataUsageInterfacePeerIDKey
+ _kWiFiSettingDataUsageDateKey
+ _kWiFiSettingDataUsagePHClientsKey
+ _kWiFiSettingDataUsageRecentDateKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_hasConnectedClients
+ _objc_msgSend$_restartMISDiscovery
+ _objc_msgSend$_setWiFiNetworkName:
+ _objc_msgSend$_wiFiNetworkName
+ _objc_msgSend$activate
+ _objc_msgSend$applyNetworkName:
+ _objc_msgSend$copy
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$doneButtonClicked:
+ _objc_msgSend$fetchHotspotClientsUsage
+ _objc_msgSend$hasConnectedClients
+ _objc_msgSend$hotspotClientsUsage
+ _objc_msgSend$initWithServiceType:
+ _objc_msgSend$internetSharingNetworkName
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$nameSpec
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setHotspotClientsUsage:
+ _objc_msgSend$setInternetSharingNetworkName:error:
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$setNetworkName:
+ _objc_msgSend$setPreferredAction:
+ _objc_msgSend$showDisconnectAlertWithName:
+ _objc_msgSend$stringByReplacingCharactersInRange:withString:
+ _objc_msgSend$stringValue
+ _objc_msgSend$utf8ByteLength:
+ _objc_opt_new
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _swift_release_x19
+ _swift_release_x8
+ _swift_retain_x19
- -[BluetoothSetupView initWithFrame:]
- GCC_except_table41
- GCC_except_table59
- GCC_except_table93
- _CTTelephonyCenterAddObserver
- _CTTelephonyCenterGetDefault
- _OBJC_CLASS_$_BluetoothSetupView
- _OBJC_IVAR_$_TetheringSetupView._btView
- _OBJC_METACLASS_$_BluetoothSetupView
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _PHocalizedStringWithFormat
- __OBJC_$_INSTANCE_METHODS_BluetoothSetupView
- __OBJC_CLASS_RO_$_BluetoothSetupView
- __OBJC_METACLASS_RO_$_BluetoothSetupView
- ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.14
- ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.16
- ___57-[WMSPersonalHotspotDataUsageCache _fetchDeviceDataUsage]_block_invoke.16.cold.1
- ___block_literal_global.18
- ___block_literal_global.20
- ___block_literal_global.76
- ___logger_block_invoke
- ___usageSizeString_block_invoke
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_WirelessModemSettings
- _cellDataChangedNotification
- _cellDataChangedNotification.cold.1
- _logger
- _logger.cold.1
- _logger.logger
- _logger.onceToken
- _objc_msgSend$arrayWithCapacity:
- _objc_msgSend$componentsJoinedByString:
- _objc_msgSend$initWithValidatedFormat:validFormatSpecifiers:locale:arguments:error:
- _objc_msgSend$setAdaptive:
- _objc_msgSend$setCountStyle:
- _objc_msgSend$setZeroPadsFractionDigits:
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$stringByTrimmingCharactersInSet:
- _objc_msgSend$stringFromByteCount:
- _objc_msgSend$whitespaceCharacterSet
- _objc_release_x10
- _objc_retain_x23
- _objc_retain_x24
- _objc_retain_x25
- _objc_retain_x27
- _objc_retain_x28
- _swift_retain
- _usageSizeString
- _usageSizeString.byteCountFormatter
- _usageSizeString.cold.1
- _usageSizeString.onceToken
- _zeroPaddedMACAddress
CStrings:
+ "%@"
+ "%s PHS has clients connected, showing confirmation prompt"
+ "%s setting network name: %@"
+ "%s: Could not create WiFiManagerClient"
+ "%s: Fetched hotspot usage: %{public}@"
+ "%s: Requesting connected devices update from manager"
+ "%s: restarting MIS discovery"
+ "-[WMSPersonalHotspotDataUsageCache fetchHotspotClientsUsage]"
+ "-[WiFiNetworkNameController applyNetworkName:]"
+ "-[WiFiNetworkNameController doneButtonClicked:]"
+ "-[WirelessModemController _restartMISDiscovery]"
+ "-[WirelessModemController _updateConnectedDevicesSection]"
+ "AirPort"
+ "Bluetooth"
+ "DISCONNECT_BUTTON_TITLE"
+ "DISCONNECT_HOTSPOT_MESSAGE"
+ "DISCONNECT_HOTSPOT_TITLE"
+ "Failed to set WiFi network name: %@"
+ "Hosts"
+ "HotspotDataUsage"
+ "NAME"
+ "NETWORK_NAME_STR"
+ "Other Devices"
+ "Others"
+ "PersonalHotspotSettings"
+ "Received cellDataChangedNotification"
+ "RenamePH"
+ "Successfully set WiFi network name to: %@"
+ "Type"
+ "WIFI_NAME"
+ "WIFI_NAME_TITLE"
+ "Wi-Fi Name"
+ "Wifi-NAN"
+ "a"
+ "ph-rename"
+ "ph-rename-clients"
+ "yyyy-MM-dd HH:mm:ss Z"
- "#"
- "#16@0:8"
- ".cxx_destruct"
- "0"
- ":"
- "@"
- "@\"BluetoothSetupView\""
- "@\"CTDeviceDataUsage\""
- "@\"CoreTelephonyClient\""
- "@\"NSArray\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PSSpecifier\""
- "@\"RadiosPreferences\""
- "@\"UIAlertController\""
- "@\"UIImageView\""
- "@\"UILabel\""
- "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
- "@\"UIMenu\"48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSArray\"40"
- "@\"UIView<PSHeaderFooterView>\"24@0:8@\"PSSpecifier\"16"
- "@\"USBSetupView\""
- "@\"WiFiSetupView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@36@0:8@16@24i32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@48@0:8@16{_NSRange=QQ}24@40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UITextField\"16"
- "B24@0:8@16"
- "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@16{_NSRange=QQ}24@40"
- "BluetoothSetupView"
- "CONNECT_OVER_BLUETOOTH_LABEL"
- "CONNECT_OVER_BLUETOOTH_STEP_1"
- "CONNECT_OVER_BLUETOOTH_STEP_2"
- "CONNECT_OVER_BLUETOOTH_STEP_3"
- "CoreTelephonyClientAppDataUsageDelegate"
- "CoreTelephonyClientRegistrationDelegate"
- "FamilyHotspotSettingsController"
- "HotspotClientUsageController"
- "HotspotFamilyMember"
- "MISManager"
- "MISStateChangedNotification:"
- "NSObject"
- "PHDataUsage"
- "PSHeaderFooterView"
- "PersonalHotspotBundleController"
- "Q"
- "Q16@0:8"
- "Q24@0:8Q16"
- "Received callDataChangedNotification"
- "SetupView"
- "T#,R"
- "T@\"CTDeviceDataUsage\",&,N,V_cachedDeviceDataUsage"
- "T@\"CoreTelephonyClient\",&,N,V_ctClient"
- "T@\"NSArray\",&,N,V_familyMembers"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSString\",&,N,V_altDSID"
- "T@\"NSString\",&,N,V_displayName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"PSSpecifier\",&,N,V_switchSpecifier"
- "T@?,C,N,V_refreshCompletionHandler"
- "TB,N,V_cacheNeedsRefresh"
- "TB,N,V_refreshInProgress"
- "TB,N,V_shouldShareWithFamily"
- "TQ,R"
- "T^{__WiFiManagerClient=},N,V_wifiClient"
- "Ti,N,V_shareOption"
- "UITextFieldDelegate"
- "URLWithString:"
- "USBSetupView"
- "Vv16@0:8"
- "WMSPersonalHotspotDataUsageCache"
- "WiFiPasswordController"
- "WiFiSetupView"
- "WirelessModemBundleController"
- "WirelessModemController"
- "^{NETRBClient=}"
- "^{_NSZone=}16@0:8"
- "^{__CFRunLoopSource=}"
- "^{__SCDynamicStore=}"
- "^{__WiFiDeviceClient=}"
- "^{__WiFiManagerClient=}"
- "^{__WiFiManagerClient=}16@0:8"
- "_"
- "_TtC21WirelessModemSettings33WirelessModemSettingsPluginLoader"
- "_altDSID"
- "_bandPreferenceSpec"
- "_bandPreferenceSpecFooterLabel"
- "_bandPreferenceSpecLabel"
- "_btAlert"
- "_btAlertClass"
- "_btAuthenticationRequestHandler:"
- "_btClassicDeviceClass"
- "_btDevicePairedHandler:"
- "_btPairControllerClass"
- "_btPairSetupClass"
- "_btPinRequestHandler:"
- "_btPowerChangedHandler:"
- "_btSSPAlert"
- "_btSSPConfirmationHandler:"
- "_btSSPNumericComparisonHandler:"
- "_btSSPPasskeyDisplayHandler:"
- "_btSSPRequestClass"
- "_btView"
- "_cacheNeedsRefresh"
- "_cachedDeviceDataUsage"
- "_carrierName"
- "_clearCache"
- "_ctClient"
- "_currentDeviceSpecifier"
- "_dataUsageCacheRefreshedHandler:"
- "_didRegisteredNotificationObservers"
- "_displayName"
- "_familyHotspotEnabled"
- "_familyMembers"
- "_fetchAndDisplayDataUsage"
- "_fetchDeviceDataUsage"
- "_generateFamilyPreferencesArray"
- "_generatePrefDictionaryForMember:"
- "_getFamilyMembers"
- "_getFamilyShare"
- "_groupPlacardSpec"
- "_handleUsageOrInfoChanged"
- "_hotspotDataUsageGroupSpec"
- "_hotspotDataUsageSpecifiers"
- "_icon"
- "_isInAWindow"
- "_joinOption:"
- "_labels"
- "_lastSuperviewBounds"
- "_layoutDirection"
- "_managedConfigurationChangedHandler:"
- "_misStateChangedHandler:"
- "_needStateUpdate"
- "_netClient"
- "_passwordSpec"
- "_personalHotspotModificationDisabled"
- "_placardSpec"
- "_powerAlert"
- "_preferenceLabelWithText:"
- "_queue"
- "_radioPrefs"
- "_reason"
- "_refreshCacheIfNeeded"
- "_refreshCompletionHandler"
- "_refreshInProgress"
- "_registerAllNotificationObservers"
- "_resetFamilyPreferences"
- "_scDynamicStore"
- "_scRunLoopSource"
- "_serialQueue"
- "_setFamilyPreferences"
- "_setFamilyShare:"
- "_setJoinOption:specifier:"
- "_setMISDiscoveryStateEnabled:effectiveImmediately:"
- "_setMISDiscoveryStateEnabled:effectiveImmediately:forceBand:"
- "_setWiFiPassword:"
- "_setupSteps"
- "_setupViewSpec"
- "_shareOption"
- "_shouldShareHotspotWithFamily"
- "_shouldShareWithFamily"
- "_showBTPowerPrompt"
- "_showBandPreferenceUI"
- "_showWifiView"
- "_specifierForFamilyMember:"
- "_specifiers"
- "_specifiersWithSpecifierMain:"
- "_state"
- "_stateFooterSpec"
- "_switchSpecifier"
- "_systemImageNamed:withConfiguration:"
- "_tetheringAlert"
- "_tetheringGroupSpec"
- "_tetheringPhoneNumber"
- "_tetheringSwitchSpec"
- "_tetheringURL"
- "_title"
- "_unregisterAllNotificationObservers"
- "_updateMemberWithMember:"
- "_updatePersonalHotspotModificationDisableState"
- "_updateTetheringText:"
- "_usageForBundleID:inPeriod:"
- "_usbView"
- "_waitingOnBTPower"
- "_waitingOnWifiPower"
- "_wiFiPassword"
- "_wiFiPower"
- "_wiFiPowerChangedHandler"
- "_wifiClient"
- "_wifiDevice"
- "_wifiIsWAPI"
- "_wifiTetheringSupported"
- "_wifiView"
- "actionWithTitle:style:handler:"
- "activeKeyboard"
- "addAction:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:selector:name:object:"
- "addStep:"
- "addSubview:"
- "addTarget:action:forControlEvents:"
- "address"
- "airplaneMode"
- "alertControllerWithTitle:message:preferredStyle:"
- "alertSheetDismissed:"
- "allObjects"
- "allowWirelessConnections:"
- "altDSID"
- "appDataUsageForPeriod:"
- "applicationDidBecomeActive:"
- "applicationWillResign:"
- "applicationWillResignActive:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "attachMIS"
- "authenticate"
- "autorelease"
- "bandPreference"
- "bandPreferenceSpec"
- "becomeFirstResponder"
- "bluetooth"
- "boolValue"
- "boundingRectWithSize:options:attributes:context:"
- "bounds"
- "bundleForClass:"
- "bundleId"
- "bundleIdentifier"
- "bundleURL"
- "bundleWithPath:"
- "bytes"
- "cacheNeedsRefresh"
- "cachedDeviceDataUsage"
- "callStackSymbols"
- "cancelButtonClicked:"
- "cellChanged:cell:"
- "cellForRowAtIndexPath:"
- "cellMonitorUpdate:info:"
- "cellularHome"
- "cellularRoaming"
- "characterSetWithCharactersInString:"
- "childViewControllers"
- "class"
- "cleanupPairing"
- "clearColor"
- "com.apple.cellularSettings"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByString:"
- "configurationWithPointSize:weight:scale:"
- "conformsToProtocol:"
- "copyCarrierBundleValue:key:bundleType:error:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "ctClient"
- "currentDevice"
- "currentHandler"
- "currentLocale"
- "customerServiceProfileChanged:visible:"
- "d24@0:8d16"
- "d32@0:8d16@\"UITableView\"24"
- "d32@0:8d16@24"
- "dataRatesChanged"
- "dataUsageForLastPeriods:completion:"
- "dataUsageString"
- "dataUsageString:"
- "dataUsingEncoding:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "description"
- "detachMIS"
- "deviceWithDevice:"
- "dictionary"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didUserPreventData"
- "dismiss"
- "dismissPairingAlert:"
- "dismissViewControllerAnimated:completion:"
- "displayName"
- "displayStatusChanged:status:"
- "doneButtonClicked:"
- "editableTextField"
- "emptyGroupSpecifier"
- "emptySetter:specifier:"
- "enabled"
- "encryptionStatusChanged:info:"
- "enhancedDataLinkQualityChanged:metric:"
- "enhancedVoiceLinkQualityChanged:metric:"
- "enumerateObjectsUsingBlock:"
- "familyMembers"
- "familyShareSpecifier"
- "fetchDataUsageWithCompletion:"
- "fetchPersonalHotspotDataUsageSpecifierWithTotalDataUsage:"
- "font"
- "frame"
- "generateDefaultPassword"
- "getCurrentDataSubscriptionContextSync:"
- "getSpecifiersForClients"
- "getState:andReason:"
- "getTetheringStatus:"
- "groupSpecifierWithName:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "hash"
- "hiddenAppDataUsageForPeriod:"
- "i16@0:8"
- "icon"
- "identifier"
- "image"
- "imsRegistrationChanged:info:"
- "indexPathForIndex:"
- "init"
- "initPrivate"
- "initWithAltDSID:displayName:shareOption:"
- "initWithArray:"
- "initWithBarButtonSystemItem:target:action:"
- "initWithBundleType:"
- "initWithCoreTelephonyClient:"
- "initWithDevice:"
- "initWithDevice:andSpecifier:"
- "initWithFrame:"
- "initWithImage:"
- "initWithKey:table:locale:bundleURL:"
- "initWithName:reason:userInfo:"
- "initWithObjects:"
- "initWithParentListController:"
- "initWithParentListController:properties:"
- "initWithPath:"
- "initWithQueue:"
- "initWithSpecifier:"
- "initWithValidatedFormat:validFormatSpecifiers:locale:arguments:error:"
- "insertContiguousSpecifiers:atIndex:animated:"
- "insertSpecifier:atEndOfGroup:animated:"
- "intValue"
- "internetTethering:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isProxy"
- "labelColor"
- "lastObject"
- "layoutSubviews"
- "length"
- "load"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "majorClass"
- "model"
- "mutableCopy"
- "name"
- "native"
- "navigationController"
- "navigationItem"
- "networkListAvailable:list:"
- "networkReselectionNeeded:"
- "networkSelected:success:mode:"
- "notificationWithName:object:userInfo:"
- "nrDisableStatusChanged:status:"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "openURL:withCompletionHandler:"
- "operatorNameChanged:name:"
- "pairingStyle"
- "parentViewController"
- "passwordSpec"
- "pe_emitNavigationEventForApplicationSettingsWithApplicationBundleIdentifier:title:localizedNavigationComponents:deepLink:"
- "pe_emitNavigationEventForSystemSettingsWithGraphicIconIdentifier:title:localizedNavigationComponents:deepLink:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:afterDelay:"
- "performSelector:withObject:withObject:"
- "performSelectorOnMainThread:withObject:waitUntilDone:"
- "plmnChanged:plmn:"
- "popViewControllerAnimated:"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "powered"
- "preferenceSpecifierNamed:target:set:get:detail:cell:edit:"
- "preferredHeightForWidth:"
- "preferredHeightForWidth:inTableView:"
- "presentViewController:animated:completion:"
- "principalClass"
- "properties"
- "propertyForKey:"
- "proxied"
- "proxiedOnlyAppDataUsageForPeriod:"
- "queue"
- "ratSelectionChanged:selection:"
- "readMISState:andReason:"
- "refreshCompletionHandler"
- "refreshContentsWithSpecifier:"
- "refreshDataUsageUINotification"
- "refreshInProgress"
- "rejectCauseCodeChanged:causeCode:"
- "release"
- "reloadSpecifier:"
- "reloadSpecifier:animated:"
- "reloadSpecifiers"
- "removeAllObjects"
- "removeContiguousSpecifiers:animated:"
- "removeFromSuperview"
- "removeObjectForKey:"
- "removeObserver:"
- "removeSpecifier:"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "reverseObjectEnumerator"
- "rightBarButtonItem"
- "rootController"
- "secondaryLabelColor"
- "self"
- "sendStateUpdate"
- "setAdaptive:"
- "setAltDSID:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setBandPreference:specifier:"
- "setButtonAction:"
- "setCacheNeedsRefresh:"
- "setCachedDeviceDataUsage:"
- "setClearButtonMode:"
- "setConnectable:"
- "setContentMode:"
- "setCountStyle:"
- "setCtClient:"
- "setDelegate:"
- "setDiscoverable:"
- "setDisplayName:"
- "setDisplaySecureTextUsingPlainText:"
- "setEnabled:"
- "setFamilyMembers:"
- "setFont:"
- "setFrame:"
- "setIcon:"
- "setIdentifier:"
- "setInternetTethering:specifier:"
- "setKeyboardType:"
- "setLeftBarButtonItem:"
- "setLineBreakMode:"
- "setName:"
- "setNumberOfLines:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPairingStyle:andPasskey:"
- "setParentController:"
- "setPersonalHotspotModificationDisableState:"
- "setPowered:"
- "setProperties:"
- "setProperty:forKey:"
- "setQueue:"
- "setRefreshCompletionHandler:"
- "setRefreshInProgress:"
- "setReturnKeyEnabled:"
- "setReturnKeyType:"
- "setRightBarButtonItem:"
- "setRootController:"
- "setShareOption:"
- "setShouldShareWithFamily:"
- "setShowingSetupController:"
- "setSpecifier:"
- "setState:"
- "setSwitchSpecifier:"
- "setText:"
- "setTextAlignment:"
- "setTextColor:"
- "setTextContentType:"
- "setTintColor:"
- "setTitle:"
- "setTitleView:"
- "setUserInfo:"
- "setValue:forKey:"
- "setValues:titles:"
- "setWifiClient:"
- "setZeroPadsFractionDigits:"
- "setupViewSpec"
- "shareOption"
- "shareSpecifier"
- "sharedApplication"
- "sharedInstance"
- "sharedManager"
- "shouldShareWithFamily"
- "show"
- "showAlert:"
- "showAlertWithResult:"
- "showController:"
- "showPairingAlert:"
- "showSetupAlert:"
- "signalStrengthChanged:info:"
- "sizeThatFits:"
- "sizeThatFits:inTableView:shouldSetSize:"
- "sizeThatFits:shouldSetSize:"
- "sortUsingFunction:context:"
- "specifiers"
- "specifiersWithSpecifier:"
- "stateFooterSpec"
- "stopService"
- "stringByAppendingString:"
- "stringByTrimmingCharactersInSet:"
- "stringFromByteCount:"
- "stringFromByteCount:countStyle:"
- "stringWithFormat:"
- "subviews"
- "superclass"
- "superview"
- "switchSpecifier"
- "systemServiceDataUsageForPeriod:"
- "tableView:cellForRowAtIndexPath:"
- "tag"
- "terminateSearching:"
- "tetheringSwitchSpec"
- "text"
- "textDidChange:"
- "textField:editMenuForCharactersInRange:suggestedActions:"
- "textField:editMenuForCharactersInRanges:suggestedActions:"
- "textField:insertInputSuggestion:"
- "textField:shouldChangeCharactersInRange:replacementString:"
- "textField:shouldChangeCharactersInRanges:replacementString:"
- "textField:willDismissEditMenuWithAnimator:"
- "textField:willPresentEditMenuWithAnimator:"
- "textFieldDidBeginEditing:"
- "textFieldDidChangeSelection:"
- "textFieldDidEndEditing:"
- "textFieldDidEndEditing:reason:"
- "textFieldShouldBeginEditing:"
- "textFieldShouldClear:"
- "textFieldShouldEndEditing:"
- "textFieldShouldReturn:"
- "title"
- "totalHotspotClientUsageForPeriod:"
- "traitCollection"
- "uninstalledAppDataUsageForPeriod:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateDataUsageSection"
- "updateInstructionsSection:"
- "updateSpecifiersForState:andReason:andButton:"
- "uppercaseString"
- "usageSpecifier"
- "used"
- "userInfo"
- "userInterfaceIdiom"
- "userInterfaceLayoutDirection"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
- "v24@0:8@\"PSSpecifier\"16"
- "v24@0:8@\"UITextField\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8^{__WiFiManagerClient=}16"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16B20B24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTEncryptionStatusInfo\"24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTNRStatus\"24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTPlmnInfo\"24"
- "v32@0:8@\"CTServiceDescriptor\"16@\"CTRatSelection\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTCellInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedDataLinkQualityMetric\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTEnhancedLinkQualityMetric\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTIMSRegistrationTransportInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTNetworkList\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTRegistrationDisplayStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTSignalStrengthInfo\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTVoiceLinkQualityMetric\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSDictionary\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSString\"24"
- "v32@0:8@\"UITextField\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"UITextField\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v32@0:8^i16^i24"
- "v32@0:8i16i20@24"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16B24@\"NSString\"28"
- "v36@0:8@16B24@28"
- "valueForKey:"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLoad"
- "visibleViewController"
- "voiceLinkQualityChanged:metric:"
- "whitespaceCharacterSet"
- "wifiClient"
- "wifiPassword:"
- "willMoveToParentViewController:"
- "wms_popViewControllerWithAnimated:"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{CGSize=dd}36@0:8{CGSize=dd}16B32"
- "{CGSize=dd}44@0:8{CGSize=dd}16@32B40"

```
