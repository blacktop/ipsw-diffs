## AudioAccessoryServices

> `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`

```diff

-30.48.2.1.2
-  __TEXT.__text: 0x3e8a0
-  __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_methlist: 0x4e6c
+30.51.1.1.1
+  __TEXT.__text: 0x3d21c
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0x4f8c
   __TEXT.__const: 0x290
   __TEXT.__gcc_except_tab: 0xef0
-  __TEXT.__cstring: 0xb9fe
-  __TEXT.__unwind_info: 0x1030
-  __TEXT.__objc_classname: 0x62e
-  __TEXT.__objc_methname: 0xacd4
-  __TEXT.__objc_methtype: 0x137f
-  __TEXT.__objc_stubs: 0x5a00
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0xed8
+  __TEXT.__cstring: 0xb15a
+  __TEXT.__unwind_info: 0xfd8
+  __TEXT.__objc_classname: 0x63b
+  __TEXT.__objc_methname: 0xaa36
+  __TEXT.__objc_methtype: 0x13b5
+  __TEXT.__objc_stubs: 0x5620
+  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__const: 0xe38
   __DATA_CONST.__objc_classlist: 0x178
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2348
+  __DATA_CONST.__objc_selrefs: 0x22a8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x128
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x448
-  __AUTH_CONST.__const: 0x1c0
-  __AUTH_CONST.__cfstring: 0x2220
-  __AUTH_CONST.__objc_const: 0x9008
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__cfstring: 0x2180
+  __AUTH_CONST.__objc_const: 0x90f8
   __AUTH.__objc_data: 0x7d0
   __AUTH.__data: 0xc0
   __DATA.__objc_ivar: 0x884
-  __DATA.__data: 0xc68
+  __DATA.__data: 0xc58
   __DATA.__common: 0x8
   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x6e0

   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C2ED440-9844-3F06-B54C-D58CDF27E128
-  Functions: 2109
-  Symbols:   6394
-  CStrings:  3983
+  UUID: 55A50FD7-9244-3446-B53C-45C776A03F72
+  Functions: 2096
+  Symbols:   6341
+  CStrings:  3897
 
Symbols:
+ +[AAOVADSensorInfo supportsSecureCoding]
+ +[AASensorInfo supportsSecureCoding]
+ +[AASensorService supportsSecureCoding]
+ -[AAOVADSensorInfo copyWithZone:]
+ -[AAOVADSensorInfo encodeWithCoder:]
+ -[AAOVADSensorInfo initWithBTAddress:]
+ -[AAOVADSensorInfo initWithCoder:]
+ -[AASensorInfo copyWithZone:]
+ -[AASensorInfo encodeWithCoder:]
+ -[AASensorInfo initWithBTAddress:]
+ -[AASensorInfo initWithCoder:]
+ -[AASensorService _activate:]
+ -[AASensorService _activate:].cold.1
+ -[AASensorService _activateXPC:reactivate:]
+ -[AASensorService _activateXPC:reactivate:].cold.1
+ -[AASensorService _broadcastAACPAvailabilities]
+ -[AASensorService _ensureXPCStarted]
+ -[AASensorService _interrupted]
+ -[AASensorService _interrupted].cold.1
+ -[AASensorService _invalidated]
+ -[AASensorService _invalidated].cold.1
+ -[AASensorService _invalidated].cold.2
+ -[AASensorService _reportError:]
+ -[AASensorService _reportError:].cold.1
+ -[AASensorService activateWithCompletion:]
+ -[AASensorService clientID]
+ -[AASensorService description]
+ -[AASensorService encodeWithCoder:]
+ -[AASensorService initWithCoder:]
+ -[AASensorService interruptionHandler]
+ -[AASensorService invalidationHandler]
+ -[AASensorService sensorServiceReportSensorInfo:]
+ -[AASensorService sensorServiceReportSensorInfo:].cold.1
+ -[AASensorService setClientID:]
+ -[AASensorService setInterruptionHandler:]
+ -[AASensorService setInvalidationHandler:]
+ _OBJC_IVAR_$_AASensorService._aaController
+ _OBJC_IVAR_$_AASensorService._activateCompletion
+ _OBJC_IVAR_$_AASensorService._clientID
+ _OBJC_IVAR_$_AASensorService._interruptionHandler
+ _OBJC_IVAR_$_AASensorService._invalidateCalled
+ _OBJC_IVAR_$_AASensorService._invalidateDone
+ _OBJC_IVAR_$_AASensorService._invalidationHandler
+ _OBJC_IVAR_$_AASensorService._ovadDataDict
+ _OBJC_IVAR_$_AASensorService._subscribedSensors
+ _OBJC_IVAR_$_AASensorService._xpcCnx
+ __OBJC_$_CLASS_METHODS_AAOVADSensorInfo
+ __OBJC_$_CLASS_METHODS_AASensorInfo
+ __OBJC_$_CLASS_METHODS_AASensorService
+ __OBJC_$_CLASS_PROP_LIST_AAOVADSensorInfo
+ __OBJC_$_CLASS_PROP_LIST_AASensorInfo
+ __OBJC_$_CLASS_PROP_LIST_AASensorService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_AAOVADSensorInfo
+ __OBJC_CLASS_PROTOCOLS_$_AASensorInfo
+ __OBJC_CLASS_PROTOCOLS_$_AASensorService
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSCopying
+ ___29-[AASensorService _activate:]_block_invoke
+ ___29-[AASensorService _activate:]_block_invoke.cold.1
+ ___29-[AASensorService _activate:]_block_invoke.cold.2
+ ___36-[AASensorService _ensureXPCStarted]_block_invoke
+ ___36-[AASensorService _ensureXPCStarted]_block_invoke_2
+ ___42-[AASensorService activateWithCompletion:]_block_invoke
+ ___42-[AASensorService activateWithCompletion:]_block_invoke.cold.1
+ ___43-[AASensorService _activateXPC:reactivate:]_block_invoke
+ ___43-[AASensorService _activateXPC:reactivate:]_block_invoke.cold.1
+ ___43-[AASensorService _activateXPC:reactivate:]_block_invoke.cold.2
+ ___43-[AASensorService _activateXPC:reactivate:]_block_invoke_2
+ ___block_descriptor_52_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_literal_global.114
+ ___block_literal_global.127
+ ___block_literal_global.130
+ _objc_msgSend$_broadcastAACPAvailabilities
+ _objc_msgSend$initWithBTAddress:
+ _objc_msgSend$ownVoiceActivityLevel
+ _objc_msgSend$sensorServiceActivate:completion:
+ _objc_msgSend$setOwnVoiceActivityLevel:
- -[AAOVADSensorInfo _calculateOwnVoiceActivityLevel]
- -[AAOVADSensorInfo initWithHIDDevice:]
- -[AAOVADSensorInfo update:].cold.1
- -[AAOVADSensorInfo update:].cold.2
- -[AAOVADSensorInfo update:].cold.3
- -[AASensorInfo initWithHIDDevice:]
- -[AASensorService _getBTAddressFromHIDDeviceObject:]
- -[AASensorService _notifyAvailabilityChangedWithForcedUpdate:]
- -[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]
- -[AASensorService _sensorDataAvailabilitiesAdded:]
- -[AASensorService _sensorDataAvailabilitiesLost:]
- -[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]
- -[AASensorService deviceManagerFoundHandler:]
- -[AASensorService deviceNotificationHandler:added:]
- -[AASensorService handleHIDReport:data:]
- _OBJC_CLASS_$_HIDManager
- _OBJC_CLASS_$_NSConstantDictionary
- _OBJC_CLASS_$_NSConstantIntegerNumber
- _OBJC_CLASS_$_NSMutableData
- _OBJC_IVAR_$_AAOVADSensorInfo._rawOwnVoiceActivityLevel
- _OBJC_IVAR_$_AAOVADSensorInfo._threshold
- _OBJC_IVAR_$_AASensorService._aaDeviceManager
- _OBJC_IVAR_$_AASensorService._availableSensorsLastNotified
- _OBJC_IVAR_$_AASensorService._availableSensorsLostDelayedNotificationTimer
- _OBJC_IVAR_$_AASensorService._btAddressToPIDDict
- _OBJC_IVAR_$_AASensorService._discoveryTimer
- _OBJC_IVAR_$_AASensorService._hidManager
- _OBJC_IVAR_$_AASensorService._ovadAAHIDDeviceDict
- _OBJC_IVAR_$_AASensorService._subscriptionTimer
- ___23-[AASensorService init]_block_invoke
- ___23-[AASensorService init]_block_invoke.cold.1
- ___23-[AASensorService init]_block_invoke_2
- ___23-[AASensorService init]_block_invoke_2.cold.1
- ___23-[AASensorService init]_block_invoke_3
- ___23-[AASensorService init]_block_invoke_4
- ___27-[AASensorService activate]_block_invoke.cold.1
- ___27-[AASensorService activate]_block_invoke.cold.2
- ___27-[AASensorService activate]_block_invoke.cold.3
- ___27-[AASensorService activate]_block_invoke.cold.4
- ___27-[AASensorService activate]_block_invoke.cold.5
- ___27-[AASensorService activate]_block_invoke_2
- ___27-[AASensorService activate]_block_invoke_2.cold.1
- ___27-[AASensorService activate]_block_invoke_2.cold.2
- ___27-[AASensorService activate]_block_invoke_3
- ___27-[AASensorService activate]_block_invoke_4
- ___27-[AASensorService activate]_block_invoke_4.cold.1
- ___29-[AASensorService invalidate]_block_invoke.cold.2
- ___29-[AASensorService invalidate]_block_invoke.cold.3
- ___29-[AASensorService invalidate]_block_invoke.cold.4
- ___40-[AASensorService handleHIDReport:data:]_block_invoke
- ___45-[AASensorService deviceManagerFoundHandler:]_block_invoke
- ___50-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke.cold.1
- ___50-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke.cold.2
- ___50-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke.cold.3
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.1
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.2
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.3
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.4
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.5
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.6
- ___51-[AASensorService deviceNotificationHandler:added:]_block_invoke.cold.7
- ___64-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke.cold.1
- ___64-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke_2
- ___64-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke_2.cold.1
- ___67-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]_block_invoke
- ___67-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]_block_invoke.cold.1
- ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke
- ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke.cold.1
- ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke.cold.2
- ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke.cold.3
- ___68-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e22_v20?0"HIDDevice"8B16ls32l8
- ___block_descriptor_40_e8_32s_e39_v48?0"HIDDevice"8Q16q24q32"NSData"40ls32l8
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_53_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_literal_global.110
- ___block_literal_global.123
- ___block_literal_global.126
- ___block_literal_global.16
- _isValidBtAddress
- _objc_msgSend$_calculateOwnVoiceActivityLevel
- _objc_msgSend$_getBTAddressFromHIDDeviceObject:
- _objc_msgSend$_notifyAvailabilityChangedWithForcedUpdate:
- _objc_msgSend$_ovadSubscriptionHelperWithCompletion:completion:
- _objc_msgSend$_sensorDataAvailabilitiesAdded:
- _objc_msgSend$_sensorDataAvailabilitiesLost:
- _objc_msgSend$_sensorDataAvailabilitiesLostDelayedNotification
- _objc_msgSend$activate
- _objc_msgSend$cancel
- _objc_msgSend$caseInsensitiveCompare:
- _objc_msgSend$close
- _objc_msgSend$deviceManagerFoundHandler:
- _objc_msgSend$deviceNotificationHandler:added:
- _objc_msgSend$getBytes:length:
- _objc_msgSend$handleHIDReport:data:
- _objc_msgSend$hidDevice
- _objc_msgSend$initWithHIDDevice:
- _objc_msgSend$initWithHIDDeviceAndSensorInfo:sensorInfo:
- _objc_msgSend$initWithOptions:
- _objc_msgSend$intValue
- _objc_msgSend$integerValue
- _objc_msgSend$isSetupComplete
- _objc_msgSend$isSubscribed
- _objc_msgSend$open
- _objc_msgSend$propertyForKey:
- _objc_msgSend$sensorInfo
- _objc_msgSend$setDeviceMatching:
- _objc_msgSend$setDeviceNotificationHandler:
- _objc_msgSend$setInputReportHandler:
- _objc_msgSend$setIsSetupComplete:
- _objc_msgSend$setIsSubscribed:
- _objc_msgSend$setPid:
- _objc_msgSend$setReport:reportLength:withIdentifier:forType:error:
- _objc_msgSend$setSensorInfo:
- _objc_msgSend$unsubscribeAll
- _objc_msgSend$update:
- _objc_retain_x9
CStrings:
+ "-[AASensorService _activate:]"
+ "-[AASensorService _activate:]_block_invoke"
+ "-[AASensorService _activateXPC:reactivate:]"
+ "-[AASensorService _activateXPC:reactivate:]_block_invoke"
+ "-[AASensorService _interrupted]"
+ "-[AASensorService _invalidated]"
+ "-[AASensorService _reportError:]"
+ "-[AASensorService activateWithCompletion:]_block_invoke"
+ "-[AASensorService sensorServiceReportSensorInfo:]"
+ "@\"AAController\""
+ "AASensorService, CID 0x%X"
+ "NSCopying"
+ "No sensor data info updated handler for client ID 0x%X"
+ "_aaController"
+ "_broadcastAACPAvailabilities"
+ "_ovadDataDict"
+ "_subscribedSensors"
+ "initWithBTAddress:"
+ "ovLv"
+ "sbsn"
+ "sensorServiceActivate:completion:"
+ "sensorServiceReportSensorInfo:"
+ "v24@0:8@\"AASensorInfo\"16"
+ "v32@0:8@\"AASensorService\"16@?<v@?@\"NSError\">24"
- "-[AAOVADSensorInfo update:]"
- "-[AASensorService _notifyAvailabilityChangedWithForcedUpdate:]"
- "-[AASensorService _ovadSubscriptionHelperWithCompletion:completion:]_block_invoke"
- "-[AASensorService _sensorDataAvailabilitiesAdded:]"
- "-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]"
- "-[AASensorService _sensorDataAvailabilitiesLostDelayedNotification]_block_invoke"
- "-[AASensorService activate]_block_invoke"
- "-[AASensorService activate]_block_invoke_2"
- "-[AASensorService activate]_block_invoke_4"
- "-[AASensorService deviceManagerFoundHandler:]_block_invoke"
- "-[AASensorService deviceNotificationHandler:added:]_block_invoke"
- "-[AASensorService handleHIDReport:data:]_block_invoke"
- "-[AASensorService init]_block_invoke"
- "-[AASensorService init]_block_invoke_2"
- "-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke"
- "-[AASensorService subscribeWithSensorDataFlags:rate:completion:]_block_invoke_2"
- "-[AASensorService unsubscribeWithSensorDataFlags:]_block_invoke"
- "0"
- "@\"HIDManager\""
- "AADeviceManager activation failed with error %@"
- "AADeviceManager interrupted"
- "AADeviceManager invalidated"
- "AADeviceManager succesfully activated"
- "Absent"
- "Activate already called. Cannot activate again."
- "Available devices count: %d"
- "Available sensors data lost delayed notification"
- "BT_ADDR"
- "Cached device %@ PID = %@"
- "Cleared delayed notification for lost sensor data availability"
- "Closed and cancelled all OVAD HID devices"
- "Data packet is not the correct length for parsing"
- "DeviceUsage"
- "DeviceUsagePage"
- "First OVAD capable device found"
- "Found device: %@"
- "HIDManager activated for sensor discovery"
- "HIDManager initialization failed"
- "Invalid OVAD data packet received"
- "Last OVAD capable device lost"
- "Lost device matches stored device -- removing"
- "Lost device: %@"
- "No matching AAHIDDevice found for BT address %@"
- "Notify about sensor data availability change, flags: %d, force %s"
- "Parsed OVAD Data: threshold=%d ovad=%d"
- "Present"
- "PrimaryUsage"
- "PrimaryUsagePage"
- "Received HID report with unknown ID=%d"
- "Received/updated BT address is invalid"
- "Registered change in OVAD status: %s -> %s"
- "Sensor discovery timeout"
- "SensorService invalidation complete"
- "Set device matching and notification handlers"
- "Started %.1f s timeout for sensor availability"
- "Started %.1f s timeout for subscription"
- "Subscription timeout"
- "Succesfully setReport for HID device"
- "Successfully sent stop packet"
- "Transport"
- "Triggered %.1fs delayed notification for lost sensor data availability"
- "Unable to determine HIDReport sender address"
- "Unable to send stop packet to headphones"
- "Unsubscribed from all OVAD HID devices"
- "Updated device address %@ does not match requested address %@"
- "_aaDeviceManager"
- "_availableSensorsLastNotified"
- "_availableSensorsLostDelayedNotificationTimer"
- "_btAddressToPIDDict"
- "_calculateOwnVoiceActivityLevel"
- "_discoveryTimer"
- "_getBTAddressFromHIDDeviceObject:"
- "_hidManager"
- "_notifyAvailabilityChangedWithForcedUpdate:"
- "_ovadAAHIDDeviceDict"
- "_ovadSubscriptionHelperWithCompletion:completion:"
- "_rawOwnVoiceActivityLevel"
- "_sensorDataAvailabilitiesAdded:"
- "_sensorDataAvailabilitiesLost:"
- "_sensorDataAvailabilitiesLostDelayedNotification"
- "_subscriptionTimer"
- "_threshold"
- "cancel"
- "caseInsensitiveCompare:"
- "close"
- "deviceManagerFoundHandler:"
- "deviceNotificationHandler:added:"
- "getBytes:length:"
- "handleHIDReport:data:"
- "initWithHIDDevice:"
- "initWithOptions:"
- "intValue"
- "integerValue"
- "open"
- "propertyForKey:"
- "setDeviceMatching:"
- "setDeviceNotificationHandler:"
- "setInputReportHandler:"
- "setReport failed with error: %@"
- "setReport:reportLength:withIdentifier:forType:error:"
- "v20@?0@\"HIDDevice\"8B16"
- "v29@0:8{?=CI}16@?21"
- "v48@?0@\"HIDDevice\"8Q16q24q32@\"NSData\"40"

```
