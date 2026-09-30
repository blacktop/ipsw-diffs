## online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0x34714
-  __TEXT.__auth_stubs: 0x1d80
-  __TEXT.__objc_stubs: 0xfc0
-  __TEXT.__objc_methlist: 0x304
-  __TEXT.__const: 0x223c
-  __TEXT.__cstring: 0x2ff7
-  __TEXT.__gcc_except_tab: 0x3f8
-  __TEXT.__objc_methname: 0x11a5
-  __TEXT.__oslogstring: 0x1dae
-  __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methtype: 0x212
+463.0.4.0.0
+  __TEXT.__text: 0x41c1c
+  __TEXT.__auth_stubs: 0x1e80
+  __TEXT.__objc_stubs: 0x17a0
+  __TEXT.__objc_methlist: 0x77c
+  __TEXT.__const: 0x226c
+  __TEXT.__cstring: 0x4557
+  __TEXT.__gcc_except_tab: 0x4d4
+  __TEXT.__objc_methname: 0x1c9b
+  __TEXT.__oslogstring: 0x37cb
+  __TEXT.__objc_classname: 0xd5
+  __TEXT.__objc_methtype: 0x381
   __TEXT.__dlopen_cstrs: 0x12c
-  __TEXT.__swift5_typeref: 0x8b9
-  __TEXT.__swift5_capture: 0x2bc
+  __TEXT.__swift5_typeref: 0x907
+  __TEXT.__swift5_capture: 0x5e8
   __TEXT.__constg_swiftt: 0xbfc
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x18

   __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x168
-  __TEXT.__unwind_info: 0xdb0
-  __TEXT.__eh_frame: 0x12bc
-  __DATA_CONST.__auth_got: 0xed0
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__auth_ptr: 0x440
-  __DATA_CONST.__const: 0x22c8
-  __DATA_CONST.__cfstring: 0xc00
-  __DATA_CONST.__objc_classlist: 0x70
-  __DATA_CONST.__objc_protolist: 0x28
+  __TEXT.__unwind_info: 0xfc0
+  __TEXT.__eh_frame: 0x1400
+  __DATA_CONST.__auth_got: 0xf50
+  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__auth_ptr: 0x458
+  __DATA_CONST.__const: 0x25a0
+  __DATA_CONST.__cfstring: 0x1560
+  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xce0
-  __DATA.__objc_selrefs: 0x6c0
-  __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0x2e0
-  __DATA.__data: 0x1668
-  __DATA.__bss: 0x3090
-  __DATA.__common: 0xe8
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0x1410
+  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_data: 0x4c0
+  __DATA.__data: 0x1688
+  __DATA.__bss: 0x30a0
+  __DATA.__common: 0x118
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
   - /System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1BB5D389-D525-3A8D-9314-D9C72C48CBEA
