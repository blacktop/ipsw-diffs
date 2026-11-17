## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3188.0.7.0.1
-  __TEXT.__text: 0x206dbc
+3188.0.11.0.0
+  __TEXT.__text: 0x207abc
   __TEXT.__objc_methlist: 0x9d1c
   __TEXT.__const: 0x4e50
-  __TEXT.__gcc_except_tab: 0xf1a8
-  __TEXT.__oslogstring: 0x3af70
-  __TEXT.__cstring: 0x252d2
+  __TEXT.__gcc_except_tab: 0xf204
+  __TEXT.__oslogstring: 0x3b1c4
+  __TEXT.__cstring: 0x252da
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x6140
+  __TEXT.__unwind_info: 0x6148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5246
+  Functions: 5247
   Symbols:   1085
-  CStrings:  5587
+  CStrings:  5590
 
CStrings:
+ "CLTSP,MI,integrateWithMapData,sparse input empty,GPS deviation check disabled,id,%{public}s"
+ "CLTSP,Warning,cannot interpolate along route,gps_deviation_check_failed,1,median_deviation_m,%{public}.1lf,good_gps_count,%{public}zu,routeLength_m,%{public}.1lf,li_distance_m,%{public}.1lf"
+ "CLTSP,Warning,cannot interpolate along route,invalid_route_check_failed,1,invalid_duration,%{public}d,invalid_route_length,%{public}d,invalid_li_distance,%{public}d,duration_s,%{public}.3lf,routeLength_m,%{public}.1lf,li_distance_m,%{public}.1lf"
+ "CLTSP,Warning,cannot interpolate along route,speed_check_failed,%{public}d,distance_check_failed,%{public}d,route_speed_mps,%{public}.1lf,max_start_destination_speed_mps,%{public}.1lf,routeLength_m,%{public}.1lf,li_distance_m,%{public}.1lf,short_route_check_failed,%{public}d"
+ "bool CLTripSegmentMapIntegratorSparse::interpolateLocationsAlongSegmentPedestrian(CLAStarRouteConstructor &, std::vector<CLGeoMapSnapDataPtr> &, const CLGeoMapSnapDataPtr, const CLGeoMapSnapDataPtr, const CLGeoMapLocationArray &, bool &) const"
- "CLTSP,Warning,cannot interpolate along route,speed_check_failed,%d,distance_check_failed,%d,route_speed_mps,%{public}.1lf,max_start_destination_speed_mps,%{public}.1lf,routeLength_m,%.1lf,li_distance_m,%.1lf"
- "bool CLTripSegmentMapIntegratorSparse::interpolateLocationsAlongSegmentPedestrian(CLAStarRouteConstructor &, std::vector<CLGeoMapSnapDataPtr> &, const CLGeoMapSnapDataPtr, const CLGeoMapSnapDataPtr, const CLGeoMapLocationArray &) const"
```
