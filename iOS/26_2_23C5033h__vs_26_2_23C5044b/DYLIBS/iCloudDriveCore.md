## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4257.60.5.0.1
-  __TEXT.__text: 0x31433c
+4257.60.9.0.0
+  __TEXT.__text: 0x3141c0
   __TEXT.__auth_stubs: 0x1b40
   __TEXT.__objc_methlist: 0x1a44c
   __TEXT.__const: 0x500
-  __TEXT.__cstring: 0x7dbe4
-  __TEXT.__oslogstring: 0x3c40f
-  __TEXT.__gcc_except_tab: 0x1a6a0
+  __TEXT.__cstring: 0x7dc32
+  __TEXT.__oslogstring: 0x3c3ae
+  __TEXT.__gcc_except_tab: 0x1a648
   __TEXT.__ustring: 0x88
-  __TEXT.__unwind_info: 0xa078
+  __TEXT.__unwind_info: 0xa070
   __TEXT.__objc_classname: 0x2b47
-  __TEXT.__objc_methname: 0x44a7e
+  __TEXT.__objc_methname: 0x44a4e
   __TEXT.__objc_methtype: 0x90b4
-  __TEXT.__objc_stubs: 0x2f500
+  __TEXT.__objc_stubs: 0x2f520
   __DATA_CONST.__got: 0x1718
   __DATA_CONST.__const: 0x9640
   __DATA_CONST.__objc_classlist: 0xa80

   __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0x2c00
   __AUTH_CONST.__cfstring: 0x22c60
-  __AUTH_CONST.__objc_const: 0x3d590
+  __AUTH_CONST.__objc_const: 0x3d560
   __AUTH_CONST.__objc_intobj: 0xbd0
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x28c8
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x1fb8
+  __DATA.__objc_ivar: 0x1fb4
   __DATA.__data: 0x2740
   __DATA.__bss: 0x210
   __DATA_DIRTY.__objc_data: 0x4038

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BE3D4695-F892-3B4F-9F5E-4883958C9709
-  Functions: 13650
-  Symbols:   44445
-  CStrings:  27823
+  UUID: 7088B059-4024-35CC-855A-48A64EB1B861
+  Functions: 13649
+  Symbols:   44440
+  CStrings:  27821
 
Symbols:
+ -[BRCAccountHandler handleDiskSpaceAndLoadAccountIfNeeded]
+ -[BRCAccountHandler handleDiskSpaceAndLoadAccountIfNeeded].cold.1
+ -[BRCAccountHandler handleDiskSpaceAndLoadAccountIfNeeded].cold.2
+ -[BRCSyncUpEnumerator _checkIfShouldDenylistForParentDirectoryFaultWithItem:needsDirFaultCheck:]
+ _objc_msgSend$_checkIfShouldDenylistForParentDirectoryFaultWithItem:needsDirFaultCheck:
+ _objc_msgSend$handleDiskSpaceAndLoadAccountIfNeeded
- -[BRCSyncUpEnumerator _checkIfShouldDenylistForParentDirectoryFaultWithItem:]
- -[_BRCOperation highPriorityWaitGroup]
- GCC_except_table480
- _OBJC_IVAR_$__BRCOperation._highPriorityWaitGroup
- ___46-[_BRCOperation blockOnHighPriorityOperation:]_block_invoke
- __brc_ipc_check_logged_status.cold.6
- __brc_ipc_check_logged_status.cold.7
- _objc_msgSend$_checkIfShouldDenylistForParentDirectoryFaultWithItem:
CStrings:
+ "-[BRCAccountHandler handleDiskSpaceAndLoadAccountIfNeeded]"
+ "-[BRCSyncUpEnumerator _checkIfShouldDenylistForParentDirectoryFaultWithItem:needsDirFaultCheck:]"
+ "_checkIfShouldDenylistForParentDirectoryFaultWithItem:needsDirFaultCheck:"
+ "handleDiskSpaceAndLoadAccountIfNeeded"
- "-[BRCSyncUpEnumerator _checkIfShouldDenylistForParentDirectoryFaultWithItem:]"
- "T@\"NSObject<OS_dispatch_group>\",R,N,V_highPriorityWaitGroup"
- "[WARNING] Returning error because iCloud Drive doesn't have enough disk space to be functional%@"
- "_checkIfShouldDenylistForParentDirectoryFaultWithItem:"
- "_highPriorityWaitGroup"
- "highPriorityWaitGroup"

```
