## swcd

> `/usr/libexec/swcd`

```diff

 1021.2.0.0.0
-  __TEXT.__text: 0x1db48
-  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__text: 0x1e41c
+  __TEXT.__auth_stubs: 0x9f0
   __TEXT.__objc_stubs: 0x3300
   __TEXT.__objc_methlist: 0x1044
-  __TEXT.__gcc_except_tab: 0x3e4c
-  __TEXT.__cstring: 0x1bfa
+  __TEXT.__gcc_except_tab: 0x3e14
+  __TEXT.__cstring: 0x2937
   __TEXT.__const: 0xe0
   __TEXT.__objc_methname: 0x3cc8
   __TEXT.__oslogstring: 0x1948
   __TEXT.__objc_classname: 0x1da
   __TEXT.__objc_methtype: 0x11e7
-  __TEXT.__unwind_info: 0xbc0
-  __DATA_CONST.__auth_got: 0x510
+  __TEXT.__unwind_info: 0xbe0
+  __DATA_CONST.__auth_got: 0x508
   __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0xae0
   __DATA_CONST.__cfstring: 0x13e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4527392A-82F7-3D5B-BFEC-F195CE747F82
-  Functions: 370
-  Symbols:   249
-  CStrings:  1280
+  UUID: F8291F7D-CE31-31E4-94F9-799384210B02
+  Functions: 371
+  Symbols:   248
+  CStrings:  1289
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _bzero
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHodugDWKNy3QfVkm72YZGluDeyEsJahzVJZyJQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"

```
