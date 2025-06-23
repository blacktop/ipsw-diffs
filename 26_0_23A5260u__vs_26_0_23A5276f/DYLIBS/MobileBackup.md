## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2877.0.0.0.0
-  __TEXT.__text: 0x3005c
+2891.0.0.0.0
+  __TEXT.__text: 0x3046c
   __TEXT.__auth_stubs: 0xde0
   __TEXT.__objc_methlist: 0x3ff4
   __TEXT.__const: 0x590
-  __TEXT.__cstring: 0x7c74
-  __TEXT.__gcc_except_tab: 0x12d0
-  __TEXT.__oslogstring: 0x268e
-  __TEXT.__unwind_info: 0x10f8
+  __TEXT.__cstring: 0x7d2b
+  __TEXT.__gcc_except_tab: 0x1408
+  __TEXT.__oslogstring: 0x26f9
+  __TEXT.__unwind_info: 0x1128
   __TEXT.__objc_classname: 0x397
-  __TEXT.__objc_methname: 0x9ce5
+  __TEXT.__objc_methname: 0x9cff
   __TEXT.__objc_methtype: 0x11d1
   __TEXT.__objc_stubs: 0x4b20
   __DATA_CONST.__got: 0x3b0

   __AUTH_CONST.__auth_got: 0x700
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x5bc0
-  __AUTH_CONST.__objc_const: 0x5318
+  __AUTH_CONST.__objc_const: 0x5338
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x308
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0xcd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 73B17F14-EFB4-3965-A7C2-69D325AF2C7F
+  UUID: 64ECFC6A-1908-3B7E-99C0-24C979039B27
   Functions: 1587
-  Symbols:   4921
-  CStrings:  3885
+  Symbols:   4927
+  CStrings:  3891
 
Symbols:
+ GCC_except_table5
+ GCC_except_table6
+ GCC_except_table8
+ GCC_except_table9
+ _OBJC_IVAR_$_MBXPCClient._enabledOverCellularToken
Functions:
~ -[MBXPCClient initWithDelegate:eventQueue:personaIdentifier:] : 268 -> 280
~ -[MBXPCClient dealloc] : 184 -> 208
~ -[MBXPCClient isBackupOnCellularEnabledWithError:] : 180 -> 924
~ -[MBStateInfo encodeWithCoder:] : 248 -> 292
~ -[MBStateInfo copyWithZone:] : 108 -> 148
~ -[MBStateInfo setError:] : 188 -> 228
~ -[MBStateInfo dictionaryRepresentation] : 740 -> 804
~ -[MBStateInfo description] : 124 -> 196
CStrings:
+ "Fetched backup enabled over cellular notify state: 0x%llx"
+ "Fetched backup enabled over cellular via XPC: %d"
+ "_enabledOverCellularToken"
+ "com.apple.private.restrict-post.MobileBackup.BackupOverCellularEnabledState"

```
