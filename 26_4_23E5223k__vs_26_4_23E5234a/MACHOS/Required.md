## Required

> `/System/Library/Trace/Providers/Required.bundle/Required`

```diff

 134.100.20.0.0
-  __TEXT.__text: 0x9218
-  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__text: 0x90a8
+  __TEXT.__auth_stubs: 0x790
   __TEXT.__objc_stubs: 0x740
   __TEXT.__objc_methlist: 0x2dc
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x1728
+  __TEXT.__cstring: 0x9eb
   __TEXT.__objc_methname: 0x7c7
   __TEXT.__objc_classname: 0x79
   __TEXT.__objc_methtype: 0x29a
   __TEXT.__gcc_except_tab: 0x370
-  __TEXT.__unwind_info: 0x368
-  __DATA_CONST.__auth_got: 0x3e0
+  __TEXT.__unwind_info: 0x370
+  __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x1c8
   __DATA_CONST.__cfstring: 0x5c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B4275EA-9A1F-35E1-BD52-E11C5C468234
+  UUID: 9F8933FD-DD19-3C5F-A076-FD28CA44E4E1
   Functions: 199
-  Symbols:   177
-  CStrings:  272
+  Symbols:   176
+  CStrings:  263
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
Functions:
~ sub_4a88 : 260 -> 188
~ sub_4b8c -> sub_4b44 : 508 -> 356
~ sub_4d88 -> sub_4ca8 : 492 -> 348
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJl7ugC-tjxunwpOm-eBd-Mjo55rYAIvLn8aLcI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"

```
