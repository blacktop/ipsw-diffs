## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/libmalloc_exclaves_introspector`

```diff

-812.100.31.0.0
-  __TEXT.__text: 0x43cc
+812.160.3.0.0
+  __TEXT.__text: 0x440c
   __TEXT.__auth_stubs: 0x200
   __TEXT.__const: 0x7b
   __TEXT.__cstring: 0x20ff

   __DATA.__bss: 0x11
   __DATA.__common: 0x4
   - /usr/lib/libSystem.B.dylib
-  UUID: 0DAAB8E8-0093-3140-890F-CF3F4C3384A9
+  UUID: 8CCCC12D-F1FD-3459-B631-493472AD3886
   Functions: 48
   Symbols:   162
   CStrings:  268
Functions:
~ ___xzm_print_block_invoke_4 : 1356 -> 1420
CStrings:
+ "        \"user_slices\": %u,\n"
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/E92950EA-C068-402C-AF6A-60EA3B1C8D2B/TemporaryDirectory.8ZJcbl/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:838)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/E92950EA-C068-402C-AF6A-60EA3B1C8D2B/TemporaryDirectory.8ZJcbl/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:836)"
- "        \"slot_slices\": %u,\n"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/Library/Caches/com.apple.xbs/FB491110-B229-4C38-BCD3-DF25C3C71EE8/TemporaryDirectory.J5DpC0/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:838)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/Library/Caches/com.apple.xbs/FB491110-B229-4C38-BCD3-DF25C3C71EE8/TemporaryDirectory.J5DpC0/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:836)"

```
