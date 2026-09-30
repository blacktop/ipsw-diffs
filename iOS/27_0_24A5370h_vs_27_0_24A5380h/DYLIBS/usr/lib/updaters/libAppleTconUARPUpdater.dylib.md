## libAppleTconUARPUpdater.dylib

> `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

```diff

-  __TEXT.__text: 0x6d514
-  __TEXT.__objc_methlist: 0x63ec
-  __TEXT.__cstring: 0x7439
+  __TEXT.__text: 0x702e4
+  __TEXT.__objc_methlist: 0x67fc
+  __TEXT.__cstring: 0x7675
   __TEXT.__const: 0x110
-  __TEXT.__oslogstring: 0x37a1
+  __TEXT.__oslogstring: 0x377b
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x1938
+  __TEXT.__unwind_info: 0x1a50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xdb8
-  __DATA_CONST.__objc_classlist: 0x518
+  __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ee0
+  __DATA_CONST.__objc_selrefs: 0x1f70
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x508
+  __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0xd8
-  __DATA_CONST.__got: 0x620
+  __DATA_CONST.__got: 0x680
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x5340
-  __AUTH_CONST.__objc_const: 0xc810
+  __AUTH_CONST.__cfstring: 0x54c0
+  __AUTH_CONST.__objc_const: 0xd1f8
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x3d0
-  __AUTH.__objc_data: 0x32f0
-  __DATA.__objc_ivar: 0x870
+  __AUTH.__objc_data: 0x36b0
+  __DATA.__objc_ivar: 0x8a4
   __DATA.__data: 0x305
