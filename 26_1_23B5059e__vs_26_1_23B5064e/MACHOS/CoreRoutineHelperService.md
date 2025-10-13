## CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService`

```diff

-1069.0.1.0.0
-  __TEXT.__text: 0x87300
-  __TEXT.__auth_stubs: 0xdc0
+1069.0.2.0.0
+  __TEXT.__text: 0x884d4
+  __TEXT.__auth_stubs: 0xdb0
   __TEXT.__objc_stubs: 0x50c0
-  __TEXT.__objc_methlist: 0x2d74
-  __TEXT.__const: 0x1300
-  __TEXT.__cstring: 0x2163
-  __TEXT.__oslogstring: 0x23e9
+  __TEXT.__objc_methlist: 0x2d8c
+  __TEXT.__const: 0x13b0
+  __TEXT.__cstring: 0x2396
+  __TEXT.__oslogstring: 0x2456
   __TEXT.__objc_classname: 0x578
-  __TEXT.__objc_methname: 0x8843
-  __TEXT.__objc_methtype: 0x38c2
-  __TEXT.__gcc_except_tab: 0x2114
-  __TEXT.__unwind_info: 0xf38
-  __DATA_CONST.__auth_got: 0x6f8
+  __TEXT.__objc_methname: 0x88ea
+  __TEXT.__objc_methtype: 0x38e5
+  __TEXT.__gcc_except_tab: 0x21b0
+  __TEXT.__unwind_info: 0xf90
+  __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0xdc0
-  __DATA_CONST.__cfstring: 0x18e0
+  __DATA_CONST.__const: 0xed8
+  __DATA_CONST.__cfstring: 0x1920
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x108
-  __DATA_CONST.__objc_doubleobj: 0x30
+  __DATA_CONST.__objc_doubleobj: 0x40
   __DATA.__objc_const: 0x32c8
-  __DATA.__objc_selrefs: 0x2270
+  __DATA.__objc_selrefs: 0x2280
   __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x910
   __DATA.__data: 0xbc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B60EEA0E-BE98-3792-A2F6-D1F6BDF1DB3D
-  Functions: 1021
-  Symbols:   422
-  CStrings:  2329
+  UUID: 34416211-5211-336B-A7AA-D62BC60C41A2
+  Functions: 1038
+  Symbols:   421
+  CStrings:  2341
 
Symbols:
- _objc_retain_x7
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B_ZjugBzhk30cJAuV_0boJ31mX9g7luphswv78k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B_ZjugBzhk30cJAuV_0boJ31mX9g7luphswv78k/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "@48@0:8@16@24^@32^@40"
+ "@64@0:8@16@24@32@40@48@56"
+ "AOI inference error"
+ "AOI inference error: %@"
+ "Boost.Geometry Empty-Input exception"
+ "Distance to AOI boundary: %.21f, isInsideAOI: %@"
+ "NSPOSIXErrorDomain"
+ "Polygonal BluePOI Results: %@, distanceToNearestAOILowerBound: %@"
+ "categoryFilteredLocalBluePOIResultWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:bluePOITile:"
+ "computeOverlapForLocation:withGEOBluePOIAOIPolygon:distanceToAOIBoundary:"
+ "d40@0:8@16@24^@32"
+ "hasAOIInferenceError"
+ "hasStorageFullError"
+ "inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:refreshAOI:handler:"
+ "inferLocalPolygonalBluePOIsWithReferenceLocation:queryTime:distanceToNearestAOILowerBound:error:"
+ "initWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:"
+ "v64@0:8@\"RTLocation\"16@\"NSArray\"24@\"NSArray\"32@\"RTBluePOITile\"40i48B52@?<v@?@\"RTLocalBluePOIResult\"@\"NSError\">56"
+ "v64@0:8@16@24@32@40i48B52@?56"
+ "void boost::geometry::detail::throw_on_empty_input(const Geometry &) [Geometry = boost::geometry::model::polygon<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>>]"
- "/AppleInternal/Library/BuildRoots/4~B-4HugCC6UNFM-9d-vSyQVupnhUBwscO85SwZ3Q/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "@56@0:8@16@24@32@40@48"
- "Polygonal BluePOI Results: %@"
- "categoryFilteredLocalBluePOIResultWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:bluePOITile:"
- "computeOverlapForLocation:withGEOBluePOIAOIPolygon:"
- "d32@0:8@16@24"
- "inferLocalBluePOIWithReferenceLocation:locations:accessPoints:bluePOITile:signalEnv:handler:"
- "inferLocalPolygonalBluePOIsWithReferenceLocation:queryTime:error:"
- "initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:"
- "v60@0:8@\"RTLocation\"16@\"NSArray\"24@\"NSArray\"32@\"RTBluePOITile\"40i48@?<v@?@\"RTLocalBluePOIResult\"@\"NSError\">52"
- "v60@0:8@16@24@32@40i48@?52"

```
