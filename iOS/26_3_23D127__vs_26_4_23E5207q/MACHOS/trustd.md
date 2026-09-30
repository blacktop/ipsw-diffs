## trustd

> `/usr/libexec/trustd`

```diff

-61901.80.25.0.0
-  __TEXT.__text: 0x63a0c
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x2ee0
-  __TEXT.__objc_methlist: 0xc5c
-  __TEXT.__const: 0x5c81
-  __TEXT.__gcc_except_tab: 0xca4
-  __TEXT.__cstring: 0x70d1
-  __TEXT.__oslogstring: 0x6029
-  __TEXT.__objc_classname: 0x194
-  __TEXT.__objc_methname: 0x2daa
-  __TEXT.__objc_methtype: 0xaf6
-  __TEXT.__unwind_info: 0x10b8
-  __DATA_CONST.__auth_got: 0x1228
-  __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x4cd8
-  __DATA_CONST.__cfstring: 0x6480
-  __DATA_CONST.__objc_classlist: 0x70
+61901.100.267.0.2
+  __TEXT.__text: 0x6879c
+  __TEXT.__auth_stubs: 0x23f0
+  __TEXT.__objc_stubs: 0x3120
+  __TEXT.__objc_methlist: 0xd54
+  __TEXT.__const: 0x5cb1
+  __TEXT.__dlopen_cstrs: 0x54
+  __TEXT.__gcc_except_tab: 0xc90
+  __TEXT.__cstring: 0x7387
+  __TEXT.__oslogstring: 0x66a1
+  __TEXT.__objc_classname: 0x1b1
+  __TEXT.__objc_methname: 0x3045
+  __TEXT.__objc_methtype: 0xc64
+  __TEXT.__unwind_info: 0x1168
+  __DATA_CONST.__auth_got: 0x1208
+  __DATA_CONST.__got: 0x7c0
+  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__const: 0x4ee0
+  __DATA_CONST.__cfstring: 0x6860
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_dictobj: 0x190
-  __DATA.__objc_const: 0x14e0
-  __DATA.__objc_selrefs: 0xd68
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__objc_data: 0x460
-  __DATA.__data: 0x3c0
-  __DATA.__bss: 0x520
+  __DATA.__objc_const: 0x1740
+  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_data: 0x4b0
+  __DATA.__data: 0x420
+  __DATA.__bss: 0x540
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6A772E3E-9F30-3112-9134-4D32B964ADF5
-  Functions: 1282
-  Symbols:   843
-  CStrings:  3069
+  UUID: EE78D558-2744-3091-9F77-1B3B7CC5411C
+  Functions: 1337
+  Symbols:   841
+  CStrings:  3224
 
Symbols:
+ _OBJC_CLASS_$_NSHashTable
+ __sl_dlopen
+ _abort_report_np
+ _clock_gettime_nsec_np
+ _dlerror
+ _dlsym
+ _kSecTrustInfoRevocationInfoKey
+ _objc_copyStruct
+ _os_unfair_lock_trylock
+ _write
+ _xpc_dictionary_get_int64
- _SecCRLiteGetCoverageInfo
- _atol
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _pthread_mutex_destroy
- _pthread_mutex_init
- _pthread_mutexattr_destroy
- _pthread_mutexattr_init
- _pthread_mutexattr_setpolicy_np
CStrings:
+ "\""
+ ","
+ "@\"NSHashTable\""
+ "@32@0:8r^{?=*Q}16^{?=*Q}24"
+ "@40@0:8@16^{?=*Q}24@32"
+ "@40@0:8r^{?=*Q}16^{?=*Q}24^{policy_set={?=*Q}^{policy_set}}32"
+ "B16@?0@\"NSObject<OS_policy_node>\"8"
+ "B16@?0^{__OpaqueSecDbConnection={__CFRuntimeBase=QAQ}^{__OpaqueSecDb}BBQBiB^{__CFError}^{sqlite3}i^{__CFArray}}8"
+ "B44@0:8@16q24B32@36"
+ "CRLite result not being enforced (revoked=%d), falling back to Valid"
+ "Next update time: %f"
+ "OS_policy_node"
+ "Reader attempting to acquire lock starting from index %d"
+ "Reader no locks available, waiting on lock[%d]"
+ "Reader releasing lock[%d]"
+ "Reader successfully acquired lock[%d]"
+ "Reader successfully acquired lock[%d] (after waiting)"
+ "Reader successfully released lock[%d]"
+ "SELECT COUNT(*) FROM pragma_table_info('groups') WHERE name = 'policies'"
+ "SELECT filterid,generatedat FROM crlitefiltercoverage WHERE logid=?1 AND ?2 >= start AND ?2 <= end ORDER BY generatedat DESC LIMIT 1"
+ "SecCRLiteCopyCoverageInfo"
+ "SecDbConnectionAcquireRefMigrationSafe: acquired %s connection with index %d"
+ "SecDbConnectionAcquireRefMigrationSafe: acquiring %s connection%s"
+ "SecDbConnectionAcquireRefMigrationSafe: failed to get connection, releasing acquired lock"
+ "SecDbConnectionAcquireRefMigrationSafe: stored lock index %d in %s connection %p"
+ "SecDbConnectionAcquireRefMigrationSafe: successfully acquired %s connection %p with lock index %d"
+ "SecDbConnectionRelease: releasing %s connection %p with lock index %d"
+ "SecDbCreate: initializing %zu reader locks and 1 writer lock supporting priority donation"
+ "SecDbCreate: successfully initialized separated locking system with %zu reader locks and 1 writer lock"
+ "T@\"NSHashTable\",&,V_parents"
+ "T@\"NSMutableArray\",&,V_children"
+ "TB,V_forceVersion"
+ "T^{?=*Q},V_qualifier_set"
+ "T^{policy_set={?=*Q}^{policy_set}},V_expected_policy_set"
+ "Tq,V_version"
+ "T{?=*Q},V_valid_policy"
+ "Update received: v%ld"
+ "UsePolicyGraphVerifier"
+ "Writer attempting to acquire writer lock"
+ "Writer releasing writer lock"
+ "Writer successfully acquired writer lock"
+ "Writer successfully released writer lock"
+ "^{?=*Q}"
+ "^{?=*Q}16@0:8"
+ "^{policy_set={?=*Q}^{policy_set}}"
+ "^{policy_set={?=*Q}^{policy_set}}16@0:8"
+ "_SecRevocationDbUpdateSchema failed: no DBC"
+ "_SecTrustSettingsSetData: _writeEmptyTrustSettingsFile failure"
+ "_SecTrustSettingsSetData: _writeFile failure"
+ "_children"
+ "_expected_policy_set"
+ "_forceVersion"
+ "_parents"
+ "_qualifier_set"
+ "_valid_policy"
+ "_version"
+ "_writeFile: short write (%ld)"
+ "allowed"
+ "anchorHash"
+ "certHash"
+ "checkOCSP"
+ "checking revocation"
+ "checking revocation for cert: %ld"
+ "children"
+ "com.apple.security.file./Library/Caches/com.apple.xbs/976818CC-C13D-4FFB-9873-5EC4FBE1A043/TemporaryDirectory.mkgcly/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
+ "componentsJoinedByString:"
+ "crlite"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "db vacuum couldn't format string"
+ "expected_policy_set"
+ "forceVersion"
+ "found CRLite info for cert: %ld"
+ "generationUsed"
+ "hasDateConstraints"
+ "hasNameConstraints"
+ "hasPolicyConstraints"
+ "https://%@/o%ld/v%ld"
+ "initWithOid:qualifier:"
+ "initWithOid:qualifier:expected_policies:"
+ "initWithOid:qualifier:expected_policy_set:"
+ "isDefinitive"
+ "isOnList"
+ "isRevoked"
+ "issuerHash"
+ "knownOnly"
+ "nameConstraints"
+ "noCACheck"
+ "node<%p> (%@) p:%@ c:%@"
+ "notAfterDate"
+ "notBeforeDate"
+ "parents"
+ "policyConstraints"
+ "policy_node"
+ "policy_node_t<%p>"
+ "possibly "
+ "processing CRLLite section"
+ "q16@0:8"
+ "qualifier_set"
+ "reader"
+ "requireCT"
+ "revoked"
+ "rvc: %s%s cert %ld (will check OCSP)"
+ "rvc: definitely %s cert %ld"
+ "setChildren:"
+ "setExpected_policy_set:"
+ "setForceVersion:"
+ "setParents:"
+ "setQualifier_set:"
+ "setValid_policy:"
+ "setVersion:"
+ "setWithObject:"
+ "skipping revocation checks for no-check cert: %ld"
+ "softlink:o:path:/System/Library/PrivateFrameworks/SwiftCRLite.framework/SwiftCRLite"
+ "starting to process full update; clearing database"
+ "thisUpdate"
+ "trustList"
+ "trustVersion"
+ "update finished at %@ (took %f) with version: %d"
+ "update started at %@: version=%d"
+ "updateDb:forceVersion:"
+ "updateNowFromServer:version:forceVersion:queue:"
+ "updating db schema from v%lld to v%lld"
+ "v24@0:8^{?=*Q}16"
+ "v24@0:8^{policy_set={?=*Q}^{policy_set}}16"
+ "v28@0:8q16B24"
+ "v32@0:8{?=*Q}16"
+ "vacuum complete"
+ "vacuum not needed page_count: %lld free_count: %lld loadFactor: %f"
+ "vacuum pages_to_free: %lld  page_count: %lld free_count: %lld loadFactor: %f"
+ "vacuum too close to boot: %lld page_count: %lld free_count: %lld loadFactor: %f"
+ "valid_policy"
+ "versionUsed"
+ "weakObjectsHashTable"
+ "writer"
+ "{?=\"data\"*\"length\"Q}"
+ "{?=*Q}16@0:8"
- "B16@?0^{__OpaqueSecDbConnection={__CFRuntimeBase=QAQ}^{__OpaqueSecDb}BBQBiB^{__CFError}^{sqlite3}^{__CFArray}}8"
- "CRLite result not being enforced, falling back to Valid"
- "SELECT * FROM crlitefiltercoverage WHERE logid=?1 AND ?2 >= start AND ?2 <= end ORDER BY generatedat DESC LIMIT 1"
- "SecDb: SecDbCreate failed to create attributes for the write mutex; fairness properties are no longer present"
- "SecDb: SecDbCreate failed to init the write mutex, this will end badly"
- "cStringUsingEncoding:"
- "com.apple.security.file./Library/Caches/com.apple.xbs/Sources/Security_executables_core/trust/trustd/OTAAutoAssetClient.m"
- "q24@0:8@16"
- "step[%d]: %s returned SQLITE_ROW with NULL row block"
- "taskDescription"
- "update finished at %@ (took %f)"
- "update started at %@"
- "updateDb:"
- "updateNowFromServer:version:queue:"
- "versionFromTask:"

```
