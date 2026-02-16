## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-65.0.3.0.0
-  __TEXT.__text: 0xfc0b4
-  __TEXT.__auth_stubs: 0x1030
+67.0.1.0.0
+  __TEXT.__text: 0xfc9b8
+  __TEXT.__auth_stubs: 0x1000
   __TEXT.__objc_stubs: 0x3160
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0xb04
-  __TEXT.__const: 0x9df3
-  __TEXT.__gcc_except_tab: 0xf4a0
-  __TEXT.__cstring: 0x6404
-  __TEXT.__oslogstring: 0x3f80f
+  __TEXT.__const: 0x9411
+  __TEXT.__gcc_except_tab: 0xf5b8
+  __TEXT.__cstring: 0x7e4c
+  __TEXT.__oslogstring: 0x3fa2e
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methname: 0x3a6f
   __TEXT.__objc_methtype: 0x1b29
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x4360
-  __DATA_CONST.__auth_got: 0x828
+  __TEXT.__unwind_info: 0x4368
+  __DATA_CONST.__auth_got: 0x810
   __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x85c8
-  __DATA_CONST.__cfstring: 0x62e0
+  __DATA_CONST.__cfstring: 0x6300
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C21538D0-2EC5-3325-B465-83C24BCFE048
-  Functions: 3501
-  Symbols:   455
-  CStrings:  5554
+  UUID: 56A67321-FE55-32FB-A4ED-2E2C205FD681
+  Functions: 3503
+  Symbols:   452
+  CStrings:  5578
 
Symbols:
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ " "
+ "."
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4qugC6ZLYyeyQn4QCQCBZmGvXJ-z2bwaeNQDQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/467CDD69-E1C6-475F-96C4-8E463A8101A1/TemporaryDirectory.SCOmPR/Sources/SafetyAlerts/Sources/Daemon/framework/geometry/SAGeometry.mm"
+ "/Library/Caches/com.apple.xbs/467CDD69-E1C6-475F-96C4-8E463A8101A1/TemporaryDirectory.SCOmPR/Sources/SafetyAlerts/Sources/Daemon/framework/util/SAStateMachine.h"
+ "/Library/Caches/com.apple.xbs/467CDD69-E1C6-475F-96C4-8E463A8101A1/TemporaryDirectory.SCOmPR/Sources/SafetyAlerts/Sources/Daemon/system/coreTelephony/prod/SACoreTelephonyClientHelper.mm"
+ "/Library/Caches/com.apple.xbs/467CDD69-E1C6-475F-96C4-8E463A8101A1/TemporaryDirectory.SCOmPR/Sources/SafetyAlerts/Sources/Daemon/system/coreTelephony/prod/SACoreTelephonyProd.mm"
+ "/Library/Caches/com.apple.xbs/467CDD69-E1C6-475F-96C4-8E463A8101A1/TemporaryDirectory.SCOmPR/Sources/SafetyAlerts/Sources/Daemon/system/mobileAsset/prod/SAMobileAssetProd.mm"
+ "/Library/Caches/com.apple.xbs/467CDD69-E1C6-475F-96C4-8E463A8101A1/TemporaryDirectory.SCOmPR/Sources/SafetyAlerts/Sources/Daemon/system/mobileAsset/test/SAMobileAssetTest.mm"
+ "_"
+ "isActionAlert"
+ "{\"msg%{public}.0s\":\"#daemon,forwardAlertToCA,alert dropped\"}"
+ "{\"msg%{public}.0s\":\"#uimetrics,SAUiDisplayMetricsEntry,postToAnalytics,values\", \"bleAlertID\":%{private, location:escape_only}@, \"isFirstUnlocked\":%{private, location:escape_only}@, \"isInLOI\":%{sensitive, location:escape_only}@, \"isLocked\":%{private, location:escape_only}@, \"transport\":%{private, location:escape_only}@, \"userTapped\":%{private, location:escape_only}@, \"postToTapLatency\":%{private, location:escape_only}@, \"serverToPostingLatency\":%{private, location:escape_only}@, \"tapToDisplayLatency\":%{private, location:escape_only}@, \"serverToTapLatency\":%{private, location:escape_only}@, \"isLockedDuringPosting\":%{private, location:escape_only}@, \"isLockedDuringSubmission\":%{private, location:escape_only}@, \"isRelayedAlert\":%{private, location:escape_only}@, \"level\":%{private, location:escape_only}@, \"isActionAlert\":%{private}hhd, \"alertType\":%{private}d, \"environmentId\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"alert dropped\", \"alertLevel\":%{private, location:escape_only}s, \"purpose\":%{private, location:escape_only}s, \"class\":%{private, location:escape_only}s, \"function\":%{private, location:escape_only}s, \"uid\":%{private, location:escape_only}s, \"interface\":%{private}d, \"transport\":%{private}d, \"ingressToServerTime\":\"%{private}.3f\", \"egressFromSourceTime\":\"%{private}.3f\", \"eventOriginTime\":\"%{private}.3f\", \"effectiveTime\":\"%{private}.3f\", \"expiryTime\":\"%{private}.3f\", \"advTime\":\"%{private}.3f\"}"
- "/Library/Caches/com.apple.xbs/Sources/SafetyAlerts/Sources/Daemon/framework/geometry/SAGeometry.mm"
- "/Library/Caches/com.apple.xbs/Sources/SafetyAlerts/Sources/Daemon/framework/util/SAStateMachine.h"
- "/Library/Caches/com.apple.xbs/Sources/SafetyAlerts/Sources/Daemon/system/coreTelephony/prod/SACoreTelephonyClientHelper.mm"
- "/Library/Caches/com.apple.xbs/Sources/SafetyAlerts/Sources/Daemon/system/coreTelephony/prod/SACoreTelephonyProd.mm"
- "/Library/Caches/com.apple.xbs/Sources/SafetyAlerts/Sources/Daemon/system/mobileAsset/prod/SAMobileAssetProd.mm"
- "/Library/Caches/com.apple.xbs/Sources/SafetyAlerts/Sources/Daemon/system/mobileAsset/test/SAMobileAssetTest.mm"
- "{\"msg%{public}.0s\":\"#daemonInterfaceProd,unknownMessage,nil\"}"
- "{\"msg%{public}.0s\":\"#uimetrics,SAUiDisplayMetricsEntry,postToAnalytics,values\", \"bleAlertID\":%{private, location:escape_only}@, \"isFirstUnlocked\":%{private, location:escape_only}@, \"isInLOI\":%{sensitive, location:escape_only}@, \"isLocked\":%{private, location:escape_only}@, \"transport\":%{private, location:escape_only}@, \"userTapped\":%{private, location:escape_only}@, \"postToTapLatency\":%{private, location:escape_only}@, \"serverToPostingLatency\":%{private, location:escape_only}@, \"tapToDisplayLatency\":%{private, location:escape_only}@, \"serverToTapLatency\":%{private, location:escape_only}@, \"isLockedDuringPosting\":%{private, location:escape_only}@, \"isLockedDuringSubmission\":%{private, location:escape_only}@, \"isRelayedAlert\":%{private, location:escape_only}@, \"level\":%{private, location:escape_only}@, \"alertType\":%{private}d, \"environmentId\":%{private, location:escape_only}s}"

```
