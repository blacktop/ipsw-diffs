## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-423.30.6.9.11
-  __TEXT.__text: 0x71904
+423.30.6.9.17
+  __TEXT.__text: 0x74408
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_methlist: 0xace4
-  __TEXT.__cstring: 0x65e7
+  __TEXT.__objc_methlist: 0xb04c
+  __TEXT.__cstring: 0x6657
   __TEXT.__const: 0x450
-  __TEXT.__gcc_except_tab: 0x1ba8
-  __TEXT.__oslogstring: 0x7228
+  __TEXT.__gcc_except_tab: 0x1cb4
+  __TEXT.__oslogstring: 0x7388
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x124
   __TEXT.__swift5_fieldmd: 0xfc

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift5_capture: 0x60
   __TEXT.__swift_as_ret: 0x18
-  __TEXT.__unwind_info: 0x2500
+  __TEXT.__unwind_info: 0x2570
   __TEXT.__eh_frame: 0x278
-  __TEXT.__objc_classname: 0x1265
-  __TEXT.__objc_methname: 0x12635
-  __TEXT.__objc_methtype: 0x3690
-  __TEXT.__objc_stubs: 0xa540
-  __DATA_CONST.__got: 0x5a0
-  __DATA_CONST.__const: 0x2040
-  __DATA_CONST.__objc_classlist: 0x408
-  __DATA_CONST.__objc_protolist: 0x1a8
+  __TEXT.__objc_classname: 0x12cf
+  __TEXT.__objc_methname: 0x12b73
+  __TEXT.__objc_methtype: 0x3753
+  __TEXT.__objc_stubs: 0xa7a0
+  __DATA_CONST.__got: 0x5a8
+  __DATA_CONST.__const: 0x20c8
+  __DATA_CONST.__objc_classlist: 0x420
+  __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x39b0
+  __DATA_CONST.__objc_selrefs: 0x3ab0
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x640
-  __AUTH_CONST.__const: 0xb58
-  __AUTH_CONST.__cfstring: 0x5a80
-  __AUTH_CONST.__objc_const: 0x12808
+  __AUTH_CONST.__const: 0xb78
+  __AUTH_CONST.__cfstring: 0x5b80
+  __AUTH_CONST.__objc_const: 0x12f10
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1128
-  __DATA.__objc_ivar: 0xd88
-  __DATA.__data: 0x1418
+  __AUTH.__objc_data: 0x1218
+  __DATA.__objc_ivar: 0xde8
+  __DATA.__data: 0x1478
   __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x1738
   __DATA_DIRTY.__data: 0x1b8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EAFF381C-3461-3BE1-9613-4B330D1DFF56
-  Functions: 4049
-  Symbols:   12539
-  CStrings:  5756
+  UUID: CB5AAFF9-C8F5-3664-A54B-6B99DCD4159F
+  Functions: 4136
+  Symbols:   12804
+  CStrings:  5840
 
