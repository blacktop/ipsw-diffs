## com.apple.driver.AppleUSBLightningAdapter

> `com.apple.driver.AppleUSBLightningAdapter`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`

```diff

-91.0.0.0.0
+92.0.0.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1316
+  __TEXT.__cstring: 0x135b
   __TEXT.__os_log: 0xdbe
-  __TEXT_EXEC.__text: 0x5d9c
+  __TEXT_EXEC.__text: 0x5dd0
   __TEXT_EXEC.__auth_stubs: 0x350
   __DATA.__data: 0xc4
   __DATA.__common: 0x60

   __DATA_CONST.__got: 0xa8
   Functions: 107
   Symbols:   0
-  CStrings:  179
+  CStrings:  180
 
Functions:
~ __ZN24AppleUSBLightningAdapter11auxpBosInfoEPh : 1368 -> 1420
CStrings:
+ "[ERROR] %s::%s(): BOS wTotalLength changed mid-read: was %u, now %u\n"
```
