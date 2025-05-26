## IOAccessoryManager

> `/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`

```diff

-898.2.3.0.0
-  __TEXT.__text: 0x6a870
-  __TEXT.__auth_stubs: 0x1450
-  __TEXT.__objc_methlist: 0x2794
-  __TEXT.__cstring: 0x4d79
-  __TEXT.__oslogstring: 0xb1e7
+898.42.3.0.0
+  __TEXT.__text: 0x6bd68
+  __TEXT.__auth_stubs: 0x1470
+  __TEXT.__objc_methlist: 0x27e4
+  __TEXT.__cstring: 0x4ef3
+  __TEXT.__oslogstring: 0xb304
   __TEXT.__const: 0x124
-  __TEXT.__gcc_except_tab: 0x4e4
+  __TEXT.__gcc_except_tab: 0x504
   __TEXT.__ustring: 0x146
-  __TEXT.__unwind_info: 0xd24
+  __TEXT.__unwind_info: 0xd50
   __TEXT.__objc_classname: 0x471
-  __TEXT.__objc_methname: 0x7c8b
-  __TEXT.__objc_methtype: 0xf77
-  __TEXT.__objc_stubs: 0x5820
-  __DATA_CONST.__got: 0x210
+  __TEXT.__objc_methname: 0x7dc1
+  __TEXT.__objc_methtype: 0xfeb
+  __TEXT.__objc_stubs: 0x58e0
+  __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0xc50
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x46f0
-  __DATA_CONST.__objc_selrefs: 0x1c00
+  __DATA_CONST.__objc_const: 0x47b0
+  __DATA_CONST.__objc_selrefs: 0x1c38
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x3d00
+  __AUTH_CONST.__cfstring: 0x3e00
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_const: 0x938
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0xa38
+  __AUTH_CONST.__auth_got: 0xa48
   __AUTH.__objc_data: 0x230
   __DATA.__objc_classrefs: 0x200
   __DATA.__objc_superrefs: 0xa8
-  __DATA.__objc_ivar: 0x3f0
+  __DATA.__objc_ivar: 0x400
   __DATA.__data: 0x5e6
   __DATA.__bss: 0xc5
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2189
-  Symbols:   6011
-  CStrings:  3103
+  Functions: 2215
+  Symbols:   6068
+  CStrings:  3144
 
Symbols:
+ -[ACCTransportIOAccessoryAuthCP _logToAnalytics].cold.1
+ -[ACCTransportIOAccessoryManager _processAccessoryInfo].cold.26
+ -[ACCTransportIOAccessoryManager _processAccessoryInfo].cold.27
+ -[ACCTransportIOAccessoryManager initWithIOService:].cold.6
+ -[ACCTransportIOAccessoryManager isAdapter]
+ -[ACCTransportIOAccessoryManager managerParent]
+ -[ACCTransportIOAccessoryManager productID]
+ -[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:]
+ -[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:].cold.1
+ -[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:].cold.2
+ -[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:].cold.3
+ -[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:].cold.4
+ -[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:].cold.5
+ -[ACCTransportIOAccessoryManager setProductID:]
+ -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:]
+ -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:].cold.1
+ -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:].cold.2
+ -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:].cold.3
+ -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:].cold.4
+ -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:].cold.5
+ -[ACCTransportIOAccessoryManager setVendorID:]
+ -[ACCTransportIOAccessoryManager vendorID]
+ -[ACCTransportIOAccessorySharedManager connectedThroughAdapter:]
+ -[ACCTransportIOAccessorySharedManager setBatteryPackMode:forConnectionUUID:forceResponse:]
+ -[ACCTransportIOAccessorySharedManager setBatteryPackMode:forConnectionUUID:forceResponse:].cold.1
+ -[ACCTransportIOAccessorySharedManager setUSBCurrentLimitBase:forConnectionUUID:forceResponse:]
+ -[ACCTransportIOAccessorySharedManager setUSBCurrentLimitBase:forConnectionUUID:forceResponse:].cold.1
+ -[ACCTransportPluginIOAccessoryManager setBatteryPackMode:forConnectionUUID:forceResponse:]
+ -[ACCTransportPluginIOAccessoryManager setUSBCurrentLimitBase:forConnectionUUID:forceResponse:]
+ GCC_except_table103
+ GCC_except_table99
+ _ACMSEPControl
+ _ACMSEPControlEx
+ _IORegistryEntryGetName
+ _IORegistryEntrySearchCFProperty
+ _LibCall_ACMSEPControl
+ _LibCall_ACMSEPControl_Block
+ _LibSer_SEPControlResponse_Deserialize
+ _LibSer_SEPControlResponse_GetSize
+ _LibSer_SEPControlResponse_Serialize
+ _LibSer_SEPControl_Deserialize
+ _LibSer_SEPControl_GetSize
+ _LibSer_SEPControl_Serialize
+ _OBJC_IVAR_$_ACCTransportIOAccessoryManager._isAdapter
+ _OBJC_IVAR_$_ACCTransportIOAccessoryManager._managerParent
+ _OBJC_IVAR_$_ACCTransportIOAccessoryManager._productID
+ _OBJC_IVAR_$_ACCTransportIOAccessoryManager._vendorID
+ _OUTLINED_FUNCTION_21
+ _Util_getSubrequirement
+ _Util_getSubrequirement.cold.1
+ _Util_getSubrequirementOfType
+ _Util_getSubrequirementOfType.cold.1
+ ___67-[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:]_block_invoke
+ ___67-[ACCTransportIOAccessoryManager setBatteryPackMode:forceResponse:]_block_invoke.cold.1
+ ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.66
+ ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.66.cold.1
+ ___71-[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:]_block_invoke
+ ___71-[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:forceResponse:]_block_invoke.cold.1
+ ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.131
+ ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.136
+ ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.136.cold.1
+ __unnamed_array_storage.146
+ __unnamed_array_storage.152
+ _kACCInfo_ProductID
+ _kACCInfo_VendorID
+ _kACCProperties_Connection_IsAdapter
+ _kACCProperties_Connection_ManagerParent
+ _kCFACCProperties_Endpoint_AIDInfo
+ _objc_msgSend$isAdapter
+ _objc_msgSend$managerParent
+ _objc_msgSend$productID
+ _objc_msgSend$setBatteryPackMode:forConnectionUUID:forceResponse:
+ _objc_msgSend$setBatteryPackMode:forceResponse:
+ _objc_msgSend$setProductID:
+ _objc_msgSend$setUSBCurrentLimitBase:forConnectionUUID:forceResponse:
+ _objc_msgSend$setUSBCurrentLimitBase:forceResponse:
+ _objc_msgSend$setVendorID:
+ _objc_msgSend$vendorID
- -[ACCTransportIOAccessoryManager setBatteryPackMode:]
- -[ACCTransportIOAccessoryManager setBatteryPackMode:].cold.1
- -[ACCTransportIOAccessoryManager setBatteryPackMode:].cold.2
- -[ACCTransportIOAccessoryManager setBatteryPackMode:].cold.3
- -[ACCTransportIOAccessoryManager setBatteryPackMode:].cold.4
- -[ACCTransportIOAccessoryManager setBatteryPackMode:].cold.5
- -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:]
- -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:].cold.1
- -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:].cold.2
- -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:].cold.3
- -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:].cold.4
- -[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:].cold.5
- -[ACCTransportIOAccessorySharedManager setBatteryPackMode:forConnectionUUID:]
- -[ACCTransportIOAccessorySharedManager setBatteryPackMode:forConnectionUUID:].cold.1
- -[ACCTransportIOAccessorySharedManager setUSBCurrentLimitBase:forConnectionUUID:]
- -[ACCTransportIOAccessorySharedManager setUSBCurrentLimitBase:forConnectionUUID:].cold.1
- -[ACCTransportPluginIOAccessoryManager setBatteryPackMode:forConnectionUUID:]
- -[ACCTransportPluginIOAccessoryManager setUSBCurrentLimitBase:forConnectionUUID:]
- GCC_except_table102
- GCC_except_table98
- ___53-[ACCTransportIOAccessoryManager setBatteryPackMode:]_block_invoke
- ___53-[ACCTransportIOAccessoryManager setBatteryPackMode:]_block_invoke.cold.1
- ___57-[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:]_block_invoke
- ___57-[ACCTransportIOAccessoryManager setUSBCurrentLimitBase:]_block_invoke.cold.1
- ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.55
- ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.55.cold.1
- ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.129
- ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.135
- ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.135.cold.1
- __unnamed_array_storage.145
- __unnamed_array_storage.150
- _objc_msgSend$setBatteryPackMode:
- _objc_msgSend$setBatteryPackMode:forConnectionUUID:
- _objc_msgSend$setUSBCurrentLimitBase:
- _objc_msgSend$setUSBCurrentLimitBase:forConnectionUUID:
CStrings:
+ "\x11_\x06"
+ "%s:%d (%d) service %d, adapterName '%@', adapterFWVer %@, adapterSerNumVer %@, adapterVID '%@', adapterPID %@"
+ "%s:%d (%d) service %d, aidInfo %@"
+ "%s:%d service %d, _managerParent %@ -> %@ "
+ "-[ACCTransportIOAccessoryManager _processAccessoryInfo]"
+ "-[ACCTransportIOAccessoryManager initWithIOService:]"
+ "ACMRequirement - ACMRequirementDataRatchet"
+ "AppleUVDMEndpoint"
+ "B24@0:8B16B20"
+ "B24@0:8I16B20"
+ "B32@0:8B16@\"NSString\"20B28"
+ "B32@0:8B16@20B28"
+ "B32@0:8I16@\"NSString\"20B28"
+ "B32@0:8I16@20B28"
+ "Description"
+ "Firmware Version"
+ "Got accessory Info for IOAccessoryManager service %d:\nname:%@\nmanufacturer:%@\nmodel:%@\nserial number:%@\nfirmwareRevision:%@\nhardwareRevision:%@\ndigitalID:%@\nvendorID:%@\nproductID:%@\n"
+ "IOAccessoryManager added,  isRootPort = %d, isAdapter = %d, _connectionType = %{coreacc:ACCConnection_Type_t}d, _bIsInductive = %d, _bIsInductivePowerToAccessory = %d, _managerParent = %@"
+ "IOProviderClass"
+ "IOService"
+ "LibCall_ACMSEPControl"
+ "LibCall_ACMSEPControl_Block"
+ "Product ID"
+ "Serial Number"
+ "T@\"NSNumber\",&,N,V_productID"
+ "T@\"NSNumber\",&,N,V_vendorID"
+ "T@\"NSString\",R,N,V_managerParent"
+ "TB,R,N,V_isAdapter"
+ "User String"
+ "Util_getSubrequirement"
+ "Util_getSubrequirementOfType"
+ "Vendor ID"
+ "_isAdapter"
+ "_managerParent"
+ "_productID"
+ "_vendorID"
+ "connectedThroughAdapter:"
+ "isAdapter"
+ "managerParent"
+ "productID"
+ "req"
+ "setBatteryPackMode: not lightning device, batteryPackModeEnabled %d -> %d, valid %d -> %d, forceResponse %d"
+ "setBatteryPackMode:forConnectionUUID:forceResponse:"
+ "setBatteryPackMode:forceResponse:"
+ "setProductID:"
+ "setUSBCurrentLimitBase: not lightning device, currentLimitBaseInmA %d -> %d, valid %d -> %d, forceResponse %d"
+ "setUSBCurrentLimitBase:forConnectionUUID:forceResponse:"
+ "setUSBCurrentLimitBase:forceResponse:"
+ "setVendorID:"
+ "vendorID"
- "\x11_\x03"
- "Got accessory Info for IOAccessoryManager service %d:\nname:%@\nmanufacturer:%@\nmodel:%@\nserial number:%@\nfirmwareRevision:%@\nhardwareRevision:%@\ndigitalID:%@\n"
- "IOAccessoryManager added,  isRootPort = %d, _connectionType = %{coreacc:ACCConnection_Type_t}d, _bIsInductive = %d, _bIsInductivePowerToAccessory = %d"
- "setBatteryPackMode:"
- "setBatteryPackMode: not lightning device, batteryPackModeEnabled %d -> %d, valid %d -> %d"
- "setBatteryPackMode:forConnectionUUID:"
- "setUSBCurrentLimitBase:"
- "setUSBCurrentLimitBase: not lightning device, currentLimitBaseInmA %d -> %d, valid %d -> %d"
- "setUSBCurrentLimitBase:forConnectionUUID:"

```
