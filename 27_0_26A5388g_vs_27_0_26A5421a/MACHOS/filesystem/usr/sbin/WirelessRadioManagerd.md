## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-1786.17.0.0.0
-  __TEXT.__text: 0x953c4
-  __TEXT.__auth_stubs: 0xca0
+1786.19.0.0.0
+  __TEXT.__text: 0x95508
+  __TEXT.__auth_stubs: 0xcc0
   __TEXT.__objc_stubs: 0x14e40
   __TEXT.__objc_methlist: 0xb62c
   __TEXT.__const: 0x2fd0
-  __TEXT.__objc_methname: 0x259f5
+  __TEXT.__objc_methname: 0x25a30
   __TEXT.__objc_classname: 0x7a3
-  __TEXT.__objc_methtype: 0x5667
-  __TEXT.__cstring: 0x318d3
+  __TEXT.__objc_methtype: 0x567a
+  __TEXT.__cstring: 0x318dc
   __TEXT.__gcc_except_tab: 0xd30
   __TEXT.__dlopen_cstrs: 0x43
   __TEXT.__oslogstring: 0xbd
-  __TEXT.__unwind_info: 0x1930
+  __TEXT.__unwind_info: 0x1938
   __DATA_CONST.__const: 0x2450
-  __DATA_CONST.__cfstring: 0x1ca60
+  __DATA_CONST.__cfstring: 0x1ca80
   __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_intobj: 0x21d8
   __DATA_CONST.__objc_arrayobj: 0x660
-  __DATA_CONST.__auth_got: 0x668
+  __DATA_CONST.__auth_got: 0x678
   __DATA_CONST.__got: 0x530
-  __DATA.__objc_const: 0x11b58
+  __DATA.__objc_const: 0x11bb8
   __DATA.__objc_selrefs: 0x6e68
-  __DATA.__objc_ivar: 0x14b0
+  __DATA.__objc_ivar: 0x14bc
   __DATA.__objc_data: 0x19a0
-  __DATA.__data: 0x2f8
+  __DATA.__data: 0x2f0
   __DATA.__bss: 0x578
-  __DATA.__common: 0xf0
+  __DATA.__common: 0xd9
   - /System/Library/Frameworks/CallKit.framework/Versions/A/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 3992
-  Symbols:   356
-  CStrings:  10521
+  Symbols:   358
+  CStrings:  10525
 
