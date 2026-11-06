## DistributedSensing

> `/System/Library/PrivateFrameworks/DistributedSensing.framework/Versions/A/DistributedSensing`

```diff

-1.12.0.0.0
-  __TEXT.__text: 0xd394
-  __TEXT.__objc_methlist: 0xb54
-  __TEXT.__cstring: 0x5a8
-  __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x580
-  __TEXT.__oslogstring: 0x1d59
-  __TEXT.__unwind_info: 0x378
+2.4.0.0.0
+  __TEXT.__text: 0x179bc
+  __TEXT.__objc_methlist: 0x1654
+  __TEXT.__const: 0x70
+  __TEXT.__cstring: 0x8e3
+  __TEXT.__oslogstring: 0x283a
+  __TEXT.__gcc_except_tab: 0x658
+  __TEXT.__unwind_info: 0x640
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c8
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__const: 0x258
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x708
-  __DATA_CONST.__objc_superrefs: 0x68
-  __DATA_CONST.__got: 0xf8
-  __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x1e20
-  __AUTH_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__objc_selrefs: 0xbd8
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__got: 0x1b0
+  __AUTH_CONST.__const: 0x5d0
+  __AUTH_CONST.__cfstring: 0x540
+  __AUTH_CONST.__objc_const: 0x3220
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x15c
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x2a8
   __DATA.__data: 0x120
-  __DATA.__bss: 0x8
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x18
+  - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics

   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 257
-  Symbols:   744
-  CStrings:  211
+  Functions: 570
+  Symbols:   1363
+  CStrings:  357
 
Symbols:
+ -[DSAdvertiseManager .cxx_destruct]
+ -[DSAdvertiseManager _getAdvertisementFields]
+ -[DSAdvertiseManager _setDSActionFieldsInAdvertiser:]
+ -[DSAdvertiseManager _setDSInfoFieldsInAdvertiser:]
+ -[DSAdvertiseManager dispatchQueue]
+ -[DSAdvertiseManager dsAdvertiseFlags]
+ -[DSAdvertiseManager setDispatchQueue:]
+ -[DSAdvertiseManager setDsAdvertiseFlags:]
+ -[DSAdvertiseManager setXpcDaemonServer:]
+ -[DSAdvertiseManager startAdvertising]
+ -[DSAdvertiseManager stopAdvertising]
+ -[DSAdvertiseManager xpcDaemonServer]
+ -[DSCohortManager .cxx_destruct]
+ -[DSCohortManager _deviceFound:]
+ -[DSCohortManager _deviceLost:]
+ -[DSCohortManager deviceFound:]
+ -[DSCohortManager deviceLost:]
+ -[DSCohortManager devices]
+ -[DSCohortManager dispatchQueue]
+ -[DSCohortManager printConsensusDataFromWindowStart:ToWindowEnd:]
+ -[DSCohortManager printConsensusData]
+ -[DSCohortManager setDevices:]
+ -[DSCohortManager setDispatchQueue:]
+ -[DSCohortManager setXpcDaemonServer:]
+ -[DSCohortManager xpcDaemonServer]
+ -[DSConsensusDataManager .cxx_destruct]
+ -[DSConsensusDataManager _addDatumToFrequencyTable:]
+ -[DSConsensusDataManager _addDatumtoDataArrayMap:]
+ -[DSConsensusDataManager _evictOldestDatum]
+ -[DSConsensusDataManager _removeDatumFromDataArrayMap:]
+ -[DSConsensusDataManager _removeDatumFromFrequencyTable:]
+ -[DSConsensusDataManager addDatum:]
+ -[DSConsensusDataManager consensusDataArrayMap]
+ -[DSConsensusDataManager consensusDataArray]
+ -[DSConsensusDataManager consensusFrequencyTable]
+ -[DSConsensusDataManager initWithWindowOfInterest:]
+ -[DSConsensusDataManager printConsensusDataFromWindowStart:ToWindowEnd:]
+ -[DSConsensusDataManager printConsensusData]
+ -[DSConsensusDataManager setConsensusDataArray:]
+ -[DSConsensusDataManager setConsensusDataArrayMap:]
+ -[DSConsensusDataManager setConsensusFrequencyTable:]
+ -[DSConsensusDatum .cxx_destruct]
+ -[DSConsensusDatum confidence]
+ -[DSConsensusDatum identifier]
+ -[DSConsensusDatum initWithIdentifier:andConfidence:atTime:]
+ -[DSConsensusDatum printInfo]
+ -[DSConsensusDatum setConfidence:]
+ -[DSConsensusDatum setIdentifier:]
+ -[DSConsensusDatum setTime:]
+ -[DSConsensusDatum time]
+ -[DSDeviceContext .cxx_destruct]
+ -[DSDeviceContext bleDevice]
+ -[DSDeviceContext changedFlag]
+ -[DSDeviceContext coordinationStatus]
+ -[DSDeviceContext discoveryFlag]
+ -[DSDeviceContext dsActionIsAlreadyFound]
+ -[DSDeviceContext dsInfoIsAlreadyFound]
+ -[DSDeviceContext encodeSelf:]
+ -[DSDeviceContext identifier]
+ -[DSDeviceContext initWithCBDevice:error:]
+ -[DSDeviceContext initWithXPCObject:error:]
+ -[DSDeviceContext isMe]
+ -[DSDeviceContext setBleDevice:]
+ -[DSDeviceContext setChangedFlag:]
+ -[DSDeviceContext setCoordinationStatus:]
+ -[DSDeviceContext setDiscoveryFlag:]
+ -[DSDeviceContext setDsActionIsAlreadyFound:]
+ -[DSDeviceContext setDsInfoIsAlreadyFound:]
+ -[DSDeviceContext setIdentifier:]
+ -[DSDeviceContext setIsMe:]
+ -[DSDeviceContext setTiebreaker:]
+ -[DSDeviceContext setVehicleConfidence:]
+ -[DSDeviceContext setVehicleState:]
+ -[DSDeviceContext tiebreaker]
+ -[DSDeviceContext updateWithCBDevice:]
+ -[DSDeviceContext vehicleConfidence]
+ -[DSDeviceContext vehicleState]
+ -[DSKappaSession .cxx_destruct]
+ -[DSKappaSession _activateXPCHandleReply:]
+ -[DSKappaSession _activateXPC]
+ -[DSKappaSession _activate]
+ -[DSKappaSession _deviceChangedMessage:]
+ -[DSKappaSession _deviceFoundMessage:]
+ -[DSKappaSession _deviceLostMessage:]
+ -[DSKappaSession _getXPCConnection]
+ -[DSKappaSession _handleXPCMessage:]
+ -[DSKappaSession _interrupted]
+ -[DSKappaSession _invalidateXPC]
+ -[DSKappaSession _invalidate]
+ -[DSKappaSession _invalidated]
+ -[DSKappaSession _updateKappaCoordinationStatus:]
+ -[DSKappaSession _xpcEventHandler:]
+ -[DSKappaSession _xpcHandleCompletionBlockReply:error:]
+ -[DSKappaSession activateWithCompletion:]
+ -[DSKappaSession cancelElection]
+ -[DSKappaSession coordinationStatus]
+ -[DSKappaSession deviceChangedHandler]
+ -[DSKappaSession deviceFoundHandler]
+ -[DSKappaSession deviceLostHandler]
+ -[DSKappaSession dispatchQueue]
+ -[DSKappaSession encodeSelf:]
+ -[DSKappaSession initWithXPCObject:error:]
+ -[DSKappaSession init]
+ -[DSKappaSession interruptionHandler]
+ -[DSKappaSession invalidate]
+ -[DSKappaSession invalidationHandler]
+ -[DSKappaSession setCoordinationStatus:]
+ -[DSKappaSession setDeviceChangedHandler:]
+ -[DSKappaSession setDeviceFoundHandler:]
+ -[DSKappaSession setDeviceLostHandler:]
+ -[DSKappaSession setDispatchQueue:]
+ -[DSKappaSession setInterruptionHandler:]
+ -[DSKappaSession setInvalidationHandler:]
+ -[DSKappaSession setTiebreaker:]
+ -[DSKappaSession setXpcConnection:]
+ -[DSKappaSession startElectionWithTimeout:completion:]
+ -[DSKappaSession tiebreaker]
+ -[DSKappaSession updateKappaCoordinationStatus:]
+ -[DSKappaSession xpcConnection]
+ -[DSMotionSession .cxx_destruct]
+ -[DSMotionSession _activateXPCHandleReply:]
+ -[DSMotionSession _activateXPC]
+ -[DSMotionSession _activate]
+ -[DSMotionSession _deviceChangedMessage:]
+ -[DSMotionSession _deviceFoundMessage:]
+ -[DSMotionSession _deviceLostMessage:]
+ -[DSMotionSession _getXPCConnection]
+ -[DSMotionSession _handleXPCMessage:]
+ -[DSMotionSession _interrupted]
+ -[DSMotionSession _invalidateXPC]
+ -[DSMotionSession _invalidate]
+ -[DSMotionSession _invalidated]
+ -[DSMotionSession _printCohort]
+ -[DSMotionSession _updateVehicleState:confidence:]
+ -[DSMotionSession _xpcEventHandler:]
+ -[DSMotionSession _xpcHandleCompletionBlockReply:error:]
+ -[DSMotionSession activateWithCompletion:]
+ -[DSMotionSession deviceChangedHandler]
+ -[DSMotionSession deviceFoundHandler]
+ -[DSMotionSession deviceLostHandler]
+ -[DSMotionSession dispatchQueue]
+ -[DSMotionSession encodeSelf:]
+ -[DSMotionSession initWithXPCObject:error:]
+ -[DSMotionSession interruptionHandler]
+ -[DSMotionSession invalidate]
+ -[DSMotionSession invalidationHandler]
+ -[DSMotionSession printCohort]
+ -[DSMotionSession setDeviceChangedHandler:]
+ -[DSMotionSession setDeviceFoundHandler:]
+ -[DSMotionSession setDeviceLostHandler:]
+ -[DSMotionSession setDispatchQueue:]
+ -[DSMotionSession setInterruptionHandler:]
+ -[DSMotionSession setInvalidationHandler:]
+ -[DSMotionSession setVehicleConfidence:]
+ -[DSMotionSession setVehicleState:]
+ -[DSMotionSession updateVehicleState:confidence:]
+ -[DSMotionSession vehicleConfidence]
+ -[DSMotionSession vehicleState]
+ -[DSScanManager .cxx_destruct]
+ -[DSScanManager _deviceFound:]
+ -[DSScanManager _deviceLost:]
+ -[DSScanManager _shouldUpdateDiscovery]
+ -[DSScanManager _updateBLEDiscoveryFlags]
+ -[DSScanManager deviceFoundHandler]
+ -[DSScanManager deviceLostHandler]
+ -[DSScanManager dispatchQueue]
+ -[DSScanManager dsScanFlags]
+ -[DSScanManager setDeviceFoundHandler:]
+ -[DSScanManager setDeviceLostHandler:]
+ -[DSScanManager setDispatchQueue:]
+ -[DSScanManager setDsScanFlags:]
+ -[DSScanManager startScanning]
+ -[DSScanManager stopScanning]
+ -[DSXPCConnection .cxx_destruct]
+ -[DSXPCConnection _activateKappaSessionMessage:]
+ -[DSXPCConnection _activateMotionSessionMessage:]
+ -[DSXPCConnection _checkEntitlement:error:]
+ -[DSXPCConnection _deviceChangedHandler:]
+ -[DSXPCConnection _deviceFoundHandler:]
+ -[DSXPCConnection _deviceLostHandler:]
+ -[DSXPCConnection _handleXPCMessage:]
+ -[DSXPCConnection _printCohortMessage:]
+ -[DSXPCConnection _updateCoordinationStatusMessage:]
+ -[DSXPCConnection _updateVehicleStateMessage:]
+ -[DSXPCConnection _xpcCohortDeviceMessage:type:]
+ -[DSXPCConnection _xpcConnectionSendEvent:]
+ -[DSXPCConnection _xpcEventHandler:]
+ -[DSXPCConnection _xpcSendReplyForMessage:error:]
+ -[DSXPCConnection activate]
+ -[DSXPCConnection dispatchQueue]
+ -[DSXPCConnection invalidate]
+ -[DSXPCConnection kappaSession]
+ -[DSXPCConnection motionSession]
+ -[DSXPCConnection pid]
+ -[DSXPCConnection setDispatchQueue:]
+ -[DSXPCConnection setKappaSession:]
+ -[DSXPCConnection setMotionSession:]
+ -[DSXPCConnection setPid:]
+ -[DSXPCConnection setXpcConnection:]
+ -[DSXPCConnection setXpcDaemonServer:]
+ -[DSXPCConnection xpcConnection]
+ -[DSXPCConnection xpcDaemonServer]
+ -[DSXPCServer .cxx_destruct]
+ -[DSXPCServer _activate]
+ -[DSXPCServer _deviceFoundHandler:]
+ -[DSXPCServer _deviceLostHandler:]
+ -[DSXPCServer _ensureAdvertiserStarted]
+ -[DSXPCServer _ensureAdvertiserStopped]
+ -[DSXPCServer _ensureScannerStarted]
+ -[DSXPCServer _ensureScannerStopped]
+ -[DSXPCServer _handleXPCConnection:]
+ -[DSXPCServer _invalidate]
+ -[DSXPCServer _receivedXPCObject:]
+ -[DSXPCServer activate]
+ -[DSXPCServer cohortManager]
+ -[DSXPCServer dispatchQueue]
+ -[DSXPCServer init]
+ -[DSXPCServer invalidate]
+ -[DSXPCServer myDeviceContext]
+ -[DSXPCServer removeXPCConnection:]
+ -[DSXPCServer setCohortManager:]
+ -[DSXPCServer setDispatchQueue:]
+ -[DSXPCServer setMyDeviceContext:]
+ -[DSXPCServer updateAdvertiser]
+ -[DSXPCServer updateScanner]
+ -[DSXPCServer xpcConnections]
+ DSLogObjectForCategory_DSDeviceContext
+ DSLogObjectForCategory_DSKappaSession
+ DSLogObjectForCategory_DSMotionSession
+ DSLogObjectForCategory_DSXPCConnection
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table23
+ OBJC_IVAR_$_DSAdvertiseManager._bleAdvertiser
+ OBJC_IVAR_$_DSAdvertiseManager._cbDSActionFlags
+ OBJC_IVAR_$_DSAdvertiseManager._cbTieBreaker
+ OBJC_IVAR_$_DSAdvertiseManager._cbVehicleConfidence
+ OBJC_IVAR_$_DSAdvertiseManager._cbVehicleState
+ OBJC_IVAR_$_DSAdvertiseManager._dispatchQueue
+ OBJC_IVAR_$_DSAdvertiseManager._dsAdvertiseFlags
+ OBJC_IVAR_$_DSAdvertiseManager._xpcDaemonServer
+ OBJC_IVAR_$_DSCohortManager._dataManager
+ OBJC_IVAR_$_DSCohortManager._devices
+ OBJC_IVAR_$_DSCohortManager._dispatchQueue
+ OBJC_IVAR_$_DSCohortManager._xpcDaemonServer
+ OBJC_IVAR_$_DSConsensusDataManager._consensusDataArray
+ OBJC_IVAR_$_DSConsensusDataManager._consensusDataArrayMap
+ OBJC_IVAR_$_DSConsensusDataManager._consensusFrequencyTable
+ OBJC_IVAR_$_DSConsensusDataManager._windowOfInterest
+ OBJC_IVAR_$_DSConsensusDatum._confidence
+ OBJC_IVAR_$_DSConsensusDatum._identifier
+ OBJC_IVAR_$_DSConsensusDatum._time
+ OBJC_IVAR_$_DSDeviceContext._bleDevice
+ OBJC_IVAR_$_DSDeviceContext._changedFlag
+ OBJC_IVAR_$_DSDeviceContext._coordinationStatus
+ OBJC_IVAR_$_DSDeviceContext._discoveryFlag
+ OBJC_IVAR_$_DSDeviceContext._dsActionIsAlreadyFound
+ OBJC_IVAR_$_DSDeviceContext._dsInfoIsAlreadyFound
+ OBJC_IVAR_$_DSDeviceContext._identifier
+ OBJC_IVAR_$_DSDeviceContext._isMe
+ OBJC_IVAR_$_DSDeviceContext._tiebreaker
+ OBJC_IVAR_$_DSDeviceContext._vehicleConfidence
+ OBJC_IVAR_$_DSDeviceContext._vehicleState
+ OBJC_IVAR_$_DSKappaSession._activateCompletionHandler
+ OBJC_IVAR_$_DSKappaSession._coordinationStatus
+ OBJC_IVAR_$_DSKappaSession._deviceChangedHandler
+ OBJC_IVAR_$_DSKappaSession._deviceFoundHandler
+ OBJC_IVAR_$_DSKappaSession._deviceLostHandler
+ OBJC_IVAR_$_DSKappaSession._dispatchQueue
+ OBJC_IVAR_$_DSKappaSession._interruptionHandler
+ OBJC_IVAR_$_DSKappaSession._invalidateFinished
+ OBJC_IVAR_$_DSKappaSession._invalidationHandler
+ OBJC_IVAR_$_DSKappaSession._shouldActivate
+ OBJC_IVAR_$_DSKappaSession._shouldInvalidate
+ OBJC_IVAR_$_DSKappaSession._tiebreaker
+ OBJC_IVAR_$_DSKappaSession._xpcConnection
+ OBJC_IVAR_$_DSMotionSession._activateCompletionHandler
+ OBJC_IVAR_$_DSMotionSession._deviceChangedHandler
+ OBJC_IVAR_$_DSMotionSession._deviceFoundHandler
+ OBJC_IVAR_$_DSMotionSession._deviceLostHandler
+ OBJC_IVAR_$_DSMotionSession._dispatchQueue
+ OBJC_IVAR_$_DSMotionSession._interruptionHandler
+ OBJC_IVAR_$_DSMotionSession._invalidateFinished
+ OBJC_IVAR_$_DSMotionSession._invalidationHandler
+ OBJC_IVAR_$_DSMotionSession._shouldActivate
+ OBJC_IVAR_$_DSMotionSession._shouldInvalidate
+ OBJC_IVAR_$_DSMotionSession._vehicleConfidence
+ OBJC_IVAR_$_DSMotionSession._vehicleState
+ OBJC_IVAR_$_DSMotionSession._xpcConnection
+ OBJC_IVAR_$_DSScanManager._bleDiscovery
+ OBJC_IVAR_$_DSScanManager._bleDiscoveryFlags
+ OBJC_IVAR_$_DSScanManager._deviceFoundHandler
+ OBJC_IVAR_$_DSScanManager._deviceLostHandler
+ OBJC_IVAR_$_DSScanManager._dispatchQueue
+ OBJC_IVAR_$_DSScanManager._dsScanFlags
+ OBJC_IVAR_$_DSXPCConnection._deviceDictionary
+ OBJC_IVAR_$_DSXPCConnection._dispatchQueue
+ OBJC_IVAR_$_DSXPCConnection._isEntitledForKappa
+ OBJC_IVAR_$_DSXPCConnection._isEntitledForMotion
+ OBJC_IVAR_$_DSXPCConnection._kappaSession
+ OBJC_IVAR_$_DSXPCConnection._motionSession
+ OBJC_IVAR_$_DSXPCConnection._pid
+ OBJC_IVAR_$_DSXPCConnection._xpcConnection
+ OBJC_IVAR_$_DSXPCConnection._xpcDaemonServer
+ OBJC_IVAR_$_DSXPCServer._advertiseManager
+ OBJC_IVAR_$_DSXPCServer._cohortManager
+ OBJC_IVAR_$_DSXPCServer._dispatchQueue
+ OBJC_IVAR_$_DSXPCServer._myDeviceContext
+ OBJC_IVAR_$_DSXPCServer._scanManager
+ OBJC_IVAR_$_DSXPCServer._shouldActivate
+ OBJC_IVAR_$_DSXPCServer._shouldAdvertiseDSAction
+ OBJC_IVAR_$_DSXPCServer._shouldAdvertiseDSInfo
+ OBJC_IVAR_$_DSXPCServer._shouldScanDSAction
+ OBJC_IVAR_$_DSXPCServer._shouldScanDSInfo
+ OBJC_IVAR_$_DSXPCServer._xpcConnections
+ OBJC_IVAR_$_DSXPCServer._xpcListener
+ _DSLogObjectForCategory_DSDeviceContext
+ _DSLogObjectForCategory_DSKappaSession
+ _DSLogObjectForCategory_DSMotionSession
+ _DSLogObjectForCategory_DSXPCConnection
+ _OBJC_CLASS_$_CBAdvertiser
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_DSAdvertiseManager
+ _OBJC_CLASS_$_DSCohortManager
+ _OBJC_CLASS_$_DSConsensusDataManager
+ _OBJC_CLASS_$_DSConsensusDatum
+ _OBJC_CLASS_$_DSDeviceContext
+ _OBJC_CLASS_$_DSKappaSession
+ _OBJC_CLASS_$_DSMotionSession
+ _OBJC_CLASS_$_DSScanManager
+ _OBJC_CLASS_$_DSXPCConnection
+ _OBJC_CLASS_$_DSXPCServer
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSSet
+ _OBJC_METACLASS_$_DSAdvertiseManager
+ _OBJC_METACLASS_$_DSCohortManager
+ _OBJC_METACLASS_$_DSConsensusDataManager
+ _OBJC_METACLASS_$_DSConsensusDatum
+ _OBJC_METACLASS_$_DSDeviceContext
+ _OBJC_METACLASS_$_DSKappaSession
+ _OBJC_METACLASS_$_DSMotionSession
+ _OBJC_METACLASS_$_DSScanManager
+ _OBJC_METACLASS_$_DSXPCConnection
+ _OBJC_METACLASS_$_DSXPCServer
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _RPOptionStatusFlags
+ __30-[DSScanManager startScanning]_block_invoke
+ __30-[DSScanManager startScanning]_block_invoke_2
+ __36-[DSXPCServer _ensureScannerStarted]_block_invoke
+ __38-[DSAdvertiseManager startAdvertising]_block_invoke
+ __48-[DSKappaSession updateKappaCoordinationStatus:]_block_invoke
+ __48-[DSXPCConnection _activateKappaSessionMessage:]_block_invoke
+ __49-[DSMotionSession updateVehicleState:confidence:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_DSAdvertiseManager
+ __OBJC_$_INSTANCE_METHODS_DSCohortManager
+ __OBJC_$_INSTANCE_METHODS_DSConsensusDataManager
+ __OBJC_$_INSTANCE_METHODS_DSConsensusDatum
+ __OBJC_$_INSTANCE_METHODS_DSDeviceContext
+ __OBJC_$_INSTANCE_METHODS_DSKappaSession
+ __OBJC_$_INSTANCE_METHODS_DSMotionSession
+ __OBJC_$_INSTANCE_METHODS_DSScanManager
+ __OBJC_$_INSTANCE_METHODS_DSXPCConnection
+ __OBJC_$_INSTANCE_METHODS_DSXPCServer
+ __OBJC_$_INSTANCE_VARIABLES_DSAdvertiseManager
+ __OBJC_$_INSTANCE_VARIABLES_DSCohortManager
+ __OBJC_$_INSTANCE_VARIABLES_DSConsensusDataManager
+ __OBJC_$_INSTANCE_VARIABLES_DSConsensusDatum
+ __OBJC_$_INSTANCE_VARIABLES_DSDeviceContext
+ __OBJC_$_INSTANCE_VARIABLES_DSKappaSession
+ __OBJC_$_INSTANCE_VARIABLES_DSMotionSession
+ __OBJC_$_INSTANCE_VARIABLES_DSScanManager
+ __OBJC_$_INSTANCE_VARIABLES_DSXPCConnection
+ __OBJC_$_INSTANCE_VARIABLES_DSXPCServer
+ __OBJC_$_PROP_LIST_DSAdvertiseManager
+ __OBJC_$_PROP_LIST_DSCohortManager
+ __OBJC_$_PROP_LIST_DSConsensusDataManager
+ __OBJC_$_PROP_LIST_DSConsensusDatum
+ __OBJC_$_PROP_LIST_DSDeviceContext
+ __OBJC_$_PROP_LIST_DSKappaSession
+ __OBJC_$_PROP_LIST_DSMotionSession
+ __OBJC_$_PROP_LIST_DSScanManager
+ __OBJC_$_PROP_LIST_DSXPCConnection
+ __OBJC_$_PROP_LIST_DSXPCServer
+ __OBJC_CLASS_RO_$_DSAdvertiseManager
+ __OBJC_CLASS_RO_$_DSCohortManager
+ __OBJC_CLASS_RO_$_DSConsensusDataManager
+ __OBJC_CLASS_RO_$_DSConsensusDatum
+ __OBJC_CLASS_RO_$_DSDeviceContext
+ __OBJC_CLASS_RO_$_DSKappaSession
+ __OBJC_CLASS_RO_$_DSMotionSession
+ __OBJC_CLASS_RO_$_DSScanManager
+ __OBJC_CLASS_RO_$_DSXPCConnection
+ __OBJC_CLASS_RO_$_DSXPCServer
+ __OBJC_METACLASS_RO_$_DSAdvertiseManager
+ __OBJC_METACLASS_RO_$_DSCohortManager
+ __OBJC_METACLASS_RO_$_DSConsensusDataManager
+ __OBJC_METACLASS_RO_$_DSConsensusDatum
+ __OBJC_METACLASS_RO_$_DSDeviceContext
+ __OBJC_METACLASS_RO_$_DSKappaSession
+ __OBJC_METACLASS_RO_$_DSMotionSession
+ __OBJC_METACLASS_RO_$_DSScanManager
+ __OBJC_METACLASS_RO_$_DSXPCConnection
+ __OBJC_METACLASS_RO_$_DSXPCServer
+ ___23-[DSXPCServer activate]_block_invoke
+ ___24-[DSXPCServer _activate]_block_invoke
+ ___25-[DSXPCServer invalidate]_block_invoke
+ ___27-[DSXPCConnection activate]_block_invoke
+ ___28-[DSKappaSession invalidate]_block_invoke
+ ___29-[DSMotionSession invalidate]_block_invoke
+ ___30-[DSKappaSession _activateXPC]_block_invoke
+ ___30-[DSMotionSession printCohort]_block_invoke
+ ___30-[DSScanManager startScanning]_block_invoke
+ ___30-[DSScanManager startScanning]_block_invoke_2
+ ___31-[DSMotionSession _activateXPC]_block_invoke
+ ___35-[DSKappaSession _getXPCConnection]_block_invoke
+ ___36-[DSMotionSession _getXPCConnection]_block_invoke
+ ___36-[DSXPCServer _ensureScannerStarted]_block_invoke
+ ___38-[DSAdvertiseManager startAdvertising]_block_invoke
+ ___41-[DSKappaSession activateWithCompletion:]_block_invoke
+ ___42-[DSMotionSession activateWithCompletion:]_block_invoke
+ ___48-[DSKappaSession updateKappaCoordinationStatus:]_block_invoke
+ ___48-[DSXPCConnection _activateKappaSessionMessage:]_block_invoke
+ ___48-[DSXPCConnection _activateKappaSessionMessage:]_block_invoke_2
+ ___49-[DSMotionSession updateVehicleState:confidence:]_block_invoke
+ ___49-[DSXPCConnection _activateMotionSessionMessage:]_block_invoke
+ ___49-[DSXPCConnection _activateMotionSessionMessage:]_block_invoke_2
+ ___49-[DSXPCConnection _activateMotionSessionMessage:]_block_invoke_3
+ ___DSLogObjectForCategory_DSAdvertiseManager_block_invoke
+ ___DSLogObjectForCategory_DSCohortManager_block_invoke
+ ___DSLogObjectForCategory_DSConsensus_block_invoke
+ ___DSLogObjectForCategory_DSDeviceContext_block_invoke
+ ___DSLogObjectForCategory_DSKappaSession_block_invoke
+ ___DSLogObjectForCategory_DSMotionSession_block_invoke
+ ___DSLogObjectForCategory_DSScanManager_block_invoke
+ ___DSLogObjectForCategory_DSXPCConnection_block_invoke
+ ___DSLogObjectForCategory_DSXPCServer_block_invoke
+ ___block_descriptor_40_e8_32s_e18_v16?0"CBDevice"8l
+ ___block_descriptor_40_e8_32s_e25_v16?0"DSDeviceContext"8l
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_41_e8_32s_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40s_e18_v16?0"CBDevice"8l
+ ___block_descriptor_50_e8_32s40r_e5_v8?0l
+ __xpc_error_connection_interrupted
+ __xpc_error_connection_invalid
+ __xpc_type_connection
+ __xpc_type_data
+ __xpc_type_dictionary
+ _logObjDSAdvertiseManager
+ _logObjDSCohortManager
+ _logObjDSConsensus
+ _logObjDSDeviceContext
+ _logObjDSKappaSession
+ _logObjDSMotionSession
+ _logObjDSScanManager
+ _logObjDSXPCConnection
+ _logObjDSXPCServer
+ _objc_msgSend$_activate
+ _objc_msgSend$_activateKappaSessionMessage:
+ _objc_msgSend$_activateMotionSessionMessage:
+ _objc_msgSend$_activateXPC
+ _objc_msgSend$_activateXPCHandleReply:
+ _objc_msgSend$_addDatumToFrequencyTable:
+ _objc_msgSend$_addDatumtoDataArrayMap:
+ _objc_msgSend$_checkEntitlement:error:
+ _objc_msgSend$_deviceChangedHandler:
+ _objc_msgSend$_deviceChangedMessage:
+ _objc_msgSend$_deviceFound:
+ _objc_msgSend$_deviceFoundHandler:
+ _objc_msgSend$_deviceFoundMessage:
+ _objc_msgSend$_deviceLost:
+ _objc_msgSend$_deviceLostHandler:
+ _objc_msgSend$_deviceLostMessage:
+ _objc_msgSend$_ensureAdvertiserStarted
+ _objc_msgSend$_ensureAdvertiserStopped
+ _objc_msgSend$_ensureScannerStarted
+ _objc_msgSend$_ensureScannerStopped
+ _objc_msgSend$_evictOldestDatum
+ _objc_msgSend$_getAdvertisementFields
+ _objc_msgSend$_getXPCConnection
+ _objc_msgSend$_handleXPCConnection:
+ _objc_msgSend$_handleXPCMessage:
+ _objc_msgSend$_interrupted
+ _objc_msgSend$_invalidate
+ _objc_msgSend$_invalidateXPC
+ _objc_msgSend$_invalidated
+ _objc_msgSend$_printCohort
+ _objc_msgSend$_printCohortMessage:
+ _objc_msgSend$_receivedXPCObject:
+ _objc_msgSend$_removeDatumFromDataArrayMap:
+ _objc_msgSend$_removeDatumFromFrequencyTable:
+ _objc_msgSend$_setDSActionFieldsInAdvertiser:
+ _objc_msgSend$_setDSInfoFieldsInAdvertiser:
+ _objc_msgSend$_shouldUpdateDiscovery
+ _objc_msgSend$_updateBLEDiscoveryFlags
+ _objc_msgSend$_updateCoordinationStatusMessage:
+ _objc_msgSend$_updateKappaCoordinationStatus:
+ _objc_msgSend$_updateVehicleState:confidence:
+ _objc_msgSend$_updateVehicleStateMessage:
+ _objc_msgSend$_xpcCohortDeviceMessage:type:
+ _objc_msgSend$_xpcConnectionSendEvent:
+ _objc_msgSend$_xpcEventHandler:
+ _objc_msgSend$_xpcHandleCompletionBlockReply:error:
+ _objc_msgSend$_xpcSendReplyForMessage:error:
+ _objc_msgSend$activate
+ _objc_msgSend$addDatum:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$bytes
+ _objc_msgSend$changedFlag
+ _objc_msgSend$cohortManager
+ _objc_msgSend$confidence
+ _objc_msgSend$coordinationStatus
+ _objc_msgSend$deviceChangedHandler
+ _objc_msgSend$deviceFound:
+ _objc_msgSend$deviceFoundHandler
+ _objc_msgSend$deviceLost:
+ _objc_msgSend$deviceLostHandler
+ _objc_msgSend$devices
+ _objc_msgSend$discoveryFlag
+ _objc_msgSend$discoveryFlags
+ _objc_msgSend$dsActionFlags
+ _objc_msgSend$dsActionIsAlreadyFound
+ _objc_msgSend$dsActionTieBreaker
+ _objc_msgSend$dsInfoIsAlreadyFound
+ _objc_msgSend$dsInfoVehicleConfidence
+ _objc_msgSend$dsInfoVehicleState
+ _objc_msgSend$encodeSelf:
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithCBDevice:error:
+ _objc_msgSend$initWithIdentifier:andConfidence:atTime:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$initWithWindowOfInterest:
+ _objc_msgSend$initWithXPCObject:error:
+ _objc_msgSend$kappaSession
+ _objc_msgSend$motionSession
+ _objc_msgSend$myDeviceContext
+ _objc_msgSend$now
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$printConsensusData
+ _objc_msgSend$printConsensusDataFromWindowStart:ToWindowEnd:
+ _objc_msgSend$printInfo
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeXPCConnection:
+ _objc_msgSend$setCoordinationStatus:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDeviceChangedHandler:
+ _objc_msgSend$setDiscoveryFlags:
+ _objc_msgSend$setDsActionFlags:
+ _objc_msgSend$setDsActionTieBreaker:
+ _objc_msgSend$setDsAdvertiseFlags:
+ _objc_msgSend$setDsInfoVehicleConfidence:
+ _objc_msgSend$setDsInfoVehicleState:
+ _objc_msgSend$setDsScanFlags:
+ _objc_msgSend$setIsMe:
+ _objc_msgSend$setNearbyActionType:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setTiebreaker:
+ _objc_msgSend$setVehicleConfidence:
+ _objc_msgSend$setVehicleState:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$setXpcConnection:
+ _objc_msgSend$setXpcDaemonServer:
+ _objc_msgSend$startAdvertising
+ _objc_msgSend$startScanning
+ _objc_msgSend$stopAdvertising
+ _objc_msgSend$stopScanning
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$tiebreaker
+ _objc_msgSend$time
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
+ _objc_msgSend$updateAdvertiser
+ _objc_msgSend$updateScanner
+ _objc_msgSend$updateWithCBDevice:
+ _objc_msgSend$vehicleConfidence
+ _objc_msgSend$vehicleState
+ _objc_msgSend$xpcConnections
+ _objc_opt_class
+ _onceTokenDSAdvertiseManager
+ _onceTokenDSCohortManager
+ _onceTokenDSConsensus
+ _onceTokenDSDeviceContext
+ _onceTokenDSKappaSession
+ _onceTokenDSMotionSession
+ _onceTokenDSScanManager
+ _onceTokenDSXPCConnection
+ _onceTokenDSXPCServer
+ _strcmp
+ _xpc_connection_activate
+ _xpc_connection_cancel
+ _xpc_connection_copy_invalidation_reason
+ _xpc_connection_create_mach_service
+ _xpc_connection_get_audit_token
+ _xpc_connection_get_pid
+ _xpc_connection_send_message
+ _xpc_connection_send_message_with_reply
+ _xpc_connection_set_event_handler
+ _xpc_connection_set_target_queue
+ _xpc_copy_description
+ _xpc_copy_entitlement_for_token
+ _xpc_data_create
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
+ _xpc_dictionary_create
+ _xpc_dictionary_create_reply
+ _xpc_dictionary_expects_reply
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_string
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_string
+ _xpc_dictionary_set_uint64
+ _xpc_dictionary_set_value
+ _xpc_get_type
- __49-[DSListener startMotionDataListenerWithOptions:]_block_invoke_2
- ___49-[DSProvider startMotionDataProviderWithOptions:]_block_invoke_2
CStrings:
+ "Activate"
+ "Activate XPC"
+ "Activate already called"
+ "Activate called after invalidate"
+ "Activated"
+ "Adding device with ID: %@"
+ "Advertisement fields not set"
+ "Allocation failed"
+ "Already updated"
+ "CBAdvertiser Activated"
+ "CBDiscovery Activated"
+ "Call In-Progress"
+ "Changed DSInfo: %d, DSAction %d"
+ "Consensus Datum with ID: %s, Confidence: %s, time: %@"
+ "Coordination status %s"
+ "Crash"
+ "DSAdvertiseManager"
+ "DSCohortManager"
+ "DSConsensus"
+ "DSDeviceContext"
+ "DSKappaSession"
+ "DSKappaSession Interrupted"
+ "DSKappaSession Invalidated"
+ "DSMotionSession"
+ "DSMotionSession Interrupted"
+ "DSMotionSession Invalidated"
+ "DSScanManager"
+ "DSXPCConnection"
+ "DSXPCConnection activated for PID: %d"
+ "DSXPCServer"
+ "Device Changed XPC Message"
+ "Device Found XPC Message"
+ "Device ID %s : Kappa Coordination Status updated from %s to %s"
+ "Device ID %s : Kappa tie breaker updated from %d to %d"
+ "Device ID %s : Vehicle Confidence updated from %s to %s"
+ "Device ID %s : Vehicle State updated from %s to %s"
+ "Device Lost XPC Message"
+ "Device found %@"
+ "Device lost %@"
+ "Discovered DSInfo: %d, DSAction %d"
+ "Discovery flags need to be updated"
+ "Dispatch queue not set"
+ "Ensure Advertiser Started"
+ "Ensure Advertiser Stopped"
+ "Ensure Scanner Started"
+ "Ensure Scanner Stopped"
+ "Entitlement Missing"
+ "Error creating Kappa Session for pid %d"
+ "Error creating Motion Session for pid %d"
+ "Error decoding coordination status"
+ "Error decoding device context"
+ "Error decoding vehicle state"
+ "Error decoding winner context"
+ "Error while unarchiving completion block error"
+ "Fail"
+ "Failed to activate CBAdvertiser"
+ "Failed to activate CBDiscovery"
+ "Failed to activate with error %@"
+ "Failed to init DSDeviceContext with error : %@"
+ "Identifier : %s"
+ "In-Vehicle"
+ "Instance not activated"
+ "Invalid XPC Message :%s"
+ "Invalid window start: %f and end: %f. Configured window of interest: %f"
+ "Invalidate"
+ "Invalidate already called"
+ "Is self device: %s"
+ "Missing entitlement :%s"
+ "NO"
+ "No Message type in XPC"
+ "No message type in XPC"
+ "Not In-Vehicle"
+ "Q"
+ "Removing device with ID: %@"
+ "Send reply error: no connection"
+ "Send reply error: reply creation error"
+ "Set DSAction Discovery flag"
+ "Set DSInfo Discovery flag"
+ "Siri check"
+ "SpatialAudio"
+ "Start Advertising"
+ "Starting Advertiser"
+ "Starting Scanner"
+ "States already updated"
+ "Stop Advertising"
+ "Stopping Scan"
+ "Success"
+ "Tie breaker: %llu"
+ "Unhandled message from distributedsensingd"
+ "Unknown message type in XPC: %s"
+ "Update called after invalidate"
+ "Updating Discovery flags"
+ "Updating Vehicle State from %s to %s"
+ "Updating Vehicle confidence from %s to %s"
+ "Updating device with ID: %@"
+ "Vehicle confidence: %llu"
+ "Vehicle state %s"
+ "Vehicle state : %s"
+ "XPC Connection Invalidated for pid: %d"
+ "XPC Connection Invalidated for reason: %s"
+ "XPC Listener error, received XPC object :%s"
+ "XPC Listener invalidated"
+ "XPC connection not cleaned"
+ "XPC message does not expect reply"
+ "YES"
+ "[DSListenerProxy] observer added. Current Listener client count %u\n"
+ "[DSListenerProxy] observer removed. Current Listener client count %u\n"
+ "com.apple.distributedsensingd"
+ "com.apple.distributedsensingd-kappa"
+ "com.apple.distributedsensingd-motionState"
+ "consensus data array at its maximum capacity: %lu"
+ "dskappafeature"
+ "feature flag not enabled"
+ "highest"
+ "init with invalid dictionary"
+ "kDSCohortPrint"
+ "kDSCoordStatus"
+ "kDSDevCtxDevID"
+ "kDSDevCtxIsMe"
+ "kDSKappaActivate"
+ "kDSKappaUpdate"
+ "kDSMotionActivate"
+ "kDSMotionUpdate"
+ "kDSTiebreaker"
+ "kDSVehicleConfidence"
+ "kDSVehicleState"
+ "kDSXPCDeviceChanged"
+ "kDSXPCDeviceFound"
+ "kDSXPCDeviceLost"
+ "kDSXPCError"
+ "kDSXPCErrorData"
+ "kDSXPCMsg"
+ "kDSXPCSuccess"
+ "low-medium"
+ "lowest"
+ "max listener clients %u\n"
+ "medium"
+ "medium-high"
+ "missing identifier in Device Changed"
+ "missing identifier in Device Found"
+ "missing identifier in Device Lost"
+ "print cohort message"
+ "q"
+ "v16@?0@\"CBDevice\"8"
+ "v16@?0@\"DSDeviceContext\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "window start: %f and end: %f. Configured window of interest: %f"
+ "xpc connection not set"
+ "xpc send message: %s"
+ "yyyy-MM-dd 'at' HH:mm"
- "[DSListenerProxy] observer added. Current Listener client count %lu\n"
- "[DSListenerProxy] observer removed. Current Listener client count %lu\n"
- "max listener clients %lu\n"
- "\x81"
```
