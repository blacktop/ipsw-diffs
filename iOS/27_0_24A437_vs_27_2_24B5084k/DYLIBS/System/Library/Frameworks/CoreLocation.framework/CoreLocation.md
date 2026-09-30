## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3185.0.6.0.3
-  __TEXT.__text: 0x204cec
-  __TEXT.__objc_methlist: 0x9bd4
+3186.0.12.0.0
+  __TEXT.__text: 0x206604
+  __TEXT.__objc_methlist: 0x9cb4
   __TEXT.__const: 0x4dd0
-  __TEXT.__gcc_except_tab: 0xf25c
-  __TEXT.__oslogstring: 0x3abea
-  __TEXT.__cstring: 0x2514e
+  __TEXT.__gcc_except_tab: 0xf188
+  __TEXT.__oslogstring: 0x3aeb6
+  __TEXT.__cstring: 0x2525f
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x60b8
+  __TEXT.__unwind_info: 0x6118
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x21b0
+  __DATA_CONST.__const: 0x2248
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x52d0
+  __DATA_CONST.__objc_selrefs: 0x5338
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__got: 0x690
-  __AUTH_CONST.__const: 0x3d30
-  __AUTH_CONST.__cfstring: 0xba40
-  __AUTH_CONST.__objc_const: 0x10468
+  __AUTH_CONST.__const: 0x3d38
+  __AUTH_CONST.__cfstring: 0xbae0
+  __AUTH_CONST.__objc_const: 0x104e0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0xdb8
   __AUTH.__objc_data: 0x2850
-  __DATA.__objc_ivar: 0xb24
+  __DATA.__objc_ivar: 0xb30
   __DATA.__data: 0x1eb0
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_ivar: 0x68

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5216
-  Symbols:   1084
-  CStrings:  5555
+  Functions: 5240
+  Symbols:   1085
+  CStrings:  5583
 
