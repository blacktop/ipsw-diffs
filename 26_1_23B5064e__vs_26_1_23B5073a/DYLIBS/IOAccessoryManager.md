## IOAccessoryManager

> `/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`

```diff

 1139.40.6.0.0
-  __TEXT.__text: 0x64600
+  __TEXT.__text: 0x6470c
   __TEXT.__auth_stubs: 0x1590
   __TEXT.__objc_methlist: 0x2e7c
-  __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x5bd9
+  __TEXT.__const: 0x368
+  __TEXT.__cstring: 0x5bf9
   __TEXT.__oslogstring: 0xbb7d
-  __TEXT.__gcc_except_tab: 0x9f8
+  __TEXT.__gcc_except_tab: 0xa04
   __TEXT.__ustring: 0x146
   __TEXT.__unwind_info: 0xd38
   __TEXT.__objc_classname: 0x474
-  __TEXT.__objc_methname: 0x875e
+  __TEXT.__objc_methname: 0x879d
   __TEXT.__objc_methtype: 0xff9
-  __TEXT.__objc_stubs: 0x5d00
+  __TEXT.__objc_stubs: 0x5d20
   __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0xe90
+  __DATA_CONST.__const: 0xea8
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e48
+  __DATA_CONST.__objc_selrefs: 0x1e50
   __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x128
   __AUTH_CONST.__auth_got: 0xad8
   __AUTH_CONST.__const: 0x300
-  __AUTH_CONST.__cfstring: 0x4400
+  __AUTH_CONST.__cfstring: 0x4460
   __AUTH_CONST.__objc_const: 0x4c20
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x48

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: 60F52771-F402-3CF3-B449-8EA3386C172F
-  Functions: 1794
-  Symbols:   6649
-  CStrings:  3905
+  UUID: CE2E2949-5D77-3C22-9922-EED1ADB21B7F
+  Functions: 1795
+  Symbols:   6650
+  CStrings:  3912
 
Symbols:
+ ___52-[ACCTransportIOAccessoryManager initWithIOService:]_block_invoke.48
+ ___52-[ACCTransportIOAccessoryManager initWithIOService:]_block_invoke.48.cold.1
+ ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.76
+ ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.76.cold.1
+ ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.133
+ ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.134
+ ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.139
+ ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.139.cold.1
+ ___78-[ACCTransportIOAccessoryAuthCP initWithDelegate:andIOService:connectionType:]_block_invoke.120
+ ___89-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingDataFinishedForEndpointUUID:]_block_invoke.160
+ ___block_literal_global.110
+ _objc_msgSend$authenticateLASWithChallenge:completionHandler:updateRegistry:
- ___52-[ACCTransportIOAccessoryManager initWithIOService:]_block_invoke.45
- ___52-[ACCTransportIOAccessoryManager initWithIOService:]_block_invoke.45.cold.1
- ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.73
- ___70-[ACCTransportIOAccessoryManager _handleResistorIDChangeNotification:]_block_invoke.73.cold.1
- ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.130
- ___72-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceArrived:]_block_invoke.131
- ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.136
- ___75-[ACCTransportIOAccessorySharedManager IOAccessoryAuthCPServiceTerminated:]_block_invoke.136.cold.1
- ___78-[ACCTransportIOAccessoryAuthCP initWithDelegate:andIOService:connectionType:]_block_invoke.117
- ___89-[ACCTransportIOAccessorySharedManager IOAccessoryOOBPairingDataFinishedForEndpointUUID:]_block_invoke.157
- ___block_literal_global.107
Functions:
+ sub_233636f10
~ -[ACCTransportIOAccessoryAuthCP initWithDelegate:andIOService:connectionType:] : 2936 -> 2996
~ -[ACCTransportIOAccessoryAuthCP _authInternalModuleWithCert:withError:] : 2016 -> 2076
~ -[ACCTransportIOAccessoryAuthCP _fdrCertCheck] : 1636 -> 1656
~ -[ACCTransportIOAccessoryAuthCP _logToAnalytics] : 1716 -> 1752
~ _OUTLINED_FUNCTION_0 : 24 -> 28
~ -[ACCTransportIOAccessoryAuthCP _publishAuthStats:fdrStatus:] : 1300 -> 1332
~ _cpGetInternalComponents : 960 -> 1000
CStrings:
+ "CertificateSupportsLAS"
+ "LAS"
+ "authenticateLASWithChallenge:completionHandler:updateRegistry:"
+ "wcrt"

```
