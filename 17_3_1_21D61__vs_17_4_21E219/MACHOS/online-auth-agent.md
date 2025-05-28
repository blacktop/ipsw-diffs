## online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

-381.0.0.0.0
-  __TEXT.__text: 0xee08
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_stubs: 0xd00
-  __TEXT.__objc_methlist: 0x14
-  __TEXT.__cstring: 0x1103
-  __TEXT.__oslogstring: 0x1cf6
-  __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__objc_methname: 0xa29
+386.100.27.0.0
+  __TEXT.__text: 0x399f4
+  __TEXT.__auth_stubs: 0x1cc0
+  __TEXT.__objc_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x1cc
+  __TEXT.__const: 0x1a2c
+  __TEXT.__cstring: 0x2f03
+  __TEXT.__oslogstring: 0x1fa4
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__objc_methname: 0x110d
   __TEXT.__dlopen_cstrs: 0x12c
-  __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methtype: 0x16c
-  __TEXT.__unwind_info: 0x2e0
-  __DATA_CONST.__auth_got: 0x668
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x830
-  __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __TEXT.__objc_classname: 0x58
+  __TEXT.__objc_methtype: 0x212
+  __TEXT.__swift5_typeref: 0x7d9
+  __TEXT.__swift5_capture: 0x2a0
+  __TEXT.__constg_swiftt: 0xab8
+  __TEXT.__swift5_reflstr: 0x6a5
+  __TEXT.__swift5_fieldmd: 0x908
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__swift5_proto: 0x148
+  __TEXT.__swift5_types: 0xd8
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_assocty: 0x150
+  __TEXT.__swift5_mpenum: 0x18
+  __TEXT.__unwind_info: 0xedc
+  __TEXT.__eh_frame: 0x114c
+  __DATA_CONST.__auth_got: 0xe70
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__auth_ptr: 0x60
+  __DATA_CONST.__const: 0x2750
+  __DATA_CONST.__cfstring: 0xce0
+  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x448
-  __DATA.__objc_selrefs: 0x348
-  __DATA.__objc_classrefs: 0xc8
-  __DATA.__objc_data: 0x50
-  __DATA.__data: 0x72c
-  __DATA.__bss: 0xc0
+  __DATA.__objc_const: 0xee0
+  __DATA.__objc_selrefs: 0x5d0
+  __DATA.__objc_ivar: 0x14
+  __DATA.__objc_data: 0x2e0
+  __DATA.__data: 0x1c14
+  __DATA.__bss: 0x2640
+  __DATA.__common: 0xa8
+  - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 295
-  Symbols:   275
-  CStrings:  504
+  - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  Functions: 1396
+  Symbols:   418
+  CStrings:  832
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CKErrorDomain
+ _MISetLaunchWarning
+ _NSFileSize
+ _OBJC_CLASS_$_CKAsset
+ _OBJC_CLASS_$_CKContainer
+ _OBJC_CLASS_$_CKContainerID
+ _OBJC_CLASS_$_CKFetchRecordZoneChangesConfiguration
+ _OBJC_CLASS_$_CKFetchRecordZoneChangesOperation
+ _OBJC_CLASS_$_CKFetchRecordsOperation
+ _OBJC_CLASS_$_CKRecord
+ _OBJC_CLASS_$_CKRecordID
+ _OBJC_CLASS_$_CKRecordZone
+ _OBJC_CLASS_$_CKRecordZoneID
+ _OBJC_CLASS_$_CKServerChangeToken
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_MIAppIdentity
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_OS_dispatch_queue_serial
+ _OBJC_CLASS_$_OS_os_log
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_CLASS_$_RBSTerminateContext
+ _OBJC_CLASS_$_RBSTerminateRequest
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _SecCodeCopySigningInformation
+ _SecStaticCodeCreateWithPath
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreGraphics
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_reportUnimplementedInitializer
+ _chmod
+ _fstat
+ _kSecCodeInfoCdHashesFull
+ _kSecCodeInfoDigestAlgorithm
+ _malloc_size
+ _memmove
+ _memset
+ _objc_allocWithZone
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x4
+ _objc_retain_x9
+ _setxattr
+ _sqlite3_bind_blob
+ _sqlite3_bind_int64
+ _sqlite3_bind_text
+ _sqlite3_busy_timeout
+ _sqlite3_close
+ _sqlite3_column_blob
+ _sqlite3_column_bytes
+ _sqlite3_column_count
+ _sqlite3_column_int64
+ _sqlite3_column_name
+ _sqlite3_column_origin_name
+ _sqlite3_column_table_name
+ _sqlite3_column_text
+ _sqlite3_db_readonly
+ _sqlite3_errcode
+ _sqlite3_errmsg
+ _sqlite3_finalize
+ _sqlite3_last_insert_rowid
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_step
+ _sqlite3_wal_checkpoint_v2
+ _swift_allocBox
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_dynamicCastObjCClass
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initEnumMetadataMultiPayload
+ _swift_initStackObject
+ _swift_initStaticObject
+ _swift_initStructMetadata
+ _swift_isEscapingClosureAtFileLocation
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_projectBox
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_retain_n
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagMultiPayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _xpc_dictionary_set_data
CStrings:
+ "\x01\x11"
+ "%@-shm"
+ "%@-wal"
+ "%@_%s"
+ ", user_override, pk FROM launch_warning WHERE cdhash_type = ?1 AND cdhash = ?2"
+ ", user_override, pk FROM launch_warning WHERE pk = ?1"
+ ".cxx_destruct"
+ "/var/db/MobileIdentityData"
+ "/var/db/MobileIdentityData/LaunchWarning.db"
+ "@\"NSDictionary\"8@?0"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSURL\""
+ "@24@0:8@16"
+ "@28@0:8@16B24"
+ "@36@0:8@16I24^@28"
+ "ALTER TABLE launch_warning ADD COLUMN kb_url TEXT DEFAULT NULL"
+ "Adding launch warning mark to: %@"
+ "Attempt to fetch warning details with no zone"
+ "B"
+ "B24@0:8^@16"
+ "B24@?0^{sqlite3_stmt=}8@\"NSDictionary\"16"
+ "B36@0:8B16Q20^@28"
+ "Base asset had invalid payload: %@"
+ "Base asset record changed: %@"
+ "Base asset record error: %@, %@"
+ "Base asset sync with token: %@"
+ "Base sync completion error: %@"
+ "CKRecordValue"
+ "CREATE TABLE IF NOT EXISTS launch_warning (\n    pk INTEGER PRIMARY KEY AUTOINCREMENT,\n    cdhash_type INTEGER,\n    cdhash BLOB NOT NULL,\n    reason INTEGER,\n    flags INTEGER,\n    user_override BOOLEAN,\n    timestamp INTEGER,\n    UNIQUE(cdhash_type, cdhash))"
+ "CREATE TABLE IF NOT EXISTS settings ( name TEXT, value TEXT, PRIMARY KEY (name) )"
+ "Caller didn't provide cdhash data"
+ "CloudKit asset doesn't have a file URL: %@"
+ "CloudKit fetch for warning: %@"
+ "CloudKit record has invalid algorithm: %@"
+ "CloudKit record has invalid bitsPerEntry count: %@"
+ "CloudKit record has invalid data: %@"
+ "CloudKit record has invalid details zone: %@"
+ "CloudKit record has invalid entryCount: %@"
+ "CloudKit record has invalid flags field: %@"
+ "CloudKit record has invalid id: %@"
+ "CloudKit record has invalid payload field: %@"
+ "CloudKit record has invalid reason field: %@"
+ "CloudKit record has invalid salt: %@"
+ "CloudKit record has invalid size: %@"
+ "CloudKit record has invalid update number: %@"
+ "CloudKit record has invalid update zone: %@"
+ "CloudKit record has invalid uuid: %@"
+ "CloudKit results block never called."
+ "CloudKit unexpected error during fetch: %@"
+ "Created launch warning entry: %d"
+ "DB being loaded from %@"
+ "DELETE FROM settings WHERE name = ?1"
+ "Database failed to initialize."
+ "Division by zero"
+ "Division results in an overflow"
+ "Error creating new launch warning for %@"
+ "Error opening DB: %d"
+ "Error processing app: %@, %@"
+ "Failed to add launch warning mark with no error: %@"
+ "Failed to add launch warning mark: %@, %@"
+ "Failed to chmod document checker: %d"
+ "Failed to install document checker: %@"
+ "Failed to notify about new document checker: %u"
+ "Failed to terminate app: %@"
+ "Fatal error"
+ "Finalize error (%d) on query: %@"
+ "Found launch warning for %@ with details: %@"
+ "Found launch warning with details: %@"
+ "Found no launch warning for %@"
+ "Found no launch warning for cdhash: %d, %@"
+ "Get launch warning data failed: %@"
+ "Got updated base sync token: %@"
+ "Got updated update sync token: %@"
+ "INSERT INTO launch_warning (cdhash_type, cdhash, reason, flags, user_override, timestamp, kb_url) VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)"
+ "INSERT OR REPLACE INTO settings (name, value) VALUES (?1, ?2)"
+ "Insufficient space allocated to copy string contents"
+ "Invalid reason in database: %lld"
+ "Item not present in bloom filter: %d, %@"
+ "LWControllerOperations"
+ "Launch warning found: %d, %@"
+ "Launch warning has unknown reason and flags indicate to ignore: %d, %@"
+ "Launch warning lookup failed due to missing controller."
+ "Launch warning sync failed due to missing controller."
+ "Launch warning sync found %ld local warnings."
+ "Launch warning sync found no impacted apps."
+ "Launch warning sync had error: %@"
+ "Launch warning sync triggered an update."
+ "LaunchWarnings"
+ "Looking up launch warning for cdhash: %d, %@"
+ "Merging in bloom filter update: %d for filter %@"
+ "MobileIdentityService"
+ "No bloom filter configured."
+ "No launch warning present: %d, %@"
+ "PRAGMA foreign_keys = ON"
+ "PRAGMA journal_mode = WAL"
+ "Performing regular launch warning sync."
+ "Posting launch warning override notification failed: %d"
+ "Prepare error (%d) on query: %@"
+ "Q24@0:8@16"
+ "Query canceled"
+ "Removing old bloom filter: %s"
+ "SELECT COUNT(*) FROM %@"
+ "SELECT value FROM settings WHERE name = ?1"
+ "SQL error '%s' (%1d)"
+ "SQLDB"
+ "Set launch warning override failed: %@"
+ "Setting up new base filter: %@"
+ "Setting user override: %lld to %d"
+ "Starting sync of zone: %@"
+ "Step error (%d) on query: %@"
+ "Successfully terminated app: %@"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Sync error: %@"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSURL\",R,N"
+ "T@\"NSURL\",R,N,V_url"
+ "Td,R,N,V_totalSizeMB"
+ "Terminated for launch warning enforcement."
+ "Terminating app: %s"
+ "UPDATE launch_warning SET user_override = ?1 WHERE pk = ?2"
+ "URL"
+ "URLByAppendingPathComponent:"
+ "URLByDeletingLastPathComponent"
+ "Unable to add launch warning to app without installation ID: $@"
+ "Unable to create code object (%d) for: %@"
+ "Unable to create signing info (%d) for: %@"
+ "Unable to find cdhash for %@"
+ "Unable to get best cdhash data: %@"
+ "Unable to get best cdhash digest algorithm: %@"
+ "Unable to get full cdhash information for: %@"
+ "Unable to look up launch warning info for ID: %lld"
+ "Unable to table row count for %@: %d"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Update asset %lld had invalid compressed data"
+ "Update asset had incorrect ID: %{public}@, %{public}@"
+ "Update asset had invalid compression type: %@"
+ "Update entry sync error: %{public}@"
+ "Update sync completion error: %@"
+ "Update sync error: %@"
+ "Update zone record changed: %@"
+ "Update zone sync with no configured zone"
+ "Update zone sync with token: %@"
+ "Updated new document checker."
+ "Visiting application: %@"
+ "XPC: checking launch warning data for: %llu, %@"
+ "XPC: launch warning data response: %@, %lu"
+ "^{sqlite3=}"
+ "_TtC17online_auth_agent10AppManager"
+ "_TtC17online_auth_agent11BloomFilter"
+ "_TtC17online_auth_agent12SQLStatement"
+ "_TtC17online_auth_agent14MetricReporter"
+ "_TtC17online_auth_agent15LaunchWarningDB"
+ "_TtC17online_auth_agent17LaunchWarningMark"
+ "_TtC17online_auth_agent18CloudKitOperations"
+ "_TtC17online_auth_agent20BloomFilterAlgorithm"
+ "_TtC17online_auth_agent22BloomFilterDiskStorage"
+ "_TtC17online_auth_agent23LaunchWarningController"
+ "_TtC17online_auth_agent23LaunchWarningOperations"
+ "_TtC17online_auth_agent6Logger"
+ "__swift_objectForKeyedSubscript:"
+ "_db"
+ "_readonly"
+ "_totalSizeMB"
+ "_transactionSem"
+ "_url"
+ "addOperation:"
+ "algorithm"
+ "appManager"
+ "attributesOfItemAtPath:error:"
+ "baseURL"
+ "begin immediate transaction"
+ "begin transaction"
+ "bitsPerEntry"
+ "bits_per_element"
+ "bloomfilter.plist"
+ "bundleIdentifier"
+ "cdhash_type, cdhash, reason, flags, timestamp, kb_url"
+ "cdhd"
+ "cdht"
+ "checkpoint"
+ "chlw"
+ "cloudkit"
+ "code"
+ "com.apple.mis.launchwarning.flagged"
+ "com.apple.mis.launchwarning.override"
+ "com.apple.mis.launchwarning.sync"
+ "com.apple.mis.launchwarning.sync.error"
+ "com.apple.mis.warning"
+ "com.apple.mis.warning.override"
+ "com.apple.sear.launch-warnings"
+ "configuration"
+ "copyItemAtURL:toURL:error:"
+ "createFileAtPath:contents:attributes:"
+ "creationDate"
+ "d"
+ "d16@0:8"
+ "data"
+ "databaseSchemaVersion"
+ "databaseWithURL:"
+ "db"
+ "dbURL"
+ "db_utils.m"
+ "dealloc"
+ "defaultManager"
+ "deleteSetting:"
+ "dictionaryWithCapacity:"
+ "document_checker_v1"
+ "domain"
+ "end transaction"
+ "enumeratorWithOptions:"
+ "execute:"
+ "executeQuery:withBind:withCancellableResults:"
+ "executeQuery:withBind:withResults:"
+ "expiredBaseToken"
+ "expiredUpdateToken"
+ "fh"
+ "fileExistsAtPath:"
+ "fileHandleForReadingFromURL:error:"
+ "fileHandleForUpdatingURL:error:"
+ "fileHandleForWritingToURL:error:"
+ "fileURL"
+ "filter"
+ "hasSuffix:"
+ "hashFn"
+ "i16@0:8"
+ "i24@0:8@?16"
+ "i28@0:8@?16B24"
+ "i40@0:8@16@?24@?32"
+ "iTunesMetadata"
+ "id"
+ "init"
+ "init()"
+ "initWithBase64EncodedString:options:"
+ "initWithBundleID:"
+ "initWithContainerID:"
+ "initWithContainerIdentifier:environment:"
+ "initWithContentsOfURL:options:error:"
+ "initWithDatabaseURL:"
+ "initWithDatabaseURL:asReadOnly:"
+ "initWithExplanation:"
+ "initWithPredicate:context:"
+ "initWithRecordIDs:"
+ "initWithZoneName:"
+ "invalid Collection: less than 'count' elements in collection"
+ "isAppStoreVendable"
+ "lastInsertRowID"
+ "lastPathComponent"
+ "launchWarningController"
+ "launch_warnings_base_asset_v1"
+ "launch_warnings_base_assets_v1"
+ "launch_warnings_update_v1"
+ "lookupLaunchWarningData:cdhashType:error:"
+ "lwid"
+ "lwov"
+ "metrics"
+ "name"
+ "newDocumentChecker"
+ "online_auth_agent.LaunchWarningDB"
+ "path != NULL"
+ "predicateMatchingBundleIdentifier:"
+ "publicCloudDatabase"
+ "raw"
+ "readSetting:"
+ "removeItemAtURL:error:"
+ "rollback transaction"
+ "runtime"
+ "s"
+ "salt"
+ "seekToOffset:error:"
+ "setDatabasePermissionsInternal"
+ "setMaximumTerminationResistance:"
+ "setPreferAnonymousRequests:"
+ "setPreviousServerChangeToken:"
+ "setQualityOfService:"
+ "setSetting:toValue:"
+ "setUserOverride:forID:error:"
+ "setupPermissions"
+ "setupSchema"
+ "shmURL"
+ "size"
+ "storage"
+ "stringWithFormat:"
+ "substringToIndex:"
+ "substringWithRange:"
+ "swift_forEach:"
+ "syncLaunchWarningsAndReturnError:"
+ "syncQueue"
+ "tableRowCount:"
+ "teamIdentifier"
+ "totalSizeMB"
+ "transaction:"
+ "transaction:immediate:"
+ "unable to check filesystem permissions on db: %d, %s"
+ "unable to open file to update permissions: %d, %s"
+ "unable to set filesystem permissions on db: %d, %s"
+ "uniqueInstallIdentifier"
+ "unsignedIntegerValue"
+ "url"
+ "v16@0:8"
+ "v16@?0@\"LSApplicationRecord\"8"
+ "v16@?0^v8"
+ "v16@?0^{sqlite3_stmt=}8"
+ "v24@?0^v8@\"NSDictionary\"16"
+ "v24@?0^{sqlite3_stmt=}8@\"NSDictionary\"16"
+ "versionIdentifier"
+ "waitUntilFinished"
+ "walURL"
+ "warndata"
+ "warningID"
+ "writeData:"
+ "zoneID"
+ "zoneName"

```
