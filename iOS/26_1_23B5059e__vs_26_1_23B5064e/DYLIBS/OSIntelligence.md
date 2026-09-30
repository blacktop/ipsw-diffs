## OSIntelligence

> `/System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence`

```diff

-234.40.3.0.0
-  __TEXT.__text: 0x18ab4
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_methlist: 0x20a0
-  __TEXT.__const: 0x190
-  __TEXT.__cstring: 0x17a8
+234.40.6.0.0
+  __TEXT.__text: 0x18ea8
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x20e0
+  __TEXT.__const: 0x1a0
+  __TEXT.__cstring: 0x1819
   __TEXT.__gcc_except_tab: 0x634
-  __TEXT.__oslogstring: 0x1c02
-  __TEXT.__unwind_info: 0x900
+  __TEXT.__oslogstring: 0x1be8
+  __TEXT.__unwind_info: 0x908
   __TEXT.__objc_classname: 0x455
-  __TEXT.__objc_methname: 0x3ef8
-  __TEXT.__objc_methtype: 0xbb4
-  __TEXT.__objc_stubs: 0x2d00
+  __TEXT.__objc_methname: 0x3fdd
+  __TEXT.__objc_methtype: 0xbc5
+  __TEXT.__objc_stubs: 0x2da0
   __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x808
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10b0
+  __DATA_CONST.__objc_selrefs: 0x10e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__auth_got: 0x300
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x1380
-  __AUTH_CONST.__objc_const: 0x2ec0
+  __AUTH_CONST.__cfstring: 0x1400
+  __AUTH_CONST.__objc_const: 0x2ef0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 382F085F-47B4-398F-893B-3280C71875A8
-  Functions: 861
-  Symbols:   2898
-  CStrings:  1364
+  UUID: CA53EB6F-C41E-3C04-9F28-344CF366F6BF
+  Functions: 867
+  Symbols:   2921
+  CStrings:  1380
 
Symbols:
+ +[_OSITimeSeriesUtilities resampleTimeSeries:withMaxDays:withFrequency:]
+ -[_OSIBLMAnalyticsHandler recordAnalyticsFeatureState:forCategory:]
+ -[_OSIBLMAnalyticsHandler recordFeatureNotificationState:]
+ -[_OSIBLMAnalyticsHandler recordFeatureNotificationState:].cold.1
+ -[_OSIBLManager handlePPSTaskingStarted]
+ -[_OSIBLManager setTaskingPPSStartDate:]
+ -[_OSIBLManager shouldRunForShadowAnalytics]
+ -[_OSIBLManager taskingPPSStartDate]
+ _OBJC_IVAR_$__OSIBLManager._taskingPPSStartDate
+ ___21-[_OSIBLManager init]_block_invoke.91
+ ___21-[_OSIBLManager init]_block_invoke_2.93
+ ___22-[_OSIBLManager start]_block_invoke.114
+ ___22-[_OSIBLManager start]_block_invoke.117
+ ___40-[_OSIBLManager handlePPSTaskingStarted]_block_invoke
+ ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.102
+ ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.107
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.111
+ ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.112
+ ___block_literal_global.124
+ _objc_msgSend$handlePPSTaskingStarted
+ _objc_msgSend$isIBLMNotificationsCurrentlyEnabled
+ _objc_msgSend$recordAnalyticsFeatureState:forCategory:
+ _objc_msgSend$recordFeatureNotificationState:
+ _objc_msgSend$shouldRunForShadowAnalytics
+ _objc_msgSend$subarrayWithRange:
+ _objc_retain_x24
- +[_OSITimeSeriesUtilities resampleTimeSeries:withFrequency:]
- -[_OSIBLMAnalyticsHandler recordAnalyticsFeatureState:]
- ___21-[_OSIBLManager init]_block_invoke.85
- ___21-[_OSIBLManager init]_block_invoke_2.87
- ___22-[_OSIBLManager start]_block_invoke.107
- ___22-[_OSIBLManager start]_block_invoke.110
- ___41-[_OSIBLManager updateTrialOSIParameters]_block_invoke.95
- ___54-[_OSIBLMAnalyticsHandler historicalDrainDataForDate:]_block_invoke.101
- ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.105
- ___58-[_OSIBLMAnalyticsHandler historicalPluggedInDataForDate:]_block_invoke.106
- ___block_literal_global.118
- _objc_msgSend$recordAnalyticsFeatureState:
CStrings:
+ ":\"3"
+ "@40@0:8@16q24d32"
+ "IBLMFeatureNotificationState"
+ "T@\"NSDate\",&,N,V_taskingPPSStartDate"
+ "_taskingPPSStartDate"
+ "handlePPSTaskingStarted"
+ "isFeatureNotificationEnabled"
+ "kPLTaskingStartNotificationGlobal"
+ "lastTaskingStartDate"
+ "recordAnalyticsFeatureState:forCategory:"
+ "recordFeatureNotificationState:"
+ "resampleTimeSeries:withMaxDays:withFrequency:"
+ "setTaskingPPSStartDate:"
+ "shouldRunForShadowAnalytics"
+ "subarrayWithRange:"
+ "taskingPPSStartDate"
+ "v32@0:8q16@24"
- ":\"2"
- "@32@0:8@16d24"
- "Received notification: %s"
- "recordAnalyticsFeatureState:"
- "resampleTimeSeries:withFrequency:"

```
