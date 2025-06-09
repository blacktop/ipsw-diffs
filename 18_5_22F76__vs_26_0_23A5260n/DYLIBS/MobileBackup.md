## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2624.120.12.0.0
-  __TEXT.__text: 0x3094c
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x404c
-  __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x7e5a
-  __TEXT.__gcc_except_tab: 0x13c4
-  __TEXT.__oslogstring: 0x2762
-  __TEXT.__unwind_info: 0x1148
+2877.0.0.0.0
+  __TEXT.__text: 0x3005c
+  __TEXT.__auth_stubs: 0xde0
+  __TEXT.__objc_methlist: 0x3ff4
+  __TEXT.__const: 0x590
+  __TEXT.__cstring: 0x7c74
+  __TEXT.__gcc_except_tab: 0x12d0
+  __TEXT.__oslogstring: 0x268e
+  __TEXT.__unwind_info: 0x10f8
   __TEXT.__objc_classname: 0x397
-  __TEXT.__objc_methname: 0x9ca2
-  __TEXT.__objc_methtype: 0x11dc
-  __TEXT.__objc_stubs: 0x4b40
+  __TEXT.__objc_methname: 0x9ce5
+  __TEXT.__objc_methtype: 0x11d1
+  __TEXT.__objc_stubs: 0x4b20
   __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x668
+  __DATA_CONST.__const: 0x640
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2368
+  __DATA_CONST.__objc_selrefs: 0x2360
   __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x718
+  __DATA_CONST.__objc_arraydata: 0xa0
+  __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x5d20
-  __AUTH_CONST.__objc_const: 0x5288
+  __AUTH_CONST.__cfstring: 0x5bc0
+  __AUTH_CONST.__objc_const: 0x5318
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x388
+  __DATA.__objc_ivar: 0x390
   __DATA.__data: 0x308
-  __DATA.__bss: 0x150
-  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA.__bss: 0x120
+  __DATA_DIRTY.__objc_data: 0xcd0
   __DATA_DIRTY.__data: 0x48
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__bss: 0x130
   __DATA_DIRTY.__common: 0x1
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D29A4A0-AF21-35AD-AA4C-A24D332147B1
-  Functions: 1599
-  Symbols:   4954
-  CStrings:  3918
+  UUID: 73B17F14-EFB4-3965-A7C2-69D325AF2C7F
+  Functions: 1587
+  Symbols:   4921
+  CStrings:  3885
 
