## ReminderKit

> `/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit`

```diff

-3793.0.0.0.0
-  __TEXT.__text: 0x13bb7c
+3796.11.0.0.0
+  __TEXT.__text: 0x13c64c
   __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x15008
+  __TEXT.__objc_methlist: 0x15170
   __TEXT.__const: 0x16b7
-  __TEXT.__oslogstring: 0x11955
-  __TEXT.__cstring: 0xdc94
-  __TEXT.__gcc_except_tab: 0x833c
+  __TEXT.__oslogstring: 0x1199e
+  __TEXT.__cstring: 0xdcf8
+  __TEXT.__gcc_except_tab: 0x8350
   __TEXT.__ustring: 0x292
   __TEXT.__dlopen_cstrs: 0xb4
-  __TEXT.__unwind_info: 0x6728
-  __TEXT.__objc_classname: 0x3927
-  __TEXT.__objc_methname: 0x26e9e
-  __TEXT.__objc_methtype: 0x41a7
-  __TEXT.__objc_stubs: 0x16300
-  __DATA_CONST.__got: 0xee8
-  __DATA_CONST.__const: 0x29b0
-  __DATA_CONST.__objc_classlist: 0xb90
+  __TEXT.__unwind_info: 0x6778
+  __TEXT.__objc_classname: 0x39b5
+  __TEXT.__objc_methname: 0x2712c
+  __TEXT.__objc_methtype: 0x41b0
+  __TEXT.__objc_stubs: 0x16420
+  __DATA_CONST.__got: 0xef8
+  __DATA_CONST.__const: 0x29f8
+  __DATA_CONST.__objc_classlist: 0xba0
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7900
+  __DATA_CONST.__objc_selrefs: 0x7958
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x9c8
+  __DATA_CONST.__objc_superrefs: 0x9d8
   __DATA_CONST.__objc_arraydata: 0x988
   __AUTH_CONST.__auth_got: 0x678
-  __AUTH_CONST.__const: 0x2c40
-  __AUTH_CONST.__cfstring: 0xe180
-  __AUTH_CONST.__objc_const: 0x231e8
+  __AUTH_CONST.__const: 0x2c80
+  __AUTH_CONST.__cfstring: 0xe1c0
+  __AUTH_CONST.__objc_const: 0x23478
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x2f30
+  __AUTH.__objc_data: 0x2fd0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x10d8
+  __DATA.__objc_ivar: 0x10ec
   __DATA.__data: 0x1a3c
   __DATA.__bss: 0x304
   __DATA.__common: 0x8

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 238CDE59-1EBD-3B0D-A19A-B7233D148625
-  Functions: 8559
-  Symbols:   27456
-  CStrings:  11277
+  UUID: B3B0CE7F-9765-3835-929A-A1931978F9BB
+  Functions: 8589
+  Symbols:   27555
+  CStrings:  11303
 
Symbols:
+ +[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult supportsSecureCoding]
+ +[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount supportsSecureCoding]
+ +[REMReminderStorage isDate:overdueAtReferenceDate:allDay:floatingDateSecondsFromGMT:floatingDateTargetTimeZone:showAllDayRemindersAsOverdue:showTimedRemindersAsOverdue:]
+ -[REMDisplayDate dateByAdjustingFloatingDateForDefaultTimeZone]
+ -[REMDisplayDate dateByAdjustingFloatingDateForTimeZone:]
+ -[REMDisplayDate floatingDateSecondsFromGMT]
+ -[REMDisplayDate initWithDate:allDay:timeZone:floatingDateSecondsFromGMT:]
+ -[REMDisplayDate initWithDate:allDay:timeZone:floatingDateSecondsFromGMT:].cold.1
+ -[REMICloudIsOffDataView fetchHasAnyDirtyCloudObjectInAccount:error:]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult .cxx_destruct]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult copyWithZone:]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult encodeWithCoder:]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult hasAnyDirtyCloudObject]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult hash]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult initWithCoder:]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult initWithHasAnyDirtyCloudObject:]
+ -[REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult isEqual:]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount .cxx_destruct]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount accountObjectID]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount copyWithZone:]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount encodeWithCoder:]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount hash]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount initWithAccountObjectID:]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount initWithCoder:]
+ -[REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount isEqual:]
+ -[REMStore setUnitTest_forceSupportsAutoCategorizationModels:]
+ -[REMStore unitTest_forceSupportsAutoCategorizationModels]
+ -[REMUserActivity decodeStorageIfNeededWithBlock:]
+ -[REMUserActivity ivarLock]
+ -[REMUserActivity l_decodedStorage]
+ -[REMUserActivity setL_decodedStorage:]
+ _OBJC_CLASS_$_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ _OBJC_CLASS_$_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ _OBJC_IVAR_$_REMDisplayDate._floatingDateSecondsFromGMT
+ _OBJC_IVAR_$_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult._hasAnyDirtyCloudObject
+ _OBJC_IVAR_$_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount._accountObjectID
+ _OBJC_IVAR_$_REMStore._unitTest_forceSupportsAutoCategorizationModels
+ _OBJC_IVAR_$_REMUserActivity._ivarLock
+ _OBJC_IVAR_$_REMUserActivity._l_decodedStorage
+ _OBJC_METACLASS_$_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ _OBJC_METACLASS_$_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_$_CLASS_METHODS_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_$_CLASS_METHODS_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_$_CLASS_PROP_LIST_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_$_CLASS_PROP_LIST_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_$_INSTANCE_METHODS_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_$_INSTANCE_METHODS_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_$_INSTANCE_VARIABLES_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_$_INSTANCE_VARIABLES_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_$_PROP_LIST_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_$_PROP_LIST_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_CLASS_PROTOCOLS_$_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_CLASS_PROTOCOLS_$_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_CLASS_RO_$_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_CLASS_RO_$_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ __OBJC_METACLASS_RO_$_REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult
+ __OBJC_METACLASS_RO_$_REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount
+ ___29-[REMUserActivity siriIntent]_block_invoke
+ ___29-[REMUserActivity siriIntent]_block_invoke.cold.1
+ ___31-[REMUserActivity userActivity]_block_invoke
+ ___31-[REMUserActivity userActivity]_block_invoke.cold.1
+ ___50-[REMUserActivity decodeStorageIfNeededWithBlock:]_block_invoke
+ ___block_descriptor_32_e16_16?0"NSData"8l
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_literal_global.578
+ ___block_literal_global.581
+ _objc_msgSend$dateByAdjustingFloatingDateForTimeZone:
+ _objc_msgSend$decodeStorageIfNeededWithBlock:
+ _objc_msgSend$floatingDateSecondsFromGMT
+ _objc_msgSend$hasAnyDirtyCloudObject
+ _objc_msgSend$initWithAccountObjectID:
+ _objc_msgSend$initWithDate:allDay:timeZone:floatingDateSecondsFromGMT:
+ _objc_msgSend$initWithHasAnyDirtyCloudObject:
+ _objc_msgSend$isDate:overdueAtReferenceDate:allDay:floatingDateSecondsFromGMT:floatingDateTargetTimeZone:showAllDayRemindersAsOverdue:showTimedRemindersAsOverdue:
+ _objc_msgSend$l_decodedStorage
+ _objc_msgSend$secondsFromGMT
+ _objc_msgSend$setL_decodedStorage:
- +[REMReminderStorage isDate:overdueAtReferenceDate:allDay:showAllDayRemindersAsOverdue:showTimedRemindersAsOverdue:]
- -[REMDisplayDate initWithDate:allDay:timeZone:]
- -[REMDisplayDate initWithDate:allDay:timeZone:].cold.1
- -[REMStore setUnitTest_forceSupportsGenerativeModels:]
- -[REMStore unitTest_forceSupportsGenerativeModels]
- -[REMUserActivity siriIntent].cold.1
- _OBJC_IVAR_$_REMStore._unitTest_forceSupportsGenerativeModels
- ___block_literal_global.577
- ___block_literal_global.580
- _objc_msgSend$initWithDate:allDay:timeZone:
- _objc_msgSend$isDate:overdueAtReferenceDate:allDay:showAllDayRemindersAsOverdue:showTimedRemindersAsOverdue:
CStrings:
+ "<%@: %p date: %@, timeZone: %@, floatingDateSecondsFromGMT: %ld, allDay: %ld>"
+ "@16@?0@\"NSData\"8"
+ "@44@0:8@16B24@28q36"
+ "B60@0:8@16@24B32q36@44B52B56"
+ "REMICloudIsOffDataViewFetchHasAnyCKDirtyObjectInAccountInvocationResult"
+ "REMICloudIsOffDataViewInvocation_fetchHasAnyDirtyCloudObjectInAccount"
+ "REMUserActivity: failed to create NSUserActivity from data"
+ "REMUserActivity: failed to unarchive Siri Intent. {error: %@}"
+ "T@\"NSNumber\",&,N,V_unitTest_forceSupportsAutoCategorizationModels"
+ "T@\"NSNumber\",R,N,V_hasAnyDirtyCloudObject"
+ "T@,&,N,V_l_decodedStorage"
+ "Tq,R,N,V_floatingDateSecondsFromGMT"
+ "T{os_unfair_lock_s=I},R,N,V_ivarLock"
+ "_floatingDateSecondsFromGMT"
+ "_hasAnyDirtyCloudObject"
+ "_l_decodedStorage"
+ "_unitTest_forceSupportsAutoCategorizationModels"
+ "clearAutoCategorizationLocalCorrectionsOfListsOwnedByCurrentUserWithSupportsAutoCategorizationModels:completion:"
+ "dateByAdjustingFloatingDateForDefaultTimeZone"
+ "dateByAdjustingFloatingDateForTimeZone:"
+ "decodeStorageIfNeededWithBlock:"
+ "fetchHasAnyDirtyCloudObjectInAccount:error:"
+ "floatingDateSecondsFromGMT"
+ "hasAnyDirtyCloudObject"
+ "initWithAccountObjectID:"
+ "initWithDate:allDay:timeZone:floatingDateSecondsFromGMT:"
+ "initWithHasAnyDirtyCloudObject:"
+ "isDate:overdueAtReferenceDate:allDay:floatingDateSecondsFromGMT:floatingDateTargetTimeZone:showAllDayRemindersAsOverdue:showTimedRemindersAsOverdue:"
+ "l_decodedStorage"
+ "secondsFromGMT"
+ "setL_decodedStorage:"
+ "setUnitTest_forceSupportsAutoCategorizationModels:"
+ "unitTest_forceSupportsAutoCategorizationModels"
- "<%@: %p date: %@, timeZone: %@, allDay: %ld>"
- "@36@0:8@16B24@28"
- "B44@0:8@16@24B32B36B40"
- "Error when unarchiving Siri Intent. {error: %@}"
- "T@\"NSNumber\",&,N,V_unitTest_forceSupportsGenerativeModels"
- "_unitTest_forceSupportsGenerativeModels"
- "clearAutoCategorizationLocalCorrectionsOfListsOwnedByCurrentUserWithSupportsGenerativeModels:completion:"
- "initWithDate:allDay:timeZone:"
- "isDate:overdueAtReferenceDate:allDay:showAllDayRemindersAsOverdue:showTimedRemindersAsOverdue:"
- "setUnitTest_forceSupportsGenerativeModels:"
- "unitTest_forceSupportsGenerativeModels"

```
