## CarAccessoryFramework

> `/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`

```diff

-515.29.0.0.0
-  __TEXT.__text: 0x120d34
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x185fc
-  __TEXT.__const: 0x198
-  __TEXT.__cstring: 0x7c27
-  __TEXT.__oslogstring: 0x3a1f
-  __TEXT.__gcc_except_tab: 0x604
+515.34.1.0.0
+  __TEXT.__text: 0x122ae4
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x18884
+  __TEXT.__const: 0x1a8
+  __TEXT.__gcc_except_tab: 0x640
+  __TEXT.__oslogstring: 0x3bad
+  __TEXT.__cstring: 0x7ce9
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x3da8
-  __TEXT.__objc_classname: 0x3dc0
-  __TEXT.__objc_methname: 0x1f9c0
-  __TEXT.__objc_methtype: 0x4cc4
-  __TEXT.__objc_stubs: 0x14900
-  __DATA_CONST.__got: 0xec0
-  __DATA_CONST.__const: 0x2650
-  __DATA_CONST.__objc_classlist: 0xd90
+  __TEXT.__unwind_info: 0x3e78
+  __TEXT.__objc_classname: 0x3dee
+  __TEXT.__objc_methname: 0x1ff10
+  __TEXT.__objc_methtype: 0x4d88
+  __TEXT.__objc_stubs: 0x14d20
+  __DATA_CONST.__got: 0xee0
+  __DATA_CONST.__const: 0x26a8
+  __DATA_CONST.__objc_classlist: 0xda0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a50
+  __DATA_CONST.__objc_selrefs: 0x7ba0
   __DATA_CONST.__objc_protorefs: 0x5a8
-  __DATA_CONST.__objc_superrefs: 0x7d0
-  __DATA_CONST.__objc_arraydata: 0xb898
-  __AUTH_CONST.__auth_got: 0x338
+  __DATA_CONST.__objc_superrefs: 0x7d8
+  __DATA_CONST.__objc_arraydata: 0xb8f8
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0xdaa0
-  __AUTH_CONST.__objc_const: 0x4e800
-  __AUTH_CONST.__objc_dictobj: 0x6360
-  __AUTH_CONST.__objc_intobj: 0x678
+  __AUTH_CONST.__cfstring: 0xdba0
+  __AUTH_CONST.__objc_const: 0x4ec60
   __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x678
   __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__objc_dictobj: 0x6360
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x2c10
-  __DATA.__objc_ivar: 0x668
+  __AUTH.__objc_data: 0x2cb0
+  __DATA.__objc_ivar: 0x680
   __DATA.__data: 0x4880
   __DATA.__bss: 0x3c0
   __DATA_DIRTY.__objc_data: 0x5b90

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85E46B24-771C-36E1-8550-58698F5089E5
-  Functions: 7572
-  Symbols:   25187
-  CStrings:  9913
+  UUID: B52745F0-286B-32E5-B49B-3101526BC924
+  Functions: 7630
+  Symbols:   25385
+  CStrings:  10000
 
Symbols:
+ +[CAFCarAttributes supportsSecureCoding]
+ +[CAFStartupNotificationGate fallbackInterval]
+ +[CAFStartupNotificationGate readyInterval]
+ -[CAFBooleanSetting onRestricted]
+ -[CAFButtonSetting hasHeartbeatFrequency]
+ -[CAFButtonSetting hasSupportsPressAndHold]
+ -[CAFButtonSetting heartbeatFrequencyCharacteristic]
+ -[CAFButtonSetting heartbeatFrequencyRange]
+ -[CAFButtonSetting heartbeatFrequency]
+ -[CAFButtonSetting registeredForSupportsPressAndHold]
+ -[CAFButtonSetting registeredForheartbeatFrequency]
+ -[CAFButtonSetting supportsPressAndHoldCharacteristic]
+ -[CAFButtonSetting supportsPressAndHold]
+ -[CAFCar attributes]
+ -[CAFCar setStartupNotificationGate:]
+ -[CAFCar shouldSuppressStartupNotifications]
+ -[CAFCar startupNotificationGate]
+ -[CAFCar updateAttributes:]
+ -[CAFCarAttributes copyWithZone:]
+ -[CAFCarAttributes description]
+ -[CAFCarAttributes echoSuppressionInterval]
+ -[CAFCarAttributes encodeWithCoder:]
+ -[CAFCarAttributes hash]
+ -[CAFCarAttributes initWithCoder:]
+ -[CAFCarAttributes init]
+ -[CAFCarAttributes isEqual:]
+ -[CAFCarAttributes setEchoSuppressionInterval:]
+ -[CAFCarAttributes updateWithCapabilities:]
+ -[CAFCarConfiguration attributes]
+ -[CAFCarConfiguration setAttributes:]
+ -[CAFCarConfiguration updateAttributes:]
+ -[CAFCarConfiguration updateCapabilitiesIfNeeded]
+ -[CAFCharacteristic _cancelEchoSuppressionTimer]
+ -[CAFCharacteristic _cancelEchoSuppressionTimer].cold.1
+ -[CAFCharacteristic _echoSuppressionTimerFired]
+ -[CAFCharacteristic _echoSuppressionTimerFired].cold.1
+ -[CAFCharacteristic _resetEchoSuppressionTimer]
+ -[CAFCharacteristic _resetEchoSuppressionTimer].cold.1
+ -[CAFCharacteristic echoSuppressionTimer]
+ -[CAFCharacteristic setEchoSuppressionTimer:]
+ -[CAFStartupNotificationGate .cxx_destruct]
+ -[CAFStartupNotificationGate carFirstObservedAt]
+ -[CAFStartupNotificationGate carReadyAt]
+ -[CAFStartupNotificationGate clearCar]
+ -[CAFStartupNotificationGate clearCar].cold.1
+ -[CAFStartupNotificationGate markCarObserved]
+ -[CAFStartupNotificationGate markCarObserved].cold.1
+ -[CAFStartupNotificationGate markCarReady]
+ -[CAFStartupNotificationGate markCarReady].cold.1
+ -[CAFStartupNotificationGate setCarFirstObservedAt:]
+ -[CAFStartupNotificationGate setCarReadyAt:]
+ -[CAFStartupNotificationGate shouldSuppress]
+ -[_CAFCarDataClientProxy didUpdateAttributes:]
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table16
+ GCC_except_table35
+ GCC_except_table80
+ _CAFCharacteristicTypeSupportsPressAndHold
+ _CAFCharacteristicTypeheartbeatFrequency
+ _CAFDefaultsGetDouble
+ _NSStringFromClass
+ _OBJC_CLASS_$_CAFCarAttributes
+ _OBJC_CLASS_$_CAFStartupNotificationGate
+ _OBJC_CLASS_$_CRCarPlayCapabilities
+ _OBJC_IVAR_$_CAFCar._startupNotificationGate
+ _OBJC_IVAR_$_CAFCarAttributes._echoSuppressionInterval
+ _OBJC_IVAR_$_CAFCarConfiguration._attributes
+ _OBJC_IVAR_$_CAFCharacteristic._echoSuppressionTimer
+ _OBJC_IVAR_$_CAFStartupNotificationGate._carFirstObservedAt
+ _OBJC_IVAR_$_CAFStartupNotificationGate._carReadyAt
+ _OBJC_METACLASS_$_CAFCarAttributes
+ _OBJC_METACLASS_$_CAFStartupNotificationGate
+ __OBJC_$_CLASS_METHODS_CAFCarAttributes
+ __OBJC_$_CLASS_METHODS_CAFStartupNotificationGate
+ __OBJC_$_CLASS_PROP_LIST_CAFCarAttributes
+ __OBJC_$_CLASS_PROP_LIST_CAFStartupNotificationGate
+ __OBJC_$_INSTANCE_METHODS_CAFCarAttributes
+ __OBJC_$_INSTANCE_METHODS_CAFStartupNotificationGate
+ __OBJC_$_INSTANCE_VARIABLES_CAFCarAttributes
+ __OBJC_$_INSTANCE_VARIABLES_CAFStartupNotificationGate
+ __OBJC_$_PROP_LIST_CAFCarAttributes
+ __OBJC_$_PROP_LIST_CAFStartupNotificationGate
+ __OBJC_CLASS_PROTOCOLS_$_CAFCarAttributes
+ __OBJC_CLASS_RO_$_CAFCarAttributes
+ __OBJC_CLASS_RO_$_CAFStartupNotificationGate
+ __OBJC_METACLASS_RO_$_CAFCarAttributes
+ __OBJC_METACLASS_RO_$_CAFStartupNotificationGate
+ ___29-[CAFCar _refreshAccessories]_block_invoke.102
+ ___29-[CAFCar _refreshAccessories]_block_invoke.96
+ ___29-[CAFCar _refreshAccessories]_block_invoke.96.cold.1
+ ___29-[CAFCar _refreshAccessories]_block_invoke.96.cold.2
+ ___29-[CAFCar _refreshAccessories]_block_invoke.96.cold.3
+ ___29-[CAFCar _refreshAccessories]_block_invoke.98
+ ___29-[CAFCar _refreshAccessories]_block_invoke.98.cold.1
+ ___29-[CAFCar _refreshAccessories]_block_invoke.98.cold.2
+ ___29-[CAFCar _refreshAccessories]_block_invoke.98.cold.3
+ ___29-[CAFCar _refreshAccessories]_block_invoke.98.cold.4
+ ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.120
+ ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.120.cold.1
+ ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.123
+ ___40-[CAFCar _groupInitialization:controls:]_block_invoke.113
+ ___40-[CAFCar _groupInitialization:controls:]_block_invoke.113.cold.1
+ ___46-[_CAFCarDataClientProxy didUpdateAttributes:]_block_invoke
+ ___46-[_CAFCarDataClientProxy didUpdateAttributes:]_block_invoke.cold.1
+ ___47-[CAFCharacteristic _resetEchoSuppressionTimer]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_literal_global.115
+ ___block_literal_global.126
+ ___block_literal_global.1701
+ ___block_literal_global.1703
+ ___block_literal_global.1707
+ ___block_literal_global.1804
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _kCAFEchoSuppressionInterval
+ _objc_msgSend$_cancelEchoSuppressionTimer
+ _objc_msgSend$_echoSuppressionTimerFired
+ _objc_msgSend$_resetEchoSuppressionTimer
+ _objc_msgSend$attributes
+ _objc_msgSend$buttonSettingService:didUpdateHeartbeatFrequency:
+ _objc_msgSend$buttonSettingService:didUpdateSupportsPressAndHold:
+ _objc_msgSend$capabilitiesIdentifier
+ _objc_msgSend$carFirstObservedAt
+ _objc_msgSend$carReadyAt
+ _objc_msgSend$clearCar
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$echoSuppressionInterval
+ _objc_msgSend$echoSuppressionTimer
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$fallbackInterval
+ _objc_msgSend$fetchCarCapabilitiesWithIdentifier:
+ _objc_msgSend$heartbeatFrequency
+ _objc_msgSend$heartbeatFrequencyCharacteristic
+ _objc_msgSend$markCarObserved
+ _objc_msgSend$markCarReady
+ _objc_msgSend$readyInterval
+ _objc_msgSend$setAttributes:
+ _objc_msgSend$setCarFirstObservedAt:
+ _objc_msgSend$setCarReadyAt:
+ _objc_msgSend$setEchoSuppressionInterval:
+ _objc_msgSend$setEchoSuppressionTimer:
+ _objc_msgSend$shouldSuppress
+ _objc_msgSend$startupNotificationGate
+ _objc_msgSend$supportsPressAndHold
+ _objc_msgSend$supportsPressAndHoldCharacteristic
+ _objc_msgSend$updateAttributes:
+ _objc_msgSend$updateWithCapabilities:
+ _objc_msgSend$userInfo
- GCC_except_table135
- GCC_except_table136
- GCC_except_table15
- ___29-[CAFCar _refreshAccessories]_block_invoke.101
- ___29-[CAFCar _refreshAccessories]_block_invoke.95
- ___29-[CAFCar _refreshAccessories]_block_invoke.95.cold.1
- ___29-[CAFCar _refreshAccessories]_block_invoke.95.cold.2
- ___29-[CAFCar _refreshAccessories]_block_invoke.95.cold.3
- ___29-[CAFCar _refreshAccessories]_block_invoke.97
- ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.1
- ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.2
- ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.3
- ___29-[CAFCar _refreshAccessories]_block_invoke.97.cold.4
- ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.119
- ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.119.cold.1
- ___35-[CAFCar didUpdatePluginID:values:]_block_invoke.122
- ___40-[CAFCar _groupInitialization:controls:]_block_invoke.112
- ___40-[CAFCar _groupInitialization:controls:]_block_invoke.112.cold.1
- ___block_literal_global.114
- ___block_literal_global.125
- ___block_literal_global.1689
- ___block_literal_global.1691
- ___block_literal_global.1695
- ___block_literal_global.1792
CStrings:
+ "%{public}@ cancel timer existing=%@"
+ "%{public}@ reset timer to %.3fs existing=%@"
+ "%{public}@ timer fired pending=%@ cached=%@ lockState=%@"
+ "%{public}@ value set %@ stillPending=%@"
+ "0x000000003600006E"
+ "0x000000003600006F"
+ "<%@: %p echoSuppressionInterval=%.3f>"
+ "@\"CAFCarAttributes\""
+ "@\"CAFStartupNotificationGate\""
+ "@\"NSDate\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "CAFCarAttributes"
+ "CAFCarConfigurationCarAttributes"
+ "CAFEchoSuppressionInterval"
+ "CAFStartupNotificationGate"
+ "PressedAndHolding"
+ "SupportsPressAndHold"
+ "T@\"CAFCarAttributes\",&,N,V_attributes"
+ "T@\"CAFStartupNotificationGate\",&,N,V_startupNotificationGate"
+ "T@\"NSDate\",&,N,V_carFirstObservedAt"
+ "T@\"NSDate\",&,N,V_carReadyAt"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_echoSuppressionTimer"
+ "Td,N,V_echoSuppressionInterval"
+ "Update attributes, but current car does not exist."
+ "_attributes"
+ "_cancelEchoSuppressionTimer"
+ "_carFirstObservedAt"
+ "_carReadyAt"
+ "_echoSuppressionInterval"
+ "_echoSuppressionTimer"
+ "_echoSuppressionTimerFired"
+ "_resetEchoSuppressionTimer"
+ "_startupNotificationGate"
+ "attributes"
+ "buttonSettingService:didUpdateHeartbeatFrequency:"
+ "buttonSettingService:didUpdateSupportsPressAndHold:"
+ "capabilitiesIdentifier"
+ "car cleared, startup notification gate state reset"
+ "car observed, starting startup notification gate window (ready=%.1fs, fallback=%.1fs)"
+ "car receivedAllValues YES, startup notification gate will open in %.1fs"
+ "carFirstObservedAt"
+ "carReadyAt"
+ "clearCar"
+ "decodeDoubleForKey:"
+ "didUpdateAttributes:"
+ "echoSuppressionInterval"
+ "echoSuppressionTimer"
+ "encodeDouble:forKey:"
+ "fallbackInterval"
+ "fetchCarCapabilitiesWithIdentifier:"
+ "hasHeartbeatFrequency"
+ "hasSupportsPressAndHold"
+ "heartbeatFrequency"
+ "heartbeatFrequencyCharacteristic"
+ "heartbeatFrequencyRange"
+ "markCarObserved"
+ "markCarReady"
+ "readyInterval"
+ "registeredForSupportsPressAndHold"
+ "registeredForheartbeatFrequency"
+ "setAttributes:"
+ "setCarFirstObservedAt:"
+ "setCarReadyAt:"
+ "setEchoSuppressionInterval:"
+ "setEchoSuppressionTimer:"
+ "setStartupNotificationGate:"
+ "shouldSuppress"
+ "shouldSuppressStartupNotifications"
+ "startupNotificationGate"
+ "supportsPressAndHold"
+ "supportsPressAndHoldCharacteristic"
+ "updateAttributes:"
+ "updateCapabilitiesIfNeeded"
+ "updateWithCapabilities:"
+ "userInfo"
+ "v24@0:8@\"CAFCarAttributes\"16"
+ "v24@0:8d16"
+ "v28@0:8@\"CAFButtonSetting\"16B24"
+ "v28@0:8@\"CAFButtonSetting\"16f24"
+ "\xb1"
- "%{public}@ value set %@ decodeError=%@"
- "\xa1"

```
