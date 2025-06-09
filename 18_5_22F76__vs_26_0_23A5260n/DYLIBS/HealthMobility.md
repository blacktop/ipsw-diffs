## HealthMobility

> `/System/Library/PrivateFrameworks/HealthMobility.framework/HealthMobility`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x783c
-  __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0xc2c
+6074.1.2.4.0
+  __TEXT.__text: 0x791c
+  __TEXT.__auth_stubs: 0x390
+  __TEXT.__objc_methlist: 0xc74
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0xdd5
+  __TEXT.__cstring: 0xe20
   __TEXT.__oslogstring: 0x40b
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__unwind_info: 0x2b0
   __TEXT.__objc_classname: 0x40d
-  __TEXT.__objc_methname: 0x28f5
-  __TEXT.__objc_methtype: 0x4b3
-  __TEXT.__objc_stubs: 0x1ac0
+  __TEXT.__objc_methname: 0x29a9
+  __TEXT.__objc_methtype: 0x4c8
+  __TEXT.__objc_stubs: 0x1b00
   __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x470
+  __DATA_CONST.__const: 0x480
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f0
+  __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH_CONST.__auth_got: 0x1d8
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xb60
-  __AUTH_CONST.__objc_const: 0x16b0
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x1738
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xb8
-  __DATA.__data: 0x378
+  __DATA.__objc_ivar: 0xc4
+  __DATA.__data: 0x370
   __DATA.__bss: 0x80
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3BF6F096-9E01-37FF-8FB4-E1657C067596
-  Functions: 250
-  Symbols:   1088
-  CStrings:  677
+  UUID: A7976C50-9C7C-3046-B5E5-152B3561F273
+  Functions: 255
+  Symbols:   1103
+  CStrings:  686
 
Symbols:
+ +[UNMutableNotificationContent(HKMobility) _makeUserInfoForCategory:isShowingPregnancyContent:]
+ +[UNMutableNotificationContent(HKMobility) _makeUserInfoForCategory:isShowingPregnancyContent:].cold.1
+ -[HKMobilityWalkingSteadinessAnalyticsNotificationEventMetric isShowingPregnancyContent]
+ -[HKMobilityWalkingSteadinessAnalyticsNotificationEventMetric setIsShowingPregnancyContent:]
+ -[HKMobilityWalkingSteadinessAnalyticsNotificationInteractionEventDataSource initWithHealthStore:category:action:isShowingPregnancyContent:]
+ -[HKMobilityWalkingSteadinessAnalyticsNotificationInteractionEventDataSource isShowingPregnancyContent]
+ -[HKMobilityWalkingSteadinessAnalyticsNotificationInteractionEventMetric isShowingPregnancyContent]
+ -[HKMobilityWalkingSteadinessAnalyticsNotificationInteractionEventMetric setIsShowingPregnancyContent:]
+ _OBJC_IVAR_$_HKMobilityWalkingSteadinessAnalyticsNotificationEventMetric._isShowingPregnancyContent
+ _OBJC_IVAR_$_HKMobilityWalkingSteadinessAnalyticsNotificationInteractionEventDataSource._isShowingPregnancyContent
+ _OBJC_IVAR_$_HKMobilityWalkingSteadinessAnalyticsNotificationInteractionEventMetric._isShowingPregnancyContent
+ ___block_literal_global.318
+ ___block_literal_global.320
+ _kHKMobilityNotificationIsShowingPregnancyContentKey
+ _objc_msgSend$_makeUserInfoForCategory:isShowingPregnancyContent:
+ _objc_msgSend$isShowingPregnancyContent
+ _objc_msgSend$setIsShowingPregnancyContent:
- +[UNMutableNotificationContent(HKMobility) _makeUserInfoForCategory:]
- +[UNMutableNotificationContent(HKMobility) _makeUserInfoForCategory:].cold.1
- -[HKMobilityWalkingSteadinessAnalyticsNotificationInteractionEventDataSource initWithHealthStore:category:action:]
- ___block_literal_global.312
- ___block_literal_global.317
- _objc_msgSend$_makeUserInfoForCategory:
- _objc_retain_x22
CStrings:
+ "@\"NSNumber\"16@0:8"
+ "@44@0:8@16@24@32B40"
+ "T@\"NSNumber\",&,N,V_isShowingPregnancyContent"
+ "_isShowingPregnancyContent"
+ "_makeUserInfoForCategory:isShowingPregnancyContent:"
+ "initWithHealthStore:category:action:isShowingPregnancyContent:"
+ "isPregnancyModeEnabled"
+ "isShowingPregnancyContent"
+ "kHKMobilityNotificationIsShowingPregnancyContentKey"
+ "setIsShowingPregnancyContent:"
- "@40@0:8@16@24@32"
- "_makeUserInfoForCategory:"
- "initWithHealthStore:category:action:"

```
