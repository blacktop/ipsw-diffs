## USBHost

> `/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`

```diff

-898.2.3.0.0
-  __TEXT.__text: 0x1f37c
-  __TEXT.__auth_stubs: 0xa20
+898.42.3.0.0
+  __TEXT.__text: 0x1faf0
+  __TEXT.__auth_stubs: 0xa30
   __TEXT.__objc_methlist: 0xf50
-  __TEXT.__oslogstring: 0x2c87
-  __TEXT.__cstring: 0x15af
-  __TEXT.__gcc_except_tab: 0x348
+  __TEXT.__oslogstring: 0x2dca
+  __TEXT.__cstring: 0x15ff
+  __TEXT.__gcc_except_tab: 0x354
   __TEXT.__const: 0x80
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__unwind_info: 0x4c4
   __TEXT.__objc_classname: 0x1ec
   __TEXT.__objc_methname: 0x31d0
   __TEXT.__objc_methtype: 0x777
   __TEXT.__objc_stubs: 0x2060
-  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x7a0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1fd0
   __DATA_CONST.__objc_selrefs: 0xa50
-  __AUTH_CONST.__cfstring: 0x1240
+  __AUTH_CONST.__cfstring: 0x1260
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__objc_const: 0x5e8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x520
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH.__objc_data: 0x320
   __DATA.__objc_classrefs: 0xe0
   __DATA.__objc_superrefs: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 740
-  Symbols:   2405
-  CStrings:  1134
+  Functions: 742
+  Symbols:   2414
+  CStrings:  1144
 
Symbols:
+ _CFStringCreateWithCString
+ ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.61
+ ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.61.cold.1
+ ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.65
+ ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.65.cold.1
+ ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.65.cold.2
+ ___54-[AccessoryTransportPluginUSBHost VIDPIDServiceAdded:]_block_invoke.82
+ ___76-[AccessoryTransportPluginUSBHost unlockUSBHostInterfacesForConnectionUUID:]_block_invoke.75
+ ___90-[AccessoryTransportPluginUSBHost _handleOpenEASessionNotificationForEndpoint:connection:]_block_invoke.67
+ ___90-[AccessoryTransportPluginUSBHost _handleOpenEASessionNotificationForEndpoint:connection:]_block_invoke.67.cold.1
+ _kACCInfo_ProductID
+ _kACCInfo_VendorID
+ _kACCProperties_Connection_AdapterPID
+ _kACCProperties_Connection_AdapterVID
+ _kACCProperties_Connection_ManagerParent
+ _usbUtil_findParentOfClass
+ _usbUtil_findParentOfClass.cold.1
+ _usbUtil_findParentOfClass.cold.2
+ _usbUtil_findParentOfClass.cold.3
- -[AccessoryIAPInterface configureInterface:skipPipeSetup:].cold.35
- -[AccessoryIAPInterface configureInterface:skipPipeSetup:].cold.36
- ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.55
- ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.55.cold.1
- ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.59
- ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.59.cold.1
- ___48-[AccessoryTransportPluginUSBHost serviceAdded:]_block_invoke.59.cold.2
- ___54-[AccessoryTransportPluginUSBHost VIDPIDServiceAdded:]_block_invoke.76
- ___76-[AccessoryTransportPluginUSBHost unlockUSBHostInterfacesForConnectionUUID:]_block_invoke.69
- ___90-[AccessoryTransportPluginUSBHost _handleOpenEASessionNotificationForEndpoint:connection:]_block_invoke.61
- ___90-[AccessoryTransportPluginUSBHost _handleOpenEASessionNotificationForEndpoint:connection:]_block_invoke.61.cold.1
CStrings:
+ "%s:%d Found match for %s!"
+ "%s:%d Looking for match for %s in plane %s"
+ "%s:%d parent %d after Looking for match for %s in plane %s"
+ "%s:%d service %d, name '%s', vid / pid = 0x%x / 0x%x, override adapterVID/PID, newProperties = %@"
+ "%s:%d service %d, name '%s', vid / pid = 0x%x / 0x%x, override managerParent, newProperties = %@"
+ "Description"
+ "IOAccessoryManager"
+ "IOPort"
+ "IOUSBHostDevice"
+ "usbUtil_findParentOfClass"

```
