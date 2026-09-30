## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2326.1.0.11.0
-  __TEXT.__text: 0x93118
-  __TEXT.__auth_stubs: 0x1c30
-  __TEXT.__objc_methlist: 0x369c
-  __TEXT.__const: 0x328
-  __TEXT.__cstring: 0x71a0
-  __TEXT.__gcc_except_tab: 0x3d7c
-  __TEXT.__oslogstring: 0x83a8
-  __TEXT.__unwind_info: 0x1ed8
-  __TEXT.__objc_classname: 0x452
-  __TEXT.__objc_methname: 0xc729
-  __TEXT.__objc_methtype: 0x208b
-  __TEXT.__objc_stubs: 0xa1e0
-  __DATA_CONST.__got: 0x8c8
-  __DATA_CONST.__const: 0x3530
+2328.3.0.4.0
+  __TEXT.__text: 0x94c98
+  __TEXT.__auth_stubs: 0x1c70
+  __TEXT.__objc_methlist: 0x36f4
+  __TEXT.__const: 0x338
+  __TEXT.__cstring: 0x72b8
+  __TEXT.__gcc_except_tab: 0x3e5c
+  __TEXT.__oslogstring: 0x879a
+  __TEXT.__unwind_info: 0x1f60
+  __TEXT.__objc_classname: 0x461
+  __TEXT.__objc_methname: 0xc86e
+  __TEXT.__objc_methtype: 0x20ac
+  __TEXT.__objc_stubs: 0xa340
+  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__const: 0x35c8
   __DATA_CONST.__objc_classlist: 0x148
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e20
+  __DATA_CONST.__objc_selrefs: 0x2e88
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xe8
-  __DATA_CONST.__objc_arraydata: 0x410
-  __AUTH_CONST.__auth_got: 0xe30
+  __DATA_CONST.__objc_arraydata: 0x430
+  __AUTH_CONST.__auth_got: 0xe50
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0xd68
-  __AUTH_CONST.__cfstring: 0x6100
-  __AUTH_CONST.__objc_const: 0x5af8
+  __AUTH_CONST.__const: 0xde8
+  __AUTH_CONST.__cfstring: 0x6280
+  __AUTH_CONST.__objc_const: 0x5b38
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x3e0
   __DATA.__data: 0x7a0
-  __DATA.__bss: 0x129
+  __DATA.__bss: 0xd9
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x220
-  __DATA_DIRTY.__bss: 0x4c8
+  __DATA_DIRTY.__bss: 0x518
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto
+  - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 2429
-  Symbols:   3319
-  CStrings:  4270
+  Functions: 2450
+  Symbols:   3350
+  CStrings:  4310
 
