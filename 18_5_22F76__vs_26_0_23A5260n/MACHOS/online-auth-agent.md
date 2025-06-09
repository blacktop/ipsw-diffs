## online-auth-agent

> `/usr/libexec/online-auth-agent`

```diff

-436.100.18.0.0
-  __TEXT.__text: 0x34024
-  __TEXT.__auth_stubs: 0x1ca0
-  __TEXT.__objc_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x38c
-  __TEXT.__const: 0x1ebc
-  __TEXT.__gcc_except_tab: 0x3ec
-  __TEXT.__cstring: 0x3278
-  __TEXT.__objc_methname: 0x1163
-  __TEXT.__oslogstring: 0x1fee
+463.0.0.0.0
+  __TEXT.__text: 0x34714
+  __TEXT.__auth_stubs: 0x1d80
+  __TEXT.__objc_stubs: 0xfc0
+  __TEXT.__objc_methlist: 0x304
+  __TEXT.__const: 0x223c
+  __TEXT.__cstring: 0x2ff7
+  __TEXT.__gcc_except_tab: 0x3f8
+  __TEXT.__objc_methname: 0x11a5
+  __TEXT.__oslogstring: 0x1dae
   __TEXT.__objc_classname: 0x58
   __TEXT.__objc_methtype: 0x212
   __TEXT.__dlopen_cstrs: 0x12c
-  __TEXT.__constg_swiftt: 0xb7c
-  __TEXT.__swift5_typeref: 0x7f7
-  __TEXT.__swift5_reflstr: 0x6f5
-  __TEXT.__swift5_fieldmd: 0x984
-  __TEXT.__swift5_types: 0xe8
-  __TEXT.__swift5_capture: 0x430
+  __TEXT.__swift5_typeref: 0x8b9
+  __TEXT.__swift5_capture: 0x2bc
+  __TEXT.__constg_swiftt: 0xbfc
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_proto: 0x148
+  __TEXT.__swift5_reflstr: 0x765
+  __TEXT.__swift5_fieldmd: 0x9d0
+  __TEXT.__swift5_proto: 0x198
+  __TEXT.__swift5_types: 0xf0
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_assocty: 0x150
-  __TEXT.__unwind_info: 0xdf0
-  __TEXT.__eh_frame: 0x1310
-  __DATA_CONST.__auth_got: 0xe60
-  __DATA_CONST.__got: 0x4a8
-  __DATA_CONST.__auth_ptr: 0x468
-  __DATA_CONST.__const: 0x22c0
-  __DATA_CONST.__cfstring: 0xc80
-  __DATA_CONST.__objc_classlist: 0x80
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__unwind_info: 0xdb0
+  __TEXT.__eh_frame: 0x12bc
+  __DATA_CONST.__auth_got: 0xed0
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__auth_ptr: 0x440
+  __DATA_CONST.__const: 0x22c8
+  __DATA_CONST.__cfstring: 0xc00
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xd58
-  __DATA.__objc_selrefs: 0x698
+  __DATA.__objc_const: 0xce0
+  __DATA.__objc_selrefs: 0x6c0
   __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0x460
-  __DATA.__data: 0x1618
-  __DATA.__bss: 0x2660
-  __DATA.__common: 0xf8
+  __DATA.__objc_data: 0x2e0
+  __DATA.__data: 0x1668
+  __DATA.__bss: 0x3090
+  __DATA.__common: 0xe8
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/InstalledContentLibrary.framework/InstalledContentLibrary
+  - /System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A13C8F27-7CF8-3F81-8567-EFC76EC6093D
-  Functions: 1147
-  Symbols:   431
-  CStrings:  952
+  UUID: 1BB5D389-D525-3A8D-9314-D9C72C48CBEA
+  Functions: 1128
+  Symbols:   426
+  CStrings:  930
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _OBJC_CLASS_$_MSCMSContentInfo
+ _OBJC_CLASS_$_MSCMSSignedData
+ _OBJC_CLASS_$_MSCMSSignerInfo
+ _OBJC_CLASS_$_MSDecodeOptions
+ _SecPolicyCreateApplePinned
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _objc_retain_x9
+ _sqlite3_bind_null
+ _swift_arrayDestroy
+ _swift_setDeallocating
- _CFAllocatorAllocate
- _CFNotificationCenterGetDarwinNotifyCenter
- _CFNotificationCenterPostNotification
- _CFURLCreateWithFileSystemPath
- _CFURLCreateWithFileSystemPathRelativeToBase
- _OBJC_CLASS_$_NSUUID
- _OBJC_CLASS_$__TtC17online_auth_agent24UserTrustAgentOperations
- _OBJC_METACLASS_$__TtC17online_auth_agent24UserTrustAgentOperations
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _kCFAllocatorNull
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_retain_n
CStrings:
+ "1.2.840.113635.100.12.53"
+ "1.2.840.113635.100.6.2.17"
+ "294be08b-487f-4020-a986-011dbc7a4fc8"
+ "48988f8b-9b77-4165-8eb1-038a0745dc87"
+ "65033b0b-6071-4ad2-8509-f8e087b74d5b"
+ "CMS signers is empty"
+ "Failed to create LWAssetTrustPolicy"
+ "Fatal error"
+ "Invalid number of keys found, expected one."
+ "Invalid signature for %@ record %@"
+ "LWAssetTrustPolicy"
+ "LaunchWarning.db"
+ "Missing signature for %@ record %@"
+ "Not MSCMSSignedData: %@"
+ "Signature validation error: %@"
+ "Unable to create data directory '%@' (error %{errno}d)!"
+ "Unable to read CloudKit asset file URL: %@"
+ "_TtC17online_auth_agent13DataValidator"
+ "cdhash is nil in database"
+ "com.apple.mis.launchwarning.cloudkit.validation.error"
+ "containerIdentifier"
+ "decodeMessageSecurityObject:options:error:"
+ "embeddedContent"
+ "fileSystemRepresentation"
+ "fileURLWithPath:isDirectory:"
+ "ignoreSignatures"
+ "online_auth_agent/DataValidator.swift"
+ "recordID"
+ "recordName"
+ "setDataContent:"
+ "signers"
+ "stringByDeletingLastPathComponent"
+ "verifySignaturesAndSignersWithPolicies:verifyTime:error:"
- "/var/db/MobileIdentityData"
- "/var/db/MobileIdentityData/LaunchWarning.db"
- "/var/db/MobileIdentityData/UserTrust.db"
- "B16@?0^{__CFString=}8"
- "B32@0:8@16^@24"
- "B48@0:8@16@24@32^@40"
- "BEGIN TRANSACTION"
- "COMMIT TRANSACTION"
- "CREATE TABLE IF NOT EXISTS sep_trusted_team_ids (\n    team_id TEXT PRIMARY KEY,\n    signature BLOB NOT NULL\n)"
- "CREATE TABLE IF NOT EXISTS user_trusted_profiles (\n    uuid TEXT NOT NULL PRIMARY KEY,\n    team_id TEXT,\n    CONSTRAINT fk_team_id\n        FOREIGN KEY (team_id)\n        REFERENCES sep_trusted_team_ids(team_id)\n        ON DELETE CASCADE\n)"
- "Could not allocate path buffer for MIS data directory (this should not happen)."
- "Could not get path for MIS data directory (this should not happen)."
- "CreateMISAuthListWithFile: url is NULL"
- "Creating UserTrust.db if it doesn't exist"
- "DELETE FROM sep_trusted_team_ids WHERE team_id = ?1"
- "DELETE FROM user_trusted_profiles WHERE uuid = ?1"
- "Failed to migrate UPP %@: %@"
- "Failed to set trust for UPP %s: %@"
- "INSERT INTO sep_trusted_team_ids (team_id, signature)\nVALUES (?1, ?2)\nON CONFLICT(team_id) DO UPDATE SET signature = ?2"
- "INSERT OR REPLACE INTO user_trusted_profiles (uuid, team_id) VALUES (?1, ?2)"
- "MISUPPTrustRevoked"
- "MISUPPTrustSet"
- "ROLLBACK TRANSACTION"
- "Removing old trusted UPP plist"
- "SELECT COUNT(team_id)\nFROM user_trusted_profiles\nWHERE team_id = ?1"
- "SELECT team_id\nFROM user_trusted_profiles\nWHERE uuid = ?1"
- "Setting trust for UPP %s: trust: %d, use db: %d, team ID: %@, auxiliary signature: %@"
- "URLByAppendingPathComponent:"
- "URLByDeletingLastPathComponent"
- "Unable to create data directory '%s' (error %{errno}d)!"
- "Upgrading MIS data: Migrating old trusted UPP plist to new database (phase %llu)"
- "UserTrustedUpps.plist"
- "Version.plist"
- "_TtC17online_auth_agent11UserTrustDB"
- "_TtC17online_auth_agent24UserTrustAgentOperations"
- "_TtC17online_auth_agent6Logger"
- "authListIterate: row with unknown type"
- "createUserTrustedProfileEntryWithUuid:teamId:signature:error:"
- "deleteTrustedProfileWithUuid:error:"
- "initWithUUIDString:"
- "online_auth_agent"
- "online_auth_agent.UserTrustDB"
- "phas"
- "removeItemAtPath:error:"
- "rqup"
- "trst"
- "unable to create CFDataRef for signature data"
- "upp_uuid missing from message."
- "usdb"
- "utdb"
- "xsig"

```
