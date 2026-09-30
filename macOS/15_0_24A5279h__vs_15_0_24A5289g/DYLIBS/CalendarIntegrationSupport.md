## CalendarIntegrationSupport

> `/System/Library/PrivateFrameworks/CalendarIntegrationSupport.framework/Versions/A/CalendarIntegrationSupport`

```diff

-1186.0.0.0.0
-  __TEXT.__text: 0x1fea8
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_methlist: 0xbc
-  __TEXT.__oslogstring: 0x8a7
-  __TEXT.__cstring: 0x6cd
-  __TEXT.__const: 0xcf4
-  __TEXT.__constg_swiftt: 0x718
-  __TEXT.__swift5_typeref: 0x5e1
-  __TEXT.__swift5_reflstr: 0x470
-  __TEXT.__swift5_fieldmd: 0x66c
+1188.0.0.0.0
+  __TEXT.__text: 0x21808
+  __TEXT.__auth_stubs: 0xe60
+  __TEXT.__objc_methlist: 0xc8
+  __TEXT.__oslogstring: 0x8f7
+  __TEXT.__cstring: 0x754
+  __TEXT.__const: 0xc94
+  __TEXT.__constg_swiftt: 0x794
+  __TEXT.__swift5_typeref: 0x623
+  __TEXT.__swift5_reflstr: 0x4d0
+  __TEXT.__swift5_fieldmd: 0x680
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_types: 0x78
-  __TEXT.__swift5_capture: 0x34
-  __TEXT.__swift5_proto: 0x94
+  __TEXT.__swift5_types: 0x74
+  __TEXT.__swift5_proto: 0x88
+  __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x6e8
-  __TEXT.__eh_frame: 0x640
+  __TEXT.__unwind_info: 0x768
+  __TEXT.__eh_frame: 0x810
   __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0x99b
+  __TEXT.__objc_methname: 0x99c
   __TEXT.__objc_methtype: 0x10c
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x1b8
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__const: 0xd8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x328
+  __DATA_CONST.__objc_selrefs: 0x360
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x738
   __AUTH_CONST.__auth_ptr: 0x1f0
-  __AUTH_CONST.__const: 0xbc8
+  __AUTH_CONST.__const: 0xb20
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0xb28
+  __AUTH_CONST.__objc_const: 0xba8
   __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0x740
+  __AUTH.__data: 0x7f0
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x5a0
-  __DATA.__bss: 0x1080
   __DATA.__common: 0x30
+  __DATA.__bss: 0xf00
+  - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/EventKit.framework/Versions/A/EventKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CalendarDaemon.framework/Versions/A/CalendarDaemon
+  - /System/Library/PrivateFrameworks/CalendarDatabase.framework/Versions/A/CalendarDatabase
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/Versions/A/CalendarFoundation
   - /System/Library/PrivateFrameworks/CalendarUI.framework/Versions/A/CalendarUI
   - /System/Library/PrivateFrameworks/ReminderKit.framework/Versions/A/ReminderKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 683
-  Symbols:   406
-  CStrings:  49
+  Functions: 688
+  Symbols:   409
+  CStrings:  53
 
Symbols:
+ -[CISIntegrationServerModule regularSyncRequested]
+ _OBJC_CLASS_$_ACAccountStore
+ ___swift_memcpy88_8
+ __swiftEmptySetSingleton
+ _kCalDatabaseRestoredNotification
+ _objc_msgSend$requestRegularSync
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _symbolic SDyS2SSgG
+ _symbolic SDySSSgSo10EKCalendarCG
+ _symbolic SDySSSgSo8EKSourceCG
+ _symbolic SaySo10EKCalendarCGSg
+ _symbolic So14ACAccountStoreCSg
+ _symbolic _____yS2SSgG s18_DictionaryStorageC
+ _symbolic _____ySSSgSo10EKCalendarCG s18_DictionaryStorageC
+ _symbolic _____ySSSgSo8EKSourceCG s18_DictionaryStorageC
- _OBJC_CLASS_$_EKChangeTrackingClientId
- ___swift_memcpy104_8
- _associated conformance 26CalendarIntegrationSupport0B4SyncC0D5ErrorOSHAASQ
- _objc_msgSend$reminderDatabaseChanged
- _swift_deallocPartialClassInstance
- _swift_dynamicCastObjCClass
- _symbolic So10EKCalendarC
- _symbolic So12EKEventStoreCSSc
- _symbolic _____ 26CalendarIntegrationSupport0B4SyncC0D5ErrorO
- _symbolic _____ySSSgSay_____GG s18_DictionaryStorageC 26CalendarIntegrationSupport0D10CollectionV
- _symbolic _____ySSSo10EKCalendarCG s18_DictionaryStorageC
CStrings:
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "_allCalendars"
+ "accountIDToPersonaIDMap"
+ "accountStore"
+ "calendarsByPersona"
+ "sourcesByPersona"
- "IntegrationSync-"
- "calendar"

```