-  Functions: 1128
-  Symbols:   426
-  CStrings:  930
+  UUID: FD596C94-9848-332D-B0C7-0930EDDDD256
+  Functions: 1364
+  Symbols:   447
+  CStrings:  1315
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDictionaryCreate
+ _CFEqual
+ _CFURLCreateWithFileSystemPath
+ _MISEntitlementDictionaryAllowsEntitlementValue
+ _MISProfileCreateDataRepresentation
+ _MISProfileCreateWithData
+ _MISProfileGetValue
+ _MISProfileIsDEREncoded
+ _MISProfileValidateSignature
+ _MISProvisioningProfileGetDeveloperCertificatesHashes
+ _MISProvisioningProfileGetEmbeddedDER
+ _MISProvisioningProfileGetEntitlements
+ _MISProvisioningProfileGetExpirationDate
+ _MISProvisioningProfileGetName
+ _MISProvisioningProfileGetTeamIdentifier
+ _MISProvisioningProfileGetTeamName
+ _MISProvisioningProfileGetUUID
+ _MISProvisioningProfileIsAppleInternalProfile
+ _MISProvisioningProfileIsForBetaDeployment
+ _MISProvisioningProfileIsForLocalProvisioning
+ _MISProvisioningProfileProvisionsAllDevices
+ _MISProvisioningProfileValidateSignature
+ _MISValidateSignatureAndCopyInfo
+ _MISXMLProvisioningProfileGetDeveloperCertificates
+ _OBJC_CLASS_$_MISOnlineAuthEntry
+ _OBJC_CLASS_$_MISProfileDBClient
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_METACLASS_$_MISOnlineAuthEntry
+ _SecCertificateCopySubjectSummary
+ _SecCertificateCreateWithData
+ _SecCodeSetDetachedSignature
+ _SecStaticCodeCreateWithPathAndAttributes
+ _TMGetKernelMonotonicClock
+ _TMGetRTCResetCount
+ ___kCFBooleanTrue
+ _kCFTypeDictionaryKeyCallBacks
+ _kCFTypeDictionaryValueCallBacks
+ _kMISValidationInfoCdHash
+ _kSecCodeAttributeUniversalFileOffset
+ _kSecCodeInfoUnique
+ _objc_getProperty
+ _objc_retain_x3
+ _objc_setProperty_atomic
+ _objc_setProperty_nonatomic_copy
+ _objc_storeWeak
+ _sqlite3_bind_int
+ _sqlite3_bind_parameter_index
+ _sqlite3_column_int
+ _sqlite3_errstr
- _CFArrayCreate
- _CFArrayGetTypeID
- _CFDataCreateWithBytesNoCopy
- _CFNumberGetTypeID
- _CFNumberGetValue
- _CFPropertyListCreateWithStream
- _CFReadStreamCreateWithFile
- _CFReadStreamOpen
- _MISExistsIndeterminateApps
- _MISValidateSignature
- _NSLog
- _OBJC_CLASS_$_CKRecord
- _OBJC_CLASS_$_LSApplicationWorkspace
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_OS_os_log
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL_1_HOUR
- _XPC_ACTIVITY_INTERVAL_8_HOURS
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- _kCFTypeArrayCallBacks
- _xpc_activity_unregister
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
CStrings:
+ "\x1f"
+ "%@%@%@"
+ "%@%@%lld"
+ "(%lu,@p%lu)"
+ "*"
+ ","
+ "/Library/MobileDevice/ProvisioningProfiles"
+ "1"
+ "2"
+ "243LU875E5"
+ "3"
+ "4"
+ "5"
+ "6"
+ "7"
+ "8"
+ "9"
+ "@\"MISDBManager\""
+ "@\"MISEntitlementsModel\""
+ "@\"MISProfileModel\""
+ "@\"NSData\""
+ "@\"NSDate\""
+ "@\"NSString\""
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8@16@24"
+ "@32@0:8^{sqlite3_stmt=}16@24"
+ "@60@0:8@16@24i32q36q44B52B56"
+ "@64@0:8@16@24@32@40C48C52C56C60"
+ "@cert"
+ "@cms_blob"
+ "@expires"
+ "@is_apple_internal"
+ "@is_beta"
+ "@is_der"
+ "@is_for_all_devices"
+ "@is_local"
+ "@leaf_pk"
+ "@name"
+ "@p%u"
+ "@predicate"
+ "@signing_identity"
+ "@team_id"
+ "@team_name"
+ "@totalPredicates"
+ "@uuid"
+ "@wildcard"
+ "ALTER TABLE profiles ADD COLUMN is_der INTEGER DEFAULT (0)"
+ "Adding launch warning mark to: %{public}s"
+ "App revalidation: CDHash missing for %@"
+ "App revalidation: Failed to validate app %{public}@, 0%x"
+ "AppAudience"
+ "AppleInternal"
+ "AppleInternalProfile"
+ "Authorized: %{public}@, %{public}@"
+ "B32@0:8@16^@24"
+ "B32@0:8q16q24"
+ "B36@0:8@16B24@?28"
+ "B36@0:8@16i24^@28"
+ "B40@0:8@16@24^@32"
+ "B40@0:8q16@24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B60@0:8@16@24i32q36q44^@52"
+ "Base asset had invalid payload: %{public}s"
+ "Base asset record changed: %{public}@"
+ "Base asset record error: %@, %{public}s"
+ "Base asset sync with token: %{public}s"
+ "Base sync completion error: %{public}s"
+ "Beta"
+ "BoxedMISProfile"
+ "C"
+ "C16@0:8"
+ "CREATE TABLE IF NOT EXISTS banned_cdhashes (  cdhash BLOB NOT NULL )"
+ "CREATE TABLE IF NOT EXISTS banned_profile_uuids (  uuid TEXT NOT NULL )"
+ "CREATE TABLE IF NOT EXISTS online_auth (  uuid TEXT NOT NULL,  cdhash BLOB NOT NULL,  grace_period INT NOT NULL,  last_success_monotonic_time INT NOT NULL,  last_success_reset_count INT NOT NULL,  is_rejected INT NOT NULL DEFAULT (0),  is_rejected_by_whole_profile INT NOT NULL DEFAULT (0),  PRIMARY KEY (uuid, cdhash),  CONSTRAINT fk_online_auth_profile_uuid    FOREIGN KEY (uuid)    REFERENCES profiles(uuid)    ON DELETE CASCADE )"
+ "CREATE TABLE IF NOT EXISTS signing_identities ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, signing_identity TEXT NOT NULL, UNIQUE(uuid, signing_identity), CONSTRAINT fk_signing_identity_profile_uuid  FOREIGN KEY (uuid)  REFERENCES profiles(uuid)   ON DELETE CASCADE )"
+ "CREATE TABLE IF NOT EXISTS team_id_info ( team_id TEXT NOT NULL, team_name TEXT NOT NULL,  PRIMARY KEY (team_id) )"
+ "CREATE TABLE IF NOT EXISTS trusted_team_ids ( team_id TEXT PRIMARY KEY, signature BLOB )"
+ "CREATE TABLE certificate_provisioning_cache ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, leaf_pk INTEGER NOT NULL, UNIQUE(uuid, leaf_pk), CONSTRAINT fk_certificate_leaf  FOREIGN KEY (leaf_pk)  REFERENCES certificates(pk)  ON DELETE CASCADE, CONSTRAINT fk_cert_profile_uuid  FOREIGN KEY (uuid)  REFERENCES profiles(uuid)   ON DELETE CASCADE )"
+ "CREATE TABLE certificates ( pk INTEGER PRIMARY KEY AUTOINCREMENT, leaf BLOB UNIQUE NOT NULL)"
+ "CREATE TABLE entitlements_provisioning_cache ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, predicate TEXT NOT NULL, wildcard INTEGER NOT NULL, UNIQUE(uuid, predicate), CONSTRAINT fk_predicate_profile_uuid  FOREIGN KEY (uuid)  REFERENCES profiles(uuid)   ON DELETE CASCADE )"
+ "CREATE TABLE profiles ( uuid TEXT NOT NULL PRIMARY KEY, team_id TEXT NOT NULL, install_time TEXT DEFAULT CURRENT_TIMESTAMP, name TEXT NOT NULL, expires INTEGER, is_for_all_devices INTEGER, is_apple_internal INTEGER, is_local INTEGER, is_beta INTEGER, cms_blob BLOB NOT NULL)"
+ "CREATE TABLE xml_profiles_cache ( uuid TEXT NOT NULL PRIMARY KEY, cms_blob BLOB NOT NULL, CONSTRAINT fk_xml_profile_cache_uuid  FOREIGN KEY (uuid)  REFERENCES profiles(uuid)   ON DELETE CASCADE )"
+ "CREATE UNIQUE INDEX certificate_leaf_index ON certificates (leaf)"
+ "CREATE UNIQUE INDEX entitlements_cache_index ON entitlements_provisioning_cache (uuid, predicate)"
+ "CloudKit asset doesn't have a file URL: %{public}@"
+ "CloudKit fetch for warning: %{public}s"
+ "CloudKit record has invalid algorithm: %{public}@"
+ "CloudKit record has invalid bitsPerEntry count: %{public}@"
+ "CloudKit record has invalid data: %{public}@"
+ "CloudKit record has invalid details zone: %{public}@"
+ "CloudKit record has invalid entryCount: %{public}@"
+ "CloudKit record has invalid flags field: %s"
+ "CloudKit record has invalid id: %{public}@"
+ "CloudKit record has invalid payload field: %{public}@"
+ "CloudKit record has invalid reason field: %s"
+ "CloudKit record has invalid salt: %{public}@"
+ "CloudKit record has invalid size: %@, privacy: .public"
+ "CloudKit record has invalid update number: %{public}@"
+ "CloudKit record has invalid update zone: %{public}@"
+ "CloudKit record has invalid uuid: %{public}@"
+ "CloudKit unexpected error during fetch: %{public}s"
+ "Could not convert JSON to Dictionary: %{public}@"
+ "Could not convert dictionary to JSON: %{public}@"
+ "Could not copy code directory hash."
+ "Could not copy signature, error 0x%x"
+ "Could not perform authorization attempt"
+ "Couldn't add is_der to the profiles table: %s"
+ "Couldn't create SecCertificate for %@"
+ "Couldn't create certificates index: %s"
+ "Couldn't create certificates provisioning cache: %s"
+ "Couldn't create certificates table: %s"
+ "Couldn't create entitlements index: %s"
+ "Couldn't create entitlements provisioning cache: %s"
+ "Couldn't create profiles table: %s"
+ "Couldn't create the banned cdhashes table: %s"
+ "Couldn't create the banned profile UUIDs table: %s"
+ "Couldn't create the online auth table: %s"
+ "Couldn't create the signing identities table: %s"
+ "Couldn't create the team ID info table: %s"
+ "Couldn't create the trusted team IDs table: %s"
+ "Couldn't create the xml profiles table: %s"
+ "Couldn't fetch single asterisk wildcard predicates: %s"
+ "Couldn't fetch trusted signing identities from profiles: %s"
+ "Couldn't fetch trusted signing identities from xml_profiles_cache: %s"
+ "Couldn't fetch trusted team ID info: %s"
+ "Couldn't get device identity %{public}@"
+ "Couldn't get signing identity for %@"
+ "Couldn't insert into signing identities: %s"
+ "Couldn't insert new types for single asterisk wildcard predicates: %s"
+ "Couldn't insert team ID info: %s"
+ "Couldn't replace signature with nil: %s"
+ "Couldn't update is_beta column: %s"
+ "Created launch warning entry: %{public}llu"
+ "Critical SQLite error, could not checkpoint"
+ "DB being loaded from %{public}@"
+ "DELETE FROM online_auth WHERE cdhash = ?1"
+ "DELETE FROM online_auth WHERE uuid = ?1 AND cdhash = ?2"
+ "DER-Encoded-Profile"
+ "DeveloperCertificates"
+ "Encountered a non-boolean value for 'PPQCheck'."
+ "Entitlements"
+ "Error authorizing entry for %{public}@, %{public}@, %d, %{public}@"
+ "Error banning cdhash %{public}@, %{public}@"
+ "Error banning profile %{public}@, %{public}@"
+ "Error counting cdhashes rejected by profile %{public}s"
+ "Error creating new launch warning for %{public}s"
+ "Error deleting online auth entry %{public}s"
+ "Error deleting online auth entry %{public}s, %{public}s"
+ "Error getting online auth entries: %{public}@"
+ "Error getting online auth entry %{public}s, %{public}s"
+ "Error processing app: %s, %s"
+ "Error recording indeterminate entry %{public}s, %{public}s, %{bool}d"
+ "Error rejecting entry for %{public}@, %{public}@, %{public}@"
+ "Error rejecting profile for %{public}@, %{public}@, %{public}@"
+ "Error searching for zero length signatures: %s"
+ "Error setting grace period for %{public}s, %d"
+ "ExpirationDate"
+ "Expires"
+ "Failed to add launch warning mark with no error: %s"
+ "Failed to add launch warning mark: %{public}s, %{public}@"
+ "Failed to install document checker: %{public}@"
+ "Failed to terminate app: %s"
+ "Failed to terminate app: %{public}s"
+ "Failure creating static code: %d"
+ "Failure setting detached signature: %d"
+ "Finalize error (%d) on query: %{public}@"
+ "Found launch warning for %{public}s with details: %{public}s"
+ "Found launch warning with details: %{public}s"
+ "Found no launch warning for %{public}s"
+ "Found no launch warning for cdhash: %u, %s"
+ "Full JSON message to send: %{public}s"
+ "Get launch warning data failed: %{public}@"
+ "Got updated base sync token: %{public}s"
+ "Got updated update sync token: %{public}s"
+ "INSERT INTO banned_cdhashes (cdhash)\nVALUES (?1)\nON CONFLICT DO NOTHING"
+ "INSERT INTO banned_profile_uuids (uuid)\nVALUES (?1)\nON CONFLICT DO NOTHING"
+ "INSERT INTO certificate_provisioning_cache VALUES (NULL, @uuid, @leaf_pk)"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 0, 0)\n"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 1, ?3)\nON CONFLICT(uuid, cdhash) DO UPDATE SET\n    is_rejected = 1,\n    is_rejected_by_whole_profile = ?3"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)\nON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = ?3,\n    last_success_monotonic_time = ?4,\n    last_success_reset_count = ?5,\n    is_rejected = ?6,\n    is_rejected_by_whole_profile = ?7"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?3, ?4, ?5, ?1, ?2, 0, 0)\nON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = ?5,\n    last_success_monotonic_time = ?1,\n    last_success_reset_count = ?2,\n    is_rejected = 0,\n    is_rejected_by_whole_profile = 0"
+ "INSERT INTO profiles VALUES (@uuid, @team_id, NULL, @name, @expires, @is_for_all_devices, @is_apple_internal, @is_local, @is_beta, @cms_blob, @is_der)"
+ "INSERT INTO team_id_info VALUES (@team_id, @team_name)"
+ "INSERT INTO team_id_info VALUES (@team_id, @team_name) ON CONFLICT DO NOTHING"
+ "INSERT INTO xml_profiles_cache VALUES (@uuid, @cms_blob)"
+ "INSERT OR IGNORE INTO certificates VALUES (NULL, @cert)"
+ "INSERT OR IGNORE INTO entitlements_provisioning_cache (uuid, predicate, wildcard) VALUES (?1, ?2, 1)"
+ "INSERT OR IGNORE INTO entitlements_provisioning_cache VALUES (NULL, @uuid, @predicate, @wildcard)"
+ "INSERT OR IGNORE INTO signing_identities VALUES (NULL, @uuid, @signing_identity)"
+ "InternalBuild"
+ "Invalid signature for %{public}s record %{public}s"
+ "Item not present in bloom filter: %u, %{public}s"
+ "Launch warning found: %u, %{public}s"
+ "Launch warning has unknown reason and flags indicate to ignore: %u, %{public}s"
+ "Local"
+ "LocalProvision"
+ "Looking up launch warning for cdhash: %u, %{public}s"
+ "MISDBManager"
+ "MISEntitlementsModel"
+ "MISOnlineAuthEntry"
+ "MISOnlineAuthEntry(%@, %@, gracePeriod: %i, lastSuccessMonotonicTime: %lli, lastSuccessResetCount: %lli, isRejected: %i, isRejectedByWholeProfile: %i)"
+ "MISProfileModel"
+ "MISQL: null version, potential erase or upgrade"
+ "MISQL: performing database migration 1 -> 2"
+ "MISQL: performing database migration 2 -> 3"
+ "MISQL: performing database migration 3 -> 4"
+ "MISQL: performing database migration 4 -> 5"
+ "MISQL: performing database migration 5 -> 6"
+ "MISQL: performing database migration 6 -> 7"
+ "MISQL: performing database migration 7 -> 8"
+ "MISQL: performing database migration 8 -> 9"
+ "Merging in bloom filter update: %lld for filter %{public}s"
+ "Migrating team ID info: Unable to create profile for %@"
+ "Migration: Couldn't create SecCertificate for %@"
+ "Migration: Unable to create profile for %@"
+ "Migration: Unable to get signing identity from %@"
+ "Missing signature for %{public}s record %{public}s"
+ "NSCopying"
+ "Name"
+ "No launch warning present: %u, %{public}s"
+ "Not MSCMSSignedData: %{public}@"
+ "ON CONFLICT(uuid, cdhash) DO NOTHING"
+ "ON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = 0,\n    last_success_monotonic_time = -1,\n    last_success_reset_count = -1"
+ "OnlineAuthorizationOnAllMatchingProfiles"
+ "PPQCheck"
+ "Performing auth request for: %{public}@, %{public}@, %{public}@"
+ "Permanently rejected profile: %{public}@, %{public}@"
+ "Prepare error (%d) on query: %{public}@"
+ "Profiles"
+ "ProvisionsAllDevices"
+ "Pruning online auth entry: %{public}@"
+ "Rejected app/profile combination: %{public}@, %{public}@"
+ "Rejected profile: %{public}@, %{public}@"
+ "Removing old bloom filter: %{public}s"
+ "Revalidating apps"
+ "SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth"
+ "SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth\nWHERE uuid = ?1 AND cdhash = ?2"
+ "SELECT COUNT(*)\nFROM online_auth\nWHERE uuid =  ?1 AND is_rejected = 1 AND is_rejected_by_whole_profile = 1"
+ "SELECT cms_blob FROM profiles WHERE is_der = 0"
+ "SELECT cms_blob FROM profiles WHERE uuid = @uuid"
+ "SELECT cms_blob FROM xml_profiles_cache WHERE uuid = @uuid"
+ "SELECT cms_blob as blob FROM xml_profiles_cache"
+ "SELECT pk FROM certificates WHERE leaf = @cert"
+ "SELECT profiles.team_id, profiles.cms_blob, profiles.uuid FROM profiles"
+ "SELECT team_id, signature FROM trusted_team_ids"
+ "SELECT uuid FROM certificate_provisioning_cache JOIN certificates ON certificates.pk = leaf_pk WHERE certificates.leaf = @cert"
+ "SELECT uuid FROM profiles"
+ "SELECT uuid FROM profiles WHERE uuid = @uuid"
+ "SELECT uuid, cms_blob FROM profiles WHERE is_der = 0 AND (is_for_all_devices = 1 OR is_local = 1)"
+ "SELECT uuid, predicate FROM entitlements_provisioning_cache WHERE predicate LIKE 'string%' || x'1f' || '*' AND wildcard = 1"
+ "SELECT uuid, team_id, name, expires, is_for_all_devices, is_apple_internal, is_local, is_beta FROM profiles"
+ "SELECT xml_profiles_cache.uuid, xml_profiles_cache.cms_blob FROM xml_profiles_cache LEFT JOIN profiles ON profiles.uuid = xml_profiles_cache.uuid WHERE profiles.is_for_all_devices = 1 OR profiles.is_local = 1"
+ "SQL error '%{public}s' (%1d)"
+ "Sending request for %{public}@, %{public}@"
+ "Set launch warning override failed: %{public}@"
+ "Setting up new base filter: %{public}s"
+ "Setting user override: %llu to %{bool}d"
+ "Signature validation error: %{public}@"
+ "Signing JSON message for %{public}@, %{public}@"
+ "Starting sync of zone: %{public}s"
+ "Step error (%d) on query: %{public}@"
+ "Successfully terminated app: %{public}s"
+ "Sync error: %{public}s"
+ "T@\"MISEntitlementsModel\",&,VEntitlements"
+ "T@\"MISProfileModel\",&,VProfiles"
+ "T@\"NSData\",C,N,V_cdHash"
+ "T@\"NSDate\",&,VExpires"
+ "T@\"NSString\",&,VName"
+ "T@\"NSString\",&,VTeamID"
+ "T@\"NSString\",&,VUUID"
+ "T@\"NSString\",C,N,V_profileUUID"
+ "TB,N,V_isRejected"
+ "TB,N,V_isRejectedByWholeProfile"
+ "TC,VAppleInternal"
+ "TC,VBeta"
+ "TC,VLocal"
+ "TC,VProvisionsAllDevices"
+ "TeamID"
+ "TeamIdentifier"
+ "TeamName"
+ "Terminating app: %{public}s"
+ "The server returned: %{public}s"
+ "Ti,N,V_gracePeriod"
+ "Tq,N,V_lastSuccessMonotonicTime"
+ "Tq,N,V_lastSuccessResetCount"
+ "UPDATE online_auth SET grace_period = ?2\nWHERE uuid = ?1"
+ "UPDATE online_auth SET last_success_monotonic_time = last_success_monotonic_time + ?1 "
+ "UPDATE online_auth SET last_success_reset_count = last_success_reset_count + ?1 "
+ "UPDATE profiles SET is_beta = 1 WHERE uuid = @uuid"
+ "UPDATE trusted_team_ids SET signature = NULL WHERE team_id = ?1"
+ "UUID"
+ "Unable to add launch warning to app without installation ID: %{public}s"
+ "Unable to create code object (%d) for: %{public}s"
+ "Unable to create signing info (%d) for: %{public}s"
+ "Unable to find cdhash for %{public}s"
+ "Unable to get best cdhash data: %{public}s"
+ "Unable to get best cdhash digest algorithm: %{public}s"
+ "Unable to get full cdhash information for: %{public}s"
+ "Unable to look up launch warning info for ID: %llu"
+ "Unable to read CloudKit asset file URL: %{public}s"
+ "Unable to statfs app: %d, %{public}s"
+ "Unable to table row count for %{public}@: %d"
+ "Update asset had incorrect ID: %{public}s, %{public}s"
+ "Update asset had invalid compression type: %{public}s"
+ "Update entry sync error: %{public}s"
+ "Update sync completion error: %{public}s"
+ "Update sync error: %{public}s"
+ "Update zone record changed: %{public}@"
+ "Update zone sync with token: %{public}s"
+ "Using emulated device UDID: %{public}@\n"
+ "Visiting application: %{public}s"
+ "WHERE cdhash = ?2"
+ "WITH filteredProfileUUIDs(uuid) AS (%@) SELECT profiles.uuid, profiles.team_id, profiles.name, profiles.expires, profiles.is_for_all_devices, profiles.is_apple_internal, profiles.is_local, profiles.is_beta, profiles.is_der FROM filteredProfileUUIDs JOIN profiles ON profiles.uuid = filteredProfileUUIDs.uuid ORDER BY  profiles.is_der DESC, profiles.is_local ASC, profiles.is_for_all_devices ASC"
+ "WITH predicates(idx, predicate) AS (VALUES %@), filteredProfileUUIDs(uuid) AS (%@) SELECT * FROM (SELECT profiles.uuid, profiles.team_id, profiles.name, profiles.expires, profiles.is_for_all_devices, profiles.is_apple_internal, profiles.is_local, profiles.is_beta, profiles.is_der, COUNT(DISTINCT predicates.idx) as matchCount FROM filteredProfileUUIDs JOIN profiles ON profiles.uuid = filteredProfileUUIDs.uuid JOIN entitlements_provisioning_cache ON entitlements_provisioning_cache.uuid = filteredProfileUUIDs.uuid CROSS JOIN predicates WHERE profiles.is_apple_internal OR ((entitlements_provisioning_cache.wildcard = 0 AND entitlements_provisioning_cache.predicate = predicates.predicate) OR (entitlements_provisioning_cache.wildcard = 1 AND glob(entitlements_provisioning_cache.predicate, predicates.predicate) )) GROUP BY profiles.uuid, profiles.is_apple_internal) AS aggregated WHERE aggregated.matchCount = @totalPredicates OR aggregated.is_apple_internal ORDER BY  aggregated.is_der DESC, aggregated.is_local ASC, aggregated.is_for_all_devices ASC"
+ "XPC: checking launch warning data for: %llu, %{public}@"
+ "XPC: launch warning data response: %{public}@, %lu"
+ "^v24@0:8@16"
+ "_cdHash"
+ "_gracePeriod"
+ "_isRejected"
+ "_isRejectedByWholeProfile"
+ "_lastSuccessMonotonicTime"
+ "_lastSuccessResetCount"
+ "_profileUUID"
+ "_weak_db"
+ "addMonotonicTimeOffset:cdHash:error:"
+ "addRTCResetCountOffset:cdHash:error:"
+ "allCMSBlobs"
+ "allProfiles"
+ "allocWithZone:"
+ "appendFormat:"
+ "appendString:"
+ "arrayWithCapacity:"
+ "authorizeEntryWithProfileUUID:cdHash:gracePeriod:currentMonotonicTime:currentResetCount:error:"
+ "banCDHash:error:"
+ "banProfileUUID:error:"
+ "beta-reports-active"
+ "blob"
+ "bool"
+ "bool%@"
+ "cdHash"
+ "certs"
+ "copyWithZone:"
+ "countCDHashesRejectedByProfileNoThrowWithProfileUUID:"
+ "createOnlineAuthEntry:error:"
+ "dateWithTimeIntervalSince1970:"
+ "deleteCharactersInRange:"
+ "deleteOnlineAuthEntryNoThrowWithCdHash:"
+ "deleteOnlineAuthEntryNoThrowWithProfileUUID:cdHash:"
+ "deleteOnlineAuthEntryWithCdHash:error:"
+ "deleteOnlineAuthEntryWithProfileUUID:cdHash:error:"
+ "dictionaryDescription"
+ "emitEntitlementPredicates:predicateHandler:"
+ "entitlements"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "existsIndeterminatesSoon"
+ "false"
+ "findProfilesMatchingEntitlements:withCertificate:"
+ "findProfilesMatchingPredicates:withCertificate:"
+ "findProfilesWithCertificate:"
+ "fromSQLStatement:withMap:"
+ "getCertPrimaryKey:"
+ "getOnlineAuthEntriesNoThrow"
+ "getOnlineAuthEntryNoThrowWithProfileUUID:cdHash:"
+ "gracePeriod"
+ "i24@0:8^v16"
+ "i32@0:8@16@24"
+ "indeterminateTime"
+ "initWithDB:"
+ "initWithProfileUUID:cdHash:gracePeriod:lastSuccessMonotonicTime:lastSuccessResetCount:isRejected:isRejectedByWholeProfile:"
+ "initWithUUID:withTeamID:withName:withExpiry:isUniversal:isAppleInternal:isLocal:isBeta:"
+ "insertEntitlement:forProfile:"
+ "insertProfile:"
+ "insertSigningIdentities:withProfileUUID:"
+ "isIndeterminate:resetCount:"
+ "isProfileInstalled:"
+ "isRejected"
+ "isRejectedByWholeProfile"
+ "lastSuccessMonotonicTime"
+ "lastSuccessResetCount"
+ "longLongValue"
+ "migrate"
+ "mis.db"
+ "number"
+ "number%@"
+ "numberWithUnsignedInteger:"
+ "online_auth_agent"
+ "pk"
+ "ppq Server URL is %{public}@"
+ "profileUUID"
+ "profile_cms_blob"
+ "profile_expires"
+ "profile_is_apple_internal"
+ "profile_is_beta"
+ "profile_is_for_all_devices"
+ "profile_is_local"
+ "profile_name"
+ "profile_team_id"
+ "profile_uuid"
+ "q"
+ "q16@0:8"
+ "q24@0:8@16"
+ "queryCMSBlobForProfile:forcingXML:handler:"
+ "queryProfile:"
+ "rangeOfString:"
+ "recordIndeterminateEntryNoThrowWithProfileUUID:cdHash:onConflictDoNothing:"
+ "recordIndeterminateEntryWithProfileUUID:cdHash:onConflictDoNothing:error:"
+ "redactedDescription"
+ "rejectEntryWithProfileUUID:cdHash:isRejectedByWholeProfile:error:"
+ "revalidateApps: Checking %{public}@"
+ "session error: %{public}@"
+ "setAppleInternal:"
+ "setBeta:"
+ "setCdHash:"
+ "setEntitlements:"
+ "setExpires:"
+ "setGracePeriod:"
+ "setGracePeriodNoThrowWithProfileUUID:gracePeriod:"
+ "setGracePeriodWithProfileUUID:gracePeriod:error:"
+ "setIsRejected:"
+ "setIsRejectedByWholeProfile:"
+ "setLastSuccessMonotonicTime:"
+ "setLastSuccessResetCount:"
+ "setLocal:"
+ "setName:"
+ "setProfileUUID:"
+ "setProfiles:"
+ "setProvisionsAllDevices:"
+ "setTeamID:"
+ "setUUID:"
+ "string"
+ "stringWithCapacity:"
+ "stringWithString:"
+ "substringFromIndex:"
+ "timeIntervalSince1970"
+ "true"
+ "unrecognized status %d from codesigning library"
+ "v16@?0@\"NSString\"8"
+ "v16@?0^{__CFString=}8"
+ "v20@0:8B16"
+ "v20@0:8C16"
+ "v20@0:8i16"
+ "v24@0:8q16"
+ "v24@?0@\"NSString\"8@\"NSData\"16"
+ "v28@0:8@16i24"
+ "v32@0:8@16@?24"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v32@?0@8@16^B24"
+ "v36@0:8@16@24B32"
- " (periodic)"
- "AGP.plist"
- "Adding launch warning mark to: %@"
- "AuthListBannedCdHashes.plist"
- "AuthListBannedUpps.plist"
- "AuthListReadyCdHashes.plist"
- "Authorized: %@, %@"
- "B36@?0^{__CFString=}8^{__CFString=}16^{__CFString=}24B32"
- "B48@?0^{__CFString=}8^{__CFString=}16^{__CFString=}24^{__CFNumber=}32^{__CFNumber=}40"
- "Base asset had invalid payload: %@"
- "Base asset record changed: %@"
- "Base asset record error: %@, %@"
- "Base asset sync with token: %@"
- "Base sync completion error: %@"
- "CloudKit asset doesn't have a file URL: %@"
- "CloudKit fetch for warning: %@"
- "CloudKit record has invalid algorithm: %@"
- "CloudKit record has invalid bitsPerEntry count: %@"
- "CloudKit record has invalid data: %@"
- "CloudKit record has invalid details zone: %@"
- "CloudKit record has invalid entryCount: %@"
- "CloudKit record has invalid flags field: %@"
- "CloudKit record has invalid id: %@"
- "CloudKit record has invalid payload field: %@"
- "CloudKit record has invalid reason field: %@"
- "CloudKit record has invalid salt: %@"
- "CloudKit record has invalid size: %@"
- "CloudKit record has invalid update number: %@"
- "CloudKit record has invalid update zone: %@"
- "CloudKit record has invalid uuid: %@"
- "CloudKit unexpected error during fetch: %@"
- "Could not convert JSON to Dictionary: %@"
- "Could not convert dictionary to JSON: %@"
- "Could not perform authorization attempt. Forcing indeterminate..."
- "Couldn't get device identity %@"
- "CreateMISAuthListWithStream: authList parse failed (malformed?), error %@"
- "CreateMISAuthListWithStream: creating stream failed"
- "CreateMISAuthListWithStream: open stream failed (may be non-existing)"
- "CreateMISAuthListWithStream: plist root has wrong type"
- "Created launch warning entry: %d"
- "DB being loaded from %@"
- "Error creating new launch warning for %@"
- "Error processing app: %@, %@"
- "Failed to add launch warning mark with no error: %@"
- "Failed to add launch warning mark: %@, %@"
- "Failed to install document checker: %@"
- "Failed to terminate app: %@"
- "Finalize error (%d) on query: %@"
- "Found launch warning for %@ with details: %@"
- "Found launch warning with details: %@"
- "Found no launch warning for %@"
- "Found no launch warning for cdhash: %d, %@"
- "Full JSON message to send: %s"
- "Get launch warning data failed: %@"
- "Got updated base sync token: %@"
- "Got updated update sync token: %@"
- "Indeterminates.plist"
- "Invalid signature for %@ record %@"
- "Item not present in bloom filter: %d, %@"
- "Launch warning found: %d, %@"
- "Launch warning has unknown reason and flags indicate to ignore: %d, %@"
- "Looking up launch warning for cdhash: %d, %@"
- "Merging in bloom filter update: %d for filter %@"
- "Missing signature for %@ record %@"
- "No launch warning present: %d, %@"
- "Not MSCMSSignedData: %@"
- "Nothing about to go indeterminate, cancelling any opportunistic validation."
- "Performing auth request for: %@, %@, %@"
- "Performing opportunistic validation."
- "Permanently rejected profile: %@, %@"
- "Prepare error (%d) on query: %@"
- "Rejected app/profile combination: %@, %@"
- "Rejected profile: %@, %@"
- "Rejections.plist"
- "Removing old bloom filter: %s"
- "Revalidating apps.%s"
- "SQL error '%s' (%1d)"
- "Scheduling opportunistic validation."
- "Sending request for %@, %@"
- "Set launch warning override failed: %@"
- "Setting up new base filter: %@"
- "Setting user override: %lld to %d"
- "Signature validation error: %@"
- "Signing JSON message for %@, %@"
- "Starting sync of zone: %@"
- "Step error (%d) on query: %@"
- "Successfully terminated app: %@"
- "Sync error: %@"
- "Terminating app: %s"
- "The server returned: %s"
- "Unable to add launch warning to app without installation ID: $@"
- "Unable to create code object (%d) for: %@"
- "Unable to create signing info (%d) for: %@"
- "Unable to find cdhash for %@"
- "Unable to get best cdhash data: %@"
- "Unable to get best cdhash digest algorithm: %@"
- "Unable to get full cdhash information for: %@"
- "Unable to look up launch warning info for ID: %lld"
- "Unable to read CloudKit asset file URL: %@"
- "Unable to statfs app: %d, %@"
- "Unable to table row count for %@: %d"
- "Unhandled onlineCheckType %ld encountered. (This should not happen.)"
- "Update asset had incorrect ID: %{public}@, %{public}@"
- "Update asset had invalid compression type: %@"
- "Update entry sync error: %{public}@"
- "Update sync completion error: %@"
- "Update sync error: %@"
- "Update zone record changed: %@"
- "Update zone sync with token: %@"
- "Using emulated device UDID: %@\n"
- "Visiting application: %@"
- "XPC: checking launch warning data for: %llu, %@"
- "XPC: launch warning data response: %@, %lu"
- "attempt in row %@ is not a number, removing"
- "attempts"
- "bad or incomplete graces row: %@"
- "bad or incomplete indeterminates row: %@"
- "bad or incomplete rejections row: %@"
- "cannot decode cdhash: %@"
- "cannot decode rejections cdhash: %@"
- "cdhash"
- "com.apple.mis.opportunistic-validation.scheduled"
- "compare:"
- "could not read in graces, creating new one"
- "could not read in indeterminates, creating new one"
- "could not read in rejections, creating new one"
- "date"
- "defaultWorkspace"
- "enumerateBundlesOfType:block:"
- "firstFailure"
- "firstFailure in %@ is in the future, throwing away"
- "grace"
- "graces row is not a dictionary, but %@"
- "indeterminateListIterate: malformed row"
- "indeterminateListIterate: row with unknown type"
- "indeterminates row is not a dictionary, but %@"
- "lastCheck"
- "lastCheck in %@ is in the future, throwing away"
- "mutableCopy"
- "numberWithInteger:"
- "ppq Server URL is %@"
- "profileValidated"
- "rejectionListIterate: could not convert wholeProfile"
- "rejectionListIterate: malformed row"
- "rejectionListIterate: row with unknown type"
- "rejections row is not a dictionary, but %@"
- "removeObjectForKey:"
- "session error: %@"
- "setValue:forKey:"
- "teamid"
- "type in row %@ is invalid, throwing away"
- "upp-uuid"
- "v24@?0@\"LSBundleProxy\"8^B16"
- "wholeProfile"

```