Symbols:
+ -[MBBehaviorOptions d2dTransferDisconnectTimeout]
+ -[MBBehaviorOptions maxRestorePathsToFailPlacing]
+ -[MBDomain relativePathsNotToTransferDeviceToDevice]
+ -[MBDomain relativePathsToBackupLive]
+ -[MBDomain setRelativePathsNotToTransferDeviceToDevice:]
+ -[MBDomain setRelativePathsToBackupLive:]
+ -[MBPersona personaName]
+ -[MBXPCClient deviceIsLocking]
+ -[MBXPCClient deviceIsUnlocked]
+ GCC_except_table100
+ GCC_except_table104
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table125
+ GCC_except_table127
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table145
+ GCC_except_table152
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table97
+ _OBJC_IVAR_$_MBDomain._relativePathsNotToTransferDeviceToDevice
+ _OBJC_IVAR_$_MBDomain._relativePathsToBackupLive
+ ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.186
+ ___block_descriptor_32_e88_v20?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}12l
+ ___block_literal_global.133
+ ___block_literal_global.285
+ ___block_literal_global.293
+ ___block_literal_global.49
+ ___block_literal_global.51
+ ___block_literal_global.74
+ _objc_msgSend$isEnterprisePersona
+ _objc_msgSend$placeholderNameWithAppID:
- -[MBBehaviorOptions validateSignatureOnRestoreWithDefaultValue:]
- -[MBDeviceTransferTask _resume]
- -[MBDeviceTransferTask _resume].cold.1
- -[MBDeviceTransferTask _resume].cold.2
- -[MBManager getAppleIDsForBackupUDID:snapshotID:activeAppleID:error:]
- -[MBManager getAppleIDsForBackupUDID:snapshotID:error:]
- -[MBManager resumeDeviceTransferWithTaskType:error:]
- -[MBManager saveKeybagsForBackupUDID:withError:]
- -[MBManager setRestoreSessionWithBackupUDID:snapshotUUID:]
- -[MBXPCClient deleteSnapshotID:fromBackupUDID:error:]
- -[MBXPCClient getAppleIDsForBackupUDID:snapshotID:activeAppleID:error:]
- -[MBXPCClient getAppleIDsForBackupUDID:snapshotID:error:]
- -[MBXPCClient keyBagIsLocking]
- -[MBXPCClient keyBagIsUnlocked]
- -[MBXPCClient resumeDeviceTransferWithTaskType:error:]
- -[MBXPCClient resumeDeviceTransferWithTaskType:error:].cold.1
- -[MBXPCClient resumeDeviceTransferWithTaskType:error:].cold.2
- -[MBXPCClient saveKeybagsForBackupUDID:withError:]
- -[MBXPCClient setRestoreSessionWithBackupUDID:snapshotUUID:]
- GCC_except_table108
- GCC_except_table109
- GCC_except_table120
- GCC_except_table122
- GCC_except_table124
- GCC_except_table128
- GCC_except_table130
- GCC_except_table131
- GCC_except_table137
- GCC_except_table138
- GCC_except_table139
- GCC_except_table140
- GCC_except_table141
- GCC_except_table148
- GCC_except_table155
- GCC_except_table157
- GCC_except_table176
- GCC_except_table177
- GCC_except_table178
- GCC_except_table179
- GCC_except_table180
- GCC_except_table181
- GCC_except_table95
- GCC_except_table98
- _CFMakeCollectable
- _CacheDeletePurgeSpaceWithInfo
- _MBPurgeDiskSpace
- _OBJC_CLASS_$_NSConstantIntegerNumber
- ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.183
- ___MBPurgeDiskSpace_block_invoke
- ___block_descriptor_32_e78_v20?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}12l
- ___block_descriptor_48_e8_32o40r_e25_v16?0^{__CFDictionary=}8lr40l8s32l8
- ___block_literal_global.142
- ___block_literal_global.294
- ___block_literal_global.302
- ___block_literal_global.31
- ___block_literal_global.56
- _objc_msgSend$_resume
- _objc_msgSend$getAppleIDsForBackupUDID:snapshotID:activeAppleID:error:
- _objc_msgSend$resumeDeviceTransferWithTaskType:error:
- _os_log_type_get_name
CStrings:
+ "D2DDisconnectTimeout"
+ "Db"
+ "Df"
+ "E "
+ "EDS"
+ "F "
+ "Failed to send DeviceIsLocking message to backupd: %@"
+ "Failed to send DeviceIsUnlocked message to backupd: %@"
+ "I "
+ "MaxRestorePathsToFailPlacing"
+ "Personal"
+ "RelativePathsNotToTransferDeviceToDevice"
+ "RelativePathsToBackupLive"
+ "T@\"NSSet\",&,N,V_relativePathsNotToTransferDeviceToDevice"
+ "T@\"NSSet\",&,N,V_relativePathsToBackupLive"
+ "UNEXPECTED %@"
+ "_relativePathsNotToTransferDeviceToDevice"
+ "_relativePathsToBackupLive"
+ "d2dTransferDisconnectTimeout"
+ "deviceIsLocking"
+ "deviceIsUnlocked"
+ "kMBMessageDeviceIsLocking"
+ "kMBMessageDeviceIsUnlocked"
+ "kMBNotifyDaemonNextTimeDeviceIsUnlocked %d (%@)"
+ "maxRestorePathsToFailPlacing"
+ "personaName"
+ "relativePathsNotToTransferDeviceToDevice"
+ "relativePathsToBackupLive"
+ "setRelativePathsNotToTransferDeviceToDevice:"
+ "setRelativePathsToBackupLive:"
+ "v20@?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICB(?=QQ)*(?=CC)C*}12"
- "%@: Resuming"
- "-[MBDeviceTransferTask _resume]"
- "-[MBXPCClient resumeDeviceTransferWithTaskType:error:]"
- "B20@0:8B16"
- "Beta"
- "CACHE_DELETE_AMOUNT"
- "CACHE_DELETE_URGENCY_LIMIT"
- "CACHE_DELETE_VOLUME"
- "Carrier"
- "DEBUG"
- "DEFAULT"
- "ERROR"
- "FAULT"
- "Failed to send KeyBagIsLocking message to backupd: %@"
- "Failed to send KeyBagIsUnlocked message to backupd: %@"
- "HomeDomain"
- "INFO"
- "Library/Application Support/CloudDocs/backup"
- "Library/Application Support/CloudDocs/backup/"
- "Library/Application Support/FileProvider/backup"
- "Library/Application Support/FileProvider/backup/"
- "ReleaseType"
- "ValidateSignatureOnRestore"
- "_resume"
- "deleteSnapshotID:fromBackupUDID:error:"
- "getAppleIDsForBackupUDID:snapshotID:activeAppleID:error:"
- "getAppleIDsForBackupUDID:snapshotID:error:"
- "kMBMessageDeleteSnapshot"
- "kMBMessageGetAppleIDs"
- "kMBMessageKeyBagIsLocking"
- "kMBMessageKeyBagIsUnlocked"
- "kMBMessageResumeDeviceTransfer"
- "kMBMessageSaveKeybags"
- "kMBMessageSetRestoreSession"
- "kMBNotifyDaemonNextTimeKeyBagIsUnlocked %d (%@)"
- "keyBagIsLocking"
- "keyBagIsUnlocked"
- "must provide a valid backupUDID"
- "resumeDeviceTransfer"
- "resumeDeviceTransferWithTaskType:error:"
- "resumed"
- "saveKeybagsForBackupUDID:withError:"
- "setRestoreSessionWithBackupUDID:snapshotUUID:"
- "suspended"
- "v16@?0^{__CFDictionary=}8"
- "v20@?0C8^{os_log_message_s=QQQ**{timeval=qi}{timezone=ii}QQI**Q*Q**ICBQ*CC*}12"
- "validateSignatureOnRestoreWithDefaultValue:"

```
