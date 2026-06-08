## CoreLocationRepromptAlwaysAuthPromptPlugin

> `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0x4190
-  __TEXT.__auth_stubs: 0x270
+3164.0.0.0.0
+  __TEXT.__text: 0x3f88
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_stubs: 0xb80
   __TEXT.__objc_methlist: 0x570
   __TEXT.__const: 0xe4
-  __TEXT.__gcc_except_tab: 0x580
+  __TEXT.__gcc_except_tab: 0x548
   __TEXT.__oslogstring: 0x2be
   __TEXT.__objc_methname: 0xe78
-  __TEXT.__cstring: 0xa0
-  __TEXT.__objc_classname: 0xc7
+  __TEXT.__cstring: 0xdd2
+  __TEXT.__objc_classname: 0xc1
   __TEXT.__objc_methtype: 0x577
-  __TEXT.__unwind_info: 0x200
-  __DATA_CONST.__auth_got: 0x148
-  __DATA_CONST.__got: 0xe8
+  __TEXT.__unwind_info: 0x1d0
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0xe8
   __DATA.__objc_const: 0xf08
   __DATA.__objc_selrefs: 0x4b8
   __DATA.__objc_ivar: 0x40

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7D52319-DA0F-3E44-8F15-8DBF0AD1C97E
-  Functions: 68
-  Symbols:   88
-  CStrings:  294
+  UUID: 2CA9ACDD-3F27-33F4-A3E6-4C0CFAE18165
+  Functions: 71
+  Symbols:   89
+  CStrings:  301
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x8
- __os_feature_enabled_impl
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "Solarium"
- "SwiftUI"

```
