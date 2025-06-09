## MicroLocation

> `/System/Library/PrivateFrameworks/MicroLocation.framework/MicroLocation`

```diff

-27.0.28.0.7
-  __TEXT.__text: 0xcaa8
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x11bc
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x15c
-  __TEXT.__cstring: 0x18ea
-  __TEXT.__oslogstring: 0x736
-  __TEXT.__unwind_info: 0x410
-  __TEXT.__objc_classname: 0x1a8
-  __TEXT.__objc_methname: 0x274d
-  __TEXT.__objc_methtype: 0x6ab
-  __TEXT.__objc_stubs: 0x1900
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x508
-  __DATA_CONST.__objc_classlist: 0x80
-  __DATA_CONST.__objc_catlist: 0x8
+27.0.60.0.7
+  __TEXT.__text: 0x1272c
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x1b84
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x2278
+  __TEXT.__gcc_except_tab: 0x130
+  __TEXT.__oslogstring: 0x8df
+  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__objc_classname: 0x25f
+  __TEXT.__objc_methname: 0x37d9
+  __TEXT.__objc_methtype: 0x865
+  __TEXT.__objc_stubs: 0x24e0
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__objc_classlist: 0xd8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f0
+  __DATA_CONST.__objc_selrefs: 0xbb0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x248
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x1680
-  __AUTH_CONST.__objc_const: 0x1980
-  __DATA.__objc_ivar: 0xd4
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__auth_got: 0x260
+  __AUTH_CONST.__const: 0x80
+  __AUTH_CONST.__cfstring: 0x2260
+  __AUTH_CONST.__objc_const: 0x2ab8
+  __AUTH_CONST.__objc_intobj: 0x270
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x240
-  __DATA_DIRTY.__objc_data: 0x500
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 472E0590-2747-3682-B889-CAC6AAE8F255
-  Functions: 360
-  Symbols:   1375
-  CStrings:  915
+  UUID: 774C36F6-6B3F-37AA-9C16-FF4996E819AB
+  Functions: 561
+  Symbols:   2072
+  CStrings:  1361
 
Symbols:
+ +[ULConfiguration new]
+ +[ULConfiguration supportsSecureCoding]
+ +[ULConnection createServiceIdentifierForToken:].cold.1
+ +[ULConnection(Diagnostic) imageFeaturesDebugWithTask:additionalInformation:reply:]
+ +[ULConnection(Diagnostic) imageFeaturesDebugWithTask:additionalInformation:reply:].cold.1
+ +[ULConnection(Diagnostic) polarisDebugWithTask:reply:]
+ +[ULConnection(Diagnostic) polarisDebugWithTask:reply:].cold.1
+ +[ULContextLayerUtilities _getContextLayerEnumToStringMapping]
+ +[ULContextLayerUtilities _getContextLayerEnumToStringMapping].cold.1
+ +[ULContextLayerUtilities contextLayerEnumFromStringType:]
+ +[ULContextLayerUtilities contextLayerStringTypeFromEnum:]
+ +[ULContextLayerUtilities getDefaultContextLayerForService:]
+ +[ULContextLayerUtilities getDefaultContextLayerForService:].cold.1
+ +[ULHomeSlamModelData emptyHomeSlamModelData]
+ +[ULHomeSlamModelData new]
+ +[ULHomeSlamModelData supportsSecureCoding]
+ +[ULLabel supportsSecureCoding]
+ +[ULLabelWiFi supportsSecureCoding]
+ +[ULLocationOfInterest emptyLocationOfInterest]
+ +[ULLocationOfInterest supportsSecureCoding]
+ +[ULMap emptyMap]
+ +[ULMap supportsSecureCoding]
+ +[ULMapItem _verifyInput:]
+ +[ULMapItem _verifyInput:labels:]
+ +[ULMapItem supportsSecureCoding]
+ +[ULMapPoint new]
+ +[ULMapPoint supportsSecureCoding]
+ +[ULMapROI new]
+ +[ULMapROI supportsSecureCoding]
+ +[ULMapTrajectoryPoint new]
+ +[ULMapTrajectoryPoint supportsSecureCoding]
+ +[ULPredictionContext emptyPredictionContext]
+ +[ULPredictionContext supportsSecureCoding]
+ +[ULServiceMetaInfo emptyServiceMetaInfo]
+ -[NSCoder(ULExtensions) ul_decodeAndCacheNSStringForKey:]
+ -[NSCoder(ULExtensions) ul_decodeVector3ForKey:]
+ -[NSCoder(ULExtensions) ul_encodeVector3:forKey:]
+ -[ULConfiguration .cxx_destruct]
+ -[ULConfiguration contextLayers]
+ -[ULConfiguration copyWithZone:]
+ -[ULConfiguration description]
+ -[ULConfiguration deviceClass]
+ -[ULConfiguration encodeWithCoder:]
+ -[ULConfiguration hash]
+ -[ULConfiguration initWithCoder:]
+ -[ULConfiguration initWithContextLayers:]
+ -[ULConfiguration init]
+ -[ULConfiguration isEqual:]
+ -[ULConfiguration predictionsUpdateType]
+ -[ULConfiguration setContextLayers:]
+ -[ULConfiguration setDeviceClass:]
+ -[ULConfiguration setPredictionsUpdateType:]
+ -[ULConnection addLabel:]
+ -[ULConnection addLabel:betweenStartDate:andEndDate:]
+ -[ULConnection configuration]
+ -[ULConnection connect].cold.1
+ -[ULConnection connect].cold.2
+ -[ULConnection currentMap]
+ -[ULConnection didUpdateMap:]
+ -[ULConnection didUpdatePredictionContext:]
+ -[ULConnection internalMap]
+ -[ULConnection runWithConfiguration:]
+ -[ULConnection setConfiguration:]
+ -[ULConnection setInternalMap:]
+ -[ULConnection startUpdatingWithConfiguration:].cold.1
+ -[ULConnection stopUpdating].cold.1
+ -[ULFingerprintMetaInfo initWithNumWiFiAccessPoints:numBLESources:numUWBSources:requestIdentifier:]
+ -[ULHomeSlamModelData .cxx_destruct]
+ -[ULHomeSlamModelData copyWithZone:]
+ -[ULHomeSlamModelData description]
+ -[ULHomeSlamModelData encodeWithCoder:]
+ -[ULHomeSlamModelData hash]
+ -[ULHomeSlamModelData initWithCoder:]
+ -[ULHomeSlamModelData initWithMapROIs:trajectoryPoints:numInputSegments:]
+ -[ULHomeSlamModelData init]
+ -[ULHomeSlamModelData isEqual:]
+ -[ULHomeSlamModelData mapROIs]
+ -[ULHomeSlamModelData numberOfInputSegments]
+ -[ULHomeSlamModelData setMapROIs:]
+ -[ULHomeSlamModelData setNumberOfInputSegments:]
+ -[ULHomeSlamModelData setTrajectoryPoints:]
+ -[ULHomeSlamModelData trajectoryPoints]
+ -[ULLabel .cxx_destruct]
+ -[ULLabel contextLayerEnum]
+ -[ULLabel contextLayer]
+ -[ULLabel coordinates]
+ -[ULLabel copyWithReplacementContextLayerFromServiceIdentifier:]
+ -[ULLabel copyWithZone:]
+ -[ULLabel description]
+ -[ULLabel deviceClass]
+ -[ULLabel encodeWithCoder:]
+ -[ULLabel hash]
+ -[ULLabel imageIdentifiersVector]
+ -[ULLabel initWithCoder:]
+ -[ULLabel initWithName:]
+ -[ULLabel initWithName:andContextLayerType:]
+ -[ULLabel initWithName:contextLayerType:andDeviceClass:]
+ -[ULLabel initWithName:timestamp:contextLayer:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:]
+ -[ULLabel isEqual:]
+ -[ULLabel name]
+ -[ULLabel probabilityVector]
+ -[ULLabel setContextLayer:]
+ -[ULLabel setCoordinates:]
+ -[ULLabel setDeviceClass:]
+ -[ULLabel setImageIdentifiersVector:]
+ -[ULLabel setName:]
+ -[ULLabel setProbabilityVector:]
+ -[ULLabel setTimestamp:]
+ -[ULLabel timestamp]
+ -[ULLabel(Testing) setCoordinatesForTesting:]
+ -[ULLabelWiFi copyWithZone:]
+ -[ULLabelWiFi description]
+ -[ULLabelWiFi encodeWithCoder:]
+ -[ULLabelWiFi hash]
+ -[ULLabelWiFi initWithCoder:]
+ -[ULLabelWiFi initWithName:rssi:]
+ -[ULLabelWiFi initWithName:rssi:timestamp:coordinates:probabilityVector:imageIdentifiersVector:]
+ -[ULLabelWiFi isEqual:]
+ -[ULLabelWiFi rssi]
+ -[ULLabelWiFi setRssi:]
+ -[ULLocationOfInterest .cxx_destruct]
+ -[ULLocationOfInterest copyWithZone:]
+ -[ULLocationOfInterest description]
+ -[ULLocationOfInterest encodeWithCoder:]
+ -[ULLocationOfInterest hash]
+ -[ULLocationOfInterest initWithCoder:]
+ -[ULLocationOfInterest initWithLocationOfInterestType:locationOfInterestUUID:]
+ -[ULLocationOfInterest isEqual:]
+ -[ULLocationOfInterest locationOfInterestType]
+ -[ULLocationOfInterest locationOfInterestUUID]
+ -[ULLocationOfInterest setLocationOfInterestType:]
+ -[ULLocationOfInterest setLocationOfInterestUUID:]
+ -[ULMap .cxx_destruct]
+ -[ULMap _cosineSimilarity_isSameSpaceForLabel:]
+ -[ULMap _cosineSimilarity_isSameSpaceForLabel:].cold.1
+ -[ULMap _extendProbabilityVectorForLabel:toMatchPredictionContext:]
+ -[ULMap _geo_isSameSpaceForLabel:]
+ -[ULMap _image_isSameSpaceForLabel:]
+ -[ULMap averageRSSIOfSameSpaceLabelsForMapItem:]
+ -[ULMap copyWithReplacementPredictionContext:]
+ -[ULMap copyWithZone:]
+ -[ULMap description]
+ -[ULMap encodeWithCoder:]
+ -[ULMap hash]
+ -[ULMap homeSlamModelData]
+ -[ULMap initWithCoder:]
+ -[ULMap initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:homeSlamModelData:]
+ -[ULMap isEqual:]
+ -[ULMap isMapValid]
+ -[ULMap labelsInSameSpaceForMapItem:]
+ -[ULMap locationOfInterest]
+ -[ULMap mapItems]
+ -[ULMap metaInfo]
+ -[ULMap numberOfLabelsInSameSpaceForMapItem:]
+ -[ULMap predictionContext]
+ -[ULMap serviceState]
+ -[ULMap serviceSuspendReasons]
+ -[ULMap setHomeSlamModelData:]
+ -[ULMap setIsMapValid:]
+ -[ULMap setLocationOfInterest:]
+ -[ULMap setMapItems:]
+ -[ULMap setMetaInfo:]
+ -[ULMap setPredictionContext:]
+ -[ULMap setServiceState:]
+ -[ULMap setServiceSuspendReasons:]
+ -[ULMapItem .cxx_destruct]
+ -[ULMapItem contextLayerEnum]
+ -[ULMapItem contextLayer]
+ -[ULMapItem copyWithZone:]
+ -[ULMapItem description]
+ -[ULMapItem encodeWithCoder:]
+ -[ULMapItem hash]
+ -[ULMapItem initWithCoder:]
+ -[ULMapItem initWithName:labels:mapItemType:]
+ -[ULMapItem isEqual:]
+ -[ULMapItem labels]
+ -[ULMapItem mapItemType]
+ -[ULMapItem name]
+ -[ULMapItem setContextLayer:]
+ -[ULMapItem setLabels:]
+ -[ULMapItem setMapItemType:]
+ -[ULMapItem setName:]
+ -[ULMapPoint copyWithZone:]
+ -[ULMapPoint description]
+ -[ULMapPoint encodeWithCoder:]
+ -[ULMapPoint hash]
+ -[ULMapPoint initWithCoder:]
+ -[ULMapPoint initWithX:Y:Z:]
+ -[ULMapPoint init]
+ -[ULMapPoint isEqual:]
+ -[ULMapPoint setX:]
+ -[ULMapPoint setY:]
+ -[ULMapPoint setZ:]
+ -[ULMapPoint x]
+ -[ULMapPoint y]
+ -[ULMapPoint z]
+ -[ULMapROI .cxx_destruct]
+ -[ULMapROI copyWithZone:]
+ -[ULMapROI description]
+ -[ULMapROI encodeWithCoder:]
+ -[ULMapROI hash]
+ -[ULMapROI initWithCoder:]
+ -[ULMapROI initWithMapPoints:roomIndex:]
+ -[ULMapROI init]
+ -[ULMapROI isEqual:]
+ -[ULMapROI mapPoints]
+ -[ULMapROI roomIndex]
+ -[ULMapROI setMapPoints:]
+ -[ULMapROI setRoomIndex:]
+ -[ULMapTrajectoryPoint .cxx_destruct]
+ -[ULMapTrajectoryPoint backwardAzimuthDegrees]
+ -[ULMapTrajectoryPoint backwardElevationDegrees]
+ -[ULMapTrajectoryPoint copyWithZone:]
+ -[ULMapTrajectoryPoint description]
+ -[ULMapTrajectoryPoint encodeWithCoder:]
+ -[ULMapTrajectoryPoint forwardAzimuthDegrees]
+ -[ULMapTrajectoryPoint forwardElevationDegrees]
+ -[ULMapTrajectoryPoint hash]
+ -[ULMapTrajectoryPoint initWithCoder:]
+ -[ULMapTrajectoryPoint initWithMapPoint:forwardAzimuth:forwardElevation:backwardAzimuth:backwardElevation:]
+ -[ULMapTrajectoryPoint init]
+ -[ULMapTrajectoryPoint isEqual:]
+ -[ULMapTrajectoryPoint mapPoint]
+ -[ULMapTrajectoryPoint setBackwardAzimuthDegrees:]
+ -[ULMapTrajectoryPoint setBackwardElevationDegrees:]
+ -[ULMapTrajectoryPoint setForwardAzimuthDegrees:]
+ -[ULMapTrajectoryPoint setForwardElevationDegrees:]
+ -[ULMapTrajectoryPoint setMapPoint:]
+ -[ULPredictionContext .cxx_destruct]
+ -[ULPredictionContext coordinates]
+ -[ULPredictionContext copyWithZone:]
+ -[ULPredictionContext description]
+ -[ULPredictionContext encodeWithCoder:]
+ -[ULPredictionContext hash]
+ -[ULPredictionContext imageIdentifiersVector]
+ -[ULPredictionContext initWithCoder:]
+ -[ULPredictionContext initWithUniqueIdentifier:timestamp:isMotionDetected:coordinates:probabilityVector:imageIdentifiersVector:particles:]
+ -[ULPredictionContext isEqual:]
+ -[ULPredictionContext isMotionDetected]
+ -[ULPredictionContext isPredictionValid]
+ -[ULPredictionContext particles]
+ -[ULPredictionContext probabilityVector]
+ -[ULPredictionContext setCoordinates:]
+ -[ULPredictionContext setImageIdentifiersVector:]
+ -[ULPredictionContext setIsMotionDetected:]
+ -[ULPredictionContext setParticles:]
+ -[ULPredictionContext setProbabilityVector:]
+ -[ULPredictionContext setTimestamp:]
+ -[ULPredictionContext setUniqueIdentifier:]
+ -[ULPredictionContext timestamp]
+ -[ULPredictionContext uniqueIdentifier]
+ -[ULPredictionContext(Testing) setCoordinatesForTesting:]
+ GCC_except_table113
+ GCC_except_table14
+ GCC_except_table18
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table33
+ GCC_except_table58
+ GCC_except_table99
+ _OBJC_CLASS_$_NSCoder
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_ULBidirectionalDictionary
+ _OBJC_CLASS_$_ULConfiguration
+ _OBJC_CLASS_$_ULContextLayerUtilities
+ _OBJC_CLASS_$_ULHomeSlamModelData
+ _OBJC_CLASS_$_ULLabel
+ _OBJC_CLASS_$_ULLabelWiFi
+ _OBJC_CLASS_$_ULLocationOfInterest
+ _OBJC_CLASS_$_ULMap
+ _OBJC_CLASS_$_ULMapItem
+ _OBJC_CLASS_$_ULMapPoint
+ _OBJC_CLASS_$_ULMapROI
+ _OBJC_CLASS_$_ULMapTrajectoryPoint
+ _OBJC_CLASS_$_ULNumericUtilities
+ _OBJC_CLASS_$_ULObjectCacheNSString
+ _OBJC_CLASS_$_ULPredictionContext
+ _OBJC_CLASS_$_ULSameSpaceUtilities
+ _OBJC_IVAR_$_ULConfiguration._contextLayers
+ _OBJC_IVAR_$_ULConfiguration._deviceClass
+ _OBJC_IVAR_$_ULConfiguration._predictionsUpdateType
+ _OBJC_IVAR_$_ULConnection._configuration
+ _OBJC_IVAR_$_ULConnection._internalMap
+ _OBJC_IVAR_$_ULHomeSlamModelData._mapROIs
+ _OBJC_IVAR_$_ULHomeSlamModelData._numberOfInputSegments
+ _OBJC_IVAR_$_ULHomeSlamModelData._trajectoryPoints
+ _OBJC_IVAR_$_ULLabel._contextLayer
+ _OBJC_IVAR_$_ULLabel._coordinates
+ _OBJC_IVAR_$_ULLabel._deviceClass
+ _OBJC_IVAR_$_ULLabel._imageIdentifiersVector
+ _OBJC_IVAR_$_ULLabel._name
+ _OBJC_IVAR_$_ULLabel._probabilityVector
+ _OBJC_IVAR_$_ULLabel._timestamp
+ _OBJC_IVAR_$_ULLabelWiFi._rssi
+ _OBJC_IVAR_$_ULLocationOfInterest._locationOfInterestType
+ _OBJC_IVAR_$_ULLocationOfInterest._locationOfInterestUUID
+ _OBJC_IVAR_$_ULMap._homeSlamModelData
+ _OBJC_IVAR_$_ULMap._isMapValid
+ _OBJC_IVAR_$_ULMap._locationOfInterest
+ _OBJC_IVAR_$_ULMap._mapItems
+ _OBJC_IVAR_$_ULMap._metaInfo
+ _OBJC_IVAR_$_ULMap._predictionContext
+ _OBJC_IVAR_$_ULMap._serviceState
+ _OBJC_IVAR_$_ULMap._serviceSuspendReasons
+ _OBJC_IVAR_$_ULMapItem._contextLayer
+ _OBJC_IVAR_$_ULMapItem._labels
+ _OBJC_IVAR_$_ULMapItem._mapItemType
+ _OBJC_IVAR_$_ULMapItem._name
+ _OBJC_IVAR_$_ULMapPoint._x
+ _OBJC_IVAR_$_ULMapPoint._y
+ _OBJC_IVAR_$_ULMapPoint._z
+ _OBJC_IVAR_$_ULMapROI._mapPoints
+ _OBJC_IVAR_$_ULMapROI._roomIndex
+ _OBJC_IVAR_$_ULMapTrajectoryPoint._backwardAzimuthDegrees
+ _OBJC_IVAR_$_ULMapTrajectoryPoint._backwardElevationDegrees
+ _OBJC_IVAR_$_ULMapTrajectoryPoint._forwardAzimuthDegrees
+ _OBJC_IVAR_$_ULMapTrajectoryPoint._forwardElevationDegrees
+ _OBJC_IVAR_$_ULMapTrajectoryPoint._mapPoint
+ _OBJC_IVAR_$_ULPredictionContext._coordinates
+ _OBJC_IVAR_$_ULPredictionContext._imageIdentifiersVector
+ _OBJC_IVAR_$_ULPredictionContext._isMotionDetected
+ _OBJC_IVAR_$_ULPredictionContext._particles
+ _OBJC_IVAR_$_ULPredictionContext._probabilityVector
+ _OBJC_IVAR_$_ULPredictionContext._timestamp
+ _OBJC_IVAR_$_ULPredictionContext._uniqueIdentifier
+ _OBJC_METACLASS_$_ULConfiguration
+ _OBJC_METACLASS_$_ULContextLayerUtilities
+ _OBJC_METACLASS_$_ULHomeSlamModelData
+ _OBJC_METACLASS_$_ULLabel
+ _OBJC_METACLASS_$_ULLabelWiFi
+ _OBJC_METACLASS_$_ULLocationOfInterest
+ _OBJC_METACLASS_$_ULMap
+ _OBJC_METACLASS_$_ULMapItem
+ _OBJC_METACLASS_$_ULMapPoint
+ _OBJC_METACLASS_$_ULMapROI
+ _OBJC_METACLASS_$_ULMapTrajectoryPoint
+ _OBJC_METACLASS_$_ULPredictionContext
+ _ULContextLayerTypeDataCollectionApp
+ _ULContextLayerTypeFocusMode
+ _ULContextLayerTypeHomeSlamApp
+ _ULContextLayerTypeIRAppleTVControl
+ _ULContextLayerTypeIRControlCenter
+ _ULContextLayerTypeIRHome
+ _ULContextLayerTypeIRHostTestsAppleTVControl
+ _ULContextLayerTypeIRHostTestsHome
+ _ULContextLayerTypeIRHostTestsMedia
+ _ULContextLayerTypeIRMedia
+ _ULContextLayerTypeIRMediaRemote
+ _ULContextLayerTypeIRMusic
+ _ULContextLayerTypeIRNeighborhoodActivity
+ _ULContextLayerTypeIRRoutePickerView
+ _ULContextLayerTypeIRRoverApp
+ _ULContextLayerTypeIRTVRemote
+ _ULContextLayerTypeIRTelephonyUtilities
+ _ULContextLayerTypeLslApp
+ _ULContextLayerTypeMiLoDebug
+ _ULContextLayerTypeMiLoHostTests
+ _ULContextLayerTypeMiLoPlaceholderApp
+ _ULContextLayerTypeRoomClass
+ _ULContextLayerTypeUnknown
+ _ULContextLayerTypeWiFi
+ _ULCoordinatesNotAvailable
+ _ULDeviceClassToString
+ _ULMapItemTypeClientGenerated
+ _ULMapItemTypeMiLoGenerated
+ _ULPolarisManagerTaskToString
+ _ULPredictionsUpdateTypeToString
+ _ULRssiNotAvailable
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSCoder_$_ULExtensions
+ __OBJC_$_CATEGORY_NSCoder_$_ULExtensions
+ __OBJC_$_CLASS_METHODS_ULConfiguration
+ __OBJC_$_CLASS_METHODS_ULContextLayerUtilities
+ __OBJC_$_CLASS_METHODS_ULHomeSlamModelData
+ __OBJC_$_CLASS_METHODS_ULLabel
+ __OBJC_$_CLASS_METHODS_ULLabelWiFi
+ __OBJC_$_CLASS_METHODS_ULLocationOfInterest
+ __OBJC_$_CLASS_METHODS_ULMap
+ __OBJC_$_CLASS_METHODS_ULMapItem
+ __OBJC_$_CLASS_METHODS_ULMapPoint
+ __OBJC_$_CLASS_METHODS_ULMapROI
+ __OBJC_$_CLASS_METHODS_ULMapTrajectoryPoint
+ __OBJC_$_CLASS_METHODS_ULPredictionContext
+ __OBJC_$_CLASS_PROP_LIST_ULConfiguration
+ __OBJC_$_CLASS_PROP_LIST_ULHomeSlamModelData
+ __OBJC_$_CLASS_PROP_LIST_ULLabel
+ __OBJC_$_CLASS_PROP_LIST_ULLocationOfInterest
+ __OBJC_$_CLASS_PROP_LIST_ULMap
+ __OBJC_$_CLASS_PROP_LIST_ULMapItem
+ __OBJC_$_CLASS_PROP_LIST_ULMapPoint
+ __OBJC_$_CLASS_PROP_LIST_ULMapROI
+ __OBJC_$_CLASS_PROP_LIST_ULMapTrajectoryPoint
+ __OBJC_$_CLASS_PROP_LIST_ULPredictionContext
+ __OBJC_$_INSTANCE_METHODS_ULConfiguration
+ __OBJC_$_INSTANCE_METHODS_ULHomeSlamModelData
+ __OBJC_$_INSTANCE_METHODS_ULLabel(Testing)
+ __OBJC_$_INSTANCE_METHODS_ULLabelWiFi
+ __OBJC_$_INSTANCE_METHODS_ULLocationOfInterest
+ __OBJC_$_INSTANCE_METHODS_ULMap
+ __OBJC_$_INSTANCE_METHODS_ULMapItem
+ __OBJC_$_INSTANCE_METHODS_ULMapPoint
+ __OBJC_$_INSTANCE_METHODS_ULMapROI
+ __OBJC_$_INSTANCE_METHODS_ULMapTrajectoryPoint
+ __OBJC_$_INSTANCE_METHODS_ULPredictionContext(Testing)
+ __OBJC_$_INSTANCE_VARIABLES_ULConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_ULHomeSlamModelData
+ __OBJC_$_INSTANCE_VARIABLES_ULLabel
+ __OBJC_$_INSTANCE_VARIABLES_ULLabelWiFi
+ __OBJC_$_INSTANCE_VARIABLES_ULLocationOfInterest
+ __OBJC_$_INSTANCE_VARIABLES_ULMap
+ __OBJC_$_INSTANCE_VARIABLES_ULMapItem
+ __OBJC_$_INSTANCE_VARIABLES_ULMapPoint
+ __OBJC_$_INSTANCE_VARIABLES_ULMapROI
+ __OBJC_$_INSTANCE_VARIABLES_ULMapTrajectoryPoint
+ __OBJC_$_INSTANCE_VARIABLES_ULPredictionContext
+ __OBJC_$_PROP_LIST_ULConfiguration
+ __OBJC_$_PROP_LIST_ULHomeSlamModelData
+ __OBJC_$_PROP_LIST_ULLabel
+ __OBJC_$_PROP_LIST_ULLabelWiFi
+ __OBJC_$_PROP_LIST_ULLocationOfInterest
+ __OBJC_$_PROP_LIST_ULMap
+ __OBJC_$_PROP_LIST_ULMapItem
+ __OBJC_$_PROP_LIST_ULMapPoint
+ __OBJC_$_PROP_LIST_ULMapROI
+ __OBJC_$_PROP_LIST_ULMapTrajectoryPoint
+ __OBJC_$_PROP_LIST_ULPredictionContext
+ __OBJC_CLASS_PROTOCOLS_$_ULConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_ULHomeSlamModelData
+ __OBJC_CLASS_PROTOCOLS_$_ULLabel
+ __OBJC_CLASS_PROTOCOLS_$_ULLocationOfInterest
+ __OBJC_CLASS_PROTOCOLS_$_ULMap
+ __OBJC_CLASS_PROTOCOLS_$_ULMapItem
+ __OBJC_CLASS_PROTOCOLS_$_ULMapPoint
+ __OBJC_CLASS_PROTOCOLS_$_ULMapROI
+ __OBJC_CLASS_PROTOCOLS_$_ULMapTrajectoryPoint
+ __OBJC_CLASS_PROTOCOLS_$_ULPredictionContext
+ __OBJC_CLASS_RO_$_ULConfiguration
+ __OBJC_CLASS_RO_$_ULContextLayerUtilities
+ __OBJC_CLASS_RO_$_ULHomeSlamModelData
+ __OBJC_CLASS_RO_$_ULLabel
+ __OBJC_CLASS_RO_$_ULLabelWiFi
+ __OBJC_CLASS_RO_$_ULLocationOfInterest
+ __OBJC_CLASS_RO_$_ULMap
+ __OBJC_CLASS_RO_$_ULMapItem
+ __OBJC_CLASS_RO_$_ULMapPoint
+ __OBJC_CLASS_RO_$_ULMapROI
+ __OBJC_CLASS_RO_$_ULMapTrajectoryPoint
+ __OBJC_CLASS_RO_$_ULPredictionContext
+ __OBJC_METACLASS_RO_$_ULConfiguration
+ __OBJC_METACLASS_RO_$_ULContextLayerUtilities
+ __OBJC_METACLASS_RO_$_ULHomeSlamModelData
+ __OBJC_METACLASS_RO_$_ULLabel
+ __OBJC_METACLASS_RO_$_ULLabelWiFi
+ __OBJC_METACLASS_RO_$_ULLocationOfInterest
+ __OBJC_METACLASS_RO_$_ULMap
+ __OBJC_METACLASS_RO_$_ULMapItem
+ __OBJC_METACLASS_RO_$_ULMapPoint
+ __OBJC_METACLASS_RO_$_ULMapROI
+ __OBJC_METACLASS_RO_$_ULMapTrajectoryPoint
+ __OBJC_METACLASS_RO_$_ULPredictionContext
+ ___25-[ULConnection addLabel:]_block_invoke
+ ___25-[ULConnection addLabel:]_block_invoke.cold.1
+ ___26-[ULConnection currentMap]_block_invoke
+ ___29-[ULConnection didUpdateMap:]_block_invoke
+ ___37-[ULConnection runWithConfiguration:]_block_invoke
+ ___37-[ULConnection runWithConfiguration:]_block_invoke.cold.1
+ ___39-[ULConnection _xpcInterruptionHandler]_block_invoke
+ ___43-[ULConnection didUpdatePredictionContext:]_block_invoke
+ ___53-[ULConnection addLabel:betweenStartDate:andEndDate:]_block_invoke
+ ___53-[ULConnection addLabel:betweenStartDate:andEndDate:]_block_invoke.cold.1
+ ___55+[ULConnection(Diagnostic) polarisDebugWithTask:reply:]_block_invoke
+ ___55+[ULConnection(Diagnostic) polarisDebugWithTask:reply:]_block_invoke_2
+ ___55+[ULConnection(Diagnostic) polarisDebugWithTask:reply:]_block_invoke_2.cold.1
+ ___60+[ULContextLayerUtilities getDefaultContextLayerForService:]_block_invoke
+ ___62+[ULContextLayerUtilities _getContextLayerEnumToStringMapping]_block_invoke
+ ___65+[ULConnection createServiceWithServiceType:locationTypes:reply:]_block_invoke
+ ___65+[ULConnection createServiceWithServiceType:locationTypes:reply:]_block_invoke_2
+ ___65+[ULConnection createServiceWithServiceType:locationTypes:reply:]_block_invoke_2.cold.1
+ ___83+[ULConnection(Diagnostic) imageFeaturesDebugWithTask:additionalInformation:reply:]_block_invoke
+ ___83+[ULConnection(Diagnostic) imageFeaturesDebugWithTask:additionalInformation:reply:]_block_invoke_2
+ ___83+[ULConnection(Diagnostic) imageFeaturesDebugWithTask:additionalInformation:reply:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSUUID"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.161
+ __getContextLayerEnumToStringMapping.contextLayerEnumToStringMap
+ __getContextLayerEnumToStringMapping.onceToken
+ _getDefaultContextLayerForService:.onceToken
+ _getDefaultContextLayerForService:.serviceToDefaultContextLayerMap
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_cosineSimilarity_isSameSpaceForLabel:
+ _objc_msgSend$_extendProbabilityVectorForLabel:toMatchPredictionContext:
+ _objc_msgSend$_geo_isSameSpaceForLabel:
+ _objc_msgSend$_getContextLayerEnumToStringMapping
+ _objc_msgSend$_image_isSameSpaceForLabel:
+ _objc_msgSend$absoluteVerticalDistanceBetweenPredictionCoordinates:andLabelCoordinates:
+ _objc_msgSend$addLabel:
+ _objc_msgSend$addLabel:betweenStartDate:andEndDate:
+ _objc_msgSend$addObject:
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$backwardAzimuthDegrees
+ _objc_msgSend$backwardElevationDegrees
+ _objc_msgSend$configuration
+ _objc_msgSend$connectionDidUpdateMap:
+ _objc_msgSend$connectionDidUpdatePredictionContext:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$contextLayer
+ _objc_msgSend$contextLayerEnumFromStringType:
+ _objc_msgSend$contextLayers
+ _objc_msgSend$coordinates
+ _objc_msgSend$copyWithReplacementContextLayerFromServiceIdentifier:
+ _objc_msgSend$copyWithReplacementPredictionContext:
+ _objc_msgSend$cosineSimilarityBetweenPredictionProbabilities:withPreCalculatedMagnitude:andLabelProbabilities:
+ _objc_msgSend$count
+ _objc_msgSend$createServiceWithServiceType:locationTypes:reply:
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$date
+ _objc_msgSend$deviceClass
+ _objc_msgSend$emptyHomeSlamModelData
+ _objc_msgSend$emptyLocationOfInterest
+ _objc_msgSend$emptyMap
+ _objc_msgSend$emptyPredictionContext
+ _objc_msgSend$emptyServiceMetaInfo
+ _objc_msgSend$firstObject
+ _objc_msgSend$floatValue
+ _objc_msgSend$forwardAzimuthDegrees
+ _objc_msgSend$forwardElevationDegrees
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getDefaultContextLayerForService:
+ _objc_msgSend$homeSlamModelData
+ _objc_msgSend$horizontalDistanceSquaredBetweenPredictionCoordinates:andLabelCoordinates:
+ _objc_msgSend$imageFeaturesDebugWithTask:additionalInformation:reply:
+ _objc_msgSend$imageIdentifiersVector
+ _objc_msgSend$initWithContextLayers:
+ _objc_msgSend$initWithLocationOfInterestType:locationOfInterestUUID:
+ _objc_msgSend$initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:homeSlamModelData:
+ _objc_msgSend$initWithMapPoint:forwardAzimuth:forwardElevation:backwardAzimuth:backwardElevation:
+ _objc_msgSend$initWithMapPoints:roomIndex:
+ _objc_msgSend$initWithMapROIs:trajectoryPoints:numInputSegments:
+ _objc_msgSend$initWithName:labels:mapItemType:
+ _objc_msgSend$initWithName:rssi:timestamp:coordinates:probabilityVector:imageIdentifiersVector:
+ _objc_msgSend$initWithName:timestamp:contextLayer:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:
+ _objc_msgSend$initWithNumWiFiAccessPoints:numBLESources:numUWBSources:requestIdentifier:
+ _objc_msgSend$initWithUniqueIdentifier:timestamp:isMotionDetected:coordinates:probabilityVector:imageIdentifiersVector:particles:
+ _objc_msgSend$initWithX:Y:Z:
+ _objc_msgSend$integerValue
+ _objc_msgSend$internalMap
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isMapValid
+ _objc_msgSend$isMotionDetected
+ _objc_msgSend$isPredictionValid
+ _objc_msgSend$keyForObject:
+ _objc_msgSend$labels
+ _objc_msgSend$labelsInSameSpaceForMapItem:
+ _objc_msgSend$locationOfInterest
+ _objc_msgSend$locationOfInterestType
+ _objc_msgSend$locationOfInterestUUID
+ _objc_msgSend$magnitudeOfVector:
+ _objc_msgSend$mapItemType
+ _objc_msgSend$mapItems
+ _objc_msgSend$mapPoint
+ _objc_msgSend$mapPoints
+ _objc_msgSend$mapROIs
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$now
+ _objc_msgSend$numberOfInputSegments
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$particles
+ _objc_msgSend$polarisDebugWithTask:reply:
+ _objc_msgSend$predictionContext
+ _objc_msgSend$predictionsUpdateType
+ _objc_msgSend$probabilityVector
+ _objc_msgSend$roomIndex
+ _objc_msgSend$rssi
+ _objc_msgSend$runWithConfiguration:
+ _objc_msgSend$runWithConfiguration:serviceIdentifier:legacyServiceIdentifier:andRequestIdentifier:
+ _objc_msgSend$set
+ _objc_msgSend$setBackwardAzimuthDegrees:
+ _objc_msgSend$setBackwardElevationDegrees:
+ _objc_msgSend$setConfiguration:
+ _objc_msgSend$setContextLayer:
+ _objc_msgSend$setContextLayers:
+ _objc_msgSend$setCoordinates:
+ _objc_msgSend$setDeviceClass:
+ _objc_msgSend$setForwardAzimuthDegrees:
+ _objc_msgSend$setForwardElevationDegrees:
+ _objc_msgSend$setHomeSlamModelData:
+ _objc_msgSend$setImageIdentifiersVector:
+ _objc_msgSend$setInternalMap:
+ _objc_msgSend$setIsMapValid:
+ _objc_msgSend$setIsMotionDetected:
+ _objc_msgSend$setLabels:
+ _objc_msgSend$setLocationOfInterest:
+ _objc_msgSend$setLocationOfInterestType:
+ _objc_msgSend$setLocationOfInterestUUID:
+ _objc_msgSend$setMapItemType:
+ _objc_msgSend$setMapItems:
+ _objc_msgSend$setMapPoint:
+ _objc_msgSend$setMapPoints:
+ _objc_msgSend$setMapROIs:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNumberOfInputSegments:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setParticles:
+ _objc_msgSend$setPredictionContext:
+ _objc_msgSend$setPredictionsUpdateType:
+ _objc_msgSend$setProbabilityVector:
+ _objc_msgSend$setRoomIndex:
+ _objc_msgSend$setRssi:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$setTrajectoryPoints:
+ _objc_msgSend$setUniqueIdentifier:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$setX:
+ _objc_msgSend$setY:
+ _objc_msgSend$setZ:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$sumOfVector:
+ _objc_msgSend$timestamp
+ _objc_msgSend$trajectoryPoints
+ _objc_msgSend$ul_cachedInstanceForNSString:
+ _objc_msgSend$ul_decodeAndCacheNSStringForKey:
+ _objc_msgSend$ul_decodeVector3ForKey:
+ _objc_msgSend$ul_encodeVector3:forKey:
+ _objc_msgSend$uniqueIdentifier
+ _objc_msgSend$x
+ _objc_msgSend$y
+ _objc_msgSend$z
+ _objc_retain
+ _objc_retain_x4
+ _objc_setProperty_nonatomic_copy
- +[ULFingerprintError new]
- +[ULFingerprintError supportsSecureCoding]
- -[ULConnection didUpdatePrediction:]
- -[ULConnection didUpdateServiceStatus:]
- -[ULConnection labelRequestIdentifier:withPlaceIdentifier:]
- -[ULConnection serviceStatus]
- -[ULConnection setServiceStatus:]
- -[ULConnection setUpdateConfiguration:]
- -[ULConnection updateConfiguration]
- -[ULFingerprintError copyWithZone:]
- -[ULFingerprintError description]
- -[ULFingerprintError encodeWithCoder:]
- -[ULFingerprintError fingerprintErrorEnum]
- -[ULFingerprintError hash]
- -[ULFingerprintError initWithCoder:]
- -[ULFingerprintError initWithFingerprintErrorEnum:]
- -[ULFingerprintError init]
- -[ULFingerprintError isEqual:]
- -[ULFingerprintError setFingerprintErrorEnum:]
- -[ULFingerprintMetaInfo errors]
- -[ULFingerprintMetaInfo initWithNumWiFiAccessPoints:numBLESources:numUWBSources:requestIdentifier:errors:]
- -[ULFingerprintMetaInfo setErrors:]
- -[ULPlace description]
- -[ULPlace hash]
- -[ULPlace initWithIdentifier:score:]
- -[ULPlace isEqual:]
- -[ULPlace setIdentifier:]
- -[ULPlace setScore:]
- -[ULPrediction description]
- -[ULPrediction hash]
- -[ULPrediction initWithPlaces:error:requestIdentifier:time:confidence:confidenceReasons:]
- -[ULPrediction isEqual:]
- -[ULPrediction setConfidence:]
- -[ULPrediction setConfidenceReasons:]
- -[ULPrediction setError:]
- -[ULPrediction setPlaces:]
- -[ULPrediction setRequestIdentifier:]
- -[ULPrediction setTime:]
- -[ULServiceStatus description]
- -[ULServiceStatus hash]
- -[ULServiceStatus initWithServiceState:serviceSuspendReasons:serviceDescriptor:currentLocationOfInterestUuid:currentLocationOfInterestType:error:serviceQualityInfo:metaInfo:]
- -[ULServiceStatus isEqual:]
- -[ULServiceStatus setCurrentLocationOfInterestType:]
- -[ULServiceStatus setCurrentLocationOfInterestUuid:]
- -[ULServiceStatus setError:]
- -[ULServiceStatus setMetaInfo:]
- -[ULServiceStatus setServiceDescriptor:]
- -[ULServiceStatus setServiceQualityInfo:]
- -[ULServiceStatus setServiceState:]
- -[ULServiceStatus setServiceSuspendReasons:]
- -[ULServiceStatus updateServiceState:]
- -[ULServiceStatus updateServiceSuspendReasons:]
- GCC_except_table106
- GCC_except_table11
- GCC_except_table15
- GCC_except_table17
- GCC_except_table19
- GCC_except_table21
- GCC_except_table23
- GCC_except_table25
- GCC_except_table52
- GCC_except_table87
- _NSLocalizedDescriptionKey
- _OBJC_CLASS_$_ULFingerprintError
- _OBJC_IVAR_$_ULConnection._serviceStatus
- _OBJC_IVAR_$_ULConnection._updateConfiguration
- _OBJC_IVAR_$_ULFingerprintError._fingerprintErrorEnum
- _OBJC_IVAR_$_ULFingerprintMetaInfo._errors
- _OBJC_METACLASS_$_ULFingerprintError
- __OBJC_$_CLASS_METHODS_ULFingerprintError
- __OBJC_$_CLASS_PROP_LIST_ULFingerprintError
- __OBJC_$_INSTANCE_METHODS_ULFingerprintError
- __OBJC_$_INSTANCE_VARIABLES_ULFingerprintError
- __OBJC_$_PROP_LIST_ULFingerprintError
- __OBJC_CLASS_PROTOCOLS_$_ULFingerprintError
- __OBJC_CLASS_RO_$_ULFingerprintError
- __OBJC_METACLASS_RO_$_ULFingerprintError
- ___109+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:]_block_invoke
- ___109+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:]_block_invoke_2
- ___109+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:]_block_invoke_2.cold.1
- ___138+[ULConnection(Legacy) getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:]_block_invoke_2
- ___138+[ULConnection(Legacy) getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:]_block_invoke_2.cold.1
- ___23-[ULConnection connect]_block_invoke
- ___23-[ULConnection connect]_block_invoke.cold.1
- ___28-[ULConnection stopUpdating]_block_invoke
- ___28-[ULConnection stopUpdating]_block_invoke.cold.1
- ___36-[ULConnection didUpdatePrediction:]_block_invoke
- ___39-[ULConnection didUpdateServiceStatus:]_block_invoke
- ___47-[ULConnection startUpdatingWithConfiguration:]_block_invoke
- ___47-[ULConnection startUpdatingWithConfiguration:]_block_invoke.cold.1
- ___59-[ULConnection labelRequestIdentifier:withPlaceIdentifier:]_block_invoke
- ___59-[ULConnection labelRequestIdentifier:withPlaceIdentifier:]_block_invoke.cold.1
- ___98+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:]_block_invoke
- ___98+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:]_block_invoke_2
- ___98+[ULConnection(Legacy) donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:]_block_invoke_2.cold.1
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_57_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
- _objc_msgSend$compare:
- _objc_msgSend$confidence
- _objc_msgSend$confidenceReasons
- _objc_msgSend$connectWithServiceIdentifier:legacyServiceIdentifier:andRequestIdentifier:
- _objc_msgSend$connection:didUpdatePrediction:
- _objc_msgSend$connection:didUpdateServiceStatus:
- _objc_msgSend$currentLocationOfInterestType
- _objc_msgSend$currentLocationOfInterestUuid
- _objc_msgSend$didUpdateServiceStatus:
- _objc_msgSend$donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:
- _objc_msgSend$donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:
- _objc_msgSend$error
- _objc_msgSend$errors
- _objc_msgSend$fingerprintErrorEnum
- _objc_msgSend$getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:
- _objc_msgSend$identifier
- _objc_msgSend$initWithDomain:code:userInfo:
- _objc_msgSend$initWithFingerprintErrorEnum:
- _objc_msgSend$initWithIdentifier:score:
- _objc_msgSend$initWithNumWiFiAccessPoints:numBLESources:numUWBSources:requestIdentifier:errors:
- _objc_msgSend$initWithPlaces:error:requestIdentifier:time:confidence:confidenceReasons:
- _objc_msgSend$initWithServiceState:serviceSuspendReasons:serviceDescriptor:currentLocationOfInterestUuid:currentLocationOfInterestType:error:serviceQualityInfo:metaInfo:
- _objc_msgSend$labelRequestIdentifier:withPlaceIdentifier:withReturnIdentifier:
- _objc_msgSend$places
- _objc_msgSend$score
- _objc_msgSend$serviceDescriptor
- _objc_msgSend$serviceQualityInfo
- _objc_msgSend$serviceStatus
- _objc_msgSend$setConfidence:
- _objc_msgSend$setConfidenceReasons:
- _objc_msgSend$setCurrentLocationOfInterestType:
- _objc_msgSend$setCurrentLocationOfInterestUuid:
- _objc_msgSend$setError:
- _objc_msgSend$setFingerprintErrorEnum:
- _objc_msgSend$setIdentifier:
- _objc_msgSend$setPlaces:
- _objc_msgSend$setRequestIdentifier:
- _objc_msgSend$setScore:
- _objc_msgSend$setServiceDescriptor:
- _objc_msgSend$setServiceQualityInfo:
- _objc_msgSend$setServiceStatus:
- _objc_msgSend$setTime:
- _objc_msgSend$setUpdateConfiguration:
- _objc_msgSend$startUpdatingWithConfiguration:withRequestIdentifier:
- _objc_msgSend$stopUpdatingWithRequestIdentifier:
- _objc_msgSend$time
- _objc_msgSend$updateConfiguration
- _objc_msgSend$updateServiceState:
- _objc_msgSend$updateServiceSuspendReasons:
CStrings:
+ "!"
+ "%@, rssi: %@"
+ "%@: "
+ "+[ULConfiguration new]"
+ "+[ULHomeSlamModelData new]"
+ "+[ULMapPoint new]"
+ "+[ULMapROI new]"
+ "+[ULMapTrajectoryPoint new]"
+ ", backwardAzimuthDegrees: %f"
+ ", backwardElevationDegrees: %f"
+ ", contextLayer: %@"
+ ", contextLayers: %@"
+ ", coordinates: (%@, %@, %@)"
+ ", deviceClass: %@"
+ ", forwardAzimuthDegrees: %f"
+ ", forwardElevationDegrees: %f"
+ ", homeSlamModelData: %@"
+ ", imageIdentifiersVector: %@"
+ ", isMapValid: %@"
+ ", isMotionDetected: %@"
+ ", isPredictionValid: %@"
+ ", labels: %@"
+ ", locationOfInterest: %@"
+ ", locationOfInterestType: %@"
+ ", locationOfInterestUUID: %@"
+ ", mapItemType: %@"
+ ", mapItems: %@"
+ ", mapPoint: %@"
+ ", mapPoints: %@"
+ ", mapROIs: %@"
+ ", name: %@"
+ ", numberOfInputSegments: %@"
+ ", particles: %@"
+ ", predictionContext: %@"
+ ", predictionsUpdateType: %@"
+ ", probabilityVector: %@"
+ ", roomIndex: %@"
+ ", timestamp: %@"
+ ", trajectoryPoints: %@"
+ ", uniqueIdentifier: %@"
+ ", x: %f"
+ ", y: %f"
+ ", z: %f"
+ "-[ULConfiguration init]"
+ "-[ULHomeSlamModelData init]"
+ "-[ULMapPoint init]"
+ "-[ULMapROI init]"
+ "-[ULMapTrajectoryPoint init]"
+ "00000000-0000-0000-0000-000000000017"
+ "00000000-0000-0000-0000-000000000022"
+ "00000000-0000-0000-0000-000000000023"
+ "00000000-0000-0000-0000-000000000024"
+ "00000000-0000-0000-0000-000000000025"
+ "16@0:8"
+ "24@0:8@16"
+ "@\"NSSet\""
+ "@\"NSString\""
+ "@\"ULConfiguration\""
+ "@\"ULHomeSlamModelData\""
+ "@\"ULLocationOfInterest\""
+ "@\"ULMap\""
+ "@\"ULMapPoint\""
+ "@\"ULPredictionContext\""
+ "@28@0:8f16f20f24"
+ "@32@0:8@16q24"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16@24Q32"
+ "@40@0:8@16f24f28f32f36"
+ "@48@0:8@16@24@32@40"
+ "@72@0:8@16q24@3240@56@64"
+ "@76@0:8@16@24@32Q40@48B56@60@68"
+ "@76@0:8@16@24B3236@52@60@68"
+ "@80@0:8@16@24@32Q4048@64@72"
+ "AirPods"
+ "B32@0:8@16@24"
+ "Creating a service"
+ "Creating service, identifier: %@, error:%@"
+ "HighLatency"
+ "Image features debug response, error:%@"
+ "LearningInProgress"
+ "LocationServicesDisabled"
+ "LowLatency"
+ "Main"
+ "PlatformNotSupported"
+ "Q24@0:8@16"
+ "Recovering: internalMap: %@, configuration: %@"
+ "SignificantLocationsDisabled"
+ "Suspend"
+ "T,N,V_coordinates"
+ "T@\"NSArray\",&,N,V_imageIdentifiersVector"
+ "T@\"NSArray\",&,N,V_labels"
+ "T@\"NSArray\",&,N,V_mapItems"
+ "T@\"NSArray\",&,N,V_mapPoints"
+ "T@\"NSArray\",&,N,V_mapROIs"
+ "T@\"NSArray\",&,N,V_particles"
+ "T@\"NSArray\",&,N,V_probabilityVector"
+ "T@\"NSArray\",&,N,V_trajectoryPoints"
+ "T@\"NSArray\",R,N,V_confidenceReasons"
+ "T@\"NSArray\",R,N,V_places"
+ "T@\"NSArray\",R,N,V_serviceSuspendReasons"
+ "T@\"NSDate\",&,N,V_timestamp"
+ "T@\"NSDate\",R,N,V_time"
+ "T@\"NSError\",R,N,V_error"
+ "T@\"NSNumber\",&,N,V_numberOfInputSegments"
+ "T@\"NSNumber\",&,N,V_roomIndex"
+ "T@\"NSNumber\",R,N,V_score"
+ "T@\"NSSet\",&,N,V_contextLayers"
+ "T@\"NSString\",&,N,V_contextLayer"
+ "T@\"NSString\",&,N,V_mapItemType"
+ "T@\"NSString\",&,N,V_name"
+ "T@\"NSUUID\",&,N,V_locationOfInterestUUID"
+ "T@\"NSUUID\",&,N,V_uniqueIdentifier"
+ "T@\"NSUUID\",R,N,V_currentLocationOfInterestUuid"
+ "T@\"NSUUID\",R,N,V_identifier"
+ "T@\"NSUUID\",R,N,V_requestIdentifier"
+ "T@\"ULConfiguration\",C,N,V_configuration"
+ "T@\"ULHomeSlamModelData\",&,N,V_homeSlamModelData"
+ "T@\"ULLocationOfInterest\",&,N,V_locationOfInterest"
+ "T@\"ULLocationType\",R,N,V_currentLocationOfInterestType"
+ "T@\"ULMap\",&,N,V_internalMap"
+ "T@\"ULMap\",R,C,N"
+ "T@\"ULMapPoint\",&,N,V_mapPoint"
+ "T@\"ULPredictionContext\",&,N,V_predictionContext"
+ "T@\"ULServiceDescriptor\",R,N,V_serviceDescriptor"
+ "T@\"ULServiceMetaInfo\",R,N,V_metaInfo"
+ "T@\"ULServiceQualityInfo\",R,N,V_serviceQualityInfo"
+ "TB,N,V_isMapValid"
+ "TB,N,V_isMotionDetected"
+ "TB,R,N"
+ "TQ,N,V_deviceClass"
+ "TQ,N,V_locationOfInterestType"
+ "TQ,N,V_predictionsUpdateType"
+ "TQ,R,N,V_confidence"
+ "TQ,R,N,V_serviceState"
+ "Testing"
+ "Tf,N,V_backwardAzimuthDegrees"
+ "Tf,N,V_backwardElevationDegrees"
+ "Tf,N,V_forwardAzimuthDegrees"
+ "Tf,N,V_forwardElevationDegrees"
+ "Tf,N,V_x"
+ "Tf,N,V_y"
+ "Tf,N,V_z"
+ "Tq,N,V_rssi"
+ "ULConfiguration"
+ "ULConfiguration.m"
+ "ULContextLayerTypeDataCollectionApp"
+ "ULContextLayerTypeFocusMode"
+ "ULContextLayerTypeHomeSlamApp"
+ "ULContextLayerTypeIRAppleTVControl"
+ "ULContextLayerTypeIRControlCenter"
+ "ULContextLayerTypeIRHome"
+ "ULContextLayerTypeIRHostTestsAppleTVControl"
+ "ULContextLayerTypeIRHostTestsHome"
+ "ULContextLayerTypeIRHostTestsMedia"
+ "ULContextLayerTypeIRMedia"
+ "ULContextLayerTypeIRMediaRemote"
+ "ULContextLayerTypeIRMusic"
+ "ULContextLayerTypeIRNeighborhoodActivity"
+ "ULContextLayerTypeIRRoutePickerView"
+ "ULContextLayerTypeIRRoverApp"
+ "ULContextLayerTypeIRTVRemote"
+ "ULContextLayerTypeIRTelephonyUtilities"
+ "ULContextLayerTypeLslApp"
+ "ULContextLayerTypeMiLoDebug"
+ "ULContextLayerTypeMiLoHostTests"
+ "ULContextLayerTypeMiLoPlaceholderApp"
+ "ULContextLayerTypeRoomClass"
+ "ULContextLayerTypeUnknown"
+ "ULContextLayerTypeWiFi"
+ "ULContextLayerUtilities"
+ "ULHomeSlamModelData"
+ "ULLabel"
+ "ULLabelWiFi"
+ "ULLocationOfInterest"
+ "ULMap"
+ "ULMapItem"
+ "ULMapItemTypeClientGenerated"
+ "ULMapItemTypeMiLoGenerated"
+ "ULMapPoint"
+ "ULMapROI"
+ "ULMapTrajectoryPoint"
+ "ULPredictionContext"
+ "ULServiceSuspendReasonAirplaneMode"
+ "UUIDString"
+ "[%@] invalid signing identity: %@"
+ "[DEPRECATED][DoNothing] received recording scan request"
+ "[DEPRECATED][DoNothing] received truth label donation request between Dates"
+ "[DEPRECATED][DoNothing] received truth label donation request for a recording trigger"
+ "[ULMap]: _cosineSimilarity_isSameSpaceForLabel: labelName: %@, labelProbabilityVector: %@, predictionContextProbabilityVector: %@, cosineSimilarity: %@"
+ "_backwardAzimuthDegrees"
+ "_backwardElevationDegrees"
+ "_configuration"
+ "_contextLayer"
+ "_contextLayers"
+ "_coordinates"
+ "_cosineSimilarity_isSameSpaceForLabel:"
+ "_deviceClass"
+ "_extendProbabilityVectorForLabel:toMatchPredictionContext:"
+ "_forwardAzimuthDegrees"
+ "_forwardElevationDegrees"
+ "_geo_isSameSpaceForLabel:"
+ "_getContextLayerEnumToStringMapping"
+ "_homeSlamModelData"
+ "_imageIdentifiersVector"
+ "_image_isSameSpaceForLabel:"
+ "_internalMap"
+ "_isMapValid"
+ "_isMotionDetected"
+ "_labels"
+ "_locationOfInterest"
+ "_locationOfInterestType"
+ "_locationOfInterestUUID"
+ "_mapItemType"
+ "_mapItems"
+ "_mapPoint"
+ "_mapPoints"
+ "_mapROIs"
+ "_name"
+ "_numberOfInputSegments"
+ "_particles"
+ "_predictionContext"
+ "_predictionsUpdateType"
+ "_probabilityVector"
+ "_roomIndex"
+ "_rssi"
+ "_timestamp"
+ "_trajectoryPoints"
+ "_uniqueIdentifier"
+ "_verifyInput:"
+ "_verifyInput:labels:"
+ "_x"
+ "_y"
+ "_z"
+ "absoluteVerticalDistanceBetweenPredictionCoordinates:andLabelCoordinates:"
+ "addLabel with name: %@ contextLayer: %@ between dates: %@ - %@"
+ "addLabel with name: %@ to contextLayer: %@ to device: %@"
+ "addLabel:"
+ "addLabel:betweenStartDate:andEndDate:"
+ "addObject:"
+ "array"
+ "arrayByAddingObject:"
+ "averageRSSIOfSameSpaceLabelsForMapItem:"
+ "backwardAzimuthDegrees"
+ "backwardElevationDegrees"
+ "com.apple.HomeSlam"
+ "com.apple.IntelligentRoutingHostTests.xctrunner.AppleTVControl"
+ "com.apple.IntelligentRoutingHostTests.xctrunner.Home"
+ "com.apple.IntelligentRoutingHostTests.xctrunner.Media"
+ "com.apple.MiLoLSL2"
+ "com.apple.MicroLocation.createServiceWithServiceType"
+ "com.apple.MicroLocation.imageFeaturesDebug"
+ "com.apple.MicroLocation.polarisDebug"
+ "com.apple.contextstored"
+ "com.apple.intelligentroutingclient.Home"
+ "com.apple.proactive.ProactiveContextClient"
+ "com.vpg.Rover"
+ "configuration"
+ "connectionDidUpdateMap:"
+ "connectionDidUpdatePredictionContext:"
+ "containsObject:"
+ "contextLayer"
+ "contextLayerEnum"
+ "contextLayerEnumFromStringType:"
+ "contextLayerStringTypeFromEnum:"
+ "contextLayers"
+ "coordinates"
+ "copyWithReplacementContextLayerFromServiceIdentifier:"
+ "copyWithReplacementPredictionContext:"
+ "cosineSimilarityBetweenPredictionProbabilities:withPreCalculatedMagnitude:andLabelProbabilities:"
+ "count"
+ "currentMap"
+ "dataWithBytes:length:"
+ "date"
+ "deviceClass"
+ "didUpdateMap:"
+ "didUpdatePredictionContext:"
+ "emptyHomeSlamModelData"
+ "emptyLocationOfInterest"
+ "emptyMap"
+ "emptyPredictionContext"
+ "emptyServiceMetaInfo"
+ "f"
+ "f16@0:8"
+ "firstObject"
+ "floatValue"
+ "forwardAzimuthDegrees"
+ "forwardElevationDegrees"
+ "getBytes:length:"
+ "getDefaultContextLayerForService:"
+ "homeSlamModelData"
+ "horizontalDistanceSquaredBetweenPredictionCoordinates:andLabelCoordinates:"
+ "i"
+ "imageFeaturesDebug"
+ "imageFeaturesDebugWithTask:additionalInformation:reply:"
+ "imageIdentifiersVector"
+ "initWithContextLayers:"
+ "initWithLocationOfInterestType:locationOfInterestUUID:"
+ "initWithMapItems:predictionContext:locationOfInterest:serviceState:serviceSuspendReasons:isMapValid:metaInfo:homeSlamModelData:"
+ "initWithMapPoint:forwardAzimuth:forwardElevation:backwardAzimuth:backwardElevation:"
+ "initWithMapPoints:roomIndex:"
+ "initWithMapROIs:trajectoryPoints:numInputSegments:"
+ "initWithName:"
+ "initWithName:andContextLayerType:"
+ "initWithName:contextLayerType:andDeviceClass:"
+ "initWithName:labels:mapItemType:"
+ "initWithName:rssi:"
+ "initWithName:rssi:timestamp:coordinates:probabilityVector:imageIdentifiersVector:"
+ "initWithName:timestamp:contextLayer:deviceClass:coordinates:probabilityVector:imageIdentifiersVector:"
+ "initWithNumWiFiAccessPoints:numBLESources:numUWBSources:requestIdentifier:"
+ "initWithUniqueIdentifier:timestamp:isMotionDetected:coordinates:probabilityVector:imageIdentifiersVector:particles:"
+ "initWithX:Y:Z:"
+ "integerValue"
+ "internalMap"
+ "intersectsSet:"
+ "isEqualToString:"
+ "isMapValid"
+ "isMotionDetected"
+ "isPredictionValid"
+ "keyForObject:"
+ "labels"
+ "labelsInSameSpaceForMapItem:"
+ "locationOfInterest"
+ "locationOfInterestType"
+ "locationOfInterestUUID"
+ "magnitudeOfVector:"
+ "mapItemType"
+ "mapItems"
+ "mapPoint"
+ "mapPoints"
+ "mapROIs"
+ "mutableCopy"
+ "name"
+ "none"
+ "now"
+ "numberOfInputSegments"
+ "numberOfLabelsInSameSpaceForMapItem:"
+ "numberWithDouble:"
+ "numberWithFloat:"
+ "numberWithInteger:"
+ "particles"
+ "polaris debug response, error:%@"
+ "polarisDebug. task: %@"
+ "polarisDebugWithTask:reply:"
+ "predictionContext"
+ "predictionsUpdateType"
+ "probabilityVector"
+ "q"
+ "q16@0:8"
+ "q24@0:8@16"
+ "roomIndex"
+ "rssi"
+ "runWithConfiguration"
+ "runWithConfiguration:"
+ "runWithConfiguration:serviceIdentifier:legacyServiceIdentifier:andRequestIdentifier:"
+ "set"
+ "setBackwardAzimuthDegrees:"
+ "setBackwardElevationDegrees:"
+ "setConfiguration:"
+ "setContextLayer:"
+ "setContextLayers:"
+ "setCoordinates:"
+ "setCoordinatesForTesting:"
+ "setDeviceClass:"
+ "setForwardAzimuthDegrees:"
+ "setForwardElevationDegrees:"
+ "setHomeSlamModelData:"
+ "setImageIdentifiersVector:"
+ "setInternalMap:"
+ "setIsMapValid:"
+ "setIsMotionDetected:"
+ "setLabels:"
+ "setLocationOfInterest:"
+ "setLocationOfInterestType:"
+ "setLocationOfInterestUUID:"
+ "setMapItemType:"
+ "setMapItems:"
+ "setMapPoint:"
+ "setMapPoints:"
+ "setMapROIs:"
+ "setName:"
+ "setNumberOfInputSegments:"
+ "setObject:forKey:"
+ "setParticles:"
+ "setPredictionContext:"
+ "setPredictionsUpdateType:"
+ "setProbabilityVector:"
+ "setRoomIndex:"
+ "setRssi:"
+ "setTimestamp:"
+ "setTrajectoryPoints:"
+ "setUniqueIdentifier:"
+ "setWithObject:"
+ "setX:"
+ "setY:"
+ "setZ:"
+ "setup-graphs"
+ "stringWithFormat:"
+ "sumOfVector:"
+ "teardown-graphs"
+ "timestamp"
+ "trajectoryPoints"
+ "ul_cachedInstanceForNSString:"
+ "ul_decodeAndCacheNSStringForKey:"
+ "ul_decodeVector3ForKey:"
+ "ul_encodeVector3:forKey:"
+ "uniqueIdentifier"
+ "unknown"
+ "v20@0:8f16"
+ "v24@0:8@\"ULLabel\"16"
+ "v24@0:8@\"ULMap\"16"
+ "v24@0:8@\"ULPredictionContext\"16"
+ "v24@0:8q16"
+ "v24@?0@\"NSString\"8@\"NSError\"16"
+ "v24@?0@\"NSUUID\"8@\"NSError\"16"
+ "v32@0:816"
+ "v32@0:8Q16@?24"
+ "v32@0:8Q16@?<v@?@\"NSError\">24"
+ "v40@0:816@32"
+ "v40@0:8@\"ULLabel\"16@\"NSDate\"24@\"NSDate\"32"
+ "v40@0:8Q16@\"NSArray\"24@?<v@?@\"NSString\"@\"NSError\">32"
+ "v40@0:8Q16@\"NSArray\"24@?<v@?@\"NSUUID\"@\"NSError\">32"
+ "v48@0:8@\"ULConfiguration\"16@\"NSUUID\"24@\"NSUUID\"32@\"NSUUID\"40"
+ "v48@0:8@16@24@32@40"
+ "x"
+ "y"
+ "z"
+ "{\"msg%{public}.0s\":\"connect: No context layers provided. Setting default context layer for service\", \"ServiceUUID\":%{public, location:escape_only}s, \"ContextLayer\":%{public, location:escape_only}s}"
- "+[ULFingerprintError new]"
- ", confidence: %@"
- ", confidenceReasons: %@"
- ", currentLocationOfInterestType: %@"
- ", currentLocationOfInterestUuid: %@"
- ", error: %@"
- ", errors: %@"
- ", fingerprintErrorEnum: %@"
- ", identifier: %@"
- ", places: %@"
- ", score: %@"
- ", serviceDescriptor: %@"
- ", serviceQualityInfo: %@"
- ", time: %@"
- "-[ULFingerprintError init]"
- "@\"ULServiceStatus\""
- "@\"ULUpdateConfiguration\""
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32@40Q48@56"
- "@80@0:8Q16@24@32@40@48@56@64@72"
- "Creating a service is not supported, only static tokens are supported"
- "Recovering: serviceStatus: %@, updateConfiguration: %@"
- "T@\"NSArray\",&,N,V_confidenceReasons"
- "T@\"NSArray\",&,N,V_errors"
- "T@\"NSArray\",&,N,V_places"
- "T@\"NSDate\",&,N,V_time"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSNumber\",&,N,V_score"
- "T@\"NSUUID\",&,N,V_currentLocationOfInterestUuid"
- "T@\"NSUUID\",&,N,V_identifier"
- "T@\"ULLocationType\",&,N,V_currentLocationOfInterestType"
- "T@\"ULServiceDescriptor\",&,N,V_serviceDescriptor"
- "T@\"ULServiceQualityInfo\",&,N,V_serviceQualityInfo"
- "T@\"ULServiceStatus\",&,N,V_serviceStatus"
- "T@\"ULUpdateConfiguration\",&,N,V_updateConfiguration"
- "TQ,N,V_confidence"
- "TQ,N,V_fingerprintErrorEnum"
- "ULConnectionDomain"
- "ULFingerprintError"
- "_errors"
- "_fingerprintErrorEnum"
- "_serviceStatus"
- "_updateConfiguration"
- "com.apple.IntelligentRoutingHostTests.xctrunner"
- "com.apple.MiLoLSL"
- "com.apple.MiLoWiFiHeatmap"
- "com.apple.MicroLocation.donateMicroLocationTruthTagWithTagUUID"
- "compare:"
- "connectWithServiceIdentifier:legacyServiceIdentifier:andRequestIdentifier:"
- "connection:didUpdatePrediction:"
- "connection:didUpdateServiceStatus:"
- "didUpdatePrediction:"
- "didUpdateServiceStatus:"
- "donate truth tagUUID between dates, error:%@"
- "donate truth tagUUID with corresponding triggerUUID, error:%@"
- "donateTruthTagLabelForClient failed because startDate is later than endDate"
- "errors"
- "fingerprintErrorEnum"
- "get triggerUUID and request scan, information: %@, shouldForceRecording: %@, success: %@, error: %@"
- "initWithDomain:code:userInfo:"
- "initWithFingerprintErrorEnum:"
- "initWithIdentifier:score:"
- "initWithNumWiFiAccessPoints:numBLESources:numUWBSources:requestIdentifier:errors:"
- "initWithPlaces:error:requestIdentifier:time:confidence:confidenceReasons:"
- "initWithServiceState:serviceSuspendReasons:serviceDescriptor:currentLocationOfInterestUuid:currentLocationOfInterestType:error:serviceQualityInfo:metaInfo:"
- "labelRequestIdentifier: %@, withPlaceIdentifier: %@"
- "labelRequestIdentifier:withPlaceIdentifier:"
- "labelRequestIdentifier:withPlaceIdentifier:withReturnIdentifier:"
- "received recording scan request, forced: %@"
- "received truth label donation request between Dates"
- "received truth label donation request for a recording trigger"
- "serviceStatus"
- "setConfidence:"
- "setConfidenceReasons:"
- "setCurrentLocationOfInterestType:"
- "setCurrentLocationOfInterestUuid:"
- "setError:"
- "setErrors:"
- "setFingerprintErrorEnum:"
- "setIdentifier:"
- "setPlaces:"
- "setScore:"
- "setServiceDescriptor:"
- "setServiceQualityInfo:"
- "setServiceStatus:"
- "setTime:"
- "setUpdateConfiguration:"
- "startUpdatingWithConfiguration:withRequestIdentifier:"
- "stopUpdatingWithRequestIdentifier:"
- "updateConfiguration"
- "updateServiceState:"
- "updateServiceSuspendReasons:"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@\"ULPrediction\"16"
- "v24@0:8@\"ULServiceStatus\"16"
- "v32@0:8@\"ULUpdateConfiguration\"16@\"NSUUID\"24"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSUUID\"32"
- "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@?<v@?@\"NSError\">32"
- "v48@0:8@\"NSUUID\"16@\"NSDate\"24@\"NSDate\"32@?<v@?@\"NSError\">40"

```
