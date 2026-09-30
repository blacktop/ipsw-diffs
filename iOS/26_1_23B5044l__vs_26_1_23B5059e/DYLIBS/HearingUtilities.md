## HearingUtilities

> `/System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities`

```diff

-496.2.0.0.0
-  __TEXT.__text: 0x991a0
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x7d6c
+496.4.1.0.0
+  __TEXT.__text: 0x99984
+  __TEXT.__auth_stubs: 0x1140
+  __TEXT.__objc_methlist: 0x7d84
   __TEXT.__const: 0x40a
-  __TEXT.__gcc_except_tab: 0x2938
-  __TEXT.__cstring: 0x4eab
-  __TEXT.__oslogstring: 0x7e38
+  __TEXT.__gcc_except_tab: 0x290c
+  __TEXT.__cstring: 0x4edb
+  __TEXT.__oslogstring: 0x9bc7
   __TEXT.__dlopen_cstrs: 0x7a7
   __TEXT.__swift5_typeref: 0x46
   __TEXT.__swift5_capture: 0x30

   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0x25d0
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x841
-  __TEXT.__objc_methname: 0x14230
-  __TEXT.__objc_methtype: 0x2183
-  __TEXT.__objc_stubs: 0xed60
+  __TEXT.__objc_classname: 0x843
+  __TEXT.__objc_methname: 0x142ac
+  __TEXT.__objc_methtype: 0x2197
+  __TEXT.__objc_stubs: 0xed80
   __DATA_CONST.__got: 0x620
-  __DATA_CONST.__const: 0x3458
+  __DATA_CONST.__const: 0x3420
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4980
+  __DATA_CONST.__objc_selrefs: 0x4988
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x430
-  __AUTH_CONST.__auth_got: 0x898
+  __AUTH_CONST.__auth_got: 0x8b0
   __AUTH_CONST.__const: 0xd98
   __AUTH_CONST.__cfstring: 0x5200
-  __AUTH_CONST.__objc_const: 0xa5d8
+  __AUTH_CONST.__objc_const: 0xa608
   __AUTH_CONST.__objc_intobj: 0xa80
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_doubleobj: 0x1290
   __AUTH.__objc_data: 0xfa8
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x8f8
+  __DATA.__objc_ivar: 0x8fc
   __DATA.__data: 0xc20
   __DATA.__bss: 0x408
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5C2EA768-6CEA-31EF-824D-480D4E03CB0A
+  UUID: 42D91E66-F097-3976-85B4-82B526AB5265
   Functions: 3585
-  Symbols:   11533
-  CStrings:  6025
+  Symbols:   11540
+  CStrings:  6050
 
Symbols:
+ -[AXHAServer handleMessageWithPayload:forIdentifier:].cold.1
+ -[AXHearingAidDevice setValue:forProperty:].cold.1
+ -[AXHearingAidLEAudioDevice updateName].cold.1
+ -[HANanoSettings domainAccessorQueue]
+ -[HANanoSettings setDomainAccessorQueue:]
+ -[HUNoiseController sendNotificationRequestWithTitle:body:suggestANCMode:suggestHearingProtection:]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table26
+ GCC_except_table31
+ GCC_except_table85
+ _HCLogHearingLiveListen
+ _OBJC_IVAR_$_AXHearingAidDevice._leftPowerSourceDictionary
+ _OBJC_IVAR_$_AXHearingAidDevice._leftPowerSourceID
+ _OBJC_IVAR_$_HANanoSettings._domainAccessorQueue
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.429
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.433
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.441
+ ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.450
+ ___37-[HUNoiseController restartADAMTimer]_block_invoke.392
+ ___41-[HANanoSettings _valueForPreferenceKey:]_block_invoke
+ ___41-[HANanoSettings _valueForPreferenceKey:]_block_invoke.cold.1
+ ___44-[HANanoSettings setValue:forPreferenceKey:]_block_invoke
+ ___44-[HANanoSettings setValue:forPreferenceKey:]_block_invoke.cold.1
+ ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.403
+ ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.50
+ ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.50.cold.1
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.412
+ ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.417
+ ___99-[HUNoiseController sendNotificationRequestWithTitle:body:suggestANCMode:suggestHearingProtection:]_block_invoke
+ ___99-[HUNoiseController sendNotificationRequestWithTitle:body:suggestANCMode:suggestHearingProtection:]_block_invoke.cold.1
+ ___block_descriptor_57_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_literal_global.391
+ ___block_literal_global.435
+ ___block_literal_global.443
+ ___block_literal_global.452
+ ___block_literal_global.49
+ ___block_literal_global.52
+ __os_signpost_emit_with_name_impl
+ _objc_msgSend$domainAccessorQueue
+ _objc_msgSend$sendNotificationRequestWithTitle:body:suggestANCMode:suggestHearingProtection:
+ _os_signpost_enabled
- -[AXHearingAidDevice peripheral:didDiscoverServices:].cold.1
- -[AXHearingAidDevice peripheral:didDiscoverServices:].cold.2
- -[AXHearingAidDevice valueForProperty:].cold.2
- -[AXHearingAidDevice valueForProperty:].cold.3
- -[AXHearingAidDeviceController centralManager:didConnectPeripheral:].cold.1
- -[HANanoSettings _valueForPreferenceKey:].cold.1
- -[HANanoSettings setValue:forPreferenceKey:].cold.1
- -[HUNoiseController shouldShowHearingProtectionSuggestionForAlertType:]
- GCC_except_table103
- GCC_except_table152
- GCC_except_table29
- GCC_except_table97
- _OBJC_IVAR_$_AXHearingAidDevice._leftPowerSouceDictionary
- _OBJC_IVAR_$_AXHearingAidDevice._leftPowerSouceID
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.428
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.432
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.440
- ___107-[HUNoiseController checkToSurfaceAnalyticsNotificationForSPL:withDuration:andBuffer:forTime:andThreshold:]_block_invoke.449
- ___37-[HUNoiseController restartADAMTimer]_block_invoke.390
- ___50-[HUNoiseController showNotificationForAlertType:]_block_invoke.cold.1
- ___53-[HUNoiseController readEnvironmentalDosimetryLevels]_block_invoke.401
- ___56-[HUComfortSoundsController audioSessionWasInterrupted:]_block_invoke
- ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.46
- ___62-[AXHearingAidLEAudioDevice delayWriteProperty:forPeripheral:]_block_invoke.46.cold.1
- ___71-[HUNoiseController shouldShowHearingProtectionSuggestionForAlertType:]_block_invoke
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.411
- ___85-[HUNoiseController checkToSurfaceNotificationForSPL:withDuration:andBuffer:forTime:]_block_invoke.416
- ___block_literal_global.389
- ___block_literal_global.434
- ___block_literal_global.442
- ___block_literal_global.45
- ___block_literal_global.451
- ___block_literal_global.48
- _objc_msgSend$shouldShowHearingProtectionSuggestionForAlertType:
CStrings:
+ "AXHAServer: Availability %@"
+ "AXHAServer: HA server is ready."
+ "AXHAServer: Handle incoming message ID: %@ %@"
+ "AXHAServer: Unexpected message ID: %@"
+ "AXHAServer: Unregister from available devices listener: %@"
+ "AXHAServer: Unregister from property update listener: %@"
+ "AXHAServer: Unregister from updates listenerHash: %@"
+ "AXHAServer: XPC sending messagesPriority: Default"
+ "AXHAServer: XPC sending messagesPriority: Urgent"
+ "AXHAServer: writeValue, XPC sending payload %@"
+ "AXHeardController: BT not yet ready, delaying shutdown check"
+ "AXHeardController: BT ready, processing shutdown check"
+ "AXHeardController: BT state updated %@"
+ "AXHeardController: Found clients %llu = %@"
+ "AXHeardController: IDS stats is saved, should be running: %d"
+ "AXHeardController: Setting boost %@"
+ "AXHeardController: Will shutdown, save IDS stats"
+ "AXHeardController: continueSetup, Recently rebooted. Disabling fake hearing aids"
+ "AXHeardController: handleMessage %llu - %@"
+ "AXHeardController: handleMessage %llu - %{mask.hash}@"
+ "AXHeardController: heard should be running. Continuing"
+ "AXHeardController: heard shouldn't be running. Shutting down."
+ "AXHeardController: heard shouldn't be running. Starting timer"
+ "BackgroundSoundsEnablement"
+ "CentralManager LEA 3: session connected peripherals %@"
+ "CentralManager: BT not available. Caching [%ld, %d]"
+ "CentralManager: No peripherals with identifiers, unpairing %@"
+ "CentralManager: centralManagerDidUpdateState, Central state (%ld) %d = %d"
+ "CentralManager: didConnectPeripheral, %@ in %@"
+ "CentralManager: didConnectPeripheral, state: %ld %@"
+ "CentralManager: didDisconnectPeripheral state: %ld %@ %@ error: %@"
+ "CentralManager: didDiscoverPeripheral %@\n serviceUUIDs: %@\n existingDevice: %@\n advertisementData: %@"
+ "CentralManager: didFailToConnectPeripheral %@ - %@"
+ "CentralManager: didFailToConnectPeripheral, Fatal error"
+ "CentralManager: didFailToConnectPeripheral, Non fatal error. Attempting reconnect"
+ "CentralManager: didRetrieveConnectedPeripherals %@"
+ "CentralManager: didRetrievePeripherals %@, persistentDevices %@"
+ "CentralManager: disconnectFromPeripheral: state: %ld, %@"
+ "Failed to update the power source with peripheralUUID %@ and deviceUUID %@"
+ "HAController: Checking paired %d"
+ "HAController: Current controller is device, connected=%d, connecting=%d, nearby state=%@\nPaired Device=%@"
+ "HAController: Current controller is nearby"
+ "HAController: HearingAidDeviceController updated Available Devices, Changing paired Hearing Aids from: %@ to: %@, Update clients with properties"
+ "HAController: HearingAidDeviceController updated Available Devices, Updating Clients with Available Devices: %@"
+ "HAController: setPairedHearingAidID %@, related: %d, connected: (old %d, new %d), new loaded: %d, \n old: %@, \n new: %@"
+ "HAController: setPairedHearingAidID, Hearing Aids unpaired. Cleared and updated available controllers"
+ "HAController: setPairedHearingAidID, connect and start updates new aids: %@"
+ "HAController: setPairedHearingAidID, stop updates and unpair old aids: %@"
+ "HUDeviceController: Stopping Updates"
+ "HUDeviceController: didUpdateProperty, UPDATING %@ - %@"
+ "HUDeviceController: didUpdateProperty, Update Paired %@ Connected %@"
+ "HearingAidDevice peripheral: Reloading services %@, %@"
+ "HearingAidDevice peripheral: didDiscoverCharacteristicsForService, %@ %@, service %@ - %@"
+ "HearingAidDevice peripheral: didDiscoverCharacteristicsForService, EMPTY CHARACTERISTICS %@"
+ "HearingAidDevice peripheral: didDiscoverServices, %@ %@ %@"
+ "HearingAidDevice peripheral: didDiscoverServices, EMPTY SERVICES %@ %@"
+ "HearingAidDevice peripheral: didDiscoverServices, Error discovering services %@ %@ %@"
+ "HearingAidDevice peripheral: didInvalidateServices, peripheral %@, services %@, \n%@"
+ "HearingAidDevice peripheral: didUpdateCharacteristic, %@ %@ %@"
+ "HearingAidDevice peripheral: didUpdateCharacteristic, %@ %@ DIS value: %@, ear: %@, L: %@, R: %@"
+ "HearingAidDevice peripheral: didUpdateCharacteristic, Firmware version found: %@ %@ %@"
+ "HearingAidDevice peripheral: didUpdateCharacteristic, Getting property: %@ (%@) for %@ - %@"
+ "HearingAidDevice peripheral: didUpdateCharacteristic, Hardware version found: %@ %@ %@"
+ "HearingAidDevice peripheral: didUpdateCharacteristic, Manufacturer found: %@ %@ |%@|"
+ "HearingAidDevice peripheral: didUpdateCharacteristic, Model Number found: %@ %@ |%@|"
+ "HearingAidDevice peripheral: didUpdateValueForCharacteristic, Error reading characteristic value (%@)(%@): %@"
+ "HearingAidDevice peripheral: didWriteValueForCharacteristic, %@ - %@"
+ "HearingAidDevice peripheral: didWriteValueForCharacteristic, Error writing characteristic value (%@): %@"
+ "HearingAidDevice peripheral: peripheralDidUnpair %@"
+ "HearingAidDevice peripheral: readValueForCharacteristic, Reading %@ from %@"
+ "HearingAidDevice peripheral: writeInt, Writing %d for %@ - %@"
+ "HearingAidDevice peripheral: writeSignedInt, Writing %d for %@ - %@"
+ "HearingAidDevice: Did pair with result %d - %@"
+ "HearingAidDevice: Disabling input for %@"
+ "HearingAidDevice: Enabling input for %@"
+ "HearingAidDevice: Mate, self: %@ other %@"
+ "HearingAidDevice: Setting notify %d for peripheral: %@ - %@"
+ "HearingAidDevice: Updated shouldStreamToLeftAid, Hearing aid isn't paired, but we're changing streaming prefs %@"
+ "HearingAidDevice: Updated shouldStreamToRightAid, Hearing aid isn't paired, but we're changing streaming prefs %@"
+ "HearingAidDevice: Wrist orientation changed %@"
+ "HearingAidDevice: _sendDelayedWrites, Left %lld - Right %lld"
+ "HearingAidDevice: addPeripheral %@ %@ to device:\n%@"
+ "HearingAidDevice: addPeripheral %@ to device:\n%@"
+ "HearingAidDevice: connectionDidChange, Confirmed Paired and BT paired: %@ - %@"
+ "HearingAidDevice: connectionDidChange, connecting %d, connected %d"
+ "HearingAidDevice: dealloc, Disconnecting %@"
+ "HearingAidDevice: delayWriteProperty, Not writing because peripheral isn't paired"
+ "HearingAidDevice: delayWriteProperty, [%d] %lld - %@"
+ "HearingAidDevice: didLoadBasicProperties {%d} LEFT [%d]: (%d, %d, %d, %d) RIGHT [%d]: (%d, %d, %d, %d)"
+ "HearingAidDevice: didLoadOptionalBasicProperties {%d} LEFT [%d, %d] RIGHT [%d, %d]"
+ "HearingAidDevice: didLoadOptionalBasicProperties, Adding available %@ - %@"
+ "HearingAidDevice: didLoadOptionalBasicProperties, Checking %@"
+ "HearingAidDevice: didLoadOptionalBasicProperties, No optional properties on left"
+ "HearingAidDevice: didLoadOptionalBasicProperties, No optional properties on right"
+ "HearingAidDevice: didLoadRequiredProperties {%d} LEFT [%d]: (%d, %d, %d, %d, %d) RIGHT [%d]: (%d, %d, %d, %d, %d)"
+ "HearingAidDevice: disconnectAndUnpair %d"
+ "HearingAidDevice: init with Left&Right devices, Connecting %@"
+ "HearingAidDevice: init with Left&Right devices, Missing left peripheral UUID %@"
+ "HearingAidDevice: init with Left&Right devices, Missing right peripheral UUID %@"
+ "HearingAidDevice: init with Left&Right devices, Paired [L:%d, R:%d, iCloudPaired: %d] Disconnecting %@"
+ "HearingAidDevice: loadFailedProperties, (L: %@ - R: %@)"
+ "HearingAidDevice: loadProperties, Loading %@ for %@"
+ "HearingAidDevice: loadProperties, Not loading %@, %d, %d - %@ = %@"
+ "HearingAidDevice: loadRequiredProperties, Loading required properties for %@ - (%d, %d, %d, %d, %d, %d)"
+ "HearingAidDevice: pairingDidCompleteForPeripheral: failed, Disconnecting %@"
+ "HearingAidDevice: setKeepInSync, Not completely loaded, trying again"
+ "HearingAidDevice: setValue, Setting %@ to %@"
+ "HearingAidDevice: setValue, Status: Disconnected, Disconnecting %@"
+ "HearingAidDevice: swapPeripheral, %@: HearingDevice Swapped to Left %@, Right %@"
+ "HearingAidDevice: swapPeripheral, %@: HearingDevice Swapped to Right %@, Left %@"
+ "HearingAidDevice: updateName %@"
+ "HearingAidDevice: valueForProperty, %@ property %@ value %@"
+ "HearingAidDevice: valueForProperty, Compound property: %ld"
+ "HearingAidDevice: valueForProperty, Reading component property %@"
+ "HearingAidDevice: writeValueForProperty, FAILED left write response check %lld"
+ "HearingAidDevice: writeValueForProperty, FAILED right write response check %lld"
+ "HearingAidDeviceController LEA 3: didDiscoverPeripheral %@, Created Hearing Aids device %@"
+ "HearingAidDeviceController LEA 3: session added the second peripheral %@ to %@"
+ "HearingAidDeviceController LEA 3: session setup"
+ "HearingAidDeviceController LEA 3: session update - ID %@, state %@"
+ "HearingAidDeviceController LEA 3: session update - event %@ error %@"
+ "HearingAidDeviceController LEA 3: session update - eventType %@, connectedIdentifiers %@, locations %@"
+ "HearingAidDeviceController: Already scanning"
+ "HearingAidDeviceController: Cancelling pending connections"
+ "HearingAidDeviceController: Device finished loading %@"
+ "HearingAidDeviceController: Device finished loading, not paired, Disconnecting %@"
+ "HearingAidDeviceController: Merging device %@ with: %@"
+ "HearingAidDeviceController: Not unpairing, no peripheral for %@"
+ "HearingAidDeviceController: Replacing device %@ with %@"
+ "HearingAidDeviceController: Resetting connection to %@"
+ "HearingAidDeviceController: Scan for available devices"
+ "HearingAidDeviceController: Scanning LEA 3"
+ "HearingAidDeviceController: Scanning MFi"
+ "HearingAidDeviceController: Unpairing peripheral %@"
+ "HearingAidDeviceController: checkPartiallyPaired, Partial pair %d = %@"
+ "HearingAidDeviceController: clearMissingHearingAids, Device stopped advertising. Removing %@"
+ "HearingAidDeviceController: connectToPeripheral, Requesting connection in state %@ to %@"
+ "HearingAidDeviceController: didConnectPeripheral %@\n connectedDevice (paired: %d)\n%@"
+ "HearingAidDeviceController: didConnectPeripheral, More than one valid hearing device %@"
+ "HearingAidDeviceController: didConnectPeripheral, No device found, disconnecting peripheral %@"
+ "HearingAidDeviceController: didDisconnectPeripheral, Will reconnect if possible: %@"
+ "HearingAidDeviceController: didDiscoverPeripheral %@, Created Hearing Aids device %@"
+ "HearingAidDeviceController: didDiscoverPeripheral, Connecting %d = [%d, %d, %d, %d]"
+ "HearingAidDeviceController: didDiscoverPeripheral, Will reconnect if possible %@"
+ "HearingAidDeviceController: didFailToConnectPeripheral, Non fatal error, Will reconnect if possible: %@"
+ "HearingAidDeviceController: didRetrieveConnectedPeripherals, Will reconnect if possible %@"
+ "HearingAidDeviceController: disconnectFromHearingAidWithDeviceUUID %@, Disconnection from %@"
+ "HearingAidDeviceController: disconnectFromHearingAidWithDeviceUUID %@, Disconnection is not allowed from %@"
+ "HearingAidDeviceController: isConnected, Found connected device %@"
+ "HearingAidDeviceController: isConnecting, Found connecting device %@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Adding peripheral to device [%d] %@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, New aids: %@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, No peripheral identifiers %@, unpairing rep %@"
+ "HearingAidDeviceController: pairedHearingAidsDidChange, Persistent device %@, %@"
+ "HearingAidDeviceController: shouldRelinquishForPartialConnection, Should relinquish %d, %d, %d, %d"
+ "HearingAidDeviceController: shouldRelinquishForPartialConnection, Wrong number of paired devices %@"
+ "HearingAidLEA3Device LEA 3: Connect to %@"
+ "HearingAidLEA3Device LEA 3: addPeripheral %@ %@ didAdd: %d to device:\n%@"
+ "HearingAidLEA3Device LEA 3: addPeripheral: %@, didAdd: %d\n%@"
+ "HearingAidLEA3Device LEA 3: availablePropertiesForPeripheral SKIP for %@"
+ "HearingAidLEA3Device LEA 3: characteristicForUUID SKIP for %@"
+ "HearingAidLEA3Device LEA 3: connectionDidChange, isConnecting %d %@"
+ "HearingAidLEA3Device LEA 3: delayWriteProperty %@ ear %@ peripheral %@ device name %@"
+ "HearingAidLEA3Device LEA 3: didLoadPersistentProperties %d %@, Left %@, Right %@"
+ "HearingAidLEA3Device LEA 3: disconnectAndUnpair(%d) from \n%@"
+ "HearingAidLEA3Device LEA 3: disconnectAndUnpair(%d), SKIP disconnecting/unpairing from %@ %@\n%@"
+ "HearingAidLEA3Device LEA 3: loadBasicProperties SKIP for %@"
+ "HearingAidLEA3Device LEA 3: loadProperties SKIP for %@ %@"
+ "HearingAidLEA3Device LEA 3: loadRequiredProperties SKIP for %@"
+ "HearingAidLEA3Device LEA 3: peripheral is unknown - %@"
+ "HearingAidLEA3Device LEA 3: peripheral setting notify %d for peripheral: %@ - %@"
+ "HearingAidLEA3Device LEA 3: peripheral setup update handler fail, device has no such peripheral - %@"
+ "HearingAidLEA3Device LEA 3: peripheralDidUpdateDeviceInfo, (paired: %d %d) device info updated: %p %@, left: %@, right: %@"
+ "HearingAidLEA3Device LEA 3: sessionDidUpdateLocations, session location %@ %@ %s"
+ "HearingAidLEA3Device LEA 3: sessionDidUpdateLocations, session location for unknown peripheral identifier %@"
+ "HearingAidLEA3Device LEA 3: sessionDidUpdateLocations, session unknown location %@ for %@"
+ "HearingAidLEA3Device LEA 3: sessionDidUpdateValue %@ for property %@, wrong format error, device %@"
+ "HearingAidLEA3Device LEA 3: setBasicPropertiesLoaded for %@"
+ "HearingAidLEA3Device LEA 3: setNotify SKIP for %@"
+ "HearingAidLEA3Device LEA 3: setValue, %@ %@ %@"
+ "HearingAidLEA3Device LEA 3: setup update handler for peripheral %@, device: %@"
+ "HearingAidLEA3Device LEA 3: setupLoadingProperties for %@"
+ "HearingAidLEA3Device LEA 3: updateName, (paired: %d %d) name: %p %@, left: %@, right: %@"
+ "HearingAidLEA3Device LEA 3: updated name %@"
+ "HearingAidLEA3Device LEA 3: updated name %@, saving persistent representation - %@"
+ "HearingAidLEA3Device LEA 3: writeValueForProperty SKIP for %@"
+ "HearingAidLEA3Device peripheral LEA 3: LeftPrograms %@"
+ "HearingAidLEA3Device peripheral LEA 3: RightPrograms %@"
+ "HearingAidLEA3Device peripheral LEA 3: availablePropertiesFromDIS %@ for Peripheral %@"
+ "HearingAidLEA3Device peripheral LEA 3: leftSelectedProgram %@"
+ "HearingAidLEA3Device peripheral LEA 3: preset - %@ "
+ "HearingAidLEA3Device peripheral LEA 3: preset available %d"
+ "HearingAidLEA3Device peripheral LEA 3: preset index: %d"
+ "HearingAidLEA3Device peripheral LEA 3: preset name: %s"
+ "HearingAidLEA3Device peripheral LEA 3: preset writable: %d"
+ "HearingAidLEA3Device peripheral LEA 3: rightSelectedProgram %@"
+ "HearingAidLEA3Device peripheral LEA 3: setActivePreset %@"
+ "HearingAidLEA3Device peripheral LEA 3: setActivePreset error %@"
+ "HearingAidLEA3Device peripheral LEA 3: setVolume %@ adjusted %@"
+ "HearingAidLEA3Device peripheral LEA 3: setVolume error %@"
+ "HearingAidLEA3Device peripheral LEA 3: update %@, HA features %@"
+ "HearingAidLEA3Device peripheral LEA 3: update %@, active preset %@"
+ "HearingAidLEA3Device peripheral LEA 3: update %@, name preset at index: %@"
+ "HearingAidLEA3Device peripheral LEA 3: update %@, presets %@, active preset index %@"
+ "HearingAidLEA3Device peripheral LEA 3: update %@, volume %@"
+ "HearingAidLEA3Device peripheral LEA 3: updateHandler %@ deviceType: %@, event type: %@, event: %@\n %@device: %@"
+ "HearingAidsSettings: Setting paired hearing aids %@"
+ "PairingAgent: Unpairing [%d] %@"
+ "PairingAgent: peerDidCompletePairing, Creating new easy pairing device %@"
+ "PairingAgent: peerDidCompletePairing, Found easy paired peripheral %@ - %@"
+ "PairingAgent: peerDidCompletePairing, Not iCloud paired. Storing UUIDs %@"
+ "PairingAgent: peerDidCompletePairing, Pairing completed %@ - %@"
+ "PairingAgent: peerDidCompletePairing, Peripheral missing tag %@"
+ "PairingAgent: peerDidCompletePairing, Skipping pairing because not a hearing device %@"
+ "PairingAgent: peerDidFailToCompletePairing, %@ - %@"
+ "PairingAgent: peerDidUnpair, Did Unpair %@ in device %@"
+ "T@\"AVAudioEngine\",&,V_engine"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_domainAccessorQueue"
+ "_domainAccessorQueue"
+ "_leftPowerSourceDictionary"
+ "_leftPowerSourceID"
+ "domainAccessorQueue"
+ "heard_hearing_aids_nano_domain_accessor_queue"
+ "sendNotificationRequestWithTitle:body:suggestANCMode:suggestHearingProtection:"
+ "setDomainAccessorQueue:"
+ "v40@0:8@16@24B32B36"
- "%@ - %@ - %@ - %@"
- "%@ peripheral %@, services %@"
- "%@: Firmware version found: %@"
- "%@: Hardware version found: %@"
- "%@: HearingDevice Swapped to Left %@, Right %@"
- "%@: HearingDevice Swapped to Right %@, Left %@"
- "%@: HearingDevice valueForProperty %@"
- "%@: HearingDevice valueForProperty value %@"
- "%@: Manufacturer found: |%@|"
- "%@: Model Number found: |%@|"
- "%@: peripheral %@ didDiscoverCharacteristicsForService %@ - %@"
- "%@: peripheral %@ didDiscoverServices %@"
- "%@: peripheral %@ didUpdateCharacteristic %@"
- "%@: peripheral %@ didUpdateCharacteristic DIS value: %@, ear: %@, L: %@, R: %@"
- "%d, %d, %d - %@ - %@ == %d, %@"
- "%llu - %@"
- "%llu - %{mask.hash}@"
- "(%@ - %@)"
- "Adding available %@ - %@"
- "Adding periperal %@ - %@"
- "Adding peripheral to device [%d] %@"
- "Already scanning"
- "Availability %@"
- "Available Devices: %@"
- "BT disconnectFromPeripheral: state: %ld, %@"
- "BT not available. Caching [%ld, %d]"
- "BT not yet ready, delaying shutdown check"
- "BT ready, processing shutdown check"
- "BT state updated %@"
- "Cancelling connections"
- "Central state (%ld) %d = %d"
- "CentralManager didDisconnectPeripheral state: %ld %@ %@ error: %@"
- "CentralManager didRetrieveConnectedPeripherals, Connect"
- "CentralManager: %@ in %@"
- "CentralManager: didConnectPeripheral %@\n Connected device: %@"
- "CentralManager: didConnectPeripheral state: %ld %@"
- "CentralManager: didDisconnectPeripheral, Connect"
- "CentralManager: didDiscoverPeripheral %@\nserviceUUIDs: %@\nadvertisementData: %@"
- "CentralManager: didDiscoverPeripheral, Connect to device %@"
- "CentralManager: didFailToConnectPeripheral, Non fatal, Reconnect: %@"
- "CentralManager: peripheral unpair %@"
- "Changing paired hearing aids %@"
- "Changing pairing %@ - %@"
- "Checking %@"
- "Checking paired %d"
- "Compound property: %ld"
- "Connecting %d = [%d, %d, %d, %d]"
- "Created Hearing Aids device %@"
- "Creating new easy pairing device %@"
- "Current controller is device %d, %d, %d - %@"
- "Current controller is nearby"
- "Device %@ did merge with: %@"
- "Device finished loading %@"
- "Device stopped advertising. Removing %@"
- "Did Unpair %@ in device %@"
- "Did Unpair: %@"
- "Did pair with result %d - %@"
- "Disabling input for %@"
- "Disconnection from %@"
- "Disconnection is not allowed from %@"
- "EMPTY CHARACTERISTICS %@"
- "EMPTY SERVICES"
- "Enabling input for %@"
- "Error discovering services (%@): %@"
- "Error reading characteristic value (%@)(%@): %@"
- "Error writing characteristic value (%@): %@"
- "FAILED left write response check %lld"
- "FAILED right write response check %lld"
- "Failed to update the power source with periperalUUID %@ and deviceUUID %@"
- "Fatal error"
- "Found clients %llu = %@"
- "Found connected device %@"
- "Found connecting device %@"
- "Found easy paired peripheral %@ - %@"
- "Getting property: %@ (%@) for %@ - %@"
- "HA server is ready."
- "Handle incoming message ID: %@ %@"
- "Hearing aid isn't paired, but we're changing streaming prefs %@"
- "Hearing aids unpaired. Updated available controllers"
- "HearingAidDevice connectionDidChange connecting: %d connected: %d"
- "IDS stats is saved, should be running: %d"
- "LEA 3: HearingDevice %@ setValue %@ %@"
- "LEA 3: HearingDevice (paired: %d %d) device info updated: %p %@, left: %@, right: %@"
- "LEA 3: HearingDevice (paired: %d %d) name updated: %p %@, left: %@, right: %@"
- "LEA 3: HearingDevice Basic Properties Loaded for %@"
- "LEA 3: HearingDevice Connect to %@"
- "LEA 3: HearingDevice SKIP disconnecting/unpairing from %@ %@\n%@"
- "LEA 3: HearingDevice connectionDidChange isConnecting %d %@"
- "LEA 3: HearingDevice didLoadPersistentProperties %d %@, Left %@, Right %@"
- "LEA 3: HearingDevice disconnecting/unpairing(%d) from \n%@"
- "LEA 3: HearingDevice name updated, saving persistent representation - %@"
- "LEA 3: HearingDevice newName %@"
- "LEA 3: HearingDevice setupLoadingProperties for %@"
- "LEA 3: Peripheral discovered %@, created Hearing Aids device %@"
- "LEA 3: addPeripheral: %@, didAdd: %d\n%@"
- "LEA 3: addPeripheral: %@, isLeft: %d, didAdd: %d\n%@"
- "LEA 3: availablePropertiesForPeripheral SKIP for %@"
- "LEA 3: characteristicForUUID SKIP for %@"
- "LEA 3: loadBasicProperties SKIP for %@"
- "LEA 3: loadProperties SKIP for %@ %@"
- "LEA 3: loadRequiredProperties SKIP for %@"
- "LEA 3: peripheral %@ deviceType: %@, event type: %@, event: %@\n %@device: %@"
- "LEA 3: peripheral BT setActivePreset %@"
- "LEA 3: peripheral BT setVolume %@ adjusted %@"
- "LEA 3: peripheral LeftPrograms %@"
- "LEA 3: peripheral RightPrograms %@"
- "LEA 3: peripheral availablePropertiesFromDIS %@ for Peripheral %@"
- "LEA 3: peripheral is unknown - %@"
- "LEA 3: peripheral leftSelectedProgram %@"
- "LEA 3: peripheral preset - %@ "
- "LEA 3: peripheral preset available %d"
- "LEA 3: peripheral preset index: %d"
- "LEA 3: peripheral preset name: %s"
- "LEA 3: peripheral preset writable: %d"
- "LEA 3: peripheral property write %@ ear %@ for %@ id %@"
- "LEA 3: peripheral rightSelectedProgram %@"
- "LEA 3: peripheral setActivePreset error %@"
- "LEA 3: peripheral setVolume error %@"
- "LEA 3: peripheral setting notify %d for peripheral: %@ - %@"
- "LEA 3: peripheral setup update handler -  %@"
- "LEA 3: peripheral setup update handler fail, device has no such peripheral - %@"
- "LEA 3: peripheral update - HA features %@"
- "LEA 3: peripheral update - active preset %@"
- "LEA 3: peripheral update - name preset at index: %@"
- "LEA 3: peripheral update - presets %@, active preset index %@"
- "LEA 3: peripheral update - volume %@"
- "LEA 3: session added the second peripheral %@ to %@"
- "LEA 3: session connected peripherals %@"
- "LEA 3: session location %@ %@ %s"
- "LEA 3: session location for unknown peripheral identifier %@"
- "LEA 3: session setup"
- "LEA 3: session unknown location %@ for %@"
- "LEA 3: session update - ID %@, state %@"
- "LEA 3: session update - event %@ error %@"
- "LEA 3: session update - eventType %@, connectedIdentifiers %@, locations %@"
- "LEA 3: setNotify SKIP for %@"
- "LEA 3: writeValueForProperty SKIP for %@"
- "Left %lld - Right %lld"
- "Loading %@ for %@"
- "Loading required properties for %@ - (%d, %d, %d, %d, %d, %d)"
- "MATE: self: %@ other %@"
- "Missing left peripheral UUID %@"
- "Missing right peripheral UUID %@"
- "More than one valid hearing device %@"
- "New aids: %@"
- "New name: %@"
- "No BT identifiers %@, unpairing rep %@"
- "No BT peripherals with identifiers, unpairing %@"
- "No device for peripheral %@"
- "No optional properties on left"
- "No optional properties on right"
- "Non fatal error. Attempting reconnect"
- "Not iCloud paired. Storing UUIDs %@"
- "Not loading %@, %d, %d - %@ = %@"
- "Not unpairing %@"
- "Not writing because peripheral isn't paired"
- "Paired: %@ - %@"
- "Pairing completed %@ - %@"
- "Partial pair %d = %@"
- "Peripheral missing tag %@"
- "Persistent device %@, %@"
- "Reading %@ from %@"
- "Reading component property %@"
- "Recently rebooted. Disabling fake hearing aids"
- "Reloading services %@, %@"
- "Replacing %@ with %@"
- "Requesting connection in state %@ to %@"
- "Resetting connection to %@"
- "Scanning LEA 3"
- "Scanning MFi"
- "Setting boost %@"
- "Should relinquish %d, %d, %d, %d"
- "Skipping pairing because not a hearing device %@"
- "Stopping Updates"
- "T@\"AVAudioEngine\",&,N,V_engine"
- "UPDATING %@ - %@"
- "Unexpected message ID: %@"
- "Unpairing [%d] %@"
- "Unregister from available devices listener: %@"
- "Unregister from property update listener: %@"
- "Unregister from updates listenerHash: %@"
- "Update Paired %@ Connected %@"
- "Will shutdown, save IDS stats"
- "Wrist orientation changed %@"
- "Writing %d for %@ - %@"
- "Wrong number of paired devices %@"
- "XPC sending messagesPriority: Default"
- "XPC sending messagesPriority: Urgent"
- "XPC sending payload %@"
- "[%d] %lld - %@"
- "_leftPowerSouceDictionary"
- "_leftPowerSouceID"
- "heard should be running. Continuing"
- "heard shouldn't be running. Shutting down."
- "heard shouldn't be running. Starting timer"
- "multiDeviceSettingsEnabled"
- "shouldShowHearingProtectionSuggestionForAlertType:"
- "{%d} LEFT [%d, %d] RIGHT [%d, %d]"
- "{%d} LEFT [%d]: (%d, %d, %d, %d) RIGHT [%d]: (%d, %d, %d, %d)"
- "{%d} LEFT [%d]: (%d, %d, %d, %d, %d) RIGHT [%d]: (%d, %d, %d, %d, %d)"

```
