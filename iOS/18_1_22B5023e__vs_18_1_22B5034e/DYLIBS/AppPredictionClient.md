## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-576.0.4.0.0
-  __TEXT.__text: 0x175e14
+579.0.0.0.0
+  __TEXT.__text: 0x1766e8
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0x16088
+  __TEXT.__objc_methlist: 0x16110
   __TEXT.__const: 0x6f8
-  __TEXT.__cstring: 0x1a193
+  __TEXT.__cstring: 0x1a371
   __TEXT.__oslogstring: 0x16598
   __TEXT.__gcc_except_tab: 0x21e4
   __TEXT.__dlopen_cstrs: 0x3d0
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x6028
-  __TEXT.__objc_classname: 0x37f5
-  __TEXT.__objc_methname: 0x31023
-  __TEXT.__objc_methtype: 0x64d7
-  __TEXT.__objc_stubs: 0x1b400
+  __TEXT.__unwind_info: 0x6048
+  __TEXT.__objc_classname: 0x37f3
+  __TEXT.__objc_methname: 0x31220
+  __TEXT.__objc_methtype: 0x651d
+  __TEXT.__objc_stubs: 0x1b420
   __DATA_CONST.__got: 0x1678
-  __DATA_CONST.__const: 0x5dc8
+  __DATA_CONST.__const: 0x5e78
   __DATA_CONST.__objc_classlist: 0xd38
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x94c0
+  __DATA_CONST.__objc_selrefs: 0x9518
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0xb70
   __DATA_CONST.__objc_arraydata: 0xae8
   __AUTH_CONST.__auth_got: 0x778
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x26e0
-  __AUTH_CONST.__cfstring: 0x141a0
-  __AUTH_CONST.__objc_const: 0x449d8
+  __AUTH_CONST.__cfstring: 0x14220
+  __AUTH_CONST.__objc_const: 0x44ab8
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x6a8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x2a08
-  __DATA.__objc_ivar: 0x1b14
+  __DATA.__objc_ivar: 0x1b24
   __DATA.__data: 0x1b50
   __DATA.__bss: 0x308
   __DATA_DIRTY.__objc_data: 0x5a28

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 10000
-  Symbols:   12230
-  CStrings:  12681
+  Functions: 10013
+  Symbols:   12245
+  CStrings:  12704
 
Symbols:
+ _ATXUserNotificationSummaryStatusToString
+ OBJC_IVAR_$_ATXPBUserNotification._summaryStatus
+ _ATXStringToUserNotificationSummaryStatus
+ OBJC_IVAR_$_ATXPBUserNotification._isPriorityNotificationEnabled
+ OBJC_IVAR_$_ATXPBUserNotification._isNotificationSummaryEnabled
- OBJC_IVAR_$_ATXPBUserNotification._isDeterminedUrgentByModel
CStrings:
+ "Ti,N,V_summaryStatus"
+ "\xb6\x15\x12\x12"
+ "hasIsPriorityNotificationEnabled"
+ "setSummaryStatus:"
+ "hasSummaryStatus"
+ "_isPriorityNotificationEnabled"
+ "setHasSummaryStatus:"
+ "_isNotificationSummaryEnabled"
+ "Ineligible"
+ "User notification: {uuid: %!@(MISSING)},  {bundle-id: %!@(MISSING)},  {thread-id: %!@(MISSING)},  {category-id: %!@(MISSING)},  {section-id: %!@(MISSING)},  {contact-ids: %!@(MISSING)},  {is group message: %!d(MISSING)},  {title: %!@(MISSING)},  {subtitle: %!@(MISSING)},  {body: %!@(MISSING)},  {is part of stack: %!d(MISSING)},  {number of notifications in Stack: %!d(MISSING)}  {is summarized: %!d(MISSING)},  {summary: %!@(MISSING)},  {is stack summary: %!d(MISSING)},  {priority status: %!d(MISSING)},  {summary status: %!d(MISSING)},  {is priority notification enabled: %!d(MISSING)},  {is notification summary enabled: %!d(MISSING)},  {title length: %!d(MISSING)},  {subtitle length: %!d(MISSING)},  {body length: %!d(MISSING)},  {summary length: %!d(MISSING)},  "
+ "isPriorityNotificationEnabled"
+ "_summaryStatus"
+ "setHasIsNotificationSummaryEnabled:"
+ "TB,N,V_isPriorityNotificationEnabled"
+ "Summarized"
+ "isNotificationSummaryEnabled"
+ "TQ,R,N,V_subtitleLength"
+ "hasIsNotificationSummaryEnabled"
+ "TQ,R,N,V_titleLength"
+ "@32@0:8C16i20@24"
+ "summaryStatus"
+ "setHasIsPriorityNotificationEnabled:"
+ "{?=\"appSpecifiedScore\"b1\"badge\"b1\"bodyLength\"b1\"numberOfNotificationsInStack\"b1\"positionInStack\"b1\"recordTimestamp\"b1\"subtitleLength\"b1\"summaryLength\"b1\"timestamp\"b1\"titleLength\"b1\"attachmentType\"b1\"priorityStatus\"b1\"summaryStatus\"b1\"urgency\"b1\"isGroupMessage\"b1\"isMessage\"b1\"isNotificationSummaryEnabled\"b1\"isPartOfStack\"b1\"isPriorityNotificationEnabled\"b1\"isStackSummary\"b1\"isSummarized\"b1}"
+ "StringAsSummaryStatus:"
+ "TQ,N,V_summaryStatus"
+ "summaryStatusAsString:"
+ "appPredictionsForConsumerSubType:limit:personaUID:"
+ "TB,N,V_isNotificationSummaryEnabled"
+ "setIsPriorityNotificationEnabled:"
+ "TQ,R,N,V_bodyLength"
+ "setIsNotificationSummaryEnabled:"
- "TB,N,V_isDeterminedUrgentByModel"
- "setHasIsDeterminedUrgentByModel:"
- "\xb6\x17\x12"
- "\x02\x11"
- "{?=\"appSpecifiedScore\"b1\"badge\"b1\"bodyLength\"b1\"numberOfNotificationsInStack\"b1\"positionInStack\"b1\"recordTimestamp\"b1\"subtitleLength\"b1\"summaryLength\"b1\"timestamp\"b1\"titleLength\"b1\"attachmentType\"b1\"priorityStatus\"b1\"urgency\"b1\"isDeterminedUrgentByModel\"b1\"isGroupMessage\"b1\"isMessage\"b1\"isPartOfStack\"b1\"isStackSummary\"b1\"isSummarized\"b1}"
- "User notification: uuid: %!@(MISSING), bundle-id: %!@(MISSING), thread-id: %!@(MISSING), category-id: %!@(MISSING), section-id: %!@(MISSING), contact-ids: %!@(MISSING), is group message: %!d(MISSING), "
- "setIsDeterminedUrgentByModel:"
- "isDeterminedUrgentByModel"
- "_isDeterminedUrgentByModel"
- "hasIsDeterminedUrgentByModel"

```
