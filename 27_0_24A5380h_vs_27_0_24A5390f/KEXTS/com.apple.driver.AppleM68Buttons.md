## com.apple.driver.AppleM68Buttons

> `com.apple.driver.AppleM68Buttons`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

 132.0.0.0.0
-  __TEXT.__cstring: 0x4e79
+  __TEXT.__cstring: 0x4eb6
   __TEXT.__const: 0x208
   __TEXT.__os_log: 0x61f
-  __TEXT_EXEC.__text: 0x1d094
+  __TEXT_EXEC.__text: 0x1d0d0
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0xca
   __DATA.__common: 0x88

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 328
   Symbols:   0
-  CStrings:  628
+  CStrings:  629
 
Functions:
~ _DeserializeCredential : 1380 -> 1440
CStrings:
+ "sigSize > 0 && sigSize <= kACMCredentialDataSignatureMaxSize"
```
