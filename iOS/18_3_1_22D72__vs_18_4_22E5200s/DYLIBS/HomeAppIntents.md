## HomeAppIntents

> `/System/Library/PrivateFrameworks/HomeAppIntents.framework/HomeAppIntents`

```diff

-989.4.12.0.0
-  __TEXT.__text: 0x158dc4
-  __TEXT.__auth_stubs: 0x28c0
-  __TEXT.__const: 0x1c3f8
-  __TEXT.__cstring: 0x3d43
-  __TEXT.__swift5_typeref: 0xc2d6
-  __TEXT.__swift5_reflstr: 0x2873
-  __TEXT.__swift5_assocty: 0x3e20
-  __TEXT.__constg_swiftt: 0x2438
-  __TEXT.__swift5_fieldmd: 0x3284
-  __TEXT.__swift5_builtin: 0xf0
-  __TEXT.__swift5_proto: 0x1cbc
-  __TEXT.__swift5_types: 0x478
-  __TEXT.__oslogstring: 0x10f9
-  __TEXT.__swift5_capture: 0x168
+1025.0.0.1.1
+  __TEXT.__text: 0x18e9b8
+  __TEXT.__auth_stubs: 0x2f40
+  __TEXT.__const: 0x1f6e8
+  __TEXT.__cstring: 0x3332
+  __TEXT.__swift5_typeref: 0xccde
+  __TEXT.__swift5_reflstr: 0x2c73
+  __TEXT.__swift5_assocty: 0x40e0
+  __TEXT.__constg_swiftt: 0x2720
+  __TEXT.__swift5_fieldmd: 0x3618
+  __TEXT.__swift5_builtin: 0x104
+  __TEXT.__swift5_proto: 0x1e2c
+  __TEXT.__swift5_types: 0x4c8
+  __TEXT.__swift_as_entry: 0x638
+  __TEXT.__swift_as_ret: 0x50c
+  __TEXT.__swift5_capture: 0x390
+  __TEXT.__oslogstring: 0x1e79
   __TEXT.__swift5_mpenum: 0x50
-  __TEXT.__unwind_info: 0x6948
-  __TEXT.__eh_frame: 0x6fc0
-  __TEXT.__objc_methname: 0x2a
-  __DATA_CONST.__got: 0xdf8
-  __DATA_CONST.__const: 0x148
+  __TEXT.__unwind_info: 0x6d28
+  __TEXT.__eh_frame: 0x8c98
+  __TEXT.__objc_methname: 0x5a
+  __DATA_CONST.__got: 0xfe8
+  __DATA_CONST.__const: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1460
-  __AUTH_CONST.__auth_ptr: 0xc88
-  __AUTH_CONST.__const: 0x7320
-  __AUTH.__data: 0x6e8
-  __DATA.__data: 0x75a8
-  __DATA.__common: 0xb10
-  __DATA.__bss: 0x39ab0
+  __DATA_CONST.__objc_selrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x17a0
+  __AUTH_CONST.__auth_ptr: 0xd20
+  __AUTH_CONST.__const: 0x7df0
+  __AUTH.__data: 0x9c0
+  __DATA.__data: 0x8460
+  __DATA.__common: 0xa70
+  __DATA.__bss: 0x3c940
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit
+  - /System/Library/Frameworks/Matter.framework/Matter
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/HomeDataModel.framework/HomeDataModel
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8384
-  Symbols:   159
-  CStrings:  622
+  Functions: 9439
+  Symbols:   193
+  CStrings:  636
 
Symbols:
+ _MGGetSInt32Answer
+ _MTRErrorDomain
+ _OBJC_CLASS_$_HMAccessory
+ _OBJC_CLASS_$_HMCharacteristic
+ _OBJC_CLASS_$_HMHome
+ _OBJC_CLASS_$_HMRoom
+ _OBJC_CLASS_$_HMTrigger
+ _OBJC_CLASS_$_HMZone
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_retain_x19
+ _objc_retain_x22
+ _objc_retain_x26
+ _objc_retain_x28
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getAtKeyPath
+ _swift_getErrorValue
+ _swift_getExistentialTypeMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- _HMAccessoryCategoryTypeOther
- __swift_FORCE_LOAD_$_swiftFileProvider
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
- _swift_projectBox
CStrings:
+ " offset "
+ "%s-%s"
+ "%s-%s Found failed device IDs - adding to display %s"
+ "%s-%s No device IDs found"
+ "%s-%s Using currentStateSnapshot"
+ "%s-%s Using source state snapshot"
+ "ActivateSceneIntent completed executing %{private}s(%{public}s) with results: %{public}s"
+ "Adding device %s to failed list due to device error: %@"
+ "Adding device %s to failed list due to error: %@"
+ "Adding device %s to failed list due to homekit error code: %ld"
+ "Adding device %s to success list"
+ "All Devices are Read Only - Showing Answer Sheet"
+ "Attempting to set intentDeepLinkManager.deviceResultTitle as %s"
+ "AttributeResult { kind: "
+ "Automation Result"
+ "AutomationOutcome.failure"
+ "AutomationOutcome.success"
+ "Created toggle dictionary %s"
+ "DataModel.executeAndWait(attributes:staticEndpoints:in:timeout:) - Exiting execution task group because task %s threw error %@"
+ "DataModel.executeAndWait(attributes:staticEndpoints:in:timeout:) - Exiting execution task group because value waiter ended with error %@"
+ "DeltaAttributeValueIntent returning ShowDeviceResultIntent for %s"
+ "DeviceClassNumber"
+ "DeviceResult { device: "
+ "Error preparing device results for Accessory Controls Animation: %@"
+ "Failed to create trigger with error: %@"
+ "Failed to execution actionSet because we are missing a homeManager (THIS SHOULD NEVER HAPPEN"
+ "Failed to find cleanMode for %{public}s in rvc clusters on %llu"
+ "Failed to find home with ID %s"
+ "Found Accessory in Device's additionalIDs - Name: %s ID: %s"
+ "Found Attribute Kinds from Read Results: %s"
+ "Found Home Name in user specificity: %s"
+ "Found Service Group in Device's additionalIDs - Name: %s ID: %s"
+ "Found additionalIds in Device Entities from ShowDeviceResultIntent: %s Original Device ID: %s"
+ "Found either only currentTemperature or only currentHumidity for attribute kinds - Showing Answer Sheet"
+ "Found more than one tile: %ld belonging to the Notice, but the userSpecificity requires displaying deviceName, showing the first tile's name"
+ "Found sceneEntities: %s for name: %s"
+ "Found secondaryAccessoryControlDestination: %s"
+ "GetAttributeValueIntent completed with results: %{public}s"
+ "GetAttributeValueIntent returning ShowDeviceResultIntent for %s"
+ "GetAttributeValueIntent: %s resulted in %s"
+ "GetDeviceInfoIntent finished with results %s"
+ "Got request to set attributes for endpoint %{public}s outside of home %{public}s. Ignoring"
+ "HAIMultipleRooms"
+ "HAIRoomOrZoneDeviceTitle"
+ "HAIZoneAndRoomDeviceTitle"
+ "Has Siri Execution Failure"
+ "Home entity provided %s (%s), filtering sharedAsync"
+ "HomeAppIntents/ShowDeviceResultIntent.swift"
+ "HomeAppIntents/ShowNavigationIntent.swift"
+ "HomeEntityQuery"
+ "Matter device %llu exited with errors %s"
+ "No destination found from ShowDeviceResultIntent - navigating by Deep Link"
+ "No home entity provided, not filtering sharedAsync"
+ "No matter snapshot for %s for snapshot search"
+ "No snapshot found for current home"
+ "Object With Name Already Exists"
+ "Outcome.deviceFailure"
+ "PossibleValuesForAttribute.rvcCurrentRun"
+ "Query: Found deviceEntities: %s"
+ "Query: Found homeEntities: %s for identifiers: %s"
+ "Query: Found homeEntities: %s for string: %s"
+ "Query: Performing device query {%s} for %s with homeEntity: %s"
+ "Query: Searching for homes with identifiers: %s"
+ "Query: Searching for homes with string: %s"
+ "Received error %@ when executing commands"
+ "Received user specificity for group, but unable to find a static service group with any of the given IDs: %s"
+ "Robot Vacuum Dust Bin Is Full"
+ "Robot Vacuum Failed To Find Charging Dock"
+ "Robot Vacuum Is Missing Dust Bin"
+ "Robot Vacuum Is Missing Water Tank"
+ "Robot Vacuum Mopping Pad Is Missing"
+ "Robot Vacuum Stuck"
+ "Robot Vacuum Water Tank Is Empty"
+ "Robot Vacuum Water Tank Lid Is Open"
+ "RoomEntityResolver"
+ "Searching for scenes with name: %s"
+ "SetAttributeValueIntent completed with results: %{public}s"
+ "SetAttributeValueIntent returning ShowDeviceResultIntent for %s"
+ "SetAttributeValueIntent: %s resulted in %s"
+ "SetAttributeValueIntent: %s will be set attributes %s"
+ "SetAttributeValueIntent: will be set attributes %{public}s on devices %{public}s"
+ "Setting SecondaryAccessoryControlDestinationin in ShowDeviceResultIntent: %s"
+ "Show Device Result Intent perform() called - successDeviceIDs: %s failedDeviceIDs: %s failedDeviceIDsToIgnore: %s userSpecificity: %s secondaryAccessoryControlDestination: %s"
+ "ShowNavigationIntent = %s"
+ "Skipping execution of commands due to validation errors: %s"
+ "Successfully executed the commands and the expected values were reached"
+ "ToggleAttributeIntent completed with results: %{public}s"
+ "ToggleAttributeIntent: %s resulted in %s"
+ "ToggleAttributeValueIntent returning ShowDeviceResultIntent for %s"
+ "Unable To Complete Opearation"
+ "Unable To Start Or Resume"
+ "Unable to create DeviceEntity for %s because can't find room with id %s"
+ "Unable to create DeviceEntity for %s because can't find the accessory for nodeID %llu"
+ "Unable to create DeviceEntity for %s because couldn't find a staticAccessory for nodeID %llu"
+ "Unable to create DeviceEntity for %s because primaryDeviceType couldn't be determined "
+ "Unable to create DeviceEntity for %s with accessoryID: %s serviceKind: %s primaryServiceKind: %s"
+ "Unable to create DeviceEntity for media profile %s"
+ "Unable to find serviceKind for devices: %s"
+ "Unexpected error thrown during attribute apply execution: %@"
+ "Unexpectedly found clean mode (id: %lu, label: %s) without mop or vacuum tags: %s"
+ "Using matter snapshot for %s for snapshot search"
+ "Using snapshots for homes %s for snapshot search"
+ "accessories"
+ "accessoryControlDeepLinkURL"
+ "answerDeepLinkURL"
+ "app intent execution"
+ "attributeKind inputDescription "
+ "commandTask"
+ "deviceEntitiesFromUUIDs"
+ "deviceName"
+ "deviceResult"
+ "deviceType"
+ "expectedValueWaiterTask"
+ "failed, no home manager"
+ "group"
+ "id name "
+ "legacy"
+ "majorityDeviceType"
+ "name"
+ "navigation"
+ "navigationDestination"
+ "objectWithNameAlreadyExists"
+ "rooms"
+ "rvcDustBinFull"
+ "rvcDustBinMissing"
+ "rvcFailedToFindChargingDock"
+ "rvcMopCleaningPadMissing"
+ "rvcStuck"
+ "rvcWaterTankEmpty"
+ "rvcWaterTankLidOpen"
+ "rvcWaterTankMissing"
+ "sceneResult"
+ "searchDeepLinkURL"
+ "showIntentDestinationFromRead - Found %ld deviceIDs: %s"
+ "sortedHomes"
+ "triggers"
+ "unableToCompleteOpearation"
+ "unableToStartOrResume"
+ "uniqueIdentifier"
+ "zones"
- "App Intent Created!"
- "Can't construct Array with count < 0"
- "Cannot found home with id: %s"
- "Created toggle dicctionary %s"
- "Device Already In State"
- "Device Encountered Error"
- "Division by zero"
- "Division results in an overflow"
- "Found deviceEntities: %s"
- "Found deviceEntities: %s for deviceTypes: %s"
- "Found deviceEntities: %s for identifiers: %s"
- "Found deviceEntities: %s for ids: %s"
- "Found deviceEntities: %s for names: %s"
- "Found deviceEntities: %s for string: %s"
- "Found homeEntities: %s for identifiers: %s"
- "Found homeEntities: %s for string: %s"
- "Found sceneEntities: %s for names: %s"
- "GetAttributeValueIntent returning ShowIntent for %s"
- "GetAttributeValueIntent unable to find attributeKind for results: %s"
- "HAIAirParticulateDensity_AttributeCapitalized"
- "HAIAirParticulateSize_AttributeCapitalized"
- "HAIAirQuality_AttributeCapitalized"
- "HAIBatteryLevel_AttributeCapitalized"
- "HAIBrightness_AttributeCapitalized"
- "HAICarbonDioxideDetected_AttributeCapitalized"
- "HAICarbonDioxideLevel_AttributeCapitalized"
- "HAICarbonDioxidePeakLevel_AttributeCapitalized"
- "HAICarbonMonoxideDetected_AttributeCapitalized"
- "HAICarbonMonoxideLevel_AttributeCapitalized"
- "HAICarbonMonoxidePeakLevel_AttributeCapitalized"
- "HAIChargingState_AttributeCapitalized"
- "HAIChildLockEnabled_AttributeCapitalized"
- "HAIColor_AttributeCapitalized"
- "HAIContactDetected_AttributeCapitalized"
- "HAICurrentAirPurifierState_AttributeCapitalized"
- "HAICurrentDoorState_AttributeCapitalized"
- "HAICurrentHorizontalTilt_AttributeCapitalized"
- "HAICurrentHumidifierDehumidifierMode_AttributeCapitalized"
- "HAICurrentHumidity_AttributeCapitalized"
- "HAICurrentLockState_AttributeCapitalized"
- "HAICurrentPosition_AttributeCapitalized"
- "HAICurrentSecuritySystemState_AttributeCapitalized"
- "HAICurrentTemperature_AttributeCapitalized"
- "HAICurrentThermostatMode_AttributeCapitalized"
- "HAICurrentVerticalTilt_AttributeCapitalized"
- "HAIDuration_AttributeCapitalized"
- "HAIFilterChangeNeeded_AttributeCapitalized"
- "HAIFilterLifeLevel_AttributeCapitalized"
- "HAIInUse_AttributeCapitalized"
- "HAILeakDetected_AttributeCapitalized"
- "HAILightLevel_AttributeCapitalized"
- "HAILowBattery_AttributeCapitalized"
- "HAIMotionDetected_AttributeCapitalized"
- "HAINaturalLight_AttributeCapitalized"
- "HAINitrogenDioxideDensity_AttributeCapitalized"
- "HAINone_AttributeCapitalized"
- "HAIObstructionDetected_AttributeCapitalized"
- "HAIOccupancyDetected_AttributeCapitalized"
- "HAIOzoneDensity_AttributeCapitalized"
- "HAIPm10Density_AttributeCapitalized"
- "HAIPm2_5Density_AttributeCapitalized"
- "HAIPositionState_AttributeCapitalized"
- "HAIPower_AttributeCapitalized"
- "HAIRotationDirection_AttributeCapitalized"
- "HAIRotationSpeed_AttributeCapitalized"
- "HAIRvc_AttributeCapitalized"
- "HAISmokeDetected_AttributeCapitalized"
- "HAISulphurDioxideDensity_AttributeCapitalized"
- "HAISwingModeEnabled_AttributeCapitalized"
- "HAITargetAirPurifierState_AttributeCapitalized"
- "HAITargetDoorState_AttributeCapitalized"
- "HAITargetHorizontalTilt_AttributeCapitalized"
- "HAITargetHumidifierDehumidifierConfiguration_AttributeCapitalized"
- "HAITargetHumidity_AttributeCapitalized"
- "HAITargetLockState_AttributeCapitalized"
- "HAITargetPosition_AttributeCapitalized"
- "HAITargetSecuritySystemState_AttributeCapitalized"
- "HAITargetThermostatConfiguration_AttributeCapitalized"
- "HAITargetVerticalTilt_AttributeCapitalized"
- "HAIVolatileOrganicCompoundDensity_AttributeCapitalized"
- "HAIWaterLevel_AttributeCapitalized"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "No matter snapshot id: %s for %s for snapshot search"
- "No snapshot found for home %s"
- "Not enough bits to represent the passed value"
- "Scene Activation State"
- "Searching for devices with comparators: %s"
- "Searching for devices with deviceTypes: %s"
- "Searching for devices with identifiers: %s"
- "Searching for devices with ids: %s"
- "Searching for devices with names: %s"
- "Searching for devices with string: %s"
- "Searching for homes with identifiers: %s"
- "Searching for homes with string: %s"
- "Searching for scenes with names: %s"
- "SetAttributeValueIntent returning ShowIntent for %s"
- "Show Device Result Intent perform() called - successDeviceIDs: %s failedDeviceIDs: %s failedDeviceIDsToIgnore: %s userSpecificity: %s"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unable to create DeviceEntity for %s with accessoryID: %s serviceKind: %s primaryServiceKind: %s)"
- "Unable to create DeviceEntity for %s)"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "Using matter snapshot id: %s for %s for snapshot search"
- "Using snapshot for %s for snapshot search"
- "deviceAlreadyInState"
- "deviceEncounteredError"
- "deviceEntityResolver"
- "failed"
- "homeEntity was nil"
- "invalid Collection: less than 'count' elements in collection"
- "matterControllerID"
- "robot Vacuum Cleaner"
- "success"

```
