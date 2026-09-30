## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-438.24.7.11.24
-  __TEXT.__text: 0x7c9a8
+438.25.2.11.6
+  __TEXT.__text: 0x7cedc
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_stubs: 0xd320
-  __TEXT.__objc_methlist: 0x8644
+  __TEXT.__objc_stubs: 0xd400
+  __TEXT.__objc_methlist: 0x867c
   __TEXT.__const: 0x1e8
-  __TEXT.__gcc_except_tab: 0x19ec
-  __TEXT.__objc_methname: 0x10550
-  __TEXT.__oslogstring: 0x950d
-  __TEXT.__cstring: 0x52d9
-  __TEXT.__objc_classname: 0xf2b
-  __TEXT.__objc_methtype: 0x1f9c
+  __TEXT.__gcc_except_tab: 0x19c8
+  __TEXT.__objc_methname: 0x1062c
+  __TEXT.__oslogstring: 0x9683
+  __TEXT.__cstring: 0x5350
+  __TEXT.__objc_classname: 0xf42
+  __TEXT.__objc_methtype: 0x1ff6
   __TEXT.__ustring: 0x56
-  __TEXT.__unwind_info: 0x1c38
+  __TEXT.__unwind_info: 0x1c50
   __DATA_CONST.__auth_got: 0x728
-  __DATA_CONST.__got: 0x560
-  __DATA_CONST.__const: 0x28b0
-  __DATA_CONST.__cfstring: 0x6b60
-  __DATA_CONST.__objc_classlist: 0x428
+  __DATA_CONST.__got: 0x570
+  __DATA_CONST.__const: 0x2988
+  __DATA_CONST.__cfstring: 0x6bc0
+  __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x2e0
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA_CONST.__objc_intobj: 0x228
+  __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x68
   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_floatobj: 0x30
-  __DATA.__objc_const: 0xde68
-  __DATA.__objc_selrefs: 0x3f90
-  __DATA.__objc_ivar: 0x858
-  __DATA.__objc_data: 0x2990
+  __DATA.__objc_const: 0xdf58
+  __DATA.__objc_selrefs: 0x3fe0
+  __DATA.__objc_ivar: 0x860
+  __DATA.__objc_data: 0x29e0
   __DATA.__data: 0xff8
   __DATA.__bss: 0x470
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
+  - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3235
-  Symbols:   415
-  CStrings:  5168
+  Functions: 3246
+  Symbols:   417
+  CStrings:  5209
 
Symbols:
+ _OBJC_CLASS_$_CBAdvertiser
+ _OBJC_CLASS_$_CBController
CStrings:
+ "\x1b\x12"
+ "0_0"
+ "?"
+ "@\"CBAdvertiser\""
+ "@\"CBController\""
+ "@32@0:8S16I20q24"
+ "@40@0:8S16I20q24@32"
+ "Activate failed: %@"
+ "BluetoothState: %@"
+ "BluetoothStateChangedNotification - new state %s"
+ "Creating shared instance of FMDBLEStateOwner"
+ "FMDSupportedAccessoryRegistry - Cannot verify support if vendorID/productID are 0. Default to unsupported."
+ "FMDSupportedAccessoryRegistry accessory %@ is NOT in the listed of supportedAccessories %@"
+ "FMDSupportedAccessoryRegistry accessory (vendorID: %d, productID: %d) is supported %@"
+ "FMDSupportedAccessoryRegistry initialized %@"
+ "FMDTheftAndLossManager"
+ "Get controller info failed : %@"
+ "New supported accessory added %hu, %u"
+ "PoweredOff"
+ "PoweredOn"
+ "Resetting"
+ "Restricted"
+ "S"
+ "S16@0:8"
+ "T@\"CBAdvertiser\",&,N,V_btAdvertiser"
+ "T@\"CBController\",&,N,V_btController"
+ "TI,N,V_productID"
+ "TI,R,N"
+ "TS,N,V_vendorID"
+ "TS,R,N"
+ "Unauthorized"
+ "Unsupported"
+ "_btAdvertiser"
+ "_btController"
+ "_productID"
+ "_vendorID"
+ "activateWithCompletion:"
+ "bluetoothState"
+ "btAdvertiser"
+ "btController"
+ "decodeIntForKey:"
+ "encodeInt:forKey:"
+ "getControllerInfoWithCompletion:"
+ "initWithVendorID:productID:"
+ "initWithVendorID:productID:profile:"
+ "initWithVendorID:productID:profile:assets:"
+ "off"
+ "on"
+ "productID"
+ "setBluetoothStateChangedHandler:"
+ "setBtAdvertiser:"
+ "setBtController:"
+ "setProductID:"
+ "setVendorID:"
+ "supportedAccessoryForAccessory - accessory (name: %@) addressableAccessory (vendorID: %d, productID: %d)"
+ "v20@0:8S16"
+ "v24@?0@\"CBControllerInfo\"8@\"NSError\"16"
+ "vendorID"
- "\r\x12"
- "FMDSupportedAccessoryRegistry accessory is NOT supported %@"
- "FMDSupportedAccessoryRegistry accessory is supported %@"
- "FMDSupportedAccessoryRegistry initizlied %@"
- "FMDSupportedAccessoryRegistry supportedAccessoryForAccessory %@"
- "New supported accessory added %li, %li"
- "T@\"NSNumber\",&,N,V_deviceProductId"
- "T@\"NSNumber\",&,N,V_deviceVendor"
- "_deviceProductId"
- "_deviceVendor"
- "deviceProductId"
- "deviceVendor"
- "initWithDeviceVendor:deviceProductId:"
- "initWithDeviceVendor:deviceProductId:profile:"
- "initWithDeviceVendor:deviceProductId:profile:assets:"
- "setDeviceProductId:"
- "setDeviceVendor:"

```
