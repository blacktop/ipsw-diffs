## CoreRoutineHelperService

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/XPCServices/CoreRoutineHelperService.xpc/CoreRoutineHelperService`

```diff

-1071.0.1.0.0
-  __TEXT.__text: 0x89374
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_stubs: 0x51a0
-  __TEXT.__objc_methlist: 0x2d8c
-  __TEXT.__const: 0x13b0
-  __TEXT.__cstring: 0x245c
-  __TEXT.__oslogstring: 0x25ee
-  __TEXT.__objc_classname: 0x578
-  __TEXT.__objc_methname: 0x89de
-  __TEXT.__objc_methtype: 0x38ed
-  __TEXT.__gcc_except_tab: 0x21b0
-  __TEXT.__unwind_info: 0xf90
-  __DATA_CONST.__auth_got: 0x6f0
-  __DATA_CONST.__got: 0x450
+1072.0.5.0.1
+  __TEXT.__text: 0x8e084
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_stubs: 0x5300
+  __TEXT.__objc_methlist: 0x2dec
+  __TEXT.__const: 0x13c0
+  __TEXT.__cstring: 0x4059
+  __TEXT.__oslogstring: 0x268d
+  __TEXT.__objc_classname: 0x589
+  __TEXT.__objc_methname: 0x8bf1
+  __TEXT.__objc_methtype: 0x398b
+  __TEXT.__gcc_except_tab: 0x21a0
+  __TEXT.__unwind_info: 0x1040
+  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xed8
   __DATA_CONST.__cfstring: 0x1a40
   __DATA_CONST.__objc_classlist: 0xe8
-  __DATA_CONST.__objc_catlist: 0x60
+  __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc0

   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0x32c8
-  __DATA.__objc_selrefs: 0x22b8
+  __DATA.__objc_const: 0x3330
+  __DATA.__objc_selrefs: 0x2338
   __DATA.__objc_ivar: 0x140
   __DATA.__objc_data: 0x910
   __DATA.__data: 0xbc0

   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20619354-F2D9-344B-9EAE-12048E94D60C
-  Functions: 1038
-  Symbols:   423
-  CStrings:  2372
+  UUID: E6A5F79D-AB57-34D1-9EBB-E6F2FE922ADE
+  Functions: 1045
+  Symbols:   422
+  CStrings:  2417
 
Symbols:
+ _OBJC_CLASS_$_CLGeocoder
+ _OBJC_CLASS_$_CLLocation
+ _OBJC_CLASS_$_RTBusinessHours
+ _OBJC_CLASS_$_RTDailyHours
+ _OBJC_CLASS_$_RTLocalTimeInterval
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
- _rand
CStrings:
+ "%@, confidenceWeight, %.2f, businessHours, %.2f, duration, %.2f, muid, %lu, hasBusinessHours, %@"
+ "%@, dailyHours weekday, %lu, compareDate weekday, %lu"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1530: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugC9rPBK6IkiopftqRaaHfPQx9QFBm-0HJk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "@48@0:8@16@24@32^@40"
+ "Failed to create BluePOI model directory: %@"
+ "GeoBusinessHours"
+ "_timeZoneAtLocation:"
+ "businessHours"
+ "businessHoursFromGEOBusinessHours:"
+ "category"
+ "confidenceWeightForMapItem:startDate:endDate:"
+ "d40@0:8@16@24@32"
+ "dailyHours"
+ "fetchGeoMapItemWithMUID:options:handler:"
+ "fetchVisitWithIdentifier:reply:"
+ "initWithHoursType:dailyHours:"
+ "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:"
+ "initWithStartTime:endTime:"
+ "initWithWeekday:timeIntervals:"
+ "insideRTBusinessHours:date:timeZone:"
+ "processTile:fileManager:cacheDirectory:error:"
+ "setMallocStackLoggingEnabled:mode:handler:"
+ "simulateGeneratedTripSegment:withCallback:"
+ "startMonitoringForGeneratedTripSegmentsWithReply:"
+ "stopMonitoringForGeneratedTripSegmentsWithReply:"
+ "timeIntervals"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"RTVisit\"@\"NSError\">24"
+ "v32@0:8@\"RTTripSegment\"16@?<v@?@\"RTTripSegment\"@\"NSError\">24"
+ "v36@0:8B16q20@?28"
+ "v36@0:8B16q20@?<v@?@\"NSError\">28"
+ "v40@0:8Q16@\"RTMapServiceOptions\"24@?<v@?@\"<GEOMapItem>\"@\"NSError\">32"
+ "weightBasedOnRTBusinessHours:startDate:endDate:timeZone:metrics:"
- "%@, internalInstall, %@, sampled, %@"
- "/AppleInternal/Library/BuildRoots/4~CG7hugDyb2uzsi_OhdrtNXcCA8wu0RoXOwRjtQU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "/AppleInternal/Library/BuildRoots/4~CG7hugDyb2uzsi_OhdrtNXcCA8wu0RoXOwRjtQU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "B20@0:8B16"
- "fetchConfidenceWeightForMapItem:startDate:endDate:options:handler:"
- "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
- "processTile:fileManager:error:"
- "shouldFilterByBusinessHours:"
- "v56@0:8@\"RTMapItem\"16@\"NSDate\"24@\"NSDate\"32@\"RTMapServiceOptions\"40@?<v@?@\"NSNumber\"@\"NSError\">48"

```
