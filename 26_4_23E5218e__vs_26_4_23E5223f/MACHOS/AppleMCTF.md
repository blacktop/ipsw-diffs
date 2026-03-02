## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

 905.36.1.0.0
-  __TEXT.__text: 0x777c4
-  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__text: 0x76d54
+  __TEXT.__auth_stubs: 0xd50
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x24dd8
-  __TEXT.__const: 0x20128
+  __TEXT.__gcc_except_tab: 0x638
+  __TEXT.__cstring: 0x23a95
+  __TEXT.__const: 0x20148
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x618
-  __DATA_CONST.__auth_got: 0x6c0
+  __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x4238

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2BDF8602-2728-3873-BB40-9D0CB3745470
-  Functions: 633
-  Symbols:   356
-  CStrings:  3023
+  UUID: 211C40D4-8D66-3E42-B8C5-BF86984B2AAD
+  Functions: 631
+  Symbols:   355
+  CStrings:  3009
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "23:11:13"
+ "Feb 26 2026"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJRfugBnSH262HLdYCQdx3LdPVHK9ygRxigvmes/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "21:46:58"
- "Feb 17 2026"

```
