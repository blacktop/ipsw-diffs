## ArchiveService

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/XPCServices/ArchiveService.xpc/ArchiveService`

```diff

-1827.4.3.2.0
-  __TEXT.__text: 0x31950
-  __TEXT.__auth_stubs: 0x19d0
+1827.4.6.0.0
+  __TEXT.__text: 0x30b38
+  __TEXT.__auth_stubs: 0x19c0
   __TEXT.__objc_stubs: 0x1ee0
   __TEXT.__objc_methlist: 0x85c
-  __TEXT.__gcc_except_tab: 0x46e0
+  __TEXT.__gcc_except_tab: 0x46dc
   __TEXT.__const: 0x902
   __TEXT.__objc_methname: 0x2892
-  __TEXT.__cstring: 0x23e2
+  __TEXT.__cstring: 0x1632
   __TEXT.__objc_classname: 0x152
   __TEXT.__objc_methtype: 0xf9f
   __TEXT.__oslogstring: 0x1486

   __TEXT.__swift5_fieldmd: 0xb8
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__unwind_info: 0x12e0
   __TEXT.__eh_frame: 0xe8
-  __DATA_CONST.__auth_got: 0xcf8
+  __DATA_CONST.__auth_got: 0xcf0
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0xf8
   __DATA_CONST.__const: 0x1190

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B1D3A3BE-C7DE-3711-B8E3-FFC18F956D48
-  Functions: 721
-  Symbols:   653
-  CStrings:  896
+  UUID: 1AB5ED9B-05A4-3B4B-9E42-9B04EBAA1DE3
+  Functions: 718
+  Symbols:   652
+  CStrings:  885
 
Symbols:
+ _SecPolicyCreateXcodeAEASigning
- _SecPolicyCreateBasicX509
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1476: libc++ Hardening assertion !empty() failed: string::back(): string is empty\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3371: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:329: libc++ Hardening assertion __len <= static_cast<size_type>(numeric_limits<difference_type>::max()) failed: string_view::string_view(_CharT *, size_t): length does not fit in difference_type\n"
- "/AppleInternal/Library/BuildRoots/4~CI7XugDM_3hKU0Uai9Iq9dWYA7FUzFYYeX76-_c/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"

```
