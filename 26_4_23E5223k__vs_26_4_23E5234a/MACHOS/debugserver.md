## debugserver

> `/usr/libexec/debugserver`

```diff

 1700.2.2.124.0
-  __TEXT.__text: 0x56cd0
-  __TEXT.__auth_stubs: 0x1300
+  __TEXT.__text: 0x553d8
+  __TEXT.__auth_stubs: 0x12e0
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__init_offsets: 0x10
-  __TEXT.__cstring: 0xd816
+  __TEXT.__cstring: 0xc487
   __TEXT.__const: 0x308
-  __TEXT.__gcc_except_tab: 0x100c
+  __TEXT.__gcc_except_tab: 0x1010
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x282
-  __TEXT.__unwind_info: 0xd50
-  __DATA_CONST.__auth_got: 0x990
+  __TEXT.__unwind_info: 0xd28
+  __DATA_CONST.__auth_got: 0x980
   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x28
   __DATA_CONST.__const: 0x3c90

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpmenergy.dylib
   - /usr/lib/libpmsample.dylib
-  UUID: 872A9D7B-8EFB-350F-A057-1A333CAC179B
-  Functions: 961
-  Symbols:   390
-  CStrings:  1793
+  UUID: C937E381-BA2B-32D9-84E7-519714BA5B9E
+  Functions: 956
+  Symbols:   388
+  CStrings:  1777
 
Symbols:
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:282: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:301: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1461: libc++ Hardening assertion !empty() failed: string::front(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1471: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "/AppleInternal/Library/BuildRoots/4~CJlVugB4B_e8GyLwDgaX7TVhtOwbaSU8KCRqMzA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:431: libc++ Hardening assertion __n <= size() failed: remove_prefix() can't remove more than size()\n"

```
