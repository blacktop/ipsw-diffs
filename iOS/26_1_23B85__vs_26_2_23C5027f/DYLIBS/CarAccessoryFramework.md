## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-488.18.3.2.0
-  __TEXT.__text: 0xf8ef8
-  __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x1856c
-  __TEXT.__const: 0x148
-  __TEXT.__gcc_except_tab: 0x670
-  __TEXT.__cstring: 0x7211
-  __TEXT.__oslogstring: 0x352a
+488.25.0.0.0
+  __TEXT.__text: 0x10077c
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x18e54
+  __TEXT.__const: 0x158
+  __TEXT.__gcc_except_tab: 0x694
+  __TEXT.__cstring: 0x7827
+  __TEXT.__oslogstring: 0x3693
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3cf8
-  __TEXT.__objc_classname: 0x3dd6
-  __TEXT.__objc_methname: 0x1d187
-  __TEXT.__objc_methtype: 0x4645
-  __TEXT.__objc_stubs: 0x12860
-  __DATA_CONST.__got: 0xc10
-  __DATA_CONST.__const: 0x23c8
-  __DATA_CONST.__objc_classlist: 0xcc0
-  __DATA_CONST.__objc_nlclslist: 0x958
+  __TEXT.__unwind_info: 0x3e70
+  __TEXT.__objc_classname: 0x3f7f
+  __TEXT.__objc_methname: 0x1e383
+  __TEXT.__objc_methtype: 0x4782
+  __TEXT.__objc_stubs: 0x14040
+  __DATA_CONST.__got: 0xc60
+  __DATA_CONST.__const: 0x2588
+  __DATA_CONST.__objc_classlist: 0xd18
+  __DATA_CONST.__objc_nlclslist: 0x9a0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x6b8
+  __DATA_CONST.__objc_protolist: 0x6d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7198
-  __DATA_CONST.__objc_protorefs: 0x658
-  __DATA_CONST.__objc_superrefs: 0x1178
-  __DATA_CONST.__objc_arraydata: 0xaea8
-  __AUTH_CONST.__auth_got: 0x348
+  __DATA_CONST.__objc_selrefs: 0x74e0
+  __DATA_CONST.__objc_protorefs: 0x670
+  __DATA_CONST.__objc_superrefs: 0x11f0
+  __DATA_CONST.__objc_arraydata: 0xb308
+  __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0xce40
-  __AUTH_CONST.__objc_const: 0x4f4b8
+  __AUTH_CONST.__cfstring: 0xd600
+  __AUTH_CONST.__objc_const: 0x50c98
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_intobj: 0x510
-  __AUTH_CONST.__objc_dictobj: 0x5e38
+  __AUTH_CONST.__objc_intobj: 0x528
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x23a0
-  __DATA.__objc_ivar: 0x5f0
-  __DATA.__data: 0x50c0
+  __AUTH_CONST.__objc_dictobj: 0x5f78
+  __AUTH.__objc_data: 0x2760
+  __DATA.__objc_ivar: 0x618
+  __DATA.__data: 0x51e0
   __DATA.__bss: 0x300
-  __DATA_DIRTY.__objc_data: 0x5be0
+  __DATA_DIRTY.__objc_data: 0x5b90
   __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65B25A5E-D298-303E-B583-84AD23F1BD5E
-  Functions: 7506
-  Symbols:   24643
-  CStrings:  9315
+  UUID: 43F47AED-4D77-304E-9B4B-8144FD643068
+  Functions: 7679
+  Symbols:   25347
+  CStrings:  9597
 
