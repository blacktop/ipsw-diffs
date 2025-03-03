## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-206.0.5.0.0
-  __TEXT.__text: 0x68b70
+206.0.7.0.0
+  __TEXT.__text: 0x690ec
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0xac00
-  __TEXT.__objc_methlist: 0x6c70
-  __TEXT.__objc_classname: 0x825
-  __TEXT.__objc_methtype: 0xfd3
-  __TEXT.__cstring: 0xb572
-  __TEXT.__objc_methname: 0x119bb
+  __TEXT.__objc_stubs: 0xad00
+  __TEXT.__objc_methlist: 0x6db0
+  __TEXT.__objc_classname: 0x848
+  __TEXT.__objc_methtype: 0xfe8
+  __TEXT.__cstring: 0xb745
+  __TEXT.__objc_methname: 0x11b62
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xbe0
   __TEXT.__oslogstring: 0x6d58
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1170
+  __TEXT.__unwind_info: 0x1198
   __DATA_CONST.__auth_got: 0x480
   __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2e98
-  __DATA_CONST.__cfstring: 0xe960
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __DATA_CONST.__const: 0x2f50
+  __DATA_CONST.__cfstring: 0xecc0
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_intobj: 0xc00
   __DATA_CONST.__objc_arraydata: 0x908
   __DATA_CONST.__objc_arrayobj: 0xa50
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xba60
-  __DATA.__objc_selrefs: 0x3770
-  __DATA.__objc_ivar: 0x924
-  __DATA.__objc_data: 0x1c70
+  __DATA.__objc_const: 0xbd00
+  __DATA.__objc_selrefs: 0x37c0
+  __DATA.__objc_ivar: 0x938
+  __DATA.__objc_data: 0x1d10
   __DATA.__data: 0x4c0
   __DATA.__bss: 0x40
   __DATA.__common: 0x78

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 2474
-  Symbols:   18837
-  CStrings:  5532
+  Functions: 2497
+  Symbols:   19015
+  CStrings:  5582
 
Symbols:
+ +[MOCategoryUsage descriptionOfAppCategory:]
+ +[MOCategoryUsage supportsSecureCoding]
+ +[MOEventScreenTime supportsSecureCoding]
+ -[MOCategoryUsage .cxx_destruct]
+ -[MOCategoryUsage appCategory]
+ -[MOCategoryUsage copyWithZone:]
+ -[MOCategoryUsage description]
+ -[MOCategoryUsage duration]
+ -[MOCategoryUsage encodeWithCoder:]
+ -[MOCategoryUsage initWithCoder:]
+ -[MOCategoryUsage setAppCategory:]
+ -[MOCategoryUsage setDuration:]
+ -[MOEvent screenTimeEvent]
+ -[MOEvent setScreenTimeEvent:]
+ -[MOEventScreenTime .cxx_destruct]
+ -[MOEventScreenTime appCategoryUsages]
+ -[MOEventScreenTime copyWithZone:]
+ -[MOEventScreenTime description]
+ -[MOEventScreenTime encodeWithCoder:]
+ -[MOEventScreenTime initWithCoder:]
+ -[MOEventScreenTime longestActivity]
+ -[MOEventScreenTime setAppCategoryUsages:]
+ -[MOEventScreenTime setLongestActivity:]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOEventScreenTime.o
+ MOEventScreenTime.m
+ OBJC_IVAR_$_MOCategoryUsage._appCategory
+ OBJC_IVAR_$_MOCategoryUsage._duration
+ OBJC_IVAR_$_MOEvent._screenTimeEvent
+ OBJC_IVAR_$_MOEventScreenTime._appCategoryUsages
+ OBJC_IVAR_$_MOEventScreenTime._longestActivity
+ _OBJC_CLASS_$_MOCategoryUsage
+ _OBJC_CLASS_$_MOEventScreenTime
+ _OBJC_METACLASS_$_MOCategoryUsage
+ _OBJC_METACLASS_$_MOEventScreenTime
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1385
+ __OBJC_$_CLASS_METHODS_MOCategoryUsage
+ __OBJC_$_CLASS_METHODS_MOEventScreenTime
+ __OBJC_$_CLASS_PROP_LIST_MOCategoryUsage
+ __OBJC_$_CLASS_PROP_LIST_MOEventScreenTime
+ __OBJC_$_INSTANCE_METHODS_MOCategoryUsage
+ __OBJC_$_INSTANCE_METHODS_MOEventScreenTime
+ __OBJC_$_INSTANCE_VARIABLES_MOCategoryUsage
+ __OBJC_$_INSTANCE_VARIABLES_MOEventScreenTime
+ __OBJC_$_PROP_LIST_MOCategoryUsage
+ __OBJC_$_PROP_LIST_MOEventScreenTime
+ __OBJC_CLASS_PROTOCOLS_$_MOCategoryUsage
+ __OBJC_CLASS_PROTOCOLS_$_MOEventScreenTime
+ __OBJC_CLASS_RO_$_MOCategoryUsage
+ __OBJC_CLASS_RO_$_MOEventScreenTime
+ __OBJC_METACLASS_RO_$_MOCategoryUsage
+ __OBJC_METACLASS_RO_$_MOEventScreenTime
+ __block_literal_global.1505
+ _kMOEventCategoryUsage
+ _kMOEventCategoryUsageAppCategory
+ _kMOEventCategoryUsageDuration
+ _kMOEventLongestScreenTimeEndDate
+ _kMOEventLongestScreenTimeStartDate
+ _objc_msgSend$appCategory
+ _objc_msgSend$appCategoryUsages
+ _objc_msgSend$descriptionOfAppCategory:
+ _objc_msgSend$longestActivity
+ _objc_msgSend$setAppCategory:
+ _objc_msgSend$setAppCategoryUsages:
+ _objc_msgSend$setDuration:
+ _objc_msgSend$setLongestActivity:
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1388
- __block_literal_global.1508
CStrings:
+ "\x17!\x1f\x01"
+ "@\"MOEventScreenTime\""
+ "Creativity"
+ "Education"
+ "Entertainment"
+ "Game"
+ "HealthAndFitness"
+ "MOCategoryUsage"
+ "MOEventScreenTime"
+ "Networking"
+ "Other"
+ "OtherUnknown"
+ "Productivity"
+ "ReadingAndReference"
+ "ShoppingAndFood"
+ "SystemBlockable"
+ "SystemHidden"
+ "SystemUnblockable"
+ "T@\"MOEventScreenTime\",&,N,V_screenTimeEvent"
+ "T@\"NSArray\",&,N,V_appCategoryUsages"
+ "T@\"NSDateInterval\",&,N,V_longestActivity"
+ "T@\"NSNumber\",&,N,V_duration"
+ "TQ,N,V_appCategory"
+ "Utilities"
+ "_appCategory"
+ "_appCategoryUsages"
+ "_duration"
+ "_longestActivity"
+ "_screenTimeEvent"
+ "app category, %@, duration, %f"
+ "app usages, %@, longest activity, %@"
+ "appCategory"
+ "appCategoryUsages"
+ "categoryUsages"
+ "descriptionOfAppCategory:"
+ "eventCategoryUsage"
+ "eventCategoryUsageAppCategory"
+ "eventCategoryUsageDuration"
+ "eventLongestScreenTimeEndDate"
+ "eventLongestScreenTimeStartDate"
+ "longestActivity"
+ "screenTimeEvent"
+ "setAppCategory:"
+ "setAppCategoryUsages:"
+ "setDuration:"
+ "setLongestActivity:"
+ "setScreenTimeEvent:"
- "\x17!\x1f"

```
