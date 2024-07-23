## UARPUpdaterServiceDFU

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/UARPUpdaterServiceDFU`

```diff

-1163.0.0.0.0
-  __TEXT.__text: 0x16e30
+1170.0.7.0.0
+  __TEXT.__text: 0x16b64
   __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_stubs: 0x15c0
   __TEXT.__objc_methlist: 0x70c
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x1eba
-  __TEXT.__objc_methname: 0x2344
+  __TEXT.__objc_methname: 0x2345
   __TEXT.__oslogstring: 0xd8c
   __TEXT.__objc_classname: 0x112
-  __TEXT.__objc_methtype: 0x2f22
-  __TEXT.__unwind_info: 0x540
+  __TEXT.__objc_methtype: 0x2f25
+  __TEXT.__unwind_info: 0x538
   __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 620
-  Symbols:   471
+  Functions: 616
+  Symbols:   467
   CStrings:  843
 
Symbols:
+ _uarpPlatformAssetSuperBinaryPullProposedPayloadHeader
- _uarpPlatformAssetSuperBinaryPullPayloadHeader
- _uarpSendAssetAvailableNotificationAck
- _uarpSendAssetProcessingNotificationAck
- _uarpSendDynamicAssetPreProcessingStatusAck
- _uarpSendNoFirmwareUpdateAvailable
CStrings:
+ "@32@0:8^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@24"
+ "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R,V_pAsset"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"
- "@32@0:8^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@24"
- "T^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}},R,V_pAsset"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}16@0:8"

```
