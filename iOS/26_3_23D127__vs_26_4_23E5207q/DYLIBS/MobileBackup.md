## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2899.80.3.0.0
-  __TEXT.__text: 0x3073c
-  __TEXT.__auth_stubs: 0xde0
-  __TEXT.__objc_methlist: 0x401c
+2969.100.18.0.0
+  __TEXT.__text: 0x30f90
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x3e5c
   __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x7db6
-  __TEXT.__gcc_except_tab: 0x144c
-  __TEXT.__oslogstring: 0x274b
-  __TEXT.__unwind_info: 0x1150
+  __TEXT.__cstring: 0x7a7b
+  __TEXT.__gcc_except_tab: 0x132c
+  __TEXT.__oslogstring: 0x2623
+  __TEXT.__unwind_info: 0x12c0
   __TEXT.__objc_classname: 0x398
-  __TEXT.__objc_methname: 0x9dcd
-  __TEXT.__objc_methtype: 0x11f7
-  __TEXT.__objc_stubs: 0x4ae0
+  __TEXT.__objc_methname: 0x9b33
+  __TEXT.__objc_methtype: 0x11ed
+  __TEXT.__objc_stubs: 0x4980
   __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2360
+  __DATA_CONST.__objc_selrefs: 0x2290
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x5c00
-  __AUTH_CONST.__objc_const: 0x53a8
+  __AUTH_CONST.__cfstring: 0x5860
+  __AUTH_CONST.__objc_const: 0x5268
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x3a0
+  __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0x308
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A98595F4-E0E4-3AFC-A90F-4CB12A25D9D1
-  Functions: 1591
-  Symbols:   4941
-  CStrings:  3899
+  UUID: 530EC30E-9489-359D-94F8-2784A2823CD3
+  Functions: 1568
+  Symbols:   4857
+  CStrings:  3792
 
