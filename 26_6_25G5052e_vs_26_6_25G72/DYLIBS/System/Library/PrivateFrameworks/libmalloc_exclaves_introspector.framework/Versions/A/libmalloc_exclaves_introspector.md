## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/Versions/A/libmalloc_exclaves_introspector`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-812.160.4.0.0
+812.160.5.0.0
   __TEXT.__text: 0x4744
   __TEXT.__auth_stubs: 0x210
   __TEXT.__const: 0x83
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qTxVxd/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:838)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qTxVxd/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:836)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9bEmiu/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:838)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.9bEmiu/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:836)"
```
