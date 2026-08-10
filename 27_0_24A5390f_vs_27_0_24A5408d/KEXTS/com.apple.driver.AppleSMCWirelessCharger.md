## com.apple.driver.AppleSMCWirelessCharger

> `com.apple.driver.AppleSMCWirelessCharger`

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

-155.0.5.0.0
+155.0.10.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x37ce
+  __TEXT.__cstring: 0x3848
   __TEXT.__os_log: 0x5f0
-  __TEXT_EXEC.__text: 0x110e4
+  __TEXT_EXEC.__text: 0x113c4
   __TEXT_EXEC.__auth_stubs: 0x5e0
   __DATA.__data: 0xcd
   __DATA.__common: 0x90

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 212
   Symbols:   0
-  CStrings:  464
+  CStrings:  468
 
Functions:
~ sub_fffffe000969ab34 -> sub_fffffe0009685af4 : 5532 -> 5760
~ sub_fffffe00096a7e64 -> sub_fffffe0009692f08 : 1456 -> 1760
~ sub_fffffe00096aa650 -> sub_fffffe0009695824 : 2132 -> 2332
~ sub_fffffe00096aaea4 -> sub_fffffe0009696140 : 112 -> 116
CStrings:
+ "%s: Failed to set WAEQ to %d (ret=%d)\n"
+ "chg-disable-inductive-fw-reload-on-crash"
+ "chg-esp-dis-coex-mask"
+ "chg-esp-keyfob-risk"
```
