## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-25.2.0.0.0
-  __TEXT.__text: 0x1abd4c
-  __TEXT.__auth_stubs: 0x2760
-  __TEXT.__objc_stubs: 0xe440
-  __TEXT.__objc_methlist: 0x6990
+25.3.1.0.0
+  __TEXT.__text: 0x1b63d0
+  __TEXT.__auth_stubs: 0x27f0
+  __TEXT.__objc_stubs: 0xee80
+  __TEXT.__objc_methlist: 0x6ff0
   __TEXT.__const: 0x3a40
-  __TEXT.__gcc_except_tab: 0x35e4
-  __TEXT.__cstring: 0x2b533
-  __TEXT.__objc_methname: 0x158d5
-  __TEXT.__objc_classname: 0x693
-  __TEXT.__objc_methtype: 0x2465
+  __TEXT.__gcc_except_tab: 0x3a28
+  __TEXT.__cstring: 0x2e0f3
+  __TEXT.__objc_classname: 0x707
+  __TEXT.__objc_methname: 0x163c7
+  __TEXT.__objc_methtype: 0x24ea
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca
   __TEXT.__constg_swiftt: 0x18ec

   __TEXT.__swift5_capture: 0x25e8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x3e88
+  __TEXT.__unwind_info: 0x4150
   __TEXT.__eh_frame: 0x2208
-  __DATA_CONST.__auth_got: 0x13c0
-  __DATA_CONST.__got: 0xae8
-  __DATA_CONST.__auth_ptr: 0x6d8
-  __DATA_CONST.__const: 0xad90
-  __DATA_CONST.__cfstring: 0x6a00
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __DATA_CONST.__auth_got: 0x1408
+  __DATA_CONST.__got: 0xb10
+  __DATA_CONST.__auth_ptr: 0x6d0
+  __DATA_CONST.__const: 0xafe8
+  __DATA_CONST.__cfstring: 0x6f40
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x110
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x88
-  __DATA_CONST.__objc_superrefs: 0xc0
+  __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA_CONST.__objc_arraydata: 0x2c8
-  __DATA_CONST.__objc_dictobj: 0x4b0
+  __DATA_CONST.__objc_arraydata: 0x2e8
+  __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x10b30
-  __DATA.__objc_selrefs: 0x4be0
-  __DATA.__objc_ivar: 0xd38
-  __DATA.__objc_data: 0x1f38
-  __DATA.__data: 0x32a8
-  __DATA.__bss: 0x6c90
+  __DATA.__objc_const: 0x11878
+  __DATA.__objc_selrefs: 0x4e68
+  __DATA.__objc_ivar: 0xdf8
+  __DATA.__objc_data: 0x2078
+  __DATA.__data: 0x33e8
+  __DATA.__bss: 0x6cb0
   __DATA.__common: 0x358
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6714
-  Symbols:   1133
-  CStrings:  8937
+  Functions: 7014
+  Symbols:   1147
+  CStrings:  9336
 
