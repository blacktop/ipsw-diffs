## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3056.0.14.0.0
-  __TEXT.__text: 0x1fd458
+3056.0.20.0.2
+  __TEXT.__text: 0x1fdce4
   __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_methlist: 0xa594
-  __TEXT.__const: 0x4938
-  __TEXT.__gcc_except_tab: 0xefe4
-  __TEXT.__oslogstring: 0x3a8f3
-  __TEXT.__cstring: 0x259bb
+  __TEXT.__const: 0x4950
+  __TEXT.__gcc_except_tab: 0xefec
+  __TEXT.__oslogstring: 0x3aa4e
+  __TEXT.__cstring: 0x25a2e
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x5878
+  __TEXT.__unwind_info: 0x5880
   __TEXT.__objc_classname: 0x1395
-  __TEXT.__objc_methname: 0x1d101
-  __TEXT.__objc_methtype: 0x5da4
+  __TEXT.__objc_methname: 0x1d1b5
+  __TEXT.__objc_methtype: 0x5dcb
   __TEXT.__objc_stubs: 0xeac0
   __DATA_CONST.__got: 0x748
   __DATA_CONST.__const: 0x2170

   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0xd98
   __AUTH_CONST.__const: 0x3b98
-  __AUTH_CONST.__cfstring: 0xbec0
+  __AUTH_CONST.__cfstring: 0xbee0
   __AUTH_CONST.__objc_const: 0x11950
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1F737E56-F0E3-309B-9AEE-864235635B20
-  Functions: 5307
+  UUID: AA2D3D41-C657-335D-BC3C-92F25AC57EC8
+  Functions: 5309
   Symbols:   1115
-  CStrings:  12056
+  CStrings:  12060
 
