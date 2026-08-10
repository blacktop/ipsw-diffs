## com.apple.security.AppleImage4

> `com.apple.security.AppleImage4`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__image4_exp`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

 374.0.0.0.0
   __TEXT.__const: 0xe830
   __TEXT.__cstring: 0x642b
-  __TEXT_EXEC.__text: 0x23fdc
+  __TEXT_EXEC.__text: 0x2401c
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x738
   __DATA.__bss: 0x2ce
Functions:
~ sub_fffffe00090100b4 -> sub_fffffe0009017204 : 372 -> 436
CStrings:
+ "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Wed Aug  5 21:45:34 PDT 2026; root:AppleImage4-374~13653/AppleImage4/RELEASE_ARM64E"
+ "Darwin Image4 Extension Version 7.0.0: Wed Aug  5 21:45:34 PDT 2026; root:AppleImage4-374~13653/AppleImage4/RELEASE_ARM64E"
- "@(#)VERSION:Darwin Image4 Extension Version 7.0.0: Tue Jul 14 21:12:19 PDT 2026; root:AppleImage4-374~10023/AppleImage4/RELEASE_ARM64E"
- "Darwin Image4 Extension Version 7.0.0: Tue Jul 14 21:12:19 PDT 2026; root:AppleImage4-374~10023/AppleImage4/RELEASE_ARM64E"
```
