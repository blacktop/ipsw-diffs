## libAWDSupport.dylib

> `/usr/lib/libAWDSupport.dylib`

```diff

 998.0.0.0.0
-  __TEXT.__text: 0x379a0
-  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__text: 0x376a0
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x4750
-  __TEXT.__cstring: 0x122f
+  __TEXT.__cstring: 0xad4
   __TEXT.__const: 0xf98
   __TEXT.__oslogstring: 0x7a
-  __TEXT.__unwind_info: 0x1868
+  __TEXT.__unwind_info: 0x1840
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x198
-  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__auth_got: 0x618
   __AUTH_CONST.__const: 0x1800
   __AUTH_CONST.__cfstring: 0x40
   __AUTH.__data: 0x30

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: B7CBEE5B-D325-3AB2-BE13-6329E90ADF72
-  Functions: 1119
-  Symbols:   372
-  CStrings:  194
+  UUID: 728AE933-BBF8-3291-94DF-0ABB2810604E
+  Functions: 1113
+  Symbols:   371
+  CStrings:  188
 
Symbols:
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
- "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1332: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:1340: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3352: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/4~CJkrugBzI9H_Fn59zVMdHev11w8oGDCQ9ZpqGp0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/string:3362: libc++ Hardening assertion __first <= __last failed: string::erase(first, last) called with invalid range\n"

```
