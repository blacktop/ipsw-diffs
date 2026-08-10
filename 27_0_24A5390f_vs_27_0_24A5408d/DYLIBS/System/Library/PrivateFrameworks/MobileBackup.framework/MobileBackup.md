## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3039.0.1.0.0
-  __TEXT.__text: 0x2e0c8
-  __TEXT.__objc_methlist: 0x3e84
+3039.2.2.0.0
+  __TEXT.__text: 0x2e290
+  __TEXT.__objc_methlist: 0x3ea4
   __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x7a30
+  __TEXT.__cstring: 0x7a5b
   __TEXT.__gcc_except_tab: 0x1200
   __TEXT.__oslogstring: 0x265e
-  __TEXT.__unwind_info: 0x10c8
+  __TEXT.__unwind_info: 0x10d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x148
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2270
+  __DATA_CONST.__objc_selrefs: 0x2280
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa0
   __DATA_CONST.__got: 0x3b0
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x56e0
-  __AUTH_CONST.__objc_const: 0x5288
+  __AUTH_CONST.__cfstring: 0x5700
+  __AUTH_CONST.__objc_const: 0x52d8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x6e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1570
-  Symbols:   3170
-  CStrings:  1138
+  Functions: 1572
+  Symbols:   3175
+  CStrings:  1139
 
Symbols:
+ -[CoreTelephonyClient(BackupOnCellularSupport) mb_backupOnCellularSupport:cellularRadioType:error:]
+ -[MBBehaviorOptions d2dBackgroundDisconnectTimeout]
+ -[MBBehaviorOptions d2dFileTransferDisconnectTimeout]
+ -[MBXPCClient _fetchBackupOnCellularSupportWithCaching]
+ __OBJC_$_CATEGORY_CoreTelephonyClient_$_BackupOnCellularSupport
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CoreTelephonyClient_$_BackupOnCellularSupport
+ ___55-[MBXPCClient _fetchBackupOnCellularSupportWithCaching]_block_invoke
+ _objc_msgSend$_fetchBackupOnCellularSupportWithCaching
+ _objc_msgSend$mb_backupOnCellularSupport:cellularRadioType:error:
- -[MBBehaviorOptions d2dTransferDisconnectTimeout]
- -[MBXPCClient _backupOnCellularSupport]
- ___39-[MBXPCClient _backupOnCellularSupport]_block_invoke
- _objc_msgSend$_backupOnCellularSupport
Functions:
~ -[MBCellularDataSubscriptionMonitor _backupOnCellularSupportWithError:] : 2248 -> 220
+ -[CoreTelephonyClient(BackupOnCellularSupport) mb_backupOnCellularSupport:cellularRadioType:error:]
~ -[MBXPCClient backupOnCellularSupportWithAccount:error:] : 96 -> 276
+ -[MBBehaviorOptions d2dBackgroundDisconnectTimeout]
CStrings:
+ "D2DBackgroundDisconnectTimeout"
+ "D2DFileTransferDisconnectTimeout"
- "D2DDisconnectTimeout"
```
