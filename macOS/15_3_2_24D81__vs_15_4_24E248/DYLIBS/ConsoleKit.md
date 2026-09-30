## ConsoleKit

> `/System/Library/PrivateFrameworks/ConsoleKit.framework/Versions/A/ConsoleKit`

```diff

 8.4.1.0.0
-  __TEXT.__text: 0x678e4
+  __TEXT.__text: 0x673bc
   __TEXT.__auth_stubs: 0xa30
-  __TEXT.__objc_methlist: 0x6c90
+  __TEXT.__objc_methlist: 0x7a0c
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0x12c4
-  __TEXT.__cstring: 0x3dba
+  __TEXT.__gcc_except_tab: 0x12c0
+  __TEXT.__cstring: 0x3db2
   __TEXT.__oslogstring: 0x167d
   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x1bd0

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4518
+  __DATA_CONST.__objc_selrefs: 0x4938
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2b0
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__const: 0x1dd0
   __AUTH_CONST.__cfstring: 0x3e40
-  __AUTH_CONST.__objc_const: 0x12c98
+  __AUTH_CONST.__objc_const: 0x11400
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: EEEBAE67-B72F-357F-914A-DFAD94F6E822
-  Functions: 2718
-  Symbols:   7019
-  CStrings:  5202
+  UUID: A7CB012B-AF68-3613-9B2D-EC7A76B79F7A
+  Functions: 2740
+  Symbols:   7054
+  CStrings:  5198
 
Symbols:
+ +[CSKAuthenticationController sharedAuthenticator].cold.1
+ +[CSKDatabaseHandle sortIdentifierToDBColumnIdentifier:].cold.1
+ +[CSKDeviceManager sharedManager].cold.1
+ +[CSKEntity(CSKTableColumnLayoutAddings) csk_propertiesNameFromTableColumnIdentifiers:].cold.1
+ +[CSKFileSystem archiveFileExtensions].cold.1
+ +[CSKHelpers _timeStructFromDate:timeZone:usec:].cold.1
+ +[CSKHelpers _updateTimeZoneDateFormattersWithDate:timeZone:].cold.1
+ +[CSKHelpers formattedNumberFromUnsignedInteger:].cold.1
+ +[CSKLogging coalescerHandle].cold.1
+ +[CSKLogging deviceHandle].cold.1
+ +[CSKLogging deviceManagerHandle].cold.1
+ +[CSKLogging directoryObserverHandle].cold.1
+ +[CSKLogging fileObserverHandle].cold.1
+ +[CSKLogging fileSystemHandle].cold.1
+ +[CSKLogging fileTailObserverHandle].cold.1
+ +[CSKLogging streamASLSourceHandle].cold.1
+ +[CSKLogging streamArchiveSourceHandle].cold.1
+ +[CSKLogging streamDataAdditionTaskHandle].cold.1
+ +[CSKLogging streamDataDirectionModifierTaskHandle].cold.1
+ +[CSKLogging streamDataHandle].cold.1
+ +[CSKLogging streamDataRemovalTaskHandle].cold.1
+ +[CSKLogging streamDataTaskHandle].cold.1
+ +[CSKLogging streamDeviceSourceHandle].cold.1
+ +[CSKLogging streamFiltersPredicateHandle].cold.1
+ +[CSKLogging streamHandle].cold.1
+ +[CSKLogging streamObserverTaskHandle].cold.1
+ +[CSKLogging streamSourceHandle].cold.1
+ +[CSKLogging streamTaskOperationHandle].cold.1
+ +[CSKLogging streamTasksSchedulerHandle].cold.1
+ +[NSImage(CSKAssets) csk_sidebarGenericFileIcon].cold.1
+ +[NSImage(CSKAssets) csk_sidebarGenericFolderIcon].cold.1
+ +[NSImage(CSKAssets) csk_sidebarMacIcon].cold.1
+ -[CSKTableColumnLayout layoutColumnCanBeResizedWithIdentifier:].cold.1
+ -[CSKTableColumnLayout layoutColumnSortDescriptorForColumnWithIdentifier:].cold.1
+ -[NSTableView(CSKTableColumnLayout) _csk_isColumnIdentifierValid:].cold.1
- _OUTLINED_FUNCTION_5
CStrings:
- "s"

```
