## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2899.0.11.0.0
-  __TEXT.__text: 0x3066c
+2899.40.32.0.0
+  __TEXT.__text: 0x306cc
   __TEXT.__auth_stubs: 0xde0
   __TEXT.__objc_methlist: 0x4014
   __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x7e3d
-  __TEXT.__gcc_except_tab: 0x1424
-  __TEXT.__oslogstring: 0x270c
-  __TEXT.__unwind_info: 0x1148
-  __TEXT.__objc_classname: 0x397
-  __TEXT.__objc_methname: 0x9d52
-  __TEXT.__objc_methtype: 0x11d1
-  __TEXT.__objc_stubs: 0x4b20
+  __TEXT.__cstring: 0x7d85
+  __TEXT.__gcc_except_tab: 0x144c
+  __TEXT.__oslogstring: 0x274b
+  __TEXT.__unwind_info: 0x1150
+  __TEXT.__objc_classname: 0x398
+  __TEXT.__objc_methname: 0x9dad
+  __TEXT.__objc_methtype: 0x11f7
+  __TEXT.__objc_stubs: 0x4ae0
   __DATA_CONST.__got: 0x3b0
   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2370
+  __DATA_CONST.__objc_selrefs: 0x2358
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x5cc0
-  __AUTH_CONST.__objc_const: 0x5348
+  __AUTH_CONST.__cfstring: 0x5b80
+  __AUTH_CONST.__objc_const: 0x5398
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x394
+  __DATA.__objc_ivar: 0x3a0
   __DATA.__data: 0x308
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5BCFA01F-AD0A-3690-9FC9-1488B428E14A
+  UUID: 631E02EE-0544-3752-9829-3DB22CEC09A3
   Functions: 1590
-  Symbols:   4937
-  CStrings:  3910
+  Symbols:   4939
+  CStrings:  3890
 
Symbols:
+ -[MBBackgroundRestoreInfo commitID]
+ -[MBBackgroundRestoreInfo initWithDataClassesRemaining:bytesRemaining:failedDomains:recentATCErrors:perClassItemsRemaining:airTrafficDidFinishRestore:appDataDidFinishRestore:snapshotFormat:snapshotID:commitID:]
+ -[MBBackgroundRestoreInfo setCommitID:]
+ -[MBBackgroundRestoreInfo setSnapshotFormat:]
+ -[MBBackgroundRestoreInfo setSnapshotID:]
+ -[MBBackgroundRestoreInfo snapshotFormat]
+ -[MBBackgroundRestoreInfo snapshotID]
+ -[MBXPCClient passcodeChanged]
+ GCC_except_table108
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table139
+ GCC_except_table95
+ GCC_except_table98
+ _OBJC_IVAR_$_MBBackgroundRestoreInfo._commitID
+ _OBJC_IVAR_$_MBBackgroundRestoreInfo._snapshotFormat
+ _OBJC_IVAR_$_MBBackgroundRestoreInfo._snapshotID
+ ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.183
+ ___block_literal_global.133
+ ___block_literal_global.289
+ ___block_literal_global.297
+ _objc_msgSend$initWithDataClassesRemaining:bytesRemaining:failedDomains:recentATCErrors:perClassItemsRemaining:airTrafficDidFinishRestore:appDataDidFinishRestore:snapshotFormat:snapshotID:commitID:
- -[MBBehaviorOptions dryRestoreGBAllowance]
- -[MBBehaviorOptions dryRestoreInterval]
- -[MBBehaviorOptions setDryRestoreGBAllowance:]
- -[MBBehaviorOptions setDryRestoreInterval:]
- -[MBManager dryRestore:snapshotUUID:error:]
- -[MBPersona dryRestoreContentDirectory]
- -[MBPersona dryRestoreMetadataDirectory]
- -[MBXPCClient dryRestore:snapshotUUID:error:]
- GCC_except_table110
- GCC_except_table121
- GCC_except_table123
- GCC_except_table125
- GCC_except_table127
- GCC_except_table134
- GCC_except_table96
- GCC_except_table99
- ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.189
- ___block_literal_global.142
- ___block_literal_global.285
- ___block_literal_global.293
- _objc_msgSend$setBytesRemaining:
- _objc_msgSend$setDataClassesRemaining:
- _objc_msgSend$setFailedDomains:
CStrings:
+ "@84@0:8i16Q20@28@36@44B52B56q60@68@76"
+ "Failed to send passcode message to backupd: %@"
+ "T@\"NSArray\",&,N,V_failedDomains"
+ "T@\"NSDictionary\",&,N,V_perClassItemsRemaining"
+ "T@\"NSDictionary\",&,N,V_recentATCErrors"
+ "T@\"NSString\",&,N,V_snapshotID"
+ "T@\"NSString\",R,N,V_backupBuildVersion"
+ "T@\"NSString\",R,N,V_deviceBuildVersion"
+ "TB,R,N,V_wasCloudRestore"
+ "TQ,N,V_bytesRemaining"
+ "Ti,N,V_dataClassesRemaining"
+ "Tq,N,V_snapshotFormat"
+ "_snapshotFormat"
+ "bytesRemaining:%llu, dataClassesRemaining:0x%x, failedDomains:%@ format:%@"
+ "initWithDataClassesRemaining:bytesRemaining:failedDomains:recentATCErrors:perClassItemsRemaining:airTrafficDidFinishRestore:appDataDidFinishRestore:snapshotFormat:snapshotID:commitID:"
+ "kMBMessagePasscodeChanged"
+ "passcodeChanged"
+ "setSnapshotFormat:"
+ "snapshotFormat"
- "Beta"
- "Carrier"
- "DryRestoreGBAllowance"
- "DryRestoreInterval"
- "NSString *MBStringForBackupReason(MBBackupReason)"
- "ReleaseType"
- "T@\"NSArray\",&,V_failedDomains"
- "T@\"NSDate\",R,V_date"
- "T@\"NSMutableDictionary\",&,V_perClassItemsRemaining"
- "T@\"NSMutableDictionary\",&,V_recentATCErrors"
- "T@\"NSNumber\",&,N"
- "T@\"NSString\",R,V_backupBuildVersion"
- "T@\"NSString\",R,V_deviceBuildVersion"
- "TB,R,V_wasCloudRestore"
- "TQ,V_bytesRemaining"
- "Ti,V_dataClassesRemaining"
- "Unknown backup reason %lu"
- "bytesRemaining:%llu, dataClassesRemaining:0x%x, failedDomains:%@"
- "dryRestore:snapshotUUID:error:"
- "dryRestoreContentDirectory"
- "dryRestoreGBAllowance"
- "dryRestoreInterval"
- "dryRestoreMetadataDirectory"
- "dry_restore_content"
- "dry_restore_metadata"
- "kMBMessageDryRestore"
- "kMBMessageDryRestoreAllowance"
- "kMBMessageDryRestoreSnapshotUUID"
- "setDryRestoreGBAllowance:"
- "setDryRestoreInterval:"

```
