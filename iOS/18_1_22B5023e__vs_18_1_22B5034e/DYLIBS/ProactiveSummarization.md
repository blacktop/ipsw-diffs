## ProactiveSummarization

> `/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization`

```diff

-1260.1.0.3.0
-  __TEXT.__text: 0x101c0c
-  __TEXT.__auth_stubs: 0x2f80
+1260.3.0.1.0
+  __TEXT.__text: 0x10625c
+  __TEXT.__auth_stubs: 0x2fb0
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0x9980
-  __TEXT.__oslogstring: 0x57ed
-  __TEXT.__cstring: 0x537c
-  __TEXT.__swift5_typeref: 0x2f92
-  __TEXT.__swift5_proto: 0x8e0
-  __TEXT.__constg_swiftt: 0x22a4
-  __TEXT.__swift5_fieldmd: 0x2820
-  __TEXT.__swift5_types: 0x378
-  __TEXT.__swift5_reflstr: 0x244e
+  __TEXT.__const: 0xa230
+  __TEXT.__oslogstring: 0x587d
+  __TEXT.__cstring: 0x59cc
+  __TEXT.__swift5_typeref: 0x3198
+  __TEXT.__swift5_proto: 0x964
+  __TEXT.__constg_swiftt: 0x2404
+  __TEXT.__swift5_fieldmd: 0x29c8
+  __TEXT.__swift5_types: 0x3a0
+  __TEXT.__swift5_reflstr: 0x25ce
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__swift5_capture: 0x7d4
+  __TEXT.__swift5_capture: 0x8d8
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__unwind_info: 0x4a28
-  __TEXT.__eh_frame: 0xc458
+  __TEXT.__unwind_info: 0x4b48
+  __TEXT.__eh_frame: 0xc540
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methname: 0x1ef2
+  __TEXT.__objc_methname: 0x1f10
   __TEXT.__objc_methtype: 0x2b2
   __TEXT.__objc_stubs: 0x5e0
-  __DATA_CONST.__got: 0xe90
-  __DATA_CONST.__const: 0x548
+  __DATA_CONST.__got: 0xeb8
+  __DATA_CONST.__const: 0x530
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x928
+  __DATA_CONST.__objc_selrefs: 0x930
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x17d0
-  __AUTH_CONST.__auth_ptr: 0x7d0
-  __AUTH_CONST.__const: 0x4f08
+  __AUTH_CONST.__auth_got: 0x17e8
+  __AUTH_CONST.__auth_ptr: 0x7e8
+  __AUTH_CONST.__const: 0x5490
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x2398
+  __AUTH_CONST.__objc_const: 0x23f8
   __AUTH.__objc_data: 0x1c0
   __AUTH.__data: 0x9e0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x22e8
-  __DATA.__bss: 0x11a30
-  __DATA.__common: 0x128
+  __DATA.__data: 0x2388
+  __DATA.__bss: 0x12ba0
+  __DATA.__common: 0x138
   __DATA_DIRTY.__objc_data: 0x328
-  __DATA_DIRTY.__data: 0xbc0
+  __DATA_DIRTY.__data: 0xbc8
   __DATA_DIRTY.__bss: 0x3c8
   __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6257
-  Symbols:   3158
-  CStrings:  1277
+  Functions: 6441
+  Symbols:   3234
+  CStrings:  1311
 
CStrings:
+ "INSERT INTO queue (date, spotlightUniqueId, spotlightDomainId, spotlightBundleId, payload, isRetry) VALUES (:date, :spotlightUniqueId, :spotlightDomainId, :spotlightBundleId, :payload, :isRetry)"
+ "Notification stack summarization was not enabled"
+ "maxAgeForLastNotificationInSeconds"
+ "timeSinceLastNotificationReceived"
+ ":isRetry"
+ "maxNonCommNotificationsToSummarizeInStack"
+ ":threadId"
+ "DELETE FROM lastNotification WHERE bundleId = :bundleId AND threadId = :threadId AND domainId = :domainId"
+ "Notification not eligible for summarization (content length of %!l(MISSING)d is too short); id: %!{(MISSING)public}s"
+ "Notification stack not eligible for summarization (summmarization not enabled); id: %!{(MISSING)public}s"
+ ":bundleId"
+ "Notification urgency was not enabled"
+ "Could not set last notification time: %!@(MISSING)"
+ "Notification not eligible for summarization (won't summarize a conversation that had outgoing messages in the last 8 minutes); id: %!{(MISSING)public}s"
+ "getDoubleForColumnName:table:"
+ "urgencyFilter_message_pipelineDisabled"
+ "Could not prune last notification time: %!@(MISSING)"
+ "com.apple.suggestd"
+ "Notification summarization was not enabled"
+ "date"
+ "summarizationFilter_mail_pipelineDisabled"
+ "Notification not eligible for summarization (summarization not enabled); id: %!{(MISSING)public}s"
+ "proportionCommunicationNotifications"
+ "CREATE INDEX IF NOT EXISTS lastNotification_bundleId_threadId ON lastNotification(bundleId, threadId, domainId)"
+ "summarizationFilter_notificationStack_pipelineDisabled"
+ "Message urgenncy was not enabled"
+ "SELECT payload, pk FROM queue WHERE isRetry = :isRetry ORDER BY date ASC LIMIT :n"
+ "urgencyFilter_mail_pipelineDisabled"
+ "Mail not eligible for summarization (summarization not enabled); id: %!{(MISSING)public}s"
+ "ALTER TABLE queue ADD COLUMN isRetry DEFAULT 0 NOT NULL"
+ "CREATE TABLE IF NOT EXISTS lastNotification (pk INTEGER PRIMARY KEY AUTOINCREMENT, date NOT NULL, bundleId TEXT NOT NULL, threadId TEXT NOT NULL, domainId TEXT NOT NULL)"
+ "Mail urgency was not enabled"
+ "Could not store last notification time to disk: %!@(MISSING)"
+ "DELETE FROM lastNotification WHERE date < :threshold"
+ "urgencyFilter_notification_pipelineDisabled"
+ ":domainId"
+ "Could not retrieve last notification time from disk: %!@(MISSING)"
+ "Mail summarization was not enabled"
+ "Message summarization was not enabled"
+ "summarizationFilter_notification_pipelineDisabled"
+ "SELECT date FROM lastNotification WHERE bundleId = :bundleId AND threadId = :threadId AND domainId = :domainId ORDER BY date DESC LIMIT 1"
+ "Message not eligible for summarization (summarization not enabled); id: %!{(MISSING)public}s"
+ "disableSummarization"
+ "INSERT INTO lastNotification (date, bundleId, threadId, domainId) VALUES (:date, :bundleId, :threadId, :domainId)"
+ "summarizationFilter_message_pipelineDisabled"
+ "Notification not eligible for summarization (not communication); id: %!{(MISSING)public}s"
- "INSERT INTO queue (date, spotlightUniqueId, spotlightDomainId, spotlightBundleId, payload) VALUES (:date, :spotlightUniqueId, :spotlightDomainId, :spotlightBundleId, :payload)"
- "Not writing a summary on the notification corresponding to the mail: %!{(MISSING)public}s; will try transferring it later if the notification comes in"
- "summarizationFilter_notification_featureDisabled"
- "Not writing a status code on the notification corresponding to the message: %!{(MISSING)public}s; will try transferring it later if the notification comes in"
- "Not writing a summary on the notification corresponding to the message: %!{(MISSING)public}s; will try transferring it later if the notification comes in"
- "Not writing a status code on the notification corresponding to the mail: %!{(MISSING)public}s; will try transferring it later if the notification comes in"
- "Notification stack summarization is disabled"
- "SELECT payload, pk FROM queue ORDER BY date ASC LIMIT :n"
- "Notification stack not eligible for summarization (feature disabled); id: %!{(MISSING)public}s"
- "summarizationFilter_notificationStack_featureDisabled"
- "Notification not eligible for summarization (feature disabled); id: %!{(MISSING)public}s"
- "Notification summarization is disabled"

```
