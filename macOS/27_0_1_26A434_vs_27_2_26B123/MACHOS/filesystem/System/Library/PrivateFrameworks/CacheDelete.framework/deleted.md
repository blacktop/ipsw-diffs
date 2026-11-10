## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-904.0.7.0.0
-  __TEXT.__text: 0x5c32c
+904.40.2.0.0
+  __TEXT.__text: 0x5c590
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_stubs: 0x6780
-  __TEXT.__objc_methlist: 0x2f64
+  __TEXT.__objc_stubs: 0x67a0
+  __TEXT.__objc_methlist: 0x2f6c
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x2738
   __TEXT.__cstring: 0x45fe
-  __TEXT.__objc_methname: 0x7c33
-  __TEXT.__oslogstring: 0xa14d
+  __TEXT.__objc_methname: 0x7c43
+  __TEXT.__oslogstring: 0xa247
   __TEXT.__objc_classname: 0x3fb
   __TEXT.__objc_methtype: 0xeab
-  __TEXT.__unwind_info: 0x1078
+  __TEXT.__unwind_info: 0x1080
   __DATA_CONST.__const: 0x1ed8
   __DATA_CONST.__cfstring: 0x47c0
   __DATA_CONST.__objc_classlist: 0x120

   __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x4910
-  __DATA.__objc_selrefs: 0x1ee0
+  __DATA.__objc_selrefs: 0x1ee8
   __DATA.__objc_ivar: 0x38c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x4e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1307
-  Symbols:   3057
-  CStrings:  3098
+  Functions: 1308
+  Symbols:   3059
+  CStrings:  3103
 
Symbols:
+ +[CacheDeleteAnalytics isInternalBuild]
+ GCC_except_table65
+ GCC_except_table71
+ _objc_msgSend$isInternalBuild
- GCC_except_table64
- GCC_except_table70
CStrings:
+ "Developer type %d for %@, treating as third-party"
+ "Fair Purge Analytics: reporting up to %lu third-party apps individually on a %@ build"
+ "Unable to get LSBundleRecord for %@ : %@"
+ "Unknown developer type for %@, treating as first-party on internal build"
+ "isInternalBuild"
```
