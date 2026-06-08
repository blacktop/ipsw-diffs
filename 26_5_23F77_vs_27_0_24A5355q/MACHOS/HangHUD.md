## HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

```diff

-398.2.0.0.0
-  __TEXT.__text: 0x27180
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_stubs: 0x4840
-  __TEXT.__objc_methlist: 0x25ac
-  __TEXT.__const: 0x488
-  __TEXT.__gcc_except_tab: 0x2f4
-  __TEXT.__objc_methname: 0x8834
-  __TEXT.__cstring: 0x30dc
-  __TEXT.__objc_classname: 0x39c
-  __TEXT.__objc_methtype: 0x13cc
-  __TEXT.__oslogstring: 0x4381
-  __TEXT.__unwind_info: 0xa98
-  __DATA_CONST.__auth_got: 0x540
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x1830
-  __DATA_CONST.__cfstring: 0x49c0
-  __DATA_CONST.__objc_classlist: 0x110
-  __DATA_CONST.__objc_protolist: 0x60
+412.0.0.0.0
+  __TEXT.__text: 0x2e73c
+  __TEXT.__auth_stubs: 0xbd0
+  __TEXT.__objc_stubs: 0x5860
+  __TEXT.__objc_methlist: 0x3254
+  __TEXT.__const: 0x4b0
+  __TEXT.__gcc_except_tab: 0x324
+  __TEXT.__objc_methname: 0xa350
+  __TEXT.__cstring: 0x3771
+  __TEXT.__objc_classname: 0x45a
+  __TEXT.__objc_methtype: 0x19b6
+  __TEXT.__oslogstring: 0x50c0
+  __TEXT.__unwind_info: 0xc28
+  __DATA_CONST.__const: 0x1a80
+  __DATA_CONST.__cfstring: 0x5160
+  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_intobj: 0x168
+  __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x5218
-  __DATA.__objc_selrefs: 0x19e0
-  __DATA.__objc_ivar: 0x4cc
-  __DATA.__objc_data: 0xaa0
-  __DATA.__data: 0x4b0
-  __DATA.__bss: 0x2d8
+  __DATA_CONST.__auth_got: 0x5f8
+  __DATA_CONST.__got: 0x2d0
+  __DATA.__objc_const: 0x6898
+  __DATA.__objc_selrefs: 0x2058
+  __DATA.__objc_ivar: 0x600
+  __DATA.__objc_data: 0xe60
+  __DATA.__data: 0x518
+  __DATA.__bss: 0x300
   - /AppleInternal/Library/Frameworks/PerformanceControlKitInternal.framework/PerformanceControlKitInternal
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreSVG.framework/CoreSVG
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12515BAE-4A70-399F-A3AA-D644E429F0CA
-  Functions: 1204
-  Symbols:   263
-  CStrings:  3154
+  UUID: 3D246C47-8CE6-3938-B653-7DFC26922E6A
+  Functions: 1511
+  Symbols:   292
+  CStrings:  3726
 
Symbols:
+ _AnalyticsSendEventLazy
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFCopyDescription
+ _CFCopyTypeIDDescription
+ _CFGetTypeID
+ _CGColorGetAlpha
+ _NSLocalizedDescriptionKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_BSMachPortSendRight
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableString
+ __os_log_fault_impl
+ _mach_continuous_time
+ _mach_make_memory_entry_64
+ _mach_port_deallocate
+ _mach_task_self_
+ _mach_vm_allocate
+ _mach_vm_deallocate
+ _memcpy
+ _notify_post
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x8
+ _objc_retain_x9
+ _strnlen
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x28
CStrings:
+ "\n    %@"
+ "  ==> removing PerfHUD line: globalKey=%@ timeSinceReceived=%.0fms timeSinceUpdate=%.0fms state=%@"
+ "  Clearing active line: lineID=%@ title=\"%@\""
+ "  Clearing pending line: lineID=%@ title=\"%@\""
+ "  Deallocating shared memory at %p size=%llu"
+ "  Invalidating client: clientID=%@ activeLines=%lu pendingLines=%lu"
+ " No HUD lines to clear, hiding container layer."
+ "#"
+ "%.0f"
+ "%.1f"
+ "%@ %@"
+ "%lld"
+ "(nil)"
+ "(none)"
+ ":"
+ "<%@: %p lineID=%llu type=%@ op=%@ title=\"%@\" label=\"%@\" %@ color=%@ staticColor=%@ thresholdMet=%@ displayThreshold=%lld thresholdDir=%@ timeoutMS=%u overflowValue=%u flags=0x%x receivedTimestamp=%llu (%.0fms ago) lastUpdateTimestamp=%llu (%.0fms ago) writeTimestamp=%llu clientProvidedTimestamp=%llu>"
+ "<%@: %p pid=%d clientID=\"%@\" activeLines=%lu pendingLines=%lu shmem=%p memAddr=0x%llx memSize=%llu>"
+ "<%@: %p totalClients=%lu isPolling=%@ pollingInterval=%.0fms connections=[%@]>"
+ "<="
+ "<nil>"
+ ">="
+ "@\"BSMachPortSendRight\""
+ "@\"NSDictionary\"8@?0"
+ "@\"PerfHUDAnimatedValueLayer\""
+ "@\"PerfHUDKeyLayer\""
+ "@\"PerfHUDLineConfig\""
+ "@\"PerfHUDOverflowConfig\""
+ "@\"PerfHUDValueLayer\""
+ "@24@0:8^{_NSZone=}16"
+ "@288@0:8{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}16"
+ "@28@0:8i16@20"
+ "@28@0:8q16B24"
+ "@28@0:8q16C24"
+ "@36@0:8B16@20@28"
+ "@36@0:8^{?=QQI^{?}}16i24@28"
+ "@36@0:8q16C24@28"
+ "@40@0:8q16@24@32"
+ "@48@0:8@16@24d32@40"
+ "@48@0:8@16q24C32I36@40"
+ "@52@0:8i16@20^{?={?=IIAIAIi[4C][64c]}[12{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}]}28Q36Q44"
+ "@56@0:8@16@24@32d40d48"
+ "A line with this client-provided ID already exists"
+ "A new PerfHUD line is created with title=%@ label=%@ value=%@ with lineID %llu. contentId:%@"
+ "Added PerfHUD connection: %@ (total clients for pid: %lu)"
+ "After END: client=%d:%@ activeLines=%lu pendingLines=%lu"
+ "B28@0:8@16B24"
+ "B32@0:8@16@?24"
+ "B32@0:8^{?=QQI^{?}}16@?24"
+ "B36@0:8q16C24q28"
+ "B44@0:8^{?=QQI^{?}}16i24@28@?36"
+ "C24@0:8q16"
+ "Client is already registered"
+ "Client is not enabled"
+ "Connection invalidated: pid=%d clientID=%@"
+ "Connection not found for timed-out line: %@"
+ "Demoted active line %llu: value=%lld below threshold=%lld"
+ "Duration content is not allowed for notifications; use stream lines instead"
+ "Failed to allocate shared memory"
+ "Failed to create memory entry"
+ "HangHUDClient does not support PerfHUDs"
+ "HangTracerEnableHUDClients"
+ "HangTracerHUDOpacity"
+ "Invalid argument"
+ "Invalid global key format for timeout: %@"
+ "Invalidating connection: pid=%d clientID=%@ activeLines=%lu pendingLines=%lu shmem=%p"
+ "Line %llu timed out: title=\"%@\" timeSinceLastUpdate=%.0fms > timeoutMS=%u"
+ "Line BEGIN: lineID=%llu title=\"%@\" client=%d:%@ thresholdMet=%@"
+ "Line END: after updateWithEntry state.title=\"%@\" state.label=\"%@\" state.timeValue=%llu state.eventStart=%llu"
+ "Line END: before updateWithEntry state.title=\"%@\" state.label=\"%@\" state.timeValue=%llu state.eventStart=%llu"
+ "Line END: lineID=%llu client=%d:%@ wasActive=%@ wasPending=%@ entry.titleLen=%u entry.labelLen=%u entry.valueType=%d entry.timeValue=%llu entry.label=\"%@\""
+ "Line has timed out on the server and can no longer be updated"
+ "NSCopying"
+ "PerfHUD"
+ "PerfHUD clients disabled dynamically — all connections torn down"
+ "PerfHUD clients enabled dynamically"
+ "PerfHUD: %{public}@ has unexpected CFTypeID %lu (expected CFBoolean)"
+ "PerfHUDAnimatedValueLayer"
+ "PerfHUDClientConfiguration"
+ "PerfHUDClientConnection"
+ "PerfHUDClientManager"
+ "PerfHUDColorThreshold"
+ "PerfHUDConnectionResponse"
+ "PerfHUDKeyLayer"
+ "PerfHUDLine %llu (one-shot) finished updates, no fade"
+ "PerfHUDLine %llu finished updates, starting fade-out"
+ "PerfHUDLine %llu reactivating from faded state"
+ "PerfHUDLine %llu: animation in progress, skipping update"
+ "PerfHUDLineConfig"
+ "PerfHUDLineState"
+ "PerfHUDOverflowConfig"
+ "PerfHUDOverflowConfig: triggersTimeout is YES but value is 0 - timeout will never trigger"
+ "PerfHUDServerLine"
+ "PerfHUDValueLayer"
+ "ProcessTerminations"
+ "Processing entry: lineID=%llu op=%@ type=%@ client=%d:%@"
+ "Promoted pending line %llu: value=%lld >= threshold=%lld"
+ "Q32@0:8@16Q24"
+ "Registered content source: %@"
+ "Removed PerfHUD connection: pid=%d clientID=%@ (remaining: %@)"
+ "Removed all PerfHUD connections for pid=%d (remaining total clients: %lu)"
+ "Removed last client for pid=%d, removing pid entry"
+ "Removed timed-out line %llu from connection %d:%@"
+ "Removing PerfHUD connection: %@"
+ "Removing all PerfHUD client connections (count: %lu)"
+ "Removing all PerfHUD connections for pid=%d (count: %lu)"
+ "Replacing existing PerfHUD connection: %@ (new: %@)"
+ "Ring buffer is full"
+ "Ring buffer overflow: skipped %u entries for client=%d:%@"
+ "Ring buffer version mismatch between client and server"
+ "Ring buffer version mismatch: expected=%u actual=%u for client=%d:%@"
+ "Sending content to HUD: globalKey=%@ connection=%@ state=%@"
+ "Shared memory not mapped"
+ "Started PerfHUD polling with interval: %.0fms on dedicated queue"
+ "Stopped PerfHUD polling (no enabled clients or no connections)"
+ "T@\"AssertionManager\",&,N,V_assertionManager"
+ "T@\"BSMachPortSendRight\",R,N,V_sharedMemoryPort"
+ "T@\"CATextLayer\",R,N,V_labelLayer"
+ "T@\"CATextLayer\",R,N,V_titleLayer"
+ "T@\"CATextLayer\",R,N,V_unitLayer"
+ "T@\"CATextLayer\",R,N,V_valueTextLayer"
+ "T@\"HUDContext\",W,N,V_hudContext"
+ "T@\"NSArray\",C,N,V_colorThresholds"
+ "T@\"NSDictionary\",C,N,V_selectedValues"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSMutableDictionary\",&,N,V_activeLines"
+ "T@\"NSMutableDictionary\",&,N,V_mutableConnections"
+ "T@\"NSMutableDictionary\",&,N,V_pendingLines"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_pollingQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_pollingTimer"
+ "T@\"NSString\",C,N,V_clientID"
+ "T@\"NSString\",C,N,V_label"
+ "T@\"NSString\",C,N,V_stringValue"
+ "T@\"NSString\",C,N,V_title"
+ "T@\"NSString\",C,N,V_unit"
+ "T@\"PerfHUDAnimatedValueLayer\",R,N,V_perfAnimatedValueLayer"
+ "T@\"PerfHUDKeyLayer\",R,N,V_perfKeyLayer"
+ "T@\"PerfHUDLineConfig\",C,N,V_lineConfig"
+ "T@\"PerfHUDOverflowConfig\",C,N,V_overflow"
+ "T@\"PerfHUDValueLayer\",R,N,V_perfValueLayer"
+ "TB,N,V_clientEnabled"
+ "TB,N,V_isPolling"
+ "TB,N,V_thresholdMet"
+ "TB,N,V_triggersTimeout"
+ "TB,R,N"
+ "TB,R,V_areHUDClientsEnabled"
+ "TC,N,V_color"
+ "TC,N,V_colorThresholdCount"
+ "TC,N,V_currentColor"
+ "TC,N,V_flags"
+ "TC,N,V_lineType"
+ "TC,N,V_operation"
+ "TC,N,V_staticColor"
+ "TC,N,V_thresholdDirection"
+ "TC,N,V_valueType"
+ "TI,N,V_overflowValue"
+ "TI,N,V_timeoutMS"
+ "TI,R,V_hudOpacityLevel"
+ "TQ,N,V_clientProvidedTimestamp"
+ "TQ,N,V_eventStart"
+ "TQ,N,V_lastUpdateTimestamp"
+ "TQ,N,V_lineID"
+ "TQ,N,V_memoryAddress"
+ "TQ,N,V_memorySize"
+ "TQ,N,V_receivedTimestamp"
+ "TQ,N,V_timeValue"
+ "TQ,N,V_writeTimestamp"
+ "T^{?={?=IIAIAIi[4C][64c]}[12{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}]},N,V_sharedMemory"
+ "Td,N,V_currentValue"
+ "Td,N,V_floatValue"
+ "Td,R,N"
+ "Ti,N,V_pid"
+ "Tq,N,V_displayThreshold"
+ "Tq,N,V_intValue"
+ "Tq,N,V_threshold"
+ "Tq,N,V_value"
+ "Tr^{?=qC[7C]},R,N"
+ "Unknown error"
+ "Unregistered content source: %@"
+ "[3{?=\"threshold\"q\"color\"C\"_pad\"[7C]}]"
+ "^{?={?=IIAIAIi[4C][64c]}[12{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}]}"
+ "^{?={?=IIAIAIi[4C][64c]}[12{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}]}16@0:8"
+ "^{CGColor=}24@0:8@16"
+ "_activeContentSources"
+ "_activeLines"
+ "_allocatePerfHUDSharedMemory:handler:"
+ "_animationLock"
+ "_areHUDClientsEnabled"
+ "_clientEnabled"
+ "_clientID"
+ "_clientProvidedTimestamp"
+ "_color"
+ "_colorThresholdCount"
+ "_colorThresholds"
+ "_contentSourcesLock"
+ "_currentColor"
+ "_currentValue"
+ "_displayThreshold"
+ "_eventStart"
+ "_flags"
+ "_floatValue"
+ "_hudOpacityLevel"
+ "_initializeRingBuffer:withPID:clientID:handler:"
+ "_intValue"
+ "_isPolling"
+ "_label"
+ "_labelLayer"
+ "_lastUpdateTimestamp"
+ "_lineConfig"
+ "_lineID"
+ "_lineType"
+ "_lockedClearAnimation"
+ "_lockedGetAnimation"
+ "_lockedSetAnimation:"
+ "_memoryAddress"
+ "_memorySize"
+ "_mutableConnections"
+ "_notifyTokenPerfHUDConfigChanged"
+ "_opacityNotifyToken"
+ "_operation"
+ "_overflow"
+ "_overflowValue"
+ "_pendingLines"
+ "_pendingPIDByClientIdentifier"
+ "_perfAnimatedValueLayer"
+ "_perfKeyLayer"
+ "_perfValueLayer"
+ "_pollingQueue"
+ "_pollingTimer"
+ "_registerPerfHUDConnectionWithAllocation:pid:clientID:"
+ "_selectedValues"
+ "_sharedMemory"
+ "_sharedMemoryPort"
+ "_spaceBetweenLayers"
+ "_staticColor"
+ "_stringValue"
+ "_teardownActiveLinesForConnection:"
+ "_threshold"
+ "_thresholdDirection"
+ "_thresholdMet"
+ "_timeValue"
+ "_timeoutMS"
+ "_title"
+ "_titleLayer"
+ "_triggersTimeout"
+ "_unit"
+ "_unitLayer"
+ "_userBackgroundOpacity"
+ "_validatePerfHUDHandshakeWithClientID:handler:"
+ "_value"
+ "_valueTextLayer"
+ "_valueType"
+ "_writeTimestamp"
+ "activeLineCount"
+ "activeLines"
+ "activeLinesCopy"
+ "addConnection:"
+ "addLineWithID:state:"
+ "allActiveGlobalKeys"
+ "allActiveLineIDs"
+ "allPendingLineIDs"
+ "allValues"
+ "allocWithZone:"
+ "appendFormat:"
+ "applyBackgroundOpacity"
+ "areHUDClientsEnabled"
+ "assertionManager"
+ "bitmaskValueForKey:defaultValue:"
+ "boolValueForKey:defaultValue:"
+ "class_name"
+ "clientEnabled"
+ "clientID"
+ "clientProvidedTimestamp"
+ "color"
+ "colorForLineState:"
+ "colorThresholdCount"
+ "colorThresholds"
+ "com.apple.HangHUD.PerfHUDPolling"
+ "com.apple.HangHUD.perfhud_enablement"
+ "com.apple.PerfHUD"
+ "com.apple.PerfHUD.configuration_changed"
+ "com.apple.da.hud_layer_refresh"
+ "com.apple.hangtracer.prefs_type_mismatch"
+ "computeColorForValue:"
+ "configWithColorThresholds:displayThreshold:thresholdDirection:timeoutMS:overflow:"
+ "connectPerfHUDClientWithBundleID:clientID:completion:"
+ "connectionForPID:clientID:"
+ "connections"
+ "copyWithZone:"
+ "critical"
+ "currentColor"
+ "currentValue"
+ "currentValueAtTime:"
+ "defaultConfig"
+ "demoteLineWithID:"
+ "displayThreshold"
+ "durationConfigWithDisplayThreshold:overflow:colorThresholds:"
+ "end"
+ "enforceTimeoutsForConnection:atTimeMATU:"
+ "errorWithDomain:code:userInfo:"
+ "evaluateActiveLinesForConnection:atTimeMCTU:"
+ "evaluatePendingLinesForConnection:atTimeMCTU:"
+ "evaluateThreshold:direction:currentValue:"
+ "eventStart"
+ "eventStart=%llu timeValue=%llu"
+ "expected_selector"
+ "f"
+ "filters"
+ "flags"
+ "float=%.2f%@"
+ "floatValue"
+ "getCString:maxLength:encoding:"
+ "globalKeyForLineID:"
+ "handleCompletionWithLineState:"
+ "handleLineTimeoutForGlobalKey:"
+ "handleReactivationWithLineState:"
+ "handshake complete: pid=%d clientID=%@ shmem=%p size=%llu"
+ "handshake received: pid=%d clientID=%@"
+ "handshake: PerfHUD clients not enabled"
+ "handshake: clientID conversion failed"
+ "handshake: mach_make_memory_entry_64 failed: %d"
+ "handshake: mach_vm_allocate failed: %d"
+ "handshake: manager not initialized"
+ "handshake: nil clientID"
+ "handshake: nil handler"
+ "handshake: no pending pid for clientIdentifier=%@"
+ "hasPrefix:"
+ "hudContext"
+ "hudOpacityLevel"
+ "initPrivate"
+ "initPropertyAreHUDClientsEnabled:"
+ "initPropertyHUDOpacity:"
+ "initWithBytes:length:encoding:"
+ "initWithCapacity:"
+ "initWithClientEnabled:lineConfig:selectedValues:"
+ "initWithEntry:"
+ "initWithLineState:theme:fontSize:lineDelegate:"
+ "initWithPID:clientID:sharedMemory:memoryAddress:memorySize:"
+ "initWithPort:"
+ "initWithSharedMemoryPort:"
+ "initWithTitle:label:theme:fontSize:contentScale:"
+ "initWithValueText:unit:theme:"
+ "int=%lld%@"
+ "integerValueForKey:defaultValue:"
+ "isLineActive:"
+ "isLinePending:"
+ "isPolling"
+ "key_name"
+ "label"
+ "labelFadeIn"
+ "labelLayer"
+ "lastUpdateTimestamp"
+ "lineConfig"
+ "lineID"
+ "lineKey"
+ "lineType"
+ "longLongValue"
+ "markAsEnded"
+ "memoryAddress"
+ "memorySize"
+ "mutableConnections"
+ "normal"
+ "numericConfigWithDisplayThreshold:thresholdDirection:colorThresholds:"
+ "oneshot"
+ "operation"
+ "overflow"
+ "overflowAtValue:"
+ "overflowAtValue:triggersTimeout:"
+ "overflowIndicatesTimeout"
+ "overflowValue"
+ "pendingLineCount"
+ "pendingLines"
+ "pendingLinesCopy"
+ "perf"
+ "perf:"
+ "perf:%@"
+ "perf:%d:%@:%llu"
+ "perfAnimatedValueLayer"
+ "perfHUDClientsEnabled"
+ "perfKeyLayer"
+ "perfValueLayer"
+ "pollAllClients"
+ "pollConnection:"
+ "pollingInterval"
+ "pollingQueue"
+ "pollingTimer"
+ "populateFromEntry:"
+ "processEntry:forConnection:"
+ "promoteLineWithID:"
+ "q32@0:8@16q24"
+ "r^{?=qC[7C]}16@0:8"
+ "receivePerfHUDConnectionWithBundleID:clientID:completion:"
+ "received connection %p with identifier %@ from %@ (pid=%d)"
+ "registerContentSource:"
+ "removeAllConnections"
+ "removeAllConnectionsForPID:"
+ "removeAnimationForKey:"
+ "removeConnectionForPID:clientID:"
+ "removeLineWithID:"
+ "selectedValues"
+ "sendDurationUpdatesForConnection:atTimeMCTU:"
+ "sendLineToHUD:forConnection:"
+ "setActiveLines:"
+ "setAnimationDuration:"
+ "setAssertionManager:"
+ "setClientEnabled:"
+ "setClientID:"
+ "setClientProvidedTimestamp:"
+ "setColor:"
+ "setColorThresholdCount:"
+ "setColorThresholds:"
+ "setCurrentColor:"
+ "setCurrentValue:"
+ "setDisplayThreshold:"
+ "setEventStart:"
+ "setFilters:"
+ "setFlags:"
+ "setFloatValue:"
+ "setHudContext:"
+ "setIntValue:"
+ "setIsPolling:"
+ "setLabel:"
+ "setLastUpdateTimestamp:"
+ "setLineConfig:"
+ "setLineID:"
+ "setLineType:"
+ "setMemoryAddress:"
+ "setMemorySize:"
+ "setMutableConnections:"
+ "setOperation:"
+ "setOverflow:"
+ "setOverflowValue:"
+ "setPendingLines:"
+ "setPid:"
+ "setPollingQueue:"
+ "setPollingTimer:"
+ "setReceivedTimestamp:"
+ "setSelectedValues:"
+ "setSharedMemory:"
+ "setStaticColor:"
+ "setStringValue:"
+ "setThreshold:"
+ "setThresholdDirection:"
+ "setThresholdMet:"
+ "setTimeValue:"
+ "setTimeoutMS:"
+ "setTitle:"
+ "setTriggersTimeout:"
+ "setUnit:"
+ "setValue:"
+ "setValue:animated:"
+ "setValueType:"
+ "setWriteTimestamp:"
+ "severe"
+ "sharedMemory"
+ "sharedMemoryPort"
+ "shouldInterpolate"
+ "shouldShowOverflow"
+ "startPollingIfNeeded"
+ "startPollingIfNeeded: No connections, not starting"
+ "stateForLineID:"
+ "staticColor"
+ "stopPollingIfIdle"
+ "stream"
+ "string=\"%@\""
+ "stringSetForKey:"
+ "stringValue"
+ "threshold"
+ "thresholdDirection"
+ "thresholdMet"
+ "thresholdWithValue:color:"
+ "timeValue"
+ "timeoutMS"
+ "title"
+ "titleLayer"
+ "totalClientCount"
+ "triggersTimeout"
+ "type_mismatch"
+ "unit"
+ "unitLayer"
+ "unknown"
+ "unregisterContentSource:"
+ "update"
+ "updateLineInHUD:forConnection:"
+ "updateLineWithID:state:"
+ "updateValueLayersWithLineState:"
+ "updateWithEntry:"
+ "updateWithEntry: after update lineID=%llu title=\"%@\" label=\"%@\" timeValue=%llu eventStart=%llu"
+ "updateWithEntry: lineID=%llu op=%@ hasContent=%@ titleLen=%u labelLen=%u valueType=%d timeValue=%llu"
+ "updateWithEntry: skipping content update for PerfOpEnd with no content"
+ "updateWithTitle:color:"
+ "updateWithTitle:label:color:theme:fontSize:contentScale:"
+ "updateWithValueText:color:"
+ "v20@0:8C16"
+ "v20@0:8I16"
+ "v24@0:8^{?={?=IIAIAIi[4C][64c]}[12{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}]}16"
+ "v288@0:8{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}16"
+ "v28@0:8i16@20"
+ "v296@0:8{?=QCCCC[4C]QQIIqC[7C][3{?=qC[7C]}]CC[6C]C[7C](?=[56c]qdQ)[8c][32c][48c]CC[6C]}16@288"
+ "v32@0:8@16@24"
+ "v32@0:8Q16@24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"PerfHUDConnectionResponse\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "v64@0:8@16@24^{CGColor=}32@40d48d56"
+ "value"
+ "valueForKey:"
+ "valueTextForLineState:"
+ "valueTextLayer"
+ "valueType"
+ "writeTimestamp"
+ "\xf1C"
- " Invalid HUD line clear request found. The number of HUD lines is 0."
- "received connection %p with identifier %@ from %@"

```
