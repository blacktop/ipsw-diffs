## MLCompilerRuntime

> `/System/Library/PrivateFrameworks/MLCompilerRuntime.framework/MLCompilerRuntime`

```diff

 3404.3.1.0.0
-  __TEXT.__text: 0x50cd4
+  __TEXT.__text: 0x52694
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__const: 0x1008
-  __TEXT.__cstring: 0x1583
-  __TEXT.__gcc_except_tab: 0x43b8
-  __TEXT.__unwind_info: 0x1288
+  __TEXT.__const: 0xff8
+  __TEXT.__cstring: 0x20bf
+  __TEXT.__gcc_except_tab: 0x4428
+  __TEXT.__unwind_info: 0x12a8
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x148
   __AUTH_CONST.__auth_got: 0x3c0

   - /System/Library/PrivateFrameworks/MLCompilerRuntime.framework/Libraries/libmlc_rt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: E8770EA0-BE69-3A0B-8BF4-D2E7895B12D2
-  Functions: 854
+  UUID: 48DB4A0C-AC3C-3BEB-95B7-D89D884253DF
+  Functions: 863
   Symbols:   196
-  CStrings:  264
+  CStrings:  276
 
Symbols:
+ __ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEx
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- _nan
- _nanf
CStrings:
+ "' at index '"
+ "' would overflow"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:437: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1559: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2296: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/streambuf:281: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CHoNugBfqQiTsLOQH1r92JIk6yluSJRg7gin2YY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string_view:341: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "Value '"

```
