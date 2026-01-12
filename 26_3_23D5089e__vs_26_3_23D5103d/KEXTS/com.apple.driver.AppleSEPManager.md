## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

```diff

-880.80.5.0.0
+880.80.6.0.0
   __TEXT.__const: 0x94d7
-  __TEXT.__cstring: 0x105d1
-  __TEXT_EXEC.__text: 0x47bc8
+  __TEXT.__cstring: 0x108d8
+  __TEXT_EXEC.__text: 0x481f4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x168
   __DATA.__common: 0xc48

   __DATA_CONST.__auth_ptr: 0x38
   __DATA_CONST.__mod_init_func: 0xc0
   __DATA_CONST.__mod_term_func: 0xc0
-  __DATA_CONST.__const: 0x9ad8
+  __DATA_CONST.__const: 0x9b28
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: 0398E585-99CA-32F9-9191-66B2CC465E27
-  Functions: 2411
+  UUID: 11FFF20B-ED78-3441-8D45-A590069702AD
+  Functions: 2419
   Symbols:   0
-  CStrings:  1431
+  CStrings:  1447
 
CStrings:
+ "!_fips_reseed_in_progress"
+ "\"Failed to reseed XNU PRNG after %d attempts during boot\" @%s:%d"
+ "\"Unreachable.\" @%s:%d"
+ "%s: FIPS reseed complete, waking up pending sleep operation\n"
+ "%s: FIPS reseed completed\n"
+ "%s: FIPS reseed rejected: SEP not ready (state: %u)\n"
+ "%s: FIPS reseed rejected: operation already in progress\n"
+ "%s: FIPS reseed rejected: system not in PM_STATE_ON (current: %u)\n"
+ "%s: FIPS reseed started\n"
+ "%s: Power state transition %u -> %u proceeding after FIPS reseeding completed\n"
+ "%s: Power state transition %u -> %u waiting for FIPS reseeding to complete\n"
+ "121111121222121211121212221211111111112212221121111121222211111111121222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221211222222222222222222222222222222222221212"
+ "AppleSEP:WARNING: Unable to reseed XNU PRNG, attempt %d/%d\n"
+ "GET_ENTROPY_FOR_XNU_PRNG call to SEP returned unknown error"
+ "Unable to retrieve randomness out of SEP"
+ "_fips_reseed_in_progress"
+ "bool AppleSEPManager::reseedXNUPRNG()"
+ "bool AppleSEPManager::tryStartReseed()_block_invoke"
+ "void AppleSEPManager::endReseed()_block_invoke"
- "\"GET_ENTROPY_FOR_XNU_PRNG call to SEP returned unknown error\" @%s:%d"
- "12111112122212121112121222121111111111221222112111112122221111111112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121122222222222222222222222222222222222121"
- "void AppleSEPManager::reseedXNUPRNG()"

```
