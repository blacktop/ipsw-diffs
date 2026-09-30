## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3288.40.13.0.0
-  __TEXT.__text: 0x4ccf8
+3288.40.14.0.0
+  __TEXT.__text: 0x4ce0c
   __TEXT.__auth_stubs: 0x780
   __TEXT.__cstring: 0xf7c5
   __TEXT.__const: 0x220
Functions:
~ sub_10000525c : 68 -> 84
~ sub_1000148dc -> sub_1000148ec : 572 -> 596
~ sub_1000307b4 -> sub_1000307dc : 284 -> 276
~ sub_1000429b8 -> sub_1000429d8 : 1028 -> 1040
~ sub_100042dbc -> sub_100042de8 : 3792 -> 3856
~ sub_100045bfc -> sub_100045c68 : 3480 -> 3524
~ sub_100046994 -> sub_100046a2c : 3596 -> 3720
CStrings:
+ "3288.40.14"
- "3288.40.13"
```
