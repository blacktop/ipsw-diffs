## webbookmarksd

> `/usr/libexec/webbookmarksd`

```diff

-7623.2.7.10.4
-  __TEXT.__text: 0x1753c
-  __TEXT.__auth_stubs: 0xab0
-  __TEXT.__objc_stubs: 0x3a20
-  __TEXT.__objc_methlist: 0xc94
+7624.1.11.10.3
+  __TEXT.__text: 0x18c88
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_stubs: 0x3b40
+  __TEXT.__objc_methlist: 0xd14
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x5fc
-  __TEXT.__objc_methname: 0x4636
-  __TEXT.__cstring: 0xeda
-  __TEXT.__oslogstring: 0x228d
-  __TEXT.__objc_classname: 0x274
+  __TEXT.__gcc_except_tab: 0x654
+  __TEXT.__objc_methname: 0x4805
+  __TEXT.__cstring: 0xf44
+  __TEXT.__oslogstring: 0x2318
+  __TEXT.__objc_classname: 0x2be
   __TEXT.__objc_methtype: 0x6a3
-  __TEXT.__unwind_info: 0x6e0
-  __DATA_CONST.__auth_got: 0x570
-  __DATA_CONST.__got: 0x710
-  __DATA_CONST.__const: 0x11e8
-  __DATA_CONST.__cfstring: 0x6a0
-  __DATA_CONST.__objc_classlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x48
+  __TEXT.__unwind_info: 0x6f8
+  __DATA_CONST.__auth_got: 0x578
+  __DATA_CONST.__got: 0x7f0
+  __DATA_CONST.__const: 0x1210
+  __DATA_CONST.__cfstring: 0x6e0
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x1118
-  __DATA.__objc_selrefs: 0x1118
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__objc_data: 0x3c0
-  __DATA.__data: 0x368
+  __DATA.__objc_const: 0x11f8
+  __DATA.__objc_selrefs: 0x1160
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_data: 0x410
+  __DATA.__data: 0x3c8
   __DATA.__bss: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/BrowserEngineCore.framework/BrowserEngineCore

   - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C374324C-7E6A-3F92-9CE6-75B5183F390E
-  Functions: 481
-  Symbols:   413
-  CStrings:  1030
+  UUID: EC248AC8-3516-381D-80E7-97450C8AD448
+  Functions: 507
+  Symbols:   442
+  CStrings:  1051
 
Symbols:
+ _OBJC_CLASS_$_WBSScopeTimeoutHandler
+ _WBSHistoryTombstoneMakeAttributes
+ __WBSRunOnceImpl
+ _dispatch_block_create
+ _kWebBookmarksBrowserDataExchangeBookmarksExportFinishedMessageName
+ _kWebBookmarksBrowserDataExchangeExportBookmarksFolderIdentifierKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksIdentifierKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksIsFolderKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksMessageName
+ _kWebBookmarksBrowserDataExchangeExportBookmarksTitleKey
+ _kWebBookmarksBrowserDataExchangeExportBookmarksURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryHttpGetKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryLoadSuccessfulKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryMessageName
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectDestinationURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectDestinationVisitTimeKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectSourceURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryRedirectSourceVisitTimeKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryTitleKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryURLStringKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryVisitCountKey
+ _kWebBookmarksBrowserDataExchangeExportHistoryVisitTimeKey
+ _kWebBookmarksBrowserDataExchangeExportReadingListDateOfLastVisitKey
+ _kWebBookmarksBrowserDataExchangeExportReadingListMessageName
+ _kWebBookmarksBrowserDataExchangeExportReadingListTitleKey
+ _kWebBookmarksBrowserDataExchangeExportReadingListURLStringKey
+ _kWebBookmarksBrowserDataExchangeHistoryExportFinishedMessageName
+ _kWebBookmarksBrowserDataExchangeReadingListExportFinishedMessageName
+ _kWebBookmarksExportReadingListMessageName
+ _kWebBookmarksExportReadingListSandboxExtensionKey
+ _kWebBookmarksExportReadingListURLKey
+ _objc_retainAutoreleasedReturnValue
+ _objc_sync_enter
+ _objc_sync_exit
+ _xpc_dictionary_set_double
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x4
- _objc_retain_x5
- _os_transaction_needs_more_time
CStrings:
+ "%d"
+ "Error exporting reading list: %{public}@"
+ "Export Bookmarks"
+ "Export History"
+ "Export Reading List"
+ "Timed out when fetching all identifiers"
+ "Timeout performing operation on data store %@"
+ "Unable to connect to the history database: %{public}@"
+ "Unable to export history: %{public}@"
+ "WBSHistoryExporterProtocol"
+ "WebBookmarksBrowserDataExchangeHistoryExporter"
+ "_connection:exportBookmarksForBrowserDataExchangeWithMessage:"
+ "_connection:exportHistoryForBrowserDataExchangeWithMessage:"
+ "_connection:exportReadingListForBrowserDataExchangeWithMessage:"
+ "_connection:exportReadingListWithMessage:"
+ "_exportBookmarksWithConnection:collection:folder:parentFolderIdentifier:"
+ "addEntryWithURLString:visitTime:title:loadSuccessful:httpGet:redirectSourceURLString:redirectSourceVisitTime:redirectDestinationURLString:redirectDestinationVisitTime:visitCount:"
+ "allProfileIdentifiers"
+ "clearHistoryVisitsAddedAfterDate:beforeDate:tombstoneMode:tombstoneAttributes:clearAllSpotlightHistoryForProfile:completionHandler:"
+ "com.apple.private.webbookmarks.browserdataexchange"
+ "dateLastViewed"
+ "defaultStore"
+ "initWithTimeout:handler:"
+ "initWithURL:readingList:error:"
+ "readingListFolder"
+ "stringWithFormat:"
- "Clearing all history"
- "Failed to connect to default history database: %{public}@"
- "_clearAllHistory"
- "_connection:clearAllSafariHistoryWithMessage:"
- "clearAllHistoryInsertingTombstoneUpToDate:clearAllSpotlightHistoryForProfile:completionHandler:"
- "clearHistoryVisitsAddedAfterDate:beforeDate:tombstoneMode:clearAllSpotlightHistoryForProfile:completionHandler:"
- "isReadingListFolder"

```
