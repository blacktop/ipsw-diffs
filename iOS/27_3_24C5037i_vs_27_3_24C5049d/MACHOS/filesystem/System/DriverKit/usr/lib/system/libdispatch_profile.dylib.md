## libdispatch_profile.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_profile.dylib`

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
-  __TEXT.__text: 0x45f30
+1605.60.5.0.0
+  __TEXT.__text: 0x45fbc
   __TEXT.__const: 0x7a0
   __TEXT.__cstring: 0x6493
   __TEXT.__dof_dispatch: 0x4712
Functions:
~ _dispatch_data_create_with_transform : 304 -> 316
~ ____dispatch_transform_from_base32_with_table_block_invoke : 572 -> 588
~ ____dispatch_transform_from_base64_block_invoke : 480 -> 496
~ ____dispatch_transform_from_utf16_block_invoke : 900 -> 992
~ ____dispatch_transform_to_utf16_block_invoke : 696 -> 700
```
