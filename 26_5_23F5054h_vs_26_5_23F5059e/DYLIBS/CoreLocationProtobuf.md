## CoreLocationProtobuf

> `/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`

```diff

-162.0.4.0.0
-  __TEXT.__text: 0x80270
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0xa154
+162.0.5.0.0
+  __TEXT.__text: 0x82860
+  __TEXT.__auth_stubs: 0x4f0
+  __TEXT.__objc_methlist: 0xa434
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x24c8
-  __TEXT.__unwind_info: 0x1800
-  __TEXT.__objc_classname: 0x9b4
-  __TEXT.__objc_methname: 0xb05e
-  __TEXT.__objc_methtype: 0x1beb
-  __TEXT.__objc_stubs: 0x2e60
-  __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x460
-  __DATA_CONST.__objc_classlist: 0x308
+  __TEXT.__cstring: 0x255b
+  __TEXT.__unwind_info: 0x1878
+  __TEXT.__objc_classname: 0x9c6
+  __TEXT.__objc_methname: 0xb3f6
+  __TEXT.__objc_methtype: 0x1ca4
+  __TEXT.__objc_stubs: 0x2fc0
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x480
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x32f0
-  __DATA_CONST.__objc_superrefs: 0x308
-  __AUTH_CONST.__auth_got: 0x248
-  __AUTH_CONST.__cfstring: 0x4320
-  __AUTH_CONST.__objc_const: 0xdc20
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xa64
+  __DATA_CONST.__objc_selrefs: 0x3408
+  __DATA_CONST.__objc_superrefs: 0x310
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__cfstring: 0x4460
+  __AUTH_CONST.__objc_const: 0xdf58
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0xa90
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x1d10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17D68959-B7F7-399B-ADD1-3F2816ACF669
-  Functions: 3474
-  Symbols:   8746
-  CStrings:  3745
+  UUID: BF99CE2E-7C3B-3120-B802-B1AF952192B1
+  Functions: 3535
+  Symbols:   8905
+  CStrings:  3820
 
Symbols:
+ +[CLPCellWifiCollectionRequest nomapMacsType]
+ +[CLPPassKitEvent associatedStoreIdsType]
+ -[CLPCellWifiCollectionRequest addNomapMacs:]
+ -[CLPCellWifiCollectionRequest clearNomapMacs]
+ -[CLPCellWifiCollectionRequest nomapMacsAtIndex:]
+ -[CLPCellWifiCollectionRequest nomapMacsCount]
+ -[CLPCellWifiCollectionRequest nomapMacs]
+ -[CLPCellWifiCollectionRequest setNomapMacs:]
+ -[CLPIndoorEvent hasPasskitEvent]
+ -[CLPIndoorEvent passkitEvent]
+ -[CLPIndoorEvent setPasskitEvent:]
+ -[CLPLocationProcessingMetadata eventTimestampIndex]
+ -[CLPLocationProcessingMetadata hasEventTimestampIndex]
+ -[CLPLocationProcessingMetadata setEventTimestampIndex:]
+ -[CLPLocationProcessingMetadata setHasEventTimestampIndex:]
+ -[CLPLocationProcessingPipelineMetadata addSegmentEventTimestamps:]
+ -[CLPLocationProcessingPipelineMetadata clearSegmentEventTimestamps]
+ -[CLPLocationProcessingPipelineMetadata dealloc]
+ -[CLPLocationProcessingPipelineMetadata segmentEventTimestampsAtIndex:]
+ -[CLPLocationProcessingPipelineMetadata segmentEventTimestampsCount]
+ -[CLPLocationProcessingPipelineMetadata segmentEventTimestamps]
+ -[CLPLocationProcessingPipelineMetadata setSegmentEventTimestamps:count:]
+ -[CLPPassKitEvent .cxx_destruct]
+ -[CLPPassKitEvent StringAsEventType:]
+ -[CLPPassKitEvent addAssociatedStoreIds:]
+ -[CLPPassKitEvent associatedStoreIdsAtIndex:]
+ -[CLPPassKitEvent associatedStoreIdsCount]
+ -[CLPPassKitEvent associatedStoreIds]
+ -[CLPPassKitEvent clearAssociatedStoreIds]
+ -[CLPPassKitEvent copyTo:]
+ -[CLPPassKitEvent copyWithZone:]
+ -[CLPPassKitEvent description]
+ -[CLPPassKitEvent dictionaryRepresentation]
+ -[CLPPassKitEvent eventTypeAsString:]
+ -[CLPPassKitEvent eventType]
+ -[CLPPassKitEvent hasEventType]
+ -[CLPPassKitEvent hasMuid]
+ -[CLPPassKitEvent hasProviderIdentifier]
+ -[CLPPassKitEvent hasTimestamp]
+ -[CLPPassKitEvent hasTransactionDate]
+ -[CLPPassKitEvent hash]
+ -[CLPPassKitEvent isEqual:]
+ -[CLPPassKitEvent mergeFrom:]
+ -[CLPPassKitEvent muid]
+ -[CLPPassKitEvent providerIdentifier]
+ -[CLPPassKitEvent readFrom:]
+ -[CLPPassKitEvent setAssociatedStoreIds:]
+ -[CLPPassKitEvent setEventType:]
+ -[CLPPassKitEvent setHasEventType:]
+ -[CLPPassKitEvent setHasMuid:]
+ -[CLPPassKitEvent setHasProviderIdentifier:]
+ -[CLPPassKitEvent setHasTimestamp:]
+ -[CLPPassKitEvent setHasTransactionDate:]
+ -[CLPPassKitEvent setMuid:]
+ -[CLPPassKitEvent setProviderIdentifier:]
+ -[CLPPassKitEvent setTimestamp:]
+ -[CLPPassKitEvent setTransactionDate:]
+ -[CLPPassKitEvent timestamp]
+ -[CLPPassKitEvent transactionDate]
+ -[CLPPassKitEvent writeTo:]
+ OBJC_IVAR_$_CLPCellWifiCollectionRequest._nomapMacs
+ OBJC_IVAR_$_CLPIndoorEvent._passkitEvent
+ OBJC_IVAR_$_CLPLocationProcessingMetadata._eventTimestampIndex
+ OBJC_IVAR_$_CLPLocationProcessingPipelineMetadata._segmentEventTimestamps
+ OBJC_IVAR_$_CLPPassKitEvent._associatedStoreIds
+ OBJC_IVAR_$_CLPPassKitEvent._eventType
+ OBJC_IVAR_$_CLPPassKitEvent._has
+ OBJC_IVAR_$_CLPPassKitEvent._muid
+ OBJC_IVAR_$_CLPPassKitEvent._providerIdentifier
+ OBJC_IVAR_$_CLPPassKitEvent._timestamp
+ OBJC_IVAR_$_CLPPassKitEvent._transactionDate
+ _CLPPassKitEventReadFrom
+ _OBJC_CLASS_$_CLPPassKitEvent
+ _OBJC_METACLASS_$_CLPPassKitEvent
+ _PBRepeatedInt64Add
+ _PBRepeatedInt64Clear
+ _PBRepeatedInt64Copy
+ _PBRepeatedInt64Hash
+ _PBRepeatedInt64IsEqual
+ _PBRepeatedInt64NSArray
+ _PBRepeatedInt64Set
+ __OBJC_$_CLASS_METHODS_CLPPassKitEvent
+ __OBJC_$_INSTANCE_METHODS_CLPPassKitEvent
+ __OBJC_$_INSTANCE_VARIABLES_CLPPassKitEvent
+ __OBJC_$_PROP_LIST_CLPPassKitEvent
+ __OBJC_CLASS_PROTOCOLS_$_CLPPassKitEvent
+ __OBJC_CLASS_RO_$_CLPPassKitEvent
+ __OBJC_METACLASS_RO_$_CLPPassKitEvent
+ _objc_msgSend$addAssociatedStoreIds:
+ _objc_msgSend$addNomapMacs:
+ _objc_msgSend$addSegmentEventTimestamps:
+ _objc_msgSend$associatedStoreIdsAtIndex:
+ _objc_msgSend$clearNomapMacs
+ _objc_msgSend$clearSegmentEventTimestamps
+ _objc_msgSend$nomapMacsAtIndex:
+ _objc_msgSend$nomapMacsCount
+ _objc_msgSend$segmentEventTimestampsAtIndex:
+ _objc_msgSend$segmentEventTimestampsCount
+ _objc_msgSend$setPasskitEvent:
CStrings:
+ "2"
+ "@\"CLPPassKitEvent\""
+ "CLPPassKitEvent"
+ "PassKitEvent"
+ "PassUsage"
+ "PaymentUsage"
+ "StringAsEventType:"
+ "T@\"CLPPassKitEvent\",&,N,V_passkitEvent"
+ "T@\"NSMutableArray\",&,N,V_nomapMacs"
+ "T^q,R,N"
+ "Td,N,V_transactionDate"
+ "Ti,N,V_eventTimestampIndex"
+ "Ti,N,V_eventType"
+ "^q16@0:8"
+ "_eventTimestampIndex"
+ "_eventType"
+ "_nomapMacs"
+ "_passkitEvent"
+ "_segmentEventTimestamps"
+ "_transactionDate"
+ "addAssociatedStoreIds:"
+ "addNomapMacs:"
+ "addSegmentEventTimestamps:"
+ "associatedStoreIdsAtIndex:"
+ "associatedStoreIdsType"
+ "clearNomapMacs"
+ "clearSegmentEventTimestamps"
+ "eventTimestampIndex"
+ "eventType"
+ "eventTypeAsString:"
+ "hasEventTimestampIndex"
+ "hasEventType"
+ "hasMuid"
+ "hasPasskitEvent"
+ "hasTransactionDate"
+ "nomapMacs"
+ "nomapMacsAtIndex:"
+ "nomapMacsCount"
+ "nomapMacsType"
+ "passkitEvent"
+ "q24@0:8Q16"
+ "segmentEventTimestamps"
+ "segmentEventTimestampsAtIndex:"
+ "segmentEventTimestampsCount"
+ "setEventTimestampIndex:"
+ "setEventType:"
+ "setHasEventTimestampIndex:"
+ "setHasEventType:"
+ "setHasMuid:"
+ "setHasTransactionDate:"
+ "setNomapMacs:"
+ "setPasskitEvent:"
+ "setSegmentEventTimestamps:count:"
+ "setTransactionDate:"
+ "transactionDate"
+ "v32@0:8^q16Q24"
+ "{?=\"eventTimestampIndex\"b1\"tripSourceType\"b1}"
+ "{?=\"list\"^q\"count\"Q\"size\"Q}"
+ "{?=\"muid\"b1\"timestamp\"b1\"transactionDate\"b1\"eventType\"b1\"providerIdentifier\"b1}"
- "{?=\"tripSourceType\"b1}"

```
