## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-716.300.51.0.0
-  __TEXT.__text: 0x9f4c0
+716.300.121.0.0
+  __TEXT.__text: 0x9f4b0
   __TEXT.__auth_stubs: 0x1e00
   __TEXT.__objc_methlist: 0x8fb4
   __TEXT.__const: 0x39d8
-  __TEXT.__cstring: 0x15684
+  __TEXT.__cstring: 0x15694
   __TEXT.__gcc_except_tab: 0x171c
   __TEXT.__oslogstring: 0x6fd
   __TEXT.__swift5_typeref: 0x7cb

   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0xf10
   __AUTH_CONST.__const: 0x1318
-  __AUTH_CONST.__cfstring: 0x51e0
+  __AUTH_CONST.__cfstring: 0x5200
   __AUTH_CONST.__objc_const: 0x10a40
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8BDFF83E-D8B6-3192-8F2F-E3F2ADFBBFEE
-  Functions: 4566
-  Symbols:   12318
-  CStrings:  7137
+  UUID: 6ADC3662-A583-3C1A-B320-E8FC87AE1819
+  Functions: 4567
+  Symbols:   12320
+  CStrings:  7139
 
Functions:
+ _OUTLINED_FUNCTION_0
~ -[RPNWActivityEventMetrics _metricsDictionary] : 180 -> 200
~ -[RPNWActivityRequestMetrics _metricsDictionary] : 312 -> 332
~ -[RPFileTransferSession _controlCnxStartIfNeeded] : 748 -> 744
~ -[RPFileTransferSession _activateTargetAndReturnError:].cold.1 : 72 -> 68
~ -[RPLegacyDeviceDiscovery _bonjourHandleRemoveDevice:].cold.1 : 124 -> 120
~ -[RPNWActivityMetrics _withLock:] : 96 -> 104
~ -[RPStreamSession _startServerConnectionAndReturnError:].cold.1 : 140 -> 132
~ -[RPStreamSession _invalidate].cold.1 : 104 -> 96
~ -[RPStreamSession _invalidated].cold.1 : 104 -> 96
~ ___72-[RPStreamSession _serverUDPNWPathStartRequest:options:responseHandler:]_block_invoke_2.cold.2 : 112 -> 116
~ -[RPStreamSession _clientUDPSocketStartResponse:options:completion:].cold.3 : 108 -> 100
~ -[RPStreamSession _serverUDPSocketStartRequest:options:responseHandler:].cold.5 : 116 -> 108
~ -[RPStreamSession _clientRPConnectionPrepareWithCompletion:].cold.1 : 104 -> 96
~ -[RPStreamSession _clientRPConnectionStartWithCompletion:].cold.1 : 116 -> 108
~ -[RPStreamSession _getSockAddrInterfaceType:].cold.1 : 132 -> 128
~ -[RPStreamSession _getSockAddrInterfaceType:].cold.2 : 128 -> 124
~ -[RPStreamSession _getSockAddrInterfaceType:].cold.3 : 128 -> 124
~ -[RPStreamSession _getSockAddrInterfaceType:].cold.4 : 140 -> 136
CStrings:
+ "rapport:rdid:"

```
