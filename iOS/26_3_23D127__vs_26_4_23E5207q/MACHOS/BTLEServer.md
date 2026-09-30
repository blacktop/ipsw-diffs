## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-351.2.0.0.0
-  __TEXT.__text: 0x7b468
-  __TEXT.__auth_stubs: 0x10b0
-  __TEXT.__objc_stubs: 0xc880
-  __TEXT.__objc_methlist: 0x74dc
+354.10.0.0.0
+  __TEXT.__text: 0x82a38
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_stubs: 0xca40
+  __TEXT.__objc_methlist: 0x767c
   __TEXT.__const: 0x598
-  __TEXT.__cstring: 0x3462
-  __TEXT.__objc_methname: 0x126f4
-  __TEXT.__oslogstring: 0xc467
-  __TEXT.__objc_classname: 0x8bc
-  __TEXT.__objc_methtype: 0x306d
-  __TEXT.__gcc_except_tab: 0xf10
+  __TEXT.__cstring: 0x3488
+  __TEXT.__objc_methname: 0x12a6c
+  __TEXT.__oslogstring: 0xcba8
+  __TEXT.__objc_classname: 0x8f0
+  __TEXT.__objc_methtype: 0x30d8
+  __TEXT.__gcc_except_tab: 0xe0c
   __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x18f0
-  __DATA_CONST.__auth_got: 0x868
+  __TEXT.__unwind_info: 0x1f98
+  __DATA_CONST.__auth_got: 0x840
   __DATA_CONST.__got: 0x940
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x1660
-  __DATA_CONST.__cfstring: 0x4b00
+  __DATA_CONST.__const: 0x1680
+  __DATA_CONST.__cfstring: 0x4b20
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_intobj: 0x600
   __DATA_CONST.__objc_arraydata: 0x1c0
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xee88
-  __DATA.__objc_selrefs: 0x4028
-  __DATA.__objc_ivar: 0x7d8
+  __DATA.__objc_const: 0xf078
+  __DATA.__objc_selrefs: 0x4100
+  __DATA.__objc_ivar: 0x7f4
   __DATA.__objc_data: 0x19f0
-  __DATA.__data: 0x990
+  __DATA.__data: 0xa50
   __DATA.__bss: 0x1b8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/StudyLog.framework/StudyLog
   - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
+  - /System/Library/PrivateFrameworks/UARPKit.framework/UARPKit
   - /System/Library/PrivateFrameworks/VisualVoicemail.framework/VisualVoicemail
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC9C839D-09D1-33EA-B6D3-2755ED117FF9
-  Functions: 2891
-  Symbols:   566
-  CStrings:  5645
+  UUID: 0B1F0BDD-7226-3A20-908E-CB0405E58240
+  Functions: 2944
+  Symbols:   562
+  CStrings:  5718
 
