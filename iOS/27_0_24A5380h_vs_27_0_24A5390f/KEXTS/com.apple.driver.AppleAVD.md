## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-989.1.0.0.0
-  __TEXT.__os_log: 0x1b0ed
-  __TEXT.__cstring: 0x7cfb
+991.0.0.0.0
+  __TEXT.__os_log: 0x1b1cb
+  __TEXT.__cstring: 0x7d1b
   __TEXT.__const: 0xcc129
-  __TEXT_EXEC.__text: 0x5fd98
-  __TEXT_EXEC.__auth_stubs: 0x700
+  __TEXT_EXEC.__text: 0x5ff10
+  __TEXT_EXEC.__auth_stubs: 0x6f0
   __DATA.__data: 0x1334
   __DATA.__common: 0x78
   __DATA.__bss: 0x14

   __DATA_CONST.__const: 0x47f8
   __DATA_CONST.__kalloc_type: 0x3680
   __DATA_CONST.__kalloc_var: 0xd70
-  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__auth_got: 0x378
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x10
-  Functions: 2163
+  Functions: 2162
   Symbols:   0
-  CStrings:  1770
+  CStrings:  1771
 
CStrings:
+ "AppleAVD: %s(): active_mcc_bit_vector_val is 0x%x\n"
+ "AppleAVD: ERROR: %s(): [Core %u] AVD Reset Function handle is NULL! Check the EDT\n"
+ "AppleAVD: INFO: %s(): Unexpected active-mcc-bit-vector value. Assume tunablesIdx is 1.\n"
+ "AppleAVD: INFO: %s(): [Core %u] AVD reset function returned %d\n"
+ "AppleAVD: INFO: %s(): [Core %u] resetPsdService(0, %u) returned %d\n"
- "AppleAVD: ERROR: %s(): AVD Reset Function handle is NULL! Check the EDT\n"
- "AppleAVD: INFO: %s(): AVD reset function returned %d\n"
- "AppleAVD: INFO: %s(): resetPsdService(0) returned %d\n"
- "setEventEntryFloat"
```
