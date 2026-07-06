## HybridDatabaseTokenizer

> `/System/Library/PrivateFrameworks/HybridDatabaseTokenizer.framework/Versions/A/HybridDatabaseTokenizer`

```diff

-  __TEXT.__text: 0x23c4
-  __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__constg_swiftt: 0x7a
-  __TEXT.__swift5_typeref: 0x22
-  __TEXT.__swift5_reflstr: 0xa
-  __TEXT.__swift5_fieldmd: 0x3c
+  __TEXT.__text: 0x2a8c
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
+  __TEXT.__oslogstring: 0x18e
   __TEXT.__cstring: 0x60
-  __TEXT.__unwind_info: 0x168
-  __TEXT.__eh_frame: 0x168
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
-  __AUTH_CONST.__auth_got: 0x168
+  __AUTH_CONST.__auth_got: 0x178
   __DATA.__data: 0x18
   __DATA.__bss: 0x10
+  __DATA_DIRTY.__data: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/NaturalLanguage.framework/Versions/A/NaturalLanguage

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 50
-  Symbols:   57
+  Functions: 68
+  Symbols:   60
   CStrings:  12
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
Symbols:
+ _objc_autoreleaseReturnValue
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_
- _objc_retain
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "HDBTokenizer: segment: failed to extract UTF-8 bytes (length %llu)"
+ "HDBTokenizer: segment: sanitized input still failed UTF-8 decode (original %zu bytes)"
+ "HDBTokenizer: segment: token normalization failed"
- "HDBTokenizer: Latin-ASCII transform failed (%llu UTF-16 code units)"
- "HDBTokenizer: failed to extract UTF-8 bytes for normalized string of length %llu"
- "HDBTokenizer: sanitized input still failed UTF-8 decode (original %zu bytes, sanitized %zu bytes)"

```