Symbols:
+ +[MBPersona personaWithAttributes:volumeMountPoint:].cold.1
+ +[MBPersona personaWithUMPersona:error:].cold.1
+ +[MBPersona personaWithUMPersona:error:].cold.2
+ +[MBPersona personaWithUMPersona:error:].cold.3
+ +[MBPersona personaWithUMPersona:error:].cold.4
+ GCC_except_table109
+ GCC_except_table110
+ GCC_except_table121
+ GCC_except_table127
+ GCC_except_table131
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table152
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table46
+ GCC_except_table48
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table72
+ GCC_except_table96
+ GCC_except_table99
+ _OBJC_IVAR_$_MBBehaviorOptions._shouldKeepFileSystemSnapshotAfterBackupSuccess
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.180
+ ___block_literal_global.133
+ ___block_literal_global.262
+ ___block_literal_global.270
+ _objc_msgSend$personaWithAttributes:volumeMountPoint:
- -[MBBehaviorOptions requiredRestoreSnapshotFormatString]
- -[MBBehaviorOptions setSnapshotAfterForegroundRestore:]
- -[MBBehaviorOptions setUseABC:]
- -[MBBehaviorOptions shouldRestoreFromLegacySnapshotFormat]
- -[MBManager allowiTunesBackup]
- -[MBManager clearRestoreSession]
- -[MBManager insufficientFreeSpaceToRestore]
- -[MBManager restoreFileExistsWithPath:]
- -[MBManager restoreSupportsBatching]
- -[MBManager setAllowiTunesBackup:]
- -[MBManager setRestoreQualityOfService:]
- -[MBPersona initWithPersonaAttributes:volumeMountPoint:]
- -[MBPersona initWithPersonaAttributes:volumeMountPoint:].cold.1
- -[MBPersona initWithUMPersona:error:]
- -[MBPersona initWithUMPersona:error:].cold.1
- -[MBPersona initWithUMPersona:error:].cold.2
- -[MBPersona initWithUMPersona:error:].cold.3
- -[MBPersona initWithUMPersona:error:].cold.4
- -[MBRestoreFailure .cxx_destruct]
- -[MBRestoreFailure assetType]
- -[MBRestoreFailure dataclass]
- -[MBRestoreFailure description]
- -[MBRestoreFailure displayName]
- -[MBRestoreFailure error]
- -[MBRestoreFailure icon]
- -[MBRestoreFailure identifier]
- -[MBRestoreFailure setAssetType:]
- -[MBRestoreFailure setDataclass:]
- -[MBRestoreFailure setDisplayName:]
- -[MBRestoreFailure setError:]
- -[MBRestoreFailure setIcon:]
- -[MBRestoreFailure setIdentifier:]
- -[MBXPCClient allowiTunesBackup]
- -[MBXPCClient clearRestoreSession]
- -[MBXPCClient insufficientFreeSpaceToRestore]
- -[MBXPCClient recordRestoreFailure:error:].cold.1
- -[MBXPCClient recordRestoreFailure:error:].cold.2
- -[MBXPCClient repair]
- -[MBXPCClient restoreFileExistsWithPath:]
- -[MBXPCClient restoreSupportsBatching]
- -[MBXPCClient setAllowiTunesBackup:]
- -[MBXPCClient setRestoreQualityOfService:]
- GCC_except_table102
- GCC_except_table103
- GCC_except_table113
- GCC_except_table115
- GCC_except_table117
- GCC_except_table119
- GCC_except_table124
- GCC_except_table126
- GCC_except_table135
- GCC_except_table138
- GCC_except_table144
- GCC_except_table149
- GCC_except_table151
- GCC_except_table170
- GCC_except_table171
- GCC_except_table172
- GCC_except_table173
- GCC_except_table174
- GCC_except_table175
- GCC_except_table176
- GCC_except_table177
- GCC_except_table35
- GCC_except_table41
- GCC_except_table42
- GCC_except_table43
- GCC_except_table44
- GCC_except_table47
- GCC_except_table49
- GCC_except_table51
- GCC_except_table55
- GCC_except_table56
- GCC_except_table60
- GCC_except_table62
- GCC_except_table64
- GCC_except_table68
- GCC_except_table69
- GCC_except_table92
- GCC_except_table95
- _NSStringFromRange
- _OBJC_IVAR_$_MBRestoreFailure._assetType
- _OBJC_IVAR_$_MBRestoreFailure._dataclass
- _OBJC_IVAR_$_MBRestoreFailure._displayName
- _OBJC_IVAR_$_MBRestoreFailure._error
- _OBJC_IVAR_$_MBRestoreFailure._icon
- _OBJC_IVAR_$_MBRestoreFailure._identifier
- __OBJC_$_INSTANCE_VARIABLES_MBRestoreFailure
- __OBJC_$_PROP_LIST_MBRestoreFailure
- ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.186
- ___block_literal_global.142
- ___block_literal_global.289
- ___block_literal_global.297
- __os_feature_enabled_impl
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$dataclass
- _objc_msgSend$identifier
- _objc_msgSend$initWithPersonaAttributes:volumeMountPoint:
- _objc_msgSend$initWithUMPersona:error:
- _objc_msgSend$manager:didFailVerificationWithError:
- _objc_msgSend$managerDidFinishVerification:
- _objc_msgSend$setAssetType:
- _objc_msgSend$setDataclass:
- _objc_msgSend$setDisplayName:
- _objc_msgSend$setError:
- _objc_msgSend$setIcon:
- _objc_msgSend$setIdentifier:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "+[MBPersona personaWithAttributes:volumeMountPoint:]"
+ "+[MBPersona personaWithUMPersona:error:]"
+ "MBS Removed"
+ "TB,N,V_shouldKeepFileSystemSnapshotAfterBackupSuccess"
+ "_shouldKeepFileSystemSnapshotAfterBackupSuccess"
- "-[MBPersona initWithPersonaAttributes:volumeMountPoint:]"
- "-[MBPersona initWithUMPersona:error:]"
- "/var/mobile/Library/Backup/SystemContainers/Data"
- "/var/mobile/Library/Backup/SystemContainers/Shared"
- "@\"NSData\""
- "Beta"
- "Carrier"
- "ReleaseType"
- "RequiredRestoreSnapshotFormat"
- "ShouldRestoreLegacySnapshotFormat"
- "T@\"NSData\",C,N,V_icon"
- "T@\"NSError\",C,N,V_error"
- "T@\"NSString\",C,N,V_assetType"
- "T@\"NSString\",C,N,V_dataclass"
- "T@\"NSString\",C,N,V_displayName"
- "T@\"NSString\",C,N,V_identifier"
- "_assetType"
- "_dataclass"
- "_displayName"
- "_icon"
- "_identifier"
- "allowiTunesBackup"
- "assetType"
- "clearRestoreSession"
- "containermanagerd"
- "countOfRestoreFailuresForDataclass:assetType"
- "dataclass"
- "dataclass must be non null"
- "displayName"
- "has icon"
- "icon"
- "identifier"
- "identifier must be non null"
- "initWithPersonaAttributes:volumeMountPoint:"
- "initWithUMPersona:error:"
- "insufficientFreeSpaceToRestore"
- "kMBMessageClearRestoreSession"
- "kMBMessageCountRestoreFailures"
- "kMBMessageDidFailVerification"
- "kMBMessageDidFinishVerification"
- "kMBMessageFileExists"
- "kMBMessageGetAllowiTunesBackup"
- "kMBMessageInsufficientFreeSpaceToRestore"
- "kMBMessageListRestoreFailures"
- "kMBMessageRepair"
- "kMBMessageReportRestoreFailure"
- "kMBMessageRestoreSupportsBatching"
- "kMBMessageSetAllowiTunesBackup"
- "kMBMessageSetRestoreQualityOfService"
- "manager:didFailVerificationWithError:"
- "managerDidFinishVerification:"
- "no icon"
- "repair"
- "requiredRestoreSnapshotFormatString"
- "restoreFileExistsWithPath:"
- "restoreSupportsBatching"
- "restoreSupportsBatching:"
- "restore_system_containers_to_shared_volume"
- "setAllowiTunesBackup:"
- "setAssetType:"
- "setDataclass:"
- "setDisplayName:"
- "setIcon:"
- "setIdentifier:"
- "setRestoreQualityOfService:"
- "setSnapshotAfterForegroundRestore:"
- "setUseABC:"
- "shouldRestoreFromLegacySnapshotFormat"
- "{ %@, identifier = %@, dataclass = %@, assetType = %@, error = %@, %@ }"

```
