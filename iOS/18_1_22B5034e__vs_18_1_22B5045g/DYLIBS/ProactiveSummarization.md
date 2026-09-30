## ProactiveSummarization

> `/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization`

```diff

-1260.3.0.1.0
-  __TEXT.__text: 0x10625c
+1260.5.0.3.0
+  __TEXT.__text: 0x1092e0
   __TEXT.__auth_stubs: 0x2fb0
   __TEXT.__objc_methlist: 0x20c
-  __TEXT.__const: 0xa230
-  __TEXT.__oslogstring: 0x587d
-  __TEXT.__cstring: 0x59cc
-  __TEXT.__swift5_typeref: 0x3198
-  __TEXT.__swift5_proto: 0x964
-  __TEXT.__constg_swiftt: 0x2404
-  __TEXT.__swift5_fieldmd: 0x29c8
-  __TEXT.__swift5_types: 0x3a0
-  __TEXT.__swift5_reflstr: 0x25ce
+  __TEXT.__const: 0xa630
+  __TEXT.__oslogstring: 0x58ed
+  __TEXT.__cstring: 0x5f8c
+  __TEXT.__swift5_typeref: 0x3244
+  __TEXT.__swift5_proto: 0x99c
+  __TEXT.__constg_swiftt: 0x248c
+  __TEXT.__swift5_fieldmd: 0x2aa4
+  __TEXT.__swift5_types: 0x3b0
+  __TEXT.__swift5_reflstr: 0x26ee
   __TEXT.__swift5_protos: 0x30
-  __TEXT.__swift5_capture: 0x8d8
+  __TEXT.__swift5_capture: 0x9f0
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_mpenum: 0x34
   __TEXT.__swift5_assocty: 0x228
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__unwind_info: 0x4b48
-  __TEXT.__eh_frame: 0xc540
+  __TEXT.__unwind_info: 0x4bc8
+  __TEXT.__eh_frame: 0xc608
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methname: 0x1f10
+  __TEXT.__objc_methname: 0x1f26
   __TEXT.__objc_methtype: 0x2b2
   __TEXT.__objc_stubs: 0x5e0
-  __DATA_CONST.__got: 0xeb8
-  __DATA_CONST.__const: 0x530
+  __DATA_CONST.__got: 0xec0
+  __DATA_CONST.__const: 0x518
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x930
+  __DATA_CONST.__objc_selrefs: 0x938
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x17e8
-  __AUTH_CONST.__auth_ptr: 0x7e8
-  __AUTH_CONST.__const: 0x5490
+  __AUTH_CONST.__auth_ptr: 0x7d8
+  __AUTH_CONST.__const: 0x5a70
   __AUTH_CONST.__cfstring: 0x60
-  __AUTH_CONST.__objc_const: 0x23f8
+  __AUTH_CONST.__objc_const: 0x2478
   __AUTH.__objc_data: 0x1c0
-  __AUTH.__data: 0x9e0
+  __AUTH.__data: 0x9f0
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x2388
-  __DATA.__bss: 0x12ba0
+  __DATA.__data: 0x23e8
+  __DATA.__bss: 0x132e0
   __DATA.__common: 0x138
-  __DATA_DIRTY.__objc_data: 0x328
-  __DATA_DIRTY.__data: 0xbc8
+  __DATA_DIRTY.__objc_data: 0x330
+  __DATA_DIRTY.__data: 0xbd0
   __DATA_DIRTY.__bss: 0x3c8
   __DATA_DIRTY.__common: 0x118
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6441
-  Symbols:   3234
-  CStrings:  1311
+  Functions: 6559
+  Symbols:   3297
+  CStrings:  1342
 
CStrings:
+ "isLowPowerModeEnabled"
+ "urgencyFilter_mail_read"
+ "maxAgeForUrgentNotificationInSeconds"
+ "Could not select urgent notification count: %!@(MISSING)"
+ "overridenIsLowPowerMode"
+ "DELETE FROM urgentNotifications WHERE bundleId = :bundleId AND date >= :threshold ORDER BY date ASC LIMIT :limit"
+ "CREATE INDEX IF NOT EXISTS urgentNotifications_bundleId ON urgentNotifications(bundleId)"
+ "Mail not eligible for urgency determination (category is not personal or high impact transaction); id: %!{(MISSING)public}s"
+ "Message not eligible for pipeline (open conversation); id: %!{(MISSING)public}s"
+ "Mail not eligible for urgency determination (already read); id: %!{(MISSING)public}s"
+ "DELETE FROM urgentNotifications WHERE date < :threshold"
+ "Urgent notification count exceeds frequency threshold allowed"
+ "Number of urgent notifications from app exceeds frequency threshold"
+ ":limit"
+ ":deniedDueToSpecifiedSystemState:"
+ "Mail is already read"
+ "Could not set urgent notification: %!@(MISSING)"
+ "In the observation period for urgent notifications"
+ "Error accessing urgent notification database: %!@(MISSING)"
+ "Could not select urgent notifications before threshold: %!@(MISSING)"
+ "INSERT OR IGNORE INTO urgentNotifications (date, bundleId) VALUES (:date, :bundleId)"
+ "urgentNotificationsMaxCount"
+ "preFilter_message_conversationOpen"
+ "userActivityConversationDetector"
+ "CREATE TABLE IF NOT EXISTS urgentNotifications (pk INTEGER PRIMARY KEY AUTOINCREMENT, date REAL NOT NULL, bundleId TEXT NOT NULL, UNIQUE(date, bundleId) ON CONFLICT IGNORE)"
+ "SELECT * FROM urgentNotifications WHERE bundleId = :bundleId AND date < :threshold"
+ "powerFilter_lowPowerMode"
+ "Could not prune urgent notifications: %!@(MISSING)"
+ "SELECT * FROM urgentNotifications WHERE bundleId = :bundleId AND date >= :threshold"
+ "System is in Low power mode"
+ "throttleOnLPM"
+ "UrgentNotificationsMaxCount"
+ "urgentNotificationsFrequencyWindow"
+ "Could not prune older urgent notifications: %!@(MISSING)"
+ "DELETE FROM urgentNotifications WHERE bundleId = :bundleId AND date < :threshold ORDER BY date ASC LIMIT :limit"
- "Message not eligible for Smart Replies precomputation (won't precompute SR for a conversation that is visible in the Messages app on screen); id: %!{(MISSING)public}s"
- "Mail not eligible for urgency determination (category is not high impact, personal, or other); id: %!{(MISSING)public}s"
- "Message not eligible for urgency (won't run urgency on a conversation that is visible in the Messages app on screen); id: %!{(MISSING)public}s"
- "Mail not valid for processing (already read); id: %!{(MISSING)public}s"
- "Message not eligible for summarization (won't summarize a conversation that is visible in the Messages app on screen); id: %!{(MISSING)public}s"

```
