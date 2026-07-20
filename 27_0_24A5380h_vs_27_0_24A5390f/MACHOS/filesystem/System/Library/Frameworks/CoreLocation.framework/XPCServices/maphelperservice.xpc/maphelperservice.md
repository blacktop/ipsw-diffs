## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3176.0.0.0.0
-  __TEXT.__text: 0x11810
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x304
+3183.0.0.0.0
+  __TEXT.__text: 0x12718
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x324
   __TEXT.__const: 0x3b8
-  __TEXT.__gcc_except_tab: 0x1208
-  __TEXT.__cstring: 0x1552
+  __TEXT.__gcc_except_tab: 0x1374
+  __TEXT.__cstring: 0x1b11
   __TEXT.__oslogstring: 0x673
   __TEXT.__objc_classname: 0x8a
-  __TEXT.__objc_methname: 0x1014
-  __TEXT.__objc_methtype: 0x5c6
-  __TEXT.__unwind_info: 0x530
-  __DATA_CONST.__const: 0x370
-  __DATA_CONST.__cfstring: 0x1100
+  __TEXT.__objc_methname: 0x11c5
+  __TEXT.__objc_methtype: 0x74e
+  __TEXT.__unwind_info: 0x548
+  __DATA_CONST.__const: 0x398
+  __DATA_CONST.__cfstring: 0x13a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x610
-  __DATA.__objc_selrefs: 0x438
+  __DATA.__objc_const: 0x638
+  __DATA.__objc_selrefs: 0x470
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0xa28

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 233
-  Symbols:   247
-  CStrings:  356
+  Functions: 237
+  Symbols:   251
+  CStrings:  398
 
Symbols:
+ _OBJC_CLASS_$_NSConstantDictionary
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ _objc_retain_x4
+ _objc_retain_x7
CStrings:
+ "B52@0:8@16B24B28B32B36B40^@44"
+ "CLMM,CLTSP,Roads,intersection query returned error,useStartOfRoad,%d"
+ "CLMM,CLTSP,Roads,intersection query,semaphore timed out,useStartOfRoad,%d"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint ENTRY,roadID,%llu,clRoadID,%llu,projection,%.3lf,snapCourse,%.1lf,allowNetwork,%d,preferCachedTiles,%d"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint EXIT nil,forward scan failed,iterOut,%d,distSoFar,%.1lf,reason,%s"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint EXIT nil,start road not found or not tunnel,startRoad,%d,gmf,%d,isTunnel,%d"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint EXIT ok,distToExit,%.1lf,tunnelLength,%.1lf,iterOut,%d,iterIn,%d,curved,%d"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint,%s,fillFromGEOMapFeatureRoad failed"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint,%s,reached max iterations,%d"
+ "TEPA,backward scan reached max iterations,"
+ "TEPA,forward scan reached max iterations,"
+ "TEPA,tunnel start point not found (TEPA exit point still valid),backward fillFromGEOMapFeatureRoad failed"
+ "TEPA,tunnel start point not found (TEPA exit point still valid),backward intersection query failed"
+ "TEPA,tunnel start point not found (TEPA exit point still valid),multi-inbound,"
+ "bwd"
+ "bwdFailureReason"
+ "courseAtExitPoint"
+ "dictionaryWithDictionary:"
+ "endPointDistanceFromCurrentSolution"
+ "failureReason"
+ "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:useStartOfRoad:returnRoads:"
+ "fetchGEORoadDataAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:includeRoadNames:withReply:"
+ "findRoadsToPreviousIntersectionOf:handler:completionHandler:"
+ "findTunnelEndPointFromLocation:roadID:clRoadID:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:clearTiles:withReply:"
+ "firstObject"
+ "fwd"
+ "isTunnelCurved"
+ "iterationsIn"
+ "iterationsOut"
+ "latitude"
+ "longitude"
+ "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:useStartOfRoad:returnRoads:"
+ "no TEPA,forward fillFromGEOMapFeatureRoad failed"
+ "no TEPA,forward intersection query failed"
+ "no TEPA,forward scan failed (unknown reason)"
+ "no TEPA,multi-outbound,"
+ "no TEPA,start road not found or not tunnel"
+ "numberWithInt:"
+ "scanTunnelWalkingBackward:fromRoad:gmf:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:"
+ "setObject:forKeyedSubscript:"
+ "speedLimitMps"
+ "startLatitude"
+ "startLongitude"
+ "tunnelLength"
+ "tunnelWidthAtExitPoint"
+ "v68@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52B56@?60"
+ "v68@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52B56@?<v@?@\"NSArray\">60"
+ "v88@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48d56i64B68B72B76@?80"
+ "v88@0:8{CLLocationCoordinate2D=dd}16Q32Q40d48d56i64B68B72B76@?<v@?@\"NSDictionary\">80"
+ "{TunnelScanIterResult=BidddddB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}72@0:8B16{shared_ptr<CLMapRoad>=^{CLMapRoad}^{__shared_weak_count}}20@36d44d52i60B64B68"
- "B48@0:8@16B24B28B32B36^@40"
- "CLMM,CLTSP,Roads,findRoadsFromNextIntersectionOf returned error"
- "CLMM,CLTSP,Roads,findRoadsFromNextIntersectionOf,semaphore timed out"
- "fetchGEOMapFeatureRoadDataAtIntersectionOf:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:"
- "fetchGEORoadDataAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:withReply:"
- "makeIntersectionQueryCallUsingMapsAPIFor:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:returnRoads:"
- "v64@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52@?56"
- "v64@0:8{CLLocationCoordinate2D=dd}16d32B40B44B48B52@?<v@?@\"NSArray\">56"
```
