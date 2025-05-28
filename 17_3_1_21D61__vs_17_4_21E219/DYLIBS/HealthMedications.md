## HealthMedications

> `/System/Library/PrivateFrameworks/HealthMedications.framework/HealthMedications`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x14988
+4146.4.18.0.0
+  __TEXT.__text: 0x14b94
   __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x1b90
+  __TEXT.__objc_methlist: 0x1ba8
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x2836
+  __TEXT.__cstring: 0x2843
   __TEXT.__oslogstring: 0x722
   __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__unwind_info: 0x710
   __TEXT.__objc_classname: 0x6e9
-  __TEXT.__objc_methname: 0x5825
-  __TEXT.__objc_methtype: 0xc9e
-  __TEXT.__objc_stubs: 0x2d20
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__objc_methname: 0x58bf
+  __TEXT.__objc_methtype: 0xcaf
+  __TEXT.__objc_stubs: 0x2d80
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0xaf8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2e68
-  __DATA_CONST.__objc_selrefs: 0x1140
-  __AUTH_CONST.__cfstring: 0x2d40
+  __DATA_CONST.__objc_const: 0x2e98
+  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_protorefs: 0x60
+  __DATA_CONST.__objc_classrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0x100
+  __AUTH_CONST.__cfstring: 0x2d60
   __AUTH_CONST.__objc_const: 0x13f8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__const: 0x120
   __AUTH_CONST.__auth_got: 0x280
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x238
-  __DATA.__objc_superrefs: 0x100
-  __DATA.__objc_ivar: 0x254
+  __DATA.__objc_ivar: 0x258
   __DATA.__data: 0x788
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x820

   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 685
-  Symbols:   2553
-  CStrings:  1391
+  Functions: 688
+  Symbols:   2562
+  CStrings:  1399
 
Symbols:
+ +[HKMedicationScheduleItem _makeStableIdentifierFromScheduledDateTime:]
+ +[HKMedicationScheduleItem isScheduleItemIdentifier:matchingDateTime:]
+ +[HKMedicationsNotification notificationBeforeFirstUnlockWithScheduleItemIdentifier:dueDate:]
+ +[HKMedicationsNotification notificationMissedWithScheduleItemIdentifier:dueDate:]
+ +[HKMedicationsNotification notificationNotMissedWithScheduleItemIdentifier:dueDate:]
+ +[HKMedicationsNotification notificationNotMissedWithScheduleItemIdentifier:dueDate:isCritical:isFollowUp:]
+ +[UNNotificationRequest _requestIDForNotification:]
+ -[HKMedicationsNotification dueDate]
+ -[HKMedicationsNotification initWithScheduleItemIdentifier:dueDate:category:argument:extraUserInfo:]
+ _OBJC_IVAR_$_HKMedicationsNotification._dueDate
+ ___block_literal_global.246
+ ___block_literal_global.248
+ ___block_literal_global.252
+ ___block_literal_global.275
+ ___block_literal_global.299
+ _objc_msgSend$dueDate
+ _objc_msgSend$isScheduleItemIdentifier:matchingDateTime:
+ _objc_msgSend$second
+ _objc_msgSend$stringByAppendingFormat:
- +[HKMedicationsNotification notificationBeforeFirstUnlockWithScheduleItemIdentifier:]
- +[HKMedicationsNotification notificationMissedWithScheduleItemIdentifier:]
- +[HKMedicationsNotification notificationNotMissedWithScheduleItemIdentifier:]
- +[HKMedicationsNotification notificationNotMissedWithScheduleItemIdentifier:isCritical:isFollowUp:]
- -[HKMedicationScheduleItem _makeStableIdentifierFromScheduledDateTime:]
- -[HKMedicationsNotification initWithScheduleItemIdentifier:category:argument:extraUserInfo:]
- ___block_literal_global.222
- ___block_literal_global.224
- ___block_literal_global.228
- ___block_literal_global.251
- ___block_literal_global.274
- _kHKNotificationsSuppressNotificationForwardingKey
- _objc_msgSend$setWithObject:
CStrings:
+ "%02d:%02d:%02d"
+ "-%f"
+ "@40@0:8@16@24B32B36"
+ "B32@0:8@16@24"
+ "T@\"NSDate\",R,N,V_dueDate"
+ "T@\"NSString\",?,R,C"
+ "_dueDate"
+ "dueDate"
+ "isScheduleItemIdentifier:matchingDateTime:"
+ "notificationBeforeFirstUnlockWithScheduleItemIdentifier:dueDate:"
+ "notificationMissedWithScheduleItemIdentifier:dueDate:"
+ "notificationNotMissedWithScheduleItemIdentifier:dueDate:"
+ "notificationNotMissedWithScheduleItemIdentifier:dueDate:isCritical:isFollowUp:"
+ "second"
+ "stringByAppendingFormat:"
- "%i:%i"
- "@32@0:8@16B24B28"
- "notificationBeforeFirstUnlockWithScheduleItemIdentifier:"
- "notificationMissedWithScheduleItemIdentifier:"
- "notificationNotMissedWithScheduleItemIdentifier:"
- "notificationNotMissedWithScheduleItemIdentifier:isCritical:isFollowUp:"
- "setWithObject:"

```
