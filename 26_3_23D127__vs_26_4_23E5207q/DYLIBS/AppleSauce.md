## AppleSauce

> `/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce`

```diff

-17.1.0.0.0
-  __TEXT.__text: 0x1fea4
-  __TEXT.__auth_stubs: 0x640
-  __TEXT.__gcc_except_tab: 0x1520
+17.7.0.0.0
+  __TEXT.__text: 0x21014
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__gcc_except_tab: 0x1580
   __TEXT.__const: 0x893
-  __TEXT.__cstring: 0x3f4
-  __TEXT.__unwind_info: 0xcb8
+  __TEXT.__cstring: 0x1172
+  __TEXT.__unwind_info: 0xd28
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__const: 0x48
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0xfc8
   __DATA.__data: 0xe0
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x48
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7D80CC74-0C43-37A9-BFDA-C5CBCA24F805
-  Functions: 572
-  Symbols:   162
-  CStrings:  65
+  UUID: FE14E552-0443-3664-A929-C476FBF495A4
+  Functions: 587
+  Symbols:   163
+  CStrings:  76
 
Symbols:
+ __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1162: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/deque:2310: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3352: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/4~CHn7ugAqRu2pewaVr-8AW4TM5xJ5Y5hXMRYRaRU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"

```
