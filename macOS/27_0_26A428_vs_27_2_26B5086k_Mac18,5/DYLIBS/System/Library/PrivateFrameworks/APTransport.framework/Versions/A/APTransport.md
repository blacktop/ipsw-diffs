## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/Versions/A/APTransport`

```diff

-980.77.5.3.0
-  __TEXT.__text: 0x8c1e0
-  __TEXT.__objc_methlist: 0x1a64
-  __TEXT.__const: 0x63c
-  __TEXT.__gcc_except_tab: 0x850
-  __TEXT.__cstring: 0x24dee
+1005.7.1.0.0
+  __TEXT.__text: 0x8c1a8
+  __TEXT.__objc_methlist: 0x1aa4
+  __TEXT.__const: 0x64c
+  __TEXT.__gcc_except_tab: 0x844
+  __TEXT.__cstring: 0x24de6
   __TEXT.__dlopen_cstrs: 0xfe
   __TEXT.__oslogstring: 0x1af
-  __TEXT.__unwind_info: 0x3680
+  __TEXT.__unwind_info: 0x3640
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1b08
+  __DATA_CONST.__const: 0x1b00
   __DATA_CONST.__objc_classlist: 0x58
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16f0
+  __DATA_CONST.__objc_selrefs: 0x1738
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__got: 0x360
-  __AUTH_CONST.__const: 0x38e0
-  __AUTH_CONST.__cfstring: 0x5800
-  __AUTH_CONST.__objc_const: 0x20c8
+  __AUTH_CONST.__const: 0x38b0
+  __AUTH_CONST.__cfstring: 0x5820
+  __AUTH_CONST.__objc_const: 0x2128
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x0

   __DATA.__objc_ivar: 0x174
   __DATA.__data: 0xeb0
   __DATA_DIRTY.__objc_data: 0x280
-  __DATA_DIRTY.__data: 0xaf0
-  __DATA_DIRTY.__bss: 0x240
+  __DATA_DIRTY.__data: 0xa80
+  __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4233
-  Symbols:   4663
-  CStrings:  3632
+  Functions: 4221
+  Symbols:   4669
+  CStrings:  3628
 
Symbols:
+ -[WiFiAwareDatapathInfo(APTNANDataSession) peerSignalStrength]
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table8
+ _APSSignalStrengthDBmFromScaled
+ _APTDiagnosticSendStreamInfo
+ _APTNANDataSessionCopyDatapathIDAndPeerMAC
+ _APTNANDataSessionGetDatapathRSSI
+ _APTransportConnectionCopyProperty
+ _APTransportConnectionGetDSCPForSocketQoS
+ _APTransportConnectionQoSFromSocketQoS
+ _APTransportSocketQoSFromConnectionQoS
+ __APTNANDataSessionCopyDatapathIDAndPeerMAC
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_WiFiAwareDatapathInfo_$_APTNANDataSession
+ __OBJC_$_CATEGORY_WiFiAwareDatapathInfo_$_APTNANDataSession
+ ___62-[WiFiAwareDatapathInfo(APTNANDataSession) peerSignalStrength]_block_invoke
+ ___block_descriptor_48_e8_32o40o_e44_v16?0"WiFiAwareDatapathPerformanceReport"8l
+ _nw_content_context_set_metadata_for_protocol
+ _nw_ip_create_metadata
+ _nw_ip_metadata_set_dscp_value
+ _objc_msgSend$deactivate
+ _objc_msgSend$firstObject
+ _objc_msgSend$peerSignalStrength
+ _objc_msgSend$performance:
+ _objc_msgSend$signalStrength
+ _unbufnwGuts_setQualityOfServiceInternal
- APTPacingControllerReset
- APTransportWifiManagerClientCreate
- GCC_except_table42
- GCC_except_table45
- _APTDiagnosticMulticastDataToAllHosts
- _APTPacingControllerReset
- _APTransportWifiManagerClientCreate
- _APTransportWifiManagerClientRegister
- _APTransportWifiManagerClientUnregister
- _CMBaseObjectCopyProperty
- ___APTransportWifiManagerClientRegister_block_invoke
- ___APTransportWifiManagerClientUnregister_block_invoke
- _gLogCategory_APTransportWifiManagerClient
- _kAPTransportProperty_WifiManagerClient
- _kAPTransportWifiManagerClientClass
- _session_performWifiManagerRegistration
- _wifiManagerClient_Finalize
- _wifiManagerClient_getTypeID
- session_performWifiManagerRegistration
- wifiManagerClient_Finalize
CStrings:
+ "1005.7.1"
+ "APTNANDataSessionGetDatapathRSSI"
+ "[%{ptr}] APTransportKeepAliveControllerStandard created for stream [%{ptr}] with queue QoS class %u\n"
+ "[%{ptr}] addBytesSent nowNs=%llu epochNs=%llu bytesSent=%llu burstStartNs=%llu burstBytesSent=%llu"
+ "[%{ptr}] begYield nowNs=%llu epochNs=%llu bytesSent=%llu burstStartNs=%llu burstBytesSent=%llu"
+ "[%{ptr}] created leewayNs=%llu minYieldNs=%llu maxBehindNs=%llu"
+ "[%{ptr}] re-anchor behindNs=%llu"
+ "[%{ptr}] socketQoS=%u (trafficClass=%u, dscp=%u)"
+ "_APTNANDataSessionCopyDatapathIDAndPeerMAC"
+ "_APTNANDataSessionCreateDatapathInfo"
+ "pacingController_maxBehindUs"
+ "unbufnwQoS"
+ "v16@?0@\"WiFiAwareDatapathPerformanceReport\"8"
+ "void unbufnwGuts_setQualityOfServiceInternal(APTransportConnectionUnbufferedNWGutsRef, int)"
- "980.77.5.3"
- "APTPacingControllerReset"
- "APTransportWifiManagerClient"
- "APTransportWifiManagerClient %{ptr} created\n"
- "APTransportWifiManagerClient %{ptr} finalizing\n"
- "APTransportWifiManagerClient.queue"
- "APTransportWifiManagerClientCreate"
- "OSStatus APTPacingControllerReset(APTPacingControllerRef)"
- "OSStatus APTransportWifiManagerClientCreate(CFAllocatorRef, APTransportWifiManagerClientRef *)"
- "WifiManagerClient"
- "[%{ptr}] APTransportKeepAliveControllerStandard created for stream [%{ptr}]\n"
- "[%{ptr}] addBytesSent nowNs=%llu epochNs=%llu bytesSent=%llu"
- "[%{ptr}] begYield nowNs=%llu epochNs=%llu bytesSent=%llu"
- "[%{ptr}] created"
- "[%{ptr}] reset"
- "[%{ptr}] socketQoS=%u (trafficClass=%u)"
- "session_performWifiManagerRegistration"
- "void wifiManagerClient_Finalize(CFTypeRef)"
```
