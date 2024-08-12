## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1899.0.1.0.0
-  __TEXT.__text: 0x12f78c
-  __TEXT.__auth_stubs: 0x1490
-  __TEXT.__objc_methlist: 0x13830
+1900.0.0.0.0
+  __TEXT.__text: 0x12ff1c
+  __TEXT.__auth_stubs: 0x14b0
+  __TEXT.__objc_methlist: 0x13890
   __TEXT.__const: 0x5f2
-  __TEXT.__cstring: 0xaea4
-  __TEXT.__oslogstring: 0xd1fe
+  __TEXT.__cstring: 0xaec4
+  __TEXT.__oslogstring: 0xd22e
   __TEXT.__gcc_except_tab: 0x35f8
   __TEXT.__dlopen_cstrs: 0x30e
   __TEXT.__ustring: 0x162

   __TEXT.__swift5_fieldmd: 0xe8
   __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x4c30
-  __TEXT.__objc_classname: 0x18ae
-  __TEXT.__objc_methname: 0x2bc94
+  __TEXT.__unwind_info: 0x4c58
+  __TEXT.__objc_classname: 0x18c3
+  __TEXT.__objc_methname: 0x2bd9e
   __TEXT.__objc_methtype: 0x4042
-  __TEXT.__objc_stubs: 0x1f180
-  __DATA_CONST.__got: 0x15f0
-  __DATA_CONST.__const: 0x4060
-  __DATA_CONST.__objc_classlist: 0x6d8
+  __TEXT.__objc_stubs: 0x1f260
+  __DATA_CONST.__got: 0x1608
+  __DATA_CONST.__const: 0x4088
+  __DATA_CONST.__objc_classlist: 0x6e0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa140
+  __DATA_CONST.__objc_selrefs: 0xa190
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x4e0
   __DATA_CONST.__objc_arraydata: 0x5c0
-  __AUTH_CONST.__auth_got: 0xa58
+  __AUTH_CONST.__auth_got: 0xa68
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x1e80
-  __AUTH_CONST.__cfstring: 0x9340
-  __AUTH_CONST.__objc_const: 0x17298
+  __AUTH_CONST.__const: 0x1ea0
+  __AUTH_CONST.__cfstring: 0x9380
+  __AUTH_CONST.__objc_const: 0x17328
   __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH.__objc_data: 0x2568
+  __AUTH.__objc_data: 0x25b8
   __AUTH.__data: 0xa8
   __DATA.__objc_ivar: 0xbe4
   __DATA.__data: 0x1640
-  __DATA.__bss: 0x3a0
+  __DATA.__bss: 0x3b0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2120
   __DATA_DIRTY.__data: 0x18

   - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon
   - /System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8242
-  Symbols:   9555
-  CStrings:  9629
+  Functions: 8252
+  Symbols:   9572
+  CStrings:  9643
 
Symbols:
+ _APHiddenAppsChangedNotificationCStr
+ _OBJC_CLASS_$_APApplication
+ _OBJC_CLASS_$_EKAppProtectionUtils
+ _OBJC_METACLASS_$_EKAppProtectionUtils
+ _kREMAppBundleIdentifier
+ _notify_check
+ _notify_register_check
CStrings:
+ "EKAppProtectionUtils"
+ "Returning [%!l(MISSING)u] %!@(MISSING) of [%!l(MISSING)u] calendars: [%!l(MISSING)d] holiday [%!l(MISSING)d] suggestion [%!l(MISSING)d] birthday [%!l(MISSING)d] other"
+ "Updating pending integration event ID from %!{(MISSING)public}@ to %!{(MISSING)public}@"
+ "_addPendingIntegrationEvent:toArrayOfHashTables:"
+ "appRecordCache"
+ "applicationWithBundleIdentifier:"
+ "clearAppRecordCache"
+ "isLocked"
+ "isPendingIntegrationEvent:"
+ "isReminderAppLocked"
+ "pendingIntegrationEventChangedIdentifierFrom:to:"
+ "reminderApApp"
+ "reminderCalendarInEventStore:"
- "Returning [%!l(MISSING)u] selectedCalendars of [%!l(MISSING)u] calendars: [%!l(MISSING)d] holiday [%!l(MISSING)d] suggestion [%!l(MISSING)d] birthday [%!l(MISSING)d] other"

```
