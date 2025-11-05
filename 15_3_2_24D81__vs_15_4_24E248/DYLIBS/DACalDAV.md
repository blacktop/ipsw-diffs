## DACalDAV

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/Versions/A/DACalDAV`

```diff

-2673.0.0.0.0
-  __TEXT.__text: 0x3c1fc
+2673.5.2.0.0
+  __TEXT.__text: 0x3c530
   __TEXT.__auth_stubs: 0x1ce0
-  __TEXT.__objc_methlist: 0x2dc8
+  __TEXT.__objc_methlist: 0x3dc4
   __TEXT.__const: 0x110
   __TEXT.__gcc_except_tab: 0x5c8
   __TEXT.__cstring: 0x16da
   __TEXT.__oslogstring: 0x506e
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__unwind_info: 0xa20
   __TEXT.__objc_classname: 0x48c
   __TEXT.__objc_methname: 0x9ba9
   __TEXT.__objc_methtype: 0x1be2

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26a0
+  __DATA_CONST.__objc_selrefs: 0x27e8
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0xe80
   __AUTH_CONST.__const: 0x560
   __AUTH_CONST.__cfstring: 0x24a0
-  __AUTH_CONST.__objc_const: 0x91d0
+  __AUTH_CONST.__objc_const: 0x7318
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x730
   __DATA.__objc_ivar: 0x334

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: E28EF7B5-7154-34AD-8E96-0D53CE7C4173
-  Functions: 1025
-  Symbols:   3513
+  UUID: A434A427-A824-3E85-B7EE-0E0DB113ADBD
+  Functions: 1045
+  Symbols:   3536
   CStrings:  2867
 
Symbols:
+ +[DACalDAViCalItem _checkOccurrencesForEvent:fromDate:toDate:].cold.1
+ +[DACalDAViCalItem _shouldApplyEvent:instanceWithStartDate:startRange:endRange:].cold.1
+ +[DACalDAViCalItem _shouldApplyEventFromSyncReport:startDate:endDate:].cold.1
+ +[MobileCalDAVCalendar calURLToUIDCache].cold.1
+ -[MobileCalDAVAccount dealloc].cold.1
+ -[MobileCalDAVAccount initWithBackingAccountInfo:].cold.1
+ -[MobileCalDAVAccount refreshActor:didCompleteWithError:].cold.1
+ -[MobileCalDAVAccount refreshActor:didCompleteWithError:].cold.2
+ -[MobileCalDAVAccountRefreshActor _sendResultToAccount].cold.1
+ -[MobileCalDAVAccountRefreshActor dealloc].cold.1
+ -[MobileCalDAVAccountRefreshActor dealloc].cold.2
+ -[MobileCalDAVAccountRefreshActor refresh].cold.1
+ -[MobileCalDAVInboxCalendar setETag:forInvitationAtURL:uniqueIdentifier:].cold.1
+ -[MobileCalDAVInboxCalendar setETag:forInvitationAtURL:uniqueIdentifier:].cold.2
+ -[MobileCalDAVInboxCalendar setETag:forInvitationAtURL:uniqueIdentifier:].cold.3
+ -[MobileCalDAVPrincipal calendarOfType:atURL:withOptions:].cold.1
+ -[MobileCalDAVPrincipal initWithConfiguration:principalUID:account:].cold.1
+ RecordCalendarDiagnostics.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __58-[MobileCalDAVAccountRefreshActor _waitForStateTransition]_block_invoke.cold.1
+ __58-[MobileCalDAVAccountRefreshActor _waitForStateTransition]_block_invoke.cold.2

```