CStrings:
+ "-[CLMapsXPCServiceManager collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:WithReply:]_block_invoke"
+ "-[CLMapsXPCServiceManager constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:]_block_invoke"
+ "22:11:36"
+ "@140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112B116d120@128B136"
+ "B48@0:8@16B24B28B32B36^@40"
+ "B60@0:8{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}16B32B36B40B44B48^v52"
+ "B64@0:8d16d24d32B40B44B48B52@56"
+ "CLTSP,CVR,route construction completed,allowNetwork,%d,preferCachedTiles,%d"
+ "CLTSP,CVR-MHS,useMapsAPIForIntersectionQuery,%d,processingTimeMSec,%.2lf,openSet,%d,closedSet,%d,iterationCount,%d/%d"
+ "CLTSP,getGeoMapGeometrySettingsForRouteReconstruction,fTypeName,%s,fGeometryType,%{public}d,fIntersectionRoadSearchDistance,%{public}.1lf,fUseXPCServiceForDataQuery,%{public}d,fAllowNetworkTileDownload,%{public}d,fStoringRoadConnectionEnabled,%{public}d,fMinimumRadiusForMapDataBuffer_m,%{public}.1lf,fWaitForMapDataQueryToComplete,%{public}d,fMinSnapRadiusM,%{public}.1lf,fMaxSnapRadiusM,%{public}.1lf,preferPrecachedTilesDefaults,%{public}d,preferCachedTilesSetting,%{public}d"
+ "Jul 30 2025"
+ "PreferPrecachedTilesInTripSegmentProcessor"
+ "[CLLocationOutlierRejector]:[isTrajectoryStraightBeforeAndAfterFlag] trajecotry does not go straight.firstFlagIdx,%zu,secondFlagIdx,%zu,ioCount,%zu"
+ "[CLLocationOutlierRejector]:[isTrajectoryStraightBeforeAndAfterFlag] trajectory is not straight after the flag.flagIdx,%zu,straightness,%.2f,ioCount,%zu"
+ "collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:WithReply:"
+ "constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:"
+ "fetchGEOBuildingDataAroundCoordinate:inRadius:tileSetStyle:allowNetwork:preferCachedTiles:clearTiles:withReply:"
+ "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "fetchGEORoadDataAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:withReply:"
+ "fetchGEORoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:ignoreUTurns:returnRoads:"
+ "getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:gmfRoad:"
+ "getGEOMapFeatureRoadDataAroundLatitude:longitude:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:"
+ "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:"
+ "v148@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112B116d120@\"NSArray\"128B136@?<v@?@\"NSArray\">140"
+ "v148@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112B116d120@128B136@?140"
+ "v64@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52@?56"
+ "v64@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52@?<v@?@\"NSArray\">56"
+ "v64@0:8{CLLocationCoordinate2D=dd}16d32i40B44B48B52@?56"
+ "v64@0:8{CLLocationCoordinate2D=dd}16d32i40B44B48B52@?<v@?@\"NSArray\">56"
+ "v76@0:8q16{CLLocationCoordinate2D=dd}24d40B48B52B56B60B64@?68"
+ "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}72@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56B60^@64"
- "-[CLMapsXPCServiceManager collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:isPedestrianOrCycling:clearTiles:callSynchronously:WithReply:]_block_invoke"
- "-[CLMapsXPCServiceManager constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:]_block_invoke"
- "00:48:43"
- "@136@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124B132"
- "B44@0:8@16B24B28B32^@36"
- "B56@0:8{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}16B32B36B40B44^v48"
- "B60@0:8d16d24d32B40B44B48@52"
- "CLTSP,CVR,route construction completed"
- "CLTSP,CVR-MHS,useMapsAPIForIntersectionQuery,%d,processingTimeMSec,%.2lf,openSet,%d,closedSet,%d,iterationThreshold,%d"
- "CLTSP,getGeoMapGeometrySettingsForRouteReconstruction,fTypeName,%s,fGeometryType,%{public}d,fIntersectionRoadSearchDistance,%{public}.1lf,fUseXPCServiceForDataQuery,%{public}d,fAllowNetworkTileDownload,%{public}d,fStoringRoadConnectionEnabled,%{public}d,fMinimumRadiusForMapDataBuffer_m,%{public}.1lf,fWaitForMapDataQueryToComplete,%{public}d,fPreferCachedTiles,%{public}d,fMinSnapRadiusM,%{public}.1lf,fMaxSnapRadiusM,%{public}.1lf"
- "Jul 15 2025"
- "collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:isPedestrianOrCycling:clearTiles:callSynchronously:WithReply:"
- "constructRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:withReply:"
- "fetchGEOBuildingDataAroundCoordinate:inRadius:tileSetStyle:allowNetwork:clearTiles:withReply:"
- "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
- "fetchGEORoadDataAroundCoordinate:inRadius:allowNetwork:isPedestrianOrCycling:clearTiles:withReply:"
- "fetchGEORoadDataAtIntersectionOf:allowNetwork:isPedestrianOrCycling:clearTiles:ignoreUTurns:returnRoads:"
- "getCLMapRoadForLocation:roadID:clRoadID:allowNetwork:isPedestrianOrCycling:clearTiles:gmfRoad:"
- "getGEOMapFeatureRoadDataAroundLatitude:longitude:inRadius:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
- "internalConstructVehicularRouteFromLocation:roadID:clRoadID:projection:toLocation:toRoadID:toCLRoadID:toProjection:maxRouteLength:allowNetwork:isPedestrianOrCycling:clearTiles:iOSTime:familiarityData:useMapsAPIForIntersectionQuery:"
- "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:isPedestrianOrCycling:clearTiles:returnRoads:"
- "v144@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@\"NSArray\"124B132@?<v@?@\"NSArray\">136"
- "v144@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124B132@?136"
- "v60@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48@?52"
- "v60@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48@?<v@?@\"NSArray\">52"
- "v60@0:8{CLLocationCoordinate2D=dd}16d32i40B44B48@?52"
- "v60@0:8{CLLocationCoordinate2D=dd}16d32i40B44B48@?<v@?@\"NSArray\">52"
- "v72@0:8q16{CLLocationCoordinate2D=dd}24d40B48B52B56B60@?64"
- "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}68@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56^@60"

```
