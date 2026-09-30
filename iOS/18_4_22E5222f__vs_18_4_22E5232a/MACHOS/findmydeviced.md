## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.34.7.11.24
-  __TEXT.__text: 0x245530
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_stubs: 0x16a40
-  __TEXT.__objc_methlist: 0xf694
+438.34.7.11.27
+  __TEXT.__text: 0x244874
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_stubs: 0x16940
+  __TEXT.__objc_methlist: 0xf7b4
   __TEXT.__const: 0x2cc50
-  __TEXT.__gcc_except_tab: 0x2b70
-  __TEXT.__objc_methname: 0x1c595
-  __TEXT.__oslogstring: 0x112d8
-  __TEXT.__cstring: 0x8c27
-  __TEXT.__objc_classname: 0x1a62
-  __TEXT.__objc_methtype: 0x30c8
+  __TEXT.__gcc_except_tab: 0x2b80
+  __TEXT.__objc_methname: 0x1c4fe
+  __TEXT.__oslogstring: 0x10ce1
+  __TEXT.__cstring: 0x8b57
+  __TEXT.__objc_classname: 0x1a9c
+  __TEXT.__objc_methtype: 0x30c7
   __TEXT.__constg_swiftt: 0x58
   __TEXT.__swift5_typeref: 0x77
   __TEXT.__swift5_reflstr: 0x8

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x34d8
+  __TEXT.__unwind_info: 0x34b0
   __TEXT.__eh_frame: 0x378
-  __DATA_CONST.__auth_got: 0x848
-  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__auth_got: 0x840
+  __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0xda78
-  __DATA_CONST.__cfstring: 0xa800
+  __DATA_CONST.__const: 0xd988
+  __DATA_CONST.__cfstring: 0xa760
   __DATA_CONST.__objc_classlist: 0x6d0
-  __DATA_CONST.__objc_catlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_catlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x568
-  __DATA_CONST.__objc_intobj: 0x420
+  __DATA_CONST.__objc_intobj: 0x4b0
   __DATA_CONST.__objc_doubleobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x5f8
   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x19c50
-  __DATA.__objc_selrefs: 0x66f8
-  __DATA.__objc_ivar: 0x10d4
+  __DATA.__objc_const: 0x19ee8
+  __DATA.__objc_selrefs: 0x66c8
+  __DATA.__objc_ivar: 0x10cc
   __DATA.__objc_data: 0x44a0
-  __DATA.__data: 0x2498
+  __DATA.__data: 0x2558
   __DATA.__bss: 0x7f0
   __DATA.__common: 0x6c
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
-  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
+  - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP
   - /System/Library/PrivateFrameworks/FMCore.framework/FMCore
   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5995
-  Symbols:   639
-  CStrings:  8581
+  Functions: 5983
+  Symbols:   641
+  CStrings:  8531
 
