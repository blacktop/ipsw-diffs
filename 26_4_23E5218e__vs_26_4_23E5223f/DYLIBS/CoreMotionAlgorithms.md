## CoreMotionAlgorithms

> `/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`

```diff

-3072.0.42.0.0
-  __TEXT.__text: 0x1a624c
-  __TEXT.__auth_stubs: 0xd20
+3072.0.44.0.2
+  __TEXT.__text: 0x1a0e1c
+  __TEXT.__auth_stubs: 0xd00
   __TEXT.__objc_methlist: 0x9b4
   __TEXT.__const: 0x5402
-  __TEXT.__gcc_except_tab: 0x44c4
-  __TEXT.__cstring: 0x13e5c
+  __TEXT.__gcc_except_tab: 0x4380
+  __TEXT.__cstring: 0x119f2
   __TEXT.__oslogstring: 0x5efa
   __TEXT.__ustring: 0xce
-  __TEXT.__unwind_info: 0x5378
+  __TEXT.__unwind_info: 0x5350
   __TEXT.__objc_classname: 0x1b5
   __TEXT.__objc_methname: 0x257c
   __TEXT.__objc_methtype: 0x2f7a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7f0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x690
   __AUTH_CONST.__const: 0xad60
   __AUTH_CONST.__cfstring: 0xa20
   __AUTH_CONST.__objc_const: 0x17c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 42F48882-7C68-3655-A34F-9D7FD7C1C6BF
-  Functions: 5536
-  Symbols:   290
-  CStrings:  4390
+  UUID: 922FC48E-9299-3F9C-AEAA-904BF9EDE1A4
+  Functions: 5525
+  Symbols:   288
+  CStrings:  4363
 
Symbols:
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "Assertion failed: (fIirFilterParams != __null) && (fIirFilterParams->filterOrder <= kMaxFilterOrder), file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/CMIirFilter.cpp, line 17,IirFilterParams,%p,filterOrder,%d,maxFilterOrder,%d."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 231,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 232,invalid element %zu <= %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
+ "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
+ "Assertion failed: i < fCapacity, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
+ "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 302,indices exceed factored matrix size."
+ "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: rhs.capacity() == capacity(), file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 70,capacity,%zu,%zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 186,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/E0253080-B15F-4DC8-9EAC-4211D98FF8BE/TemporaryDirectory.fRmE4E/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/iterator_operations.h:209: libc++ Hardening assertion __count == 0 || (__dist < 0) == (__count < 0) failed: __sentinel must precede __iter when __count < 0\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJIsugCg6QYQjraaGw1Wqn8SW5JJ7ptgAUqaFxU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "Assertion failed: (fIirFilterParams != __null) && (fIirFilterParams->filterOrder <= kMaxFilterOrder), file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/CMIirFilter.cpp, line 17,IirFilterParams,%p,filterOrder,%d,maxFilterOrder,%d."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 231,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 237,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 232,invalid element %zu <= %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 238,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 273,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMVector.h, line 279,invalid index %zu >= %zu."
- "Assertion failed: i < fCapacity, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 233,i,%zu,capacity,%u."
- "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 302,indices exceed factored matrix size."
- "Assertion failed: ldx < M*N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
- "Assertion failed: rhs.capacity() == capacity(), file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/CMQueue.h, line 70,capacity,%zu,%zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
- "Assertion failed: row < M, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 186,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/B92413EA-87F2-4E67-BBED-9D947F53D439/TemporaryDirectory.1jenaz/Sources/CoreMotionAlgorithmsFramework/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."

```
