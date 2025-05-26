## SensorKit

> `/System/Library/Frameworks/SensorKit.framework/SensorKit`

```diff

-707.0.47.0.0
-  __TEXT.__text: 0x2d0b0
-  __TEXT.__auth_stubs: 0x780
-  __TEXT.__objc_methlist: 0x3544
-  __TEXT.__const: 0x4c
-  __TEXT.__constg_swiftt: 0x40
-  __TEXT.__swift5_typeref: 0x5f
-  __TEXT.__gcc_except_tab: 0x770
-  __TEXT.__cstring: 0x42ea
-  __TEXT.__oslogstring: 0x3e74
+756.0.25.0.0
+  __TEXT.__text: 0x35b4c
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x42ec
+  __TEXT.__const: 0x6c
+  __TEXT.__constg_swiftt: 0x68
+  __TEXT.__swift5_typeref: 0x91
+  __TEXT.__swift5_reflstr: 0x46
+  __TEXT.__swift5_fieldmd: 0x40
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0x81c
+  __TEXT.__cstring: 0x48cc
+  __TEXT.__oslogstring: 0x44a0
   __TEXT.__dlopen_cstrs: 0x95
-  __TEXT.__unwind_info: 0xd60
-  __TEXT.__objc_classname: 0x82a
-  __TEXT.__objc_methname: 0x7ca2
-  __TEXT.__objc_methtype: 0x1226
-  __TEXT.__objc_stubs: 0x5000
+  __TEXT.__unwind_info: 0x102c
+  __TEXT.__objc_classname: 0xa6c
+  __TEXT.__objc_methname: 0x88d8
+  __TEXT.__objc_methtype: 0x1a52
+  __TEXT.__objc_stubs: 0x5b20
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0x10a8
-  __DATA_CONST.__objc_classlist: 0x1b8
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__const: 0x1158
+  __DATA_CONST.__objc_classlist: 0x248
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5728
-  __DATA_CONST.__objc_selrefs: 0x1b08
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__const: 0x290
-  __AUTH_CONST.__cfstring: 0x4080
-  __AUTH_CONST.__objc_const: 0x1e78
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __DATA_CONST.__objc_const: 0x7478
+  __DATA_CONST.__objc_selrefs: 0x1de0
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_classrefs: 0x3a8
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0x5e0
+  __AUTH_CONST.__const: 0x318
+  __AUTH_CONST.__cfstring: 0x46e0
+  __AUTH_CONST.__objc_const: 0x27b8
+  __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3d0
-  __AUTH.__objc_data: 0xe60
-  __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x2f0
-  __DATA.__objc_superrefs: 0x180
-  __DATA.__objc_ivar: 0x444
-  __DATA.__data: 0xd40
-  __DATA.__bss: 0x70
+  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH.__objc_data: 0x1400
+  __DATA.__objc_ivar: 0x544
+  __DATA.__data: 0xec0
+  __DATA.__bss: 0x90
   __DATA.__common: 0x30
   __DATA_DIRTY.__objc_ivar: 0xc
   __DATA_DIRTY.__objc_data: 0x2d0

   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftARKit.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSceneKit.dylib
+  - /usr/lib/swift/libswiftShazamKit.dylib
   - /usr/lib/swift/libswiftSpriteKit.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVision.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1286
-  Symbols:   4767
-  CStrings:  2437
+  Functions: 1567
+  Symbols:   5740
+  CStrings:  2728
 
Symbols:
+ +[NSArray(HAAccelSamples) sr_arrayWithHAAccelSamples:]
+ +[NSArray(HAOpticalSamples) sr_arrayWithHAOpticalSamples:]
+ +[SRCursor initialize]
+ +[SRCursor new]
+ +[SRCursor supportsSecureCoding]
+ +[SRElectrocardiogramData new]
+ +[SRElectrocardiogramData supportsSecureCoding]
+ +[SRElectrocardiogramSample new]
+ +[SRElectrocardiogramSample supportsSecureCoding]
+ +[SRElectrocardiogramSession new]
+ +[SRElectrocardiogramSession supportsSecureCoding]
+ +[SRFaceMetricsPacket initialize]
+ +[SRFaceMetricsPacket new]
+ +[SRFaceMetricsPacket packetWithData:]
+ +[SRFaceMetricsPacketV0 packetWithHAFacialMetricsPacket:]
+ +[SRFaceMetricsPacketV1 packetWithHAFacialMetricsPacket:]
+ +[SRFaceMetricsPacketV2 packetWithHAFacialMetricsPacket:]
+ +[SRFaceMetricsPacketV3 packetWithHAFacialMetricsPacket:]
+ +[SRFaceMetricsPacketV4 packetWithHAFacialMetricsPacket:]
+ +[SRFaceMetricsPacketV5 packetWithHAFacialMetricsPacket:]
+ +[SRPhotoplethysmogramAccelerometerSample supportsSecureCoding]
+ +[SRPhotoplethysmogramOpticalSample supportsSecureCoding]
+ +[SRPhotoplethysmogramSample new]
+ +[SRPhotoplethysmogramSample supportsSecureCoding]
+ +[SRReaderLongTermBackend clientInterface]
+ +[SRReaderLongTermBackend connectionToEndpoint]
+ +[SRReaderLongTermBackend initialize]
+ +[SRReaderLongTermBackend new]
+ +[SRReaderLongTermBackend remoteInterface]
+ +[SRReaderSensorKitBackend clientInterface]
+ +[SRReaderSensorKitBackend connectionToEndpoint]
+ +[SRReaderSensorKitBackend initialize]
+ +[SRReaderSensorKitBackend new]
+ +[SRReaderSensorKitBackend remoteInterface]
+ -[SRCursor copyWithZone:]
+ -[SRCursor dealloc]
+ -[SRCursor description]
+ -[SRCursor encodeWithCoder:]
+ -[SRCursor hash]
+ -[SRCursor initWithCoder:]
+ -[SRCursor initWithPayload:hmac:]
+ -[SRCursor init]
+ -[SRCursor isEqual:]
+ -[SRCursor(_PayloadInspection) _payloadOfClass:error:]
+ -[SRDebugInfoClient fetchDeviceInformationForDeviceIdentifiers:reply:]
+ -[SRECGSampleArray initWithBinarySampleRepresentation:metadata:timestamp:]
+ -[SRElectrocardiogramData copyWithZone:]
+ -[SRElectrocardiogramData description]
+ -[SRElectrocardiogramData encodeWithCoder:]
+ -[SRElectrocardiogramData flags]
+ -[SRElectrocardiogramData hash]
+ -[SRElectrocardiogramData initWithCoder:]
+ -[SRElectrocardiogramData initWithFlags:value:]
+ -[SRElectrocardiogramData init]
+ -[SRElectrocardiogramData isEqual:]
+ -[SRElectrocardiogramData isEqualToECGData:]
+ -[SRElectrocardiogramData value]
+ -[SRElectrocardiogramSample copyWithZone:]
+ -[SRElectrocardiogramSample data]
+ -[SRElectrocardiogramSample date]
+ -[SRElectrocardiogramSample dealloc]
+ -[SRElectrocardiogramSample description]
+ -[SRElectrocardiogramSample encodeWithCoder:]
+ -[SRElectrocardiogramSample frequency]
+ -[SRElectrocardiogramSample hash]
+ -[SRElectrocardiogramSample initWithCoder:]
+ -[SRElectrocardiogramSample initWithHAECGSample:]
+ -[SRElectrocardiogramSample initWithTimestamp:frequency:session:lead:data:]
+ -[SRElectrocardiogramSample init]
+ -[SRElectrocardiogramSample isEqual:]
+ -[SRElectrocardiogramSample isEqualToSample:]
+ -[SRElectrocardiogramSample lead]
+ -[SRElectrocardiogramSample session]
+ -[SRElectrocardiogramSession copyWithZone:]
+ -[SRElectrocardiogramSession dealloc]
+ -[SRElectrocardiogramSession description]
+ -[SRElectrocardiogramSession encodeWithCoder:]
+ -[SRElectrocardiogramSession hash]
+ -[SRElectrocardiogramSession identifier]
+ -[SRElectrocardiogramSession initWithCoder:]
+ -[SRElectrocardiogramSession initWithState:sessionGuidance:identifier:]
+ -[SRElectrocardiogramSession init]
+ -[SRElectrocardiogramSession isEqual:]
+ -[SRElectrocardiogramSession isEqualToSession:]
+ -[SRElectrocardiogramSession sessionGuidance]
+ -[SRElectrocardiogramSession state]
+ -[SRFaceMetricsPacketV0 blendshapes]
+ -[SRFaceMetricsPacketV0 context]
+ -[SRFaceMetricsPacketV0 dealloc]
+ -[SRFaceMetricsPacketV0 faceIdentifier]
+ -[SRFaceMetricsPacketV0 gaze]
+ -[SRFaceMetricsPacketV0 geometryLeftEye]
+ -[SRFaceMetricsPacketV0 geometryRightEye]
+ -[SRFaceMetricsPacketV0 leftEyePitch]
+ -[SRFaceMetricsPacketV0 leftEyeYaw]
+ -[SRFaceMetricsPacketV0 partialFaceExpressions]
+ -[SRFaceMetricsPacketV0 rightEyePitch]
+ -[SRFaceMetricsPacketV0 rightEyeYaw]
+ -[SRFaceMetricsPacketV0 rotation]
+ -[SRFaceMetricsPacketV0 sessionIdentifier]
+ -[SRFaceMetricsPacketV0 trackingData]
+ -[SRFaceMetricsPacketV0 translation]
+ -[SRFaceMetricsPacketV0 version]
+ -[SRFaceMetricsPacketV0 wholeFaceExpressions]
+ -[SRFaceMetricsPacketV1 blendshapes]
+ -[SRFaceMetricsPacketV1 context]
+ -[SRFaceMetricsPacketV1 dealloc]
+ -[SRFaceMetricsPacketV1 faceIdentifier]
+ -[SRFaceMetricsPacketV1 gaze]
+ -[SRFaceMetricsPacketV1 geometryLeftEye]
+ -[SRFaceMetricsPacketV1 geometryRightEye]
+ -[SRFaceMetricsPacketV1 leftEyePitch]
+ -[SRFaceMetricsPacketV1 leftEyeYaw]
+ -[SRFaceMetricsPacketV1 partialFaceExpressions]
+ -[SRFaceMetricsPacketV1 rightEyePitch]
+ -[SRFaceMetricsPacketV1 rightEyeYaw]
+ -[SRFaceMetricsPacketV1 rotation]
+ -[SRFaceMetricsPacketV1 sessionIdentifier]
+ -[SRFaceMetricsPacketV1 trackingData]
+ -[SRFaceMetricsPacketV1 translation]
+ -[SRFaceMetricsPacketV1 version]
+ -[SRFaceMetricsPacketV1 wholeFaceExpressions]
+ -[SRFaceMetricsPacketV2 blendshapes]
+ -[SRFaceMetricsPacketV2 context]
+ -[SRFaceMetricsPacketV2 dealloc]
+ -[SRFaceMetricsPacketV2 faceIdentifier]
+ -[SRFaceMetricsPacketV2 gaze]
+ -[SRFaceMetricsPacketV2 geometryLeftEye]
+ -[SRFaceMetricsPacketV2 geometryRightEye]
+ -[SRFaceMetricsPacketV2 leftEyePitch]
+ -[SRFaceMetricsPacketV2 leftEyeYaw]
+ -[SRFaceMetricsPacketV2 partialFaceExpressions]
+ -[SRFaceMetricsPacketV2 rightEyePitch]
+ -[SRFaceMetricsPacketV2 rightEyeYaw]
+ -[SRFaceMetricsPacketV2 rotation]
+ -[SRFaceMetricsPacketV2 sessionIdentifier]
+ -[SRFaceMetricsPacketV2 trackingData]
+ -[SRFaceMetricsPacketV2 translation]
+ -[SRFaceMetricsPacketV2 version]
+ -[SRFaceMetricsPacketV2 wholeFaceExpressions]
+ -[SRFaceMetricsPacketV3 blendshapes]
+ -[SRFaceMetricsPacketV3 context]
+ -[SRFaceMetricsPacketV3 dealloc]
+ -[SRFaceMetricsPacketV3 faceIdentifier]
+ -[SRFaceMetricsPacketV3 gaze]
+ -[SRFaceMetricsPacketV3 geometryLeftEye]
+ -[SRFaceMetricsPacketV3 geometryRightEye]
+ -[SRFaceMetricsPacketV3 leftEyePitch]
+ -[SRFaceMetricsPacketV3 leftEyeYaw]
+ -[SRFaceMetricsPacketV3 partialFaceExpressions]
+ -[SRFaceMetricsPacketV3 rightEyePitch]
+ -[SRFaceMetricsPacketV3 rightEyeYaw]
+ -[SRFaceMetricsPacketV3 rotation]
+ -[SRFaceMetricsPacketV3 sessionIdentifier]
+ -[SRFaceMetricsPacketV3 trackingData]
+ -[SRFaceMetricsPacketV3 translation]
+ -[SRFaceMetricsPacketV3 version]
+ -[SRFaceMetricsPacketV3 wholeFaceExpressions]
+ -[SRFaceMetricsPacketV4 blendshapes]
+ -[SRFaceMetricsPacketV4 context]
+ -[SRFaceMetricsPacketV4 dealloc]
+ -[SRFaceMetricsPacketV4 faceIdentifier]
+ -[SRFaceMetricsPacketV4 gaze]
+ -[SRFaceMetricsPacketV4 geometryLeftEye]
+ -[SRFaceMetricsPacketV4 geometryRightEye]
+ -[SRFaceMetricsPacketV4 leftEyePitch]
+ -[SRFaceMetricsPacketV4 leftEyeYaw]
+ -[SRFaceMetricsPacketV4 partialFaceExpressions]
+ -[SRFaceMetricsPacketV4 rightEyePitch]
+ -[SRFaceMetricsPacketV4 rightEyeYaw]
+ -[SRFaceMetricsPacketV4 rotation]
+ -[SRFaceMetricsPacketV4 sessionIdentifier]
+ -[SRFaceMetricsPacketV4 trackingData]
+ -[SRFaceMetricsPacketV4 translation]
+ -[SRFaceMetricsPacketV4 version]
+ -[SRFaceMetricsPacketV4 wholeFaceExpressions]
+ -[SRFaceMetricsPacketV5 blendshapes]
+ -[SRFaceMetricsPacketV5 context]
+ -[SRFaceMetricsPacketV5 dealloc]
+ -[SRFaceMetricsPacketV5 faceIdentifier]
+ -[SRFaceMetricsPacketV5 gaze]
+ -[SRFaceMetricsPacketV5 geometryLeftEye]
+ -[SRFaceMetricsPacketV5 geometryRightEye]
+ -[SRFaceMetricsPacketV5 leftEyePitch]
+ -[SRFaceMetricsPacketV5 leftEyeYaw]
+ -[SRFaceMetricsPacketV5 partialFaceExpressions]
+ -[SRFaceMetricsPacketV5 rightEyePitch]
+ -[SRFaceMetricsPacketV5 rightEyeYaw]
+ -[SRFaceMetricsPacketV5 rotation]
+ -[SRFaceMetricsPacketV5 sessionIdentifier]
+ -[SRFaceMetricsPacketV5 trackingData]
+ -[SRFaceMetricsPacketV5 translation]
+ -[SRFaceMetricsPacketV5 version]
+ -[SRFaceMetricsPacketV5 wholeFaceExpressions]
+ -[SRFetchRequest _cursor]
+ -[SRFetchRequest set_cursor:]
+ -[SRFetchResult _cursor]
+ -[SRFetchResult initWithBytes:length:timestamp:metadata:configuration:cursor:sampleClass:]
+ -[SRFetchResult initWithData:timestamp:metadata:configuration:cursor:sampleClass:]
+ -[SRFetchResult set_cursor:]
+ -[SRPPGSampleArray initWithBinarySampleRepresentation:metadata:timestamp:]
+ -[SRPhotoplethysmogramAccelerometerSample copyWithZone:]
+ -[SRPhotoplethysmogramAccelerometerSample description]
+ -[SRPhotoplethysmogramAccelerometerSample encodeWithCoder:]
+ -[SRPhotoplethysmogramAccelerometerSample hash]
+ -[SRPhotoplethysmogramAccelerometerSample initWithCoder:]
+ -[SRPhotoplethysmogramAccelerometerSample initWithHAPPGAccelSample:]
+ -[SRPhotoplethysmogramAccelerometerSample initWithTimestamp:frequency:x:y:z:]
+ -[SRPhotoplethysmogramAccelerometerSample isEqual:]
+ -[SRPhotoplethysmogramAccelerometerSample isEqualToAccelSample:]
+ -[SRPhotoplethysmogramAccelerometerSample nanosecondsSinceStart]
+ -[SRPhotoplethysmogramAccelerometerSample samplingFrequency]
+ -[SRPhotoplethysmogramAccelerometerSample x]
+ -[SRPhotoplethysmogramAccelerometerSample y]
+ -[SRPhotoplethysmogramAccelerometerSample z]
+ -[SRPhotoplethysmogramOpticalSample activePhotodiodeIndexes]
+ -[SRPhotoplethysmogramOpticalSample backgroundNoiseOffset]
+ -[SRPhotoplethysmogramOpticalSample backgroundNoise]
+ -[SRPhotoplethysmogramOpticalSample conditions]
+ -[SRPhotoplethysmogramOpticalSample copyWithZone:]
+ -[SRPhotoplethysmogramOpticalSample dealloc]
+ -[SRPhotoplethysmogramOpticalSample description]
+ -[SRPhotoplethysmogramOpticalSample effectiveWavelength]
+ -[SRPhotoplethysmogramOpticalSample emitter]
+ -[SRPhotoplethysmogramOpticalSample encodeWithCoder:]
+ -[SRPhotoplethysmogramOpticalSample hash]
+ -[SRPhotoplethysmogramOpticalSample initWithCoder:]
+ -[SRPhotoplethysmogramOpticalSample initWithEmitter:photodiodes:signalIdentifier:nominalWavelength:effectiveWavelength:frequency:timestamp:normalizedReflectance:whiteNoise:pinkNoise:backgroundNoise:backgrounNoiseOffset:conditions:]
+ -[SRPhotoplethysmogramOpticalSample initWithHAPPGOpticalSample:]
+ -[SRPhotoplethysmogramOpticalSample isEqual:]
+ -[SRPhotoplethysmogramOpticalSample isEqualToOpticalSample:]
+ -[SRPhotoplethysmogramOpticalSample nanosecondsSinceStart]
+ -[SRPhotoplethysmogramOpticalSample nominalWavelength]
+ -[SRPhotoplethysmogramOpticalSample normalizedReflectance]
+ -[SRPhotoplethysmogramOpticalSample pinkNoise]
+ -[SRPhotoplethysmogramOpticalSample samplingFrequency]
+ -[SRPhotoplethysmogramOpticalSample signalIdentifier]
+ -[SRPhotoplethysmogramOpticalSample whiteNoise]
+ -[SRPhotoplethysmogramSample accelerometerSamples]
+ -[SRPhotoplethysmogramSample copyWithZone:]
+ -[SRPhotoplethysmogramSample dealloc]
+ -[SRPhotoplethysmogramSample description]
+ -[SRPhotoplethysmogramSample encodeWithCoder:]
+ -[SRPhotoplethysmogramSample hash]
+ -[SRPhotoplethysmogramSample initWithCoder:]
+ -[SRPhotoplethysmogramSample initWithHAPPGFrame:]
+ -[SRPhotoplethysmogramSample initWithStartDate:nsSinceStart:usage:opticalSamples:accelSamples:degrees:]
+ -[SRPhotoplethysmogramSample init]
+ -[SRPhotoplethysmogramSample isEqual:]
+ -[SRPhotoplethysmogramSample isEqualToPPGSample:]
+ -[SRPhotoplethysmogramSample nanosecondsSinceStart]
+ -[SRPhotoplethysmogramSample opticalSamples]
+ -[SRPhotoplethysmogramSample startDate]
+ -[SRPhotoplethysmogramSample temperature]
+ -[SRPhotoplethysmogramSample usage]
+ -[SRReaderFetchRequest cursor]
+ -[SRReaderFetchRequest setCursor:]
+ -[SRReaderLongTermBackend connection]
+ -[SRReaderLongTermBackend continueFetchRequest:samples:timestamp:cursor:fetchState:error:withCallback:]
+ -[SRReaderLongTermBackend dealloc]
+ -[SRReaderLongTermBackend fetch:withCallback:]
+ -[SRReaderLongTermBackend fetchDevices:reply:]
+ -[SRReaderLongTermBackend fetchReaderMetadata:reply:]
+ -[SRReaderLongTermBackend initWithSensor:xpcConnection:]
+ -[SRReaderLongTermBackend init]
+ -[SRReaderLongTermBackend setConnection:]
+ -[SRReaderLongTermBackend setupConnection]
+ -[SRReaderLongTermBackend startRecording:reply:]
+ -[SRReaderLongTermBackend stopRecording:reply:]
+ -[SRReaderSensorKitBackend connection]
+ -[SRReaderSensorKitBackend continueFetchRequest:from:to:withDatastoreFiles:callback:]
+ -[SRReaderSensorKitBackend datastore]
+ -[SRReaderSensorKitBackend dealloc]
+ -[SRReaderSensorKitBackend fetch:withCallback:]
+ -[SRReaderSensorKitBackend fetchDevices:reply:]
+ -[SRReaderSensorKitBackend fetchReaderMetadata:reply:]
+ -[SRReaderSensorKitBackend fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]
+ -[SRReaderSensorKitBackend initWithSensor:xpcConnection:]
+ -[SRReaderSensorKitBackend init]
+ -[SRReaderSensorKitBackend resetDatastoreFiles:]
+ -[SRReaderSensorKitBackend setConnection:]
+ -[SRReaderSensorKitBackend setupConnection]
+ -[SRReaderSensorKitBackend startRecording:reply:]
+ -[SRReaderSensorKitBackend stopRecording:reply:]
+ -[SRSensorDescription datastoreBackend]
+ -[SRSensorReader datastoreBackend]
+ -[SRSensorReader initWithSensor:sensorDescription:datastoreBackend:authorizationClient:bundleId:]
+ -[SRSensorReader setDatastoreBackend:]
+ GCC_except_table27
+ GCC_except_table35
+ GCC_except_table7
+ GCC_except_table9
+ _OBJC_CLASS_$_HAECGSample
+ _OBJC_CLASS_$_HAPPGSegment
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSUnitAcceleration
+ _OBJC_CLASS_$_NSUnitElectricPotentialDifference
+ _OBJC_CLASS_$_NSUnitFrequency
+ _OBJC_CLASS_$_NSUnitTemperature
+ _OBJC_CLASS_$_SRCursor
+ _OBJC_CLASS_$_SRECGSampleArray
+ _OBJC_CLASS_$_SRElectrocardiogramData
+ _OBJC_CLASS_$_SRElectrocardiogramSample
+ _OBJC_CLASS_$_SRElectrocardiogramSession
+ _OBJC_CLASS_$_SRFaceMetricsPacket
+ _OBJC_CLASS_$_SRFaceMetricsPacketV0
+ _OBJC_CLASS_$_SRFaceMetricsPacketV1
+ _OBJC_CLASS_$_SRFaceMetricsPacketV2
+ _OBJC_CLASS_$_SRFaceMetricsPacketV3
+ _OBJC_CLASS_$_SRFaceMetricsPacketV4
+ _OBJC_CLASS_$_SRFaceMetricsPacketV5
+ _OBJC_CLASS_$_SRPPGSampleArray
+ _OBJC_CLASS_$_SRPhotoplethysmogramAccelerometerSample
+ _OBJC_CLASS_$_SRPhotoplethysmogramOpticalSample
+ _OBJC_CLASS_$_SRPhotoplethysmogramSample
+ _OBJC_CLASS_$_SRReaderLongTermBackend
+ _OBJC_CLASS_$_SRReaderSensorKitBackend
+ _OBJC_IVAR_$_SRCursor._hmac
+ _OBJC_IVAR_$_SRCursor._payload
+ _OBJC_IVAR_$_SRElectrocardiogramData._flags
+ _OBJC_IVAR_$_SRElectrocardiogramData._val
+ _OBJC_IVAR_$_SRElectrocardiogramSample._data
+ _OBJC_IVAR_$_SRElectrocardiogramSample._freq
+ _OBJC_IVAR_$_SRElectrocardiogramSample._lead
+ _OBJC_IVAR_$_SRElectrocardiogramSample._session
+ _OBJC_IVAR_$_SRElectrocardiogramSample._time
+ _OBJC_IVAR_$_SRElectrocardiogramSession._identifier
+ _OBJC_IVAR_$_SRElectrocardiogramSession._sessionGuidance
+ _OBJC_IVAR_$_SRElectrocardiogramSession._state
+ _OBJC_IVAR_$_SRFaceMetricsPacketV0._faceIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV0._packet
+ _OBJC_IVAR_$_SRFaceMetricsPacketV1._faceIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV1._packet
+ _OBJC_IVAR_$_SRFaceMetricsPacketV2._context
+ _OBJC_IVAR_$_SRFaceMetricsPacketV2._faceIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV2._packet
+ _OBJC_IVAR_$_SRFaceMetricsPacketV2._sessionIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV3._context
+ _OBJC_IVAR_$_SRFaceMetricsPacketV3._faceIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV3._packet
+ _OBJC_IVAR_$_SRFaceMetricsPacketV3._sessionIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV4._context
+ _OBJC_IVAR_$_SRFaceMetricsPacketV4._faceIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV4._packet
+ _OBJC_IVAR_$_SRFaceMetricsPacketV4._sessionIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV5._context
+ _OBJC_IVAR_$_SRFaceMetricsPacketV5._faceIdentifier
+ _OBJC_IVAR_$_SRFaceMetricsPacketV5._packet
+ _OBJC_IVAR_$_SRFaceMetricsPacketV5._sessionIdentifier
+ _OBJC_IVAR_$_SRFetchRequest.__cursor
+ _OBJC_IVAR_$_SRFetchResult.__cursor
+ _OBJC_IVAR_$_SRPhotoplethysmogramAccelerometerSample._nanosecondsSinceStart
+ _OBJC_IVAR_$_SRPhotoplethysmogramAccelerometerSample._rawFrequency
+ _OBJC_IVAR_$_SRPhotoplethysmogramAccelerometerSample._rawX
+ _OBJC_IVAR_$_SRPhotoplethysmogramAccelerometerSample._rawY
+ _OBJC_IVAR_$_SRPhotoplethysmogramAccelerometerSample._rawZ
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._activePhotodiodeIndexes
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._backgroundNoise
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._backgroundNoiseOffset
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._conditions
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._emitter
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._nanosecondsSinceStart
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._normalizedReflectance
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._pinkNoise
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._rawEffectiveWavelength
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._rawFrequency
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._rawNominalWavelength
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._signalIdentifier
+ _OBJC_IVAR_$_SRPhotoplethysmogramOpticalSample._whiteNoise
+ _OBJC_IVAR_$_SRPhotoplethysmogramSample._accelerometerSamples
+ _OBJC_IVAR_$_SRPhotoplethysmogramSample._nanosecondsSinceStart
+ _OBJC_IVAR_$_SRPhotoplethysmogramSample._opticalSamples
+ _OBJC_IVAR_$_SRPhotoplethysmogramSample._startDate
+ _OBJC_IVAR_$_SRPhotoplethysmogramSample._temperature
+ _OBJC_IVAR_$_SRPhotoplethysmogramSample._usage
+ _OBJC_IVAR_$_SRReaderFetchRequest._cursor
+ _OBJC_IVAR_$_SRReaderLongTermBackend._connection
+ _OBJC_IVAR_$_SRReaderLongTermBackend._connectionDidInvalidate
+ _OBJC_IVAR_$_SRReaderLongTermBackend._sensor
+ _OBJC_IVAR_$_SRReaderSensorKitBackend._connection
+ _OBJC_IVAR_$_SRReaderSensorKitBackend._connectionDidInvalidate
+ _OBJC_IVAR_$_SRReaderSensorKitBackend._datastore
+ _OBJC_IVAR_$_SRReaderSensorKitBackend._deviceDetails
+ _OBJC_IVAR_$_SRReaderSensorKitBackend._nextDatastoreFiles
+ _OBJC_IVAR_$_SRReaderSensorKitBackend._sensor
+ _OBJC_IVAR_$_SRSensorDescription._datastoreBackend
+ _OBJC_IVAR_$_SRSensorReader._datastoreBackend
+ _OBJC_METACLASS_$_NSArray
+ _OBJC_METACLASS_$_SRCursor
+ _OBJC_METACLASS_$_SRECGSampleArray
+ _OBJC_METACLASS_$_SRElectrocardiogramData
+ _OBJC_METACLASS_$_SRElectrocardiogramSample
+ _OBJC_METACLASS_$_SRElectrocardiogramSession
+ _OBJC_METACLASS_$_SRFaceMetricsPacket
+ _OBJC_METACLASS_$_SRFaceMetricsPacketV0
+ _OBJC_METACLASS_$_SRFaceMetricsPacketV1
+ _OBJC_METACLASS_$_SRFaceMetricsPacketV2
+ _OBJC_METACLASS_$_SRFaceMetricsPacketV3
+ _OBJC_METACLASS_$_SRFaceMetricsPacketV4
+ _OBJC_METACLASS_$_SRFaceMetricsPacketV5
+ _OBJC_METACLASS_$_SRPPGSampleArray
+ _OBJC_METACLASS_$_SRPhotoplethysmogramAccelerometerSample
+ _OBJC_METACLASS_$_SRPhotoplethysmogramOpticalSample
+ _OBJC_METACLASS_$_SRPhotoplethysmogramSample
+ _OBJC_METACLASS_$_SRReaderLongTermBackend
+ _OBJC_METACLASS_$_SRReaderSensorKitBackend
+ _SRLogCursor
+ _SRLogFaceMetrics
+ _SRLogLongTermBackend
+ _SRLogSensorKitBackend
+ _SRPhotoplethysmogramOpticalSampleConditionSignalSaturation
+ _SRPhotoplethysmogramOpticalSampleConditionUnreliableNoise
+ _SRPhotoplethysmogramSampleUsageBackgroundSystem
+ _SRPhotoplethysmogramSampleUsageDeepBreathing
+ _SRPhotoplethysmogramSampleUsageForegroundBloodOxygen
+ _SRPhotoplethysmogramSampleUsageForegroundHeartRate
+ _SRSensorCardiovascularMetrics
+ _SRSensorElectrocardiogram
+ _SRSensorMobilityMetrics
+ _SRSensorPhotoplethysmogram
+ __OBJC_$_CATEGORY_NSArray_$_HAOpticalSamples
+ __OBJC_$_CLASS_METHODS_NSArray(HAOpticalSamples|HAAccelSamples)
+ __OBJC_$_CLASS_METHODS_SRCursor(_PayloadInspection)
+ __OBJC_$_CLASS_METHODS_SRElectrocardiogramData
+ __OBJC_$_CLASS_METHODS_SRElectrocardiogramSample
+ __OBJC_$_CLASS_METHODS_SRElectrocardiogramSession
+ __OBJC_$_CLASS_METHODS_SRFaceMetricsPacket
+ __OBJC_$_CLASS_METHODS_SRFaceMetricsPacketV0
+ __OBJC_$_CLASS_METHODS_SRFaceMetricsPacketV1
+ __OBJC_$_CLASS_METHODS_SRFaceMetricsPacketV2
+ __OBJC_$_CLASS_METHODS_SRFaceMetricsPacketV3
+ __OBJC_$_CLASS_METHODS_SRFaceMetricsPacketV4
+ __OBJC_$_CLASS_METHODS_SRFaceMetricsPacketV5
+ __OBJC_$_CLASS_METHODS_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_$_CLASS_METHODS_SRPhotoplethysmogramOpticalSample
+ __OBJC_$_CLASS_METHODS_SRPhotoplethysmogramSample
+ __OBJC_$_CLASS_METHODS_SRReaderLongTermBackend
+ __OBJC_$_CLASS_METHODS_SRReaderSensorKitBackend
+ __OBJC_$_CLASS_PROP_LIST_SRCursor
+ __OBJC_$_CLASS_PROP_LIST_SRElectrocardiogramData
+ __OBJC_$_CLASS_PROP_LIST_SRElectrocardiogramSample
+ __OBJC_$_CLASS_PROP_LIST_SRElectrocardiogramSession
+ __OBJC_$_CLASS_PROP_LIST_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_$_CLASS_PROP_LIST_SRPhotoplethysmogramOpticalSample
+ __OBJC_$_CLASS_PROP_LIST_SRPhotoplethysmogramSample
+ __OBJC_$_INSTANCE_METHODS_SRCursor(_PayloadInspection)
+ __OBJC_$_INSTANCE_METHODS_SRECGSampleArray
+ __OBJC_$_INSTANCE_METHODS_SRElectrocardiogramData
+ __OBJC_$_INSTANCE_METHODS_SRElectrocardiogramSample
+ __OBJC_$_INSTANCE_METHODS_SRElectrocardiogramSession
+ __OBJC_$_INSTANCE_METHODS_SRFaceMetricsPacketV0
+ __OBJC_$_INSTANCE_METHODS_SRFaceMetricsPacketV1
+ __OBJC_$_INSTANCE_METHODS_SRFaceMetricsPacketV2
+ __OBJC_$_INSTANCE_METHODS_SRFaceMetricsPacketV3
+ __OBJC_$_INSTANCE_METHODS_SRFaceMetricsPacketV4
+ __OBJC_$_INSTANCE_METHODS_SRFaceMetricsPacketV5
+ __OBJC_$_INSTANCE_METHODS_SRPPGSampleArray
+ __OBJC_$_INSTANCE_METHODS_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_$_INSTANCE_METHODS_SRPhotoplethysmogramOpticalSample
+ __OBJC_$_INSTANCE_METHODS_SRPhotoplethysmogramSample
+ __OBJC_$_INSTANCE_METHODS_SRReaderLongTermBackend
+ __OBJC_$_INSTANCE_METHODS_SRReaderSensorKitBackend
+ __OBJC_$_INSTANCE_VARIABLES_SRCursor
+ __OBJC_$_INSTANCE_VARIABLES_SRElectrocardiogramData
+ __OBJC_$_INSTANCE_VARIABLES_SRElectrocardiogramSample
+ __OBJC_$_INSTANCE_VARIABLES_SRElectrocardiogramSession
+ __OBJC_$_INSTANCE_VARIABLES_SRFaceMetricsPacketV0
+ __OBJC_$_INSTANCE_VARIABLES_SRFaceMetricsPacketV1
+ __OBJC_$_INSTANCE_VARIABLES_SRFaceMetricsPacketV2
+ __OBJC_$_INSTANCE_VARIABLES_SRFaceMetricsPacketV3
+ __OBJC_$_INSTANCE_VARIABLES_SRFaceMetricsPacketV4
+ __OBJC_$_INSTANCE_VARIABLES_SRFaceMetricsPacketV5
+ __OBJC_$_INSTANCE_VARIABLES_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_$_INSTANCE_VARIABLES_SRPhotoplethysmogramOpticalSample
+ __OBJC_$_INSTANCE_VARIABLES_SRPhotoplethysmogramSample
+ __OBJC_$_INSTANCE_VARIABLES_SRReaderLongTermBackend
+ __OBJC_$_INSTANCE_VARIABLES_SRReaderSensorKitBackend
+ __OBJC_$_PROP_LIST_SRECGSampleArray
+ __OBJC_$_PROP_LIST_SRElectrocardiogramData
+ __OBJC_$_PROP_LIST_SRElectrocardiogramSample
+ __OBJC_$_PROP_LIST_SRElectrocardiogramSession
+ __OBJC_$_PROP_LIST_SRFaceMetricsPacket
+ __OBJC_$_PROP_LIST_SRFaceMetricsPacketV0
+ __OBJC_$_PROP_LIST_SRFaceMetricsPacketV1
+ __OBJC_$_PROP_LIST_SRFaceMetricsPacketV2
+ __OBJC_$_PROP_LIST_SRFaceMetricsPacketV3
+ __OBJC_$_PROP_LIST_SRFaceMetricsPacketV4
+ __OBJC_$_PROP_LIST_SRFaceMetricsPacketV5
+ __OBJC_$_PROP_LIST_SRPPGSampleArray
+ __OBJC_$_PROP_LIST_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_$_PROP_LIST_SRPhotoplethysmogramOpticalSample
+ __OBJC_$_PROP_LIST_SRPhotoplethysmogramSample
+ __OBJC_$_PROP_LIST_SRReaderLongTermBackend
+ __OBJC_$_PROP_LIST_SRReaderSensorKitBackend
+ __OBJC_$_PROP_LIST_SRReaderStorageBackend
+ __OBJC_$_PROTOCOL_CLASS_METHODS_SRReaderStorageBackend
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRFaceMetricsPacket
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRReaderStorageBackend
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SensorKitLongTermStorageHelperProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRFaceMetricsPacket
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRReaderStorageBackend
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SensorKitLongTermStorageHelperProtocol
+ __OBJC_$_PROTOCOL_REFS_SRFaceMetricsPacket
+ __OBJC_$_PROTOCOL_REFS_SRReaderStorageBackend
+ __OBJC_CLASS_PROTOCOLS_$_SRCursor
+ __OBJC_CLASS_PROTOCOLS_$_SRECGSampleArray
+ __OBJC_CLASS_PROTOCOLS_$_SRElectrocardiogramData
+ __OBJC_CLASS_PROTOCOLS_$_SRElectrocardiogramSample
+ __OBJC_CLASS_PROTOCOLS_$_SRElectrocardiogramSession
+ __OBJC_CLASS_PROTOCOLS_$_SRFaceMetricsPacketV0
+ __OBJC_CLASS_PROTOCOLS_$_SRFaceMetricsPacketV1
+ __OBJC_CLASS_PROTOCOLS_$_SRFaceMetricsPacketV2
+ __OBJC_CLASS_PROTOCOLS_$_SRFaceMetricsPacketV3
+ __OBJC_CLASS_PROTOCOLS_$_SRFaceMetricsPacketV4
+ __OBJC_CLASS_PROTOCOLS_$_SRFaceMetricsPacketV5
+ __OBJC_CLASS_PROTOCOLS_$_SRPPGSampleArray
+ __OBJC_CLASS_PROTOCOLS_$_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_CLASS_PROTOCOLS_$_SRPhotoplethysmogramOpticalSample
+ __OBJC_CLASS_PROTOCOLS_$_SRPhotoplethysmogramSample
+ __OBJC_CLASS_PROTOCOLS_$_SRReaderLongTermBackend
+ __OBJC_CLASS_PROTOCOLS_$_SRReaderSensorKitBackend
+ __OBJC_CLASS_RO_$_SRCursor
+ __OBJC_CLASS_RO_$_SRECGSampleArray
+ __OBJC_CLASS_RO_$_SRElectrocardiogramData
+ __OBJC_CLASS_RO_$_SRElectrocardiogramSample
+ __OBJC_CLASS_RO_$_SRElectrocardiogramSession
+ __OBJC_CLASS_RO_$_SRFaceMetricsPacket
+ __OBJC_CLASS_RO_$_SRFaceMetricsPacketV0
+ __OBJC_CLASS_RO_$_SRFaceMetricsPacketV1
+ __OBJC_CLASS_RO_$_SRFaceMetricsPacketV2
+ __OBJC_CLASS_RO_$_SRFaceMetricsPacketV3
+ __OBJC_CLASS_RO_$_SRFaceMetricsPacketV4
+ __OBJC_CLASS_RO_$_SRFaceMetricsPacketV5
+ __OBJC_CLASS_RO_$_SRPPGSampleArray
+ __OBJC_CLASS_RO_$_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_CLASS_RO_$_SRPhotoplethysmogramOpticalSample
+ __OBJC_CLASS_RO_$_SRPhotoplethysmogramSample
+ __OBJC_CLASS_RO_$_SRReaderLongTermBackend
+ __OBJC_CLASS_RO_$_SRReaderSensorKitBackend
+ __OBJC_LABEL_PROTOCOL_$_SRFaceMetricsPacket
+ __OBJC_LABEL_PROTOCOL_$_SRReaderStorageBackend
+ __OBJC_LABEL_PROTOCOL_$_SensorKitLongTermStorageHelperClientProtocol
+ __OBJC_LABEL_PROTOCOL_$_SensorKitLongTermStorageHelperProtocol
+ __OBJC_METACLASS_RO_$_SRCursor
+ __OBJC_METACLASS_RO_$_SRECGSampleArray
+ __OBJC_METACLASS_RO_$_SRElectrocardiogramData
+ __OBJC_METACLASS_RO_$_SRElectrocardiogramSample
+ __OBJC_METACLASS_RO_$_SRElectrocardiogramSession
+ __OBJC_METACLASS_RO_$_SRFaceMetricsPacket
+ __OBJC_METACLASS_RO_$_SRFaceMetricsPacketV0
+ __OBJC_METACLASS_RO_$_SRFaceMetricsPacketV1
+ __OBJC_METACLASS_RO_$_SRFaceMetricsPacketV2
+ __OBJC_METACLASS_RO_$_SRFaceMetricsPacketV3
+ __OBJC_METACLASS_RO_$_SRFaceMetricsPacketV4
+ __OBJC_METACLASS_RO_$_SRFaceMetricsPacketV5
+ __OBJC_METACLASS_RO_$_SRPPGSampleArray
+ __OBJC_METACLASS_RO_$_SRPhotoplethysmogramAccelerometerSample
+ __OBJC_METACLASS_RO_$_SRPhotoplethysmogramOpticalSample
+ __OBJC_METACLASS_RO_$_SRPhotoplethysmogramSample
+ __OBJC_METACLASS_RO_$_SRReaderLongTermBackend
+ __OBJC_METACLASS_RO_$_SRReaderSensorKitBackend
+ __OBJC_PROTOCOL_$_SRFaceMetricsPacket
+ __OBJC_PROTOCOL_$_SRReaderStorageBackend
+ __OBJC_PROTOCOL_$_SensorKitLongTermStorageHelperClientProtocol
+ __OBJC_PROTOCOL_$_SensorKitLongTermStorageHelperProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SensorKitLongTermStorageHelperClientProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SensorKitLongTermStorageHelperProtocol
+ ___103-[SRReaderSensorKitBackend fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]_block_invoke
+ ___103-[SRReaderSensorKitBackend fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]_block_invoke.68
+ ___103-[SRReaderSensorKitBackend fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]_block_invoke.69
+ ___32-[SRSensorWriter setMonitoring:]_block_invoke.136
+ ___34-[SRAuthorizationClient syncProxy]_block_invoke.33
+ ___42-[SRDebugInfoClient dumpClientsWithReply:]_block_invoke.30
+ ___42-[SRReaderLongTermBackend setupConnection]_block_invoke
+ ___42-[SRReaderLongTermBackend setupConnection]_block_invoke.18
+ ___43-[SRDebugInfoClient dumpDefaultsWithReply:]_block_invoke.37
+ ___43-[SRReaderSensorKitBackend setupConnection]_block_invoke
+ ___43-[SRReaderSensorKitBackend setupConnection]_block_invoke.52
+ ___45-[SRDebugInfoClient dumpStateCacheWithReply:]_block_invoke.32
+ ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.146
+ ___46-[SRReaderLongTermBackend fetch:withCallback:]_block_invoke
+ ___46-[SRReaderLongTermBackend fetch:withCallback:]_block_invoke.21
+ ___46-[SRReaderLongTermBackend fetch:withCallback:]_block_invoke_2
+ ___46-[SRReaderLongTermBackend fetchDevices:reply:]_block_invoke
+ ___46-[SRReaderLongTermBackend fetchDevices:reply:]_block_invoke.23
+ ___47-[SRDebugInfoClient datastoreListingWithReply:]_block_invoke.33
+ ___47-[SRReaderSensorKitBackend fetch:withCallback:]_block_invoke
+ ___47-[SRReaderSensorKitBackend fetch:withCallback:]_block_invoke.58
+ ___47-[SRReaderSensorKitBackend fetch:withCallback:]_block_invoke.60
+ ___47-[SRReaderSensorKitBackend fetchDevices:reply:]_block_invoke
+ ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.148
+ ___48-[SRReaderSensorKitBackend stopRecording:reply:]_block_invoke
+ ___49-[SRDebugInfoClient dumpConfigurationsWithReply:]_block_invoke.36
+ ___49-[SRReaderSensorKitBackend startRecording:reply:]_block_invoke
+ ___49-[SRReaderSensorKitBackend startRecording:reply:]_block_invoke.70
+ ___54-[SRReaderSensorKitBackend fetchReaderMetadata:reply:]_block_invoke
+ ___70-[SRDebugInfoClient fetchDeviceInformationForDeviceIdentifiers:reply:]_block_invoke
+ ___block_descriptor_48_e8_32o40b_e77_B72?0^v8Q16d24"NSDictionary"32"NSDictionary"40Q48"SRCursor"56"NSError"64ls40l8s32l8
+ ___block_descriptor_48_e8_32o40w_e77_B72?0^v8Q16d24"NSDictionary"32"NSDictionary"40Q48"SRCursor"56"NSError"64lw40l8s32l8
+ ___block_descriptor_56_e8_32o40b48w_e47_v48?0"NSData"8d16Q24"SRCursor"32"NSError"40lw48l8s32l8s40l8
+ ___block_literal_global.251
+ ___block_literal_global.35
+ ___swift_memcpy32_8
+ ___swift_noop_void_return
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_SensorKit
+ __swift_FORCE_LOAD_$_swiftShazamKit
+ __swift_FORCE_LOAD_$_swiftShazamKit_$_SensorKit
+ __unnamed_array_storage.11
+ __unnamed_array_storage.213
+ __unnamed_array_storage.216
+ __unnamed_array_storage.219
+ __unnamed_array_storage.222
+ __unnamed_array_storage.226
+ __unnamed_array_storage.230
+ __unnamed_array_storage.233
+ __unnamed_array_storage.236
+ __unnamed_array_storage.239
+ __unnamed_array_storage.253
+ __unnamed_array_storage.256
+ __unnamed_array_storage.260
+ __unnamed_array_storage.263
+ __unnamed_array_storage.266
+ __unnamed_array_storage.269
+ __unnamed_array_storage.273
+ __unnamed_array_storage.277
+ __unnamed_array_storage.280
+ __unnamed_array_storage.283
+ __unnamed_array_storage.286
+ __unnamed_array_storage.301
+ __unnamed_array_storage.304
+ __unnamed_array_storage.308
+ __unnamed_array_storage.311
+ __unnamed_array_storage.314
+ __unnamed_array_storage.317
+ __unnamed_array_storage.321
+ __unnamed_array_storage.325
+ __unnamed_array_storage.328
+ __unnamed_array_storage.331
+ __unnamed_array_storage.334
+ __unnamed_array_storage.346
+ __unnamed_array_storage.349
+ __unnamed_array_storage.352
+ __unnamed_array_storage.355
+ __unnamed_array_storage.359
+ __unnamed_array_storage.363
+ __unnamed_array_storage.366
+ __unnamed_array_storage.369
+ __unnamed_array_storage.372
+ __unnamed_array_storage.384
+ __unnamed_array_storage.387
+ __unnamed_array_storage.390
+ __unnamed_array_storage.393
+ __unnamed_array_storage.397
+ __unnamed_array_storage.401
+ __unnamed_array_storage.404
+ __unnamed_array_storage.407
+ __unnamed_array_storage.410
+ __unnamed_array_storage.50
+ __unnamed_array_storage.53
+ __unnamed_array_storage.56
+ __unnamed_array_storage.59
+ __unnamed_array_storage.62
+ __unnamed_array_storage.65
+ __unnamed_array_storage.68
+ __unnamed_array_storage.71
+ __unnamed_array_storage.74
+ _objc_msgSend$_cursor
+ _objc_msgSend$accelSamples
+ _objc_msgSend$accelerometerSamples
+ _objc_msgSend$activePhotodiodeIndexes
+ _objc_msgSend$backgroundNoise
+ _objc_msgSend$backgroundNoiseOffset
+ _objc_msgSend$blendshapes
+ _objc_msgSend$celsius
+ _objc_msgSend$conditions
+ _objc_msgSend$connectionToEndpoint
+ _objc_msgSend$continueFetchRequest:samples:timestamp:cursor:fetchState:error:withCallback:
+ _objc_msgSend$data
+ _objc_msgSend$datastoreBackend
+ _objc_msgSend$date
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$degreesCelsius
+ _objc_msgSend$ecgData
+ _objc_msgSend$effectiveWavelength
+ _objc_msgSend$emitter
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$estimatedDeviceNoiseOffset
+ _objc_msgSend$estimatedDevicePinkNoise
+ _objc_msgSend$estimatedDeviceWhiteNoise
+ _objc_msgSend$faceIdentifier
+ _objc_msgSend$fetch:withCallback:
+ _objc_msgSend$fetchAllDevices:reply:
+ _objc_msgSend$fetchCardioSamples:reply:
+ _objc_msgSend$fetchDeviceInformationForDeviceIdentifiers:reply:
+ _objc_msgSend$fetchDevices:reply:
+ _objc_msgSend$fetchMobilitySamples:reply:
+ _objc_msgSend$flags
+ _objc_msgSend$frameEnumerator
+ _objc_msgSend$frequency
+ _objc_msgSend$gaze
+ _objc_msgSend$geometryLeftEye
+ _objc_msgSend$geometryRightEye
+ _objc_msgSend$gravity
+ _objc_msgSend$hardwareSetting
+ _objc_msgSend$hertz
+ _objc_msgSend$initWithBinaryRepresentation:
+ _objc_msgSend$initWithBinarySampleRepresentation:metadata:
+ _objc_msgSend$initWithBitfield:
+ _objc_msgSend$initWithBytes:length:timestamp:metadata:configuration:cursor:sampleClass:
+ _objc_msgSend$initWithData:timestamp:metadata:configuration:cursor:sampleClass:
+ _objc_msgSend$initWithEmitter:photodiodes:signalIdentifier:nominalWavelength:effectiveWavelength:frequency:timestamp:normalizedReflectance:whiteNoise:pinkNoise:backgroundNoise:backgrounNoiseOffset:conditions:
+ _objc_msgSend$initWithFlags:value:
+ _objc_msgSend$initWithHAECGSample:
+ _objc_msgSend$initWithHAPPGAccelSample:
+ _objc_msgSend$initWithHAPPGFrame:
+ _objc_msgSend$initWithHAPPGOpticalSample:
+ _objc_msgSend$initWithSensor:sensorDescription:datastoreBackend:authorizationClient:bundleId:
+ _objc_msgSend$initWithSensor:xpcConnection:
+ _objc_msgSend$initWithStartDate:nsSinceStart:usage:opticalSamples:accelSamples:degrees:
+ _objc_msgSend$initWithState:sessionGuidance:identifier:
+ _objc_msgSend$initWithTimestamp:frequency:session:lead:data:
+ _objc_msgSend$initWithTimestamp:frequency:x:y:z:
+ _objc_msgSend$isEqualToAccelSample:
+ _objc_msgSend$isEqualToData:
+ _objc_msgSend$isEqualToECGData:
+ _objc_msgSend$isEqualToOpticalSample:
+ _objc_msgSend$isEqualToPPGSample:
+ _objc_msgSend$isEqualToSample:
+ _objc_msgSend$isEqualToSession:
+ _objc_msgSend$lead
+ _objc_msgSend$leftEyePitch
+ _objc_msgSend$leftEyeYaw
+ _objc_msgSend$microvolts
+ _objc_msgSend$nanometers
+ _objc_msgSend$nanosecondsSinceStart
+ _objc_msgSend$noiseIsUnreliable
+ _objc_msgSend$nominalWavelength
+ _objc_msgSend$normalizedReflectance
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$opticalSamples
+ _objc_msgSend$packetWithData:
+ _objc_msgSend$packetWithHAFacialMetricsPacket:
+ _objc_msgSend$photodiodes
+ _objc_msgSend$pinkNoise
+ _objc_msgSend$rightEyePitch
+ _objc_msgSend$rightEyeYaw
+ _objc_msgSend$rotation
+ _objc_msgSend$samplingFrequency
+ _objc_msgSend$saturated
+ _objc_msgSend$session
+ _objc_msgSend$sessionGuidance
+ _objc_msgSend$setCursor:
+ _objc_msgSend$setDatastoreBackend:
+ _objc_msgSend$set_cursor:
+ _objc_msgSend$signalIdentifier
+ _objc_msgSend$sr_arrayWithHAAccelSamples:
+ _objc_msgSend$sr_arrayWithHAOpticalSamples:
+ _objc_msgSend$state
+ _objc_msgSend$temperature
+ _objc_msgSend$temperatureSample
+ _objc_msgSend$trackingData
+ _objc_msgSend$translation
+ _objc_msgSend$usage
+ _objc_msgSend$whiteNoise
+ _objc_msgSend$x
+ _objc_msgSend$y
+ _objc_msgSend$z
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _swift_retain
+ _symbolic Sd
+ _symbolic So33SRPhotoplethysmogramOpticalSampleC
+ _symbolic _____ So33SRPhotoplethysmogramOpticalSampleC9SensorKitE10NoiseTermsV
- +[SRSensorReader clientInterface]
- +[SRSensorReader connectionToDaemon]
- +[SRSensorReader remoteInterface]
- +[SRSensorReaderClient readerClientWithReader:]
- -[SRFaceMetrics convertHAFacialMetricsPacketToTrackedFaceDict:]
- -[SRFetchResult initWithData:timestamp:metadata:configuration:sampleClass:]
- -[SRSensorReader connectionDidInvalidate]
- -[SRSensorReader connection]
- -[SRSensorReader continueFetchRequest:from:to:withDatastoreFiles:callback:]
- -[SRSensorReader daemonNotificationDaemonDidStart:]
- -[SRSensorReader datastore]
- -[SRSensorReader fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]
- -[SRSensorReader fetchSampleBytesFrom:to:inSegment:fetchRequest:sampleCallback:]
- -[SRSensorReader initWithSensor:xpcConnection:daemonNotification:authorizationClient:bundleId:]
- -[SRSensorReader nextDatastoreFiles]
- -[SRSensorReader resetDatastoreFiles:]
- -[SRSensorReader setConnection:]
- -[SRSensorReader setConnectionDidInvalidate:]
- -[SRSensorReader setNextDatastoreFiles:]
- -[SRSensorReader setupConnection]
- -[SRSensorReaderClient initWithReader:]
- -[SRSensorReaderClient reader]
- -[SRSensorReaderClient setReader:]
- GCC_except_table19
- GCC_except_table42
- GCC_except_table54
- GCC_except_table60
- _OBJC_IVAR_$_SRSensorReader._connection
- _OBJC_IVAR_$_SRSensorReader._connectionDidInvalidate
- _OBJC_IVAR_$_SRSensorReader._daemonNotification
- _OBJC_IVAR_$_SRSensorReader._datastore
- _OBJC_IVAR_$_SRSensorReader._deviceDetails
- _OBJC_IVAR_$_SRSensorReader._nextDatastoreFiles
- __OBJC_$_CLASS_METHODS_SRSensorReaderClient
- __OBJC_$_PROP_LIST_SRSensorReaderClient
- ___24-[SRSensorReader fetch:]_block_invoke.166
- ___24-[SRSensorReader fetch:]_block_invoke.167
- ___31-[SRSensorReader fetchDevices:]_block_invoke.184
- ___32-[SRSensorWriter setMonitoring:]_block_invoke.135
- ___33-[SRSensorReader setupConnection]_block_invoke
- ___33-[SRSensorReader setupConnection]_block_invoke.77
- ___34-[SRAuthorizationClient syncProxy]_block_invoke.32
- ___37-[SRSensorReader fetchReaderMetadata]_block_invoke.138
- ___42-[SRDebugInfoClient dumpClientsWithReply:]_block_invoke.27
- ___43-[SRDebugInfoClient dumpDefaultsWithReply:]_block_invoke.34
- ___45-[SRDebugInfoClient dumpStateCacheWithReply:]_block_invoke.29
- ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.145
- ___47-[SRDebugInfoClient datastoreListingWithReply:]_block_invoke.30
- ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.146
- ___49-[SRDebugInfoClient dumpConfigurationsWithReply:]_block_invoke.33
- ___53-[SRSensorReader stopRecordingWithCompletionHandler:]_block_invoke
- ___53-[SRSensorReader stopRecordingWithCompletionHandler:]_block_invoke.182
- ___75-[SRSensorReader _startRecordingWithSensorConfiguration:completionHandler:]_block_invoke
- ___75-[SRSensorReader _startRecordingWithSensorConfiguration:completionHandler:]_block_invoke.181
- ___93-[SRSensorReader fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]_block_invoke
- ___93-[SRSensorReader fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]_block_invoke.172
- ___93-[SRSensorReader fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:]_block_invoke.173
- ___block_descriptor_56_e8_32o40o48w_e64_B64?0^v8Q16d24"NSDictionary"32"NSDictionary"40Q48"NSError"56lw48l8s32l8s40l8
- ___block_literal_global.250
- ___block_literal_global.34
- __unnamed_array_storage.194
- __unnamed_array_storage.197
- __unnamed_array_storage.200
- __unnamed_array_storage.203
- __unnamed_array_storage.212
- __unnamed_array_storage.215
- _extractPartialFaceExpressions
- _extractWholeFaceExpressions
- _objc_msgSend$arrayWithObjects:
- _objc_msgSend$continueFetchRequest:from:to:withDatastoreFiles:callback:
- _objc_msgSend$fetchAllDevices:idOnly:reply:
- _objc_msgSend$fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:
- _objc_msgSend$fetchSampleBytesFrom:to:inSegment:fetchRequest:sampleCallback:
- _objc_msgSend$initWithData:timestamp:metadata:configuration:sampleClass:
- _objc_msgSend$initWithReader:
- _objc_msgSend$initWithSensor:xpcConnection:daemonNotification:authorizationClient:bundleId:
- _objc_msgSend$reader
- _objc_msgSend$readerClientWithReader:
- _objc_msgSend$setObject:atIndexedSubscript:
- _objc_msgSend$setReader:
CStrings:
+ "%@ (%p)"
+ "%@ (%p): emitter: %ld, photodiodes: %@, signalIdentifier: %ld, nominalWavelength: %f, effectiveWavelength: %f, frequency: %f, nanosecondsSinceStart: %lld, normalizedReflectance: %@, whiteNoise: %@, pinkNoise: %@, backgroundNoise: %@, noiseOffset: %@, conditions: %@"
+ "%@ (%p): flags: %lu, value: %@"
+ "%@ (%p): from: %f, to: %f, cursor: %@, %@"
+ "%@ (%p): name: %@, authService: %@, writer: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons: %@, storageBackend: %ld"
+ "%@ (%p): nanosecondsSinceStart: %lld, frequency: %f, x: %f, y: %f, z: %f"
+ "%@ (%p): startDate: %@, nanosecondsSinceStart: %lld, usage: %@, opticalSamples: %@, accelerometerSamples: %@, temperature: %@"
+ "%@ (%p): state: %ld, guidance: %ld, identifier: %@"
+ "%@ (%p): timestamp: %@, frequency: %@, session: %@, lead: %ld, data: %@"
+ "@\"<SRReaderStorageBackend>\""
+ "@\"NSArray\"16@0:8"
+ "@\"NSIndexSet\""
+ "@\"NSUUID\"16@0:8"
+ "@\"NSXPCConnection\"16@0:8"
+ "@\"NSXPCInterface\"16@0:8"
+ "@\"SRCursor\""
+ "@\"SRCursor\"16@0:8"
+ "@\"SRElectrocardiogramSession\""
+ "@\"SRReaderSensorKitBackend\""
+ "@120@0:8q16@24q32d40d48d56q64@72@80@88@96@104@112"
+ "@24@0:8^{?=IIIQQQdQd{?=[3[3f]][3f]}[3f][3f]ffff[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}}16"
+ "@24@0:8^{?=IIIQdQd[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}}16"
+ "@24@0:8^{?=IIIQdQd{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}}16"
+ "@24@0:8^{?=III[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}}16"
+ "@24@0:8^{?=II[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}}16"
+ "@24@0:8^{?=I[16C]IQQQdQd{?=[3[3f]][3f]}[3f][3f]ffff[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}}16"
+ "@32@0:8#16^@24"
+ "@32@0:8Q16d24"
+ "@40@0:8q16q24@32"
+ "@56@0:8d16d24@32q40@48"
+ "@56@0:8q16d24d32d40d48"
+ "@64@0:8@16d24@32@40@48#56"
+ "@64@0:8@16q24@32@40@48@56"
+ "@72@0:8^v16Q24d32@40@48@56#64"
+ "B72@?0^v8Q16d24@\"NSDictionary\"32@\"NSDictionary\"40Q48@\"SRCursor\"56@\"NSError\"64"
+ "Backend is for sensor %{public}@ but fetching for sensor %{public}@"
+ "BackgroundSystem"
+ "Cursor"
+ "DeepBreathing"
+ "Failed to create SRFaceMetricsPacket"
+ "Failed to find initializer to create SRFaceMetricsPacket, data length:%lu"
+ "Failed to generate V0 face metrics, because of empty face indentifier"
+ "Failed to generate V0 face metrics, because of empty neutral face geometry"
+ "Failed to generate V1 face metrics, because of empty face indentifier"
+ "Failed to generate V1 face metrics, because of empty neutral face geometry"
+ "Failed to generate V2 face metrics, because of empty face indentifier"
+ "Failed to generate V2 face metrics, because of empty neutral face geometry"
+ "Failed to generate V2 face metrics, because of empty session identifiers"
+ "Failed to generate V3 face metrics, because of empty face indentifier"
+ "Failed to generate V3 face metrics, because of empty neutral face geometry"
+ "Failed to generate V3 face metrics, because of empty session identifiers"
+ "Failed to generate V4 face metrics, because of empty context"
+ "Failed to generate V4 face metrics, because of empty face indentifier"
+ "Failed to generate V4 face metrics, because of empty neutral face geometry"
+ "Failed to generate V4 face metrics, because of empty session identifiers"
+ "Failed to generate V5 face metrics, because of empty context"
+ "Failed to generate V5 face metrics, because of empty face indentifier"
+ "Failed to generate V5 face metrics, because of empty neutral face geometry"
+ "Failed to generate V5 face metrics, because of empty session identifiers"
+ "ForegroundBloodOxygen"
+ "ForegroundHeartRate"
+ "HAAccelSamples"
+ "HAOpticalSamples"
+ "Invalid input data for V0"
+ "Invalid input data for V1"
+ "Invalid input data for V2"
+ "Invalid input data for V3"
+ "Invalid input data for V4"
+ "Invalid input data for V5"
+ "Legacy data support: got %@ version of HAFacialMetricsPacket"
+ "SRCursor"
+ "SRCursor.m"
+ "SRECGSampleArray"
+ "SRElectrocardiogramData"
+ "SRElectrocardiogramSample"
+ "SRElectrocardiogramSample.m"
+ "SRElectrocardiogramSession"
+ "SRElectrocardiogramSession.m"
+ "SRFaceMetricsPacket"
+ "SRFaceMetricsPacket.m"
+ "SRFaceMetricsPacketV0"
+ "SRFaceMetricsPacketV1"
+ "SRFaceMetricsPacketV2"
+ "SRFaceMetricsPacketV3"
+ "SRFaceMetricsPacketV4"
+ "SRFaceMetricsPacketV5"
+ "SRLogFaceMetricsPacket"
+ "SRLogLongTermBackend"
+ "SRPPGSampleArray"
+ "SRPhotoplethysmogramAccelerometerSample"
+ "SRPhotoplethysmogramOpticalSample"
+ "SRPhotoplethysmogramSample"
+ "SRPhotoplethysmogramSample.m"
+ "SRReaderLongTermBackend"
+ "SRReaderLongTermBackend.m"
+ "SRReaderSensorKitBackend"
+ "SRReaderSensorKitBackend.m"
+ "SRReaderStorageBackend"
+ "SensorKitLongTermStorageHelperClientProtocol"
+ "SensorKitLongTermStorageHelperProtocol"
+ "SensorKitReaderBackend"
+ "SignalSaturation"
+ "StorageBackend"
+ "T@\"<SRReaderStorageBackend>\",&,N,V_datastoreBackend"
+ "T@\"NSArray\",R,&,N"
+ "T@\"NSArray\",R,C,N,V_accelerometerSamples"
+ "T@\"NSArray\",R,C,N,V_conditions"
+ "T@\"NSArray\",R,C,N,V_data"
+ "T@\"NSArray\",R,C,N,V_opticalSamples"
+ "T@\"NSArray\",R,C,N,V_usage"
+ "T@\"NSData\",R,&,N"
+ "T@\"NSDate\",R,N,V_startDate"
+ "T@\"NSDictionary\",R,&,N"
+ "T@\"NSIndexSet\",R,N,V_activePhotodiodeIndexes"
+ "T@\"NSMeasurement\",R,N,V_temperature"
+ "T@\"NSNumber\",R,N,V_backgroundNoise"
+ "T@\"NSNumber\",R,N,V_backgroundNoiseOffset"
+ "T@\"NSNumber\",R,N,V_normalizedReflectance"
+ "T@\"NSNumber\",R,N,V_pinkNoise"
+ "T@\"NSNumber\",R,N,V_whiteNoise"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",R,&,N"
+ "T@\"NSXPCConnection\",R,N"
+ "T@\"SRCursor\",&,N"
+ "T@\"SRCursor\",&,N,V__cursor"
+ "T@\"SRCursor\",&,N,V_cursor"
+ "T@\"SRElectrocardiogramSession\",R,N,V_session"
+ "TQ,R,N"
+ "TQ,R,N,V_flags"
+ "Tq,R,N,V_datastoreBackend"
+ "Tq,R,N,V_emitter"
+ "Tq,R,N,V_lead"
+ "Tq,R,N,V_nanosecondsSinceStart"
+ "Tq,R,N,V_sessionGuidance"
+ "Tq,R,N,V_signalIdentifier"
+ "Tq,R,N,V_state"
+ "Trying to fetch long term data for a sensor %{public}@ that doesn't support it"
+ "UnreliableNoise"
+ "[%@{public}@] Fetch is complete"
+ "[%{public}@] Failed to get proxy object for fetch because %{public}@"
+ "[%{public}@] Failed to get proxy object for fetchDevices because %{public}@"
+ "[%{public}@] Requesting data from new cursor %{public}@"
+ "^{?=IIIQQQdQd{?=[3[3f]][3f]}[3f][3f]ffff[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}}"
+ "^{?=IIIQdQd[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}}"
+ "^{?=IIIQdQd{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}}"
+ "^{?=III[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}}"
+ "^{?=II[501f]{?=[3[3f]][3f]}[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=ffffffffff}{?=ffffffff}}}"
+ "^{?=I[16C]IQQQdQd{?=[3[3f]][3f]}[3f][3f]ffff[3f]{?=fffffffffffffffffffffffffffffffffffffffffffffffffff}{?={?=fffffff}{?=ffffffff}}}"
+ "_PayloadInspection"
+ "__cursor"
+ "_accelerometerSamples"
+ "_activePhotodiodeIndexes"
+ "_backgroundNoise"
+ "_backgroundNoiseOffset"
+ "_conditions"
+ "_cursor"
+ "_data"
+ "_datastoreBackend"
+ "_emitter"
+ "_faceIdentifier"
+ "_flags"
+ "_freq"
+ "_hmac"
+ "_lead"
+ "_nanosecondsSinceStart"
+ "_normalizedReflectance"
+ "_opticalSamples"
+ "_packet"
+ "_payload"
+ "_payloadOfClass:error:"
+ "_pinkNoise"
+ "_rawEffectiveWavelength"
+ "_rawFrequency"
+ "_rawNominalWavelength"
+ "_rawX"
+ "_rawY"
+ "_rawZ"
+ "_session"
+ "_sessionGuidance"
+ "_signalIdentifier"
+ "_startDate"
+ "_state"
+ "_temperature"
+ "_time"
+ "_usage"
+ "_val"
+ "_whiteNoise"
+ "accelSamples"
+ "accelerometerSamples"
+ "activePhotodiodeIndexes"
+ "backgroundNoise"
+ "backgroundNoiseOffset"
+ "celsius"
+ "com.apple.SensorKit.ECG"
+ "com.apple.SensorKit.LongTermStorageHelper"
+ "com.apple.SensorKit.PPG"
+ "com.apple.SensorKit.cardioMetrics"
+ "com.apple.SensorKit.mobilityMetrics"
+ "conditions"
+ "connectionToEndpoint"
+ "continueFetchRequest:samples:timestamp:cursor:fetchState:error:withCallback:"
+ "cursor"
+ "data"
+ "datastoreBackend"
+ "date"
+ "decodeInt64ForKey:"
+ "degreesCelsius"
+ "ecgData"
+ "effectiveWavelength"
+ "emitter"
+ "encodeInt64:forKey:"
+ "estimatedDeviceNoiseOffset"
+ "estimatedDevicePinkNoise"
+ "estimatedDeviceWhiteNoise"
+ "faceIdentifier"
+ "fetch:withCallback:"
+ "fetchAllDevices:reply:"
+ "fetchCardioSamples:reply:"
+ "fetchDeviceInformationForDeviceIdentifiers:reply:"
+ "fetchDevices:reply:"
+ "fetchMobilitySamples:reply:"
+ "fetchReaderMetadata: is not supported for the long term storage backend"
+ "flags"
+ "frameEnumerator"
+ "frequency"
+ "geometryLeftEye"
+ "geometryRightEye"
+ "gravity"
+ "hardwareSetting"
+ "hertz"
+ "hmac"
+ "initWithBinaryRepresentation:"
+ "initWithBinarySampleRepresentation:metadata:"
+ "initWithBitfield:"
+ "initWithBytes:length:timestamp:metadata:configuration:cursor:sampleClass:"
+ "initWithData:timestamp:metadata:configuration:cursor:sampleClass:"
+ "initWithEmitter:photodiodes:signalIdentifier:nominalWavelength:effectiveWavelength:frequency:timestamp:normalizedReflectance:whiteNoise:pinkNoise:backgroundNoise:backgrounNoiseOffset:conditions:"
+ "initWithFlags:value:"
+ "initWithHAECGSample:"
+ "initWithHAPPGAccelSample:"
+ "initWithHAPPGFrame:"
+ "initWithHAPPGOpticalSample:"
+ "initWithSensor:sensorDescription:datastoreBackend:authorizationClient:bundleId:"
+ "initWithSensor:xpcConnection:"
+ "initWithStartDate:nsSinceStart:usage:opticalSamples:accelSamples:degrees:"
+ "initWithState:sessionGuidance:identifier:"
+ "initWithTimestamp:frequency:session:lead:data:"
+ "initWithTimestamp:frequency:x:y:z:"
+ "isEqualToAccelSample:"
+ "isEqualToData:"
+ "isEqualToECGData:"
+ "isEqualToOpticalSample:"
+ "isEqualToPPGSample:"
+ "isEqualToSample:"
+ "isEqualToSession:"
+ "lead"
+ "leftEyePitch"
+ "leftEyeYaw"
+ "microvolts"
+ "nanometers"
+ "nanosecondsSinceStart"
+ "noiseIsUnreliable"
+ "nominalWavelength"
+ "normalizedReflectance"
+ "numberWithLongLong:"
+ "opticalSamples"
+ "packetWithData:"
+ "packetWithHAFacialMetricsPacket:"
+ "payload"
+ "photodiodes"
+ "pinkNoise"
+ "rightEyePitch"
+ "rightEyeYaw"
+ "samplingFrequency"
+ "saturated"
+ "session"
+ "sessionGuidance"
+ "setCursor:"
+ "setDatastoreBackend:"
+ "set_cursor:"
+ "signalIdentifier"
+ "sr_arrayWithHAAccelSamples:"
+ "sr_arrayWithHAOpticalSamples:"
+ "state"
+ "temperature"
+ "temperatureSample"
+ "trackingData"
+ "usage"
+ "v24@0:8@\"SRCursor\"16"
+ "v32@0:8@\"<SRRequestFetching>\"16@?<v@?@\"NSData\"dQ@\"SRCursor\"@\"NSError\">24"
+ "v32@0:8@\"<SRRequestReading>\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"SRReaderFetchRequest\"16@?<B@?^vQd@\"NSDictionary\"@\"NSDictionary\"Q@\"SRCursor\"@\"NSError\">24"
+ "v48@?0@\"NSData\"8d16Q24@\"SRCursor\"32@\"NSError\"40"
+ "v72@0:8@16@24d32@40Q48@56@?64"
+ "whiteNoise"
+ "z"
- "%@ (%p): from: %f, to: %f, %@"
- "%@ (%p): name: %@, authService: %@, writer: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons; %@"
- "@\"SRSensorReader\""
- "@56@0:8@16d24@32@40#48"
- "B64@?0^v8Q16d24@\"NSDictionary\"32@\"NSDictionary\"40Q48@\"NSError\"56"
- "Failed to generate face tracking data for V0"
- "Failed to generate face tracking data for V1"
- "Failed to generate face tracking data for V2"
- "Failed to generate face tracking data for V3"
- "Failed to generate face tracking data for V4"
- "Failed to generate face tracking data for V5"
- "Failed to read neutral face geometry"
- "Failed to read session identifier"
- "Got unknown version of HAFacialMetricsPacket %i"
- "Legacy data support: got %i version of HAFacialMetricsPacket"
- "T@\"SRSensorReader\",W,V_reader"
- "[%{public}@] Daemon has restarted"
- "a"
- "arrayWithObjects:"
- "com.apple.private.SensorKit.ECG"
- "com.apple.private.SensorKit.PPG"
- "continueFetchRequest:from:to:withDatastoreFiles:callback:"
- "fetchAllDevices:idOnly:reply:"
- "fetchSampleBytesFrom:to:inSegment:fetchRequest:retryAttempt:sampleCallback:"
- "fetchSampleBytesFrom:to:inSegment:fetchRequest:sampleCallback:"
- "initWithData:timestamp:metadata:configuration:sampleClass:"
- "initWithReader:"
- "initWithSensor:xpcConnection:daemonNotification:authorizationClient:bundleId:"
- "reader"
- "readerClientWithReader:"
- "setObject:atIndexedSubscript:"
- "setReader:"
- "v36@0:8@\"<SRRequestReading>\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
- "v36@0:8@16B24@?28"
- "v56@0:8@16d24d32@40@?48"
- "v56@0:8d16d24@32@40@?48"
- "v64@0:8d16d24@32@40q48@?56"

```
