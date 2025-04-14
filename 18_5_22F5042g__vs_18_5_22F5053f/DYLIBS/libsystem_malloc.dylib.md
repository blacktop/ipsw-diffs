## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

```diff

-715.120.10.0.0
-  __TEXT.__text: 0x34c5c
+715.120.12.0.0
+  __TEXT.__text: 0x34c3c
   __TEXT.__auth_stubs: 0x6f0
   __TEXT.__const: 0x50c
   __TEXT.__cstring: 0x8966
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:923)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2036)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2035)"
+ "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2137)"
+ "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:898)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:835)"
+ "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:834)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:892)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:837)"
+ "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:836)"
- "BUG IN LIBMALLOC: malloc assertion \"(start_address >= left_void.min_address && end_address + XZM_RANGE_SEPARATION <= left_void.max_address) || (start_address >= right_void.min_address + XZM_RANGE_SEPARATION && start_address + XZM_POINTER_RANGE_SIZE <= right_void.max_address)\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:891)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2004)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2003)"
- "BUG IN LIBMALLOC: malloc assertion \"(uintptr_t)segment_body < XZM_LIMIT_ADDRESS\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:2105)"
- "BUG IN LIBMALLOC: malloc assertion \"candidate_span\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:866)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.max_address >= left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:803)"
- "BUG IN LIBMALLOC: malloc assertion \"left_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:802)"
- "BUG IN LIBMALLOC: malloc assertion \"right_candidate_span % XZM_PAGE_TABLE_GRANULE == 0\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:860)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.max_address >= right_void.min_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:805)"
- "BUG IN LIBMALLOC: malloc assertion \"right_void.min_address >= left_void.max_address\" failed (/Library/Caches/com.apple.xbs/Sources/libmalloc/src/xzone/xzone_segment.c:804)"

```
