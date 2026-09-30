## SearchIndexer

> `/System/Library/PrivateFrameworks/Message.framework/XPCServices/SearchIndexer.xpc/SearchIndexer`

```diff

-3826.600.15.2.1
-  __TEXT.__text: 0x4e147c
-  __TEXT.__auth_stubs: 0x4440
+3826.600.32.0.0
+  __TEXT.__text: 0x4ec0d0
+  __TEXT.__auth_stubs: 0x44c0
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x684
-  __TEXT.__cstring: 0x8d99
+  __TEXT.__cstring: 0x9049
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x59e10
-  __TEXT.__swift5_typeref: 0xe055
-  __TEXT.__swift5_capture: 0x8164
-  __TEXT.__constg_swiftt: 0xb7e0
-  __TEXT.__swift5_reflstr: 0xd4b9
-  __TEXT.__swift5_fieldmd: 0x11f50
-  __TEXT.__swift5_proto: 0x2388
-  __TEXT.__swift5_types: 0x13fc
-  __TEXT.__swift5_assocty: 0x1620
-  __TEXT.__oslogstring: 0xef00
+  __TEXT.__const: 0x5a1b0
+  __TEXT.__swift5_typeref: 0xe1ff
+  __TEXT.__swift5_capture: 0x8100
+  __TEXT.__constg_swiftt: 0xb8ec
+  __TEXT.__swift5_reflstr: 0xd5c9
+  __TEXT.__swift5_fieldmd: 0x120a0
+  __TEXT.__swift5_proto: 0x23c0
+  __TEXT.__swift5_types: 0x1410
+  __TEXT.__swift5_assocty: 0x1638
+  __TEXT.__oslogstring: 0xf250
   __TEXT.__swift5_builtin: 0xaa0
   __TEXT.__swift5_mpenum: 0x7a0
   __TEXT.__swift5_protos: 0x74

   __TEXT.__objc_methname: 0x17c9
   __TEXT.__objc_methtype: 0x420
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x100b0
-  __TEXT.__eh_frame: 0x195b8
-  __DATA_CONST.__auth_got: 0x2230
-  __DATA_CONST.__got: 0xc40
-  __DATA_CONST.__auth_ptr: 0x2ff8
-  __DATA_CONST.__const: 0x486a0
+  __TEXT.__unwind_info: 0x101c0
+  __TEXT.__eh_frame: 0x196c8
+  __DATA_CONST.__auth_got: 0x2270
+  __DATA_CONST.__got: 0xc38
+  __DATA_CONST.__auth_ptr: 0x3048
+  __DATA_CONST.__const: 0x48820
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA.__objc_const: 0x42c0
+  __DATA.__objc_const: 0x4320
   __DATA.__objc_selrefs: 0x898
   __DATA.__objc_data: 0x930
-  __DATA.__data: 0x12158
-  __DATA.__bss: 0x45bb0
-  __DATA.__common: 0xc70
+  __DATA.__data: 0x12290
+  __DATA.__bss: 0x462b0
+  __DATA.__common: 0xc88
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CertUI.framework/CertUI
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/EmailCore.framework/EmailCore
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 26118
-  Symbols:   457
-  CStrings:  3007
+  Functions: 26212
+  Symbols:   460
+  CStrings:  3043
 
Symbols:
+ _AnalyticsSendEvent
+ ___exp10
+ _log10
CStrings:
+ "Invalid response when requesting analytics"
+ "N/A"
+ "Received a response when requesting analytics"
+ "Request to send analytics failed with error %@"
+ "Sending analytics request to SearchIndexer."
+ "Unexpected error %@ when requesting analytics"
+ "[%.*hhx-%{public}s] C%llu %{public}s"
+ "[%.*hhx-%{public}s] Ignoring restart"
+ "[%.*hhx-%{public}s] Restart"
+ "[%.*hhx-%{public}s] Sending connection traits %s as %{public}s"
+ "[%.*hhx-{%.*hx}-%{sensitive,mask.mailbox}s] Adding %{public}s sync #%u."
+ "[%.*hhx] Adding %{public}s sync #%u (while local mailboxes are unknown)."
+ "[%.*hhx] Adding %{public}s sync #%u."
+ "[%.*hhx] Push sync %{public}s for %ld mailbox(es)"
+ "[%.*hhx] Push sync %{public}s for mailbox {%.*hx} '%{sensitive,mask.mailbox}s'"
+ "[%.*hhx] Skipping update of mailbox list for sync ."
+ "back-fill"
+ "com.apple.email.SearchIndexer.statistics.daily"
+ "com.apple.email.SearchIndexer.statistics.weekly"
+ "com.apple.email.SearchIndexer.status"
+ "connectionTraits"
+ "dataUsage_receivedByteCount"
+ "dataUsage_sentByteCount"
+ "errors_dataUsageAboveQuotaCount"
+ "errors_serverUnavailableCount"
+ "lastDailyAnalytics"
+ "lastWeeklyAnalytics"
+ "messageCountInLargestAccount"
+ "percentToRedonate"
+ "sourceApplicationKind"
+ "spotlight_completeReindexCount"
+ "spotlight_deletedMessagesCount"
+ "spotlight_messageIndexCount"
+ "spotlight_messageRedonateCount"
+ "spotlight_updateFlagsCount"
+ "totalMessageCount"

```
