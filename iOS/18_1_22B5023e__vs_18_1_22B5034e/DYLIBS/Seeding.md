## Seeding

> `/System/Library/PrivateFrameworks/Seeding.framework/Seeding`

```diff

-104.0.0.0.0
-  __TEXT.__text: 0x1f7bc
+105.0.0.0.0
+  __TEXT.__text: 0x1f9ec
   __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0x15ac
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x6a0
-  __TEXT.__cstring: 0x1e20
-  __TEXT.__oslogstring: 0x2e28
+  __TEXT.__cstring: 0x1edc
+  __TEXT.__oslogstring: 0x2e82
   __TEXT.__unwind_info: 0x8a8
   __TEXT.__objc_classname: 0x256
   __TEXT.__objc_methname: 0x3eba

   - /usr/lib/libobjc.A.dylib
   Functions: 724
   Symbols:   1005
-  CStrings:  1375
+  CStrings:  1379
 
CStrings:
+ "No accounts available. Cannot proceed"
+ "No credential tokens available. Cannot proceed"
+ "-[SDBetaManager _finallyQueryProgramsForSystemAccountsWithPlatforms:credentials:betaEnrollmentTokens:completion:]"
+ "Will use BET: [%!{(MISSING)public}@]"
+ "-[SDBetaManager _queryProgramsForSystemAccountsWithPlatforms:completion:]"
+ "Proceeding without account info."
- "No accounts available."
- "No credential tokens available."

```
