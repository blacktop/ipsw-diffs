## Navigation

> `/System/Library/PrivateFrameworks/Navigation.framework/Navigation`

```diff

-2298.31.8.9.6
-  __TEXT.__text: 0xe7864
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0xddb4
+2298.32.9.28.5
+  __TEXT.__text: 0xe91e8
+  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__objc_methlist: 0xdf24
   __TEXT.__const: 0x42c
-  __TEXT.__cstring: 0x12a6c
-  __TEXT.__oslogstring: 0xa953
-  __TEXT.__gcc_except_tab: 0x3ca4
+  __TEXT.__cstring: 0x12ce4
+  __TEXT.__oslogstring: 0xaa38
+  __TEXT.__gcc_except_tab: 0x3d04
   __TEXT.__ustring: 0x290
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__unwind_info: 0x38d8
+  __TEXT.__unwind_info: 0x3910
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x20fa
-  __TEXT.__objc_methname: 0x24bd0
-  __TEXT.__objc_methtype: 0x7abc
-  __TEXT.__objc_stubs: 0x1c460
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x53a8
-  __DATA_CONST.__objc_classlist: 0x6b0
+  __TEXT.__objc_classname: 0x2123
+  __TEXT.__objc_methname: 0x25028
+  __TEXT.__objc_methtype: 0x7ab5
+  __TEXT.__objc_stubs: 0x1c700
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x53f8
+  __DATA_CONST.__objc_classlist: 0x6b8
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x18c18
-  __DATA_CONST.__objc_selrefs: 0x7dc8
+  __DATA_CONST.__objc_const: 0x18ed8
+  __DATA_CONST.__objc_selrefs: 0x7eb8
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__cfstring: 0xbce0
+  __AUTH_CONST.__cfstring: 0xbe60
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__objc_const: 0x5808
+  __AUTH_CONST.__objc_const: 0x5850
   __AUTH_CONST.__const: 0x22a0
   __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__auth_got: 0x8a0
-  __AUTH.__objc_data: 0x1810
+  __AUTH_CONST.__auth_got: 0x8a8
+  __AUTH.__objc_data: 0x1860
   __DATA.__objc_protorefs: 0xb8
-  __DATA.__objc_classrefs: 0xbf0
+  __DATA.__objc_classrefs: 0xc00
   __DATA.__objc_superrefs: 0x490
-  __DATA.__objc_ivar: 0x1158
+  __DATA.__objc_ivar: 0x118c
   __DATA.__data: 0x2570
   __DATA.__common: 0x50
   __DATA.__bss: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 5470
-  Symbols:   19471
-  CStrings:  9812
+  Functions: 5506
+  Symbols:   19588
+  CStrings:  9879
 
Symbols:
+ +[MNFilePaths _validFilenameForTraceName:]
+ +[MNFilePaths routePreviewTraceExtension]
+ +[MNFilePaths tracePathForTraceName:extension:]
+ -[GEOArrivalParameters(MNExtras) containsCoordinate:arrivalRegionType:]
+ -[GEOArrivalParameters(MNExtras) containsLocation:arrivalRegionType:]
+ -[GEOArrivalParameters(MNExtras) containsLocation:arrivalRegionType:parameters:]
+ -[GEOArrivalParameters(MNExtras) regionContainmentTypeForLocation:arrivalRegionType:parameters:]
+ -[GEOComposedWaypoint(MNExtras) _spokenPlaceName]
+ -[MNArrivalRegionContainmentParameters excludeDistancePadding]
+ -[MNArrivalRegionContainmentParameters includeDistancePadding]
+ -[MNArrivalRegionContainmentParameters setExcludeDistancePadding:]
+ -[MNArrivalRegionContainmentParameters setIncludeDistancePadding:]
+ -[MNLocation distanceToEndOfCurrentLeg]
+ -[MNLocation distanceToEndOfRoute]
+ -[MNNavigationSessionLogger navigationSessionState]
+ -[MNNavigationSessionLogger setNavigationSessionState:]
+ -[MNNavigationTraceManager _clearOldRoutePreviewTraces]
+ -[MNNavigationTraceManager saveRoutePreviewTrace:]
+ -[MNServerSessionStateInfo addDisplayedBannerID:withEventInfo:]
+ -[MNServerSessionStateInfo displayedTrafficBanners]
+ -[MNTrace dateFromTimestamp:]
+ -[MNTrace directionsStartDate]
+ -[MNTrace navigationEndDate]
+ -[MNTrace navigationStartDate]
+ -[MNTrace recordingStartDate]
+ -[MNTrace setDirectionsStartDate:]
+ -[MNTrace setNavigationEndDate:]
+ -[MNTrace setNavigationStartDate:]
+ -[MNTrace setRecordingStartDate:]
+ -[MNTracePreparedStatement _bindParameterIndexWithName:]
+ -[MNTracePreparedStatement bindNullParameter:]
+ -[MNTracePreparedStatement bindParameter:data:]
+ -[MNTracePreparedStatement bindParameter:double:]
+ -[MNTracePreparedStatement bindParameter:int:]
+ -[MNTracePreparedStatement bindParameter:string:]
+ -[MNTraceRecorder recordingStartDate]
+ -[MNTraceRecorder setNavigationEndDate:]
+ -[MNTraceRecorder setNavigationStartDate:]
+ -[MNTraceRecorder setRecordingStartDate:]
+ -[MNTraceRecorder tracePath]
+ -[MNTraceRecordingData routePreviewTracePath]
+ -[MNTraceRecordingData setRoutePreviewTracePath:]
+ -[MNTrafficIncidentAlert eventInfo]
+ _NSFileCreationDate
+ _OBJC_CLASS_$_GEOClientFeedbackInfo
+ _OBJC_CLASS_$_MNArrivalRegionContainmentParameters
+ _OBJC_IVAR_$_MNArrivalRegionContainmentParameters._excludeDistancePadding
+ _OBJC_IVAR_$_MNArrivalRegionContainmentParameters._includeDistancePadding
+ _OBJC_IVAR_$_MNNavigationSessionLogger._navigationSessionState
+ _OBJC_IVAR_$_MNServerSessionStateInfo._displayedTrafficBanners
+ _OBJC_IVAR_$_MNTrace._directionsStartDate
+ _OBJC_IVAR_$_MNTrace._navigationEndDate
+ _OBJC_IVAR_$_MNTrace._navigationStartDate
+ _OBJC_IVAR_$_MNTrace._recordingStartDate
+ _OBJC_IVAR_$_MNTraceRecorder._recordingStartDate
+ _OBJC_IVAR_$_MNTraceRecorder._updateDirectionsStartTimeStatement
+ _OBJC_IVAR_$_MNTraceRecorder._updateNavigationEndTimeStatement
+ _OBJC_IVAR_$_MNTraceRecorder._updateNavigationStartTimeStatement
+ _OBJC_IVAR_$_MNTraceRecorder._updateRecordingStartTimeStatement
+ _OBJC_IVAR_$_MNTraceRecordingData._routePreviewTracePath
+ _OBJC_IVAR_$_MNTrafficIncidentAlert._eventInfo
+ _OBJC_METACLASS_$_MNArrivalRegionContainmentParameters
+ __OBJC_$_INSTANCE_METHODS_MNArrivalRegionContainmentParameters
+ __OBJC_$_INSTANCE_VARIABLES_MNArrivalRegionContainmentParameters
+ __OBJC_$_PROP_LIST_MNArrivalRegionContainmentParameters
+ __OBJC_CLASS_RO_$_MNArrivalRegionContainmentParameters
+ __OBJC_METACLASS_RO_$_MNArrivalRegionContainmentParameters
+ ___112-[MNDirectionsRequestManager _requestServerDirections:preferredRoute:withIdentifier:auditToken:finishedHandler:]_block_invoke.53
+ ___40-[MNTraceRecorder setNavigationEndDate:]_block_invoke
+ ___41-[MNTraceRecorder setRecordingStartDate:]_block_invoke
+ ___42-[MNTraceRecorder setNavigationStartDate:]_block_invoke
+ ___58-[MNTurnByTurnLocationTracker _handleOffRouteForLocation:]_block_invoke.78
+ ___58-[MNTurnByTurnLocationTracker _handleOffRouteForLocation:]_block_invoke.79
+ ___64-[MNDrivingTurnByTurnLocationTracker updateRequestForETAUpdate:]_block_invoke
+ ___65-[MNTurnByTurnLocationTracker _handleWaypointRerouteForLocation:]_block_invoke.69
+ ___82-[MNTurnByTurnLocationTracker _rerouteRequestParametersForLocation:transportType:]_block_invoke_2
+ ___96-[GEOArrivalParameters(MNExtras) regionContainmentTypeForLocation:arrivalRegionType:parameters:]_block_invoke
+ ___block_descriptor_40_e8_32s_e33_v32?0"NSString"8"NSData"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e33_v32?0"NSString"8"NSData"16^B24ls32l8
+ ___block_descriptor_97_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.81
+ _objc_msgSend$_bindParameterIndexWithName:
+ _objc_msgSend$_clearOldRoutePreviewTraces
+ _objc_msgSend$_spokenPlaceName
+ _objc_msgSend$addDisplayedBannerEventInfo:
+ _objc_msgSend$addDisplayedBannerID:withEventInfo:
+ _objc_msgSend$addDisplayedBannerId:
+ _objc_msgSend$bindParameter:double:
+ _objc_msgSend$clientFeedbackInfo
+ _objc_msgSend$containsCoordinate:arrivalRegionType:
+ _objc_msgSend$containsLocation:arrivalRegionType:
+ _objc_msgSend$containsLocation:arrivalRegionType:parameters:
+ _objc_msgSend$displayedTrafficBanners
+ _objc_msgSend$distanceToEndOfCurrentLeg
+ _objc_msgSend$earlierDate:
+ _objc_msgSend$eventInfo
+ _objc_msgSend$excludeDistancePadding
+ _objc_msgSend$includeDistancePadding
+ _objc_msgSend$maneuverAndInstructionDescription
+ _objc_msgSend$recordLocation:timestamp:
+ _objc_msgSend$recordingStartDate
+ _objc_msgSend$regionContainmentTypeForLocation:arrivalRegionType:parameters:
+ _objc_msgSend$routePreviewTraceExtension
+ _objc_msgSend$routePreviewTracePath
+ _objc_msgSend$saveRoutePreviewTrace:
+ _objc_msgSend$setClientFeedbackInfo:
+ _objc_msgSend$setDirectionsStartDate:
+ _objc_msgSend$setExcludeDistancePadding:
+ _objc_msgSend$setIncludeDistancePadding:
+ _objc_msgSend$setNavigationEndDate:
+ _objc_msgSend$setNavigationStartDate:
+ _objc_msgSend$setRecordingStartDate:
+ _objc_msgSend$setRoutePreviewTracePath:
+ _objc_msgSend$tracePathForTraceName:extension:
+ _sqlite3_bind_parameter_index
- -[GEOArrivalParameters(MNExtras) containsCoordinate:arrivalRegionType:distanceToEndOfLeg:]
- -[GEOArrivalParameters(MNExtras) containsCoordinate:arrivalRegionType:distanceToEndOfLeg:excludeRadius:]
- -[GEOArrivalParameters(MNExtras) regionContainmentTypeFor:arrivalRegionType:distanceToEndOfLeg:excludeRadius:]
- -[MNDrivingTurnByTurnLocationTracker _overrideRerouteDirectionsRequest:]
- -[MNNavigationTraceManager _defaultTraceExtension]
- -[MNNavigationTraceManager _tracePathForTraceName:]
- -[MNNavigationTraceManager _validFilenameForTraceName:]
- -[MNTraceRecorder recordingStartTime]
- -[MNTraceRecorder setRecordingStartTime:]
- -[MNTrafficIncidentAlertUpdater _updatePreviousDisplayedBannerForRequest:]
- -[MNTrafficIncidentAlertUpdater _updateRerouteProposalStatusForRequest:]
- -[MNTurnByTurnLocationTracker _overrideRerouteDirectionsRequest:]
- _OBJC_IVAR_$_MNTrace._mainTransportType
- _OBJC_IVAR_$_MNTraceRecorder._recordingStartTime
- ___110-[GEOArrivalParameters(MNExtras) regionContainmentTypeFor:arrivalRegionType:distanceToEndOfLeg:excludeRadius:]_block_invoke
- ___112-[MNDirectionsRequestManager _requestServerDirections:preferredRoute:withIdentifier:auditToken:finishedHandler:]_block_invoke.52
- ___31-[MNTraceLoader _loadInfoTable]_block_invoke
- ___58-[MNTurnByTurnLocationTracker _handleOffRouteForLocation:]_block_invoke.76
- ___58-[MNTurnByTurnLocationTracker _handleOffRouteForLocation:]_block_invoke.77
- ___65-[MNTurnByTurnLocationTracker _handleWaypointRerouteForLocation:]_block_invoke.67
- ___block_descriptor_96_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$_defaultTraceExtension
- _objc_msgSend$_overrideRerouteDirectionsRequest:
- _objc_msgSend$_tracePathForTraceName:
- _objc_msgSend$_updatePreviousDisplayedBannerForRequest:
- _objc_msgSend$_updateRerouteProposalStatusForRequest:
- _objc_msgSend$containsCoordinate:arrivalRegionType:distanceToEndOfLeg:
- _objc_msgSend$containsCoordinate:arrivalRegionType:distanceToEndOfLeg:excludeRadius:
- _objc_msgSend$displayedBannerIds
- _objc_msgSend$recordingStartTime
- _objc_msgSend$regionContainmentTypeFor:arrivalRegionType:distanceToEndOfLeg:excludeRadius:
- _objc_msgSend$setRecordingStartTime:
- _objc_msgSend$updateIncidentResultForRerouteRequest:
CStrings:
+ "\x03\x13\x11\x13B1!"
+ "\x04\x1f\t\""
+ "\x05!"
+ "\x14?\x05"
+ ":directions_start_time"
+ ":navigation_end_time"
+ ":navigation_start_time"
+ ":recording_start_time"
+ "B28@0:8@16i24"
+ "B36@0:8@16i24@28"
+ "B44@0:8{?=ddd}16i40"
+ "Changed step index: %d %@| segment index: %d"
+ "Error calling -[MNTracePreparedStatement bindParameter:] because no parameter with the name \"%@\" was found."
+ "Error removing route preview trace \"%@\": %@"
+ "Error removing route preview trace at \"%@\": %@"
+ "MNArrivalRegionContainmentParameters"
+ "Q36@0:8@16i24@28"
+ "Removed route preview trace \"%@\" because it is over a week old."
+ "Removed route preview trace at \"%@\" because we're recording a navtrace."
+ "SELECT recording_start_time, directions_start_time, navigation_start_time, navigation_end_time, simulation, original_version FROM info LIMIT 1"
+ "T@\"NSData\",R,N,V_eventInfo"
+ "T@\"NSDate\",&,N,V_directionsStartDate"
+ "T@\"NSDate\",&,N,V_navigationEndDate"
+ "T@\"NSDate\",&,N,V_navigationStartDate"
+ "T@\"NSDate\",&,N,V_recordingStartDate"
+ "T@\"NSString\",C,N,V_routePreviewTracePath"
+ "Td,N,V_excludeDistancePadding"
+ "Td,N,V_includeDistancePadding"
+ "UPDATE info SET directions_start_time = :directions_start_time"
+ "UPDATE info SET navigation_end_time = :navigation_end_time"
+ "UPDATE info SET navigation_start_time = :navigation_start_time"
+ "UPDATE info SET recording_start_time = :recording_start_time"
+ "_bindParameterIndexWithName:"
+ "_clearOldRoutePreviewTraces"
+ "_directionsStartDate"
+ "_displayedTrafficBanners"
+ "_eventInfo"
+ "_excludeDistancePadding"
+ "_includeDistancePadding"
+ "_navigationEndDate"
+ "_navigationStartDate"
+ "_recordingStartDate"
+ "_routePreviewTracePath"
+ "_spokenPlaceName"
+ "_updateDirectionsStartTimeStatement"
+ "_updateNavigationEndTimeStatement"
+ "_updateNavigationStartTimeStatement"
+ "_updateRecordingStartTimeStatement"
+ "addDisplayedBannerEventInfo:"
+ "addDisplayedBannerID:withEventInfo:"
+ "addDisplayedBannerId:"
+ "bindNullParameter:"
+ "bindParameter:data:"
+ "bindParameter:double:"
+ "bindParameter:int:"
+ "bindParameter:string:"
+ "clientFeedbackInfo"
+ "containsCoordinate:arrivalRegionType:"
+ "containsLocation:arrivalRegionType:"
+ "containsLocation:arrivalRegionType:parameters:"
+ "dateFromTimestamp:"
+ "directionsStartDate"
+ "displayedTrafficBanners"
+ "distanceToEndOfCurrentLeg"
+ "distanceToEndOfRoute"
+ "earlierDate:"
+ "eventInfo"
+ "excludeDistancePadding"
+ "includeDistancePadding"
+ "maneuverAndInstructionDescription"
+ "navigationEndDate"
+ "navigationStartDate"
+ "recordingStartDate"
+ "regionContainmentTypeForLocation:arrivalRegionType:parameters:"
+ "routePreviewTraceExtension"
+ "routePreviewTracePath"
+ "routepreviewtrace"
+ "saveRoutePreviewTrace:"
+ "setClientFeedbackInfo:"
+ "setDirectionsStartDate:"
+ "setExcludeDistancePadding:"
+ "setIncludeDistancePadding:"
+ "setNavigationEndDate:"
+ "setNavigationStartDate:"
+ "setRecordingStartDate:"
+ "setRoutePreviewTracePath:"
+ "tracePathForTraceName:extension:"
+ "v32@?0@\"NSString\"8@\"NSData\"16^B24"
- "\x03\x13\x11\x13B1"
- "\x04\x1f\x05\""
- "\x14:\x16"
- "B52@0:8{?=ddd}16i40d44"
- "B60@0:8{?=ddd}16i40d44d52"
- "Changed step index: %d | segment index: %d"
- "Q60@0:8{?=ddd}16i40d44d52"
- "SELECT simulation, original_version FROM info LIMIT 1"
- "T@\"NSDate\",&,N,V_recordingStartTime"
- "Ti,R,N,V_mainTransportType"
- "_defaultTraceExtension"
- "_mainTransportType"
- "_overrideRerouteDirectionsRequest:"
- "_recordingStartTime"
- "_tracePathForTraceName:"
- "_updatePreviousDisplayedBannerForRequest:"
- "_updateRerouteProposalStatusForRequest:"
- "containsCoordinate:arrivalRegionType:distanceToEndOfLeg:"
- "containsCoordinate:arrivalRegionType:distanceToEndOfLeg:excludeRadius:"
- "displayedBannerIds"
- "recordingStartTime"
- "regionContainmentTypeFor:arrivalRegionType:distanceToEndOfLeg:excludeRadius:"
- "setRecordingStartTime:"

```
