## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`

```diff

-  __TEXT.__text: 0x44d8
+  __TEXT.__text: 0x4528
   __TEXT.__const: 0x7b
   __TEXT.__cstring: 0x2191
   __TEXT.__unwind_info: 0xf0
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ _xzm_segment_group_segment_foreach_span : 416 -> 452
~ ____xzm_introspect_enumerate_block_invoke_2 : 1416 -> 1460
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:995)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:993)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:960)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:958)"

```
