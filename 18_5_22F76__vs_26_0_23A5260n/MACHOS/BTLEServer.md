## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-345.1.0.0.0
-  __TEXT.__text: 0x740a4
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_stubs: 0xbf60
-  __TEXT.__objc_methlist: 0x6e0c
-  __TEXT.__const: 0x518
-  __TEXT.__cstring: 0x3152
-  __TEXT.__objc_methname: 0x11089
-  __TEXT.__oslogstring: 0xb840
-  __TEXT.__objc_classname: 0x7f0
-  __TEXT.__objc_methtype: 0x2e42
-  __TEXT.__gcc_except_tab: 0xdfc
-  __TEXT.__dlopen_cstrs: 0x13e
+350.33.1.1.0
+  __TEXT.__text: 0x7a848
+  __TEXT.__auth_stubs: 0x10b0
+  __TEXT.__objc_stubs: 0xc7a0
+  __TEXT.__objc_methlist: 0x747c
+  __TEXT.__const: 0x598
+  __TEXT.__cstring: 0x3450
+  __TEXT.__objc_methname: 0x12587
+  __TEXT.__oslogstring: 0xc28c
+  __TEXT.__objc_classname: 0x8ba
+  __TEXT.__objc_methtype: 0x306d
+  __TEXT.__gcc_except_tab: 0xf10
+  __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x17b8
-  __DATA_CONST.__auth_got: 0x850
-  __DATA_CONST.__got: 0x8a8
+  __TEXT.__unwind_info: 0x18c8
+  __DATA_CONST.__auth_got: 0x868
+  __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x15a0
-  __DATA_CONST.__cfstring: 0x4820
-  __DATA_CONST.__objc_classlist: 0x270
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0xb0
+  __DATA_CONST.__const: 0x1660
+  __DATA_CONST.__cfstring: 0x4b00
+  __DATA_CONST.__objc_classlist: 0x298
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x238
-  __DATA_CONST.__objc_intobj: 0x5e8
-  __DATA_CONST.__objc_arraydata: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_intobj: 0x600
+  __DATA_CONST.__objc_arraydata: 0x1c0
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xdd00
-  __DATA.__objc_selrefs: 0x3c68
-  __DATA.__objc_ivar: 0x758
-  __DATA.__objc_data: 0x1860
-  __DATA.__data: 0x848
-  __DATA.__bss: 0x1a8
+  __DATA.__objc_const: 0xedf8
+  __DATA.__objc_selrefs: 0x3fe8
+  __DATA.__objc_ivar: 0x7cc
+  __DATA.__objc_data: 0x19f0
+  __DATA.__data: 0x990
+  __DATA.__bss: 0x1b8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
   - /System/Library/PrivateFrameworks/HID.framework/HID
+  - /System/Library/PrivateFrameworks/HealthLEHeartRate.framework/HealthLEHeartRate
   - /System/Library/PrivateFrameworks/IAPAuthentication.framework/IAPAuthentication
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9F4F646C-84BC-3404-8B3A-3F6C62D0A76B
-  Functions: 2740
-  Symbols:   544
-  CStrings:  5302
+  UUID: E167429B-9BFE-3261-89D9-E737466C7140
+  Functions: 2876
+  Symbols:   564
+  CStrings:  5621
 