-  __DATA.__bss: 0x1188
+  __DATA.__bss: 0x1180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2835
-  Symbols:   8252
-  CStrings:  1949
+  Functions: 2921
+  Symbols:   8532
+  CStrings:  1974
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:tlvs:]
+ -[UARPEndpointLayer3 notifyDownstreamEndpointReachable:tlvs:]
+ -[UARPEndpointLayer3 packetTracking:packetDirection:inFunction:]
+ -[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackDownstreamReachable:tlvs:]
+ -[UARPMetaDataPersonalizationBoardID64 boardID]
+ -[UARPMetaDataPersonalizationBoardID64 description]
+ -[UARPMetaDataPersonalizationBoardID64 initWithLength:value:]
+ -[UARPMetaDataPersonalizationBoardID64 initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationBoardID64 init]
+ -[UARPMetaDataPersonalizationBoardID64 tlvValue]
+ -[UARPMetaDataPersonalizationDemotionProductionMode demotionProductionMode]
+ -[UARPMetaDataPersonalizationDemotionProductionMode description]
+ -[UARPMetaDataPersonalizationDemotionProductionMode initWithLength:value:]
+ -[UARPMetaDataPersonalizationDemotionProductionMode initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationDemotionProductionMode init]
+ -[UARPMetaDataPersonalizationDemotionProductionMode tlvValue]
+ -[UARPMetaDataPersonalizationDemotionSecurityMode demotionSecurityMode]
+ -[UARPMetaDataPersonalizationDemotionSecurityMode description]
+ -[UARPMetaDataPersonalizationDemotionSecurityMode initWithLength:value:]
+ -[UARPMetaDataPersonalizationDemotionSecurityMode initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationDemotionSecurityMode init]
+ -[UARPMetaDataPersonalizationDemotionSecurityMode tlvValue]
+ -[UARPMetaDataPersonalizationDigestListSize description]
+ -[UARPMetaDataPersonalizationDigestListSize digestListSize]
+ -[UARPMetaDataPersonalizationDigestListSize initWithLength:value:]
+ -[UARPMetaDataPersonalizationDigestListSize initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationDigestListSize init]
+ -[UARPMetaDataPersonalizationDigestListSize tlvValue]
+ -[UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride description]
+ -[UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride initWithLength:value:]
+ -[UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride init]
+ -[UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride productionModeHostOverride]
+ -[UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride tlvValue]
+ -[UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride description]
+ -[UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride initWithLength:value:]
+ -[UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride init]
+ -[UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride securityModeHostOverride]
+ -[UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride tlvValue]
+ -[UARPMetaDataPersonalizationMatchingData .cxx_destruct]
+ -[UARPMetaDataPersonalizationMatchingData description]
+ -[UARPMetaDataPersonalizationMatchingData initWithLength:value:]
+ -[UARPMetaDataPersonalizationMatchingData initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationMatchingData init]
+ -[UARPMetaDataPersonalizationMatchingData matchingData]
+ -[UARPMetaDataPersonalizationMatchingData tlvValue]
+ -[UARPMetaDataPersonalizationMatchingDataPayloadTags .cxx_destruct]
+ -[UARPMetaDataPersonalizationMatchingDataPayloadTags description]
+ -[UARPMetaDataPersonalizationMatchingDataPayloadTags initWithLength:value:]
+ -[UARPMetaDataPersonalizationMatchingDataPayloadTags initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationMatchingDataPayloadTags init]
+ -[UARPMetaDataPersonalizationMatchingDataPayloadTags payloadTags]
+ -[UARPMetaDataPersonalizationMatchingDataPayloadTags tlvValue]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMax description]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMax initWithLength:value:]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMax initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMax init]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMax productRevisionMax]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMax tlvValue]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMin description]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMin initWithLength:value:]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMin initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMin init]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMin productRevisionMin]
+ -[UARPMetaDataPersonalizationMatchingDataProductRevisionMin tlvValue]
+ -[UARPMetaDataPersonalizationMoreRequestsToFollow description]
+ -[UARPMetaDataPersonalizationMoreRequestsToFollow initWithLength:value:]
+ -[UARPMetaDataPersonalizationMoreRequestsToFollow initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationMoreRequestsToFollow init]
+ -[UARPMetaDataPersonalizationMoreRequestsToFollow moreRequestsToFollow]
+ -[UARPMetaDataPersonalizationMoreRequestsToFollow tlvValue]
+ -[UARPMetaDataPersonalizationSharedManifest description]
+ -[UARPMetaDataPersonalizationSharedManifest initWithLength:value:]
+ -[UARPMetaDataPersonalizationSharedManifest initWithPropertyListValue:relativeURL:]
+ -[UARPMetaDataPersonalizationSharedManifest init]
+ -[UARPMetaDataPersonalizationSharedManifest sharedManifest]
+ -[UARPMetaDataPersonalizationSharedManifest tlvValue]
+ -[UARPRTKitFTAB adjustSubfileLengthsAndOffsets]
+ -[UARPRTKitFTABSubfile updateSubfileOffset:]
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationBoardID64
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationDemotionProductionMode
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationDemotionSecurityMode
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationDigestListSize
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationMatchingData
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationMatchingDataPayloadTags
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMax
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMin
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationMoreRequestsToFollow
+ _OBJC_CLASS_$_UARPMetaDataPersonalizationSharedManifest
+ _OBJC_IVAR_$_UARPEndpointLayer3._packetQueue
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationBoardID64._boardID
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationDemotionProductionMode._demotionProductionMode
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationDemotionSecurityMode._demotionSecurityMode
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationDigestListSize._digestListSize
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride._productionModeHostOverride
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride._securityModeHostOverride
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingData._matchingData
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingDataPayloadTags._payloadTags
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMax._productRevisionMax
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMin._productRevisionMin
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationMoreRequestsToFollow._moreRequestsToFollow
+ _OBJC_IVAR_$_UARPMetaDataPersonalizationSharedManifest._sharedManifest
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationBoardID64
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationDemotionProductionMode
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationDemotionSecurityMode
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationDigestListSize
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationMatchingData
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationMatchingDataPayloadTags
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMax
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMin
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationMoreRequestsToFollow
+ _OBJC_METACLASS_$_UARPMetaDataPersonalizationSharedManifest
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationBoardID64
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationDemotionProductionMode
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationDemotionSecurityMode
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationDigestListSize
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationMatchingData
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationMatchingDataPayloadTags
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationMatchingDataProductRevisionMax
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationMatchingDataProductRevisionMin
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationMoreRequestsToFollow
+ __OBJC_$_INSTANCE_METHODS_UARPMetaDataPersonalizationSharedManifest
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationBoardID64
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationDemotionProductionMode
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationDemotionSecurityMode
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationDigestListSize
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationMatchingData
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationMatchingDataPayloadTags
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationMatchingDataProductRevisionMax
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationMatchingDataProductRevisionMin
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationMoreRequestsToFollow
+ __OBJC_$_INSTANCE_VARIABLES_UARPMetaDataPersonalizationSharedManifest
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationBoardID64
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationDemotionProductionMode
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationDemotionSecurityMode
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationDigestListSize
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationMatchingData
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationMatchingDataPayloadTags
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationMatchingDataProductRevisionMax
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationMatchingDataProductRevisionMin
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationMoreRequestsToFollow
+ __OBJC_$_PROP_LIST_UARPMetaDataPersonalizationSharedManifest
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationBoardID64
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationDemotionProductionMode
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationDemotionSecurityMode
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationDigestListSize
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationMatchingData
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationMatchingDataPayloadTags
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMax
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMin
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationMoreRequestsToFollow
+ __OBJC_CLASS_RO_$_UARPMetaDataPersonalizationSharedManifest
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationBoardID64
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationDemotionProductionMode
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationDemotionSecurityMode
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationDigestListSize
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationMatchingData
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationMatchingDataPayloadTags
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMax
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMin
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationMoreRequestsToFollow
+ __OBJC_METACLASS_RO_$_UARPMetaDataPersonalizationSharedManifest
+ ___64-[UARPEndpointLayer3 packetTracking:packetDirection:inFunction:]_block_invoke
+ ___76-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:tlvs:]_block_invoke
+ ___86-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackDownstreamReachable:tlvs:]_block_invoke
+ _objc_msgSend$adjustSubfileLengthsAndOffsets
+ _objc_msgSend$data
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$demotionProductionMode
+ _objc_msgSend$demotionSecurityMode
+ _objc_msgSend$digestListSize
+ _objc_msgSend$downstreamEndpointReachable:downstreamEndpointID:tlvs:
+ _objc_msgSend$layer2CallbackDownstreamReachable:tlvs:
+ _objc_msgSend$layer3DownstreamEndpointReachable:downstreamID:tlvs:
+ _objc_msgSend$matchingData
+ _objc_msgSend$moreRequestsToFollow
+ _objc_msgSend$notifyDownstreamEndpointReachable:tlvs:
+ _objc_msgSend$packetTracking:packetDirection:inFunction:
+ _objc_msgSend$payloadTags
+ _objc_msgSend$productRevisionMax
+ _objc_msgSend$productRevisionMin
+ _objc_msgSend$productionModeHostOverride
+ _objc_msgSend$securityModeHostOverride
+ _objc_msgSend$sharedManifest
+ _objc_msgSend$updateSubfileOffset:
+ _uarpDownstreamEndpointProcessReachableMessage
+ _uarpPlatformDownstreamEndpointReachable2
+ _uarpProcessTLV2
+ _uarpProtocolSupportsDownstreamReachableTLVs
+ _uarpSendDownstreamEndpointReachable2
- -[UARPEndpointLayer3 notifyDownstreamEndpointReachable:]
- -[UARPEndpointLayer3 packetTracking:inFunction:]
- ___71-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:]_block_invoke
- ___81-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackDownstreamReachable:]_block_invoke
- _composeFTAB.paddingBytes
- _objc_msgSend$layer2CallbackDownstreamReachable:
- _objc_msgSend$layer3DownstreamEndpointReachable:downstreamID:
- _objc_msgSend$notifyDownstreamEndpointReachable:
- _objc_msgSend$packetTracking:inFunction:
- _uarpTransmitBufferUpstream
CStrings:
+ "%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: Error creating payload at index %lu"
+ "%s: Failed to create payload at index %lu"
+ "-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:tlvs:]_block_invoke"
+ "-[UARPEndpointLayer3 notifyDownstreamEndpointReachable:tlvs:]"
+ "-[UARPSuperBinaryLayer3 addPayloadWith4cc:payloadVersion:payloadIndex:]"
+ "Endpoint %@: Downstream Endpoint Reachable, ID = %u, TLVs = %@"
+ "Personalization Board ID (64 bits)"
+ "Personalization Digest List Size"
+ "Personalization FTAB Payload Production Mode Host Override"
+ "Personalization FTAB Payload Security Mode Host Override"
+ "Personalization Matching Data"
+ "Personalization Matching Data Payload Tags"
+ "Personalization Matching Data Product Revision Maximum"
+ "Personalization Matching Data Product Revision Minimum"
+ "Personalization More Requests to Follow"
+ "Personalization Payload Demotion Production Mode"
+ "Personalization Payload Demotion Security Mode"
+ "Shared Manifest"
+ "com.apple.uarp.endpoint.packet.parser"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x831"
- "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
- "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
- "%s: Padding before subfiles is off by %d bytes; adjust %d to %d"
- "%s: Padding subfile %c%c%c%c is off by %d bytes; pad from %d to %d"
- "-[UARPEndpointLayer3 downstreamEndpointReachable:downstreamEndpointID:]_block_invoke"
- "-[UARPEndpointLayer3 notifyDownstreamEndpointReachable:]"
- "Endpoint %@: Downstream Endpoint Reachable, ID = %u"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0c1"

```
