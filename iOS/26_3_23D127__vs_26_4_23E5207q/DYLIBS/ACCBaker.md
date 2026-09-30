## ACCBaker

> `/System/Library/PrivateFrameworks/ACCBaker.framework/ACCBaker`

```diff

-2.1.3.0.0
-  __TEXT.__text: 0x478a0
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__const: 0x256db
-  __TEXT.__gcc_except_tab: 0x33b0
-  __TEXT.__cstring: 0x64c4
+2.4.0.0.0
+  __TEXT.__text: 0x3b9dc
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__const: 0x227f8
+  __TEXT.__gcc_except_tab: 0x2d60
+  __TEXT.__cstring: 0x8480
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0xd48
+  __TEXT.__unwind_info: 0xc80
   __TEXT.__objc_methname: 0x32
   __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x828
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x418
-  __AUTH_CONST.__const: 0xbe0
+  __AUTH_CONST.__auth_got: 0x3c0
+  __AUTH_CONST.__const: 0xb70
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH.__data: 0x28
+  __AUTH.__data: 0x8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0x80
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/URLCompression.framework/URLCompression
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 0C8C8774-F7DE-3EC5-A0F3-E250027A5156
-  Functions: 451
-  Symbols:   186
-  CStrings:  220
+  UUID: 007318B8-5E34-3F27-A566-CCF1780A1FF7
+  Functions: 407
+  Symbols:   174
+  CStrings:  196
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_release_x25
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
- __ZNSt13runtime_errorC2EPKc
- __ZNSt3__18numpunctIcE2idE
- __ZNSt3__18to_charsEPcS0_d
- __ZNSt3__18to_charsEPcS0_dNS_12chars_formatE
- __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
- __ZNSt3__18to_charsEPcS0_e
- __ZNSt3__18to_charsEPcS0_eNS_12chars_formatE
- __ZNSt3__18to_charsEPcS0_eNS_12chars_formatEi
- __ZNSt3__18to_charsEPcS0_f
- __ZNSt3__18to_charsEPcS0_fNS_12chars_formatE
- __ZNSt3__18to_charsEPcS0_fNS_12chars_formatEi
- ___udivti3
- ___umodti3
- _objc_claimAutoreleasedReturnValue
- _objc_release_x22
- _objc_retain_x8
CStrings:
+ "\n"
+ " : "
+ "(cfref == nullptr) || ((detail::CFTypeIDGet(cfref) != 0) && IsOfCFType<T>(cfref))"
+ ") scale("
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:286: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:271: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:692: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/bitset:697: libc++ Hardening assertion __p < _Size failed: bitset::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:801: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:811: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/optional:816: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/property_tree/detail/ptree_implementation.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/property_tree/detail/xml_parser_read_rapidxml.hpp"
+ "/AppleInternal/Library/BuildRoots/4~CInVugDxSaYXY1JVrJb5AhM699b5Wj5APTtrqSg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/local/include/boost/property_tree/detail/xml_parser_write.hpp"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/library/AppCode/Codec/src/Version.cpp"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/library/Essentials/Array/src/ArrayBuffer.cpp"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/library/Kit/Foundation/src/Ptr.cpp"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/product/AppCode/ACCBaker/src/ACCBaker.cpp"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/product/AppCode/ACCBaker/src/ACCBakerInternal.cpp"
+ "/Library/Caches/com.apple.xbs/A7611C9C-0BA6-45C5-A397-B509DCD96279/TemporaryDirectory.krOhY3/Sources/ACCBaker/product/AppCode/ACCBaker/src/ACCBakerUtil.mm"
+ ":"
+ "Are you wrapping a CFTypeRef from a different type ?"
- " : {}"
- " does not allow the "
- " formatting argument"
- "/AppleInternal/Library/BuildRoots/4~CHzmugBlE2Fw8FhE6_cdI8UDRMeJjdUem635fnw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/property_tree/detail/ptree_implementation.hpp"
- "/AppleInternal/Library/BuildRoots/4~CHzmugBlE2Fw8FhE6_cdI8UDRMeJjdUem635fnw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/property_tree/detail/xml_parser_read_rapidxml.hpp"
- "/AppleInternal/Library/BuildRoots/4~CHzmugBlE2Fw8FhE6_cdI8UDRMeJjdUem635fnw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.3.Internal.sdk/usr/local/include/boost/property_tree/detail/xml_parser_write.hpp"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/library/AppCode/Codec/src/Version.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/library/Essentials/Array/include/Essentials/Array/ArrayView.h"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/library/Essentials/Array/src/ArrayBuffer.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/library/Kit/Foundation/include/Kit/Foundation/Ptr.h"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/library/Kit/Foundation/src/Ptr.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/product/AppCode/ACCBaker/src/ACCBaker.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/product/AppCode/ACCBaker/src/ACCBakerInternal.cpp"
- "/Library/Caches/com.apple.xbs/Sources/ACCBaker/product/AppCode/ACCBaker/src/ACCBakerUtil.mm"
- "01"
- "01234567"
- "0123456789abcdef"
- "0123456789abcdefghijklmnopqrstuvwxyz"
- "0B"
- "0X"
- "0b"
- "0x"
- "An argument index may not have a negative value"
- "Are you wrapping a CFTypeRef from an other type ?"
- "End of input while parsing an argument index"
- "End of input while parsing format specifier precision"
- "Integral value outside the range of the char type"
- "Replacement argument isn't a standard signed or unsigned integer type"
- "The argument index is invalid"
- "The argument index should end with a ':' or a '}'"
- "The argument index starts with an invalid character"
- "The argument index value is too large for the number of arguments supplied"
- "The fill option contains an invalid value"
- "The format specifier contains malformed Unicode characters"
- "The format specifier for "
- "The format specifier should consume the input or end with a '}'"
- "The format string contains an invalid escape sequence"
- "The format string terminates at a '{'"
- "The numeric value of the format specifier is too large"
- "The precision option does not contain a value or an argument index"
- "The replacement field misses a terminating '}'"
- "The type option contains an invalid value for "
- "The type option contains an invalid value for a string formatting argument"
- "The value of the argument index exceeds its maximum value"
- "The width option should not have a leading zero"
- "Using automatic argument numbering in manual argument numbering mode"
- "Using manual argument numbering in automatic argument numbering mode"
- "\\\""
- "\\'"
- "\\\\"
- "\\n"
- "\\r"
- "\\t"
- "a bool"
- "a character"
- "a floating-point"
- "a pointer"
- "alternate form"
- "an integer"
- "cfref == nullptr || IsOfCFType<T>(cfref)"
- "false"
- "infnanINFNAN"
- "precision"
- "sign"
- "true"
- "zero-padding"
- "{}: {}"
- "{}:{}{}{}\n"

```
