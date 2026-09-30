## com.apple.driver.AppleSEPCredentialManager

> `com.apple.driver.AppleSEPCredentialManager`

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

-949.0.9.0.0
-  __TEXT.__cstring: 0x1312c
-  __TEXT.__const: 0x420
-  __TEXT_EXEC.__text: 0x4dcf4
+949.0.13.0.0
+  __TEXT.__cstring: 0x13342
+  __TEXT.__const: 0x428
+  __TEXT_EXEC.__text: 0x4e214
   __TEXT_EXEC.__auth_stubs: 0x660
   __DATA.__data: 0x3061
   __DATA.__common: 0x9c8

   __DATA_CONST.__auth_got: 0x330
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x10
-  Functions: 1016
+  Functions: 1019
   Symbols:   0
-  CStrings:  1971
+  CStrings:  1981
 
CStrings:
+ "%s: %s: *** GOING OFFLINE *** ---> aborting SEP command=%u (isPoweringOff=%s, isSystemShuttingDown=%s).\n"
+ "%s: %s: marked system shutting down, stateFlags=0x%x.\n"
+ "%s: %s: newState=%u (prev=%u), stateFlags=0x%x.\n"
+ "%s: %s: prepared for system shutdown.\n"
+ "%s: %s: preparing for system shutdown.\n"
+ "%s: %s: timed out waiting for %s (timeoutMs=%llu).\n"
+ "%s: %s: timed out waiting for AppleSEPManager (timeoutMs=%llu).\n"
+ "%s: %s: wait canceled, system is shutting down (cmd=%u).\n"
+ "%s: %s: waiting (cmd=%u).\n"
+ "121111121222121212111111111111112121122211122212211"
+ "21:20:00"
+ "Jul 14 2026"
+ "markSystemIsShuttingDownGated"
+ "newState"
+ "sigSize > 0 && sigSize <= kACMCredentialDataSignatureMaxSize"
+ "systemWillShutdown"
+ "waitForSEPEndpoint"
- "%s: %s: called, currentState=%u -> newState=%u.\n"
- "%s: %s: waiting cmd=%u.\n"
- "12111112122212121211111111111111212112211122212211"
- "20:59:31"
- "Jun 30 2026"
- "newstate"
- "sepEndpoint"
```