Symbols:
+ _CBConnectPeripheralOptionLESynchronizationEvents
+ _CBUUIDAccessoryAttributesCharacteristicString
+ _CBUUIDAccessoryTypeCharacteristicString
+ _CBUUIDBatteryLevelLeftCharacteristicString
+ _CBUUIDBatteryLevelMainCharacteristicString
+ _CBUUIDBatteryLevelRightCharacteristicString
+ _CBUUIDCharacteristicFormatString
+ _CBUUIDCommandCharacteristicString
+ _CBUUIDMFiServiceString
+ _CBUUIDProtocolStringCharacteristicString
+ _CBUUIDTeamIDCharacteristicString
+ _CUPrintFlags32
+ _NSAppendPrintF_safe
+ _OBJC_CLASS_$_CBCharacteristic
+ _OBJC_CLASS_$_CBDescriptor
+ _kACCProperties_Endpoint_MFi_AccessoryAttributes_TLV
+ _kACCProperties_Endpoint_MFi_AccessoryTypes_TLV
+ _kACCProperties_Endpoint_MFi_AppMatch_ProtocolStrings_TLV
+ _kACCProperties_Endpoint_MFi_AppMatch_TeamIDs_TLV
+ _objc_release_x2
CStrings:
+ "\r"
+ "\"%@\" (0x%04X): %@"
+ "\"%@\" retry attempts (limit %d) %@"
+ "## Invalid value received from \"%@\", trying again: %@"
+ "### BatteryLevelStatus failed to convert data to ptr: %@"
+ "### BatteryLevelStatus ptr is invalid %p with data: %@"
+ "### Failed to extract battery level for peripheral \"%@\" (0x%04X): %@"
+ ", AdSt %@"
+ ", CFR %@"
+ ", ID 0x%04X"
+ ", Level %s"
+ ", Level %u%%"
+ ", SF %@"
+ ", State %s"
+ ", Type %s"
+ ", Wired %s"
+ ", Wireless %s"
+ "."
+ "2BED"
+ "?"
+ "@\"BatteryLevelStatusPowerState\""
+ "@\"CBPairingAgent\""
+ "@\"HIDSingleReportDevice\""
+ "@\"HLEHeartRateCollectionObserver\""
+ "@24@0:8r*16"
+ "Added DI Read complete listener:%@ to list %@"
+ "Adding DI Read complete listener:%@ to list %@"
+ "Allowing GATT HRM for FWV %li"
+ "ApplePencilGen"
+ "AuthStatusDidChange for connectionUUID %@ %s"
+ "B24@0:8@?16"
+ "BAS"
+ "Battery Service device '%@' has _CATT_ tag, registering services"
+ "Battery level for peripheral \"%@\" (0x%04X): %u%%"
+ "BatteryClientService started for '%@' with services: %@"
+ "BatteryLevelStatus"
+ "BatteryLevelStatus %@"
+ "BatteryLevelStatusPowerState"
+ "BatteryServiceNotification"
+ "BlockCATTHRM"
+ "Blocking GATT HRM for FWV %li"
+ "CATT Peripheral \"%@\" is now connected"
+ "CBPairingAgentDelegate"
+ "Cannot set up HRMService HID device: Update health disabled"
+ "Central %@ ancsAuthorization changed to %d, interestedCategory %x"
+ "Central %@ subscribed to NotificationSourceCharacteristic, interestedCategory %x"
+ "Connecting peripheral \"%@\" with state %ld and options %@..."
+ "ConnectionRetryCount"
+ "ConstantCurrent"
+ "ConstantVoltage"
+ "Couldn't find matching peripheral"
+ "Creating accTransportClient connection for identifier %@ and connectionUUID %@"
+ "Creating accTransportClient endpoint for auth with type %@"
+ "Creating accTransportClient endpoint for generic MFi"
+ "Critical"
+ "DA_ASK_RETAIN_DEVICE"
+ "DIClientServiceListener"
+ "DeviceInfo received: %@"
+ "DeviceInformation for “%@” read complete for HRM"
+ "DischargingActive"
+ "DischargingInactive"
+ "Disconnecting Peripheral \"%@\" as it is not in list of Peripherals to connect."
+ "DisconnectionReason"
+ "Drop summary update to avoid duplicate notification"
+ "DurationSinceLastSuccessConnectionInSecs"
+ "Fitness Classic device FW revision: %@, components:\u00a0%@"
+ "FitnessDeviceManager should collect heart rate: %@, already collecting: %@"
+ "FitnessService %@ (%@) starting for “%@” PID:0x%04X VID:0x%04X"
+ "FitnessService %@ (%@) stopping for “%@”"
+ "FitnessService - DeviceInformation ClientService not available for “%@”"
+ "FitnessService - allServicesAvailable"
+ "Float"
+ "Good"
+ "Group Identifier"
+ "HIDDeviceAccessEntitlement"
+ "HIDServiceAccessEntitlement"
+ "HLEHeartRateCollectionObserver"
+ "HLEHeartRateCollectionObserverDelegate"
+ "HRMService HID Device created with properties:%@"
+ "HRMService HID device already exists"
+ "HRMService HID device did start"
+ "HRMService HID device did stop"
+ "HRMService refreshUpdateHealthEnabledStatus: starting HRM"
+ "HRMService stopping HID"
+ "HealthDaemon"
+ "HeartRateCoordinator"
+ "Low"
+ "MFi-Generic"
+ "MFi4"
+ "MFiAccessoryConnection"
+ "MFiClientService"
+ "Missing major string of FW revision"
+ "No"
+ "Not Fitness Classic Device"
+ "Not tracking this peripheral"
+ "Opening L2CAP auth channel to \"%@\""
+ "Part Identifier"
+ "Performing MFI Auth for CBPeripheral UUID %@"
+ "Peripheral \"%@\" is in the connectAlwaysIdentifiersMap."
+ "Present %s"
+ "Registered Fitness callback with HeartRateCoordinator for %@"
+ "Registering service %@ (%@) for:“%@”"
+ "Removed DI Read complete listener:%@ from list %@"
+ "Removing DI Read complete listener:%@ from list %@"
+ "S24@0:8@16"
+ "Sending data to Generic Endpoint with type %@"
+ "Setting up HRMService HID device"
+ "T@\"BatteryLevelStatusPowerState\",C,N,V_powerState"
+ "T@\"CBCharacteristic\",&,N,V_accessoryAttributesCharacteristic"
+ "T@\"CBCharacteristic\",&,N,V_accessoryTypeCharacteristic"
+ "T@\"CBCharacteristic\",&,N,V_batteryLevelStatusCharacteristic"
+ "T@\"CBCharacteristic\",&,N,V_commandCharacteristic"
+ "T@\"CBCharacteristic\",&,N,V_protocolStringCharacteristic"
+ "T@\"CBCharacteristic\",&,N,V_teamIDCharacteristic"
+ "T@\"CBPairingAgent\",&,N,V_pairingAgent"
+ "T@\"HIDSingleReportDevice\",&,N,V_hidBluetoothDevice"
+ "T@\"HLEHeartRateCollectionObserver\",&,N,V_heartRateCollectionObserver"
+ "T@\"NSArray\",&,N,V_readCompleteListeners"
+ "T@\"NSArray\",&,N,V_unreadCharacteristics"
+ "T@\"NSArray\",&,V_hkActiveDataCollectionObserverKnownQuantityTypes"
+ "T@\"NSArray\",&,V_hleHeartRateCollectionObserverKnownQuantityTypes"
+ "T@\"NSMutableDictionary\",&,N,V_accessoryConnectionMap"
+ "T@\"NSMutableDictionary\",&,N,V_activeCentralsInterestedCategories"
+ "T@\"NSSet\",&,N,V_connectOptionsAllowableOnConnectedPeripherals"
+ "T@\"NSString\",R,N,V_connectionUUID"
+ "T@\"NSString\",R,N,V_endpointUUID"
+ "T@\"NSString\",R,N,V_genericMFiEndpointUUID"
+ "TB,N,V_batteryPresent"
+ "TC,N,V_additionalFlags"
+ "TC,N,V_batteryChargeLevel"
+ "TC,N,V_batteryChargeState"
+ "TC,N,V_batteryChargeType"
+ "TC,N,V_batteryLevel"
+ "TC,N,V_chargingFaultReason"
+ "TC,N,V_externalPowerSourceWired"
+ "TC,N,V_externalPowerSourceWireless"
+ "TC,N,V_statusFlags"
+ "TS,N,V_batteryLevelCharacteristicFormat"
+ "TS,N,V_identifier"
+ "Tearing down MFiAccessoryConnection for connectionUUID %@"
+ "Tearing down peer channel for connectionUUID %@"
+ "Trickle"
+ "Unregistering service %@ (%@) for: “%@”"
+ "Updated HKDevice name:“%@” manufacturer:“%@” model:“%@” HW:“%@” SW:“%@” FW:“%@” localID:“%@”"
+ "UserDefaultsOverrides"
+ "Yes"
+ "_CATT_"
+ "_UARP_"
+ "_accessoryAttributesCharacteristic"
+ "_accessoryConnectionMap"
+ "_accessoryTypeCharacteristic"
+ "_activeCentralsInterestedCategories"
+ "_additionalFlags"
+ "_batteryChargeLevel"
+ "_batteryChargeState"
+ "_batteryChargeType"
+ "_batteryLevel"
+ "_batteryLevelCharacteristicFormat"
+ "_batteryLevelStatusCharacteristic"
+ "_batteryPresent"
+ "_chargingFaultReason"
+ "_commandCharacteristic"
+ "_connectOptionsAllowableOnConnectedPeripherals"
+ "_externalPowerSourceWired"
+ "_externalPowerSourceWireless"
+ "_genericMFiEndpointUUID"
+ "_handleValueForDescriptor:"
+ "_heartRateCollectionObserver"
+ "_hidBluetoothDevice"
+ "_hkActiveDataCollectionObserverKnownQuantityTypes"
+ "_hleHeartRateCollectionObserverKnownQuantityTypes"
+ "_pairingAgent"
+ "_powerState"
+ "_protocolStringCharacteristic"
+ "_readCompleteListeners"
+ "_requireDescriptor"
+ "_retryAttemptsMap"
+ "_setBatteryLevelCharacteristicFormatFrom:"
+ "_setSoftwareVersion:"
+ "_statusFlags"
+ "_teamIDCharacteristic"
+ "_unreadCharacteristics"
+ "_validData:"
+ "accClientPropertyStringFromCharacteristicString:"
+ "accConnTypeToString:"
+ "accessoryAttributesCharacteristic"
+ "accessoryConnectionMap"
+ "accessoryTypeCharacteristic"
+ "activateAuthEndpointWithType:andChannel:"
+ "activateConnectionWithIdentifier:"
+ "activateGenericEndpoint"
+ "activeCentralsInterestedCategories"
+ "addReadCompleteListener:"
+ "additionalFlags"
+ "appendToArrayProperty:values:forEndpointWithUUID:"
+ "arrayByAddingObjectsFromArray:"
+ "batteryChargeLevel"
+ "batteryChargeState"
+ "batteryChargeType"
+ "batteryLevel"
+ "batteryLevelCharacteristicFormat"
+ "batteryLevelStatusCharacteristic"
+ "batteryPresent"
+ "batteryServiceDeviceConnected:"
+ "cancelPeripheralConnection:"
+ "centralManager:didUpdateSynchronizationEventForPeripheral:results:"
+ "characteristicFormatFrom:"
+ "chargingFaultReason"
+ "com.apple.Bluetooth.PencilReconnectionFailures"
+ "com.apple.hid.heartrate-access"
+ "com.starkey."
+ "commandCharacteristic"
+ "connectOptionsAllowableOnConnectedPeripherals"
+ "createAuthEndpointWithType:channel:"
+ "deactivate"
+ "deviceInformation:readCompleteForDeviceUUID:"
+ "externalPowerSourceWired"
+ "externalPowerSourceWireless"
+ "extractBatteryLevelStatus"
+ "genericMFiEndpointUUID"
+ "getTags"
+ "handleCATTBatteryServiceDeviceConnectedMsg:"
+ "handleEvent - NSStreamEventEndEncountered"
+ "handleEvent - NSStreamEventErrorOccurred: %@"
+ "handleEvent - NSStreamEventHasBytesAvailable"
+ "haveAllCharacteristicsBeenRead"
+ "heartRateCollectionObserver"
+ "heartRateCollectionObserver:didChangeShouldCollectHeartRate:"
+ "hidBluetoothDevice"
+ "hkActiveDataCollectionObserverKnownQuantityTypes"
+ "hleHeartRateCollectionObserverKnownQuantityTypes"
+ "iAP2"
+ "incoming data with size %ld read : %@"
+ "initWithPtr:"
+ "integerValue"
+ "intersectsSet:"
+ "isZeroValue"
+ "kBTHRMManualConnectionKey"
+ "needsMFiAuthenticationCertClass2.0c"
+ "none"
+ "pairing failed with peer %@ error %@, disconnecting"
+ "pairingAgent"
+ "pairingAgent:peerDidCompletePairing:"
+ "pairingAgent:peerDidFailToCompletePairing:error:"
+ "pairingAgent:peerDidRequestPairing:type:passkey:"
+ "pairingAgent:peerDidUnpair:"
+ "peerDidCompletePairing"
+ "peerDidFailToCompletePairing %@ error %@"
+ "peerDidUnpair"
+ "peripheralForConnectionUUID:"
+ "peripheralToAddressString:"
+ "powerState"
+ "protocolStringCharacteristic"
+ "quantityTypesForIdentifiers:"
+ "queryCompleteForAccessory:boardID:error:"
+ "queryCompleteForAccessory:chipID:error:"
+ "queryCompleteForAccessory:chipRevision:error:"
+ "queryCompleteForAccessory:ecid:error:"
+ "queryCompleteForAccessory:enableMixMatch:error:"
+ "queryCompleteForAccessory:epoch:error:"
+ "queryCompleteForAccessory:liveNonce:error:"
+ "queryCompleteForAccessory:manifestPrefix:error:"
+ "queryCompleteForAccessory:nonceHash:error:"
+ "queryCompleteForAccessory:nonceSeed:error:"
+ "queryCompleteForAccessory:productionMode:error:"
+ "queryCompleteForAccessory:securityDomain:error:"
+ "queryCompleteForAccessory:securityMode:error:"
+ "readCompleteListeners"
+ "registerWithHealthKit - Missing HealthLEHeartRate framework"
+ "removeReadCompleteListener:"
+ "retrievePeripheralsWithIdentifiers:completion:"
+ "sendBatteryServiceNotification %@"
+ "sendBatteryServiceNotification:"
+ "sendDataToGenericEndpoint:withProperty:"
+ "setAccessoryAttributesCharacteristic:"
+ "setAccessoryConnectionMap:"
+ "setAccessoryTypeCharacteristic:"
+ "setActiveCentralsInterestedCategories:"
+ "setAdditionalFlags:"
+ "setAuthenticated"
+ "setBatteryChargeLevel:"
+ "setBatteryChargeState:"
+ "setBatteryChargeType:"
+ "setBatteryLevel:"
+ "setBatteryLevelCharacteristicFormat:"
+ "setBatteryLevelStatusCharacteristic:"
+ "setBatteryPresent:"
+ "setChargingFaultReason:"
+ "setCommandCharacteristic:"
+ "setConnectOptionsAllowableOnConnectedPeripherals:"
+ "setDictionary:"
+ "setExternalPowerSourceWired:"
+ "setExternalPowerSourceWireless:"
+ "setHeartRateCollectionObserver:"
+ "setHidBluetoothDevice:"
+ "setHkActiveDataCollectionObserverKnownQuantityTypes:"
+ "setHleHeartRateCollectionObserverKnownQuantityTypes:"
+ "setIAPProperty:withValue:forPeripheral:"
+ "setPairingAgent:"
+ "setPowerState:"
+ "setProtocolStringCharacteristic:"
+ "setReadCompleteListeners:"
+ "setStatusFlags:"
+ "setTeamIDCharacteristic:"
+ "setUnreadCharacteristics:"
+ "setUpPeerChannel:"
+ "setupHIDBluetoothDevice"
+ "setupKnownQuantityTypes"
+ "softlink:o:path:/System/Library/Frameworks/HealthLEHeartRate.framework/HealthLEHeartRate"
+ "softwareVersion"
+ "statusFlags"
+ "teamIDCharacteristic"
+ "tearDownPeerChannel"
+ "threadSummary"
+ "unreadCharacteristics"
+ "untag:"
+ "v28@0:8@\"HLEHeartRateCollectionObserver\"16B24"
+ "v28@0:8C16@20"
+ "v32@0:8@\"CBPairingAgent\"16@\"CBPeer\"24"
+ "v32@0:8@\"DIClientService\"16@\"NSString\"24"
+ "v36@0:8@\"UARPAccessory\"16B24@\"NSError\"28"
+ "v40@0:8@\"CBPairingAgent\"16@\"CBPeer\"24@\"NSError\"32"
+ "v40@0:8@\"UARPAccessory\"16@\"NSData\"24@\"NSError\"32"
+ "v40@0:8@\"UARPAccessory\"16Q24@\"NSError\"32"
+ "v40@0:8@16Q24@32"
+ "v48@0:8@\"CBPairingAgent\"16@\"CBPeer\"24q32@\"NSNumber\"40"
+ "v48@0:8@16@24q32@40"
- "AuthStatusDidChange %@ %s"
- "B222"
- "B332"
- "B482"
- "B532"
- "Battery level for peripheral \"%@\": %u%%"
- "Central %@ subscribed to NotificationSourceCharacteristic"
- "FitnessService starting for “%@” PID:0x%04X VID:0x%04X"
- "FitnessService stopping for “%@”"
- "L2CAPChannels"
- "NSStreamEventEndEncountered"
- "NSStreamEventErrorOccurred : %@. Teardown auth"
- "NSStreamEventHasBytesAvailable"
- "Not tracking an Mfi peripheral"
- "Perform MFIAuth for %@"
- "Perform mfi auth for \"%@\"..."
- "Registering service %@ for:“%@”"
- "T@\"CBL2CAPChannel\",&,N,V_mfiAuthChannel"
- "T@\"CBPeripheral\",&,N,V_mfiPeripheral"
- "T@\"NSMutableArray\",&,N,V_L2CAPChannels"
- "T@\"NSString\",&,N,V_endpointUUID"
- "Unregistering service %@ for peripheral: %@"
- "_L2CAPChannels"
- "_mfiAuthChannel"
- "_mfiPeripheral"
- "data with size %ld read : %@"
- "mfiAuthChannel"
- "mfiPeripheral"
- "setEndpointUUID:"
- "setL2CAPChannels:"
- "setMfiAuthChannel:"
- "setMfiPeripheral:"

```
