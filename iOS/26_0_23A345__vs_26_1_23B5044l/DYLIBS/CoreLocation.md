## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3056.0.25.0.8
-  __TEXT.__text: 0x1fe350
-  __TEXT.__auth_stubs: 0x1b00
-  __TEXT.__objc_methlist: 0xa5ac
-  __TEXT.__const: 0x4a70
-  __TEXT.__gcc_except_tab: 0xf06c
-  __TEXT.__oslogstring: 0x3ab76
-  __TEXT.__cstring: 0x25a7c
+3060.0.8.0.2
+  __TEXT.__text: 0x2037ac
+  __TEXT.__auth_stubs: 0x1b20
+  __TEXT.__objc_methlist: 0xa5c4
+  __TEXT.__const: 0x4a80
+  __TEXT.__gcc_except_tab: 0xf474
+  __TEXT.__oslogstring: 0x3b753
+  __TEXT.__cstring: 0x26100
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x5880
+  __TEXT.__unwind_info: 0x5930
   __TEXT.__objc_classname: 0x1395
-  __TEXT.__objc_methname: 0x1d23b
-  __TEXT.__objc_methtype: 0x5dcb
-  __TEXT.__objc_stubs: 0xeb00
+  __TEXT.__objc_methname: 0x1d2d1
+  __TEXT.__objc_methtype: 0x5de4
+  __TEXT.__objc_stubs: 0xeb20
   __DATA_CONST.__got: 0x748
   __DATA_CONST.__const: 0x2170
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5578
+  __DATA_CONST.__objc_selrefs: 0x5588
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0xd98
-  __AUTH_CONST.__const: 0x3b98
-  __AUTH_CONST.__cfstring: 0xbf40
+  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__const: 0x3bd0
+  __AUTH_CONST.__cfstring: 0xc100
   __AUTH_CONST.__objc_const: 0x11980
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2ee0
   __DATA.__objc_ivar: 0xb54
-  __DATA.__data: 0xf20
-  __DATA.__bss: 0xae0
+  __DATA.__data: 0x9c8
+  __DATA.__bss: 0xa80
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_ivar: 0xa8
   __DATA_DIRTY.__objc_data: 0x550

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A9534CFD-E6C9-3434-9281-CA9CBB20D910
-  Functions: 5311
-  Symbols:   1115
-  CStrings:  12072
+  UUID: 1F826942-297B-33E5-A51A-590D0D8B6E33
+  Functions: 5331
+  Symbols:   1116
+  CStrings:  12141
 
