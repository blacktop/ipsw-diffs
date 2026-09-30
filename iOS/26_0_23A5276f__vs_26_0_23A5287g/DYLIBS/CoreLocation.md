## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3056.0.0.0.0
-  __TEXT.__text: 0x1fbdb4
+3056.0.6.0.2
+  __TEXT.__text: 0x1fd0cc
   __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0xa4fc
-  __TEXT.__const: 0x4938
-  __TEXT.__gcc_except_tab: 0xee4c
-  __TEXT.__oslogstring: 0x3a62d
-  __TEXT.__cstring: 0x250dc
+  __TEXT.__objc_methlist: 0xa554
+  __TEXT.__const: 0x4948
+  __TEXT.__gcc_except_tab: 0xf060
+  __TEXT.__oslogstring: 0x3a8ad
+  __TEXT.__cstring: 0x257aa
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x58d0
+  __TEXT.__unwind_info: 0x5910
   __TEXT.__objc_classname: 0x1395
-  __TEXT.__objc_methname: 0x1cdf8
-  __TEXT.__objc_methtype: 0x5d9e
-  __TEXT.__objc_stubs: 0xea80
+  __TEXT.__objc_methname: 0x1cf9d
+  __TEXT.__objc_methtype: 0x5dc7
+  __TEXT.__objc_stubs: 0xeb00
   __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x2170
+  __DATA_CONST.__const: 0x2198
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5518
+  __DATA_CONST.__objc_selrefs: 0x5540
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0xd90
-  __AUTH_CONST.__const: 0x3bf8
-  __AUTH_CONST.__cfstring: 0xba40
-  __AUTH_CONST.__objc_const: 0x117e0
+  __AUTH_CONST.__const: 0x3b98
+  __AUTH_CONST.__cfstring: 0xbde0
+  __AUTH_CONST.__objc_const: 0x11838
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2ee0
-  __DATA.__objc_ivar: 0xb30
+  __DATA.__objc_ivar: 0xb38
   __DATA.__data: 0xf20
   __DATA.__bss: 0xae0
   __DATA.__common: 0x68

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EBAF9503-F070-3FF0-AC04-E1C5FD89FA21
-  Functions: 5320
+  UUID: E9E528FE-0A12-3A59-9FBC-2E5E7DE80B1B
+  Functions: 5322
   Symbols:   1115
-  CStrings:  11946
+  CStrings:  12022
 
CStrings:
+ "%@ %@"
+ "-[CLMapsXPCServiceManager constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:]_block_invoke"
+ "-[CLMapsXPCServiceManager stopConstructRouteFromLocation]"
+ "-[CLMapsXPCServiceManager stopConstructRouteFromLocation]_block_invoke"
+ "-[CLTripSegmentProcessorManager killProcessingWithID:]"
+ "21:28:14"
+ "@136@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124B132"
+ "B44@0:8@16B24B28B32^@36"
+ "CLFindMyAccessoryFirmwareVersion <%p> VanBurenVersion: %@, RTKitVersion: %@, RoseAPVersion: %lu, RoseDSPVersion: %lu, CalibrationDataVersion: %lu, DebugVariant: %s"
+ "CLMM,CLTSP,MapHelperService,XPCService returned constructRouteFromLocation call,useMapsAPIForIntersectionQuery,%{public}d,roadCount,%{public}d,error,%{public}d,responseTime,%{public}.1lf"
+ "CLMM,CLTSP,MapHelperService,stopConstructRouteFromLocation,sharedInstance is nil"
+ "CLMM,CLTSP,Roads,findRoadsFromNextIntersectionOf returned error"
+ "CLMM,CLTSP,Roads,findRoadsFromNextIntersectionOf,semaphore timed out"
+ "CLTSP,%{public}.3lf,aStarConstruct,unable to init destinationRouteRoad"
+ "CLTSP,%{public}.3lf,aStarConstruct,unable to init startRouteRoad"
+ "CLTSP,CLAStarRouteConstructor,processingTime exceeded max allowed,constructRouteCandidates,destination loop"
+ "CLTSP,CLAStarRouteConstructor,processingTime exceeded max allowed,constructRouteCandidates,start loop"
+ "CLTSP,CLMM,API call to ge intersections failed"
+ "CLTSP,CLMM,Error,failed to get intersection data as input road is nil"
+ "CLTSP,CLMM,Error,intersection data object is nil"
+ "CLTSP,CLMM,got road with duplicate coordinates,coordinateCount,%d"
+ "CLTSP,CLMM,input road is nil"
+ "CLTSP,CVR,MaphelperService,invalid start or end road"
+ "CLTSP,CVR,best path found is the destinationPath - search complete!,iterations,%d"
+ "CLTSP,CVR,constructed route is empty,roadCount,%lu,iterations,%d"
+ "CLTSP,CVR,constructed,roadCount,%lu,iterations,%d"
+ "CLTSP,CVR,constructed,start road and destination road are neighbors"
+ "CLTSP,CVR,constructed,start road is same as destination road"
+ "CLTSP,CVR,did not find best path,iterations,%d"
+ "CLTSP,CVR,external signal received to stop processing after iterations,%d"
+ "CLTSP,CVR,intersection query failed,%d"
+ "CLTSP,CVR,iterations,%d,exceeded max,%d"
+ "CLTSP,CVR,route construction completed"
+ "CLTSP,CVR,route length exceeded max allowed,length,%.1lf,maxLength,%.1lf"
+ "CLTSP,CVR,search failed"
+ "CLTSP,CVR,search null road"
+ "CLTSP,CVR,search road already added,%lld"
+ "CLTSP,CVR,search road count,%d,exceeded max,%d"
+ "CLTSP,CVR,unable to init destinationRouteRoad"
+ "CLTSP,CVR,unable to init neighbor"
+ "CLTSP,CVR,unable to init startRouteRoad"
+ "CLTSP,CVR-MHS,useMapsAPIForIntersectionQuery,%d,processingTimeMSec,%.2lf,openSet,%d,closedSet,%d,iterationThreshold,%d"
+ "CLTSP,killProcessingWithID,ID,%{public}@"
+ "CLTSP,killProcessingWithID,max processing time set to 0.0 for id,%{public}@"
+ "Jul  1 2025"
+ "UseMapsAPIFunctionForIntersectionSearch"
+ "^{?=ISSSSSSCCC}"
+ "constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:"
+ "debugVariant"
+ "fEnableDebugLogging"
+ "fExternalSignalReceivedToStopConstructVehicularRouteProcessing"
+ "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:isPedestrianOrCycling:clearTiles:gmfRoad:"
+ "internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:"
+ "killProcessingWithID:"
+ "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "stopConstructRouteFromLocation"
+ "v144@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@\"NSArray\"124B132@?<v@?@\"NSArray\">136"
+ "v144@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124B132@?136"
+ "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}68@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56^@60"
- "-[CLMapsXPCServiceManager constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:withReply:]_block_invoke"
- "21:34:11"
- "@132@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124"
- "CLFindMyAccessoryFirmwareVersion <%p> VanBurenVersion: %@, RTKitVersion: %@, RoseAPVersion: %lu, RoseDSPVersion: %lu, CalibrationDataVersion: %lu"
- "CLTSP,CLAStarRouteConstructor,processingTime exceeded max allowed,constructRouteCandidates"
- "Jun 17 2025"
- "^{?=ISSSSSSCC}"
- "constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:withReply:"
- "getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:isPedestrianOrCycling:clearTiles:"
- "internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:"
- "v140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@\"NSArray\"124@?<v@?@\"NSArray\">132"
- "v140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124@?132"
- "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}60@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56"

```
