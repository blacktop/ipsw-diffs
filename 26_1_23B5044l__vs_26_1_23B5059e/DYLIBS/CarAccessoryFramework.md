## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-488.11.0.0.0
-  __TEXT.__text: 0xec528
+488.17.3.0.0
+  __TEXT.__text: 0xf8ef8
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__objc_methlist: 0x170d4
+  __TEXT.__objc_methlist: 0x1856c
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x670
-  __TEXT.__cstring: 0x6c95
-  __TEXT.__oslogstring: 0x33ff
+  __TEXT.__cstring: 0x7211
+  __TEXT.__oslogstring: 0x352a
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x39e8
-  __TEXT.__objc_classname: 0x3a68
-  __TEXT.__objc_methname: 0x1b888
-  __TEXT.__objc_methtype: 0x42db
-  __TEXT.__objc_stubs: 0x11bc0
-  __DATA_CONST.__got: 0xb58
-  __DATA_CONST.__const: 0x2200
-  __DATA_CONST.__objc_classlist: 0xbe0
-  __DATA_CONST.__objc_nlclslist: 0x8b8
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x670
+  __TEXT.__unwind_info: 0x3cf8
+  __TEXT.__objc_classname: 0x3dd6
+  __TEXT.__objc_methname: 0x1d187
+  __TEXT.__objc_methtype: 0x4645
+  __TEXT.__objc_stubs: 0x12860
+  __DATA_CONST.__got: 0xc10
+  __DATA_CONST.__const: 0x23c8
+  __DATA_CONST.__objc_classlist: 0xcc0
+  __DATA_CONST.__objc_nlclslist: 0x958
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x6b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6bd0
-  __DATA_CONST.__objc_protorefs: 0x610
-  __DATA_CONST.__objc_superrefs: 0x1050
-  __DATA_CONST.__objc_arraydata: 0xa838
+  __DATA_CONST.__objc_selrefs: 0x7198
+  __DATA_CONST.__objc_protorefs: 0x658
+  __DATA_CONST.__objc_superrefs: 0x1178
+  __DATA_CONST.__objc_arraydata: 0xaea8
   __AUTH_CONST.__auth_got: 0x348
   __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0xc300
-  __AUTH_CONST.__objc_const: 0x4b648
+  __AUTH_CONST.__cfstring: 0xce40
+  __AUTH_CONST.__objc_const: 0x4f4b8
   __AUTH_CONST.__objc_arrayobj: 0x120
-  __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x510
+  __AUTH_CONST.__objc_dictobj: 0x5e38
+  __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_dictobj: 0x5a28
-  __AUTH.__objc_data: 0x1b30
-  __DATA.__objc_ivar: 0x5a0
-  __DATA.__data: 0x4d60
+  __AUTH.__objc_data: 0x23a0
+  __DATA.__objc_ivar: 0x5f0
+  __DATA.__data: 0x50c0
   __DATA.__bss: 0x300
-  __DATA_DIRTY.__objc_data: 0x5b90
+  __DATA_DIRTY.__objc_data: 0x5be0
   __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE1F1C0B-481F-3FD3-A0D1-BBE3147A5062
-  Functions: 7125
-  Symbols:   23401
-  CStrings:  8826
+  UUID: E832808D-89D6-387D-B345-02B9F54B18CE
+  Functions: 7506
+  Symbols:   24643
+  CStrings:  9315
 
