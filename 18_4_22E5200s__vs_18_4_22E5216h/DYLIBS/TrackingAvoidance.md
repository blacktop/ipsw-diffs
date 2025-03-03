## TrackingAvoidance

> `/System/Library/PrivateFrameworks/TrackingAvoidance.framework/TrackingAvoidance`

```diff

-107.0.1.0.0
-  __TEXT.__text: 0x47ab8
+107.0.3.0.0
+  __TEXT.__text: 0x483d4
   __TEXT.__auth_stubs: 0x580
-  __TEXT.__objc_methlist: 0x4588
+  __TEXT.__objc_methlist: 0x45f0
   __TEXT.__const: 0x340
-  __TEXT.__oslogstring: 0x69c9
-  __TEXT.__cstring: 0x2d80
-  __TEXT.__gcc_except_tab: 0x5ac
-  __TEXT.__unwind_info: 0xd40
+  __TEXT.__oslogstring: 0x6b0f
+  __TEXT.__cstring: 0x2ddb
+  __TEXT.__gcc_except_tab: 0x5cc
+  __TEXT.__unwind_info: 0xd48
   __TEXT.__objc_classname: 0x77a
-  __TEXT.__objc_methname: 0xca06
-  __TEXT.__objc_methtype: 0x1229
-  __TEXT.__objc_stubs: 0x7420
+  __TEXT.__objc_methname: 0xcba6
+  __TEXT.__objc_methtype: 0x1231
+  __TEXT.__objc_stubs: 0x74e0
   __DATA_CONST.__got: 0x398
-  __DATA_CONST.__const: 0x760
+  __DATA_CONST.__const: 0x768
   __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2190
+  __DATA_CONST.__objc_selrefs: 0x21d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1d8
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x2d8
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x46e0
-  __AUTH_CONST.__objc_const: 0x8470
+  __AUTH_CONST.__cfstring: 0x4740
+  __AUTH_CONST.__objc_const: 0x84d0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x60c
+  __DATA.__objc_ivar: 0x614
   __DATA.__data: 0x600
   __DATA_DIRTY.__objc_data: 0x12c0
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1505
-  Symbols:   1888
-  CStrings:  2934
+  Functions: 1513
+  Symbols:   1897
+  CStrings:  2952
 
Symbols:
+ _kTAFutureEventToleranceIntervalKey
CStrings:
+ "@144@0:8d16d24d32d40d48Q56Q64d72B80B84d88d96B104d108Q116B124d128d136"
+ "@160@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152"
+ "FutureExpiryInterval"
+ "TADeviceRecordFutureExpiryTimeInterval"
+ "TAFutureEventToleranceInterval"
+ "Td,N,V_futureEventToleranceInterval"
+ "Td,N,V_futureExpiryTimeInterval"
+ "_futureEventToleranceInterval"
+ "_futureExpiryTimeInterval"
+ "futureEventToleranceInterval"
+ "futureExpiryTimeInterval"
+ "getAirPodsBudPosition:"
+ "initWithExpiryTimeInterval:futureExpiryTimeInterval:purgeTimeInterval:keepAliveInterval:minimumStagingInterval:stagingBackstopHour:assumedKeyRollHour:scanInterval:surfaceImmediatelyBeepOnMove:surfaceAfterHyperStagingIntervalBetweenBackstopAndKeyroll:maxExpectedHELEWildInterval:maxExpectedDurianWildInterval:shouldAlertHELEImmediatelyForImmediateTypes:minimumHELEStagingInterval:stagingHELEBackstopHour:surfaceHELEAfterHyperStagingIntervalBetweenBackstopAndKeyroll:hyperHELEStagingInterval:hyperStagingInterval:"
+ "initWithExpiryTimeIntervalOrDefault:futureExpiryTimeIntervalOrDefault:purgeTimeIntervalOrDefault:keepAliveIntervalOrDefault:minimumStagingIntervalOrDefault:stagingBackstopHourOrDefault:assumedKeyRollHourOrDefault:scanIntervalOrDefault:surfaceImmediatelyBeepOnMoveOrDefault:surfaceAfterHyperStagingIntervalBetweenBackstopAndKeyrollOrDefault:maxExpectedHELEWildIntervalOrDefault:maxExpectedDurianWildIntervalOrDefault:shouldAlertHELEImmediatelyForImmediateTypesOrDefault:minimumHELEStagingIntervalOrDefault:stagingHELEBackstopHourOrDefault:surfaceHELEAfterHyperStagingIntervalBetweenBackstopAndKeyrollOrDefault:hyperHELEStagingIntervalOrDefault:hyperStagingIntervalOrDefault:"
+ "isCapableOfBOM"
+ "k"
+ "normalizeDualT18PoshAdvertisersAsPosh:deviceRecord:"
+ "setFutureEventToleranceInterval:"
+ "setFutureExpiryTimeInterval:"
+ "shouldUpdateAdvertisement:"
+ "{\"msg%{public}.0s\":\"#TAFilterGeneral found BOM on unsupported device\", \"address\":\"%{private}@\"}"
+ "{\"msg%{public}.0s\":\"#TATrackingAvoidanceService event is dated too far in the future, not ingesting\", \"event\":\"%{sensitive}@\"}"
+ "{\"msg%{public}.0s\":\"received unexpected part identifier for AirPods bud\", \"partIdentifier\":%{public}d}"
- "@136@0:8d16d24d32d40Q48Q56d64B72B76d80d88B96d100Q108B116d120d128"
- "@152@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144"
- "["
- "initWithExpiryTimeInterval:purgeTimeInterval:keepAliveInterval:minimumStagingInterval:stagingBackstopHour:assumedKeyRollHour:scanInterval:surfaceImmediatelyBeepOnMove:surfaceAfterHyperStagingIntervalBetweenBackstopAndKeyroll:maxExpectedHELEWildInterval:maxExpectedDurianWildInterval:shouldAlertHELEImmediatelyForImmediateTypes:minimumHELEStagingInterval:stagingHELEBackstopHour:surfaceHELEAfterHyperStagingIntervalBetweenBackstopAndKeyroll:hyperHELEStagingInterval:hyperStagingInterval:"
- "initWithExpiryTimeIntervalOrDefault:purgeTimeIntervalOrDefault:keepAliveIntervalOrDefault:minimumStagingIntervalOrDefault:stagingBackstopHourOrDefault:assumedKeyRollHourOrDefault:scanIntervalOrDefault:surfaceImmediatelyBeepOnMoveOrDefault:surfaceAfterHyperStagingIntervalBetweenBackstopAndKeyrollOrDefault:maxExpectedHELEWildIntervalOrDefault:maxExpectedDurianWildIntervalOrDefault:shouldAlertHELEImmediatelyForImmediateTypesOrDefault:minimumHELEStagingIntervalOrDefault:stagingHELEBackstopHourOrDefault:surfaceHELEAfterHyperStagingIntervalBetweenBackstopAndKeyrollOrDefault:hyperHELEStagingIntervalOrDefault:hyperStagingIntervalOrDefault:"

```
