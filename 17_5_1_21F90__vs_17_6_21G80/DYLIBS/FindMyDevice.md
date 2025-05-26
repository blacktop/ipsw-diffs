## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-424.6.0.0.0
-  __TEXT.__text: 0x1c7bc
+424.9.0.0.0
+  __TEXT.__text: 0x1d490
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x1a88
+  __TEXT.__objc_methlist: 0x1c30
   __TEXT.__const: 0x70
-  __TEXT.__oslogstring: 0x2204
-  __TEXT.__cstring: 0x3b4c
+  __TEXT.__oslogstring: 0x227b
+  __TEXT.__cstring: 0x3c22
   __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__unwind_info: 0x6a8
-  __TEXT.__objc_classname: 0x586
-  __TEXT.__objc_methname: 0x451d
-  __TEXT.__objc_methtype: 0x1094
-  __TEXT.__objc_stubs: 0x3080
+  __TEXT.__unwind_info: 0x6f4
+  __TEXT.__objc_classname: 0x5c3
+  __TEXT.__objc_methname: 0x4829
+  __TEXT.__objc_methtype: 0x10fc
+  __TEXT.__objc_stubs: 0x30c0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x1118
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__const: 0x1128
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6488
-  __DATA_CONST.__objc_selrefs: 0xef8
+  __DATA_CONST.__objc_const: 0x68e8
+  __DATA_CONST.__objc_selrefs: 0xf80
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_classrefs: 0x120
-  __DATA_CONST.__objc_superrefs: 0xe8
-  __AUTH_CONST.__objc_const: 0x1090
-  __AUTH_CONST.__cfstring: 0x3560
-  __AUTH_CONST.__const: 0x440
+  __DATA_CONST.__objc_classrefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x100
+  __AUTH_CONST.__objc_const: 0x1240
+  __AUTH_CONST.__cfstring: 0x3680
+  __AUTH_CONST.__const: 0x460
   __AUTH_CONST.__auth_got: 0x240
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x1d0
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x1f0
   __DATA.__data: 0x920
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xe0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x40

   - /System/Library/PrivateFrameworks/FMCoreLite.framework/FMCoreLite
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 841
-  Symbols:   3415
-  CStrings:  1694
+  Functions: 877
+  Symbols:   3550
+  CStrings:  1744
 
