## libmalloc_exclaves_introspector

> `/System/Library/PrivateFrameworks/libmalloc_exclaves_introspector.framework/Versions/A/libmalloc_exclaves_introspector`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`

```diff

-886.0.4.0.0
+886.0.8.0.0
   __TEXT.__text: 0x4848
   __TEXT.__const: 0x83
   __TEXT.__cstring: 0x21c3
CStrings:
+ "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYzZEa/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:995)"
+ "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYzZEa/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:993)"
- "BUG IN LIBMALLOC: malloc assertion \"main_address\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gNQZPz/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:995)"
- "BUG IN LIBMALLOC: malloc assertion \"zone\" failed (/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.gNQZPz/Sources/libmalloc_frameworks/src/xzone_malloc/xzone_introspect.c:993)"
```
