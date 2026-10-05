## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
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
-  __TEXT.__text: 0x5ab10
+904.40.2.0.0
+  __TEXT.__text: 0x5ae5c
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x6920
-  __TEXT.__objc_methlist: 0x2ff4
+  __TEXT.__objc_stubs: 0x6940
+  __TEXT.__objc_methlist: 0x2ffc
   __TEXT.__const: 0x190
-  __TEXT.__gcc_except_tab: 0x2910
+  __TEXT.__gcc_except_tab: 0x2934
   __TEXT.__cstring: 0x4977
-  __TEXT.__objc_methname: 0x7e16
-  __TEXT.__oslogstring: 0xacf0
+  __TEXT.__objc_methname: 0x7e26
+  __TEXT.__oslogstring: 0xae60
   __TEXT.__objc_classname: 0x407
   __TEXT.__objc_methtype: 0xe8c
-  __TEXT.__unwind_info: 0xfc8
+  __TEXT.__unwind_info: 0xfd0
   __DATA_CONST.__const: 0x1d28
   __DATA_CONST.__cfstring: 0x4b80
   __DATA_CONST.__objc_classlist: 0x128

   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x4a68
-  __DATA.__objc_selrefs: 0x1f08
+  __DATA.__objc_selrefs: 0x1f10
   __DATA.__objc_ivar: 0x39c
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1240
-  Symbols:   3039
-  CStrings:  3165
+  Functions: 1241
+  Symbols:   3041
+  CStrings:  3172
 
Symbols:
+ +[CacheDeleteAnalytics isInternalBuild]
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table68
+ _objc_msgSend$isInternalBuild
- GCC_except_table60
- GCC_except_table64
- GCC_except_table67
CStrings:
+ "Developer type %d for %@, treating as third-party"
+ "Fair Purge Analytics: reporting up to %lu third-party apps individually on a %@ build"
+ "Unable to get LSBundleRecord for %@ : %@"
+ "Unknown developer type for %@, treating as first-party on internal build"
+ "isInternalBuild"
+ "updateFollowup: skipping \"%{public}@\" because it became invalid"
+ "updateFollowup: skipping non-user volume \"%{public}@\""
```
