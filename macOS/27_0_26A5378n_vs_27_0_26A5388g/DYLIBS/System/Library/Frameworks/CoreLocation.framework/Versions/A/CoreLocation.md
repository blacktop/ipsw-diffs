## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3176.0.0.0.0
-  __TEXT.__text: 0x1ce918
-  __TEXT.__objc_methlist: 0x8cbc
-  __TEXT.__const: 0x3cd8
-  __TEXT.__gcc_except_tab: 0xd9b8
-  __TEXT.__oslogstring: 0x343ce
-  __TEXT.__cstring: 0x20c04
+3183.0.0.0.0
+  __TEXT.__text: 0x1cfac4
+  __TEXT.__objc_methlist: 0x8d14
+  __TEXT.__const: 0x3d48
+  __TEXT.__gcc_except_tab: 0xd958
+  __TEXT.__oslogstring: 0x34636
+  __TEXT.__cstring: 0x20f38
   __TEXT.__ustring: 0x1b0
-  __TEXT.__unwind_info: 0x4b40
+  __TEXT.__unwind_info: 0x4ba8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x4b18
+  __DATA_CONST.__objc_selrefs: 0x4b50
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__got: 0x620
-  __AUTH_CONST.__const: 0x4768
-  __AUTH_CONST.__cfstring: 0xa040
-  __AUTH_CONST.__objc_const: 0xf230
+  __AUTH_CONST.__const: 0x48a8
+  __AUTH_CONST.__cfstring: 0xa1e0
+  __AUTH_CONST.__objc_const: 0xf270
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__auth_got: 0xc48
   __AUTH.__objc_data: 0x2490
-  __DATA.__objc_ivar: 0xa78
+  __DATA.__objc_ivar: 0xa7c
   __DATA.__data: 0x1c30
   __DATA.__bss: 0xa78
   __DATA.__common: 0x50

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4719
-  Symbols:   1006
-  CStrings:  4902
+  Functions: 4741
+  Symbols:   1007
+  CStrings:  4926
 
