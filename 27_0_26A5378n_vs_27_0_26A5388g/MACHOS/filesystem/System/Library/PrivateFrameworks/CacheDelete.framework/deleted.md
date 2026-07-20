## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-904.0.5.0.0
-  __TEXT.__text: 0x5c004
+904.0.7.0.0
+  __TEXT.__text: 0x5d194
   __TEXT.__auth_stubs: 0xe30
-  __TEXT.__objc_stubs: 0x66e0
-  __TEXT.__objc_methlist: 0x2f3c
+  __TEXT.__objc_stubs: 0x6780
+  __TEXT.__objc_methlist: 0x2f64
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x2738
-  __TEXT.__cstring: 0x45c5
-  __TEXT.__objc_methname: 0x7b9c
-  __TEXT.__oslogstring: 0xa040
+  __TEXT.__cstring: 0x45fe
+  __TEXT.__objc_methname: 0x7c33
+  __TEXT.__oslogstring: 0xa14d
   __TEXT.__objc_classname: 0x3fb
-  __TEXT.__objc_methtype: 0xe9a
-  __TEXT.__unwind_info: 0xdc0
-  __DATA_CONST.__const: 0x1eb8
-  __DATA_CONST.__cfstring: 0x4780
+  __TEXT.__objc_methtype: 0xeab
+  __TEXT.__unwind_info: 0xdd0
+  __DATA_CONST.__const: 0x1ed8
+  __DATA_CONST.__cfstring: 0x47c0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__auth_got: 0x728
-  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x4910
-  __DATA.__objc_selrefs: 0x1eb8
+  __DATA.__objc_selrefs: 0x1ee0
   __DATA.__objc_ivar: 0x38c
   __DATA.__objc_data: 0xb40
   __DATA.__data: 0x4e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1303
-  Symbols:   3047
-  CStrings:  3088
+  Functions: 1307
+  Symbols:   3057
+  CStrings:  3098
 
Symbols:
+ +[CacheDeleteAnalytics appStatsBatchForFairPurgeResult:purgeAttempt:]
+ +[CacheDeleteAnalytics individualAppStatsForAppInfo:phase:purgeAttempt:]
+ +[CacheDeleteAnalytics isThirdPartyAppInfo:]
+ GCC_except_table64
+ GCC_except_table70
+ ___69+[CacheDeleteAnalytics appStatsBatchForFairPurgeResult:purgeAttempt:]_block_invoke
+ _objc_msgSend$appTelemetryData
+ _objc_msgSend$developerType
+ _objc_msgSend$individualAppStatsForAppInfo:phase:purgeAttempt:
+ _objc_msgSend$isThirdPartyAppInfo:
+ _objc_msgSend$sortUsingComparator:
- GCC_except_table60
CStrings:
+ "@40@0:8@16Q24Q32"
+ "Fair Purge Analytics: classified %lu first-party, %lu third-party apps"
+ "Fair Purge Analytics: first-party app bundles=[%@] visible=%d weight=%f purgeable=%llu purged=%llu"
+ "Fair Purge Analytics: third-party app bundles=[%@] visible=%d weight=%f purgeable=%llu purged=%llu"
+ "appStatsBatchForFairPurgeResult:purgeAttempt:"
+ "com.apple.cache_delete.fair_purge.aggregated_third_party"
+ "developerType"
+ "individualAppStatsForAppInfo:phase:purgeAttempt:"
+ "isThirdPartyAppInfo:"
+ "sortUsingComparator:"
```
