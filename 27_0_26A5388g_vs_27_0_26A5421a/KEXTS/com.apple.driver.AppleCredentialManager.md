## com.apple.driver.AppleCredentialManager

> `com.apple.driver.AppleCredentialManager`

```diff

-949.0.13.0.0
-  __TEXT.__cstring: 0x1c7bc
+949.0.17.0.0
+  __TEXT.__cstring: 0x1cc97
   __TEXT.__const: 0x4a0
-  __TEXT_EXEC.__text: 0x7cdd8
+  __TEXT_EXEC.__text: 0x7dae8
   __TEXT_EXEC.__auth_stubs: 0x750
   __DATA.__data: 0xa501
   __DATA.__common: 0x9c8

   __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x30
-  Functions: 1368
-  Symbols:   2070
-  CStrings:  2936
+  Functions: 1370
+  Symbols:   2072
+  CStrings:  2965
 
Symbols:
+ _TRMMultiState_ReplaceInBuffer
+ _Util_ThumbAndPayDefaut
+ copyCredentials.kalloc_type_view_9360
- copyCredentials.kalloc_type_view_9320
Functions:
~ __findValidCredential : 3816 -> 3832
+ _Util_ThumbAndPayDefaut
~ __ZN30ACMRestrictedModeKernelService12_startPolicyEbhhhh : 4412 -> 4504
~ _Env_SetVariableWithParams : 2528 -> 2572
~ _DefaultValueProvider_ThumbAndPayEnabled : 444 -> 448
~ _TRMMultiState_ReadFromBuffer : 3936 -> 4392
~ _TRMMultiState_WriteToBuffer : 1480 -> 1700
+ _TRMMultiState_ReplaceInBuffer
~ __ZN28AppleCredentialManagerShared33_checkRequiredCommandEntitlementsEP13acm_command_tmNS_23CheckEntitlementsLambdaE : 1340 -> 1356
~ _DeserializeCredential : 1520 -> 1524
~ _LibSer_SEPControl_Deserialize : 384 -> 528
~ _LibSer_SEPControlResponse_Deserialize : 216 -> 296
~ _Storage_GetDataProperty : 2392 -> 2416
~ _setData : 1860 -> 1936
~ __ZN32AppleCredentialManagerUserClient17extPerformCommandEP22AppleCredentialManagerPvP25IOExternalMethodArguments : 1308 -> 1768
~ __ZN22AppleCredentialManager19performCommandGatedEP18IOMemoryDescriptorS1_PjPK26ACMPerformCommandContextV3 : 2888 -> 2784
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
+ "21:49:50"
+ "Aug 11 2026"
+ "Aug 11 2026, 21:50:02"
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
- "21:29:10"
- "Jul 14 2026"
- "Jul 14 2026, 21:29:22"
- "inData && inSize >= sizeof(uid_t)"
- "size > originalSize"
- "state->cache.body.numRecords <= kACMTRMLegacyAccessoryCache_CacheSize"
```
