## com.apple.driver.AppleSEPManager

> `com.apple.driver.AppleSEPManager`

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

-928.0.0.0.0
-  __TEXT.__cstring: 0xd178
+928.0.2.0.0
+  __TEXT.__cstring: 0xd406
   __TEXT.__const: 0x56c
-  __TEXT_EXEC.__text: 0x2dfe4
-  __TEXT_EXEC.__auth_stubs: 0x900
+  __TEXT_EXEC.__text: 0x2ef4c
+  __TEXT_EXEC.__auth_stubs: 0x920
   __DATA.__data: 0x168
   __DATA.__common: 0xb08
   __DATA.__bss: 0x49

   __DATA_CONST.__const: 0xaa78
   __DATA_CONST.__kalloc_type: 0xc00
   __DATA_CONST.__kalloc_var: 0x50
-  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__auth_got: 0x490
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 1747
-  Symbols:   2116
-  CStrings:  1148
+  Functions: 1773
+  Symbols:   2133
+  CStrings:  1168
 
Symbols:
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _ZL17gl_fixup_rev_initP6gl_ctx
+ _ZN15AppleSEPManager19_report_sandcat_pwnEj
+ _ZN9KdbgScope3popEj
+ _ZN9KdbgScope4pushEj
+ _ZN9KdbgScopeD1Ev
+ __ZL7gl_readPK6gl_ctxyPhm
+ __ZL8gl_writePK6gl_ctxyPKhm
+ __ZN12OSDictionary11withObjectsEPPK8OSObjectPPK8OSStringjj
+ __ZN15AppleSEPManager19_report_sandcat_pwnEj
+ __ZN9IOService22CoreAnalyticsSendEventEyP8OSStringP12OSDictionaryPFiP15OSMetaClassBase5IORPCE
+ __ZN9KdbgScope3popEj
+ __ZN9KdbgScope4pushEj
+ __ZN9KdbgScopeD1Ev
+ __ZZ12gl_rec_writeP6gl_ctxPK9gl_rec_idPKhmE20kalloc_type_view_756
+ __ZZ12gl_rec_writeP6gl_ctxPK9gl_rec_idPKhmE20kalloc_type_view_800
+ __ZZ13gl_rec_deletePK6gl_ctxyE20kalloc_type_view_679
+ __ZZ13gl_rec_deletePK6gl_ctxyE20kalloc_type_view_694
+ __ZZ22gl_crash_recovery_testP6gl_ctxE21kalloc_type_view_1035
+ __ZZ22gl_crash_recovery_testP6gl_ctxE21kalloc_type_view_1115
+ __ZZ25gl_corrupt_nand_size_testP6gl_ctxE21kalloc_type_view_1391
+ __ZZ25gl_corrupt_nand_size_testP6gl_ctxE21kalloc_type_view_1461
+ __ZZ30gl_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1132
+ __ZZ30gl_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1211
+ __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1231
+ __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1234
+ __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1369
+ __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1374
+ __ZZL17gl_fixup_rev_initP6gl_ctxE20kalloc_type_view_171
+ __ZZL17gl_fixup_rev_initP6gl_ctxE20kalloc_type_view_252
- __ZZ12gl_rec_writeP6gl_ctxPK9gl_rec_idPKhmE20kalloc_type_view_703
- __ZZ12gl_rec_writeP6gl_ctxPK9gl_rec_idPKhmE20kalloc_type_view_747
- __ZZ13gl_rec_deletePK6gl_ctxyE20kalloc_type_view_632
- __ZZ13gl_rec_deletePK6gl_ctxyE20kalloc_type_view_647
- __ZZ22gl_crash_recovery_testP6gl_ctxE20kalloc_type_view_981
- __ZZ22gl_crash_recovery_testP6gl_ctxE21kalloc_type_view_1061
- __ZZ25gl_corrupt_nand_size_testP6gl_ctxE21kalloc_type_view_1337
- __ZZ25gl_corrupt_nand_size_testP6gl_ctxE21kalloc_type_view_1407
- __ZZ30gl_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1078
- __ZZ30gl_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1157
- __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1177
- __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1180
- __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1315
- __ZZ41gl_many_types_many_duplicate_records_testP6gl_ctxE21kalloc_type_view_1320
- __ZZL17gl_fixup_rev_initP6gl_ctxE20kalloc_type_view_167
- __ZZL17gl_fixup_rev_initP6gl_ctxE20kalloc_type_view_248
CStrings:
+ "%s: SEP CoreAnalytics: Failed to send CA event %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AllocMPM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPBooter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPCommand.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPCommon.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPControl.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPDebug.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPDebugArgs.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPDevice.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPDiscovery.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPEndpoint.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPFirmware.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPLogger.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPManagerARM.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPPairing.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPSharedMemoryBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPTesting.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPTraceBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/AppleSEPUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/FIFO.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/SEPApNonce.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/SEPEpoch.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/SEPROMPanicBuffer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/xART/AppleSEPXART.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/xART/DisableLog.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.RAfTvd/Sources/AppleSEPManager/xART/gigalocker/gigalocker.cpp"
+ "AppleSEPCommon.h"
+ "KdbgScope::~KdbgScope()"
+ "analytics.version == 1"
+ "begin_code & TRACE_FUNCTION_BEGIN"
+ "code_begin & TRACE_FUNCTION_BEGIN"
+ "code_end & TRACE_FUNCTION_END"
+ "com.apple.applesepos.storage.stats"
+ "dictData[0]"
+ "dictKey[0]"
+ "eventName"
+ "eventPayload"
+ "in_msg_p->length == sizeof(xart_analytics_t)"
+ "pwn"
+ "top_ < kMaxDepth"
+ "top_ > 0"
+ "void AppleSEPManager::_report_sandcat_pwn(uint32_t)"
+ "void KdbgScope::pop(uint32_t)"
+ "void KdbgScope::push(uint32_t)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AllocMPM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPBooter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPCommand.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPControl.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPCoreBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDebug.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDebugArgs.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDevice.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPDiscovery.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPEndpoint.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPFirmware.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPLogger.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPManagerARM.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPPairing.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPSharedMemoryBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPTesting.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPTraceBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/AppleSEPUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/FIFO.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/SEPApNonce.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/SEPEpoch.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/SEPROMPanicBuffer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/AppleSEPXART.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/AppleSEPXART_embedded.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/DisableLog.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.heK1CU/Sources/AppleSEPManager/xART/gigalocker/gigalocker.cpp"
```
