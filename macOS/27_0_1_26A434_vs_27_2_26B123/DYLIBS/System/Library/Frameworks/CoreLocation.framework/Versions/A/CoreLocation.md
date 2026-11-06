## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation`

```diff

-3185.0.6.0.0
-  __TEXT.__text: 0x1d02d0
-  __TEXT.__objc_methlist: 0x8d64
+3186.0.22.0.0
+  __TEXT.__text: 0x1d1f68
+  __TEXT.__objc_methlist: 0x8e5c
   __TEXT.__const: 0x3d88
-  __TEXT.__gcc_except_tab: 0xd954
-  __TEXT.__oslogstring: 0x345e6
-  __TEXT.__cstring: 0x20f50
+  __TEXT.__gcc_except_tab: 0xd8a8
+  __TEXT.__oslogstring: 0x348ec
+  __TEXT.__cstring: 0x21168
   __TEXT.__ustring: 0x1b0
-  __TEXT.__unwind_info: 0x4bb8
+  __TEXT.__unwind_info: 0x4c30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__const: 0xbc8
   __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x4b70
+  __DATA_CONST.__objc_selrefs: 0x4bf8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x628
-  __AUTH_CONST.__const: 0x48f8
-  __AUTH_CONST.__cfstring: 0xa220
-  __AUTH_CONST.__objc_const: 0xf440
+  __AUTH_CONST.__const: 0x4960
+  __AUTH_CONST.__cfstring: 0xa2e0
+  __AUTH_CONST.__objc_const: 0xf4c0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0xc50
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x24e0
-  __DATA.__objc_ivar: 0xaa0
+  __AUTH.__objc_data: 0x23f0
+  __DATA.__objc_ivar: 0xaac
   __DATA.__data: 0x1c30
   __DATA.__bss: 0xa78
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_ivar: 0x68
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x78
   __DATA_DIRTY.__bss: 0xcf0
   __DATA_DIRTY.__common: 0x19

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4748
-  Symbols:   1009
-  CStrings:  4927
+  Functions: 4775
+  Symbols:   1011
+  CStrings:  4959
 
Symbols:
+ _CFEqual
+ _CLCopyAuthorization
CStrings:
+ "#Spi, CLCopyAuthorization failed"
+ "#Spi, _CLInternalClearLocationAuthorizationLoctool failed"
+ "-[CLLocationInternalClient clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:]_block_invoke"
+ "-[CLLocationInternalClient copyAuthorizationFromBundleID:toBundleID:]_block_invoke"
+ "16:37:32"
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
+ "Oct  3 2026"
+ "RegistrationResultString"
+ "RequiresAgent"
+ "TransientAwareRegistrationResultString"
+ "UNKNOWN"
+ "altitudeSamplesPacked"
+ "intervalCount"
+ "locationSamplesPacked"
+ "odometrySamplesPacked"
+ "v12@?0B8"
+ "v16@?0@?<v@?B>8"
+ "{\"msg%{public}.0s\":\"CLCopyAuthorization\", \"event\":%{public, location:escape_only}s}"
+ "\x81"
+ "\xb1"
- "16:12:40"
- "Aug  8 2026"
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
- "CLTSP,getCLTripSegmentRoadDataArrayAsCLMapRoadVector,findRoadsNear call failed,roadID,%{public}lld"
- "CLTSP,getCLTripSegmentRoadDataArrayAsCLMapRoadVector,road data query failed,roadID,%{public}lld"
- "\xa1"
```
