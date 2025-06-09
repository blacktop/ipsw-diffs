## SensorKitWriting

> `/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`

```diff

-860.0.16.0.0
-  __TEXT.__text: 0xe69c
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0xf14
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x118e
-  __TEXT.__gcc_except_tab: 0x604
-  __TEXT.__oslogstring: 0x1fc3
-  __TEXT.__unwind_info: 0x4d0
-  __TEXT.__objc_classname: 0x314
-  __TEXT.__objc_methname: 0x2e62
-  __TEXT.__objc_methtype: 0x877
-  __TEXT.__objc_stubs: 0x1e80
+950.0.0.0.0
+  __TEXT.__text: 0xec1c
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0xfa4
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x126e
+  __TEXT.__gcc_except_tab: 0x608
+  __TEXT.__oslogstring: 0x2092
+  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__objc_classname: 0x323
+  __TEXT.__objc_methname: 0x301d
+  __TEXT.__objc_methtype: 0x8b6
+  __TEXT.__objc_stubs: 0x1ec0
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x510
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa20
+  __DATA_CONST.__objc_selrefs: 0xa60
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x1f30
+  __AUTH_CONST.__cfstring: 0x1060
+  __AUTH_CONST.__objc_const: 0x2168
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x1c0
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0x1ec
   __DATA.__data: 0x5a8
   __DATA.__bss: 0x90
   __DATA.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4553D918-AFB6-313E-B0F5-12B663CB42F8
-  Functions: 316
-  Symbols:   1450
-  CStrings:  1043
+  UUID: C07839A4-C3AA-3CF3-A88E-AD5657020C75
+  Functions: 327
+  Symbols:   1496
+  CStrings:  1078
 
Symbols:
+ +[SRSensorDescription allDescriptions]
+ -[SRAuthorizationClient completeEnrollmentForBundleId:sensors:]
+ -[SRAuthorizationStore initWithSensors:withAuthorizationTimes:]
+ -[SRAuthorizationStore sensors]
+ -[SRAuthorizationStore setSensors:]
+ -[SRDatastore initWithSampleFile:metadataFile:configurationFile:permission:defaults:writingStats:]
+ -[SRSensorWriter setWritingStats:]
+ -[SRSensorWriter writingStats]
+ -[SRWritingStats dealloc]
+ -[SRWritingStats description]
+ -[SRWritingStats initWithSensor:]
+ -[SRWritingStats totalFillDuration]
+ -[SRWritingStats totalSegmentsCreated]
+ -[SRWritingStats updateSegmentCreationTime:rateAdjustedSize:]
+ GCC_except_table25
+ GCC_except_table27
+ GCC_except_table32
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table9
+ _OBJC_CLASS_$_SRWritingStats
+ _OBJC_IVAR_$_SRAuthorizationStore._fetchAuthorizationTimes
+ _OBJC_IVAR_$_SRDefaults._segmentFillDuration
+ _OBJC_IVAR_$_SRDefaults._segmentMinimumFactor
+ _OBJC_IVAR_$_SRSensorWriter._writingStats
+ _OBJC_IVAR_$_SRWritingStats._rateAdjustedSegmentSize
+ _OBJC_IVAR_$_SRWritingStats._segmentCreationTime
+ _OBJC_IVAR_$_SRWritingStats._sensor
+ _OBJC_IVAR_$_SRWritingStats._sessionStart
+ _OBJC_IVAR_$_SRWritingStats._totalBytesWritten
+ _OBJC_IVAR_$_SRWritingStats._totalFillDuration
+ _OBJC_IVAR_$_SRWritingStats._totalSamplesWritten
+ _OBJC_IVAR_$_SRWritingStats._totalSegmentsCreated
+ _OBJC_METACLASS_$_SRWritingStats
+ _SRSensorAcousticSettings
+ _SRSensorSleepSessions
+ _SensorInfoKeySegmentFillDuration
+ _SensorInfoKeySegmentMinimumFactor
+ __OBJC_$_INSTANCE_METHODS_SRWritingStats
+ __OBJC_$_INSTANCE_VARIABLES_SRWritingStats
+ __OBJC_$_PROP_LIST_SRWritingStats
+ __OBJC_CLASS_RO_$_SRWritingStats
+ __OBJC_METACLASS_RO_$_SRWritingStats
+ ___32-[SRSensorWriter setMonitoring:]_block_invoke.130
+ ___33-[SRSensorWriter setupConnection]_block_invoke.63
+ ___34-[SRAuthorizationClient syncProxy]_block_invoke.36
+ ___35-[SRSensorWriter requestNewSegment]_block_invoke.72
+ ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.140
+ ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.142
+ ___block_literal_global.38
+ ___block_literal_global.65
+ _exp2
+ _objc_msgSend$completeEnrollmentForBundleId:sensors:
+ _objc_msgSend$initWithSensors:withAuthorizationTimes:
- -[SRDatastore initWithSampleFile:metadataFile:configurationFile:permission:defaults:]
- -[SRMemoryMapping writeBytes:toOffset:length:]
- -[SRSensorDescription writerBundleIdentifier]
- GCC_except_table11
- GCC_except_table24
- GCC_except_table26
- GCC_except_table29
- GCC_except_table33
- GCC_except_table36
- _OBJC_IVAR_$_SRSensorDescription._writerBundleIdentifier
- _SRSensorOnWristDetailedState
- ___32-[SRSensorWriter setMonitoring:]_block_invoke.129
- ___33-[SRSensorWriter setupConnection]_block_invoke.62
- ___34-[SRAuthorizationClient syncProxy]_block_invoke.33
- ___35-[SRSensorWriter requestNewSegment]_block_invoke.70
- ___45-[SRSensorWriter startUpdatingAuthorizations]_block_invoke.139
- ___47-[SRSensorWriter bundleEligibility:completion:]_block_invoke.140
- ___block_literal_global.35
- ___block_literal_global.64
CStrings:
+ "%@ (%p): name: %@, authService: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons: %@, storageBackend: %ld"
+ "<%@ (%p)> [%@]:\n{\n  sessionStart: %f (CF: %f),\n  bytesWritten: %llu,\n  samplesWritten: %lu,\n  segmentCreationTime: %f,\n  rateAdjustedSegmentSize: %lu,\n  averageFillDuration: %f\n}"
+ "@\"SRWritingStats\""
+ "@28@0:8@16B24"
+ "Resizing file %{private}@ to %llu bytes"
+ "SRWritingStats"
+ "SegmentFillDuration"
+ "SegmentMinimumFactor"
+ "T@\"NSSet\",&,V_sensors"
+ "T@\"SRWritingStats\",&,N,V_writingStats"
+ "TQ,R,N,V_totalSegmentsCreated"
+ "Td,R,N,V_totalFillDuration"
+ "Writing Stats: %@\nExpected segment lifetime: %{public}f\nDefault segment size: %lu"
+ "_fetchAuthorizationTimes"
+ "_rateAdjustedSegmentSize"
+ "_segmentCreationTime"
+ "_segmentFillDuration"
+ "_segmentMinimumFactor"
+ "_sensor"
+ "_sessionStart"
+ "_totalBytesWritten"
+ "_totalFillDuration"
+ "_totalSamplesWritten"
+ "_totalSegmentsCreated"
+ "_writingStats"
+ "allDescriptions"
+ "com.apple.SensorKit.hearing.acousticSettings"
+ "com.apple.SensorKit.sleep.sessions"
+ "completeEnrollmentForBundleId:sensors:"
+ "initWithSensors:withAuthorizationTimes:"
+ "sensors"
+ "setSensors:"
+ "setWritingStats:"
+ "totalFillDuration"
+ "totalSegmentsCreated"
+ "v32@0:8@\"NSString\"16@\"NSSet\"24"
+ "writing to %{public}p with length %{public}lu would go past end of file (%{public}p)"
+ "writingStats"
- "%@ (%p): name: %@, authService: %@, writer: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons: %@, storageBackend: %ld"
- "T@\"NSString\",R,C,V_writerBundleIdentifier"
- "WriterBundleId"
- "_writerBundleIdentifier"
- "com.apple.private.SensorKit.onWristDetailedState"
- "writerBundleIdentifier"

```