Symbols:
+ +[CAFBatteryConditioning load]
+ +[CAFBatteryConditioning observerProtocol]
+ +[CAFBatteryConditioning serviceIdentifier]
+ +[CAFBatteryConditioningStateCharacteristic load]
+ +[CAFBatteryConditioningStateCharacteristic primaryCharacteristicFormat]
+ +[CAFBatteryConditioningStateCharacteristic secondaryCharacteristicFormats]
+ +[CAFChargingLevel load]
+ +[CAFCoordinateCharacteristic load]
+ +[CAFCoordinateCharacteristic primaryCharacteristicFormat]
+ +[CAFCoordinateCharacteristic secondaryCharacteristicFormats]
+ +[CAFCoordinates coordinatesWithArray:]
+ +[CAFCoordinates coordinatesWithCoordinates:]
+ +[CAFCoordinatesCharacteristic load]
+ +[CAFCoordinatesCharacteristic primaryCharacteristicFormat]
+ +[CAFCoordinatesCharacteristic secondaryCharacteristicFormats]
+ +[CAFGeodeticSystemCharacteristic load]
+ +[CAFGeodeticSystemCharacteristic primaryCharacteristicFormat]
+ +[CAFGeodeticSystemCharacteristic secondaryCharacteristicFormats]
+ +[CAFInteriorAmbientLights load]
+ +[CAFInteriorAmbientLights observerProtocol]
+ +[CAFInteriorAmbientLights serviceIdentifier]
+ +[CAFLighting accessoryIdentifier]
+ +[CAFLighting load]
+ +[CAFLighting observerProtocol]
+ +[CAFMinimumChargingLevel load]
+ +[CAFMinimumChargingLevel observerProtocol]
+ +[CAFMinimumChargingLevel serviceIdentifier]
+ +[CAFNavigation accessoryIdentifier]
+ +[CAFNavigation load]
+ +[CAFNavigation observerProtocol]
+ +[CAFPointOfInterestCharacteristic load]
+ +[CAFPointOfInterestCharacteristic primaryCharacteristicFormat]
+ +[CAFPointOfInterestCharacteristic secondaryCharacteristicFormats]
+ +[CAFPointsOfInterest pointsOfInterestWithArray:]
+ +[CAFPointsOfInterest pointsOfInterestWithPointOfInterests:]
+ +[CAFPointsOfInterestCharacteristic load]
+ +[CAFPointsOfInterestCharacteristic primaryCharacteristicFormat]
+ +[CAFPointsOfInterestCharacteristic secondaryCharacteristicFormats]
+ +[CAFRegistrations carPlayTemplateUIHost]
+ +[CAFRegistrations cpNavTool]
+ +[CAFRegistrations maps]
+ +[CAFRoute load]
+ +[CAFRoute observerProtocol]
+ +[CAFRoute serviceIdentifier]
+ +[CAFRouteLegCharacteristic load]
+ +[CAFRouteLegCharacteristic primaryCharacteristicFormat]
+ +[CAFRouteLegCharacteristic secondaryCharacteristicFormats]
+ +[CAFRouteLegs routeLegsWithArray:]
+ +[CAFRouteLegs routeLegsWithRouteLegs:]
+ +[CAFRouteLegsCharacteristic load]
+ +[CAFRouteLegsCharacteristic primaryCharacteristicFormat]
+ +[CAFRouteLegsCharacteristic secondaryCharacteristicFormats]
+ +[CAFRouteStateCharacteristic load]
+ +[CAFRouteStateCharacteristic primaryCharacteristicFormat]
+ +[CAFRouteStateCharacteristic secondaryCharacteristicFormats]
+ +[CAFSupportedColorCharacteristic load]
+ +[CAFSupportedColorCharacteristic primaryCharacteristicFormat]
+ +[CAFSupportedColorCharacteristic secondaryCharacteristicFormats]
+ +[CAFSupportedColors supportedColorsWithArray:]
+ +[CAFSupportedColors supportedColorsWithSupportedColors:]
+ +[CAFSupportedColorsCharacteristic load]
+ +[CAFSupportedColorsCharacteristic primaryCharacteristicFormat]
+ +[CAFSupportedColorsCharacteristic secondaryCharacteristicFormats]
+ +[CAFTargetChargingLevel load]
+ +[CAFTargetChargingLevel observerProtocol]
+ +[CAFTargetChargingLevel serviceIdentifier]
+ +[CAFUIConfiguration load]
+ +[CAFUIConfiguration observerProtocol]
+ +[CAFUIConfiguration serviceIdentifier]
+ -[CAFBatteryConditioning _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFBatteryConditioning addObserver:]
+ -[CAFBatteryConditioning batteryConditioningStateCharacteristic]
+ -[CAFBatteryConditioning batteryConditioningState]
+ -[CAFBatteryConditioning name]
+ -[CAFBatteryConditioning registerObserver:]
+ -[CAFBatteryConditioning registeredForBatteryConditioningState]
+ -[CAFBatteryConditioning removeObserver:]
+ -[CAFBatteryConditioning unregisterObserver:]
+ -[CAFBatteryConditioningStateCharacteristic batteryConditioningStateValue]
+ -[CAFBatteryConditioningStateCharacteristic formattedValue]
+ -[CAFBatteryConditioningStateCharacteristic setBatteryConditioningStateValue:]
+ -[CAFBooleanSettingNotificationEntry initWithOffSymbolColor:offSymbolName:offUserVisibleLabel:onSymbolColor:onSymbolName:onUserVisibleLabel:]
+ -[CAFBooleanSettingNotificationEntryList arrayRepresentation]
+ -[CAFCar(Accessories) lighting]
+ -[CAFCar(Accessories) navigation]
+ -[CAFCarManager _isEntitled]
+ -[CAFCarManager _isEntitled].cold.1
+ -[CAFCarManager _isEntitled].cold.2
+ -[CAFCharacteristicValue description]
+ -[CAFCharging minimumChargingLevelService]
+ -[CAFCharging minimumChargingLevel]
+ -[CAFCharging targetChargingLevelService]
+ -[CAFCharging targetChargingLevel]
+ -[CAFChargingLevel _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFChargingLevel addObserver:]
+ -[CAFChargingLevel chargingLevelCharacteristic]
+ -[CAFChargingLevel chargingLevelMeasurementRange]
+ -[CAFChargingLevel chargingLevelRange]
+ -[CAFChargingLevel chargingLevel]
+ -[CAFChargingLevel distanceKMCharacteristic]
+ -[CAFChargingLevel distanceKMInvalid]
+ -[CAFChargingLevel distanceKMMeasurementRange]
+ -[CAFChargingLevel distanceKMRange]
+ -[CAFChargingLevel distanceKM]
+ -[CAFChargingLevel distanceMilesCharacteristic]
+ -[CAFChargingLevel distanceMilesInvalid]
+ -[CAFChargingLevel distanceMilesMeasurementRange]
+ -[CAFChargingLevel distanceMilesRange]
+ -[CAFChargingLevel distanceMiles]
+ -[CAFChargingLevel hasDistanceKM]
+ -[CAFChargingLevel hasDistanceMiles]
+ -[CAFChargingLevel name]
+ -[CAFChargingLevel registerObserver:]
+ -[CAFChargingLevel registeredForChargingLevel]
+ -[CAFChargingLevel registeredForDistanceKM]
+ -[CAFChargingLevel registeredForDistanceMiles]
+ -[CAFChargingLevel removeObserver:]
+ -[CAFChargingLevel setChargingLevel:]
+ -[CAFChargingLevel unregisterObserver:]
+ -[CAFChargingStatus chargingModeIdentifierCharacteristic]
+ -[CAFChargingStatus chargingModeIdentifier]
+ -[CAFChargingStatus hasChargingModeIdentifier]
+ -[CAFChargingStatus registeredForChargingModeIdentifier]
+ -[CAFCoordinate altitude]
+ -[CAFCoordinate description]
+ -[CAFCoordinate dictionaryRepresentation]
+ -[CAFCoordinate initWithAltitude:latitude:longitude:]
+ -[CAFCoordinate initWithDictionary:]
+ -[CAFCoordinate latitude]
+ -[CAFCoordinate longitude]
+ -[CAFCoordinateCharacteristic coordinateValue]
+ -[CAFCoordinateCharacteristic formattedValue]
+ -[CAFCoordinateCharacteristic setCoordinateValue:]
+ -[CAFCoordinates .cxx_destruct]
+ -[CAFCoordinates arrayRepresentation]
+ -[CAFCoordinates coordinates]
+ -[CAFCoordinates countByEnumeratingWithState:objects:count:]
+ -[CAFCoordinates formattedValue]
+ -[CAFCoordinates initWithArray:]
+ -[CAFCoordinates initWithCoordinates:]
+ -[CAFCoordinates objectAtIndex:]
+ -[CAFCoordinates objectAtIndexedSubscript:]
+ -[CAFCoordinates parseError]
+ -[CAFCoordinatesCharacteristic coordinatesValue]
+ -[CAFCoordinatesCharacteristic formattedValue]
+ -[CAFCoordinatesCharacteristic setCoordinatesValue:]
+ -[CAFEntry initWithSymbolName:userVisibleLabel:]
+ -[CAFEntryList arrayRepresentation]
+ -[CAFGeodeticSystemCharacteristic formattedValue]
+ -[CAFGeodeticSystemCharacteristic geodeticSystemValue]
+ -[CAFGeodeticSystemCharacteristic setGeodeticSystemValue:]
+ -[CAFHighVoltageBattery batteryConditioningService]
+ -[CAFHighVoltageBattery batteryConditioning]
+ -[CAFHistoricalNotificationUserAction initWithContentURLAction:symbolName:userVisibleLabel:]
+ -[CAFHistoricalNotificationUserActions arrayRepresentation]
+ -[CAFInteriorAmbientLights _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFInteriorAmbientLights addObserver:]
+ -[CAFInteriorAmbientLights brightnessCharacteristic]
+ -[CAFInteriorAmbientLights brightnessRange]
+ -[CAFInteriorAmbientLights brightness]
+ -[CAFInteriorAmbientLights hasBrightness]
+ -[CAFInteriorAmbientLights hasSupportedColors]
+ -[CAFInteriorAmbientLights name]
+ -[CAFInteriorAmbientLights primaryColorCharacteristic]
+ -[CAFInteriorAmbientLights primaryColor]
+ -[CAFInteriorAmbientLights registerObserver:]
+ -[CAFInteriorAmbientLights registeredForBrightness]
+ -[CAFInteriorAmbientLights registeredForPrimaryColor]
+ -[CAFInteriorAmbientLights registeredForSupportedColors]
+ -[CAFInteriorAmbientLights removeObserver:]
+ -[CAFInteriorAmbientLights setBrightness:]
+ -[CAFInteriorAmbientLights setPrimaryColor:]
+ -[CAFInteriorAmbientLights supportedColorsCharacteristic]
+ -[CAFInteriorAmbientLights supportedColors]
+ -[CAFInteriorAmbientLights unregisterObserver:]
+ -[CAFLighting addObserver:]
+ -[CAFLighting interiorAmbientLightsService]
+ -[CAFLighting interiorAmbientLights]
+ -[CAFLighting registerObserver:]
+ -[CAFLighting removeObserver:]
+ -[CAFLighting unregisterObserver:]
+ -[CAFMediaItem initWithArtist:ensemble:frequency:identifier:mediaItemCategory:mediaItemCategoryUserVisibleLabel:mediaItemGroup:mediaItemImageIdentifier:mediaItemName:mediaItemShortName:mediaItemType:multicast:title:userVisibleDescription:]
+ -[CAFMediaItemImage initWithIdentifier:imageData:]
+ -[CAFMediaItemImages arrayRepresentation]
+ -[CAFMediaItems arrayRepresentation]
+ -[CAFMinimumChargingLevel addObserver:]
+ -[CAFMinimumChargingLevel name]
+ -[CAFMinimumChargingLevel registerObserver:]
+ -[CAFMinimumChargingLevel removeObserver:]
+ -[CAFMinimumChargingLevel unregisterObserver:]
+ -[CAFModeItems defaultIndexCharacteristic]
+ -[CAFModeItems defaultIndexRange]
+ -[CAFModeItems defaultIndex]
+ -[CAFModeItems hasDefaultIndex]
+ -[CAFModeItems registeredForDefaultIndex]
+ -[CAFNavigation addObserver:]
+ -[CAFNavigation registerObserver:]
+ -[CAFNavigation removeObserver:]
+ -[CAFNavigation routeService]
+ -[CAFNavigation route]
+ -[CAFNavigation unregisterObserver:]
+ -[CAFNotificationUserAction initWithContentURLAction:userVisibleLabel:]
+ -[CAFNotificationUserActions arrayRepresentation]
+ -[CAFPairedDevice initWithIdentifier:name:sortOrder:state:]
+ -[CAFPairedDeviceList arrayRepresentation]
+ -[CAFPointOfInterest .cxx_destruct]
+ -[CAFPointOfInterest description]
+ -[CAFPointOfInterest dictionaryRepresentation]
+ -[CAFPointOfInterest entryPoints]
+ -[CAFPointOfInterest initWithDictionary:]
+ -[CAFPointOfInterest initWithEntryPoints:location:locationThreshold:userVisibleAddress:userVisibleName:]
+ -[CAFPointOfInterest locationThreshold]
+ -[CAFPointOfInterest location]
+ -[CAFPointOfInterest userVisibleAddress]
+ -[CAFPointOfInterest userVisibleName]
+ -[CAFPointOfInterestCharacteristic formattedValue]
+ -[CAFPointOfInterestCharacteristic pointOfInterestValue]
+ -[CAFPointOfInterestCharacteristic setPointOfInterestValue:]
+ -[CAFPointsOfInterest .cxx_destruct]
+ -[CAFPointsOfInterest arrayRepresentation]
+ -[CAFPointsOfInterest countByEnumeratingWithState:objects:count:]
+ -[CAFPointsOfInterest formattedValue]
+ -[CAFPointsOfInterest initWithArray:]
+ -[CAFPointsOfInterest initWithPointOfInterests:]
+ -[CAFPointsOfInterest objectAtIndex:]
+ -[CAFPointsOfInterest objectAtIndexedSubscript:]
+ -[CAFPointsOfInterest parseError]
+ -[CAFPointsOfInterest pointOfInterests]
+ -[CAFPointsOfInterestCharacteristic formattedValue]
+ -[CAFPointsOfInterestCharacteristic pointsOfInterestValue]
+ -[CAFPointsOfInterestCharacteristic setPointsOfInterestValue:]
+ -[CAFProminenceInfo arrayRepresentation]
+ -[CAFProminenceInformation initWithColor:prominenceLevel:sortOrder:userVisibleLabel:userVisibleValue:]
+ -[CAFRoute _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFRoute addObserver:]
+ -[CAFRoute applicationEnabledCharacteristic]
+ -[CAFRoute applicationEnabledInvalid]
+ -[CAFRoute applicationEnabled]
+ -[CAFRoute destinationCharacteristic]
+ -[CAFRoute destinationInvalid]
+ -[CAFRoute destination]
+ -[CAFRoute geodeticSystemCharacteristic]
+ -[CAFRoute geodeticSystem]
+ -[CAFRoute hasLegs]
+ -[CAFRoute legsCharacteristic]
+ -[CAFRoute legsInvalid]
+ -[CAFRoute legs]
+ -[CAFRoute name]
+ -[CAFRoute originCharacteristic]
+ -[CAFRoute originInvalid]
+ -[CAFRoute origin]
+ -[CAFRoute registerObserver:]
+ -[CAFRoute registeredForApplicationEnabled]
+ -[CAFRoute registeredForDestination]
+ -[CAFRoute registeredForGeodeticSystem]
+ -[CAFRoute registeredForLegs]
+ -[CAFRoute registeredForOrigin]
+ -[CAFRoute registeredForRouteState]
+ -[CAFRoute registeredForUserEnabled]
+ -[CAFRoute registeredForUserVisibleApplicationName]
+ -[CAFRoute registeredForVehicleEnabled]
+ -[CAFRoute removeObserver:]
+ -[CAFRoute routeStateCharacteristic]
+ -[CAFRoute routeState]
+ -[CAFRoute setApplicationEnabled:]
+ -[CAFRoute setDestination:]
+ -[CAFRoute setGeodeticSystem:]
+ -[CAFRoute setLegs:]
+ -[CAFRoute setOrigin:]
+ -[CAFRoute setRouteState:]
+ -[CAFRoute setUserEnabled:]
+ -[CAFRoute setUserVisibleApplicationName:]
+ -[CAFRoute unregisterObserver:]
+ -[CAFRoute userEnabledCharacteristic]
+ -[CAFRoute userEnabledInvalid]
+ -[CAFRoute userEnabled]
+ -[CAFRoute userVisibleApplicationNameCharacteristic]
+ -[CAFRoute userVisibleApplicationNameInvalid]
+ -[CAFRoute userVisibleApplicationName]
+ -[CAFRoute vehicleEnabledCharacteristic]
+ -[CAFRoute vehicleEnabled]
+ -[CAFRouteLeg .cxx_destruct]
+ -[CAFRouteLeg coordinates]
+ -[CAFRouteLeg description]
+ -[CAFRouteLeg destination]
+ -[CAFRouteLeg dictionaryRepresentation]
+ -[CAFRouteLeg initWithCoordinates:destination:origin:]
+ -[CAFRouteLeg initWithDictionary:]
+ -[CAFRouteLeg origin]
+ -[CAFRouteLegCharacteristic formattedValue]
+ -[CAFRouteLegCharacteristic routeLegValue]
+ -[CAFRouteLegCharacteristic setRouteLegValue:]
+ -[CAFRouteLegs .cxx_destruct]
+ -[CAFRouteLegs arrayRepresentation]
+ -[CAFRouteLegs countByEnumeratingWithState:objects:count:]
+ -[CAFRouteLegs formattedValue]
+ -[CAFRouteLegs initWithArray:]
+ -[CAFRouteLegs initWithRouteLegs:]
+ -[CAFRouteLegs objectAtIndex:]
+ -[CAFRouteLegs objectAtIndexedSubscript:]
+ -[CAFRouteLegs parseError]
+ -[CAFRouteLegs routeLegs]
+ -[CAFRouteLegsCharacteristic formattedValue]
+ -[CAFRouteLegsCharacteristic routeLegsValue]
+ -[CAFRouteLegsCharacteristic setRouteLegsValue:]
+ -[CAFRouteStateCharacteristic formattedValue]
+ -[CAFRouteStateCharacteristic routeStateValue]
+ -[CAFRouteStateCharacteristic setRouteStateValue:]
+ -[CAFSelectSettingEntry initWithDisabled:symbolName:userVisibleDescription:userVisibleLabel:]
+ -[CAFSelectSettingEntryList arrayRepresentation]
+ -[CAFSelectSettingNotificationEntry initWithSymbolColor:symbolName:userVisibleLabel:]
+ -[CAFSelectSettingNotificationEntryList arrayRepresentation]
+ -[CAFSelectableNotificationEntry initWithDisabled:offSymbolColor:offSymbolName:offUserVisibleLabel:onSymbolColor:onSymbolName:onUserVisibleLabel:]
+ -[CAFSelectableNotificationEntryList arrayRepresentation]
+ -[CAFSettingNotificationEntry initWithSymbolColor:symbolName:userVisibleLabel:]
+ -[CAFSettingNotificationEntryList arrayRepresentation]
+ -[CAFSupportedColor .cxx_destruct]
+ -[CAFSupportedColor color]
+ -[CAFSupportedColor description]
+ -[CAFSupportedColor dictionaryRepresentation]
+ -[CAFSupportedColor initWithColor:]
+ -[CAFSupportedColor initWithDictionary:]
+ -[CAFSupportedColorCharacteristic formattedValue]
+ -[CAFSupportedColorCharacteristic setSupportedColorValue:]
+ -[CAFSupportedColorCharacteristic supportedColorValue]
+ -[CAFSupportedColors .cxx_destruct]
+ -[CAFSupportedColors arrayRepresentation]
+ -[CAFSupportedColors countByEnumeratingWithState:objects:count:]
+ -[CAFSupportedColors formattedValue]
+ -[CAFSupportedColors initWithArray:]
+ -[CAFSupportedColors initWithSupportedColors:]
+ -[CAFSupportedColors objectAtIndex:]
+ -[CAFSupportedColors objectAtIndexedSubscript:]
+ -[CAFSupportedColors parseError]
+ -[CAFSupportedColors supportedColors]
+ -[CAFSupportedColorsCharacteristic formattedValue]
+ -[CAFSupportedColorsCharacteristic setSupportedColorsValue:]
+ -[CAFSupportedColorsCharacteristic supportedColorsValue]
+ -[CAFSymbolImageWithColor initWithColor:name:]
+ -[CAFSymbolNameAndColor arrayRepresentation]
+ -[CAFSymbolNotificationUserAction initWithContentURLAction:disabled:symbolColor:symbolName:userVisibleLabel:]
+ -[CAFSymbolNotificationUserActions arrayRepresentation]
+ -[CAFTargetChargingLevel addObserver:]
+ -[CAFTargetChargingLevel name]
+ -[CAFTargetChargingLevel registerObserver:]
+ -[CAFTargetChargingLevel removeObserver:]
+ -[CAFTargetChargingLevel unregisterObserver:]
+ -[CAFTestComplexArrayItem initWithKey:value:]
+ -[CAFTestComplexArrayItems arrayRepresentation]
+ -[CAFTestComplexItem initWithKey:value:]
+ -[CAFTestComplexItems arrayRepresentation]
+ -[CAFTestComplexNestedItem initWithNestedKey:nestedValue:]
+ -[CAFTestComplexNestedItems arrayRepresentation]
+ -[CAFTestComplexNestedListItem initWithNestedKey:nestedValue:]
+ -[CAFTestComplexNestedListItems arrayRepresentation]
+ -[CAFTirePressure hasPressure]
+ -[CAFTirePressure hasSensorState]
+ -[CAFTrailingButton initWithContentURLAction:type:]
+ -[CAFTrailingButtons arrayRepresentation]
+ -[CAFUIConfiguration _characteristicDidUpdate:fromGroupUpdate:]
+ -[CAFUIConfiguration addObserver:]
+ -[CAFUIConfiguration configurationIdentifierCharacteristic]
+ -[CAFUIConfiguration configurationIdentifier]
+ -[CAFUIConfiguration configurationOptionsCharacteristic]
+ -[CAFUIConfiguration configurationOptions]
+ -[CAFUIConfiguration hasConfigurationOptions]
+ -[CAFUIConfiguration name]
+ -[CAFUIConfiguration registerObserver:]
+ -[CAFUIConfiguration registeredForConfigurationIdentifier]
+ -[CAFUIConfiguration registeredForConfigurationOptions]
+ -[CAFUIConfiguration removeObserver:]
+ -[CAFUIConfiguration unregisterObserver:]
+ -[CAFUIControl uiConfigurationService]
+ -[CAFUIControl uiConfiguration]
+ -[CAFUserVisibleDetailedDescription initWithImage:languageCode:text:]
+ -[CAFUserVisibleDetailedDescriptionList arrayRepresentation]
+ -[CAFVolume hasMute]
+ -[CAFVolume muteCharacteristic]
+ -[CAFVolume mute]
+ -[CAFVolume registeredForMute]
+ -[CAFVolume setMute:]
+ -[NSArray(CAF) arrayRepresentation]
+ GCC_except_table18
+ GCC_except_table61
+ _CAFAccessoryTypeLighting
+ _CAFAccessoryTypeNavigation
+ _CAFCharacteristicTypeApplicationEnabled
+ _CAFCharacteristicTypeBatteryConditioningState
+ _CAFCharacteristicTypeBrightness
+ _CAFCharacteristicTypeChargingLevel
+ _CAFCharacteristicTypeChargingModeIdentifier
+ _CAFCharacteristicTypeConfigurationIdentifier
+ _CAFCharacteristicTypeConfigurationOptions
+ _CAFCharacteristicTypeDefaultIndex
+ _CAFCharacteristicTypeDestination
+ _CAFCharacteristicTypeGeodeticSystem
+ _CAFCharacteristicTypeLegs
+ _CAFCharacteristicTypeMute
+ _CAFCharacteristicTypeOrigin
+ _CAFCharacteristicTypePrimaryColor
+ _CAFCharacteristicTypeRouteState
+ _CAFCharacteristicTypeSupportedColors
+ _CAFCharacteristicTypeUserEnabled
+ _CAFCharacteristicTypeUserVisibleApplicationName
+ _CAFCharacteristicTypeVehicleEnabled
+ _CAFServiceTypeBatteryConditioning
+ _CAFServiceTypeInteriorAmbientLights
+ _CAFServiceTypeMinimumChargingLevel
+ _CAFServiceTypeRoute
+ _CAFServiceTypeTargetChargingLevel
+ _CAFServiceTypeUIConfiguration
+ _CARPKeyCoordinateAltitude
+ _CARPKeyCoordinateLatitude
+ _CARPKeyCoordinateLongitude
+ _CARPKeyPointOfInterestEntryPoints
+ _CARPKeyPointOfInterestLocation
+ _CARPKeyPointOfInterestLocationThreshold
+ _CARPKeyPointOfInterestUserVisibleAddress
+ _CARPKeyPointOfInterestUserVisibleName
+ _CARPKeyRouteLegCoordinates
+ _CARPKeyRouteLegDestination
+ _CARPKeyRouteLegOrigin
+ _CARPKeySupportedColorColor
+ _NSStringFromBatteryConditioningState
+ _NSStringFromGeodeticSystem
+ _NSStringFromRouteState
+ _OBJC_CLASS_$_CAFBatteryConditioning
+ _OBJC_CLASS_$_CAFBatteryConditioningStateCharacteristic
+ _OBJC_CLASS_$_CAFChargingLevel
+ _OBJC_CLASS_$_CAFCoordinate
+ _OBJC_CLASS_$_CAFCoordinateCharacteristic
+ _OBJC_CLASS_$_CAFCoordinates
+ _OBJC_CLASS_$_CAFCoordinatesCharacteristic
+ _OBJC_CLASS_$_CAFGeodeticSystemCharacteristic
+ _OBJC_CLASS_$_CAFInteriorAmbientLights
+ _OBJC_CLASS_$_CAFLighting
+ _OBJC_CLASS_$_CAFMinimumChargingLevel
+ _OBJC_CLASS_$_CAFNavigation
+ _OBJC_CLASS_$_CAFPointOfInterest
+ _OBJC_CLASS_$_CAFPointOfInterestCharacteristic
+ _OBJC_CLASS_$_CAFPointsOfInterest
+ _OBJC_CLASS_$_CAFPointsOfInterestCharacteristic
+ _OBJC_CLASS_$_CAFRoute
+ _OBJC_CLASS_$_CAFRouteLeg
+ _OBJC_CLASS_$_CAFRouteLegCharacteristic
+ _OBJC_CLASS_$_CAFRouteLegs
+ _OBJC_CLASS_$_CAFRouteLegsCharacteristic
+ _OBJC_CLASS_$_CAFRouteStateCharacteristic
+ _OBJC_CLASS_$_CAFSupportedColor
+ _OBJC_CLASS_$_CAFSupportedColorCharacteristic
+ _OBJC_CLASS_$_CAFSupportedColors
+ _OBJC_CLASS_$_CAFSupportedColorsCharacteristic
+ _OBJC_CLASS_$_CAFTargetChargingLevel
+ _OBJC_CLASS_$_CAFUIConfiguration
+ _OBJC_IVAR_$_CAFCoordinate._altitude
+ _OBJC_IVAR_$_CAFCoordinate._latitude
+ _OBJC_IVAR_$_CAFCoordinate._longitude
+ _OBJC_IVAR_$_CAFCoordinates._coordinates
+ _OBJC_IVAR_$_CAFCoordinates._parseError
+ _OBJC_IVAR_$_CAFPointOfInterest._entryPoints
+ _OBJC_IVAR_$_CAFPointOfInterest._location
+ _OBJC_IVAR_$_CAFPointOfInterest._locationThreshold
+ _OBJC_IVAR_$_CAFPointOfInterest._userVisibleAddress
+ _OBJC_IVAR_$_CAFPointOfInterest._userVisibleName
+ _OBJC_IVAR_$_CAFPointsOfInterest._parseError
+ _OBJC_IVAR_$_CAFPointsOfInterest._pointOfInterests
+ _OBJC_IVAR_$_CAFRouteLeg._coordinates
+ _OBJC_IVAR_$_CAFRouteLeg._destination
+ _OBJC_IVAR_$_CAFRouteLeg._origin
+ _OBJC_IVAR_$_CAFRouteLegs._parseError
+ _OBJC_IVAR_$_CAFRouteLegs._routeLegs
+ _OBJC_IVAR_$_CAFSupportedColor._color
+ _OBJC_IVAR_$_CAFSupportedColors._parseError
+ _OBJC_IVAR_$_CAFSupportedColors._supportedColors
+ _OBJC_METACLASS_$_CAFBatteryConditioning
+ _OBJC_METACLASS_$_CAFBatteryConditioningStateCharacteristic
+ _OBJC_METACLASS_$_CAFChargingLevel
+ _OBJC_METACLASS_$_CAFCoordinate
+ _OBJC_METACLASS_$_CAFCoordinateCharacteristic
+ _OBJC_METACLASS_$_CAFCoordinates
+ _OBJC_METACLASS_$_CAFCoordinatesCharacteristic
+ _OBJC_METACLASS_$_CAFGeodeticSystemCharacteristic
+ _OBJC_METACLASS_$_CAFInteriorAmbientLights
+ _OBJC_METACLASS_$_CAFLighting
+ _OBJC_METACLASS_$_CAFMinimumChargingLevel
+ _OBJC_METACLASS_$_CAFNavigation
+ _OBJC_METACLASS_$_CAFPointOfInterest
+ _OBJC_METACLASS_$_CAFPointOfInterestCharacteristic
+ _OBJC_METACLASS_$_CAFPointsOfInterest
+ _OBJC_METACLASS_$_CAFPointsOfInterestCharacteristic
+ _OBJC_METACLASS_$_CAFRoute
+ _OBJC_METACLASS_$_CAFRouteLeg
+ _OBJC_METACLASS_$_CAFRouteLegCharacteristic
+ _OBJC_METACLASS_$_CAFRouteLegs
+ _OBJC_METACLASS_$_CAFRouteLegsCharacteristic
+ _OBJC_METACLASS_$_CAFRouteStateCharacteristic
+ _OBJC_METACLASS_$_CAFSupportedColor
+ _OBJC_METACLASS_$_CAFSupportedColorCharacteristic
+ _OBJC_METACLASS_$_CAFSupportedColors
+ _OBJC_METACLASS_$_CAFSupportedColorsCharacteristic
+ _OBJC_METACLASS_$_CAFTargetChargingLevel
+ _OBJC_METACLASS_$_CAFUIConfiguration
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_CAF
+ __OBJC_$_CATEGORY_NSArray_$_CAF
+ __OBJC_$_CLASS_METHODS_CAFBatteryConditioning
+ __OBJC_$_CLASS_METHODS_CAFBatteryConditioningStateCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFChargingLevel
+ __OBJC_$_CLASS_METHODS_CAFCoordinateCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFCoordinates
+ __OBJC_$_CLASS_METHODS_CAFCoordinatesCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFGeodeticSystemCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFInteriorAmbientLights
+ __OBJC_$_CLASS_METHODS_CAFLighting
+ __OBJC_$_CLASS_METHODS_CAFMinimumChargingLevel
+ __OBJC_$_CLASS_METHODS_CAFNavigation
+ __OBJC_$_CLASS_METHODS_CAFPointOfInterestCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFPointsOfInterest
+ __OBJC_$_CLASS_METHODS_CAFPointsOfInterestCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFRoute
+ __OBJC_$_CLASS_METHODS_CAFRouteLegCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFRouteLegs
+ __OBJC_$_CLASS_METHODS_CAFRouteLegsCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFRouteStateCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFSupportedColorCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFSupportedColors
+ __OBJC_$_CLASS_METHODS_CAFSupportedColorsCharacteristic
+ __OBJC_$_CLASS_METHODS_CAFTargetChargingLevel
+ __OBJC_$_CLASS_METHODS_CAFUIConfiguration
+ __OBJC_$_INSTANCE_METHODS_CAFBatteryConditioning
+ __OBJC_$_INSTANCE_METHODS_CAFBatteryConditioningStateCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFChargingLevel
+ __OBJC_$_INSTANCE_METHODS_CAFCoordinate
+ __OBJC_$_INSTANCE_METHODS_CAFCoordinateCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFCoordinates
+ __OBJC_$_INSTANCE_METHODS_CAFCoordinatesCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFGeodeticSystemCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFInteriorAmbientLights
+ __OBJC_$_INSTANCE_METHODS_CAFLighting
+ __OBJC_$_INSTANCE_METHODS_CAFMinimumChargingLevel
+ __OBJC_$_INSTANCE_METHODS_CAFNavigation
+ __OBJC_$_INSTANCE_METHODS_CAFPointOfInterest
+ __OBJC_$_INSTANCE_METHODS_CAFPointOfInterestCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFPointsOfInterest
+ __OBJC_$_INSTANCE_METHODS_CAFPointsOfInterestCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFRoute
+ __OBJC_$_INSTANCE_METHODS_CAFRouteLeg
+ __OBJC_$_INSTANCE_METHODS_CAFRouteLegCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFRouteLegs
+ __OBJC_$_INSTANCE_METHODS_CAFRouteLegsCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFRouteStateCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFSupportedColor
+ __OBJC_$_INSTANCE_METHODS_CAFSupportedColorCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFSupportedColors
+ __OBJC_$_INSTANCE_METHODS_CAFSupportedColorsCharacteristic
+ __OBJC_$_INSTANCE_METHODS_CAFTargetChargingLevel
+ __OBJC_$_INSTANCE_METHODS_CAFUIConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CAFCoordinate
+ __OBJC_$_INSTANCE_VARIABLES_CAFCoordinates
+ __OBJC_$_INSTANCE_VARIABLES_CAFPointOfInterest
+ __OBJC_$_INSTANCE_VARIABLES_CAFPointsOfInterest
+ __OBJC_$_INSTANCE_VARIABLES_CAFRouteLeg
+ __OBJC_$_INSTANCE_VARIABLES_CAFRouteLegs
+ __OBJC_$_INSTANCE_VARIABLES_CAFSupportedColor
+ __OBJC_$_INSTANCE_VARIABLES_CAFSupportedColors
+ __OBJC_$_PROP_LIST_CAFBatteryConditioning
+ __OBJC_$_PROP_LIST_CAFBatteryConditioningStateCharacteristic
+ __OBJC_$_PROP_LIST_CAFChargingLevel
+ __OBJC_$_PROP_LIST_CAFCoordinate
+ __OBJC_$_PROP_LIST_CAFCoordinateCharacteristic
+ __OBJC_$_PROP_LIST_CAFCoordinates
+ __OBJC_$_PROP_LIST_CAFCoordinatesCharacteristic
+ __OBJC_$_PROP_LIST_CAFGeodeticSystemCharacteristic
+ __OBJC_$_PROP_LIST_CAFInteriorAmbientLights
+ __OBJC_$_PROP_LIST_CAFLighting
+ __OBJC_$_PROP_LIST_CAFNavigation
+ __OBJC_$_PROP_LIST_CAFPointOfInterest
+ __OBJC_$_PROP_LIST_CAFPointOfInterestCharacteristic
+ __OBJC_$_PROP_LIST_CAFPointsOfInterest
+ __OBJC_$_PROP_LIST_CAFPointsOfInterestCharacteristic
+ __OBJC_$_PROP_LIST_CAFRoute
+ __OBJC_$_PROP_LIST_CAFRouteLeg
+ __OBJC_$_PROP_LIST_CAFRouteLegCharacteristic
+ __OBJC_$_PROP_LIST_CAFRouteLegs
+ __OBJC_$_PROP_LIST_CAFRouteLegsCharacteristic
+ __OBJC_$_PROP_LIST_CAFRouteStateCharacteristic
+ __OBJC_$_PROP_LIST_CAFSupportedColor
+ __OBJC_$_PROP_LIST_CAFSupportedColorCharacteristic
+ __OBJC_$_PROP_LIST_CAFSupportedColors
+ __OBJC_$_PROP_LIST_CAFSupportedColorsCharacteristic
+ __OBJC_$_PROP_LIST_CAFUIConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFBatteryConditioningObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFChargingLevelObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFInteriorAmbientLightsObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFUIConfigurationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFBatteryConditioningObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFChargingLevelObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFInteriorAmbientLightsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFUIConfigurationObserver
+ __OBJC_$_PROTOCOL_REFS_CAFBatteryConditioningObserver
+ __OBJC_$_PROTOCOL_REFS_CAFChargingLevelObserver
+ __OBJC_$_PROTOCOL_REFS_CAFInteriorAmbientLightsObserver
+ __OBJC_$_PROTOCOL_REFS_CAFLightingObserver
+ __OBJC_$_PROTOCOL_REFS_CAFMinimumChargingLevelObserver
+ __OBJC_$_PROTOCOL_REFS_CAFNavigationObserver
+ __OBJC_$_PROTOCOL_REFS_CAFRouteObserver
+ __OBJC_$_PROTOCOL_REFS_CAFTargetChargingLevelObserver
+ __OBJC_$_PROTOCOL_REFS_CAFUIConfigurationObserver
+ __OBJC_CLASS_PROTOCOLS_$_CAFCoordinates
+ __OBJC_CLASS_PROTOCOLS_$_CAFPointsOfInterest
+ __OBJC_CLASS_PROTOCOLS_$_CAFRouteLegs
+ __OBJC_CLASS_PROTOCOLS_$_CAFSupportedColors
+ __OBJC_CLASS_RO_$_CAFBatteryConditioning
+ __OBJC_CLASS_RO_$_CAFBatteryConditioningStateCharacteristic
+ __OBJC_CLASS_RO_$_CAFChargingLevel
+ __OBJC_CLASS_RO_$_CAFCoordinate
+ __OBJC_CLASS_RO_$_CAFCoordinateCharacteristic
+ __OBJC_CLASS_RO_$_CAFCoordinates
+ __OBJC_CLASS_RO_$_CAFCoordinatesCharacteristic
+ __OBJC_CLASS_RO_$_CAFGeodeticSystemCharacteristic
+ __OBJC_CLASS_RO_$_CAFInteriorAmbientLights
+ __OBJC_CLASS_RO_$_CAFLighting
+ __OBJC_CLASS_RO_$_CAFMinimumChargingLevel
+ __OBJC_CLASS_RO_$_CAFNavigation
+ __OBJC_CLASS_RO_$_CAFPointOfInterest
+ __OBJC_CLASS_RO_$_CAFPointOfInterestCharacteristic
+ __OBJC_CLASS_RO_$_CAFPointsOfInterest
+ __OBJC_CLASS_RO_$_CAFPointsOfInterestCharacteristic
+ __OBJC_CLASS_RO_$_CAFRoute
+ __OBJC_CLASS_RO_$_CAFRouteLeg
+ __OBJC_CLASS_RO_$_CAFRouteLegCharacteristic
+ __OBJC_CLASS_RO_$_CAFRouteLegs
+ __OBJC_CLASS_RO_$_CAFRouteLegsCharacteristic
+ __OBJC_CLASS_RO_$_CAFRouteStateCharacteristic
+ __OBJC_CLASS_RO_$_CAFSupportedColor
+ __OBJC_CLASS_RO_$_CAFSupportedColorCharacteristic
+ __OBJC_CLASS_RO_$_CAFSupportedColors
+ __OBJC_CLASS_RO_$_CAFSupportedColorsCharacteristic
+ __OBJC_CLASS_RO_$_CAFTargetChargingLevel
+ __OBJC_CLASS_RO_$_CAFUIConfiguration
+ __OBJC_LABEL_PROTOCOL_$_CAFBatteryConditioningObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFChargingLevelObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFInteriorAmbientLightsObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFLightingObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFMinimumChargingLevelObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFNavigationObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFRouteObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFTargetChargingLevelObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFUIConfigurationObserver
+ __OBJC_METACLASS_RO_$_CAFBatteryConditioning
+ __OBJC_METACLASS_RO_$_CAFBatteryConditioningStateCharacteristic
+ __OBJC_METACLASS_RO_$_CAFChargingLevel
+ __OBJC_METACLASS_RO_$_CAFCoordinate
+ __OBJC_METACLASS_RO_$_CAFCoordinateCharacteristic
+ __OBJC_METACLASS_RO_$_CAFCoordinates
+ __OBJC_METACLASS_RO_$_CAFCoordinatesCharacteristic
+ __OBJC_METACLASS_RO_$_CAFGeodeticSystemCharacteristic
+ __OBJC_METACLASS_RO_$_CAFInteriorAmbientLights
+ __OBJC_METACLASS_RO_$_CAFLighting
+ __OBJC_METACLASS_RO_$_CAFMinimumChargingLevel
+ __OBJC_METACLASS_RO_$_CAFNavigation
+ __OBJC_METACLASS_RO_$_CAFPointOfInterest
+ __OBJC_METACLASS_RO_$_CAFPointOfInterestCharacteristic
+ __OBJC_METACLASS_RO_$_CAFPointsOfInterest
+ __OBJC_METACLASS_RO_$_CAFPointsOfInterestCharacteristic
+ __OBJC_METACLASS_RO_$_CAFRoute
+ __OBJC_METACLASS_RO_$_CAFRouteLeg
+ __OBJC_METACLASS_RO_$_CAFRouteLegCharacteristic
+ __OBJC_METACLASS_RO_$_CAFRouteLegs
+ __OBJC_METACLASS_RO_$_CAFRouteLegsCharacteristic
+ __OBJC_METACLASS_RO_$_CAFRouteStateCharacteristic
+ __OBJC_METACLASS_RO_$_CAFSupportedColor
+ __OBJC_METACLASS_RO_$_CAFSupportedColorCharacteristic
+ __OBJC_METACLASS_RO_$_CAFSupportedColors
+ __OBJC_METACLASS_RO_$_CAFSupportedColorsCharacteristic
+ __OBJC_METACLASS_RO_$_CAFTargetChargingLevel
+ __OBJC_METACLASS_RO_$_CAFUIConfiguration
+ __OBJC_PROTOCOL_$_CAFBatteryConditioningObserver
+ __OBJC_PROTOCOL_$_CAFChargingLevelObserver
+ __OBJC_PROTOCOL_$_CAFInteriorAmbientLightsObserver
+ __OBJC_PROTOCOL_$_CAFLightingObserver
+ __OBJC_PROTOCOL_$_CAFMinimumChargingLevelObserver
+ __OBJC_PROTOCOL_$_CAFNavigationObserver
+ __OBJC_PROTOCOL_$_CAFRouteObserver
+ __OBJC_PROTOCOL_$_CAFTargetChargingLevelObserver
+ __OBJC_PROTOCOL_$_CAFUIConfigurationObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFBatteryConditioningObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFChargingLevelObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFInteriorAmbientLightsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFLightingObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFMinimumChargingLevelObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFNavigationObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFRouteObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFTargetChargingLevelObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CAFUIConfigurationObserver
+ ___30-[CAFRouteLegs initWithArray:]_block_invoke
+ ___30-[CAFRouteLegs initWithArray:]_block_invoke.cold.1
+ ___32-[CAFCoordinates initWithArray:]_block_invoke
+ ___32-[CAFCoordinates initWithArray:]_block_invoke.cold.1
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.246
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.246.cold.1
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.247
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.247.cold.1
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.247.cold.2
+ ___34-[_CAFCarDataClientProxy activate]_block_invoke.248
+ ___36-[CAFSupportedColors initWithArray:]_block_invoke
+ ___36-[CAFSupportedColors initWithArray:]_block_invoke.cold.1
+ ___37-[CAFPointsOfInterest initWithArray:]_block_invoke
+ ___37-[CAFPointsOfInterest initWithArray:]_block_invoke.cold.1
+ ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.120
+ ___block_literal_global.1587
+ ___block_literal_global.1589
+ ___block_literal_global.225
+ ___block_literal_global.227
+ ___block_literal_global.693
+ ___block_literal_global.695
+ _objc_msgSend$_isEntitled
+ _objc_msgSend$altitude
+ _objc_msgSend$applicationEnabled
+ _objc_msgSend$applicationEnabledCharacteristic
+ _objc_msgSend$arrayRepresentation
+ _objc_msgSend$batteryConditioningService
+ _objc_msgSend$batteryConditioningService:didUpdateBatteryConditioningState:
+ _objc_msgSend$batteryConditioningState
+ _objc_msgSend$batteryConditioningStateCharacteristic
+ _objc_msgSend$batteryConditioningStateValue
+ _objc_msgSend$brightness
+ _objc_msgSend$brightnessCharacteristic
+ _objc_msgSend$carPlayTemplateUIHost
+ _objc_msgSend$chargingLevel
+ _objc_msgSend$chargingLevelCharacteristic
+ _objc_msgSend$chargingLevelRange
+ _objc_msgSend$chargingLevelService:didUpdateChargingLevel:
+ _objc_msgSend$chargingLevelService:didUpdateDistanceKM:
+ _objc_msgSend$chargingLevelService:didUpdateDistanceMiles:
+ _objc_msgSend$chargingModeIdentifier
+ _objc_msgSend$chargingModeIdentifierCharacteristic
+ _objc_msgSend$chargingStatusService:didUpdateChargingModeIdentifier:
+ _objc_msgSend$configurationIdentifier
+ _objc_msgSend$configurationIdentifierCharacteristic
+ _objc_msgSend$configurationOptions
+ _objc_msgSend$configurationOptionsCharacteristic
+ _objc_msgSend$coordinateValue
+ _objc_msgSend$coordinates
+ _objc_msgSend$coordinatesValue
+ _objc_msgSend$coordinatesWithArray:
+ _objc_msgSend$cpNavTool
+ _objc_msgSend$defaultIndex
+ _objc_msgSend$defaultIndexCharacteristic
+ _objc_msgSend$destination
+ _objc_msgSend$destinationCharacteristic
+ _objc_msgSend$entryPoints
+ _objc_msgSend$geodeticSystem
+ _objc_msgSend$geodeticSystemCharacteristic
+ _objc_msgSend$geodeticSystemValue
+ _objc_msgSend$initWithCoordinates:
+ _objc_msgSend$initWithPointOfInterests:
+ _objc_msgSend$initWithRouteLegs:
+ _objc_msgSend$initWithSupportedColors:
+ _objc_msgSend$interiorAmbientLightsService
+ _objc_msgSend$interiorAmbientLightsService:didUpdateBrightness:
+ _objc_msgSend$interiorAmbientLightsService:didUpdatePrimaryColor:
+ _objc_msgSend$interiorAmbientLightsService:didUpdateSupportedColors:
+ _objc_msgSend$latitude
+ _objc_msgSend$legs
+ _objc_msgSend$legsCharacteristic
+ _objc_msgSend$location
+ _objc_msgSend$locationThreshold
+ _objc_msgSend$longitude
+ _objc_msgSend$maps
+ _objc_msgSend$minimumChargingLevelService
+ _objc_msgSend$modeItemsService:didUpdateDefaultIndex:
+ _objc_msgSend$mute
+ _objc_msgSend$muteCharacteristic
+ _objc_msgSend$origin
+ _objc_msgSend$originCharacteristic
+ _objc_msgSend$pointOfInterestValue
+ _objc_msgSend$pointOfInterests
+ _objc_msgSend$pointsOfInterestValue
+ _objc_msgSend$pointsOfInterestWithArray:
+ _objc_msgSend$primaryColor
+ _objc_msgSend$primaryColorCharacteristic
+ _objc_msgSend$routeLegValue
+ _objc_msgSend$routeLegs
+ _objc_msgSend$routeLegsValue
+ _objc_msgSend$routeLegsWithArray:
+ _objc_msgSend$routeService
+ _objc_msgSend$routeService:didUpdateApplicationEnabled:
+ _objc_msgSend$routeService:didUpdateDestination:
+ _objc_msgSend$routeService:didUpdateGeodeticSystem:
+ _objc_msgSend$routeService:didUpdateLegs:
+ _objc_msgSend$routeService:didUpdateOrigin:
+ _objc_msgSend$routeService:didUpdateRouteState:
+ _objc_msgSend$routeService:didUpdateUserEnabled:
+ _objc_msgSend$routeService:didUpdateUserVisibleApplicationName:
+ _objc_msgSend$routeService:didUpdateVehicleEnabled:
+ _objc_msgSend$routeState
+ _objc_msgSend$routeStateCharacteristic
+ _objc_msgSend$routeStateValue
+ _objc_msgSend$setGeodeticSystemValue:
+ _objc_msgSend$setPointOfInterestValue:
+ _objc_msgSend$setRouteLegsValue:
+ _objc_msgSend$setRouteStateValue:
+ _objc_msgSend$supportedColorValue
+ _objc_msgSend$supportedColors
+ _objc_msgSend$supportedColorsCharacteristic
+ _objc_msgSend$supportedColorsValue
+ _objc_msgSend$supportedColorsWithArray:
+ _objc_msgSend$targetChargingLevelService
+ _objc_msgSend$uiConfigurationService
+ _objc_msgSend$uiConfigurationService:didUpdateConfigurationIdentifier:
+ _objc_msgSend$uiConfigurationService:didUpdateConfigurationOptions:
+ _objc_msgSend$userEnabled
+ _objc_msgSend$userEnabledCharacteristic
+ _objc_msgSend$userVisibleAddress
+ _objc_msgSend$userVisibleApplicationName
+ _objc_msgSend$userVisibleApplicationNameCharacteristic
+ _objc_msgSend$userVisibleName
+ _objc_msgSend$vehicleEnabled
+ _objc_msgSend$vehicleEnabledCharacteristic
+ _objc_msgSend$volumeService:didUpdateMute:
- -[CAFBatteryLevel batteryTargetChargeLevelCharacteristic]
- -[CAFBatteryLevel batteryTargetChargeLevelMeasurementRange]
- -[CAFBatteryLevel batteryTargetChargeLevelRange]
- -[CAFBatteryLevel batteryTargetChargeLevel]
- -[CAFBatteryLevel registeredForBatteryTargetChargeLevel]
- -[CAFBatteryLevel setBatteryTargetChargeLevel:]
- -[CAFCarManager _setupCafdConnectionIfAvailable].cold.3
- -[CAFCarManager _setupCafdConnectionIfAvailable].cold.4
- -[CAFSettingProminenceLevelCharacteristic hasClimateCard]
- -[CAFSettingProminenceLevelCharacteristic hasClimateQuickAction]
- -[CAFSettingProminenceLevelCharacteristic setHasClimateCard:]
- -[CAFSettingProminenceLevelCharacteristic setHasClimateQuickAction:]
- GCC_except_table16
- GCC_except_table60
- _CAFCharacteristicTypeBatteryTargetChargeLevel
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.240
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.240.cold.1
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.241
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.241.cold.1
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.241.cold.2
- ___34-[_CAFCarDataClientProxy activate]_block_invoke.242
- ___56-[CAFCarManager shouldAllocAccessoryType:serviceConfig:]_block_invoke.115
- ___block_literal_global.1479
- ___block_literal_global.1481
- ___block_literal_global.213
- ___block_literal_global.215
- ___block_literal_global.657
- ___block_literal_global.659
- _objc_msgSend$batteryLevelService:didUpdateBatteryTargetChargeLevel:
- _objc_msgSend$batteryTargetChargeLevel
- _objc_msgSend$batteryTargetChargeLevelCharacteristic
- _objc_msgSend$batteryTargetChargeLevelRange
CStrings:
+ "%{public}@: Error parsing dictionary from Coordinates array - %{public}@"
+ "%{public}@: Error parsing dictionary from PointsOfInterest array - %{public}@"
+ "%{public}@: Error parsing dictionary from RouteLegs array - %{public}@"
+ "%{public}@: Error parsing dictionary from SupportedColors array - %{public}@"
+ "0x0000000002100001"
+ "0x000000000E000002"
+ "0x0000000011100005"
+ "0x0000000019000008"
+ "0x0000000019000009"
+ "0x000000001900000A"
+ "0x000000001E000101"
+ "0x0000000025000001"
+ "0x0000000030000039"
+ "0x0000000033000009"
+ "0x000000004000000B"
+ "0x000000004000000C"
+ "0x000000004000000D"
+ "0x0000000045000101"
+ "0x0000000045000102"
+ "0x0000000045000103"
+ "0x0000000045000104"
+ "0x0000000045000105"
+ "0x0000000045000106"
+ "0x0000000045000107"
+ "0x0000000045000108"
+ "0x0000000045000109"
+ "0x0000000047000011"
+ "0x0000000048000010"
+ "0x0000000052000001"
+ "0x0000000052000002"
+ "0x0000000052000003"
+ "<%@: %p value=%@ error=%@>"
+ "<%@: %p { %@: %@ }>"
+ "<%@: %p { %@: %@, %@: %@, %@: %u, %@: %@, %@: %@ }>"
+ "<%@: %p { %@: %g, %@: %g, %@: %g }>"
+ "@\"CAFCoordinate\""
+ "@\"CAFPointOfInterest\""
+ "@116@0:8@16@24I32@36C44@48@56@64@72@80@88C96@100@108"
+ "@28@0:8@16C24"
+ "@28@0:8@16I24"
+ "@28@0:8f16f20f24"
+ "@36@0:8C16@20@28"
+ "@40@0:8@16@24S32C36"
+ "@44@0:8B16@20@28@36"
+ "@48@0:8@16B24C28@32@40"
+ "@48@0:8C16Q20C28@32@40"
+ "@52@0:8@16@24I32@36@44"
+ "@56@0:8C16@20@28C36@40@48"
+ "@60@0:8B16C20@24@32C40@44@52"
+ "ApplicationEnabled"
+ "ApplicationError"
+ "Arrived"
+ "BatteryConditioning"
+ "BatteryConditioningState"
+ "Brightness"
+ "CAFBatteryConditioning"
+ "CAFBatteryConditioningObserver"
+ "CAFBatteryConditioningStateCharacteristic"
+ "CAFChargingLevel"
+ "CAFChargingLevelObserver"
+ "CAFCoordinate"
+ "CAFCoordinateCharacteristic"
+ "CAFCoordinates"
+ "CAFCoordinatesCharacteristic"
+ "CAFGeodeticSystemCharacteristic"
+ "CAFInteriorAmbientLights"
+ "CAFInteriorAmbientLightsObserver"
+ "CAFLighting"
+ "CAFLightingObserver"
+ "CAFMinimumChargingLevel"
+ "CAFMinimumChargingLevelObserver"
+ "CAFNavigation"
+ "CAFNavigationObserver"
+ "CAFPointOfInterest"
+ "CAFPointOfInterestCharacteristic"
+ "CAFPointsOfInterest"
+ "CAFPointsOfInterestCharacteristic"
+ "CAFRoute"
+ "CAFRouteLeg"
+ "CAFRouteLegCharacteristic"
+ "CAFRouteLegs"
+ "CAFRouteLegsCharacteristic"
+ "CAFRouteObserver"
+ "CAFRouteStateCharacteristic"
+ "CAFSupportedColor"
+ "CAFSupportedColorCharacteristic"
+ "CAFSupportedColors"
+ "CAFSupportedColorsCharacteristic"
+ "CAFTargetChargingLevel"
+ "CAFTargetChargingLevelObserver"
+ "CAFUIConfiguration"
+ "CAFUIConfigurationObserver"
+ "CPNavTool"
+ "CarPlayTemplateUIHost"
+ "ChargingLevel"
+ "ChargingModeIdentifier"
+ "ConfigurationIdentifier"
+ "ConfigurationOptions"
+ "Cooling"
+ "Coordinate"
+ "Coordinates"
+ "DefaultIndex"
+ "Destination"
+ "Discharging"
+ "Front"
+ "GCJ02"
+ "GeodeticSystem"
+ "Heating"
+ "InteriorAmbientLights"
+ "Legs"
+ "Lighting"
+ "Locating"
+ "Maps"
+ "MinimumChargingLevel"
+ "Mute"
+ "NotActive"
+ "Origin"
+ "PointOfInterest"
+ "PointsOfInterest"
+ "PrimaryColor"
+ "ProceedToRoute"
+ "Rear"
+ "Rerouting"
+ "Route"
+ "RouteLeg"
+ "RouteLegs"
+ "RouteState"
+ "SupportedColor"
+ "SupportedColors"
+ "T@\"CAFBatteryConditioning\",R,N"
+ "T@\"CAFBatteryConditioningStateCharacteristic\",R,N"
+ "T@\"CAFCoordinate\",C,N"
+ "T@\"CAFCoordinate\",R,N,V_location"
+ "T@\"CAFCoordinates\",C,N"
+ "T@\"CAFGeodeticSystemCharacteristic\",R,N"
+ "T@\"CAFInteriorAmbientLights\",R,N"
+ "T@\"CAFLighting\",R,N"
+ "T@\"CAFMinimumChargingLevel\",R,N"
+ "T@\"CAFNavigation\",R,N"
+ "T@\"CAFPointOfInterest\",&,N"
+ "T@\"CAFPointOfInterest\",C,N"
+ "T@\"CAFPointOfInterest\",R,N,V_destination"
+ "T@\"CAFPointOfInterest\",R,N,V_origin"
+ "T@\"CAFPointOfInterestCharacteristic\",R,N"
+ "T@\"CAFPointsOfInterest\",C,N"
+ "T@\"CAFRoute\",R,N"
+ "T@\"CAFRouteLeg\",C,N"
+ "T@\"CAFRouteLegs\",C,N"
+ "T@\"CAFRouteLegsCharacteristic\",R,N"
+ "T@\"CAFRouteStateCharacteristic\",R,N"
+ "T@\"CAFSupportedColor\",C,N"
+ "T@\"CAFSupportedColors\",C,N"
+ "T@\"CAFSupportedColors\",R,N"
+ "T@\"CAFSupportedColorsCharacteristic\",R,N"
+ "T@\"CAFTargetChargingLevel\",R,N"
+ "T@\"CAFUIConfiguration\",R,N"
+ "T@\"NSArray\",R,C,N,V_coordinates"
+ "T@\"NSArray\",R,C,N,V_entryPoints"
+ "T@\"NSArray\",R,N,V_coordinates"
+ "T@\"NSArray\",R,N,V_pointOfInterests"
+ "T@\"NSArray\",R,N,V_routeLegs"
+ "T@\"NSArray\",R,N,V_supportedColors"
+ "T@\"NSString\",R,C,N,V_color"
+ "T@\"NSString\",R,C,N,V_userVisibleAddress"
+ "T@\"NSString\",R,C,N,V_userVisibleName"
+ "TI,R,N,V_locationThreshold"
+ "TargetChargingLevel"
+ "Tf,R,N,V_altitude"
+ "Tf,R,N,V_latitude"
+ "Tf,R,N,V_longitude"
+ "UIConfiguration"
+ "Unknown"
+ "UserEnabled"
+ "UserVisibleApplicationName"
+ "VehicleEnabled"
+ "WGS84"
+ "_altitude"
+ "_coordinates"
+ "_destination"
+ "_entryPoints"
+ "_isEntitled"
+ "_latitude"
+ "_location"
+ "_locationThreshold"
+ "_longitude"
+ "_origin"
+ "_pointOfInterests"
+ "_routeLegs"
+ "_supportedColors"
+ "_userVisibleAddress"
+ "_userVisibleName"
+ "altitude"
+ "applicationEnabled"
+ "applicationEnabledCharacteristic"
+ "applicationEnabledInvalid"
+ "arrayRepresentation"
+ "batteryConditioning"
+ "batteryConditioningService"
+ "batteryConditioningService:didUpdateBatteryConditioningState:"
+ "batteryConditioningState"
+ "batteryConditioningStateCharacteristic"
+ "batteryConditioningStateValue"
+ "brightness"
+ "brightnessCharacteristic"
+ "brightnessRange"
+ "carPlayTemplateUIHost"
+ "chargingLevel"
+ "chargingLevelCharacteristic"
+ "chargingLevelMeasurementRange"
+ "chargingLevelRange"
+ "chargingLevelService:didUpdateChargingLevel:"
+ "chargingLevelService:didUpdateDistanceKM:"
+ "chargingLevelService:didUpdateDistanceMiles:"
+ "chargingModeIdentifier"
+ "chargingModeIdentifierCharacteristic"
+ "chargingStatusService:didUpdateChargingModeIdentifier:"
+ "com.apple.CarPlayTemplateUIHost"
+ "com.apple.Maps"
+ "configurationIdentifier"
+ "configurationIdentifierCharacteristic"
+ "configurationOptions"
+ "configurationOptionsCharacteristic"
+ "coordinateValue"
+ "coordinates"
+ "coordinatesValue"
+ "coordinatesWithArray:"
+ "coordinatesWithCoordinates:"
+ "cpNavTool"
+ "defaultIndex"
+ "defaultIndexCharacteristic"
+ "defaultIndexRange"
+ "destination"
+ "destinationCharacteristic"
+ "destinationInvalid"
+ "entryPoints"
+ "f"
+ "geodeticSystem"
+ "geodeticSystemCharacteristic"
+ "geodeticSystemValue"
+ "hasBrightness"
+ "hasChargingModeIdentifier"
+ "hasConfigurationOptions"
+ "hasDefaultIndex"
+ "hasDistanceKM"
+ "hasDistanceMiles"
+ "hasLegs"
+ "hasMute"
+ "hasPressure"
+ "hasSensorState"
+ "hasSupportedColors"
+ "initWithAltitude:latitude:longitude:"
+ "initWithArtist:ensemble:frequency:identifier:mediaItemCategory:mediaItemCategoryUserVisibleLabel:mediaItemGroup:mediaItemImageIdentifier:mediaItemName:mediaItemShortName:mediaItemType:multicast:title:userVisibleDescription:"
+ "initWithColor:"
+ "initWithColor:name:"
+ "initWithColor:prominenceLevel:sortOrder:userVisibleLabel:userVisibleValue:"
+ "initWithContentURLAction:disabled:symbolColor:symbolName:userVisibleLabel:"
+ "initWithContentURLAction:symbolName:userVisibleLabel:"
+ "initWithContentURLAction:type:"
+ "initWithContentURLAction:userVisibleLabel:"
+ "initWithCoordinates:"
+ "initWithCoordinates:destination:origin:"
+ "initWithDisabled:offSymbolColor:offSymbolName:offUserVisibleLabel:onSymbolColor:onSymbolName:onUserVisibleLabel:"
+ "initWithDisabled:symbolName:userVisibleDescription:userVisibleLabel:"
+ "initWithEntryPoints:location:locationThreshold:userVisibleAddress:userVisibleName:"
+ "initWithIdentifier:imageData:"
+ "initWithIdentifier:name:sortOrder:state:"
+ "initWithImage:languageCode:text:"
+ "initWithKey:value:"
+ "initWithNestedKey:nestedValue:"
+ "initWithOffSymbolColor:offSymbolName:offUserVisibleLabel:onSymbolColor:onSymbolName:onUserVisibleLabel:"
+ "initWithPointOfInterests:"
+ "initWithRouteLegs:"
+ "initWithSupportedColors:"
+ "initWithSymbolColor:symbolName:userVisibleLabel:"
+ "initWithSymbolName:userVisibleLabel:"
+ "interiorAmbientLights"
+ "interiorAmbientLightsService"
+ "interiorAmbientLightsService:didUpdateBrightness:"
+ "interiorAmbientLightsService:didUpdatePrimaryColor:"
+ "interiorAmbientLightsService:didUpdateSupportedColors:"
+ "latitude"
+ "legs"
+ "legsCharacteristic"
+ "legsInvalid"
+ "lighting"
+ "location"
+ "locationThreshold"
+ "longitude"
+ "maps"
+ "minimumChargingLevel"
+ "minimumChargingLevelService"
+ "modeItemsService:didUpdateDefaultIndex:"
+ "mute"
+ "muteCharacteristic"
+ "navigation"
+ "origin"
+ "originCharacteristic"
+ "originInvalid"
+ "pointOfInterestValue"
+ "pointOfInterests"
+ "pointsOfInterestValue"
+ "pointsOfInterestWithArray:"
+ "pointsOfInterestWithPointOfInterests:"
+ "primaryColor"
+ "primaryColorCharacteristic"
+ "registeredForApplicationEnabled"
+ "registeredForBatteryConditioningState"
+ "registeredForBrightness"
+ "registeredForChargingLevel"
+ "registeredForChargingModeIdentifier"
+ "registeredForConfigurationIdentifier"
+ "registeredForConfigurationOptions"
+ "registeredForDefaultIndex"
+ "registeredForDestination"
+ "registeredForGeodeticSystem"
+ "registeredForLegs"
+ "registeredForMute"
+ "registeredForOrigin"
+ "registeredForPrimaryColor"
+ "registeredForRouteState"
+ "registeredForSupportedColors"
+ "registeredForUserEnabled"
+ "registeredForUserVisibleApplicationName"
+ "registeredForVehicleEnabled"
+ "route"
+ "routeLegValue"
+ "routeLegs"
+ "routeLegsValue"
+ "routeLegsWithArray:"
+ "routeLegsWithRouteLegs:"
+ "routeService"
+ "routeService:didUpdateApplicationEnabled:"
+ "routeService:didUpdateDestination:"
+ "routeService:didUpdateGeodeticSystem:"
+ "routeService:didUpdateLegs:"
+ "routeService:didUpdateOrigin:"
+ "routeService:didUpdateRouteState:"
+ "routeService:didUpdateUserEnabled:"
+ "routeService:didUpdateUserVisibleApplicationName:"
+ "routeService:didUpdateVehicleEnabled:"
+ "routeState"
+ "routeStateCharacteristic"
+ "routeStateValue"
+ "setApplicationEnabled:"
+ "setBatteryConditioningStateValue:"
+ "setBrightness:"
+ "setChargingLevel:"
+ "setCoordinateValue:"
+ "setCoordinatesValue:"
+ "setDestination:"
+ "setGeodeticSystem:"
+ "setGeodeticSystemValue:"
+ "setLegs:"
+ "setMute:"
+ "setOrigin:"
+ "setPointOfInterestValue:"
+ "setPointsOfInterestValue:"
+ "setPrimaryColor:"
+ "setRouteLegValue:"
+ "setRouteLegsValue:"
+ "setRouteState:"
+ "setRouteStateValue:"
+ "setSupportedColorValue:"
+ "setSupportedColorsValue:"
+ "setUserEnabled:"
+ "setUserVisibleApplicationName:"
+ "supportedColorValue"
+ "supportedColors"
+ "supportedColorsCharacteristic"
+ "supportedColorsValue"
+ "supportedColorsWithArray:"
+ "supportedColorsWithSupportedColors:"
+ "targetChargingLevel"
+ "targetChargingLevelService"
+ "uiConfiguration"
+ "uiConfigurationService"
+ "uiConfigurationService:didUpdateConfigurationIdentifier:"
+ "uiConfigurationService:didUpdateConfigurationOptions:"
+ "userEnabled"
+ "userEnabledCharacteristic"
+ "userEnabledInvalid"
+ "userVisibleAddress"
+ "userVisibleApplicationName"
+ "userVisibleApplicationNameCharacteristic"
+ "userVisibleApplicationNameInvalid"
+ "userVisibleName"
+ "v28@0:8@\"CAFBatteryConditioning\"16C24"
+ "v28@0:8@\"CAFInteriorAmbientLights\"16I24"
+ "v28@0:8@\"CAFRoute\"16B24"
+ "v28@0:8@\"CAFRoute\"16C24"
+ "v28@0:8@\"CAFVolume\"16B24"
+ "v32@0:8@\"CAFChargingLevel\"16@\"NSMeasurement\"24"
+ "v32@0:8@\"CAFChargingStatus\"16@\"NSString\"24"
+ "v32@0:8@\"CAFInteriorAmbientLights\"16@\"CAFSupportedColors\"24"
+ "v32@0:8@\"CAFInteriorAmbientLights\"16@\"NSString\"24"
+ "v32@0:8@\"CAFRoute\"16@\"CAFPointOfInterest\"24"
+ "v32@0:8@\"CAFRoute\"16@\"CAFRouteLegs\"24"
+ "v32@0:8@\"CAFRoute\"16@\"NSString\"24"
+ "v32@0:8@\"CAFUIConfiguration\"16@\"NSArray\"24"
+ "v32@0:8@\"CAFUIConfiguration\"16@\"NSString\"24"
+ "vehicleEnabled"
+ "vehicleEnabledCharacteristic"
+ "volumeService:didUpdateMute:"
- "0x0000000040000001"
- "BatteryTargetChargeLevel"
- "batteryLevelService:didUpdateBatteryTargetChargeLevel:"
- "batteryTargetChargeLevel"
- "batteryTargetChargeLevelCharacteristic"
- "batteryTargetChargeLevelMeasurementRange"
- "batteryTargetChargeLevelRange"
- "climateCard=%@"
- "climateQuickAction=%@"
- "hasClimateCard"
- "hasClimateQuickAction"
- "registeredForBatteryTargetChargeLevel"
- "setBatteryTargetChargeLevel:"
- "setHasClimateCard:"
- "setHasClimateQuickAction:"

```
