## misagent

> `/usr/libexec/misagent`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0x1215c
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__objc_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x5ec
-  __TEXT.__const: 0x3a2
-  __TEXT.__oslogstring: 0x12f7
-  __TEXT.__cstring: 0x239f
-  __TEXT.__objc_classname: 0xaa
-  __TEXT.__objc_methname: 0xd03
-  __TEXT.__objc_methtype: 0x21c
-  __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__swift5_typeref: 0x1b6
-  __TEXT.__swift5_capture: 0x4bc
+463.0.4.0.0
+  __TEXT.__text: 0x18fc0
+  __TEXT.__auth_stubs: 0x1310
+  __TEXT.__objc_stubs: 0x1120
+  __TEXT.__objc_methlist: 0x80c
+  __TEXT.__const: 0x3e2
+  __TEXT.__oslogstring: 0x1d3c
+  __TEXT.__cstring: 0x347f
+  __TEXT.__objc_classname: 0xc7
+  __TEXT.__objc_methname: 0x1401
+  __TEXT.__objc_methtype: 0x27e
+  __TEXT.__gcc_except_tab: 0x4c0
+  __TEXT.__swift5_typeref: 0x21c
+  __TEXT.__swift5_capture: 0x7e8
   __TEXT.__constg_swiftt: 0x1ac
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x10

   __TEXT.__swift5_fieldmd: 0xe8
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x5b8
-  __TEXT.__eh_frame: 0x408
-  __DATA_CONST.__auth_got: 0x908
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0xac0
-  __DATA_CONST.__cfstring: 0x1080
-  __DATA_CONST.__objc_classlist: 0x60
+  __TEXT.__unwind_info: 0x708
+  __TEXT.__eh_frame: 0x514
+  __DATA_CONST.__auth_got: 0x998
+  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__auth_ptr: 0xb0
+  __DATA_CONST.__const: 0xd98
+  __DATA_CONST.__cfstring: 0x1440
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0xb70
-  __DATA.__objc_selrefs: 0x438
-  __DATA.__objc_ivar: 0x64
-  __DATA.__objc_data: 0x450
-  __DATA.__data: 0x238
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0xd80
+  __DATA.__objc_selrefs: 0x5a0
+  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_data: 0x4a0
+  __DATA.__data: 0x2b0
   __DATA.__bss: 0x170
