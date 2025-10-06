## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-173.2.0.0.0
-  __TEXT.__text: 0x876dc
+174.16.1.1.2
+  __TEXT.__text: 0x89e7c
   __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x7780
+  __TEXT.__objc_methlist: 0x7960
   __TEXT.__oslogstring: 0x2576
-  __TEXT.__cstring: 0xfbbc
-  __TEXT.__const: 0x20fa
-  __TEXT.__gcc_except_tab: 0x13c0
+  __TEXT.__cstring: 0xfec3
+  __TEXT.__const: 0x2133
+  __TEXT.__gcc_except_tab: 0x1e10
   __TEXT.__ustring: 0xcc
-  __TEXT.__unwind_info: 0x1894
-  __TEXT.__objc_classname: 0x61d
-  __TEXT.__objc_methname: 0x11dc0
+  __TEXT.__unwind_info: 0x18f0
+  __TEXT.__objc_classname: 0x645
+  __TEXT.__objc_methname: 0x12634
   __TEXT.__objc_methtype: 0x20e5
-  __TEXT.__objc_stubs: 0x7da0
+  __TEXT.__objc_stubs: 0x7ee0
   __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x3a28
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __DATA_CONST.__const: 0x3db8
+  __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xe9d0
-  __DATA_CONST.__objc_selrefs: 0x3d58
+  __DATA_CONST.__objc_const: 0xed88
+  __DATA_CONST.__objc_selrefs: 0x3e68
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__cfstring: 0x9ae0
-  __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__objc_intobj: 0x828
+  __AUTH_CONST.__cfstring: 0x9cc0
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__objc_intobj: 0x840
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__auth_got: 0x850
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x200
-  __DATA.__objc_superrefs: 0x128
-  __DATA.__objc_ivar: 0xcec
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0xd34
   __DATA.__data: 0xd18
   __DATA.__common: 0x0
-  __DATA_DIRTY.__const: 0x2e0
+  __DATA_DIRTY.__const: 0x1e0
   __DATA_DIRTY.__objc_const: 0x1280
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__data: 0x1c0
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 83E1EFAE-43FD-3CB2-9571-FC472794A3AD
-  Functions: 3184
-  Symbols:   9769
-  CStrings:  8006
+  UUID: CA860659-C2D5-32D4-B5E4-5E94A2CDA525
+  Functions: 3232
+  Symbols:   9909
+  CStrings:  8138
 
