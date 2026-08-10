## libdispatch.dylib

> `/usr/lib/system/libdispatch.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1605.0.1.0.0
-  __TEXT.__text: 0x3de9c
+1605.0.2.0.0
+  __TEXT.__text: 0x3de44
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x750
   __TEXT.__cstring: 0x61a0

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libunwind.dylib
-  Functions: 1379
+  Functions: 1378
   Symbols:   1803
   CStrings:  512
 
Functions:
- _OUTLINED_FUNCTION_8
~ __dispatch_block_sync_invoke.cold.3 : 404 -> 324
~ __dispatch_root_queue_drain_deferred_item.cold.1 : 516 -> 528
```
