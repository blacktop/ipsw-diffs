## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2903.30.6.6.6
-  __TEXT.__text: 0x7fc40
+2905.30.6.20.7
+  __TEXT.__text: 0x7ffe8
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x8380
+  __TEXT.__objc_methlist: 0x83c0
   __TEXT.__const: 0x290
   __TEXT.__cstring: 0x5fb3
-  __TEXT.__oslogstring: 0x8130
-  __TEXT.__gcc_except_tab: 0x1270
+  __TEXT.__oslogstring: 0x81d6
+  __TEXT.__gcc_except_tab: 0x1288
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__ustring: 0x2b2
-  __TEXT.__unwind_info: 0x1e50
+  __TEXT.__unwind_info: 0x1e70
   __TEXT.__objc_classname: 0x12bb
-  __TEXT.__objc_methname: 0x119d4
-  __TEXT.__objc_methtype: 0x34a0
-  __TEXT.__objc_stubs: 0xcde0
-  __DATA_CONST.__got: 0x6b0
+  __TEXT.__objc_methname: 0x11aac
+  __TEXT.__objc_methtype: 0x34b0
+  __TEXT.__objc_stubs: 0xcee0
+  __DATA_CONST.__got: 0x6b8
   __DATA_CONST.__const: 0x2f20
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43b0
+  __DATA_CONST.__objc_selrefs: 0x43f0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x358
-  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0xc60
   __AUTH_CONST.__cfstring: 0x4400
-  __AUTH_CONST.__objc_const: 0xd6e0
-  __AUTH_CONST.__objc_intobj: 0x228
+  __AUTH_CONST.__objc_const: 0xd6f0
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x14a0

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7CA1665-9AB2-3A7D-A74B-2F83BB2486C2
-  Functions: 2887
-  Symbols:   10100
-  CStrings:  5405
+  UUID: 8103149F-5FAB-3CB1-8F29-B05FDFCB5BE4
+  Functions: 2892
+  Symbols:   10119
+  CStrings:  5416
 
Symbols:
+ +[MSPSharedTripReceiverCapabilities luckierReceiverCapabilities]
+ -[GEOSharedNavState(MSPExtras) _polylineCoordinateForRoute:]
+ -[GEOSharedNavState(MSPExtras) setComposedRouteFromState:]
+ -[GEOSharedNavState(MSPExtras) updateElevationModelToLegacyEGM96]
+ -[MSPSharedTripReceiverCapabilities supportsWGS84ElevationModel]
+ _IDSRegistrationPropertySupportsMapsWGS84ElevationModel
+ _objc_msgSend$_polylineCoordinateForRoute:
+ _objc_msgSend$endRouteCoordinate
+ _objc_msgSend$initWithRoute:range:desiredElevationModel:
+ _objc_msgSend$luckierReceiverCapabilities
+ _objc_msgSend$rawData
+ _objc_msgSend$setComposedRouteFromState:
+ _objc_msgSend$supportsWGS84ElevationModel
+ _objc_msgSend$updateElevationModelToLegacyEGM96
- GCC_except_table25
CStrings:
+ "_polylineCoordinateForRoute:"
+ "endRouteCoordinate"
+ "initWithRoute:range:desiredElevationModel:"
+ "luckierReceiverCapabilities"
+ "polylineCoordinateForRoute closest index %lu, sourced from route + latlng"
+ "polylineCoordinateForRoute no valid closest index, will use whole route (sender provided: %@)"
+ "rawData"
+ "setComposedRouteFromState:"
+ "supportsWGS84ElevationModel"
+ "updateElevationModelToLegacyEGM96"
+ "updateElevationModelToLegacyEGM96 early exit: closestPointOnRoute returned GEOPolylineCoordinateInvalid"
+ "updateElevationModelToLegacyEGM96 early exit: no composed route"
+ "{?=If}24@0:8@16"
- "truncatePointDataForPrivacy closest index %lu, sourced from route + latlng"
- "truncatePointDataForPrivacy no valid closest index, will use whole route (sender provided: %@)"

```
