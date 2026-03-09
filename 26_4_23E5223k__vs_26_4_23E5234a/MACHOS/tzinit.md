## tzinit

> `/usr/libexec/tzinit`

```diff

 88.0.0.0.0
-  __TEXT.__text: 0x108e4
-  __TEXT.__auth_stubs: 0x530
+  __TEXT.__text: 0xfd2c
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x726
   __TEXT.__gcc_except_tab: 0xbb8
-  __TEXT.__cstring: 0xe34
-  __TEXT.__unwind_info: 0x7a8
-  __DATA_CONST.__auth_got: 0x2a0
+  __TEXT.__cstring: 0x5d8
+  __TEXT.__unwind_info: 0x798
+  __DATA_CONST.__auth_got: 0x298
   __DATA_CONST.__got: 0x98
   __DATA_CONST.__const: 0x8a8
   __DATA.__bss: 0x18
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 54332009-524A-3F57-9963-18DFC4346572
-  Functions: 331
-  Symbols:   109
-  CStrings:  58
+  UUID: DD18E2BA-C132-3706-ABE7-CA98A904812C
+  Functions: 330
+  Symbols:   108
+  CStrings:  51
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJlWugCYJadJ_JNS5lyn9sR59Ynf4AdurtTnfiE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlWugCYJadJ_JNS5lyn9sR59Ynf4AdurtTnfiE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJlWugCYJadJ_JNS5lyn9sR59Ynf4AdurtTnfiE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlWugCYJadJ_JNS5lyn9sR59Ynf4AdurtTnfiE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJlWugCYJadJ_JNS5lyn9sR59Ynf4AdurtTnfiE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlWugCYJadJ_JNS5lyn9sR59Ynf4AdurtTnfiE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CJlWugCYJadJ_JNS5lyn9sR59Ynf4AdurtTnfiE/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"

```
