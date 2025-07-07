## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

-3056.0.0.0.0
-  __TEXT.__text: 0xb610
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_stubs: 0xba0
-  __TEXT.__objc_methlist: 0x27c
+3056.0.6.0.2
+  __TEXT.__text: 0xbd28
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x2b4
   __TEXT.__const: 0x40c
-  __TEXT.__gcc_except_tab: 0xcac
-  __TEXT.__cstring: 0xcc4
+  __TEXT.__gcc_except_tab: 0xea8
+  __TEXT.__cstring: 0x127b
   __TEXT.__oslogstring: 0x1a7
   __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0xc45
-  __TEXT.__objc_methtype: 0x4c0
-  __TEXT.__unwind_info: 0x418
-  __DATA_CONST.__auth_got: 0x330
+  __TEXT.__objc_methname: 0xe2b
+  __TEXT.__objc_methtype: 0x4e8
+  __TEXT.__unwind_info: 0x410
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x398
-  __DATA_CONST.__cfstring: 0xba0
+  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__cfstring: 0xf00
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x4c8
-  __DATA.__objc_selrefs: 0x3d0
-  __DATA.__objc_ivar: 0x24
+  __DATA.__objc_const: 0x530
+  __DATA.__objc_selrefs: 0x400
+  __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__common: 0x18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: EC7B44C5-432F-3853-94BC-40809A37A8EE
-  Functions: 184
-  Symbols:   222
-  CStrings:  400
+  UUID: 372A8997-2572-3C79-96E4-3B5BC83B1FDC
+  Functions: 182
+  Symbols:   225
+  CStrings:  463
 
Symbols:
+ __ZN11CLRouteRoad10initializeENSt3__110shared_ptrI9CLMapRoadEEP17GEOMapFeatureRoad
+ __ZN11CLRouteRoadD1Ev
+ __ZN11CLRouteRoadD2Ev
+ _objc_retain_x22
+ _objc_retain_x28
- __ZN11CLRouteRoad10initializeENSt3__110shared_ptrI9CLMapRoadEE
- __ZNSt3__112__next_primeEm
CStrings:
+ "@136@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124B132"
+ "B44@0:8@16B24B28B32^@36"
+ "CLMM,CLTSP,Roads,findRoadsFromNextIntersectionOf returned error"
+ "CLMM,CLTSP,Roads,findRoadsFromNextIntersectionOf,semaphore timed out"
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
+ "addObjectsFromArray:"
+ "constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:"
+ "fEnableDebugLogging"
+ "fExternalSignalReceivedToStopConstructVehicularRouteProcessing"
+ "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "findRoadsFromNextIntersectionOf:handler:completionHandler:"
+ "getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:isPedestrianOrCycling:clearTiles:gmfRoad:"
+ "internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:"
+ "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "setPreferStaleData:"
+ "stopConstructRouteFromLocation"
+ "v144@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@\"NSArray\"124B132@?<v@?@\"NSArray\">136"
+ "v144@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124B132@?136"
+ "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}68@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56^@60"
- "@132@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124"
- "constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:withReply:"
- "getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:isPedestrianOrCycling:clearTiles:"
- "internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:"
- "v140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@\"NSArray\"124@?<v@?@\"NSArray\">132"
- "v140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124@?132"
- "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}60@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56"

```
