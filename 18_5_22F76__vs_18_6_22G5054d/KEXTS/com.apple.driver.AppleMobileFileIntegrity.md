## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-938.120.13.0.0
-  __TEXT.__cstring: 0xb0d5
+938.140.13.0.0
+  __TEXT.__cstring: 0xb030
   __TEXT.__const: 0x1580
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x26a70
+  __TEXT_EXEC.__text: 0x269a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x402
   __DATA.__common: 0xb0

   __DATA_CONST.__kalloc_type: 0xfc0
   __DATA_CONST.__kalloc_var: 0x1360
   __DATA_CONST.__assert: 0xf0
-  UUID: 378DF758-22D9-378D-9C3A-3C4C80DCAC65
+  UUID: E6BC9939-FA04-33CC-AF8E-4D969B44F2C4
   Functions: 842
   Symbols:   0
-  CStrings:  1105
+  CStrings:  1102
 
Functions:
~ __ZN34AppleMobileFileIntegrityUserClient20isCdhashInTrustCacheEP8OSObjectPvP25IOExternalMethodArguments : 372 -> 220
~ __ZL15_policy_syscallP4prociy : 2488 -> 2436
CStrings:
+ "21:07:35"
+ "Jun 11 2025"
- "%s: Only allowed processes can check the trustcache\n"
- "%s: only allowed process can check the trust cache\n"
- "20:14:59"
- "Apr 22 2025"
- "int _check_cdhash_in_trustcache(struct proc *, user_addr_t)"

```