-  __DATA.__common: 0x10
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
   - /usr/lib/libCoreEntitlements.dylib
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B952599B-674F-3057-92D5-716DF295BC1F
-  Functions: 494
-  Symbols:   338
-  CStrings:  680
+  UUID: 1AE23676-5A94-33F5-9A3B-6AC5C2AC2FE7
+  Functions: 640
+  Symbols:   345
+  CStrings:  886
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _CFAllocatorDeallocate
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFStringAppendFormat
+ _CFStringCreateMutable
+ _OBJC_CLASS_$_MISOnlineAuthEntry
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_METACLASS_$_MISOnlineAuthEntry
+ _TMGetKernelMonotonicClock
+ _TMGetRTCResetCount
+ _swift_arrayDestroy
- _OBJC_CLASS_$_OS_os_log
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "%02x"
+ "8"
+ "9"
+ "@24@0:8^{_NSZone=}16"
+ "@60@0:8@16@24i32q36q44B52B56"
+ "AGP.plist"
+ "AddMonotonicTimeOffset"
+ "AddRTCResetCountOffset"
+ "AuthListBannedCdHashes.plist"
+ "AuthListBannedUpps.plist"
+ "B32@0:8q16q24"
+ "B36@0:8@16i24^@28"
+ "B36@?0^{__CFString=}8^{__CFString=}16^{__CFString=}24B32"
+ "B40@0:8q16@24^@32"
+ "B44@0:8@16@24B32^@36"
+ "B48@?0^{__CFString=}8^{__CFString=}16^{__CFString=}24^{__CFNumber=}32^{__CFNumber=}40"
+ "B60@0:8@16@24i32q36q44^@52"
+ "CDHash"
+ "CREATE TABLE IF NOT EXISTS banned_cdhashes (  cdhash BLOB NOT NULL )"
+ "CREATE TABLE IF NOT EXISTS banned_profile_uuids (  uuid TEXT NOT NULL )"
+ "CREATE TABLE IF NOT EXISTS online_auth (  uuid TEXT NOT NULL,  cdhash BLOB NOT NULL,  grace_period INT NOT NULL,  last_success_monotonic_time INT NOT NULL,  last_success_reset_count INT NOT NULL,  is_rejected INT NOT NULL DEFAULT (0),  is_rejected_by_whole_profile INT NOT NULL DEFAULT (0),  PRIMARY KEY (uuid, cdhash),  CONSTRAINT fk_online_auth_profile_uuid    FOREIGN KEY (uuid)    REFERENCES profiles(uuid)    ON DELETE CASCADE )"
+ "Caller (pid %d) does not have required entitlement '%{public}s'"
+ "Cannot add RTC reset count offset on this build"
+ "Cannot add monotonic time offset on this build"
+ "Copying profiles for %{public}@"
+ "Copying profiles for cert %{public}@"
+ "Couldn't create the banned cdhashes table: %s"
+ "Couldn't create the banned profile UUIDs table: %s"
+ "Couldn't create the online auth table: %s"
+ "Couldn't fetch single asterisk wildcard predicates: %s"
+ "Couldn't find a profile matching these predicates:"
+ "Couldn't insert new types for single asterisk wildcard predicates: %s"
+ "CreateMISAuthListWithStream: authList parse failed (malformed?), error %{public}@"
+ "DB being loaded from %{public}@"
+ "DELETE FROM online_auth WHERE cdhash = ?1"
+ "DELETE FROM online_auth WHERE uuid = ?1 AND cdhash = ?2"
+ "Error adding RTC reset count offset: error = %{public}@, offset = %ld, cdHash = %{public}@"
+ "Error adding monotonic time offset: error = %{public}@, offset = %ld, cdHash = %{public}@"
+ "Error counting cdhashes rejected by profile %{public}s"
+ "Error deleting online auth entry %{public}s"
+ "Error deleting online auth entry %{public}s, %{public}s"
+ "Error getting auxiliary signature for %{public}s from legacy user trust DB: %{public}@"
+ "Error getting online auth entries: %{public}@"
+ "Error getting online auth entry %{public}s, %{public}s"
+ "Error migrating online auth: 0x%x"
+ "Error migrating user trust: 0x%x"
+ "Error recording indeterminate entry %{public}s, %{public}s, %{bool}d"
+ "Error removing profile: %{public}@"
+ "Error setting grace period for %{public}s, %d"
+ "Error setting user trust: error = %{public}@, profileUUID = %{public}@, team = %{public}@, signature = %{public}@, trust = %d"
+ "Finalize error (%d) on query: %{public}@"
+ "Found indeterminate entry for profile %{public}@, but not installed, skipping"
+ "INSERT INTO banned_cdhashes (cdhash)\nVALUES (?1)\nON CONFLICT DO NOTHING"
+ "INSERT INTO banned_profile_uuids (uuid)\nVALUES (?1)\nON CONFLICT DO NOTHING"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 0, 0)\n"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, 0, -1, -1, 1, ?3)\nON CONFLICT(uuid, cdhash) DO UPDATE SET\n    is_rejected = 1,\n    is_rejected_by_whole_profile = ?3"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7)\nON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = ?3,\n    last_success_monotonic_time = ?4,\n    last_success_reset_count = ?5,\n    is_rejected = ?6,\n    is_rejected_by_whole_profile = ?7"
+ "INSERT INTO online_auth (\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\n)\nVALUES (?3, ?4, ?5, ?1, ?2, 0, 0)\nON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = ?5,\n    last_success_monotonic_time = ?1,\n    last_success_reset_count = ?2,\n    is_rejected = 0,\n    is_rejected_by_whole_profile = 0"
+ "INSERT OR IGNORE INTO entitlements_provisioning_cache (uuid, predicate, wildcard) VALUES (?1, ?2, 1)"
+ "Indeterminates.plist"
+ "Installing provisioning profile: %{public}@"
+ "MISOnlineAuthEntry"
+ "MISOnlineAuthEntry(%@, %@, gracePeriod: %i, lastSuccessMonotonicTime: %lli, lastSuccessResetCount: %lli, isRejected: %i, isRejectedByWholeProfile: %i)"
+ "MISQL: performing database migration 7 -> 8"
+ "MISQL: performing database migration 8 -> 9"
+ "Migrate"
+ "Migration: Error banning cdHash %{public}@, %{public}@"
+ "Migration: Error banning profile %{public}@, %{public}@"
+ "Migration: Error creating online auth entry: %{public}@, %{public}@"
+ "Migration: Error deleting banned CDHashes plist: %{public}@"
+ "Migration: Error deleting banned UPPs plist: %{public}@"
+ "Migration: Error deleting legacy graces plist: %{public}@"
+ "Migration: Error deleting legacy indeterminates plist: %{public}@"
+ "Migration: Error deleting legacy rejections plist: %{public}@"
+ "Migration: Error fetching team ID for profile UUID %{public}@"
+ "Migration: Error fetching user trusted UUIDs, aborting migration: %{public}@"
+ "Migration: Error rejecting (%{public}@, %{public}@, %d), %{public}@"
+ "Migration: Error trusting profile UUID %{public}@"
+ "Migration: Error trusting team ID %{public}@ with signature %{public}@"
+ "Migration: Finished online auth migration: %d"
+ "Migration: Starting migration of %{public}@"
+ "Migration: Trusting profile UUID %{public}@"
+ "Migration: Trusting team ID %{public}@ with signature %{public}@"
+ "NSCopying"
+ "NULL"
+ "ON CONFLICT(uuid, cdhash) DO NOTHING"
+ "ON CONFLICT(uuid, cdhash) DO UPDATE SET\n    grace_period = 0,\n    last_success_monotonic_time = -1,\n    last_success_reset_count = -1"
+ "Offset"
+ "Predicate: %{public}@"
+ "Prepare error (%d) on query: %{public}@"
+ "Profile %{public}@ is rejected but not installed, skipping"
+ "Rejections.plist"
+ "Removing provisioning profile: %{public}@"
+ "Requested profile has invalid UUID '%{public}s'."
+ "SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth"
+ "SELECT\n    uuid,\n    cdhash,\n    grace_period,\n    last_success_monotonic_time,\n    last_success_reset_count,\n    is_rejected,\n    is_rejected_by_whole_profile\nFROM online_auth\nWHERE uuid = ?1 AND cdhash = ?2"
+ "SELECT COUNT(*)\nFROM online_auth\nWHERE uuid =  ?1 AND is_rejected = 1 AND is_rejected_by_whole_profile = 1"
+ "SELECT uuid, predicate FROM entitlements_provisioning_cache WHERE predicate LIKE 'string%' || x'1f' || '*' AND wildcard = 1"
+ "SQL error '%{public}s' (%1d)"
+ "Sending %{public}@ - %{public}@"
+ "Setting trust for profileUUID = %{public}@, trust = %d, auxiliary signature = %{public}@"
+ "Setting trust for teamID = %{public}@, trust = %d, auxiliary signature = %{public}@"
+ "Step error (%d) on query: %{public}@"
+ "T@\"NSData\",C,N,V_cdHash"
+ "T@\"NSString\",C,N,V_profileUUID"
+ "TB,N,V_isRejected"
+ "TB,N,V_isRejectedByWholeProfile"
+ "Ti,N,V_gracePeriod"
+ "Tq,N,V_lastSuccessMonotonicTime"
+ "Tq,N,V_lastSuccessResetCount"
+ "UPDATE online_auth SET grace_period = ?2\nWHERE uuid = ?1"
+ "UPDATE online_auth SET last_success_monotonic_time = last_success_monotonic_time + ?1 "
+ "UPDATE online_auth SET last_success_reset_count = last_success_reset_count + ?1 "
+ "Unable to table row count for %{public}@: %d"
+ "Using emulated device UDID: %{public}@\n"
+ "WHERE cdhash = ?2"
+ "_cdHash"
+ "_gracePeriod"
+ "_isRejected"
+ "_isRejectedByWholeProfile"
+ "_lastSuccessMonotonicTime"
+ "_lastSuccessResetCount"
+ "_profileUUID"
+ "addMonotonicTimeOffset:cdHash:error:"
+ "addRTCResetCountOffset:cdHash:error:"
+ "allocWithZone:"
+ "arrayWithObjects:count:"
+ "authorizeEntryWithProfileUUID:cdHash:gracePeriod:currentMonotonicTime:currentResetCount:error:"
+ "bad or incomplete graces row: %{public}@"
+ "banCDHash:error:"
+ "banProfileUUID:error:"
+ "bool%@"
+ "cdHash"
+ "cdhash"
+ "client connection error: %{public}s\n"
+ "copy single message missing '%{public}s' key"
+ "copyWithZone:"
+ "countCDHashesRejectedByProfileNoThrowWithProfileUUID:"
+ "createOnlineAuthEntry:error:"
+ "deleteOnlineAuthEntryNoThrowWithCdHash:"
+ "deleteOnlineAuthEntryNoThrowWithProfileUUID:cdHash:"
+ "deleteOnlineAuthEntryWithCdHash:error:"
+ "deleteOnlineAuthEntryWithProfileUUID:cdHash:error:"
+ "dictionaryDescription"
+ "dictionaryWithObjects:forKeys:count:"
+ "encountered migration error %{public}@"
+ "getOnlineAuthEntriesNoThrow"
+ "getOnlineAuthEntryNoThrowWithProfileUUID:cdHash:"
+ "grace"
+ "gracePeriod"
+ "graces row is not a dictionary, but %{public}@"
+ "i"
+ "indeterminateListIterate: malformed row"
+ "indeterminateListIterate: row with unknown type"
+ "indeterminateTime"
+ "initWithContentsOfFile:"
+ "initWithProfileUUID:cdHash:gracePeriod:lastSuccessMonotonicTime:lastSuccessResetCount:isRejected:isRejectedByWholeProfile:"
+ "install message missing '%{public}s' key"
+ "isIndeterminate:resetCount:"
+ "isRejected"
+ "isRejectedByWholeProfile"
+ "lastSuccessMonotonicTime"
+ "lastSuccessResetCount"
+ "message missing '%{public}s' key"
+ "migrate"
+ "migrated %{public}s"
+ "misagent1"
+ "number%@"
+ "numberWithBool:"
+ "profileUUID"
+ "q"
+ "q16@0:8"
+ "q24@0:8@16"
+ "rangeOfString:"
+ "recordIndeterminateEntryNoThrowWithProfileUUID:cdHash:onConflictDoNothing:"
+ "recordIndeterminateEntryWithProfileUUID:cdHash:onConflictDoNothing:error:"
+ "rejectEntryWithProfileUUID:cdHash:isRejectedByWholeProfile:error:"
+ "rejectionListIterate: could not convert wholeProfile"
+ "rejectionListIterate: malformed row"
+ "rejectionListIterate: row with unknown type"
+ "remove message missing '%{public}s' key"
+ "setCdHash:"
+ "setGracePeriod:"
+ "setGracePeriodNoThrowWithProfileUUID:gracePeriod:"
+ "setGracePeriodWithProfileUUID:gracePeriod:error:"
+ "setIsRejected:"
+ "setIsRejectedByWholeProfile:"
+ "setLastSuccessMonotonicTime:"
+ "setLastSuccessResetCount:"
+ "setProfileUUID:"
+ "substringFromIndex:"
+ "teamid"
+ "type"
+ "unable to create profile path for '%{public}s'"
+ "unrecognized value for '%{public}s' key: %{public}s"
+ "upp-uuid"
+ "v20@0:8i16"
+ "v24@0:8q16"
+ "v28@0:8@16i24"
+ "v36@0:8@16@24B32"
+ "wholeProfile"
- "Caller (pid %d) does not have required entitlement '%s'"
- "Copying profiles for %@"
- "CreateMISAuthListWithStream: authList parse failed (malformed?), error %@"
- "DB being loaded from %@"
- "Error getting auxiliary signature for %s from legacy user trust DB: %@"
- "Error removing profile: %@"
- "Error setting user trust: error = %@, profileUUID = %@, team = %@, signature = %@, trust = %d"
- "Finalize error (%d) on query: %@"
- "Installing provisioning profile: %@"
- "MigrateUserTrust"
- "Migration: Error fetching team ID for profile UUID %@"
- "Migration: Error fetching user trusted UUIDs, aborting migration: %@"
- "Migration: Error trusting profile UUID %@"
- "Migration: Error trusting team ID %@ with signature %@"
- "Migration: Trusting profile UUID %@"
- "Migration: Trusting team ID %@ with signature %@"
- "Prepare error (%d) on query: %@"
- "Releasing XPC connection"
- "Removing provisioning profile: %@"
- "Requested profile has invalid UUID '%s'."
- "SQL error '%s' (%1d)"
- "Sending %@ - %@"
- "Setting trust for profileUUID = %@, trust = %d, auxiliary signature = %@"
- "Setting trust for teamID = %@, trust = %d, auxiliary signature = %@"
- "Step error (%d) on query: %@"
- "Unable to table row count for %@: %d"
- "Using emulated device UDID: %@\n"
- "client connection error: %s\n"
- "copy single message missing '%s' key"
- "encountered migration error %@"
- "install message missing '%s' key"
- "message missing '%s' key"
- "migrated %s"
- "remove message missing '%s' key"
- "unable to create profile path for '%s'"
- "unrecognized value for '%s' key: %s"

```
