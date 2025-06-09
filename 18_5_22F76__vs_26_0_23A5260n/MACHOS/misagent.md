## misagent

> `/usr/libexec/misagent`

```diff

-436.100.18.0.0
-  __TEXT.__text: 0x8ad4
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x9a0
-  __TEXT.__objc_methlist: 0x37c
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x15fd
-  __TEXT.__objc_methname: 0x898
-  __TEXT.__objc_classname: 0x51
-  __TEXT.__objc_methtype: 0x1dd
-  __TEXT.__gcc_except_tab: 0x23c
-  __TEXT.__oslogstring: 0x841
-  __TEXT.__unwind_info: 0x2c8
-  __DATA_CONST.__auth_got: 0x628
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x4b0
-  __DATA_CONST.__cfstring: 0xb00
-  __DATA_CONST.__objc_classlist: 0x28
+463.0.0.0.0
+  __TEXT.__text: 0x1215c
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_stubs: 0xd40
+  __TEXT.__objc_methlist: 0x5ec
+  __TEXT.__const: 0x3a2
+  __TEXT.__oslogstring: 0x12f7
+  __TEXT.__cstring: 0x239f
+  __TEXT.__objc_classname: 0xaa
+  __TEXT.__objc_methname: 0xd03
+  __TEXT.__objc_methtype: 0x21c
+  __TEXT.__gcc_except_tab: 0x338
+  __TEXT.__swift5_typeref: 0x1b6
+  __TEXT.__swift5_capture: 0x4bc
+  __TEXT.__constg_swiftt: 0x1ac
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__swift5_reflstr: 0x80
+  __TEXT.__swift5_fieldmd: 0xe8
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__unwind_info: 0x5b8
+  __TEXT.__eh_frame: 0x408
+  __DATA_CONST.__auth_got: 0x908
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__const: 0xac0
+  __DATA_CONST.__cfstring: 0x1080
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x610
-  __DATA.__objc_selrefs: 0x310
-  __DATA.__objc_ivar: 0x44
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x8
-  __DATA.__bss: 0x30
+  __DATA.__objc_const: 0xb70
+  __DATA.__objc_selrefs: 0x438
+  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_data: 0x450
+  __DATA.__data: 0x238
+  __DATA.__bss: 0x170
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4B5B843C-88FE-38CE-B206-AA2F0C89F4F9
-  Functions: 223
-  Symbols:   236
-  CStrings:  437
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: B952599B-674F-3057-92D5-716DF295BC1F
+  Functions: 494
+  Symbols:   338
+  CStrings:  680
 
Symbols:
+ _CFArrayCreate
+ _CFArrayGetTypeID
+ _CFBooleanGetValue
+ _CFDateCompare
+ _CFDictionaryGetTypeID
+ _CFPropertyListCreateWithStream
+ _CFReadStreamCreateWithFile
+ _CFReadStreamOpen
+ _CFStringCreateWithSubstring
+ _CFStringGetCharacterAtIndex
+ _CFStringHasPrefix
+ _MISArrayAllowsEntitlementValue
+ _MISEntitlementDictionaryAllowsEntitlementValue
+ _MISProfileGetValue
+ _MISProfileValidateSignature
+ _MISProvisioningProfileGetTeamName
+ _MISProvisioningProfileGetVersion
+ _MISProvisioningProfileIncludesDevice
+ _MISProvisioningProfileIncludesPlatform
+ _MISXMLProvisioningProfileGetDeveloperCertificates
+ _OBJC_CLASS_$_MISTeamIDEntryForUI
+ _OBJC_CLASS_$_MISTrustedProfileEntry
+ _OBJC_CLASS_$_MISTrustedTeamIDEntry
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_OS_os_log
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$_MISTeamIDEntryForUI
+ _OBJC_METACLASS_$_MISTrustedProfileEntry
+ _OBJC_METACLASS_$_MISTrustedTeamIDEntry
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _SecCertificateCopySubjectSummary
+ _SecCertificateCreateWithData
+ __Block_copy
+ __Block_release
+ ___chkstk_darwin
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_reportUnimplementedInitializer
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_alloc_init
+ _objc_autorelease
+ _objc_opt_new
+ _objc_opt_respondsToSelector
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
+ _objc_retain_x28
+ _objc_setProperty_nonatomic_copy
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _sqlite3_bind_null
+ _swift_allocError
+ _swift_allocObject
+ _swift_arrayInitWithCopy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _xpc_dictionary_get_int64
CStrings:
+ "/private/var/db/MobileIdentityData"
+ "243LU875E5"
+ "4"
+ "5"
+ "6"
+ "7"
+ "@\"MISTrustedTeamIDEntry\""
+ "@\"NSData\""
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24B32B36"
+ "@signing_identity"
+ "@team_name"
+ "AppleInternalProfile"
+ "Attempt to set profile trust without entitlement"
+ "Attempting to trust team ID, but no installed profiles have that team ID"
+ "AuxiliarySignature"
+ "B16@?0^{__CFString=}8"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@24^@32"
+ "BEGIN TRANSACTION"
+ "COMMIT TRANSACTION"
+ "CREATE TABLE IF NOT EXISTS sep_trusted_team_ids (\n    team_id TEXT PRIMARY KEY,\n    signature BLOB NOT NULL\n)"
+ "CREATE TABLE IF NOT EXISTS signing_identities ( pk INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, signing_identity TEXT NOT NULL, UNIQUE(uuid, signing_identity), CONSTRAINT fk_signing_identity_profile_uuid  FOREIGN KEY (uuid)  REFERENCES profiles(uuid)   ON DELETE CASCADE )"
+ "CREATE TABLE IF NOT EXISTS team_id_info ( team_id TEXT NOT NULL, team_name TEXT NOT NULL,  PRIMARY KEY (team_id) )"
+ "CREATE TABLE IF NOT EXISTS trusted_team_ids ( team_id TEXT PRIMARY KEY, signature BLOB )"
+ "CREATE TABLE IF NOT EXISTS user_trusted_profiles (\n    uuid TEXT NOT NULL PRIMARY KEY,\n    team_id TEXT,\n    CONSTRAINT fk_team_id\n        FOREIGN KEY (team_id)\n        REFERENCES sep_trusted_team_ids(team_id)\n        ON DELETE CASCADE\n)"
+ "Couldn't create SecCertificate for %@"
+ "Couldn't create the signing identities table: %s"
+ "Couldn't create the team ID info table: %s"
+ "Couldn't create the trusted team IDs table: %s"
+ "Couldn't fetch trusted signing identities from profiles: %s"
+ "Couldn't fetch trusted signing identities from xml_profiles_cache: %s"
+ "Couldn't fetch trusted team ID info: %s"
+ "Couldn't get signing identity for %@"
+ "Couldn't insert into signing identities: %s"
+ "Couldn't insert team ID info: %s"
+ "Couldn't replace signature with nil: %s"
+ "CreateMISAuthListWithStream: authList parse failed (malformed?), error %@"
+ "CreateMISAuthListWithStream: creating stream failed"
+ "CreateMISAuthListWithStream: open stream failed (may be non-existing)"
+ "CreateMISAuthListWithStream: plist root has wrong type"
+ "DELETE FROM team_id_info WHERE team_id = ?1"
+ "DELETE FROM trusted_team_ids\nWHERE EXISTS (\n    SELECT 1\n    FROM profiles\n    WHERE uuid = ?1 AND profiles.team_id = trusted_team_ids.team_id\n)"
+ "DELETE FROM trusted_team_ids WHERE team_id = ?1"
+ "DER-Encoded-Profile"
+ "DeveloperCertificates"
+ "Encountered a non-array value for 'Platforms'."
+ "Encountered a null or non-string platform identifier."
+ "Encountered a provisioning profile that does not provision the current platform."
+ "Error getting auxiliary signature for %s from legacy user trust DB: %@"
+ "Error removing profile: %@"
+ "Error searching for zero length signatures: %s"
+ "Error setting user trust: error = %@, profileUUID = %@, team = %@, signature = %@, trust = %d"
+ "ExpirationDate"
+ "Failed to get XPC payload when setting user trust"
+ "INSERT INTO team_id_info VALUES (@team_id, @team_name)"
+ "INSERT INTO team_id_info VALUES (@team_id, @team_name) ON CONFLICT DO NOTHING"
+ "INSERT INTO trusted_team_ids (team_id, signature)\nVALUES (?1, ?2)\nON CONFLICT(team_id) DO UPDATE SET signature = ?2"
+ "INSERT OR IGNORE INTO signing_identities VALUES (NULL, @uuid, @signing_identity)"
+ "LocalProvision"
+ "MISQL: null version, potential erase or upgrade"
+ "MISQL: performing database migration 3 -> 4"
+ "MISQL: performing database migration 4 -> 5"
+ "MISQL: performing database migration 5 -> 6"
+ "MISQL: performing database migration 6 -> 7"
+ "MISTeamIDEntryForUI"
+ "MISTeamIDEntryForUI(%@, %@, %d, %d)"
+ "MISTrustedProfileEntry"
+ "MISTrustedProfileEntry(%@, %@, %@)"
+ "MISTrustedTeamIDEntry"
+ "MISTrustedTeamIDEntry(%@, %@)"
+ "MISUPPTrustRevoked"
+ "MISUPPTrustSet"
+ "MigrateUserTrust"
+ "Migrating team ID info: Unable to create profile for %@"
+ "Migration: Couldn't create SecCertificate for %@"
+ "Migration: Error deleting legacy user trust DB"
+ "Migration: Error deleting legacy user trust DB shm"
+ "Migration: Error deleting legacy user trust DB wal"
+ "Migration: Error deleting legacy user trust plist"
+ "Migration: Error fetching team ID for profile UUID %@"
+ "Migration: Error fetching user trusted UUIDs, aborting migration: %@"
+ "Migration: Error trusting profile UUID %@"
+ "Migration: Error trusting team ID %@ with signature %@"
+ "Migration: Finished migration from legacy user trust DB: %d"
+ "Migration: Finished migration from legacy user trust plist: %d"
+ "Migration: Starting migration from legacy user trust DB"
+ "Migration: Starting migration from legacy user trust plist"
+ "Migration: Trusting profile UUID %@"
+ "Migration: Trusting team ID %@ with signature %@"
+ "Migration: Unable to create profile for %@"
+ "Migration: Unable to get signing identity from %@"
+ "MigrationPhase"
+ "MobileIdentityService"
+ "No team ID found for profile UUID: "
+ "OSX"
+ "Platform"
+ "ProvisionedDevices"
+ "Q16@0:8"
+ "ROLLBACK TRANSACTION"
+ "SELECT COUNT(1)\nFROM profiles\nWHERE team_id = ?1"
+ "SELECT profiles.team_id, profiles.cms_blob, profiles.uuid FROM profiles"
+ "SELECT team_id\nFROM profiles\nWHERE uuid = ?1"
+ "SELECT team_id FROM profiles WHERE uuid = ?1"
+ "SELECT team_id, signature\nFROM sep_trusted_team_ids\nWHERE team_id = ?1"
+ "SELECT team_id, signature FROM trusted_team_ids"
+ "SELECT uuid\nFROM user_trusted_profiles"
+ "SELECT uuid, cms_blob FROM profiles WHERE is_der = 0 AND (is_for_all_devices = 1 OR is_local = 1)"
+ "SELECT xml_profiles_cache.uuid, xml_profiles_cache.cms_blob FROM xml_profiles_cache LEFT JOIN profiles ON profiles.uuid = xml_profiles_cache.uuid WHERE profiles.is_for_all_devices = 1 OR profiles.is_local = 1"
+ "Setting trust for profileUUID = %@, trust = %d, auxiliary signature = %@"
+ "Setting trust for teamID = %@, trust = %d, auxiliary signature = %@"
+ "T@\"MISTrustedTeamIDEntry\",C,N,V_trustedTeamIDEntry"
+ "T@\"NSData\",C,N,V_signature"
+ "T@\"NSString\",C,N,V_teamID"
+ "T@\"NSString\",C,N,V_teamName"
+ "T@\"NSString\",C,N,V_uuid"
+ "TB,N,V_hasAuxiliarySignature"
+ "TB,N,V_trusted"
+ "TeamIdentifier"
+ "TeamName"
+ "Trust"
+ "UPDATE trusted_team_ids SET signature = NULL WHERE team_id = ?1"
+ "Unknown migration phase %lld"
+ "UserTrust.db"
+ "UserTrust.db-shm"
+ "UserTrust.db-wal"
+ "UserTrustedUpps.plist"
+ "Version"
+ "When setting trust, profile UUID and team ID cannot both be NULL"
+ "When setting trust, profile UUID and team ID cannot both be non-NULL"
+ "_TtC8misagent12SQLStatement"
+ "_TtC8misagent17LegacyUserTrustDB"
+ "_TtC8misagent25LegacyUserTrustOperations"
+ "_hasAuxiliarySignature"
+ "_signature"
+ "_teamID"
+ "_teamName"
+ "_trusted"
+ "_trustedTeamIDEntry"
+ "_uuid"
+ "authListIterate: row with unknown type"
+ "caseInsensitiveCompare:"
+ "certs"
+ "com.apple.private.mis.trust.set"
+ "createTrustedTeamIDEntryWithProfileUUID:signature:error:"
+ "createTrustedTeamIDEntryWithTeamID:signature:error:"
+ "deleteTrustedWithProfileUUID:error:"
+ "deleteTrustedWithTeamID:error:"
+ "description"
+ "deviceUDID"
+ "entitlements"
+ "fileExistsAtPath:"
+ "fileSystemRepresentation"
+ "fileURLWithPath:isDirectory:"
+ "getAuxiliarySignatureWithTeamId:"
+ "getTeamIDForProfileUUID:error:"
+ "getUserTrustedUUIDsAndReturnError:"
+ "hasAuxiliarySignature"
+ "hash"
+ "iOS"
+ "init()"
+ "initWithBytes:length:"
+ "initWithTeamID:signature:"
+ "initWithTeamID:teamName:trusted:hasAuxiliarySignature:"
+ "initWithUUID:trustedTeamIDEntry:"
+ "insertSigningIdentities:withProfileUUID:"
+ "isEqual:"
+ "mis.db"
+ "misagent"
+ "misagent.LegacyUserTrustDB"
+ "objectForKey:"
+ "raw"
+ "redactedDescription"
+ "removeProfileWithUuid:error:"
+ "setHasAuxiliarySignature:"
+ "setSignature:"
+ "setTeamName:"
+ "setTrusted:"
+ "setTrustedTeamIDEntry:"
+ "setUuid:"
+ "signature"
+ "stringByAppendingPathComponent:"
+ "stringByDeletingLastPathComponent"
+ "substringWithRange:"
+ "teamID"
+ "teamName"
+ "trusted"
+ "trustedTeamIDEntry"
+ "utdb"
+ "uuid"
+ "v20@0:8B16"
+ "v24@?0@\"NSString\"8@\"NSData\"16"
+ "v24@?0^v8@\"NSDictionary\"16"
+ "visionOS"
+ "xrOS"
- "/mis.db"
- "MISQL: null version, potential erase or updgrade"
- "URLByAppendingPathComponent:"
- "URLByDeletingLastPathComponent"
- "i24@0:8@16"
- "removeProfile:"

```
