## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/Versions/A/CalendarDaemon`

```diff

-1194.4.1.0.0
-  __TEXT.__text: 0x70c84
-  __TEXT.__auth_stubs: 0x33c0
-  __TEXT.__objc_methlist: 0x4b84
-  __TEXT.__cstring: 0x6ccd
-  __TEXT.__const: 0x150
+1194.5.6.0.0
+  __TEXT.__text: 0x70fe8
+  __TEXT.__auth_stubs: 0x33e0
+  __TEXT.__objc_methlist: 0x5b8c
+  __TEXT.__cstring: 0x6ce9
+  __TEXT.__const: 0x140
   __TEXT.__oslogstring: 0x7e09
-  __TEXT.__gcc_except_tab: 0x1a84
+  __TEXT.__gcc_except_tab: 0x1a74
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1910
+  __TEXT.__unwind_info: 0x1960
   __TEXT.__objc_classname: 0x13cf
-  __TEXT.__objc_methname: 0xd942
+  __TEXT.__objc_methname: 0xd9e0
   __TEXT.__objc_methtype: 0x6367
-  __TEXT.__objc_stubs: 0x8be0
+  __TEXT.__objc_stubs: 0x8c60
   __DATA_CONST.__got: 0x908
   __DATA_CONST.__const: 0x550
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c70
+  __DATA_CONST.__objc_selrefs: 0x2db0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x350
-  __AUTH_CONST.__auth_got: 0x19f0
-  __AUTH_CONST.__const: 0x22a0
-  __AUTH_CONST.__cfstring: 0x7500
-  __AUTH_CONST.__objc_const: 0xd138
-  __AUTH_CONST.__objc_intobj: 0x3d8
+  __AUTH_CONST.__auth_got: 0x1a00
+  __AUTH_CONST.__const: 0x22c0
+  __AUTH_CONST.__cfstring: 0x7540
+  __AUTH_CONST.__objc_const: 0xb588
+  __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2580
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x6f8
+  __DATA.__objc_ivar: 0x700
   __DATA.__data: 0x1668
-  __DATA.__bss: 0x2c8
+  __DATA.__bss: 0x2d8
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: FC3EDB3C-4CEA-3EFE-B527-68384735C911
-  Functions: 2030
-  Symbols:   6336
-  CStrings:  5249
+  UUID: 67DAA8B4-9C46-3922-B314-300203F10DAA
+  Functions: 2069
+  Symbols:   6393
+  CStrings:  5262
 
Symbols:
+ +[CADBirthdayListener sharedListener].cold.1
+ +[CADDefaultAppProtectionGuard shared].cold.1
+ +[CADNullAppProtectionGuard shared].cold.1
+ +[CADRealCalendarDatabaseDataProvider realDataProvider].cold.1
+ +[CADSpotlightIndexer _entityTypesThatAffectSpotlightIndexing].cold.1
+ +[CADSpotlightLogger _logWithFormat:args:prependErrorMarker:].cold.1
+ +[CalDAVTrafficLogScrubber log].cold.1
+ +[ClientConnection poolManager].cold.1
+ -[CADCombinedPermissionValidator canAccessProcedureAlarms]
+ -[CADCombinedPermissionValidator isAutomatorApp]
+ -[CADCombinedPermissionValidator isShortcutsApp]
+ -[CADCompoundFilter extendWhereClause:usingOperation:withValues:andTypes:].cold.1
+ -[CADDefaultPermissionValidator canAccessProcedureAlarms]
+ -[CADDefaultPermissionValidator isAutomatorApp]
+ -[CADDefaultPermissionValidator isShortcutsApp]
+ -[CADEntityWrapper encodeWithCoder:].cold.1
+ -[CADEntityWrapper initWithCoder:].cold.1
+ -[CADEntityWrapper initWithCoder:].cold.2
+ -[CADEventPredicate defaultPropertiesToLoad].cold.1
+ -[CADEventPredicate predicateFormat].cold.1
+ -[CADLocalXPCConnection auditToken].cold.1
+ -[CADLocalXPCConnection processIdentifier].cold.1
+ -[CADMockPermissionValidator canAccessProcedureAlarms]
+ -[CADMockPermissionValidator isAutomatorApp]
+ -[CADMockPermissionValidator isShortcutsApp]
+ -[CADMockPermissionValidator setCanAccessProcedureAlarms:]
+ -[CADMockPermissionValidator setIsAutomatorApp:]
+ -[CADMockPermissionValidator setIsShortcutsApp:]
+ -[CADOperationProxy initWithClientConnection:].cold.1
+ -[CADSequenceToken initWithCoder:].cold.1
+ -[CADXPCImplementation accessGrantedToPerformSelector:].cold.1
+ -[CADXPCImplementation(CADDatabaseOperationGroup) _verifyClientAllowedToWriteValue:forKey:].cold.1
+ -[CADXPCProxyHelper _callReplyHandler:ofInvocation:withErrorCode:].cold.1
+ -[CalDAVTrafficLogScrubber scrub].cold.3
+ -[CalDAVTrafficLogScrubber scrub].cold.4
+ -[CalDAVTrafficLogScrubber scrub].cold.5
+ -[CalXMLElementRedactionRule redactionRuleForAttribute:].cold.1
+ -[CalXMLSanitizer currentRedactionRule].cold.1
+ -[CalXMLSanitizer flushContents].cold.1
+ -[EKPredicate initWithCoder:].cold.1
+ CADLogInitIfNeeded.cold.1
+ CalRequestAuthorizationForServiceWithCompletion.cold.1
+ GCC_except_table106
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table124
+ GetSharedXPCInterfaceForCADClientInterface.cold.1
+ GetSharedXPCInterfaceForCADInterface.cold.1
+ OBJC_IVAR_$_CADMockPermissionValidator._canAccessProcedureAlarms
+ OBJC_IVAR_$_CADMockPermissionValidator._isAutomatorApp
+ OBJC_IVAR_$_CADMockPermissionValidator._isShortcutsApp
+ _CalEventCopySuggestedEventInfo
+ _CalSuggestedEventInfoCopyExtractionGroupIdentifier
+ _EKAlarmProperty_urlWrapper
+ _EKAttachmentProperty_localRelativePath
+ _OBJC_CLASS_$_CalOpenFileURLWrapper
+ __103-[CADXPCImplementation(CADDatabaseOperationGroup) CADDatabaseMigrateSubscribedCalendar:toSource:reply:]_block_invoke.65
+ __36-[CADServer _registerForAlarmEvents]_block_invoke.cold.1
+ __59-[CADLocalXPCProxyObject _forwardInvocationAsynchronously:]_block_invoke.cold.1
+ ___91-[CADXPCImplementation(CADDatabaseOperationGroup) _verifyClientAllowedToWriteValue:forKey:]_block_invoke
+ __block_literal_global.360
+ _objc_msgSend$canAccessProcedureAlarms
+ _objc_msgSend$isAutomatorApp
+ _objc_msgSend$isShortcutsApp
+ _objc_msgSend$setEventIsCancelled:
+ _objc_msgSend$setEventMessageIdentifier:
+ _resourceChangeDeletionQueue.cold.1
+ _verifyClientAllowedToWriteValue:forKey:.onceToken
+ _verifyClientAllowedToWriteValue:forKey:.protectedKeys
+ getCADXPCProxyHelperLogHandle.cold.1
- -[CADCombinedPermissionValidator canAccessDatabaseBookmarks]
- -[CADDefaultPermissionValidator canAccessDatabaseBookmarks]
- -[CADMockPermissionValidator canAccessDatabaseBookmarks]
- -[CADMockPermissionValidator setCanAccessDatabaseBookmarks:]
- GCC_except_table105
- GCC_except_table115
- GCC_except_table118
- GCC_except_table121
- GCC_except_table123
- OBJC_IVAR_$_CADMockPermissionValidator._canAccessDatabaseBookmarks
- _EKAttachmentProperty_securityScopedURLWrapperForPendingFileCopy
- __103-[CADXPCImplementation(CADDatabaseOperationGroup) CADDatabaseMigrateSubscribedCalendar:toSource:reply:]_block_invoke.56
- __block_literal_global.359
- _kCalSecurityScopedURLWrapperMethods
- _objc_msgSend$canAccessDatabaseBookmarks
CStrings:
+ "TB,N,V_canAccessProcedureAlarms"
+ "TB,N,V_isAutomatorApp"
+ "TB,N,V_isShortcutsApp"
+ "_canAccessProcedureAlarms"
+ "_isAutomatorApp"
+ "_isShortcutsApp"
+ "canAccessProcedureAlarms"
+ "isAutomatorApp"
+ "isShortcutsApp"
+ "setCanAccessProcedureAlarms:"
+ "setEventIsCancelled:"
+ "setEventMessageIdentifier:"
+ "setIsAutomatorApp:"
+ "setIsShortcutsApp:"
- "TB,N,V_canAccessDatabaseBookmarks"
- "_canAccessDatabaseBookmarks"
- "canAccessDatabaseBookmarks"
- "searchableItemsDidUpdate:"
- "setCanAccessDatabaseBookmarks:"

```