Symbols:
+ _objc_getProperty
+ _objc_setProperty_atomic_copy
Functions:
~ sub_10000edf4 : 564 -> 580
~ sub_10002ed0c -> sub_10002ed1c : 168 -> 172
~ sub_10002eedc -> sub_10002eef0 : 316 -> 312
~ sub_10002f154 -> sub_10002f164 : 20 -> 16
~ sub_10002f168 -> sub_10002f174 : 20 -> 12
~ sub_1000501dc -> sub_1000501e0 : 20 -> 16
~ sub_1000501f0 : 20 -> 12
~ sub_100050204 -> sub_1000501fc : 20 -> 16
~ sub_100050218 -> sub_10005020c : 20 -> 12
~ sub_10005022c -> sub_100050218 : 1012 -> 1048
~ sub_100050950 -> sub_100050960 : 220 -> 236
~ sub_100050a2c -> sub_100050a4c : 164 -> 172
~ sub_100050d84 -> sub_100050dac : 1132 -> 1140
~ sub_1000511f0 -> sub_100051220 : 188 -> 204
~ sub_100061f88 -> sub_100061fc8 : 996 -> 1056
~ sub_10006a55c -> sub_10006a5d8 : 4184 -> 4192
~ sub_100090eec -> sub_100090f70 : 116 -> 120
~ sub_10009136c -> sub_1000913f4 : 48 -> 64
~ sub_10009139c -> sub_100091434 : 60 -> 76
~ sub_1000913d8 -> sub_100091480 : 48 -> 64
~ sub_100091408 -> sub_1000914c0 : 48 -> 64
~ sub_100091438 -> sub_100091500 : 48 -> 64
~ sub_100091468 -> sub_100091540 : 48 -> 64
~ sub_100091498 -> sub_100091580 : 48 -> 64
~ sub_1000921b0 -> sub_1000922a8 : 56 -> 60
~ sub_100094ce8 -> sub_100094de4 : 500 -> 572
CStrings:
+ "T@\"NSArray\",C,V_mAWDLChannelSequence"
+ "T@\"NSArray\",C,V_mNANMap0"
+ "T@\"NSArray\",C,V_mNANMap1"
+ "^{WRMMetricsCellTriggerDisconnect=d@@IIIIIIIIIIIIIIiBdBBd}16@0:8"
+ "^{WRMMetricsGenericCellularScore=dIQIdddIIIIIIBB}16@0:8"
+ "mAudioAccessoryTkn"
+ "mPrevAudioBandMessage"
+ "mPrevAudioMessage"
+ "smartLQM"
+ "{WRMMetricsCellTriggerDisconnect=\"timestamp\"d\"applicationId\"@\"NSString\"\"protocols\"@\"NSString\"\"txThroughputBefore\"I\"rxThroughputBefore\"I\"txThroughputAfter\"I\"rxThroughputAfter\"I\"rttMinBefore\"I\"rttMinAfter\"I\"rttAvgBefore\"I\"rttAvgAfter\"I\"cellScoreBefore\"I\"cellScoreAfter\"I\"wrmWifiScoreBefore\"I\"wrmWifiScoreAfter\"I\"wifiScoreBefore\"I\"wifiScoreAfter\"I\"dataLQM\"i\"didFallbackToWiFiOnCellDisconnect\"B\"postDisconnectMeasurementInterval\"d\"appRunsForeground\"B\"metricReportPending\"B\"metricSubmissionDeferInterval\"d}"
+ "{WRMMetricsGenericCellularScore=\"timestamp\"d\"lastCellScore\"I\"lastCellScoreDuration\"Q\"currentCellScore\"I\"rsrp\"d\"rsrq\"d\"snr\"d\"dataLQM\"I\"voiceLQM\"I\"smartLQM\"I\"dlConf\"I\"dlBw\"I\"rrcState\"I\"wifiPrimary\"B\"historicalInfoGood\"B}"
- "T@\"NSArray\",N,V_mAWDLChannelSequence"
- "T@\"NSArray\",N,V_mNANMap0"
- "T@\"NSArray\",N,V_mNANMap1"
- "^{WRMMetricsCellTriggerDisconnect=d@@IIIIIIIIIIIIIIiBdBBC}16@0:8"
- "^{WRMMetricsGenericCellularScore=dIQIdddIIIIBB}16@0:8"
- "{WRMMetricsCellTriggerDisconnect=\"timestamp\"d\"applicationId\"@\"NSString\"\"protocols\"@\"NSString\"\"txThroughputBefore\"I\"rxThroughputBefore\"I\"txThroughputAfter\"I\"rxThroughputAfter\"I\"rttMinBefore\"I\"rttMinAfter\"I\"rttAvgBefore\"I\"rttAvgAfter\"I\"cellScoreBefore\"I\"cellScoreAfter\"I\"wrmWifiScoreBefore\"I\"wrmWifiScoreAfter\"I\"wifiScoreBefore\"I\"wifiScoreAfter\"I\"dataLQM\"i\"didFallbackToWiFiOnCellDisconnect\"B\"postDisconnectMeasurementInterval\"d\"appRunsForeground\"B\"metricReportPending\"B\"deferUntilAdditionalNwStatsReports\"C}"
- "{WRMMetricsGenericCellularScore=\"timestamp\"d\"lastCellScore\"I\"lastCellScoreDuration\"Q\"currentCellScore\"I\"rsrp\"d\"rsrq\"d\"snr\"d\"dataLQM\"I\"dlConf\"I\"dlBw\"I\"rrcState\"I\"wifiPrimary\"B\"historicalInfoGood\"B}"
```
