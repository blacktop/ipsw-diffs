## MultitouchHID

> `/System/Library/Extensions/AppleMultitouchSPI.kext/PlugIns/MultitouchHID.plugin/MultitouchHID`

```diff

-9140.1.0.0.0
-  __TEXT.__text: 0x52ef0
-  __TEXT.__auth_stubs: 0x1780
+9140.3.0.0.0
+  __TEXT.__text: 0x53f7c
+  __TEXT.__auth_stubs: 0x1790
   __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__const: 0x17d1
-  __TEXT.__cstring: 0x6ee5
-  __TEXT.__gcc_except_tab: 0xc54
-  __TEXT.__oslogstring: 0x3423
-  __TEXT.__unwind_info: 0x14f8
+  __TEXT.__const: 0x18a1
+  __TEXT.__cstring: 0x6f2a
+  __TEXT.__gcc_except_tab: 0xc8c
+  __TEXT.__oslogstring: 0x3619
+  __TEXT.__unwind_info: 0x1568
   __TEXT.__objc_classname: 0x3e
   __TEXT.__objc_methname: 0x809
   __TEXT.__objc_methtype: 0xe6
   __TEXT.__objc_stubs: 0x9c0
-  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x760
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH_CONST.__const: 0x2a48
-  __AUTH_CONST.__cfstring: 0x5ce0
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH_CONST.__const: 0x2ad8
+  __AUTH_CONST.__cfstring: 0x5d40
   __AUTH_CONST.__objc_const: 0x2e0
   __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__data: 0xa8
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x150

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3CFFD5F4-D379-33DF-AE01-40296A1D6341
-  Functions: 1577
-  Symbols:   2906
-  CStrings:  2166
+  UUID: 7327D2C0-0A13-3018-AFCA-284CE48696C3
+  Functions: 1602
+  Symbols:   2968
+  CStrings:  2181
 
Symbols:
+ GCC_except_table15
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ __ZN23MultitouchReportTrackerC2Ev
+ __ZN28MTTelemetryAnalyticsReporter13trackReportIDEh
+ __ZN28MTTelemetryAnalyticsReporter14logPathReportsEv
+ __ZN28MTTelemetryAnalyticsReporter23scheduleOnDispatchQueueEP16dispatch_queue_s
+ __ZN28MTTelemetryAnalyticsReporter27unscheduleFromDispatchQueueEP16dispatch_queue_s
+ __ZNK23MultitouchReportTracker22iterateReceivedReportsENSt3__18functionIFvhEEE
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEE7__cloneEPNS0_6__baseIS4_EE
+ __ZNKSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEE7__cloneEv
+ __ZNKSt3__18functionIFvhEEclEh
+ __ZNSt3__110__function12__value_funcIFvhEED2B9foe210106Ev
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEE7destroyEv
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEED0Ev
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEED1Ev
+ __ZNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEEclEOh
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIhJRKNS_21piecewise_construct_tENS_5tupleIJRS5_EEENSL_IJEEEEEENS4_INS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE4findIhEENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIhhEENS_22__unordered_map_hasherIhNS_4pairIKhhEENS_4hashIhEENS_8equal_toIhEELb1EEENS_21__unordered_map_equalIhS6_SA_S8_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__next_primeEm
+ __ZNSt3__117bad_function_callD1Ev
+ __ZNSt3__125__throw_bad_function_callB9foe210106Ev
+ __ZTINSt3__110__function6__baseIFvhEEE
+ __ZTINSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEEE
+ __ZTINSt3__117bad_function_callE
+ __ZTIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0
+ __ZTSNSt3__110__function6__baseIFvhEEE
+ __ZTSNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEEE
+ __ZTSZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0
+ __ZTVNSt3__110__function6__funcIZN28MTTelemetryAnalyticsReporter14logPathReportsEvE3$_0FvhEEE
+ __ZTVNSt3__117bad_function_callE
+ __ZZN23MultitouchReportTrackerC1EvE9reportIds
+ ____ZN28MTTelemetryAnalyticsReporter23scheduleOnDispatchQueueEP16dispatch_queue_s_block_invoke
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJRnugBlNeltnxmtOcrph3SiuvsCQ_Iyoxk8M8w/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "Deallocating telemetry reporter (deviceID 0x%llX)"
+ "Sending analytics event for reportID %d: %{public}@ (deviceID 0x%llX)"
+ "Telemetry reporter failed to register frame callback (deviceID 0x%llX)"
+ "Telemetry reporter logging found report IDs (deviceID 0x%llX)"
+ "Telemetry reporter scheduling periodic 24h logging on dispatch queue (deviceID 0x%llX)"
+ "Telemetry reporter starting (deviceID 0x%llX)"
+ "Telemetry reporter stopping (deviceID 0x%llX)"
+ "Telemetry reporter unscheduling from dispatch queue (deviceID 0x%llX)"
+ "com.apple.HID.multitouchPathsReportIDUsage"
+ "i"
+ "reportID"
+ "reportID_value"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIsLugCvvvPqBu7oM7Q0wGGiZikMNSOOs5Zmf4I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"

```
