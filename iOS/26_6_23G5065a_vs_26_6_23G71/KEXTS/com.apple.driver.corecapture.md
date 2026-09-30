## com.apple.driver.corecapture

> `com.apple.driver.corecapture`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

   __TEXT.__os_log: 0x4336
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x200e
-  __TEXT_EXEC.__text: 0x26180
+  __TEXT_EXEC.__text: 0x2614c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308
Functions:
~ __Z35AppleOLYHAL_isDevFusedOrCSRInternalv : 120 -> 100
~ __Z29corecaptureIsDebuggbleUnifiedv : 100 -> 116
~ __ZN6CCPipe25initWithOwnerNameCapacityEP9IOServicePKcS3_PK13CCPipeOptions : 6308 -> 6272
~ __Z16DefaultLogPolicyv : 100 -> 108
~ __ZN11CCIOService17ccForcePanic_ImplEbP8OSString : 188 -> 184
~ __ZN16CCPipeUserClient12initWithTaskEP4taskPvjP12OSDictionary : 356 -> 352
~ sub_fffffe000a594248 -> sub_fffffe000a58e7e0 : 12 -> 8
~ sub_fffffe000a59b7bc -> sub_fffffe000a595d50 : 192 -> 188
~ sub_fffffe000a5ab82c -> sub_fffffe000a5a5dbc : 100 -> 96
```
