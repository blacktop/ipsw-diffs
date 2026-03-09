## CoreAppleCVA

> `/System/Library/PrivateFrameworks/CoreAppleCVA.framework/CoreAppleCVA`

```diff

 4.4.0.0.0
-  __TEXT.__text: 0x60c64
-  __TEXT.__auth_stubs: 0x1810
-  __TEXT.__const: 0x579
+  __TEXT.__text: 0x5fae8
+  __TEXT.__auth_stubs: 0x1800
+  __TEXT.__const: 0x569
   __TEXT.__gcc_except_tab: 0xc8c
-  __TEXT.__cstring: 0x1a31
+  __TEXT.__cstring: 0xb91
   __TEXT.__oslogstring: 0x7ea
-  __TEXT.__unwind_info: 0x11c0
+  __TEXT.__unwind_info: 0x11a8
   __TEXT.__objc_methname: 0x55b
   __TEXT.__objc_stubs: 0x920
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x248
-  __AUTH_CONST.__auth_got: 0xc18
+  __AUTH_CONST.__auth_got: 0xc10
   __AUTH_CONST.__const: 0xc60
   __AUTH_CONST.__cfstring: 0xe0
   __DATA.__data: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9B7B4680-9DCF-3E8B-9B4C-5E2E742E33B7
-  Functions: 1726
-  Symbols:   1849
-  CStrings:  265
+  UUID: D3D5A6AD-04B0-3F22-9D99-89BC4DB9A010
+  Functions: 1724
+  Symbols:   1848
+  CStrings:  253
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/array:275: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3352: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugCjtfTGGyhsDy1NlIy4x_8WKpmXil6AZEk/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
