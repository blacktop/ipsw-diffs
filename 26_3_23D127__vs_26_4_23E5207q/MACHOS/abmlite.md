## abmlite

> `/usr/bin/abmlite`

```diff

-1399.9.0.0.0
-  __TEXT.__text: 0x199f0
-  __TEXT.__auth_stubs: 0x760
+1416.1.0.0.0
+  __TEXT.__text: 0x1a24c
+  __TEXT.__auth_stubs: 0x770
   __TEXT.__objc_stubs: 0x560
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x390
-  __TEXT.__gcc_except_tab: 0x1bc8
-  __TEXT.__cstring: 0x92b
+  __TEXT.__gcc_except_tab: 0x1c40
+  __TEXT.__cstring: 0x11b1
   __TEXT.__oslogstring: 0xc6
   __TEXT.__objc_classname: 0xd
   __TEXT.__objc_methtype: 0x14
   __TEXT.__objc_methname: 0x31e
-  __TEXT.__unwind_info: 0x498
-  __DATA_CONST.__auth_got: 0x3c8
+  __TEXT.__unwind_info: 0x490
+  __DATA_CONST.__auth_got: 0x3d0
   __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x490
   __DATA_CONST.__cfstring: 0x160

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libedit.3.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 07D61EDB-BCED-3F76-AD4A-86F35B8CC398
-  Functions: 145
-  Symbols:   323
-  CStrings:  162
+  UUID: F0A8801F-5C4F-31C5-BAB0-3EAE4B5ADA00
+  Functions: 146
+  Symbols:   326
+  CStrings:  169
 
Symbols:
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyBasebandWatchdogStop
+ __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1402: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1411: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:1518: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:828: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/list:836: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZZugAMmXy5X1pnDSjGsVCWIZ0Xvrni1Yi-jms/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
