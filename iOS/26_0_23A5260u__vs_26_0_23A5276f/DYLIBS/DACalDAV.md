## DACalDAV

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV`

```diff

-2690.0.0.0.0
-  __TEXT.__text: 0x376d8
+2691.0.0.0.0
+  __TEXT.__text: 0x378b8
   __TEXT.__auth_stubs: 0x1e90
-  __TEXT.__objc_methlist: 0x45e4
+  __TEXT.__objc_methlist: 0x4604
   __TEXT.__const: 0x108
   __TEXT.__cstring: 0x1641
   __TEXT.__oslogstring: 0x506c
   __TEXT.__gcc_except_tab: 0x5e4
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0xa30
-  __TEXT.__objc_classname: 0x504
-  __TEXT.__objc_methname: 0x9e34
+  __TEXT.__unwind_info: 0xa40
+  __TEXT.__objc_classname: 0x505
+  __TEXT.__objc_methname: 0x9e2c
   __TEXT.__objc_methtype: 0x1f9f
   __TEXT.__objc_stubs: 0x7f80
   __DATA_CONST.__got: 0x7e0

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2808
+  __DATA_CONST.__objc_selrefs: 0x2810
   __DATA_CONST.__objc_superrefs: 0x90
   __AUTH_CONST.__auth_got: 0xf58
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x23a0
-  __AUTH_CONST.__objc_const: 0x8490
+  __AUTH_CONST.__objc_const: 0x8a80
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x340

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 29F2DE91-54E5-3A77-A044-F57C5FC5AB0D
-  Functions: 1087
-  Symbols:   4732
+  UUID: C1599A6E-8721-3F35-A9FE-22800D8CA245
+  Functions: 1090
+  Symbols:   4743
   CStrings:  2906
 
Symbols:
+ -[CalDAVRefreshContext addCalendarSyncFailure:]
+ -[CalDAVRefreshContext calendarSyncFailures]
+ -[MobileCalDAVDAAccount promptUserForNewCoreDAVPasswordWithCompletionBlock:]
+ _OBJC_IVAR_$_CalDAVRefreshContext._calendarSyncFailures
+ ___76-[MobileCalDAVDAAccount promptUserForNewCoreDAVPasswordWithCompletionBlock:]_block_invoke
+ _objc_msgSend$addCalendarSyncFailure:
- -[CalDAVRefreshContext setCalendarFailedToSync:]
- _OBJC_IVAR_$_CalDAVRefreshContext._calendarFailedToSync
- _objc_msgSend$setCalendarFailedToSync:
CStrings:
+ "_calendarSyncFailures"
+ "addCalendarSyncFailure:"
+ "calendarSyncFailures"
- "TB,N,V_calendarFailedToSync"
- "_calendarFailedToSync"
- "setCalendarFailedToSync:"

```