Symbols:
+ _OBJC_CLASS_$_UARPDevice
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%@/Logs/Bluetooth/UARPLogs/TapToRadar"
+ "@\"UARPDevice\""
+ "B32@0:8@\"NSData\"16@\"CBPeripheral\"24"
+ "CATTManager didReceiveUARPOverAACPData: %@, for peripheral: %@"
+ "CoreUARP - recvDataOverAACP: %@"
+ "LoggingManager (CoreUARP) - Ignoring %@"
+ "LoggingManager (CoreUARP) - file path: %@"
+ "LoggingManager (CoreUARP) - logRetrievalComplete - Failed to enumerate. Error: %@, Path: %@"
+ "LoggingManager (UARPKit) - Ignoring %@"
+ "LoggingManager (UARPKit) - file path: %@"
+ "LoggingManager (UARPKit) - handleLogRetrievalRequest assets URL for device %@, url %@"
+ "LoggingManager (UARPKit) - handleLogRetrievalRequest calling startTTR for %@"
+ "LoggingManager (UARPKit) - handleLogRetrievalRequest failed to start TTR for device %@ with error %@"
+ "LoggingManager (UARPKit) - logRetrievalComplete - Failed to enumerate. Error: %@, Path: %@"
+ "LoggingManager (UARPKit) - logRetrievalComplete UARPKit filepaths: %@"
+ "LoggingManager (UARPKit) - logRetrievalComplete calling stopTTR for %@"
+ "LoggingManager (UARPKit) - logRetrievalComplete failed to stop TTR for device %@ with error %@"
+ "LoggingManager (UARPKit) - registerUARPDevice assets URL for device %@, url %@"
+ "LoggingManager (UARPKit) - registerUARPDevice calling startTTR for %@"
+ "LoggingManager (UARPKit) - registerUARPDevice failed to start TTR for device %@ with error %@"
+ "LoggingManager (UARPKit) - registerUARPDevice: %@"
+ "LoggingManager (UARPKit) - unregisterUARPDevice failed to stop TTR for device %@ with error %@"
+ "LoggingManager (UARPKit) - unregisterUARPDevice: %@"
+ "LoggingManager - handleDisconnection calling stopTTR for %@"
+ "LoggingManager - handleDisconnection failed to stop TTR for device %@ with error %@"
+ "T@\"NSMutableArray\",&,N,V_ttrDirectories"
+ "T@\"NSMutableSet\",&,N,V_registeredUARPDevices"
+ "T@\"UARPDevice\",&,N,V_uarpDevice"
+ "TB,N,V_ttrIsOngoing"
+ "TI,N,V_productID"
+ "TS,N,V_vendorID"
+ "UARPDeviceDelegateProtocol"
+ "UARPKit - UARPService didReceiveUARPOverAACPData. peripheral: %@, data: %@"
+ "UARPOverAACPDelegate"
+ "_parseRecvdAACPData - Unexpected UARP over AACP packet: %@"
+ "_parseRecvdData - Unexpected UARP over AACP packet: %@"
+ "_registeredUARPDevices"
+ "_subscribeToNotifications"
+ "_ttrDirectories"
+ "_ttrIsOngoing"
+ "_uarpDevice"
+ "deviceReceiveUarpMessageFromTransport:"
+ "deviceSendUarpMessageToTransport for device %@"
+ "deviceSendUarpMessageToTransport:uarpMessage:"
+ "deviceTransportAvailable"
+ "deviceTransportNotNeeded for device %@"
+ "deviceTransportNotNeeded:"
+ "deviceTransportSetupRequested for device %@"
+ "deviceTransportSetupRequested:"
+ "deviceTransportTeardown for device %@"
+ "deviceTransportTeardown:"
+ "deviceTransportUnavailable"
+ "deviceUnavailable"
+ "deviceUnresponsive for device %@"
+ "deviceUnresponsive:"
+ "didReceiveUARPOverAACPData:forPeripheral:"
+ "didReceiveUARPOverAACPData:forPeripheralWithIdentifier:"
+ "incOpportunisticConnectionChecked"
+ "incOpportunisticConnectionChecked - UARPService not yet ready for %@"
+ "registerUARPDevice:"
+ "registeredUARPDevices"
+ "setProductID:"
+ "setRegisteredUARPDevices:"
+ "setTtrDirectories:"
+ "setTtrIsOngoing:"
+ "setUarpDevice:"
+ "setVendorID:"
+ "tapToRadarAssetsURL"
+ "tapToRadarStart:error:"
+ "tapToRadarStop:"
+ "ttrDirectories"
+ "ttrIsOngoing"
+ "uarpDevice"
+ "unregisterUARPDevice:"
+ "v24@0:8@\"UARPDevice\"16"
+ "v32@0:8@\"UARPDevice\"16@\"NSData\"24"
- "LoggingManager - Ignoring %@"
- "LoggingManager - file path: %@"
- "_prepareForFirmwareDownload"
- "logRetrievalComplete - Failed to enumerate. Error: %@, Path: %@"

```
