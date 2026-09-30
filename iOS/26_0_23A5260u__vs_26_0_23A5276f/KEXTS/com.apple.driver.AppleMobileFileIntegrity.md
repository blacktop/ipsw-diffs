## com.apple.driver.AppleMobileFileIntegrity

> `com.apple.driver.AppleMobileFileIntegrity`

```diff

-1045.0.1.0.1
-  __TEXT.__cstring: 0xb28c
+1045.0.16.0.0
+  __TEXT.__cstring: 0xb1e7
   __TEXT.__const: 0x1590
   __TEXT.__os_log: 0x32d
-  __TEXT_EXEC.__text: 0x2843c
+  __TEXT_EXEC.__text: 0x283a4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x402
   __DATA.__common: 0xb0

   __DATA_CONST.__kalloc_type: 0xf00
   __DATA_CONST.__kalloc_var: 0x1400
   __DATA_CONST.__assert: 0xf0
-  UUID: D5F93661-8038-3DB0-8590-4A2A7BB75E31
+  UUID: 1002B193-31FD-3578-9FF1-5E9AD7A4CD18
   Functions: 881
   Symbols:   0
-  CStrings:  1116
+  CStrings:  1113
 
Functions:
~ __ZN34AppleMobileFileIntegrityUserClient20isCdhashInTrustCacheEP8OSObjectPvP25IOExternalMethodArguments : 372 -> 220
~ __ZN22LaunchConstraintPolicy5applyEPvmPPcPm : 1344 -> 1396
~ sub_fffffff00978bed8 -> __ZN22LaunchConstraintPolicy13handleFailureER23LaunchConstraintError_tPPcPm : 88 -> 596
~ __ZN22LaunchConstraintPolicy13handleFailureER23LaunchConstraintError_tPPcPm -> sub_fffffff0097d60c8 : 596 -> 88
~ __ZL15_policy_syscallP4prociy : 2488 -> 2436
CStrings:
+ "23:38:03"
+ "Jun 16 2025"
- "%s: Only allowed processes can check the trustcache\n"
- "%s: only allowed process can check the trust cache\n"
- "19:13:11"
- "May 30 2025"
- "int _check_cdhash_in_trustcache(struct proc *, user_addr_t)"

```
