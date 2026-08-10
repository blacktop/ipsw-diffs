## com.apple.driver.AppleCredentialManager

> `com.apple.driver.AppleCredentialManager`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

 864.160.4.0.0
-  __TEXT.__cstring: 0x19f95
+  __TEXT.__cstring: 0x1a470
   __TEXT.__const: 0x478
-  __TEXT_EXEC.__text: 0x73bf4
+  __TEXT_EXEC.__text: 0x747f0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x9ed9
   __DATA.__common: 0x1d0

   __DATA_CONST.__const: 0x2f60
   __DATA_CONST.__kalloc_type: 0x640
   __DATA_CONST.__kalloc_var: 0x14f0
-  Functions: 1274
-  Symbols:   1967
-  CStrings:  2747
+  Functions: 1275
+  Symbols:   1968
+  CStrings:  2776
 
Symbols:
+ _TRMMultiState_ReplaceInBuffer
Functions:
~ _Env_SetVariableWithParams : 2416 -> 2448
~ _TRMMultiState_ReadFromBuffer : 3844 -> 4268
~ _TRMMultiState_WriteToBuffer : 1484 -> 1720
+ _TRMMultiState_ReplaceInBuffer
~ __ZN28AppleCredentialManagerShared33_checkRequiredCommandEntitlementsEP13acm_command_tmNS_23CheckEntitlementsLambdaE : 1328 -> 1344
~ _DeserializeCredential : 1380 -> 1384
~ _LibSer_SEPControl_Deserialize : 352 -> 492
~ _LibSer_SEPControlResponse_Deserialize : 208 -> 288
~ _Storage_GetDataProperty : 2192 -> 2216
~ _setData : 1820 -> 1896
~ __ZN32AppleCredentialManagerUserClient17extPerformCommandEP22AppleCredentialManagerPvP25IOExternalMethodArguments : 1312 -> 1768
~ __ZN22AppleCredentialManager19performCommandGatedEP18IOMemoryDescriptorS1_PjPK26ACMPerformCommandContextV2 : 2640 -> 2544
CStrings:
+ "!memcmp(state->cache.header.tag, (uint8_t[3])ACM_TRM_COMPACT_CACHE_TAG, sizeof(state->cache.header.tag))"
+ "!memcmp(state->policy.header.tag, (uint8_t[3])ACM_TRM_COMPACT_POLICY_TAG, sizeof(state->policy.header.tag))"
+ "%s: %s: *%s* replaced (size=%u->%u).\n"
+ "%s: %s: *acc-cache* saved (records=%u skipped=%u).\n"
+ "%s: %s: *config* saved (ver=%u size=%u).\n"
+ "%s: %s: *policy* saved (ver=%u size=%u).\n"
+ "%s: %s: [loaded] inSize=%u -> policyRead=%s configRead=NO accCacheRead=%s.\n"
+ "%s: %s: [replaced] bufSize=%u policyReplaced=%s configReplaced=%s.\n"
+ "%s: %s: [saved] outSize=%u policySaved=%s configSaved=%s accCacheSaved=%s.\n"
+ "*bufInOutSize <= bufCapacity"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CommonCrypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreCmd.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreCred.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreCredSet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreDER.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreDeveloperMode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreEnv.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreExec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreOTI.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CorePrague.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreSEPControl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreStorage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreStorageProtection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreTimer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreUserIntent.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CoreUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/CredUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/Credentials.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.u4R9v2/Sources/AppleCredentialManager/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.v17JXQ/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.v17JXQ/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.v17JXQ/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "Jul 31 2026, 20:47:43"
+ "TRMMultiState_ReplaceInBuffer"
+ "buf"
+ "bufInOutSize"
+ "copied == srcLen"
+ "inData && inSize == sizeof(uid_t)"
+ "multiStateVersion || guardedStateVersion"
+ "newTotalSize <= bufCapacity"
+ "numRecords <= kACMTRMLegacyAccessoryCache_CacheSize"
+ "originalSize == sizeof(acm_command_t)"
+ "payloadOffset + oldPayloadSize <= curSize"
+ "payloadPos <= bufLen"
+ "pos + sizeof(ItemTag) <= curSize"
+ "pos == curSize"
+ "readPos + itemTag.payloadSize <= inBufferSize"
+ "remaining >= cmdSize"
+ "remaining >= respSize"
+ "remaining >= sizeof(uint32_t)"
+ "replaceInMultiStateBuffer"
+ "sizeof(accCacheRecordItem) + accCacheRecordItem.hashLen + accCacheRecordItem.dataLen + accCacheRecordItem.groupLen <= itemTag.payloadSize"
+ "srcLen > 0"
+ "srcRec->dataLen <= kACMTRMLegacyAccessoryCache_MaxDataSize"
+ "srcRec->hashLen <= kACMTRMLegacyAccessoryCache_MaxHashSize"
+ "total <= slot->maxDataSize"
- "%s: %s: [loaded] inSize=%u -> policyRead=%s configRead=%s accCacheRead=%s.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeUtil.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CommonCrypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreCmd.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreCred.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreCredSet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreDER.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreDeveloperMode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreEnv.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreExec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreOTI.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CorePrague.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreSEPControl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreStorage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreStorageProtection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreTimer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreUserIntent.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CoreUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/CredUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/Credentials.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.g8R1Qk/Sources/AppleCredentialManager/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oJkXM2/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oJkXM2/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oJkXM2/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "Jul 11 2026, 17:13:23"
- "inData && inSize >= sizeof(uid_t)"
- "size > originalSize"
- "state->cache.body.numRecords <= kACMTRMLegacyAccessoryCache_CacheSize"
```
