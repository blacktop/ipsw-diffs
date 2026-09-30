## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3051.0.3.0.0
-  __TEXT.__text: 0x1fa678
+3056.0.0.0.0
+  __TEXT.__text: 0x1fbdb4
   __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0xa4b4
-  __TEXT.__const: 0x4948
-  __TEXT.__gcc_except_tab: 0xed4c
-  __TEXT.__oslogstring: 0x3a37a
-  __TEXT.__cstring: 0x24e7e
+  __TEXT.__objc_methlist: 0xa4fc
+  __TEXT.__const: 0x4938
+  __TEXT.__gcc_except_tab: 0xee4c
+  __TEXT.__oslogstring: 0x3a62d
+  __TEXT.__cstring: 0x250dc
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x5898
+  __TEXT.__unwind_info: 0x58d0
   __TEXT.__objc_classname: 0x1395
-  __TEXT.__objc_methname: 0x1cc1b
-  __TEXT.__objc_methtype: 0x5d9b
-  __TEXT.__objc_stubs: 0xea00
+  __TEXT.__objc_methname: 0x1cdf8
+  __TEXT.__objc_methtype: 0x5d9e
+  __TEXT.__objc_stubs: 0xea80
   __DATA_CONST.__got: 0x748
-  __DATA_CONST.__const: 0x2198
+  __DATA_CONST.__const: 0x2170
   __DATA_CONST.__objc_classlist: 0x538
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x54e8
+  __DATA_CONST.__objc_selrefs: 0x5518
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0xd90
-  __AUTH_CONST.__const: 0x3bb8
-  __AUTH_CONST.__cfstring: 0xb9e0
-  __AUTH_CONST.__objc_const: 0x11778
+  __AUTH_CONST.__const: 0x3bf8
+  __AUTH_CONST.__cfstring: 0xba40
+  __AUTH_CONST.__objc_const: 0x117e0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2ee0
-  __DATA.__objc_ivar: 0xb28
+  __DATA.__objc_ivar: 0xb30
   __DATA.__data: 0xf20
   __DATA.__bss: 0xae0
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_ivar: 0xa8
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0xd50
+  __DATA_DIRTY.__bss: 0xd60
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 50F95936-27E4-3FF0-9708-58D9938CEF10
-  Functions: 5308
+  UUID: EBAF9503-F070-3FF0-AC04-E1C5FD89FA21
+  Functions: 5320
   Symbols:   1115
-  CStrings:  11921
+  CStrings:  11946
 
CStrings:
+ "\n supportsFC1ND %s\n supportsNBAMMS %s\n supportsUnii5 %s\n supportsSimultaneousRanging %s\n capabilities %u\n"
+ "#Spi,locctl_tool,requestRouteReconstructionForPedestrian,could not request:%@"
+ "%p"
+ "-[CLLocationInternalClient requestRouteReconstructionForPedestrian]_block_invoke"
+ "21:34:11"
+ "@36@0:8B16B20B24I28B32"
+ "CLTSP,%{public}.2lf,added snap on parallel road,primaryLL,%{sensitive}.7lf,%{sensitive}.7lf,primaryCourse,%{public}.2lf,candLL,%{sensitive}.7lf,%{sensitive}.7lf,candCourse,%{public}.2lf"
+ "CLTSP,MI,integrateWithMapDataSparse,constructSegment with next snap success,%{public}s,nextIndex,%{public}d"
+ "CLTSP,MI,integrateWithMapDataSparse,errorReported,trying with next snap,%{public}s"
+ "CLTSP,RouteBuilder,generateAndCombineRoute,snap empty,index,%{public}d"
+ "CLTSP,origin and destination visit are same, distance check failed,distance,%{public}.1lf,threshold,%{public}.1lf"
+ "Jun 17 2025"
+ "TB,N,V_supportsSimultaneousRanging"
+ "Td,R,N,V_minDistanceBetweenODVisitsToGenerateTripSegmentMeters"
+ "_minDistanceBetweenODVisitsToGenerateTripSegmentMeters"
+ "_supportsSimultaneousRanging"
+ "bool CLTripSegmentProcessor::validateIncomingTripLocationData(CLTripSegmentProcessorOptions * _Nonnull, CLTripSegmentInputData * _Nonnull)"
+ "bool CLTripSegmentRouteBuilder::generateAndCombineRouteForOneSegment(bool, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, std::vector<CLGeoMapSnapDataPtr> &, std::vector<CLGeoMapSnapDataPtr> &, int, std::vector<CLRouteCandidatePtr> &, std::vector<CLRouteCandidateVector> &)"
+ "initWithSupportsFC1ND:supportsNBAMMS:supportsUnii5:capabilities:supportsSimultaneousRanging:"
+ "minDistanceBetweenODVisitsToGenerateTripSegmentMeters"
+ "requestRouteReconstructionForPedestrian"
+ "requestRouteReconstructionForPedestrianWithReplyBlock:"
+ "setMinDistanceBetweenODVisitsToGenerateTripSegmentMeters:"
+ "setSupportsSimultaneousRanging:"
+ "simultaneous_ranging"
+ "supportsSimultaneousRanging"
+ "void CLTripSegmentRouteBuilder::addAdditionalCandidates(const std::vector<CLGeoMapSnapDataPtr> &, bool, std::vector<CLGeoMapSnapDataPtr> &, std::map<CLMapRoadKey, bool> &, std::vector<CLMapRoadPtr> &)"
+ "{\"msg%{public}.0s\":\"#backgroundActivitySession Default handler received message\", \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"#backgroundActivitySession destroying connection (dealloc)\", \"self\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#ficConnectionManager destroying connection (dealloc)\", \"self\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#fullAccuracySession destroying connection (dealloc)\", \"self\":%{public, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"#serviceSession destroying connection (dealloc)\", \"self\":%{public, location:escape_only}s}"
- "\n supportsFC1ND %s\n supportsNBAMMS %s\n supportsUnii5 %s\n capabilities %u\n"
- "01:20:02"
- "@32@0:8B16B20B24I28"
- "May 30 2025"
- "bool CLTripSegmentProcessor::validateIncomingTripLocationData(CLTripSegmentProcessorOptions * _Nonnull, NSUUID * _Nonnull, NSArray<CLTripSegmentLocation *> * _Nonnull, const CLTripSegmentModeOfTransport)"
- "initWithSupportsFC1ND:supportsNBAMMS:supportsUnii5:capabilities:"
- "{\"msg%{public}.0s\":\"#backgroundActivitySession Default handler received message\", \"identityToken\":%{public, location:escape_only}s, \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"#backgroundActivitySession destroying connection (dealloc)\", \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"#ficConnectionManager destroying connection (dealloc)\"}"
- "{\"msg%{public}.0s\":\"#fullAccuracySession destroying connection (dealloc)\", \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"#serviceSession destroying connection (dealloc)\", \"self\":\"%{public}p\"}"

```
