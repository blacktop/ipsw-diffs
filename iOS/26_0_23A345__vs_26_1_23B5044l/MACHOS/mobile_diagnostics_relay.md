## mobile_diagnostics_relay

> `/usr/libexec/mobile_diagnostics_relay`

```diff

-34.0.0.0.0
-  __TEXT.__text: 0x2e4c
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__cstring: 0x10c9
+46.0.0.0.0
+  __TEXT.__text: 0x12a70
+  __TEXT.__auth_stubs: 0xc80
+  __TEXT.__objc_stubs: 0x16e0
+  __TEXT.__objc_methlist: 0xa7c
+  __TEXT.__gcc_except_tab: 0x5ac
+  __TEXT.__objc_methname: 0x1b52
+  __TEXT.__cstring: 0x35d9
+  __TEXT.__objc_classname: 0x138
+  __TEXT.__objc_methtype: 0x893
+  __TEXT.__const: 0x48
+  __TEXT.__oslogstring: 0x22
   __TEXT.__ustring: 0x1b0
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0xf80
+  __TEXT.__unwind_info: 0x478
+  __DATA_CONST.__auth_got: 0x650
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__cfstring: 0x2780
+  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x16b0
+  __DATA.__objc_selrefs: 0x7c8
+  __DATA.__objc_ivar: 0xd0
+  __DATA.__objc_data: 0x370
+  __DATA.__data: 0x1e0
+  __DATA.__bss: 0xa0
+  - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics
+  - /System/Library/Frameworks/CoreNFC.framework/CoreNFC
+  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration
+  - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
-  UUID: 5675F3C8-C1F0-3B13-8821-70D299A6F7AC
-  Functions: 34
-  Symbols:   121
-  CStrings:  302
+  - /usr/lib/libobjc.A.dylib
+  UUID: 42473CC6-0BE0-3720-AA43-4E561F339DCF
+  Functions: 303
+  Symbols:   272
+  CStrings:  1171
 
Symbols:
+ _CBAdvertisementDataServiceUUIDsKey
+ _CHHapticEventParameterIDAudioPitch
+ _CHHapticEventParameterIDAudioVolume
+ _CHHapticEventParameterIDHapticIntensity
+ _CHHapticEventParameterIDHapticSharpness
+ _CHHapticEventTypeAudioContinuous
+ _CHHapticEventTypeHapticContinuous
+ _IOHIDEventGetIntegerValue
+ _IOHIDEventGetType
+ _IOHIDEventSystemClientCreateWithType
+ _IOHIDEventSystemClientRegisterEventCallback
+ _IOHIDEventSystemClientScheduleWithDispatchQueue
+ _IOHIDEventSystemClientUnregisterEventCallback
+ _IOHIDEventSystemClientUnscheduleFromDispatchQueue
+ _NSFileProtectionCompleteUnlessOpen
+ _NSFileProtectionKey
+ _NSStringFromClass
+ _OBJC_CLASS_$_CBCentralManager
+ _OBJC_CLASS_$_CBPeripheralManager
+ _OBJC_CLASS_$_CBUUID
+ _OBJC_CLASS_$_CHHapticEngine
+ _OBJC_CLASS_$_CHHapticEvent
+ _OBJC_CLASS_$_CHHapticEventParameter
+ _OBJC_CLASS_$_CHHapticPattern
+ _OBJC_CLASS_$_NFCNDEFReaderSession
+ _OBJC_CLASS_$_NFCTagReaderSession
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSValue
+ _OBJC_METACLASS_$_NSObject
+ __Block_object_dispose
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __Unwind_Resume
+ ___NSArray0__struct
+ ___objc_personality_v0
+ __dispatch_main_q
+ __dispatch_source_type_signal
+ __dispatch_source_type_timer
+ __objc_empty_cache
+ __os_log_debug_impl
+ __os_log_error_impl
+ __os_log_impl
+ __xpc_error_connection_invalid
+ __xpc_event_key_name
+ __xpc_type_connection
+ _dispatch_async
+ _dispatch_block_create
+ _dispatch_get_global_queue
+ _dispatch_once
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_resume
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_cancel_handler
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_sync
+ _dispatch_time
+ _kLockdownCheckinConnectionInfoKey
+ _kMBTargetDeviceTransferMinutesRemainingNotification
+ _kMBTargetDeviceTransferProgressNotification
+ _lockdown_connect
+ _lockdown_copy_checkin_info
+ _lockdown_copy_value
+ _notify_cancel
+ _notify_get_state
+ _notify_register_check
+ _notify_register_dispatch
+ _objc_alloc
+ _objc_alloc_init
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_autoreleaseReturnValue
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_new
+ _objc_release
+ _objc_release_x1
+ _objc_release_x10
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_release_x9
+ _objc_retain
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x1
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _objc_storeStrong
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_log_create
+ _os_log_type_enabled
+ _os_transaction_create
+ _remote_device_copy_property
+ _remote_device_get_type
+ _remote_device_set_connected_callback
+ _remote_device_set_disconnected_callback
+ _remote_device_start_browsing
+ _signal
+ _sleep
+ _usleep
+ _xpc_connection_cancel
+ _xpc_connection_create_mach_service
+ _xpc_connection_resume
+ _xpc_connection_set_event_handler
+ _xpc_dictionary_get_string
+ _xpc_get_type
+ _xpc_set_event_stream_handler
+ _xpc_string_get_string_ptr
CStrings:
+ "#16@0:8"
+ "%02X"
+ "%@ disconnnected"
+ "%@-%04X-%02X%02X-%04X-%@"
+ "%s enter"
+ "%s exits"
+ "%{public}@"
+ "%{public}s: %{public}@"
+ "(OK) %@ connnected"
+ "(OK) DataMigration Percentage updated to %lld"
+ "(OK) Detected store service. Paring version is %ld"
+ "(OK) Detected wakeup event."
+ "(OK) Migration is done"
+ "(OK) Paring successfully with device ID %@"
+ "(OK) Received notification migrationDidFinish"
+ "(OK) Start advertising migrationDidFinish"
+ "(OK) Start broadcasting migration status"
+ "-[DeviceUtility createTimer:repeat:callback:]"
+ "-[DeviceUtility isBuddySetupDone]"
+ "-[DeviceUtility isMigrationDone]"
+ "-[DeviceUtility queryFromLockdown:key:]"
+ "-[HIDEventMonitor registerParingEventCallback:]"
+ "-[HIDEventMonitor registerWakeupEventCallback:]"
+ "-[HapticPlayer playAudioForTimes:]"
+ "-[HapticPlayer playHapticForDuration:]"
+ "-[HapticPlayer setupHapticEngine]"
+ "-[MDRStateRecorder deleteAllRecords]"
+ "-[MDRStateRecorder updateRecords:]"
+ "-[MigrationBroadcaster peripheralManagerDidUpdateState:]"
+ "-[NFCTagReader registerReadTagCallback:]"
+ "-[NFCTagReader startReading]_block_invoke"
+ "-[NFCTagReader tagReaderSession:didDetectTags:]_block_invoke"
+ "-[NotificationListener _stateForToken:]"
+ "-[NotificationListener _tokenForName:]"
+ "-[NotificationListener _tokenForName:]_block_invoke"
+ "-[ServiceScanner centralManagerDidUpdateState:]"
+ "-[ServiceScanner peripheral:didDiscoverCharacteristicsForService:error:]"
+ "-[ServiceScanner peripheral:didDiscoverServices:]"
+ "-[ServiceScanner peripheral:didUpdateValueForCharacteristic:error:]"
+ "-[ServiceScanner peripheral:didWriteValueForCharacteristic:error:]"
+ "-[StateMachineController handleButtonWakeupEvent]_block_invoke"
+ "-[StateMachineController handleMigrationStartedEvent]_block_invoke"
+ "-[StateMachineController handleMigrationTransferCompletedEvent]_block_invoke"
+ "-[StateMachineController handleParingSuccessEvent]_block_invoke"
+ "-[StateMachineController handleRemoteDeviceAttachEvent]_block_invoke"
+ "-[StateMachineController handleRemoteDeviceDetachEvent]_block_invoke"
+ "-[StateMachineController handleStoreServiceDetectedEvent]_block_invoke"
+ "-[StateMachineController handleTimerTimeoutEvent]_block_invoke"
+ "-[StateMachineController listeningForHIDParingEvent]"
+ "-[StateMachineController listeningForNFCParingEvent]"
+ "-[StateMachineController runBroadcastingMigrationStatusAction]"
+ "-[StateMachineController runInactiveAction]"
+ "-[StateMachineController runListeningForMigrationNotifAction]"
+ "-[StateMachineController runListeningForParingEventAction]"
+ "-[StateMachineController runListeningForWakeupEventAction]"
+ "-[StateMachineController runScanningStoreServiceAction]"
+ "-[StateMachineController runWaitingForMigrationDidFinishAction]"
+ "-[StateMachineController startRemoteDeviceDiscovery]_block_invoke"
+ ".cxx_destruct"
+ "/var/db/"
+ "0123456789ABCDEF"
+ ">>> Transitioning from <%@> to <%@>"
+ "@\"CBCentralManager\""
+ "@\"CBMutableCharacteristic\""
+ "@\"CBPeripheralManager\""
+ "@\"CHHapticEngine\""
+ "@\"NFCTagReaderSession\""
+ "@\"NSArray\""
+ "@\"NSMutableArray\""
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableString\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"NSString\""
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@28@0:8I16@?20"
+ "@32@0:8:16@24"
+ "@32@0:8@16@24"
+ "@32@0:8I16B20@?24"
+ "@40@0:8:16@24@32"
+ "@?"
+ "A fresh start"
+ "Advertising migrationDidFinish completed, exiting"
+ "All notifications are unregistered"
+ "Audio times should > 0"
+ "B"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B24@0:8@?16"
+ "B24@0:8d16"
+ "B24@0:8q16"
+ "B323B328"
+ "B32@0:8@16@?24"
+ "Bluetooth is OFF or unavailable."
+ "Bluetooth is ON."
+ "Broadcasting Migration Status"
+ "Buddy Setup Done: %s. My state is <%@>"
+ "C1C46849-CFBD-4949-A1A5-1E693FA4BA91"
+ "C1C46849-CFBD-4949-A1A5-1E693FA4BA92"
+ "CBCentralManagerDelegate"
+ "CBPeripheralDelegate"
+ "CBPeripheralManagerDelegate"
+ "CHHapticEngine init failed: %@"
+ "CHHapticEngine start failed: %@"
+ "CHHapticEngine stopped: %ld"
+ "CHHapticPatternPlayer start failed: %@"
+ "Can't remove file %@ with error: %@"
+ "Connection invalid"
+ "Controller is already running, ignore it"
+ "Could not create listener for %s"
+ "Create CHHapticPattern failed: %@"
+ "Create CHHapticPatternPlayer failed: %@"
+ "Current DataMigration Percentage is %lld"
+ "Current DataMigration Percentage is %lld, MinsRemaining is %lld"
+ "Current platform doesn't support Core Haptics"
+ "D"
+ "Daemon has been idle for long time, exiting"
+ "Daemon will exit soon"
+ "Daemon will exit soon due to SIGTERM"
+ "Device connnected: ProductType %@, UDID %@, isNCM %d"
+ "Device disconnnected: ProductType %@, UDID %@, isNCM %d"
+ "DeviceID"
+ "DeviceUtility"
+ "EC34D91F-F95E-4B2C-A33C-5C973F4B1255"
+ "Engine is not initialized"
+ "Event 'Button Wakeup' ignored in state <%@>"
+ "Event 'Migration Started' ignored in state <%@>"
+ "Event 'Migration Transfer Compeleted' ignored in state <%@>"
+ "Event 'Paring Success' ignored in state <%@>"
+ "Event 'Remote Device Attach' ignored in state <%@>"
+ "Event 'Remote Device Detach' ignored in state <%@>"
+ "Event 'Store Service Detected' ignored in state <%@>"
+ "Event 'Timer Timeout' ignored in state <%@>"
+ "FATAL! Can't register notification, exiting"
+ "FATAL! Can't register paring event callback, exiting"
+ "FATAL! Can't register wakeup event callback, exiting"
+ "FATAL! Device browser is canceled"
+ "Failed to connect to lockdown daemon"
+ "Failed to create a timer!"
+ "Failed to create long press timer!"
+ "Failed to create parent folder %@ with error: %@"
+ "Failed to get lockdown checkin info"
+ "Failed to init NFC reader sesssion"
+ "Failed to read Migration status"
+ "Failed to read PurpleBuddy status"
+ "Failed to read lockdown %@ domain"
+ "Failed to set attributes for %@ with error: %@"
+ "Failed to write %@"
+ "Get keyCombo: %@"
+ "Got SIGTERM in state <%@>"
+ "Got an incoming lockdown connection"
+ "HID Event: %@ pressed %d"
+ "HIDEventMonitor"
+ "HIDEventMonitor context is nil in callback!"
+ "Handle IO event: %@"
+ "HapticPlayer"
+ "Ignore device connection: already has one device connected"
+ "Ignore device disconnection: not my desired one"
+ "Inactive"
+ "It takes %.2f seconds to be here after reboot"
+ "Key %@ not exist"
+ "Listening For Migration Notification"
+ "Listening For Paring Event"
+ "Listening For Wakeup Event"
+ "Lockdown listener started"
+ "Long press timer fired"
+ "Long press timer started"
+ "MDRBaseObject"
+ "MDRLogger"
+ "MDRStateRecorder"
+ "Migration Done: %s"
+ "MigrationBroadcaster"
+ "MigrationDone"
+ "MobileDiagnosticsRelayState"
+ "Must unregister previous callback first"
+ "My ProductType is %@"
+ "NFC reading is not available on this device."
+ "NFCTagReader"
+ "NFCTagReaderSessionDelegate"
+ "NO"
+ "NSObject"
+ "No valid deviceID returned"
+ "Not a connection type"
+ "Not my business, exiting"
+ "Nothing to do before reboot, return"
+ "Nothing to do for state <%@>"
+ "NotificationListener"
+ "Paring combo string is %@"
+ "Paring event is registered!"
+ "Paring event is unregistered"
+ "Peripheral: %@ (%@) | Cancel connection"
+ "Peripheral: %@ (%@) | Connected"
+ "Peripheral: %@ (%@) | Detected Store Paring Service"
+ "Peripheral: %@ (%@) | Disconnected"
+ "Peripheral: %@ (%@) | Discovered"
+ "Peripheral: %@ (%@) | Error didDiscoverCharacteristicsForService: %@"
+ "Peripheral: %@ (%@) | Error didDiscoverServices: %@"
+ "Peripheral: %@ (%@) | Error didUpdateValueForCharacteristic: %@"
+ "Peripheral: %@ (%@) | Error writing: %@ Perhaps Paring Code not match"
+ "Peripheral: %@ (%@) | Found Store Paring Characteristic"
+ "Peripheral: %@ (%@) | Found Store Paring Service"
+ "Peripheral: %@ (%@) | Paring Version 1"
+ "Peripheral: %@ (%@) | Paring Version 2"
+ "Peripheral: %@ (%@) | Received Device ID: %@"
+ "Peripheral: %@ (%@) | responded with CBATTErrorSuccess"
+ "Power Button"
+ "Q16@0:8"
+ "Q20@0:8i16"
+ "Q24@0:8@16"
+ "Read Migration Done: %s"
+ "Read PurpleBuddy status: %@"
+ "Read tag UID: %@"
+ "Read tag callback is registered"
+ "Read tag callback is unregistered"
+ "Received Invalid Device ID: %@"
+ "Record is expired, timeval: %.2f seconds"
+ "Recovering state <%@> from last exception"
+ "Register for notification %@ token = %d"
+ "Scanning Store Service"
+ "ServiceScanner"
+ "Session %@ | Became active"
+ "Session %@ | Detected NFC tag(s): %@"
+ "Session %@ | Failed to connect to NFC tag with error: %@"
+ "Session %@ | Read MIFARE tag UID: %@"
+ "Session %@ | Restart polling"
+ "Session %@ | Start reading NFC tag..."
+ "Session %@ | Stop reading NFC tag."
+ "Session %@ | Unsupport tag type: %ld"
+ "Session %@ | didDetectTags: possibly an old session, ignore it"
+ "Session %@ | invalidated due to code %ld: %@"
+ "Session %@ | tryReadAgain: possibly an old session, ignore it"
+ "SetupDone"
+ "SetupFinishedAllSteps"
+ "Should never be here, return"
+ "Should not happen. Can't read device identifier"
+ "Should not happen. Invalid DataMigration Percentage %lld"
+ "Start advertising %@"
+ "Start fetching deviceID with paring code: %@"
+ "Start scanning Store Paring Service"
+ "Start to browsing remote device ..."
+ "State DB is empty"
+ "StateMachineController"
+ "StateNumber"
+ "StateString"
+ "Staying in state <%@>"
+ "Stop advertising"
+ "Stop fetching deviceID with paring code: %@"
+ "Stop scanning Store Paring Service"
+ "Store Paring Service detect callback is registered!"
+ "Store Paring Service detect callback is unregistered"
+ "T#,R"
+ "T@\"CBCentralManager\",&,N,V_centralManager"
+ "T@\"CBMutableCharacteristic\",&,N,V_dataMigrationIdentifierCharacteristic"
+ "T@\"CBMutableCharacteristic\",&,N,V_dataMigrationProgressCharacteristic"
+ "T@\"CBPeripheralManager\",&,N,V_peripheralManager"
+ "T@\"NSObject<OS_os_log>\",&,N,V_logger"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "ThinningProductType"
+ "Timeout waiting for advertising start, exiting"
+ "Timeout waiting for device to connect, exiting"
+ "Timeout waiting for migrationDidFinish"
+ "Timeout waiting for paring with HID"
+ "Timeout waiting for paring with NFC"
+ "Timeout waiting for scanning store service"
+ "Timeout waiting for wakeup event"
+ "Timer %p cancelled."
+ "Timer %p fired"
+ "Timer %p started"
+ "Timestamp"
+ "U"
+ "UTF8String"
+ "UUID"
+ "UUIDString"
+ "UUIDWithString:"
+ "UniqueDeviceID"
+ "Unknown Button"
+ "Unknown State"
+ "Updated DataMigration MinsRemaining to %lld"
+ "Updated DataMigration Percentage to %lld"
+ "Volume+ Button"
+ "Volume- Button"
+ "Vv16@0:8"
+ "Waiting For Migration Did Finish"
+ "Wakeup event is registered!"
+ "Wakeup event is unregistered"
+ "YES"
+ "^{_NSZone=}16@0:8"
+ "^{__IOHIDEventSystemClient=}"
+ "_bluetoothOn"
+ "_broadcastQ"
+ "_cacheDB"
+ "_callback"
+ "_callbackQ"
+ "_centralManager"
+ "_cleanupBlock"
+ "_connectedPeripherals"
+ "_connectionQ"
+ "_currentState"
+ "_dataMigrationIdentifierCharacteristic"
+ "_dataMigrationProgressCharacteristic"
+ "_detectCallback"
+ "_deviceID"
+ "_didFinish"
+ "_engine"
+ "_eventSystemClient"
+ "_executeCallbackForToken:withState:"
+ "_filePath"
+ "_hidEventQ"
+ "_identifier"
+ "_idleTimer"
+ "_isRunning"
+ "_logger"
+ "_loggerDict"
+ "_longPressTimer"
+ "_longPressTimerRunning"
+ "_minutes"
+ "_needUpdate"
+ "_pairingSem"
+ "_paringCallback"
+ "_paringCode"
+ "_paringKeyCombo"
+ "_paringVersion"
+ "_percentage"
+ "_peripheralManager"
+ "_queue"
+ "_readerQ"
+ "_scanQ"
+ "_serviceUUIDs"
+ "_session"
+ "_signalSource"
+ "_stateForToken:"
+ "_tokenForName:"
+ "_tokenMap"
+ "_tokensByName"
+ "_transaction"
+ "_transitionQ"
+ "_updateTimer"
+ "_volumeDownPressed"
+ "_volumeUpPressed"
+ "_wakeupCallback"
+ "addEntriesFromDictionary:"
+ "addObject:"
+ "allocatePeripheralsArray"
+ "appendFormat:"
+ "appendString:"
+ "array"
+ "arrayWithObjects:count:"
+ "autorelease"
+ "beginSession"
+ "boolValue"
+ "bytes"
+ "cancelFetchingDeviceID"
+ "cancelLongPressTimer"
+ "cancelPeripheralConnection:"
+ "cancelTimer:"
+ "capabilitiesForHardware"
+ "centralManager"
+ "centralManager:connectionEventDidOccur:forPeripheral:"
+ "centralManager:didConnectPeripheral:"
+ "centralManager:didDisconnectPeripheral:error:"
+ "centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:"
+ "centralManager:didDiscoverPeripheral:advertisementData:RSSI:"
+ "centralManager:didFailToConnectPeripheral:error:"
+ "centralManager:didUpdateANCSAuthorizationForPeripheral:"
+ "centralManager:willRestoreState:"
+ "centralManagerDidUpdateState:"
+ "characterSetWithCharactersInString:"
+ "characteristics"
+ "class"
+ "code"
+ "com.apple.MDR.NCM-deviceQ"
+ "com.apple.MDR.btbroadcastQ"
+ "com.apple.MDR.btconnectionQ"
+ "com.apple.MDR.btscanQ"
+ "com.apple.MDR.callbackQ"
+ "com.apple.MDR.hideventQ"
+ "com.apple.MDR.nfccallbackQ"
+ "com.apple.MDR.nfcreaderQ"
+ "com.apple.MDR.notifyQ"
+ "com.apple.MDR.transitionQ"
+ "com.apple.MobileDiagnosticsRelay"
+ "com.apple.PurpleBuddy"
+ "com.apple.datamigrator.migrationDidFinish"
+ "com.apple.iokit.matching"
+ "com.apple.lockdown.datamigrator"
+ "com.apple.mobile.diagnostics_relay.lockdown"
+ "com.apple.mobile_diagnostics_relay"
+ "com.apple.usbhub.attach"
+ "conformsToProtocol:"
+ "connectPeripheral:"
+ "connectPeripheral:options:"
+ "connectToTag:completionHandler:"
+ "containsObject:"
+ "copy"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createOneshotTimer:callback:"
+ "createPlayerWithPattern:error:"
+ "createRepeatTimer:callback:"
+ "createTimer:repeat:callback:"
+ "dataMigrationIdentifierCharacteristic"
+ "dataMigrationProgressCharacteristic"
+ "dataUsingEncoding:"
+ "date"
+ "debugDescription"
+ "decimalDigitCharacterSet"
+ "defaultManager"
+ "deleteAllRecords"
+ "description"
+ "dictionary"
+ "dictionaryWithContentsOfFile:"
+ "dictionaryWithObjects:forKeys:count:"
+ "disconnectAllPeripherals"
+ "disconnectPeripheral:"
+ "discoverCharacteristics:forService:"
+ "discoverServices:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "fetchingDeviceIDWithParingCode:"
+ "fileExistsAtPath:"
+ "firstObject"
+ "getLocalProductType"
+ "getLogger:"
+ "getParingCode"
+ "getRefactoredServiceUUID"
+ "getRemoteProductType:"
+ "getRemoteUDID:"
+ "gracefulExit"
+ "handleButtonWakeupEvent"
+ "handleIOMatchEvent:"
+ "handleMigrationStartedEvent"
+ "handleMigrationTransferCompletedEvent"
+ "handleParingSuccessEvent"
+ "handleRemoteDeviceAttachEvent"
+ "handleRemoteDeviceDetachEvent"
+ "handleStoreServiceDetectedEvent"
+ "handleTimerTimeoutEvent"
+ "hasPrefix:"
+ "hash"
+ "i24@0:8@16"
+ "identifier"
+ "init"
+ "initAndReturnError:"
+ "initWithData:encoding:"
+ "initWithDelegate:queue:"
+ "initWithEventType:parameters:relativeTime:duration:"
+ "initWithEvents:parameters:error:"
+ "initWithParameterID:value:"
+ "initWithPollingOption:delegate:queue:"
+ "intValue"
+ "invalidateSession"
+ "invertedSet"
+ "isAdvertising"
+ "isBuddySetupDone"
+ "isEqual:"
+ "isEqualToString:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isMigrationDone"
+ "isNCMDevice:"
+ "isProxy"
+ "isScanning"
+ "isValidUUID:"
+ "length"
+ "listeningForHIDParingEvent"
+ "listeningForNFCParingEvent"
+ "localizedDescription"
+ "logger"
+ "mainRunLoop"
+ "notify_get_state failed: %lu"
+ "notify_register_check failed: %lu"
+ "notify_register_check(%@) failed: %lu"
+ "notify_register_dispatch OK"
+ "numberWithInt:"
+ "numberWithInteger:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "pathWithComponents:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "peripheral:didDiscoverCharacteristicsForService:error:"
+ "peripheral:didDiscoverDescriptorsForCharacteristic:error:"
+ "peripheral:didDiscoverIncludedServicesForService:error:"
+ "peripheral:didDiscoverServices:"
+ "peripheral:didModifyServices:"
+ "peripheral:didOpenL2CAPChannel:error:"
+ "peripheral:didReadRSSI:error:"
+ "peripheral:didUpdateNotificationStateForCharacteristic:error:"
+ "peripheral:didUpdateValueForCharacteristic:error:"
+ "peripheral:didUpdateValueForDescriptor:error:"
+ "peripheral:didWriteValueForCharacteristic:error:"
+ "peripheral:didWriteValueForDescriptor:error:"
+ "peripheralDidUpdateName:"
+ "peripheralDidUpdateRSSI:error:"
+ "peripheralIsReadyToSendWriteWithoutResponse:"
+ "peripheralManager"
+ "peripheralManager:central:didSubscribeToCharacteristic:"
+ "peripheralManager:central:didUnsubscribeFromCharacteristic:"
+ "peripheralManager:didAddService:error:"
+ "peripheralManager:didOpenL2CAPChannel:error:"
+ "peripheralManager:didPublishL2CAPChannel:error:"
+ "peripheralManager:didReceiveReadRequest:"
+ "peripheralManager:didReceiveWriteRequests:"
+ "peripheralManager:didUnpublishL2CAPChannel:error:"
+ "peripheralManager:willRestoreState:"
+ "peripheralManagerDidStartAdvertising:error:"
+ "peripheralManagerDidUpdateState:"
+ "peripheralManagerIsReadyToUpdateSubscribers:"
+ "playAudioForTimes:"
+ "playHapticForDuration:"
+ "pointerValue"
+ "q"
+ "q16@0:8"
+ "queryFromLockdown:key:"
+ "rangeOfCharacterFromSet:"
+ "readingAvailable"
+ "recordDeviceID:"
+ "recordState:"
+ "recordTimestamp:"
+ "registerForNotification:callback:"
+ "registerParingEventCallback failed"
+ "registerParingEventCallback:"
+ "registerReadTagCallback:"
+ "registerServiceDetectCallback:"
+ "registerSignalHandle"
+ "registerWakeupEventCallback failed"
+ "registerWakeupEventCallback:"
+ "release"
+ "removeAllObjects"
+ "removeItemAtPath:error:"
+ "respondsToSelector:"
+ "restartPolling"
+ "retain"
+ "retainCount"
+ "returnSavedDeviceID"
+ "returnSavedKey:"
+ "returnSavedState"
+ "returnSavedTimestamp"
+ "run"
+ "runBroadcastingMigrationStatusAction"
+ "runCleanupBlock"
+ "runInactiveAction"
+ "runListeningForMigrationNotifAction"
+ "runListeningForParingEventAction"
+ "runListeningForWakeupEventAction"
+ "runScanningStoreServiceAction"
+ "runWaitingForMigrationDidFinishAction"
+ "scanForPeripheralsWithServices:options:"
+ "self"
+ "services"
+ "setAttributes:ofItemAtPath:error:"
+ "setCentralManager:"
+ "setCleanupBlock:"
+ "setDataMigrationIdentifierCharacteristic:"
+ "setDataMigrationProgressCharacteristic:"
+ "setDelegate:"
+ "setIdentifier:"
+ "setLogger:"
+ "setMigrationPercentage:minsRemaining:didFinish:"
+ "setNotifyValue:forCharacteristic:"
+ "setObject:forKeyedSubscript:"
+ "setParingCode:"
+ "setPeripheralManager:"
+ "setResetHandler:"
+ "setStoppedHandler:"
+ "setValue:forKey:"
+ "setupHapticEngine"
+ "sharedInstance"
+ "startAdvertising:"
+ "startAndReturnError:"
+ "startAtTime:error:"
+ "startReading"
+ "startRemoteDeviceDiscovery"
+ "startScanning"
+ "start_lockdown_listener"
+ "start_lockdown_listener_block_invoke"
+ "start_lockdown_listener_block_invoke_2"
+ "stateForNotification:"
+ "stopAdvertising"
+ "stopReading"
+ "stopScan"
+ "stopScanning"
+ "string"
+ "stringByDeletingLastPathComponent"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "substringToIndex:"
+ "superclass"
+ "supportsHaptics"
+ "tagReaderSession:didDetectTags:"
+ "tagReaderSession:didInvalidateWithError:"
+ "tagReaderSessionDidBecomeActive:"
+ "timeIntervalSinceDate:"
+ "transitionToState:"
+ "triggerSuccessFeedback"
+ "tryReadAgain:"
+ "type"
+ "unregisterAll"
+ "unregisterParingEventCallback"
+ "unregisterServiceDetectCallback"
+ "unregisterWakeupEventCallback"
+ "updateAdvertising"
+ "updateRecords:"
+ "v12@?0B8"
+ "v12@?0i8"
+ "v16@0:8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@\"NSObject<OS_xpc_object>\"8"
+ "v16@?0@\"NSString\"8"
+ "v16@?0@\"OS_remote_device\"8"
+ "v16@?0Q8"
+ "v16@?0^v8"
+ "v16@?0q8"
+ "v20@?0@\"OS_remote_device\"8B16"
+ "v20@?0B8q12"
+ "v24@0:8@\"CBCentralManager\"16"
+ "v24@0:8@\"CBPeripheral\"16"
+ "v24@0:8@\"CBPeripheralManager\"16"
+ "v24@0:8@\"NFCTagReaderSession\"16"
+ "v24@0:8@16"
+ "v24@0:8@?16"
+ "v24@0:8q16"
+ "v28@0:8S16S20B24"
+ "v28@0:8i16Q20"
+ "v32@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24"
+ "v32@0:8@\"CBCentralManager\"16@\"NSDictionary\"24"
+ "v32@0:8@\"CBPeripheral\"16@\"NSArray\"24"
+ "v32@0:8@\"CBPeripheral\"16@\"NSError\"24"
+ "v32@0:8@\"CBPeripheralManager\"16@\"CBATTRequest\"24"
+ "v32@0:8@\"CBPeripheralManager\"16@\"NSArray\"24"
+ "v32@0:8@\"CBPeripheralManager\"16@\"NSDictionary\"24"
+ "v32@0:8@\"CBPeripheralManager\"16@\"NSError\"24"
+ "v32@0:8@\"NFCTagReaderSession\"16@\"NSArray\"24"
+ "v32@0:8@\"NFCTagReaderSession\"16@\"NSError\"24"
+ "v32@0:8@16@24"
+ "v32@?0@\"NSNumber\"8@\"NSValue\"16^B24"
+ "v36@0:8@\"CBPeripheralManager\"16S24@\"NSError\"28"
+ "v36@0:8@16S24@28"
+ "v40@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSError\"32"
+ "v40@0:8@\"CBCentralManager\"16q24@\"CBPeripheral\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBCharacteristic\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBDescriptor\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBL2CAPChannel\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"CBService\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheral\"16@\"NSNumber\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheralManager\"16@\"CBCentral\"24@\"CBCharacteristic\"32"
+ "v40@0:8@\"CBPeripheralManager\"16@\"CBL2CAPChannel\"24@\"NSError\"32"
+ "v40@0:8@\"CBPeripheralManager\"16@\"CBService\"24@\"NSError\"32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16q24@32"
+ "v48@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24@\"NSDictionary\"32@\"NSNumber\"40"
+ "v48@0:8@16@24@32@40"
+ "v52@0:8@\"CBCentralManager\"16@\"CBPeripheral\"24d32B40@\"NSError\"44"
+ "v52@0:8@16@24d32B40@44"
+ "v8@?0"
+ "value"
+ "valueWithPointer:"
+ "void paringEventCallback(void *, void *, void *, IOHIDEventRef)"
+ "void wakeupEventCallback(void *, void *, void *, IOHIDEventRef)"
+ "writeToFile:atomically:"
+ "writeValue:forCharacteristic:type:"
+ "zone"

```
