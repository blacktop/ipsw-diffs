## safetyalertsd

> `/usr/libexec/safetyalertsd`

```diff

-61.0.0.0.0
-  __TEXT.__text: 0xa8ed0
-  __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_stubs: 0x2320
+62.0.0.0.0
+  __TEXT.__text: 0xaad20
+  __TEXT.__auth_stubs: 0xea0
+  __TEXT.__objc_stubs: 0x2360
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x2f0
-  __TEXT.__const: 0x841f
-  __TEXT.__gcc_except_tab: 0xa2e4
-  __TEXT.__cstring: 0x433b
-  __TEXT.__oslogstring: 0x23ed7
+  __TEXT.__const: 0x843f
+  __TEXT.__gcc_except_tab: 0xa350
+  __TEXT.__cstring: 0x4339
+  __TEXT.__oslogstring: 0x25108
   __TEXT.__objc_classname: 0x1b7
-  __TEXT.__objc_methname: 0x289e
+  __TEXT.__objc_methname: 0x28c7
   __TEXT.__objc_methtype: 0x111e
   __TEXT.__info_plist: 0x526
-  __TEXT.__unwind_info: 0x3330
-  __DATA_CONST.__auth_got: 0x758
+  __TEXT.__unwind_info: 0x3388
+  __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x6bd8
-  __DATA_CONST.__cfstring: 0x47c0
+  __DATA_CONST.__cfstring: 0x47e0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x1828
-  __DATA.__objc_selrefs: 0x978
+  __DATA.__objc_selrefs: 0x988
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x3d8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2718
-  Symbols:   391
-  CStrings:  2982
+  Functions: 2733
+  Symbols:   392
+  CStrings:  3036
 
Symbols:
+ _memcpy
CStrings:
+ "data"
+ "relayPduV1"
+ "safetyAlertsAlertID"
+ "setSafetyAlertsAlertID:"
+ "setSafetyAlertsVersion:"
+ "signature"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,copyDataAndReturnNewLen invalid data\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid  res byte 2\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid AlertInfo\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid CountryCode\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid EventByte\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid EventInfo\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid ExpInfo\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid GeoCode\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid Lang Code\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid Lat\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid Lon\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid MMI\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid MessageLen\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid MsgInfo\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid Range\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid data\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid magnitude\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid messageData\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid region code\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid res byte 1\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid sender\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeEQAlertToBLEPacket,invalid sentTime\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleRelayData,\", \"alertData\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleRelayData,can't read data\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleRelayData,invalid data payload.\", \"encodedDataLen\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleRelayData,invalid data\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleUID,\", \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleUID,\", \"encodedDataLen\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleUID,can't read UID\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleUID,invalid UID.\", \"encodedDataLen\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getBleUID,invalid data\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getSignature,\", \"Signature\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getSignature,can't read signature\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getSignature,invalid data\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,getSignature,invalid signature.\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,onBleCoreAlertCb\", \"hexSignatureStringh\":%!{(MISSING)private, location:escape_only}s, \"hexDataString\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,onBleCoreAlertCb\", \"safetyAlertsAlertData.length\":%!{(MISSING)private}llu, \"safetyAlertsSignature.length\":%!{(MISSING)private}llu}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,onBleCoreAlertCb,UID\", \"data.inDevice.safetyAlertsAlertID\":%!{(MISSING)private, location:escape_only}@, \"igneousAlertInformation.bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"alertUID\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,onBleCoreAlertCb,invalid UID\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateAlertInfo\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateAlertInfo,invalid\", \"alertInfoAlertType\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateCountryCode\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateEventByte\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateEventByte,invalid\", \"eventType\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateEventInfo\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateEventInfo,invalid\", \"eventInfoEventCategory\":%!{(MISSING)private}d, \"unsignedByte\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateExpInfo\", \"alertData[offset]\":%!{(MISSING)private}d, \"unsignedByte\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateExpInfo\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateGeoCode\", \"alertData[offset]\":%!{(MISSING)private}d, \"unsignedByte\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateGeoCode\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateLanguageCode\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateLat\", \"epi_latitude\":%!{(MISSING)private}d, \"intBytes\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateLat\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateLon\", \"epi_longitude\":%!{(MISSING)private}d, \"intBytes\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateLon\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateMessageData\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateMessageLen\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateMsgInfo\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateMsgInfo,invalid\", \"msgInfoMsgType\":%!{(MISSING)private}d, \"msgInfoResponseType\":%!{(MISSING)private}d, \"msgInfoLanguageFlag\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateRange\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateRegionCode\", \"offset\":%!{(MISSING)private}d, \"alertData\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateReserveByte\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateSender\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readAndValidateSender,invalid\", \"Sender\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,\", \"encodedDataLen\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readMMI\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readMagnitude\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readOriginTime\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readSentTime\", \"offset\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,updateBleDataToAlertData\", \"OriginTime\":\"%!{(MISSING)private}3f\", \"originTimeUnitCount\":%!{(MISSING)private}d, \"originTimeUnit\":%!{(MISSING)private}d, \"isNegative\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,updateBleDataToAlertData\", \"OriginTime\":\"%!{(MISSING)private}3f\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,updateBleDataToAlertData\", \"regionCode\":%!{(MISSING)private, location:escape_only}s, \"Sender\":%!{(MISSING)private}d, \"eventType\":%!{(MISSING)private}d, \"eventInfoPayloadLayout\":%!{(MISSING)private}d, \"eventInfoEventCategory\":%!{(MISSING)private}d, \"alertInfoAlertType\":%!{(MISSING)private}d, \"alertInfoFloodFill\":%!{(MISSING)private}d, \"msgInfoMsgType\":%!{(MISSING)private}d, \"msgInfoResponseType\":%!{(MISSING)private}d, \"msgInfoLanguageFlag\":%!{(MISSING)private}d, \"sentTime\":%!{(MISSING)private}llu, \"expirationLen\":%!{(MISSING)private}d, \"expirationNum\":%!{(MISSING)private}d, \"orginTimeOffsetFromSentTime\":%!{(MISSING)private}d, \"bleAdvertiseTime\":%!{(MISSING)private}d, \"Magnitude\":%!{(MISSING)private}d, \"MMI\":%!{(MISSING)private}d, \"GeoCodeType\":%!{(MISSING)private}d, \"geoCodeScale\":%!{(MISSING)private}d, \"epi_latitude\":%!{(MISSING)private}d, \"epi_longitude\":%!{(MISSING)private}d, \"effectiveDistance\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,updateBleDataToAlertData\", \"source\":%!{(MISSING)private, location:escape_only}s, \"uid\":%!{(MISSING)private, location:escape_only}s, \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"regionCode\":%!{(MISSING)private, location:escape_only}s, \"ingress_to_server_ts\":\"%!{(MISSING)private}0.3f\", \"egress_from_source_ts\":\"%!{(MISSING)private}0.3f\", \"event_origin_ts\":\"%!{(MISSING)private}0.3f\", \"effective\":\"%!{(MISSING)private}0.3f\", \"expires\":\"%!{(MISSING)private}0.3f\", \"event_update_number\":\"%!{(MISSING)private}0.3f\", \"epi_latitude\":\"%!{(MISSING)private}0.3f\", \"epi_longitude\":\"%!{(MISSING)private}0.3f\", \"magnitude\":\"%!{(MISSING)private}0.3f\", \"depth\":\"%!{(MISSING)private}0.3f\", \"mmiLat\":\"%!{(MISSING)private}0.3f\", \"mmiLon\":\"%!{(MISSING)private}0.3f\", \"mmiLevel\":\"%!{(MISSING)private}0.3f\", \"bleAdvertiseTime\":\"%!{(MISSING)private}0.3f\", \"effectiveDistance\":%!{(MISSING)private}d}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#evtTrk,updateIgneousReceived\", \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"bleUID\":%!{(MISSING)private, location:escape_only}@}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData\", \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"bleAlertData\":%!{(MISSING)private, location:escape_only}s, \"alertSignature\":%!{(MISSING)private, location:escape_only}s}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData\", \"d\":%!{(MISSING)private, location:escape_only}@}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData,BLE is not supported\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData,alertSignature nil\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData,authenticated\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData,bleAlertData nil\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData,bleAlertUid nil\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,extractBLEData,relayPDU nil\"}"
+ "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%!{(MISSING)private, location:escape_only}s, \"uid\":%!{(MISSING)private, location:escape_only}s, \"alertSignature\":%!{(MISSING)private, location:escape_only}s, \"bleAlertData\":%!{(MISSING)private, location:escape_only}s, \"bleAlertUID\":%!{(MISSING)private, location:escape_only}s, \"ingress_to_server_ts\":\"%!{(MISSING)private}0.3f\", \"egress_from_source_ts\":\"%!{(MISSING)private}0.3f\", \"event_origin_ts\":\"%!{(MISSING)private}0.3f\", \"effective\":\"%!{(MISSING)private}0.3f\", \"expires\":\"%!{(MISSING)private}0.3f\", \"event_update_number\":\"%!{(MISSING)private}0.3f\", \"epi_latitude\":\"%!{(MISSING)private}0.3f\", \"epi_longitude\":\"%!{(MISSING)private}0.3f\", \"magnitude\":\"%!{(MISSING)private}0.3f\", \"depth\":\"%!{(MISSING)private}0.3f\", \"mmiSize\":%!{(MISSING)private}llu, \"mmiLat\":\"%!{(MISSING)private}0.3f\", \"mmiLon\":\"%!{(MISSING)private}0.3f\", \"mmiLevel\":\"%!{(MISSING)private}0.3f\", \"Display\":%!{(MISSING)private}d}"
- "AlertSignature"
- "BLEAlertData"
- "setSafetyAlertsAlertIndex:"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"OriginTime\":\"%!{(MISSING)private}3f\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"alertData\":%!{(MISSING)private, location:escape_only}s, \"regionCode\":%!{(MISSING)private, location:escape_only}s, \"Sender\":%!{(MISSING)private}d, \"alertUIDHash\":%!{(MISSING)private, location:escape_only}s, \"eventType\":%!{(MISSING)private}d, \"Msgtypes\":%!{(MISSING)private}d, \"alertType\":%!{(MISSING)private}d, \"bleAlertInfo.sentTime\":%!{(MISSING)private}llu, \"ExpirationLen\":%!{(MISSING)private}d, \"ExpirationNum\":%!{(MISSING)private}d, \"GeoCodeType\":%!{(MISSING)private}d, \"GeoShapeType\":%!{(MISSING)private}d, \"GeoCode\":%!{(MISSING)private}llu, \"Magnitude\":%!{(MISSING)private}d, \"epi_latitude\":%!{(MISSING)private}d, \"epi_longitude\":%!{(MISSING)private}d, \"MMI\":%!{(MISSING)private}d, \"Radius\":%!{(MISSING)private}d, \"bleAdvertiseTime\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"alertData[offset]\":%!{(MISSING)private}d, \"unsignedByte\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"igneousAlertInformation.uid\":%!{(MISSING)private, location:escape_only}s}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"offset\":%!{(MISSING)private}d, \"alertData\":%!{(MISSING)private, location:escape_only}s, \"length:alert.length\":%!{(MISSING)private}llu}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"offset\":%!{(MISSING)private}d, \"buf\":%!{(MISSING)private, location:escape_only}s}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket\", \"source\":%!{(MISSING)private, location:escape_only}s, \"uid\":%!{(MISSING)private, location:escape_only}s, \"regionCode\":%!{(MISSING)private, location:escape_only}s, \"ingress_to_server_ts\":\"%!{(MISSING)private}0.3f\", \"egress_from_source_ts\":\"%!{(MISSING)private}0.3f\", \"event_origin_ts\":\"%!{(MISSING)private}0.3f\", \"effective\":\"%!{(MISSING)private}0.3f\", \"expires\":\"%!{(MISSING)private}0.3f\", \"event_update_number\":\"%!{(MISSING)private}0.3f\", \"epi_latitude\":\"%!{(MISSING)private}0.3f\", \"epi_longitude\":\"%!{(MISSING)private}0.3f\", \"magnitude\":\"%!{(MISSING)private}0.3f\", \"depth\":\"%!{(MISSING)private}0.3f\", \"mmiLat\":\"%!{(MISSING)private}0.3f\", \"mmiLon\":\"%!{(MISSING)private}0.3f\", \"mmiLevel\":\"%!{(MISSING)private}0.3f\", \"bleAdvertiseTime\":\"%!{(MISSING)private}0.3f\", \"radiusOfApplicableRegion\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket,invalid UID\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,decodeAlertToBLEPacket,invalid data\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,onBleCoreAlertCb\", \"safetyAlertsAlertData.length\":%!{(MISSING)public}llu, \"safetyAlertsSignature.length\":%!{(MISSING)public}llu}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,\", \"Signature\":%!{(MISSING)public, location:escape_only}s, \"alertData\":%!{(MISSING)public, location:escape_only}s}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,\", \"encodedDataLen\":%!{(MISSING)public}d, \"index\":%!{(MISSING)public}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,\", \"encodedDataLen\":%!{(MISSING)public}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,can't read data\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,can't read signature\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,invalid data payload.\", \"encodedDataLen\":%!{(MISSING)public}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,invalid data\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,readIndexDataAndSignature,invalid signature.\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#bletransport,startAdvertisingIgneousAlert,can not convert data to Bin\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#commonUtils,isValidHexString,\", \"d\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#commonUtils,isValidHexString,\", \"hexStr\":%!{(MISSING)private, location:escape_only}s}"
- "{\"msg%!{(MISSING)public}.0s\":\"#commonUtils,isValidHexString,emptry string\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#evtTrk,updateIgneousReceived\", \"bleUID\":%!{(MISSING)private, location:escape_only}@}"
- "{\"msg%!{(MISSING)public}.0s\":\"#evtTrk,updateIgneousReceived\", \"decodedAlertData.uid.c_str()\":%!{(MISSING)private, location:escape_only}s}"
- "{\"msg%!{(MISSING)public}.0s\":\"#evtTrk,updateIgneousReceived\", \"hexUID\":%!{(MISSING)private, location:escape_only}s}"
- "{\"msg%!{(MISSING)public}.0s\":\"#evtTrk,updateIgneousReceived,PDU decode failed\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#evtTrk,updateIgneousReceived,invalid UID\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert\", \"source\":%!{(MISSING)private, location:escape_only}s, \"uid\":%!{(MISSING)private, location:escape_only}s, \"alertSignature\":%!{(MISSING)private, location:escape_only}s, \"bleAlertData\":%!{(MISSING)private, location:escape_only}s, \"ingress_to_server_ts\":\"%!{(MISSING)private}0.3f\", \"egress_from_source_ts\":\"%!{(MISSING)private}0.3f\", \"event_origin_ts\":\"%!{(MISSING)private}0.3f\", \"effective\":\"%!{(MISSING)private}0.3f\", \"expires\":\"%!{(MISSING)private}0.3f\", \"event_update_number\":\"%!{(MISSING)private}0.3f\", \"epi_latitude\":\"%!{(MISSING)private}0.3f\", \"epi_longitude\":\"%!{(MISSING)private}0.3f\", \"magnitude\":\"%!{(MISSING)private}0.3f\", \"depth\":\"%!{(MISSING)private}0.3f\", \"mmiSize\":%!{(MISSING)private}llu, \"mmiLat\":\"%!{(MISSING)private}0.3f\", \"mmiLon\":\"%!{(MISSING)private}0.3f\", \"mmiLevel\":\"%!{(MISSING)private}0.3f\", \"Display\":%!{(MISSING)private}d}"
- "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert,alertSignature nil\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert,authenticated\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#iap,parseIgneousAlert,bleAlertData nil\"}"
- "{\"msg%!{(MISSING)public}.0s\":\"#nam,submitMetricInternal,empty history\"}"

```
