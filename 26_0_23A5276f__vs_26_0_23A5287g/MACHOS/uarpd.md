## uarpd

> `/usr/libexec/uarpd`

```diff

-1338.0.37.0.0
-  __TEXT.__text: 0x7a814
-  __TEXT.__auth_stubs: 0x8f0
-  __TEXT.__objc_stubs: 0x7320
-  __TEXT.__objc_methlist: 0x61e0
-  __TEXT.__objc_methname: 0xa837
-  __TEXT.__objc_classname: 0x14c9
-  __TEXT.__objc_methtype: 0x2373
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x772c
-  __TEXT.__oslogstring: 0x51f9
+1338.0.46.502.1
+  __TEXT.__text: 0x7f28c
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_stubs: 0x7660
+  __TEXT.__objc_methlist: 0x65b0
+  __TEXT.__objc_methname: 0xad4f
+  __TEXT.__objc_classname: 0x1526
+  __TEXT.__objc_methtype: 0x258f
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x7ceb
+  __TEXT.__oslogstring: 0x5739
   __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__unwind_info: 0x1918
-  __DATA_CONST.__auth_got: 0x488
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0xd98
-  __DATA_CONST.__cfstring: 0x33a0
-  __DATA_CONST.__objc_classlist: 0x460
+  __TEXT.__unwind_info: 0x19c8
+  __DATA_CONST.__auth_got: 0x490
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0xdc0
+  __DATA_CONST.__cfstring: 0x3b20
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x448
-  __DATA_CONST.__objc_intobj: 0x3c0
-  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__objc_superrefs: 0x460
+  __DATA_CONST.__objc_intobj: 0x3f0
+  __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0xc500
-  __DATA.__objc_selrefs: 0x22f8
-  __DATA.__objc_ivar: 0x848
-  __DATA.__objc_data: 0x2bc0
+  __DATA.__objc_const: 0xcbf0
+  __DATA.__objc_selrefs: 0x2420
+  __DATA.__objc_ivar: 0x8a4
+  __DATA.__objc_data: 0x2cb0
   __DATA.__data: 0x4f0
   __DATA.__bss: 0x11c0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 868DD569-C117-3412-B0EA-AA8C3FE2FECE
-  Functions: 2908
-  Symbols:   199
-  CStrings:  3825
+  UUID: 68AD73C4-3BDF-34A5-97C4-E7E4ABE4C9DB
+  Functions: 2997
+  Symbols:   201
+  CStrings:  4045
 
Symbols:
+ _OBJC_CLASS_$_UARPDeviceTatsuTicket
+ _compression_encode_buffer
CStrings:
+ "\t"
+ "%s: Active Firmware Verison is %@. Staged Firmware Version is %@. UUID of %@"
+ "%s: Apply Staged Assets - Nothing Staged"
+ "%s: Asset Identifier was updated to %@ for Apple Model Number %@"
+ "%s: Compress offset %lu from %lu bytes to %lu bytes"
+ "%s: Compressed length (%lu) out of tolerance for uncompressed length (%lu)"
+ "%s: Compressed offset %lu from %lu bytes to %lu bytes"
+ "%s: Could not create TLV for uncompressedLength"
+ "%s: Could not find %@ to take measurement"
+ "%s: Could not find subfile %@ in %@ to take measurement; let tatsu fail this"
+ "%s: Failed to craft tatsu requests, %@"
+ "%s: Failed to deompress buffer, status is %s"
+ "%s: NEED TO HANDLE DECOMPRESSION AS FILE"
+ "%s: No Data Block, no URL failed "
+ "%s: RX Firmware Asset Fully Staged, status is %lu. Asset Verison is %@. Staged Version is %@. UUID of %@"
+ "%s: Rescind Staged Assets. UUID of %@"
+ "%s: SuperBinary contains no plist"
+ "%s: SuperBinary payload cannot be compressed; %@"
+ "%s: Tatsu Request for ticket %@"
+ "%s: Tatsu Ticket %@"
+ "%s: Unhandled processing status is %lu. UUID of %@; assume corrupt"
+ "%s: cannot find component %@ for tatsu ticket; %@"
+ "%s: cannot find endpoint for tatsu ticket; %@"
+ "%s: composing payload failed"
+ "%s: configuration specifies an AssetIdentifer of %@, which overrides AppleModelNumber of %@"
+ "%s: could not decompress payload %@, index %lu"
+ "%s: could not expand FTAB for payload %@, index %lu"
+ "%s: database entry specifies an AssetIdentifer of %@, which overrides AppleModelNumber of %@"
+ "%s: metadata length is %lu"
+ "%s: metadata padded length is %lu"
+ "%s: metadata padding is %lu"
+ "%s: offset %lu does not equal %lu "
+ "%s: this endpoint personality %@ does not match %@"
+ "%s: this endpoint personality %@ matches %@"
+ "%s: uarpPlatformEndpointAssetCorrupt() failed; <%u> %s"
+ "----------------------------\n"
+ "-[UARPEndpointControllerInternal endpointControllerQueryAssetIdentifier:endpointNumber:componentNumber:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerTssRequestsForPersonalizedAsset:endpointUUID:reply:]"
+ "-[UARPEndpointControllerInternal endpointControllerTssResponsesForPersonalizedAsset:endpointUUID:reply:]"
+ "-[UARPEndpointLayer3 craftTatsuRequests:]"
+ "-[UARPEndpointLayer3 notifyLayer2RxFirmwareFullyStaged:]"
+ "-[UARPEndpointLayer3 personalizeFirmwareAssetComplete:]_block_invoke"
+ "-[UARPEndpointLayer3(Layer2AssetCallbacks) assetRescind:]"
+ "-[UARPHostManager assetPersonalizationComplete:endpointUUID:tssOptions:]"
+ "-[UARPSuperBinaryLayer3 expandSuperBinaryPlist]"
+ "-[UARPSuperBinaryLayer3 personalizationStateCompleted]"
+ "-[UARPSuperBinaryPayloadLayer3 compressPayload]"
+ "-[UARPSuperBinaryPayloadLayer3 decompressPayload]"
+ "-[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryData:]"
+ "-[UARPSuperBinaryPayloadLayer3 initWithPayloadData:payloadMetaData:payload4cc:payloadVersion:payloadIndex:]"
+ "-[UARPSuperBinaryPayloadLayer3 setDataBlockToData:offset:payloadData:]"
+ "-[UARPSuperBinaryPayloadLayer3 setDataBlockToURL:offset:url:]"
+ "@\"UARPEndpointDatabaseEntry2\""
+ "@40@0:8@16@24B32B36"
+ "@40@0:8@16Q24@32"
+ "@44@0:8@16@24Q32B40"
+ "A2512"
+ "A2513"
+ "A2580"
+ "A2617"
+ "A2618"
+ "A2619"
+ "A2698"
+ "A2699"
+ "A2700"
+ "A2871"
+ "A2872"
+ "A2931"
+ "A2952"
+ "A3047"
+ "A3048"
+ "A3049"
+ "A3050"
+ "A3053"
+ "A3054"
+ "A3055"
+ "A3056"
+ "A3057"
+ "A3059"
+ "A3063"
+ "A3064"
+ "A3065"
+ "A3150"
+ "A3151"
+ "A3153"
+ "A3157"
+ "A3158"
+ "A3159"
+ "A3250"
+ "A3502"
+ "A3503"
+ "Asset Corrupt for SuperBinary <%@> for Endpoint <%@>"
+ "Asset Identifier"
+ "Asset Length                : %lu\n"
+ "AssetIdentifier"
+ "B40@0:8@16@24@32"
+ "B64@0:8@16q24@32@40@48@56"
+ "Format Version              : %lu\n"
+ "FriendlyName"
+ "Header Length               : %lu\n"
+ "Header Length           : %lu\n"
+ "Migrating mapping database from v1 to v2 %@"
+ "Payload Data Length     : %lu\n"
+ "Payload Data Offset     : %lu\n"
+ "Payload Header\n"
+ "Payload Headers Length      : %lu\n"
+ "Payload Headers Offset      : %lu\n"
+ "Payload Index <%lu> for SuperBinary <%@> for Endpoint <%@>.updated staged firmware version to %@"
+ "Payload MetaData Length : %lu\n"
+ "Payload MetaData Offset : %lu\n"
+ "Payload Tag             : %c%c%c%c\n"
+ "Payload Version         : %lu.%lu.%lu.%lu\n"
+ "ROOT"
+ "SuperBinary Header\n"
+ "SuperBinary MetaData Length : %lu\n"
+ "SuperBinary MetaData Offset : %lu\n"
+ "SuperBinary Version         : %lu.%lu.%lu.%lu\n"
+ "T@\"NSData\",&,V_nonceSeed"
+ "T@\"NSData\",R,V_hashValue"
+ "T@\"NSDictionary\",C,V_tatsuRequest"
+ "T@\"NSDictionary\",C,V_tatsuResponse"
+ "T@\"NSString\",&,V_assetIdentifier"
+ "T@\"NSString\",&,V_friendlyName"
+ "T@\"NSString\",C,V_assetIdentifier"
+ "T@\"NSString\",R,V_assetIdentifier"
+ "TB,V_manifestAsTLV"
+ "TMAP Data is nil or not a dictionary: TMAP Value: %@, Error: %@"
+ "UARP: No personalization response"
+ "UARPEndpointDatabaseEntry2"
+ "UARPHashMachine"
+ "UARPMetaDataInformationAssetIdentifier"
+ "_assetIdentifier"
+ "_compressedHash"
+ "_compressedPayloadDataInternal"
+ "_compressedPayloadURL"
+ "_context256"
+ "_context384"
+ "_context512"
+ "_hashValue"
+ "_manifestAsTLV"
+ "_payloadHeader"
+ "_tatsuRequest"
+ "_tatsuResponse"
+ "_uncompressedHash"
+ "_useFilesystem"
+ "appendCompressedPayloadData:offset:"
+ "assetIdentifier"
+ "assetIdentifierForAppleModelNumber:"
+ "assetPersonalizationComplete:endpointUUID:tssOptions:"
+ "assetPersonalizationComplete:hostEndpoint:"
+ "compressPayload"
+ "compressedPayload.%lu"
+ "craftTatsuRequests:"
+ "decompressPayload"
+ "descriptionOfHeader"
+ "determinePayloadHashAlgorithm"
+ "endpointControllerQueryAssetIdentifier:endpointNumber:componentNumber:reply:"
+ "endpointControllerTssRequestsForPersonalizedAsset:endpointUUID:reply:"
+ "endpointControllerTssResponsesForPersonalizedAsset:endpointUUID:reply:"
+ "expandSuperBinaryPlist"
+ "finalizeHash"
+ "hashValue"
+ "initWithAlgorithm:"
+ "initWithComponentTag:tssRequest:"
+ "initWithPayloadDictionary:payloadsURL:payloadIndex:useFilesystem:"
+ "initWithPropertyList:payloadsURL:noMissingPayloads:useFilesystem:"
+ "manifestAsTLV"
+ "notifyLayer2RxFirmwareFullyStaged:"
+ "performTatsuRequest:"
+ "personalizationNeeded:endpointUUID:tssServerURL:"
+ "personalizationStateCompleted"
+ "personalizationStateStarted"
+ "personalizeAsset:error:"
+ "personalizeFirmwareAssetComplete:"
+ "reportPersonalizationTicket:endpointUUID:tssOptions:"
+ "setAssetIdentifier:"
+ "setCompressedDataBlock:offset:"
+ "setDataBlockToData:offset:payloadData:"
+ "setDataBlockToURL:offset:url:"
+ "setManifestAsTLV:"
+ "setPayloadHeader:"
+ "setTatsuRequest:"
+ "setTatsuResponse:"
+ "setTssResponse:"
+ "tatsuRequests"
+ "tatsuResponses"
+ "tssRequests"
+ "tssResponses"
+ "updateHash:"
+ "v24@0:8^{UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}16"
+ "v40@0:8@\"NSUUID\"16@\"NSUUID\"24@\"NSArray\"32"
+ "{CC_SHA256state_st=\"count\"[2I]\"hash\"[8I]\"wbuf\"[16I]}"
+ "{CC_SHA512state_st=\"count\"[2Q]\"hash\"[8Q]\"wbuf\"[16Q]}"
+ "{UARPPayloadHeader2=\"payloadHeaderLength\"I\"payloadTag\"{UARP4ccTag=\"char1\"C\"char2\"C\"char3\"C\"char4\"C}\"payloadVersion\"{UARPVersion=\"major\"I\"minor\"I\"release\"I\"build\"I}\"payloadMetadataOffset\"I\"payloadMetadataLength\"I\"payloadOffset\"I\"payloadLength\"I}"
+ "\xf0\xf0\xf0\xf0a"
- "%s: Failed to personalization; Asset UUID is %@, Endpoint UUID is %@, server URL is %@, tss options are %@"
- "%s: Personalization Ticket %@"
- "%s: Personalization succeeded; Asset UUID is %@, Endpoint UUID is %@, server URL is %@"
- "%s: RX Firmware Asset Fully Staged, status is %lu. UUID of %@"
- "%s: Tatsu Ticket for personalizing SuperBinary %@"
- "%s: manifest length is %lu"
- "%s: manifest padded length is %lu"
- "%s: manifest padding is %lu"
- "%s: ticket is %@"
- "%s: tss options are %@"
- "-[UARPEndpointControllerInternal endpointControllerTssRequestForPersonalizedAsset:endpointUUID:reply:]"
- "-[UARPEndpointControllerInternal endpointControllerTssResponseForPersonalizedAsset:endpointUUID:reply:]"
- "-[UARPEndpointLayer3 craftTatsuRequest:]"
- "-[UARPEndpointLayer3 personalizeFirmwareAssetComplete:tssResponse:]_block_invoke"
- "-[UARPHostManager assetPersonalizationComplete:endpointUUID:personalizationTicket:]"
- "-[UARPHostManager assetPersonalizationComplete:hostEndpoint:personalizationTicket:]"
- "-[UARPSuperBinaryPayloadLayer3 setDataBlockToURL:offset:]"
- "@\"UARPEndpointDatabaseEntry\""
- "NOT IMPLEMENTED YET - Asset Corrupt for SuperBinary <%@> for Endpoint <%@>"
- "NOT IMPLEMENTED YET - Asset Rescind for SuperBinary <%@> for Endpoint <%@>"
- "T@\"NSDictionary\",R,V_personalizationOptions"
- "T@\"NSDictionary\",R,V_personalizationTicket"
- "T@\"NSDictionary\",R,V_tssRequest"
- "T@\"NSDictionary\",R,V_tssResponse"
- "TMAP Data is Nil, %@"
- "TMAP Data is not a dictionary"
- "_personalizationOptions"
- "_personalizationTicket"
- "_tssRequest"
- "_tssResponse"
- "assetPersonalizationComplete:hostEndpoint:personalizationTicket:"
- "craftTatsuRequest:"
- "personalizationNeeded:endpointUUID:assetUUID:tssServerURL:"
- "reportPersonalizationTicket:endpointUUID:personalizationTicket:"
- "setDataBlockToData:offset:"
- "setDataBlockToURL:offset:"
- "v64@0:8@16q24@32@40@48@56"

```