Symbols:
+ _CBErrorF
+ _OBJC_CLASS_$_AADeviceManager
+ _OBJC_CLASS_$_SBSRemoteAlertConfigurationContext
+ _OBJC_CLASS_$_SBSRemoteAlertDefinition
+ _OBJC_CLASS_$_SBSRemoteAlertHandle
+ __xpc_type_array
+ _xpc_array_get_count
+ _xpc_array_get_string
+ _xpc_array_get_uint64
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_dictionary
+ _xpc_dictionary_get_uint64
+ _xpc_string_create
+ _xpc_uint64_create
CStrings:
+ "\x02#\x11\x16"
+ "\x15\x12"
+ "\x18"
+ "\x19"
+ "### Create transaction failed"
+ "### XPC listener error: %{xpc}"
+ "### XPC unknown message type: %lld"
+ "### proxCardUserActionOnHeadphone failed: %{error}"
+ "###Invalid BT Address"
+ "###Invalid BT Address sent over xpc!"
+ "###Invalid USB Address sent over xpc!"
+ "###No valid XPC connection"
+ "###Unable to create xpcMessage"
+ "-[AAServicesXPCConnection proxCardUserActionOnHeadphone:btAddress:withAction:completion:]"
+ "-[AAServicesXPCConnection proxCardUserActionOnHeadphone:btAddress:withAction:completion:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]"
+ "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]_block_invoke_2"
+ "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]_block_invoke_4"
+ "-[AAUSBSupportedDeviceManagerDaemon _accessoryDiscoveryEnsureStarted]_block_invoke_5"
+ "-[AAUSBSupportedDeviceManagerDaemon _bluetoothDeviceFound:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _bluetoothDeviceLost:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _bluetoothStateChanged:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _connectToUSBDevice:isUserInitiate:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _connectToUSBDevice:isUserInitiate:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon _ensureOSTransaction]"
+ "-[AAUSBSupportedDeviceManagerDaemon _invokeAnyProxCardCompletion:result:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _logCurrentListOfUSBDevice]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon _pairedDeviceMonitorEnsureStarted]"
+ "-[AAUSBSupportedDeviceManagerDaemon _pairedDeviceMonitorEnsureStarted]_block_invoke_2"
+ "-[AAUSBSupportedDeviceManagerDaemon _pairedDeviceMonitorEnsureStopped]"
+ "-[AAUSBSupportedDeviceManagerDaemon _powerMonitorEnsureStarted]"
+ "-[AAUSBSupportedDeviceManagerDaemon _powerMonitorEnsureStopped]"
+ "-[AAUSBSupportedDeviceManagerDaemon _prefsChanged]"
+ "-[AAUSBSupportedDeviceManagerDaemon _releaseOSTransaction]"
+ "-[AAUSBSupportedDeviceManagerDaemon _startEffectiveUnlockedAfterBootTimer:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _startEffectiveUnlockedAfterBootTimer:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon _startPairingCompletionTimer:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _startPairingCompletionTimer:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon _startPairingModeTimer:]"
+ "-[AAUSBSupportedDeviceManagerDaemon _startPairingModeTimer:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon _startPairingUI:repairMode:]"
+ "-[AAUSBSupportedDeviceManagerDaemon activate]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon launchPairingProxCardWithInfo:]"
+ "-[AAUSBSupportedDeviceManagerDaemon launchPairingProxCardWithInfo:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon proxCardUserActionOnHeadphone:btAddress:withAction:completion:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon proxCardUserActionOnHeadphone:btAddress:withAction:completion:]_block_invoke_2"
+ "-[AAUSBSupportedDeviceManagerDaemon remoteAlertHandle:didInvalidateWithError:]"
+ "-[AAUSBSupportedDeviceManagerDaemon remoteAlertHandleDidActivate:]"
+ "-[AAUSBSupportedDeviceManagerDaemon remoteAlertHandleDidDeactivate:]"
+ "-[AAUSBSupportedDeviceManagerDaemon usbDeviceAirplaneModeChanged:address:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon usbDeviceAirplaneModeChanged:address:]_block_invoke_2"
+ "-[AAUSBSupportedDeviceManagerDaemon usbDeviceFound:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon usbDeviceLost:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon usbDeviceLost:]_block_invoke_2"
+ "-[AAUSBSupportedDeviceManagerDaemon usbDevicePairingModeChanged:address:]_block_invoke"
+ "-[AAUSBSupportedDeviceManagerDaemon usbDevicePairingModeChanged:address:]_block_invoke_2"
+ "-[AudioDeviceManager _bluetoothStateUpdate:]"
+ "-[AudioDeviceManager _connectedDeviceFound:]"
+ "-[AudioDeviceManager _connectedDeviceLost:]"
+ "-[AudioDeviceManager _connectedUSBDeviceMonitorStart]"
+ "-[AudioDeviceManager _connectedUSBDeviceMonitorStart]_block_invoke_4"
+ "-[AudioDeviceManager _ensureXPCStarted]"
+ "-[AudioDeviceManager _invalidate]"
+ "-[AudioDeviceManager _isDevicePairedCheck:]"
+ "-[AudioDeviceManager _myBluetoothAddressString]"
+ "-[AudioDeviceManager _newUSBDeviceFound:]"
+ "-[AudioDeviceManager _startXPCConnection]"
+ "-[AudioDeviceManager _usbDeviceLost:]"
+ "-[AudioDeviceManager _usbDevicePropertyChanged:]"
+ "-[AudioDeviceManager _xpcConnectionEvent:]"
+ "-[AudioDeviceManager _xpcConnectionEvent:]_block_invoke"
+ "-[AudioDeviceManager _xpcConnectionInvalidated:]"
+ "-[AudioDeviceManager activate:]"
+ "-[AudioDeviceManager activate:]_block_invoke"
+ "-[AudioDeviceManager getAllAudioAccessoriesPublishedUIDsWithCompletion:]"
+ "-[AudioDeviceManager getAllAudioAccessoriesPublishedUIDsWithCompletion:]_block_invoke"
+ "-[AudioDeviceManager sendMsg:forUID:withArgs:]"
+ "-[AudioDeviceManager usbDeviceDisableAirPlaneMode:]"
+ "-[AudioDeviceManager usbDeviceEnableAirPlaneMode:]"
+ "-[AudioDeviceManager usbDeviceHideDevice:]"
+ "-[AudioDeviceManager usbDeviceUnHideDevice:]"
+ "-[BTSmartRoutingDaemon _cancelPairingTimer]"
+ "-[BTSmartRoutingDaemon _connectToUSBDevice:isUserInitiate:]"
+ "-[BTSmartRoutingDaemon _connectToUSBDevice:isUserInitiate:]_block_invoke"
+ "-[BTSmartRoutingDaemon _evaluatorRunForUSBDevice:trigger:]"
+ "-[BTSmartRoutingDaemon _evaluatorRunForUSBDevice:trigger:]_block_invoke"
+ "-[BTSmartRoutingDaemon _runUSBAudioRoutingPolicy:]_block_invoke"
+ "-[BTSmartRoutingDaemon _updateUSBDeviceForBluetoothStateChange:]"
+ "-[BTSmartRoutingDaemon _updateUSBDeviceForPairStateChange:paired:]"
+ "-[BTSmartRoutingDaemon _updateUSBDeviceForPairStateChange:paired:]_block_invoke"
+ "-[BTSmartRoutingDaemon usbDeviceFound:]_block_invoke"
+ "-[BTSmartRoutingDaemon usbDeviceFound:]_block_invoke_2"
+ "-[BTSmartRoutingDaemon usbDeviceLost:]_block_invoke"
+ "-[BTSmartRoutingDaemon usbDeviceLost:]_block_invoke_2"
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"SBSRemoteAlertHandle\""
+ "AAPairingManagerDaemon"
+ "AAUSBDeivce"
+ "AAUSBDeivce btAddress %@ pid %@ name %@ model %@ color %@"
+ "AAUSBSupportedDeviceManagerDaemon"
+ "AAUSBSupportedDeviceManagerDaemon Activate"
+ "Activation"
+ "Adding new USB device with address %@, name %@ and model %@ color %@ fwVersion %@ featureBitmask %@ pid %@ pairingMode %@"
+ "AudioDeviceManager"
+ "BT is off"
+ "BT off"
+ "BTOff unhide USB device."
+ "BTOnConnected"
+ "Bluetooth state powered off."
+ "Bluetooth state powered on."
+ "BluetoothDeviceFound: No btAddress"
+ "BluetoothDeviceFound: Not in USB device cache"
+ "BluetoothDeviceLost: No btAddress"
+ "BluetoothDeviceLost: Not in USB device cache"
+ "BluetoothDisconnection"
+ "BluetoothStateChange"
+ "Cancel pairing timer"
+ "Connect"
+ "Connected device lost. USBDevice %@"
+ "Creating os transaction for usb devices."
+ "Defaults writes for unified audio are not enabled, logic will not run"
+ "Device Lost: %@"
+ "Device is not paired. Attempt pairing logic."
+ "Device is paired but not connected, reconnect."
+ "DeviceManager interrupted"
+ "DeviceManager invalidated"
+ "Disable AirPlane Mode for %@"
+ "Dismissing existing Prox card %@"
+ "Enable AirPlane Mode for %@"
+ "Error reason"
+ "Error, AudioAccessoryMsgIdReturnAllPublishedUIDs was Invalidated"
+ "Error, AudioAccessoryMsgIdReturnAllPublishedUIDs was interrupted."
+ "Evaluator: Pairing failed, allow USB audio"
+ "Evaluator: Skip, USB plug-in source is connecting"
+ "Evaluator: connect complete USBDevice %@ result %@"
+ "Evaluator: connect start USBDevice %@"
+ "Evaluator: connect start USBDevice %@ isPairing %s"
+ "EvaluatorRunForUSBDevice: Wx %@ trigger %s"
+ "Fail"
+ "Failed to activate prox card"
+ "Failed to launch prox card due to existing prox card"
+ "First connected device found. USBDevice %@"
+ "Found new USB device with address %@"
+ "Found published audio device %@"
+ "Getting published devices"
+ "HeadphoneProxService.HeadphoneFlowViewController"
+ "Hiding USB device %@"
+ "Host BT Address"
+ "Launched prox card!"
+ "Launching Prox Card with userInfo %@"
+ "Manually disconnect previously"
+ "Missing wx address"
+ "NULL"
+ "New USB published device found."
+ "No AAUSBDevice found"
+ "No SRDiscoveredDevice found"
+ "No USB device found"
+ "Not Streaming"
+ "Not last routed device"
+ "Nothing is pairing at this moment"
+ "PairStateChange"
+ "Pairing completion timed out. Did not connect to %@"
+ "Pairing failed: Allow USB audio"
+ "Pairing interrupted"
+ "Pairing mode update timed out. Did not receive pairing mode ack from %@"
+ "Pairing timed out"
+ "Prox Card connect USBDevice %@ airplaneMode %s"
+ "Prox Card user action on USBDevice %@ action %s"
+ "ProxCardCompletion: Paired successfully with %@"
+ "ProxCardCompletion: Pairing interrupted for %@"
+ "ProxCardCompletion: Pairing timed out for %@"
+ "ProxCardCompletion: Skip, invalid result %s for %@"
+ "Re-Activation"
+ "Re-trying connection to audiomxd / coraudiod. "
+ "Ready to Pair."
+ "Registration to audiomxd succeeded"
+ "RemoteAlertHandle error %@"
+ "RemoteAlertHandleDidActivate"
+ "RemoteAlertHandleDidDeactivate"
+ "Removing os transaction for usb devices."
+ "RunUSBAudioPolicy: Skip %@"
+ "SBSRemoteAlertHandleObserver"
+ "Screen is off, do not show pairing Prox Card"
+ "Sending XPC msgID: %lld"
+ "Sending power update to BT driver."
+ "Skip, BT is off"
+ "Skip, Wx already plugged in"
+ "Skip, already found the USB device"
+ "Start pairing completion timer for %@. Will time out in %ds"
+ "Start pairing mode timer for %@. Will time out in %ds"
+ "Starting XPC Listener Client."
+ "Streaming"
+ "T@\"NSArray\",C,N,V_fwVersion"
+ "T@\"NSNumber\",C,N,V_color"
+ "T@\"NSNumber\",C,N,V_featureBitmask"
+ "T@\"NSNumber\",C,N,V_pairingMode"
+ "T@\"NSNumber\",C,N,V_pid"
+ "T@\"NSString\",C,N,V_btAddress"
+ "T@\"NSString\",C,N,V_model"
+ "T@\"NSString\",C,N,V_usbModel"
+ "T@\"NSString\",C,N,V_usbUID"
+ "T@?,C,N,V_proxCardhandler"
+ "TB,N,V_isCurrentRoute"
+ "TB,N,V_isStreaming"
+ "TB,N,V_isUSBPluggedIn"
+ "TC,N,V_connectionState"
+ "TQ,N,V_pairinUIClickTick"
+ "USB Device Lost. "
+ "USB Device Property Change "
+ "USB device connection lost with address %@"
+ "USB device lost."
+ "USB device property changed."
+ "USB device with btAddress %@ and USB UID %@ is %@"
+ "USB device with btAddress %@ and USB UID %@, indicated that AirPlane Mode is OFF"
+ "USB device with btAddress %@ and USB UID %@, indicated that AirPlane Mode is ON"
+ "USB device with uid %@ and btaddress %@ unplugged"
+ "USBDevice"
+ "USBDevice btAddress %@ name %@ model %@ pid %@ color %@ pairingMode %@"
+ "USBDevice is null"
+ "USBDevice: %@"
+ "USBDevice: Bluetooth state change %s usbDevice %@"
+ "USBDevice: Pair state change %@ paired %s usbPlugin %s newPair %s"
+ "USBDevice: Unable to connect. Null address"
+ "USBDevice: Update for pairing change failed. Reason %@"
+ "USBPlugIn"
+ "Unhiding USB device %@"
+ "UsbDeviceAirplaneModeChanged inAirplaneMode %s Wx %@"
+ "UsbDeviceAirplaneModeChanged isPairingInProgress %s"
+ "UsbDeviceAirplaneModeChanged: Skip, %@"
+ "We are already tracking this device. Remove and update the object!"
+ "We are not tracking this device, something went wrong. "
+ "Wx address is invalid"
+ "Wx address is null"
+ "Wx is BT connected already"
+ "Wx not USB plug in"
+ "Wx not paired"
+ "Wx paired already"
+ "XPC Listener Activated."
+ "XPC invalidating object"
+ "XPC listener interrupted, re-try activation."
+ "XPC listener invalidated, wait to re-try activation for 3 min."
+ "[%d] device dump: %@"
+ "_aaDeviceManager"
+ "_aaUSBDeviceMap"
+ "_accessoryDiscoveryEnsureStarted"
+ "_accessoryDiscoveryEnsureStopped"
+ "_bluetoothDeviceFound:"
+ "_bluetoothDeviceLost:"
+ "_bluetoothStateChanged:"
+ "_bluetoothStateUpdate:"
+ "_btPowerState"
+ "_cancelPairingTimer"
+ "_color"
+ "_connectToUSBDevice:isUserInitiate:"
+ "_connectedBTDiscovery"
+ "_connectedBTUSBDevices"
+ "_connectedUSBDeviceMonitorStart"
+ "_dismissAnyPairingBanner"
+ "_dismissAnyPairingProxCard"
+ "_ensureOSTransaction"
+ "_ensureXPCStopped"
+ "_evaluatorRunForUSBDevice:trigger:"
+ "_featureBitmask"
+ "_fwVersion"
+ "_getAllUSBAudioDeviceBtAddresses"
+ "_hostBTAddress:"
+ "_invokeAnyProxCardCompletion:result:"
+ "_isCurrentRoute"
+ "_isStreaming"
+ "_isUSBDevice:"
+ "_isUSBPluggedIn"
+ "_lastConnectedUSBDevice"
+ "_logCurrentListOfUSBDevice"
+ "_model"
+ "_myBTAddress"
+ "_newUSBDeviceFound:"
+ "_pairinUIClickTick"
+ "_pairingAlertHandle"
+ "_pairingCompletionTimer"
+ "_pairingMode"
+ "_pairingModeTimer"
+ "_pid"
+ "_prefUSBAudioDevice"
+ "_proxCardCompletion"
+ "_proxCardhandler"
+ "_releaseOSTransaction"
+ "_runUSBAudioRoutingPolicy:"
+ "_sharingClient"
+ "_startPairingCompletionTimer:"
+ "_startPairingModeTimer:"
+ "_startPairingUI:repairMode:"
+ "_startXPCConnection"
+ "_transaction"
+ "_updateUSBDeviceForBluetoothStateChange:"
+ "_updateUSBDeviceForPairStateChange:paired:"
+ "_usbDeviceLost:"
+ "_usbDeviceMap"
+ "_usbDevicePropertyChanged:"
+ "_usbModel"
+ "_usbUID"
+ "_xpcConnection"
+ "_xpcConnectionEvent:"
+ "_xpcTimer"
+ "activate:"
+ "activateWithContext:"
+ "already BT connected"
+ "com.apple.AudioDeviceManager"
+ "com.apple.BTAudioHALPluginAccessories"
+ "featureBitmask"
+ "fwVersion"
+ "getAllAudioAccessoriesPublishedUIDsWithCompletion"
+ "getAllAudioAccessoriesPublishedUIDsWithCompletion:"
+ "initWithServiceName:viewControllerClassName:"
+ "isCurrentRoute"
+ "isStreaming"
+ "isUSBPluggedIn"
+ "kAccAudioMsgArgBTAddress"
+ "kAccAudioMsgArgUSBColor"
+ "kAccAudioMsgArgUSBDeviceAirPlaneModeOff"
+ "kAccAudioMsgArgUSBDeviceAirPlaneModeOn"
+ "kAccAudioMsgArgUSBDeviceBTAddress"
+ "kAccAudioMsgArgUSBDeviceHiddenState"
+ "kAccAudioMsgArgUSBDevicePairingState"
+ "kAccAudioMsgArgUSBDeviceStreamingState"
+ "kAccAudioMsgArgUSBFeatureBitMask"
+ "kAccAudioMsgArgUSBFwVersion"
+ "kAccAudioMsgArgUSBHostBTAddress"
+ "kAccAudioMsgArgUSBID"
+ "kAccAudioMsgArgUSBModelID"
+ "kAccAudioMsgArgUSBName"
+ "kAccAudioMsgArgUSBPairingMode"
+ "kAccAudioMsgArgUSBPid"
+ "kBTAudioMsgArgAllPublishedUIDs"
+ "kBTAudioMsgArgs"
+ "kBTAudioMsgDeviceUid"
+ "kBTAudioMsgId"
+ "kBTAudioMsgMethod"
+ "launchPairingProxCardWithInfo:"
+ "launchSource"
+ "lookupHandlesForDefinition:"
+ "missing srDisDevice"
+ "missing wx address"
+ "newHandleWithDefinition:configurationContext:"
+ "no USB device found"
+ "not USB plug-in"
+ "numberWithUnsignedLong:"
+ "pairinUIClickTick"
+ "pairingMode"
+ "proxCardUserActionOnHeadphone: %@"
+ "proxCardhandler"
+ "registerObserver:"
+ "remoteAlertHandle:didInvalidateWithError:"
+ "remoteAlertHandleDidActivate:"
+ "remoteAlertHandleDidDeactivate:"
+ "repairMode"
+ "repairRSSI"
+ "sendMsg:forUID:withArgs:"
+ "setBtAddress:"
+ "setConnectionState:"
+ "setFeatureBitmask:"
+ "setFwVersion:"
+ "setIsCurrentRoute:"
+ "setIsStreaming:"
+ "setIsUSBPluggedIn:"
+ "setPairinUIClickTick:"
+ "setPairingMode:"
+ "setPid:"
+ "setProxCardhandler:"
+ "setUsbModel:"
+ "setUsbUID:"
+ "sharedAAUSBSupportedDeviceManagerDaemon"
+ "sharedAudioDeviceManager"
+ "smartRoutingAudioRoutingRequest:withResponseHandler:"
+ "startBTConnectionDiscovery"
+ "startProxCardTransactionWithOptions:completion:"
+ "startUSBDeviceMonitoring"
+ "supportedDevice"
+ "unregisterObserver:"
+ "usbDeviceAirplaneModeChanged:address:"
+ "usbDeviceDisableAirPlaneMode:"
+ "usbDeviceEnableAirPlaneMode:"
+ "usbDeviceFound:"
+ "usbDeviceHideDevice:"
+ "usbDeviceLost:"
+ "usbDevicePairingModeChanged inPairingMode %s Wx %@"
+ "usbDevicePairingModeChanged:address:"
+ "usbDeviceUnHideDevice:"
+ "usbModel"
+ "usbUID"
+ "v16@?0@\"AudioAccessoryDevice\"8"
+ "v24@0:8@\"SBSRemoteAlertHandle\"16"
+ "v32@0:8@\"SBSRemoteAlertHandle\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"AAUSBDeivce\"16^B24"
+ "wx address is null"

```
