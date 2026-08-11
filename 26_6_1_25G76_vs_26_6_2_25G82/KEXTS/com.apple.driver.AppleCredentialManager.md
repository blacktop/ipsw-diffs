## com.apple.driver.AppleCredentialManager

> `com.apple.driver.AppleCredentialManager`

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
- "inData && inSize >= sizeof(uid_t)"
- "size > originalSize"
- "state->cache.body.numRecords <= kACMTRMLegacyAccessoryCache_CacheSize"
```
