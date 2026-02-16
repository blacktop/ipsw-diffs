## Required

> `/System/Library/Trace/Providers/Required.bundle/Required`

```diff

-134.0.0.0.0
-  __TEXT.__text: 0x8f2c
-  __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_stubs: 0x720
-  __TEXT.__objc_methlist: 0x2d0
+134.100.19.0.0
+  __TEXT.__text: 0x9218
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_stubs: 0x740
+  __TEXT.__objc_methlist: 0x2dc
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x9ad
-  __TEXT.__objc_methname: 0x792
+  __TEXT.__cstring: 0x1728
+  __TEXT.__objc_methname: 0x7c7
   __TEXT.__objc_classname: 0x79
-  __TEXT.__objc_methtype: 0x272
+  __TEXT.__objc_methtype: 0x29a
   __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__unwind_info: 0x350
-  __DATA_CONST.__auth_got: 0x3f0
+  __TEXT.__unwind_info: 0x368
+  __DATA_CONST.__auth_got: 0x3e0
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__cfstring: 0x540
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA.__objc_const: 0x538
-  __DATA.__objc_selrefs: 0x250
+  __DATA.__objc_const: 0x540
+  __DATA.__objc_selrefs: 0x260
   __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x190
   __DATA.__data: 0xe8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 84E2BD0F-BA55-321E-947D-CB1EDE3ED4FF
-  Functions: 196
-  Symbols:   179
-  CStrings:  252
+  UUID: 1157FC81-52D8-302C-9F67-22FC942E0E2C
+  Functions: 199
+  Symbols:   177
+  CStrings:  272
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x8
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHpougDu7mHTwVcZzb67Fpcb9mN9T4C0zAoKTMQ/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "AbsTimeOffset"
+ "B32@0:8^{ktrace_target_process=i}16^@24"
+ "ContTimeOffset"
+ "abs_time_offset"
+ "cont_time_offset"
+ "dictionaryWithDictionary:"
+ "shouldTargetProcess:error:"

```
