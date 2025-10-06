## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3060.0.8.0.2
-  __TEXT.__text: 0x2037ac
+3060.0.16.0.0
+  __TEXT.__text: 0x2085f4
   __TEXT.__auth_stubs: 0x1b20
-  __TEXT.__objc_methlist: 0xa5c4
-  __TEXT.__const: 0x4a80
-  __TEXT.__gcc_except_tab: 0xf474
-  __TEXT.__oslogstring: 0x3b753
-  __TEXT.__cstring: 0x26100
+  __TEXT.__objc_methlist: 0xa5e4
+  __TEXT.__const: 0x4ab0
+  __TEXT.__gcc_except_tab: 0xf860
+  __TEXT.__oslogstring: 0x3bdb1
+  __TEXT.__cstring: 0x2624c
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x5930
-  __TEXT.__objc_classname: 0x1395
-  __TEXT.__objc_methname: 0x1d2d1
+  __TEXT.__unwind_info: 0x5968
+  __TEXT.__objc_classname: 0x13a5
+  __TEXT.__objc_methname: 0x1d317
   __TEXT.__objc_methtype: 0x5de4
-  __TEXT.__objc_stubs: 0xeb20
+  __TEXT.__objc_stubs: 0xeb60
   __DATA_CONST.__got: 0x748
   __DATA_CONST.__const: 0x2170
-  __DATA_CONST.__objc_classlist: 0x538
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5588
+  __DATA_CONST.__objc_selrefs: 0x55a0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0xda8
-  __AUTH_CONST.__const: 0x3bd0
-  __AUTH_CONST.__cfstring: 0xc100
-  __AUTH_CONST.__objc_const: 0x11980
+  __AUTH_CONST.__const: 0x3bf0
+  __AUTH_CONST.__cfstring: 0xc180
+  __AUTH_CONST.__objc_const: 0x11a10
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH.__objc_data: 0x2ee0
+  __AUTH.__objc_data: 0x2f30
   __DATA.__objc_ivar: 0xb54
   __DATA.__data: 0x9c8
   __DATA.__bss: 0xa80

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1F826942-297B-33E5-A51A-590D0D8B6E33
-  Functions: 5331
+  UUID: 03B27543-37EA-3FCC-83DB-6CED43154C9A
+  Functions: 5341
   Symbols:   1116
-  CStrings:  12141
+  CStrings:  12173
 
CStrings:
+ "+[CLRouteAnalyzer calculateRouteLinearity:]"
+ "+[CLRouteAnalyzer extractRouteCorners:]"
+ "06:50:46"
+ "CLOR,corner,index,%{public}zu,latitude,%{sensitive}.7f,longitude,%{sensitive}.7f,signedAngle,%{public}.2f,timestamp,%{public}.1f"
+ "CLOR,cornerSummary,totalPoints,%{public}zu,cornersDetected,%{public}zu"
+ "CLOR,extractRouteCorners,error,null tripLocations"
+ "CLOR,extractRouteCorners,warning,insufficient samples,%{public}zu"
+ "CLOR,routeLinearity,error,null locationSamples"
+ "CLOR,routeLinearity,segment,%{public}zu,points,%{public}zu,distance,%{public}.1f,avgDeviation,%{public}.2f,rawLinearity,%{public}.3f,linearity,%{public}.3f,weightedContrib,%{public}.3f"
+ "CLOR,routeLinearity,segmentBounds,%{public}zu,startIdx,%{public}zu,endIdx,%{public}zu,startLat,%{sensitive}.8f,startLon,%{sensitive}.8f,endLat,%{sensitive}.8f,endLon,%{sensitive}.8f"
+ "CLOR,routeLinearity,summary,segments,%{public}zu,turns,%{public}zu,processedSegments,%{public}zu,totalDistance,%{public}.1f,finalScore,%{public}.3f"
+ "CLOR,routeLinearity,turn,%{public}zu,index,%{public}zu,latitude,%{sensitive}.8f,longitude,%{sensitive}.8f,angle,%{public}.2f"
+ "CLOR,routeLinearity,warning,insufficient samples,%{public}zu"
+ "CLOR,tripLocation,index,%{public}zu,latitude,%{sensitive}.7f,longitude,%{sensitive}.7f,timestamp,%{public}.1f"
+ "CLRouteAnalyzer"
+ "CLTSP,CLMM,MaphelperService,stopConstructRouteFromLocation"
+ "CLTSP,CVR,iterations,%d/%d,exceeded max"
+ "CLTSP,CVR,iterations,%d/%d,exceeded max allowed time,%.2lf"
+ "CLTSP,CVR,route construction completed,allowNetwork,%d,preferCachedTiles,%d,processingTimeMSec,%.2lf,iterations,%d/%d"
+ "CLTSP,CVR,route length exceeded max allowed,length,%.1lf,maxLength,%.1lf,iterations,%d/%d"
+ "CLTSP,CVR,search failed,processingTimeMSec,%.2lf,iterations,%d/%d"
+ "CLTSP,getWaypointsSubsetFromSnapPoint,findClosestPointOnRoad returned false"
+ "CLTSP,getWaypointsSubsetFromSnapPoint,matched on a road not in route"
+ "CLTSP,getWaypointsSubsetFromSnapPoint,waypoint is nil or zero"
+ "CLTSP,getWaypointsSubsetFromSnapPoint,waypoint subset is nil"
+ "CLTSP,matchLocationsToRoute,waypoint subset is nil"
+ "CLTSP,matchLocationsToRoute,waypoints is invalid"
+ "Sep 26 2025"
+ "[CLLocationOutlierRejector]:[constructIOTrajecotry] empty inertial odometry data batch."
+ "calculateRouteLinearity:"
+ "extractRouteCorners:"
+ "initWithObjectsAndKeys:"
+ "locationIndex"
+ "signedAngleDeg"
- "20:28:19"
- "CLTSP,CVR,iterations,%d,exceeded max,%d"
- "CLTSP,CVR,route construction completed,allowNetwork,%d,preferCachedTiles,%d"
- "CLTSP,CVR,route length exceeded max allowed,length,%.1lf,maxLength,%.1lf"
- "CLTSP,CVR,search failed"
- "Sep 16 2025"

```
