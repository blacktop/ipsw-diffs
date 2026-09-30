## DADaemonSupport

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DADaemonSupport.framework/Versions/A/DADaemonSupport`

```diff

-2673.0.0.0.0
-  __TEXT.__text: 0x39e08
+2673.5.2.0.0
+  __TEXT.__text: 0x3a3cc
   __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x2014
+  __TEXT.__objc_methlist: 0x2580
   __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x7e4
   __TEXT.__oslogstring: 0x5fc1
   __TEXT.__cstring: 0x11e9
-  __TEXT.__unwind_info: 0xae8
+  __TEXT.__unwind_info: 0xb08
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x6fd
   __TEXT.__objc_methname: 0x7c74

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1de0
+  __DATA_CONST.__objc_selrefs: 0x1f08
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x560
   __AUTH_CONST.__const: 0x9f0
   __AUTH_CONST.__cfstring: 0xd60
-  __AUTH_CONST.__objc_const: 0x6e30
+  __AUTH_CONST.__objc_const: 0x64e0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x870

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F8E2690-D03B-311A-BBC4-EDC065245537
-  Functions: 897
-  Symbols:   2968
+  UUID: DE0D4237-1634-3074-8486-04A9DED5189E
+  Functions: 934
+  Symbols:   3006
   CStrings:  2091
 
Symbols:
+ +[DADAgentManager sharedManager].cold.1
+ +[DADClient permissionsForMessage:].cold.1
+ +[DADMain sharedMain].cold.1
+ +[DAReachability sharedReachability].cold.1
+ +[DARefreshManager sharedManager].cold.1
+ -[DADAgentManager _clearOrphanedStoresAndTrafficLogFiles].cold.1
+ -[DADAgentManager _clearOrphanedStoresAndTrafficLogFiles].cold.2
+ -[DADAgentManager _hasDataclassWeCareAbout:].cold.1
+ -[DADAgentManager removePendingAccountSetup].cold.1
+ -[DADClient _beginDownloadingAttachmentEvent:eventDict:].cold.1
+ -[DADClient _beginDownloadingAttachmentEvent:eventDict:].cold.2
+ -[DADClient _cancelDownloadingAttachmentEvent:eventDict:].cold.1
+ -[DADClient _checkIsOofSettingsSupported:].cold.1
+ -[DADClient _openServerContactsSearch:].cold.1
+ -[DADClient _openServerContactsSearch:].cold.2
+ -[DADClient _openServerOofSettingsRequest:].cold.1
+ -[DADClient _performCalendarDirectorySearch:eventDict:].cold.1
+ -[DADClient _performGroupExpansion:eventDict:].cold.1
+ -[DADClient _performGroupExpansion:eventDict:].cold.2
+ -[DADClient _reportSharedCalendarAsJunkEvent:eventDict:].cold.1
+ -[DADClient _reportSharedCalendarAsJunkEvent:eventDict:].cold.2
+ -[DADClient _requestCalendarAvailability:eventDict:].cold.1
+ -[DADClient _requestCalendarAvailability:eventDict:].cold.2
+ -[DADClient _requestCalendarAvailability:eventDict:].cold.3
+ -[DADClient _requestGrantedDelegatesList:eventDict:].cold.1
+ -[DADClient _respondToSharedCalendarEvent:eventDict:].cold.1
+ -[DADClient _respondToSharedCalendarEvent:eventDict:].cold.2
+ -[DADClient _respondToSharedCalendarEvent:eventDict:].cold.3
+ -[DADClient _updateGrantedDelegatePermission:eventDict:].cold.1
+ -[DADClient _updateGrantedDelegatePermission:eventDict:].cold.2
+ -[DADClient _updateGrantedDelegatePermission:eventDict:].cold.3
+ -[DADClient applyClientStatusReportToAggregator:].cold.1
+ -[DADClient reconnectWithConnection:].cold.1
+ -[DARefreshManager _connectionForEnv:].cold.1
+ -[DARefreshManager establishAllApsConnections].cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __60-[DARefreshManager registerTopic:forDelegate:inEnvironment:]_block_invoke.cold.1

```
