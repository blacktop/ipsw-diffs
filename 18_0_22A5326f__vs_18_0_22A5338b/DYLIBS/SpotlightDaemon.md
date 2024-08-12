## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2313.3.4.0.0
-  __TEXT.__text: 0x8c6a4
-  __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_methlist: 0x34ec
+2313.4.0.1.0
+  __TEXT.__text: 0x8ec4c
+  __TEXT.__auth_stubs: 0x1bc0
+  __TEXT.__objc_methlist: 0x35cc
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x6a72
+  __TEXT.__cstring: 0x6d9c
   __TEXT.__gcc_except_tab: 0x3b34
-  __TEXT.__oslogstring: 0x7ccd
-  __TEXT.__unwind_info: 0x1df0
-  __TEXT.__objc_classname: 0x435
-  __TEXT.__objc_methname: 0xc0fc
+  __TEXT.__oslogstring: 0x7f76
+  __TEXT.__unwind_info: 0x1e30
+  __TEXT.__objc_classname: 0x452
+  __TEXT.__objc_methname: 0xc2e4
   __TEXT.__objc_methtype: 0x1fe3
-  __TEXT.__objc_stubs: 0x9c00
-  __DATA_CONST.__got: 0x878
-  __DATA_CONST.__const: 0x3320
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__objc_stubs: 0x9e60
+  __DATA_CONST.__got: 0x8d0
+  __DATA_CONST.__const: 0x3340
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ca8
+  __DATA_CONST.__objc_selrefs: 0x2d40
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x3d8
-  __AUTH_CONST.__auth_got: 0xde8
+  __AUTH_CONST.__auth_got: 0xdf8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0xca8
-  __AUTH_CONST.__cfstring: 0x5580
-  __AUTH_CONST.__objc_const: 0x5938
+  __AUTH_CONST.__const: 0xce8
+  __AUTH_CONST.__cfstring: 0x5be0
+  __AUTH_CONST.__objc_const: 0x5a48
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x3cc
-  __DATA.__data: 0x798
-  __DATA.__bss: 0xd9
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x3d8
+  __DATA.__data: 0x7a0
+  __DATA.__bss: 0xe1
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__data: 0x220

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CSExattrCrypto.framework/CSExattrCrypto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2337
-  Symbols:   3203
-  CStrings:  4055
+  - /usr/lib/libutil.dylib
+  Functions: 2370
+  Symbols:   3251
+  CStrings:  4149
 
Symbols:
+ _NSFileReferenceCount
+ _NSFileSize
+ _NSFileSystemFileNumber
+ _NSFileSystemFreeSize
+ _NSFileSystemNumber
+ _NSFileSystemSize
+ _NSFileType
+ _NSFileTypeDirectory
+ _NSURLIsPurgeableKey
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_SPIndexStorageUsageCollector
+ _OBJC_METACLASS_$_SPIndexStorageUsageCollector
+ _humanize_number
+ _remove
CStrings:
+ "\n%!@(MISSING)"
+ "%!s(MISSING) all index files purgable under %!@(MISSING)"
+ "%!s(MISSING) index file purgable:%!s(MISSING) flags:0x%!l(MISSING)lx"
+ "*warn* Failed to get free index disk space for %!s(MISSING). err=%!d(MISSING)"
+ "*warn* Failed to get total index disk space for %!s(MISSING). err=%!d(MISSING)"
+ ".directoryStoreFile"
+ ".directoryStoreFile.shadow"
+ ".indexArrays"
+ ".indexBigDates"
+ ".indexCompactDirectory"
+ ".indexDirectory"
+ ".indexGroups"
+ ".indexIds"
+ ".indexPositionTable"
+ ".indexPositions"
+ ".indexPostings"
+ ".indexScores"
+ ".indexTermIds"
+ ".ivf-"
+ ".store.db"
+ "2313.4.0.1"
+ "Cleared"
+ "Clearing"
+ "Clearing CoreSpotlight index files purgeable under %!@(MISSING). freeDiskSpace %!l(MISSING)u, totalDiskSpace %!l(MISSING)u"
+ "Converting CoreSpotlight index to read-write"
+ "Failed to %!s(MISSING) index file purgable:%!s(MISSING) flags:0x%!l(MISSING)lx (%!s(MISSING))"
+ "Failed to create touch file %!@(MISSING). errno=%!d(MISSING)"
+ "Failed to open path:%!@(MISSING)"
+ "Failed to remove touch file %!@(MISSING). errno=%!d(MISSING)"
+ "Failed to retrieve file system attributes: %!@(MISSING)"
+ "Getting total size of all index files in %!@(MISSING)"
+ "Index type %!@(MISSING) size %!@(MISSING)"
+ "Marked"
+ "Marking"
+ "Marking CoreSpotlight index files purgeable under %!@(MISSING). freeDiskSpace %!l(MISSING)u, totalDiskSpace %!l(MISSING)u"
+ "Performing background task:%!@(MISSING)"
+ "SPIndexStorageUsageCollector"
+ "SpotlightKnowledge"
+ "Task %!@(MISSING) cancelled"
+ "_createPurgeableTouchFile"
+ "_hasPurgeableTouchFile"
+ "_removePurgeableTouchFile"
+ "_shouldPurge"
+ "_storageUsage"
+ "_visitedInodes"
+ "assetConfigDump"
+ "attributesOfItemAtPath:error:"
+ "bigDate"
+ "clear"
+ "collectAtPath:"
+ "com.apple.searchd.reportStorageUsage"
+ "com.apple.spotlight.index.StorageUsage"
+ "dataMap%!u(MISSING)"
+ "dbStr-"
+ "dbStr-%!u(MISSING).map."
+ "diskSpace"
+ "embedding"
+ "forwardDirStore"
+ "freeIndexDiskSpace"
+ "getIndexDirectorySize:"
+ "group"
+ "indexId"
+ "indexTermId"
+ "journal"
+ "journalAttr."
+ "knowledgeGraph"
+ "mark"
+ "markAllFilesPurgeable:purgeableOrNot:"
+ "markIndexPurgeable:"
+ "other"
+ "position"
+ "positionTable"
+ "posting"
+ "priority"
+ "protectionClassA"
+ "protectionClassB"
+ "protectionClassC"
+ "protectionClassCX"
+ "purgeable"
+ "purgeableIndexMarker"
+ "purgeableIndexTouchFilePath"
+ "recycleAndPurgeIndex"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "restoreIndexAndClearPurgeable"
+ "reverseDirStore"
+ "reverseDirectoryStore"
+ "reverseDirectoryStore.shadow"
+ "reverseStore.updates"
+ "score"
+ "setExpirationHandler:"
+ "setTaskCompleted"
+ "spaceLeft"
+ "termIndex"
+ "total"
+ "totalIndexDiskSpace"
+ "trialConfigDump"
+ "v16@?0@\"BGRepeatingSystemTask\"8"
- "2313.3.4"
- "Converting index to read-only"
- "Converting index to read-write"

```
