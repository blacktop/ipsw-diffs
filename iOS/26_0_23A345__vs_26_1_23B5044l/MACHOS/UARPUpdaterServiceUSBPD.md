## UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD`

```diff

-1338.0.72.0.0
-  __TEXT.__text: 0x25a04
+1338.40.19.0.0
+  __TEXT.__text: 0x27534
   __TEXT.__auth_stubs: 0x870
-  __TEXT.__objc_stubs: 0x33c0
-  __TEXT.__objc_methlist: 0x19c0
+  __TEXT.__objc_stubs: 0x3580
+  __TEXT.__objc_methlist: 0x1ab0
   __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x26a9
-  __TEXT.__cstring: 0x2f45
-  __TEXT.__objc_classname: 0x209
-  __TEXT.__objc_methtype: 0x37e9
+  __TEXT.__oslogstring: 0x2983
+  __TEXT.__cstring: 0x30ae
+  __TEXT.__objc_classname: 0x20b
+  __TEXT.__objc_methtype: 0x38d9
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__objc_methname: 0x45ba
-  __TEXT.__unwind_info: 0x798
+  __TEXT.__objc_methname: 0x47da
+  __TEXT.__unwind_info: 0x828
   __DATA_CONST.__auth_got: 0x448
   __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__const: 0x718
-  __DATA_CONST.__cfstring: 0x620
+  __DATA_CONST.__cfstring: 0x640
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x35b0
-  __DATA.__objc_selrefs: 0x1030
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_const: 0x3708
+  __DATA.__objc_selrefs: 0x10b8
+  __DATA.__objc_ivar: 0x240
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x375
-  __DATA.__bss: 0x1174
+  __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 266C64CE-50C8-314A-B15C-7A62FA40E709
-  Functions: 1066
-  Symbols:   571
-  CStrings:  1591
+  UUID: 5000C8AE-0820-3BFE-A32C-BC4915701E59
+  Functions: 1114
+  Symbols:   590
+  CStrings:  1645
 
Symbols:
+ _uarpPlatformDelegateForDownstreamID
+ _uarpPlatformDownstreamEndpointAdd
+ _uarpPlatformDownstreamEndpointAddWithID
+ _uarpPlatformDownstreamEndpointDiscovery
+ _uarpPlatformDownstreamEndpointReachable
+ _uarpPlatformDownstreamEndpointRemove
+ _uarpPlatformDownstreamEndpointSendMessage
+ _uarpPlatformDownstreamEndpointUnreachable
+ _uarpPlatformEndpointBulkInfoQuery
+ _uarpPlatformEndpointDiscoverEndpointIDs
+ _uarpPlatformEndpointPayloadRequestAllHeadersAndMetaData
+ _uarpPlatformEndpointRequestInfoProperty
+ _uarpPlatformEndpointStreamingRecvBytes
+ _uarpPlatformEndpointStreamingRecvDeinit
+ _uarpPlatformEndpointStreamingRecvInit
+ _uarpPlatformNoFirmwareUpdateAvailable
+ _uarpPlatformQueryEndpointComponentDiscovery
+ _uarpPlatformSendMessageFromDownstreamEndpointID
+ _uarpPlatformSendMessageToDownstreamEndpointID
CStrings:
+ "%c%c%c%c"
+ "%s: - Tag is %c%c%c%c"
+ "%s: - Version is %u.%u.%u.%u"
+ "%s: Asset has zero payloads that match requirements; %s"
+ "%s: Asset has zero payloads; %s"
+ "%s: Comparing current payload FW version (index %lu) to active Firmware Version; results <%ld>"
+ "%s: Did not find a payload that matches requirements"
+ "%s: ESPRESSO Corrupt Entry ? pBuffer = %p, pMsg = %p"
+ "%s: Error querying all headers and metadata"
+ "%s: Failed to query number of payloads; <%u> %s"
+ "%s: Matched payload did not meet strictly higher version requirement"
+ "%s: Payload Index %lu"
+ "%s: activeFwVersion <%@>"
+ "%s: address space read failed for 0x%x"
+ "%s: payloadFwVersion <%@>"
+ "%s: uarpAssetQueryPayloadInfo() failed; <%u> %s"
+ "%s: uarpPlatformEndpointAssetSetPayloadIndex() failed; <%u> %s"
+ "-[UARPMagSafeCable queryHardwareVersion]"
+ "-[VUARPAsset assetAllHeadersAndMetaDataComplete:error:]"
+ "-[VUARPAsset assetReady:error:]"
+ "-[VUARPAsset isAcceptablePayloadVersion:error:]"
+ "-[VUARPAsset payloadMatchesAtIndex:index:]"
+ "-[VUARPAsset selectMatchingPayloadIndex:error:]"
+ "@\"NSNumber\"16@0:8"
+ "B32@0:8@16Q24"
+ "Failed to query hardware version"
+ "Querying hardware version"
+ "T@\"NSNumber\",&,N,V_hardwareVersion"
+ "T@\"NSString\",&,N,V_expectedPayloadTag"
+ "_currentPayloadInfo"
+ "_expectedPayloadTag"
+ "_hardwareVersion"
+ "_numPayloads"
+ "_tagAlreadyQueried"
+ "assetAllHeadersAndMetaDataComplete:error:"
+ "compare:"
+ "expectedPayloadTag"
+ "expectedTag"
+ "getFirmwareVersionGiven32Bits:"
+ "initWithString:"
+ "isAcceptablePayloadVersion:error:"
+ "numberWithUnsignedChar:"
+ "payloadMatchesAtIndex:index:"
+ "queryExpectedPayloadTag"
+ "queryHardwareVersion"
+ "selectMatchingPayloadIndex:error:"
+ "setExpectedPayloadTag:"
+ "setHardwareVersion:"
+ "setHwRevision:"
+ "stringValue"
+ "uarpTransmitEntryIsValidToSend"
+ "vuarpExpectedTag"
+ "{uarpPayloadInfo=\"payloadTag\"{UARP4ccTag=\"char1\"C\"char2\"C\"char3\"C\"char4\"C}\"payloadVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"payloadMetadataLength\"I\"payloadLength\"I\"uncompressedPayloadLength\"I}"

```
