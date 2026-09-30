## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-579.2.8.0.0
-  __TEXT.__text: 0x39b1c
-  __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x1904
+579.2.15.0.0
+  __TEXT.__text: 0x3a33c
+  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__objc_methlist: 0x1934
   __TEXT.__const: 0x264
-  __TEXT.__oslogstring: 0x618a
-  __TEXT.__cstring: 0x2337
+  __TEXT.__oslogstring: 0x61aa
+  __TEXT.__cstring: 0x2397
   __TEXT.__gcc_except_tab: 0x814
-  __TEXT.__swift5_typeref: 0x372
+  __TEXT.__swift5_typeref: 0x382
   __TEXT.__swift5_fieldmd: 0x9c
   __TEXT.__constg_swiftt: 0x1f0
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__unwind_info: 0xd38
   __TEXT.__eh_frame: 0x218
   __TEXT.__objc_classname: 0x708
-  __TEXT.__objc_methname: 0xba62
-  __TEXT.__objc_methtype: 0x19e8
-  __TEXT.__objc_stubs: 0x9f00
-  __DATA_CONST.__got: 0x898
+  __TEXT.__objc_methname: 0xbc1a
+  __TEXT.__objc_methtype: 0x19cf
+  __TEXT.__objc_stubs: 0xa0a0
+  __DATA_CONST.__got: 0x900
   __DATA_CONST.__const: 0x1160
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ac0
+  __DATA_CONST.__objc_selrefs: 0x2b28
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__auth_ptr: 0xa8
-  __AUTH_CONST.__const: 0x568
-  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__auth_got: 0x8a0
+  __AUTH_CONST.__auth_ptr: 0xb8
+  __AUTH_CONST.__const: 0x588
+  __AUTH_CONST.__cfstring: 0x18a0
   __AUTH_CONST.__objc_const: 0x6ae0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xf8
   __AUTH.__data: 0x238
   __DATA.__objc_ivar: 0x208
-  __DATA.__data: 0xcd0
-  __DATA.__bss: 0x1
+  __DATA.__data: 0xce0
+  __DATA.__bss: 0xa
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_data: 0x758
   __DATA_DIRTY.__data: 0x220

   - /System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices
   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1017
-  Symbols:   1419
-  CStrings:  2401
+  Functions: 1025
+  Symbols:   1428
+  CStrings:  2419
 
Symbols:
+ _UNNotificationSourceFilterDefault
+ _MGGetSInt32Answer
+ __UNNotificationSourceFilterAll
+ __IsTelephonyDevice
CStrings:
+ "notificationSummaryStatus"
+ "com.apple.mobilephone"
+ "setSummaryStatus:"
+ "allowGameCenter"
+ "UNSNotificationSettingsService [%!{(MISSING)public}@] Returning %!{(MISSING)public}@ Notification Sources For Filter '%!{(MISSING)public}@'"
+ "setNotificationSummaryStatus:"
+ "isBoolSettingLockedDownByRestrictions:"
+ "All"
+ "setPriorityNotificationStatus:"
+ "_notificationRecordSummaryStatusForBulletinStatus:"
+ "_bulletinSummaryStatusForNotificationSummaryStatus:"
+ "priorityNotificationStatus"
+ "UNSNotificationSettingsService [%!{(MISSING)public}@] Getting Notification Sources For Filter '%!{(MISSING)public}@'"
+ "%!l(MISSING)u of %!l(MISSING)u"
+ "_notificationRecordPriorityStatusForBulletinStatus:"
+ "setPriorityStatus:"
+ "getNotificationSourcesWithFilter:completionHandler:"
+ "summaryStatus"
+ "com.apple.gamecenter"
+ "notificationSourcesWithFilter:"
+ "DeviceClassNumber"
+ "priorityStatus"
+ "_bulletinPriorityStatusForNotificationPriorityStatus:"
- "allNotificationSources"
- "UNSNotificationSettingsService [%!{(MISSING)public}@] Returning All Notification Sources %!{(MISSING)public}@"
- "v24@0:8@?<v@?@\"NSSet\">16"
- "getAllNotificationSourcesWithCompletionHandler:"
- "UNSNotificationSettingsService [%!{(MISSING)public}@] Getting All Notification Sources"

```
