## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

-3056.0.14.0.0
-  __TEXT.__text: 0xbd28
+3056.0.20.0.2
+  __TEXT.__text: 0xbdd4
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0xc40
   __TEXT.__objc_methlist: 0x2b4
   __TEXT.__const: 0x40c
-  __TEXT.__gcc_except_tab: 0xea8
-  __TEXT.__cstring: 0x127b
+  __TEXT.__gcc_except_tab: 0xea4
+  __TEXT.__cstring: 0x129f
   __TEXT.__oslogstring: 0x1a7
   __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0xe2b
-  __TEXT.__objc_methtype: 0x4e8
+  __TEXT.__objc_methname: 0xecd
+  __TEXT.__objc_methtype: 0x50c
   __TEXT.__unwind_info: 0x410
   __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xb8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 21BCFCD5-B8B2-3A98-92DC-BE36BE35C057
+  UUID: F135BC14-0123-3A3F-B5A2-B4A847A6698C
   Functions: 182
   Symbols:   225
   CStrings:  463
Symbols:
+ _objc_retain_x23
+ _objc_retain_x27
+ _objc_retain_x6
- _objc_retain_x26
- _objc_retain_x28
- _objc_retain_x5
Functions:
~ sub_100008000 : 692 -> 708
~ sub_100008a04 -> sub_100008a14 : 736 -> 752
~ sub_100009460 -> sub_100009480 : 828 -> 844
~ sub_100009920 -> sub_100009950 : 848 -> 864
~ sub_100009d08 -> sub_100009d48 : 308 -> 292
~ sub_100009e3c -> sub_100009e6c : 1080 -> 1088
~ sub_10000a274 -> sub_10000a2ac : 1236 -> 1244
~ sub_10000a828 -> sub_10000a868 : 560 -> 568
~ sub_10000afb8 -> sub_10000b000 : 424 -> 432
~ sub_10000b160 -> sub_10000b1b0 : 4460 -> 4552
CStrings:
+ "@140@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112B116d120@128B136"
+ "B48@0:8@16B24B28B32B36^@40"
+ "B60@0:8{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}16B32B36B40B44B48^v52"
+ "B64@0:8d16d24d32B40B44B48B52@56"
+ "CLTSP,CVR,route construction completed,allowNetwork,%d,preferCachedTiles,%d"
+ "CLTSP,CVR-MHS,useMapsAPIForIntersectionQuery,%d,processingTimeMSec,%.2lf,openSet,%d,closedSet,%d,iterationCount,%d/%d"
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
+ "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}72@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56B60^@64"
- "@136@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48{CLLocationCoordinate2D=dd}56Q72Q80d88d96B104B108B112d116@124B132"
- "B44@0:8@16B24B28B32^@36"
- "B56@0:8{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}16B32B36B40B44^v48"
- "B60@0:8d16d24d32B40B44B48@52"
- "CLTSP,CVR,route construction completed"
- "CLTSP,CVR-MHS,useMapsAPIForIntersectionQuery,%d,processingTimeMSec,%.2lf,openSet,%d,closedSet,%d,iterationThreshold,%d"
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
- "{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}68@0:8{CLLocationCoordinate2D=dd}16Q32Q40B48B52B56^@60"

```
