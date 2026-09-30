## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

 905.29.1.0.0
-  __TEXT.__text: 0x1814a0
-  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__text: 0x1814b8
+  __TEXT.__auth_stubs: 0x1060
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0xc
-  __TEXT.__const: 0x23b58
-  __TEXT.__cstring: 0x527cc
+  __TEXT.__const: 0x23b88
+  __TEXT.__cstring: 0x53aa2
   __TEXT.__gcc_except_tab: 0x720
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x8b8
-  __DATA_CONST.__auth_got: 0x838
+  __TEXT.__unwind_info: 0x8c0
+  __DATA_CONST.__auth_got: 0x840
   __DATA_CONST.__got: 0x760
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0xa110

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BF19924E-BE4A-3C7F-B262-A3F2E2E85227
-  Functions: 1587
-  Symbols:   511
-  CStrings:  6993
+  UUID: 48EF86CA-E97D-37EA-8756-764F87877C5C
+  Functions: 1595
+  Symbols:   512
+  CStrings:  7005
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1522: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIU9ugBMSzi5lCU8UkagCSYMrs0ATdH4Al63-zc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "23:57:46"
+ "23:57:48"
+ "23:57:50"
+ "23:57:51"
+ "Feb  4 2026"
- "%lld %d AVE %s: %s:%d %s | PerFrameData = NULL"
- "%lld %d AVE %s: %s:%d %s | PerFrameData = NULL\n"
- "21:03:07"
- "21:03:09"
- "21:03:10"
- "Jan 26 2026"
- "PerFrameData != __null"

```