Symbols:
+ _CacheDeleteRegisterInfoCallbacks
+ _CacheDeleteRegisterInfoCallbacksForProcess
+ _NSURLFileAllocatedSizeKey
+ _NSURLIsRegularFileKey
+ _NSURLTotalFileAllocatedSizeKey
+ _OBJC_CLASS_$_NSScanner
+ _SIPurgeVectorIndex
+ _SIVectorIndexStorageSize
+ _kSecEntitlementCSAllowMessagesContent
CStrings:
+ "%!s(MISSING) index directory %!@(MISSING) atomically purgable. flags=0x%!l(MISSING)lx"
+ "2328.3.0.4"
+ "CACHE_DELETE_AMOUNT"
+ "CACHE_DELETE_VOLUME"
+ "CacheDelete: asked for size on %!@(MISSING) for urgency: %!d(MISSING)"
+ "CacheDelete: asked to periodic clear %!d(MISSING) on %!@(MISSING) for urgency: %!d(MISSING)"
+ "CacheDelete: did purge %!l(MISSING)u on %!@(MISSING) for urgency: %!d(MISSING)"
+ "CacheDelete: failed to purge indexer %!s(MISSING) error: %!@(MISSING)."
+ "CacheDelete: failed to register Callbacks"
+ "CacheDelete: indexer: %!@(MISSING) size: %!z(MISSING)u."
+ "CacheDelete: purge %!s(MISSING) vectors size: %!z(MISSING)u."
+ "CacheDelete: purge indexer %!s(MISSING) size: %!z(MISSING)u."
+ "CacheDelete: purge purgeable vectors size: %!z(MISSING)u."
+ "CacheDelete: purgeable size on %!@(MISSING) for urgency: %!d(MISSING) is %!l(MISSING)u"
+ "CacheDelete: purged %!l(MISSING)u bytes for %!@(MISSING)"
+ "CacheDelete: register Callbacks for %!@(MISSING) on %!@(MISSING)"
+ "CacheDelete: will purge %!d(MISSING) on %!@(MISSING) for urgency: %!d(MISSING)"
+ "Failed to %!s(MISSING) index directory %!@(MISSING) atomically purgable. fd:%!d(MISSING) errno:%!d(MISSING)"
+ "Failed to get dir stats %!@(MISSING). fd:%!d(MISSING) errno:%!d(MISSING)"
+ "Getting dir stats version:%!d(MISSING) flags:0x%!l(MISSING)lx dir_stats_id:%!l(MISSING)lu gen_count:%!l(MISSING)lu descendants:%!l(MISSING)lu physical_size:%!l(MISSING)lu clone_size:%!l(MISSING)lu purgeable_size:%!l(MISSING)lu purgeable_urgency:%!d(MISSING).%!@(MISSING)"
+ "Notifications access allowed for %!@(MISSING)"
+ "Q20@0:8B16"
+ "Q24@0:8@16"
+ "Q24@0:8Q16"
+ "SplitWithLimit"
+ "Waiting for apfs to unlock"
+ "Waiting for apfs to unlock complete"
+ "^{__CFDictionary=}20@?0i8^{__CFDictionary=}12"
+ "all"
+ "cacheDeleteId"
+ "com.apple.CacheDelete"
+ "com.apple.internal.suiuntool.SystemExperienceAutomationAngel"
+ "com.apple.private.corespotlight.allowmessagescontent"
+ "com.apple.spotlightknowledged"
+ "com.apple.spotlightknowledged.importer"
+ "com.apple.spotlightknowledged.updater"
+ "componentsSeparatedByString:limit:"
+ "enable_notifications_access"
+ "failed to set dir stats %!s(MISSING) err %!d(MISSING)"
+ "indexFromBundle: client state mismatch ... expected:%!@(MISSING) stored:%!@(MISSING)"
+ "isAtEnd"
+ "job:"
+ "keysSortedByValueUsingComparator:"
+ "markDirectoryAtomicallyPurgeable:purgeableOrNot:"
+ "processorAttributesForRecord:bundleID:protectionClass:isUpdate:"
+ "purgeIndexForSize:"
+ "purgeVectorIndex:"
+ "purgeableIndexSize:"
+ "purgeableVectorIndexSize:"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "registerCacheDeleteCallbackForVolumePath:"
+ "reindexJob:"
+ "scanLocation"
+ "scanString:intoString:"
+ "scanUpToString:intoString:"
+ "scannerWithString:"
+ "storageSizeForFolder:"
+ "successfully set dir stats %!s(MISSING)"
+ "usernoted"
- "%!s(MISSING) all index files purgable under %!@(MISSING)"
- "%!s(MISSING) index file purgable:%!s(MISSING) flags:0x%!l(MISSING)lx"
- ".created"
- ".ivf-vector-indexes"
- ".modified"
- ".quantizer"
- "2326.1.0.11"
- "Clearing"
- "Failed to %!s(MISSING) index file purgable:%!s(MISSING) flags:0x%!l(MISSING)lx (%!s(MISSING))"
- "Failed to open index file:%!s(MISSING) (%!s(MISSING))"
- "Marking"
- "clientstatesmetafile"
- "dbStr"
- "indexState"
- "markAllFilesPurgeable:purgeableOrNot:"
- "processorAttributesForRecord:bundleID:protectionClass:"
- "purgeableFixup"
- "store.updates"
- "tmp.spotlight.state"

```
