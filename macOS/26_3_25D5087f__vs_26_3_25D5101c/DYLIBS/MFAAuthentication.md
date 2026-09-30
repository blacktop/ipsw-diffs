## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/Versions/A/MFAAuthentication`

```diff

-1139.80.2.0.0
-  __TEXT.__text: 0x28df4
-  __TEXT.__auth_stubs: 0xbf0
+1139.80.3.0.0
+  __TEXT.__text: 0x28dc0
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x5e428
   __TEXT.__cstring: 0x142c
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__oslogstring: 0x45b1
+  __TEXT.__oslogstring: 0x459a
   __TEXT.__ustring: 0xa
   __TEXT.__unwind_info: 0x620
   __TEXT.__objc_classname: 0x6e

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x608
-  __AUTH_CONST.__const: 0x6a0
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__const: 0x670
   __AUTH_CONST.__cfstring: 0x16e0
   __AUTH_CONST.__objc_const: 0x608
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x60
-  __DATA.__bss: 0xb0
+  __DATA.__data: 0xa0
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__bss: 0x100
   __DATA_DIRTY.__common: 0x1c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 705A38BB-3AFB-3A0A-9EC6-104E9BA99B28
-  Functions: 671
-  Symbols:   2179
-  CStrings:  971
+  UUID: 3EC55CDB-45F4-31E2-BC97-F6B37C51244F
+  Functions: 674
+  Symbols:   2193
+  CStrings:  973
 
Symbols:
+ CertCacheReferenceCountUpdate.cold.1
+ CertCacheReferenceCountUpdate.cold.2
+ CertCacheReferenceCountUpdate.cold.3
+ CreateCacheEntryArray.cold.1
+ CreateCacheEntryArray.kAuthUsageInitialCount
+ GetCertCacheDomainQueueAndInit.gCertCacheDomainQueue
+ GetCertCacheDomainQueueAndInit.onceToken
+ MFAAAddCertChainDataEntryToCacheForHash.cold.2
+ MFAAAddCertDataEntryToCacheForSerialNumber.cold.2
+ MFAACreateCertChainDataFromHash.cold.2
+ MFAACreateCertDataFromSerialNumber.cold.2
+ MFAACreateCertificateCache.cold.5
+ MFAACreateMatchingHashForCertChainFromHashLSB.cold.2
+ MFAADeallocCertificateCache.cold.3
+ MFAARemoveCertChainDataEntryFromCache.cold.2
+ MFAARemoveCertDataEntryFromCache.cold.2
+ RemoveLeastUsedCacheEntry.cold.1
+ SyncCertCacheContentsToPreferencesFile.certCachePrefsLock
+ ValidateCacheStateCreated.cold.1
+ ValidateCacheStateCreated.cold.2
+ _CFSetAddValue
+ _CFSetContainsValue
+ _CFSetCreateMutable
+ _CFSetRemoveValue
+ _CreateCacheEntryArray
+ _RemoveLeastUsedCacheEntry
+ _ValidateCacheStateCreated
+ __GetCertCacheDomainQueueAndInit_block_invoke.cold.1
+ __GetCertCacheDomainQueueAndInit_block_invoke_2.cold.1
+ __GetCertCacheDomainQueueAndInit_block_invoke_2.cold.2
+ __MFAACreateCertificateCache_block_invoke.cold.2
+ ___GetCertCacheDomainQueueAndInit_block_invoke
+ ___GetCertCacheDomainQueueAndInit_block_invoke_2
+ ___copy_helper_block_8_32r40r48r56r
+ ___destroy_helper_block_8_32r40r48r56r
+ __block_descriptor_tmp.23
+ __block_descriptor_tmp.24
+ __block_descriptor_tmp.30
+ __block_descriptor_tmp.33
+ __block_descriptor_tmp.36
+ __block_descriptor_tmp.39
+ __block_descriptor_tmp.42
+ __block_descriptor_tmp.44
+ __block_descriptor_tmp.45
+ __block_literal_global.47
+ _gCertCacheValidStructSet
- MFAACreateCertificateCache.onceToken
- __CertCacheReferenceCountUpdate_block_invoke.cold.1
- __CertCacheReferenceCountUpdate_block_invoke.cold.2
- __CertCacheReferenceCountUpdate_block_invoke.cold.3
- __MFAAAddCertChainDataEntryToCacheForHash_block_invoke.cold.1
- __MFAAAddCertChainDataEntryToCacheForHash_block_invoke.cold.2
- __MFAAAddCertDataEntryToCacheForSerialNumber_block_invoke.cold.1
- __MFAAAddCertDataEntryToCacheForSerialNumber_block_invoke.cold.2
- __MFAACreateCertificateCache_block_invoke.20
- __MFAACreateCertificateCache_block_invoke.20.cold.1
- __MFAACreateCertificateCache_block_invoke.20.cold.2
- __MFAACreateCertificateCache_block_invoke_2.cold.1
- ___CertCacheReferenceCountUpdate_block_invoke
- ___MFAACreateCertificateCache_block_invoke_2
- ___copy_helper_block_8_32r
- ___copy_helper_block_8_32r40r48r56r64r
- ___destroy_helper_block_8_32r
- ___destroy_helper_block_8_32r40r48r56r64r
- __block_descriptor_tmp.1
- __block_descriptor_tmp.28
- __block_descriptor_tmp.29
- __block_descriptor_tmp.32
- __block_descriptor_tmp.35
- __block_descriptor_tmp.38
- __block_descriptor_tmp.41
- __block_descriptor_tmp.46
- __block_descriptor_tmp.49
- __block_descriptor_tmp.52
- __block_literal_global.3
- _block_invoke_2.kAuthUsageInitialCount
- _block_invoke_3.kAuthUsageInitialCount
- _dispatch_release
- _gCertCacheDomainQueue
CStrings:
+ "Bypass due to pkCacheState:%04X, pkCertChain:%04X, pkCertHashStr:%04X\n"
+ "Bypass due to pkCacheState:%04X, pkCertData:%04X, pCFStrSerNum:%04X\n"
+ "Bypass due to pkCacheState:%04X, pkCertHashLSBStr:%04X (%@)\n"
+ "Bypass due to pkCacheState:%04X, pkCertHashStr:%04X\n"
+ "Bypass due to pkCacheState:%04X, pkStrSerNum:%04X\n"
+ "CFDictionaryCreateMutable valid struct set NULL !\n"
+ "Cache validation failed - cache may have been deallocated\n"
+ "Parameter failed pkCacheState:%04X, pkCertHashStr:%04X\n"
+ "Parameter failed pkCacheState:%04X, pkStrSerNum:%04X\n"
- "Bypass due to pkCacheState:%04X, pkCertChain:%04X, pkCertHashStr:%04X, bCertNotCached:%d\n"
- "Bypass due to pkCacheState:%04X, pkCertData:%04X, pCFStrSerNum:%04X, bCertNotCached:%d\n"
- "Bypass due to pkCacheState:%04X, pkCertHashLSBStr:%04X (%@), bCertNotCached:%d\n"
- "Bypass due to pkCacheState:%04X, pkCertHashStr:%04X, bCertNotCached:%d\n"
- "Bypass due to pkCacheState:%04X, pkStrSerNum:%04X, bCertNotCached:%d\n"
- "Parameter failed pkCacheState:%04X, pkCertHashStr:%04X, bCertNotCached:%d\n"
- "Parameter failed pkCacheState:%04X, pkStrSerNum:%04X, bCertNotCached:%d\n"

```
