## SensorKitWriting

> `/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`

```diff

-958.0.1.0.0
-  __TEXT.__text: 0xec1c
+958.0.3.0.0
+  __TEXT.__text: 0xecac
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_methlist: 0xfa4
   __TEXT.__const: 0xe0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 97EC3144-9178-349F-894E-05751C64D5A3
+  UUID: 6432C46E-96E7-32BA-A8BF-70EC6C5969E0
   Functions: 327
   Symbols:   1496
   CStrings:  1078
Symbols:
+ ___33-[SRSensorWriter setupConnection]_block_invoke.62
+ ___block_literal_global.64
- ___33-[SRSensorWriter setupConnection]_block_invoke.63
- ___block_literal_global.65
Functions:
~ -[SRSensorWriter initWithIdentifier:xpcConnection:daemonNotification:authStore:tccStore:] : 572 -> 532
~ -[SRSensorWriter resetDatastoreFiles:] : 4 -> 116
~ -[SRSensorWriter provideSampleBytes:length:timestamp:error:] : 680 -> 712
~ -[SRDatastore initWithSampleFile:metadataFile:configurationFile:permission:defaults:writingStats:] : 744 -> 776
~ -[SRWritingStats updateSegmentCreationTime:rateAdjustedSize:] : 120 -> 128

```
