## com.apple.driver.AppleLockdownMode

> `com.apple.driver.AppleLockdownMode`

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

-128.0.4.0.0
+128.0.5.0.0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x4892
-  __TEXT_EXEC.__text: 0x15064
+  __TEXT.__cstring: 0x48cf
+  __TEXT_EXEC.__text: 0x150a0
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 211
   Symbols:   0
-  CStrings:  494
+  CStrings:  495
 
Functions:
~ _DeserializeCredential : 1380 -> 1440
CStrings:
+ "sigSize > 0 && sigSize <= kACMCredentialDataSignatureMaxSize"
```
