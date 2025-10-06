## CoreLocationProtobuf

> `/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`

```diff

-159.0.0.0.0
-  __TEXT.__text: 0x66bb4
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x91ac
+160.0.2.0.0
+  __TEXT.__text: 0x68d50
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_methlist: 0x9484
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x21c8
-  __TEXT.__unwind_info: 0x119c
-  __TEXT.__objc_classname: 0x8f4
-  __TEXT.__objc_methname: 0xa58f
-  __TEXT.__objc_methtype: 0x1919
-  __TEXT.__objc_stubs: 0x2b20
+  __TEXT.__cstring: 0x22e5
+  __TEXT.__unwind_info: 0x11dc
+  __TEXT.__objc_classname: 0x905
+  __TEXT.__objc_methname: 0xa73b
+  __TEXT.__objc_methtype: 0x1a49
+  __TEXT.__objc_stubs: 0x2b40
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa580
-  __DATA_CONST.__objc_selrefs: 0x2fa0
-  __AUTH_CONST.__cfstring: 0x3de0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x240
-  __DATA.__objc_classrefs: 0x268
-  __DATA.__objc_superrefs: 0x2b8
-  __DATA.__objc_ivar: 0x954
+  __DATA_CONST.__objc_const: 0xa910
+  __DATA_CONST.__objc_selrefs: 0x2ff8
+  __AUTH_CONST.__cfstring: 0x3f60
+  __AUTH_CONST.__objc_const: 0x48
+  __AUTH_CONST.__auth_got: 0x248
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_classrefs: 0x270
+  __DATA.__objc_superrefs: 0x2c0
+  __DATA.__objc_ivar: 0x988
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_const: 0x2010
   __DATA_DIRTY.__objc_data: 0x1b30

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27C62D6D-38B3-3B72-BB26-6C8AC9AAE5C4
-  Functions: 3167
-  Symbols:   7918
-  CStrings:  3503
+  UUID: 18AB7D0E-EF2A-3508-9DED-C34F01C76739
+  Functions: 3229
+  Symbols:   8062
+  CStrings:  3548
 
Symbols:
+ -[CLPCellTowerLocation hasHasWifiFallback]
+ -[CLPCellTowerLocation hasUniqueCount]
+ -[CLPCellTowerLocation hasWifiFallback]
+ -[CLPCellTowerLocation setHasHasWifiFallback:]
+ -[CLPCellTowerLocation setHasUniqueCount:]
+ -[CLPCellTowerLocation setHasWifiFallback:]
+ -[CLPCellTowerLocation setUniqueCount:]
+ -[CLPCellTowerLocation uniqueCount]
+ -[CLPIndoorEvent hasOutdoorUpdate]
+ -[CLPIndoorEvent outdoorUpdate]
+ -[CLPIndoorEvent setOutdoorUpdate:]
+ -[CLPLteCellTowerLocation hasHasWifiFallback]
+ -[CLPLteCellTowerLocation hasUniqueCount]
+ -[CLPLteCellTowerLocation hasWifiFallback]
+ -[CLPLteCellTowerLocation setHasHasWifiFallback:]
+ -[CLPLteCellTowerLocation setHasUniqueCount:]
+ -[CLPLteCellTowerLocation setHasWifiFallback:]
+ -[CLPLteCellTowerLocation setUniqueCount:]
+ -[CLPLteCellTowerLocation uniqueCount]
+ -[CLPNRCellTowerLocation hasHasWifiFallback]
+ -[CLPNRCellTowerLocation hasUniqueCount]
+ -[CLPNRCellTowerLocation hasWifiFallback]
+ -[CLPNRCellTowerLocation setHasHasWifiFallback:]
+ -[CLPNRCellTowerLocation setHasUniqueCount:]
+ -[CLPNRCellTowerLocation setHasWifiFallback:]
+ -[CLPNRCellTowerLocation setUniqueCount:]
+ -[CLPNRCellTowerLocation uniqueCount]
+ -[CLPOutdoorUpdate StringAsConfidence:]
+ -[CLPOutdoorUpdate StringAsType:]
+ -[CLPOutdoorUpdate confidenceAsString:]
+ -[CLPOutdoorUpdate confidence]
+ -[CLPOutdoorUpdate copyTo:]
+ -[CLPOutdoorUpdate copyWithZone:]
+ -[CLPOutdoorUpdate description]
+ -[CLPOutdoorUpdate dictionaryRepresentation]
+ -[CLPOutdoorUpdate estimatedStateProbabilityOutdoor]
+ -[CLPOutdoorUpdate hasConfidence]
+ -[CLPOutdoorUpdate hasEstimatedStateProbabilityOutdoor]
+ -[CLPOutdoorUpdate hasMctTimestamp]
+ -[CLPOutdoorUpdate hasTimestamp]
+ -[CLPOutdoorUpdate hasType]
+ -[CLPOutdoorUpdate hash]
+ -[CLPOutdoorUpdate isEqual:]
+ -[CLPOutdoorUpdate mctTimestamp]
+ -[CLPOutdoorUpdate mergeFrom:]
+ -[CLPOutdoorUpdate readFrom:]
+ -[CLPOutdoorUpdate setConfidence:]
+ -[CLPOutdoorUpdate setEstimatedStateProbabilityOutdoor:]
+ -[CLPOutdoorUpdate setHasConfidence:]
+ -[CLPOutdoorUpdate setHasEstimatedStateProbabilityOutdoor:]
+ -[CLPOutdoorUpdate setHasMctTimestamp:]
+ -[CLPOutdoorUpdate setHasTimestamp:]
+ -[CLPOutdoorUpdate setHasType:]
+ -[CLPOutdoorUpdate setMctTimestamp:]
+ -[CLPOutdoorUpdate setTimestamp:]
+ -[CLPOutdoorUpdate setType:]
+ -[CLPOutdoorUpdate timestamp]
+ -[CLPOutdoorUpdate typeAsString:]
+ -[CLPOutdoorUpdate type]
+ -[CLPOutdoorUpdate writeTo:]
+ OBJC_IVAR_$_CLPCellTowerLocation._hasWifiFallback
+ OBJC_IVAR_$_CLPCellTowerLocation._uniqueCount
+ OBJC_IVAR_$_CLPIndoorEvent._outdoorUpdate
+ OBJC_IVAR_$_CLPLteCellTowerLocation._hasWifiFallback
+ OBJC_IVAR_$_CLPLteCellTowerLocation._uniqueCount
+ OBJC_IVAR_$_CLPNRCellTowerLocation._hasWifiFallback
+ OBJC_IVAR_$_CLPNRCellTowerLocation._uniqueCount
+ OBJC_IVAR_$_CLPOutdoorUpdate._confidence
+ OBJC_IVAR_$_CLPOutdoorUpdate._estimatedStateProbabilityOutdoor
+ OBJC_IVAR_$_CLPOutdoorUpdate._has
+ OBJC_IVAR_$_CLPOutdoorUpdate._mctTimestamp
+ OBJC_IVAR_$_CLPOutdoorUpdate._timestamp
+ OBJC_IVAR_$_CLPOutdoorUpdate._type
+ _CLPOutdoorUpdateReadFrom
+ _OBJC_CLASS_$_CLPOutdoorUpdate
+ _OBJC_METACLASS_$_CLPOutdoorUpdate
+ __OBJC_$_INSTANCE_METHODS_CLPOutdoorUpdate
+ __OBJC_$_INSTANCE_VARIABLES_CLPOutdoorUpdate
+ __OBJC_$_PROP_LIST_CLPOutdoorUpdate
+ __OBJC_CLASS_PROTOCOLS_$_CLPOutdoorUpdate
+ __OBJC_CLASS_RO_$_CLPOutdoorUpdate
+ __OBJC_METACLASS_RO_$_CLPOutdoorUpdate
+ _objc_msgSend$setOutdoorUpdate:
+ _objc_retainAutoreleaseReturnValue
CStrings:
+ "\b\x14"
+ "@\"CLPOutdoorUpdate\""
+ "CLPOutdoorUpdate"
+ "IndoorOutdoorConfidenceHigh"
+ "IndoorOutdoorConfidenceLow"
+ "IndoorOutdoorConfidenceMedium"
+ "IndoorOutdoorConfidenceUnknown"
+ "IndoorOutdoorTypeIndoor"
+ "IndoorOutdoorTypeMax"
+ "IndoorOutdoorTypeOutdoor"
+ "IndoorOutdoorTypeUnknown"
+ "OutdoorUpdate"
+ "T@\"CLPOutdoorUpdate\",&,N,V_outdoorUpdate"
+ "Td,N,V_estimatedStateProbabilityOutdoor"
+ "Td,N,V_mctTimestamp"
+ "_estimatedStateProbabilityOutdoor"
+ "_mctTimestamp"
+ "_outdoorUpdate"
+ "estimatedStateProbabilityOutdoor"
+ "hasEstimatedStateProbabilityOutdoor"
+ "hasMctTimestamp"
+ "hasOutdoorUpdate"
+ "mctTimestamp"
+ "outdoorUpdate"
+ "setEstimatedStateProbabilityOutdoor:"
+ "setHasEstimatedStateProbabilityOutdoor:"
+ "setHasMctTimestamp:"
+ "setMctTimestamp:"
+ "setOutdoorUpdate:"
+ "{?=\"arfcn\"b1\"ecn0\"b1\"psc\"b1\"rat\"b1\"rscp\"b1\"serverHash\"b1\"transmit\"b1\"hasWifiFallback\"b1\"isLimitedService\"b1\"uniqueCount\"b1}"
+ "{?=\"cellLatitude\"b1\"cellLongitude\"b1\"bandInfo\"b1\"bandwidth\"b1\"csgId\"b1\"csgIndication\"b1\"deploymentType\"b1\"downlinkBandwidth\"b1\"ecn0\"b1\"latency\"b1\"maxThroughput\"b1\"pid\"b1\"pmax\"b1\"rscp\"b1\"rssi\"b1\"serverHash\"b1\"timingAdvance\"b1\"uarfcn\"b1\"hasWifiFallback\"b1\"isLimitedService\"b1\"isStalled\"b1\"uniqueCount\"b1}"
+ "{?=\"cellLatitude\"b1\"cellLongitude\"b1\"ci\"b1\"bandInfo\"b1\"bandwidth\"b1\"bwpSupport\"b1\"downlinkBandwidth\"b1\"ecn0\"b1\"gscn\"b1\"latency\"b1\"maxThroughput\"b1\"mcc\"b1\"mnc\"b1\"nrarfcn\"b1\"pid\"b1\"pmax\"b1\"rscp\"b1\"rssi\"b1\"scs\"b1\"serverHash\"b1\"tac\"b1\"timingAdvance\"b1\"hasWifiFallback\"b1\"isLimitedService\"b1\"isStalled\"b1\"uniqueCount\"b1}"
+ "{?=\"estimatedStateProbabilityOutdoor\"b1\"mctTimestamp\"b1\"timestamp\"b1\"confidence\"b1\"type\"b1}"
- "\a\x14"
- "{?=\"cellLatitude\"b1\"cellLongitude\"b1\"bandInfo\"b1\"bandwidth\"b1\"csgId\"b1\"csgIndication\"b1\"deploymentType\"b1\"downlinkBandwidth\"b1\"ecn0\"b1\"latency\"b1\"maxThroughput\"b1\"pid\"b1\"pmax\"b1\"rscp\"b1\"rssi\"b1\"serverHash\"b1\"timingAdvance\"b1\"uarfcn\"b1\"isLimitedService\"b1\"isStalled\"b1}"
- "{?=\"cellLatitude\"b1\"cellLongitude\"b1\"ci\"b1\"bandInfo\"b1\"bandwidth\"b1\"bwpSupport\"b1\"downlinkBandwidth\"b1\"ecn0\"b1\"gscn\"b1\"latency\"b1\"maxThroughput\"b1\"mcc\"b1\"mnc\"b1\"nrarfcn\"b1\"pid\"b1\"pmax\"b1\"rscp\"b1\"rssi\"b1\"scs\"b1\"serverHash\"b1\"tac\"b1\"timingAdvance\"b1\"isLimitedService\"b1\"isStalled\"b1}"

```
