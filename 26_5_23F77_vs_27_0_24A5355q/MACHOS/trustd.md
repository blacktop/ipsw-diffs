## trustd

> `/usr/libexec/trustd`

```diff

-61901.120.67.0.0
-  __TEXT.__text: 0x68534
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x3200
-  __TEXT.__objc_methlist: 0xd54
-  __TEXT.__const: 0x5ab1
+62426.0.0.0.4
+  __TEXT.__text: 0x593f4
+  __TEXT.__auth_stubs: 0x2390
+  __TEXT.__objc_stubs: 0x3340
+  __TEXT.__objc_methlist: 0xe0c
+  __TEXT.__const: 0xbd50
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__gcc_except_tab: 0xce0
-  __TEXT.__cstring: 0x735c
-  __TEXT.__oslogstring: 0x68b8
-  __TEXT.__objc_classname: 0x1b1
-  __TEXT.__objc_methname: 0x3082
-  __TEXT.__objc_methtype: 0xc75
-  __TEXT.__unwind_info: 0x1148
-  __DATA_CONST.__auth_got: 0x1228
-  __DATA_CONST.__got: 0x7d0
-  __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x4e38
-  __DATA_CONST.__cfstring: 0x6840
-  __DATA_CONST.__objc_classlist: 0x78
+  __TEXT.__objc_classname: 0x1ce
+  __TEXT.__objc_methname: 0x2f89
+  __TEXT.__objc_methtype: 0xc79
+  __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_typeref: 0x17
+  __TEXT.__swift5_reflstr: 0x4
+  __TEXT.__swift5_fieldmd: 0x1c
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0xb04
+  __TEXT.__cstring: 0x5ddc
+  __TEXT.__oslogstring: 0x5739
+  __TEXT.__unwind_info: 0x1000
+  __DATA_CONST.__const: 0x41b0
+  __DATA_CONST.__cfstring: 0x5d80
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA.__objc_const: 0x16e0
-  __DATA.__objc_selrefs: 0xe20
-  __DATA.__objc_ivar: 0xd4
-  __DATA.__objc_data: 0x4b0
-  __DATA.__data: 0x428
-  __DATA.__bss: 0x528
+  __DATA_CONST.__auth_got: 0x11d8
+  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__objc_const: 0x1758
+  __DATA.__objc_selrefs: 0xe50
+  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_data: 0x5b8
+  __DATA.__data: 0x450
+  __DATA.__bss: 0x520
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C541921D-EE79-3A36-B808-115E3F386531
-  Functions: 1325
-  Symbols:   847
-  CStrings:  3233
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: A564EC80-E7E1-3154-8DFE-E16E4AB4C1E6
+  Functions: 1219
+  Symbols:   851
+  CStrings:  2934
 
Symbols:
+ _$sBOWV
+ _CFURLCopyHostName
+ _CFURLCreateWithString
+ _NSKeyValueChangeNewKey
+ _NSKeyValueChangeOldKey
+ _OBJC_CLASS_$_NWPath
+ _OBJC_CLASS_$_NWPathEvaluator
+ _SecCertificateHasExtensions
+ _SecCertificateHasNoSecondsUTCValidityDate
+ _SecCertificateHasUniqueIdentifiers
+ __CFHostIsDomainTopLevelForCertificatePolicy
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ _kSecPolicyCheckCertificateVersionExtensions
+ _kSecPolicyCheckRevocationDbIgnoredForAppleCodeSignChain
+ _kSecPolicyCheckUTCTimeNoSeconds
+ _kSecPolicyCheckUniqueIdentifiers
+ _kSecTrustInfoBuilderKey
+ _kSecTrustInfoRevocationDbIgnored
+ _kSecTrustInfoRevocationIfTrusted
+ _kSecTrustInfoRevocationOnline
+ _objc_claimAutoreleasedReturnValue
+ _objc_getClass
+ _objc_opt_respondsToSelector
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _CC_SHA256_Final
- _CC_SHA256_Init
- _CC_SHA256_Update
- _CFCharacterSetCreateWithCharactersInString
- _CFDictionaryGetKeysAndValues
- _CFStringAppendCString
- _CFStringCreateExternalRepresentation
- _CFStringFindCharacterFromSet
- _OBJC_CLASS_$_NSFileHandle
- _OBJC_EHTYPE_$_NSException
- _SecCMSVerify
- _SecCRLiteCertStatus
- _SecCRLiteCreate
- _SecCRLiteDestroy
- _SecCRLiteLoadFilter
- _SecPolicyCreateApplePinned
- _SecTrustGetTrustResult
- __CFCopySystemVersionDictionary
- __kCFSystemVersionBuildVersionKey
- _abort_report_np
- _deflate
- _deflateEnd
- _deflateInit_
- _dlerror
- _dlsym
- _kCFPreferencesCurrentHost
- _objc_setProperty_atomic_copy
- _os_variant_has_internal_diagnostics
- _qsort
- _sysctl
- _time
CStrings:
+ "@\"LRUStringCache\""
+ "@24@0:8Q16"
+ "@24@0:8^{__SecCertificate=}16"
+ "AnchorNoSecUTC"
+ "AnchorUniqueID"
+ "AnchorV1V2Ext"
+ "Apple Code Signing Certification Authority"
+ "Apple Worldwide Developer Relations Certification Authority"
+ "B20@0:8B16"
+ "B24@?0^{__SecRevocationDbConnection=^{__SecRevocationDb}^{__OpaqueSecDbConnection}qq}8^^{__CFError}16"
+ "B32@0:8@16^{__SecCertificate=}24"
+ "Enforcing CRLite result: idx: %d revoked: %d"
+ "HeuristicMitmDetector"
+ "Ignoring RevocationDb for Apple code signing chain"
+ "LRUStringCache"
+ "MITMErrorDomain"
+ "MitmDetectionEvent"
+ "MitmDetectorRootUsage"
+ "PriorMitmRoots.plist"
+ "SecDbConnectionRelease: backup connection %p not cached (ephemeral)"
+ "SecRevocationInitialSetup class method setup returned: %{public}@"
+ "SecRevocationInitialSetup instance method setup returned: %{public}@"
+ "SecRevocationInitialSetup no class"
+ "SecRevocationInitialSetup: no client for system trustd"
+ "SecRevocationResetDatabase class method setup returned: %{public}@"
+ "SecRevocationResetDatabase complete"
+ "SecRevocationResetDatabase needs update framework"
+ "SecRevocationUpdateValid: %{public}@"
+ "SwiftCRLiteClient"
+ "T@\"LRUStringCache\",&,V_gTLDPlusOne"
+ "T@\"LRUStringCache\",&,V_hostnames"
+ "T@\"NSArray\",&,V__priorMitmRoots"
+ "T@\"NSDate\",&,V_lastReset"
+ "T@\"NSDate\",&,V_lastUse"
+ "T@\"NSMutableArray\",&,V_strings"
+ "T@\"NSMutableDictionary\",&,V__rootHostnameMap"
+ "TB,V_pinningMitmDetected"
+ "TB,V_priorMitmRoot"
+ "TB,V_userTrustStore"
+ "TQ,V_size"
+ "Tq,V_score"
+ "Unable to open db connection (error %d)"
+ "Unable to open db connection (error %d/%d)"
+ "V1V2ExtSelfIssued"
+ "_TtC6trustd10TrustDObjC"
+ "__priorMitmRoots"
+ "__rootHostnameMap"
+ "_gTLDPlusOne"
+ "_hostnames"
+ "_lastReset"
+ "_lastUse"
+ "_pinningMitmDetected"
+ "_priorMitmRoot"
+ "_priorMitmRoots"
+ "_rootHostnameMap"
+ "_score"
+ "_size"
+ "_strings"
+ "_userTrustStore"
+ "addHostname:"
+ "addHostname:forRoot:"
+ "addObserver:forKeyPath:options:context:"
+ "addPinningFailureForRoot:"
+ "addRootUsage:forRoot:"
+ "arrayWithArray:"
+ "asking for help from Validupdater for initial setup"
+ "characterAtIndex:"
+ "checking revocation for cert: %ld (EV path %d)"
+ "com.apple.security.file./Library/Caches/com.apple.xbs/48649C44-242A-4662-B6EB-26485875B635/TemporaryDirectory.XNofSZ/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "completed: %{private}@ policies: %{public}@ details: %{public}@ result: %d"
+ "dateWithTimeIntervalSinceNow:"
+ "detected MITM for %@"
+ "detected MITM!!"
+ "failed to write mitm roots to disk: %@"
+ "findCRLiteForCertificate:issuer:additionalSCTs:"
+ "foo"
+ "gTLDPlusOne"
+ "getSwiftCRLiteClient: init failed with %{public}@"
+ "hostnames"
+ "initWithSize:"
+ "initWithURL:creationAllowed:error:"
+ "initialSetup:"
+ "isEqualToPath:"
+ "isMitmOperatingWithReporting:"
+ "isSetup"
+ "lastReset"
+ "lastUse"
+ "mitm"
+ "mitm_detection_purge_unused_roots"
+ "network changed, resetting detector"
+ "numDomains"
+ "observeValueForKeyPath:ofObject:change:context:"
+ "overallScore"
+ "pinningMitm"
+ "pinningMitmDetected"
+ "priorMitm"
+ "priorMitmRoot"
+ "priorMitmRoots"
+ "priorMitmRootsFileUrl"
+ "provisionDatabaseAt:environment:completionHandler:"
+ "purgeUnusedRoots"
+ "removeAllRoots"
+ "removeRoot:"
+ "reportMitmScores:"
+ "requestUpdateValid:"
+ "reset of valid database complete"
+ "resetDatabase:"
+ "rootHostnameMap"
+ "rootUsageForRoot:"
+ "rootUsages"
+ "schedule reset of valid database"
+ "score"
+ "setGTLDPlusOne:"
+ "setHostnames:"
+ "setLastReset:"
+ "setLastUse:"
+ "setPinningMitmDetected:"
+ "setPriorMitmRoot:"
+ "setPriorMitmRoots:"
+ "setScore:"
+ "setSize:"
+ "setStrings:"
+ "setUserTrustStore:"
+ "set_priorMitmRoots:"
+ "set_rootHostnameMap:"
+ "setup complete"
+ "sharedDefaultEvaluator"
+ "size"
+ "strings"
+ "timeSinceLastReset"
+ "userAnchor"
+ "userTrustStore"
+ "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}^{dispatch_queue_s}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
+ "v24@0:8^{__SecCertificate=}16"
+ "v48@0:8@16@24@32^v40"
+ "values"
- "%"
- "%ld"
- "%s canceled at %f"
- "*/*"
- "-journal"
- "-shm"
- "-wal"
- ".valid_replace"
- "0"
- "1"
- "1.2.840.113635.100.6.2.10"
- "1.2.840.113635.100.6.51"
- "2"
- "3"
- "4"
- "5"
- "6"
- "7"
- "8"
- "9"
- ":/"
- "://"
- "@\"NSFileHandle\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSURL\""
- "@\"NSURLSession\""
- "@20@0:8B16"
- "@36@0:8B16@20@28"
- "A"
- "ALTER TABLE groups ADD COLUMN policies BLOB"
- "Accept"
- "Accept-Encoding"
- "B12@?0i8"
- "B24@?0^{__SecRevocationDbConnection=^{__SecRevocationDb}^{__OpaqueSecDbConnection}qqqB}8^^{__CFError}16"
- "B40@0:8@16q24@32"
- "B44@0:8@16q24B32@36"
- "BEGIN IMMEDIATE"
- "CREATE TABLE IF NOT EXISTS admin(key TEXT PRIMARY KEY NOT NULL,ival INTEGER NOT NULL,value BLOB);CREATE TABLE IF NOT EXISTS issuers(groupid INTEGER NOT NULL,issuer_hash BLOB PRIMARY KEY NOT NULL);CREATE INDEX IF NOT EXISTS issuer_idx ON issuers(issuer_hash);CREATE TABLE IF NOT EXISTS groups(groupid INTEGER PRIMARY KEY AUTOINCREMENT,flags INTEGER,format INTEGER,data BLOB,policies BLOB);CREATE TABLE IF NOT EXISTS serials(groupid INTEGER NOT NULL,serial BLOB NOT NULL,UNIQUE(groupid,serial));CREATE TABLE IF NOT EXISTS hashes(groupid INTEGER NOT NULL,sha256 BLOB NOT NULL,UNIQUE(groupid,sha256));CREATE TABLE IF NOT EXISTS dates(groupid INTEGER PRIMARY KEY NOT NULL,notbefore REAL,notafter REAL);CREATE TABLE IF NOT EXISTS crlitefilters(filterid INTEGER PRIMARY KEY NOT NULL,filterversion INTEGER,data BLOB);CREATE TABLE IF NOT EXISTS crlitefiltercoverage(filterid INTEGER NOT NULL,logid BLOB NOT NULL,generatedat REAL,start REAL,end REAL,UNIQUE(filterid,logid));CREATE TRIGGER IF NOT EXISTS group_del BEFORE DELETE ON groups FOR EACH ROW BEGIN DELETE FROM serials WHERE groupid=OLD.groupid; DELETE FROM hashes WHERE groupid=OLD.groupid; DELETE FROM issuers WHERE groupid=OLD.groupid; DELETE FROM dates WHERE groupid=OLD.groupid; END;"
- "CREATE TABLE IF NOT EXISTS dates(groupid INTEGER PRIMARY KEY NOT NULL,notbefore REAL,notafter REAL);"
- "CRLite section trailing bytes exceed remaining buffer"
- "CRLite: certificate is %s"
- "Computed: %@"
- "D"
- "DELETE FROM crlitefiltercoverage; DELETE FROM crlitefilters;"
- "DELETE FROM groups WHERE groupid=?"
- "DELETE FROM groups; DELETE FROM crlitefiltercoverage; DELETE FROM crlitefilters;DELETE FROM admin WHERE key='version'; DELETE FROM sqlite_sequence"
- "DELETE FROM hashes WHERE groupid=? AND hex(sha256) LIKE ?"
- "DELETE FROM issuers WHERE groupid=?"
- "DELETE FROM serials WHERE groupid=? AND hex(serial) LIKE ?"
- "DROP TRIGGER IF EXISTS group_del;CREATE TRIGGER group_del BEFORE DELETE ON groups FOR EACH ROW BEGIN DELETE FROM serials WHERE groupid=OLD.groupid; DELETE FROM hashes WHERE groupid=OLD.groupid; DELETE FROM issuers WHERE groupid=OLD.groupid; DELETE FROM dates WHERE groupid=OLD.groupid; END;"
- "E"
- "Enforcing CRLite result"
- "Expected: %@"
- "F"
- "FAIL"
- "Failed to deserialize CRLite filter metadata for filter %u of %u"
- "Failed to deserialize update chunk %u of %u"
- "Failed to evaluate CRLite certificate revocation status against filter %lld: %@"
- "Failed to extract SCT logID and timestamp"
- "Failed to get CRLite filter data for filter %ld: %@"
- "Failed to get CRLite filter data: %@"
- "Failed to ingest CRLite filter for filter %u of %u"
- "Failed to load CRLite filter: %@"
- "Failed to parse CRLite filter metadata for filter %u of %u"
- "Finished verifying db content; result=%s"
- "Got SIGTERM, abandon all hope and clear transaction"
- "INSERT INTO crlitefiltercoverage (filterid,logid,generatedat,start,end) VALUES (?,?,?,?,?)"
- "INSERT INTO crlitefilters (filterversion,data) VALUES (?,?)"
- "INSERT OR REPLACE INTO dates (groupid,notbefore,notafter) VALUES (?,?,?)"
- "INSERT OR REPLACE INTO groups (groupid,flags,format,data,policies) VALUES (?,?,?,?,?)"
- "INSERT OR REPLACE INTO hashes (groupid,sha256) VALUES (?,?)"
- "INSERT OR REPLACE INTO issuers (groupid,issuer_hash) VALUES (?,?)"
- "INSERT OR REPLACE INTO serials (groupid,serial) VALUES (?,?)"
- "Invalid filter version in metadata; expected: %ld, got: %ld"
- "MIMEType"
- "Next update time: %f"
- "Reader attempting to acquire lock starting from index %d"
- "Reader no locks available, waiting on lock[%d]"
- "Reader releasing lock[%d]"
- "Reader successfully acquired lock[%d]"
- "Reader successfully acquired lock[%d] (after waiting)"
- "Reader successfully released lock[%d]"
- "Recreate VALID db generation %ld from previous %ld"
- "SELECT COUNT(*) FROM pragma_table_info('groups') WHERE name = 'policies'"
- "SELECT DISTINCT groupid FROM issuers ORDER BY issuer_hash ASC"
- "SELECT count(*) FROM groups"
- "SELECT count(*) FROM hashes WHERE groupid=?"
- "SELECT count(*) FROM issuers WHERE groupid=?"
- "SELECT count(*) FROM serials WHERE groupid=?"
- "SELECT data FROM crlitefilters WHERE filterid=?"
- "SELECT filterid FROM crlitefiltercoverage WHERE logid=?1 AND ?2 >= start AND ?2 <= end ORDER BY generatedat"
- "SELECT flags,format,data FROM groups WHERE groupid=?"
- "SELECT issuer_hash FROM issuers WHERE groupid=? ORDER BY issuer_hash ASC"
- "SELECT ival FROM admin WHERE key='db_format'"
- "SELECT ival FROM admin WHERE key='interval'"
- "SELECT serial FROM serials WHERE groupid=? ORDER BY serial ASC"
- "SELECT sha256 FROM hashes WHERE groupid=? ORDER by sha256 ASC"
- "SELECT value FROM admin WHERE key='check_again'"
- "SELECT value FROM admin WHERE key='db_hash'"
- "SUCCESS"
- "SecCRLiteCopyCoverageInfo"
- "SecDbConnectionAcquireRefMigrationSafe: acquired %s connection with index %d"
- "SecDbConnectionAcquireRefMigrationSafe: acquiring %s connection%s"
- "SecDbConnectionAcquireRefMigrationSafe: failed to get connection, releasing acquired lock"
- "SecDbConnectionAcquireRefMigrationSafe: stored lock index %d in %s connection %p"
- "SecDbConnectionAcquireRefMigrationSafe: successfully acquired %s connection %p with lock index %d"
- "SecDbConnectionRelease: releasing %s connection %p with lock index %d"
- "SecDbCreate: initializing %zu reader locks and 1 writer lock supporting priority donation"
- "SecDbCreate: successfully initialized separated locking system with %zu reader locks and 1 writer lock"
- "SecDbForEach step[%d]"
- "SecDbForEach: SecDbConnection is readonly but we're about to write: %s"
- "SecRevocationDbIngestCRLiteUpdate failed: %@"
- "SecValidUpdateProcessCRLiteSection: CRLite section overrun"
- "SecValidUpdateProcessCRLiteSection: failed to clear CRLite database due to fullCRLiteUpdate"
- "SecValidUpdateProcessCRLiteSection: failed to ingest CRLite filter"
- "SecValidUpdateProcessCRLiteSection: failed to parse CRLite filter metadata"
- "SecValidUpdateProcessCRLiteSection: failed to parse overall CRLite metadata"
- "SecValidUpdateProcessCRLiteSection: invalid CRLite filter data length"
- "SecValidUpdateProcessCRLiteSection: invalid CRLite section length"
- "SecValidUpdateProcessCRLiteSection: missing CRLite filter count"
- "SecValidUpdateProcessCRLiteSection: missing CRLite filter data length"
- "SecValidUpdateProcessCRLiteSection: missing CRLite filter metadata length"
- "SecValidUpdateProcessCRLiteSection: missing CRLite section length"
- "SecValidUpdateProcessCRLiteSection: missing overall CRLite metadata length"
- "SecValidUpdateProcessData: data length is too short"
- "SecValidUpdateProcessData: data longer than expected"
- "SecValidUpdateProcessData: failed to get update chunk"
- "SecValidUpdateProcessData: invalid filter version in metadata"
- "SecValidUpdateProcessData: invalid update format"
- "Session %@ data task %@ returned response %ld (%@), expecting %lld bytes"
- "Session %@ task %@ failed with error %@"
- "Skipping property list creation (dataLength=%ld, bytesRemaining=%ld)"
- "Skipping property list creation (length %ld is too short)"
- "Started verifying db content"
- "T@\"NSDate\",&,V_startedDownload"
- "T@\"NSFileHandle\",&,V_currentUpdateFile"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_revDbUpdateQueue"
- "T@\"NSObject<OS_os_transaction>\",&,V_transaction"
- "T@\"NSString\",&,V_currentUpdateServer"
- "T@\"NSURL\",&,V_currentUpdateFileURL"
- "T@\"NSURLSession\",&,V_backgroundSession"
- "T@\"NSURLSession\",&,V_ephemeralSession"
- "T@?,C,V_handler"
- "TB,V_finishedDownloading"
- "TB,V_forceVersion"
- "Td,V_updateScheduled"
- "Tq,V_version"
- "UPDATE OR IGNORE groups SET policies=? WHERE groupid=?"
- "Unable to force reset of Valid DB"
- "Unable to read db_hash values"
- "Unable to update Valid DB from user agent"
- "Update received: v%ld"
- "Valid Update SecTrustEvaluate failed with trust result %d\n"
- "Valid updates not enabled on this device"
- "ValidDelegate"
- "ValidDownloadMetric"
- "ValidIngestionMetric"
- "ValidUpdateBackground"
- "ValidUpdateEnabled"
- "ValidUpdateEvent"
- "ValidUpdateGeneration"
- "ValidUpdateInterval"
- "ValidUpdateRequest"
- "ValidUpdateServer"
- "ValidUpdateWiFiOnly"
- "ValidVerifyEnabled"
- "Writer attempting to acquire writer lock"
- "Writer releasing writer lock"
- "Writer successfully acquired writer lock"
- "Writer successfully released writer lock"
- "_SecRevocationDbApplyGroupDelete failed: %@"
- "_SecRevocationDbApplyUpdate failed: invalid args"
- "_SecRevocationDbApplyUpdate: invalid db or update parameter"
- "_SecRevocationDbCRLiteMergeCoveringFilter failed: %@"
- "_SecRevocationDbGetNextUpdateTime failed: %@"
- "_SecRevocationDbGetUpdateFormat failed: %@"
- "_SecRevocationDbGetUpdateInterval failed: %@"
- "_SecRevocationDbRemoveAllEntries failed: %@"
- "_SecRevocationDbSetGeneration failed: %@"
- "_SecRevocationDbSetNextUpdate failed: %@"
- "_SecRevocationDbSetSchemaVersion failed: %@"
- "_SecRevocationDbSetUpdateFormat failed: %@"
- "_SecRevocationDbSetUpdateInterval failed: %@"
- "_SecRevocationDbSetUpdateSource failed: %@"
- "_SecRevocationDbSetUpdateSource failed: %d"
- "_SecRevocationDbSetUpdateSource failed: unable to get UTF-8 encoding"
- "_SecRevocationDbSetVersion failed: %@"
- "_SecRevocationDbUpdateDateConstraints failed (ok=%s, localError=%@)"
- "_SecRevocationDbUpdateGroup failed: %@"
- "_SecRevocationDbUpdateIssuers failed: %@"
- "_SecRevocationDbUpdatePerIssuerData failed: %@"
- "_SecRevocationDbUpdatePolicyConstraints failed (ok=%s, localError=%@)"
- "_SecRevocationDbUpdateSchema failed: %@"
- "_SecRevocationDbUpdateSchema failed: no DBC"
- "_backgroundSession"
- "_currentUpdateFile"
- "_currentUpdateFileURL"
- "_currentUpdateServer"
- "_ephemeralSession"
- "_finishedDownloading"
- "_forceVersion"
- "_handler"
- "_obliterateAllBackgroundSessionsWithCompletionHandler:"
- "_revDbUpdateQueue"
- "_startedDownload"
- "_transaction"
- "_updateScheduled"
- "_version"
- "backgroundSession"
- "backgroundSessionConfigurationWithIdentifier:"
- "cancel"
- "check-again"
- "check-ocsp"
- "check_again"
- "checking revocation for cert: %ld"
- "closeFile"
- "com.apple.security.file./Library/Caches/com.apple.xbs/D00E3CE5-2824-4945-9D1C-0AA58C59B514/TemporaryDirectory.YfKjPN/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
- "com.apple.trustd.networking.background"
- "com.apple.trustd.valid.checkNextUpdate"
- "com.apple.trustd.valid.download"
- "com.apple.trustd.valid.scheduleUpdate"
- "com.apple.trustd.valid.updateDb"
- "completed: %{private}@ details: %{public}@ result: %d"
- "copyfile error %d"
- "createSession:queue:forServer:"
- "createSessions:forServer:"
- "crlitefiltercache"
- "currentUpdateFile"
- "currentUpdateFileURL"
- "currentUpdateServer"
- "dataTaskWithURL:"
- "db_format"
- "db_hash"
- "db_source"
- "db_version"
- "download"
- "download started at %@"
- "downloadTime"
- "ephemeralSession"
- "expectedContentLength"
- "failed to change protection class of copied valid snapshot: %@"
- "failed to change replace valid db flag protection class: %@"
- "failed to clear CRLite database due to fullCRLiteUpdate"
- "failed to connect to URL. canceling task %@"
- "failed to find revocation info directory. canceling task %@"
- "failed to open %@: %@. canceling task %@"
- "failed to parse overall CRLite metadata"
- "failed to parse overall CRLite metadata (len %u, remaining %zu)"
- "failed to process valid update: %@"
- "failed to read %@ with error %d"
- "failed to verify Valid Update: %d"
- "failed to verify valid update"
- "fileHandleForWritingToURL:error:"
- "finishedDownloading"
- "forceVersion"
- "found a bad filter cache entry at %ld"
- "full"
- "fullCRLiteUpdate"
- "generatedAt"
- "generation"
- "group not found for issuer"
- "gzip,deflate,br"
- "handler"
- "https://%@/g%ld/v%ld"
- "https://%@/o%ld/v%ld"
- "initializing database"
- "insufficient data for CRLite filter count"
- "insufficient data for CRLite filter data length"
- "insufficient data for CRLite filter metadata length"
- "insufficient data for CRLite section length"
- "insufficient data for overall CRLite metadata length"
- "interval"
- "invalid CRLite filter data length %u (remaining %zu)"
- "invalid CRLite section length: %u (remaining %zu)"
- "invalid update data"
- "invalid update request"
- "issuer-hash"
- "known-intermediates-only"
- "logMetric:withName:"
- "missing update queue, skipping update"
- "no-ca"
- "no-ca-v2"
- "not-after"
- "not-before"
- "notRevoked"
- "nto1"
- "postponing update until %f"
- "process exiting to replace db file"
- "processing CRLLite section"
- "reader"
- "received data, but output file is not open"
- "remove (%s): %s"
- "removing all old sessions for trustd"
- "require-ct"
- "reschedule"
- "resetting database, result: %d (expected 1)"
- "revDbUpdateQueue"
- "running foreground data task %@ at %f URL:%@"
- "scheduleUpdateFromServer:forVersion:withQueue:"
- "scheduled background data task %@ at %f URL:%@"
- "scheduling update at %f"
- "serial"
- "setBackgroundSession:"
- "setCurrentUpdateFile:"
- "setCurrentUpdateFileURL:"
- "setCurrentUpdateServer:"
- "setEphemeralSession:"
- "setFinishedDownloading:"
- "setForceVersion:"
- "setHandler:"
- "setMaxConcurrentOperationCount:"
- "setNetworkServiceType:"
- "setRevDbUpdateQueue:"
- "setStartedDownload:"
- "setTLSMinimumSupportedProtocol:"
- "setTaskDescription:"
- "setTransaction:"
- "setUpdateScheduled:"
- "setVersion:"
- "set_requiresPowerPluggedIn:"
- "skipping update"
- "startedDownload"
- "starting to process full update; clearing database"
- "starting update"
- "statusCode"
- "stringWithContentsOfFile:"
- "switching db source from \"%@\" to \"%@\""
- "timeIntervalSinceDate:"
- "transaction"
- "trigger downgrade from gen8"
- "unable to map %s (errno %d)"
- "unable to open %@ (errno %d)"
- "unable to unmap current update %ld bytes at %p (error %d)"
- "unable to write %s (error %d)"
- "update finished at %@ (took %f) with version: %d"
- "update started at %@: version=%d"
- "update-current"
- "updateDb:forceVersion:"
- "updateNowFromServer:version:forceVersion:queue:"
- "updateScheduled"
- "update_check"
- "updating db schema from v%lld to v%lld"
- "v16@?0^{__SecRevocationDb=^{__OpaqueSecDb}^{dispatch_queue_s}BBB^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}^{__CFArray}^{__CFDictionary}{os_unfair_lock_s=I}}8"
- "v28@0:8q16B24"
- "vacuum not needed page_count: %lld free_count: %lld loadFactor: %f"
- "valid generation received %ld is different from requested %ld"
- "valid-downgrade"
- "validUpdateConfiguration:"
- "writeData:"
- "writeToFile:atomically:"
- "writer"

```
