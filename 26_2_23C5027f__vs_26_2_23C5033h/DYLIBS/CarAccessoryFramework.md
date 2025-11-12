## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-488.25.0.0.0
-  __TEXT.__text: 0x10077c
+488.28.0.0.0
+  __TEXT.__text: 0x101478
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x18e54
+  __TEXT.__objc_methlist: 0x190dc
   __TEXT.__const: 0x158
   __TEXT.__gcc_except_tab: 0x694
-  __TEXT.__cstring: 0x7827
-  __TEXT.__oslogstring: 0x3693
+  __TEXT.__cstring: 0x784f
+  __TEXT.__oslogstring: 0x36eb
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3e70
-  __TEXT.__objc_classname: 0x3f7f
-  __TEXT.__objc_methname: 0x1e383
-  __TEXT.__objc_methtype: 0x4782
+  __TEXT.__unwind_info: 0x3eb8
+  __TEXT.__objc_classname: 0x402a
+  __TEXT.__objc_methname: 0x1e318
+  __TEXT.__objc_methtype: 0x47f2
   __TEXT.__objc_stubs: 0x14040
-  __DATA_CONST.__got: 0xc60
-  __DATA_CONST.__const: 0x2588
-  __DATA_CONST.__objc_classlist: 0xd18
-  __DATA_CONST.__objc_nlclslist: 0x9a0
+  __DATA_CONST.__got: 0xc88
+  __DATA_CONST.__const: 0x2590
+  __DATA_CONST.__objc_classlist: 0xd40
+  __DATA_CONST.__objc_nlclslist: 0x9b8
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x6d0
+  __DATA_CONST.__objc_protolist: 0x6e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x74e0
-  __DATA_CONST.__objc_protorefs: 0x670
-  __DATA_CONST.__objc_superrefs: 0x11f0
-  __DATA_CONST.__objc_arraydata: 0xb308
+  __DATA_CONST.__objc_selrefs: 0x7510
+  __DATA_CONST.__objc_protorefs: 0x680
+  __DATA_CONST.__objc_superrefs: 0x1228
+  __DATA_CONST.__objc_arraydata: 0xb1c8
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0xd600
-  __AUTH_CONST.__objc_const: 0x50c98
+  __AUTH_CONST.__cfstring: 0xd660
+  __AUTH_CONST.__objc_const: 0x51940
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__objc_dictobj: 0x5fc8
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x5f78
-  __AUTH.__objc_data: 0x2760
-  __DATA.__objc_ivar: 0x618
-  __DATA.__data: 0x51e0
+  __AUTH.__objc_data: 0x28f0
+  __DATA.__objc_ivar: 0x630
+  __DATA.__data: 0x52a0
   __DATA.__bss: 0x300
   __DATA_DIRTY.__objc_data: 0x5b90
   __DATA_DIRTY.__bss: 0x158

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43F47AED-4D77-304E-9B4B-8144FD643068
-  Functions: 7679
-  Symbols:   25347
-  CStrings:  9597
+  UUID: 85F94396-5BCD-3398-B48D-59BC05F9B121
+  Functions: 7728
+  Symbols:   25525
+  CStrings:  9627
 
