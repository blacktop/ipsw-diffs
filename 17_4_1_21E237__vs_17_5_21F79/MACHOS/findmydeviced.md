## findmydeviced

> `/usr/libexec/findmydeviced`

```diff

-423.5.0.0.0
-  __TEXT.__text: 0x2387e0
+424.6.0.0.0
+  __TEXT.__text: 0x23a5ec
   __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x162c0
-  __TEXT.__objc_methlist: 0xdcc8
+  __TEXT.__objc_stubs: 0x164a0
+  __TEXT.__objc_methlist: 0xdfa0
   __TEXT.__const: 0x2e1f0
   __TEXT.__gcc_except_tab: 0x1f0c
-  __TEXT.__objc_methname: 0x1bbfb
-  __TEXT.__oslogstring: 0x105b1
-  __TEXT.__cstring: 0x879a
-  __TEXT.__objc_classname: 0x1a32
-  __TEXT.__objc_methtype: 0x2fb1
-  __TEXT.__unwind_info: 0x3214
+  __TEXT.__objc_methname: 0x1bfad
+  __TEXT.__oslogstring: 0x106a3
+  __TEXT.__cstring: 0x87c6
+  __TEXT.__objc_classname: 0x1a57
+  __TEXT.__objc_methtype: 0x3007
+  __TEXT.__unwind_info: 0x326c
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x708
   __DATA_CONST.__got: 0x498
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xc988
-  __DATA_CONST.__cfstring: 0xa560
-  __DATA_CONST.__objc_classlist: 0x6b0
+  __DATA_CONST.__const: 0xc9a8
+  __DATA_CONST.__cfstring: 0xa5e0
+  __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_classrefs: 0xa68
-  __DATA_CONST.__objc_superrefs: 0x550
-  __DATA_CONST.__objc_intobj: 0x468
+  __DATA_CONST.__objc_classrefs: 0xa70
+  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_intobj: 0x480
   __DATA_CONST.__objc_doubleobj: 0x5a0
   __DATA_CONST.__objc_arraydata: 0x5f8
   __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_floatobj: 0x30
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0x1bbc0
-  __DATA.__objc_selrefs: 0x63c8
-  __DATA.__objc_ivar: 0x1050
-  __DATA.__objc_data: 0x42e0
+  __DATA.__objc_const: 0x1c090
+  __DATA.__objc_selrefs: 0x6460
+  __DATA.__objc_ivar: 0x1098
+  __DATA.__objc_data: 0x4330
   __DATA.__data: 0x2480
   __DATA.__bss: 0x7c0
   __DATA.__common: 0x74

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5C3B710F-8CB4-36B7-97A0-7DF26A3DB753
-  Functions: 5876
+  UUID: 70EA0879-F444-3D76-BD8E-8F5EF051BBE8
+  Functions: 5935
   Symbols:   568
-  CStrings:  9677
+  CStrings:  9734
 
CStrings:
+ "\x1f\x01"
+ "0_0"
+ "@\"FMDLocalFindableAccessory\""
+ "DAEMON API - didAddLocalFindableAccessory"
+ "DAEMON API - didRemoveLocalFindableAccessory"
+ "FMDInternalLocalFindableAccessory"
+ "Now Registering Accessory - %@"
+ "Now Unregistering Accessory - %@"
+ "T@\"FMDCommandContext\",R,N,VcommandContext"
+ "T@\"FMDLocalFindableAccessory\",&,N,V_localFindableAccessory"
+ "T@\"NSData\",&,N,V_irkData"
+ "T@\"NSString\",&,N,V_bluetoothColorCode"
+ "T@\"NSString\",C,N,V_alternateSerialNumber"
+ "T@\"NSString\",C,N,V_btAddress"
+ "T@\"NSString\",C,N,V_firmwareVersion"
+ "T@\"NSString\",C,N,V_productId"
+ "T@\"NSString\",C,N,V_serialNumber"
+ "T@\"NSString\",C,N,V_vendorId"
+ "T@\"NSUUID\",&,N,V_identifier"
+ "TB,N,GisConnected,V_connected"
+ "TB,R,N,Vnearby"
+ "_alternateSerialNumber"
+ "_btAddress"
+ "_connected"
+ "_deviceTypeFromVendorId:productId:"
+ "_irkData"
+ "_localFindableAccessory"
+ "_productId"
+ "_vendorId"
+ "accessoryTypesNeedConfig %@"
+ "alternateSerialNumber"
+ "btAddress"
+ "didAddLocalFindableAccessory:completion:"
+ "didRemoveLocalFindableAccessory:completion:"
+ "didVisit %@ %{private}f %{private}f"
+ "initWithLocalFindableAccessory:"
+ "irkData"
+ "isConnected"
+ "localFindableAccessory"
+ "registerAccessory:completion:"
+ "scanHexInt:"
+ "setAlternateSerialNumber:"
+ "setBtAddress:"
+ "setConnected:"
+ "setIrkData:"
+ "setLocalFindableAccessory:"
+ "setProductId:"
+ "setVendorId:"
+ "unregisterAccessory:completion:"
+ "updateAccessoriesDatabase called with context %@"
+ "v32@0:8@\"FMDLocalFindableAccessory\"16@?<v@?@\"NSError\">24"
+ "vendorId = %u productId = %u"
- "didVisit %@ %f %f"
- "updateAccessoriesDatabase called"

```
