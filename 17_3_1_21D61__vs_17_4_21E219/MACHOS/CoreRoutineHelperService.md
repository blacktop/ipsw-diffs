## CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService`

```diff

-896.0.1.0.1
-  __TEXT.__text: 0x105d8
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x2880
-  __TEXT.__objc_methlist: 0x95c
+900.0.12.0.0
+  __TEXT.__text: 0x1141c
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_stubs: 0x2a00
+  __TEXT.__objc_methlist: 0x974
   __TEXT.__const: 0x138
-  __TEXT.__oslogstring: 0xe24
+  __TEXT.__oslogstring: 0xebe
   __TEXT.__cstring: 0xe48
-  __TEXT.__objc_methname: 0x4e02
+  __TEXT.__objc_methname: 0x50da
   __TEXT.__objc_classname: 0x351
-  __TEXT.__objc_methtype: 0x25c4
+  __TEXT.__objc_methtype: 0x276d
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__auth_got: 0x378
+  __TEXT.__unwind_info: 0x344
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x4d8
+  __DATA_CONST.__const: 0x578
   __DATA_CONST.__cfstring: 0xb60
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_classrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2fe8
-  __DATA.__objc_selrefs: 0xeb8
-  __DATA.__objc_protorefs: 0xa0
-  __DATA.__objc_classrefs: 0x1d0
-  __DATA.__objc_superrefs: 0x48
+  __DATA.__objc_const: 0x30e8
+  __DATA.__objc_selrefs: 0xf20
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x990

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 232
-  Symbols:   203
-  CStrings:  1150
+  Functions: 238
+  Symbols:   206
+  CStrings:  1183
 
Symbols:
+ _OBJC_CLASS_$_GEOSpatialLookupParameters
+ _OBJC_CLASS_$_RTPointOfInterestAttributes
+ _objc_retain_x9
CStrings:
+ "%@, POI attributes, %@"
+ "%@, found geoMapItem, muid, %lu, category, %@"
+ "%@, muid, %lu, geoMapItem count, %lu, error, %@"
+ "%@, muid, %lu, nearby POI count, %lu"
+ "T@\"NSString\",?,R,C"
+ "_amenities"
+ "_hasAnyAmenities"
+ "_hasMUID"
+ "_hasResultProviderID"
+ "fetchPlaceInferenceQueriesWithDateInterval:ascending:reply:"
+ "fetchPointOfInterestAttributesWithIdentifier:options:handler:"
+ "fetchPointOfInterestAttributesWithIdentifier:reply:"
+ "fetchPointOfInterestsAroundCoordinate:radius:options:handler:"
+ "fetchPointOfInterestsAroundCoordinate:radius:reply:"
+ "initWithApplePaySupport:category:muid:nearbyPoiCount:"
+ "initWithCoordinate:radius:categories:"
+ "initializeAndStartSessionWithConfiguration:handler:"
+ "isApplePayAmenity"
+ "mapItemsForParameters:"
+ "numberWithUnsignedLongLong:"
+ "startSamplingPointOfInterestWithInterval:handler:"
+ "stopSamplingPointOfInterest:"
+ "ticketForMUIDs:traits:"
+ "ticketForSpatialLookupParameters:traits:"
+ "v32@0:8Q16@?<v@?@\"RTPointOfInterestAttributes\"@\"NSError\">24"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?@\"NSError\">24"
+ "v36@0:8@\"NSDateInterval\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v40@0:8@\"RTCoordinate\"16d24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8Q16@\"RTMapServiceOptions\"24@?<v@?@\"RTPointOfInterestAttributes\"@\"NSError\">32"
+ "v40@0:8Q16@24@?32"
+ "v48@0:8@\"RTCoordinate\"16d24@\"RTMapServiceOptions\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16d24@32@?40"

```
