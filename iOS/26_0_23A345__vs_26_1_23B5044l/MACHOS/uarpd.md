## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.0.72.0.0
-  __TEXT.__text: 0x83dfc
-  __TEXT.__auth_stubs: 0x970
-  __TEXT.__objc_stubs: 0x78e0
-  __TEXT.__objc_methlist: 0x6988
-  __TEXT.__objc_methname: 0xb40a
-  __TEXT.__objc_classname: 0x162e
-  __TEXT.__objc_methtype: 0x2564
+1338.40.19.0.0
+  __TEXT.__text: 0x84bf4
+  __TEXT.__auth_stubs: 0x960
+  __TEXT.__objc_stubs: 0x7a20
+  __TEXT.__objc_methlist: 0x6a90
+  __TEXT.__objc_methname: 0xb691
+  __TEXT.__objc_classname: 0x1664
+  __TEXT.__objc_methtype: 0x25e6
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x85c9
-  __TEXT.__oslogstring: 0x5c88
+  __TEXT.__cstring: 0x8783
+  __TEXT.__oslogstring: 0x5d75
   __TEXT.__gcc_except_tab: 0x158
-  __TEXT.__unwind_info: 0x1a50
-  __DATA_CONST.__auth_got: 0x4c8
+  __TEXT.__unwind_info: 0x1a80
+  __DATA_CONST.__auth_got: 0x4c0
   __DATA_CONST.__got: 0x490
   __DATA_CONST.__const: 0xee0
   __DATA_CONST.__cfstring: 0x44a0
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x498
   __DATA_CONST.__objc_intobj: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xd380
-  __DATA.__objc_selrefs: 0x2530
-  __DATA.__objc_ivar: 0x904
+  __DATA.__objc_const: 0xd420
+  __DATA.__objc_selrefs: 0x25b8
+  __DATA.__objc_ivar: 0x910
   __DATA.__objc_data: 0x2ee0
-  __DATA.__data: 0x4e8
+  __DATA.__data: 0x548
   __DATA.__bss: 0x1178
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: B16C5C5F-6DDE-3287-B33F-377B2896B99D
-  Functions: 3066
-  Symbols:   207
-  CStrings:  4319
+  UUID: D68BBF24-0A4E-30FE-BEE7-45111AA28D16
+  Functions: 3098
+  Symbols:   206
+  CStrings:  4357
 
Symbols:
- _objc_retain_x6
CStrings:
+ "%s: Asset DENIED due to firmware version %@"
+ "%s: _data is nil"
+ "%s: _superbinaryURLis nil"
+ "%s: closeAndReturnError failed %@ "
+ "%s: could not prepare personalized URL for payload index %lu"
+ "%s: endpoint %@Available firmware version %@ is not greater than Active firmware version %@ "
+ "%s: invalid payload header size; expected %lu, but got %u"
+ "%s: no previous ftab associated for payload index %lu"
+ "%s: not an FTAB payload for payload index %lu"
+ "%s: payload URL is nil for payload index %lu"
+ "%s: todo: as data for payload index %lu"
+ "-[UARPHostManager preflightOfferRestrictionByFirmwareVersion:hostEndpoint:]"
+ "-[UARPHostManager preflightOfferRestrictions:hostEndpoint:]"
+ "-[UARPSuperBinaryLayer3 expandPayloadWithHeader:payloadIndex:]"
+ "-[UARPSuperBinaryLayer3 expandPayloadWithHeaderAsData:payloadIndex:payload4cc:payloadVersion:payloadMetaData:]"
+ "-[UARPSuperBinaryLayer3 prepareComposedComponents:excludingTags:allHeaders:allMetaData:error:]"
+ "-[UARPSuperBinaryPayloadLayer3 composePersonalizedFTAB]"
+ "-[UARPSuperBinaryPayloadLayer3 preparePersonalizedURL]"
+ "@\"<UARPEndpointPacketCaptureDelegateProtocol>\""
+ "@\"UARPEndpointPacketCaptureDelegate\""
+ "@24@0:8o^@16"
+ "B68@0:8@16@24@32@40S48@52@60"
+ "T@\"<UARPEndpointPacketCaptureDelegateProtocol>\",R,V_pcapDelegate"
+ "UARPEndpointPacketCaptureDelegate"
+ "UARPEndpointPacketCaptureDelegateProtocol"
+ "_delegate"
+ "_layer2PayloadHeader"
+ "_pcapDelegate"
+ "addToVersion:"
+ "closeDumper"
+ "com.apple.uarp.uarpd.logger"
+ "composePersonalizedFTAB"
+ "composePersonalizedPayload"
+ "composeToData:"
+ "composeToDataExcludingTags:error:"
+ "dumpPacket:packetDirection:"
+ "initWithUUID:tmpFolderPath:delegate:"
+ "payloadDataAsData"
+ "payloadDataAsURL"
+ "pcapDelegate"
+ "preflightOfferRestrictionByFirmwareVersion:hostEndpoint:"
+ "preflightOfferRestrictions:hostEndpoint:"
+ "prepareComposedComponents:excludingTags:allHeaders:allMetaData:error:"
+ "preparePersonalizedURL"
+ "startUARPLayer2:configuration:infoProperties:appleProperties:endpointID:upstreamEndpoint:pcapDelegate:"
+ "updateDelegateFilename"
+ "updateFilepath:uuid:"
+ "v32@0:8@\"NSString\"16@\"NSUUID\"24"
+ "writeComposedPayloadDataToFile:error:"
+ "writeComposedPayloadURLToFile:error:"
- "%s: Checking active firmware version for endpoint %@"
- "%s: Proceeding with update. Available firmware version %@ is greater than Active firmware version %@ of endpoint %@"
- "%s: Skipping update. Available firmware version %@ is not greater than Active firmware version %@ of endpoint %@"
- "-[UARPHostManager preflightOfferRestrictions:]"
- "-[UARPSuperBinaryLayer3 writeToURL:excludeTags:error:]"
- "@\"UARPEndpointPacketDumper\""
- "UARPEndpointPacketDumper"
- "_packetDumper"
- "_payloadHeader"
- "initWithUUID:packetCaptureURL:"
- "logPacket:packetDirection:"
- "preflightOfferRestrictions:"

```
