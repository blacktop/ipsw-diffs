## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/Versions/A/KnowledgeMonitor`

```diff

-455.2.0.0.0
-  __TEXT.__text: 0x1c524
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_methlist: 0x1af4
+458.5.0.1.0
+  __TEXT.__text: 0x1c7c4
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_methlist: 0x1e94
   __TEXT.__const: 0x100
   __TEXT.__gcc_except_tab: 0x49c
-  __TEXT.__cstring: 0x1497
-  __TEXT.__oslogstring: 0x1774
-  __TEXT.__unwind_info: 0x6e0
-  __TEXT.__objc_classname: 0x399
-  __TEXT.__objc_methname: 0x5635
+  __TEXT.__cstring: 0x14b9
+  __TEXT.__oslogstring: 0x186f
+  __TEXT.__unwind_info: 0x720
+  __TEXT.__objc_classname: 0x39a
+  __TEXT.__objc_methname: 0x5672
   __TEXT.__objc_methtype: 0xa63
-  __TEXT.__objc_stubs: 0x3f60
+  __TEXT.__objc_stubs: 0x3f80
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1510
+  __DATA_CONST.__objc_selrefs: 0x1630
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x458
   __AUTH_CONST.__const: 0x710
   __AUTH_CONST.__cfstring: 0xd20
-  __AUTH_CONST.__objc_const: 0x3600
+  __AUTH_CONST.__objc_const: 0x2fd8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_ivar: 0x230
   __DATA.__data: 0x3c8
   __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x500

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DEE17B95-9BBD-3497-9EC3-6084B14BC4B5
-  Functions: 722
-  Symbols:   1972
-  CStrings:  1489
+  UUID: 61006D4D-9A5C-3EB6-9132-F4D5A96B2D59
+  Functions: 735
+  Symbols:   1993
+  CStrings:  1498
 
Symbols:
+ +[_DKBluetoothMonitor log].cold.1
+ +[_DKBluetoothMonitor writeToBiome]
+ +[_DKMonitor qualityOfService]
+ +[_DKNotificationTimeZoneChangeMonitor log].cold.1
+ +[_DKPluggedInMonitor qualityOfService]
+ +[_DKProcessContext isRunningInUserContext].cold.1
+ -[_DKBatteryMonitor _handleBatteryNotification].cold.1
+ -[_DKMonitor qualityOfService]
+ -[_DKMonitor systemClockDidChange:].cold.1
+ -[_DKPluggedInMonitor setCurrentState].cold.1
+ -[_DKPluggedInMonitor setCurrentState].cold.2
+ -[_DKPluggedInMonitor synchronouslyReflectCurrentValue].cold.1
+ -[_DKPluggedInMonitor synchronouslyReflectCurrentValue].cold.2
+ GCC_except_table26
+ GCC_except_table33
+ GCC_except_table41
+ OBJC_IVAR_$__DKMonitor._qualityOfService
+ _DKPluggedInMonitorLog.cold.1
+ __28-[_DKBluetoothMonitor start]_block_invoke.61
+ __28-[_DKBluetoothMonitor start]_block_invoke.69
+ __28-[_DKBluetoothMonitor start]_block_invoke_2.74
+ __48-[_DKNotificationTimeZoneChangeMonitor activate]_block_invoke.30
+ __block_literal_global.10
+ __block_literal_global.34
+ __os_feature_enabled_impl
+ _dispatch_queue_attr_make_with_qos_class
+ _objc_msgSend$qualityOfService
+ _qos_class_self
- GCC_except_table25
- GCC_except_table31
- GCC_except_table40
- GCC_except_table8
- __28-[_DKBluetoothMonitor start]_block_invoke.59
- __28-[_DKBluetoothMonitor start]_block_invoke.67
- __28-[_DKBluetoothMonitor start]_block_invoke_2.72
- __48-[_DKNotificationTimeZoneChangeMonitor activate]_block_invoke.18
- __block_literal_global.21
- __block_literal_global.28
- __block_literal_global.4
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:262"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBatteryMonitor.m:137"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBatteryMonitor.m:67"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:385"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:443"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:485"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:704"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNotificationTimeZoneChangeMonitor.m:163"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:494"
+ "BluetoothClassicBiomeDonation"
+ "BluetoothFeatures"
+ "IOPSCopyPowerSourcesInfo returned nil"
+ "IOPSPowerSourceSupported returned nil"
+ "Ignoring notification for adapter change"
+ "Querying current state with QoS %d"
+ "Received battery kIOPMMessageBatteryStatusHasChanged message"
+ "Setting current state plugin:%{public}@, adapterType:%{public}@, wireless:%{public}@"
+ "Synchronously reflecting current plug in status: %{public}@"
+ "TI,R,N,V_qualityOfService"
+ "Updating context store with plug in state: %{public}@"
+ "_qualityOfService"
+ "qualityOfService"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:262"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBatteryMonitor.m:134"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBatteryMonitor.m:66"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:377"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:435"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:477"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBluetoothMonitor.m:696"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNotificationTimeZoneChangeMonitor.m:163"
- "/AppleInternal/Library/BuildRoots/ccc52ca0-be37-11ef-914f-aabfac210453/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKNowPlayingMonitor.m:494"
- "Setting current state plugin:%@, adapterType:%@, wireless:%@, "
- "Synchronously reflecting current plug in status: %@"
- "Updating context store with plug in state: %@"
- "com.apple.duetknowledged"
- "deviceactivitymonitor"
- "sunrisesunsetmonitor"

```
