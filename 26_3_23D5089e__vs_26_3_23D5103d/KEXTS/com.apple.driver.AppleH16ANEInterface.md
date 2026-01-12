## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-9.200.2.0.0
+9.300.0.0.0
   __TEXT.__const: 0xbb8
   __TEXT.__cstring: 0xee37
-  __TEXT.__os_log: 0x3607f
-  __TEXT_EXEC.__text: 0x106cf0
+  __TEXT.__os_log: 0x361d2
+  __TEXT_EXEC.__text: 0x106fb4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x434c
   __DATA.__common: 0x658

   __DATA_CONST.__const: 0xc2f8
   __DATA_CONST.__kalloc_type: 0x3ac0
   __DATA_CONST.__kalloc_var: 0x3160
-  UUID: F9A0057B-777E-3C0A-B249-3240E1E24A0C
+  UUID: 0DC5EE3F-4F63-3C86-81C1-DFADBD798453
   Functions: 3296
   Symbols:   0
-  CStrings:  4331
+  CStrings:  4333
 
Functions:
~ __ZN11ANEHWDevice26ANE_ProgramUnprepare_gatedEP21ANEProgramPrepareArgs : 2256 -> 2444
~ __ZN11ANEHWDevice51ANE_ProgramSendRequestInitialChecksAndLookups_gatedEP21ANEProgramRequestArgsP15ANESharedEventsP37ANEProgramSendRequestAdditionalParams : 9200 -> 9360
~ __ZN11ANEHWDevice26ANE_MemoryMapRequest_gatedEPK18ANEMemoryMapParamsbbRNSt3__110unique_ptrI21ANEResourceCollectionNS3_14default_deleteIS5_EEEE : 12532 -> 12776
~ __ZN11ANEHWDevice23aneAddressToHostAddressEy : 836 -> 948
~ __ZN11ANEHWDevice26cleanupAllChainingMappingsEP25ANEChainingCacheReqParams : 1836 -> 1840
CStrings:
+ "%s programHandle: 0x%llx cacheHandle: 0x%llx groupCacheHandle: 0x%llx\n"
+ "%s: %s: Invalidate cache req programHandle: 0x%llx programId: %d processId: %d procedureId: %d\n"
+ "[ERROR] %s: %s: invalid procedureId: %u, kANEMaxProcedures: %u\n"
- "%s programHandle: 0x%llx cacheHandle: 0x%llx\n"

```