Symbols:
+ +[CAFASCTree supportsSecureCoding]
+ +[CAFASCTreeNode supportsSecureCoding]
+ +[CAFAccessory accessoryWithCar:pluginID:handlerName:config:]
+ +[CAFEnergyGaugeUI load]
+ +[CAFEnergyGaugeUI observerProtocol]
+ +[CAFEnergyGaugeUI serviceIdentifier]
+ +[CAFRerouteReasonCharacteristic load]
+ +[CAFRerouteReasonCharacteristic primaryCharacteristicFormat]
+ +[CAFRerouteReasonCharacteristic secondaryCharacteristicFormats]
+ +[CAFRouteSharing load]
+ +[CAFRouteSharing observerProtocol]
+ +[CAFRouteSharing serviceIdentifier]
+ +[CAFRouteSourceCharacteristic load]
+ +[CAFRouteSourceCharacteristic primaryCharacteristicFormat]
+ +[CAFRouteSourceCharacteristic secondaryCharacteristicFormats]
+ +[CAFRouteStatus load]
+ +[CAFRouteStatus observerProtocol]
+ +[CAFRouteStatus serviceIdentifier]
+ +[CAFSharingStateCharacteristic load]
+ +[CAFSharingStateCharacteristic primaryCharacteristicFormat]
+ +[CAFSharingStateCharacteristic secondaryCharacteristicFormats]
+ +[CAFSystemInformation load]
+ +[CAFSystemInformation observerProtocol]
+ +[CAFSystemInformation serviceIdentifier]
+ +[CAFUIConfigurationOptionCharacteristic load]
+ +[CAFUIConfigurationOptionCharacteristic primaryCharacteristicFormat]
+ +[CAFUIConfigurationOptionCharacteristic secondaryCharacteristicFormats]
+ +[CAFUIConfigurationOptions uIConfigurationOptionsWithArray:]
+ +[CAFUIConfigurationOptions uIConfigurationOptionsWithUIConfigurationOptions:]
+ +[CAFUIConfigurationOptionsCharacteristic load]
+ +[CAFUIConfigurationOptionsCharacteristic primaryCharacteristicFormat]
+ +[CAFUIConfigurationOptionsCharacteristic secondaryCharacteristicFormats]
+ +[CAFUIEmphasizedConsumptionGaugeCharacteristic load]
+ +[CAFUIEmphasizedConsumptionGaugeCharacteristic primaryCharacteristicFormat]
+ +[CAFUIEmphasizedConsumptionGaugeCharacteristic secondaryCharacteristicFormats]
+ +[CAFUIEmphasizedEnergyLevelGaugeCharacteristic load]
+ +[CAFUIEmphasizedEnergyLevelGaugeCharacteristic primaryCharacteristicFormat]
+ +[CAFUIEmphasizedEnergyLevelGaugeCharacteristic secondaryCharacteristicFormats]
+ -[CAFASCTree encodeWithCoder:]
+ -[CAFASCTree initEmpty]
+ -[CAFASCTree initWithCarSessionConfiguration:]
+ -[CAFASCTree initWithCoder:]
+ -[CAFASCTree routeSharingOEMName]
+ -[CAFASCTree routeSharingUserVisibleReason]
+ -[CAFASCTreeNode encodeWithCoder:]
+ -[CAFASCTreeNode initWithCoder:]
+ -[CAFAccessory handlerName]
+ -[CAFAccessory initWithCar:pluginID:handlerName:config:]
+ -[CAFAccessory initWithCar:pluginID:handlerName:config:].cold.1
+ -[CAFAccessory initWithCar:pluginID:handlerName:config:].cold.2
+ -[CAFAccessory initWithCar:pluginID:handlerName:config:].cold.3
+ -[CAFAutoClimateControl autoModeIntensityIndexCharacteristic]
+ -[CAFAutoClimateControl autoModeIntensityIndexDisabled]
+ -[CAFAutoClimateControl autoModeIntensityIndexInvalid]
+ -[CAFAutoClimateControl autoModeIntensityIndexRange]
+ -[CAFAutoClimateControl autoModeIntensityIndexRestricted]
+ -[CAFAutoClimateControl autoModeIntensityIndex]
+ -[CAFAutoClimateControl hasAutoModeIntensityIndex]
+ -[CAFAutoClimateControl hasIntensities]
+ -[CAFAutoClimateControl intensitiesCharacteristic]
+ -[CAFAutoClimateControl intensities]
+ -[CAFAutoClimateControl registeredForAutoModeIntensities]
+ -[CAFAutoClimateControl registeredForAutoModeIntensityIndex]
+ -[CAFAutoClimateControl setAutoModeIntensityIndex:]
+ -[CAFAutoClimateControl setIntensities:]
+ -[CAFCabin hvacOnDisabled]
+ -[CAFCar accessoriesForCategory:withHandler:]
+ -[CAFCarConfiguration configureDisabledASCFromSessionConfig:featureDenyList:]
+ -[CAFCarConfiguration configureDisabledASCFromSessionConfig:featureDenyList:].cold.1
+ -[CAFCarConfiguration disabledASC]
+ -[CAFCarConfiguration initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:]
+ -[CAFCarConfiguration pluginNameDictionary]
+ -[CAFCarConfiguration pluginNameForIdentifier:]
+ -[CAFCarConfiguration setDisabledASC:]
+ -[CAFCarConfiguration updatePluginConfigs:]
+ -[CAFCarConfiguration updatePluginConfigs:].cold.1
+ -[CAFEnergyGaugeUI _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFEnergyGaugeUI addObserver:]
+ -[CAFEnergyGaugeUI hasUiEmphasizedConsumptionGauge]
+ -[CAFEnergyGaugeUI hasUiEmphasizedEnergyLevelGauge]
+ -[CAFEnergyGaugeUI name]
+ -[CAFEnergyGaugeUI registerObserver:]
+ -[CAFEnergyGaugeUI registeredForUIEmphasizedConsumptionGauge]
+ -[CAFEnergyGaugeUI registeredForUIEmphasizedEnergyLevelGauge]
+ -[CAFEnergyGaugeUI removeObserver:]
+ -[CAFEnergyGaugeUI uiEmphasizedConsumptionGaugeCharacteristic]
+ -[CAFEnergyGaugeUI uiEmphasizedConsumptionGauge]
+ -[CAFEnergyGaugeUI uiEmphasizedEnergyLevelGaugeCharacteristic]
+ -[CAFEnergyGaugeUI uiEmphasizedEnergyLevelGauge]
+ -[CAFEnergyGaugeUI unregisterObserver:]
+ -[CAFNavigation routeSharingService]
+ -[CAFNavigation routeSharing]
+ -[CAFNavigation routeStatusService]
+ -[CAFNavigation routeStatus]
+ -[CAFNavigation systemInformationService]
+ -[CAFNavigation systemInformation]
+ -[CAFNowPlayingSnapshot initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:mediaItemIdentifier:]
+ -[CAFNowPlayingSnapshot mediaItemIdentifier]
+ -[CAFRerouteReasonCharacteristic formattedValue]
+ -[CAFRerouteReasonCharacteristic rerouteReasonValue]
+ -[CAFRerouteReasonCharacteristic setRerouteReasonValue:]
+ -[CAFRouteSharing _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFRouteSharing addObserver:]
+ -[CAFRouteSharing applicationEnabledCharacteristic]
+ -[CAFRouteSharing applicationEnabledInvalid]
+ -[CAFRouteSharing applicationEnabled]
+ -[CAFRouteSharing hasLegs]
+ -[CAFRouteSharing legsCharacteristic]
+ -[CAFRouteSharing legsInvalid]
+ -[CAFRouteSharing legs]
+ -[CAFRouteSharing name]
+ -[CAFRouteSharing registerObserver:]
+ -[CAFRouteSharing registeredForApplicationEnabled]
+ -[CAFRouteSharing registeredForLegs]
+ -[CAFRouteSharing registeredForSharingState]
+ -[CAFRouteSharing registeredForUserEnabled]
+ -[CAFRouteSharing registeredForUserVisibleReason]
+ -[CAFRouteSharing registeredForVehicleEnabled]
+ -[CAFRouteSharing removeObserver:]
+ -[CAFRouteSharing setApplicationEnabled:]
+ -[CAFRouteSharing setLegs:]
+ -[CAFRouteSharing setSharingState:]
+ -[CAFRouteSharing setUserEnabled:]
+ -[CAFRouteSharing sharingStateCharacteristic]
+ -[CAFRouteSharing sharingState]
+ -[CAFRouteSharing unregisterObserver:]
+ -[CAFRouteSharing userEnabledCharacteristic]
+ -[CAFRouteSharing userEnabledInvalid]
+ -[CAFRouteSharing userEnabled]
+ -[CAFRouteSharing userVisibleReasonCharacteristic]
+ -[CAFRouteSharing userVisibleReason]
+ -[CAFRouteSharing vehicleEnabledCharacteristic]
+ -[CAFRouteSharing vehicleEnabled]
+ -[CAFRouteSourceCharacteristic formattedValue]
+ -[CAFRouteSourceCharacteristic routeSourceValue]
+ -[CAFRouteSourceCharacteristic setRouteSourceValue:]
+ -[CAFRouteStatus _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFRouteStatus addObserver:]
+ -[CAFRouteStatus destinationCharacteristic]
+ -[CAFRouteStatus destinationInvalid]
+ -[CAFRouteStatus destination]
+ -[CAFRouteStatus geodeticSystemCharacteristic]
+ -[CAFRouteStatus geodeticSystem]
+ -[CAFRouteStatus hasRerouteReason]
+ -[CAFRouteStatus name]
+ -[CAFRouteStatus originCharacteristic]
+ -[CAFRouteStatus originInvalid]
+ -[CAFRouteStatus origin]
+ -[CAFRouteStatus registerObserver:]
+ -[CAFRouteStatus registeredForDestination]
+ -[CAFRouteStatus registeredForGeodeticSystem]
+ -[CAFRouteStatus registeredForOrigin]
+ -[CAFRouteStatus registeredForRerouteReason]
+ -[CAFRouteStatus registeredForRouteState]
+ -[CAFRouteStatus registeredForUserVisibleApplicationName]
+ -[CAFRouteStatus removeObserver:]
+ -[CAFRouteStatus rerouteReasonCharacteristic]
+ -[CAFRouteStatus rerouteReason]
+ -[CAFRouteStatus routeStateCharacteristic]
+ -[CAFRouteStatus routeState]
+ -[CAFRouteStatus setDestination:]
+ -[CAFRouteStatus setGeodeticSystem:]
+ -[CAFRouteStatus setOrigin:]
+ -[CAFRouteStatus setRerouteReason:]
+ -[CAFRouteStatus setRouteState:]
+ -[CAFRouteStatus setUserVisibleApplicationName:]
+ -[CAFRouteStatus unregisterObserver:]
+ -[CAFRouteStatus userVisibleApplicationNameCharacteristic]
+ -[CAFRouteStatus userVisibleApplicationNameInvalid]
+ -[CAFRouteStatus userVisibleApplicationName]
+ -[CAFSharingStateCharacteristic formattedValue]
+ -[CAFSharingStateCharacteristic setSharingStateValue:]
+ -[CAFSharingStateCharacteristic sharingStateValue]
+ -[CAFSystemInformation _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFSystemInformation addObserver:]
+ -[CAFSystemInformation hasUserVisibleNavigationAidedDrivingFeatureName]
+ -[CAFSystemInformation hasUserVisibleNavigationAidedDrivingFeatureShortName]
+ -[CAFSystemInformation name]
+ -[CAFSystemInformation navigationAidedDrivingActiveCharacteristic]
+ -[CAFSystemInformation navigationAidedDrivingActive]
+ -[CAFSystemInformation registerObserver:]
+ -[CAFSystemInformation registeredForNavigationAidedDrivingActive]
+ -[CAFSystemInformation registeredForRouteSource]
+ -[CAFSystemInformation registeredForUserVisibleNavigationAidedDrivingFeatureName]
+ -[CAFSystemInformation registeredForUserVisibleNavigationAidedDrivingFeatureShortName]
+ -[CAFSystemInformation registeredForUserVisibleNavigationSystemName]
+ -[CAFSystemInformation registeredForUserVisibleVehicleBrand]
+ -[CAFSystemInformation registeredForUserVisibleVehicleManufacturer]
+ -[CAFSystemInformation registeredForUserVisibleVehicleModel]
+ -[CAFSystemInformation removeObserver:]
+ -[CAFSystemInformation routeSourceCharacteristic]
+ -[CAFSystemInformation routeSource]
+ -[CAFSystemInformation unregisterObserver:]
+ -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureNameCharacteristic]
+ -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureName]
+ -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureShortNameCharacteristic]
+ -[CAFSystemInformation userVisibleNavigationAidedDrivingFeatureShortName]
+ -[CAFSystemInformation userVisibleNavigationSystemNameCharacteristic]
+ -[CAFSystemInformation userVisibleNavigationSystemName]
+ -[CAFSystemInformation userVisibleVehicleBrandCharacteristic]
+ -[CAFSystemInformation userVisibleVehicleBrand]
+ -[CAFSystemInformation userVisibleVehicleManufacturerCharacteristic]
+ -[CAFSystemInformation userVisibleVehicleManufacturer]
+ -[CAFSystemInformation userVisibleVehicleModelCharacteristic]
+ -[CAFSystemInformation userVisibleVehicleModel]
+ -[CAFUIConfiguration registeredForUIConfigurationOptions]
+ -[CAFUIConfiguration uiConfigurationOptionsCharacteristic]
+ -[CAFUIConfiguration uiConfigurationOptions]
+ -[CAFUIConfigurationOption .cxx_destruct]
+ -[CAFUIConfigurationOption description]
+ -[CAFUIConfigurationOption dictionaryRepresentation]
+ -[CAFUIConfigurationOption identifier]
+ -[CAFUIConfigurationOption initWithDictionary:]
+ -[CAFUIConfigurationOption initWithIdentifier:value:]
+ -[CAFUIConfigurationOption value]
+ -[CAFUIConfigurationOptionCharacteristic formattedValue]
+ -[CAFUIConfigurationOptionCharacteristic setUIConfigurationOptionValue:]
+ -[CAFUIConfigurationOptionCharacteristic uIConfigurationOptionValue]
+ -[CAFUIConfigurationOptions .cxx_destruct]
+ -[CAFUIConfigurationOptions arrayRepresentation]
+ -[CAFUIConfigurationOptions countByEnumeratingWithState:objects:count:]
+ -[CAFUIConfigurationOptions formattedValue]
+ -[CAFUIConfigurationOptions initWithArray:]
+ -[CAFUIConfigurationOptions initWithUIConfigurationOptions:]
+ -[CAFUIConfigurationOptions objectAtIndex:]
+ -[CAFUIConfigurationOptions objectAtIndexedSubscript:]
+ -[CAFUIConfigurationOptions parseError]
+ -[CAFUIConfigurationOptions uIConfigurationOptions]
+ -[CAFUIConfigurationOptionsCharacteristic formattedValue]
+ -[CAFUIConfigurationOptionsCharacteristic setUIConfigurationOptionsValue:]
+ -[CAFUIConfigurationOptionsCharacteristic uIConfigurationOptionsValue]
+ -[CAFUIControl energyGaugeUIService]
+ -[CAFUIControl energyGaugeUI]
+ -[CAFUIEmphasizedConsumptionGaugeCharacteristic formattedValue]
+ -[CAFUIEmphasizedConsumptionGaugeCharacteristic setUIEmphasizedConsumptionGaugeValue:]
+ -[CAFUIEmphasizedConsumptionGaugeCharacteristic uIEmphasizedConsumptionGaugeValue]
+ -[CAFUIEmphasizedEnergyLevelGaugeCharacteristic formattedValue]
+ -[CAFUIEmphasizedEnergyLevelGaugeCharacteristic setUIEmphasizedEnergyLevelGaugeValue:]
+ -[CAFUIEmphasizedEnergyLevelGaugeCharacteristic uIEmphasizedEnergyLevelGaugeValue]
+ GCC_except_table42
+ _CAFAccessoryTypeNULL
+ _CAFCharacteristicTypeAutoModeIntensities
+ _CAFCharacteristicTypeAutoModeIntensityIndex
+ _CAFCharacteristicTypeNULL
+ _CAFCharacteristicTypeNavigationAidedDrivingActive
+ _CAFCharacteristicTypeRerouteReason
+ _CAFCharacteristicTypeRouteSource
+ _CAFCharacteristicTypeSharingState
+ _CAFCharacteristicTypeUIConfigurationOptions
+ _CAFCharacteristicTypeUIEmphasizedConsumptionGauge
+ _CAFCharacteristicTypeUIEmphasizedEnergyLevelGauge
+ _CAFCharacteristicTypeUserVisibleNavigationAidedDrivingFeatureName
+ _CAFCharacteristicTypeUserVisibleNavigationAidedDrivingFeatureShortName
+ _CAFCharacteristicTypeUserVisibleNavigationSystemName
+ _CAFCharacteristicTypeUserVisibleReason
+ _CAFCharacteristicTypeUserVisibleVehicleBrand
+ _CAFCharacteristicTypeUserVisibleVehicleManufacturer
+ _CAFCharacteristicTypeUserVisibleVehicleModel
+ _CAFControlTypeNULL
+ _CAFServiceTypeEnergyGaugeUI
+ _CAFServiceTypeNULL
+ _CAFServiceTypeRouteSharing
+ _CAFServiceTypeRouteStatus
+ _CAFServiceTypeSystemInformation
+ _CARPKeyUIConfigurationOptionIdentifier
+ _CARPKeyUIConfigurationOptionValue
+ _NSStringFromRerouteReason
+ _NSStringFromRouteSource
+ _NSStringFromSharingState
+ _NSStringFromUIEmphasizedConsumptionGauge
+ _NSStringFromUIEmphasizedEnergyLevelGauge
+ _OBJC_CLASS_$_CAFEnergyGaugeUI
+ _OBJC_CLASS_$_CAFRerouteReasonCharacteristic
+ _OBJC_CLASS_$_CAFRouteSharing
+ _OBJC_CLASS_$_CAFRouteSourceCharacteristic
+ _OBJC_CLASS_$_CAFRouteStatus
+ _OBJC_CLASS_$_CAFSharingStateCharacteristic
+ _OBJC_CLASS_$_CAFSystemInformation
+ _OBJC_CLASS_$_CAFUIConfigurationOption
+ _OBJC_CLASS_$_CAFUIConfigurationOptionCharacteristic
+ _OBJC_CLASS_$_CAFUIConfigurationOptions
+ _OBJC_CLASS_$_CAFUIConfigurationOptionsCharacteristic
+ _OBJC_CLASS_$_CAFUIEmphasizedConsumptionGaugeCharacteristic
+ _OBJC_CLASS_$_CAFUIEmphasizedEnergyLevelGaugeCharacteristic
+ _OBJC_IVAR_$_CAFASCTree._routeSharingOEMName
+ _OBJC_IVAR_$_CAFASCTree._routeSharingUserVisibleReason
+ _OBJC_IVAR_$_CAFAccessory._handlerName
+ _OBJC_IVAR_$_CAFCarConfiguration._disabledASC
+ _OBJC_IVAR_$_CAFCarConfiguration._pluginNameDictionary
+ _OBJC_IVAR_$_CAFNowPlayingSnapshot._mediaItemIdentifier
+ _OBJC_IVAR_$_CAFUIConfigurationOption._identifier
+ _OBJC_IVAR_$_CAFUIConfigurationOption._value
+ _OBJC_IVAR_$_CAFUIConfigurationOptions._parseError
+ _OBJC_IVAR_$_CAFUIConfigurationOptions._uIConfigurationOptions
+ _OBJC_METACLASS_$_CAFEnergyGaugeUI
+ _OBJC_METACLASS_$_CAFRerouteReasonCharacteristic
+ _OBJC_METACLASS_$_CAFRouteSharing
+ _OBJC_METACLASS_$_CAFRouteSourceCharacteristic
+ _OBJC_METACLASS_$_CAFRouteStatus
+ _OBJC_METACLASS_$_CAFSharingStateCharacteristic
+ _OBJC_METACLASS_$_CAFSystemInformation
+ _OBJC_METACLASS_$_CAFUIConfigurationOption
+ _OBJC_METACLASS_$_CAFUIConfigurationOptionCharacteristic
+ _OBJC_METACLASS_$_CAFUIConfigurationOptions
+ _OBJC_METACLASS_$_CAFUIConfigurationOptionsCharacteristic
+ _OBJC_METACLASS_$_CAFUIEmphasizedConsumptionGaugeCharacteristic
+ _OBJC_METACLASS_$_CAFUIEmphasizedEnergyLevelGaugeCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFEnergyGaugeUI
+ __OBJC_$_CLASS_METHODS_CAFRerouteReasonCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFRouteSharing
+ __OBJC_$_CLASS_METHODS_CAFRouteSourceCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFRouteStatus
+ __OBJC_$_CLASS_METHODS_CAFSharingStateCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFSystemInformation
+ __OBJC_$_CLASS_METHODS_CAFUIConfigurationOptionCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFUIConfigurationOptions
+ __OBJC_$_CLASS_METHODS_CAFUIConfigurationOptionsCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFUIEmphasizedConsumptionGaugeCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFUIEmphasizedEnergyLevelGaugeCharacteristic
+ __OBJC_$_CLASS_PROP_LIST_CAFASCTree
+ __OBJC_$_CLASS_PROP_LIST_CAFASCTreeNode
+ __OBJC_$_INSTANCE_METHODS_CAFCar(CAFNowPlaying|Accessories)
+ __OBJC_$_INSTANCE_METHODS_CAFEnergyGaugeUI
+ __OBJC_$_INSTANCE_METHODS_CAFRerouteReasonCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFRouteSharing
+ __OBJC_$_INSTANCE_METHODS_CAFRouteSourceCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFRouteStatus
+ __OBJC_$_INSTANCE_METHODS_CAFSharingStateCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFSystemInformation
+ __OBJC_$_INSTANCE_METHODS_CAFUIConfigurationOption
+ __OBJC_$_INSTANCE_METHODS_CAFUIConfigurationOptionCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFUIConfigurationOptions
+ __OBJC_$_INSTANCE_METHODS_CAFUIConfigurationOptionsCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFUIEmphasizedConsumptionGaugeCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFUIEmphasizedEnergyLevelGaugeCharacteristic
+ __OBJC_$_INSTANCE_VARIABLES_CAFUIConfigurationOption
+ __OBJC_$_INSTANCE_VARIABLES_CAFUIConfigurationOptions
+ __OBJC_$_PROP_LIST_CAFEnergyGaugeUI
+ __OBJC_$_PROP_LIST_CAFRerouteReasonCharacteristic
+ __OBJC_$_PROP_LIST_CAFRouteSharing
+ __OBJC_$_PROP_LIST_CAFRouteSourceCharacteristic
+ __OBJC_$_PROP_LIST_CAFRouteStatus
+ __OBJC_$_PROP_LIST_CAFSharingStateCharacteristic
+ __OBJC_$_PROP_LIST_CAFSystemInformation
+ __OBJC_$_PROP_LIST_CAFUIConfigurationOption
+ __OBJC_$_PROP_LIST_CAFUIConfigurationOptionCharacteristic
+ __OBJC_$_PROP_LIST_CAFUIConfigurationOptions
+ __OBJC_$_PROP_LIST_CAFUIConfigurationOptionsCharacteristic
+ __OBJC_$_PROP_LIST_CAFUIEmphasizedConsumptionGaugeCharacteristic
+ __OBJC_$_PROP_LIST_CAFUIEmphasizedEnergyLevelGaugeCharacteristic
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFEnergyGaugeUIObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteSharingObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteStatusObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFSystemInformationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFEnergyGaugeUIObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteSharingObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteStatusObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFSystemInformationObserver
+ __OBJC_$_PROTOCOL_REFS_CAFEnergyGaugeUIObserver
+ __OBJC_$_PROTOCOL_REFS_CAFRouteSharingObserver
+ __OBJC_$_PROTOCOL_REFS_CAFRouteStatusObserver
+ __OBJC_$_PROTOCOL_REFS_CAFSystemInformationObserver
+ __OBJC_CLASS_PROTOCOLS_$_CAFASCTree
+ __OBJC_CLASS_PROTOCOLS_$_CAFASCTreeNode
+ __OBJC_CLASS_PROTOCOLS_$_CAFUIConfigurationOptions
+ __OBJC_CLASS_RO_$_CAFEnergyGaugeUI
+ __OBJC_CLASS_RO_$_CAFRerouteReasonCharacteristic
+ __OBJC_CLASS_RO_$_CAFRouteSharing
+ __OBJC_CLASS_RO_$_CAFRouteSourceCharacteristic
+ __OBJC_CLASS_RO_$_CAFRouteStatus
+ __OBJC_CLASS_RO_$_CAFSharingStateCharacteristic
+ __OBJC_CLASS_RO_$_CAFSystemInformation
+ __OBJC_CLASS_RO_$_CAFUIConfigurationOption
+ __OBJC_CLASS_RO_$_CAFUIConfigurationOptionCharacteristic
+ __OBJC_CLASS_RO_$_CAFUIConfigurationOptions
+ __OBJC_CLASS_RO_$_CAFUIConfigurationOptionsCharacteristic
+ __OBJC_CLASS_RO_$_CAFUIEmphasizedConsumptionGaugeCharacteristic
+ __OBJC_CLASS_RO_$_CAFUIEmphasizedEnergyLevelGaugeCharacteristic
+ __OBJC_LABEL_PROTOCOL_$_CAFEnergyGaugeUIObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFRouteSharingObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFRouteStatusObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFSystemInformationObserver
+ __OBJC_METACLASS_RO_$_CAFEnergyGaugeUI
+ __OBJC_METACLASS_RO_$_CAFRerouteReasonCharacteristic
+ __OBJC_METACLASS_RO_$_CAFRouteSharing
+ __OBJC_METACLASS_RO_$_CAFRouteSourceCharacteristic
+ __OBJC_METACLASS_RO_$_CAFRouteStatus
+ __OBJC_METACLASS_RO_$_CAFSharingStateCharacteristic
+ __OBJC_METACLASS_RO_$_CAFSystemInformation
+ __OBJC_METACLASS_RO_$_CAFUIConfigurationOption
+ __OBJC_METACLASS_RO_$_CAFUIConfigurationOptionCharacteristic
+ __OBJC_METACLASS_RO_$_CAFUIConfigurationOptions
+ __OBJC_METACLASS_RO_$_CAFUIConfigurationOptionsCharacteristic
+ __OBJC_METACLASS_RO_$_CAFUIEmphasizedConsumptionGaugeCharacteristic
+ __OBJC_METACLASS_RO_$_CAFUIEmphasizedEnergyLevelGaugeCharacteristic
+ __OBJC_PROTOCOL_$_CAFEnergyGaugeUIObserver
+ __OBJC_PROTOCOL_$_CAFRouteSharingObserver
+ __OBJC_PROTOCOL_$_CAFRouteStatusObserver
+ __OBJC_PROTOCOL_$_CAFSystemInformationObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFEnergyGaugeUIObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFRouteSharingObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFRouteStatusObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFSystemInformationObserver
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.241
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.241.cold.1
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.242
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.242.cold.1
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.242.cold.2
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.243
+ ___43-[CAFCarConfiguration updatePluginConfigs:]_block_invoke
+ ___43-[CAFCarConfiguration updatePluginConfigs:]_block_invoke.cold.1
+ ___43-[CAFCarConfiguration updatePluginConfigs:]_block_invoke.cold.2
+ ___43-[CAFUIConfigurationOptions initWithArray:]_block_invoke
+ ___43-[CAFUIConfigurationOptions initWithArray:]_block_invoke.cold.1
+ ___46-[CAFASCTree initWithCarSessionConfiguration:]_block_invoke
+ ___46-[CAFASCTree initWithCarSessionConfiguration:]_block_invoke_2
+ ___46-[CAFASCTree initWithCarSessionConfiguration:]_block_invoke_3
+ ___46-[CAFASCTree initWithCarSessionConfiguration:]_block_invoke_4
+ ___47-[CAFCarConfiguration pluginNameForIdentifier:]_block_invoke
+ ___56-[CAFAccessory initWithCar:pluginID:handlerName:config:]_block_invoke
+ ___56-[CAFAccessory initWithCar:pluginID:handlerName:config:]_block_invoke.cold.1
+ ___56-[CAFAccessory initWithCar:pluginID:handlerName:config:]_block_invoke.cold.2
+ ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.116
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e15_v32?08Q16^B24ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_40_e8_32s_e15_v32?08Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e15_v32?08Q16^B24ls32l8s40l8s48l8
+ ___block_literal_global.1671
+ ___block_literal_global.1673
+ ___block_literal_global.213
+ ___block_literal_global.231
+ ___block_literal_global.233
+ ___block_literal_global.717
+ ___block_literal_global.719
+ _kCarDataConfigurationOEMWritableKey
+ _objc_msgSend$accessoriesForCategory:withHandler:
+ _objc_msgSend$accessoryWithCar:pluginID:handlerName:config:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$aqiInvalid
+ _objc_msgSend$autoClimateControlService:didUpdateAutoModeIntensityIndex:
+ _objc_msgSend$autoClimateControlService:didUpdateIntensities:
+ _objc_msgSend$autoModeIntensityIndex
+ _objc_msgSend$autoModeIntensityIndexCharacteristic
+ _objc_msgSend$averageEnergyEfficiencyInvalid
+ _objc_msgSend$averageFuelEfficiencyInvalid
+ _objc_msgSend$averageSpeedInvalid
+ _objc_msgSend$chargingSpeedInvalid
+ _objc_msgSend$currentMediaItemIdentifierInvalid
+ _objc_msgSend$currentTemperatureInvalid
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$destinationInvalid
+ _objc_msgSend$disabledASC
+ _objc_msgSend$distanceInvalid
+ _objc_msgSend$distanceKMInvalid
+ _objc_msgSend$distanceMilesInvalid
+ _objc_msgSend$durationInvalid
+ _objc_msgSend$energyEfficiencyInvalid
+ _objc_msgSend$energyGaugeUIService
+ _objc_msgSend$energyGaugeUIService:didUpdateUiEmphasizedConsumptionGauge:
+ _objc_msgSend$energyGaugeUIService:didUpdateUiEmphasizedEnergyLevelGauge:
+ _objc_msgSend$energyInvalid
+ _objc_msgSend$featureDisabled
+ _objc_msgSend$fuelEfficiencyInvalid
+ _objc_msgSend$handlerName
+ _objc_msgSend$hasAqi
+ _objc_msgSend$hasAudioLogo
+ _objc_msgSend$hasAverageEnergyEfficiency
+ _objc_msgSend$hasAverageFuelEfficiency
+ _objc_msgSend$hasAverageSpeed
+ _objc_msgSend$hasBatteryLevelMarkerCriticalLow
+ _objc_msgSend$hasBatteryLevelMarkerLow
+ _objc_msgSend$hasBooleanNotificationInfo
+ _objc_msgSend$hasChargingModeIdentifier
+ _objc_msgSend$hasChargingSpeed
+ _objc_msgSend$hasChildrenIdentifiers
+ _objc_msgSend$hasChildrenSettingsIdentifiers
+ _objc_msgSend$hasContentURLAction
+ _objc_msgSend$hasCurrentMediaItemIdentifier
+ _objc_msgSend$hasCurrentTemperature
+ _objc_msgSend$hasDistance
+ _objc_msgSend$hasDistanceKM
+ _objc_msgSend$hasDistanceMiles
+ _objc_msgSend$hasDuration
+ _objc_msgSend$hasEnergy
+ _objc_msgSend$hasEnergyEfficiency
+ _objc_msgSend$hasEnergyEfficiencyMax
+ _objc_msgSend$hasFuelEfficiency
+ _objc_msgSend$hasFuelEfficiencyMax
+ _objc_msgSend$hasFuelLevelMarkerLow
+ _objc_msgSend$hasHistoricalNotificationUserActions
+ _objc_msgSend$hasImage
+ _objc_msgSend$hasIntensities
+ _objc_msgSend$hasJumpBackwardInterval
+ _objc_msgSend$hasJumpForwardInterval
+ _objc_msgSend$hasLegs
+ _objc_msgSend$hasMaximumSymbolName
+ _objc_msgSend$hasMediaItemImages
+ _objc_msgSend$hasMediaItems
+ _objc_msgSend$hasMinimumSymbolName
+ _objc_msgSend$hasNotificationInfo
+ _objc_msgSend$hasPowerLevelMarkerAvailableMax
+ _objc_msgSend$hasPowerLevelMarkerAvailableMin
+ _objc_msgSend$hasPowerMarkerAvailableMax
+ _objc_msgSend$hasPowerMarkerAvailableMin
+ _objc_msgSend$hasPressure
+ _objc_msgSend$hasProminenceInfo
+ _objc_msgSend$hasRotationalSpeedMarkerRedline
+ _objc_msgSend$hasSectionIdentifier
+ _objc_msgSend$hasSelectSettingEntryListNotificationInfo
+ _objc_msgSend$hasSupportedColors
+ _objc_msgSend$hasSymbolName
+ _objc_msgSend$hasSymbolNameAndColor
+ _objc_msgSend$hasTemperatureMarkerCold
+ _objc_msgSend$hasTemperatureMarkerHot
+ _objc_msgSend$hasTestArrayBool
+ _objc_msgSend$hasTestArrayData
+ _objc_msgSend$hasTestArrayFloat
+ _objc_msgSend$hasTestArrayInt16
+ _objc_msgSend$hasTestArrayInt32
+ _objc_msgSend$hasTestArrayInt64
+ _objc_msgSend$hasTestArrayInt8
+ _objc_msgSend$hasTestArrayRawData
+ _objc_msgSend$hasTestArrayString
+ _objc_msgSend$hasTestArrayUInt16
+ _objc_msgSend$hasTestArrayUInt32
+ _objc_msgSend$hasTestArrayUInt64
+ _objc_msgSend$hasTestArrayUInt8
+ _objc_msgSend$hasTestComplexArrayItemValue
+ _objc_msgSend$hasTestComplexItem
+ _objc_msgSend$hasTestComplexItemList
+ _objc_msgSend$hasTestComplexItemValue
+ _objc_msgSend$hasTestComplexItems
+ _objc_msgSend$hasTestComplexNestedItemList
+ _objc_msgSend$hasTestComplexNestedItemValue
+ _objc_msgSend$hasTestComplexNestedListItemValue
+ _objc_msgSend$hasTestData
+ _objc_msgSend$hasTestRawData
+ _objc_msgSend$hasTestString
+ _objc_msgSend$hasUiSceneOptions
+ _objc_msgSend$hasUserVisibleDescription
+ _objc_msgSend$hasUserVisibleDetailedDescription
+ _objc_msgSend$hasUserVisibleFooter
+ _objc_msgSend$hasUserVisibleFullDescription
+ _objc_msgSend$hasUserVisibleLabel
+ _objc_msgSend$hasUserVisibleNavigationAidedDrivingFeatureName
+ _objc_msgSend$hasUserVisibleNavigationAidedDrivingFeatureShortName
+ _objc_msgSend$hasUserVisibleSectionName
+ _objc_msgSend$hasUserVisibleValue
+ _objc_msgSend$hasVehicleLayout
+ _objc_msgSend$hasVehicleLayoutKey
+ _objc_msgSend$hasVehicleLogo
+ _objc_msgSend$infoResponse
+ _objc_msgSend$initEmpty
+ _objc_msgSend$initWithCar:pluginID:handlerName:config:
+ _objc_msgSend$initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:
+ _objc_msgSend$initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:mediaItemIdentifier:
+ _objc_msgSend$initWithUIConfigurationOptions:
+ _objc_msgSend$intensities
+ _objc_msgSend$intensitiesCharacteristic
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$legsInvalid
+ _objc_msgSend$mediaItemIdentifier
+ _objc_msgSend$navigationAidedDrivingActive
+ _objc_msgSend$navigationAidedDrivingActiveCharacteristic
+ _objc_msgSend$originInvalid
+ _objc_msgSend$pluginNameDictionary
+ _objc_msgSend$pluginNameForIdentifier:
+ _objc_msgSend$rerouteReason
+ _objc_msgSend$rerouteReasonCharacteristic
+ _objc_msgSend$rerouteReasonValue
+ _objc_msgSend$routeSharingMode
+ _objc_msgSend$routeSharingService
+ _objc_msgSend$routeSharingService:didUpdateApplicationEnabled:
+ _objc_msgSend$routeSharingService:didUpdateLegs:
+ _objc_msgSend$routeSharingService:didUpdateSharingState:
+ _objc_msgSend$routeSharingService:didUpdateUserEnabled:
+ _objc_msgSend$routeSharingService:didUpdateUserVisibleReason:
+ _objc_msgSend$routeSharingService:didUpdateVehicleEnabled:
+ _objc_msgSend$routeSource
+ _objc_msgSend$routeSourceCharacteristic
+ _objc_msgSend$routeSourceValue
+ _objc_msgSend$routeStatusService
+ _objc_msgSend$routeStatusService:didUpdateDestination:
+ _objc_msgSend$routeStatusService:didUpdateGeodeticSystem:
+ _objc_msgSend$routeStatusService:didUpdateOrigin:
+ _objc_msgSend$routeStatusService:didUpdateRerouteReason:
+ _objc_msgSend$routeStatusService:didUpdateRouteState:
+ _objc_msgSend$routeStatusService:didUpdateUserVisibleApplicationName:
+ _objc_msgSend$setDisabledASC:
+ _objc_msgSend$setRerouteReasonValue:
+ _objc_msgSend$setSharingStateValue:
+ _objc_msgSend$sharingState
+ _objc_msgSend$sharingStateCharacteristic
+ _objc_msgSend$sharingStateValue
+ _objc_msgSend$systemInformationService
+ _objc_msgSend$systemInformationService:didUpdateNavigationAidedDrivingActive:
+ _objc_msgSend$systemInformationService:didUpdateRouteSource:
+ _objc_msgSend$systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureName:
+ _objc_msgSend$systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureShortName:
+ _objc_msgSend$systemInformationService:didUpdateUserVisibleNavigationSystemName:
+ _objc_msgSend$systemInformationService:didUpdateUserVisibleVehicleBrand:
+ _objc_msgSend$systemInformationService:didUpdateUserVisibleVehicleManufacturer:
+ _objc_msgSend$systemInformationService:didUpdateUserVisibleVehicleModel:
+ _objc_msgSend$testArrayBoolInvalid
+ _objc_msgSend$testArrayDataInvalid
+ _objc_msgSend$testArrayFloatInvalid
+ _objc_msgSend$testArrayInt16Invalid
+ _objc_msgSend$testArrayInt32Invalid
+ _objc_msgSend$testArrayInt64Invalid
+ _objc_msgSend$testArrayInt8Invalid
+ _objc_msgSend$testArrayRawDataInvalid
+ _objc_msgSend$testArrayStringInvalid
+ _objc_msgSend$testArrayUInt16Invalid
+ _objc_msgSend$testArrayUInt32Invalid
+ _objc_msgSend$testArrayUInt64Invalid
+ _objc_msgSend$testArrayUInt8Invalid
+ _objc_msgSend$testComplexItemInvalid
+ _objc_msgSend$testComplexItemListInvalid
+ _objc_msgSend$testComplexItemValueInvalid
+ _objc_msgSend$testComplexItemsInvalid
+ _objc_msgSend$testDataInvalid
+ _objc_msgSend$testRawDataInvalid
+ _objc_msgSend$testStringInvalid
+ _objc_msgSend$uIConfigurationOptionValue
+ _objc_msgSend$uIConfigurationOptions
+ _objc_msgSend$uIConfigurationOptionsValue
+ _objc_msgSend$uIConfigurationOptionsWithArray:
+ _objc_msgSend$uIEmphasizedConsumptionGaugeValue
+ _objc_msgSend$uIEmphasizedEnergyLevelGaugeValue
+ _objc_msgSend$uiConfigurationOptions
+ _objc_msgSend$uiConfigurationOptionsCharacteristic
+ _objc_msgSend$uiConfigurationService:didUpdateUiConfigurationOptions:
+ _objc_msgSend$uiEmphasizedConsumptionGauge
+ _objc_msgSend$uiEmphasizedConsumptionGaugeCharacteristic
+ _objc_msgSend$uiEmphasizedEnergyLevelGauge
+ _objc_msgSend$uiEmphasizedEnergyLevelGaugeCharacteristic
+ _objc_msgSend$userVisibleApplicationNameInvalid
+ _objc_msgSend$userVisibleNavigationAidedDrivingFeatureName
+ _objc_msgSend$userVisibleNavigationAidedDrivingFeatureNameCharacteristic
+ _objc_msgSend$userVisibleNavigationAidedDrivingFeatureShortName
+ _objc_msgSend$userVisibleNavigationAidedDrivingFeatureShortNameCharacteristic
+ _objc_msgSend$userVisibleNavigationSystemName
+ _objc_msgSend$userVisibleNavigationSystemNameCharacteristic
+ _objc_msgSend$userVisibleReason
+ _objc_msgSend$userVisibleReasonCharacteristic
+ _objc_msgSend$userVisibleVehicleBrand
+ _objc_msgSend$userVisibleVehicleBrandCharacteristic
+ _objc_msgSend$userVisibleVehicleManufacturer
+ _objc_msgSend$userVisibleVehicleManufacturerCharacteristic
+ _objc_msgSend$userVisibleVehicleModel
+ _objc_msgSend$userVisibleVehicleModelCharacteristic
+ _objc_msgSend$vehicleDataPluginConfigs
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x9
- +[CAFAccessory accessoryWithCar:pluginID:config:]
- +[CAFAutoModeIntensityCharacteristic load]
- +[CAFAutoModeIntensityCharacteristic primaryCharacteristicFormat]
- +[CAFAutoModeIntensityCharacteristic secondaryCharacteristicFormats]
- +[CAFRoute load]
- +[CAFRoute observerProtocol]
- +[CAFRoute serviceIdentifier]
- -[CAFAccessory initWithCar:pluginID:config:]
- -[CAFAccessory initWithCar:pluginID:config:].cold.1
- -[CAFAccessory initWithCar:pluginID:config:].cold.2
- -[CAFAccessory initWithCar:pluginID:config:].cold.3
- -[CAFAutoClimateControl hasIntensity]
- -[CAFAutoClimateControl intensityCharacteristic]
- -[CAFAutoClimateControl intensityDisabled]
- -[CAFAutoClimateControl intensityRestricted]
- -[CAFAutoClimateControl intensity]
- -[CAFAutoClimateControl registeredForAutoModeIntensity]
- -[CAFAutoClimateControl setIntensity:]
- -[CAFAutoModeIntensityCharacteristic autoModeIntensityValue]
- -[CAFAutoModeIntensityCharacteristic formattedValue]
- -[CAFAutoModeIntensityCharacteristic setAutoModeIntensityValue:]
- -[CAFCar accessoriesForCategory:]
- -[CAFCarConfiguration initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:]
- -[CAFCarManager shouldAllocAccessoryType:].cold.1
- -[CAFCarManager shouldAllocAccessoryType:serviceConfig:].cold.1
- -[CAFNavigation routeService]
- -[CAFNavigation route]
- -[CAFNowPlayingSnapshot initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:]
- -[CAFRoute _characteristicDidUpdate:fromGroupUpdate:]
- -[CAFRoute addObserver:]
- -[CAFRoute applicationEnabledCharacteristic]
- -[CAFRoute applicationEnabledInvalid]
- -[CAFRoute applicationEnabled]
- -[CAFRoute destinationCharacteristic]
- -[CAFRoute destinationInvalid]
- -[CAFRoute destination]
- -[CAFRoute geodeticSystemCharacteristic]
- -[CAFRoute geodeticSystem]
- -[CAFRoute hasLegs]
- -[CAFRoute legsCharacteristic]
- -[CAFRoute legsInvalid]
- -[CAFRoute legs]
- -[CAFRoute name]
- -[CAFRoute originCharacteristic]
- -[CAFRoute originInvalid]
- -[CAFRoute origin]
- -[CAFRoute registerObserver:]
- -[CAFRoute registeredForApplicationEnabled]
- -[CAFRoute registeredForDestination]
- -[CAFRoute registeredForGeodeticSystem]
- -[CAFRoute registeredForLegs]
- -[CAFRoute registeredForOrigin]
- -[CAFRoute registeredForRouteState]
- -[CAFRoute registeredForUserEnabled]
- -[CAFRoute registeredForUserVisibleApplicationName]
- -[CAFRoute registeredForVehicleEnabled]
- -[CAFRoute removeObserver:]
- -[CAFRoute routeStateCharacteristic]
- -[CAFRoute routeState]
- -[CAFRoute setApplicationEnabled:]
- -[CAFRoute setDestination:]
- -[CAFRoute setGeodeticSystem:]
- -[CAFRoute setLegs:]
- -[CAFRoute setOrigin:]
- -[CAFRoute setRouteState:]
- -[CAFRoute setUserEnabled:]
- -[CAFRoute setUserVisibleApplicationName:]
- -[CAFRoute unregisterObserver:]
- -[CAFRoute userEnabledCharacteristic]
- -[CAFRoute userEnabledInvalid]
- -[CAFRoute userEnabled]
- -[CAFRoute userVisibleApplicationNameCharacteristic]
- -[CAFRoute userVisibleApplicationNameInvalid]
- -[CAFRoute userVisibleApplicationName]
- -[CAFRoute vehicleEnabledCharacteristic]
- -[CAFRoute vehicleEnabled]
- -[CAFUIConfiguration configurationIdentifierCharacteristic]
- -[CAFUIConfiguration configurationIdentifier]
- -[CAFUIConfiguration configurationOptionsCharacteristic]
- -[CAFUIConfiguration configurationOptions]
- -[CAFUIConfiguration hasConfigurationOptions]
- -[CAFUIConfiguration registeredForConfigurationIdentifier]
- -[CAFUIConfiguration registeredForConfigurationOptions]
- GCC_except_table33
- _CAFCharacteristicTypeAutoModeIntensity
- _CAFCharacteristicTypeConfigurationIdentifier
- _CAFCharacteristicTypeConfigurationOptions
- _CAFServiceTypeRoute
- _NSStringFromAutoModeIntensity
- _OBJC_CLASS_$_CAFAutoModeIntensityCharacteristic
- _OBJC_CLASS_$_CAFRoute
- _OBJC_METACLASS_$_CAFAutoModeIntensityCharacteristic
- _OBJC_METACLASS_$_CAFRoute
- _OUTLINED_FUNCTION_15
- __OBJC_$_CLASS_METHODS_CAFAutoModeIntensityCharacteristic
- __OBJC_$_CLASS_METHODS_CAFRoute
- __OBJC_$_INSTANCE_METHODS_CAFAutoModeIntensityCharacteristic
- __OBJC_$_INSTANCE_METHODS_CAFCar(Accessories|CAFNowPlaying)
- __OBJC_$_INSTANCE_METHODS_CAFRoute
- __OBJC_$_PROP_LIST_CAFAutoModeIntensityCharacteristic
- __OBJC_$_PROP_LIST_CAFRoute
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteObserver
- __OBJC_$_PROTOCOL_REFS_CAFRouteObserver
- __OBJC_CLASS_RO_$_CAFAutoModeIntensityCharacteristic
- __OBJC_CLASS_RO_$_CAFRoute
- __OBJC_LABEL_PROTOCOL_$_CAFRouteObserver
- __OBJC_METACLASS_RO_$_CAFAutoModeIntensityCharacteristic
- __OBJC_METACLASS_RO_$_CAFRoute
- __OBJC_PROTOCOL_$_CAFRouteObserver
- __OBJC_PROTOCOL_REFERENCE_$_CAFRouteObserver
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.246
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.246.cold.1
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.247
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.247.cold.1
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.247.cold.2
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.248
- ___44-[CAFAccessory initWithCar:pluginID:config:]_block_invoke
- ___44-[CAFAccessory initWithCar:pluginID:config:]_block_invoke.cold.1
- ___44-[CAFAccessory initWithCar:pluginID:config:]_block_invoke.cold.2
- ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.120
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e15_v32?08Q16^B24ls32l8s40l8s48l8r88l8s56l8s64l8s72l8s80l8
- ___block_literal_global.1587
- ___block_literal_global.1589
- ___block_literal_global.207
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.693
- ___block_literal_global.695
- _objc_msgSend$accessoriesForCategory:
- _objc_msgSend$accessoryWithCar:pluginID:config:
- _objc_msgSend$autoClimateControlService:didUpdateIntensity:
- _objc_msgSend$autoModeIntensityValue
- _objc_msgSend$configurationIdentifier
- _objc_msgSend$configurationIdentifierCharacteristic
- _objc_msgSend$configurationOptions
- _objc_msgSend$configurationOptionsCharacteristic
- _objc_msgSend$initWithCar:pluginID:config:
- _objc_msgSend$initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:
- _objc_msgSend$initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:
- _objc_msgSend$intensity
- _objc_msgSend$intensityCharacteristic
- _objc_msgSend$routeService
- _objc_msgSend$routeService:didUpdateApplicationEnabled:
- _objc_msgSend$routeService:didUpdateDestination:
- _objc_msgSend$routeService:didUpdateGeodeticSystem:
- _objc_msgSend$routeService:didUpdateLegs:
- _objc_msgSend$routeService:didUpdateOrigin:
- _objc_msgSend$routeService:didUpdateRouteState:
- _objc_msgSend$routeService:didUpdateUserEnabled:
- _objc_msgSend$routeService:didUpdateUserVisibleApplicationName:
- _objc_msgSend$routeService:didUpdateVehicleEnabled:
- _objc_msgSend$setAutoModeIntensityValue:
- _objc_msgSend$uiConfigurationService:didUpdateConfigurationIdentifier:
- _objc_msgSend$uiConfigurationService:didUpdateConfigurationOptions:
CStrings:
+ "%@: source %@ (%@) identifier %@, titles %@, artwork tokens (%lu,%lu), artwork %@, artworkType %@ multicast %@ playbackState %@"
+ "%s %@ disabledASCDict=%@"
+ "%s %@ routeSharing mode=%ld disabled=%@"
+ "%{public}@: Error parsing dictionary from UIConfigurationOptions array - %{public}@"
+ "-[CAFCarConfiguration configureDisabledASCFromSessionConfig:featureDenyList:]"
+ "-[CAFCarConfiguration updatePluginConfigs:]"
+ "0x0000000000000000"
+ "0x0000000011100006"
+ "0x000000001E000102"
+ "0x000000001E000103"
+ "0x000000001E000104"
+ "0x0000000031000030"
+ "0x0000000031000031"
+ "0x000000004500010A"
+ "0x000000004500010B"
+ "0x000000004500010C"
+ "0x000000004500010D"
+ "0x000000004500010E"
+ "0x000000004500010F"
+ "0x0000000045000110"
+ "0x0000000045000111"
+ "0x0000000045000112"
+ "0x0000000045000114"
+ "0x0000000045000115"
+ "0x0000000047000012"
+ "0x0000000047000013"
+ "@60@0:8@16@24B32Q36@44@52"
+ "@88@0:8@16@24C32@36q44q52q60Q68C76@80"
+ "AlternateRoute"
+ "AutoModeIntensities"
+ "AutoModeIntensityIndex"
+ "CAFASCTreeAccessoriesKey"
+ "CAFASCTreeNodeChildrenKey"
+ "CAFASCTreeNodeNameKey"
+ "CAFASCTreeNodeRegisteredValuesKey"
+ "CAFASCTreeNodeTypeKey"
+ "CAFCarConfigurationDisabledASC"
+ "CAFCarConfigurationPluginNameDictionary"
+ "CAFEnergyGaugeUI"
+ "CAFEnergyGaugeUIObserver"
+ "CAFRerouteReasonCharacteristic"
+ "CAFRouteSharing"
+ "CAFRouteSharingObserver"
+ "CAFRouteSourceCharacteristic"
+ "CAFRouteStatus"
+ "CAFRouteStatusObserver"
+ "CAFSharingStateCharacteristic"
+ "CAFSystemInformation"
+ "CAFSystemInformationObserver"
+ "CAFUIConfigurationOption"
+ "CAFUIConfigurationOptionCharacteristic"
+ "CAFUIConfigurationOptions"
+ "CAFUIConfigurationOptionsCharacteristic"
+ "CAFUIEmphasizedConsumptionGaugeCharacteristic"
+ "CAFUIEmphasizedEnergyLevelGaugeCharacteristic"
+ "Cluster_Display"
+ "Communication Plug-in"
+ "DeviceDestinationsOnly"
+ "DeviceRouteDestinationsModified"
+ "DeviceRouteModified"
+ "DeviceUnchanged"
+ "ElectricEngineEcoPower"
+ "EnergyGaugeUI"
+ "Forced"
+ "HighVoltageBatteryConsumption"
+ "HighVoltageBatteryLevel"
+ "MissedTurn"
+ "NULL"
+ "NavigationAidedDrivingActive"
+ "NoReroute"
+ "OfflineOnlineTransition"
+ "Parsing plugin configuraion with index: %lu failed for pluginConfig"
+ "Parsing pluginID %@ named %@ start"
+ "RegionUnavailable"
+ "RerouteReason"
+ "RouteSharing"
+ "RouteSource"
+ "RouteStatus"
+ "Secondary_Cluster_Display"
+ "SharingState"
+ "SystemInformation"
+ "T@\"CAFASCTree\",&,N,V_disabledASC"
+ "T@\"CAFEnergyGaugeUI\",R,N"
+ "T@\"CAFRerouteReasonCharacteristic\",R,N"
+ "T@\"CAFRouteSharing\",R,N"
+ "T@\"CAFRouteSourceCharacteristic\",R,N"
+ "T@\"CAFRouteStatus\",R,N"
+ "T@\"CAFSharingStateCharacteristic\",R,N"
+ "T@\"CAFSystemInformation\",R,N"
+ "T@\"CAFUIConfigurationOption\",C,N"
+ "T@\"CAFUIConfigurationOptions\",C,N"
+ "T@\"CAFUIConfigurationOptions\",R,N"
+ "T@\"CAFUIConfigurationOptionsCharacteristic\",R,N"
+ "T@\"CAFUIEmphasizedConsumptionGaugeCharacteristic\",R,N"
+ "T@\"CAFUIEmphasizedEnergyLevelGaugeCharacteristic\",R,N"
+ "T@\"NSArray\",R,N,V_uIConfigurationOptions"
+ "T@\"NSDictionary\",R,N,V_pluginNameDictionary"
+ "T@\"NSString\",R,C,N,V_value"
+ "T@\"NSString\",R,N,V_handlerName"
+ "T@\"NSString\",R,N,V_mediaItemIdentifier"
+ "T@\"NSString\",R,N,V_routeSharingOEMName"
+ "T@\"NSString\",R,N,V_routeSharingUserVisibleReason"
+ "UIConfigurationOption"
+ "UIConfigurationOptions"
+ "UIEmphasizedConsumptionGauge"
+ "UIEmphasizedEnergyLevelGauge"
+ "UserVisibleNavigationAidedDrivingFeatureName"
+ "UserVisibleNavigationAidedDrivingFeatureShortName"
+ "UserVisibleNavigationSystemName"
+ "UserVisibleReason"
+ "UserVisibleVehicleBrand"
+ "UserVisibleVehicleManufacturer"
+ "UserVisibleVehicleModel"
+ "Vehicle"
+ "WaypointAdded"
+ "WaypointRemoved"
+ "WaypointsModified"
+ "_disabledASC"
+ "_handlerName"
+ "_mediaItemIdentifier"
+ "_pluginNameDictionary"
+ "_routeSharingOEMName"
+ "_routeSharingUserVisibleReason"
+ "_uIConfigurationOptions"
+ "accessoriesForCategory:withHandler:"
+ "accessoryWithCar:pluginID:handlerName:config:"
+ "addEntriesFromDictionary:"
+ "autoClimateControlService:didUpdateAutoModeIntensityIndex:"
+ "autoClimateControlService:didUpdateIntensities:"
+ "autoModeIntensityIndex"
+ "autoModeIntensityIndexCharacteristic"
+ "autoModeIntensityIndexDisabled"
+ "autoModeIntensityIndexInvalid"
+ "autoModeIntensityIndexRange"
+ "autoModeIntensityIndexRestricted"
+ "configureDisabledASCFromSessionConfig:featureDenyList:"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "disabledASC"
+ "energyGaugeUI"
+ "energyGaugeUIService"
+ "energyGaugeUIService:didUpdateUiEmphasizedConsumptionGauge:"
+ "energyGaugeUIService:didUpdateUiEmphasizedEnergyLevelGauge:"
+ "featureDisabled"
+ "handlerName"
+ "hasAutoModeIntensityIndex"
+ "hasIntensities"
+ "hasRerouteReason"
+ "hasUiEmphasizedConsumptionGauge"
+ "hasUiEmphasizedEnergyLevelGauge"
+ "hasUserVisibleNavigationAidedDrivingFeatureName"
+ "hasUserVisibleNavigationAidedDrivingFeatureShortName"
+ "hvacOnDisabled"
+ "infoResponse"
+ "initEmpty"
+ "initWithCar:pluginID:handlerName:config:"
+ "initWithCarSessionConfiguration:"
+ "initWithIdentifier:value:"
+ "initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:pluginNameDictionary:"
+ "initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:mediaItemIdentifier:"
+ "initWithUIConfigurationOptions:"
+ "intensities"
+ "intensitiesCharacteristic"
+ "isEqualToNumber:"
+ "kCAFCarNowPlayingMediaItemIdentifierKey"
+ "mediaItemIdentifier"
+ "navigationAidedDrivingActive"
+ "navigationAidedDrivingActiveCharacteristic"
+ "oemWritable"
+ "pluginMapping"
+ "pluginNameDictionary"
+ "pluginNameForIdentifier:"
+ "registeredForAutoModeIntensities"
+ "registeredForAutoModeIntensityIndex"
+ "registeredForNavigationAidedDrivingActive"
+ "registeredForRerouteReason"
+ "registeredForRouteSource"
+ "registeredForSharingState"
+ "registeredForUIConfigurationOptions"
+ "registeredForUIEmphasizedConsumptionGauge"
+ "registeredForUIEmphasizedEnergyLevelGauge"
+ "registeredForUserVisibleNavigationAidedDrivingFeatureName"
+ "registeredForUserVisibleNavigationAidedDrivingFeatureShortName"
+ "registeredForUserVisibleNavigationSystemName"
+ "registeredForUserVisibleReason"
+ "registeredForUserVisibleVehicleBrand"
+ "registeredForUserVisibleVehicleManufacturer"
+ "registeredForUserVisibleVehicleModel"
+ "rerouteReason"
+ "rerouteReasonCharacteristic"
+ "rerouteReasonValue"
+ "routeSharing"
+ "routeSharingMode"
+ "routeSharingOEMName"
+ "routeSharingService"
+ "routeSharingService:didUpdateApplicationEnabled:"
+ "routeSharingService:didUpdateLegs:"
+ "routeSharingService:didUpdateSharingState:"
+ "routeSharingService:didUpdateUserEnabled:"
+ "routeSharingService:didUpdateUserVisibleReason:"
+ "routeSharingService:didUpdateVehicleEnabled:"
+ "routeSharingUserVisibleReason"
+ "routeSource"
+ "routeSourceCharacteristic"
+ "routeSourceValue"
+ "routeStatus"
+ "routeStatusService"
+ "routeStatusService:didUpdateDestination:"
+ "routeStatusService:didUpdateGeodeticSystem:"
+ "routeStatusService:didUpdateOrigin:"
+ "routeStatusService:didUpdateRerouteReason:"
+ "routeStatusService:didUpdateRouteState:"
+ "routeStatusService:didUpdateUserVisibleApplicationName:"
+ "setAutoModeIntensityIndex:"
+ "setDisabledASC:"
+ "setIntensities:"
+ "setRerouteReason:"
+ "setRerouteReasonValue:"
+ "setRouteSourceValue:"
+ "setSharingState:"
+ "setSharingStateValue:"
+ "setUIConfigurationOptionValue:"
+ "setUIConfigurationOptionsValue:"
+ "setUIEmphasizedConsumptionGaugeValue:"
+ "setUIEmphasizedEnergyLevelGaugeValue:"
+ "sharingState"
+ "sharingStateCharacteristic"
+ "sharingStateValue"
+ "should not allocate accessory %{public}@ (shouldAlloc=%{public}@ disabled=%{public}@)"
+ "should not allocate control %{public}@.%{public}@.%{public}@ (shouldAlloc=%{public}@ disabled=%{public}@)"
+ "should not allocate service %{public}@.%{public}@ (shouldAlloc=%{public}@ disabled=%{public}@)"
+ "systemInformation"
+ "systemInformationService"
+ "systemInformationService:didUpdateNavigationAidedDrivingActive:"
+ "systemInformationService:didUpdateRouteSource:"
+ "systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureName:"
+ "systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureShortName:"
+ "systemInformationService:didUpdateUserVisibleNavigationSystemName:"
+ "systemInformationService:didUpdateUserVisibleVehicleBrand:"
+ "systemInformationService:didUpdateUserVisibleVehicleManufacturer:"
+ "systemInformationService:didUpdateUserVisibleVehicleModel:"
+ "uIConfigurationOptionValue"
+ "uIConfigurationOptions"
+ "uIConfigurationOptionsValue"
+ "uIConfigurationOptionsWithArray:"
+ "uIConfigurationOptionsWithUIConfigurationOptions:"
+ "uIEmphasizedConsumptionGaugeValue"
+ "uIEmphasizedEnergyLevelGaugeValue"
+ "uiConfigurationOptions"
+ "uiConfigurationOptionsCharacteristic"
+ "uiConfigurationService:didUpdateUiConfigurationOptions:"
+ "uiEmphasizedConsumptionGauge"
+ "uiEmphasizedConsumptionGaugeCharacteristic"
+ "uiEmphasizedEnergyLevelGauge"
+ "uiEmphasizedEnergyLevelGaugeCharacteristic"
+ "updatePluginConfigs:"
+ "userVisibleNavigationAidedDrivingFeatureName"
+ "userVisibleNavigationAidedDrivingFeatureNameCharacteristic"
+ "userVisibleNavigationAidedDrivingFeatureShortName"
+ "userVisibleNavigationAidedDrivingFeatureShortNameCharacteristic"
+ "userVisibleNavigationSystemName"
+ "userVisibleNavigationSystemNameCharacteristic"
+ "userVisibleReason"
+ "userVisibleReasonCharacteristic"
+ "userVisibleVehicleBrand"
+ "userVisibleVehicleBrandCharacteristic"
+ "userVisibleVehicleManufacturer"
+ "userVisibleVehicleManufacturerCharacteristic"
+ "userVisibleVehicleModel"
+ "userVisibleVehicleModelCharacteristic"
+ "v28@0:8@\"CAFAutoClimateControl\"16I24"
+ "v28@0:8@\"CAFEnergyGaugeUI\"16C24"
+ "v28@0:8@\"CAFRouteSharing\"16B24"
+ "v28@0:8@\"CAFRouteSharing\"16C24"
+ "v28@0:8@\"CAFRouteStatus\"16C24"
+ "v28@0:8@\"CAFSystemInformation\"16B24"
+ "v28@0:8@\"CAFSystemInformation\"16C24"
+ "v32@0:8@\"CAFAutoClimateControl\"16@\"NSArray\"24"
+ "v32@0:8@\"CAFRouteSharing\"16@\"CAFRouteLegs\"24"
+ "v32@0:8@\"CAFRouteSharing\"16@\"NSString\"24"
+ "v32@0:8@\"CAFRouteStatus\"16@\"CAFPointOfInterest\"24"
+ "v32@0:8@\"CAFRouteStatus\"16@\"NSString\"24"
+ "v32@0:8@\"CAFSystemInformation\"16@\"NSString\"24"
+ "v32@0:8@\"CAFUIConfiguration\"16@\"CAFUIConfigurationOptions\"24"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "vehicleDataPluginConfigs"
+ "vehicleStateProtocolInfo"
+ "\x91"
- "%@: source %@ (%@) titles %@, artwork tokens (%lu,%lu), artwork %@, artworkType %@ multicast %@ playbackState %@"
- "/"
- "0x000000001E000101"
- "0x0000000031000028"
- "0x0000000048000010"
- "@52@0:8@16@24B32Q36@44"
- "@80@0:8@16@24C32@36q44q52q60Q68C76"
- "AutoModeIntensity"
- "CAFAutoModeIntensityCharacteristic"
- "CAFRoute"
- "CAFRouteObserver"
- "ConfigurationIdentifier"
- "ConfigurationOptions"
- "Custom"
- "Parsing pluginID %@ start"
- "Route"
- "Soft"
- "Strong"
- "T@\"CAFAutoModeIntensityCharacteristic\",R,N"
- "T@\"CAFRoute\",R,N"
- "__NO_ACCESS__"
- "accessoriesForCategory:"
- "accessoryWithCar:pluginID:config:"
- "autoClimateControlService:didUpdateIntensity:"
- "autoModeIntensityValue"
- "configurationIdentifier"
- "configurationIdentifierCharacteristic"
- "configurationOptions"
- "configurationOptionsCharacteristic"
- "hasConfigurationOptions"
- "hasIntensity"
- "initWithCar:pluginID:config:"
- "initWithName:identifier:rightHandDrive:pluginCount:sessionAnalytics:"
- "initWithTitles:artworkData:mediaSourceType:mediaSourceIdentifier:artworkToken:mediaItemImageToken:artworkType:multicast:playbackState:"
- "intensity"
- "intensityCharacteristic"
- "intensityDisabled"
- "intensityRestricted"
- "registeredForAutoModeIntensity"
- "registeredForConfigurationIdentifier"
- "registeredForConfigurationOptions"
- "route"
- "routeService"
- "routeService:didUpdateApplicationEnabled:"
- "routeService:didUpdateDestination:"
- "routeService:didUpdateGeodeticSystem:"
- "routeService:didUpdateLegs:"
- "routeService:didUpdateOrigin:"
- "routeService:didUpdateRouteState:"
- "routeService:didUpdateUserEnabled:"
- "routeService:didUpdateUserVisibleApplicationName:"
- "routeService:didUpdateVehicleEnabled:"
- "setAutoModeIntensityValue:"
- "setIntensity:"
- "should not allocate accessory %{public}@"
- "should not allocate control %{public}@.%{public}@.%{public}@"
- "should not allocate service %{public}@.%{public}@"
- "uiConfigurationService:didUpdateConfigurationIdentifier:"
- "uiConfigurationService:didUpdateConfigurationOptions:"
- "v28@0:8@\"CAFRoute\"16B24"
- "v28@0:8@\"CAFRoute\"16C24"
- "v32@0:8@\"CAFRoute\"16@\"CAFPointOfInterest\"24"
- "v32@0:8@\"CAFRoute\"16@\"CAFRouteLegs\"24"
- "v32@0:8@\"CAFRoute\"16@\"NSString\"24"
- "v32@0:8@\"CAFUIConfiguration\"16@\"NSArray\"24"
- "v32@0:8@\"CAFUIConfiguration\"16@\"NSString\"24"

```
