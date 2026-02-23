## wirelessinsightsd

> `/System/Library/Frameworks/WirelessInsights.framework/Support/wirelessinsightsd`

```diff

-278.0.0.0.0
-  __TEXT.__text: 0x2a2188
+280.0.0.0.0
+  __TEXT.__text: 0x2a201c
   __TEXT.__auth_stubs: 0x4710
   __TEXT.__objc_stubs: 0xcca0
   __TEXT.__init_offsets: 0x23c
   __TEXT.__objc_methlist: 0x612c
-  __TEXT.__gcc_except_tab: 0x245a0
-  __TEXT.__const: 0x1253f
-  __TEXT.__cstring: 0x156c2
-  __TEXT.__oslogstring: 0x26478
-  __TEXT.__objc_methname: 0x14695
-  __TEXT.__objc_classname: 0x171e
+  __TEXT.__gcc_except_tab: 0x245bc
+  __TEXT.__const: 0x125ff
+  __TEXT.__cstring: 0x15702
+  __TEXT.__oslogstring: 0x264d8
+  __TEXT.__objc_methname: 0x148c5
+  __TEXT.__objc_classname: 0x175e
   __TEXT.__objc_methtype: 0x369a
-  __TEXT.__swift5_typeref: 0x1ec8
-  __TEXT.__swift5_reflstr: 0x4d63
+  __TEXT.__swift5_typeref: 0x1eba
+  __TEXT.__swift5_reflstr: 0x4d83
   __TEXT.__swift5_assocty: 0x260
-  __TEXT.__constg_swiftt: 0x3434
-  __TEXT.__swift5_fieldmd: 0x33c0
-  __TEXT.__swift5_capture: 0xe14
+  __TEXT.__constg_swiftt: 0x3448
+  __TEXT.__swift5_fieldmd: 0x33cc
+  __TEXT.__swift5_capture: 0xe24
   __TEXT.__swift5_proto: 0x434
   __TEXT.__swift5_types: 0x248
   __TEXT.__swift_as_entry: 0x318

   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_mpenum: 0x1c
   __TEXT.__unwind_info: 0xd6c0
-  __TEXT.__eh_frame: 0x55c8
+  __TEXT.__eh_frame: 0x55f0
   __DATA_CONST.__auth_got: 0x23a0
   __DATA_CONST.__got: 0x10b0
   __DATA_CONST.__auth_ptr: 0x760
-  __DATA_CONST.__const: 0x126c8
+  __DATA_CONST.__const: 0x12788
   __DATA_CONST.__cfstring: 0x5b40
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x98

   __DATA_CONST.__objc_arrayobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x10900
+  __DATA.__objc_const: 0x10bd0
   __DATA.__objc_selrefs: 0x38a0
   __DATA.__objc_ivar: 0x8a0
-  __DATA.__objc_data: 0x3e00
-  __DATA.__data: 0x5b68
-  __DATA.__bss: 0x65b8
-  __DATA.__common: 0x488
+  __DATA.__objc_data: 0x3e50
+  __DATA.__data: 0x5b28
+  __DATA.__bss: 0x65a8
+  __DATA.__common: 0x528
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0E4A485B-FA52-3754-9AF8-76D37750AF30
-  Functions: 11802
-  Symbols:   1851
-  CStrings:  9524
+  UUID: 1747399F-0461-397C-B22C-CAD763AEDE74
+  Functions: 11801
+  Symbols:   1852
+  CStrings:  9545
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftSpatial
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CI6QugDQ82lmj6u7WLpsz-dKvtJ2SUbtFRi0TU8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJI2ugCKDcCXPu-IoQ0pYZ8-K8k51fjyXridEr8/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/AwdOptions.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/AwddMetricsGeneral.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/CellularServiceStatus.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/MetricFile.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/MetricLogHeader.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/Generated/Insights/DecisionTreeModel.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/Generated/Insights/GeoServicesDefinitions.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/Generated/Insights/InsightsDefinitions.pb.cc"
+ "/Library/Caches/com.apple.xbs/725A61D6-F442-463E-AD48-CDDDFE2051D8/TemporaryDirectory.PaPbtL/Sources/WirelessInsightsExecutables/Source/Reflection/VectorOutputStream.cpp"
+ "/Library/Caches/com.apple.xbs/C38F33FA-9649-41F3-A8DB-5386F5E59392/TemporaryDirectory.DPsTLg/Sources/WirelessInsights/AWDMetrics/cpp/AwdProfile.pb.cc"
+ "280"
+ "280~17"
+ "Backfilled time to RNF with %s for queued event"
+ "_TtCV17wirelessinsightsd20WiFiToCellTransition15TransitionEvent"
+ "actualTransitionWeekday"
+ "alternatePathAdviceLevel"
+ "cellularNasPagingRepeatInterval"
+ "dropReason"
+ "dropSubreason"
+ "eventTimestamp"
+ "isPredictingWalkout"
+ "isTransition"
+ "loc.mgr:#N Failed location update from locationd, error: %@"
+ "predictedWalkoutProbability"
+ "predictionIsTriggeredProactively"
+ "secondsFromEventToRnfOn"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1420: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CH5SugCT0NgwF-6W3q2N0a2xa95GZ2MDabDysTE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CHnfugBQfFiUsKTOUfg69qHXhLEu9BfmOtFN7Ag/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/Library/Caches/com.apple.xbs/2B844BA2-544C-4BAA-B8CD-C1D927424A9B/TemporaryDirectory.w1R5MH/Sources/WirelessInsights/AWDMetrics/cpp/AwdProfile.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/AwdOptions.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/AwddMetricsGeneral.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/CellularServiceStatus.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/MetricFile.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/AWDMetrics/cpp/MetricLogHeader.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/Generated/Insights/DecisionTreeModel.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/Generated/Insights/GeoServicesDefinitions.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/Generated/Insights/InsightsDefinitions.pb.cc"
- "/Library/Caches/com.apple.xbs/D7FAA3E7-A423-4A7D-8721-05587ACADA53/TemporaryDirectory.M0iOUW/Sources/WirelessInsightsExecutables/Source/Reflection/VectorOutputStream.cpp"
- "278"
- "278~14"
- "loc.mgr:#N Location failed"

```
