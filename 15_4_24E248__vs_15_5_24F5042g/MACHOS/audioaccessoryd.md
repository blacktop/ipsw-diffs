## audioaccessoryd

> `/System/Library/CoreServices/audioaccessoryd`

```diff

-24.26.0.0.0
-  __TEXT.__text: 0x1c7ba4
-  __TEXT.__auth_stubs: 0x2600
-  __TEXT.__objc_stubs: 0xe140
-  __TEXT.__objc_methlist: 0x6bf0
+25.2.0.0.0
+  __TEXT.__text: 0x1bc088
+  __TEXT.__auth_stubs: 0x2510
+  __TEXT.__objc_stubs: 0xd760
+  __TEXT.__objc_methlist: 0x65f0
   __TEXT.__const: 0x3c00
-  __TEXT.__gcc_except_tab: 0x3784
-  __TEXT.__cstring: 0x2c6d3
-  __TEXT.__objc_classname: 0x685
-  __TEXT.__objc_methname: 0x14fb3
-  __TEXT.__objc_methtype: 0x23af
+  __TEXT.__gcc_except_tab: 0x3318
+  __TEXT.__cstring: 0x29883
+  __TEXT.__objc_methname: 0x1465c
+  __TEXT.__objc_classname: 0x62e
+  __TEXT.__objc_methtype: 0x23a3
   __TEXT.__oslogstring: 0x881a
   __TEXT.__constg_swiftt: 0x18ec
   __TEXT.__swift5_typeref: 0x19c4

   __TEXT.__swift5_capture: 0x25e8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x4110
+  __TEXT.__unwind_info: 0x3e00
   __TEXT.__eh_frame: 0x2200
-  __DATA_CONST.__auth_got: 0x1310
-  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__auth_got: 0x1298
+  __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x6e0
-  __DATA_CONST.__const: 0xb1f0
-  __DATA_CONST.__cfstring: 0x77e0
-  __DATA_CONST.__objc_classlist: 0x1e8
+  __DATA_CONST.__const: 0xaf30
+  __DATA_CONST.__cfstring: 0x7060
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x338
-  __DATA_CONST.__objc_dictobj: 0x578
+  __DATA_CONST.__objc_arraydata: 0x308
+  __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x106c8
-  __DATA.__objc_selrefs: 0x4a20
-  __DATA.__objc_ivar: 0xcec
-  __DATA.__objc_data: 0x1f88
-  __DATA.__data: 0x30f8
-  __DATA.__bss: 0x6ce0
+  __DATA.__objc_const: 0xfd28
+  __DATA.__objc_selrefs: 0x47f0
+  __DATA.__objc_ivar: 0xc34
+  __DATA.__objc_data: 0x1e48
+  __DATA.__data: 0x3018
+  __DATA.__bss: 0x6cc0
   __DATA.__common: 0x358
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/HealthKit.framework/Versions/A/HealthKit
   - /System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth
-  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6973
-  Symbols:   1047
-  CStrings:  9046
+  Functions: 6672
+  Symbols:   1028
+  CStrings:  8642
 
Symbols:
- _CBErrorF
- _CFDataGetBytes
- _IOObjectRelease
- _IORegistryEntrySearchCFProperty
- _IOServiceGetMatchingService
- _IOServiceNameMatching
- _MGCopyAnswer
- _OBJC_CLASS_$_AADeviceManager
- _OBJC_CLASS_$_CBProductInfo
- __xpc_type_array
- _kIOMainPortDefault
- _xpc_array_get_count
- _xpc_array_get_string
- _xpc_array_get_uint64
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_dictionary
- _xpc_dictionary_get_uint64
- _xpc_string_create
- _xpc_uint64_create
CStrings:
- "\x02#\x11\x14"
- "\x15\x12"
- "\x18"
- "\x19"
- "### XPC listener error: %{xpc}"
- "### XPC unknown message type: %lld"
- "###Invalid BT Address"
- "###Invalid BT Address sent over xpc!"
- "###Invalid USB Address sent over xpc!"
- "###No valid XPC connection"
- "###Unable to create xpcMessage"
- "%02X:%02X:%02X:%02X:%02X:%02X"
- "%@_%@"
- "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]"
- "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]_block_invoke_2"
- "-[AAUSBSupportedDeviceManagerDaemon _bluetoothDeviceFound:]"
- "-[AAUSBSupportedDeviceManagerDaemon _bluetoothDeviceLost:]"
- "-[AAUSBSupportedDeviceManagerDaemon _bluetoothStateChanged:]"
- "-[AAUSBSupportedDeviceManagerDaemon _connectToUSBDevice:isUserInitiate:]"
- "-[AAUSBSupportedDeviceManagerDaemon _connectToUSBDevice:isUserInitiate:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon _invokeAnyProxCardCompletion:result:]"
- "-[AAUSBSupportedDeviceManagerDaemon _logCurrentListOfUSBDevice]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon _pairedDeviceMonitorEnsureStarted]"
- "-[AAUSBSupportedDeviceManagerDaemon _pairedDeviceMonitorEnsureStarted]_block_invoke_2"
- "-[AAUSBSupportedDeviceManagerDaemon _pairedDeviceMonitorEnsureStopped]"
- "-[AAUSBSupportedDeviceManagerDaemon _powerMonitorEnsureStarted]"
- "-[AAUSBSupportedDeviceManagerDaemon _powerMonitorEnsureStopped]"
- "-[AAUSBSupportedDeviceManagerDaemon _prefsChanged]"
- "-[AAUSBSupportedDeviceManagerDaemon _startEffectiveUnlockedAfterBootTimer:]"
- "-[AAUSBSupportedDeviceManagerDaemon _startEffectiveUnlockedAfterBootTimer:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon _startPairingCompletionTimer:]"
- "-[AAUSBSupportedDeviceManagerDaemon _startPairingCompletionTimer:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon _startPairingModeTimer:]"
- "-[AAUSBSupportedDeviceManagerDaemon _startPairingModeTimer:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon activate]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon proxCardUserActionOnHeadphone:btAddress:withAction:completion:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon proxCardUserActionOnHeadphone:btAddress:withAction:completion:]_block_invoke_2"
- "-[AAUSBSupportedDeviceManagerDaemon usbDeviceAirplaneModeChanged:address:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon usbDeviceAirplaneModeChanged:address:]_block_invoke_2"
- "-[AAUSBSupportedDeviceManagerDaemon usbDeviceFound:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon usbDeviceLost:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon usbDeviceLost:]_block_invoke_2"
- "-[AAUSBSupportedDeviceManagerDaemon usbDevicePairingModeChanged:address:]_block_invoke"
- "-[AAUSBSupportedDeviceManagerDaemon usbDevicePairingModeChanged:address:]_block_invoke_2"
- "-[AudioDeviceManager _bluetoothStateUpdate:]"
- "-[AudioDeviceManager _connectedDeviceFound:]"
- "-[AudioDeviceManager _connectedDeviceLost:]"
- "-[AudioDeviceManager _connectedUSBDeviceMonitorStart]"
- "-[AudioDeviceManager _connectedUSBDeviceMonitorStart]_block_invoke_2"
- "-[AudioDeviceManager _ensureXPCStarted]"
- "-[AudioDeviceManager _invalidate]"
- "-[AudioDeviceManager _isDevicePairedCheck:]"
- "-[AudioDeviceManager _myBluetoothAddressString]"
- "-[AudioDeviceManager _newUSBDeviceFound:]"
- "-[AudioDeviceManager _startXPCConnection]"
- "-[AudioDeviceManager _usbDeviceLost:]"
- "-[AudioDeviceManager _usbDevicePropertyChanged:]"
- "-[AudioDeviceManager _xpcConnectionEvent:]"
- "-[AudioDeviceManager _xpcConnectionEvent:]_block_invoke"
- "-[AudioDeviceManager _xpcConnectionInvalidated:]"
- "-[AudioDeviceManager activate:]"
- "-[AudioDeviceManager activate:]_block_invoke"
- "-[AudioDeviceManager getAllAudioAccessoriesPublishedUIDsWithCompletion:]"
- "-[AudioDeviceManager getAllAudioAccessoriesPublishedUIDsWithCompletion:]_block_invoke"
- "-[AudioDeviceManager sendMsg:forUID:withArgs:]"
- "-[AudioDeviceManager usbDeviceDisableAirPlaneMode:]"
- "-[AudioDeviceManager usbDeviceEnableAirPlaneMode:]"
- "-[AudioDeviceManager usbDeviceHideDevice:]"
- "-[AudioDeviceManager usbDeviceUnHideDevice:]"
- "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]"
- "-[BTServicesDaemon _audioQualityShowBanner:title:deviceAddressString:messageKey:messageArgs:timeoutSeconds:]_block_invoke"
- "-[BTSmartRoutingDaemon _cancelPairingTimer]"
- "-[BTSmartRoutingDaemon _connectToUSBDevice:isUserInitiate:]"
- "-[BTSmartRoutingDaemon _connectToUSBDevice:isUserInitiate:]_block_invoke"
- "-[BTSmartRoutingDaemon _evaluatorRunForUSBDevice:trigger:]"
- "-[BTSmartRoutingDaemon _evaluatorRunForUSBDevice:trigger:]_block_invoke"
- "-[BTSmartRoutingDaemon _runUSBAudioRoutingPolicy:]_block_invoke"
- "-[BTSmartRoutingDaemon _showPairingBanner:retryAfterFailure:]"
- "-[BTSmartRoutingDaemon _showPairingBanner:retryAfterFailure:]_block_invoke"
- "-[BTSmartRoutingDaemon _showPairingBanner:retryAfterFailure:]_block_invoke_2"
- "-[BTSmartRoutingDaemon _showPairingBanner:retryAfterFailure:]_block_invoke_3"
- "-[BTSmartRoutingDaemon _startUSBPairing:]"
- "-[BTSmartRoutingDaemon _updateUSBDeviceForBluetoothStateChange:]"
- "-[BTSmartRoutingDaemon _updateUSBDeviceForPairStateChange:paired:]"
- "-[BTSmartRoutingDaemon _updateUSBDeviceForPairStateChange:paired:]_block_invoke"
- "-[BTSmartRoutingDaemon startPairingTimer:]"
- "-[BTSmartRoutingDaemon startPairingTimer:]_block_invoke"
- "-[BTSmartRoutingDaemon usbDeviceAirplaneModeChanged:address:]_block_invoke"
- "-[BTSmartRoutingDaemon usbDeviceAirplaneModeChanged:address:]_block_invoke_2"
- "-[BTSmartRoutingDaemon usbDeviceFound:]_block_invoke"
- "-[BTSmartRoutingDaemon usbDeviceFound:]_block_invoke_2"
- "-[BTSmartRoutingDaemon usbDeviceLost:]_block_invoke"
- "-[BTSmartRoutingDaemon usbDeviceLost:]_block_invoke_2"
- "-[BTSmartRoutingDaemon usbDevicePairingModeChanged:address:]_block_invoke"
- "-[BTSmartRoutingDaemon usbDevicePairingModeChanged:address:]_block_invoke_2"
- "@\"SFClient\""
- "AAPairingManagerDaemon"
- "AAUSBDeivce"
- "AAUSBDeivce btAddress %@ pid %@ name %@ model %@ color %@"
- "AAUSBSupportedDeviceManagerDaemon"
- "AAUSBSupportedDeviceManagerDaemon Activate"
- "Activation"
- "Adding new USB device with address %@, name %@ and model %@ color %@ fwVersion %@ featureBitmask %@ pid %@ pairingMode %@"
- "AirPods Max"
- "AudioDeviceManager"
- "AudioQualityMonitor"
- "BT is off"
- "BT off"
- "BTOff unhide USB device."
- "BTOnConnected"
- "Banner-AudioQualityMonitor"
- "Bluetooth state powered off."
- "Bluetooth state powered on."
- "BluetoothAddress"
- "BluetoothDeviceFound: No btAddress"
- "BluetoothDeviceFound: Not in USB device cache"
- "BluetoothDeviceLost: No btAddress"
- "BluetoothDeviceLost: Not in USB device cache"
- "BluetoothDisconnection"
- "BluetoothStateChange"
- "CBLocalizable"
- "CONNECTION_FAILED"
- "Cancel pairing timer"
- "Connect"
- "Connected device lost. USBDevice %@"
- "Defaults writes for unified audio are not enabled, logic will not run"
- "Device Lost: %@"
- "Device is not paired. Attempt pairing logic."
- "Device is paired but not connected, reconnect."
- "DeviceManager interrupted"
- "DeviceManager invalidated"
- "Disable AirPlane Mode for %@"
- "Enable AirPlane Mode for %@"
- "Error reason"
- "Error, AudioAccessoryMsgIdReturnAllPublishedUIDs was Invalidated"
- "Error, AudioAccessoryMsgIdReturnAllPublishedUIDs was interrupted."
- "Evaluator: Pairing failed, allow USB audio"
- "Evaluator: Skip, USB plug-in source is connecting"
- "Evaluator: connect complete USBDevice %@ result %@"
- "Evaluator: connect start USBDevice %@"
- "Evaluator: connect start USBDevice %@ isPairing %s"
- "EvaluatorRunForUSBDevice: Wx %@ trigger %s"
- "Fail"
- "First connected device found. USBDevice %@"
- "Found new USB device with address %@"
- "Found published audio device %@"
- "Getting published devices"
- "Hiding USB device %@"
- "Host BT Address"
- "IODeviceTree"
- "Manually disconnect previously"
- "Missing wx address"
- "NULL"
- "New USB published device found."
- "No AAUSBDevice found"
- "No SRDiscoveredDevice found"
- "No USB device found"
- "Not Streaming"
- "Not last routed device"
- "Nothing is pairing at this moment"
- "PairStateChange"
- "Pairing completion timed out. Did not connect to %@"
- "Pairing failed: Allow USB audio"
- "Pairing interrupted"
- "Pairing mode update timed out. Did not receive pairing mode ack from %@"
- "Pairing timed out"
- "Pairing timeout. Did not receive pairing mode ack from %@"
- "Pairing timeout: Allow USB audio"
- "PostingBanner: Action TryAgain"
- "PostingBanner: Action connect. airplaneMode %s"
- "PostingBanner: Screen is locked, do not show pairing banner"
- "PostingBanner: Show pairing banner for %@ retry %s productID %u name %@"
- "Prox Card connect USBDevice %@ airplaneMode %s"
- "Prox Card user action on USBDevice %@ action %s"
- "ProxCardCompletion: Paired successfully with %@"
- "ProxCardCompletion: Pairing interrupted for %@"
- "ProxCardCompletion: Pairing timed out for %@"
- "ProxCardCompletion: Skip, invalid result %s for %@"
- "Re-Activation"
- "Re-trying connection to audiomxd / coraudiod. "
- "Ready to Pair."
- "Registration to coreaudiod succeeded"
- "RoutingActionIDTryAgain"
- "RunUSBAudioPolicy: Skip %@"
- "Sending XPC msgID: %lld"
- "Sending power update to BT driver."
- "Skip, Wx already plugged in"
- "Skip, already found the USB device"
- "Start pairing completion timer for %@. Will time out in %ds"
- "Start pairing mode timer for %@. Will time out in %ds"
- "StartUSBPairing: airplaneMode %s"
- "Started pairing timer for %@. Will time out in %ds"
- "Starting XPC Listener Client."
- "Starting pairing timer for %@"
- "Streaming"
- "T@\"NSArray\",C,N,V_fwVersion"
- "T@\"NSNumber\",C,N,V_color"
- "T@\"NSNumber\",C,N,V_featureBitmask"
- "T@\"NSNumber\",C,N,V_pairingMode"
- "T@\"NSNumber\",C,N,V_pid"
- "T@\"NSString\",C,N,V_btAddress"
- "T@\"NSString\",C,N,V_model"
- "T@\"NSString\",C,N,V_usbModel"
- "T@\"NSString\",C,N,V_usbUID"
- "T@?,C,N,V_proxCardhandler"
- "TB,N,V_isCurrentRoute"
- "TB,N,V_isStreaming"
- "TB,N,V_isUSBPluggedIn"
- "TC,N,V_connectionState"
- "TQ,N,V_pairinUIClickTick"
- "TRY_AGAIN"
- "USB Device Lost. "
- "USB Device Property Change "
- "USB device connection lost with address %@"
- "USB device lost."
- "USB device property changed."
- "USB device with btAddress %@ and USB UID %@ is %@"
- "USB device with btAddress %@ and USB UID %@, indicated that AirPlane Mode is OFF"
- "USB device with btAddress %@ and USB UID %@, indicated that AirPlane Mode is ON"
- "USB device with uid %@ and btaddress %@ unplugged"
- "USBDevice"
- "USBDevice btAddress %@ name %@ model %@ pid %@ color %@ pairingMode %@"
- "USBDevice is null"
- "USBDevice: %@"
- "USBDevice: Bluetooth state change %s usbDevice %@"
- "USBDevice: Pair state change %@ paired %s usbPlugin %s newPair %s"
- "USBDevice: Unable to connect. Null address"
- "USBDevice: Update for pairing change failed. Reason %@"
- "USBDevicePairingModeChanged %@ %s"
- "USBDevicePairingModeChanged: Skip %@"
- "USBDevicePairingModeChanged: isPairingInProgress %s secondsSincePairingBannerClick %us"
- "USBPlugIn"
- "Unhiding USB device %@"
- "UsbDeviceAirplaneModeChanged inAirplaneMode %s Wx %@"
- "UsbDeviceAirplaneModeChanged isPairingInProgress %s"
- "UsbDeviceAirplaneModeChanged: Skip, %@"
- "VIA_USB"
- "Voice Call"
- "We are already tracking this device. Remove and update the object!"
- "We are not tracking this device, something went wrong. "
- "Wx address is invalid"
- "Wx address is null"
- "Wx is BT connected already"
- "Wx not USB plug in"
- "Wx not paired"
- "Wx paired already"
- "XPC Listener Activated."
- "XPC invalidating object"
- "XPC listener interrupted, re-try activation."
- "XPC listener invalidated, wait to re-try activation for 3 min."
- "[%d] device dump: %@"
- "_aaDeviceManager"
- "_aaUSBDeviceMap"
- "_accessoryDiscoveryEnsureStarted"
- "_accessoryDiscoveryEnsureStopped"
- "_bluetoothDeviceFound:"
- "_bluetoothDeviceLost:"
- "_bluetoothStateChanged:"
- "_bluetoothStateUpdate:"
- "_btPowerState"
- "_cancelPairingTimer"
- "_color"
- "_connectToUSBDevice:isUserInitiate:"
- "_connectedBTDiscovery"
- "_connectedBTUSBDevices"
- "_connectedUSBDeviceMonitorStart"
- "_dismissAnyPairingBanner"
- "_ensureXPCStopped"
- "_evaluatorRunForUSBDevice:trigger:"
- "_featureBitmask"
- "_fwVersion"
- "_getAllUSBAudioDeviceBtAddresses"
- "_hostBTAddress:"
- "_invokeAnyProxCardCompletion:result:"
- "_isCurrentRoute"
- "_isStreaming"
- "_isUSBDevice:"
- "_isUSBPluggedIn"
- "_lastConnectedUSBDevice"
- "_logCurrentListOfUSBDevice"
- "_model"
- "_myBTAddress"
- "_newUSBDeviceFound:"
- "_pairinUIClickTick"
- "_pairingCompletionTimer"
- "_pairingMode"
- "_pairingModeTimer"
- "_pid"
- "_prefUSBAudioDevice"
- "_proxCardCompletion"
- "_proxCardhandler"
- "_runUSBAudioRoutingPolicy:"
- "_sharingClient"
- "_showPairingBanner:retryAfterFailure:"
- "_startPairingCompletionTimer:"
- "_startPairingModeTimer:"
- "_startUSBPairing:"
- "_startXPCConnection"
- "_updateUSBDeviceForBluetoothStateChange:"
- "_updateUSBDeviceForPairStateChange:paired:"
- "_usbDeviceLost:"
- "_usbDeviceMap"
- "_usbDevicePropertyChanged:"
- "_usbModel"
- "_usbUID"
- "_xpcConnection"
- "_xpcConnectionEvent:"
- "_xpcTimer"
- "activate:"
- "already BT connected"
- "apple_airpods_case"
- "apple_magic_keyboard"
- "apple_magic_keyboard_keypad"
- "apple_magic_keyboard_touch"
- "apple_magic_keyboard_touch_keypad"
- "apple_magic_mouse"
- "apple_magic_trackpad"
- "apple_mighty_mouse"
- "apple_wireless_keyboard"
- "apple_wireless_mouse"
- "audioQuality banner click result %d"
- "audioQuality banner user click"
- "audioQuality: Type %s, Name %@, Addr %@,  Timeout %.3f"
- "bluetooth"
- "bundleWithIdentifier:"
- "com.apple.AudioDeviceManager"
- "com.apple.BTAudioHALPluginAccessories"
- "com.apple.CoreBluetooth"
- "featureBitmask"
- "fwVersion"
- "getAllAudioAccessoriesPublishedUIDsWithCompletion"
- "getAllAudioAccessoriesPublishedUIDsWithCompletion:"
- "isCurrentRoute"
- "isStreaming"
- "isUSBPluggedIn"
- "kAccAudioMsgArgBTAddress"
- "kAccAudioMsgArgUSBColor"
- "kAccAudioMsgArgUSBDeviceAirPlaneModeOff"
- "kAccAudioMsgArgUSBDeviceAirPlaneModeOn"
- "kAccAudioMsgArgUSBDeviceBTAddress"
- "kAccAudioMsgArgUSBDeviceHiddenState"
- "kAccAudioMsgArgUSBDevicePairingState"
- "kAccAudioMsgArgUSBDeviceStreamingState"
- "kAccAudioMsgArgUSBFeatureBitMask"
- "kAccAudioMsgArgUSBFwVersion"
- "kAccAudioMsgArgUSBHostBTAddress"
- "kAccAudioMsgArgUSBID"
- "kAccAudioMsgArgUSBModelID"
- "kAccAudioMsgArgUSBName"
- "kAccAudioMsgArgUSBPairingMode"
- "kAccAudioMsgArgUSBPid"
- "kBTAudioMsgArgAllPublishedUIDs"
- "kBTAudioMsgArgs"
- "kBTAudioMsgDeviceUid"
- "kBTAudioMsgId"
- "kBTAudioMsgMethod"
- "local-mac-address"
- "localizedStringForKey:value:table:"
- "missing srDisDevice"
- "missing wx address"
- "no USB device found"
- "not USB plug-in"
- "pairinUIClickTick"
- "pairingMode"
- "productInfoWithProductID:"
- "proxCardhandler"
- "sendMsg:forUID:withArgs:"
- "setBtAddress:"
- "setConnectionState:"
- "setFeatureBitmask:"
- "setFwVersion:"
- "setIsCurrentRoute:"
- "setIsStreaming:"
- "setIsUSBPluggedIn:"
- "setPairinUIClickTick:"
- "setPairingMode:"
- "setPid:"
- "setProxCardhandler:"
- "setUsbModel:"
- "setUsbUID:"
- "sharedAAUSBSupportedDeviceManagerDaemon"
- "sharedAudioDeviceManager"
- "srDisDevice is null"
- "startBTConnectionDiscovery"
- "startPairingTimer:"
- "startUSBDeviceMonitoring"
- "usbDeviceAirplaneModeChanged:address:"
- "usbDeviceDisableAirPlaneMode:"
- "usbDeviceEnableAirPlaneMode:"
- "usbDeviceFound:"
- "usbDeviceHideDevice:"
- "usbDeviceLost:"
- "usbDevicePairingModeChanged inPairingMode %s Wx %@"
- "usbDevicePairingModeChanged:address:"
- "usbDeviceUnHideDevice:"
- "usbModel"
- "usbUID"
- "v16@?0@\"AudioAccessoryDevice\"8"
- "v32@?0@\"NSString\"8@\"AAUSBDeivce\"16^B24"
- "wx address is null"

```