Symbols:
+ +[CAFBatchUpdate supportsSecureCoding]
+ +[CAFBatchUpdateItem supportsSecureCoding]
+ +[CAFDriverAssistanceSystem load]
+ +[CAFDriverAssistanceSystem observerProtocol]
+ +[CAFDriverAssistanceSystem serviceIdentifier]
+ +[CAFLaneKeepAlertCharacteristic load]
+ +[CAFLaneKeepAlertCharacteristic primaryCharacteristicFormat]
+ +[CAFLaneKeepAlertCharacteristic secondaryCharacteristicFormats]
+ +[CAFLaneKeepAlerts load]
+ +[CAFLaneKeepAlerts observerProtocol]
+ +[CAFLaneKeepAlerts serviceIdentifier]
+ -[CAFASCTree routeSharingUserVisibleBrand]
+ -[CAFBatchUpdate .cxx_destruct]
+ -[CAFBatchUpdate copyWithZone:]
+ -[CAFBatchUpdate description]
+ -[CAFBatchUpdate encodeWithCoder:]
+ -[CAFBatchUpdate initWithCoder:]
+ -[CAFBatchUpdate initWithItems:]
+ -[CAFBatchUpdate items]
+ -[CAFBatchUpdateItem .cxx_destruct]
+ -[CAFBatchUpdateItem copyWithZone:]
+ -[CAFBatchUpdateItem description]
+ -[CAFBatchUpdateItem encodeWithCoder:]
+ -[CAFBatchUpdateItem initWithCoder:]
+ -[CAFBatchUpdateItem initWithService:characteristicType:value:]
+ -[CAFBatchUpdateItem instanceID]
+ -[CAFBatchUpdateItem pluginID]
+ -[CAFBatchUpdateItem priority]
+ -[CAFBatchUpdateItem value]
+ -[CAFCarManager invalidatedUpdate]
+ -[CAFCarManager setInvalidatedUpdate:]
+ -[CAFCarManager setInvalidatedUpdate:].cold.1
+ -[CAFDriverAssistance driverAssistanceSystemService]
+ -[CAFDriverAssistance driverAssistanceSystem]
+ -[CAFDriverAssistanceSystem _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFDriverAssistanceSystem addObserver:]
+ -[CAFDriverAssistanceSystem driverAssistanceModeIdentifierCharacteristic]
+ -[CAFDriverAssistanceSystem driverAssistanceModeIdentifier]
+ -[CAFDriverAssistanceSystem name]
+ -[CAFDriverAssistanceSystem registerObserver:]
+ -[CAFDriverAssistanceSystem registeredForDriverAssistanceModeIdentifier]
+ -[CAFDriverAssistanceSystem removeObserver:]
+ -[CAFDriverAssistanceSystem unregisterObserver:]
+ -[CAFIndicators laneKeepAlertsService]
+ -[CAFIndicators laneKeepAlerts]
+ -[CAFLaneKeepAlertCharacteristic formattedValue]
+ -[CAFLaneKeepAlertCharacteristic laneKeepAlertValue]
+ -[CAFLaneKeepAlertCharacteristic setLaneKeepAlertValue:]
+ -[CAFLaneKeepAlerts _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFLaneKeepAlerts addObserver:]
+ -[CAFLaneKeepAlerts hasLaneKeepAlertLeft]
+ -[CAFLaneKeepAlerts hasLaneKeepAlertRight]
+ -[CAFLaneKeepAlerts laneKeepAlertLeftCharacteristic]
+ -[CAFLaneKeepAlerts laneKeepAlertLeft]
+ -[CAFLaneKeepAlerts laneKeepAlertRightCharacteristic]
+ -[CAFLaneKeepAlerts laneKeepAlertRight]
+ -[CAFLaneKeepAlerts name]
+ -[CAFLaneKeepAlerts registerObserver:]
+ -[CAFLaneKeepAlerts registeredForLaneKeepAlertLeft]
+ -[CAFLaneKeepAlerts registeredForLaneKeepAlertRight]
+ -[CAFLaneKeepAlerts removeObserver:]
+ -[CAFLaneKeepAlerts unregisterObserver:]
+ -[CAFUIConfiguration setUiConfigurationOptions:]
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table64
+ _CAFCharacteristicTypeDriverAssistanceModeIdentifier
+ _CAFCharacteristicTypeLaneKeepAlertLeft
+ _CAFCharacteristicTypeLaneKeepAlertRight
+ _CAFServiceTypeDriverAssistanceSystem
+ _CAFServiceTypeLaneKeepAlerts
+ _NSStringFromLaneKeepAlert
+ _OBJC_CLASS_$_CAFBatchUpdate
+ _OBJC_CLASS_$_CAFBatchUpdateItem
+ _OBJC_CLASS_$_CAFDriverAssistanceSystem
+ _OBJC_CLASS_$_CAFLaneKeepAlertCharacteristic
+ _OBJC_CLASS_$_CAFLaneKeepAlerts
+ _OBJC_IVAR_$_CAFASCTree._routeSharingUserVisibleBrand
+ _OBJC_IVAR_$_CAFBatchUpdate._items
+ _OBJC_IVAR_$_CAFBatchUpdateItem._instanceID
+ _OBJC_IVAR_$_CAFBatchUpdateItem._pluginID
+ _OBJC_IVAR_$_CAFBatchUpdateItem._priority
+ _OBJC_IVAR_$_CAFBatchUpdateItem._value
+ _OBJC_IVAR_$_CAFCarManager._invalidatedUpdate
+ _OBJC_METACLASS_$_CAFBatchUpdate
+ _OBJC_METACLASS_$_CAFBatchUpdateItem
+ _OBJC_METACLASS_$_CAFDriverAssistanceSystem
+ _OBJC_METACLASS_$_CAFLaneKeepAlertCharacteristic
+ _OBJC_METACLASS_$_CAFLaneKeepAlerts
+ _OUTLINED_FUNCTION_15
+ __OBJC_$_CLASS_METHODS_CAFBatchUpdate
+ __OBJC_$_CLASS_METHODS_CAFBatchUpdateItem
+ __OBJC_$_CLASS_METHODS_CAFDriverAssistanceSystem
+ __OBJC_$_CLASS_METHODS_CAFLaneKeepAlertCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFLaneKeepAlerts
+ __OBJC_$_CLASS_PROP_LIST_CAFBatchUpdate
+ __OBJC_$_CLASS_PROP_LIST_CAFBatchUpdateItem
+ __OBJC_$_INSTANCE_METHODS_CAFBatchUpdate
+ __OBJC_$_INSTANCE_METHODS_CAFBatchUpdateItem
+ __OBJC_$_INSTANCE_METHODS_CAFCar(Accessories|CAFNowPlaying)
+ __OBJC_$_INSTANCE_METHODS_CAFDriverAssistanceSystem
+ __OBJC_$_INSTANCE_METHODS_CAFLaneKeepAlertCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFLaneKeepAlerts
+ __OBJC_$_INSTANCE_VARIABLES_CAFBatchUpdate
+ __OBJC_$_INSTANCE_VARIABLES_CAFBatchUpdateItem
+ __OBJC_$_PROP_LIST_CAFBatchUpdate
+ __OBJC_$_PROP_LIST_CAFBatchUpdateItem
+ __OBJC_$_PROP_LIST_CAFDriverAssistanceSystem
+ __OBJC_$_PROP_LIST_CAFLaneKeepAlertCharacteristic
+ __OBJC_$_PROP_LIST_CAFLaneKeepAlerts
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFDriverAssistanceSystemObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFLaneKeepAlertsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFDriverAssistanceSystemObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFLaneKeepAlertsObserver
+ __OBJC_$_PROTOCOL_REFS_CAFDriverAssistanceSystemObserver
+ __OBJC_$_PROTOCOL_REFS_CAFLaneKeepAlertsObserver
+ __OBJC_CLASS_PROTOCOLS_$_CAFBatchUpdate
+ __OBJC_CLASS_PROTOCOLS_$_CAFBatchUpdateItem
+ __OBJC_CLASS_RO_$_CAFBatchUpdate
+ __OBJC_CLASS_RO_$_CAFBatchUpdateItem
+ __OBJC_CLASS_RO_$_CAFDriverAssistanceSystem
+ __OBJC_CLASS_RO_$_CAFLaneKeepAlertCharacteristic
+ __OBJC_CLASS_RO_$_CAFLaneKeepAlerts
+ __OBJC_LABEL_PROTOCOL_$_CAFDriverAssistanceSystemObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFLaneKeepAlertsObserver
+ __OBJC_METACLASS_RO_$_CAFBatchUpdate
+ __OBJC_METACLASS_RO_$_CAFBatchUpdateItem
+ __OBJC_METACLASS_RO_$_CAFDriverAssistanceSystem
+ __OBJC_METACLASS_RO_$_CAFLaneKeepAlertCharacteristic
+ __OBJC_METACLASS_RO_$_CAFLaneKeepAlerts
+ __OBJC_PROTOCOL_$_CAFDriverAssistanceSystemObserver
+ __OBJC_PROTOCOL_$_CAFLaneKeepAlertsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFDriverAssistanceSystemObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFLaneKeepAlertsObserver
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.248
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.248.cold.1
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.249
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.249.cold.1
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.249.cold.2
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.250
+ ___38-[CAFCarManager setInvalidatedUpdate:]_block_invoke
+ ___38-[CAFCarManager setInvalidatedUpdate:]_block_invoke.cold.1
+ ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.117
+ ___block_literal_global.1659
+ ___block_literal_global.1661
+ ___block_literal_global.729
+ ___block_literal_global.731
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$driverAssistanceModeIdentifier
+ _objc_msgSend$driverAssistanceModeIdentifierCharacteristic
+ _objc_msgSend$driverAssistanceSystemService
+ _objc_msgSend$driverAssistanceSystemService:didUpdateDriverAssistanceModeIdentifier:
+ _objc_msgSend$items
+ _objc_msgSend$laneKeepAlertLeft
+ _objc_msgSend$laneKeepAlertLeftCharacteristic
+ _objc_msgSend$laneKeepAlertRight
+ _objc_msgSend$laneKeepAlertRightCharacteristic
+ _objc_msgSend$laneKeepAlertValue
+ _objc_msgSend$laneKeepAlertsService
+ _objc_msgSend$laneKeepAlertsService:didUpdateLaneKeepAlertLeft:
+ _objc_msgSend$laneKeepAlertsService:didUpdateLaneKeepAlertRight:
+ _objc_msgSend$setInvalidatedUpdate:withResponse:
+ _objc_msgSend$setUIConfigurationOptionsValue:
- -[CAFASCTree routeSharingOEMName]
- -[CAFSystemInformation hasUserVisibleNavigationAidedDrivingFeatureName]
- -[CAFSystemInformation hasUserVisibleNavigationAidedDrivingFeatureShortName]
- -[CAFSystemInformation navigationAidedDrivingActiveCharacteristic]
- -[CAFSystemInformation navigationAidedDrivingActive]
- -[CAFSystemInformation registeredForNavigationAidedDrivingActive]
- -[CAFSystemInformation registeredForUserVisibleNavigationAidedDrivingFeatureName]
- -[CAFSystemInformation registeredForUserVisibleNavigationAidedDrivingFeatureShortName]
- -[CAFSystemInformation registeredForUserVisibleVehicleManufacturer]
- -[CAFSystemInformation registeredForUserVisibleVehicleModel]
- -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureNameCharacteristic]
- -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureName]
- -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureShortNameCharacteristic]
- -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureShortName]
- -[CAFSystemInformation userVisibleVehicleManufacturerCharacteristic]
- -[CAFSystemInformation userVisibleVehicleManufacturer]
- -[CAFSystemInformation userVisibleVehicleModelCharacteristic]
- -[CAFSystemInformation userVisibleVehicleModel]
- GCC_except_table17
- GCC_except_table18
- GCC_except_table61
- _CAFCharacteristicTypeNavigationAidedDrivingActive
- _CAFCharacteristicTypeUserVisibleNavigationAidedDrivingFeatureName
- _CAFCharacteristicTypeUserVisibleNavigationAidedDrivingFeatureShortName
- _CAFCharacteristicTypeUserVisibleVehicleManufacturer
- _CAFCharacteristicTypeUserVisibleVehicleModel
- _OBJC_IVAR_$_CAFASCTree._routeSharingOEMName
- __OBJC_$_INSTANCE_METHODS_CAFCar(CAFNowPlaying|Accessories)
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.241
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.241.cold.1
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.242
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.242.cold.1
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.242.cold.2
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.243
- ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.116
- ___block_literal_global.1671
- ___block_literal_global.1673
- ___block_literal_global.717
- ___block_literal_global.719
- _objc_msgSend$hasUserVisibleNavigationAidedDrivingFeatureName
- _objc_msgSend$hasUserVisibleNavigationAidedDrivingFeatureShortName
- _objc_msgSend$navigationAidedDrivingActive
- _objc_msgSend$navigationAidedDrivingActiveCharacteristic
- _objc_msgSend$systemInformationService:didUpdateNavigationAidedDrivingActive:
- _objc_msgSend$systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureName:
- _objc_msgSend$systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureShortName:
- _objc_msgSend$systemInformationService:didUpdateUserVisibleVehicleManufacturer:
- _objc_msgSend$systemInformationService:didUpdateUserVisibleVehicleModel:
- _objc_msgSend$userVisibleNavigationAidedDrivingFeatureName
- _objc_msgSend$userVisibleNavigationAidedDrivingFeatureNameCharacteristic
- _objc_msgSend$userVisibleNavigationAidedDrivingFeatureShortName
- _objc_msgSend$userVisibleNavigationAidedDrivingFeatureShortNameCharacteristic
- _objc_msgSend$userVisibleVehicleManufacturer
- _objc_msgSend$userVisibleVehicleManufacturerCharacteristic
- _objc_msgSend$userVisibleVehicleModel
- _objc_msgSend$userVisibleVehicleModelCharacteristic
CStrings:
+ "%{public}@ invalidatedUpdate response error=%@"
+ "%{public}@: invalidatedUpdate=%{public}@"
+ "0x000000001E000001"
+ "0x0000000024000003"
+ "0x000000004500001D"
+ "0x0000000051000006"
+ "0x0000000051000007"
+ "<CAFBatchUpdate: %p count=%ld> items=%@"
+ "<CAFBatchUpdateItem: %p pluginID=%@ priority=%@ instanceID=%@ value=%@>"
+ "@\"CAFBatchUpdate\""
+ "CAFBatchUpdate"
+ "CAFBatchUpdateItem"
+ "CAFDriverAssistanceSystem"
+ "CAFDriverAssistanceSystemObserver"
+ "CAFLaneKeepAlertCharacteristic"
+ "CAFLaneKeepAlerts"
+ "CAFLaneKeepAlertsObserver"
+ "DriverAssistanceModeIdentifier"
+ "DriverAssistanceSystem"
+ "LaneKeepAlert"
+ "LaneKeepAlertLeft"
+ "LaneKeepAlertRight"
+ "LaneKeepAlerts"
+ "T@\"CAFBatchUpdate\",C,N,V_invalidatedUpdate"
+ "T@\"CAFDriverAssistanceSystem\",R,N"
+ "T@\"CAFLaneKeepAlertCharacteristic\",R,N"
+ "T@\"CAFLaneKeepAlerts\",R,N"
+ "T@\"NSArray\",R,C,N,V_items"
+ "T@\"NSString\",R,N,V_routeSharingUserVisibleBrand"
+ "_invalidatedUpdate"
+ "_items"
+ "_routeSharingUserVisibleBrand"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "driverAssistanceModeIdentifier"
+ "driverAssistanceModeIdentifierCharacteristic"
+ "driverAssistanceSystem"
+ "driverAssistanceSystemService"
+ "driverAssistanceSystemService:didUpdateDriverAssistanceModeIdentifier:"
+ "hasLaneKeepAlertLeft"
+ "hasLaneKeepAlertRight"
+ "initWithItems:"
+ "initWithService:characteristicType:value:"
+ "invalidatedUpdate"
+ "items"
+ "laneKeepAlertLeft"
+ "laneKeepAlertLeftCharacteristic"
+ "laneKeepAlertRight"
+ "laneKeepAlertRightCharacteristic"
+ "laneKeepAlertValue"
+ "laneKeepAlerts"
+ "laneKeepAlertsService"
+ "laneKeepAlertsService:didUpdateLaneKeepAlertLeft:"
+ "laneKeepAlertsService:didUpdateLaneKeepAlertRight:"
+ "registeredForDriverAssistanceModeIdentifier"
+ "registeredForLaneKeepAlertLeft"
+ "registeredForLaneKeepAlertRight"
+ "routeSharingUserVisibleBrand"
+ "setInvalidatedUpdate:"
+ "setInvalidatedUpdate:withResponse:"
+ "setLaneKeepAlertValue:"
+ "setUiConfigurationOptions:"
+ "v28@0:8@\"CAFLaneKeepAlerts\"16C24"
+ "v32@0:8@\"CAFBatchUpdate\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"CAFDriverAssistanceSystem\"16@\"NSString\"24"
- "0x000000004500010B"
- "0x000000004500010F"
- "0x0000000045000112"
- "0x0000000045000114"
- "0x0000000045000115"
- "NavigationAidedDrivingActive"
- "T@\"CAFUIConfigurationOptions\",R,N"
- "T@\"NSString\",R,N,V_routeSharingOEMName"
- "UserVisibleNavigationAidedDrivingFeatureName"
- "UserVisibleNavigationAidedDrivingFeatureShortName"
- "UserVisibleVehicleManufacturer"
- "UserVisibleVehicleModel"
- "WaypointAdded"
- "WaypointRemoved"
- "_routeSharingOEMName"
- "hasUserVisibleNavigationAidedDrivingFeatureName"
- "hasUserVisibleNavigationAidedDrivingFeatureShortName"
- "navigationAidedDrivingActive"
- "navigationAidedDrivingActiveCharacteristic"
- "registeredForNavigationAidedDrivingActive"
- "registeredForUserVisibleNavigationAidedDrivingFeatureName"
- "registeredForUserVisibleNavigationAidedDrivingFeatureShortName"
- "registeredForUserVisibleVehicleManufacturer"
- "registeredForUserVisibleVehicleModel"
- "routeSharingOEMName"
- "systemInformationService:didUpdateNavigationAidedDrivingActive:"
- "systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureName:"
- "systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureShortName:"
- "systemInformationService:didUpdateUserVisibleVehicleManufacturer:"
- "systemInformationService:didUpdateUserVisibleVehicleModel:"
- "userVisibleNavigationAidedDrivingFeatureName"
- "userVisibleNavigationAidedDrivingFeatureNameCharacteristic"
- "userVisibleNavigationAidedDrivingFeatureShortName"
- "userVisibleNavigationAidedDrivingFeatureShortNameCharacteristic"
- "userVisibleVehicleManufacturer"
- "userVisibleVehicleManufacturerCharacteristic"
- "userVisibleVehicleModel"
- "userVisibleVehicleModelCharacteristic"
- "v28@0:8@\"CAFSystemInformation\"16B24"

```
