## com.apple.driver.AppleSDXC

> `com.apple.driver.AppleSDXC`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-397.0.2.0.1
+397.0.4.0.0
   __TEXT.__cstring: 0x2728
-  __TEXT.__os_log: 0x2035
+  __TEXT.__os_log: 0x2095
   __TEXT.__const: 0x5f0
-  __TEXT_EXEC.__text: 0x235bc
+  __TEXT_EXEC.__text: 0x236d4
   __TEXT_EXEC.__auth_stubs: 0x670
   __DATA.__data: 0x118
   __DATA.__common: 0x108

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xe0
-  Functions: 700
-  Symbols:   1422
-  CStrings:  569
+  Functions: 703
+  Symbols:   1426
+  CStrings:  570
 
Symbols:
+ _OUTLINED_FUNCTION_202
+ _OUTLINED_FUNCTION_203
+ _OUTLINED_FUNCTION_204
+ __ZZN13AppleSDXCSlot15EnableUHSSpeedsEvE11_os_log_fmt_0
CStrings:
+ "%s: Enabling UHS Speeds. status=0x%x, error_state=%d, counter=%d retry count=%d, behavior=0x%x\n"
```
