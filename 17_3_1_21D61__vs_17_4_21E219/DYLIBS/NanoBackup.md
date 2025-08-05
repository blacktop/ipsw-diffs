## NanoBackup

> `/System/Library/PrivateFrameworks/NanoBackup.framework/NanoBackup`

```diff

   __TEXT.__cstring: 0x615
   __TEXT.__gcc_except_tab: 0x1cc
   __TEXT.__oslogstring: 0x37d
-  __TEXT.__unwind_info: 0x240
+  __TEXT.__unwind_info: 0x244
   __TEXT.__objc_classname: 0x64
-  __TEXT.__objc_methname: 0x1568
+  __TEXT.__objc_methname: 0x157c
   __TEXT.__objc_methtype: 0x362
   __TEXT.__objc_stubs: 0x7c0
   __DATA_CONST.__got: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xb50
   __DATA_CONST.__objc_selrefs: 0x480
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x168
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x1d8
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x88
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x180
   __DATA.__bss: 0x18

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 809B8454-FF51-374B-8DF8-A27EF712E0BA
+  UUID: 52B1D832-964B-34AF-8DEE-C8E0DC587CCB
   Functions: 166
   Symbols:   603
-  CStrings:  405
+  CStrings:  406
 
Symbols:
+ ___23-[NBManager connection]_block_invoke.82
+ ___26-[NBManager deleteBackup:]_block_invoke.137
+ ___44-[NBManager deleteBackup:completionHandler:]_block_invoke.133
+ ___44-[NBManager deleteBackup:completionHandler:]_block_invoke.135
+ ___44-[NBManager deleteBackup:completionHandler:]_block_invoke_2.134
+ ___44-[NBManager deleteBackup:completionHandler:]_block_invoke_2.136
+ ___46-[NBManager createManualBackupWithCompletion:]_block_invoke.129
+ ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke.93
+ ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke.95
+ ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke_2.94
+ ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke.123
+ ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke.125
+ ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke_2.124
+ ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke_2.127
+ ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke.88
+ ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke.91
+ ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke_2.90
+ ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke.103
+ ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke.105
+ ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke_2.104
+ ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke_2.106
+ ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke.113
+ ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke.115
+ ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke_2.114
+ ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke_2.116
+ ___64-[NBManager listBackupsOfType:withSynchronousCompletionHandler:]_block_invoke.96
+ ___67-[NBManager createBackupForPairingID:synchronousCompletionHandler:]_block_invoke.128
+ ___block_literal_global.80
- ___23-[NBManager connection]_block_invoke.80
- ___26-[NBManager deleteBackup:]_block_invoke.136
- ___44-[NBManager deleteBackup:completionHandler:]_block_invoke.132
- ___44-[NBManager deleteBackup:completionHandler:]_block_invoke.134
- ___44-[NBManager deleteBackup:completionHandler:]_block_invoke_2.133
- ___44-[NBManager deleteBackup:completionHandler:]_block_invoke_2.135
- ___46-[NBManager createManualBackupWithCompletion:]_block_invoke.128
- ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke.92
- ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke.94
- ___49-[NBManager setBackupsEnabled:completionHandler:]_block_invoke_2.93
- ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke.122
- ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke.124
- ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke_2.123
- ___56-[NBManager createBackupForPairingID:completionHandler:]_block_invoke_2.126
- ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke.86
- ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke.90
- ___57-[NBManager listBackupsOfType:timeout:completionHandler:]_block_invoke_2.89
- ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke.102
- ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke.104
- ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke_2.103
- ___59-[NBManager restoreFromBackup:forDevice:completionHandler:]_block_invoke_2.105
- ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke.112
- ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke.114
- ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke_2.113
- ___59-[NBManager restoreFromDevice:forDevice:completionHandler:]_block_invoke_2.115
- ___64-[NBManager listBackupsOfType:withSynchronousCompletionHandler:]_block_invoke.95
- ___67-[NBManager createBackupForPairingID:synchronousCompletionHandler:]_block_invoke.127
- ___block_literal_global.79
CStrings:
+ "T@\"NSString\",?,R,C"

```
