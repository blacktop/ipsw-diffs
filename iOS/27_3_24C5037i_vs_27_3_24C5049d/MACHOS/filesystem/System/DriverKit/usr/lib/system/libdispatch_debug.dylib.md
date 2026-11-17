## libdispatch_debug.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_debug.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__dof_dispatch`
- `__TEXT.__dof_voucher`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`

```diff

-1605.60.4.0.0
-  __TEXT.__text: 0xb890c
+1605.60.5.0.0
+  __TEXT.__text: 0xb8a74
   __TEXT.__const: 0x54b
   __TEXT.__cstring: 0x8a15
   __TEXT.__dof_dispatch: 0x288c
Functions:
~ _dispatch_data_create_with_transform : 400 -> 416
~ ____dispatch_transform_from_base32_with_table_block_invoke : 1108 -> 1172
~ ____dispatch_transform_from_base64_block_invoke : 948 -> 1012
~ ____dispatch_transform_from_utf16_block_invoke : 2188 -> 2380
~ ____dispatch_transform_to_utf16_block_invoke : 1456 -> 1480
```
