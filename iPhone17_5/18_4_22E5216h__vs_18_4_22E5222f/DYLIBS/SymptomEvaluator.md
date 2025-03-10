## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomEvaluator.framework/SymptomEvaluator`

```diff

-2022.100.25.0.0
-  __TEXT.__text: 0x258ee8
-  __TEXT.__auth_stubs: 0x22e0
-  __TEXT.__objc_methlist: 0x17290
-  __TEXT.__cstring: 0x23957
+2022.100.26.0.0
+  __TEXT.__text: 0x259a08
+  __TEXT.__auth_stubs: 0x2320
+  __TEXT.__objc_methlist: 0x17298
+  __TEXT.__cstring: 0x239d4
   __TEXT.__const: 0xab8
-  __TEXT.__gcc_except_tab: 0x5218
-  __TEXT.__oslogstring: 0x40c55
+  __TEXT.__gcc_except_tab: 0x5288
+  __TEXT.__oslogstring: 0x40e8b
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.evaluator_cfg: 0x6417
   __TEXT.default_clp: 0x2fe0

   __TEXT.bb_MAV_clp: 0xa690
   __TEXT.bb_INT_clp: 0x68e0
   __TEXT.modules_clp: 0x16e0
-  __TEXT.__unwind_info: 0x66c8
+  __TEXT.__unwind_info: 0x66e0
   __TEXT.__objc_classname: 0x1d37
-  __TEXT.__objc_methname: 0x3b996
-  __TEXT.__objc_methtype: 0x6a34
-  __TEXT.__objc_stubs: 0x251a0
+  __TEXT.__objc_methname: 0x3ba58
+  __TEXT.__objc_methtype: 0x6a83
+  __TEXT.__objc_stubs: 0x25240
   __DATA_CONST.__got: 0xdf0
-  __DATA_CONST.__const: 0x6508
+  __DATA_CONST.__const: 0x6558
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc7a0
+  __DATA_CONST.__objc_selrefs: 0xc7d0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x588
   __DATA_CONST.__objc_arraydata: 0x810
-  __AUTH_CONST.__auth_got: 0x1188
+  __AUTH_CONST.__auth_got: 0x11a8
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x2360
-  __AUTH_CONST.__cfstring: 0x1c9e0
-  __AUTH_CONST.__objc_const: 0x3b0a0
+  __AUTH_CONST.__cfstring: 0x1ca20
+  __AUTH_CONST.__objc_const: 0x3b0c0
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_dictobj: 0x898
   __AUTH_CONST.__objc_intobj: 0x780
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH.__objc_data: 0x1568
-  __DATA.__objc_ivar: 0x2ccc
+  __DATA.__objc_ivar: 0x2cd0
   __DATA.__data: 0x1c60
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x358

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10909
-  Symbols:   12351
-  CStrings:  22374
+  Functions: 10916
+  Symbols:   12362
+  CStrings:  22397
 
Symbols:
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
CStrings:
+ "\x1f\x02\x12"
+ "0123456789bcdefghjkmnpqrstuvwxyz"
+ "@40@0:8Q16d24d32"
+ "CLGeocoder"
+ "CLLocation"
+ "GeoIP: Computed geohash for latitude: %f, longitude: %f, hashLength: %zu, geohash: %@"
+ "GeoIP: Computing geohash for latitude: %f, longitude: %f, hashLength: %zu"
+ "GeoIP: Failed to get location, error: %@"
+ "GeoIP: Failed to load CLLocation or CLGeocoder"
+ "GeoIP: Helper takes over Biome donation for EdgeSelection with prefix: %{private}@, interface: %@, radio: %@, band: %@, latitude: %{private}f, longitude: %{private}f, elapsed/threshold: %f/%d sec"
+ "GeoIP: Missing geohash: %@, return"
+ "GeoIP: Missing isoCountryCode: %@ or city: %@, return"
+ "GeoIP: Reverse geocoding city: %{private}@, countryCode: %{private}@"
+ "GeoIP: Reverse geocoding failed, error: %@"
+ "GeoIP: Successfully loaded CLLocation and CLGeocoder"
+ "GeoIP: Timed out waiting for reverse geocoding, error: %ld"
+ "ISOcountryCode"
+ "Invalid parameter not satisfying: %@"
+ "coordinate"
+ "coordinatesToGeoHashWithLength:latitude:longitude:"
+ "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:"
+ "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:latitude:longitude:reply:"
+ "hashLength <= GEOHASH_MAX_LENGTH"
+ "initWithLatitude:longitude:"
+ "locality"
+ "reverseGeocodeLocation:completionHandler:"
+ "v64@0:8@16@24@32@40d48d56"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40d48d56@?<v@?@\"NSDictionary\"@\"NSError\">64"
+ "v72@0:8@16@24@32@40d48d56@?64"
- "\x1f\x01\x12"
- "GeoIP: Helper takes over Biome donation for EdgeSelection with prefix: %{private}@, interface: %@, radio: %@, band: %@, elapsed/threshold: %f/%d sec"
- "GeoIP: Missing isoCountryCode: %@, return"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:"
- "donateBiomeEventForEdgeSelectionWithPrefix:interfaceType:radioType:radioBand:reply:"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?@\"NSDictionary\"@\"NSError\">48"

```
