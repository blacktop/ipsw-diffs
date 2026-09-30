## SensorKit

> `/System/Library/Frameworks/SensorKit.framework/SensorKit`

```diff

-958.0.1.0.0
-  __TEXT.__text: 0x3adc8
+958.0.3.0.0
+  __TEXT.__text: 0x3ae58
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_methlist: 0x51a4
   __TEXT.__dlopen_cstrs: 0x95

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EEA479F6-75EC-3566-87E0-595B2510AB9E
+  UUID: B7FF5BF1-C012-3850-85F8-94E5DBD4DEE2
   Functions: 1695
   Symbols:   6183
   CStrings:  3762
Symbols:
+ ___33-[SRSensorWriter setupConnection]_block_invoke.69
+ ___block_literal_global.71
- ___33-[SRSensorWriter setupConnection]_block_invoke.70
- ___block_literal_global.72
Functions:
~ -[SRSensorWriter initWithIdentifier:xpcConnection:daemonNotification:authStore:tccStore:] : 572 -> 532
~ -[SRSensorWriter resetDatastoreFiles:] : 4 -> 116
~ -[SRSensorWriter provideSampleBytes:length:timestamp:error:] : 680 -> 712
~ -[SRDatastore initWithSampleFile:metadataFile:configurationFile:permission:defaults:writingStats:] : 744 -> 776
~ -[SRWritingStats updateSegmentCreationTime:rateAdjustedSize:] : 120 -> 128

```
