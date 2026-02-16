## TimeSync

> `/System/Library/PrivateFrameworks/TimeSync.framework/TimeSync`

```diff

-1420.2.0.0.0
-  __TEXT.__text: 0x57ea8
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x63a0
-  __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0x3ec9
-  __TEXT.__cstring: 0x6fb7
-  __TEXT.__gcc_except_tab: 0xd24
-  __TEXT.__unwind_info: 0x1790
-  __TEXT.__objc_classname: 0x9f6
-  __TEXT.__objc_methname: 0xb671
-  __TEXT.__objc_methtype: 0x1839
-  __TEXT.__objc_stubs: 0x6ec0
-  __DATA_CONST.__got: 0x390
+1440.23.0.0.0
+  __TEXT.__text: 0x535b8
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_methlist: 0x6498
+  __TEXT.__const: 0x278
+  __TEXT.__oslogstring: 0x3f21
+  __TEXT.__cstring: 0x7676
+  __TEXT.__gcc_except_tab: 0xdb0
+  __TEXT.__unwind_info: 0x1828
+  __TEXT.__objc_classname: 0xa2a
+  __TEXT.__objc_methname: 0xb926
+  __TEXT.__objc_methtype: 0x187d
+  __TEXT.__objc_stubs: 0x7040
+  __DATA_CONST.__got: 0x398
   __DATA_CONST.__const: 0xcc8
-  __DATA_CONST.__objc_classlist: 0x330
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22f0
+  __DATA_CONST.__objc_selrefs: 0x2368
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x348
-  __AUTH_CONST.__auth_got: 0x4a8
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x5160
-  __AUTH_CONST.__objc_const: 0xbd38
+  __DATA_CONST.__objc_superrefs: 0x350
+  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0x52a0
+  __AUTH_CONST.__objc_const: 0xbfd0
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x860
-  __DATA.__data: 0x488
-  __DATA.__bss: 0xa0
-  __DATA_DIRTY.__objc_data: 0x1fe0
-  __DATA_DIRTY.__bss: 0x108
+  __DATA.__objc_ivar: 0x880
+  __DATA.__data: 0x548
+  __DATA.__bss: 0x98
+  __DATA_DIRTY.__objc_data: 0x2030
+  __DATA_DIRTY.__bss: 0x110
   __DATA_DIRTY.__common: 0x4
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ECFA206F-C61B-3435-B9D3-2E85F124834E
-  Functions: 2568
-  Symbols:   7909
-  CStrings:  3861
+  UUID: 6CBF9BFB-E08A-3D39-A7D9-9F30726F74E9
+  Functions: 2616
+  Symbols:   8139
+  CStrings:  3924
 
Symbols:
+ +[TSXExternalSyncConfigData supportsSecureCoding]
+ -[TSXExternalSyncConfigData .cxx_destruct]
+ -[TSXExternalSyncConfigData encodeWithCoder:]
+ -[TSXExternalSyncConfigData initWithCoder:]
+ -[TSXExternalSyncConfigData initWithConfigData:]
+ -[TSXExternalSyncConfigData nominalTriggerDuration]
+ -[TSXExternalSyncConfigData simulationFilePath]
+ -[TSXExternalSyncConfigData syncId]
+ -[TSXExternalSyncConfigData syncMultiplier]
+ -[TSXExternalSyncConfigData timeoutNs]
+ -[TSXExternalSyncConfigData toleranceExternalTriggerNs]
+ -[TSXExternalSyncConfigData toleranceSyncOutputNs]
+ -[TSXExternalSyncConfigData triggerId]
+ -[_TSF_TSDgPTPClock pokeRemoteIPv6Destination:withDestinationAddress:]
+ _OBJC_CLASS_$_TSXExternalSyncConfigData
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._nominalTriggerDuration
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._simulationFilePath
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._syncId
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._syncMultiplier
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._timeoutNs
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._toleranceExternalTriggerNs
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._toleranceSyncOutputNs
+ _OBJC_IVAR_$_TSXExternalSyncConfigData._triggerId
+ _OBJC_METACLASS_$_TSXExternalSyncConfigData
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ __OBJC_$_CLASS_METHODS_TSXExternalSyncConfigData
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_TSXExternalSyncConfigData
+ __OBJC_$_INSTANCE_METHODS_TSXExternalSyncConfigData
+ __OBJC_$_INSTANCE_VARIABLES_TSXExternalSyncConfigData
+ __OBJC_$_PROP_LIST_TSXExternalSyncConfigData
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_CLASS_PROTOCOLS_$_TSXExternalSyncConfigData
+ __OBJC_CLASS_RO_$_TSXExternalSyncConfigData
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_METACLASS_RO_$_TSXExternalSyncConfigData
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.104
+ ___30-[TSXDaemonServiceClient init]_block_invoke.95
+ ___44-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke.120
+ ___46-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke.119
+ ___47-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke.123
+ ___47-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke.115
+ ___47-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke.124
+ ___47-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke.117
+ ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.101
+ ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.108
+ ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.112
+ ___68-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke.122
+ ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.98
+ ___86-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke.125
+ ___block_literal_global.107
+ ___block_literal_global.111
+ ___block_literal_global.170
+ _if_nametoindex
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$initWithConfigData:
+ _objc_msgSend$nominalTriggerDuration
+ _objc_msgSend$pokeRemoteIPv6Destination:withDestinationAddress:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$simulationFilePath
+ _objc_msgSend$syncMultiplier
+ _objc_msgSend$timeoutNs
+ _objc_msgSend$toleranceExternalTriggerNs
+ _objc_msgSend$toleranceSyncOutputNs
+ _objc_msgSend$triggerId
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table44
- ___169-[TSXDaemonServiceClient callMethodForDaemonClient:clientMethodSelector:scalarInputs:scalarInputCount:structInput:structInputSize:scalarOutputs:scalarOutputCount:error:]_block_invoke.101
- ___30-[TSXDaemonServiceClient init]_block_invoke.92
- ___44-[TSXDaemonServiceClient getMSGClock:error:]_block_invoke.123
- ___46-[TSXDaemonServiceClient stopMSGExternalSync:]_block_invoke.122
- ___47-[TSXDaemonServiceClient addMSGClockRef:error:]_block_invoke.126
- ___47-[TSXDaemonServiceClient isMSGServiceAvailable]_block_invoke.114
- ___47-[TSXDaemonServiceClient removeMSGClock:error:]_block_invoke.127
- ___47-[TSXDaemonServiceClient startMSGExternalSync:]_block_invoke.118
- ___50-[TSXDaemonServiceClient closeDaemonClient:error:]_block_invoke.98
- ___55-[TSXDaemonServiceClient propertiesForRegistryEntryID:]_block_invoke.105
- ___57-[TSXDaemonServiceClient propertyForRegistryEntryID:key:]_block_invoke.109
- ___68-[TSXDaemonServiceClient addMSGClock:withNominalSyncDuration:error:]_block_invoke.125
- ___79-[TSXDaemonServiceClient openDaemonClientWithRegistryEntryID:clientType:error:]_block_invoke.95
- ___86-[TSXDaemonServiceClient restoreMSGClockSession:withNominalSyncDuration:refCnt:error:]_block_invoke.128
- ___block_literal_global.104
- ___block_literal_global.108
- ___block_literal_global.113
- ___block_literal_global.117
- ___block_literal_global.121
- ___block_literal_global.173
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x28
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x8
CStrings:
+ "%s failed to create socket"
+ "%s failed to set flag on the socket"
+ "%s sin6_scope_id =%d"
+ "+%s"
+ "-[_TSF_TSDgPTPClock pokeRemoteIPv6Destination:withDestinationAddress:]"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSClockManager.mm"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSInterface.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSKernelClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSMSGService.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSTranslationClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSUserFilteredClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSgPTPClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSgPTPManager.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/API/TSgPTPPort.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/DC/TSDCKernelClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/DC/TSDCUserFilteredClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/DC/TSDCgPTPClock.mm"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/Utilities/TSClockPulser.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/TimeSync/XPC/TSXTranslationClock.mm"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/IOKRegistryEntryExtendedFramework.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDClockManager.mm"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDClockSync.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDKernelClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDKextNotifier.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDUserFilteredClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPClock.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPManager.m"
+ "/Library/Caches/com.apple.xbs/2849505F-AE9E-49B7-883A-CA9BBA8FAED4/TemporaryDirectory.zo4cY4/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPPort.m"
+ "@24@0:8@\"NSCoder\"16"
+ "@88@0:8{?=II{?=QQ}{?=QQ}QQQ*}16"
+ "A"
+ "B32@0:8@16r*24"
+ "NSCoding"
+ "NSSecureCoding"
+ "T@\"NSString\",R,C,N,V_simulationFilePath"
+ "TB,R"
+ "TI,R,N,V_triggerId"
+ "TQ,R,N,V_timeoutNs"
+ "TQ,R,N,V_toleranceExternalTriggerNs"
+ "TQ,R,N,V_toleranceSyncOutputNs"
+ "TSXExternalSyncConfigData"
+ "T{?=QQ},R,N,V_nominalTriggerDuration"
+ "T{?=QQ},R,N,V_syncMultiplier"
+ "_nominalTriggerDuration"
+ "_simulationFilePath"
+ "_syncMultiplier"
+ "_timeoutNs"
+ "_toleranceExternalTriggerNs"
+ "_toleranceSyncOutputNs"
+ "_triggerId"
+ "args != nil && numArgs == 2"
+ "decodeObjectOfClass:forKey:"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "initWithCoder:"
+ "initWithConfigData:"
+ "nominalTriggerDuration"
+ "nominalTriggerDuration.denominator"
+ "nominalTriggerDuration.numerator"
+ "pokeRemoteIPv6Destination:withDestinationAddress:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "simulationFilePath"
+ "supportsSecureCoding"
+ "syncMultiplier"
+ "syncMultiplier.denominator"
+ "syncMultiplier.numerator"
+ "timeoutNs"
+ "toleranceExternalTriggerNs"
+ "toleranceSyncOutputNs"
+ "triggerId"
+ "v24@0:8@\"NSCoder\"16"
+ "v32@0:8@\"TSXExternalSyncConfigData\"16@?<v@?I>24"
+ "v32@0:8@16@?24"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSClockManager.mm"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSInterface.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSKernelClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSMSGService.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSTranslationClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSUserFilteredClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPManager.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/API/TSgPTPPort.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCKernelClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCUserFilteredClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/DC/TSDCgPTPClock.mm"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/Utilities/TSClockPulser.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/TimeSync/XPC/TSXTranslationClock.mm"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/IOKRegistryEntryExtendedFramework.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDClockManager.mm"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDClockSync.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDKernelClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDKextNotifier.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDUserFilteredClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPClock.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPManager.m"
- "/Library/Caches/com.apple.xbs/Sources/TimeSync/clocksyncd/IOKit/TSDgPTPPort.m"
- "args != ((void *)0) && numArgs == 2"
- "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?24"
- "v32@0:8r^{?=II{?=QQ}{?=QQ}QQQ*}16@?<v@?I>24"

```
