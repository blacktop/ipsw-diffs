## MicroLocation

> `/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation`

```diff

-35.0.1.0.0
-  __TEXT.__text: 0x1272c
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x1b84
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x2278
-  __TEXT.__gcc_except_tab: 0x130
-  __TEXT.__oslogstring: 0x8df
-  __TEXT.__unwind_info: 0x5c8
-  __TEXT.__objc_classname: 0x25f
-  __TEXT.__objc_methname: 0x37d9
-  __TEXT.__objc_methtype: 0x865
-  __TEXT.__objc_stubs: 0x24e0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x620
-  __DATA_CONST.__objc_classlist: 0xd8
+59.0.1.0.9
+  __TEXT.__text: 0x191ec
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x218c
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x27fa
+  __TEXT.__gcc_except_tab: 0x140
+  __TEXT.__oslogstring: 0xb46
+  __TEXT.__unwind_info: 0x830
+  __TEXT.__objc_classname: 0x2e1
+  __TEXT.__objc_methname: 0x4660
+  __TEXT.__objc_methtype: 0xa2b
+  __TEXT.__objc_stubs: 0x2d00
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x710
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb0
+  __DATA_CONST.__objc_selrefs: 0xe38
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x2260
-  __AUTH_CONST.__objc_const: 0x2ab8
+  __DATA_CONST.__objc_superrefs: 0xd8
+  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__objc_const: 0x32c0
   __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x180
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__data: 0x240
-  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 415F658E-C73B-3769-BB00-497E820070B1
-  Functions: 561
-  Symbols:   2072
-  CStrings:  1361
+  UUID: C2A0A222-49E9-368E-9C10-AA4DE565A3CA
+  Functions: 694
+  Symbols:   2507
+  CStrings:  1654
 
Symbols:
+ +[ULAccessibilitySessionFetchOptions supportsSecureCoding]
+ +[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]
+ +[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:].cold.1
+ +[ULConnection(Diagnostic) exportVisualLoggerDataWithReply:]
+ +[ULConnection(Diagnostic) exportVisualLoggerDataWithReply:].cold.1
+ +[ULConnection(Diagnostic) peripheralDebugTask:reply:]
+ +[ULConnection(Diagnostic) peripheralDebugTask:reply:].cold.1
+ +[ULConnection(Diagnostic) terminateDaemonWithReply:]
+ +[ULConnection(Diagnostic) terminateDaemonWithReply:].cold.1
+ +[ULCoordinate invalid]
+ +[ULCoordinate supportsSecureCoding]
+ +[ULDevicePredictionContext emptyPredictionContext]
+ +[ULDevicePredictionContext supportsSecureCoding]
+ +[ULLabelHomeKitUserInteraction supportsSecureCoding]
+ -[DeviceClassObject deviceClass]
+ -[DeviceClassObject initWithDeviceClass:]
+ -[ULAccessibilitySessionFetchOptions .cxx_destruct]
+ -[ULAccessibilitySessionFetchOptions copyWithZone:]
+ -[ULAccessibilitySessionFetchOptions description]
+ -[ULAccessibilitySessionFetchOptions encodeWithCoder:]
+ -[ULAccessibilitySessionFetchOptions hash]
+ -[ULAccessibilitySessionFetchOptions initWithCoder:]
+ -[ULAccessibilitySessionFetchOptions initWithUseCaseStartTime:]
+ -[ULAccessibilitySessionFetchOptions isEqual:]
+ -[ULAccessibilitySessionFetchOptions useCaseStartTime]
+ -[ULConnection didUpdateDevicePredictionContext:]
+ -[ULConnection(Diagnostic) requestMapReconstruction]
+ -[ULConnection(Diagnostic) visualLoggerAddDestinationWithHost:]
+ -[ULConnection(HomeKit) updateHomeKitUserInteractionLabel:]
+ -[ULCoordinate copyWithZone:]
+ -[ULCoordinate description]
+ -[ULCoordinate deviceClassFrame]
+ -[ULCoordinate encodeWithCoder:]
+ -[ULCoordinate hasDirectionalContext]
+ -[ULCoordinate hash]
+ -[ULCoordinate initWithCoder:]
+ -[ULCoordinate initWithTranslation:yaw:submapIndex:isTracked:deviceClassFrame:]
+ -[ULCoordinate isEqual:]
+ -[ULCoordinate isTracked]
+ -[ULCoordinate isValid]
+ -[ULCoordinate setDeviceClassFrame:]
+ -[ULCoordinate setIsTracked:]
+ -[ULCoordinate setSubmapIndex:]
+ -[ULCoordinate setTranslation:]
+ -[ULCoordinate setYaw:]
+ -[ULCoordinate submapIndex]
+ -[ULCoordinate translation]
+ -[ULCoordinate yaw]
+ -[ULDevicePredictionContext .cxx_destruct]
+ -[ULDevicePredictionContext coordinateForFrame:andSubmapIndex:]
+ -[ULDevicePredictionContext coordinates]
+ -[ULDevicePredictionContext copyWithZone:]
+ -[ULDevicePredictionContext description]
+ -[ULDevicePredictionContext deviceClass]
+ -[ULDevicePredictionContext encodeWithCoder:]
+ -[ULDevicePredictionContext hasDirectionalContext]
+ -[ULDevicePredictionContext hasSpatialContext]
+ -[ULDevicePredictionContext hash]
+ -[ULDevicePredictionContext imageIdentifiersVector]
+ -[ULDevicePredictionContext initWithCoder:]
+ -[ULDevicePredictionContext initWithUniqueIdentifier:timestamp:isMotionDetected:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:particles:]
+ -[ULDevicePredictionContext isEqual:]
+ -[ULDevicePredictionContext isMotionDetected]
+ -[ULDevicePredictionContext isPredictionValid]
+ -[ULDevicePredictionContext particles]
+ -[ULDevicePredictionContext probabilityVector]
+ -[ULDevicePredictionContext setCoordinates:]
+ -[ULDevicePredictionContext setDeviceClass:]
+ -[ULDevicePredictionContext setImageIdentifiersVector:]
+ -[ULDevicePredictionContext setIsMotionDetected:]
+ -[ULDevicePredictionContext setIsPredictionValid:]
+ -[ULDevicePredictionContext setParticles:]
+ -[ULDevicePredictionContext setProbabilityVector:]
+ -[ULDevicePredictionContext setTimestamp:]
+ -[ULDevicePredictionContext setUniqueIdentifier:]
+ -[ULDevicePredictionContext timestamp]
+ -[ULDevicePredictionContext trackedCoordinateForFrame:]
+ -[ULDevicePredictionContext uniqueIdentifier]
+ -[ULHomeSlamModelData initWithMapROIs:trajectoryPoints:numInputSegments:numInputStaticIntervals:numMappedStaticIntervals:numFinalSegments:numFilteredSubmaps:numROIs:numWalkwayPoints:]
+ -[ULHomeSlamModelData initWithMapROIs:trajectoryPoints:numInputSegments:numberOfInputStaticIntervals:numberOfMappedStaticIntervals:numberOfMappedSegments:numberOfFilteredSubmaps:numROIs:numWalkwayPoints:]
+ -[ULHomeSlamModelData numberOfFilteredSubmaps]
+ -[ULHomeSlamModelData numberOfFinalSegments]
+ -[ULHomeSlamModelData numberOfInputStaticIntervals]
+ -[ULHomeSlamModelData numberOfMappedStaticIntervals]
+ -[ULHomeSlamModelData numberOfROIs]
+ -[ULHomeSlamModelData numberOfWalkwayPoints]
+ -[ULHomeSlamModelData setNumberOfFilteredSubmaps:]
+ -[ULHomeSlamModelData setNumberOfFinalSegments:]
+ -[ULHomeSlamModelData setNumberOfInputStaticIntervals:]
+ -[ULHomeSlamModelData setNumberOfMappedStaticIntervals:]
+ -[ULHomeSlamModelData setNumberOfROIs:]
+ -[ULHomeSlamModelData setNumberOfWalkwayPoints:]
+ -[ULLabel coordinate]
+ -[ULLabel initWithName:timestamp:contextLayer:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:]
+ -[ULLabel initWithName:timestamp:contextLayerType:deviceClass:]
+ -[ULLabel setCoordinate:]
+ -[ULLabel yaw]
+ -[ULLabel(Testing) setCoordinateForTesting:]
+ -[ULLabelHomeKitUserInteraction .cxx_destruct]
+ -[ULLabelHomeKitUserInteraction copyUpdatingInteractionType:]
+ -[ULLabelHomeKitUserInteraction copyWithZone:]
+ -[ULLabelHomeKitUserInteraction description]
+ -[ULLabelHomeKitUserInteraction encodeWithCoder:]
+ -[ULLabelHomeKitUserInteraction entityType]
+ -[ULLabelHomeKitUserInteraction hash]
+ -[ULLabelHomeKitUserInteraction initWithCoder:]
+ -[ULLabelHomeKitUserInteraction initWithName:deviceClass:andEntityType:]
+ -[ULLabelHomeKitUserInteraction initWithName:entityType:timestamp:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:interactionType:]
+ -[ULLabelHomeKitUserInteraction initWithName:entityType:timestamp:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:interactionType:labelIdentifier:]
+ -[ULLabelHomeKitUserInteraction initWithName:timestamp:deviceClass:entityType:]
+ -[ULLabelHomeKitUserInteraction initWithName:timestamp:deviceClass:entityType:interactionType:]
+ -[ULLabelHomeKitUserInteraction initWithName:timestamp:deviceClass:entityType:interactionType:labelIdentifier:]
+ -[ULLabelHomeKitUserInteraction interactionType]
+ -[ULLabelHomeKitUserInteraction isEqual:]
+ -[ULLabelHomeKitUserInteraction labelIdentifier]
+ -[ULLabelHomeKitUserInteraction setEntityType:]
+ -[ULLabelHomeKitUserInteraction setInteractionType:]
+ -[ULLabelHomeKitUserInteraction setLabelIdentifier:]
+ -[ULLabelWiFi initWithName:rssi:timestamp:coordinate:probabilityVector:imageIdentifiersVector:]
+ -[ULLabelWiFi initWithName:timestamp:rssi:]
+ -[ULMap _geo_isSameSpaceForLabel:horizontalThreshold:deviceClass:]
+ -[ULMap _geo_isSameYawLabel:yawThreshold:]
+ -[ULMap copyUpdatingDevicePredictionContext:]
+ -[ULMap labelsInSameSpaceAndYawForMapItem:]
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:]
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:]
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:].cold.1
+ -[ULPredictionContext airPodsPrediction]
+ -[ULPredictionContext copyUpdatingDevicePredictionContext:]
+ -[ULPredictionContext devicePredictionContextForDeviceClass:]
+ -[ULPredictionContext devicePredictions]
+ -[ULPredictionContext hasDirectionalContext]
+ -[ULPredictionContext hasSpatialContext]
+ -[ULPredictionContext initWithDevicePredictions:]
+ -[ULPredictionContext mainDevicePrediction]
+ -[ULPredictionContext newestDevicePrediction]
+ -[ULPredictionContext setDevicePredictions:]
+ -[ULPredictionContext trackedCoordinateInSelfFrameForDeviceClass:]
+ -[ULPredictionContext updateDevicePredictionContext:]
+ -[ULServiceMetaInfo initWithNumClustersLearnedInModel:numRecordingTriggersAtCurrentLOI:numInputValidFingerprints:numInputValidFingerprintsLabeled:numInputValidFingerprintsUnlabeled:numFingerprintsBeforePruning:numFingerprintsAfterPruning:numWiFiAccessPoints:numBLESources:numUWBSources:peripheralAvailable:modelCategory:]
+ -[ULServiceMetaInfo modelCategory]
+ -[ULServiceMetaInfo peripheralAvailable]
+ -[ULServiceMetaInfo setModelCategory:]
+ -[ULServiceMetaInfo setPeripheralAvailable:]
+ GCC_except_table101
+ GCC_except_table126
+ _OBJC_CLASS_$_DeviceClassObject
+ _OBJC_CLASS_$_ULAccessibilitySessionFetchOptions
+ _OBJC_CLASS_$_ULCoordinate
+ _OBJC_CLASS_$_ULDevicePredictionContext
+ _OBJC_CLASS_$_ULLabelHomeKitUserInteraction
+ _OBJC_IVAR_$_DeviceClassObject._deviceClass
+ _OBJC_IVAR_$_ULAccessibilitySessionFetchOptions._useCaseStartTime
+ _OBJC_IVAR_$_ULCoordinate._deviceClassFrame
+ _OBJC_IVAR_$_ULCoordinate._isTracked
+ _OBJC_IVAR_$_ULCoordinate._submapIndex
+ _OBJC_IVAR_$_ULCoordinate._translation
+ _OBJC_IVAR_$_ULCoordinate._yaw
+ _OBJC_IVAR_$_ULDevicePredictionContext._coordinates
+ _OBJC_IVAR_$_ULDevicePredictionContext._deviceClass
+ _OBJC_IVAR_$_ULDevicePredictionContext._imageIdentifiersVector
+ _OBJC_IVAR_$_ULDevicePredictionContext._isMotionDetected
+ _OBJC_IVAR_$_ULDevicePredictionContext._isPredictionValid
+ _OBJC_IVAR_$_ULDevicePredictionContext._particles
+ _OBJC_IVAR_$_ULDevicePredictionContext._probabilityVector
+ _OBJC_IVAR_$_ULDevicePredictionContext._timestamp
+ _OBJC_IVAR_$_ULDevicePredictionContext._uniqueIdentifier
+ _OBJC_IVAR_$_ULHomeSlamModelData._numberOfFilteredSubmaps
+ _OBJC_IVAR_$_ULHomeSlamModelData._numberOfFinalSegments
+ _OBJC_IVAR_$_ULHomeSlamModelData._numberOfInputStaticIntervals
+ _OBJC_IVAR_$_ULHomeSlamModelData._numberOfMappedStaticIntervals
+ _OBJC_IVAR_$_ULHomeSlamModelData._numberOfROIs
+ _OBJC_IVAR_$_ULHomeSlamModelData._numberOfWalkwayPoints
+ _OBJC_IVAR_$_ULLabel._coordinate
+ _OBJC_IVAR_$_ULLabelHomeKitUserInteraction._entityType
+ _OBJC_IVAR_$_ULLabelHomeKitUserInteraction._interactionType
+ _OBJC_IVAR_$_ULLabelHomeKitUserInteraction._labelIdentifier
+ _OBJC_IVAR_$_ULPredictionContext._devicePredictions
+ _OBJC_IVAR_$_ULServiceMetaInfo._modelCategory
+ _OBJC_IVAR_$_ULServiceMetaInfo._peripheralAvailable
+ _OBJC_METACLASS_$_DeviceClassObject
+ _OBJC_METACLASS_$_ULAccessibilitySessionFetchOptions
+ _OBJC_METACLASS_$_ULCoordinate
+ _OBJC_METACLASS_$_ULDevicePredictionContext
+ _OBJC_METACLASS_$_ULLabelHomeKitUserInteraction
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _ULContextLayerRoomClassNameBathroom
+ _ULContextLayerRoomClassNameBedroom
+ _ULContextLayerRoomClassNameChildRoom
+ _ULContextLayerRoomClassNameCorridorHallway
+ _ULContextLayerRoomClassNameDiningRoom
+ _ULContextLayerRoomClassNameGameRoom
+ _ULContextLayerRoomClassNameHomeGarage
+ _ULContextLayerRoomClassNameHomeOffice
+ _ULContextLayerRoomClassNameIndoors
+ _ULContextLayerRoomClassNameKitchen
+ _ULContextLayerRoomClassNameLaundry
+ _ULContextLayerRoomClassNameLivingRoom
+ _ULContextLayerRoomClassNameOffice
+ _ULContextLayerRoomClassNameStaircase
+ _ULContextLayerRoomClassNameUnknown
+ _ULContextLayerTypeCoLocation
+ _ULContextLayerTypeHomeKitUserInteraction
+ _ULContextLayerTypePilApp
+ _ULPeripheralDebugTaskToString
+ _ULSubmapIndexNotAvailable
+ _ULYawNotAvailable
+ __OBJC_$_CLASS_METHODS_ULAccessibilitySessionFetchOptions
+ __OBJC_$_CLASS_METHODS_ULConnection(Diagnostic|Legacy|HomeKit)
+ __OBJC_$_CLASS_METHODS_ULCoordinate
+ __OBJC_$_CLASS_METHODS_ULDevicePredictionContext
+ __OBJC_$_CLASS_METHODS_ULLabelHomeKitUserInteraction
+ __OBJC_$_CLASS_PROP_LIST_ULAccessibilitySessionFetchOptions
+ __OBJC_$_CLASS_PROP_LIST_ULCoordinate
+ __OBJC_$_CLASS_PROP_LIST_ULDevicePredictionContext
+ __OBJC_$_INSTANCE_METHODS_DeviceClassObject
+ __OBJC_$_INSTANCE_METHODS_ULAccessibilitySessionFetchOptions
+ __OBJC_$_INSTANCE_METHODS_ULConnection(Diagnostic|Legacy|HomeKit)
+ __OBJC_$_INSTANCE_METHODS_ULCoordinate
+ __OBJC_$_INSTANCE_METHODS_ULDevicePredictionContext
+ __OBJC_$_INSTANCE_METHODS_ULLabelHomeKitUserInteraction
+ __OBJC_$_INSTANCE_METHODS_ULPredictionContext
+ __OBJC_$_INSTANCE_VARIABLES_DeviceClassObject
+ __OBJC_$_INSTANCE_VARIABLES_ULAccessibilitySessionFetchOptions
+ __OBJC_$_INSTANCE_VARIABLES_ULCoordinate
+ __OBJC_$_INSTANCE_VARIABLES_ULDevicePredictionContext
+ __OBJC_$_INSTANCE_VARIABLES_ULLabelHomeKitUserInteraction
+ __OBJC_$_PROP_LIST_DeviceClassObject
+ __OBJC_$_PROP_LIST_ULAccessibilitySessionFetchOptions
+ __OBJC_$_PROP_LIST_ULCoordinate
+ __OBJC_$_PROP_LIST_ULDevicePredictionContext
+ __OBJC_$_PROP_LIST_ULLabelHomeKitUserInteraction
+ __OBJC_CLASS_PROTOCOLS_$_ULAccessibilitySessionFetchOptions
+ __OBJC_CLASS_PROTOCOLS_$_ULCoordinate
+ __OBJC_CLASS_PROTOCOLS_$_ULDevicePredictionContext
+ __OBJC_CLASS_RO_$_DeviceClassObject
+ __OBJC_CLASS_RO_$_ULAccessibilitySessionFetchOptions
+ __OBJC_CLASS_RO_$_ULCoordinate
+ __OBJC_CLASS_RO_$_ULDevicePredictionContext
+ __OBJC_CLASS_RO_$_ULLabelHomeKitUserInteraction
+ __OBJC_METACLASS_RO_$_DeviceClassObject
+ __OBJC_METACLASS_RO_$_ULAccessibilitySessionFetchOptions
+ __OBJC_METACLASS_RO_$_ULCoordinate
+ __OBJC_METACLASS_RO_$_ULDevicePredictionContext
+ __OBJC_METACLASS_RO_$_ULLabelHomeKitUserInteraction
+ ___39-[ULPredictionContext isMotionDetected]_block_invoke
+ ___40-[ULPredictionContext isPredictionValid]_block_invoke
+ ___49-[ULConnection didUpdateDevicePredictionContext:]_block_invoke
+ ___52-[ULConnection(Diagnostic) requestMapReconstruction]_block_invoke
+ ___52-[ULConnection(Diagnostic) requestMapReconstruction]_block_invoke.cold.1
+ ___53+[ULConnection(Diagnostic) terminateDaemonWithReply:]_block_invoke
+ ___53+[ULConnection(Diagnostic) terminateDaemonWithReply:]_block_invoke_2
+ ___53+[ULConnection(Diagnostic) terminateDaemonWithReply:]_block_invoke_2.cold.1
+ ___54+[ULConnection(Diagnostic) peripheralDebugTask:reply:]_block_invoke
+ ___54+[ULConnection(Diagnostic) peripheralDebugTask:reply:]_block_invoke_2
+ ___54+[ULConnection(Diagnostic) peripheralDebugTask:reply:]_block_invoke_2.cold.1
+ ___55-[ULDevicePredictionContext trackedCoordinateForFrame:]_block_invoke
+ ___59-[ULConnection(HomeKit) updateHomeKitUserInteractionLabel:]_block_invoke
+ ___59-[ULConnection(HomeKit) updateHomeKitUserInteractionLabel:]_block_invoke.cold.1
+ ___59-[ULConnection(HomeKit) updateHomeKitUserInteractionLabel:]_block_invoke.cold.2
+ ___60+[ULConnection(Diagnostic) exportVisualLoggerDataWithReply:]_block_invoke
+ ___60+[ULConnection(Diagnostic) exportVisualLoggerDataWithReply:]_block_invoke_2
+ ___60+[ULConnection(Diagnostic) exportVisualLoggerDataWithReply:]_block_invoke_2.cold.1
+ ___61+[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]_block_invoke
+ ___61+[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]_block_invoke_2
+ ___61+[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]_block_invoke_2.cold.1
+ ___63-[ULConnection(Diagnostic) visualLoggerAddDestinationWithHost:]_block_invoke
+ ___63-[ULConnection(Diagnostic) visualLoggerAddDestinationWithHost:]_block_invoke.cold.1
+ ___NSDictionary0__struct
+ ___block_descriptor_32_e22_B16?0"ULCoordinate"8l
+ ___block_descriptor_32_e35_B16?0"ULDevicePredictionContext"8l
+ ___block_literal_global.164
+ ___block_literal_global.3
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_msgSend$_geo_isSameSpaceForLabel:horizontalThreshold:deviceClass:
+ _objc_msgSend$_geo_isSameYawLabel:yawThreshold:
+ _objc_msgSend$allValues
+ _objc_msgSend$compare:
+ _objc_msgSend$coordinate
+ _objc_msgSend$coordinateForFrame:andSubmapIndex:
+ _objc_msgSend$copyUpdatingDevicePredictionContext:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$deleteDatabaseDirectoryWithReply:
+ _objc_msgSend$deviceClassFrame
+ _objc_msgSend$devicePredictionContextForDeviceClass:
+ _objc_msgSend$devicePredictions
+ _objc_msgSend$entityType
+ _objc_msgSend$exportVisualLoggerDataWithReply:
+ _objc_msgSend$hasDirectionalContext
+ _objc_msgSend$hasSpatialContext
+ _objc_msgSend$initWithDeviceClass:
+ _objc_msgSend$initWithDevicePredictions:
+ _objc_msgSend$initWithMapROIs:trajectoryPoints:numInputSegments:numInputStaticIntervals:numMappedStaticIntervals:numFinalSegments:numFilteredSubmaps:numROIs:numWalkwayPoints:
+ _objc_msgSend$initWithName:entityType:timestamp:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:interactionType:labelIdentifier:
+ _objc_msgSend$initWithName:rssi:timestamp:coordinate:probabilityVector:imageIdentifiersVector:
+ _objc_msgSend$initWithName:timestamp:contextLayer:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:
+ _objc_msgSend$initWithName:timestamp:deviceClass:entityType:interactionType:
+ _objc_msgSend$initWithName:timestamp:deviceClass:entityType:interactionType:labelIdentifier:
+ _objc_msgSend$initWithNumClustersLearnedInModel:numRecordingTriggersAtCurrentLOI:numInputValidFingerprints:numInputValidFingerprintsLabeled:numInputValidFingerprintsUnlabeled:numFingerprintsBeforePruning:numFingerprintsAfterPruning:numWiFiAccessPoints:numBLESources:numUWBSources:peripheralAvailable:modelCategory:
+ _objc_msgSend$initWithTranslation:yaw:submapIndex:isTracked:deviceClassFrame:
+ _objc_msgSend$initWithUniqueIdentifier:timestamp:isMotionDetected:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:particles:
+ _objc_msgSend$initWithUseCaseStartTime:
+ _objc_msgSend$interactionType
+ _objc_msgSend$invalid
+ _objc_msgSend$isTracked
+ _objc_msgSend$isValid
+ _objc_msgSend$labelIdentifier
+ _objc_msgSend$labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:
+ _objc_msgSend$modelCategory
+ _objc_msgSend$newestDevicePrediction
+ _objc_msgSend$numberOfFilteredSubmaps
+ _objc_msgSend$numberOfFinalSegments
+ _objc_msgSend$numberOfInputStaticIntervals
+ _objc_msgSend$numberOfMappedStaticIntervals
+ _objc_msgSend$numberOfROIs
+ _objc_msgSend$numberOfWalkwayPoints
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$peripheralAvailable
+ _objc_msgSend$peripheralDebugTask:reply:
+ _objc_msgSend$requestMapReconstructionWithRequestIdentifier:
+ _objc_msgSend$setCoordinate:
+ _objc_msgSend$setDeviceClassFrame:
+ _objc_msgSend$setDevicePredictions:
+ _objc_msgSend$setEntityType:
+ _objc_msgSend$setInteractionType:
+ _objc_msgSend$setIsTracked:
+ _objc_msgSend$setLabelIdentifier:
+ _objc_msgSend$setModelCategory:
+ _objc_msgSend$setNumberOfFilteredSubmaps:
+ _objc_msgSend$setNumberOfFinalSegments:
+ _objc_msgSend$setNumberOfInputStaticIntervals:
+ _objc_msgSend$setNumberOfMappedStaticIntervals:
+ _objc_msgSend$setNumberOfROIs:
+ _objc_msgSend$setNumberOfWalkwayPoints:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPeripheralAvailable:
+ _objc_msgSend$setSubmapIndex:
+ _objc_msgSend$setTranslation:
+ _objc_msgSend$setYaw:
+ _objc_msgSend$submapIndex
+ _objc_msgSend$terminateDaemonWithReply:
+ _objc_msgSend$trackedCoordinateForFrame:
+ _objc_msgSend$translation
+ _objc_msgSend$ul_firstWhere:
+ _objc_msgSend$updateHomeKitUserInteractionLabel:
+ _objc_msgSend$useCaseStartTime
+ _objc_msgSend$visualLoggerAddDestinationWithHost:
+ _objc_msgSend$yaw
+ _objc_retainAutoreleasedReturnValue
- +[ULConnection(Diagnostic) polarisDebugWithTask:reply:]
- +[ULConnection(Diagnostic) polarisDebugWithTask:reply:].cold.1
- -[ULConfiguration deviceClass]
- -[ULConfiguration setDeviceClass:]
- -[ULConnection didUpdatePredictionContext:]
- -[ULHomeSlamModelData initWithMapROIs:trajectoryPoints:numInputSegments:]
- -[ULLabel initWithName:timestamp:contextLayer:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:]
- -[ULLabel setCoordinates:]
- -[ULLabel(Testing) setCoordinatesForTesting:]
- -[ULLabelWiFi initWithName:rssi:timestamp:coordinates:probabilityVector:imageIdentifiersVector:]
- -[ULMap _geo_isSameSpaceForLabel:]
- -[ULPredictionContext coordinates]
- -[ULPredictionContext imageIdentifiersVector]
- -[ULPredictionContext initWithUniqueIdentifier:timestamp:isMotionDetected:coordinates:probabilityVector:imageIdentifiersVector:particles:]
- -[ULPredictionContext particles]
- -[ULPredictionContext probabilityVector]
- -[ULPredictionContext setCoordinates:]
- -[ULPredictionContext setImageIdentifiersVector:]
- -[ULPredictionContext setIsMotionDetected:]
- -[ULPredictionContext setParticles:]
- -[ULPredictionContext setProbabilityVector:]
- -[ULPredictionContext setTimestamp:]
- -[ULPredictionContext setUniqueIdentifier:]
- -[ULPredictionContext(Testing) setCoordinatesForTesting:]
- -[ULServiceMetaInfo initWithNumClustersLearnedInModel:numRecordingTriggersAtCurrentLOI:numInputValidFingerprints:numInputValidFingerprintsLabeled:numInputValidFingerprintsUnlabeled:numFingerprintsBeforePruning:numFingerprintsAfterPruning:numWiFiAccessPoints:numBLESources:numUWBSources:]
- GCC_except_table113
- _OBJC_IVAR_$_ULConfiguration._deviceClass
- _OBJC_IVAR_$_ULLabel._coordinates
- _OBJC_IVAR_$_ULPredictionContext._coordinates
- _OBJC_IVAR_$_ULPredictionContext._imageIdentifiersVector
- _OBJC_IVAR_$_ULPredictionContext._isMotionDetected
- _OBJC_IVAR_$_ULPredictionContext._particles
- _OBJC_IVAR_$_ULPredictionContext._probabilityVector
- _OBJC_IVAR_$_ULPredictionContext._timestamp
- _OBJC_IVAR_$_ULPredictionContext._uniqueIdentifier
- _ULContextLayerTypeDataCollectionApp
- _ULContextLayerTypeHomeSlamApp
- _ULContextLayerTypeLslApp
- _ULPolarisManagerTaskToString
- __OBJC_$_CLASS_METHODS_ULConnection(Diagnostic|Legacy)
- __OBJC_$_INSTANCE_METHODS_ULConnection(Diagnostic|Legacy)
- __OBJC_$_INSTANCE_METHODS_ULPredictionContext(Testing)
- ___43-[ULConnection didUpdatePredictionContext:]_block_invoke
- ___55+[ULConnection(Diagnostic) polarisDebugWithTask:reply:]_block_invoke
- ___55+[ULConnection(Diagnostic) polarisDebugWithTask:reply:]_block_invoke_2
- ___55+[ULConnection(Diagnostic) polarisDebugWithTask:reply:]_block_invoke_2.cold.1
- ___block_literal_global.161
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_geo_isSameSpaceForLabel:
- _objc_msgSend$_image_isSameSpaceForLabel:
- _objc_msgSend$initWithMapROIs:trajectoryPoints:numInputSegments:
- _objc_msgSend$initWithName:rssi:timestamp:coordinates:probabilityVector:imageIdentifiersVector:
- _objc_msgSend$initWithName:timestamp:contextLayer:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:
- _objc_msgSend$initWithNumClustersLearnedInModel:numRecordingTriggersAtCurrentLOI:numInputValidFingerprints:numInputValidFingerprintsLabeled:numInputValidFingerprintsUnlabeled:numFingerprintsBeforePruning:numFingerprintsAfterPruning:numWiFiAccessPoints:numBLESources:numUWBSources:
- _objc_msgSend$initWithUniqueIdentifier:timestamp:isMotionDetected:coordinates:probabilityVector:imageIdentifiersVector:particles:
- _objc_msgSend$intersectsSet:
- _objc_msgSend$polarisDebugWithTask:reply:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x7
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "\t"
+ "    %@: %@: %@\n"
+ "    deviceClassFrame: %@\n"
+ "    hasDirectionalContext: %@\n"
+ "    isTracked: %@\n"
+ "    isValid: %@\n"
+ "    submapIndex: %lld\n"
+ "    translation: (%.3f, %.3f, %.3f)\n"
+ "    yaw: %.3f\n"
+ "  %@\n"
+ "  contextLayer: %@\n"
+ "  coordinate: nil\n"
+ "  coordinates: %@\n"
+ "  deviceClass: %@\n"
+ "  devicePredictions: {\n"
+ "  isMotionDetected: %@\n"
+ "  isPredictionValid: %@\n"
+ "  labels: %@\n"
+ "  mapItemType: %@\n"
+ "  name: %@\n"
+ "  probabilityVector: %@\n"
+ "  timestamp: %@\n"
+ "  uniqueIdentifier: %@\n"
+ "  }\n"
+ " %@\n"
+ "%@, entityType: %@, interactionType: %@, labelIdentifier: %@"
+ "%@:\n"
+ ", mapItems:\n"
+ ", modelCategory: %ld"
+ ", numberOfFilteredSubmaps: %@"
+ ", numberOfFinalSegments: %@"
+ ", numberOfInputStaticIntervals: %@"
+ ", numberOfMappedStaticIntervals: %@"
+ ", numberOfROIs: %@"
+ ", numberOfWalkwayPoints: %@"
+ ", objectName: %@"
+ ", peripheralAvailable: %@"
+ "/Library/Caches/com.apple.xbs/2BCE50C0-F177-4BC4-93BB-65DDC52114B7/TemporaryDirectory.hAlzBA/Sources/MicroLocation/MicroLocationFramework/src/ULConnection.m"
+ "00000000-0000-0000-0000-000000000026"
+ "00000000-0000-0000-0000-000000000027"
+ "@\"NSDictionary\""
+ "@\"NSMutableDictionary\""
+ "@\"ULCoordinate\""
+ "@108@0:8@16@24@32@40@48@56@64@72@80@88B96q100"
+ "@24@0:8q16"
+ "@32@0:8@16Q24"
+ "@32@0:8Q16q24"
+ "@40@0:8@16@24q32"
+ "@40@0:8@16Q24q32"
+ "@44@0:8@16@24f32d36"
+ "@48@0:8@16@24@32Q40"
+ "@48@0:8@16@24Q32q40"
+ "@56@0:816f32q36B44Q48"
+ "@56@0:8@16@24Q32q40q48"
+ "@64@0:8@16@24Q32q40q48@56"
+ "@64@0:8@16q24@32@40@48@56"
+ "@72@0:8@16@24@32Q40@48@56@64"
+ "@76@0:8@16@24B32Q36@44@52@60@68"
+ "@80@0:8@16q24@32Q40@48@56@64q72"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "@88@0:8@16q24@32Q40@48@56@64q72@80"
+ "Awaiting Odometry setup"
+ "B16@?0@\"ULCoordinate\"8"
+ "B16@?0@\"ULDevicePredictionContext\"8"
+ "B32@0:8@16d24"
+ "B40@0:8@16d24@32"
+ "Delete database directory response, error:%@"
+ "DeviceClassObject"
+ "Export visual logger response, URLS:%@, error:%@"
+ "Exporting Visual Logger Data"
+ "HomeKit"
+ "Peripheral not enabled"
+ "Requesting database directory deletion"
+ "Requesting milod to terminate"
+ "T,N,V_translation"
+ "T@\"NSDate\",R,N"
+ "T@\"NSDate\",R,N,V_useCaseStartTime"
+ "T@\"NSDictionary\",&,N,V_coordinates"
+ "T@\"NSMutableDictionary\",&,N,V_devicePredictions"
+ "T@\"NSNumber\",&,N,V_numberOfFilteredSubmaps"
+ "T@\"NSNumber\",&,N,V_numberOfFinalSegments"
+ "T@\"NSNumber\",&,N,V_numberOfInputStaticIntervals"
+ "T@\"NSNumber\",&,N,V_numberOfMappedStaticIntervals"
+ "T@\"NSNumber\",&,N,V_numberOfROIs"
+ "T@\"NSNumber\",&,N,V_numberOfWalkwayPoints"
+ "T@\"NSUUID\",&,N,V_labelIdentifier"
+ "T@\"NSUUID\",R,N"
+ "T@\"ULCoordinate\",&,N,V_coordinate"
+ "TB,N,V_isPredictionValid"
+ "TB,N,V_isTracked"
+ "TB,N,V_peripheralAvailable"
+ "TQ,N,V_deviceClassFrame"
+ "TQ,R,N,V_deviceClass"
+ "Terminate daemon response, error:%@"
+ "Tf,N,V_yaw"
+ "Tq,N,V_entityType"
+ "Tq,N,V_interactionType"
+ "Tq,N,V_modelCategory"
+ "Tq,N,V_submapIndex"
+ "ULAccessibilitySessionFetchOptions"
+ "ULContextLayerTypeCoLocation"
+ "ULContextLayerTypeHomeKitUserInteraction"
+ "ULContextLayerTypePilApp"
+ "ULCoordinate"
+ "ULDevicePredictionContext"
+ "ULLabelHomeKitUserInteraction"
+ "YES"
+ "_coordinate"
+ "_deviceClassFrame"
+ "_devicePredictions"
+ "_entityType"
+ "_geo_isSameSpaceForLabel:horizontalThreshold:deviceClass:"
+ "_geo_isSameYawLabel:yawThreshold:"
+ "_interactionType"
+ "_isPredictionValid"
+ "_isTracked"
+ "_labelIdentifier"
+ "_modelCategory"
+ "_numberOfFilteredSubmaps"
+ "_numberOfFinalSegments"
+ "_numberOfInputStaticIntervals"
+ "_numberOfMappedStaticIntervals"
+ "_numberOfROIs"
+ "_numberOfWalkwayPoints"
+ "_peripheralAvailable"
+ "_submapIndex"
+ "_translation"
+ "_useCaseStartTime"
+ "_yaw"
+ "airPodsPrediction"
+ "allValues"
+ "bathroom"
+ "bedroom"
+ "capture-image"
+ "childRoom"
+ "com.apple.HomeKit"
+ "com.apple.MicroLocation.deleteDatabaseDirectory"
+ "com.apple.MicroLocation.exportVisualLoggerWithReply"
+ "com.apple.MicroLocation.peripheralDebugTask"
+ "com.apple.MicroLocation.terminateMilod"
+ "com.apple.PIL"
+ "com.apple.perception"
+ "com.apple.perception.PCF"
+ "compare:"
+ "coordinate"
+ "coordinateForFrame:andSubmapIndex:"
+ "copyUpdatingDevicePredictionContext:"
+ "copyUpdatingInteractionType:"
+ "corridorHallway"
+ "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
+ "deleteDatabaseDirectoryWithReply:"
+ "deviceClassFrame"
+ "devicePredictionContextForDeviceClass:"
+ "devicePredictions"
+ "didUpdateDevicePredictionContext:"
+ "diningRoom"
+ "entityType"
+ "exportVisualLoggerDataWithReply:"
+ "gameRoom"
+ "hasDirectionalContext"
+ "hasSpatialContext"
+ "homeGarage"
+ "homeOffice"
+ "indoors"
+ "initWithDeviceClass:"
+ "initWithDevicePredictions:"
+ "initWithMapROIs:trajectoryPoints:numInputSegments:numInputStaticIntervals:numMappedStaticIntervals:numFinalSegments:numFilteredSubmaps:numROIs:numWalkwayPoints:"
+ "initWithMapROIs:trajectoryPoints:numInputSegments:numberOfInputStaticIntervals:numberOfMappedStaticIntervals:numberOfMappedSegments:numberOfFilteredSubmaps:numROIs:numWalkwayPoints:"
+ "initWithName:deviceClass:andEntityType:"
+ "initWithName:entityType:timestamp:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:interactionType:"
+ "initWithName:entityType:timestamp:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:interactionType:labelIdentifier:"
+ "initWithName:rssi:timestamp:coordinate:probabilityVector:imageIdentifiersVector:"
+ "initWithName:timestamp:contextLayer:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:"
+ "initWithName:timestamp:contextLayerType:deviceClass:"
+ "initWithName:timestamp:deviceClass:entityType:"
+ "initWithName:timestamp:deviceClass:entityType:interactionType:"
+ "initWithName:timestamp:deviceClass:entityType:interactionType:labelIdentifier:"
+ "initWithName:timestamp:rssi:"
+ "initWithNumClustersLearnedInModel:numRecordingTriggersAtCurrentLOI:numInputValidFingerprints:numInputValidFingerprintsLabeled:numInputValidFingerprintsUnlabeled:numFingerprintsBeforePruning:numFingerprintsAfterPruning:numWiFiAccessPoints:numBLESources:numUWBSources:peripheralAvailable:modelCategory:"
+ "initWithTranslation:yaw:submapIndex:isTracked:deviceClassFrame:"
+ "initWithUniqueIdentifier:timestamp:isMotionDetected:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:particles:"
+ "initWithUseCaseStartTime:"
+ "interactionType"
+ "invalid"
+ "isTracked"
+ "isValid"
+ "kitchen"
+ "labelIdentifier"
+ "labelsInSameSpaceAndYawForMapItem:"
+ "labelsInSameSpaceForMapItem:forDeviceClass:"
+ "labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:"
+ "laundry"
+ "livingRoom"
+ "mainDevicePrediction"
+ "modelCategory"
+ "newestDevicePrediction"
+ "numberOfFilteredSubmaps"
+ "numberOfFinalSegments"
+ "numberOfInputStaticIntervals"
+ "numberOfMappedStaticIntervals"
+ "numberOfROIs"
+ "numberOfWalkwayPoints"
+ "numberWithLongLong:"
+ "office"
+ "peripheralAvailable"
+ "peripheralDebugTask. task: %@"
+ "peripheralDebugTask:reply:"
+ "proximity-updates"
+ "requestMapReconstruction"
+ "requestMapReconstructionWithRequestIdentifier:"
+ "setCoordinate:"
+ "setCoordinateForTesting:"
+ "setDeviceClassFrame:"
+ "setDevicePredictions:"
+ "setEntityType:"
+ "setInteractionType:"
+ "setIsPredictionValid:"
+ "setIsTracked:"
+ "setLabelIdentifier:"
+ "setModelCategory:"
+ "setNumberOfFilteredSubmaps:"
+ "setNumberOfFinalSegments:"
+ "setNumberOfInputStaticIntervals:"
+ "setNumberOfMappedStaticIntervals:"
+ "setNumberOfROIs:"
+ "setNumberOfWalkwayPoints:"
+ "setObject:forKeyedSubscript:"
+ "setPeripheralAvailable:"
+ "setSubmapIndex:"
+ "setTranslation:"
+ "setYaw:"
+ "simulate-peripheral-available"
+ "simulate-peripheral-unavailable"
+ "staircase"
+ "start-resource-consumption"
+ "stop-resource-consumption"
+ "submapIndex"
+ "terminateDaemonWithReply:"
+ "trackedCoordinateForFrame:"
+ "trackedCoordinateInSelfFrameForDeviceClass:"
+ "translation"
+ "ul_firstWhere:"
+ "updateDevicePredictionContext:"
+ "updateHomeKitUserInteractionLabel:"
+ "updateLabel with name: %@ to contextLayer: %@ to device: %@, labelIdentifier: %@"
+ "updateLabel: ULLabelHomeKitUserInteraction must have non-nil labelIdentifier"
+ "useCaseStartTime"
+ "v24@0:8@\"ULDevicePredictionContext\"16"
+ "v24@0:8@\"ULLabelHomeKitUserInteraction\"16"
+ "visualLoggerAddDestinationWithHost:"
+ "visualLoggerAddDestinationWithHost: %@"
+ "yaw"
+ "{\"msg%{public}.0s\":\"Same Space For Map Item\", \"MapItem name\":%{public, location:escape_only}s, \"Same space anchors\":%{public}lu, \"Total anchors\":%{public}lu}"
- "\n"
- ", contextLayer: %@"
- ", coordinates: (%@, %@, %@)"
- ", deviceClass: %@"
- ", imageIdentifiersVector: %@"
- ", isMotionDetected: %@"
- ", isPredictionValid: %@"
- ", labels: %@"
- ", mapItemType: %@"
- ", mapItems: %@"
- ", name: %@"
- ", particles: %@"
- ", probabilityVector: %@"
- ", timestamp: %@"
- ", uniqueIdentifier: %@"
- "/Library/Caches/com.apple.xbs/Sources/MicroLocation/MicroLocationFramework/src/ULConnection.m"
- "00000000-0000-0000-0000-000000000018"
- "00000000-0000-0000-0000-000000000020"
- "@72@0:8@16q24@3240@56@64"
- "@76@0:8@16@24B3236@52@60@68"
- "@80@0:8@16@24@32Q4048@64@72"
- "@96@0:8@16@24@32@40@48@56@64@72@80@88"
- "T,N,V_coordinates"
- "ULContextLayerTypeDataCollectionApp"
- "ULContextLayerTypeHomeSlamApp"
- "ULContextLayerTypeLslApp"
- "_geo_isSameSpaceForLabel:"
- "com.apple.HomeSlam"
- "com.apple.MiLoDataCollection"
- "com.apple.MiLoLSL2"
- "com.apple.MicroLocation.polarisDebug"
- "didUpdatePredictionContext:"
- "initWithMapROIs:trajectoryPoints:numInputSegments:"
- "initWithName:rssi:timestamp:coordinates:probabilityVector:imageIdentifiersVector:"
- "initWithName:timestamp:contextLayer:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:"
- "initWithNumClustersLearnedInModel:numRecordingTriggersAtCurrentLOI:numInputValidFingerprints:numInputValidFingerprintsLabeled:numInputValidFingerprintsUnlabeled:numFingerprintsBeforePruning:numFingerprintsAfterPruning:numWiFiAccessPoints:numBLESources:numUWBSources:"
- "initWithUniqueIdentifier:timestamp:isMotionDetected:coordinates:probabilityVector:imageIdentifiersVector:particles:"
- "intersectsSet:"
- "polarisDebug. task: %@"
- "polarisDebugWithTask:reply:"
- "setCoordinatesForTesting:"
- "setup-graphs"
- "teardown-graphs"
- "v24@0:8@\"ULPredictionContext\"16"

```
