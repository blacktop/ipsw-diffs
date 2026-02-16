## VisualLogger

> `/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger`

```diff

-8.25.6.25.71
-  __TEXT.__text: 0x736028
-  __TEXT.__auth_stubs: 0x1bc0
-  __TEXT.__const: 0x66fa0
-  __TEXT.__gcc_except_tab: 0x60710
-  __TEXT.__cstring: 0x14ed0
+8.25.12.16.0
+  __TEXT.__text: 0x72d23c
+  __TEXT.__auth_stubs: 0x1bf0
+  __TEXT.__const: 0x67370
+  __TEXT.__gcc_except_tab: 0x60174
+  __TEXT.__cstring: 0x1c317
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1b0a0
-  __TEXT.__eh_frame: 0x88
+  __TEXT.__unwind_info: 0x1b730
+  __TEXT.__eh_frame: 0x50
   __TEXT.__objc_methname: 0x23
   __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x330
+  __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x1458
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xdf0
-  __AUTH_CONST.__const: 0x315d8
-  __AUTH_CONST.__cfstring: 0x280
-  __DATA.__data: 0x2250
+  __AUTH_CONST.__auth_got: 0xe08
+  __AUTH_CONST.__const: 0x31ad0
+  __AUTH_CONST.__cfstring: 0x2a0
+  __DATA.__data: 0x21f0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x2818
-  __DATA.__common: 0x2c0
+  __DATA.__bss: 0x28b0
+  __DATA.__common: 0x298
   __DATA_DIRTY.__data: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0967B76E-9A69-3DB7-9C10-0637DA2BC0B0
-  Functions: 16475
-  Symbols:   1132
-  CStrings:  2190
+  UUID: BA1D0B82-D6D9-39BE-86F3-F55BED84A6AB
+  Functions: 16825
+  Symbols:   1143
+  CStrings:  2266
 
Symbols:
+ _CFBundleCopyBundleURL
+ _CFURLGetString
+ _VZPixelFormatFromOSType
+ _VZPixelFormatToOSType
+ _VZRecorderGetMaximumRecordCount
+ _VZRecorderGetMaximumRecordsSize
+ _VZRecorderOptionsSetMaximumRecordCount
+ _VZRecorderOptionsSetMaximumRecordsSize
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _kCFNull
+ _kVZSizeMax
+ _malloc_type_aligned_alloc
+ _objc_retainAutoreleasedReturnValue
- _malloc_type_posix_memalign
- _objc_claimAutoreleasedReturnValue
CStrings:
+ "  #"
+ " as array of type with size "
+ " bytes"
+ " for format with properties:\n"
+ " format."
+ " option"
+ " size "
+ " | "
+ "&"
+ "*"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:297: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugD21dy4En8qfZnwYc7TthjKJ3luu-Ub5UU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Apple/src/BundleInfo.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Apple/src/Clock.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Array/src/ArrayBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Dispatch/src/DispatchQueue.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Dispatch/src/DispatchQueueTypeUtil.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Dispatch/src/GrandCentralDispatchUtil.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/IO/include/Essentials/IO/Archive.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Essentials/Log/src/APILogging.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/Node.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ChannelInputModel.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/Processor.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ProcessorInputMessageHandlingStrategy.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/src/Channel/NodeTaskScheduler.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/src/Channel/NodeTaskSchedulerPool.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Container/src/Lines.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Container/src/Points.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/CoreGraphics/src/ColorSpaceRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/CoreGraphics/src/DataProviderRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/CoreGraphics/src/ImageRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/src/CVImage.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/src/CVImage.cpp:56"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/FoundationIO/include/Kit/FoundationIO/DictionaryRefIO.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/BundleRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/DictionaryRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/Ptr.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/Ref.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/URLRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurface/include/Kit/IOSurface/View.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp:47"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/Format.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/ImageView.h:1290"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/SharedImage.h:1237"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/src/Algorithm.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/src/ImageStorage.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Image/src/Size.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/include/Kit/ImageIO/ImageIO.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/Apple.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/ImageDestinationRef.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/ImageIO.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/Pnm.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/Serialization.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Memory/include/Kit/Memory/VMAllocator.hpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/include/Kit/Mesh/TriMeshAllocator.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/src/TriMesh.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/src/TriMeshAllocator.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/src/TriMeshIO.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/PixelFormat/include/Kit/PixelFormat/Properties.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/include/Kit/Visualization/DataIO.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/include/Kit/Visualization/IData.h"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/Client.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/DataIO.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/DataType.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/FileIO.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/FileIOPrivate.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/IData.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/NamedContext.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/NetworkData.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/Server.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/VisualLogger.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/Return.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZBase.cpp"
+ "/Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/src/ExternalBuffer.cpp"
+ "0 "
+ ": received data of timestamp "
+ "; caused by:\n"
+ "An error occured while loading the image"
+ "Binary not found for callable"
+ "Bundle does not have a bundle identifier"
+ "Cannot reinterpret memory region of byte size "
+ "ClientOnly"
+ "ControlledLogger"
+ "Could not access bundle location from function pointer. Detail: "
+ "Failed to create "
+ "Failed to load bundle from "
+ "Failed to obtain executable path"
+ "IOSurface"
+ "RearCameraOffsetFromDisplayCenter"
+ "VZRecorderGetMaximumRecordCount"
+ "VZRecorderGetMaximumRecordsSize"
+ "VZRecorderOptionsSetMaximumRecordCount"
+ "VZRecorderOptionsSetMaximumRecordsSize"
+ "] "
+ "bundle_url"
+ "com.apple.cv3d"
+ "failed recording data of type "
+ "file exporter"
+ "file://"
+ "given "
+ "invalid info log destination ("
+ "ptr_"
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = (lambda at /Library/Caches/com.apple.xbs/CE71A514-B8F2-4558-898D-BAA99FB1D581/TemporaryDirectory.dPWpQT/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZServer.cpp:354:37)]"
+ "std::aligned_alloc failed to allocate "
+ "warning: problem while recording data of type "
+ "{:02x}"
- " (ENOMEM)"
- ", used properties:\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Apple/src/BundlePath.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Apple/src/Clock.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Array/src/ArrayBuffer.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Dispatch/src/DispatchQueue.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Dispatch/src/DispatchQueueTypeUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Dispatch/src/GrandCentralDispatchUtil.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/IO/include/Essentials/IO/Archive.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Essentials/Log/src/APILogging.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/Node.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ChannelInputModel.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/Processor.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/include/Kit/Concurrency/Channel/detail/ProcessorInputMessageHandlingStrategy.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/src/Channel/NodeTaskScheduler.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Concurrency/src/Channel/NodeTaskSchedulerPool.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Container/src/Lines.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Container/src/Points.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/CoreGraphics/src/ColorSpaceRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/CoreGraphics/src/DataProviderRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/CoreGraphics/src/ImageRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/include/Kit/CoreVideo/PixelBufferRef.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/src/CVImage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/src/CVImage.cpp:56"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/CoreVideo/src/PixelBufferRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/FoundationIO/include/Kit/FoundationIO/DictionaryRefIO.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/BundleRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/DictionaryRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/Ptr.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/Ref.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Foundation/src/URLRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurface/include/Kit/IOSurface/View.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurface/src/IOSurfaceRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/IOSurfaceImage/src/IOSurfaceImage.cpp:47"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/Format.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/FormatAlgorithm.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/ImageBuffer.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/ImageView.h:1290"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/ImageView.h:1300"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/include/Kit/Image/SharedImage.h:1237"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/src/Algorithm.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/src/ImageStorage.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Image/src/Size.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/include/Kit/ImageIO/ImageIO.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/Apple.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/ImageDestinationRef.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/ImageIO.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/Pnm.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/ImageIO/src/Serialization.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Memory/include/Kit/Memory/VMAllocator.hpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/include/Kit/Mesh/TriMeshAllocator.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/src/TriMesh.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/src/TriMeshAllocator.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Mesh/src/TriMeshIO.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/PixelFormat/include/Kit/PixelFormat/Properties.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/include/Kit/Visualization/DataIO.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/include/Kit/Visualization/IData.h"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/Client.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/DataIO.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/DataType.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/FileIO.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/FileIOPrivate.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/IData.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/NamedContext.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/NetworkData.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/Server.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/Kit/Visualization/src/VisualLogger.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/Return.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZBase.cpp"
- "/Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/src/ExternalBuffer.cpp"
- ": error code "
- "Failed to create IOSurface for format "
- "Mesh "
- "cf_current_bundle"
- "cg_image.IsValid()"
- "given IOSurface size "
- "key '"
- "posix_memalign failed to allocate "
- "ratio<"
- "received data of timestamp "
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = (lambda at /Library/Caches/com.apple.xbs/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZServer.cpp:354:37)]"
- "while recording data of type "

```