Symbols:
+ -[SPInternalSimpleBeacon imageBaseUrl]
+ -[SPInternalSimpleBeacon isRepairCapable]
+ -[SPInternalSimpleBeacon repairState]
+ -[SPInternalSimpleBeacon setImageBaseUrl:]
+ -[SPInternalSimpleBeacon setIsRepairCapable:]
+ -[SPInternalSimpleBeacon setRepairState:]
+ -[SPOwnerInterface repairInterface]
+ -[SPRepairDeviceAttributes .cxx_destruct]
+ -[SPRepairDeviceAttributes deviceClass]
+ -[SPRepairDeviceAttributes deviceColor]
+ -[SPRepairDeviceAttributes deviceModel]
+ -[SPRepairDeviceAttributes identifier]
+ -[SPRepairDeviceAttributes imageBaseUrl]
+ -[SPRepairDeviceAttributes initWithInternalSimpleBeacon:]
+ -[SPRepairDeviceAttributes isMine]
+ -[SPRepairDeviceAttributes isRepairCapable]
+ -[SPRepairDeviceAttributes name]
+ -[SPRepairDeviceAttributes owner]
+ -[SPRepairDeviceAttributes rawDeviceModel]
+ -[SPRepairDeviceAttributes repairState]
+ -[SPRepairDeviceAttributes serialNumber]
+ -[SPRepairDeviceAttributes setDeviceClass:]
+ -[SPRepairDeviceAttributes setDeviceColor:]
+ -[SPRepairDeviceAttributes setDeviceModel:]
+ -[SPRepairDeviceAttributes setIdentifier:]
+ -[SPRepairDeviceAttributes setIsMine:]
+ -[SPRepairDeviceAttributes setIsRepairCapable:]
+ -[SPRepairDeviceAttributes setName:]
+ -[SPRepairDeviceAttributes setOwner:]
+ -[SPRepairDeviceAttributes setRawDeviceModel:]
+ -[SPRepairDeviceAttributes setRepairState:]
+ -[SPRepairDeviceAttributes setSerialNumber:]
+ -[SPRepairDeviceAttributes setThisDevice:]
+ -[SPRepairDeviceAttributes thisDevice]
+ -[SPRepairDeviceContext .cxx_destruct]
+ -[SPRepairDeviceContext beaconIdentifiers]
+ -[SPRepairDeviceContext findMyIds]
+ -[SPRepairDeviceContext initWithMatchingBeaconIdentifiers:type:]
+ -[SPRepairDeviceContext initWithMatchingFindMyIds:type:]
+ -[SPRepairDeviceContext initWithMatchingSerialNumbers:type:]
+ -[SPRepairDeviceContext serialNumbers]
+ -[SPRepairDeviceContext setBeaconIdentifiers:]
+ -[SPRepairDeviceContext setFindMyIds:]
+ -[SPRepairDeviceContext setSerialNumbers:]
+ -[SPRepairDeviceContext setType:]
+ -[SPRepairDeviceContext type]
+ -[SPRepairDeviceInterface .cxx_destruct]
+ -[SPRepairDeviceInterface beaconSession]
+ -[SPRepairDeviceInterface deviceAttributesForContext:completion:]
+ -[SPRepairDeviceInterface deviceForBeaconIdentifier:completion:]
+ -[SPRepairDeviceInterface deviceForFindMyId:completion:]
+ -[SPRepairDeviceInterface deviceForSerialNumber:completion:]
+ -[SPRepairDeviceInterface setBeaconSession:]
+ -[SPRepairDeviceInterface updateRepairStateForSerialNumber:updateBlock:]
+ -[SPSimpleBeaconContext initWithFetchProperties:matchingBeaconUUIDs:]
+ -[SPSimpleBeaconContext initWithFetchProperties:matchingFindMyIds:]
+ -[SPSimpleBeaconContext initWithFetchProperties:matchingSerialNumbers:]
+ -[SPSimpleBeaconContext matchingBeaconUUIDs]
+ -[SPSimpleBeaconContext matchingFindMyIds]
+ -[SPSimpleBeaconContext matchingSerialNumbers]
+ -[SPSimpleBeaconContext repairContextType]
+ -[SPSimpleBeaconContext setMatchingBeaconUUIDs:]
+ -[SPSimpleBeaconContext setMatchingFindMyIds:]
+ -[SPSimpleBeaconContext setMatchingSerialNumbers:]
+ -[SPSimpleBeaconContext setRepairContextType:]
+ _OBJC_CLASS_$_SPRepairDeviceAttributes
+ _OBJC_CLASS_$_SPRepairDeviceContext
+ _OBJC_CLASS_$_SPRepairDeviceInterface
+ _OBJC_IVAR_$_SPInternalSimpleBeacon._imageBaseUrl
+ _OBJC_IVAR_$_SPInternalSimpleBeacon._isRepairCapable
+ _OBJC_IVAR_$_SPInternalSimpleBeacon._repairState
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._deviceClass
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._deviceColor
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._deviceModel
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._identifier
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._imageBaseUrl
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._isMine
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._isRepairCapable
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._name
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._owner
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._rawDeviceModel
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._repairState
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._serialNumber
+ _OBJC_IVAR_$_SPRepairDeviceAttributes._thisDevice
+ _OBJC_IVAR_$_SPRepairDeviceContext._beaconIdentifiers
+ _OBJC_IVAR_$_SPRepairDeviceContext._findMyIds
+ _OBJC_IVAR_$_SPRepairDeviceContext._serialNumbers
+ _OBJC_IVAR_$_SPRepairDeviceContext._type
+ _OBJC_IVAR_$_SPRepairDeviceInterface._beaconSession
+ _OBJC_IVAR_$_SPSimpleBeaconContext._matchingBeaconUUIDs
+ _OBJC_IVAR_$_SPSimpleBeaconContext._matchingFindMyIds
+ _OBJC_IVAR_$_SPSimpleBeaconContext._matchingSerialNumbers
+ _OBJC_IVAR_$_SPSimpleBeaconContext._repairContextType
+ _OBJC_METACLASS_$_SPRepairDeviceAttributes
+ _OBJC_METACLASS_$_SPRepairDeviceContext
+ _OBJC_METACLASS_$_SPRepairDeviceInterface
+ _OUTLINED_FUNCTION_4
+ _SPRepairDeviceContextTypeRepair
+ _SPRepairDeviceContextTypeTradeIn
+ __OBJC_$_INSTANCE_METHODS_SPRepairDeviceAttributes
+ __OBJC_$_INSTANCE_METHODS_SPRepairDeviceContext
+ __OBJC_$_INSTANCE_METHODS_SPRepairDeviceInterface
+ __OBJC_$_INSTANCE_VARIABLES_SPRepairDeviceAttributes
+ __OBJC_$_INSTANCE_VARIABLES_SPRepairDeviceContext
+ __OBJC_$_INSTANCE_VARIABLES_SPRepairDeviceInterface
+ __OBJC_$_PROP_LIST_SPRepairDeviceAttributes
+ __OBJC_$_PROP_LIST_SPRepairDeviceContext
+ __OBJC_$_PROP_LIST_SPRepairDeviceInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SPRepairDeviceInterfaceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SPRepairDeviceInterfaceProtocol
+ __OBJC_$_PROTOCOL_REFS_SPRepairDeviceInterfaceProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SPRepairDeviceInterface
+ __OBJC_CLASS_RO_$_SPRepairDeviceAttributes
+ __OBJC_CLASS_RO_$_SPRepairDeviceContext
+ __OBJC_CLASS_RO_$_SPRepairDeviceInterface
+ __OBJC_LABEL_PROTOCOL_$_SPRepairDeviceInterfaceProtocol
+ __OBJC_METACLASS_RO_$_SPRepairDeviceAttributes
+ __OBJC_METACLASS_RO_$_SPRepairDeviceContext
+ __OBJC_METACLASS_RO_$_SPRepairDeviceInterface
+ __OBJC_PROTOCOL_$_SPRepairDeviceInterfaceProtocol
+ ___56-[SPRepairDeviceInterface deviceForFindMyId:completion:]_block_invoke
+ ___56-[SPRepairDeviceInterface deviceForFindMyId:completion:]_block_invoke.11
+ ___56-[SPRepairDeviceInterface deviceForFindMyId:completion:]_block_invoke.11.cold.1
+ ___56-[SPRepairDeviceInterface deviceForFindMyId:completion:]_block_invoke.12
+ ___56-[SPRepairDeviceInterface deviceForFindMyId:completion:]_block_invoke.cold.1
+ ___60-[SPRepairDeviceInterface deviceForSerialNumber:completion:]_block_invoke
+ ___60-[SPRepairDeviceInterface deviceForSerialNumber:completion:]_block_invoke.10
+ ___60-[SPRepairDeviceInterface deviceForSerialNumber:completion:]_block_invoke.9
+ ___60-[SPRepairDeviceInterface deviceForSerialNumber:completion:]_block_invoke.9.cold.1
+ ___60-[SPRepairDeviceInterface deviceForSerialNumber:completion:]_block_invoke.cold.1
+ ___64-[SPRepairDeviceInterface deviceForBeaconIdentifier:completion:]_block_invoke
+ ___64-[SPRepairDeviceInterface deviceForBeaconIdentifier:completion:]_block_invoke.13
+ ___64-[SPRepairDeviceInterface deviceForBeaconIdentifier:completion:]_block_invoke.13.cold.1
+ ___64-[SPRepairDeviceInterface deviceForBeaconIdentifier:completion:]_block_invoke.14
+ ___64-[SPRepairDeviceInterface deviceForBeaconIdentifier:completion:]_block_invoke.cold.1
+ ___65-[SPRepairDeviceInterface deviceAttributesForContext:completion:]_block_invoke
+ ___65-[SPRepairDeviceInterface deviceAttributesForContext:completion:]_block_invoke.3
+ ___65-[SPRepairDeviceInterface deviceAttributesForContext:completion:]_block_invoke.3.cold.1
+ ___65-[SPRepairDeviceInterface deviceAttributesForContext:completion:]_block_invoke.7
+ ___65-[SPRepairDeviceInterface deviceAttributesForContext:completion:]_block_invoke.cold.1
+ ___72-[SPRepairDeviceInterface updateRepairStateForSerialNumber:updateBlock:]_block_invoke
+ ___72-[SPRepairDeviceInterface updateRepairStateForSerialNumber:updateBlock:]_block_invoke.15
+ ___72-[SPRepairDeviceInterface updateRepairStateForSerialNumber:updateBlock:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32bs40w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e51_v24?0"NSOrderedCollectionDifference"8"NSError"16lw48l8s40l8s32l8
+ _objc_msgSend$allObjects
+ _objc_msgSend$beaconSession
+ _objc_msgSend$findMyIds
+ _objc_msgSend$imageBaseUrl
+ _objc_msgSend$initWithFetchProperties:matchingBeaconUUIDs:
+ _objc_msgSend$initWithFetchProperties:matchingFindMyIds:
+ _objc_msgSend$initWithFetchProperties:matchingSerialNumbers:
+ _objc_msgSend$isRepairCapable
+ _objc_msgSend$matchingBeaconUUIDs
+ _objc_msgSend$matchingFindMyIds
+ _objc_msgSend$matchingSerialNumbers
+ _objc_msgSend$repairContextType
+ _objc_msgSend$repairState
+ _objc_msgSend$serialNumbers
+ _objc_msgSend$setBeaconSession:
+ _objc_msgSend$setImageBaseUrl:
+ _objc_msgSend$setIsRepairCapable:
+ _objc_msgSend$setMatchingBeaconUUIDs:
+ _objc_msgSend$setMatchingFindMyIds:
+ _objc_msgSend$setMatchingSerialNumbers:
+ _objc_msgSend$setRepairContextType:
+ _objc_msgSend$setRepairState:
- -[SPSimpleBeaconContext initWithFetchProperties:filterBeaconUUIDs:]
- _OBJC_IVAR_$_SPSimpleBeaconContext._filterBeaconUUIDs
- _objc_msgSend$filterBeaconUUIDs
- _objc_msgSend$initWithFetchProperties:filterBeaconUUIDs:
- _objc_msgSend$setFilterBeaconUUIDs:
CStrings:
+ "Error during update of device %@ error: %@"
+ "Error during update of devices error: %@"
+ "Error stopping fetch of device for %@. Stopped %i, error: %@"
+ "Error stopping fetch of devices. Stopped %i, error: %@"
+ "REPAIR"
+ "SPOwnerSession: task last updated: %@ command: %@"
+ "SPRepairDeviceAttributes"
+ "SPRepairDeviceContext"
+ "SPRepairDeviceInterface"
+ "SPRepairDeviceInterfaceProtocol"
+ "Starting fetch of device for %@. Subscribed %i, error: %@"
+ "Starting fetch of devices. Subscribed %i, error: %@"
+ "T@\"NSArray\",C,N"
+ "T@\"NSArray\",C,N,V_matchingBeaconUUIDs"
+ "T@\"NSArray\",C,N,V_matchingFindMyIds"
+ "T@\"NSArray\",C,N,V_matchingSerialNumbers"
+ "T@\"NSNumber\",C,N,V_isRepairCapable"
+ "T@\"NSSet\",&,N,V_beaconIdentifiers"
+ "T@\"NSSet\",&,N,V_findMyIds"
+ "T@\"NSSet\",&,N,V_serialNumbers"
+ "T@\"NSString\",&,N,V_type"
+ "T@\"NSString\",C,N,V_repairContextType"
+ "T@\"NSURL\",C,N,V_imageBaseUrl"
+ "T@\"NSURL\",R,C,N,V_imageBaseUrl"
+ "T@\"SPBeaconManagerSimpleBeaconUpdateInterface\",&,N,V_beaconSession"
+ "TRADEIN"
+ "Tq,N,V_repairState"
+ "_beaconSession"
+ "_findMyIds"
+ "_imageBaseUrl"
+ "_isRepairCapable"
+ "_matchingBeaconUUIDs"
+ "_matchingFindMyIds"
+ "_matchingSerialNumbers"
+ "_repairContextType"
+ "_repairState"
+ "_serialNumbers"
+ "allObjects"
+ "beaconSession"
+ "deviceAttributesForContext:completion:"
+ "deviceForBeaconIdentifier:completion:"
+ "deviceForFindMyId:completion:"
+ "deviceForSerialNumber:completion:"
+ "findMyIds"
+ "imageBaseUrl"
+ "initWithFetchProperties:matchingBeaconUUIDs:"
+ "initWithFetchProperties:matchingFindMyIds:"
+ "initWithFetchProperties:matchingSerialNumbers:"
+ "initWithMatchingBeaconIdentifiers:type:"
+ "initWithMatchingFindMyIds:type:"
+ "initWithMatchingSerialNumbers:type:"
+ "isRepairCapable"
+ "matchingBeaconUUIDs"
+ "matchingFindMyIds"
+ "matchingSerialNumbers"
+ "repairContextType"
+ "repairInterface"
+ "repairState"
+ "serialNumbers"
+ "setBeaconSession:"
+ "setFindMyIds:"
+ "setImageBaseUrl:"
+ "setIsRepairCapable:"
+ "setMatchingBeaconUUIDs:"
+ "setMatchingFindMyIds:"
+ "setMatchingSerialNumbers:"
+ "setRepairContextType:"
+ "setRepairState:"
+ "setSerialNumbers:"
+ "updateRepairStateForSerialNumber:updateBlock:"
+ "v32@0:8@\"NSString\"16@?<v@?@\"SPRepairDeviceAttributes\"@\"NSError\">24"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"SPRepairDeviceAttributes\"@\"NSError\">24"
+ "v32@0:8@\"SPRepairDeviceContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
- "T@\"NSArray\",C,N,V_filterBeaconUUIDs"
- "_filterBeaconUUIDs"
- "initWithFetchProperties:filterBeaconUUIDs:"

```
