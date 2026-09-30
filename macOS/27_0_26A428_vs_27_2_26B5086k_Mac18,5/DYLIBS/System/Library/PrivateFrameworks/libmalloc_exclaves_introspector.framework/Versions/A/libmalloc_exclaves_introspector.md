## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/Versions/A/libmalloc_exclaves_introspector`

```diff

-886.0.8.0.0
-  __TEXT.__text: 0x4744
+886.40.15.0.0
+  __TEXT.__text: 0x47c4
   __TEXT.__const: 0x83
-  __TEXT.__cstring: 0x21c3
+  __TEXT.__cstring: 0x21c1
   __TEXT.__unwind_info: 0x140
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x188
Functions:
~ _xzm_segment_group_segment_foreach_span : 440 -> 464
~ _xzm_print_task : 5072 -> 5096
~ __xzm_introspect_enumerate : 852 -> 868
~ ____xzm_introspect_enumerate_block_invoke : 516 -> 560
~ __xzm_print_block_invoke.185 : 1464 -> 1484
CStrings:
+ "    \"buffer_len\": %u, \n"
+ "    \"max_len\": %u, \n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:1033)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:1031)"
- "    \"buffer_len\": %llu, \n"
- "    \"max_len\": %llu, \n"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:995)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:993)"
```
