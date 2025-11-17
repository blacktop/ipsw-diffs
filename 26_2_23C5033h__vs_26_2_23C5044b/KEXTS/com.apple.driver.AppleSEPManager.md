## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-880.60.4.0.0
+880.62.3.0.0
   __TEXT.__const: 0x94d7
-  __TEXT.__cstring: 0x1048d
-  __TEXT_EXEC.__text: 0x47838
+  __TEXT.__cstring: 0x105d1
+  __TEXT_EXEC.__text: 0x47bc8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xc48
   __DATA.__bss: 0x4e
-  __DATA_CONST.__auth_got: 0x570
+  __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x9ac0
+  __DATA_CONST.__const: 0x9ad8
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: D8CA9E54-3DD5-3A82-92F6-30FF58B1E82A
-  Functions: 2403
+  UUID: 30D48B23-4669-3FE1-96FB-0EDC0CAA7872
+  Functions: 2411
   Symbols:   0
-  CStrings:  1424
+  CStrings:  1431
 
CStrings:
+ "!getWorkLoop()->inGate()"
+ "\"GET_ENTROPY_FOR_XNU_PRNG call to SEP returned unknown error\" @%s:%d"
+ "0 == write_random(prng_entropy, sizeof(prng_entropy))"
+ "Failed to get response from SEP when getting entropy"
+ "IOReturn AppleSEPControl::cmsgGET_ENTROPY_FOR_XNU_PRNG(uint32_t *, UInt32)"
+ "rand_data"
+ "void AppleSEPManager::reseedXNUPRNG()"

```
