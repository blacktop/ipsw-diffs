## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0xc1ac
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0xc40
-  __TEXT.__objc_methlist: 0x2b4
-  __TEXT.__const: 0x404
-  __TEXT.__gcc_except_tab: 0xec0
-  __TEXT.__cstring: 0x13a4
-  __TEXT.__oslogstring: 0x1a7
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0xecd
-  __TEXT.__objc_methtype: 0x50c
-  __TEXT.__unwind_info: 0x400
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3c0
-  __DATA_CONST.__cfstring: 0xf60
-  __DATA_CONST.__objc_classlist: 0x10
+3164.0.0.0.0
+  __TEXT.__text: 0x11880
+  __TEXT.__auth_stubs: 0x6f0
+  __TEXT.__objc_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x304
+  __TEXT.__const: 0x3b8
+  __TEXT.__gcc_except_tab: 0x1208
+  __TEXT.__cstring: 0x1552
+  __TEXT.__oslogstring: 0x673
+  __TEXT.__objc_classname: 0x8a
+  __TEXT.__objc_methname: 0x1014
+  __TEXT.__objc_methtype: 0x5c6
+  __TEXT.__unwind_info: 0x528
+  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__cfstring: 0x1100
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x530
-  __DATA.__objc_selrefs: 0x400
+  __DATA_CONST.__auth_got: 0x388
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x610
+  __DATA.__objc_selrefs: 0x438
   __DATA.__objc_ivar: 0x2c
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x9e0
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0xa28
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 1439E272-475B-33B9-8EAE-3AE9396D588B
-  Functions: 182
-  Symbols:   220
-  CStrings:  469
+  UUID: 6BA756B0-3CB5-376A-B84C-6D1A03D1F47A
+  Functions: 233
+  Symbols:   247
+  CStrings:  519
 
Symbols:
+ _OBJC_CLASS_$_CLRoadNetworkOrientationProcessor
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_METACLASS_$_CLRoadNetworkOrientationProcessor
+ __ZN17CLGeometryHelpers16calculateAzimuthERKNS_9coord3d_tES2_Rf
+ __ZN17CLGeometryHelpers16normalizeAzimuthEf
+ __ZN17CLGeometryHelpers17azimuthDifferenceEff
+ __ZN17CLGeometryHelpers17calculateDistanceERKNS_9coord3d_tES2_
+ __ZN17CLGeometryHelpers17latLonToEastNorthERKNS_9coord3d_tES2_
+ __ZN17CLGeometryHelpers21distanceToLineSegmentERKNS_9coord3d_tES2_S2_
+ __ZN17CLGeometryHelpers21getMetersPerDegreeLonEf
+ __ZN17CLGeometryHelpers24getDestinationCoordinateEffffRfS0_
+ __ZN9CLMapRoad16modifyRoadWidthsEv
+ __ZNSt3__112__next_primeEm
+ ___NSArray0__struct
+ ___sincosf_stret
+ __os_log_debug_impl
+ __os_log_error_impl
+ _asinf
+ _atan2f
+ _cosf
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x6
+ _sinf
+ _snprintf
+ _sscanf
- __ZNSt3__119piecewise_constructE
- __ZTVN10__cxxabiv117__class_type_infoE
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x9
- _strcmp
CStrings:
+ "%lf,%lf,%lf"
+ "@44@0:8@16f24f28Q32B40"
+ "CLRoadNetworkOrientationProcessor"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,aggregation,original_roads:%{public}lu,segments_generated:%{public}lu"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,aroad,RawRoadData,roadClass,%{public}u,travelDirection,%{public}u,isTunnel,%{public}d,isBridge,%{public}d,isRail,%{public}d,isDrivable,%{public}d,coordinateCount,%{public}zu"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,clamping_max_segments,requested,%{public}lu,clamped_to,%{public}lu"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,invalid_coordinates,queryLat,%{private}f,queryLon,%{private}f,reason,non-finite"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,invalid_coordinates,queryLat,%{private}f,queryLon,%{private}f,reason,out-of-range"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,invalid_max_segments,value,%{public}lu,reason,zero"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,road_aggregation,combined:2_roads,coordinates:%{public}lu"
+ "CLTSP,CLMM,CLRoadNetworkOrientationProcessor,seg,SimplifiedSegment,startLat,%{private}.8f,startLon,%{private}.8f,startAlt,%{private}.2f,endAlt,%{private}.2f,length,%{public}.2f,azimuth,%{public}.1f,width,%{public}.2f,attributes,%{public}u,distanceFromQuery,%{public}.2f"
+ "CLTSP,CLMM,MaphelperService,Error,Application missing road data entitlement"
+ "CLTSP,CLMM,MaphelperService,Error,Invalid null-island coordinates for simplified road segments query"
+ "CLTSP,CLMM,MaphelperService,Error,Invalid radius or over the max allowed radius for simplified road segments query"
+ "CLTSP,MapHelperService,configureWithSettings,debugLogging,%d"
+ "EnableDebugLogging"
+ "arrayWithCapacity:"
+ "attributes"
+ "azimuth"
+ "configureWithSettings:"
+ "dictionaryWithObjects:forKeys:count:"
+ "endAlt"
+ "fetchSimplifiedRoadSegmentsAroundCoordinate:inRadius:allowNetwork:preferCachedTiles:clearTiles:maxSegments:withReply:"
+ "length"
+ "localizedRoadName"
+ "localizedRoadName:"
+ "numberWithFloat:"
+ "objectForKeyedSubscript:"
+ "processGEORoadsIntoSimplifiedSegments:queryLat:queryLon:maxSegments:enableDebugLogging:"
+ "setEnableDebugLogging:"
+ "startAlt"
+ "startLat"
+ "startLon"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@16"
+ "v64@0:8{CLLocationCoordinate2D=dd}16f32B36B40B44Q48@?56"
+ "v64@0:8{CLLocationCoordinate2D=dd}16f32B36B40B44Q48@?<v@?@\"NSArray\">56"
+ "width"
- "componentsSeparatedByString:"
- "coord%i"
- "valueForKey:"

```
