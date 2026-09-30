## CoreLocationProtobuf

> `/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/Versions/A/CoreLocationProtobuf`

```diff

-  __TEXT.__text: 0x8ccfc
-  __TEXT.__objc_methlist: 0xa78c
+  __TEXT.__text: 0x990a0
+  __TEXT.__objc_methlist: 0xb6c4
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x28f9
-  __TEXT.__unwind_info: 0x13c8
+  __TEXT.__cstring: 0x2d20
+  __TEXT.__unwind_info: 0x1590
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5a8
-  __DATA_CONST.__objc_classlist: 0x318
+  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__objc_classlist: 0x378
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3568
-  __DATA_CONST.__objc_superrefs: 0x318
-  __DATA_CONST.__got: 0x2d8
-  __AUTH_CONST.__cfstring: 0x49e0
-  __AUTH_CONST.__objc_const: 0xe330
+  __DATA_CONST.__objc_selrefs: 0x3950
+  __DATA_CONST.__objc_superrefs: 0x378
+  __DATA_CONST.__got: 0x338
+  __AUTH_CONST.__cfstring: 0x5120
+  __AUTH_CONST.__objc_const: 0xfad0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xac4
+  __AUTH.__objc_data: 0x640
+  __DATA.__objc_ivar: 0xbcc
   __DATA.__data: 0x60
-  __DATA_DIRTY.__objc_data: 0x1d10
+  __DATA_DIRTY.__objc_data: 0x1c70
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3608
-  Symbols:   5567
-  CStrings:  1225
+  Functions: 3933
+  Symbols:   6072
+  CStrings:  1341
 
Sections:
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CLPIndoorEvent hasProximityAccessoryMeta]
+ -[CLPIndoorEvent hasProximityAccessoryMotion]
+ -[CLPIndoorEvent hasProximityAlertRaised]
+ -[CLPIndoorEvent hasProximityGPSTile]
+ -[CLPIndoorEvent hasProximityLOI]
+ -[CLPIndoorEvent hasProximityLastVisitLocation]
+ -[CLPIndoorEvent hasProximityMonitoredDeviceCount]
+ -[CLPIndoorEvent hasProximityPOIType]
+ -[CLPIndoorEvent hasProximityRangeMeasurement]
+ -[CLPIndoorEvent hasProximityReunionLocation]
+ -[CLPIndoorEvent hasProximityScanLocation]
+ -[CLPIndoorEvent hasProximityTriggerInfo]
+ -[CLPIndoorEvent hasProximityVIOPose]
+ -[CLPIndoorEvent hasProximityVehicularState]
+ -[CLPIndoorEvent proximityAccessoryMeta]
+ -[CLPIndoorEvent proximityAccessoryMotion]
+ -[CLPIndoorEvent proximityAlertRaised]
+ -[CLPIndoorEvent proximityGPSTile]
+ -[CLPIndoorEvent proximityLOI]
+ -[CLPIndoorEvent proximityLastVisitLocation]
+ -[CLPIndoorEvent proximityMonitoredDeviceCount]
+ -[CLPIndoorEvent proximityPOIType]
+ -[CLPIndoorEvent proximityRangeMeasurement]
+ -[CLPIndoorEvent proximityReunionLocation]
+ -[CLPIndoorEvent proximityScanLocation]
+ -[CLPIndoorEvent proximityTriggerInfo]
+ -[CLPIndoorEvent proximityVIOPose]
+ -[CLPIndoorEvent proximityVehicularState]
+ -[CLPIndoorEvent setProximityAccessoryMeta:]
+ -[CLPIndoorEvent setProximityAccessoryMotion:]
+ -[CLPIndoorEvent setProximityAlertRaised:]
+ -[CLPIndoorEvent setProximityGPSTile:]
+ -[CLPIndoorEvent setProximityLOI:]
+ -[CLPIndoorEvent setProximityLastVisitLocation:]
+ -[CLPIndoorEvent setProximityMonitoredDeviceCount:]
+ -[CLPIndoorEvent setProximityPOIType:]
+ -[CLPIndoorEvent setProximityRangeMeasurement:]
+ -[CLPIndoorEvent setProximityReunionLocation:]
+ -[CLPIndoorEvent setProximityScanLocation:]
+ -[CLPIndoorEvent setProximityTriggerInfo:]
+ -[CLPIndoorEvent setProximityVIOPose:]
+ -[CLPIndoorEvent setProximityVehicularState:]
+ -[CLPInertialOdometry StringAsSource:]
+ -[CLPInertialOdometry hasSource]
+ -[CLPInertialOdometry setHasSource:]
+ -[CLPInertialOdometry setSource:]
+ -[CLPInertialOdometry sourceAsString:]
+ -[CLPInertialOdometry source]
+ -[CLPProximityAccessoryMetaEvent .cxx_destruct]
+ -[CLPProximityAccessoryMetaEvent copyTo:]
+ -[CLPProximityAccessoryMetaEvent copyWithZone:]
+ -[CLPProximityAccessoryMetaEvent description]
+ -[CLPProximityAccessoryMetaEvent dictionaryRepresentation]
+ -[CLPProximityAccessoryMetaEvent hasMake]
+ -[CLPProximityAccessoryMetaEvent hasModel]
+ -[CLPProximityAccessoryMetaEvent hasTimestamp]
+ -[CLPProximityAccessoryMetaEvent hasVersion]
+ -[CLPProximityAccessoryMetaEvent hash]
+ -[CLPProximityAccessoryMetaEvent isEqual:]
+ -[CLPProximityAccessoryMetaEvent make]
+ -[CLPProximityAccessoryMetaEvent mergeFrom:]
+ -[CLPProximityAccessoryMetaEvent model]
+ -[CLPProximityAccessoryMetaEvent readFrom:]
+ -[CLPProximityAccessoryMetaEvent setHasTimestamp:]
+ -[CLPProximityAccessoryMetaEvent setMake:]
+ -[CLPProximityAccessoryMetaEvent setModel:]
+ -[CLPProximityAccessoryMetaEvent setTimestamp:]
+ -[CLPProximityAccessoryMetaEvent setVersion:]
+ -[CLPProximityAccessoryMetaEvent timestamp]
+ -[CLPProximityAccessoryMetaEvent version]
+ -[CLPProximityAccessoryMetaEvent writeTo:]
+ -[CLPProximityAccessoryMotionEvent copyTo:]
+ -[CLPProximityAccessoryMotionEvent copyWithZone:]
+ -[CLPProximityAccessoryMotionEvent description]
+ -[CLPProximityAccessoryMotionEvent dictionaryRepresentation]
+ -[CLPProximityAccessoryMotionEvent hasMotionState]
+ -[CLPProximityAccessoryMotionEvent hasTimestamp]
+ -[CLPProximityAccessoryMotionEvent hash]
+ -[CLPProximityAccessoryMotionEvent isEqual:]
+ -[CLPProximityAccessoryMotionEvent mergeFrom:]
+ -[CLPProximityAccessoryMotionEvent motionState]
+ -[CLPProximityAccessoryMotionEvent readFrom:]
+ -[CLPProximityAccessoryMotionEvent setHasMotionState:]
+ -[CLPProximityAccessoryMotionEvent setHasTimestamp:]
+ -[CLPProximityAccessoryMotionEvent setMotionState:]
+ -[CLPProximityAccessoryMotionEvent setTimestamp:]
+ -[CLPProximityAccessoryMotionEvent timestamp]
+ -[CLPProximityAccessoryMotionEvent writeTo:]
+ -[CLPProximityAlertRaisedEvent alertRaised]
+ -[CLPProximityAlertRaisedEvent copyTo:]
+ -[CLPProximityAlertRaisedEvent copyWithZone:]
+ -[CLPProximityAlertRaisedEvent description]
+ -[CLPProximityAlertRaisedEvent dictionaryRepresentation]
+ -[CLPProximityAlertRaisedEvent hasAlertRaised]
+ -[CLPProximityAlertRaisedEvent hasTimestamp]
+ -[CLPProximityAlertRaisedEvent hash]
+ -[CLPProximityAlertRaisedEvent isEqual:]
+ -[CLPProximityAlertRaisedEvent mergeFrom:]
+ -[CLPProximityAlertRaisedEvent readFrom:]
+ -[CLPProximityAlertRaisedEvent setAlertRaised:]
+ -[CLPProximityAlertRaisedEvent setHasAlertRaised:]
+ -[CLPProximityAlertRaisedEvent setHasTimestamp:]
+ -[CLPProximityAlertRaisedEvent setTimestamp:]
+ -[CLPProximityAlertRaisedEvent timestamp]
+ -[CLPProximityAlertRaisedEvent writeTo:]
+ -[CLPProximityGPSTileEvent copyTo:]
+ -[CLPProximityGPSTileEvent copyWithZone:]
+ -[CLPProximityGPSTileEvent description]
+ -[CLPProximityGPSTileEvent dictionaryRepresentation]
+ -[CLPProximityGPSTileEvent hasTileType]
+ -[CLPProximityGPSTileEvent hasTimestamp]
+ -[CLPProximityGPSTileEvent hash]
+ -[CLPProximityGPSTileEvent isEqual:]
+ -[CLPProximityGPSTileEvent mergeFrom:]
+ -[CLPProximityGPSTileEvent readFrom:]
+ -[CLPProximityGPSTileEvent setHasTileType:]
+ -[CLPProximityGPSTileEvent setHasTimestamp:]
+ -[CLPProximityGPSTileEvent setTileType:]
+ -[CLPProximityGPSTileEvent setTimestamp:]
+ -[CLPProximityGPSTileEvent tileType]
+ -[CLPProximityGPSTileEvent timestamp]
+ -[CLPProximityGPSTileEvent writeTo:]
+ -[CLPProximityLOIEvent copyTo:]
+ -[CLPProximityLOIEvent copyWithZone:]
+ -[CLPProximityLOIEvent description]
+ -[CLPProximityLOIEvent dictionaryRepresentation]
+ -[CLPProximityLOIEvent hasLoiId]
+ -[CLPProximityLOIEvent hasTimestamp]
+ -[CLPProximityLOIEvent hash]
+ -[CLPProximityLOIEvent isEqual:]
+ -[CLPProximityLOIEvent loiId]
+ -[CLPProximityLOIEvent mergeFrom:]
+ -[CLPProximityLOIEvent readFrom:]
+ -[CLPProximityLOIEvent setHasLoiId:]
+ -[CLPProximityLOIEvent setHasTimestamp:]
+ -[CLPProximityLOIEvent setLoiId:]
+ -[CLPProximityLOIEvent setTimestamp:]
+ -[CLPProximityLOIEvent timestamp]
+ -[CLPProximityLOIEvent writeTo:]
+ -[CLPProximityLocationEvent copyTo:]
+ -[CLPProximityLocationEvent copyWithZone:]
+ -[CLPProximityLocationEvent description]
+ -[CLPProximityLocationEvent dictionaryRepresentation]
+ -[CLPProximityLocationEvent hasHorizontalAccuracy]
+ -[CLPProximityLocationEvent hasLatitude]
+ -[CLPProximityLocationEvent hasLongitude]
+ -[CLPProximityLocationEvent hasTimestamp]
+ -[CLPProximityLocationEvent hash]
+ -[CLPProximityLocationEvent horizontalAccuracy]
+ -[CLPProximityLocationEvent isEqual:]
+ -[CLPProximityLocationEvent latitude]
+ -[CLPProximityLocationEvent longitude]
+ -[CLPProximityLocationEvent mergeFrom:]
+ -[CLPProximityLocationEvent readFrom:]
+ -[CLPProximityLocationEvent setHasHorizontalAccuracy:]
+ -[CLPProximityLocationEvent setHasLatitude:]
+ -[CLPProximityLocationEvent setHasLongitude:]
+ -[CLPProximityLocationEvent setHasTimestamp:]
+ -[CLPProximityLocationEvent setHorizontalAccuracy:]
+ -[CLPProximityLocationEvent setLatitude:]
+ -[CLPProximityLocationEvent setLongitude:]
+ -[CLPProximityLocationEvent setTimestamp:]
+ -[CLPProximityLocationEvent timestamp]
+ -[CLPProximityLocationEvent writeTo:]
+ -[CLPProximityMonitoredDeviceCountEvent copyTo:]
+ -[CLPProximityMonitoredDeviceCountEvent copyWithZone:]
+ -[CLPProximityMonitoredDeviceCountEvent count]
+ -[CLPProximityMonitoredDeviceCountEvent description]
+ -[CLPProximityMonitoredDeviceCountEvent dictionaryRepresentation]
+ -[CLPProximityMonitoredDeviceCountEvent hasCount]
+ -[CLPProximityMonitoredDeviceCountEvent hasTimestamp]
+ -[CLPProximityMonitoredDeviceCountEvent hash]
+ -[CLPProximityMonitoredDeviceCountEvent isEqual:]
+ -[CLPProximityMonitoredDeviceCountEvent mergeFrom:]
+ -[CLPProximityMonitoredDeviceCountEvent readFrom:]
+ -[CLPProximityMonitoredDeviceCountEvent setCount:]
+ -[CLPProximityMonitoredDeviceCountEvent setHasCount:]
+ -[CLPProximityMonitoredDeviceCountEvent setHasTimestamp:]
+ -[CLPProximityMonitoredDeviceCountEvent setTimestamp:]
+ -[CLPProximityMonitoredDeviceCountEvent timestamp]
+ -[CLPProximityMonitoredDeviceCountEvent writeTo:]
+ -[CLPProximityPOITypeEvent copyTo:]
+ -[CLPProximityPOITypeEvent copyWithZone:]
+ -[CLPProximityPOITypeEvent description]
+ -[CLPProximityPOITypeEvent dictionaryRepresentation]
+ -[CLPProximityPOITypeEvent hasPoiType]
+ -[CLPProximityPOITypeEvent hasTimestamp]
+ -[CLPProximityPOITypeEvent hash]
+ -[CLPProximityPOITypeEvent isEqual:]
+ -[CLPProximityPOITypeEvent mergeFrom:]
+ -[CLPProximityPOITypeEvent poiType]
+ -[CLPProximityPOITypeEvent readFrom:]
+ -[CLPProximityPOITypeEvent setHasPoiType:]
+ -[CLPProximityPOITypeEvent setHasTimestamp:]
+ -[CLPProximityPOITypeEvent setPoiType:]
+ -[CLPProximityPOITypeEvent setTimestamp:]
+ -[CLPProximityPOITypeEvent timestamp]
+ -[CLPProximityPOITypeEvent writeTo:]
+ -[CLPProximityRangeMeasurementEvent azimuthAngleRad]
+ -[CLPProximityRangeMeasurementEvent copyTo:]
+ -[CLPProximityRangeMeasurementEvent copyWithZone:]
+ -[CLPProximityRangeMeasurementEvent description]
+ -[CLPProximityRangeMeasurementEvent dictionaryRepresentation]
+ -[CLPProximityRangeMeasurementEvent elevationAngleRad]
+ -[CLPProximityRangeMeasurementEvent hasAzimuthAngleRad]
+ -[CLPProximityRangeMeasurementEvent hasElevationAngleRad]
+ -[CLPProximityRangeMeasurementEvent hasMultipathProbability]
+ -[CLPProximityRangeMeasurementEvent hasRangeM]
+ -[CLPProximityRangeMeasurementEvent hasSweepAngleDeg]
+ -[CLPProximityRangeMeasurementEvent hasTechnology]
+ -[CLPProximityRangeMeasurementEvent hasTimestamp]
+ -[CLPProximityRangeMeasurementEvent hasTrackScore]
+ -[CLPProximityRangeMeasurementEvent hash]
+ -[CLPProximityRangeMeasurementEvent isEqual:]
+ -[CLPProximityRangeMeasurementEvent mergeFrom:]
+ -[CLPProximityRangeMeasurementEvent multipathProbability]
+ -[CLPProximityRangeMeasurementEvent rangeM]
+ -[CLPProximityRangeMeasurementEvent readFrom:]
+ -[CLPProximityRangeMeasurementEvent setAzimuthAngleRad:]
+ -[CLPProximityRangeMeasurementEvent setElevationAngleRad:]
+ -[CLPProximityRangeMeasurementEvent setHasAzimuthAngleRad:]
+ -[CLPProximityRangeMeasurementEvent setHasElevationAngleRad:]
+ -[CLPProximityRangeMeasurementEvent setHasMultipathProbability:]
+ -[CLPProximityRangeMeasurementEvent setHasRangeM:]
+ -[CLPProximityRangeMeasurementEvent setHasSweepAngleDeg:]
+ -[CLPProximityRangeMeasurementEvent setHasTechnology:]
+ -[CLPProximityRangeMeasurementEvent setHasTimestamp:]
+ -[CLPProximityRangeMeasurementEvent setHasTrackScore:]
+ -[CLPProximityRangeMeasurementEvent setMultipathProbability:]
+ -[CLPProximityRangeMeasurementEvent setRangeM:]
+ -[CLPProximityRangeMeasurementEvent setSweepAngleDeg:]
+ -[CLPProximityRangeMeasurementEvent setTechnology:]
+ -[CLPProximityRangeMeasurementEvent setTimestamp:]
+ -[CLPProximityRangeMeasurementEvent setTrackScore:]
+ -[CLPProximityRangeMeasurementEvent sweepAngleDeg]
+ -[CLPProximityRangeMeasurementEvent technology]
+ -[CLPProximityRangeMeasurementEvent timestamp]
+ -[CLPProximityRangeMeasurementEvent trackScore]
+ -[CLPProximityRangeMeasurementEvent writeTo:]
+ -[CLPProximityTriggerInfoEvent copyTo:]
+ -[CLPProximityTriggerInfoEvent copyWithZone:]
+ -[CLPProximityTriggerInfoEvent description]
+ -[CLPProximityTriggerInfoEvent dictionaryRepresentation]
+ -[CLPProximityTriggerInfoEvent hasTimestamp]
+ -[CLPProximityTriggerInfoEvent hasTriggerType]
+ -[CLPProximityTriggerInfoEvent hasUseCase]
+ -[CLPProximityTriggerInfoEvent hash]
+ -[CLPProximityTriggerInfoEvent isEqual:]
+ -[CLPProximityTriggerInfoEvent mergeFrom:]
+ -[CLPProximityTriggerInfoEvent readFrom:]
+ -[CLPProximityTriggerInfoEvent setHasTimestamp:]
+ -[CLPProximityTriggerInfoEvent setHasTriggerType:]
+ -[CLPProximityTriggerInfoEvent setHasUseCase:]
+ -[CLPProximityTriggerInfoEvent setTimestamp:]
+ -[CLPProximityTriggerInfoEvent setTriggerType:]
+ -[CLPProximityTriggerInfoEvent setUseCase:]
+ -[CLPProximityTriggerInfoEvent timestamp]
+ -[CLPProximityTriggerInfoEvent triggerType]
+ -[CLPProximityTriggerInfoEvent useCase]
+ -[CLPProximityTriggerInfoEvent writeTo:]
+ -[CLPProximityVIOPoseEvent addPoseMatrix:]
+ -[CLPProximityVIOPoseEvent clearPoseMatrixs]
+ -[CLPProximityVIOPoseEvent copyTo:]
+ -[CLPProximityVIOPoseEvent copyWithZone:]
+ -[CLPProximityVIOPoseEvent dealloc]
+ -[CLPProximityVIOPoseEvent description]
+ -[CLPProximityVIOPoseEvent dictionaryRepresentation]
+ -[CLPProximityVIOPoseEvent hasLightEstimateLumens]
+ -[CLPProximityVIOPoseEvent hasMajorRelocalization]
+ -[CLPProximityVIOPoseEvent hasMinorRelocalization]
+ -[CLPProximityVIOPoseEvent hasTimestamp]
+ -[CLPProximityVIOPoseEvent hasTrackingState]
+ -[CLPProximityVIOPoseEvent hash]
+ -[CLPProximityVIOPoseEvent isEqual:]
+ -[CLPProximityVIOPoseEvent lightEstimateLumens]
+ -[CLPProximityVIOPoseEvent majorRelocalization]
+ -[CLPProximityVIOPoseEvent mergeFrom:]
+ -[CLPProximityVIOPoseEvent minorRelocalization]
+ -[CLPProximityVIOPoseEvent poseMatrixAtIndex:]
+ -[CLPProximityVIOPoseEvent poseMatrixsCount]
+ -[CLPProximityVIOPoseEvent poseMatrixs]
+ -[CLPProximityVIOPoseEvent readFrom:]
+ -[CLPProximityVIOPoseEvent setHasLightEstimateLumens:]
+ -[CLPProximityVIOPoseEvent setHasMajorRelocalization:]
+ -[CLPProximityVIOPoseEvent setHasMinorRelocalization:]
+ -[CLPProximityVIOPoseEvent setHasTimestamp:]
+ -[CLPProximityVIOPoseEvent setHasTrackingState:]
+ -[CLPProximityVIOPoseEvent setLightEstimateLumens:]
+ -[CLPProximityVIOPoseEvent setMajorRelocalization:]
+ -[CLPProximityVIOPoseEvent setMinorRelocalization:]
+ -[CLPProximityVIOPoseEvent setPoseMatrixs:count:]
+ -[CLPProximityVIOPoseEvent setTimestamp:]
+ -[CLPProximityVIOPoseEvent setTrackingState:]
+ -[CLPProximityVIOPoseEvent timestamp]
+ -[CLPProximityVIOPoseEvent trackingState]
+ -[CLPProximityVIOPoseEvent writeTo:]
+ -[CLPProximityVehicularStateEvent copyTo:]
+ -[CLPProximityVehicularStateEvent copyWithZone:]
+ -[CLPProximityVehicularStateEvent description]
+ -[CLPProximityVehicularStateEvent dictionaryRepresentation]
+ -[CLPProximityVehicularStateEvent hasIsVehicular]
+ -[CLPProximityVehicularStateEvent hasTimestamp]
+ -[CLPProximityVehicularStateEvent hash]
+ -[CLPProximityVehicularStateEvent isEqual:]
+ -[CLPProximityVehicularStateEvent isVehicular]
+ -[CLPProximityVehicularStateEvent mergeFrom:]
+ -[CLPProximityVehicularStateEvent readFrom:]
+ -[CLPProximityVehicularStateEvent setHasIsVehicular:]
+ -[CLPProximityVehicularStateEvent setHasTimestamp:]
+ -[CLPProximityVehicularStateEvent setIsVehicular:]
+ -[CLPProximityVehicularStateEvent setTimestamp:]
+ -[CLPProximityVehicularStateEvent timestamp]
+ -[CLPProximityVehicularStateEvent writeTo:]
+ OBJC_IVAR_$_CLPIndoorEvent._proximityAccessoryMeta
+ OBJC_IVAR_$_CLPIndoorEvent._proximityAccessoryMotion
+ OBJC_IVAR_$_CLPIndoorEvent._proximityAlertRaised
+ OBJC_IVAR_$_CLPIndoorEvent._proximityGPSTile
+ OBJC_IVAR_$_CLPIndoorEvent._proximityLOI
+ OBJC_IVAR_$_CLPIndoorEvent._proximityLastVisitLocation
+ OBJC_IVAR_$_CLPIndoorEvent._proximityMonitoredDeviceCount
+ OBJC_IVAR_$_CLPIndoorEvent._proximityPOIType
+ OBJC_IVAR_$_CLPIndoorEvent._proximityRangeMeasurement
+ OBJC_IVAR_$_CLPIndoorEvent._proximityReunionLocation
+ OBJC_IVAR_$_CLPIndoorEvent._proximityScanLocation
+ OBJC_IVAR_$_CLPIndoorEvent._proximityTriggerInfo
+ OBJC_IVAR_$_CLPIndoorEvent._proximityVIOPose
+ OBJC_IVAR_$_CLPIndoorEvent._proximityVehicularState
+ OBJC_IVAR_$_CLPInertialOdometry._source
+ OBJC_IVAR_$_CLPProximityAccessoryMetaEvent._has
+ OBJC_IVAR_$_CLPProximityAccessoryMetaEvent._make
+ OBJC_IVAR_$_CLPProximityAccessoryMetaEvent._model
+ OBJC_IVAR_$_CLPProximityAccessoryMetaEvent._timestamp
+ OBJC_IVAR_$_CLPProximityAccessoryMetaEvent._version
+ OBJC_IVAR_$_CLPProximityAccessoryMotionEvent._has
+ OBJC_IVAR_$_CLPProximityAccessoryMotionEvent._motionState
+ OBJC_IVAR_$_CLPProximityAccessoryMotionEvent._timestamp
+ OBJC_IVAR_$_CLPProximityAlertRaisedEvent._alertRaised
+ OBJC_IVAR_$_CLPProximityAlertRaisedEvent._has
+ OBJC_IVAR_$_CLPProximityAlertRaisedEvent._timestamp
+ OBJC_IVAR_$_CLPProximityGPSTileEvent._has
+ OBJC_IVAR_$_CLPProximityGPSTileEvent._tileType
+ OBJC_IVAR_$_CLPProximityGPSTileEvent._timestamp
+ OBJC_IVAR_$_CLPProximityLOIEvent._has
+ OBJC_IVAR_$_CLPProximityLOIEvent._loiId
+ OBJC_IVAR_$_CLPProximityLOIEvent._timestamp
+ OBJC_IVAR_$_CLPProximityLocationEvent._has
+ OBJC_IVAR_$_CLPProximityLocationEvent._horizontalAccuracy
+ OBJC_IVAR_$_CLPProximityLocationEvent._latitude
+ OBJC_IVAR_$_CLPProximityLocationEvent._longitude
+ OBJC_IVAR_$_CLPProximityLocationEvent._timestamp
+ OBJC_IVAR_$_CLPProximityMonitoredDeviceCountEvent._count
+ OBJC_IVAR_$_CLPProximityMonitoredDeviceCountEvent._has
+ OBJC_IVAR_$_CLPProximityMonitoredDeviceCountEvent._timestamp
+ OBJC_IVAR_$_CLPProximityPOITypeEvent._has
+ OBJC_IVAR_$_CLPProximityPOITypeEvent._poiType
+ OBJC_IVAR_$_CLPProximityPOITypeEvent._timestamp
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._azimuthAngleRad
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._elevationAngleRad
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._has
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._multipathProbability
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._rangeM
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._sweepAngleDeg
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._technology
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._timestamp
+ OBJC_IVAR_$_CLPProximityRangeMeasurementEvent._trackScore
+ OBJC_IVAR_$_CLPProximityTriggerInfoEvent._has
+ OBJC_IVAR_$_CLPProximityTriggerInfoEvent._timestamp
+ OBJC_IVAR_$_CLPProximityTriggerInfoEvent._triggerType
+ OBJC_IVAR_$_CLPProximityTriggerInfoEvent._useCase
+ OBJC_IVAR_$_CLPProximityVIOPoseEvent._has
+ OBJC_IVAR_$_CLPProximityVIOPoseEvent._lightEstimateLumens
+ OBJC_IVAR_$_CLPProximityVIOPoseEvent._majorRelocalization
+ OBJC_IVAR_$_CLPProximityVIOPoseEvent._minorRelocalization
+ OBJC_IVAR_$_CLPProximityVIOPoseEvent._poseMatrixs
+ OBJC_IVAR_$_CLPProximityVIOPoseEvent._timestamp
+ OBJC_IVAR_$_CLPProximityVIOPoseEvent._trackingState
+ OBJC_IVAR_$_CLPProximityVehicularStateEvent._has
+ OBJC_IVAR_$_CLPProximityVehicularStateEvent._isVehicular
+ OBJC_IVAR_$_CLPProximityVehicularStateEvent._timestamp
+ _CLPProximityAccessoryMetaEventReadFrom
+ _CLPProximityAccessoryMotionEventReadFrom
+ _CLPProximityAlertRaisedEventReadFrom
+ _CLPProximityGPSTileEventReadFrom
+ _CLPProximityLOIEventReadFrom
+ _CLPProximityLocationEventReadFrom
+ _CLPProximityMonitoredDeviceCountEventReadFrom
+ _CLPProximityPOITypeEventReadFrom
+ _CLPProximityRangeMeasurementEventReadFrom
+ _CLPProximityTriggerInfoEventReadFrom
+ _CLPProximityVIOPoseEventReadFrom
+ _CLPProximityVehicularStateEventReadFrom
+ _OBJC_CLASS_$_CLPProximityAccessoryMetaEvent
+ _OBJC_CLASS_$_CLPProximityAccessoryMotionEvent
+ _OBJC_CLASS_$_CLPProximityAlertRaisedEvent
+ _OBJC_CLASS_$_CLPProximityGPSTileEvent
+ _OBJC_CLASS_$_CLPProximityLOIEvent
+ _OBJC_CLASS_$_CLPProximityLocationEvent
+ _OBJC_CLASS_$_CLPProximityMonitoredDeviceCountEvent
+ _OBJC_CLASS_$_CLPProximityPOITypeEvent
+ _OBJC_CLASS_$_CLPProximityRangeMeasurementEvent
+ _OBJC_CLASS_$_CLPProximityTriggerInfoEvent
+ _OBJC_CLASS_$_CLPProximityVIOPoseEvent
+ _OBJC_CLASS_$_CLPProximityVehicularStateEvent
+ _OBJC_METACLASS_$_CLPProximityAccessoryMetaEvent
+ _OBJC_METACLASS_$_CLPProximityAccessoryMotionEvent
+ _OBJC_METACLASS_$_CLPProximityAlertRaisedEvent
+ _OBJC_METACLASS_$_CLPProximityGPSTileEvent
+ _OBJC_METACLASS_$_CLPProximityLOIEvent
+ _OBJC_METACLASS_$_CLPProximityLocationEvent
+ _OBJC_METACLASS_$_CLPProximityMonitoredDeviceCountEvent
+ _OBJC_METACLASS_$_CLPProximityPOITypeEvent
+ _OBJC_METACLASS_$_CLPProximityRangeMeasurementEvent
+ _OBJC_METACLASS_$_CLPProximityTriggerInfoEvent
+ _OBJC_METACLASS_$_CLPProximityVIOPoseEvent
+ _OBJC_METACLASS_$_CLPProximityVehicularStateEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityAccessoryMetaEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityAccessoryMotionEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityAlertRaisedEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityGPSTileEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityLOIEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityLocationEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityMonitoredDeviceCountEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityPOITypeEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityRangeMeasurementEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityTriggerInfoEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityVIOPoseEvent
+ __OBJC_$_INSTANCE_METHODS_CLPProximityVehicularStateEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityAccessoryMetaEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityAccessoryMotionEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityAlertRaisedEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityGPSTileEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityLOIEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityLocationEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityMonitoredDeviceCountEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityPOITypeEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityRangeMeasurementEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityTriggerInfoEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityVIOPoseEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPProximityVehicularStateEvent
+ __OBJC_$_PROP_LIST_CLPProximityAccessoryMetaEvent
+ __OBJC_$_PROP_LIST_CLPProximityAccessoryMotionEvent
+ __OBJC_$_PROP_LIST_CLPProximityAlertRaisedEvent
+ __OBJC_$_PROP_LIST_CLPProximityGPSTileEvent
+ __OBJC_$_PROP_LIST_CLPProximityLOIEvent
+ __OBJC_$_PROP_LIST_CLPProximityLocationEvent
+ __OBJC_$_PROP_LIST_CLPProximityMonitoredDeviceCountEvent
+ __OBJC_$_PROP_LIST_CLPProximityPOITypeEvent
+ __OBJC_$_PROP_LIST_CLPProximityRangeMeasurementEvent
+ __OBJC_$_PROP_LIST_CLPProximityTriggerInfoEvent
+ __OBJC_$_PROP_LIST_CLPProximityVIOPoseEvent
+ __OBJC_$_PROP_LIST_CLPProximityVehicularStateEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityAccessoryMetaEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityAccessoryMotionEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityAlertRaisedEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityGPSTileEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityLOIEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityLocationEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityMonitoredDeviceCountEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityPOITypeEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityRangeMeasurementEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityTriggerInfoEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityVIOPoseEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPProximityVehicularStateEvent
+ __OBJC_CLASS_RO_$_CLPProximityAccessoryMetaEvent
+ __OBJC_CLASS_RO_$_CLPProximityAccessoryMotionEvent
+ __OBJC_CLASS_RO_$_CLPProximityAlertRaisedEvent
+ __OBJC_CLASS_RO_$_CLPProximityGPSTileEvent
+ __OBJC_CLASS_RO_$_CLPProximityLOIEvent
+ __OBJC_CLASS_RO_$_CLPProximityLocationEvent
+ __OBJC_CLASS_RO_$_CLPProximityMonitoredDeviceCountEvent
+ __OBJC_CLASS_RO_$_CLPProximityPOITypeEvent
+ __OBJC_CLASS_RO_$_CLPProximityRangeMeasurementEvent
+ __OBJC_CLASS_RO_$_CLPProximityTriggerInfoEvent
+ __OBJC_CLASS_RO_$_CLPProximityVIOPoseEvent
+ __OBJC_CLASS_RO_$_CLPProximityVehicularStateEvent
+ __OBJC_METACLASS_RO_$_CLPProximityAccessoryMetaEvent
+ __OBJC_METACLASS_RO_$_CLPProximityAccessoryMotionEvent
+ __OBJC_METACLASS_RO_$_CLPProximityAlertRaisedEvent
+ __OBJC_METACLASS_RO_$_CLPProximityGPSTileEvent
+ __OBJC_METACLASS_RO_$_CLPProximityLOIEvent
+ __OBJC_METACLASS_RO_$_CLPProximityLocationEvent
+ __OBJC_METACLASS_RO_$_CLPProximityMonitoredDeviceCountEvent
+ __OBJC_METACLASS_RO_$_CLPProximityPOITypeEvent
+ __OBJC_METACLASS_RO_$_CLPProximityRangeMeasurementEvent
+ __OBJC_METACLASS_RO_$_CLPProximityTriggerInfoEvent
+ __OBJC_METACLASS_RO_$_CLPProximityVIOPoseEvent
+ __OBJC_METACLASS_RO_$_CLPProximityVehicularStateEvent
+ _objc_msgSend$addPoseMatrix:
+ _objc_msgSend$clearPoseMatrixs
+ _objc_msgSend$poseMatrixAtIndex:
+ _objc_msgSend$poseMatrixsCount
+ _objc_msgSend$setProximityAccessoryMeta:
+ _objc_msgSend$setProximityAccessoryMotion:
+ _objc_msgSend$setProximityAlertRaised:
+ _objc_msgSend$setProximityGPSTile:
+ _objc_msgSend$setProximityLOI:
+ _objc_msgSend$setProximityLastVisitLocation:
+ _objc_msgSend$setProximityMonitoredDeviceCount:
+ _objc_msgSend$setProximityPOIType:
+ _objc_msgSend$setProximityRangeMeasurement:
+ _objc_msgSend$setProximityReunionLocation:
+ _objc_msgSend$setProximityScanLocation:
+ _objc_msgSend$setProximityTriggerInfo:
+ _objc_msgSend$setProximityVIOPose:
+ _objc_msgSend$setProximityVehicularState:
CStrings:
+ "DEVICE_PDR"
+ "HEADSET"
+ "ItemFindingCollection"
+ "ProximityAccessoryMeta"
+ "ProximityAccessoryMotion"
+ "ProximityAlertRaised"
+ "ProximityGPSTile"
+ "ProximityLOI"
+ "ProximityLastVisitLocation"
+ "ProximityMonitoredDeviceCount"
+ "ProximityPOIType"
+ "ProximityRangeMeasurement"
+ "ProximityReunionLocation"
+ "ProximityScanLocation"
+ "ProximityTriggerInfo"
+ "ProximityVIOPose"
+ "ProximityVehicularState"
+ "SOURCE_UNKNOWN"
+ "SeparationAlertCollection"
+ "TRIGGER_PERIODIC_SCAN"
+ "TRIGGER_USER_FINDING_SESSION"
+ "TRIGGER_VISIT_ENTRY"
+ "TRIGGER_VISIT_EXIT"
+ "alertRaised"
+ "azimuth_angle_rad"
+ "count"
+ "elevation_angle_rad"
+ "isVehicular"
+ "lightEstimateLumens"
+ "loiId"
+ "majorRelocalization"
+ "minorRelocalization"
+ "motionState"
+ "multipath_probability"
+ "poiType"
+ "poseMatrix"
+ "proximityAccessoryMeta"
+ "proximityAccessoryMotion"
+ "proximityAlertRaised"
+ "proximityGPSTile"
+ "proximityLOI"
+ "proximityLastVisitLocation"
+ "proximityMonitoredDeviceCount"
+ "proximityPOIType"
+ "proximityRangeMeasurement"
+ "proximityReunionLocation"
+ "proximityScanLocation"
+ "proximityTriggerInfo"
+ "proximityVIOPose"
+ "proximityVehicularState"
+ "range_m"
+ "source"
+ "sweep_angle_deg"
+ "technology"
+ "tileType"
+ "track_score"
+ "trackingState"
+ "useCase"

```
