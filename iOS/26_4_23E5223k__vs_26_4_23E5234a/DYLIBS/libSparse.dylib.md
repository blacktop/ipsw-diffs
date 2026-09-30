## libSparse.dylib

> `/System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparse.dylib`

```diff

 184.80.2.0.0
-  __TEXT.__text: 0x187754
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__const: 0x6d0
-  __TEXT.__cstring: 0x6229
+  __TEXT.__text: 0x160374
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__const: 0x6f0
+  __TEXT.__cstring: 0x4d5c
   __TEXT.__oslogstring: 0x1c5d
-  __TEXT.__gcc_except_tab: 0xa98
-  __TEXT.__unwind_info: 0x1760
-  __TEXT.__eh_frame: 0x350
+  __TEXT.__gcc_except_tab: 0xa28
+  __TEXT.__unwind_info: 0x17b8
+  __TEXT.__eh_frame: 0x890
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0xad0
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x1d0
   __AUTH.__thread_vars: 0xd8
   __AUTH.__thread_data: 0xc

   - /System/Library/Frameworks/Accelerate.framework/Frameworks/vecLib.framework/libSparseBLAS.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 57FBA7A0-C4BE-3177-B65B-5CE4C149A5D0
-  Functions: 1980
-  Symbols:   676
-  CStrings:  709
+  UUID: 7CD35D24-9612-3D56-BAF0-473886C4A9E2
+  Functions: 1959
+  Symbols:   675
+  CStrings:  694
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:493: libc++ Hardening assertion __count <= size() failed: span<T>::first(count): count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:512: libc++ Hardening assertion __offset <= size() failed: span<T>::subspan(offset, count): offset out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:516: libc++ Hardening assertion __count <= size() - __offset failed: span<T>::subspan(offset, count): offset + count out of range\n"
- "/AppleInternal/Library/BuildRoots/4~CJk5ugCTqYxmB8imdU_Hu-czWEFYmg-FUd1VBtM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/span:525: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"

```
