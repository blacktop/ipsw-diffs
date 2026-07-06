## libAppleTconUARPUpdater.dylib

> `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

```diff

-  __TEXT.__text: 0x42d68
-  __TEXT.__objc_methlist: 0x43dc
-  __TEXT.__cstring: 0x3ee6
+  __TEXT.__text: 0x45944
+  __TEXT.__objc_methlist: 0x47cc
+  __TEXT.__cstring: 0x40f2
   __TEXT.__const: 0xa0
-  __TEXT.__oslogstring: 0x1401
+  __TEXT.__oslogstring: 0x13a8
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x12d0
+  __TEXT.__unwind_info: 0x13d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa00
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __DATA_CONST.__objc_classlist: 0x518
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10f0
-  __DATA_CONST.__objc_superrefs: 0x4b8
-  __DATA_CONST.__got: 0x588
+  __DATA_CONST.__objc_selrefs: 0x1160
+  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__got: 0x5e8
   __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0x33e0
-  __AUTH_CONST.__objc_const: 0x9528
+  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__objc_const: 0x9ee8
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x2f30
-  __DATA.__objc_ivar: 0x4d4
+  __AUTH.__objc_data: 0x32f0
+  __DATA.__objc_ivar: 0x504
   __DATA.__data: 0x125
-  __DATA.__bss: 0x1168
+  __DATA.__bss: 0x1160
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1860
-  Symbols:   3889
-  CStrings:  1146
+  Functions: 1942
+  Symbols:   4079
+  CStrings:  1169
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Symbols:
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
+ OBJC_IVAR_$_UARPMetaDataPersonalizationBoardID64._boardID
+ OBJC_IVAR_$_UARPMetaDataPersonalizationDemotionProductionMode._demotionProductionMode
+ OBJC_IVAR_$_UARPMetaDataPersonalizationDemotionSecurityMode._demotionSecurityMode
+ OBJC_IVAR_$_UARPMetaDataPersonalizationDigestListSize._digestListSize
+ OBJC_IVAR_$_UARPMetaDataPersonalizationFTABPayloadProductionModeHostOverride._productionModeHostOverride
+ OBJC_IVAR_$_UARPMetaDataPersonalizationFTABPayloadSecurityModeHostOverride._securityModeHostOverride
+ OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingData._matchingData
+ OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingDataPayloadTags._payloadTags
+ OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMax._productRevisionMax
+ OBJC_IVAR_$_UARPMetaDataPersonalizationMatchingDataProductRevisionMin._productRevisionMin
+ OBJC_IVAR_$_UARPMetaDataPersonalizationMoreRequestsToFollow._moreRequestsToFollow
+ OBJC_IVAR_$_UARPMetaDataPersonalizationSharedManifest._sharedManifest
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
+ _objc_msgSend$adjustSubfileLengthsAndOffsets
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$demotionProductionMode
+ _objc_msgSend$demotionSecurityMode
+ _objc_msgSend$digestListSize
+ _objc_msgSend$matchingData
+ _objc_msgSend$moreRequestsToFollow
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
- _uarpTransmitBufferUpstream
- composeFTAB.paddingBytes
CStrings:
+ "%s: ESPRESSO: Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
+ "%s: Failed to create payload at index %lu"
+ "-[UARPSuperBinaryLayer3 addPayloadWith4cc:payloadVersion:payloadIndex:]"
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
- "%s: ESPRESSO:Bonus Message <type=0x%04x, length=x0x%04x, id=0x%04x>"
- "%s: ESPRESSO:Message <type=0x%04x, id=0x%04x> Length too big ! expected <%u>, got <%u>"
- "%s: Padding before subfiles is off by %d bytes; adjust %d to %d"
- "%s: Padding subfile %c%c%c%c is off by %d bytes; pad from %d to %d"

```
