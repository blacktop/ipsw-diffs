## sensorkitd

> `/usr/libexec/sensorkitd`

```diff

-860.0.16.0.0
-  __TEXT.__text: 0x40f50
-  __TEXT.__auth_stubs: 0xc50
-  __TEXT.__objc_stubs: 0x37a0
-  __TEXT.__objc_methlist: 0x24ac
-  __TEXT.__const: 0x150
-  __TEXT.__objc_methname: 0x5925
-  __TEXT.__objc_classname: 0x8de
-  __TEXT.__objc_methtype: 0x2635
-  __TEXT.__cstring: 0x2d64
-  __TEXT.__oslogstring: 0x6abe
-  __TEXT.__gcc_except_tab: 0x690
-  __TEXT.__unwind_info: 0x9f0
-  __DATA_CONST.__auth_got: 0x638
+950.0.0.0.0
+  __TEXT.__text: 0x42518
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__objc_stubs: 0x37e0
+  __TEXT.__objc_methlist: 0x256c
+  __TEXT.__const: 0x158
+  __TEXT.__objc_methname: 0x5b55
+  __TEXT.__objc_classname: 0x8ed
+  __TEXT.__objc_methtype: 0x26d6
+  __TEXT.__cstring: 0x2fb6
+  __TEXT.__oslogstring: 0x6dcc
+  __TEXT.__gcc_except_tab: 0x694
+  __TEXT.__unwind_info: 0xa20
+  __DATA_CONST.__auth_got: 0x640
   __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xfd0
-  __DATA_CONST.__cfstring: 0x30e0
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0xfe8
+  __DATA_CONST.__cfstring: 0x3280
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x198
-  __DATA_CONST.__objc_intobj: 0x4b0
+  __DATA_CONST.__objc_superrefs: 0x1a0
+  __DATA_CONST.__objc_intobj: 0x498
   __DATA_CONST.__objc_arraydata: 0x58
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA.__objc_const: 0x5b40
-  __DATA.__objc_selrefs: 0x13b0
-  __DATA.__objc_ivar: 0x400
-  __DATA.__objc_data: 0x1180
+  __DATA_CONST.__objc_doubleobj: 0x80
+  __DATA.__objc_const: 0x5dc8
+  __DATA.__objc_selrefs: 0x13f8
+  __DATA.__objc_ivar: 0x434
+  __DATA.__objc_data: 0x11d0
   __DATA.__data: 0x11a8
   __DATA.__bss: 0x1e0
   __DATA.__common: 0x30

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 543DF55E-F203-3C90-A2AE-E5487229E733
-  Functions: 797
-  Symbols:   325
-  CStrings:  2596
+  UUID: 71E0CFBE-CC6B-3046-9E1D-B068CD93F654
+  Functions: 813
+  Symbols:   326
+  CStrings:  2659
 
Symbols:
+ _exp2
CStrings:
+ "%@ (%p): name: %@, authService: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons: %@, storageBackend: %ld"
+ "<%@ (%p)> [%@]:\n{\n  sessionStart: %f (CF: %f),\n  bytesWritten: %llu,\n  samplesWritten: %lu,\n  segmentCreationTime: %f,\n  rateAdjustedSegmentSize: %lu,\n  averageFillDuration: %f\n}"
+ "@28@0:8@16B24"
+ "AuthorizationTimes"
+ "Enabling recording for %{private}@ from bundle %{private}@ after enrollment"
+ "Failed to find a sensor description for %{public}@ to remove authorization times"
+ "Failed to set interest for bundle %{private}@ for sensor %{public}@ because %{public}@"
+ "Force segment creation for %@"
+ "No last modified authorization time found in the state cache for auth service: %{private}@ bundle id: %{private}@. Migrating from TCC %{private}f."
+ "Request new segment for %@, because of new study authorization %{private}@"
+ "Resizing file %{private}@ to %llu bytes"
+ "SRWritingStats"
+ "SegmentFillDuration"
+ "SegmentFillDurationSecs"
+ "SegmentMinimumFactor"
+ "SegmentSizeMinimumFactor"
+ "T@\"NSSet\",&,V_sensors"
+ "TQ,R,N,V_totalSegmentsCreated"
+ "Td,R,N,V_totalFillDuration"
+ "Updating auth time for service: %{public}@ bundle: %{public}@ time: %{public}f"
+ "Writing Stats: %@\nExpected segment lifetime: %{public}f\nDefault segment size: %lu"
+ "_authorizationTimes"
+ "_earliestSegmentURL"
+ "_fetchAuthorizationTimes"
+ "_rateAdjustedSegmentSize"
+ "_segmentCreationTime"
+ "_segmentFillDuration"
+ "_segmentMinimumFactor"
+ "_sessionStart"
+ "_totalBytesWritten"
+ "_totalFillDuration"
+ "_totalSamplesWritten"
+ "_totalSegmentsCreated"
+ "allDescriptions"
+ "authorizationBroadcaster:didCompleteEnrollmentFor:sensors:"
+ "autoEnableRecordingForSensors:bundleId:"
+ "centralManager:didUpdateSynchronizationEventForPeripheral:results:"
+ "com.apple.SensorKit.deviceUsageReport"
+ "com.apple.SensorKit.heart.rate"
+ "com.apple.SensorKit.mediaEvents"
+ "com.apple.SensorKit.odometer"
+ "com.apple.private.SensorKit.prerequisite.enrollment-complete"
+ "com.apple.sensorkit.launchAcousticSettingsCollector"
+ "com.apple.sensorkit.launchMessagesUsageCollector"
+ "com.apple.sensorkit.launchPhoneUsageCollector"
+ "com.apple.sensorkit.launchSleepSessionsCollector"
+ "completeEnrollmentForBundleId:sensors:"
+ "initWithSensors:withAuthorizationTimes:"
+ "peripheral:didCompleteChannelSoundingProcedure:error:"
+ "sensors"
+ "setSensors:"
+ "totalFillDuration"
+ "totalSegmentsCreated"
+ "v32@0:8@\"NSString\"16@\"NSSet\"24"
+ "v40@0:8@\"CBPeripheral\"16@\"NSDictionary\"24@\"NSError\"32"
+ "v40@0:8@\"RDAuthorizationBroadcaster\"16@\"NSString\"24@\"NSSet\"32"
+ "writing to %{public}p with length %{public}lu would go past end of file (%{public}p)"
- "%@ (%p): name: %@, authService: %@, writer: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName: %@, filters: %@, legacySampleClass: %@, legacySampleClassLinkedBefore: %u, roundingInterval: %f, eligibleDaemons: %@, storageBackend: %ld"
- "T@\"NSString\",R,C,V_writerBundleIdentifier"
- "WriterBundleId"
- "_writerBundleIdentifier"
- "com.apple.sensorkit.launchInteractionHistoryCollector"
- "indexOfObject:inSortedRange:options:usingComparator:"
- "writerBundleIdentifier"

```
