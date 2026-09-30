## HybridDatabaseTokenizer

> `/System/Library/PrivateFrameworks/HybridDatabaseTokenizer.framework/HybridDatabaseTokenizer`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types2`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-46.0.1.0.0
-  __TEXT.__text: 0x2a4c
-  __TEXT.__const: 0x120
-  __TEXT.__gcc_except_tab: 0x1ac
-  __TEXT.__constg_swiftt: 0xb2
-  __TEXT.__swift5_typeref: 0x52
+49.0.1.0.0
+  __TEXT.__text: 0x2a3c
+  __TEXT.__const: 0x148
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__constg_swiftt: 0xd2
+  __TEXT.__swift5_typeref: 0x58
   __TEXT.__swift5_reflstr: 0x42
-  __TEXT.__swift5_fieldmd: 0xa4
+  __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__oslogstring: 0x18e
+  __TEXT.__oslogstring: 0x18f
   __TEXT.__cstring: 0x60
   __TEXT.__unwind_info: 0x190
   __TEXT.__eh_frame: 0x1a0

   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50
+  __DATA_CONST.__objc_selrefs: 0x40
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x228
+  __AUTH_CONST.__const: 0x248
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x1a8
-  __DATA.__data: 0x18
+  __AUTH_CONST.__auth_got: 0x1d8
+  __DATA.__data: 0x20
   __DATA.__bss: 0x10
   __DATA_DIRTY.__data: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 68
-  Symbols:   66
+  Functions: 69
+  Symbols:   72
   CStrings:  11
 
Symbols:
+ _CFRelease
+ _CFStringCreateMutableCopy
+ _CFStringNormalize
+ _CFStringTransform
+ _objc_release_x24
+ _objc_retain_x19
CStrings:
+ "HDBTokenizer: segment: sanitized input still failed UTF-8 decode (original %llu bytes)"
- "HDBTokenizer: segment: sanitized input still failed UTF-8 decode (original %zu bytes)"
```
