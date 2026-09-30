## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-890.68.4.0.0
-  __TEXT.__text: 0xa5928
-  __TEXT.__auth_stubs: 0x32b0
-  __TEXT.__objc_methlist: 0x1368
-  __TEXT.__cstring: 0x2b3d9
-  __TEXT.__const: 0x328
-  __TEXT.__gcc_except_tab: 0x4cc
+890.73.1.11.1
+  __TEXT.__text: 0xa8258
+  __TEXT.__auth_stubs: 0x3300
+  __TEXT.__objc_methlist: 0x1370
+  __TEXT.__cstring: 0x2bc35
+  __TEXT.__const: 0x330
+  __TEXT.__gcc_except_tab: 0x6ac
   __TEXT.__oslogstring: 0x16e
   __TEXT.__dlopen_cstrs: 0x18b
-  __TEXT.__unwind_info: 0x26e0
+  __TEXT.__unwind_info: 0x27e8
   __TEXT.__objc_classname: 0x1f5
-  __TEXT.__objc_methname: 0x48cf
+  __TEXT.__objc_methname: 0x48dc
   __TEXT.__objc_methtype: 0xf40
-  __TEXT.__objc_stubs: 0x40a0
+  __TEXT.__objc_stubs: 0x4120
   __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x3618
+  __DATA_CONST.__const: 0x3690
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f0
+  __DATA_CONST.__objc_selrefs: 0x1410
   __DATA_CONST.__objc_superrefs: 0x50
-  __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x1968
+  __DATA_CONST.__objc_arraydata: 0x28
+  __AUTH_CONST.__auth_got: 0x1990
   __AUTH_CONST.__const: 0x2b48
-  __AUTH_CONST.__cfstring: 0x5fa0
+  __AUTH_CONST.__cfstring: 0x5f80
   __AUTH_CONST.__objc_const: 0x1c90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 163C32ED-6560-3A5A-9C8D-C46EA6F42763
-  Functions: 4507
-  Symbols:   11712
-  CStrings:  5872
+  UUID: 1F706DE3-0598-3E25-A13D-8C9A7DF5E50A
+  Functions: 4558
+  Symbols:   11850
+  CStrings:  5908
 
