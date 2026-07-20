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
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-904.0.5.0.0
-  __TEXT.__text: 0x5a8a4
+904.0.7.0.0
+  __TEXT.__text: 0x5b558
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_stubs: 0x6880
-  __TEXT.__objc_methlist: 0x2fcc
+  __TEXT.__objc_stubs: 0x6920
+  __TEXT.__objc_methlist: 0x2ff4
   __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x2910
-  __TEXT.__cstring: 0x493b
-  __TEXT.__objc_methname: 0x7d7f
-  __TEXT.__oslogstring: 0xabe3
+  __TEXT.__cstring: 0x4977
+  __TEXT.__objc_methname: 0x7e16
+  __TEXT.__oslogstring: 0xacf0
   __TEXT.__objc_classname: 0x407
-  __TEXT.__objc_methtype: 0xe7b
-  __TEXT.__unwind_info: 0xe00
-  __DATA_CONST.__const: 0x1d08
-  __DATA_CONST.__cfstring: 0x4b40
+  __TEXT.__objc_methtype: 0xe8c
+  __TEXT.__unwind_info: 0xe08
+  __DATA_CONST.__const: 0x1d28
+  __DATA_CONST.__cfstring: 0x4b80
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x4a68
-  __DATA.__objc_selrefs: 0x1ee0
+  __DATA.__objc_selrefs: 0x1f08
   __DATA.__objc_ivar: 0x39c
   __DATA.__objc_data: 0xb90
   __DATA.__data: 0x4f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1236
-  Symbols:   3030
-  CStrings:  3154
+  Functions: 1240
+  Symbols:   3039
+  CStrings:  3165
 
Symbols:
+ +[CacheDeleteAnalytics appStatsBatchForFairPurgeResult:purgeAttempt:]
+ +[CacheDeleteAnalytics individualAppStatsForAppInfo:phase:purgeAttempt:]
+ +[CacheDeleteAnalytics isThirdPartyAppInfo:]
+ GCC_except_table64
+ GCC_except_table67
+ ___69+[CacheDeleteAnalytics appStatsBatchForFairPurgeResult:purgeAttempt:]_block_invoke
+ _objc_msgSend$appStatsBatchForFairPurgeResult:purgeAttempt:
+ _objc_msgSend$developerType
+ _objc_msgSend$individualAppStatsForAppInfo:phase:purgeAttempt:
+ _objc_msgSend$isThirdPartyAppInfo:
+ _objc_msgSend$sortUsingComparator:
- GCC_except_table56
- GCC_except_table63
CStrings:
+ ", "
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
