## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__lazy_load_got`
- `__DATA_DIRTY.__data`

```diff

-606.0.0.0.0
-  __TEXT.__text: 0x2e0dc
+608.0.0.0.0
+  __TEXT.__text: 0x2e154
   __TEXT.__lazy_helpers: 0x9d8
   __TEXT.__cstring: 0x1b72
   __TEXT.__const: 0x5f8
-  __TEXT.__oslogstring: 0x20c1
-  __TEXT.__unwind_info: 0xab0
+  __TEXT.__oslogstring: 0x20d1
+  __TEXT.__unwind_info: 0xaa8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__got: 0x0

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 654
+  Functions: 652
   Symbols:   1214
   CStrings:  482
 
Functions:
~ _OUTLINED_FUNCTION_7 : 12 -> 20
- _OUTLINED_FUNCTION_7
~ __ZL36CFURLCreateByResolvingDataInBookmarkPK13__CFAllocatorR12BookmarkDatajmPK9__CFArrayPhPP9__CFErrorPPK7__CFURL : 11212 -> 11284
~ __ZL12fileIDsMatchR12BookmarkDatajPK7__CFURL : 340 -> 480
- __ZL36CFURLCreateByResolvingDataInBookmarkPK13__CFAllocatorR12BookmarkDatajmPK9__CFArrayPhPP9__CFErrorPPK7__CFURL.cold.32
~ __ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh.cold.1 : 64 -> 68
~ __ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh.cold.2 : 64 -> 68
~ __ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh.cold.3 : 64 -> 68
CStrings:
+ "COMPLETED RESOLUTION of a bookmark to a filesystem item, depth=%u item=<%p: %@>, stale=%{bool}d"
- "COMPLETED RESOLUTION of a bookmark to a filesystem item, depth=%u item=<%p: %@>"
```
