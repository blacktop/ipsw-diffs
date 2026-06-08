## MicroLocation

> `/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation`

```diff

-62.0.3.0.0
-  __TEXT.__text: 0x191ec
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x218c
+106.0.2.0.0
+  __TEXT.__text: 0x1bf7c
+  __TEXT.__objc_methlist: 0x2764
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x27fa
-  __TEXT.__gcc_except_tab: 0x140
-  __TEXT.__oslogstring: 0xb46
-  __TEXT.__unwind_info: 0x830
-  __TEXT.__objc_classname: 0x2e1
-  __TEXT.__objc_methname: 0x4660
-  __TEXT.__objc_methtype: 0xa2b
-  __TEXT.__objc_stubs: 0x2d00
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0x710
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__cstring: 0x2c41
+  __TEXT.__gcc_except_tab: 0x108
+  __TEXT.__oslogstring: 0xe82
+  __TEXT.__unwind_info: 0x798
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x748
+  __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe38
+  __DATA_CONST.__objc_selrefs: 0x1070
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x2a60
-  __AUTH_CONST.__objc_const: 0x32c0
-  __AUTH_CONST.__objc_intobj: 0x270
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1d0
-  __DATA.__data: 0x240
-  __DATA_DIRTY.__objc_data: 0x820
+  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__got: 0x1d8
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x2ec0
+  __AUTH_CONST.__objc_const: 0x3bc0
+  __AUTH_CONST.__objc_intobj: 0x360
+  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x22c
+  __DATA.__data: 0x250
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0xbe0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1659AE7D-2613-362A-992E-6350E9677AF2
-  Functions: 694
-  Symbols:   2507
-  CStrings:  1654
+  UUID: B733D575-3BEB-37C2-98BD-C0A1A06CA64A
+  Functions: 821
+  Symbols:   2945
+  CStrings:  904
 
Symbols:
+ +[AnchorCounter stats]
+ +[OccupancyMapProcessingUtilities fromSessionSpaceToPixel:deviceClassFrameToBlinkerTransform:pointInSessionSpace:]
+ +[OccupancyMapProcessingUtilities hasLineOfSight:deviceClassFrameToBlinkerTransform:labelCoordinate:predictionCoordinate:]
+ +[OccupancyMapProcessingUtilities hasLineOfSightFromPixel:pointB:walkabilityGrid:walkabilityGridWidth:walkabilityGridHeight:]
+ +[OccupancyMapProcessingUtilities makeMatrix3x3:]
+ +[OccupancyMapProcessingUtilities makeMatrix4x4:]
+ +[OccupancyMapProcessingUtilities zInRoomBoundarySpace:deviceClassFrameToBlinkerTransform:pointInSessionSpace:]
+ +[ULConnection(Diagnostic) clearAllLabelsForContextLayer:reply:]
+ +[ULConnection(Diagnostic) clearAllLabelsForContextLayer:reply:].cold.1
+ +[ULConnection(Diagnostic) removeAllModelsOfType:reply:]
+ +[ULConnection(Diagnostic) removeAllModelsOfType:reply:].cold.1
+ +[ULMapPeripheralData emptyMapPeripheralData]
+ +[ULMapPeripheralData new]
+ +[ULMapPeripheralData supportsSecureCoding]
+ +[ULOccupancyData emptyOccupancyData]
+ +[ULOccupancyData new]
+ +[ULOccupancyData supportsSecureCoding]
+ +[ULOccupancyMapPoint new]
+ +[ULOccupancyMapPoint supportsSecureCoding]
+ +[ULRoomBoundaryPolygon new]
+ +[ULRoomBoundaryPolygon supportsSecureCoding]
+ -[AnchorCounter incrementSameSpace]
+ -[AnchorCounter incrementTotal]
+ -[AnchorCounter init]
+ -[AnchorCounter numAnchorsInSameSpace]
+ -[AnchorCounter numAnchors]
+ -[AnchorCounter setNumAnchors:]
+ -[AnchorCounter setNumAnchorsInSameSpace:]
+ -[NSCoder(ULExtensions) ul_decodeQuaternionForKey:]
+ -[NSCoder(ULExtensions) ul_encodeQuaternion:forKey:]
+ -[ULConnection didUpdateMap:].cold.1
+ -[ULConnection didUpdateOccupancyGrid:]
+ -[ULConnection didUpdateOccupancyGrid:].cold.1
+ -[ULConnection didUpdatePredictionContextState:]
+ -[ULConnection previousNotifiedCoordinatesByDevice]
+ -[ULConnection setPreviousNotifiedCoordinatesByDevice:]
+ -[ULConnection(Diagnostic) configureVisualLoggerStreamWithIdentifier:networkHost:networkPort:]
+ -[ULCoordinate initWithTranslation:rotation:submapIndex:isTracked:deviceClassFrame:isHighConfidence:]
+ -[ULCoordinate isHighConfidence]
+ -[ULCoordinate rotation]
+ -[ULCoordinate setIsHighConfidence:]
+ -[ULCoordinate setRotation:]
+ -[ULMap _geo_isLineOfSightForLabel:occupancyData:deviceClassFrameToBlinkerTransform:predictionCoordinate:]
+ -[ULMap _getAirpodsCoordinates:]
+ -[ULMap _trackHomeKitLabelStatistics:isSameSpace:counters:]
+ -[ULMap copyUpdatingIsPredictionContextStale:]
+ -[ULMap copyUpdatingOccupancyDataEntries:]
+ -[ULMap didPredictionContextSignificantlyChange:previousCoordinate:]
+ -[ULMap didPredictionContextSignificantlyChange:previousCoordinate:].cold.1
+ -[ULMap didPredictionContextSignificantlyChange:previousCoordinate:].cold.2
+ -[ULMap didPredictionContextSignificantlyChange:previousCoordinate:].cold.3
+ -[ULMap didPredictionContextSignificantlyChange:previousCoordinate:].cold.4
+ -[ULMap didPredictionContextSignificantlyChange:previousCoordinate:].cold.5
+ -[ULMap initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:peripheralData:homeSlamModelData:isPredictionContextStale:occupancyDataEntries:occupancyTransforms:]
+ -[ULMap isPredictionContextStale]
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:requireLineOfSight:]
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:requireLineOfSight:].cold.1
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:requireLineOfSight:].cold.2
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:requireLineOfSight:].cold.3
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:requireLineOfSight:].cold.4
+ -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:requireLineOfSight:].cold.5
+ -[ULMap occupancyDataEntries]
+ -[ULMap occupancyTransforms]
+ -[ULMap peripheralData]
+ -[ULMap setIsPredictionContextStale:]
+ -[ULMap setOccupancyDataEntries:]
+ -[ULMap setOccupancyTransforms:]
+ -[ULMap setPeripheralData:]
+ -[ULMapItem initWithName:labels:]
+ -[ULMapPeripheralData copyWithZone:]
+ -[ULMapPeripheralData description]
+ -[ULMapPeripheralData encodeWithCoder:]
+ -[ULMapPeripheralData hash]
+ -[ULMapPeripheralData initWithCoder:]
+ -[ULMapPeripheralData initWithPeripheralAvailable:proximityLevel:]
+ -[ULMapPeripheralData init]
+ -[ULMapPeripheralData isEqual:]
+ -[ULMapPeripheralData peripheralAvailable]
+ -[ULMapPeripheralData proximityLevel]
+ -[ULMapPeripheralData setPeripheralAvailable:]
+ -[ULMapPeripheralData setProximityLevel:]
+ -[ULOccupancyData .cxx_destruct]
+ -[ULOccupancyData blinkerToRoomBoundaryTransform]
+ -[ULOccupancyData ceilingHeight]
+ -[ULOccupancyData copyWithZone:]
+ -[ULOccupancyData description]
+ -[ULOccupancyData encodeWithCoder:]
+ -[ULOccupancyData floorHeight]
+ -[ULOccupancyData gridData]
+ -[ULOccupancyData gridHeight]
+ -[ULOccupancyData gridWidth]
+ -[ULOccupancyData hash]
+ -[ULOccupancyData index]
+ -[ULOccupancyData initWithCoder:]
+ -[ULOccupancyData initWithIndex:gridWidth:gridHeight:gridData:roomBoundaryToGridTransform:blinkerToRoomBoundaryTransform:ceilingHeight:floorHeight:]
+ -[ULOccupancyData init]
+ -[ULOccupancyData isEqual:]
+ -[ULOccupancyData roomBoundaryToGridTransform]
+ -[ULOccupancyData setBlinkerToRoomBoundaryTransform:]
+ -[ULOccupancyData setCeilingHeight:]
+ -[ULOccupancyData setFloorHeight:]
+ -[ULOccupancyData setGridData:]
+ -[ULOccupancyData setGridHeight:]
+ -[ULOccupancyData setGridWidth:]
+ -[ULOccupancyData setIndex:]
+ -[ULOccupancyData setRoomBoundaryToGridTransform:]
+ -[ULOccupancyMapPoint copyWithZone:]
+ -[ULOccupancyMapPoint description]
+ -[ULOccupancyMapPoint encodeWithCoder:]
+ -[ULOccupancyMapPoint hash]
+ -[ULOccupancyMapPoint initWithCoder:]
+ -[ULOccupancyMapPoint initWithX:Y:]
+ -[ULOccupancyMapPoint init]
+ -[ULOccupancyMapPoint isEqual:]
+ -[ULOccupancyMapPoint setX:]
+ -[ULOccupancyMapPoint setY:]
+ -[ULOccupancyMapPoint x]
+ -[ULOccupancyMapPoint y]
+ -[ULRoomBoundaryPolygon .cxx_destruct]
+ -[ULRoomBoundaryPolygon ceilingHeight]
+ -[ULRoomBoundaryPolygon copyWithZone:]
+ -[ULRoomBoundaryPolygon description]
+ -[ULRoomBoundaryPolygon edgeTypes]
+ -[ULRoomBoundaryPolygon encodeWithCoder:]
+ -[ULRoomBoundaryPolygon floorHeight]
+ -[ULRoomBoundaryPolygon hash]
+ -[ULRoomBoundaryPolygon initWithCoder:]
+ -[ULRoomBoundaryPolygon initWithPoints:edgeTypes:floorHeight:ceilingHeight:]
+ -[ULRoomBoundaryPolygon init]
+ -[ULRoomBoundaryPolygon isEqual:]
+ -[ULRoomBoundaryPolygon points]
+ -[ULRoomBoundaryPolygon setCeilingHeight:]
+ -[ULRoomBoundaryPolygon setEdgeTypes:]
+ -[ULRoomBoundaryPolygon setFloorHeight:]
+ -[ULRoomBoundaryPolygon setPoints:]
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table138
+ GCC_except_table63
+ _OBJC_CLASS_$_AnchorCounter
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _OBJC_CLASS_$_OccupancyMapProcessingUtilities
+ _OBJC_CLASS_$_ULMapPeripheralData
+ _OBJC_CLASS_$_ULOccupancyData
+ _OBJC_CLASS_$_ULOccupancyMapPoint
+ _OBJC_CLASS_$_ULRoomBoundaryPolygon
+ _OBJC_IVAR_$_AnchorCounter._numAnchors
+ _OBJC_IVAR_$_AnchorCounter._numAnchorsInSameSpace
+ _OBJC_IVAR_$_ULConnection._previousNotifiedCoordinatesByDevice
+ _OBJC_IVAR_$_ULCoordinate._isHighConfidence
+ _OBJC_IVAR_$_ULCoordinate._rotation
+ _OBJC_IVAR_$_ULMap._isPredictionContextStale
+ _OBJC_IVAR_$_ULMap._occupancyDataEntries
+ _OBJC_IVAR_$_ULMap._occupancyTransforms
+ _OBJC_IVAR_$_ULMap._peripheralData
+ _OBJC_IVAR_$_ULMapPeripheralData._peripheralAvailable
+ _OBJC_IVAR_$_ULMapPeripheralData._proximityLevel
+ _OBJC_IVAR_$_ULOccupancyData._blinkerToRoomBoundaryTransform
+ _OBJC_IVAR_$_ULOccupancyData._ceilingHeight
+ _OBJC_IVAR_$_ULOccupancyData._floorHeight
+ _OBJC_IVAR_$_ULOccupancyData._gridData
+ _OBJC_IVAR_$_ULOccupancyData._gridHeight
+ _OBJC_IVAR_$_ULOccupancyData._gridWidth
+ _OBJC_IVAR_$_ULOccupancyData._index
+ _OBJC_IVAR_$_ULOccupancyData._roomBoundaryToGridTransform
+ _OBJC_IVAR_$_ULOccupancyMapPoint._x
+ _OBJC_IVAR_$_ULOccupancyMapPoint._y
+ _OBJC_IVAR_$_ULRoomBoundaryPolygon._ceilingHeight
+ _OBJC_IVAR_$_ULRoomBoundaryPolygon._edgeTypes
+ _OBJC_IVAR_$_ULRoomBoundaryPolygon._floorHeight
+ _OBJC_IVAR_$_ULRoomBoundaryPolygon._points
+ _OBJC_METACLASS_$_AnchorCounter
+ _OBJC_METACLASS_$_OccupancyMapProcessingUtilities
+ _OBJC_METACLASS_$_ULMapPeripheralData
+ _OBJC_METACLASS_$_ULOccupancyData
+ _OBJC_METACLASS_$_ULOccupancyMapPoint
+ _OBJC_METACLASS_$_ULRoomBoundaryPolygon
+ _ULFenceThresholdByDeviceClass.onceToken
+ _ULFenceThresholdByDeviceClass.thresholds
+ _ULLabelHomeKitUserInteractionEntityTypeToString
+ _ULLabelHomeKitUserInteractionTypeToString
+ _ULRotationNotAvailable
+ _ULYawFromQuaternion
+ __OBJC_$_CLASS_METHODS_AnchorCounter
+ __OBJC_$_CLASS_METHODS_OccupancyMapProcessingUtilities
+ __OBJC_$_CLASS_METHODS_ULMapPeripheralData
+ __OBJC_$_CLASS_METHODS_ULOccupancyData
+ __OBJC_$_CLASS_METHODS_ULOccupancyMapPoint
+ __OBJC_$_CLASS_METHODS_ULRoomBoundaryPolygon
+ __OBJC_$_CLASS_PROP_LIST_ULMapPeripheralData
+ __OBJC_$_CLASS_PROP_LIST_ULOccupancyData
+ __OBJC_$_CLASS_PROP_LIST_ULOccupancyMapPoint
+ __OBJC_$_CLASS_PROP_LIST_ULRoomBoundaryPolygon
+ __OBJC_$_INSTANCE_METHODS_AnchorCounter
+ __OBJC_$_INSTANCE_METHODS_ULMapPeripheralData
+ __OBJC_$_INSTANCE_METHODS_ULOccupancyData
+ __OBJC_$_INSTANCE_METHODS_ULOccupancyMapPoint
+ __OBJC_$_INSTANCE_METHODS_ULRoomBoundaryPolygon
+ __OBJC_$_INSTANCE_VARIABLES_AnchorCounter
+ __OBJC_$_INSTANCE_VARIABLES_ULMapPeripheralData
+ __OBJC_$_INSTANCE_VARIABLES_ULOccupancyData
+ __OBJC_$_INSTANCE_VARIABLES_ULOccupancyMapPoint
+ __OBJC_$_INSTANCE_VARIABLES_ULRoomBoundaryPolygon
+ __OBJC_$_PROP_LIST_AnchorCounter
+ __OBJC_$_PROP_LIST_ULMapPeripheralData
+ __OBJC_$_PROP_LIST_ULOccupancyData
+ __OBJC_$_PROP_LIST_ULOccupancyMapPoint
+ __OBJC_$_PROP_LIST_ULRoomBoundaryPolygon
+ __OBJC_CLASS_PROTOCOLS_$_ULMapPeripheralData
+ __OBJC_CLASS_PROTOCOLS_$_ULOccupancyData
+ __OBJC_CLASS_PROTOCOLS_$_ULOccupancyMapPoint
+ __OBJC_CLASS_PROTOCOLS_$_ULRoomBoundaryPolygon
+ __OBJC_CLASS_RO_$_AnchorCounter
+ __OBJC_CLASS_RO_$_OccupancyMapProcessingUtilities
+ __OBJC_CLASS_RO_$_ULMapPeripheralData
+ __OBJC_CLASS_RO_$_ULOccupancyData
+ __OBJC_CLASS_RO_$_ULOccupancyMapPoint
+ __OBJC_CLASS_RO_$_ULRoomBoundaryPolygon
+ __OBJC_METACLASS_RO_$_AnchorCounter
+ __OBJC_METACLASS_RO_$_OccupancyMapProcessingUtilities
+ __OBJC_METACLASS_RO_$_ULMapPeripheralData
+ __OBJC_METACLASS_RO_$_ULOccupancyData
+ __OBJC_METACLASS_RO_$_ULOccupancyMapPoint
+ __OBJC_METACLASS_RO_$_ULRoomBoundaryPolygon
+ ___29-[ULConnection didUpdateMap:]_block_invoke_2
+ ___39-[ULConnection didUpdateOccupancyGrid:]_block_invoke
+ ___48-[ULConnection didUpdatePredictionContextState:]_block_invoke
+ ___56+[ULConnection(Diagnostic) removeAllModelsOfType:reply:]_block_invoke
+ ___56+[ULConnection(Diagnostic) removeAllModelsOfType:reply:]_block_invoke_2
+ ___56+[ULConnection(Diagnostic) removeAllModelsOfType:reply:]_block_invoke_2.cold.1
+ ___64+[ULConnection(Diagnostic) clearAllLabelsForContextLayer:reply:]_block_invoke
+ ___64+[ULConnection(Diagnostic) clearAllLabelsForContextLayer:reply:]_block_invoke_2
+ ___64+[ULConnection(Diagnostic) clearAllLabelsForContextLayer:reply:]_block_invoke_2.cold.1
+ ___94-[ULConnection(Diagnostic) configureVisualLoggerStreamWithIdentifier:networkHost:networkPort:]_block_invoke
+ ___94-[ULConnection(Diagnostic) configureVisualLoggerStreamWithIdentifier:networkHost:networkPort:]_block_invoke.cold.1
+ ___NSArray0__struct
+ ___ULFenceThresholdByDeviceClass_block_invoke
+ ____CLLogObjectForCategory_query_Default_block_invoke
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.170
+ ___block_literal_global.258
+ ___block_literal_global.267
+ _hasLineOfSightFromPixel
+ _logObject_query_Default
+ _matrix_identity_float3x3
+ _matrix_identity_float4x4
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_geo_isLineOfSightForLabel:occupancyData:deviceClassFrameToBlinkerTransform:predictionCoordinate:
+ _objc_msgSend$_getAirpodsCoordinates:
+ _objc_msgSend$_trackHomeKitLabelStatistics:isSameSpace:counters:
+ _objc_msgSend$airPodsPrediction
+ _objc_msgSend$allKeys
+ _objc_msgSend$blinkerToRoomBoundaryTransform
+ _objc_msgSend$bytes
+ _objc_msgSend$ceilingHeight
+ _objc_msgSend$clearAllLabelsForContextLayer:reply:
+ _objc_msgSend$configureVisualLoggerStreamWithIdentifier:networkHost:networkPort:
+ _objc_msgSend$copyUpdatingIsPredictionContextStale:
+ _objc_msgSend$copyUpdatingOccupancyDataEntries:
+ _objc_msgSend$data
+ _objc_msgSend$dictionary
+ _objc_msgSend$didPredictionContextSignificantlyChange:previousCoordinate:
+ _objc_msgSend$edgeTypes
+ _objc_msgSend$emptyMapPeripheralData
+ _objc_msgSend$floorHeight
+ _objc_msgSend$fromSessionSpaceToPixel:deviceClassFrameToBlinkerTransform:pointInSessionSpace:
+ _objc_msgSend$gridData
+ _objc_msgSend$gridHeight
+ _objc_msgSend$gridWidth
+ _objc_msgSend$hasLineOfSight:deviceClassFrameToBlinkerTransform:labelCoordinate:predictionCoordinate:
+ _objc_msgSend$incrementSameSpace
+ _objc_msgSend$incrementTotal
+ _objc_msgSend$index
+ _objc_msgSend$initWithIndex:gridWidth:gridHeight:gridData:roomBoundaryToGridTransform:blinkerToRoomBoundaryTransform:ceilingHeight:floorHeight:
+ _objc_msgSend$initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:peripheralData:homeSlamModelData:isPredictionContextStale:occupancyDataEntries:occupancyTransforms:
+ _objc_msgSend$initWithName:labels:
+ _objc_msgSend$initWithPeripheralAvailable:proximityLevel:
+ _objc_msgSend$initWithPoints:edgeTypes:floorHeight:ceilingHeight:
+ _objc_msgSend$initWithTranslation:rotation:submapIndex:isTracked:deviceClassFrame:isHighConfidence:
+ _objc_msgSend$initWithX:Y:
+ _objc_msgSend$isHighConfidence
+ _objc_msgSend$isPredictionContextStale
+ _objc_msgSend$labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:requireLineOfSight:
+ _objc_msgSend$length
+ _objc_msgSend$makeMatrix3x3:
+ _objc_msgSend$makeMatrix4x4:
+ _objc_msgSend$numAnchors
+ _objc_msgSend$numAnchorsInSameSpace
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$occupancyDataEntries
+ _objc_msgSend$occupancyTransforms
+ _objc_msgSend$peripheralData
+ _objc_msgSend$points
+ _objc_msgSend$previousNotifiedCoordinatesByDevice
+ _objc_msgSend$proximityLevel
+ _objc_msgSend$removeAllModelsOfType:reply:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$roomBoundaryToGridTransform
+ _objc_msgSend$rotation
+ _objc_msgSend$setBlinkerToRoomBoundaryTransform:
+ _objc_msgSend$setCeilingHeight:
+ _objc_msgSend$setEdgeTypes:
+ _objc_msgSend$setFloorHeight:
+ _objc_msgSend$setGridData:
+ _objc_msgSend$setGridHeight:
+ _objc_msgSend$setGridWidth:
+ _objc_msgSend$setIndex:
+ _objc_msgSend$setIsHighConfidence:
+ _objc_msgSend$setIsPredictionContextStale:
+ _objc_msgSend$setOccupancyDataEntries:
+ _objc_msgSend$setOccupancyTransforms:
+ _objc_msgSend$setPeripheralData:
+ _objc_msgSend$setPoints:
+ _objc_msgSend$setPreviousNotifiedCoordinatesByDevice:
+ _objc_msgSend$setProximityLevel:
+ _objc_msgSend$setRoomBoundaryToGridTransform:
+ _objc_msgSend$setRotation:
+ _objc_msgSend$stats
+ _objc_msgSend$string
+ _objc_msgSend$ul_decodeQuaternionForKey:
+ _objc_msgSend$ul_encodeQuaternion:forKey:
+ _objc_msgSend$zInRoomBoundarySpace:deviceClassFrameToBlinkerTransform:pointInSessionSpace:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x7
+ _objc_retain_x8
+ _objc_retain_x9
+ _onceToken_query_Default
+ _os_signpost_id_generate
- +[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]
- +[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:].cold.1
- +[ULMapItem _verifyInput:]
- -[ULCoordinate initWithTranslation:yaw:submapIndex:isTracked:deviceClassFrame:]
- -[ULCoordinate setYaw:]
- -[ULCoordinate yaw]
- -[ULMap initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:homeSlamModelData:]
- -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:]
- -[ULMap labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:].cold.1
- -[ULMapItem initWithName:labels:mapItemType:]
- -[ULMapItem mapItemType]
- -[ULMapItem setMapItemType:]
- GCC_except_table101
- GCC_except_table126
- GCC_except_table58
- GCC_except_table99
- _OBJC_IVAR_$_ULCoordinate._yaw
- _OBJC_IVAR_$_ULMapItem._mapItemType
- _ULMapItemTypeClientGenerated
- _ULMapItemTypeMiLoGenerated
- ___61+[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]_block_invoke
- ___61+[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]_block_invoke_2
- ___61+[ULConnection(Diagnostic) deleteDatabaseDirectoryWithReply:]_block_invoke_2.cold.1
- ___block_literal_global.164
- _objc_msgSend$containsObject:
- _objc_msgSend$deleteDatabaseDirectoryWithReply:
- _objc_msgSend$initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:homeSlamModelData:
- _objc_msgSend$initWithName:labels:mapItemType:
- _objc_msgSend$initWithTranslation:yaw:submapIndex:isTracked:deviceClassFrame:
- _objc_msgSend$labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:
- _objc_msgSend$mapItemType
- _objc_msgSend$setMapItemType:
- _objc_msgSend$setYaw:
- _objc_msgSend$yaw
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "    isHighConfidence: %@\n"
+ "    rotation: (%.3f, %.3f, %.3f, %.3f)\n"
+ "  %@: %ld|%ld"
+ ")"
+ "+[ULMapPeripheralData new]"
+ "+[ULOccupancyData new]"
+ "+[ULOccupancyMapPoint new]"
+ "+[ULRoomBoundaryPolygon new]"
+ ", isPredictionContextStale: %@"
+ ", occupancyDataEntries: %@"
+ ", occupancyTransforms: %@"
+ ", proximityLevel: %ld"
+ "-[ULMapPeripheralData init]"
+ "-[ULOccupancyData init]"
+ "-[ULOccupancyMapPoint init]"
+ "-[ULRoomBoundaryPolygon init]"
+ "00000000-0000-0000-0000-000000000028"
+ "3"
+ "<ULOccupancyData: index=%u, grid=%ux%u, ceiling=%.2f, floor=%.2f>"
+ "<ULOccupancyMapPoint: x=%.2f, y=%.2f>"
+ "<ULRoomBoundaryPolygon: %lu points, floor=%.2f, ceiling=%.2f>"
+ "Clear all labels for context layer type"
+ "LocationAuto"
+ "LocationAutoRejected"
+ "LocationExplicitConfirmationAccepted"
+ "LocationExplicitConfirmationRejected"
+ "LocationRoomUserResolving"
+ "MaintenanceInProgress"
+ "Negative"
+ "Positive"
+ "ReconstructionInProgress"
+ "Remove all models of type: %@"
+ "Room"
+ "SameSpaceForMapItem"
+ "Scene"
+ "Service"
+ "ULConnection didUpdateOccupancyGrid: entries=%lu"
+ "ULConnection: map update received, cleared fence coordinates to bypass fence on next prediction"
+ "ULMap: First update or invalid coordinate, notifying client"
+ "ULMap: RF model update (no spatial context), notifying client"
+ "ULMap: [deviceClass=%lu] Crossed fence, distance=%.2fm (threshold=%.2fm), notifying client"
+ "ULMap: [deviceClass=%lu] Within fence, distance=%.2fm (threshold=%.2fm), suppressing update"
+ "blinkerToRoomBoundaryTransform"
+ "ceilingHeight"
+ "clear all labels for context layer type response, error:%@"
+ "com.apple.FindMyPIL"
+ "com.apple.MicroLocation.clearAllLabelsForContextLayer"
+ "com.apple.MicroLocation.removeAllModelsOfType"
+ "com.apple.perceptiond"
+ "configureVisualLoggerStreamWithIdentifier: %@ host: %@ port: %u"
+ "edgeTypes"
+ "floorHeight"
+ "gridData"
+ "gridHeight"
+ "gridWidth"
+ "index"
+ "isHighConfidence"
+ "isPredictionContextStale"
+ "labels=%lu"
+ "occupancyDataEntries"
+ "occupancyTransforms"
+ "peripheralData"
+ "points"
+ "proximityLevel"
+ "query"
+ "remove all models of type response, error:%@"
+ "roomBoundaryToGridTransform"
+ "rotation"
+ "sameSpace=%lu"
+ "{\"msg%{public}.0s\":\"Line Of Sight Rejections\", \"MapItem name\":%{public, location:escape_only}s, \"Rejected by LOS\":%{public}lu}"
+ "{\"msg%{public}.0s\":\"Same Space For Map Item\", \"MapItem name\":%{public, location:escape_only}s, \"Same space anchors\":%{public}lu, \"Total anchors\":%{public}lu, \"HomeKit Anchors\":%{public, location:escape_only}s}"
- "    yaw: %.3f\n"
- "  mapItemType: %@\n"
- "#16@0:8"
- "("
- ".cxx_destruct"
- "16@0:8"
- "24@0:8@16"
- "@\"<ULConnectionDelegate>\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"ULConfiguration\""
- "@\"ULCoordinate\""
- "@\"ULDarwinNotificationHelper\""
- "@\"ULHomeSlamModelData\""
- "@\"ULLocationOfInterest\""
- "@\"ULLocationType\""
- "@\"ULMap\""
- "@\"ULMapPoint\""
- "@\"ULPredictionContext\""
- "@\"ULServiceDescriptor\""
- "@\"ULServiceMetaInfo\""
- "@\"ULServiceQualityInfo\""
- "@108@0:8@16@24@32@40@48@56@64@72@80@88B96q100"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8f16f20f24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16q24"
- "@32@0:8Q16@24"
- "@32@0:8Q16q24"
- "@36@0:8@16B24@?28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24q32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16Q24q32"
- "@40@0:8@16f24f28f32f36"
- "@44@0:8@16@24f32d36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24@32Q40"
- "@48@0:8@16@24Q32q40"
- "@56@0:816f32q36B44Q48"
- "@56@0:8@16@24Q32q40q48"
- "@64@0:8@16@24@32@40@48@56"
- "@64@0:8@16@24Q32q40q48@56"
- "@64@0:8@16q24@32@40@48@56"
- "@72@0:8@16@24@32Q40@48@56@64"
- "@76@0:8@16@24@32Q40@48B56@60@68"
- "@76@0:8@16@24B32Q36@44@52@60@68"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "@80@0:8@16q24@32Q40@48@56@64q72"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "@88@0:8@16q24@32Q40@48@56@64q72@80"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B32@0:8@16d24"
- "B40@0:8@16d24@32"
- "Delete database directory response, error:%@"
- "DeviceClassObject"
- "Diagnostic"
- "HomeKit"
- "Legacy"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "Q24@0:8@16"
- "Requesting database directory deletion"
- "T#,R"
- "T,N,V_translation"
- "T@\"<ULConnectionDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",&,N,V_imageIdentifiersVector"
- "T@\"NSArray\",&,N,V_labels"
- "T@\"NSArray\",&,N,V_mapItems"
- "T@\"NSArray\",&,N,V_mapPoints"
- "T@\"NSArray\",&,N,V_mapROIs"
- "T@\"NSArray\",&,N,V_particles"
- "T@\"NSArray\",&,N,V_probabilityVector"
- "T@\"NSArray\",&,N,V_serviceQualityReasons"
- "T@\"NSArray\",&,N,V_serviceSuspendReasons"
- "T@\"NSArray\",&,N,V_trajectoryPoints"
- "T@\"NSArray\",R,N,V_confidenceReasons"
- "T@\"NSArray\",R,N,V_locationTypes"
- "T@\"NSArray\",R,N,V_places"
- "T@\"NSArray\",R,N,V_serviceSuspendReasons"
- "T@\"NSDate\",&,N,V_timestamp"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_time"
- "T@\"NSDate\",R,N,V_useCaseStartTime"
- "T@\"NSDictionary\",&,N,V_coordinates"
- "T@\"NSError\",R,N,V_error"
- "T@\"NSMutableDictionary\",&,N,V_devicePredictions"
- "T@\"NSNumber\",&,N,V_numberOfBLESources"
- "T@\"NSNumber\",&,N,V_numberOfClustersLearnedInModel"
- "T@\"NSNumber\",&,N,V_numberOfFilteredSubmaps"
- "T@\"NSNumber\",&,N,V_numberOfFinalSegments"
- "T@\"NSNumber\",&,N,V_numberOfFingerprintsAfterPruning"
- "T@\"NSNumber\",&,N,V_numberOfFingerprintsBeforePruning"
- "T@\"NSNumber\",&,N,V_numberOfInputSegments"
- "T@\"NSNumber\",&,N,V_numberOfInputStaticIntervals"
- "T@\"NSNumber\",&,N,V_numberOfInputValidFingerprints"
- "T@\"NSNumber\",&,N,V_numberOfInputValidFingerprintsLabeled"
- "T@\"NSNumber\",&,N,V_numberOfInputValidFingerprintsUnLabeled"
- "T@\"NSNumber\",&,N,V_numberOfMappedStaticIntervals"
- "T@\"NSNumber\",&,N,V_numberOfROIs"
- "T@\"NSNumber\",&,N,V_numberOfRecordingTriggersAtCurrentLocationOfInterest"
- "T@\"NSNumber\",&,N,V_numberOfUWBSources"
- "T@\"NSNumber\",&,N,V_numberOfWalkwayPoints"
- "T@\"NSNumber\",&,N,V_numberOfWiFiAccessPoints"
- "T@\"NSNumber\",&,N,V_roomIndex"
- "T@\"NSNumber\",R,N,V_score"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_delegateQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSSet\",&,N,V_contextLayers"
- "T@\"NSString\",&,N,V_contextLayer"
- "T@\"NSString\",&,N,V_mapItemType"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSUUID\",&,N,V_labelIdentifier"
- "T@\"NSUUID\",&,N,V_legacyServiceIdentifier"
- "T@\"NSUUID\",&,N,V_locationOfInterestUUID"
- "T@\"NSUUID\",&,N,V_requestIdentifier"
- "T@\"NSUUID\",&,N,V_serviceIdentifier"
- "T@\"NSUUID\",&,N,V_uniqueIdentifier"
- "T@\"NSUUID\",R,N"
- "T@\"NSUUID\",R,N,V_currentLocationOfInterestUuid"
- "T@\"NSUUID\",R,N,V_identifier"
- "T@\"NSUUID\",R,N,V_requestIdentifier"
- "T@\"NSUUID\",R,N,V_serviceIdentifier"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "T@\"ULConfiguration\",C,N,V_configuration"
- "T@\"ULCoordinate\",&,N,V_coordinate"
- "T@\"ULDarwinNotificationHelper\",&,N,V_darwinNotificationHelper"
- "T@\"ULHomeSlamModelData\",&,N,V_homeSlamModelData"
- "T@\"ULLocationOfInterest\",&,N,V_locationOfInterest"
- "T@\"ULLocationType\",R,N,V_currentLocationOfInterestType"
- "T@\"ULMap\",&,N,V_internalMap"
- "T@\"ULMap\",R,C,N"
- "T@\"ULMapPoint\",&,N,V_mapPoint"
- "T@\"ULPredictionContext\",&,N,V_predictionContext"
- "T@\"ULServiceDescriptor\",R,N,V_serviceDescriptor"
- "T@\"ULServiceMetaInfo\",&,N,V_metaInfo"
- "T@\"ULServiceMetaInfo\",R,N,V_metaInfo"
- "T@\"ULServiceQualityInfo\",R,N,V_serviceQualityInfo"
- "TB,N,V_interrupted"
- "TB,N,V_isInRoomDetectionEnabled"
- "TB,N,V_isLowLatency"
- "TB,N,V_isMapValid"
- "TB,N,V_isMotionDetected"
- "TB,N,V_isPredictionValid"
- "TB,N,V_isTracked"
- "TB,N,V_peripheralAvailable"
- "TB,R"
- "TB,R,N"
- "TQ,N,V_confidenceReasonEnum"
- "TQ,N,V_deviceClass"
- "TQ,N,V_deviceClassFrame"
- "TQ,N,V_locationOfInterestType"
- "TQ,N,V_locationType"
- "TQ,N,V_predictionsUpdateType"
- "TQ,N,V_qualityReasonEnum"
- "TQ,N,V_serviceQuality"
- "TQ,N,V_serviceState"
- "TQ,N,V_suspendReasonEnum"
- "TQ,R"
- "TQ,R,N,V_confidence"
- "TQ,R,N,V_deviceClass"
- "TQ,R,N,V_serviceState"
- "TQ,R,N,V_serviceType"
- "Testing"
- "Tf,N,V_backwardAzimuthDegrees"
- "Tf,N,V_backwardElevationDegrees"
- "Tf,N,V_forwardAzimuthDegrees"
- "Tf,N,V_forwardElevationDegrees"
- "Tf,N,V_x"
- "Tf,N,V_y"
- "Tf,N,V_yaw"
- "Tf,N,V_z"
- "Tq,N,V_entityType"
- "Tq,N,V_interactionType"
- "Tq,N,V_modelCategory"
- "Tq,N,V_rssi"
- "Tq,N,V_submapIndex"
- "ULAccessibilitySessionFetchOptions"
- "ULConfidenceReason"
- "ULConfiguration"
- "ULConnection"
- "ULContextLayerUtilities"
- "ULCoordinate"
- "ULCustomLoiConfiguration"
- "ULDevicePredictionContext"
- "ULExtensions"
- "ULFingerprintMetaInfo"
- "ULFrameworkBundle"
- "ULHomeSlamModelData"
- "ULLabel"
- "ULLabelHomeKitUserInteraction"
- "ULLabelWiFi"
- "ULLocationOfInterest"
- "ULLocationType"
- "ULMap"
- "ULMapItem"
- "ULMapItemTypeClientGenerated"
- "ULMapItemTypeMiLoGenerated"
- "ULMapPoint"
- "ULMapROI"
- "ULMapTrajectoryPoint"
- "ULPlace"
- "ULPrediction"
- "ULPredictionContext"
- "ULServiceDescriptor"
- "ULServiceMetaInfo"
- "ULServiceQualityInfo"
- "ULServiceQualityReason"
- "ULServiceStatus"
- "ULServiceSuspendReason"
- "ULUpdateConfiguration"
- "ULXPCProtocols"
- "ULXPCRequestProtocol"
- "ULXPCResponseProtocol"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_backwardAzimuthDegrees"
- "_backwardElevationDegrees"
- "_checkAndRecoverIfNeeded"
- "_confidence"
- "_confidenceReasonEnum"
- "_confidenceReasons"
- "_configuration"
- "_connection"
- "_contextLayer"
- "_contextLayers"
- "_coordinate"
- "_coordinates"
- "_cosineSimilarity_isSameSpaceForLabel:"
- "_createNSXPCConnectionWithWeakProxy:"
- "_currentLocationOfInterestType"
- "_currentLocationOfInterestUuid"
- "_darwinNotificationHelper"
- "_delegate"
- "_delegateQueue"
- "_deviceClass"
- "_deviceClassFrame"
- "_devicePredictions"
- "_entityType"
- "_error"
- "_extendProbabilityVectorForLabel:toMatchPredictionContext:"
- "_forwardAzimuthDegrees"
- "_forwardElevationDegrees"
- "_geo_isSameSpaceForLabel:horizontalThreshold:deviceClass:"
- "_geo_isSameYawLabel:yawThreshold:"
- "_getContextLayerEnumToStringMapping"
- "_homeSlamModelData"
- "_identifier"
- "_imageIdentifiersVector"
- "_image_isSameSpaceForLabel:"
- "_interactionType"
- "_internalMap"
- "_interrupted"
- "_invalidate"
- "_isInRoomDetectionEnabled"
- "_isLowLatency"
- "_isMapValid"
- "_isMotionDetected"
- "_isPredictionValid"
- "_isTracked"
- "_labelIdentifier"
- "_labels"
- "_legacyServiceIdentifier"
- "_locationOfInterest"
- "_locationOfInterestType"
- "_locationOfInterestUUID"
- "_locationType"
- "_locationTypes"
- "_manageConnectionAvailableNotificationObservation:"
- "_mapItemType"
- "_mapItems"
- "_mapPoint"
- "_mapPoints"
- "_mapROIs"
- "_metaInfo"
- "_modelCategory"
- "_name"
- "_numberOfBLESources"
- "_numberOfClustersLearnedInModel"
- "_numberOfFilteredSubmaps"
- "_numberOfFinalSegments"
- "_numberOfFingerprintsAfterPruning"
- "_numberOfFingerprintsBeforePruning"
- "_numberOfInputSegments"
- "_numberOfInputStaticIntervals"
- "_numberOfInputValidFingerprints"
- "_numberOfInputValidFingerprintsLabeled"
- "_numberOfInputValidFingerprintsUnLabeled"
- "_numberOfMappedStaticIntervals"
- "_numberOfROIs"
- "_numberOfRecordingTriggersAtCurrentLocationOfInterest"
- "_numberOfUWBSources"
- "_numberOfWalkwayPoints"
- "_numberOfWiFiAccessPoints"
- "_particles"
- "_performAsyncOnDelegateQueueIfRespondsToSelector:block:"
- "_peripheralAvailable"
- "_places"
- "_predictionContext"
- "_predictionsUpdateType"
- "_probabilityVector"
- "_qualityReasonEnum"
- "_queue"
- "_requestIdentifier"
- "_roomIndex"
- "_rssi"
- "_score"
- "_serviceDescriptor"
- "_serviceIdentifier"
- "_serviceQuality"
- "_serviceQualityInfo"
- "_serviceQualityReasons"
- "_serviceState"
- "_serviceSuspendReasons"
- "_serviceType"
- "_setQueue:"
- "_submapIndex"
- "_suspendReasonEnum"
- "_time"
- "_timestamp"
- "_trajectoryPoints"
- "_translation"
- "_uniqueIdentifier"
- "_useCaseStartTime"
- "_verifyInput:"
- "_verifyInput:labels:"
- "_x"
- "_xpcInterruptionHandler"
- "_xpcInvalidationHandler"
- "_y"
- "_yaw"
- "_z"
- "absoluteVerticalDistanceBetweenPredictionCoordinates:andLabelCoordinates:"
- "addLabel:"
- "addLabel:betweenStartDate:andEndDate:"
- "addObject:"
- "addObserverForNotificationName:handler:"
- "airPodsPrediction"
- "allValues"
- "allocWithZone:"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayByAddingObject:"
- "arrayWithObjects:count:"
- "autorelease"
- "averageRSSIOfSameSpaceLabelsForMapItem:"
- "boolValue"
- "bundleForClass:"
- "class"
- "com.apple.MicroLocation.deleteDatabaseDirectory"
- "com.apple.perception"
- "compare:"
- "confidence"
- "confidenceReasons"
- "configuration"
- "conformsToProtocol:"
- "connection"
- "connection:didCompleteObservationWithMetaInformation:"
- "connection:didCompletePredictionWithMetaInformation:"
- "connection:didCompleteRequest:withError:"
- "connection:didDisableMicrolocationAtLocationWithIdentifier:withError:"
- "connection:didEnableMicrolocationAtCurrentLocationWithError:"
- "connection:didFailWithError:"
- "connection:didSendGenericEvent:withDescription:"
- "connectionDidUpdateMap:"
- "connectionDidUpdatePredictionContext:"
- "containsObject:"
- "contextLayerEnum"
- "contextLayerEnumFromStringType:"
- "contextLayerStringTypeFromEnum:"
- "coordinateForFrame:andSubmapIndex:"
- "copy"
- "copyUpdatingDevicePredictionContext:"
- "copyUpdatingInteractionType:"
- "copyWithReplacementContextLayerFromServiceIdentifier:"
- "copyWithReplacementPredictionContext:"
- "copyWithZone:"
- "cosineSimilarityBetweenPredictionProbabilities:withPreCalculatedMagnitude:andLabelProbabilities:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createCustomLocationOfInterestAtCurrentLocationWithConfiguration:"
- "createServiceIdentifierForToken:"
- "createServiceWithServiceType:locationTypes:reply:"
- "currentLocationOfInterestType"
- "currentLocationOfInterestUuid"
- "currentMap"
- "darwinNotificationHelper"
- "dataWithBytes:length:"
- "date"
- "dealloc"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "delegate"
- "delegateQueue"
- "deleteDatabaseDirectoryWithReply:"
- "deleteServiceWithIdentifier:reply:"
- "description"
- "devicePredictionContextForDeviceClass:"
- "dictionaryWithObjects:forKeys:count:"
- "didCompleteObservationWithMetaInformation:"
- "didCompletePredictionWithMetaInformation:"
- "didCompleteRequest:withError:"
- "didCreateCustomLocationOfInterestWithError:"
- "didFailWithError:"
- "didRemoveCustomLocationOfInterestWithIdentifier:withError:"
- "didSendGenericEvent:withDescription:"
- "didUpdateDevicePredictionContext:"
- "didUpdateMap:"
- "disableMicrolocationAtlocationWithIdentifier:"
- "disconnectWithRequestIdentifier:"
- "donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:"
- "donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:"
- "emptyHomeSlamModelData"
- "emptyLocationOfInterest"
- "emptyMap"
- "emptyPredictionContext"
- "emptyServiceMetaInfo"
- "enableMicrolocationAtCurrentLocation"
- "enableMicrolocationAtCurrentLocationWithConfiguration:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "error"
- "errorWithDomain:code:userInfo:"
- "exportDatabaseWithReply:"
- "exportVisualLoggerDataWithReply:"
- "f"
- "f16@0:8"
- "firstObject"
- "floatValue"
- "getBytes:length:"
- "getDefaultContextLayerForService:"
- "getMicroLocationInternalVersion"
- "getMicroLocationInternalVersionWithReply:"
- "getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:"
- "hasDirectionalContext"
- "hasSpatialContext"
- "hash"
- "horizontalDistanceSquaredBetweenPredictionCoordinates:andLabelCoordinates:"
- "identifier"
- "imageFeaturesDebugWithTask:additionalInformation:reply:"
- "init"
- "initServiceWithQuality:andReasons:"
- "initWithCoder:"
- "initWithConfidenceReasonEnum:"
- "initWithContextLayers:"
- "initWithDelegate:serviceIdentifier:"
- "initWithDeviceClass:"
- "initWithDevicePredictions:"
- "initWithDictionary:copyItems:"
- "initWithEnableInRoomDetection:"
- "initWithFormat:"
- "initWithIsLowLatency:"
- "initWithLocationOfInterestType:locationOfInterestUUID:"
- "initWithLocationTypeEnum:"
- "initWithMachServiceName:options:"
- "initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:homeSlamModelData:"
- "initWithMapPoint:forwardAzimuth:forwardElevation:backwardAzimuth:backwardElevation:"
- "initWithMapPoints:roomIndex:"
- "initWithMapROIs:trajectoryPoints:numInputSegments:numInputStaticIntervals:numMappedStaticIntervals:numFinalSegments:numFilteredSubmaps:numROIs:numWalkwayPoints:"
- "initWithMapROIs:trajectoryPoints:numInputSegments:numberOfInputStaticIntervals:numberOfMappedStaticIntervals:numberOfMappedSegments:numberOfFilteredSubmaps:numROIs:numWalkwayPoints:"
- "initWithName:"
- "initWithName:andContextLayerType:"
- "initWithName:contextLayerType:andDeviceClass:"
- "initWithName:deviceClass:andEntityType:"
- "initWithName:entityType:timestamp:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:interactionType:"
- "initWithName:entityType:timestamp:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:interactionType:labelIdentifier:"
- "initWithName:labels:mapItemType:"
- "initWithName:rssi:"
- "initWithName:rssi:timestamp:coordinate:probabilityVector:imageIdentifiersVector:"
- "initWithName:timestamp:contextLayer:deviceClass:coordinate:probabilityVector:imageIdentifiersVector:"
- "initWithName:timestamp:contextLayerType:deviceClass:"
- "initWithName:timestamp:deviceClass:entityType:"
- "initWithName:timestamp:deviceClass:entityType:interactionType:"
- "initWithName:timestamp:deviceClass:entityType:interactionType:labelIdentifier:"
- "initWithName:timestamp:rssi:"
- "initWithNumClustersLearnedInModel:numRecordingTriggersAtCurrentLOI:numInputValidFingerprints:numInputValidFingerprintsLabeled:numInputValidFingerprintsUnlabeled:numFingerprintsBeforePruning:numFingerprintsAfterPruning:numWiFiAccessPoints:numBLESources:numUWBSources:peripheralAvailable:modelCategory:"
- "initWithNumWiFiAccessPoints:numBLESources:numUWBSources:requestIdentifier:"
- "initWithObject:"
- "initWithQualityReasonEnum:"
- "initWithServiceIdentifier:serviceType:locationTypes:"
- "initWithSuspendReasonEnum:"
- "initWithTranslation:yaw:submapIndex:isTracked:deviceClassFrame:"
- "initWithUUIDString:"
- "initWithUniqueIdentifier:timestamp:isMotionDetected:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:particles:"
- "initWithUseCaseStartTime:"
- "initWithX:Y:Z:"
- "integerValue"
- "interfaceWithProtocol:"
- "internalMap"
- "interrupted"
- "invalid"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPredictionValid"
- "isProxy"
- "isValid"
- "keyForObject:"
- "labelsInSameSpaceAndYawForMapItem:"
- "labelsInSameSpaceForMapItem:"
- "labelsInSameSpaceForMapItem:forDeviceClass:"
- "labelsInSameSpaceForMapItem:forDeviceClass:horizontalThreshold:yawThreshold:"
- "legacyServiceIdentifier"
- "localizedDescription"
- "magnitudeOfVector:"
- "mainDevicePrediction"
- "mapItemType"
- "metadataForHomekitAccessoryControlEventWithUUID:stateString:serviceUUID:serviceType:characteristicType:serviceGroupUUID:source:roomUUID:"
- "metadataForHomekitActionSetEventWithUUID:name:type:clientName:source:homeName:"
- "mutableCopy"
- "new"
- "newestDevicePrediction"
- "now"
- "numberOfLabelsInSameSpaceForMapItem:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "peripheralDebugTask:reply:"
- "places"
- "purgeDatabaseWithReply:"
- "q16@0:8"
- "q24@0:8@16"
- "queryServicesWithReply:"
- "queue"
- "release"
- "remoteObjectProxy"
- "removeCustomLocationOfInterestWithIdentifier:"
- "removeObjectForKey:"
- "removeObserverForNotificationName:"
- "requestAllModelsLearningWithRequestIdentifier:"
- "requestCurrentMicroLocationWithAdditionalInformation:"
- "requestCurrentMicroLocationWithAdditionalInformation:reply:"
- "requestInterface"
- "requestMapReconstructionWithRequestIdentifier:"
- "requestMicroLocationRecordingScanWithAdditionalInformation:reply:"
- "requestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:"
- "requestObservationWithRequestIdentifier:"
- "requestPredictionWithRequestIdentifier:"
- "respondsToSelector:"
- "responseInterface"
- "resume"
- "retain"
- "retainCount"
- "runWithConfiguration:"
- "runWithConfiguration:serviceIdentifier:legacyServiceIdentifier:andRequestIdentifier:"
- "score"
- "self"
- "serviceDescriptor"
- "serviceQualityInfo"
- "set"
- "setBackwardAzimuthDegrees:"
- "setBackwardElevationDegrees:"
- "setClass:forSelector:argumentIndex:ofReply:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConfidenceReasonEnum:"
- "setConfiguration:"
- "setConnection:"
- "setContextLayer:"
- "setContextLayers:"
- "setCoordinate:"
- "setCoordinateForTesting:"
- "setCoordinates:"
- "setDarwinNotificationHelper:"
- "setDelegate:"
- "setDelegateQueue:"
- "setDeviceClass:"
- "setDeviceClassFrame:"
- "setDevicePredictions:"
- "setEntityType:"
- "setExportedInterface:"
- "setExportedObject:"
- "setForwardAzimuthDegrees:"
- "setForwardElevationDegrees:"
- "setHomeSlamModelData:"
- "setImageIdentifiersVector:"
- "setInteractionType:"
- "setInternalMap:"
- "setInterrupted:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsInRoomDetectionEnabled:"
- "setIsLowLatency:"
- "setIsMapValid:"
- "setIsMotionDetected:"
- "setIsPredictionValid:"
- "setIsTracked:"
- "setLabelIdentifier:"
- "setLabels:"
- "setLegacyServiceIdentifier:"
- "setLocationOfInterest:"
- "setLocationOfInterestType:"
- "setLocationOfInterestUUID:"
- "setLocationType:"
- "setMapItemType:"
- "setMapItems:"
- "setMapPoint:"
- "setMapPoints:"
- "setMapROIs:"
- "setMetaInfo:"
- "setModelCategory:"
- "setName:"
- "setNumberOfBLESources:"
- "setNumberOfClustersLearnedInModel:"
- "setNumberOfFilteredSubmaps:"
- "setNumberOfFinalSegments:"
- "setNumberOfFingerprintsAfterPruning:"
- "setNumberOfFingerprintsBeforePruning:"
- "setNumberOfInputSegments:"
- "setNumberOfInputStaticIntervals:"
- "setNumberOfInputValidFingerprints:"
- "setNumberOfInputValidFingerprintsLabeled:"
- "setNumberOfInputValidFingerprintsUnLabeled:"
- "setNumberOfMappedStaticIntervals:"
- "setNumberOfROIs:"
- "setNumberOfRecordingTriggersAtCurrentLocationOfInterest:"
- "setNumberOfUWBSources:"
- "setNumberOfWalkwayPoints:"
- "setNumberOfWiFiAccessPoints:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setParticles:"
- "setPeripheralAvailable:"
- "setPredictionContext:"
- "setPredictionsUpdateType:"
- "setProbabilityVector:"
- "setQualityReasonEnum:"
- "setQueue:"
- "setRemoteObjectInterface:"
- "setRequestIdentifier:"
- "setRoomIndex:"
- "setRssi:"
- "setServiceIdentifier:"
- "setServiceQuality:"
- "setServiceQualityReasons:"
- "setServiceState:"
- "setServiceSuspendReasons:"
- "setSubmapIndex:"
- "setSuspendReasonEnum:"
- "setTimestamp:"
- "setTrajectoryPoints:"
- "setTranslation:"
- "setUniqueIdentifier:"
- "setValue:forKey:"
- "setWithArray:"
- "setWithObject:"
- "setWithObjects:"
- "setX:"
- "setY:"
- "setYaw:"
- "setZ:"
- "signingIdentity"
- "signingIdentityForSelf"
- "startUpdatingWithConfiguration:"
- "stringWithFormat:"
- "sumOfVector:"
- "superclass"
- "supportsSecureCoding"
- "terminateDaemonWithReply:"
- "time"
- "trackedCoordinateForFrame:"
- "trackedCoordinateInSelfFrameForDeviceClass:"
- "ul_cachedInstanceForNSString:"
- "ul_decodeAndCacheNSStringForKey:"
- "ul_decodeVector3ForKey:"
- "ul_encodeVector3:forKey:"
- "ul_firstWhere:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateDevicePredictionContext:"
- "updateHomeKitUserInteractionLabel:"
- "updateLegacyServiceIdentifier:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@\"ULCustomLoiConfiguration\"16"
- "v24@0:8@\"ULDevicePredictionContext\"16"
- "v24@0:8@\"ULFingerprintMetaInfo\"16"
- "v24@0:8@\"ULLabel\"16"
- "v24@0:8@\"ULLabelHomeKitUserInteraction\"16"
- "v24@0:8@\"ULMap\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:816"
- "v32@0:8:16@?24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@\"NSError\"24"
- "v32@0:8@\"NSUUID\"16@\"NSError\"24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8Q16@\"NSString\"24"
- "v32@0:8Q16@24"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"NSError\">24"
- "v36@0:8@\"NSDictionary\"16B24@?<v@?B@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v40@0:816@32"
- "v40@0:8@\"ULLabel\"16@\"NSDate\"24@\"NSDate\"32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8Q16@\"NSArray\"24@?<v@?@\"NSString\"@\"NSError\">32"
- "v40@0:8Q16@\"NSArray\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v48@0:8@\"ULConfiguration\"16@\"NSUUID\"24@\"NSUUID\"32@\"NSUUID\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "visualLoggerAddDestinationWithHost:"
- "yaw"
- "zone"
- "{\"msg%{public}.0s\":\"Same Space For Map Item\", \"MapItem name\":%{public, location:escape_only}s, \"Same space anchors\":%{public}lu, \"Total anchors\":%{public}lu}"

```
