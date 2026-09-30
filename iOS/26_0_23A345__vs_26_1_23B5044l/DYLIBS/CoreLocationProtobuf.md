## CoreLocationProtobuf

> `/System/Library/PrivateFrameworks/CoreLocationProtobuf.framework/CoreLocationProtobuf`

```diff

-160.0.9.0.0
-  __TEXT.__text: 0x75c58
+162.0.4.0.0
+  __TEXT.__text: 0x7bc28
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x9934
+  __TEXT.__objc_methlist: 0xa154
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x2451
-  __TEXT.__unwind_info: 0x1188
-  __TEXT.__objc_classname: 0x947
-  __TEXT.__objc_methname: 0xadcb
-  __TEXT.__objc_methtype: 0x1ae0
-  __TEXT.__objc_stubs: 0x2da0
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x438
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __TEXT.__cstring: 0x24c8
+  __TEXT.__unwind_info: 0x1268
+  __TEXT.__objc_classname: 0x9b4
+  __TEXT.__objc_methname: 0xb05e
+  __TEXT.__objc_methtype: 0x1beb
+  __TEXT.__objc_stubs: 0x2e60
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0x460
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31f0
-  __DATA_CONST.__objc_superrefs: 0x2d8
+  __DATA_CONST.__objc_selrefs: 0x32f0
+  __DATA_CONST.__objc_superrefs: 0x308
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__cfstring: 0x41a0
-  __AUTH_CONST.__objc_const: 0xcfd0
-  __DATA.__objc_ivar: 0x9d8
+  __AUTH_CONST.__cfstring: 0x4320
+  __AUTH_CONST.__objc_const: 0xdc20
+  __AUTH.__objc_data: 0x1e0
+  __DATA.__objc_ivar: 0xa64
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x1c70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24998745-75F1-3E32-8493-165CB25D0C87
-  Functions: 3292
-  Symbols:   8311
-  CStrings:  3659
+  UUID: 52444ECD-0E69-36BA-8B88-8F94AD95C60B
+  Functions: 3465
+  Symbols:   8740
+  CStrings:  3745
 
Symbols:
+ -[CLPCdmaCellTower bsid]
+ -[CLPCdmaCellTower copyTo:]
+ -[CLPCdmaCellTower copyWithZone:]
+ -[CLPCdmaCellTower description]
+ -[CLPCdmaCellTower dictionaryRepresentation]
+ -[CLPCdmaCellTower hasBsid]
+ -[CLPCdmaCellTower hasMcc]
+ -[CLPCdmaCellTower hasMnc]
+ -[CLPCdmaCellTower hasNid]
+ -[CLPCdmaCellTower hasSid]
+ -[CLPCdmaCellTower hash]
+ -[CLPCdmaCellTower isEqual:]
+ -[CLPCdmaCellTower mcc]
+ -[CLPCdmaCellTower mergeFrom:]
+ -[CLPCdmaCellTower mnc]
+ -[CLPCdmaCellTower nid]
+ -[CLPCdmaCellTower readFrom:]
+ -[CLPCdmaCellTower setBsid:]
+ -[CLPCdmaCellTower setHasBsid:]
+ -[CLPCdmaCellTower setHasMcc:]
+ -[CLPCdmaCellTower setHasMnc:]
+ -[CLPCdmaCellTower setHasNid:]
+ -[CLPCdmaCellTower setHasSid:]
+ -[CLPCdmaCellTower setMcc:]
+ -[CLPCdmaCellTower setMnc:]
+ -[CLPCdmaCellTower setNid:]
+ -[CLPCdmaCellTower setSid:]
+ -[CLPCdmaCellTower sid]
+ -[CLPCdmaCellTower writeTo:]
+ -[CLPCellConnectivityInfo .cxx_destruct]
+ -[CLPCellConnectivityInfo StringAsConnectionStatus:]
+ -[CLPCellConnectivityInfo cdma]
+ -[CLPCellConnectivityInfo connectionStatusAsString:]
+ -[CLPCellConnectivityInfo connectionStatus]
+ -[CLPCellConnectivityInfo copyTo:]
+ -[CLPCellConnectivityInfo copyWithZone:]
+ -[CLPCellConnectivityInfo description]
+ -[CLPCellConnectivityInfo dictionaryRepresentation]
+ -[CLPCellConnectivityInfo gsm]
+ -[CLPCellConnectivityInfo hasCdma]
+ -[CLPCellConnectivityInfo hasConnectionStatus]
+ -[CLPCellConnectivityInfo hasGsm]
+ -[CLPCellConnectivityInfo hasLte]
+ -[CLPCellConnectivityInfo hasNr]
+ -[CLPCellConnectivityInfo hasScdma]
+ -[CLPCellConnectivityInfo hasTimestamp]
+ -[CLPCellConnectivityInfo hash]
+ -[CLPCellConnectivityInfo isEqual:]
+ -[CLPCellConnectivityInfo lte]
+ -[CLPCellConnectivityInfo mergeFrom:]
+ -[CLPCellConnectivityInfo nr]
+ -[CLPCellConnectivityInfo readFrom:]
+ -[CLPCellConnectivityInfo scdma]
+ -[CLPCellConnectivityInfo setCdma:]
+ -[CLPCellConnectivityInfo setConnectionStatus:]
+ -[CLPCellConnectivityInfo setGsm:]
+ -[CLPCellConnectivityInfo setHasConnectionStatus:]
+ -[CLPCellConnectivityInfo setHasTimestamp:]
+ -[CLPCellConnectivityInfo setLte:]
+ -[CLPCellConnectivityInfo setNr:]
+ -[CLPCellConnectivityInfo setScdma:]
+ -[CLPCellConnectivityInfo setTimestamp:]
+ -[CLPCellConnectivityInfo timestamp]
+ -[CLPCellConnectivityInfo writeTo:]
+ -[CLPGsmCellTower ci]
+ -[CLPGsmCellTower copyTo:]
+ -[CLPGsmCellTower copyWithZone:]
+ -[CLPGsmCellTower description]
+ -[CLPGsmCellTower dictionaryRepresentation]
+ -[CLPGsmCellTower hasCi]
+ -[CLPGsmCellTower hasLac]
+ -[CLPGsmCellTower hasMcc]
+ -[CLPGsmCellTower hasMnc]
+ -[CLPGsmCellTower hash]
+ -[CLPGsmCellTower isEqual:]
+ -[CLPGsmCellTower lac]
+ -[CLPGsmCellTower mcc]
+ -[CLPGsmCellTower mergeFrom:]
+ -[CLPGsmCellTower mnc]
+ -[CLPGsmCellTower readFrom:]
+ -[CLPGsmCellTower setCi:]
+ -[CLPGsmCellTower setHasCi:]
+ -[CLPGsmCellTower setHasLac:]
+ -[CLPGsmCellTower setHasMcc:]
+ -[CLPGsmCellTower setHasMnc:]
+ -[CLPGsmCellTower setLac:]
+ -[CLPGsmCellTower setMcc:]
+ -[CLPGsmCellTower setMnc:]
+ -[CLPGsmCellTower writeTo:]
+ -[CLPIndoorEvent cellConnectivity]
+ -[CLPIndoorEvent hasCellConnectivity]
+ -[CLPIndoorEvent setCellConnectivity:]
+ -[CLPLteCellTower ci]
+ -[CLPLteCellTower copyTo:]
+ -[CLPLteCellTower copyWithZone:]
+ -[CLPLteCellTower description]
+ -[CLPLteCellTower dictionaryRepresentation]
+ -[CLPLteCellTower hasCi]
+ -[CLPLteCellTower hasMcc]
+ -[CLPLteCellTower hasMnc]
+ -[CLPLteCellTower hasTac]
+ -[CLPLteCellTower hash]
+ -[CLPLteCellTower isEqual:]
+ -[CLPLteCellTower mcc]
+ -[CLPLteCellTower mergeFrom:]
+ -[CLPLteCellTower mnc]
+ -[CLPLteCellTower readFrom:]
+ -[CLPLteCellTower setCi:]
+ -[CLPLteCellTower setHasCi:]
+ -[CLPLteCellTower setHasMcc:]
+ -[CLPLteCellTower setHasMnc:]
+ -[CLPLteCellTower setHasTac:]
+ -[CLPLteCellTower setMcc:]
+ -[CLPLteCellTower setMnc:]
+ -[CLPLteCellTower setTac:]
+ -[CLPLteCellTower tac]
+ -[CLPLteCellTower writeTo:]
+ -[CLPNrCellTower ci]
+ -[CLPNrCellTower copyTo:]
+ -[CLPNrCellTower copyWithZone:]
+ -[CLPNrCellTower description]
+ -[CLPNrCellTower dictionaryRepresentation]
+ -[CLPNrCellTower hasCi]
+ -[CLPNrCellTower hasMcc]
+ -[CLPNrCellTower hasMnc]
+ -[CLPNrCellTower hasTac]
+ -[CLPNrCellTower hash]
+ -[CLPNrCellTower isEqual:]
+ -[CLPNrCellTower mcc]
+ -[CLPNrCellTower mergeFrom:]
+ -[CLPNrCellTower mnc]
+ -[CLPNrCellTower readFrom:]
+ -[CLPNrCellTower setCi:]
+ -[CLPNrCellTower setHasCi:]
+ -[CLPNrCellTower setHasMcc:]
+ -[CLPNrCellTower setHasMnc:]
+ -[CLPNrCellTower setHasTac:]
+ -[CLPNrCellTower setMcc:]
+ -[CLPNrCellTower setMnc:]
+ -[CLPNrCellTower setTac:]
+ -[CLPNrCellTower tac]
+ -[CLPNrCellTower writeTo:]
+ -[CLPScdmaCellTower ci]
+ -[CLPScdmaCellTower copyTo:]
+ -[CLPScdmaCellTower copyWithZone:]
+ -[CLPScdmaCellTower description]
+ -[CLPScdmaCellTower dictionaryRepresentation]
+ -[CLPScdmaCellTower hasCi]
+ -[CLPScdmaCellTower hasLac]
+ -[CLPScdmaCellTower hasMcc]
+ -[CLPScdmaCellTower hasMnc]
+ -[CLPScdmaCellTower hash]
+ -[CLPScdmaCellTower isEqual:]
+ -[CLPScdmaCellTower lac]
+ -[CLPScdmaCellTower mcc]
+ -[CLPScdmaCellTower mergeFrom:]
+ -[CLPScdmaCellTower mnc]
+ -[CLPScdmaCellTower readFrom:]
+ -[CLPScdmaCellTower setCi:]
+ -[CLPScdmaCellTower setHasCi:]
+ -[CLPScdmaCellTower setHasLac:]
+ -[CLPScdmaCellTower setHasMcc:]
+ -[CLPScdmaCellTower setHasMnc:]
+ -[CLPScdmaCellTower setLac:]
+ -[CLPScdmaCellTower setMcc:]
+ -[CLPScdmaCellTower setMnc:]
+ -[CLPScdmaCellTower writeTo:]
+ OBJC_IVAR_$_CLPCdmaCellTower._bsid
+ OBJC_IVAR_$_CLPCdmaCellTower._has
+ OBJC_IVAR_$_CLPCdmaCellTower._mcc
+ OBJC_IVAR_$_CLPCdmaCellTower._mnc
+ OBJC_IVAR_$_CLPCdmaCellTower._nid
+ OBJC_IVAR_$_CLPCdmaCellTower._sid
+ OBJC_IVAR_$_CLPCellConnectivityInfo._cdma
+ OBJC_IVAR_$_CLPCellConnectivityInfo._connectionStatus
+ OBJC_IVAR_$_CLPCellConnectivityInfo._gsm
+ OBJC_IVAR_$_CLPCellConnectivityInfo._has
+ OBJC_IVAR_$_CLPCellConnectivityInfo._lte
+ OBJC_IVAR_$_CLPCellConnectivityInfo._nr
+ OBJC_IVAR_$_CLPCellConnectivityInfo._scdma
+ OBJC_IVAR_$_CLPCellConnectivityInfo._timestamp
+ OBJC_IVAR_$_CLPGsmCellTower._ci
+ OBJC_IVAR_$_CLPGsmCellTower._has
+ OBJC_IVAR_$_CLPGsmCellTower._lac
+ OBJC_IVAR_$_CLPGsmCellTower._mcc
+ OBJC_IVAR_$_CLPGsmCellTower._mnc
+ OBJC_IVAR_$_CLPIndoorEvent._cellConnectivity
+ OBJC_IVAR_$_CLPLteCellTower._ci
+ OBJC_IVAR_$_CLPLteCellTower._has
+ OBJC_IVAR_$_CLPLteCellTower._mcc
+ OBJC_IVAR_$_CLPLteCellTower._mnc
+ OBJC_IVAR_$_CLPLteCellTower._tac
+ OBJC_IVAR_$_CLPNrCellTower._ci
+ OBJC_IVAR_$_CLPNrCellTower._has
+ OBJC_IVAR_$_CLPNrCellTower._mcc
+ OBJC_IVAR_$_CLPNrCellTower._mnc
+ OBJC_IVAR_$_CLPNrCellTower._tac
+ OBJC_IVAR_$_CLPScdmaCellTower._ci
+ OBJC_IVAR_$_CLPScdmaCellTower._has
+ OBJC_IVAR_$_CLPScdmaCellTower._lac
+ OBJC_IVAR_$_CLPScdmaCellTower._mcc
+ OBJC_IVAR_$_CLPScdmaCellTower._mnc
+ _CLPCdmaCellTowerReadFrom
+ _CLPCellConnectivityInfoReadFrom
+ _CLPGsmCellTowerReadFrom
+ _CLPLteCellTowerReadFrom
+ _CLPNrCellTowerReadFrom
+ _CLPScdmaCellTowerReadFrom
+ _OBJC_CLASS_$_CLPCdmaCellTower
+ _OBJC_CLASS_$_CLPCellConnectivityInfo
+ _OBJC_CLASS_$_CLPGsmCellTower
+ _OBJC_CLASS_$_CLPLteCellTower
+ _OBJC_CLASS_$_CLPNrCellTower
+ _OBJC_CLASS_$_CLPScdmaCellTower
+ _OBJC_METACLASS_$_CLPCdmaCellTower
+ _OBJC_METACLASS_$_CLPCellConnectivityInfo
+ _OBJC_METACLASS_$_CLPGsmCellTower
+ _OBJC_METACLASS_$_CLPLteCellTower
+ _OBJC_METACLASS_$_CLPNrCellTower
+ _OBJC_METACLASS_$_CLPScdmaCellTower
+ __OBJC_$_INSTANCE_METHODS_CLPCdmaCellTower
+ __OBJC_$_INSTANCE_METHODS_CLPCellConnectivityInfo
+ __OBJC_$_INSTANCE_METHODS_CLPGsmCellTower
+ __OBJC_$_INSTANCE_METHODS_CLPLteCellTower
+ __OBJC_$_INSTANCE_METHODS_CLPNrCellTower
+ __OBJC_$_INSTANCE_METHODS_CLPScdmaCellTower
+ __OBJC_$_INSTANCE_VARIABLES_CLPCdmaCellTower
+ __OBJC_$_INSTANCE_VARIABLES_CLPCellConnectivityInfo
+ __OBJC_$_INSTANCE_VARIABLES_CLPGsmCellTower
+ __OBJC_$_INSTANCE_VARIABLES_CLPLteCellTower
+ __OBJC_$_INSTANCE_VARIABLES_CLPNrCellTower
+ __OBJC_$_INSTANCE_VARIABLES_CLPScdmaCellTower
+ __OBJC_$_PROP_LIST_CLPCdmaCellTower
+ __OBJC_$_PROP_LIST_CLPCellConnectivityInfo
+ __OBJC_$_PROP_LIST_CLPGsmCellTower
+ __OBJC_$_PROP_LIST_CLPLteCellTower
+ __OBJC_$_PROP_LIST_CLPNrCellTower
+ __OBJC_$_PROP_LIST_CLPScdmaCellTower
+ __OBJC_CLASS_PROTOCOLS_$_CLPCdmaCellTower
+ __OBJC_CLASS_PROTOCOLS_$_CLPCellConnectivityInfo
+ __OBJC_CLASS_PROTOCOLS_$_CLPGsmCellTower
+ __OBJC_CLASS_PROTOCOLS_$_CLPLteCellTower
+ __OBJC_CLASS_PROTOCOLS_$_CLPNrCellTower
+ __OBJC_CLASS_PROTOCOLS_$_CLPScdmaCellTower
+ __OBJC_CLASS_RO_$_CLPCdmaCellTower
+ __OBJC_CLASS_RO_$_CLPCellConnectivityInfo
+ __OBJC_CLASS_RO_$_CLPGsmCellTower
+ __OBJC_CLASS_RO_$_CLPLteCellTower
+ __OBJC_CLASS_RO_$_CLPNrCellTower
+ __OBJC_CLASS_RO_$_CLPScdmaCellTower
+ __OBJC_METACLASS_RO_$_CLPCdmaCellTower
+ __OBJC_METACLASS_RO_$_CLPCellConnectivityInfo
+ __OBJC_METACLASS_RO_$_CLPGsmCellTower
+ __OBJC_METACLASS_RO_$_CLPLteCellTower
+ __OBJC_METACLASS_RO_$_CLPNrCellTower
+ __OBJC_METACLASS_RO_$_CLPScdmaCellTower
+ _objc_msgSend$setCdma:
+ _objc_msgSend$setCellConnectivity:
+ _objc_msgSend$setGsm:
+ _objc_msgSend$setLte:
+ _objc_msgSend$setNr:
+ _objc_msgSend$setScdma:
CStrings:
+ "@\"CLPCdmaCellTower\""
+ "@\"CLPCellConnectivityInfo\""
+ "@\"CLPGsmCellTower\""
+ "@\"CLPLteCellTower\""
+ "@\"CLPNrCellTower\""
+ "@\"CLPScdmaCellTower\""
+ "CLPCdmaCellTower"
+ "CLPCellConnectivityInfo"
+ "CLPGsmCellTower"
+ "CLPLteCellTower"
+ "CLPNrCellTower"
+ "CLPScdmaCellTower"
+ "CONNECTED"
+ "CellConnectivity"
+ "DISCONNECTED"
+ "StringAsConnectionStatus:"
+ "T@\"CLPCdmaCellTower\",&,N,V_cdma"
+ "T@\"CLPCellConnectivityInfo\",&,N,V_cellConnectivity"
+ "T@\"CLPGsmCellTower\",&,N,V_gsm"
+ "T@\"CLPLteCellTower\",&,N,V_lte"
+ "T@\"CLPNrCellTower\",&,N,V_nr"
+ "T@\"CLPScdmaCellTower\",&,N,V_scdma"
+ "Ti,N,V_connectionStatus"
+ "UNKNOWN"
+ "VisitUnsettled"
+ "_cdma"
+ "_cellConnectivity"
+ "_connectionStatus"
+ "_gsm"
+ "_lte"
+ "_nr"
+ "_scdma"
+ "cdma"
+ "cellConnectivity"
+ "connectionStatus"
+ "connectionStatusAsString:"
+ "gsm"
+ "hasBsid"
+ "hasCdma"
+ "hasCellConnectivity"
+ "hasConnectionStatus"
+ "hasGsm"
+ "hasLac"
+ "hasLte"
+ "hasNid"
+ "hasNr"
+ "hasScdma"
+ "hasSid"
+ "lte"
+ "nr"
+ "scdma"
+ "setCdma:"
+ "setCellConnectivity:"
+ "setConnectionStatus:"
+ "setGsm:"
+ "setHasBsid:"
+ "setHasConnectionStatus:"
+ "setHasLac:"
+ "setHasNid:"
+ "setHasSid:"
+ "setLte:"
+ "setNr:"
+ "setScdma:"
+ "{?=\"bsid\"b1\"mcc\"b1\"mnc\"b1\"nid\"b1\"sid\"b1}"
+ "{?=\"ci\"b1\"lac\"b1\"mcc\"b1\"mnc\"b1}"
+ "{?=\"ci\"b1\"mcc\"b1\"mnc\"b1\"tac\"b1}"
+ "{?=\"timestamp\"b1\"connectionStatus\"b1}"

```
