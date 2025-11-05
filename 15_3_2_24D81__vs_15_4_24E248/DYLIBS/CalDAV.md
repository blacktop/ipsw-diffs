## CalDAV

> `/System/Library/PrivateFrameworks/CalDAV.framework/Versions/A/CalDAV`

```diff

 1149.0.0.0.0
-  __TEXT.__text: 0x3d208
+  __TEXT.__text: 0x3d588
   __TEXT.__auth_stubs: 0x310
-  __TEXT.__objc_methlist: 0x46a0
+  __TEXT.__objc_methlist: 0x4f0c
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x9d8
   __TEXT.__cstring: 0x1eb1
   __TEXT.__oslogstring: 0x19e6
-  __TEXT.__unwind_info: 0xc00
+  __TEXT.__unwind_info: 0xc10
   __TEXT.__objc_classname: 0xf30
   __TEXT.__objc_methname: 0xbfc1
   __TEXT.__objc_methtype: 0xe6b

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b48
+  __DATA_CONST.__objc_selrefs: 0x2c18
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x258
   __AUTH_CONST.__auth_got: 0x198
   __AUTH_CONST.__const: 0x670
   __AUTH_CONST.__cfstring: 0x3160
-  __AUTH_CONST.__objc_const: 0xaec8
+  __AUTH_CONST.__objc_const: 0x9eb8
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x61c
   __DATA.__data: 0x538

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: FFD0EF6B-06CA-375D-A46B-6DBF7C754CC9
-  Functions: 1505
-  Symbols:   4355
+  UUID: 4575652B-A4F4-3240-9136-8EE27EBCD375
+  Functions: 1534
+  Symbols:   4389
   CStrings:  3223
 
Symbols:
+ +[CalDAVConcreteServerVersion prototypes].cold.1
+ -[CalDAVCalendarPropertyRefreshOperation _finishRefresh].cold.1
+ -[CalDAVCalendarSyncOperation _distantFutureEndDate].cold.1
+ -[CalDAVCalendarSyncOperation copyAllLocalURLsInFolderWithURL:].cold.1
+ -[CalDAVCalendarSyncOperation copyLocalETagsForURLs:inFolderWithURL:].cold.1
+ -[CalDAVCalendarSyncOperation setLocalETag:forItemWithURL:inFolderWithURL:].cold.1
+ -[CalDAVCalendarSyncOperation setLocalScheduleTag:forItemWithURL:inFolderWithURL:].cold.1
+ -[CalDAVContainerSyncTaskGroup copyGetEtagTaskWithPropertiesToFind:].cold.1
+ -[CalDAVOperation dealloc].cold.1
+ -[CalDAVPostStreamTask utf8PercentEscapedFilename].cold.1
+ -[CalDAVServerVersion _propertiesToComplianceClasses].cold.1
+ -[NSString(CALIDExtensions) stringByEncodingSlashes].cold.1
+ -[NSString(DAVExtensions) stringByURLQuotingPaths].cold.1
+ -[NSString(DAVExtensions) stringByURLQuoting].cold.1
+ -[NSURL(DAVExtensions) initWithDirtyString:].cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ __113-[CalDAVCalendarSyncOperation containerSyncTask:completedWithNewCTag:newSyncToken:addedOrModified:removed:error:]_block_invoke.cold.1
+ __63-[CalDAVCalendarPropertyRefreshOperation _sendAddsForCalendars]_block_invoke.cold.1
+ __63-[CalDAVCalendarPropertyRefreshOperation _sendAddsForCalendars]_block_invoke.cold.2
+ __64-[CalDAVCalendarPropertyRefreshOperation _handleCalendarPublish]_block_invoke.32.cold.1
+ __64-[CalDAVCalendarPropertyRefreshOperation _handleCalendarPublish]_block_invoke.32.cold.2
+ __66-[CalDAVCalendarPropertyRefreshOperation _sendDeletesForCalendars]_block_invoke_2.cold.1
+ __66-[CalDAVCalendarPropertyRefreshOperation _sendDeletesForCalendars]_block_invoke_2.cold.2
+ __67-[CalDAVCalendarPropertyRefreshOperation refreshCalendarProperties]_block_invoke_2.cold.1
+ __67-[CalDAVCalendarPropertyRefreshOperation refreshCalendarProperties]_block_invoke_2.cold.2
+ __72-[CalDAVCalendarPropertyRefreshOperation _prepareCalendarsBeforeRefresh]_block_invoke.cold.1
+ __90-[CalDAVCalendarPropertyRefreshOperation containerInfoTask:completedWithContainers:error:]_block_invoke.cold.1
+ __90-[CalDAVCalendarPropertyRefreshOperation containerInfoTask:completedWithContainers:error:]_block_invoke.cold.2
+ scheduleChangesLogHandle.cold.1

```
