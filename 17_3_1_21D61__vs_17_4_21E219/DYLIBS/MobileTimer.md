## MobileTimer

> `/System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer`

```diff

-2200.4.3.9.0
-  __TEXT.__text: 0xa99c8
+2200.5.5.0.0
+  __TEXT.__text: 0xb16f4
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0xa5d0
+  __TEXT.__objc_methlist: 0xac50
   __TEXT.__const: 0x330
-  __TEXT.__oslogstring: 0xcae8
-  __TEXT.__cstring: 0x7c55
-  __TEXT.__gcc_except_tab: 0xab8
-  __TEXT.__dlopen_cstrs: 0x671
+  __TEXT.__oslogstring: 0xd4c4
+  __TEXT.__cstring: 0x8108
+  __TEXT.__gcc_except_tab: 0xbcc
+  __TEXT.__dlopen_cstrs: 0x6d3
   __TEXT.__ustring: 0x1a
-  __TEXT.__unwind_info: 0x2c88
-  __TEXT.__objc_classname: 0x17ef
-  __TEXT.__objc_methname: 0x157c5
-  __TEXT.__objc_methtype: 0x3d27
-  __TEXT.__objc_stubs: 0x10300
+  __TEXT.__unwind_info: 0x2e7c
+  __TEXT.__objc_classname: 0x18b3
+  __TEXT.__objc_methname: 0x16389
+  __TEXT.__objc_methtype: 0x3f77
+  __TEXT.__objc_stubs: 0x10b80
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x3718
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __DATA_CONST.__const: 0x3a40
+  __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x2f8
+  __DATA_CONST.__objc_protolist: 0x320
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x23518
-  __DATA_CONST.__objc_selrefs: 0x53e8
+  __DATA_CONST.__objc_const: 0x24f60
+  __DATA_CONST.__objc_selrefs: 0x5688
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0x800
+  __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__const: 0xf20
-  __AUTH_CONST.__cfstring: 0x6860
-  __AUTH_CONST.__objc_const: 0x48e0
+  __AUTH_CONST.__const: 0xfa0
+  __AUTH_CONST.__cfstring: 0x6c20
+  __AUTH_CONST.__objc_const: 0x4ad8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x588
-  __AUTH.__objc_data: 0x2260
-  __DATA.__objc_protorefs: 0x60
-  __DATA.__objc_classrefs: 0x7d8
-  __DATA.__objc_superrefs: 0x3e8
-  __DATA.__objc_ivar: 0x898
-  __DATA.__data: 0x2580
-  __DATA.__common: 0x18
-  __DATA.__bss: 0x1a0
-  __DATA_DIRTY.__objc_data: 0x1810
-  __DATA_DIRTY.__bss: 0x278
+  __AUTH.__objc_data: 0x2350
+  __DATA.__objc_ivar: 0x8e0
+  __DATA.__data: 0x2760
+  __DATA.__common: 0x20
+  __DATA.__bss: 0x1d0
+  __DATA_DIRTY.__objc_data: 0x18b0
+  __DATA_DIRTY.__bss: 0x280
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4583
-  Symbols:   15701
-  CStrings:  6564
+  Functions: 4772
+  Symbols:   16328
+  CStrings:  6780
 
Symbols:
+ +[MTStopwatch descriptionForState:]
+ +[MTStopwatch supportsSecureCoding]
+ +[MTStopwatchManager warmUp]
+ -[MTAgent _setupStopwatches]
+ -[MTAgent setStopwatchServer:]
+ -[MTAgent stopwatchServer]
+ -[MTAlarmMigrator clearInvalidPendingNotifications]
+ -[MTAlarmStorage _clearOutInvalidToneIdentifiers]
+ -[MTLegacyManager clearInvalidPendingNotifications]
+ -[MTMutableStopwatch copyWithZone:]
+ -[MTStopwatch .cxx_destruct]
+ -[MTStopwatch _copyStateOntoStopwatch:]
+ -[MTStopwatch _isEqualToStopwatch:]
+ -[MTStopwatch commonInit]
+ -[MTStopwatch copyWithZone:]
+ -[MTStopwatch currentInterval]
+ -[MTStopwatch description]
+ -[MTStopwatch encodeWithCoder:]
+ -[MTStopwatch hashString]
+ -[MTStopwatch hash]
+ -[MTStopwatch identifier]
+ -[MTStopwatch initWithCoder:]
+ -[MTStopwatch initWithId:]
+ -[MTStopwatch init]
+ -[MTStopwatch isEqual:]
+ -[MTStopwatch laps]
+ -[MTStopwatch mutableCopyWithZone:]
+ -[MTStopwatch offset]
+ -[MTStopwatch previousLapsTotalInterval]
+ -[MTStopwatch setCurrentInterval:]
+ -[MTStopwatch setIdentifier:]
+ -[MTStopwatch setLaps:]
+ -[MTStopwatch setOffset:]
+ -[MTStopwatch setPreviousLapsTotalInterval:]
+ -[MTStopwatch setStartDate:]
+ -[MTStopwatch setState:]
+ -[MTStopwatch setTitle:]
+ -[MTStopwatch startDate]
+ -[MTStopwatch state]
+ -[MTStopwatch title]
+ -[MTStopwatchManager .cxx_destruct]
+ -[MTStopwatchManager _initWithConnectionProvidingBlock:metrics:]
+ -[MTStopwatchManager _initWithConnectionProvidingBlock:metrics:notificationCenter:]
+ -[MTStopwatchManager connectionProvider]
+ -[MTStopwatchManager createStopwatch:]
+ -[MTStopwatchManager dealloc]
+ -[MTStopwatchManager didAddLap:forStopwatch:sender:]
+ -[MTStopwatchManager didClearAllLapsForStopwatch:sender:]
+ -[MTStopwatchManager didLapLapTimerForStopwatch:sender:]
+ -[MTStopwatchManager didPauseLapTimerForStopwatch:sender:]
+ -[MTStopwatchManager didResetLapTimerForStopwatch:sender:]
+ -[MTStopwatchManager didResumeLapTimerForStopwatch:sender:]
+ -[MTStopwatchManager didStartLapTimerForStopwatch:sender:]
+ -[MTStopwatchManager exportedObject]
+ -[MTStopwatchManager getStopwatches]
+ -[MTStopwatchManager initWithConnectionProvider:metrics:]
+ -[MTStopwatchManager initWithConnectionProvider:metrics:notificationCenter:]
+ -[MTStopwatchManager initWithMetrics:]
+ -[MTStopwatchManager initWithoutXpc:]
+ -[MTStopwatchManager init]
+ -[MTStopwatchManager metrics]
+ -[MTStopwatchManager notificationCenter]
+ -[MTStopwatchManager notificationObject]
+ -[MTStopwatchManager reconnect]
+ -[MTStopwatchManager removeStopwatch:]
+ -[MTStopwatchManager setExportedObject:]
+ -[MTStopwatchManager setMetrics:]
+ -[MTStopwatchManager setNotificationCenter:]
+ -[MTStopwatchManager updateStopwatch:]
+ -[MTStopwatchManagerExportedObject .cxx_destruct]
+ -[MTStopwatchManagerExportedObject _didReceiveTimerServerReadyNotification:]
+ -[MTStopwatchManagerExportedObject dealloc]
+ -[MTStopwatchManagerExportedObject didAddLap:forStopwatch:]
+ -[MTStopwatchManagerExportedObject didAddLap:forStopwatch:source:]
+ -[MTStopwatchManagerExportedObject didClearAllLapsForStopwatch:]
+ -[MTStopwatchManagerExportedObject didClearAllLapsForStopwatch:source:]
+ -[MTStopwatchManagerExportedObject didCreateStopwatch:]
+ -[MTStopwatchManagerExportedObject didDeleteStopwatch:]
+ -[MTStopwatchManagerExportedObject didLapLapTimerForStopwatch:]
+ -[MTStopwatchManagerExportedObject didLapLapTimerForStopwatch:source:]
+ -[MTStopwatchManagerExportedObject didPauseLapTimerForStopwatch:]
+ -[MTStopwatchManagerExportedObject didPauseLapTimerForStopwatch:source:]
+ -[MTStopwatchManagerExportedObject didResetLapTimerForStopwatch:]
+ -[MTStopwatchManagerExportedObject didResetLapTimerForStopwatch:source:]
+ -[MTStopwatchManagerExportedObject didResumeLapTimerForStopwatch:]
+ -[MTStopwatchManagerExportedObject didResumeLapTimerForStopwatch:source:]
+ -[MTStopwatchManagerExportedObject didStartLapTimerForStopwatch:]
+ -[MTStopwatchManagerExportedObject didStartLapTimerForStopwatch:source:]
+ -[MTStopwatchManagerExportedObject didUpdateStopwatch:]
+ -[MTStopwatchManagerExportedObject initWithStopwatchManager:]
+ -[MTStopwatchManagerExportedObject publishEvent:withStopwatch:]
+ -[MTStopwatchManagerExportedObject publishEvent:withStopwatch:modifiedItem:]
+ -[MTStopwatchManagerExportedObject publishEvent:withStopwatch:modifiedItem:source:]
+ -[MTStopwatchManagerExportedObject publishEvent:withStopwatch:source:]
+ -[MTStopwatchManagerExportedObject stopwatchManager]
+ -[MTStopwatchServer .cxx_destruct]
+ -[MTStopwatchServer _isSystemReady]
+ -[MTStopwatchServer _systemNotReadyError]
+ -[MTStopwatchServer _systemNotReadyError].cold.1
+ -[MTStopwatchServer checkIn]
+ -[MTStopwatchServer connectionListenerProvider]
+ -[MTStopwatchServer createStopwatch:withCompletion:]
+ -[MTStopwatchServer deleteStopwatch:withCompletion:]
+ -[MTStopwatchServer didAddLap:forStopwatch:source:]
+ -[MTStopwatchServer didAddLap:forStopwatch:withCompletion:]
+ -[MTStopwatchServer didClearAllLapsForStopwatch:withCompletion:]
+ -[MTStopwatchServer didClearAllLapsForStopwatch:withCompletion:source:]
+ -[MTStopwatchServer didCreateStopWatch:source:]
+ -[MTStopwatchServer didDeleteStopwatch:source:]
+ -[MTStopwatchServer didLapLapTimerForStopwatch:withCompletion:]
+ -[MTStopwatchServer didLapLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchServer didPauseLapTimerForStopwatch:withCompletion:]
+ -[MTStopwatchServer didPauseLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchServer didResetLapTimerForStopwatch:withCompletion:]
+ -[MTStopwatchServer didResetLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchServer didResumeLapTimerForStopwatch:withCompletion:]
+ -[MTStopwatchServer didResumeLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchServer didStartLapTimerForStopwatch:withCompletion:]
+ -[MTStopwatchServer didStartLapTimerForStopwatch:withCompletion:source:]
+ -[MTStopwatchServer didUpdateStopwatch:source:]
+ -[MTStopwatchServer getStopwatchesWithCompletion:]
+ -[MTStopwatchServer handleSystemReady]
+ -[MTStopwatchServer initWithStorage:]
+ -[MTStopwatchServer init]
+ -[MTStopwatchServer serializerQueue]
+ -[MTStopwatchServer setSerializerQueue:]
+ -[MTStopwatchServer setStorage:]
+ -[MTStopwatchServer startListening]
+ -[MTStopwatchServer stopListening]
+ -[MTStopwatchServer storage]
+ -[MTStopwatchServer systemReady]
+ -[MTStopwatchServer testStopwatchWrite]
+ -[MTStopwatchServer updateStopwatch:withCompletion:]
+ GCC_except_table15
+ GCC_except_table21
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table43
+ _MTStopwatchClientInterface
+ _MTStopwatchClientInterface.onceToken
+ _MTStopwatchClientInterface.stopwatchClientInterface
+ _MTStopwatchEncodingKeyCurrentInterval
+ _MTStopwatchEncodingKeyIdentifier
+ _MTStopwatchEncodingKeyLaps
+ _MTStopwatchEncodingKeyOffset
+ _MTStopwatchEncodingKeyPreviousLapsTotalInterval
+ _MTStopwatchEncodingKeyStartDate
+ _MTStopwatchEncodingKeyState
+ _MTStopwatchEncodingKeyTitle
+ _MTStopwatchMachServiceName
+ _MTStopwatchManagerDidClearAllLaps
+ _MTStopwatchManagerDidLapLapTimer
+ _MTStopwatchManagerDidPauseLapTimer
+ _MTStopwatchManagerDidResetLapTimer
+ _MTStopwatchManagerDidResumeLapTimer
+ _MTStopwatchManagerDidStartLapTimer
+ _MTStopwatchManagerLapAdded
+ _MTStopwatchManagerModifiedItemKey
+ _MTStopwatchManagerStateReset
+ _MTStopwatchManagerStopwatchCreated
+ _MTStopwatchManagerStopwatchDeleted
+ _MTStopwatchManagerStopwatchKey
+ _MTStopwatchManagerStopwatchUpdated
+ _MTStopwatchManagerStopwatchesKey
+ _MTStopwatchServerErrorDomain
+ _MTStopwatchServerInterface
+ _MTStopwatchServerInterface.onceToken
+ _MTStopwatchServerInterface.stopwatchServerInterface
+ _MTStopwatchServerLifecycleNotification
+ _MTStopwatchServerReadyNotification
+ _MTStopwatchSourceIdentifierKey
+ _OBJC_CLASS_$_MTMutableStopwatch
+ _OBJC_CLASS_$_MTStopwatch
+ _OBJC_CLASS_$_MTStopwatchManager
+ _OBJC_CLASS_$_MTStopwatchManagerExportedObject
+ _OBJC_CLASS_$_MTStopwatchServer
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_IVAR_$_MTAgent._stopwatchServer
+ _OBJC_IVAR_$_MTStopwatch._currentInterval
+ _OBJC_IVAR_$_MTStopwatch._identifier
+ _OBJC_IVAR_$_MTStopwatch._laps
+ _OBJC_IVAR_$_MTStopwatch._offset
+ _OBJC_IVAR_$_MTStopwatch._previousLapsTotalInterval
+ _OBJC_IVAR_$_MTStopwatch._startDate
+ _OBJC_IVAR_$_MTStopwatch._state
+ _OBJC_IVAR_$_MTStopwatch._title
+ _OBJC_IVAR_$_MTStopwatchManager._connectionProvider
+ _OBJC_IVAR_$_MTStopwatchManager._exportedObject
+ _OBJC_IVAR_$_MTStopwatchManager._metrics
+ _OBJC_IVAR_$_MTStopwatchManager._notificationCenter
+ _OBJC_IVAR_$_MTStopwatchManagerExportedObject._stopwatchManager
+ _OBJC_IVAR_$_MTStopwatchServer._connectionListenerProvider
+ _OBJC_IVAR_$_MTStopwatchServer._serializerQueue
+ _OBJC_IVAR_$_MTStopwatchServer._storage
+ _OBJC_IVAR_$_MTStopwatchServer._systemReady
+ _OBJC_METACLASS_$_MTMutableStopwatch
+ _OBJC_METACLASS_$_MTStopwatch
+ _OBJC_METACLASS_$_MTStopwatchManager
+ _OBJC_METACLASS_$_MTStopwatchManagerExportedObject
+ _OBJC_METACLASS_$_MTStopwatchServer
+ __OBJC_$_CLASS_METHODS_MTStopwatch
+ __OBJC_$_CLASS_METHODS_MTStopwatchManager
+ __OBJC_$_CLASS_PROP_LIST_MTStopwatch
+ __OBJC_$_INSTANCE_METHODS_MTMutableStopwatch
+ __OBJC_$_INSTANCE_METHODS_MTStopwatch
+ __OBJC_$_INSTANCE_METHODS_MTStopwatchManager
+ __OBJC_$_INSTANCE_METHODS_MTStopwatchManagerExportedObject
+ __OBJC_$_INSTANCE_METHODS_MTStopwatchServer
+ __OBJC_$_INSTANCE_VARIABLES_MTStopwatch
+ __OBJC_$_INSTANCE_VARIABLES_MTStopwatchManager
+ __OBJC_$_INSTANCE_VARIABLES_MTStopwatchManagerExportedObject
+ __OBJC_$_INSTANCE_VARIABLES_MTStopwatchServer
+ __OBJC_$_PROP_LIST_MTAlarmStorage.381
+ __OBJC_$_PROP_LIST_MTMutableStopwatch
+ __OBJC_$_PROP_LIST_MTSleepModeManager.61
+ __OBJC_$_PROP_LIST_MTSleepSessionTracker.126
+ __OBJC_$_PROP_LIST_MTStopwatch
+ __OBJC_$_PROP_LIST_MTStopwatchManager
+ __OBJC_$_PROP_LIST_MTStopwatchManagerExportedObject
+ __OBJC_$_PROP_LIST_MTStopwatchServer
+ __OBJC_$_PROP_LIST_MTTimerStorage.294
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchManagerProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchPublishing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchServer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MTStopwatchStoreObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchManagerProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchPublishing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchServer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTStopwatchStoreObserver
+ __OBJC_$_PROTOCOL_REFS_MTStopwatchClient
+ __OBJC_$_PROTOCOL_REFS_MTStopwatchPublishing
+ __OBJC_$_PROTOCOL_REFS_MTStopwatchServer
+ __OBJC_CLASS_PROTOCOLS_$_MTStopwatch
+ __OBJC_CLASS_PROTOCOLS_$_MTStopwatchManager
+ __OBJC_CLASS_PROTOCOLS_$_MTStopwatchManagerExportedObject
+ __OBJC_CLASS_PROTOCOLS_$_MTStopwatchServer
+ __OBJC_CLASS_RO_$_MTMutableStopwatch
+ __OBJC_CLASS_RO_$_MTStopwatch
+ __OBJC_CLASS_RO_$_MTStopwatchManager
+ __OBJC_CLASS_RO_$_MTStopwatchManagerExportedObject
+ __OBJC_CLASS_RO_$_MTStopwatchServer
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchClient
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchManagerProtocol
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchPublishing
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchServer
+ __OBJC_LABEL_PROTOCOL_$_MTStopwatchStoreObserver
+ __OBJC_METACLASS_RO_$_MTMutableStopwatch
+ __OBJC_METACLASS_RO_$_MTStopwatch
+ __OBJC_METACLASS_RO_$_MTStopwatchManager
+ __OBJC_METACLASS_RO_$_MTStopwatchManagerExportedObject
+ __OBJC_METACLASS_RO_$_MTStopwatchServer
+ __OBJC_PROTOCOL_$_MTStopwatchClient
+ __OBJC_PROTOCOL_$_MTStopwatchManagerProtocol
+ __OBJC_PROTOCOL_$_MTStopwatchPublishing
+ __OBJC_PROTOCOL_$_MTStopwatchServer
+ __OBJC_PROTOCOL_$_MTStopwatchStoreObserver
+ __OBJC_PROTOCOL_REFERENCE_$_MTStopwatchClient
+ __OBJC_PROTOCOL_REFERENCE_$_MTStopwatchServer
+ ___31-[MTStopwatchManager reconnect]_block_invoke
+ ___35-[MTStopwatchServer _isSystemReady]_block_invoke
+ ___36-[MTStopwatchManager getStopwatches]_block_invoke
+ ___36-[MTStopwatchManager getStopwatches]_block_invoke.55
+ ___38-[MTStopwatchManager createStopwatch:]_block_invoke
+ ___38-[MTStopwatchManager initWithMetrics:]_block_invoke
+ ___38-[MTStopwatchManager initWithMetrics:]_block_invoke_2
+ ___38-[MTStopwatchManager removeStopwatch:]_block_invoke
+ ___38-[MTStopwatchManager updateStopwatch:]_block_invoke
+ ___38-[MTStopwatchServer handleSystemReady]_block_invoke
+ ___39-[MTStopwatchServer testStopwatchWrite]_block_invoke
+ ___39-[MTStopwatchServer testStopwatchWrite]_block_invoke.cold.1
+ ___44-[MTAlarmStorage _loadAlarmsWithCompletion:]_block_invoke.68
+ ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.269
+ ___47-[MTStopwatchServer didCreateStopWatch:source:]_block_invoke
+ ___47-[MTStopwatchServer didDeleteStopwatch:source:]_block_invoke
+ ___47-[MTStopwatchServer didUpdateStopwatch:source:]_block_invoke
+ ___48-[MTSessionsCoordinator source:didRemoveAlarms:]_block_invoke.135
+ ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke.140
+ ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke_2.141
+ ___49-[MTSessionsCoordinator didRestoreTimerSessions:]_block_invoke.145
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.70
+ ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.70.cold.1
+ ___51-[MTLegacyManager clearInvalidPendingNotifications]_block_invoke
+ ___51-[MTLegacyManager clearInvalidPendingNotifications]_block_invoke_2
+ ___51-[MTSessionsCoordinator repeatTimerWithIdentifier:]_block_invoke.120
+ ___51-[MTSessionsCoordinator repeatTimerWithIdentifier:]_block_invoke.120.cold.1
+ ___51-[MTStopwatchServer didAddLap:forStopwatch:source:]_block_invoke
+ ___52-[MTSessionsCoordinator dismissTimerWithIdentifier:]_block_invoke.121
+ ___52-[MTSessionsCoordinator dismissTimerWithIdentifier:]_block_invoke.121.cold.1
+ ___52-[MTStopwatchManager didAddLap:forStopwatch:sender:]_block_invoke
+ ___52-[MTStopwatchManager didAddLap:forStopwatch:sender:]_block_invoke_2
+ ___55-[MTStopwatchManagerExportedObject didCreateStopwatch:]_block_invoke
+ ___55-[MTStopwatchManagerExportedObject didDeleteStopwatch:]_block_invoke
+ ___55-[MTStopwatchManagerExportedObject didUpdateStopwatch:]_block_invoke
+ ___56-[MTStopwatchManager didLapLapTimerForStopwatch:sender:]_block_invoke
+ ___56-[MTStopwatchManager didLapLapTimerForStopwatch:sender:]_block_invoke_2
+ ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.131
+ ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.131.cold.1
+ ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.131.cold.2
+ ___57-[MTStopwatchManager didClearAllLapsForStopwatch:sender:]_block_invoke
+ ___57-[MTStopwatchManager didClearAllLapsForStopwatch:sender:]_block_invoke_2
+ ___57-[MTStopwatchManager initWithConnectionProvider:metrics:]_block_invoke
+ ___58-[MTStopwatchManager didPauseLapTimerForStopwatch:sender:]_block_invoke
+ ___58-[MTStopwatchManager didPauseLapTimerForStopwatch:sender:]_block_invoke_2
+ ___58-[MTStopwatchManager didResetLapTimerForStopwatch:sender:]_block_invoke
+ ___58-[MTStopwatchManager didResetLapTimerForStopwatch:sender:]_block_invoke_2
+ ___58-[MTStopwatchManager didStartLapTimerForStopwatch:sender:]_block_invoke
+ ___58-[MTStopwatchManager didStartLapTimerForStopwatch:sender:]_block_invoke_2
+ ___59-[MTStopwatchManager didResumeLapTimerForStopwatch:sender:]_block_invoke
+ ___59-[MTStopwatchManager didResumeLapTimerForStopwatch:sender:]_block_invoke_2
+ ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.251
+ ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.122.cold.1
+ ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.123
+ ___70-[MTStopwatchServer didLapLapTimerForStopwatch:withCompletion:source:]_block_invoke
+ ___71-[MTStopwatchServer didClearAllLapsForStopwatch:withCompletion:source:]_block_invoke
+ ___72-[MTStopwatchServer didPauseLapTimerForStopwatch:withCompletion:source:]_block_invoke
+ ___72-[MTStopwatchServer didResetLapTimerForStopwatch:withCompletion:source:]_block_invoke
+ ___72-[MTStopwatchServer didStartLapTimerForStopwatch:withCompletion:source:]_block_invoke
+ ___73-[MTStopwatchServer didResumeLapTimerForStopwatch:withCompletion:source:]_block_invoke
+ ___76-[MTStopwatchManager initWithConnectionProvider:metrics:notificationCenter:]_block_invoke
+ ___76-[MTStopwatchManagerExportedObject _didReceiveTimerServerReadyNotification:]_block_invoke
+ ___83-[MTStopwatchManagerExportedObject publishEvent:withStopwatch:modifiedItem:source:]_block_invoke
+ ___MTStopwatchClientInterface_block_invoke
+ ___MTStopwatchServerInterface_block_invoke
+ ___block_descriptor_32_e29_v16?0"<MTStopwatchServer>"8l
+ ___block_descriptor_32_e53_"MTXPCConnectionProvider"16?0"MTStopwatchManager"8l
+ ___block_descriptor_40_e8_32s_e29_v16?0"<MTStopwatchClient>"8ls32l8
+ ___block_descriptor_40_e8_32s_e29_v16?0"<MTStopwatchServer>"8ls32l8
+ ___block_descriptor_40_e8_32s_e31_v16?0"UNNotificationRequest"8ls32l8
+ ___block_descriptor_40_e8_32s_e53_"MTXPCConnectionProvider"16?0"MTStopwatchManager"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e29_v16?0"<MTStopwatchServer>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e29_v16?0"<MTStopwatchClient>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e29_v16?0"<MTStopwatchServer>"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v16?0"<MTStopwatchServer>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56w_e17_v16?0"NSError"8ls32l8s40l8w56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e17_v16?0"NSError"8ls32l8s40l8w64l8s48l8s56l8
+ ___block_literal_global.102
+ ___block_literal_global.134
+ ___block_literal_global.135
+ ___block_literal_global.138
+ ___block_literal_global.143
+ ___block_literal_global.147
+ ___block_literal_global.162
+ ___block_literal_global.171
+ ___block_literal_global.202
+ ___block_literal_global.230
+ ___block_literal_global.246
+ ___block_literal_global.335
+ ___block_literal_global.348
+ ___block_literal_global.53
+ ___block_literal_global.74
+ ___block_literal_global.78
+ ___block_literal_global.84
+ ___getMTStopwatchStorageClass_block_invoke
+ ___getMTStopwatchStorageClass_block_invoke.cold.1
+ ___getMTStopwatchStorageClass_block_invoke.cold.2
+ __dateFormatter
+ _dateFormatter
+ _getMTStopwatchStorageClass.softClass
+ _kMTDefaultAlarmMediaItemIDDefaultsKey
+ _kMTDefaultAlarmSoundTypeDefaultsKey
+ _kMTDefaultAlarmToneIDDefaultsKey
+ _kMTDefaultAlarmVibrationIDDefaultsKey
+ _objc_msgSend$_clearOutInvalidToneIdentifiers
+ _objc_msgSend$_copyStateOntoStopwatch:
+ _objc_msgSend$_isEqualToStopwatch:
+ _objc_msgSend$_setupStopwatches
+ _objc_msgSend$autoupdatingCurrentLocale
+ _objc_msgSend$clearInvalidPendingNotifications
+ _objc_msgSend$commonInit
+ _objc_msgSend$createStopWatch:withCompletion:source:
+ _objc_msgSend$createStopwatch:withCompletion:
+ _objc_msgSend$currentInterval
+ _objc_msgSend$deleteStopwatch:withCompletion:
+ _objc_msgSend$deleteStopwatch:withCompletion:source:
+ _objc_msgSend$didAddLap:forStopwatch:
+ _objc_msgSend$didAddLap:forStopwatch:source:
+ _objc_msgSend$didAddLap:forStopwatch:withCompletion:
+ _objc_msgSend$didAddLap:forStopwatch:withCompletion:source:
+ _objc_msgSend$didClearAllLapsForStopwatch:
+ _objc_msgSend$didClearAllLapsForStopwatch:source:
+ _objc_msgSend$didClearAllLapsForStopwatch:withCompletion:
+ _objc_msgSend$didClearAllLapsForStopwatch:withCompletion:source:
+ _objc_msgSend$didCreateStopwatch:
+ _objc_msgSend$didDeleteStopwatch:
+ _objc_msgSend$didLapLapTimerForStopwatch:
+ _objc_msgSend$didLapLapTimerForStopwatch:source:
+ _objc_msgSend$didLapLapTimerForStopwatch:withCompletion:
+ _objc_msgSend$didLapLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didPauseLapTimerForStopwatch:
+ _objc_msgSend$didPauseLapTimerForStopwatch:source:
+ _objc_msgSend$didPauseLapTimerForStopwatch:withCompletion:
+ _objc_msgSend$didPauseLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didResetLapTimerForStopwatch:
+ _objc_msgSend$didResetLapTimerForStopwatch:source:
+ _objc_msgSend$didResetLapTimerForStopwatch:withCompletion:
+ _objc_msgSend$didResetLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didResumeLapTimerForStopwatch:
+ _objc_msgSend$didResumeLapTimerForStopwatch:source:
+ _objc_msgSend$didResumeLapTimerForStopwatch:withCompletion:
+ _objc_msgSend$didResumeLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didStartLapTimerForStopwatch:
+ _objc_msgSend$didStartLapTimerForStopwatch:source:
+ _objc_msgSend$didStartLapTimerForStopwatch:withCompletion:
+ _objc_msgSend$didStartLapTimerForStopwatch:withCompletion:source:
+ _objc_msgSend$didUpdateStopwatch:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$getStopwatchesWitchCompletion:
+ _objc_msgSend$getStopwatchesWithCompletion:
+ _objc_msgSend$initWithConnectionProvider:metrics:notificationCenter:
+ _objc_msgSend$initWithId:
+ _objc_msgSend$initWithStopwatchManager:
+ _objc_msgSend$laps
+ _objc_msgSend$offset
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$previousLapsTotalInterval
+ _objc_msgSend$publishEvent:withStopwatch:modifiedItem:
+ _objc_msgSend$publishEvent:withStopwatch:modifiedItem:source:
+ _objc_msgSend$publishEvent:withStopwatch:source:
+ _objc_msgSend$setCurrentInterval:
+ _objc_msgSend$setLaps:
+ _objc_msgSend$setOffset:
+ _objc_msgSend$setPreviousLapsTotalInterval:
+ _objc_msgSend$setStartDate:
+ _objc_msgSend$setStorage:
+ _objc_msgSend$setSystemReady
+ _objc_msgSend$shortWeekdaySymbols
+ _objc_msgSend$stopwatchManager
+ _objc_msgSend$updateStopwatch:withCompletion:
+ _objc_msgSend$updateStopwatch:withCompletion:source:
+ _objc_msgSend$weekdaySymbols
+ _orderedWeekdaySymbols
- __OBJC_$_PROP_LIST_MTAlarmStorage.378
- __OBJC_$_PROP_LIST_MTSleepModeManager.60
- __OBJC_$_PROP_LIST_MTSleepSessionTracker.125
- __OBJC_$_PROP_LIST_MTTimerStorage.293
- ___44-[MTSleepSessionManager deviceFirstUnlocked]_block_invoke.245
- ___48-[MTSessionsCoordinator source:didRemoveAlarms:]_block_invoke.134
- ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke.139
- ___49-[MTSessionsCoordinator didRestoreAlarmSessions:]_block_invoke_2.140
- ___49-[MTSessionsCoordinator didRestoreTimerSessions:]_block_invoke.144
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.69
- ___51-[MTAlarmStorage _queue_resetAlarmsTo:sleepAlarms:]_block_invoke.69.cold.1
- ___51-[MTSessionsCoordinator repeatTimerWithIdentifier:]_block_invoke.119
- ___51-[MTSessionsCoordinator repeatTimerWithIdentifier:]_block_invoke.119.cold.1
- ___52-[MTSessionsCoordinator dismissTimerWithIdentifier:]_block_invoke.120
- ___52-[MTSessionsCoordinator dismissTimerWithIdentifier:]_block_invoke.120.cold.1
- ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.129
- ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.130.cold.1
- ___57-[MTSessionsCoordinator source:didFireAlarm:triggerType:]_block_invoke.130.cold.2
- ___64-[MTSleepSessionManager sleepSessionTracker:sessionDidComplete:]_block_invoke.227
- ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.121
- ___68-[MTSessionsCoordinator dismissTimerAndEndSessionWithId:completion:]_block_invoke.121.cold.1
- ___block_literal_global.137
- ___block_literal_global.142
- ___block_literal_global.146
- ___block_literal_global.154
- ___block_literal_global.229
- ___block_literal_global.245
- ___block_literal_global.334
- ___block_literal_global.347
- ___block_literal_global.77
- ___block_literal_global.80
- ___block_literal_global.98
CStrings:
+ "\x031"
+ "\x1f\x0f"
+ "%{public}@ - Publishing event: %{public}@, for stopwatch id: %{public}@, source identifier: %{public}@"
+ "%{public}@ Cleaning out invalid tone identifiers"
+ "%{public}@ System isn't ready..."
+ "%{public}@ addLap for: %{public}@"
+ "%{public}@ clearInvalidPendingNotifications"
+ "%{public}@ createStopwatch with id: %{public}@"
+ "%{public}@ createStopwatch:%{public}@"
+ "%{public}@ deleteStopwatch with id: %{public}@"
+ "%{public}@ didAddLap lap: %{public}@ for stopwatch: %{public}@"
+ "%{public}@ didClearAllLapsForStopwatch for stopwatch: %{public}@"
+ "%{public}@ didClearAllLapsForStopwatch for: %{public}@"
+ "%{public}@ didLapLapTimerForStopwatch for stopwatch: %{public}@"
+ "%{public}@ didLapLapTimerForStopwatch for: %{public}@"
+ "%{public}@ didPauseLapTimerForStopwatch for stopwatch: %{public}@"
+ "%{public}@ didPauseLapTimerForStopwatch for: %{public}@"
+ "%{public}@ didResetLapTimerForStopwatch for stopwatch: %{public}@"
+ "%{public}@ didResetLapTimerForStopwatch for: %{public}@"
+ "%{public}@ didResumeLapTimerForStopwatch for stopwatch: %{public}@"
+ "%{public}@ didResumeLapTimerForStopwatch for: %{public}@"
+ "%{public}@ didStartLapTimerForStopwatch for stopwatch: %{public}@"
+ "%{public}@ didStartLapTimerForStopwatch for: %{public}@"
+ "%{public}@ getStopwatches"
+ "%{public}@ getStopwatchesWithCompletion"
+ "%{public}@ handleSystemReady"
+ "%{public}@ initialized exported object, manager: %{public}@"
+ "%{public}@ initialized with storage: %{public}@ "
+ "%{public}@ no pending notifications to remove"
+ "%{public}@ received MTStopwatchServerReadyNotification"
+ "%{public}@ recieved stopwatch write error: %{public}@"
+ "%{public}@ removeStopwatch: %{public}@"
+ "%{public}@ removing all pending notifications"
+ "%{public}@ retrieved pending notification with alarm id: %{public}@, category id: %{public}@, user info: %{public}@"
+ "%{public}@ startListening"
+ "%{public}@ stopListening"
+ "%{public}@ updateStopwatch with id: %{public}@"
+ "%{public}@ updateStopwatch: %{public}@"
+ "%{public}@ wrote to stopwatch store successfully supposedly"
+ "<%@:%p, id:%@, state:%@, startDate:%@, offset:%f, currentInterval:%f, previousLapsTotalInterval:%f, laps:%@, title:%@>"
+ "@\"MTStopwatchManager\""
+ "@\"MTStopwatchManagerExportedObject\""
+ "@\"MTStopwatchServer\""
+ "@\"MTStopwatchStorage\""
+ "@\"MTXPCConnectionProvider\"16@?0@\"MTStopwatchManager\"8"
+ "@\"NAFuture\"24@0:8@\"MTStopwatch\"16"
+ "@\"NAFuture\"32@0:8@\"MTStopwatch\"16@\"<MTSource>\"24"
+ "@\"NAFuture\"40@0:8@\"NSNumber\"16@\"MTStopwatch\"24@\"<MTSource>\"32"
+ "Class getMTStopwatchStorageClass(void)_block_invoke"
+ "MTMutableStopwatch"
+ "MTStopwatch"
+ "MTStopwatchClient"
+ "MTStopwatchCurrentInterval"
+ "MTStopwatchHeaders.h"
+ "MTStopwatchIdentifier"
+ "MTStopwatchLaps"
+ "MTStopwatchManager"
+ "MTStopwatchManager - Adding Stopwatch"
+ "MTStopwatchManager - Deleting Stopwatch"
+ "MTStopwatchManager - Stopwatch Updated"
+ "MTStopwatchManager - Stopwatch created"
+ "MTStopwatchManager - Updating Stopwatch"
+ "MTStopwatchManager - adding lap for stopwatch"
+ "MTStopwatchManager - didClearAllLapsForStopwatch"
+ "MTStopwatchManager - didLapLapTimerForStopwatch"
+ "MTStopwatchManager - didPauseLapTimerForStopwatch"
+ "MTStopwatchManager - didResetLapTimerForStopwatch"
+ "MTStopwatchManager - didResumeLapTimerForStopwatch"
+ "MTStopwatchManager - didStartLapTimerForStopwatch"
+ "MTStopwatchManager - getting stopwatches"
+ "MTStopwatchManagerDidClearAllLaps"
+ "MTStopwatchManagerDidLapLapTimer"
+ "MTStopwatchManagerDidPauseLapTimer"
+ "MTStopwatchManagerDidResetLapTimer"
+ "MTStopwatchManagerDidResumeLapTimer"
+ "MTStopwatchManagerDidStartLapTimer"
+ "MTStopwatchManagerExportedObject"
+ "MTStopwatchManagerLapAdded"
+ "MTStopwatchManagerModifiedItemKey"
+ "MTStopwatchManagerProtocol"
+ "MTStopwatchManagerStateReset"
+ "MTStopwatchManagerStopwatchCreated"
+ "MTStopwatchManagerStopwatchDeleted"
+ "MTStopwatchManagerStopwatchUpdated"
+ "MTStopwatchOffset"
+ "MTStopwatchPreviousLapsTotalInterval"
+ "MTStopwatchPublishing"
+ "MTStopwatchServer"
+ "MTStopwatchSourceIdentifierKey"
+ "MTStopwatchStartDate"
+ "MTStopwatchState"
+ "MTStopwatchStorage"
+ "MTStopwatchStoreObserver"
+ "MTStopwatchTitle"
+ "Stopwatch"
+ "Stopwatches"
+ "T@\"MTStopwatchManager\",R,W,N,V_stopwatchManager"
+ "T@\"MTStopwatchManagerExportedObject\",&,N,V_exportedObject"
+ "T@\"MTStopwatchServer\",&,N,V_stopwatchServer"
+ "T@\"MTStopwatchStorage\",&,N,V_storage"
+ "T@\"NSArray\",C,N,V_laps"
+ "T@\"NSDate\",?,R,N"
+ "T@\"NSDate\",C,N,V_startDate"
+ "T@\"NSNotificationCenter\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "T@,?,R,N"
+ "TB,R,N,V_systemReady"
+ "Td,N,V_currentInterval"
+ "Td,N,V_offset"
+ "Td,N,V_previousLapsTotalInterval"
+ "Tq,N,V_state"
+ "_clearOutInvalidToneIdentifiers"
+ "_copyStateOntoStopwatch:"
+ "_currentInterval"
+ "_isEqualToStopwatch:"
+ "_laps"
+ "_offset"
+ "_previousLapsTotalInterval"
+ "_setupStopwatches"
+ "_stopwatchManager"
+ "_stopwatchServer"
+ "autoupdatingCurrentLocale"
+ "clearInvalidPendingNotifications"
+ "com.apple.MTStopwatchServer.ready"
+ "com.apple.MTStopwatchServer.wakeup"
+ "com.apple.MobileTimer.stopwatchserver"
+ "com.apple.mobiletimer.stopwatchserver.serializer"
+ "com.apple.mobiletimerd.MTStopwatchServer.wakeup"
+ "commonInit"
+ "createStopWatch:withCompletion:source:"
+ "createStopwatch:"
+ "createStopwatch:withCompletion:"
+ "currentInterval"
+ "deleteStopwatch:withCompletion:"
+ "deleteStopwatch:withCompletion:source:"
+ "didAddLap:forStopwatch:"
+ "didAddLap:forStopwatch:sender:"
+ "didAddLap:forStopwatch:source:"
+ "didAddLap:forStopwatch:withCompletion:"
+ "didAddLap:forStopwatch:withCompletion:source:"
+ "didClearAllLapsForStopwatch:"
+ "didClearAllLapsForStopwatch:sender:"
+ "didClearAllLapsForStopwatch:source:"
+ "didClearAllLapsForStopwatch:withCompletion:"
+ "didClearAllLapsForStopwatch:withCompletion:source:"
+ "didCreateStopWatch:source:"
+ "didCreateStopwatch:"
+ "didDeleteStopwatch:"
+ "didDeleteStopwatch:source:"
+ "didLapLapTimerForStopwatch:"
+ "didLapLapTimerForStopwatch:sender:"
+ "didLapLapTimerForStopwatch:source:"
+ "didLapLapTimerForStopwatch:withCompletion:"
+ "didLapLapTimerForStopwatch:withCompletion:source:"
+ "didPauseLapTimerForStopwatch:"
+ "didPauseLapTimerForStopwatch:sender:"
+ "didPauseLapTimerForStopwatch:source:"
+ "didPauseLapTimerForStopwatch:withCompletion:"
+ "didPauseLapTimerForStopwatch:withCompletion:source:"
+ "didResetLapTimerForStopwatch:"
+ "didResetLapTimerForStopwatch:sender:"
+ "didResetLapTimerForStopwatch:source:"
+ "didResetLapTimerForStopwatch:withCompletion:"
+ "didResetLapTimerForStopwatch:withCompletion:source:"
+ "didResumeLapTimerForStopwatch:"
+ "didResumeLapTimerForStopwatch:sender:"
+ "didResumeLapTimerForStopwatch:source:"
+ "didResumeLapTimerForStopwatch:withCompletion:"
+ "didResumeLapTimerForStopwatch:withCompletion:source:"
+ "didStartLapTimerForStopwatch:"
+ "didStartLapTimerForStopwatch:sender:"
+ "didStartLapTimerForStopwatch:source:"
+ "didStartLapTimerForStopwatch:withCompletion:"
+ "didStartLapTimerForStopwatch:withCompletion:source:"
+ "didUpdateStopwatch:"
+ "didUpdateStopwatch:source:"
+ "filteredArrayUsingPredicate:"
+ "getStopwatches"
+ "getStopwatchesWitchCompletion:"
+ "getStopwatchesWithCompletion:"
+ "initWithId:"
+ "initWithStopwatchManager:"
+ "initWithoutXpc:"
+ "laps"
+ "offset"
+ "predicateWithFormat:"
+ "previousLapsTotalInterval"
+ "publishEvent:withStopwatch:"
+ "publishEvent:withStopwatch:modifiedItem:"
+ "publishEvent:withStopwatch:modifiedItem:source:"
+ "publishEvent:withStopwatch:source:"
+ "removeStopwatch:"
+ "self IN %@"
+ "setCurrentInterval:"
+ "setLaps:"
+ "setOffset:"
+ "setPreviousLapsTotalInterval:"
+ "setStopwatchServer:"
+ "setSystemReady"
+ "shortWeekdaySymbols"
+ "stopwatchManager"
+ "stopwatchServer"
+ "testStopwatchWrite"
+ "updateStopwatch:"
+ "updateStopwatch:withCompletion:"
+ "updateStopwatch:withCompletion:source:"
+ "v16@?0@\"<MTStopwatchClient>\"8"
+ "v16@?0@\"<MTStopwatchServer>\"8"
+ "v16@?0@\"UNNotificationRequest\"8"
+ "v24@0:8@\"MTStopwatch\"16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v32@0:8@\"MTStopwatch\"16@\"<MTSource>\"24"
+ "v32@0:8@\"MTStopwatch\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSNumber\"16@\"MTStopwatch\"24"
+ "v40@0:8@\"MTStopwatch\"16@?<v@?@\"NSError\">24@\"<MTSource>\"32"
+ "v40@0:8@\"NSNumber\"16@\"MTStopwatch\"24@\"<MTSource>\"32"
+ "v40@0:8@\"NSNumber\"16@\"MTStopwatch\"24@?<v@?@\"NSError\">32"
+ "weekdaySymbols"
- "\x1f\x0e"
- "T@\"NSNotificationCenter\",R,N"
- "T@,R,N"

```
