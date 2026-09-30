## HybridDatabaseTokenizer

> `/System/Library/PrivateFrameworks/HybridDatabaseTokenizer.framework/HybridDatabaseTokenizer`

```diff

-  __TEXT.__text: 0x271c
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__constg_swiftt: 0x7a
-  __TEXT.__swift5_typeref: 0x22
-  __TEXT.__swift5_reflstr: 0xa
-  __TEXT.__swift5_fieldmd: 0x3c
+  __TEXT.__text: 0x2a4c
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x1ac
+  __TEXT.__constg_swiftt: 0xb2
+  __TEXT.__swift5_typeref: 0x52
+  __TEXT.__swift5_reflstr: 0x42
+  __TEXT.__swift5_fieldmd: 0xa4
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0x4
+  __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__oslogstring: 0x1ba
-  __TEXT.__cstring: 0x51a
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__eh_frame: 0x168
+  __TEXT.__oslogstring: 0x18e
+  __TEXT.__cstring: 0x60
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__eh_frame: 0x1a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0

   __DATA_CONST.__weak_got: 0x8
   __DATA_CONST.__objc_selrefs: 0x50
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x118
+  __AUTH_CONST.__const: 0x228
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x1b8
+  __AUTH_CONST.__auth_got: 0x1a8
   __DATA.__data: 0x18
   __DATA.__bss: 0x10
+  __DATA_DIRTY.__data: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 54
-  Symbols:   67
-  CStrings:  16
+  Functions: 68
+  Symbols:   66
+  CStrings:  12
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_types2 : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ _objc_autoreleaseReturnValue
+ _objc_release_x21
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- __ZNSt3__132__internal_log_hardening_failureEPKc
- _objc_release_x24
- _objc_release_x26
- _objc_release_x28
- _objc_retain_x22
- _objc_retain_x8
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "HDBTokenizer: segment: failed to extract UTF-8 bytes (length %llu)"
+ "HDBTokenizer: segment: sanitized input still failed UTF-8 decode (original %zu bytes)"
+ "HDBTokenizer: segment: token normalization failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:442: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1362: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1371: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "HDBTokenizer: Latin-ASCII transform failed (%llu UTF-16 code units)"
- "HDBTokenizer: failed to extract UTF-8 bytes for normalized string of length %llu"
- "HDBTokenizer: sanitized input still failed UTF-8 decode (original %zu bytes, sanitized %zu bytes)"

```
