## EventMetaDataExtractorPlugin

> `/System/Library/PrivateFrameworks/EventMetaDataExtractor.framework/PlugIns/EventMetaDataExtractorPlugin.appex/EventMetaDataExtractorPlugin`

```diff

 17.0.1.2.0
-  __TEXT.__text: 0x8d460
-  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__text: 0x8b460
+  __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_stubs: 0x1300
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x76c
   __TEXT.__const: 0x245f
-  __TEXT.__gcc_except_tab: 0xa9a4
+  __TEXT.__gcc_except_tab: 0xa974
   __TEXT.__objc_methname: 0x1e30
-  __TEXT.__cstring: 0x8200
+  __TEXT.__cstring: 0x6dbc
   __TEXT.__oslogstring: 0xfd3
   __TEXT.__objc_classname: 0xa5
   __TEXT.__objc_methtype: 0xcbd
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3b18
-  __DATA_CONST.__auth_got: 0x6f8
+  __TEXT.__unwind_info: 0x3af0
+  __DATA_CONST.__auth_got: 0x6f0
   __DATA_CONST.__got: 0x240
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x24a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 99CE8023-4CCC-37CE-A4DC-C927C5D762EA
-  Functions: 2629
-  Symbols:   374
-  CStrings:  1329
+  UUID: E5154C34-FC0D-3563-891D-951AF0C198CF
+  Functions: 2624
+  Symbols:   373
+  CStrings:  1313
 
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
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CJlFugAJpktGsGfCqPMfRYLhNMWsnjcs1tKiG1I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugA1D-aTBn-tZO6PslVi70TARa5HLwTHhQE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugA1D-aTBn-tZO6PslVi70TARa5HLwTHhQE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugA1D-aTBn-tZO6PslVi70TARa5HLwTHhQE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlJugA1D-aTBn-tZO6PslVi70TARa5HLwTHhQE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"

```
