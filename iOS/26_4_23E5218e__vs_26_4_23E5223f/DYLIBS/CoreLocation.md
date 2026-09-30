## CoreLocation

> `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`

```diff

-3072.0.42.0.0
-  __TEXT.__text: 0x20f8d0
-  __TEXT.__auth_stubs: 0x1b30
+3072.0.44.0.2
+  __TEXT.__text: 0x209858
+  __TEXT.__auth_stubs: 0x1b20
   __TEXT.__objc_methlist: 0xa5e4
   __TEXT.__const: 0x4a68
-  __TEXT.__gcc_except_tab: 0xf928
+  __TEXT.__gcc_except_tab: 0xf8e4
   __TEXT.__oslogstring: 0x3c017
-  __TEXT.__cstring: 0x28d57
+  __TEXT.__cstring: 0x265e8
   __TEXT.__ustring: 0x70a
-  __TEXT.__unwind_info: 0x59f8
+  __TEXT.__unwind_info: 0x59d8
   __TEXT.__objc_classname: 0x13a5
   __TEXT.__objc_methname: 0x1d317
   __TEXT.__objc_methtype: 0x5e06

   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4d0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__auth_got: 0xda8
   __AUTH_CONST.__const: 0x3bf0
   __AUTH_CONST.__cfstring: 0xc180
   __AUTH_CONST.__objc_const: 0x11a10

   __DATA.__objc_ivar: 0xb94
   __DATA.__data: 0x9c8
   __DATA.__bss: 0xa80
-  __DATA.__common: 0x60
+  __DATA.__common: 0x68
   __DATA_DIRTY.__objc_ivar: 0x68
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 08C563A5-60FB-349E-B6EA-6FD4124FA76B
-  Functions: 5348
-  Symbols:   1116
-  CStrings:  12198
+  UUID: A4ED400C-2F74-3BA8-A508-EECCE23A50ED
+  Functions: 5343
+  Symbols:   1115
+  CStrings:  12175
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "20:42:10"
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/2216DC93-5D5B-4EE6-BAF8-340BB89D5544/TemporaryDirectory.l1jspw/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Feb 25 2026"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "00:35:52"
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/78B5C499-61E1-4387-99FA-8BCCE417D80C/TemporaryDirectory.S7VCgV/Sources/CoreLocationFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
- "Feb 16 2026"

```