Symbols:
+ _BluetoothAvailabilityChangedNotification
+ _BluetoothDeviceConnectSuccessNotification
+ _BluetoothDeviceDisconnectSuccessNotification
+ _BluetoothMagicPairedDeviceNameChangedNotification
+ _BluetoothStateChangedNotification
+ _OBJC_CLASS_$_BluetoothDevice
+ _OBJC_CLASS_$_BluetoothManager
- _OBJC_CLASS_$_CBAdvertiser
- _OBJC_CLASS_$_CBConnection
- _OBJC_CLASS_$_CBController
- _OBJC_CLASS_$_CBDiscovery
- _dispatch_queue_attr_make_with_autorelease_frequency
CStrings:
+ "\x01\x17"
+ "\r\x12"
+ "\x1f\t"
+ "$#\x1f\t"
+ "@\"NSObject<FMDBluetoothFrameworkDevice>\""
+ "AACPVersionInfo"
+ "AccessoryPlaySoundAction (0x%lX) attempting to execute after beign terminated T%i"
+ "B32@0:8^i16^i24"
+ "BluetoothAvailabilityChangedNotification"
+ "BluetoothDeviceConnectSuccessNotification ignoring temporary device"
+ "BluetoothDeviceConnectSuccessNotification unexpected object type"
+ "BluetoothDeviceDisconnectSuccessNotification ignoring temporary device"
+ "BluetoothDeviceDisconnectSuccessNotification unexpected object type"
+ "BluetoothMagicPairedDeviceNameChangedNotification ignoring temporary device"
+ "BluetoothMagicPairedDeviceNameChangedNotification unexpected object type"
+ "BluetoothManager addDeviceNotification %@"
+ "BluetoothManager deviceNameChanged %@"
+ "BluetoothManager didDiscoverDevice %@"
+ "BluetoothManager didLoseDevice %@"
+ "BluetoothManager discovery ended - setting all channels inactive."
+ "BluetoothManager discovery started - setting all channels active."
+ "BluetoothManager notifying delegate bluetoothManagerDidConnectDevice %@"
+ "BluetoothManager notifying delegate bluetoothManagerDidDisconnectDevice %@"
+ "BluetoothManager removeDeviceNotification %@"
+ "BluetoothManager setInternalDeviceAudioChannels FMDInternalBluetoothManagerDevice(0x%lX)"
+ "BluetoothManager.pairedDevices Ignoring shared device %@"
+ "BluetoothManager.pairedDevices ignoring temporary device - %@"
+ "BluetoothManager.pairedDevices unexpected object type %@"
+ "BluetoothStateChangedNotification"
+ "FMDAccessory(0x%lx) name - %@, signature - %@, accessoryType - %@, baUUID - %@"
+ "FMDAccessory(0x%lx) name - %@, signature - %@, deviceVendor - %d, deviceProductId - %d, baUUID - %@"
+ "FMDAccessoryRegistry : accessory connected %@"
+ "FMDAccessoryRegistry : accessory disconnected %@"
+ "FMDAccessoryRegistry FMDBluetoothManagerDevice(0x%lX) bluetoothManagerDidUpdateDevice FMDInternalAccessory(0x%lX) %@"
+ "FMDAccessoryRegistry addAccessory %@ New? %i %i"
+ "FMDAccessoryRegistry updateAccessory %@"
+ "FMDAccessorySerialNumbers invalid info. Count: %lu, Values: %@"
+ "FMDBluetoothFrameworkBTManaging"
+ "FMDBluetoothFrameworkDevice"
+ "FMDBluetoothManager initialized"
+ "FMDBluetoothManager starting BluetoothManager %@"
+ "FMDBluetoothManager the BluetoothManager is not available."
+ "FMDSupportedAccessoryRegistry accessory is NOT supported %@"
+ "FMDSupportedAccessoryRegistry accessory is supported %@"
+ "FMDSupportedAccessoryRegistry initizlied %@"
+ "FMDSupportedAccessoryRegistry supportedAccessoryForAccessory %@"
+ "New supported accessory added %li, %li"
+ "Starting to listen for BluetoothState changes"
+ "T@\"NSNumber\",&,N,V_deviceProductId"
+ "T@\"NSNumber\",&,N,V_deviceVendor"
+ "T@\"NSObject<FMDBluetoothFrameworkDevice>\",&,N,V_bluetoothDevice"
+ "TI,N,V_majorDeviceClass"
+ "TI,N,V_minorDeviceClass"
+ "^{BTDeviceImpl=}16@0:8"
+ "_deviceProductId"
+ "_deviceVendor"
+ "_majorDeviceClass"
+ "_minorDeviceClass"
+ "accessoryInfo"
+ "accessoryList = %@"
+ "addDeviceNotification:"
+ "addObserverForName:object:queue:usingBlock:"
+ "bluetoothDeviceProductId"
+ "bluetoothDeviceVendor"
+ "bluetoothMajorDeviceClass"
+ "bluetoothMinorDeviceClass"
+ "com.apple.icloud.findmydeviced.fmdbluetoothmanager.getaccessories"
+ "connect"
+ "connectDevice:"
+ "connectionStatusString"
+ "deviceProductId"
+ "deviceVendor"
+ "enabled"
+ "inEarDetectEnabled"
+ "inEarStatusPrimary:secondary:"
+ "initWithAccessoryInfo:"
+ "initWithDeviceVendor:deviceProductId:"
+ "initWithDeviceVendor:deviceProductId:profile:"
+ "initWithDeviceVendor:deviceProductId:profile:assets:"
+ "majorClass"
+ "majorDeviceClass"
+ "minorClass"
+ "minorDeviceClass"
+ "pairedDevices"
+ "palying sound with connected = %d safe = %d safetyAlertType = %@"
+ "profileForBluetoothManagerDevice:"
+ "removeDeviceNotification:"
+ "serialNumberFromVersionInfo:"
+ "setDeviceProductId:"
+ "setDeviceVendor:"
+ "setMajorDeviceClass:"
+ "setMinorDeviceClass:"
+ "setSharedInstanceQueue:"
+ "supportedAccessory %@ %@"
+ "updateDisccovery"
+ "v16@?0@\"NSNotification\"8"
+ "v24@0:8@\"NSObject<FMDBluetoothFrameworkDevice>\"16"
+ "v32@?0@\"NSObject<FMDBluetoothFrameworkDevice>\"8Q16^B24"
+ "warning safet alert disabled"
- "\x01\x19"
- "\x14!\x1f\t"
- "\x17"
- "\x1b\x12"
- "\x1f\a"
- "%@-tsco"
- "?"
- "@\"CBAdvertiser\""
- "@\"CBController\""
- "@\"CBDevice\""
- "@\"CBDiscovery\""
- "@32@0:8S16I20q24"
- "@40@0:8S16I20q24@32"
- "AccessoryPlaySoundAction (0x%lX) attempting to execute after being terminated T%i"
- "Activate failed: %@"
- "BT is off. Cannot update accessory list."
- "BluetoothDeviceConnectSuccessNotification"
- "BluetoothDeviceDisconnectSuccessNotification"
- "BluetoothMagicPairedDeviceNameChangedNotification"
- "BluetoothStateChangedNotification - new state %s"
- "Check for removed accessories. extAccessory: %@"
- "Check for removed accessories. extensionsAlreadySynced: %@"
- "Check for removed accessories. registry: %@, previouslyPairedAccessories: %@"
- "Could not get the BT power state, timeout error %ld"
- "Creating shared instance of FMDBLEStateOwner"
- "FMDAccessory(0x%lx) name - %@, MAC - %@, accessoryType - %@, baUUID - %@, accessoryIdentifier - %@"
- "FMDAccessory(0x%lx) name - %@, signature - %@, vendorID - %d, productID - %d, baUUID - %@"
- "FMDAccessoryRegistry : accessory name: %@ connected %@"
- "FMDAccessoryRegistry : accessory name: %@ disconnected %@"
- "FMDAccessoryRegistry Received baUUID: %@ for %@, %@"
- "FMDAccessoryRegistry Retrieving baUUID for MAC: %@"
- "FMDAccessoryRegistry addAccessory %@ New - %i PreviouslyPaired - %i"
- "FMDAccessoryRegistry updateAccessory name: %@, connectionState: %{public}@"
- "FMDAccessoryRegistryDelegateAdaptor bluetoothManagerDidUpdateDevice device (name: %@, vendorID: %d, productID: %d)"
- "FMDBluetoothManager FoundHandler - device (%@) with name (%@)"
- "FMDBluetoothManager FoundHandler - ignoring temporary device"
- "FMDBluetoothManager FoundHandler - only BT classic devices are supported, ignoring device"
- "FMDBluetoothManager Ignoring shared device %@"
- "FMDBluetoothManager LostHandler - device (%@) with name (%@)"
- "FMDBluetoothManager LostHandler - ignoring temporary device"
- "FMDBluetoothManager LostHandler - only BT classic devices are supported, ignoring device (%@) with name (%@)"
- "FMDBluetoothManager deviceNameChanged (%@) => (%@)"
- "FMDBluetoothManager did not find any paired devices"
- "FMDBluetoothManager did not find any paired devices\n"
- "FMDBluetoothManager didDiscoverDevice %@"
- "FMDBluetoothManager didLoseDevice %@"
- "FMDBluetoothManager discovery ended - setting all channels inactive."
- "FMDBluetoothManager discovery started - setting all channels active."
- "FMDBluetoothManager failed to connected to paired device: %@\n"
- "FMDBluetoothManager failed to discover paired devices: %@"
- "FMDBluetoothManager failed to discover paired devices: %@\n"
- "FMDBluetoothManager ignoring temporary device - %@"
- "FMDBluetoothManager notifying delegate bluetoothManagerDidConnectDevice %@"
- "FMDBluetoothManager notifying delegate bluetoothManagerDidDisconnectDevice %@"
- "FMDBluetoothManager powered off. Not able to return accessories."
- "FMDBluetoothManager returned (allPairedDevices.count) devices"
- "FMDBluetoothManager setInternalDeviceAudioChannels FMDInternalBluetoothManagerDevice(0x%lX)"
- "FMDExtAccesoryManager"
- "FMDExtAccesoryManager FoundHandler - device (%@) with MAC (%@)"
- "FMDExtAccesoryManager FoundHandler - only BT classic devices are supported, ignoring device"
- "FMDExtAccesoryManager FoundHandler - unhandled device (%@) connectedServices (%x) discoveryFlags (flags %llx)"
- "FMDExtAccesoryManager LostHandler - device (%@) with MAC (%@)"
- "FMDExtAccesoryManager LostHandler - only BT classic devices are supported, ignoring device (%@) with MAC (%@)"
- "FMDExtAccesoryManager deviceNameChanged (%@) => (%@)"
- "FMDExtAccessoryManager.CBDiscovery.SerialQueue"
- "FMDSupportedAccessoryRegistry - Cannot verify support if vendorID/productID are 0. Default to unsupported."
- "FMDSupportedAccessoryRegistry accessory %@ is NOT in the listed of supportedAccessories %@"
- "FMDSupportedAccessoryRegistry accessory (vendorID: %d, productID: %d) is supported %@"
- "FMDSupportedAccessoryRegistry initialized %@"
- "Get controller info failed : %@"
- "Ignore notification. Bailing."
- "New supported accessory added %hu, %u"
- "PoweredOff"
- "PoweredOn"
- "Resetting"
- "Restricted"
- "S"
- "S16@0:8"
- "Starting BT Discovery"
- "Starting BT Discovery failed with error %@"
- "T@\"CBAdvertiser\",&,N,V_btAdvertiser"
- "T@\"CBController\",&,N,V_btController"
- "T@\"CBDevice\",&,N,V_bluetoothDevice"
- "T@\"CBDiscovery\",&,N,V_btDiscovery"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_btDiscoverySerialQueue"
- "TI,N,V_productID"
- "TI,R,N"
- "TS,N,V_vendorID"
- "TS,R,N"
- "UNSUPPORTED"
- "Unauthorized"
- "Unsupported"
- "_btAdvertiser"
- "_btController"
- "_btDiscovery"
- "_btDiscoverySerialQueue"
- "_cbPoweredOff"
- "_productID"
- "_vendorID"
- "activateWithCompletion:"
- "bluetoothState"
- "btAddressData"
- "btAdvertiser"
- "btController"
- "btDiscovery"
- "btDiscoverySerialQueue"
- "connectedServices"
- "connectionStateAsString"
- "decodeIntForKey:"
- "deviceFlags"
- "devicesWithDiscoveryFlags:error:"
- "discoveryFlags"
- "encodeInt:forKey:"
- "ext: Registry %@"
- "getControllerInfoWithCompletion:"
- "initWithDevice:"
- "initWithVendorID:productID:"
- "initWithVendorID:productID:profile:"
- "initWithVendorID:productID:profile:assets:"
- "isAccessorySupported - Accessory (name: %@, baUUID: %@) of category extension is supported"
- "playing sound with connected = %d safe = %d safetyAlertType = %@"
- "productID"
- "profileWithVendorID:productID:"
- "q24@0:8S16I20"
- "serialNumberLeft"
- "serialNumberRight"
- "setBluetoothStateChangedHandler:"
- "setBtAdvertiser:"
- "setBtController:"
- "setBtDiscovery:"
- "setBtDiscoverySerialQueue:"
- "setConnectionFlags:"
- "setDeviceFoundHandler:"
- "setDeviceLostHandler:"
- "setDiscoveryFlags:"
- "setDispatchQueue:"
- "setLabel:"
- "setPeerDevice:"
- "setProductID:"
- "setVendorID:"
- "supportedAccessoryForAccessory - Accessory (productID: %d) of category extension is supported"
- "supportedAccessoryForAccessory - accessory (name: %@) addressableAccessory (vendorID: %d, productID: %d)"
- "updateDiscovery"
- "updateNotificationReceived:withName:"
- "v16@?0@\"CBDevice\"8"
- "v20@0:8S16"
- "v24@?0@\"CBControllerInfo\"8@\"NSError\"16"
- "v32@?0@\"CBDevice\"8Q16^B24"
- "vendorID"
- "warning safety alert disabled"

```
