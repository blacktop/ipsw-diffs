## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

-754.120.4.0.0
-  __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x99ea
-  __TEXT.__os_log: 0x45d6
-  __TEXT_EXEC.__text: 0x3cc94
+859.0.0.0.0
+  __TEXT.__const: 0x318
+  __TEXT.__cstring: 0x9e80
+  __TEXT.__os_log: 0x4706
+  __TEXT_EXEC.__text: 0x3d80c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8
-  __DATA.__bss: 0x85
-  __DATA_CONST.__auth_got: 0x5b0
+  __DATA.__bss: 0x88
+  __DATA_CONST.__auth_got: 0x5c0
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x1fe8
+  __DATA_CONST.__const: 0x2030
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 3D7AD9BB-D6F6-32B4-A6FB-9843F9458CE5
-  Functions: 623
+  UUID: 40E28EE0-D515-3CBD-9E21-B717686B8BB5
+  Functions: 612
   Symbols:   0
-  CStrings:  1545
+  CStrings:  1585
 
CStrings:
+ "\n"
+ " "
+ "!_secureStreamingCheckInProgress && (_brunorKeyUnwrappingState == kBrunorKeyUnwrappingStateNone) && (_cameraState != kCameraStateAriesSessionPrepare)"
+ "%02x%s"
+ "%04zx: "
+ "%s"
+ "%s <- sequenceType:%s (%d) overrideIsPearlDisabled:%d loadingFDR:%d\n"
+ "%s: (hexdump failed)\n"
+ "%s: Clearing _bioCaptureFramesToProcess (remaining:%zu)\n"
+ "%s: bioCapture frame received with _bioCaptureFramesToProcess == 0\n"
+ "%s:%s%s\n"
+ "(_cameraState == kCameraStateIdle) || (_cameraState == kCameraStatePearlSURv2) || (_cameraState == kCameraStateAriesSessionPrepare)"
+ "(_cameraState == kCameraStatePearlSURv2) || (_cameraState == kCameraStateAriesSessionPrepare)"
+ "*sensorFamilyReply != kSensorFamilyNotSet"
+ "*sensorFamilyReply < kSensorFamilyCount"
+ "121111121222121211212111111111111111111111211211222222221222112222222212111211111212222111212111222222222221122222222221221112111211222111222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222122222222122122222222121222222222212221222222222222222212121122222222122122212211112222222211212222311122212212211111111111211222"
+ "AriesSessionPrepare"
+ "ERROR: %s: Unknown sensor type (deviceID: 0x%04x) - assuming %d to be able to proceed\n\n"
+ "GenerateUnwrapSessionRequest"
+ "GetSensorFamily"
+ "GetSensorFamilyCommand"
+ "PearlCamSendBuffersInfoString_GlassesScore"
+ "PearlCamSendBuffersInfoString_HasGlasses"
+ "SetUnwrapSessionResponse"
+ "SystemSleep"
+ "_bioCaptureFramesToProcess == 0"
+ "bytes && bytesLength"
+ "bytesLength && bytesLength <= BYTES_MAX"
+ "bytesWritten && static_cast<size_t>(bytesWritten) < buffRemaining"
+ "cameraStateHandlerSwitch"
+ "data->getLength() == sizeof(unwrapResponse.unwrapOutputNonce)"
+ "data->getLength() == sizeof(unwrapResponse.unwrapOutputSensorTagBrunor)"
+ "getSensorFamily"
+ "hexdumpBytes"
+ "logHexdumpBytesWithTitle"
+ "outSize && (*outSize >= sizeof(response))"
+ "pearl-enable-log-hexdump"
+ "rawData"
+ "rawData->appendBytes(buff, static_cast<unsigned int>(buffOffset + bytesWritten))"
+ "rawData->appendBytes(buff, static_cast<unsigned int>(buffOffset))"
+ "rawData->appendValue('\\0')"
+ "replySize == sizeof(*sensorFamilyReply)"
+ "sensorFamily == kSensorFamilyBrunor"
+ "sensorFamilyOut"
+ "sizeof(_savageSessionOptions.fwNonce) == _brunorBootNonce->getLength()"
+ "sizeof(unwrapSessionOptions.wrappedKey) == _brunorWrappedKey->getLength()"
+ "title"
+ "unwrapOutputKey"
+ "unwrapOutputKeyHmac"
+ "unwrapOutputNonce"
+ "unwrapOutputSensorIV"
+ "unwrapOutputSensorTag"
+ "unwrapSessionRequest"
+ "unwrapSessionRequestSize == sizeof(*unwrapSessionRequest)"
- "!_secureStreamingCheckInProgress && (_brunorKeyUnwrappingState == kBrunorKeyUnwrappingStateNone)"
- "%s -> _platformHasBrunorSensor: %d\n"
- "121111121222121211212111111111111111111111211211222222221222112222222121112111112122111212111222222222211222222222212211121112112221112222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222221221222222221212222222222122212222222222222222121211222222221221222122111122222222112122223111222122122111111111112211222"
- "ERROR: %s: Unknown sensor type - assuming %d to be able to proceed\n\n"
- "_cameraState == kCameraStateIdle || _cameraState == kCameraStatePearlSURv2"
- "_cameraState == kCameraStatePearlSURv2"
- "brunorUnwrapRequest"
- "brunorUnwrapRequestSize == sizeof(*brunorUnwrapRequest)"
- "data->getLength() == sizeof(unwrapResponse.unwrapOutNonce)"
- "data->getLength() == sizeof(unwrapResponse.unwrapOutputSensorTag)"
- "platformHasBrunorSensor"
- "platformHasBrunorSensor()"
- "sizeof(brunorSessionOptions.bootNonce) == _brunorBootNonce->getLength()"
- "sizeof(brunorSessionOptions.wrappedKey) == _brunorWrappedKey->getLength()"

```
