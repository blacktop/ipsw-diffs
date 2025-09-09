## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

 873.0.1.0.0
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x9f96
-  __TEXT.__os_log: 0x470b
-  __TEXT_EXEC.__text: 0x3dbd4
+  __TEXT.__cstring: 0xa72f
+  __TEXT.__os_log: 0x48a5
+  __TEXT_EXEC.__text: 0x3fc70
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x2030
+  __DATA_CONST.__const: 0x2050
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 07FF3843-426B-3BD5-B9B7-BD7178A8BF43
-  Functions: 617
+  UUID: 536A6F1F-DEC0-3E6A-A915-9D65E6817C5A
+  Functions: 624
   Symbols:   0
-  CStrings:  1599
+  CStrings:  1655
 
CStrings:
+ "%s -> %serr:0x%x\n"
+ "%s <- options:%p, secretPattern:%d\n"
+ "%s: PREPARE SEQUENCE [%d:*] %s\n"
+ "%s: Skipping trigger BioCapture for enrollment. _bioCaptureFramesToProcess: %zu\n"
+ "%s: Waiting for session prepare result. Timeout = %ums.\n"
+ "%s: frameId:[%d:%d], mainKeyIdx:%u, contextIdx:%u\n"
+ "(sensorFamily == kSensorFamilyBrunor) || (sensorFamily == kSensorFamilyAries)"
+ "(sequenceType == kPearlCamSequenceType_Enrollment) || (sequenceType == kPearlCamSequenceType_Authentication) || (sequenceType == kPearlCamSequenceType_PearlSURv2)"
+ "(skipped) "
+ "1211111212221212112121111111111111111111112112112222222212221122222222121112111112122221112121112222222222222112222222222122111211121122211122222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222221221222222221212222222222122212222222222222222121211222222221221222122111122222222112122223111222122122111111111112112222"
+ "ERROR: %s: %s (%d): occurred during Aries session preparation\n\n"
+ "EphemeralPublicKeyOutput"
+ "GetAttestationToPDAK"
+ "GetPDAK"
+ "PearlCamDoBioCaptureOptionsString_HostMainKeyIndex"
+ "PearlCamDoBioCaptureOptionsString_IVE"
+ "PearlCamDoBioCaptureOptionsString_LFSRE"
+ "PearlCamDoBioCaptureOptionsString_Nonce"
+ "PearlCamDoSecretPatternOptionsString_HostMainKeyIndex"
+ "PearlCamDoSecretPatternOptionsString_IVE"
+ "PearlCamDoSecretPatternOptionsString_LFSRE"
+ "PearlCamDoSecretPatternOptionsString_Nonce"
+ "PearlCamPearlSURDataString_EphemeralPublicKeySignature"
+ "PearlCamPearlSURDataString_EphemeralPublicKeyX"
+ "PearlCamPearlSURDataString_EphemeralPublicKeyY"
+ "PearlCamStartOptionsString_StartPrepareSession"
+ "TestAriesHostAuthorization"
+ "_ariesSessionPrepareResult == 0 "
+ "_savageSessionOptions.sensorType == kSavageSensorTypeAries"
+ "ariesEphPublicKey"
+ "ariesEphPublicKeySig"
+ "ariesFrameGetSensorIndexes"
+ "ariesGetStreamingSessionData"
+ "ariesSessionData"
+ "ariesSessionPrepare"
+ "contextIdxOut"
+ "data->getLength() == sizeof(ariesEphPublicKey->x)"
+ "data->getLength() == sizeof(ariesEphPublicKey->y)"
+ "data->getLength() == sizeof(sessionPrepareResponse.ariesEphPublicKeySig)"
+ "data->getLength() == sizeof(unwrapResponse.unwrapOutputSensorSigAries)"
+ "handleCameraAriesSessionPrepareOutputNotification"
+ "hostMasterKeyIdx"
+ "ivE"
+ "lfsrE"
+ "mainKeyIdxOut"
+ "memcmp(edlIdx->padding0, paddingBytes, sizeof(edlIdx->padding0)) == 0 "
+ "memcmp(edlIdx->padding1, paddingBytes, sizeof(edlIdx->padding1)) == 0 "
+ "nonce"
+ "rawFrameLength >= mainKeyIdxAbsoluteOffset + sizeof(*edlIdx)"
+ "rawFrameVA"
+ "rawMap"
+ "sensorFamily == kSensorFamilyAries"
+ "streamingSessionData"
+ "streamingSessionData::hostMasterKeyIdx"
+ "streamingSessionData::ivE"
+ "streamingSessionData::lfsrE"
+ "streamingSessionData::nonce"
+ "streamingSessionDataLength == sizeof(*streamingSessionData)"
- "121111121222121211212111111111111111111111211211222222221222112222222212111211111212222111212111222222222222211222222222212211121112112221112222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222121222222222212221222222222222222212121122222222122122212211112222222211212222311122212212211111111111211222"
- "sensorFamily == kSensorFamilyBrunor"

```
