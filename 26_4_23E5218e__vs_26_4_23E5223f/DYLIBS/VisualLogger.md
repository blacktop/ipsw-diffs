## VisualLogger

> `/System/Library/PrivateFrameworks/VisualLogger.framework/VisualLogger`

```diff

 8.25.12.16.5
-  __TEXT.__text: 0x72d23c
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__const: 0x67370
-  __TEXT.__gcc_except_tab: 0x60174
-  __TEXT.__cstring: 0x1c317
+  __TEXT.__text: 0x706444
+  __TEXT.__auth_stubs: 0x1be0
+  __TEXT.__const: 0x67350
+  __TEXT.__gcc_except_tab: 0x60198
+  __TEXT.__cstring: 0x16324
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x1b730
+  __TEXT.__unwind_info: 0x1b5c0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_methname: 0x23
   __TEXT.__objc_stubs: 0x60

   __DATA_CONST.__const: 0x1458
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xe08
+  __AUTH_CONST.__auth_got: 0xe00
   __AUTH_CONST.__const: 0x31ad0
   __AUTH_CONST.__cfstring: 0x2a0
   __DATA.__data: 0x21f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8CA3E65-D334-3044-8451-1BBF6C663AC3
-  Functions: 16825
-  Symbols:   1143
-  CStrings:  2266
+  UUID: 6996D1B7-348C-3181-9A59-5AFC273C1C84
+  Functions: 16784
+  Symbols:   1142
+  CStrings:  2219
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = (lambda at /Library/Caches/com.apple.xbs/2273046A-AEC9-44C9-B0CE-D2A7DD8CF199/TemporaryDirectory.gs7w1e/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZServer.cpp:354:37)]"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:237: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:250: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/formatter_output.h:264: libc++ Hardening assertion __first <= __last failed: Not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__format/parser_std_format_spec.h:594: libc++ Hardening assertion __begin != __end failed: when called with an empty input the function will cause undefined behavior by evaluating data not in the input\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:333: libc++ Hardening assertion !empty() failed: vector<bool>::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1553: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2464: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:796: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:806: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:279: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:280: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:297: libc++ Hardening assertion std::__is_valid_range(__pbeg, __pend) failed: [pbeg, pend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJRjugAGx17pwFWyAVLPqAbfUEYrpkW_sBUgyek/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "static auto cv3d::esn::TypeNameHelpers::PrettyArgName() [T = (lambda at /Library/Caches/com.apple.xbs/850FD46D-1329-4F20-92B0-36C7F70F5482/TemporaryDirectory.aZvzr7/Sources/AppleCV3D_VisualLogger/library/VL/VisualLogger/VisualLogger/src/VZServer.cpp:354:37)]"

```