Symbols:
+ -[CBAdvertiser safetyAlertsAlertData]
+ -[CBAdvertiser safetyAlertsAlertIndex]
+ -[CBAdvertiser safetyAlertsSignature]
+ -[CBAdvertiser safetyAlertsVersion]
+ -[CBAdvertiser setSafetyAlertsAlertData:]
+ -[CBAdvertiser setSafetyAlertsAlertIndex:]
+ -[CBAdvertiser setSafetyAlertsSignature:]
+ -[CBAdvertiser setSafetyAlertsVersion:]
+ -[CBDevice _parseSafetyAlertsSegmentServiceData:]
+ -[CBDevice getSpatialInteractionDeviceTimestampArrayForClientID:]
+ -[CBDevice safetyAlertsAlertData]
+ -[CBDevice safetyAlertsAlertIndex]
+ -[CBDevice safetyAlertsSegmentAlertData]
+ -[CBDevice safetyAlertsSegmentSegmentNumber]
+ -[CBDevice safetyAlertsSegmentSegmentsTotal]
+ -[CBDevice safetyAlertsSegmentServiceData]
+ -[CBDevice safetyAlertsSegmentSignature]
+ -[CBDevice safetyAlertsSignature]
+ -[CBDevice safetyAlertsVersion]
+ -[CBDevice setSafetyAlertsSegmentAlertData:]
+ -[CBDevice setSafetyAlertsSegmentSegmentNumber:]
+ -[CBDevice setSafetyAlertsSegmentSegmentsTotal:]
+ -[CBDevice setSafetyAlertsSegmentServiceData:]
+ -[CBDevice setSafetyAlertsSegmentSignature:]
+ -[CBDevice setSpatialInteractionDeviceTimestampArrayClientIDs:]
+ -[CBDevice setSpatialInteractionDeviceTimestampArrayDictionary:]
+ -[CBDevice setSpatialInteractionDeviceTimestampArrayForClientID:clientID:]
+ -[CBDevice spatialInteractionDeviceTimestampArrayClientIDs]
+ -[CBDevice spatialInteractionDeviceTimestampArrayDictionary]
+ -[CBDevice updateWithSafetyAlertsSegments:error:]
+ -[CBManager queryBluetoothStatus:completion:]
+ -[CBSpatialInteractionDeviceTimestampInfo descriptionWithLevel:]
+ -[CBSpatialInteractionDeviceTimestampInfo description]
+ -[CBSpatialInteractionDeviceTimestampInfo duplicateCount]
+ -[CBSpatialInteractionDeviceTimestampInfo reason]
+ -[CBSpatialInteractionDeviceTimestampInfo setDuplicateCount:]
+ -[CBSpatialInteractionDeviceTimestampInfo setReason:]
+ -[CBSpatialInteractionDeviceTimestampInfo setTimestamp:]
+ -[CBSpatialInteractionDeviceTimestampInfo timestamp]
+ GCC_except_table119
+ GCC_except_table132
+ GCC_except_table148
+ _CBCentralManagerScanContainsBlobMaskForServiceUUIDs
+ _CBCentralManagerScanOptionAddRulesKey
+ _CBCentralManagerScanOptionBlobForServiceUUID
+ _CBCentralManagerScanOptionBlobMaskServiceUUID
+ _CBCentralManagerScanOptionMaskForServiceUUID
+ _CBNearbyActionTypeToString
+ _CBProductIDToNSLocalizedProductNameString
+ _CBProductInfoB465
+ _OBJC_CLASS_$_CBSpatialInteractionDeviceTimestampInfo
+ _OBJC_IVAR_$_CBAdvertiser._safetyAlertsAlertData
+ _OBJC_IVAR_$_CBAdvertiser._safetyAlertsAlertIndex
+ _OBJC_IVAR_$_CBAdvertiser._safetyAlertsSignature
+ _OBJC_IVAR_$_CBAdvertiser._safetyAlertsVersion
+ _OBJC_IVAR_$_CBDevice._safetyAlertsAlertData
+ _OBJC_IVAR_$_CBDevice._safetyAlertsAlertIndex
+ _OBJC_IVAR_$_CBDevice._safetyAlertsSegmentAlertData
+ _OBJC_IVAR_$_CBDevice._safetyAlertsSegmentSegmentNumber
+ _OBJC_IVAR_$_CBDevice._safetyAlertsSegmentSegmentsTotal
+ _OBJC_IVAR_$_CBDevice._safetyAlertsSegmentServiceData
+ _OBJC_IVAR_$_CBDevice._safetyAlertsSegmentSignature
+ _OBJC_IVAR_$_CBDevice._safetyAlertsSignature
+ _OBJC_IVAR_$_CBDevice._safetyAlertsVersion
+ _OBJC_IVAR_$_CBDevice._spatialInteractionDeviceTimestampArrayClientIDs
+ _OBJC_IVAR_$_CBDevice._spatialInteractionDeviceTimestampArrayDictionary
+ _OBJC_IVAR_$_CBSpatialInteractionDeviceTimestampInfo._duplicateCount
+ _OBJC_IVAR_$_CBSpatialInteractionDeviceTimestampInfo._reason
+ _OBJC_IVAR_$_CBSpatialInteractionDeviceTimestampInfo._timestamp
+ _OBJC_METACLASS_$_CBSpatialInteractionDeviceTimestampInfo
+ __OBJC_$_INSTANCE_METHODS_CBSpatialInteractionDeviceTimestampInfo
+ __OBJC_$_INSTANCE_VARIABLES_CBSpatialInteractionDeviceTimestampInfo
+ __OBJC_$_PROP_LIST_CBSpatialInteractionDeviceTimestampInfo
+ __OBJC_CLASS_RO_$_CBSpatialInteractionDeviceTimestampInfo
+ __OBJC_METACLASS_RO_$_CBSpatialInteractionDeviceTimestampInfo
+ ___33-[CBDevice descriptionWithLevel:]_block_invoke
+ ___39-[CBAdvertiser setSafetyAlertsVersion:]_block_invoke
+ ___41-[CBAdvertiser setSafetyAlertsAlertData:]_block_invoke
+ ___41-[CBAdvertiser setSafetyAlertsSignature:]_block_invoke
+ ___42-[CBAdvertiser setSafetyAlertsAlertIndex:]_block_invoke
+ ___45-[CBManager queryBluetoothStatus:completion:]_block_invoke
+ ___64-[CBSpatialInteractionDeviceTimestampInfo descriptionWithLevel:]_block_invoke
+ ___block_descriptor_44_e8_32r_e41_v32?0"NSNumber"8"NSMutableArray"16^B24lr32l8
+ ___block_literal_global.245
+ ___block_literal_global.247
+ ___block_literal_global.249
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.255
+ ___block_literal_global.257
+ ___block_literal_global.259
+ ___block_literal_global.375
+ ___block_literal_global.664
+ _objc_msgSend$_parseSafetyAlertsSegmentServiceData:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$safetyAlertsAlertData
+ _objc_msgSend$safetyAlertsAlertIndex
+ _objc_msgSend$safetyAlertsSegmentAlertData
+ _objc_msgSend$safetyAlertsSegmentSegmentsTotal
+ _objc_msgSend$safetyAlertsSegmentServiceData
+ _objc_msgSend$safetyAlertsSegmentSignature
+ _objc_msgSend$safetyAlertsSignature
+ _objc_msgSend$safetyAlertsVersion
- GCC_except_table110
- GCC_except_table123
- GCC_except_table144
- ___block_literal_global.244
- ___block_literal_global.246
- ___block_literal_global.248
- ___block_literal_global.250
- ___block_literal_global.252
- ___block_literal_global.254
- ___block_literal_global.256
- ___block_literal_global.258
- ___block_literal_global.371
CStrings:
+ "\x11!\xa4\x1e\x1a"
+ " CID 0x%X : %@"
+ " siTD %d"
+ " siTR %@"
+ " }>"
+ "%f"
+ ", AVC %@"
+ ", CDC %@"
+ ", ECC %@"
+ ", Invl %gms"
+ ", MCC %@"
+ ", PrNm %@"
+ ", SSLC %@"
+ ", saAd <%@>"
+ ", saAi %d"
+ ", saSAd <%@>"
+ ", saSSg <%@>"
+ ", saSSn %d"
+ ", saSSvcD <%@>"
+ ", saSTs %d"
+ ", saSg <%@>"
+ ", saVs %d"
+ ", siTAD <{"
+ ", ssCp %@"
+ ", ssLC %@"
+ "B24@0:8r^{?=[4C]}16"
+ "Beats Solo 4"
+ "CBSpatialInteractionDeviceTimestampInfo"
+ "Common Audio Service"
+ "Count"
+ "Device1,8229"
+ "DoubleTap"
+ "FindNearbyPencil"
+ "HasInvitation"
+ "Invalid alert data length"
+ "Invalid signature length"
+ "Invalid value"
+ "Invalid version"
+ "SafetyAlerts"
+ "Segment %d/%d not found"
+ "SharingVisionProDiscovery"
+ "SharingVisionProStateChange"
+ "SingleTap"
+ "T@\"NSData\",C,N,V_safetyAlertsAlertData"
+ "T@\"NSData\",C,N,V_safetyAlertsSegmentAlertData"
+ "T@\"NSData\",C,N,V_safetyAlertsSegmentServiceData"
+ "T@\"NSData\",C,N,V_safetyAlertsSegmentSignature"
+ "T@\"NSData\",C,N,V_safetyAlertsSignature"
+ "T@\"NSData\",R,C,N,V_safetyAlertsAlertData"
+ "T@\"NSData\",R,C,N,V_safetyAlertsSignature"
+ "T@\"NSMutableArray\",C,N,V_spatialInteractionDeviceTimestampArrayClientIDs"
+ "T@\"NSMutableDictionary\",C,N,V_spatialInteractionDeviceTimestampArrayDictionary"
+ "T@\"NSString\",?,R,C"
+ "TC,N,V_duplicateCount"
+ "TC,N,V_reason"
+ "TC,N,V_safetyAlertsAlertIndex"
+ "TC,N,V_safetyAlertsSegmentSegmentNumber"
+ "TC,N,V_safetyAlertsSegmentSegmentsTotal"
+ "TC,N,V_safetyAlertsVersion"
+ "TC,R,N,V_safetyAlertsAlertIndex"
+ "TC,R,N,V_safetyAlertsVersion"
+ "T^{?=[4C]},R,N"
+ "Td,N,V_timestamp"
+ "^{?=[4C]}16@0:8"
+ "_duplicateCount"
+ "_parseSafetyAlertsSegmentServiceData:"
+ "_reason"
+ "_safetyAlertsAlertData"
+ "_safetyAlertsAlertIndex"
+ "_safetyAlertsSegmentAlertData"
+ "_safetyAlertsSegmentSegmentNumber"
+ "_safetyAlertsSegmentSegmentsTotal"
+ "_safetyAlertsSegmentServiceData"
+ "_safetyAlertsSegmentSignature"
+ "_safetyAlertsSignature"
+ "_safetyAlertsVersion"
+ "_spatialInteractionDeviceTimestampArrayClientIDs"
+ "_spatialInteractionDeviceTimestampArrayDictionary"
+ "_timestamp"
+ "dateWithTimeIntervalSince1970:"
+ "duplicateCount"
+ "getSpatialInteractionDeviceTimestampArrayForClientID:"
+ "kCBScanOptionAddRulesKey"
+ "kCBScanOptionBlobForServiceUUID"
+ "kCBScanOptionContainsBlobMaskForServiceUUID"
+ "kCBScanOptionContainsBlobMaskForServiceUUIDs"
+ "kCBScanOptionMaskForServiceUUID"
+ "queryBluetoothStatus:completion:"
+ "reason"
+ "saAd"
+ "saAd: %@ -> %@"
+ "saAi"
+ "saAi: %d -> %d"
+ "saSg"
+ "saSg: %@ -> %@"
+ "saVs"
+ "saVs: %d -> %d"
+ "safetyAlertsAlertData"
+ "safetyAlertsAlertIndex"
+ "safetyAlertsSegmentAlertData"
+ "safetyAlertsSegmentSegmentNumber"
+ "safetyAlertsSegmentSegmentsTotal"
+ "safetyAlertsSegmentServiceData"
+ "safetyAlertsSegmentSignature"
+ "safetyAlertsSignature"
+ "safetyAlertsVersion"
+ "setDuplicateCount:"
+ "setReason:"
+ "setSafetyAlertsAlertData:"
+ "setSafetyAlertsAlertIndex:"
+ "setSafetyAlertsSegmentAlertData:"
+ "setSafetyAlertsSegmentSegmentNumber:"
+ "setSafetyAlertsSegmentSegmentsTotal:"
+ "setSafetyAlertsSegmentServiceData:"
+ "setSafetyAlertsSegmentSignature:"
+ "setSafetyAlertsSignature:"
+ "setSafetyAlertsVersion:"
+ "setSpatialInteractionDeviceTimestampArrayClientIDs:"
+ "setSpatialInteractionDeviceTimestampArrayDictionary:"
+ "setSpatialInteractionDeviceTimestampArrayForClientID:clientID:"
+ "setTimestamp:"
+ "siTT %@"
+ "spatialInteractionDeviceTimestampArrayClientIDs"
+ "spatialInteractionDeviceTimestampArrayDictionary"
+ "timestamp"
+ "updateWithSafetyAlertsSegments:error:"
+ "v32@?0@\"NSNumber\"8@\"NSMutableArray\"16^B24"
+ "{?=\"bitArray\"[4C]}"
+ "\xf0\x94\x12\x12/\x1f\x06\x11\x19"
- "\x11!\xa4\x1e\x18"
- " AVC %u"
- " CDC %u"
- " SSLC %u"
- ", inV %hu"
- ", ssCp %u"
- ", ssLC %u"
- "B24@0:8r^{?=[3C]}16"
- "T^{?=[3C]},R,N"
- "^{?=[3C]}16@0:8"
- "{?=\"bitArray\"[3C]}"
- "\xf0\x84\x12\x12/\x1f\x04\x11\x14"

```
