## abmlite

> `/usr/bin/abmlite`

```diff

-1417.0.0.0.0
-  __TEXT.__text: 0x1a24c
-  __TEXT.__auth_stubs: 0x770
+1418.1.0.0.0
+  __TEXT.__text: 0x19e1c
+  __TEXT.__auth_stubs: 0x760
   __TEXT.__objc_stubs: 0x560
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0x1c40
-  __TEXT.__cstring: 0x11b1
+  __TEXT.__gcc_except_tab: 0x1c24
+  __TEXT.__cstring: 0x92b
   __TEXT.__oslogstring: 0xc6
   __TEXT.__objc_classname: 0xd
   __TEXT.__objc_methtype: 0x14
   __TEXT.__objc_methname: 0x31e
   __TEXT.__unwind_info: 0x490
-  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x490
   __DATA_CONST.__cfstring: 0x160

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7069475-44B1-3038-B49F-BC45CD8024EB
+  UUID: 0B92161D-B11F-340C-B765-81C96AE0B0FE
   Functions: 146
-  Symbols:   326
-  CStrings:  169
+  Symbols:   323
+  CStrings:  162
 
Symbols:
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyBasebandWatchdogStop
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_100003ca8 : 728 -> 700
~ sub_100003f80 -> sub_100003f64 : 956 -> 900
~ sub_100004550 -> sub_1000044fc : 17684 -> 17528
~ sub_100008d3c -> sub_100008c4c : 14132 -> 13476
~ sub_100016190 -> sub_100015e10 : 1360 -> 1336
~ sub_10001a540 -> sub_10001a1a8 : 1476 -> 1324
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRnugBJQVh_0UvyFSAukEw4XJM6nZ8AmFIwcoA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
