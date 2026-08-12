## PowerlogLiteOperators

> `/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`

```diff

-3486.0.81.502.4
-  __TEXT.__text: 0x4daef0
-  __TEXT.__objc_methlist: 0x2e4f4
-  __TEXT.__const: 0x2ce0
+3486.2.4.0.0
+  __TEXT.__text: 0x4dcf2c
+  __TEXT.__objc_methlist: 0x2e594
+  __TEXT.__const: 0x2cc0
   __TEXT.__swift5_typeref: 0x710
   __TEXT.__constg_swiftt: 0x544
   __TEXT.__swift5_reflstr: 0x4de

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__cstring: 0x5ee66
+  __TEXT.__cstring: 0x5efd9
   __TEXT.__swift5_capture: 0x73c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift_as_entry: 0x64
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0xd0
-  __TEXT.__oslogstring: 0x158fe
+  __TEXT.__oslogstring: 0x15a25
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__gcc_except_tab: 0x2cf0
+  __TEXT.__gcc_except_tab: 0x2d5c
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x8240
+  __TEXT.__unwind_info: 0x8248
   __TEXT.__eh_frame: 0x16d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9440
+  __DATA_CONST.__const: 0x9478
   __DATA_CONST.__objc_classlist: 0xa28
   __DATA_CONST.__objc_nlclslist: 0x268
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14768
+  __DATA_CONST.__objc_selrefs: 0x14818
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb00
-  __DATA_CONST.__objc_arraydata: 0x16670
-  __DATA_CONST.__got: 0x1b18
+  __DATA_CONST.__objc_arraydata: 0x16680
+  __DATA_CONST.__got: 0x1b30
   __AUTH_CONST.__const: 0x2a58
-  __AUTH_CONST.__cfstring: 0x75aa0
-  __AUTH_CONST.__objc_const: 0x37308
+  __AUTH_CONST.__cfstring: 0x75ba0
+  __AUTH_CONST.__objc_const: 0x373c8
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x6e58
   __AUTH_CONST.__objc_arrayobj: 0x2fa0
   __AUTH_CONST.__objc_dictobj: 0x50a0
   __AUTH_CONST.__objc_doubleobj: 0x1310
-  __AUTH_CONST.__auth_got: 0x1950
+  __AUTH_CONST.__auth_got: 0x1948
   __AUTH.__objc_data: 0x29e0
   __AUTH.__data: 0x668
-  __DATA.__objc_ivar: 0x1ec8
+  __DATA.__objc_ivar: 0x1ed0
   __DATA.__data: 0x10f8
   __DATA.__common: 0x1f8
   __DATA.__bss: 0x26f0
-  __DATA_DIRTY.__objc_ivar: 0x1308
+  __DATA_DIRTY.__objc_ivar: 0x1310
   __DATA_DIRTY.__objc_data: 0x3e68
   __DATA_DIRTY.__data: 0x728
-  __DATA_DIRTY.__bss: 0x46e0
+  __DATA_DIRTY.__bss: 0x46e8
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /System/Library/PrivateFrameworks/AccessibilityUtilities.framework/AccessibilityUtilities

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
+  - /System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 19458
-  Symbols:   31854
-  CStrings:  19471
+  Functions: 19473
+  Symbols:   31896
+  CStrings:  19489
 
Symbols:
+ +[PLBatteryAgent entryEventPointDefinitionBatteryShutdownPack]
+ +[PLDisplayAgent _entryEventBackwardDefinitionAPLStatsWithLogSelector:]
+ -[KernelTaskMonitorStats cpu_energy_m]
+ -[KernelTaskMonitorStats setCpu_energy_m:]
+ -[PLBatteryAgent logBatteryShutdownToCA:forBatteryPack:]
+ -[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]
+ -[PLSMCMetricsAgent lastAccumlatedSampleCA]
+ -[PLSMCMetricsAgent setLastAccumlatedSampleCA:]
+ -[PLSpringBoardAgent attentionAwarenessClient]
+ -[PLSpringBoardAgent lastUserEventMediaTime]
+ -[PLSpringBoardAgent setAttentionAwarenessClient:]
+ -[PLSpringBoardAgent setLastUserEventMediaTime:]
+ -[PLSpringBoardAgent startAttentionAwarenessClient]
+ -[PLSpringBoardAgent stopAttentionAwarenessClient]
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table158
+ GCC_except_table175
+ GCC_except_table187
+ GCC_except_table193
+ GCC_except_table248
+ GCC_except_table257
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table271
+ GCC_except_table278
+ GCC_except_table283
+ GCC_except_table325
+ GCC_except_table328
+ GCC_except_table332
+ _OBJC_CLASS_$_AWAttentionAwarenessClient
+ _OBJC_CLASS_$_AWAttentionAwarenessConfiguration
+ _OBJC_IVAR_$_KernelTaskMonitorStats._cpu_energy_m
+ _OBJC_IVAR_$_PLSpringBoardAgent._lastUserEventMediaTime
+ ___51-[PLSpringBoardAgent startAttentionAwarenessClient]_block_invoke
+ ___56-[PLBatteryAgent logBatteryShutdownToCA:forBatteryPack:]_block_invoke
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke
+ ___84-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e26_v16?0"AWAttentionEvent"8lw32l8
+ _kCLLocationAccuracyReduced
+ _kPLBatteryAgentEventPointNameBatteryShutdownPack0
+ _kPLBatteryAgentStringLastShutdownSystemTimestamp0
+ _kPLBatteryAgentStringLastShutdownSystemTimestampSystem
+ _objc_msgSend$_entryEventBackwardDefinitionAPLStatsWithLogSelector:
+ _objc_msgSend$attentionAwarenessClient
+ _objc_msgSend$cpu_energy_m
+ _objc_msgSend$entryEventPointDefinitionBatteryShutdownPack
+ _objc_msgSend$eventMask
+ _objc_msgSend$getHardwarePerfKind:
+ _objc_msgSend$invalidateWithError:
+ _objc_msgSend$lastAccumlatedSampleCA
+ _objc_msgSend$lastUserEventMediaTime
+ _objc_msgSend$logBatteryShutdownToCA:forBatteryPack:
+ _objc_msgSend$logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:
+ _objc_msgSend$resumeWithError:
+ _objc_msgSend$setAttentionAwarenessClient:
+ _objc_msgSend$setAttentionLostTimeout:
+ _objc_msgSend$setConfiguration:shouldReset:error:
+ _objc_msgSend$setCpu_energy_m:
+ _objc_msgSend$setEventHandlerWithQueue:block:
+ _objc_msgSend$setEventMask:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setLastAccumlatedSampleCA:
+ _objc_msgSend$setLastUserEventMediaTime:
+ _objc_msgSend$startAttentionAwarenessClient
+ _objc_msgSend$stopAttentionAwarenessClient
- -[PLBatteryAgent logBatteryShutdownToCA:]
- GCC_except_table117
- GCC_except_table135
- GCC_except_table139
- GCC_except_table157
- GCC_except_table174
- GCC_except_table186
- GCC_except_table192
- GCC_except_table247
- GCC_except_table256
- GCC_except_table259
- GCC_except_table261
- GCC_except_table269
- GCC_except_table275
- GCC_except_table281
- GCC_except_table323
- GCC_except_table326
- GCC_except_table330
- _BKSHIDServicesLastUserEventTime
- ___41-[PLBatteryAgent logBatteryShutdownToCA:]_block_invoke
- ___46-[PLBatteryAgent logEventPointBatteryShutdown]_block_invoke
- ___46-[PLBatteryAgent logEventPointBatteryShutdown]_block_invoke_2
- _kPLBatteryAgentStringLastShutdownSystemTimestamp
- _objc_msgSend$logBatteryShutdownToCA:
CStrings:
+ "-[PLBatteryAgent logEventPointBatteryShutdownWithRawData:packID:systemShutdownData:]"
+ "-[PLSpringBoardAgent startAttentionAwarenessClient]"
+ "AppleSmartBatteryPack"
+ "AttentionAwareness unavailable on this image; autolock energy will use fallback timing"
+ "BatteryShutdown: Failed to get AppleSmartBatteryPack data with result=%x"
+ "BatteryShutdown: log entry for pack=%@"
+ "BatteryShutdownPack0"
+ "CPUEnergyM"
+ "Failed to configure AttentionAwareness client: %{public}@"
+ "Failed to resume AttentionAwareness client: %{public}@"
+ "Failed to retrieve power sources list handle."
+ "LastShutdownSystemTimestampSystem"
+ "PDEB"
+ "PDTP"
+ "Unable to retrieve %s"
+ "com.apple.powerlog.autolock"
+ "gcSlowInlineWritesMigration"
+ "gcSlowInlineWritesTotal"
+ "hw.perflevel%d.physicalcpu"
+ "numMcpuCores"
+ "skipping PE mitigated via BackgroundQoSDisabled"
+ "v16@?0@\"AWAttentionEvent\"8"
- "-[PLBatteryAgent logEventPointBatteryShutdown]"
- "Unable to retrieve hw.perflevel%d.physicalcpu"
- "hw.perflevel0.physicalcpu"
- "hw.perflevel1.physicalcpu"
```
