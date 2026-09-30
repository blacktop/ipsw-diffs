## MFAAuthentication

> `/System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication`

```diff

-1139.80.2.0.0
-  __TEXT.__text: 0x3c6cc
-  __TEXT.__auth_stubs: 0xee0
+1139.80.3.0.0
+  __TEXT.__text: 0x3c6d0
+  __TEXT.__auth_stubs: 0xf10
   __TEXT.__objc_methlist: 0x444
   __TEXT.__const: 0x62b98
   __TEXT.__cstring: 0x193f
   __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__oslogstring: 0x4a9f
+  __TEXT.__oslogstring: 0x4a88
   __TEXT.__ustring: 0xa
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x788

   __TEXT.__objc_methtype: 0x3dc
   __TEXT.__objc_stubs: 0xfe0
   __DATA_CONST.__got: 0x210
-  __DATA_CONST.__const: 0x4f40
+  __DATA_CONST.__const: 0x4f20
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH_CONST.__const: 0x16b0
   __AUTH_CONST.__cfstring: 0x1aa0
   __AUTH_CONST.__objc_const: 0x608

   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x60
-  __DATA.__bss: 0xf8
+  __DATA.__data: 0xa0
+  __DATA.__bss: 0x110
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x1c0
+  __DATA_DIRTY.__bss: 0x1b0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A4A9CB25-D474-30C0-81D2-87DDEA7AF7FB
-  Functions: 788
-  Symbols:   3029
-  CStrings:  1096
+  UUID: B4D5C902-2D68-3CB0-A493-DA49E4F827AB
+  Functions: 793
+  Symbols:   3056
+  CStrings:  1098
 
Symbols:
+ _CFSetAddValue
+ _CFSetContainsValue
+ _CFSetCreateMutable
+ _CFSetRemoveValue
+ _CertCacheReferenceCountUpdate.cold.1
+ _CertCacheReferenceCountUpdate.cold.2
+ _CertCacheReferenceCountUpdate.cold.3
+ _CreateCacheEntryArray
+ _CreateCacheEntryArray.cold.1
+ _CreateCacheEntryArray.kAuthUsageInitialCount
+ _GetCertCacheDomainQueueAndInit.gCertCacheDomainQueue
+ _GetCertCacheDomainQueueAndInit.onceToken
+ _MFAAAddCertChainDataEntryToCacheForHash.cold.2
+ _MFAAAddCertDataEntryToCacheForSerialNumber.cold.2
+ _MFAACreateCertChainDataFromHash.cold.2
+ _MFAACreateCertDataFromSerialNumber.cold.2
+ _MFAACreateCertificateCache.cold.5
+ _MFAACreateMatchingHashForCertChainFromHashLSB.cold.2
+ _MFAADeallocCertificateCache.cold.3
+ _MFAARemoveCertChainDataEntryFromCache.cold.2
+ _MFAARemoveCertDataEntryFromCache.cold.2
+ _RemoveLeastUsedCacheEntry
+ _RemoveLeastUsedCacheEntry.cold.1
+ _SyncCertCacheContentsToPreferencesFile.certCachePrefsLock
+ _ValidateCacheStateCreated
+ _ValidateCacheStateCreated.cold.1
+ _ValidateCacheStateCreated.cold.2
+ ___GetCertCacheDomainQueueAndInit_block_invoke
+ ___GetCertCacheDomainQueueAndInit_block_invoke.cold.1
+ ___GetCertCacheDomainQueueAndInit_block_invoke_2
+ ___GetCertCacheDomainQueueAndInit_block_invoke_2.cold.1
+ ___GetCertCacheDomainQueueAndInit_block_invoke_2.cold.2
+ ___MFAACreateCertificateCache_block_invoke.cold.2
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.24
+ ___block_descriptor_tmp.25
+ ___block_descriptor_tmp.26
+ ___block_literal_global.35
+ _gCertCacheValidStructSet
- _MFAACreateCertificateCache.onceToken
- ___CertCacheReferenceCountUpdate_block_invoke
- ___CertCacheReferenceCountUpdate_block_invoke.cold.1
- ___CertCacheReferenceCountUpdate_block_invoke.cold.2
- ___CertCacheReferenceCountUpdate_block_invoke.cold.3
- ___MFAAAddCertChainDataEntryToCacheForHash_block_invoke.cold.1
- ___MFAAAddCertChainDataEntryToCacheForHash_block_invoke.cold.2
- ___MFAAAddCertDataEntryToCacheForSerialNumber_block_invoke.cold.1
- ___MFAAAddCertDataEntryToCacheForSerialNumber_block_invoke.cold.2
- ___MFAACreateCertificateCache_block_invoke.20
- ___MFAACreateCertificateCache_block_invoke.20.cold.1
- ___MFAACreateCertificateCache_block_invoke.20.cold.2
- ___MFAACreateCertificateCache_block_invoke_2
- ___MFAACreateCertificateCache_block_invoke_2.cold.1
- ___block_descriptor_tmp.1
- ___block_descriptor_tmp.31
- ___block_descriptor_tmp.36
- ___block_descriptor_tmp.37
- ___block_descriptor_tmp.40
- __block_invoke_2.kAuthUsageInitialCount
- __block_invoke_3.kAuthUsageInitialCount
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
