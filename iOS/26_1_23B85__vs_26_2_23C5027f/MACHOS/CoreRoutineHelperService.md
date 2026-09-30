## CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService`

```diff

-1069.0.4.0.0
-  __TEXT.__text: 0x884d4
+1070.0.1.0.1
+  __TEXT.__text: 0x89360
   __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_stubs: 0x50c0
+  __TEXT.__objc_stubs: 0x51a0
   __TEXT.__objc_methlist: 0x2d8c
   __TEXT.__const: 0x13b0
-  __TEXT.__cstring: 0x2396
-  __TEXT.__oslogstring: 0x2456
+  __TEXT.__cstring: 0x245c
+  __TEXT.__oslogstring: 0x25ee
   __TEXT.__objc_classname: 0x578
-  __TEXT.__objc_methname: 0x88ea
-  __TEXT.__objc_methtype: 0x38e5
+  __TEXT.__objc_methname: 0x89de
+  __TEXT.__objc_methtype: 0x38ed
   __TEXT.__gcc_except_tab: 0x21b0
   __TEXT.__unwind_info: 0xf90
   __DATA_CONST.__auth_got: 0x6f0
-  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__got: 0x450
   __DATA_CONST.__const: 0xed8
-  __DATA_CONST.__cfstring: 0x1920
+  __DATA_CONST.__cfstring: 0x1a40
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xe8

   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA.__objc_const: 0x32c8
-  __DATA.__objc_selrefs: 0x2280
+  __DATA.__objc_selrefs: 0x22b8
   __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x910
   __DATA.__data: 0xbc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4A6DF4B-E83C-39D4-9004-83888E06B80E
+  UUID: 3D42A285-DB9A-3414-B7BC-26BD279F9F5C
   Functions: 1038
-  Symbols:   421
-  CStrings:  2341
+  Symbols:   422
+  CStrings:  2372
 
Symbols:
+ _OBJC_CLASS_$_NSKeyedUnarchiver
Functions:
~ sub_1000013e8 : 22692 -> 22708
~ sub_10000aeb0 -> sub_10000aec0 : 344 -> 348
~ sub_100018630 -> sub_100018644 : 368 -> 360
~ sub_10001dd7c -> sub_10001dd88 : 1428 -> 3108
~ sub_100021b7c -> sub_100022218 : 3104 -> 5112
~ sub_10002bd3c -> sub_10002cbb0 : 416 -> 420
~ sub_10005914c -> sub_100059fc4 : 364 -> 372
~ sub_100062980 -> sub_100063800 : 2696 -> 2700
~ sub_100063408 -> sub_10006428c : 504 -> 508
~ sub_1000772d4 -> sub_10007815c : 7400 -> 7404
CStrings:
+ "%@, compiledModelURL, %@, size, %.1f (kB), featureToHashedApMappingDataURL, %@, size, %.1f (kB)"
+ "%@, featureToHashedApMapping is nil after recovery attempt"
+ "%@, hashedApToModelMapping is nil after recovery attempt"
+ "%@, hashedApToModelMappingDataURL, %@, size, %.1f (kB)"
+ "%@, recovered featureToHashedApMapping, %@, from URL, %@, error, %@"
+ "%@, recovered hashedApToModelMapping, %@, from URL, %@, error, %@"
+ "%@, remove existing compiled model or metadata, %@, error, %@"
+ "%@, single-model tile, %{sensitive}@"
+ "%@-%lu.bin"
+ "%@.bin"
+ ".bin"
+ ".mlmodelc"
+ "/AppleInternal/Library/BuildRoots/4~CBNaugD45XVXvk_3piXtou_QVBf82TS_GelF6Pg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CBNaugD45XVXvk_3piXtou_QVBf82TS_GelF6Pg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "anyObject"
+ "contentsOfDirectoryAtPath:error:"
+ "failed to archive featureToHashedApMapping"
+ "failed to archive hashedApToModelMapping"
+ "failed to save featureToHashedApMapping"
+ "failed to save hashedApToModelMapping"
+ "featureToHashedApMappingDataURL"
+ "hasSuffix:"
+ "hashedApToModelMappingDataURL"
+ "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashedApToModelMappingDataURL:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
+ "initWithIdentifier:featureToHashedApMapping:featureToHashedApMappingDataURL:url:"
+ "unarchivedObjectOfClasses:fromData:error:"
+ "writeToFile:atomically:"
+ "{polygon<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>, true, true, std::vector, std::vector, std::allocator, std::allocator>={ring<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>, true, true, std::vector, std::allocator>=^v^v{?=^v}}{vector<boost::geometry::model::ring<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>>, std::allocator<boost::geometry::model::ring<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>>>>=^v^v{?=^v}}}24@0:8@16"
- "%@, compiledModelURL, %@, size, %.1f (kB)"
- "%@, remove existing compiled model, %@, error, %@"
- "/AppleInternal/Library/BuildRoots/4~CAohugBgcvY2d3fQkChIpRuDUti1iqMghFcjgVY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "/AppleInternal/Library/BuildRoots/4~CAohugBgcvY2d3fQkChIpRuDUti1iqMghFcjgVY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "initWithIdentifier:apToModelMapping:date:downloadKey:geoCacheInfo:geoTileKey:hashedApToModelMapping:hashSalt:modelCalibrationParameters:models:modelURLs:pointsOfInterest:singlePOIMuid:size:"
- "initWithIdentifier:featureToHashedApMapping:url:"
- "{polygon<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>, true, true, std::vector, std::vector, std::allocator, std::allocator>={ring<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>, true, true, std::vector, std::allocator>=^v^v^v}{vector<boost::geometry::model::ring<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>>, std::allocator<boost::geometry::model::ring<boost::geometry::model::point<double, 2, boost::geometry::cs::spherical_equatorial<boost::geometry::degree>>>>>=^v^v^v}}24@0:8@16"

```
