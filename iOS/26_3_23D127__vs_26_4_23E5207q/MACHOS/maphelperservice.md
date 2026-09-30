## maphelperservice

> `/System/Library/Frameworks/CoreLocation.framework/XPCServices/maphelperservice.xpc/maphelperservice`

```diff

-3068.0.15.0.0
-  __TEXT.__text: 0xbf84
-  __TEXT.__auth_stubs: 0x650
+3072.0.40.0.1
+  __TEXT.__text: 0xc4bc
+  __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_stubs: 0xc40
   __TEXT.__objc_methlist: 0x2b4
-  __TEXT.__const: 0x414
+  __TEXT.__const: 0x404
   __TEXT.__gcc_except_tab: 0xec0
-  __TEXT.__cstring: 0x13a4
+  __TEXT.__cstring: 0x1b35
   __TEXT.__oslogstring: 0x1a7
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methname: 0xecd
   __TEXT.__objc_methtype: 0x50c
-  __TEXT.__unwind_info: 0x408
-  __DATA_CONST.__auth_got: 0x338
+  __TEXT.__unwind_info: 0x418
+  __DATA_CONST.__auth_got: 0x310
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x3c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 9022E7C4-DF97-3743-8F3D-093779079E30
-  Functions: 182
-  Symbols:   226
-  CStrings:  469
+  UUID: BD5A6F6F-7D30-313C-980B-106B537FB349
+  Functions: 183
+  Symbols:   221
+  CStrings:  475
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x20
+ _objc_retain_x9
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x6
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CILXugDx32nSryXDAg0oKhE7cNZiTnzY8Tz5gec/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
