## com.apple.driver.DiskImages

> `com.apple.driver.DiskImages`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-698.0.0.0.0
+701.0.0.0.0
   __TEXT.__cstring: 0xda8
   __TEXT_EXEC.__text: 0x942c
   __TEXT_EXEC.__auth_stubs: 0x470
CStrings:
+ "701"
- "698"
```
