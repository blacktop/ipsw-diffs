## deviceaccessd

> `/usr/libexec/deviceaccessd`

```diff

-313.1.0.0.0
-  __TEXT.__text: 0x24df0
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_stubs: 0x3700
-  __TEXT.__objc_methlist: 0xd50
+314.11.0.0.0
+  __TEXT.__text: 0x2659c
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_stubs: 0x3780
+  __TEXT.__objc_methlist: 0x10c4
   __TEXT.__const: 0x38
-  __TEXT.__gcc_except_tab: 0x1964
-  __TEXT.__cstring: 0x817b
-  __TEXT.__objc_classname: 0x15d
-  __TEXT.__objc_methname: 0x3d47
-  __TEXT.__objc_methtype: 0xa07
-  __TEXT.__unwind_info: 0x650
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__cfstring: 0xe80
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__gcc_except_tab: 0x19a0
+  __TEXT.__cstring: 0x818a
+  __TEXT.__objc_classname: 0x12a
+  __TEXT.__objc_methname: 0x3d25
+  __TEXT.__objc_methtype: 0x99a
+  __TEXT.__unwind_info: 0x838
+  __DATA_CONST.__auth_got: 0x648
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0xd18
+  __DATA_CONST.__cfstring: 0xe20
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x2090
-  __DATA.__objc_selrefs: 0xf28
-  __DATA.__objc_ivar: 0x180
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x5b0
+  __DATA.__objc_const: 0x1738
+  __DATA.__objc_selrefs: 0x1108
+  __DATA.__objc_ivar: 0x178
+  __DATA.__objc_data: 0x280
+  __DATA.__data: 0x490
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 413
+  Functions: 654
   Symbols:   295
-  CStrings:  1716
+  CStrings:  1698
 
Symbols:
+ _CBAdvertisementDataLocalNameKey
+ _CBCentralManagerScanOptionMatchingRuleNameNSStringCompareOptions
+ _OBJC_CLASS_$_DAPartialIP
- _CUXPCDecodeNSData
- _strcmp
- _xpc_dictionary_set_data
CStrings:
+ "\x02\x11\x12\x13\xea\x13"
+ "### Found device with SSID %@ for DADevice %@"
+ "### _findDeviceWithSSID looking for device %@ associated with %@"
+ "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:]"
+ "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:completion:]"
+ "-[DADaemonServer _findExistingDeviceWithSSID:bundleID:]"
+ "-[DADaemonServer _findExistingDeviceWithSSID:bundleID:]_block_invoke"
+ "ASK_ALLOW_HID"
+ "Get error %@ from nw connection with state: %u!"
+ "Get nw connection state %u"
+ "S24@0:8@16"
+ "TB,N,V_supportsHID"
+ "Unpairing btuuid %@ task %@, because accessory does not support HID servie despite app claimed it to."
+ "_HID_DEVICE_"
+ "_addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:"
+ "_findExistingDeviceWithSSID:bundleID:"
+ "_getAdvName:"
+ "_getAppearance:"
+ "_supportsHID"
+ "kCBAdvDataAppearance"
+ "persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:supportsHID:completion:"
+ "setBluetoothAppearance:"
+ "setSupportsHID:"
+ "supportsHID"
+ "unsignedShortValue"
+ "v64@0:8@16B24B28@32@40B48B52@?56"
+ "v68@0:8@16@?24q32B40@44@52B60B64"
- "\x02"
- "\x02\x11\x12\x13\xfa\x13"
- "%@ super init failed"
- "-V"
- "-[DABluetoothPairingManager _addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:]"
- "-[DABluetoothPairingManager persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:completion:]"
- "@\"NSData\""
- "@24@0:8@\"NSCoder\"16"
- "@32@0:8@\"NSObject<OS_xpc_object>\"16^@24"
- "ASK_LINKED_RADIO_ADDRESS"
- "BluetoothTransportBridgingTimeoutSeconds: %f -> %f"
- "CUXPCCodable"
- "DAPartialIP"
- "Error updating device with bridging flag: appID %@, %@"
- "Get error %@ from nw connection with state: %d!"
- "Get nw connection state %d"
- "NSCoding"
- "NSSecureCoding"
- "Sign data length mismatch"
- "T@\"NSData\",R,C,N,V_address"
- "T@\"NSData\",R,C,N,V_mask"
- "TB,R"
- "_addNewTask:completion:bluetoothOp:pairCTKD:displayName:taskTimeout:appConfirmsAuth:"
- "_address"
- "_checkAppAccessInfoExpired: found CBPeripheral, %@ awaitingTransportBridging %d"
- "_mask"
- "_prefsBluetoothTransportBridgingTimeoutSeconds"
- "addr: %@, mask: %@"
- "bluetoothTransportBridgingTimeoutSeconds"
- "customProperty:"
- "decodeObjectForKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "initWithCoder:"
- "ipAd"
- "ipMa"
- "kCBScanOptionFilterNameMatchNSStringCompareOptions"
- "persistBluetoothDevice:pairingRequired:pairWithCTKD:displayName:taskTimeout:appConfirmsAuth:completion:"
- "supportsSecureCoding"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSObject<OS_xpc_object>\"16"
- "v60@0:8@16B24B28@32@40B48@?52"
- "v64@0:8@16@?24q32B40@44@52B60"

```
