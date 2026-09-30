## LocationSupport

> `/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`

```diff

-3072.0.42.0.0
-  __TEXT.__text: 0x241a8
-  __TEXT.__auth_stubs: 0xe40
+3072.0.44.0.2
+  __TEXT.__text: 0x2411c
+  __TEXT.__auth_stubs: 0xe30
   __TEXT.__objc_methlist: 0x174c
-  __TEXT.__const: 0x2dd
-  __TEXT.__cstring: 0x2047
+  __TEXT.__const: 0x2e5
+  __TEXT.__cstring: 0x1c21
   __TEXT.__gcc_except_tab: 0x16d4
   __TEXT.__oslogstring: 0x5aeb
-  __TEXT.__unwind_info: 0xc90
+  __TEXT.__unwind_info: 0xc88
   __TEXT.__objc_classname: 0x412
   __TEXT.__objc_methname: 0x2847
   __TEXT.__objc_methtype: 0x858

   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x738
+  __AUTH_CONST.__auth_got: 0x730
   __AUTH_CONST.__const: 0x950
   __AUTH_CONST.__cfstring: 0x500
   __AUTH_CONST.__objc_const: 0x2b08

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C8004CA-A7E0-33C1-A786-C1ACA1747CC3
+  UUID: F38F9F66-4B72-3925-B326-A27372782779
   Functions: 730
-  Symbols:   469
-  CStrings:  1197
+  Symbols:   468
+  CStrings:  1194
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_1e3dd8ab0 -> sub_1e2bc9ab0 : 1360 -> 1276
~ sub_1e3de8060 -> sub_1e2bd900c : 2088 -> 2072
~ sub_1e3de97f0 -> sub_1e2bda78c : 344 -> 304
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJIqugClfI06gqfL8cT9eg8YQxQd7BXeh0K9Evc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
