## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2899.80.3.0.0
-  __TEXT.__text: 0x9f528
-  __TEXT.__auth_stubs: 0x1a40
-  __TEXT.__objc_stubs: 0xd9a0
-  __TEXT.__objc_methlist: 0x6be0
-  __TEXT.__const: 0x4d0
-  __TEXT.__cstring: 0x1bb72
-  __TEXT.__oslogstring: 0xe828
-  __TEXT.__objc_methname: 0xfd72
-  __TEXT.__objc_classname: 0xaeb
-  __TEXT.__objc_methtype: 0x2176
-  __TEXT.__gcc_except_tab: 0x2730
-  __TEXT.__unwind_info: 0x1bc8
-  __DATA_CONST.__auth_got: 0xd30
-  __DATA_CONST.__got: 0x540
+2969.100.18.0.0
+  __TEXT.__text: 0x9dc8c
+  __TEXT.__auth_stubs: 0x18a0
+  __TEXT.__objc_stubs: 0xd060
+  __TEXT.__objc_methlist: 0x6730
+  __TEXT.__const: 0x4c8
+  __TEXT.__cstring: 0x18f46
+  __TEXT.__oslogstring: 0xe000
+  __TEXT.__objc_methname: 0xf4e5
+  __TEXT.__objc_classname: 0xa9f
+  __TEXT.__objc_methtype: 0x1f94
+  __TEXT.__gcc_except_tab: 0x25c8
+  __TEXT.__unwind_info: 0x1bf0
+  __DATA_CONST.__auth_got: 0xc60
+  __DATA_CONST.__got: 0x528
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1640
-  __DATA_CONST.__cfstring: 0xa3a0
-  __DATA_CONST.__objc_classlist: 0x3c0
+  __DATA_CONST.__const: 0x1550
+  __DATA_CONST.__cfstring: 0x9940
+  __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x270
+  __DATA_CONST.__objc_superrefs: 0x248
   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x100
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0xaad0
-  __DATA.__objc_selrefs: 0x4378
-  __DATA.__objc_ivar: 0x638
-  __DATA.__objc_data: 0x2580
-  __DATA.__data: 0x8d8
-  __DATA.__bss: 0x250
+  __DATA.__objc_const: 0xa430
+  __DATA.__objc_selrefs: 0x4080
+  __DATA.__objc_ivar: 0x5e0
+  __DATA.__objc_data: 0x2440
+  __DATA.__data: 0x878
+  __DATA.__bss: 0x220
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F8D1DCD4-CAEB-3446-892E-89FD54055BEF
-  Functions: 2713
-  Symbols:   603
-  CStrings:  8940
+  UUID: B0D80C45-CD32-34A2-9A25-E1A27CEA4DA0
+  Functions: 2595
+  Symbols:   574
+  CStrings:  8526
 
