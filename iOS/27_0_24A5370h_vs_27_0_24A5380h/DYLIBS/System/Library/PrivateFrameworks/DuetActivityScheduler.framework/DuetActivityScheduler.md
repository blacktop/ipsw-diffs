## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-  __TEXT.__text: 0x3efe4
-  __TEXT.__objc_methlist: 0x49e8
-  __TEXT.__const: 0x208
+  __TEXT.__text: 0x3e758
+  __TEXT.__objc_methlist: 0x4988
+  __TEXT.__const: 0x200
   __TEXT.__gcc_except_tab: 0x1568
-  __TEXT.__cstring: 0x413c
-  __TEXT.__oslogstring: 0x3306
-  __TEXT.__unwind_info: 0x12f8
+  __TEXT.__cstring: 0x40f2
+  __TEXT.__oslogstring: 0x31da
+  __TEXT.__unwind_info: 0x12e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf30
+  __DATA_CONST.__const: 0xf10
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2960
+  __DATA_CONST.__objc_selrefs: 0x28e8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x180
-  __DATA_CONST.__got: 0x338
-  __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x5080
-  __AUTH_CONST.__objc_const: 0x7f58
+  __DATA_CONST.__got: 0x330
+  __AUTH_CONST.__const: 0x380
+  __AUTH_CONST.__cfstring: 0x5060
+  __AUTH_CONST.__objc_const: 0x7ec8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x690
+  __AUTH.__objc_data: 0x6e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x4a0
+  __DATA.__objc_ivar: 0x494
   __DATA.__data: 0xd68
-  __DATA.__bss: 0xe8
+  __DATA.__bss: 0xf8
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x6e0
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x690
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1686
-  Symbols:   5852
-  CStrings:  1632
+  Functions: 1674
+  Symbols:   5807
+  CStrings:  1624
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[_DASPairedSystemContext usageThresholdForPriority:batteryLevel:isPluggedIn:shouldBypassApplicationUsage:]
+ GCC_except_table25
+ GCC_except_table33
+ _objc_msgSend$usageThresholdForPriority:batteryLevel:isPluggedIn:shouldBypassApplicationUsage:
- -[_DASPairedSystemContext appUsageRefreshTimer]
- -[_DASPairedSystemContext launchedAppCount]
- -[_DASPairedSystemContext remoteAppLaunchCount]
- -[_DASPairedSystemContext setAppUsageRefreshTimer:]
- -[_DASPairedSystemContext setLaunchedAppCount:]
- -[_DASPairedSystemContext setRemoteAppLaunchCount:]
- -[_DASPairedSystemContext updateAppUsageHistory]
- -[_DASPairedSystemContext usageLikelihoodForApplication:]
- -[_DASPairedSystemContext usageThresholdForPriority:batteryLevel:isPluggedIn:]
- GCC_except_table20
- GCC_except_table27
- GCC_except_table39
- GCC_except_table40
- _OBJC_CLASS_$_BMPublisherOptions
- _OBJC_IVAR_$__DASPairedSystemContext._appUsageRefreshTimer
- _OBJC_IVAR_$__DASPairedSystemContext._launchedAppCount
- _OBJC_IVAR_$__DASPairedSystemContext._remoteAppLaunchCount
- ___129-[_DASPairedSystemContext initWithClientIdentifier:context:callbackQueue:systemConditionChangeCallback:trafficCancelationHander:]_block_invoke_2
- ___48-[_DASPairedSystemContext updateAppUsageHistory]_block_invoke
- ___53-[_DASPairedSystemContext setPairedDeviceIdentifier:]_block_invoke
- ___block_descriptor_32_e32_"NSString"16?0"BMStoreEvent"8l
- _dispatch_block_create_with_qos_class
- _objc_msgSend$App
- _objc_msgSend$InFocus
- _objc_msgSend$builderWithPublisher:
- _objc_msgSend$bundleID
- _objc_msgSend$countsDictionary
- _objc_msgSend$idsDeviceIdentifier
- _objc_msgSend$publisherForDevice:withUseCase:options:
- _objc_msgSend$remoteAppLaunchCount
- _objc_msgSend$remoteDevicesWithError:
- _objc_msgSend$setEndDate:
- _objc_msgSend$setRemoteAppLaunchCount:
- _objc_msgSend$setTransform:
- _objc_msgSend$updateAppUsageHistory
- _objc_msgSend$usageLikelihoodForApplication:
- _objc_msgSend$usageThresholdForPriority:batteryLevel:isPluggedIn:
CStrings:
+ "(6"
- "(9"
- "@\"NSString\"16@?0@\"BMStoreEvent\"8"
- "CHECKING: %@, Priority=%@, App Usage: %lf, Watch Battery Level: %d, Watch Plugin Status: %u"
- "DENIED: %@, Priority=%@, App Usage: %lf, Watch Battery Level: %d, Watch Plugin Status: %u"
- "DuetActivitySchedulerPairedSystemContext"
- "Failed to get remote devices: %@"
- "Remote results for app usage history: %@"
- "Selected device (%@) for app usage history."

```
