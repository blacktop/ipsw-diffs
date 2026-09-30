## com.apple.driver.AppleMultitouchDriver

> `com.apple.driver.AppleMultitouchDriver`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__got`

```diff

-10400.39.2.0.0
-  __TEXT.__const: 0xf8
+10400.42.0.0.0
+  __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x1e89
   __TEXT.__os_log: 0x3400
-  __TEXT_EXEC.__text: 0x1a8ac
-  __TEXT_EXEC.__auth_stubs: 0x620
+  __TEXT_EXEC.__text: 0x1a8c0
+  __TEXT_EXEC.__auth_stubs: 0x630
   __DATA.__data: 0xca
   __DATA.__common: 0x1d0
   __DATA.__bss: 0x11

   __DATA_CONST.__const: 0x55c0
   __DATA_CONST.__kalloc_var: 0x280
   __DATA_CONST.__kalloc_type: 0x7c0
-  __DATA_CONST.__auth_got: 0x310
+  __DATA_CONST.__auth_got: 0x318
   __DATA_CONST.__got: 0x110
   Functions: 524
-  Symbols:   1393
+  Symbols:   1394
   CStrings:  476
 
Symbols:
+ _kern_config_is_development
Functions:
~ __ZN31AppleMultitouchDeviceUserClient11injectFrameEi : 368 -> 372
~ __ZN31AppleMultitouchDeviceUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 444 -> 460
```