Symbols:
- _MBDataWithString
- _MBGetSQLLog
- _NSGenericException
- _OBJC_CLASS_$_MBRestoreFailure
- _OBJC_CLASS_$_NSKeyedArchiver
- _dispatch_after
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
- _sqlite3_bind_blob
- _sqlite3_bind_int
- _sqlite3_bind_int64
- _sqlite3_bind_text
- _sqlite3_busy_timeout
- _sqlite3_clear_bindings
- _sqlite3_column_blob
- _sqlite3_column_bytes
- _sqlite3_column_count
- _sqlite3_column_double
- _sqlite3_column_int64
- _sqlite3_column_name
- _sqlite3_column_type
- _sqlite3_errcode
- _sqlite3_open
- _sqlite3_reset
- _sqlite3_trace_v2
CStrings:
+ "%@-%d"
+ "=scanning= Scanning domain %{public}@ at %@ with mtpt %@ from snapshot %@ policy:0x%lx"
+ "@\"MBSuspendingClock\""
+ "@40@0:8@16Q24@32"
+ "B40@0:8@16^d24^@32"
+ "Containers"
+ "Error opening SQLite file to calculate freelist ratio: %s (%d)"
+ "Failed finalize statement: %s"
+ "Failed to close db when calculating free list ratio: %s"
+ "Failed to prepare statement: %s (%d)"
+ "MBSuspendingClock"
+ "PRAGMA freelist_count"
+ "PRAGMA page_count"
+ "T@\"MBSuspendingClock\",&,N,V_start"
+ "T@\"MBSuspendingClock\",&,N,V_uploadStart"
+ "Td,N,V_postUploadDuration"
+ "Td,N,V_preUploadDuration"
+ "_containersByContainerIDAndType"
+ "_containersByContainerIDAndType value not an NSDictionary"
+ "_legacy_containersByContainerID"
+ "_legacy_containersByContainerID value not an NSDictionary"
+ "_start"
+ "_startNanoseconds"
+ "_uploadStart"
+ "calculateFreeListRatioForDatabase:outRatio:error:"
+ "elapsedDuration"
+ "initWithDelegate:enginePolicy:debugContext:"
+ "setStart:"
+ "setUploadStart:"
+ "sqlite_step did not return a row: %s (%d)"
+ "uploadStart"
+ "\xf0!"
- " (%d(%d)/%s)"
- "%f"
- "-[MBFileScanner initWithDelegate:mode:enginePolicy:debugContext:]"
- "-[MBSCachePool _openCache]_block_invoke"
- "-[MBServiceCache initWithPath:domainManager:]"
- "..."
- "26"
- "=scanning= =scanning= Unexpected file name"
- "=scanning= Deleted/modified while scanning: %@"
- "=scanning= Finished scanning the live path at %@"
- "=scanning= Found %u items under %{public}s (%{public}@)"
- "=scanning= Found a total of %u items under %{public}s (%{public}@)"
- "=scanning= MBNodeForRelativePathAt() failed at %@ (%@): %{errno}d"
- "=scanning= Modification error when opening directory \"%@\" while scanning"
- "=scanning= Modification error when stating directory \"%@\" while scanning"
- "=scanning= No directory found at live path %@"
- "=scanning= Reached max directory depth (%d) under %{public}@"
- "=scanning= Scanning domain %{public}@ at %@ with mtpt %@ from snapshot %@ mode:0x%lx policy:0x%lx"
- "=scanning= Scanning the live path at %@"
- "=scanning= Skipping file with MBNodeForRelativePathAt() failure %@ (%@): %{errno}d"
- "=scanning= Skipping file with fstat failure %@ (%s): %{errno}d"
- "=scanning= Skipping file with openat failure %@ (%s): %{errno}d"
- "=scanning= Skipping unsupported mbNode type: %@ %@"
- "=scanning= Unable to open domain directory at %@:%@: %@"
- "=scanning= Unexpected file name: %@"
- "=scanning= fdopendir failed at %@ (%s): %{errno}d"
- "=scanning= fstat failed at %@ (%s): %{errno}d"
- "=scanning= fstatat failed at %@ (%s): %{errno}d"
- "=scanning= openat failed at %@ (%s): %{errno}d"
- "=scanning= readdir_r failed at %@: %d"
- "@\"<MBSCacheLikeObject>\""
- "@\"MBServiceConfiguration\""
- "@28@0:8I16r*20"
- "@32@0:8@16^q24"
- "@32@0:8Q16Q24"
- "@40@0:8@16@24^{sqlite3_stmt=}32"
- "@48@0:8@16@24{_NSRange=QQ}32"
- "@48@0:8@16Q24Q32@40"
- "@60@0:8@16@24@32@40i48^{_MBFileScannerDomainStats=qqqQQQQQQ}52"
- "@72@0:8@16@24@32i40@44@52i60^{_MBFileScannerDomainStats=qqqQQQQQQ}64"
- "Adding cache to pool: %p"
- "App uninstalled for protection class to restore: %@:%@"
- "B40@0:8@16d24@32"
- "Cache pool is empty"
- "Can't drain because cache pool is empty"
- "Closing cache db"
- "Closing cache: %p"
- "Column %d values don't match (%@ != %@)"
- "Column %s values don't match (%@ != %@)"
- "Column count doesn't match (%d != %d)"
- "Configuration"
- "Containers value not an NSDictionary"
- "Created"
- "Database is closed"
- "Discarding deleted files from snapshot %lu"
- "Domain not found for protection class to restore: %@:%@"
- "Draining cache pool"
- "Duplicate container ID detected: %@"
- "Error binding blob at %d: \"%@\""
- "Error binding int at %d: \"%@\""
- "Error binding int64 at %d: \"%@\""
- "Error binding integer at %d: \"%@\""
- "Error binding text at %d: \"%@\""
- "Error clearing prepared statement bindings: \"%@\""
- "Error closing corrupt db: %@"
- "Error closing database"
- "Error creating cache dir at %@: %@"
- "Error deserializing configuration"
- "Error deserializing configuration from cache: %@"
- "Error executing SQL: \"%@\""
- "Error finalizing prepared statement: \"%@\""
- "Error getting configuration"
- "Error loading apps: %@"
- "Error opening cache db at %@"
- "Error preparing statement: %@"
- "Error resetting prepared statement: \"%@\""
- "Error setting cache db busy timeout"
- "Failed to convert backup UDID: \"%@\""
- "Failed to step (%d): \"%@\""
- "Fewer results on left-hand side"
- "Fewer results on right-hand side"
- "Library/Application Support/CloudDocs"
- "Library/Application Support/CloudDocs/backup"
- "Library/Application Support/CloudDocs/backup/"
- "Library/Application Support/FileProvider"
- "Library/Application Support/FileProvider/backup"
- "Library/Application Support/FileProvider/backup/"
- "MBKeyBagInfo"
- "MBNodeForRelativePathAt() error"
- "MBSCacheLikeObject"
- "MBSCachePool"
- "MBSCachePool.m"
- "MBSCacheStmt"
- "MBSCacheStmt.m"
- "MBServiceCache"
- "MBServiceCache.m"
- "MBServiceConfiguration"
- "Merging snapshot %lu into snapshot %lu"
- "Missing handle for open cache db"
- "Not adding to cache because pool is full: %p"
- "Not scheduling cache pool drain because it's empty"
- "Not scheduling duplicate drain"
- "Null backup UDID"
- "Null key"
- "Opened cache: %p"
- "Opening cache db"
- "Q32@0:8@16Q24"
- "Re-creating cache db because schema version changed (%@ != %@)"
- "Re-using cache from pool: %p"
- "Removing cache db"
- "Removing cache from pool"
- "Removing corrupt backup cache db (%d/%s)"
- "Removing last snapshot"
- "Removing uncommitted snapshot"
- "SQL: %6ld  %6.3f s  %@"
- "SQL: %@"
- "SQL: Profile"
- "Scheduling drain of cache pool in %d s"
- "SchemaVersion"
- "Statement is not reset: \"%@\""
- "Statement is reset: \"%@\""
- "Statement not reset after last use: \"%@\""
- "T@\"MBDomainManager\",&,N,V_domainManager"
- "TB,N,GisReset,V_reset"
- "TI,V_bagID"
- "TQ,N,V_postUploadDuration"
- "TQ,N,V_preUploadDuration"
- "TQ,N,V_uploadStartTime"
- "Td,N,V_startTime"
- "Unexpected column type: %d"
- "[16C]"
- "^{sqlite3=}"
- "^{sqlite3_stmt=}"
- "_SQL"
- "_bagID"
- "_cache"
- "_caches"
- "_closeCache:"
- "_configuration"
- "_configurationUpToDate"
- "_containers"
- "_corrupt"
- "_countAndTimeBySQL"
- "_db"
- "_disabledDomainNames"
- "_drain"
- "_drainScheduled"
- "_exec:"
- "_finalizeAll"
- "_logProfile"
- "_mode"
- "_openCache"
- "_openCount"
- "_positiveIntegerForKey:defaultValue:"
- "_prepare:"
- "_profile:time:"
- "_raise:"
- "_remove"
- "_removeSnapshotForID:backupUDID:"
- "_reset"
- "_scanDirectory:domain:fds:domainDirFd:snapshotPath:relativePath:depth:stats:"
- "_scanFilesUsingReaddirForDomain:fds:snapshotPath:relativePath:depth:stats:"
- "_scheduleDrain"
- "_snapshotWithStmt:"
- "_stmt"
- "_stmtsBySQL"
- "_upToDateBackupUDIDs"
- "_uploadStartTime"
- "acquireCache"
- "addDisabledDomainNames:restricted:"
- "addFilesCount"
- "addFilesSize"
- "addRestoreFailure:"
- "and assetType = ?"
- "and dataclass = ?"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "assetType"
- "backupForUDID:lastModified:"
- "bagID"
- "begin"
- "begin exclusive"
- "bindBlob:atIndex:"
- "bindInt64:atIndex:"
- "bindInt:atIndex:"
- "bindInteger:atIndex:"
- "bindText:atIndex:"
- "blobColumn:"
- "bundleIDsNotToBackUp"
- "cache.db"
- "columnCount"
- "com.apple.backupd.MBSCachePool"
- "configuration"
- "configurationWithPropertyList:"
- "configurationWithURL:error:"
- "containerWithIdentifier:"
- "countOfRestoreFailuresForDataclass:assetType:"
- "create table if not exists Backups (\n    backupUDID             text primary key,\n    lastModified           integer,\n    attributes             blob\n);\n\ncreate trigger if not exists DeleteBackupSnapshots\nbefore delete on Backups\nfor each row begin\n    delete from Snapshots where backupUDID = OLD.backupUDID;\nend;\n\ncreate table if not exists Snapshots (\n    backupUDID             text,\n    snapshotID             integer,\n    lastModified           integer,\n    committed              integer,\n    localCommitted         integer,\n    stale                  integer,\n    attributes             blob,\n    primary key (backupUDID, snapshotID)\n);\n\ncreate index if not exists SnapshotBackupUDID on Snapshots (backupUDID);\n\ncreate trigger if not exists DeleteSnapshotFiles\nbefore delete on Snapshots\nfor each row begin\n    delete from Files where backupUDID = OLD.backupUDID and snapshotID = OLD.snapshotID;\nend;\n\ncreate table if not exists Files (\n    rowID                  integer primary key,\n    backupUDID             text,\n    snapshotID             integer,\n    fileID                 text,\n    domainName             text,\n    relativePath           text,\n    signature              blob,\n    size                   integer,\n    added                  integer,\n    committed              integer,\n    deleted                integer,\n    duplicateFileID        text,\n    duplicateSnapshotID    integer,\n    target                 text,\n    keybagID               integer,\n    encryptionKey          blob,\n    encryptionKeyVersion   integer,\n    decryptedSize          integer,\n    mode                   integer,\n    inodeNumber            integer,\n    userID                 integer,\n    groupID                integer,\n    lastModified           integer,\n    lastStatusChange       integer,\n    birth                  integer,\n    protectionClass        integer,\n    extendedAttributesCount integer,\n    unique (backupUDID, snapshotID, fileID)\n);\n\ncreate index if not exists FileBackupUDIDFileIDAndSnapshotID on Files (backupUDID, fileID, snapshotID);\ncreate index if not exists FileBackupUDIDDomainNameAndRelativePath on Files (backupUDID, domainName, relativePath);\ncreate index if not exists FileBackupUDIDDomainNameRelativePathFileID on Files (backupUDID, domainName ASC, relativePath ASC, fileID);\n\ncreate trigger if not exists DeleteFileExtendedAttributes\nbefore delete on Files\nfor each row begin\n    delete from FileExtendedAttributes where fileRowID = OLD.rowID;\nend;\n\ncreate table if not exists FileExtendedAttributes (\n    fileRowID              integer,\n    name                   text,\n    value                  blob,\n    primary key (fileRowID, name)\n);\n\ncreate table if not exists DisabledDomains (\n    domainName              text primary key,\n    restricted              integer\n);\n\ncreate table if not exists FileChanges (\n    fileID                 text primary key,\n    type                   integer,\n    domainName             text,\n    relativePath           text,\n    duplicateFileID        text,\n    duplicateSnapshotID    integer,\n    size                   integer,\n    result                 integer\n);\n\ncreate index if not exists FileChangeType on FileChanges (type);\ncreate index if not exists FileChangeDomainName on FileChanges (domainName);\n\ncreate table if not exists FilesMissingEncryptionKey (\n   path                    text primary key\n);\n\ncreate table if not exists FileEncryptionKeys (\n   inodeNumber             integer primary key,\n   encryptionKey           blob\n);\n\ncreate table if not exists Restores (\n    restoreID              integer,\n    type                   integer,\n    value                  text,\n    primary key            (type, value)\n);\ncreate index if not exists RestoreTypeAndValue on Restores (type, value);\n\ncreate trigger if not exists DeleteRestoreFiles\nbefore delete on Restores\nfor each row begin\n    delete from RestoreFiles where restoreID = OLD.restoreID;\nend;\n\ncreate table if not exists RestoreFiles (\n    restoreID              integer,\n    fileID                 text primary key,\n    snapshotID             integer,\n    itemID                 integer,\n    state                  integer,\n    priority               integer\n);\ncreate index if not exists RestoreFileRestoreIDAndSnapshotIDs on RestoreFiles (restoreID, snapshotID);\ncreate index if not exists RestoreFileFileID on RestoreFiles (fileID);\ncreate index if not exists RestoreFileItemID on RestoreFiles (itemID);\ncreate index if not exists RestoreFilePriority on RestoreFiles (priority);\n\ncreate table if not exists FileProtectionClassesToRestore (\n    domainName             text,\n    relativePath           text,\n    protectionClass        integer,\n    primary key (domainName, relativePath)\n);\n\ncreate table if not exists RestoreFailures (\n    identifier             text,\n    dataclass              text,\n    assetType              text,\n    displayName            text,\n    icon                   blob,\n    error                  blob,\n    primary key (dataclass, identifier)\n);\ncreate table if not exists PlaceholderResources (\n    bundleID               text,\n    relativePath           text,\n    lastModified           integer,\n    primary key (bundleID, relativePath)\n);\ncreate table if not exists KeyBagInfo (\n    backupUDID             text,\n    keybagID               integer,\n    keybagUUID             blob,\n    primary key (backupUDID, keybagID, keybagUUID)\n);\n"
- "create table if not exists Properties (\n    key                    text primary key,\n    value                  text\n);\n"
- "d20@0:8i16"
- "dataclass"
- "defaultConfiguration"
- "delete from Backups where backupUDID = ?"
- "delete from DisabledDomains"
- "delete from FileProtectionClassesToRestore"
- "delete from Files where backupUDID = ? and snapshotID = ? and deleted = 1"
- "delete from FilesMissingEncryptionKey where path = ?"
- "delete from Properties where key = ?"
- "delete from Snapshots where backupUDID = ? and snapshotID = ?"
- "domainNamesNotToBackUp"
- "doubleColumn:"
- "drop table if exists Properties;\ndrop table if exists Backups;\ndrop table if exists Snapshots;\ndrop table if exists Files;\ndrop table if exists FileExtendedAttributes;\ndrop table if exists DisabledDomains;\ndrop table if exists FileChanges;\ndrop table if exists FilesMissingEncryptionKey;\ndrop table if exists FileEncryptionKeys;\ndrop table if exists Restores;\ndrop table if exists RestoreFiles;\ndrop table if exists PlaceholderIcons;\ndrop table if exists FileProtectionClassesToRestore;\ndrop table if exists RestoreFailures;\ndrop table if exists PlaceholderResources;\ndrop table if exists KeyBagInfo;\n"
- "end"
- "errorWithCode:error:URL:format:"
- "fdopendir error"
- "getFilesCount"
- "getFilesSize"
- "icon"
- "infoWithID:uuid:"
- "initWithCache:SQL:stmt:"
- "initWithDelegate:mode:enginePolicy:debugContext:"
- "initWithFormat:arguments:"
- "initWithID:uuid:"
- "insert or replace into DisabledDomains values (?,?)"
- "insert or replace into FileEncryptionKeys values (?,?)"
- "insert or replace into Properties (key, value) values (?,?)"
- "insert or replace into RestoreFailures values (?,?,?,?,?,?)"
- "int64Column:"
- "intColumn:"
- "isReset"
- "listFilesCount"
- "maxFileAttributesSize"
- "maxInflightContainers"
- "mode != MBFileScannerModeUnspecified"
- "newlineCharacterSet"
- "numberWithUnsignedChar:"
- "pathsForFilesMissingEncryptionKeyWithOffset:limit:"
- "personalPersona"
- "pragma synchronous = normal"
- "protectionClassesToRestoreByPathWithOffset:limit:"
- "q20@0:8i16"
- "range.location == 0"
- "rangeOfCharacterFromSet:"
- "readdir error"
- "releaseCache:"
- "removeAllDisabledDomains"
- "removeAllProtectionClassesToRestore"
- "removeBackupForUDID:"
- "removeFileMissingEncryptionKeyWithPath:"
- "removeFilesCount"
- "removeObjectAtIndex:"
- "removePropertyForKey:"
- "removeSnapshotForID:backupUDID:lastModified:"
- "replaceSnapshotMountPointPrefix"
- "restoreFailuresForDataClass:assetType:range:"
- "select * from Snapshots where backupUDID = ?"
- "select count(*) from RestoreFailures where 1 %@ %@"
- "select domainName, relativePath, protectionClass from FileProtectionClassesToRestore limit ? offset ?"
- "select identifier, dataclass, assetType, displayName, icon, error from RestoreFailures where 1 %@ %@ order by dataclass, identifier limit ? offset ?"
- "select lastModified, attributes from Backups where backupUDID = ?"
- "select path from FilesMissingEncryptionKey limit ? offset ?"
- "select value from Properties where key = ?"
- "setAssetType:"
- "setBagID:"
- "setDataclass:"
- "setDisabledDomainNames:restrictedDomainNames:"
- "setDomainManager:"
- "setError:"
- "setFileEncryptionKey:forInodeNumber:"
- "setIcon:"
- "setIdentifier:"
- "setLastModified:forBackupUDID:"
- "setProperty:forKey:"
- "setReset:"
- "setStartTime:"
- "setUUID:"
- "setUploadStartTime:"
- "sharedPool"
- "snapshotsForBackupUDID:"
- "sortUsingComparator:"
- "startTime"
- "step"
- "systemPath"
- "textColumn:"
- "timeIntervalSinceNow"
- "typeOfColumn:"
- "unarchivedObjectOfClass:fromData:error:"
- "update Backups set lastModified = ? where backupUDID = ?"
- "update Files set duplicateFileID = null, duplicateSnapshotID = 0 where backupUDID = ? and snapshotID = ? and duplicateSnapshotID = ?"
- "update Snapshots set lastModified = ? where backupUDID = ? and snapshotID = ?"
- "update or ignore Files set snapshotID = ? where backupUDID = ? and snapshotID = ?"
- "uploadStartTime"
- "v24@0:8@\"NSString\"16"
- "v24@0:8i16i20"
- "v24@0:8r*16"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8q16i24"
- "v32@0:8@\"NSString\"16d24"
- "v32@0:8@16d24"
- "v40@0:8Q16@24q32"
- "valueOfColumn:"
- "verifyEqualToStmt:exceptColumnNumbers:"
- "\xf01"

```
