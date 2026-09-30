## iCloudDriveCore

> `/System/Library/PrivateFrameworks/iCloudDriveCore.framework/iCloudDriveCore`

```diff

-4479.100.98.0.2
-  __TEXT.__text: 0x321658
+4479.100.103.0.0
+  __TEXT.__text: 0x321adc
   __TEXT.__auth_stubs: 0x1a90
   __TEXT.__objc_methlist: 0x1aa7c
   __TEXT.__const: 0x4e0
-  __TEXT.__cstring: 0x7e0ab
-  __TEXT.__oslogstring: 0x3b6dc
-  __TEXT.__gcc_except_tab: 0x19f70
+  __TEXT.__cstring: 0x7e0ad
+  __TEXT.__oslogstring: 0x3b864
+  __TEXT.__gcc_except_tab: 0x19f98
   __TEXT.__ustring: 0x36
   __TEXT.__unwind_info: 0xa7e8
   __TEXT.__objc_classname: 0x2ae4
-  __TEXT.__objc_methname: 0x45c08
+  __TEXT.__objc_methname: 0x45c09
   __TEXT.__objc_methtype: 0x94d2
   __TEXT.__objc_stubs: 0x2fca0
   __DATA_CONST.__got: 0x1728

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B009B0A0-B25D-31D0-A84D-8ACB652CC74D
-  Functions: 13778
-  Symbols:   45373
-  CStrings:  27852
+  UUID: B92CC907-D3E5-3437-8578-48BEE6FB7441
+  Functions: 13779
+  Symbols:   45379
+  CStrings:  27857
 
Symbols:
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.1
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.2
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.3
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.4
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.5
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.6
+ -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:].cold.7
+ ___90-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]_block_invoke
+ ___90-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]_block_invoke.cold.1
+ _objc_msgSend$handlePathMatchConflictForDirectoryCreationIfNecessary:
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary]
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary].cold.1
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary].cold.2
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary].cold.3
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary].cold.4
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary].cold.5
- -[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary].cold.6
- ___89-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary]_block_invoke
- ___89-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary]_block_invoke.cold.1
- _objc_msgSend$handlePathMatchConflictForDirectoryCreationIfNecessary
CStrings:
+ "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]"
+ "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary:]_block_invoke"
+ "[CRIT] Assertion failed: self.db.isBatchSuspended%@"
+ "[CRIT] UNREACHABLE: Can't merge into a folder which is not live / in trash / already accepting a merge %@%@"
+ "[DEBUG] Item is eligible for revive but has a processing stamp, cannot proceed with creation: %@%@"
+ "[ERROR] Failed to handle path match conflict during cross-zone move for %@: %@%@"
+ "[ERROR] Failed to handle path match conflict for directory %@: %@%@"
+ "[WARNING] Unable to path-match item successfully. Marking as failed%@"
+ "handlePathMatchConflictForDirectoryCreationIfNecessary:"
- "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary]"
- "-[BRCDirectoryItem(FPFSAdditions) handlePathMatchConflictForDirectoryCreationIfNecessary]_block_invoke"
- "[CRIT] UNREACHABLE: Can't merge into a folder which is already accepting a merge %@%@"
- "handlePathMatchConflictForDirectoryCreationIfNecessary"

```
