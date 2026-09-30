## CoreServicesInternal

> `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/Versions/A/CoreServicesInternal`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__lazy_load_got`
- `__DATA_DIRTY.__data`

```diff

-606.0.0.0.0
-  __TEXT.__text: 0x369a8
+608.0.0.0.0
+  __TEXT.__text: 0x36a40
   __TEXT.__lazy_helpers: 0x690
-  __TEXT.__cstring: 0x2784
+  __TEXT.__cstring: 0x2798
   __TEXT.__const: 0x4f0
-  __TEXT.__oslogstring: 0x2c14
-  __TEXT.__unwind_info: 0xcb8
+  __TEXT.__oslogstring: 0x2c24
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x428
-  __AUTH_CONST.__cfstring: 0x1a60
+  __AUTH_CONST.__cfstring: 0x1a80
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__lazy_load_got: 0xa0
   __AUTH_CONST.__auth_got: 0xe50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libfakelink.dylib
-  Functions: 787
+  Functions: 785
   Symbols:   1508
-  CStrings:  648
+  CStrings:  649
 
Functions:
~ __ZL36CFURLCreateByResolvingDataInBookmarkPK13__CFAllocatorR12BookmarkDatajmPK9__CFArrayPhPP9__CFErrorPPK7__CFURL : 13480 -> 13584
~ __ZL12fileIDsMatchR12BookmarkDatajPK7__CFURL : 340 -> 480
~ _OUTLINED_FUNCTION_2 : 16 -> 24
~ _OUTLINED_FUNCTION_3 : 24 -> 16
~ _OUTLINED_FUNCTION_9 : 12 -> 20
- _OUTLINED_FUNCTION_10
- _ZL36CFURLCreateByResolvingDataInBookmarkPK13__CFAllocatorR12BookmarkDatajmPK9__CFArrayPhPP9__CFErrorPPK7__CFURL.cold.33
~ _ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh.cold.1 : 64 -> 68
~ _ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh.cold.2 : 64 -> 68
~ _ZL18matchURLToBookmarkR12BookmarkDatajPK7__CFURLPh.cold.3 : 64 -> 68
CStrings:
+ "COMPLETED RESOLUTION of a bookmark to a filesystem item, depth=%u item=<%p: %@>, stale=%{bool}d"
+ "mp-apple-quarantine"
- "COMPLETED RESOLUTION of a bookmark to a filesystem item, depth=%u item=<%p: %@>"
```