Symbols:
+ +[FMDRepairDevice supportsSecureCoding]
+ +[FMDRepairDeviceContext supportsSecureCoding]
+ +[FMDRepairDeviceResult supportsSecureCoding]
+ -[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]
+ -[FMDFMIPManager enableRepairWithContext:completion:]
+ -[FMDRepairDevice .cxx_destruct]
+ -[FMDRepairDevice encodeWithCoder:]
+ -[FMDRepairDevice identifier]
+ -[FMDRepairDevice initWithClientIdentifier:isThisDevice:]
+ -[FMDRepairDevice initWithCoder:]
+ -[FMDRepairDevice isThisDevice]
+ -[FMDRepairDeviceContext .cxx_destruct]
+ -[FMDRepairDeviceContext encodeWithCoder:]
+ -[FMDRepairDeviceContext ephemeralToken]
+ -[FMDRepairDeviceContext initWithCoder:]
+ -[FMDRepairDeviceContext repairDeviceMode]
+ -[FMDRepairDeviceContext searchIdentifiers]
+ -[FMDRepairDeviceContext selectedDevices]
+ -[FMDRepairDeviceContext setEphemeralToken:]
+ -[FMDRepairDeviceContext setRepairDeviceMode:]
+ -[FMDRepairDeviceContext setSearchIdentifiers:]
+ -[FMDRepairDeviceContext setSelectedDevices:]
+ -[FMDRepairDeviceResult .cxx_destruct]
+ -[FMDRepairDeviceResult devicesInRepairMode]
+ -[FMDRepairDeviceResult eligibleDevices]
+ -[FMDRepairDeviceResult encodeWithCoder:]
+ -[FMDRepairDeviceResult initWithCoder:]
+ -[FMDRepairDeviceResult initWithEligibleDevices:devicesInRepairMode:]
+ -[FMDRepairDeviceResult setDevicesInRepairMode:]
+ -[FMDRepairDeviceResult setEligibleDevices:]
+ _FMDRepairDeviceThisDeviceIdentifier
+ _LogCategory_RepairDevice
+ _LogCategory_RepairDevice.log
+ _LogCategory_RepairDevice.onceToken
+ _OBJC_CLASS_$_FMDRepairDevice
+ _OBJC_CLASS_$_FMDRepairDeviceContext
+ _OBJC_CLASS_$_FMDRepairDeviceResult
+ _OBJC_IVAR_$_FMDRepairDevice._identifier
+ _OBJC_IVAR_$_FMDRepairDevice._isThisDevice
+ _OBJC_IVAR_$_FMDRepairDeviceContext._ephemeralToken
+ _OBJC_IVAR_$_FMDRepairDeviceContext._repairDeviceMode
+ _OBJC_IVAR_$_FMDRepairDeviceContext._searchIdentifiers
+ _OBJC_IVAR_$_FMDRepairDeviceContext._selectedDevices
+ _OBJC_IVAR_$_FMDRepairDeviceResult._devicesInRepairMode
+ _OBJC_IVAR_$_FMDRepairDeviceResult._eligibleDevices
+ _OBJC_METACLASS_$_FMDRepairDevice
+ _OBJC_METACLASS_$_FMDRepairDeviceContext
+ _OBJC_METACLASS_$_FMDRepairDeviceResult
+ __OBJC_$_CLASS_METHODS_FMDRepairDevice
+ __OBJC_$_CLASS_METHODS_FMDRepairDeviceContext
+ __OBJC_$_CLASS_METHODS_FMDRepairDeviceResult
+ __OBJC_$_CLASS_PROP_LIST_FMDRepairDevice
+ __OBJC_$_CLASS_PROP_LIST_FMDRepairDeviceContext
+ __OBJC_$_CLASS_PROP_LIST_FMDRepairDeviceResult
+ __OBJC_$_INSTANCE_METHODS_FMDRepairDevice
+ __OBJC_$_INSTANCE_METHODS_FMDRepairDeviceContext
+ __OBJC_$_INSTANCE_METHODS_FMDRepairDeviceResult
+ __OBJC_$_INSTANCE_VARIABLES_FMDRepairDevice
+ __OBJC_$_INSTANCE_VARIABLES_FMDRepairDeviceContext
+ __OBJC_$_INSTANCE_VARIABLES_FMDRepairDeviceResult
+ __OBJC_$_PROP_LIST_FMDRepairDevice
+ __OBJC_$_PROP_LIST_FMDRepairDeviceContext
+ __OBJC_$_PROP_LIST_FMDRepairDeviceResult
+ __OBJC_CLASS_PROTOCOLS_$_FMDRepairDevice
+ __OBJC_CLASS_PROTOCOLS_$_FMDRepairDeviceContext
+ __OBJC_CLASS_PROTOCOLS_$_FMDRepairDeviceResult
+ __OBJC_CLASS_RO_$_FMDRepairDevice
+ __OBJC_CLASS_RO_$_FMDRepairDeviceContext
+ __OBJC_CLASS_RO_$_FMDRepairDeviceResult
+ __OBJC_METACLASS_RO_$_FMDRepairDevice
+ __OBJC_METACLASS_RO_$_FMDRepairDeviceContext
+ __OBJC_METACLASS_RO_$_FMDRepairDeviceResult
+ ___53-[FMDFMIPManager enableRepairWithContext:completion:]_block_invoke
+ ___53-[FMDFMIPManager enableRepairWithContext:completion:]_block_invoke.cold.1
+ ___64-[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]_block_invoke
+ ___64-[FMDFMIPManager deviceEligibleForRepairWithContext:completion:]_block_invoke.cold.1
+ ___LogCategory_RepairDevice_block_invoke
+ ___block_literal_global.44
+ _kFMDRepairDeviceAccessEntitlement
+ _objc_msgSend$deviceEligibleForRepairWithContext:completion:
+ _objc_msgSend$enableRepairWithContext:completion:
CStrings:
+ "@\"NSArray\""
+ "@28@0:8@16B24"
+ "FMDRepairDevice"
+ "FMDRepairDeviceContext"
+ "FMDRepairDeviceResult"
+ "FMDRepairDeviceThisDeviceIdentifier"
+ "T@\"NSArray\",&,N,V_devicesInRepairMode"
+ "T@\"NSArray\",&,N,V_eligibleDevices"
+ "T@\"NSArray\",&,N,V_searchIdentifiers"
+ "T@\"NSArray\",&,N,V_selectedDevices"
+ "T@\"NSString\",&,N,V_ephemeralToken"
+ "T@\"NSString\",R,N,V_identifier"
+ "TB,R,N,V_isThisDevice"
+ "Tq,N,V_repairDeviceMode"
+ "Vv32@0:8@\"FMDRepairDeviceContext\"16@?<v@?@\"FMDRepairDeviceResult\"@\"NSError\">24"
+ "XPC error for deviceEligibleForRepairWithContext:completion: %li"
+ "XPC error for enableRepairWithContext:completion: %li"
+ "_devicesInRepairMode"
+ "_eligibleDevices"
+ "_ephemeralToken"
+ "_isThisDevice"
+ "_repairDeviceMode"
+ "_searchIdentifiers"
+ "_selectedDevices"
+ "com.apple.icloud.FindMyDevice.RepairDevice.access"
+ "deviceEligibleForRepairWithContext:completion:"
+ "devicesInRepairMode"
+ "eligibleDevices"
+ "enableRepairWithContext:completion:"
+ "ephemeralToken"
+ "initWithClientIdentifier:isThisDevice:"
+ "initWithEligibleDevices:devicesInRepairMode:"
+ "isThisDevice"
+ "repairDevice"
+ "repairDeviceMode"
+ "searchIdentifiers"
+ "selectedDevices"
+ "setDevicesInRepairMode:"
+ "setEligibleDevices:"
+ "setEphemeralToken:"
+ "setRepairDeviceMode:"
+ "setSearchIdentifiers:"
+ "setSelectedDevices:"

```
