## LanguageModeling

> `/System/Library/PrivateFrameworks/LanguageModeling.framework/LanguageModeling`

```diff

 433.5.0.0.0
-  __TEXT.__text: 0x1bfff8
-  __TEXT.__auth_stubs: 0x1e00
+  __TEXT.__text: 0x1be208
+  __TEXT.__auth_stubs: 0x1de0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0xe284
-  __TEXT.__gcc_except_tab: 0x18884
-  __TEXT.__cstring: 0xf121
+  __TEXT.__gcc_except_tab: 0x1890c
+  __TEXT.__cstring: 0xe301
   __TEXT.__dlopen_cstrs: 0x2cc
   __TEXT.__oslogstring: 0x188f
   __TEXT.__ustring: 0x8ee
-  __TEXT.__unwind_info: 0x75a0
+  __TEXT.__unwind_info: 0x7570
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1a
   __TEXT.__objc_methname: 0x11e

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0xf10
+  __AUTH_CONST.__auth_got: 0xf00
   __AUTH_CONST.__const: 0xa470
   __AUTH_CONST.__cfstring: 0x3060
   __AUTH_CONST.__objc_const: 0x90

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2D295744-F7CB-346F-A579-30FC44EC250B
-  Functions: 5304
-  Symbols:   1223
-  CStrings:  2563
+  UUID: 17F64E02-0147-31FA-A575-09C6D1CA1936
+  Functions: 5280
+  Symbols:   1222
+  CStrings:  2552
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"

```
