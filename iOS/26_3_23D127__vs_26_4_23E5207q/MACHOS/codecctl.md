## codecctl

> `/usr/bin/codecctl`

```diff

-530.8.0.0.0
-  __TEXT.__text: 0x7734
-  __TEXT.__auth_stubs: 0x5d0
+540.19.0.0.0
+  __TEXT.__text: 0x7990
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x634
-  __TEXT.__cstring: 0xb82
+  __TEXT.__cstring: 0x10a1
   __TEXT.__const: 0x3c
-  __TEXT.__unwind_info: 0x348
-  __DATA_CONST.__auth_got: 0x2f0
+  __TEXT.__unwind_info: 0x358
+  __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__cfstring: 0xc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C33C6683-366E-3C2B-9CE2-734FD0DB2416
-  Functions: 133
-  Symbols:   124
-  CStrings:  98
+  UUID: 4F2D2E2B-6C74-3F41-9DDD-D70C09A6E0ED
+  Functions: 137
+  Symbols:   125
+  CStrings:  102
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CH4KugD_0r610xN5G9T5Oh324lqsd1FXS9bb_Ns/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4KugD_0r610xN5G9T5Oh324lqsd1FXS9bb_Ns/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4KugD_0r610xN5G9T5Oh324lqsd1FXS9bb_Ns/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
+ "/AppleInternal/Library/BuildRoots/4~CH4KugD_0r610xN5G9T5Oh324lqsd1FXS9bb_Ns/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
