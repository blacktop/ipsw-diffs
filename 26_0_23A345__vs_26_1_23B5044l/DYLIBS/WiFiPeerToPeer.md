## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-826.105.0.0.0
-  __TEXT.__text: 0x20ea8
+835.3.0.0.0
+  __TEXT.__text: 0x20e3c
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x338c
+  __TEXT.__objc_methlist: 0x3374
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x5467
   __TEXT.__oslogstring: 0x7e2
   __TEXT.__gcc_except_tab: 0x380
   __TEXT.__unwind_info: 0x968
   __TEXT.__objc_classname: 0x779
-  __TEXT.__objc_methname: 0x8196
-  __TEXT.__objc_methtype: 0x1bcb
-  __TEXT.__objc_stubs: 0x41a0
+  __TEXT.__objc_methname: 0x811a
+  __TEXT.__objc_methtype: 0x1b7d
+  __TEXT.__objc_stubs: 0x4180
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0xd30
+  __DATA_CONST.__const: 0xd38
   __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1728
+  __DATA_CONST.__objc_selrefs: 0x1718
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x3500
-  __AUTH_CONST.__objc_const: 0x5918
+  __AUTH_CONST.__objc_const: 0x5910
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x42c
   __DATA.__data: 0x900

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F691001B-A120-3904-A450-A70E5DF0358C
-  Functions: 1035
-  Symbols:   3698
-  CStrings:  2428
+  UUID: 84D4068D-BB88-32FF-B2EF-B89BE4A37D24
+  Functions: 1034
+  Symbols:   3695
+  CStrings:  2424
 
Symbols:
+ +[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:peerMacAddress:]
+ GCC_except_table42
+ ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.115
+ ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.118
+ ___81+[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:peerMacAddress:]_block_invoke
+ ___block_descriptor_49_e8_32s_e40_v24?0"<WiFiP2PXPCProtocol>"8?<v?>16ls32l8
+ _objc_msgSend$queryPerformanceReportFor:datapathType:peerMacAddress:completion:
- +[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:]
- -[WiFiAwareDataSession datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:]
- GCC_except_table43
- ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.120
- ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.123
- ___66+[WiFiAwareDatapathPerformanceReport performanceFor:datapathType:]_block_invoke
- ___block_descriptor_41_e40_v24?0"<WiFiP2PXPCProtocol>"8?<v?>16l
- _objc_msgSend$dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:
- _objc_msgSend$queryPerformanceReportFor:datapathType:completion:
CStrings:
+ "@36@0:8C16q20@28"
+ "performanceFor:datapathType:peerMacAddress:"
+ "queryPerformanceReportFor:datapathType:peerMacAddress:completion:"
+ "v44@0:8C16q20@\"WiFiMACAddress\"28@?<v@?@\"WiFiAwareDatapathPerformanceReport\">36"
+ "v44@0:8C16q20@28@?36"
- "@28@0:8C16q20"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
- "datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:"
- "performanceFor:datapathType:"
- "queryPerformanceReportFor:datapathType:completion:"
- "v36@0:8C16q20@?28"
- "v36@0:8C16q20@?<v@?@\"WiFiAwareDatapathPerformanceReport\">28"
- "v40@0:8@\"WiFiMACAddress\"16@\"WiFiAwarePublishDatapathServiceSpecificInfo\"24@\"NSUUID\"32"
- "v40@0:8@16@24@32"

```