Symbols:
+ _CLCopyAuthorization
CStrings:
+ "#Spi, CLCopyAuthorization failed"
+ "-[CLLocationInternalClient copyAuthorizationFromBundleID:toBundleID:]_block_invoke"
+ "AllowedAlways"
+ "AllowedAlwaysProvisionally"
+ "AllowedWhenInUse"
+ "AuthContext InUse:%d  RegResult Transient:%s Effective:%s  EffectiveMask:%d  ProvisionalMask:%d  DiagnosticMask:%d"
+ "CL: CLCopyAuthorization"
+ "CLMM,%{public}.1lf,TEPA,XPC dispatch,roadID,%{private}llu,clRoadID,%{sensitive}llu,projection,%{public}.3lf,snapCourse,%{public}.1lf"
+ "CLRS,CLTSP,intervalCountMismatch,decoded,%{public}lu,recorded,%{public}lu"
+ "CLRS,CLTSP,malformedPackedAltitudeBlob,bytes,%{public}lu,stride,%{public}lu"
+ "CLRS,CLTSP,malformedPackedLocationBlob,bytes,%{public}lu,stride,%{public}lu"
+ "CLRS,CLTSP,malformedPackedOdometryBlob,bytes,%{public}lu,stride,%{public}lu"
+ "CLRS,CLTSP,packedAltitudeBlobAllocationFailed,samples,%{public}lu"
+ "CLRS,CLTSP,packedLocationBlobAllocationFailed,samples,%{public}lu"
+ "CLRS,CLTSP,packedOdometryBlobAllocationFailed,samples,%{public}lu"
+ "CLRS,CLTSP,unsupportedBatchInputSchemaVersion,decoded,%{public}lu,oldestSupported,%{public}lu,current,%{public}lu"
+ "CLTSP,%{public}.1lf,A* Search road already added,%{sensitive}llu"
+ "CLTSP,%{public}.1lf,aStarConstruct,added first road,%{sensitive}llu,processingTime,%{private}.2lf"
+ "CLTSP,%{public}.1lf,aStarConstruct,search road already added,%{sensitive}llu"
+ "CLTSP,%{public}.1lf,added first road,%{sensitive}llu"
+ "CLTSP,%{public}.1lf,added last road,%{sensitive}llu"
+ "CLTSP,%{public}.3lf,aStarConstruct,found neighbors for %{sensitive}llu,size,%{public}lu,g,%{public}.2lf,h,%{public}.2lf,cost,%{public}.2lf,iterationCount,%{public}d,stopLL,%{sensitive}.7lf,%{sensitive}.7lf,stopJunction,%{private}d,stopAlt,%{private}.2lf,processingTime,%{private}.2lf,openSet,%{public}d,closedSet,%{public}d,iterationThreshold,%{public}d"
+ "CLTSP,%{public}.3lf,constructing between,start,%{sensitive}llu,stop,%{sensitive}llu"
+ "CLTSP,%{public}.3lf,found neighbors for %{sensitive}llu,size,%{public}lu,g,%{public}.2lf,h,%{public}.2lf,cost,%{public}.2lf,iterationCount,%{public}d"
+ "CLTSP,%{sensitive}llu,KPIComputer,findClosestPointOnRoad returned false,isRouteWithSkippedPart,%{public}d"
+ "CLTSP,getCLTripSegmentRoadDataArrayAsCLMapRoadVector,findRoadsNear call failed,roadID,%{sensitive}llu"
+ "CLTSP,getCLTripSegmentRoadDataArrayAsCLMapRoadVector,road data query failed,roadID,%{sensitive}llu"
+ "FailedBlocklisted"
+ "FailedUnavailable"
+ "FailedUnverified"
+ "FailedUserDenied"
+ "Missing"
+ "RegistrationResultString"
+ "RequiresAgent"
+ "TransientAwareRegistrationResultString"
+ "UNKNOWN"
+ "altitudeSamplesPacked"
+ "intervalCount"
+ "locationSamplesPacked"
+ "odometrySamplesPacked"
+ "v16@?0@?<v@?B>8"
+ "{\"msg%{public}.0s\":\"CLCopyAuthorization\", \"event\":%{public, location:escape_only}s}"
+ "\x81"
+ "\xb1"
- "AuthContext InUse:%d  RegResult:%d(%d) EffectiveMask:%d  ProvisionalMask:%d  DiagnosticMask:%d"
- "CLMM,%{public}.1lf,TEPA,XPC dispatch,roadID,%{private}llu,clRoadID,%{private}llu,projection,%{public}.3lf,snapCourse,%{public}.1lf"
- "CLRS,CLTSP,unsupportedBatchInputSchemaVersion,decoded,%{public}lu,expected,%{public}lu"
- "CLTSP,%{private}llu,KPIComputer,findClosestPointOnRoad returned false,isRouteWithSkippedPart,%{public}d"
- "CLTSP,%{public}.1lf,A* Search road already added,%{private}lld"
- "CLTSP,%{public}.1lf,aStarConstruct,added first road,%{private}lld,processingTime,%{private}.2lf"
- "CLTSP,%{public}.1lf,aStarConstruct,search road already added,%{private}lld"
- "CLTSP,%{public}.1lf,added first road,%lld"
- "CLTSP,%{public}.1lf,added last road,%lld"
- "CLTSP,%{public}.3lf,aStarConstruct,found neighbors for %{private}lld,size,%{public}lu,g,%{public}.2lf,h,%{public}.2lf,cost,%{public}.2lf,iterationCount,%{public}d,stopLL,%{sensitive}.7lf,%{sensitive}.7lf,stopJunction,%{private}d,stopAlt,%{private}.2lf,processingTime,%{private}.2lf,openSet,%{public}d,closedSet,%{public}d,iterationThreshold,%{public}d"
- "CLTSP,%{public}.3lf,constructing between,start,%{public}lld,stop,%{public}lld"
- "CLTSP,%{public}.3lf,found neighbors for %{private}lld,size,%{public}lu,g,%{public}.2lf,h,%{public}.2lf,cost,%{public}.2lf,iterationCount,%{public}d"
- "CLTSP,CLMM,MaphelperService,findTunnelEndPoint ENTRY,roadID,%llu,clRoadID,%llu,projection,%.3lf,snapCourse,%.1lf,allowNetwork,%d,preferCachedTiles,%d"
- "CLTSP,getCLTripSegmentRoadDataArrayAsCLMapRoadVector,findRoadsNear call failed,roadID,%{public}lld"
- "CLTSP,getCLTripSegmentRoadDataArrayAsCLMapRoadVector,road data query failed,roadID,%{public}lld"
- "\xa1"
```