Symbols:
+ _CLPromoteSystemService
CStrings:
+ "#Spi, CLPromoteSystemService failed"
+ "+[CLMapsXPCServiceManager sharedInstance]_block_invoke"
+ "-[CLLocationInternalClient promoteSystemServiceWithBundlePath:]_block_invoke"
+ "-[CLMapsXPCServiceManager collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:includeRoadNames:WithReply:]_block_invoke"
+ "-[CLMapsXPCServiceManager findTunnelEndPointFromLocation:roadID:clRoadID:projection:snapCourse:maxIterations:allowNetwork:preferCachedTiles:clearTiles:callSynchronously:withReply:]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Daemon/Core/CSI/CLMachThreadSupport.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Daemon/Positioning/GPS/Core/CLStateMachine.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Daemon/Positioning/MapMatching/CLGeoMapFeatureAccessGeometry.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Daemon/Positioning/MapMatching/CLGeoMapFeatureAccessGeometryPedestrian.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLPreferences.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CLClient_OSX.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLBackgroundActivitySession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLCondition.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLConditionLedger.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLGeocoder.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLIdentifiableClientConnectionManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLLocationManager_OSX.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLLocationUpdater.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLPlacemark.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLServiceSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Framework/CoreLocation/CLServiceSessionInternal.mm"
+ "23:10:16"
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 73,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 80,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 299,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 305,invalid index %zu >= %zu."
+ "Assertion failed: ldx < M*N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 86,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 72,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.x6XIQI/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 79,invalid row %zu > %zu."
+ "CL: CLPromoteSystemService"
+ "CLMM,%{public}.1lf,TEPA,XPC dispatch,roadID,%{private}llu,clRoadID,%{private}llu,projection,%{public}.3lf,snapCourse,%{public}.1lf"
+ "CLMM,%{public}.1lf,no TEPA,XPC scan returned nil"
+ "CLMM,%{public}.1lf,no TEPA,exit lat/lon are null-island in helper reply"
+ "CLMM,%{public}.1lf,no TEPA,gated by launch throttle,launchAge,%{public}.2lf,inFlight,%{public}d,succeeded,%{public}d"
+ "CLMM,%{public}s"
+ "CLMM,CLTSP,CLMapHelperService XPCService asynchronous TEPA tunnel scan error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "CLMM,CLTSP,CLMapHelperService XPCService synchronous TEPA tunnel scan error,%{public}lld,domain,%{public}@,description,\"%{private}@\""
+ "CLMM,CLTSP,MapHelperService,XPCService returned findTunnelEndPoint,success,%{public}d,responseTime,%{public}.1lf,syncCall,%{public}d"
+ "CLMM,CarPlayDRLowSpeedCourseUnc,suppressing override,speed,%{public}.2f,courseUnc,%{public}.1f"
+ "CLMM,fetchTunnelEndPointAssistance,anchor crumb invalid"
+ "CLMM,no TEPA,isTunnel,%{public}d,isSnapUsable,%{public}d,lastLaunchTime,%{public}.1lf,inFlight,%{public}d,succeeded,%{public}d"
+ "CLTSP,CLMM,MaphelperService,findTunnelEndPoint not supported on this platform"
+ "Jul 10 2026"
+ "bwdFailureReason"
+ "courseAtExitPoint"
+ "endPointDistanceFromCurrentSolution"
+ "failureReason"
+ "generateRouteSummary"
+ "isTunnelCurved"
+ "iterationsIn"
+ "iterationsOut"
+ "speedLimitMps"
+ "startLatitude"
+ "startLongitude"
+ "tunnelLength"
+ "tunnelWidthAtExitPoint"
+ "v132@?0B8{TunnelEndPositionAssistance=dddddddddBiBidddd}12"
+ "v16@?0@\"NSDictionary\"8"
+ "virtual void CLParticleMapMatcher::fetchTunnelEndPointAssistance(double, CLMapGeometryPtr, bool, CLTunnelEndPointReply)_block_invoke"
+ "void CLParticleMapMatcherCommon::SolutionPropagator::fetchTunnelEndPointAssistance(double, CLMapGeometryPtr, bool, CLTunnelEndPointReply)"
+ "void CLParticleMapMatcherCommon::SolutionPropagator::fetchTunnelEndPointAssistance(double, CLMapGeometryPtr, bool, CLTunnelEndPointReply)_block_invoke"
+ "{\"msg%{public}.0s\":\"CLPromoteSystemService\", \"event\":%{public, location:escape_only}s}"
- "+[CLMapsXPCServiceManager sharedInstance]"
- "-[CLMapsXPCServiceManager collectMapDataOfType:aroundCoordinate:inRadius:allowNetwork:preferCachedTiles:isPedestrianOrCycling:clearTiles:callSynchronously:WithReply:]_block_invoke"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Daemon/Core/CSI/CLMachThreadSupport.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Daemon/Positioning/GPS/Core/CLStateMachine.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Daemon/Positioning/MapMatching/CLGeoMapFeatureAccessGeometry.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Daemon/Positioning/MapMatching/CLGeoMapFeatureAccessGeometryPedestrian.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Daemon/Shared/Utilities/CLPreferences.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CLClient_OSX.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLBackgroundActivitySession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLCondition.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLConditionLedger.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLGeocoder.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLIdentifiableClientConnectionManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLLocationManager_OSX.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLLocationUpdater.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLPlacemark.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLServiceSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Framework/CoreLocation/CLServiceSessionInternal.mm"
- "21:37:25"
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 81,invalid col %zu > %zu."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 88,invalid col %zu > %zu."
- "Assertion failed: col > row, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 292,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 298,invalid index %zu >= %zu."
- "Assertion failed: ldx < M*N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 94,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 80,invalid row %zu > %zu."
- "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.BLYrY2/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 87,invalid row %zu > %zu."
- "CLMM,TEPA,incoming reached max iterations,%{public}d"
- "CLMM,TEPA,outgoing reached max iterations,%{public}d"
- "CLMM,TEPA,tunnel start point not found (TEPA exit point still valid),multi-inbound,%{public}d"
- "CLMM,getTunnelEndPointAssistance,m_current.crumb invalid"
- "CLMM,no TEPA,isTunnel,%{public}d,isSnapUsable,%{public}d,lastAssistanceTime,%{public}.1lf"
- "CLMM,no TEPA,multi-outbound,%{public}d"
- "CLTSP,constructRouteUsingFamiliarRoads,routeSummary,%{sensitive}s,tripID,%{public}s,attempt,%{public}d,percentageFamiliarRoads,%{public}.1f%%"
- "Jun 27 2026"
- "[CLPedestrianRTSSmoother]:[runRTS] Course offset is not initialized."
- "bool CLParticleMapMatcherCommon::SolutionPropagator::findTunnelEndPoint(double, CLGpsAssistant_Type::TunnelEndPositionAssistance &, CLMapGeometryPtr, bool)"
- "speedLimit"
- "virtual bool CLParticleMapMatcher::getTunnelEndPointAssistance(double, CLGpsAssistant_Type::TunnelEndPositionAssistance &)"
```