Symbols:
+ -[APBonjourCacheHomeKit diskWriteCoalescer]
+ -[APBonjourCacheHomeKit setDiskWriteCoalescer:]
+ -[APBonjourCacheHomeKit setupDiskWriteCoalescer]
+ -[APBonjourCacheHomeKit setupDiskWriteCoalescer].cold.1
+ -[APHomeKitDeviceMonitor deviceIdentifiers]
+ -[APHomeKitDeviceMonitor setDeviceIdentifiers:]
+ GCC_except_table107
+ GCC_except_table23
+ GCC_except_table24
+ GCC_except_table30
+ GCC_except_table33
+ GCC_except_table46
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table66
+ GCC_except_table67
+ GCC_except_table68
+ GCC_except_table82
+ GCC_except_table86
+ _APCarPlayHelperSessionCreate.cold.14
+ _APConnectivityHelperCreateWithWiFiInterfaceClass.cold.16
+ _APConnectivityHelperCreateWithWiFiInterfaceClass.cold.17
+ _APSCFStringToSockAddr
+ _CMTimeAdd
+ _OBJC_IVAR_$_APBonjourCacheHomeKit._diskWriteCoalescer
+ _OBJC_IVAR_$_APHomeKitDeviceMonitor._deviceIdentifiers
+ __APConnectivityHelperEnsureIPv4AddressesListenerStopped
+ __APConnectivityHelperHandleIPv4ChangedEvent
+ __APConnectivityHelperHandleIPv4ChangedEvent.cold.1
+ __APConnectivityHelperHandleIPv4ChangedEvent.cold.2
+ __APConnectivityHelperHandleIPv4ChangedEvent.cold.3
+ __APConnectivityHelperHandleIPv4ChangedEvent.cold.4
+ __APConnectivityHelperStopIPv4AddressListener
+ __APConnectivityHelperStopListeningToEvent.cold.13
+ __APConnectivityHelperTrySettingAWDLDevice.cold.1
+ __APConnectivityHelperTrySettingAWDLDevice.cold.2
+ __APConnectivityHelperTrySettingAWDLDevice.cold.3
+ __APConnectivityHelperUpdateInterfaceAddedListener.cold.1
+ __APConnectivityHelperUpdateInterfaceAddedListener.cold.2
+ ___48-[APBonjourCacheHomeKit setupDiskWriteCoalescer]_block_invoke
+ ___48-[APBonjourCacheHomeKit setupDiskWriteCoalescer]_block_invoke.cold.1
+ ___APConnectivityHelperCreateWithWiFiInterfaceClass_block_invoke_2
+ ___APConnectivityHelperRegisterActivity_block_invoke.cold.1
+ ___APConnectivityHelperRegisterActivity_block_invoke.cold.2
+ ___APConnectivityHelperRegisterActivity_block_invoke.cold.3
+ ___APConnectivityHelperRegisterActivity_block_invoke.cold.4
+ ___APConnectivityHelperRegisterActivity_block_invoke.cold.5
+ ____APConnectivityHelperHandleInterfaceAddedRetryTimerFired_block_invoke
+ ____APConnectivityHelperPopulateCurrentWiFiNetworkInfo_block_invoke
+ ____APConnectivityHelperPopulateCurrentWiFiNetworkInfo_block_invoke_2
+ ____APConnectivityHelperQueryWiFiPower_block_invoke
+ ____APConnectivityHelperStartInterfaceAddedListenerIfNecessary_block_invoke
+ ____APConnectivityHelperStartLinkDebounceFailedListener_block_invoke
+ ____APConnectivityHelperStartWakeOnWireless_block_invoke
+ ____APConnectivityHelperStartWiFiNetworkListener_block_invoke
+ ____APConnectivityHelperStartWiFiPowerListener_block_invoke
+ ____APConnectivityHelperStopInterfaceAddedListenerIfNecessary_block_invoke
+ ____APConnectivityHelperStopLinkDebounceFailedListener_block_invoke
+ ____APConnectivityHelperStopWakeOnWireless_block_invoke
+ ____APConnectivityHelperStopWiFiNetworkListener_block_invoke
+ ____APConnectivityHelperStopWiFiPowerListener_block_invoke
+ ____APConnectivityHelperTrySettingAWDLDevice_block_invoke
+ ____APConnectivityHelperTrySettingWiFiDevice_block_invoke
+ ____APConnectivityHelperUpdateTrafficRegistration_block_invoke
+ ___block_descriptor_56_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_64_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_literal_global.132
+ ___block_literal_global.176
+ ___block_literal_global.361
+ ___block_literal_global.38
+ ___block_literal_global.47
+ ___block_literal_global.61
+ ___block_literal_global.85
+ ___carPlayHelperSession_IPv4InterfaceAddressesChanged_block_invoke
+ ___carPlayHelperSession_IPv4InterfaceAddressesChanged_block_invoke.cold.1
+ ___carPlayHelperSession_IPv4InterfaceAddressesChanged_block_invoke.cold.2
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.1
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.10
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.11
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.12
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.13
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.14
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.15
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.16
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.17
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.18
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.19
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.2
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.20
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.21
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.3
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.4
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.5
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.6
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.7
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.8
+ ___carPlayHelperSession_handleConnectivityHelperEvent_block_invoke.cold.9
+ ___lowPowerKeepAliveController_Suspend_block_invoke.cold.1
+ ___standardKeepAliveController_Finalize_block_invoke
+ _carPlayHelperSession_updateIPAddresses
+ _carPlayHelperSession_updateIPAddresses.cold.1
+ _carPlayHelperSession_updateIPAddresses.cold.2
+ _carPlayHelperSession_updateIPAddresses.cold.3
+ _dispatch_async_and_wait
+ _dispatch_queue_get_qos_class
+ _httpconnection_asyncConnectionCompleted
+ _kAPConnectivityHelperEventInfoKey_IPv4Addresses
+ _lowPowerKeepAliveController_Resume.cold.1
+ _lowPowerKeepAliveController_Suspend.cold.1
+ _objc_msgSend$cancel
+ _objc_msgSend$deviceIdentifiers
+ _objc_msgSend$diskWriteCoalescer
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$setDeviceIdentifiers:
+ _objc_msgSend$setDiskWriteCoalescer:
+ _objc_msgSend$setLeeway:
+ _objc_msgSend$setWithSet:
+ _objc_msgSend$setupDiskWriteCoalescer
+ _qos_class_self
+ _standardKeepAliveController_Resume.cold.1
+ _standardKeepAliveController_Suspend.cold.1
+ _standardKeepAliveController_controllerSuspendedCallback.cold.1
+ _standardKeepAliveController_timerFiredCheck
- -[APBonjourCacheHomeKit setUseStrictNetworkSignatureMatching:]
- -[APBonjourCacheHomeKit useStrictNetworkSignatureMatching]
- -[APHomeKitDeviceMonitor homeAccessories]
- -[APHomeKitDeviceMonitor setHomeAccessories:]
- GCC_except_table105
- GCC_except_table22
- GCC_except_table25
- GCC_except_table31
- GCC_except_table34
- _APConnectivityHelperSetWiFiPower
- _OBJC_IVAR_$_APBonjourCacheHomeKit._useStrictNetworkSignatureMatching
- _OBJC_IVAR_$_APHomeKitDeviceMonitor._homeAccessories
- __APConnectivityHelperPopulateCurrentWiFiNetworkInfo.cold.1
- __APConnectivityHelperPopulateCurrentWiFiNetworkInfo.cold.2
- __APConnectivityHelperQueryWiFiPower.cold.1
- __APConnectivityHelperQueryWiFiPower.cold.2
- __APConnectivityHelperSetWiFiPower
- __APConnectivityHelperSetWiFiPower.cold.1
- __APConnectivityHelperSetWiFiPower.cold.2
- __APConnectivityHelperSetWiFiPower.cold.3
- __APConnectivityHelperUpdateTrafficRegistration.cold.1
- __APConnectivityHelperUpdateTrafficRegistration.cold.2
- __APConnectivityHelperUpdateTrafficRegistration.cold.3
- __APConnectivityHelperUpdateTrafficRegistration.cold.4
- __APConnectivityHelperUpdateTrafficRegistration.cold.5
- __APConnectivityHelperUpdateTrafficRegistration.cold.6
- __APTNANDataSessionGenerateDiversifiedPIN.cold.1
- ____APConnectivityHelperStartInterfaceAddedRetryTimer_block_invoke.cold.1
- ___block_literal_global.128
- ___block_literal_global.173
- ___block_literal_global.33
- ___block_literal_global.371
- ___block_literal_global.45
- ___block_literal_global.57
- ___block_literal_global.79
- _carPlayHelperSession_updateNetworkAndSessionState.cold.11
- _carPlayHelperSession_updateNetworkAndSessionState.cold.12
- _httpconnection_asyncConnectionConnected
- _objc_msgSend$hash
- _objc_msgSend$homeAccessories
- _objc_msgSend$setHomeAccessories:
- _objc_msgSend$setPower:error:
- _objc_msgSend$useStrictNetworkSignatureMatching
- _standardKeepAliveController_SetProperty.cold.3
- _standardKeepAliveController_sendKeepAliveCallback.cold.5
CStrings:
+ "-[APBonjourCacheHomeKit setupDiskWriteCoalescer]"
+ "-[APBonjourCacheHomeKit setupDiskWriteCoalescer]_block_invoke"
+ "890.73.1.11.1"
+ "APConnectivityHelperHighPriorityQueue"
+ "IPv4 Addresses Changed"
+ "IPv4 Addresses Changed Listening Stopped"
+ "IPv4Addresses"
+ "OSStatus _APConnectivityHelperStartIPv4AddressListener(APConnectivityHelperRef)"
+ "OSStatus _APConnectivityHelperStopIPv4AddressListener(APConnectivityHelperRef)"
+ "OSStatus carPlayHelperSession_IPv4InterfaceAddressesChanged(APCarPlayHelperRef, CFDictionaryRef)_block_invoke"
+ "OSStatus carPlayHelperSession_updateIPAddresses(APCarPlayHelperRef, CFStringRef, CFArrayRef, const int8_t)"
+ "OSStatus lowPowerKeepAliveController_Resume(APTransportKeepAliveControllerRef)"
+ "OSStatus lowPowerKeepAliveController_Suspend(APTransportKeepAliveControllerRef)"
+ "OSStatus lowPowerKeepAliveController_Suspend(APTransportKeepAliveControllerRef)_block_invoke"
+ "OSStatus lowPowerKeepAliveController_resumeInternal(APTransportKeepAliveControllerRef)"
+ "OSStatus standardKeepAliveController_Resume(APTransportKeepAliveControllerRef)"
+ "OSStatus standardKeepAliveController_Suspend(APTransportKeepAliveControllerRef)"
+ "T@\"CUCoalescer\",N,V_diskWriteCoalescer"
+ "T@\"NSMutableSet\",&,N,V_deviceIdentifiers"
+ "[%{ptr}] %s Ignoring IPv4 LinkLocal/Loopback address: %@\n"
+ "[%{ptr}] %s Ignoring update change(%lf seconds): interface %@ IPv%d addresses changed to %@\n"
+ "[%{ptr}] %s StartSessionHost: requestID=%@, isIPv4=%s, host=%@\n"
+ "[%{ptr}] %s interface %@ IPv%d addresses changed to %@\n"
+ "[%{ptr}] IPv4 Address changed (for interface %@): %@ = %@\n"
+ "[%{ptr}] IPv4 address listener stopped.\n"
+ "[%{ptr}] IPv4 address watching started.\n"
+ "[%{ptr}] Keep alive interval set to %d ms"
+ "[%{ptr}] Keep-alive response received with reply: %@\n"
+ "[%{ptr}] Keep-alive resuming\n"
+ "[%{ptr}] Keep-alive suspending\n"
+ "[%{ptr}] Received response for CID:0x%08X groupID %llu%?{end} duration %llums%?{end} receiver %llums"
+ "[%{ptr}] Sending Keep-alive\n"
+ "[%{ptr}] Sending legacy Keep-alive\n"
+ "[%{ptr}] Started keep alive with interval %d ms"
+ "[%{ptr}] Started keep alive with interval %d s"
+ "[%{ptr}] Stopped keep alive"
+ "[%{ptr}] Timer was delayed by %.3f seconds\n"
+ "[%{ptr}] Write delay timer fired"
+ "[%{ptr}] Writing cache to disk"
+ "_APConnectivityHelperEnsureIPv4AddressesListenerStarted"
+ "_APConnectivityHelperEnsureIPv4AddressesListenerStopped"
+ "_APConnectivityHelperHandleIPv4ChangedEvent"
+ "_APConnectivityHelperStartIPv4AddressListener"
+ "_APConnectivityHelperStopIPv4AddressListener"
+ "_deviceIdentifiers"
+ "_diskWriteCoalescer"
+ "bonjourCacheHomeKitCoalesceMaxSeconds"
+ "bonjourCacheHomeKitCoalesceMinSeconds"
+ "cancel"
+ "carPlayHelperSession_IPv4InterfaceAddressesChanged"
+ "carPlayHelperSession_IPv4InterfaceAddressesChanged_block_invoke"
+ "carPlayHelperSession_IPv6InterfaceAddressesChanged"
+ "carPlayHelperSession_containsOnlyIPv4Addresses"
+ "carPlayHelperSession_updateIPAddresses"
+ "deviceIdentifiers"
+ "diskWriteCoalescer"
+ "httpconnection_asyncConnectionCompleted"
+ "isEqualToSet:"
+ "setDeviceIdentifiers:"
+ "setDiskWriteCoalescer:"
+ "setLeeway:"
+ "setWithSet:"
+ "setupDiskWriteCoalescer"
+ "void _APConnectivityHelperHandleIPv4ChangedEvent(SCDynamicStoreRef, CFStringRef, CFStringRef, void *)"
+ "void httpconnection_asyncConnectionCompleted(SocketRef, OSStatus, void *)"
+ "void standardKeepAliveController_controllerSuspendedCallback(void *)"
+ "void standardKeepAliveController_timerFiredCheck(APTransportKeepAliveControllerRef, CMTime, Boolean)"
- "890.68.4"
- ";IPv4.RouterHardwareAddress="
- ";IPv6.RouterHardwareAddress="
- "IPv4.Router="
- "IPv6.Prefix="
- "Keep alive interval set to %d ms"
- "Keep-alive response received with reply: %@\n"
- "OSStatus carPlayHelperSession_interfaceAddressesChanged(APCarPlayHelperRef, CFDictionaryRef)"
- "Sending Keep-alive\n"
- "Sending legacy Keep-alive\n"
- "Starting keep alive with interval %lld ns (%d ms)"
- "T@\"NSMutableSet\",&,N,V_homeAccessories"
- "TB,N,V_useStrictNetworkSignatureMatching"
- "[%{ptr}] %s Ignoring update change(%lf seconds): interface %@ IPv6 addresses changed to %@\n"
- "[%{ptr}] %s StartSessionHost: requestID=%@, host=%@\n"
- "[%{ptr}] %s interface %@ IPv6 addresses changed to %@\n"
- "[%{ptr}] Received response for httpMessage [%{ptr}] groupID %d"
- "[%{ptr}] Setting WiFi power to: %s.\n"
- "_APConnectivityHelperSetWiFiPower"
- "_homeAccessories"
- "_useStrictNetworkSignatureMatching"
- "carPlayHelperSession_interfaceAddressesChanged"
- "homeAccessories"
- "httpconnection_asyncConnectionConnected"
- "setHomeAccessories:"
- "setPower:error:"
- "setUseStrictNetworkSignatureMatching:"
- "useStrictNetworkSignatureMatching"
- "void _APConnectivityHelperSetWiFiPower(void *)"
- "void httpconnection_asyncConnectionConnected(SocketRef, OSStatus, void *)"

```