Symbols:
+ __ZNSt3__15mutex4lockEv
+ __ZNSt3__15mutex6unlockEv
- _objc_release_x28
CStrings:
+ "-[CLTripSegmentProcessorManager constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:]"
+ "-[CLTripSegmentProcessorManager constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:completionHandler:]_block_invoke"
+ "20:28:19"
+ "CLMM,CLTSP,CLAStarRouteConstructor,construct,invalid processingTimeTracker"
+ "CLMM,CLTSP,CLAStarRouteConstructor,constructPedestrian,invalid processingTimeTracker"
+ "CLTSP,CLAStarRouteConstructor,constructRouteCandidates,invalid processingTimeTracker"
+ "CLTSP,CLMM,input retrun road array is nil"
+ "CLTSP,CLTripSegmentProcessor,processingTime exceeded max allowed,at the start of the processing in processData"
+ "CLTSP,constructRouteFromWaypoints called with waypoints,%{public}d,tripID,%{public}s"
+ "CLTSP,constructRouteFromWaypoints failed"
+ "CLTSP,constructRouteFromWaypoints failed,routeID,%{public}s"
+ "CLTSP,constructRouteFromWaypoints,AStar Route Reconstruction failed for segment,%{public}zu,tripID,%{public}s"
+ "CLTSP,constructRouteFromWaypoints,Empty AStar route for segment %{public}zu"
+ "CLTSP,constructRouteFromWaypoints,failed to get snap candidates for waypoint"
+ "CLTSP,constructRouteFromWaypoints,insufficient waypoints data"
+ "CLTSP,constructRouteFromWaypoints,no route segments constructed successfully"
+ "CLTSP,constructRouteFromWaypoints,output,routeID,%{public}s,modeOfTransport,%{public}d,inputWaypoints,%{public}d,routeRoadsCount,%{public}d,outputWaypoints,%{public}d,totalIterations,%{public}d,processingTimeMSec,%{public}.1lf"
+ "CLTSP,constructRouteFromWaypoints,processing segment,%{public}zu,to,%{public}zu,tripID,%{public}s"
+ "CLTSP,constructRouteFromWaypoints,processingTime exceeded max allowed,segment %{public}zu"
+ "CLTSP,constructRouteFromWaypoints,returned error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "CLTSP,constructRouteFromWaypoints,unable to generate waypoints"
+ "CLTSP,constructRouteFromWaypoints,waypoints data is nil or empty,tripID,%{public}s"
+ "CLTSP,constructRouteFromWaypoints,waypoints or constructed route is empty,routeCount,%{public}d,wpCount,%{public}d"
+ "CLTSP,constructSegment,tripID,%{public}s is not in CLTripSegmentSharedData"
+ "CLTSP,convert1HzDataToSparseAndComputeRouteMatchKPI,tripID,%{public}s is not in CLTripSegmentSharedData"
+ "CLTSP,convert1HzDataToSparseAndComputeRouteMatchKPI,tripID,%{public}s,chunk of previously skipped trip,duration,%{public}d,chunks,%{public}d"
+ "CLTSP,convert1HzDataToSparseAndComputeRouteMatchKPI,tripID,%{public}s,processing rate limited,generatedNumber,%{public}d"
+ "CLTSP,convert1HzDataToSparseAndComputeRouteMatchKPI,tripID,%{public}s,trip duration check failed,duration,%{public}d,chunkCount,%{public}d"
+ "CLTSP,null sequenceNumber,skip sequenceNumber update."
+ "CLTSP,recordAnalyticsInCLTSPFile,tripID,%{public}s is not in CLTripSegmentSharedData"
+ "CLTSP,segment crossed more than one multi-intersection, could be an incorrectly constructed segment,%{public}lu"
+ "CLTSP,sharedData,stop trip processing element erased due to timeout,tripID,%{public}s,count,%{public}lu"
+ "CLTSP,sharedData,stopProcessingForTrip,max processing time set to,%{public}.2lf,for id,%{public}s,status,%{public}d"
+ "CLTSP,sharedData,stopProcessingForTrip,trip added to map,%{public}s"
+ "CLTSP,sharedData,tripData add failed, static data pointer is null,tripID,%{public}s,count,%{public}lu"
+ "CLTSP,sharedData,tripData element added,tripID,%{public}s,count,%{public}lu"
+ "CLTSP,sharedData,tripData element erased due to timeout,tripID,%{public}s,count,%{public}lu"
+ "CLTSP,sharedData,tripData element updated pointer,tripID,%{public}s,count,%{public}lu"
+ "CLTSP,sharedData,tripData stats submitted and element erased,tripID,%{public}s,count,%{public}lu"
+ "CLTSP,sharedData,tripID not present in CLTripSegmentSharedData array while accessing getAnalyticsInstance,%{public}s,arraySize,%{public}d"
+ "CLTSP,sharedData,tripID not present in CLTripSegmentSharedData array while accessing getProcessingTimeTrackerInternal,%{public}s,arraySize,%{public}d"
+ "CLTSP,sharedData,tripID not present in CLTripSegmentSharedData array while accessing getRoadSequenceNumber,%{public}s,arraySize,%{public}d"
+ "CLTSP,sharedData,tripID not present in CLTripSegmentSharedData array while accessing getRouteMatchKPIComputer,%{public}s,arraySize,%{public}d"
+ "CLTSP,tripSegmentID,%{public}s should exist in CLTripSegmentSharedData"
+ "CLTSP,waypoints data is nil or empty"
+ "ConstructRouteFromWaypoints"
+ "ConstructRouteFromWaypoints_Analytics"
+ "ConstructRouteFromWaypoints_InputWaypoints"
+ "ConstructRouteFromWaypoints_Output"
+ "ConstructRouteFromWaypoints_RouteID"
+ "ConstructRouteFromWaypoints_SegmentsFailedToReconstruct"
+ "ConstructRouteFromWaypoints_WaypointsFailedToSnap"
+ "Sep 16 2025"
+ "aStarProcessingTimeMSec"
+ "bool CLAStarRouteConstructor::construct(CLDistanceCalc &, const CFAbsoluteTime, std::shared_ptr<CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker>, const CLGeoMapSnapDataPtr, const CLGeoMapSnapDataPtr, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const double, const bool, std::shared_ptr<CLFamiliarRoadData>, const double)"
+ "bool CLAStarRouteConstructor::construct(CLDistanceCalc &, const CFAbsoluteTime, std::shared_ptr<CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker>, const CLGeoMapSnapDataPtr, const CLGeoMapSnapDataPtr, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const double, const bool, std::shared_ptr<CLFamiliarRoadData>, const double)_block_invoke"
+ "bool CLAStarRouteConstructor::constructPedestrian(CLDistanceCalc &, const CFAbsoluteTime, std::shared_ptr<CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker>, const CLMapRoadPtr &, const CLMapRoadPtr &, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const GEOLocationCoordinate2D &, const double, double, const std::optional<double>)"
+ "bool CLTripSegmentProcessor::constructRouteFromWaypoints(NSUUID * _Nonnull, NSArray<CLTripSegmentLocation *> * _Nonnull, CLTripSegmentProcessorOptions * _Nonnull, TripSegmentOutputDataHandler _Nonnull)"
+ "constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:"
+ "constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:completionHandler:"
+ "constructedRoadCount"
+ "segmentsFailedDueToMoreThanOneMultiIntersectionCrossing"
+ "segmentsSuccessful"
+ "static void CLRoadTypeConversionUtilities::getCLMapRoadVectorAsCLTripSegmentRoadDataArray(const std::vector<CLMapRoadPtr> &, std::shared_ptr<double>, NSMutableArray<CLTripSegmentRoadData *> * _Nonnull)"
+ "std::shared_ptr<CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker> CLTripSegmentSharedData::getProcessingTimeTrackerInternal(const std::string &)"
+ "std::shared_ptr<CLTripSegmentAnalytics> CLTripSegmentSharedData::getAnalyticsInstance(const std::string &)"
+ "std::shared_ptr<CLTripSegmentRouteMatchKPI> CLTripSegmentSharedData::getRouteMatchKPIComputer(const std::string &)"
+ "std::shared_ptr<double> CLTripSegmentSharedData::getRoadSequenceNumber(const std::string &)"
+ "totalProcessingTimeMsec"
+ "v56@0:8@16@24@32@?40@?48"
+ "void CLAStarRouteConstructor::constructRouteCandidates(std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, std::shared_ptr<CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker>, const std::vector<CLGeoMapSnapDataPtr> &, const std::vector<CLGeoMapSnapDataPtr> &, std::vector<CLRouteCandidatePtr> &)"
+ "void CLTripSegmentProcessor::recordAnalyticsInCLTSPFile(CLTripSegmentInputData * _Nonnull, const CLTripSegmentProcessorStatus)"
+ "void CLTripSegmentSharedData::addTrip(const std::string &, std::shared_ptr<CLTripSegmentStaticData> &, double)"
+ "void CLTripSegmentSharedData::stopProcessingForTripInternal(const std::string &, bool)"
- "18:42:58"
- "Aug  9 2025"
- "CLTSP,killProcessingWithID,max processing time set to 0.0 for id,%{public}@"
- "CLTSP,tripData add failed, static data pointer is null,tripID,%{public}s,count,%{public}lu"
- "CLTSP,tripData element added,tripID,%{public}s,count,%{public}lu"
- "CLTSP,tripData element erased due to timeout,tripID,%{public}s,count,%{public}lu"
- "CLTSP,tripData element updated pointer,tripID,%{public}s,count,%{public}lu"
- "CLTSP,tripData stats submitted and element erased,tripID,%{public}s,count,%{public}lu"
- "CLTSP,tripID not present in CLTripSegmentSharedData array while accessing getAnalyticsInstance,%{public}s,arraySize,%{public}d"
- "CLTSP,tripID not present in CLTripSegmentSharedData array while accessing getRoadSequenceNumber,%{public}s,arraySize,%{public}d"
- "CLTSP,tripID not present in CLTripSegmentSharedData array while accessing getRouteMatchKPIComputer,%{public}s,arraySize,%{public}d"
- "CLTripSegmentAnalytics &CLTripSegmentSharedData::getAnalyticsInstance(const std::string &)"
- "CLTripSegmentRouteMatchKPI &CLTripSegmentSharedData::getRouteMatchKPIComputer(const std::string &)"
- "bool CLAStarRouteConstructor::construct(CLDistanceCalc &, const CFAbsoluteTime, CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker &, const CLGeoMapSnapDataPtr, const CLGeoMapSnapDataPtr, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const double, const bool, std::shared_ptr<CLFamiliarRoadData>, const double)"
- "bool CLAStarRouteConstructor::construct(CLDistanceCalc &, const CFAbsoluteTime, CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker &, const CLGeoMapSnapDataPtr, const CLGeoMapSnapDataPtr, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const double, const bool, std::shared_ptr<CLFamiliarRoadData>, const double)_block_invoke"
- "bool CLAStarRouteConstructor::constructPedestrian(CLDistanceCalc &, const CFAbsoluteTime, CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker &, const CLMapRoadPtr &, const CLMapRoadPtr &, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const GEOLocationCoordinate2D &, const double, double, const std::optional<double>)"
- "double &CLTripSegmentSharedData::getRoadSequenceNumber(const std::string &)"
- "void CLAStarRouteConstructor::constructRouteCandidates(std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker &, const std::vector<CLGeoMapSnapDataPtr> &, const std::vector<CLGeoMapSnapDataPtr> &, std::vector<CLRouteCandidatePtr> &)"
- "void CLTripSegmentSharedData::addTrip(const std::string &, std::shared_ptr<CLTripSegmentStaticData> &)"

```
