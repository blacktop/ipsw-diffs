## wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

-280.0.0.0.0
-  __TEXT.__text: 0x2a201c
+281.0.0.0.0
+  __TEXT.__text: 0x2a1254
   __TEXT.__auth_stubs: 0x4710
   __TEXT.__objc_stubs: 0xcca0
   __TEXT.__init_offsets: 0x23c
   __TEXT.__objc_methlist: 0x612c
-  __TEXT.__gcc_except_tab: 0x245bc
-  __TEXT.__const: 0x125ff
-  __TEXT.__cstring: 0x15702
-  __TEXT.__oslogstring: 0x264d8
+  __TEXT.__gcc_except_tab: 0x245fc
+  __TEXT.__const: 0x1265f
+  __TEXT.__cstring: 0x12bdc
+  __TEXT.__oslogstring: 0x267d8
   __TEXT.__objc_methname: 0x148c5
   __TEXT.__objc_classname: 0x175e
   __TEXT.__objc_methtype: 0x369a

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0xd6c0
+  __TEXT.__unwind_info: 0xd6b8
   __TEXT.__eh_frame: 0x55f0
   __DATA_CONST.__auth_got: 0x23a0
   __DATA_CONST.__got: 0x10b0
   __DATA_CONST.__auth_ptr: 0x760
-  __DATA_CONST.__const: 0x12788
+  __DATA_CONST.__const: 0x127a8
   __DATA_CONST.__cfstring: 0x5b40
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_protolist: 0x188

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1747399F-0461-397C-B22C-CAD763AEDE74
-  Functions: 11801
+  UUID: 61C9DBFA-412D-3C82-9E82-F9CD758EBEB5
+  Functions: 11811
   Symbols:   1852
-  CStrings:  9545
+  CStrings:  9523
 
CStrings:
+ " timing_error_ms:"
+ "#D Horizontal accuracy from micro tile = %lf, interemediate tile = %lf"
+ "#I A Geoservices request is in progress, queueing the location"
+ "#I Evaluating pending location change updates, found = %lu"
+ "#I Evaluating the location update - latitude:%{sensitive}lf, longitude: %{sensitive}lf, horizontalAccuracy = %lf"
+ "#I Reached the max pending location update queue size, trying GeoServices updates again"
+ "#I Received location update - latitude:%{sensitive}lf, longitude: %{sensitive}lf, horizontalAccuracy = %lf"
+ "#I Setting Horizontal Accuracy to : %u"
+ "#I Using the last received update - latitude:%{sensitive}lf, longitude: %{sensitive}lf, horizontalAccuracy = %lf"
+ "#I currentLatitude = %{sensitive}lf, latfromIntermediateTile = %{sensitive}lf, currentLong = %{sensitive}lf, longfromIntermediateTile = %{sensitive}lf"
+ "#I currentLatitude = %{sensitive}lf, latfromMicroTile = %{sensitive}lf, currentLong = %{sensitive}lf, longFromMicroTile = %{sensitive}lf"
+ "#I horizontalAccuracy = %lf, distanceChangedMicroTile = %lf, distanceChangedIntermediateTile = %lf"
+ "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "281"
+ "281~17"
+ "Horizontal accuracy of lat/long that are used to fetch micro and intermediate tiles are different"
+ "SAR_REPORT_TIMING_ERROR"
+ "WISABC:Exception while reading timing_error_ms metric field for %s"
+ "timing_error_ms"
- "#I Handling update location - latitude:%{sensitive}lf, longitude: %{sensitive}lf, horizontalAccuracy = %lf"
- "#I currentLatitude = %lf, latfromIntermediateTile = %lf, currentLong = %lf, longfromIntermediateTile = %lf"
- "#I currentLatitude = %lf, latfromMicroTile = %lf, currentLong = %lf, longFromMicroTile = %lf"
- "#I horizontalAccuracy = %lf, distanceChangedIntermediateTile = %lf"
- "#I horizontalAccuracy = %lf, distanceChangedMicroTile = %lf"
- "/AppleInternal/Library/BuildRoots/4~CI6QugDQ82lmj6u7WLpsz-dKvtJ2SUbtFRi0TU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "280"
- "280~17"

```
