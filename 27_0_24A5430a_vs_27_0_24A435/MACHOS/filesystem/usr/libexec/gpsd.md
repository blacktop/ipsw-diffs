## gpsd

> `/usr/libexec/gpsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 365.0.9.0.1
-  __TEXT.__text: 0x177cf4
+  __TEXT.__text: 0x177f64
   __TEXT.__auth_stubs: 0x20c0
   __TEXT.__objc_stubs: 0x860
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__gcc_except_tab: 0x9074
-  __TEXT.__const: 0xf2d0
+  __TEXT.__const: 0xf390
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x6a4
   __TEXT.__swift5_typeref: 0x2f1
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-801c24cfe646fc8b93d2f14fcc3a8608.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-9d1e5c7edfe944d734891dc41347dfa1.o)
Functions:
~ __ZN26GpsdGnssDeviceRequestQueue13handleRequestEONSt3__16vectorIhNS0_9allocatorIhEEEE : 1456 -> 1468
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERNS_7greaterIvEEPfLb1EEEvT1_S6_T0_NS_15iterator_traitsIS6_E15difference_typeEb : 3104 -> 3100
~ __ZN21GpsdIndicationHandler29handleMeasureReportIndicationERKN6cproto4gpsd10IndicationERNSt3__16vectorIhNS5_9allocatorIhEEEE : 1832 -> 1836
~ __ZNSt3__16vectorIN6cproto4gnss17SensorSample3AxisENS_9allocatorIS3_EEE6resizeEm : 372 -> 376
~ __ZN12MessageQueueIN6cproto4gpsd10IndicationELm16EE4pushERKS2_b : 420 -> 424
~ __ZN17GnssDevicePayload16flushIndicationsEv : 280 -> 284
~ __ZN14GnssByteBufferILm65536EE4tickEy : 292 -> 296
~ __ZN12MessageQueueIN6cproto4gpsd10IndicationELm16EE4tickEy : 180 -> 184
~ __ZN14GnssByteBufferILm65536EE4pushEPKhm : 636 -> 640
~ __ZNSt3__16vectorIN7GnssHal7NvStore4ItemENS_9allocatorIS3_EEE6resizeEm : 352 -> 364
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE6resizeEm : 284 -> 288
~ __ZN12ProtobufUtil7convert21cpbSetAssistanceAccelERKN6cproto4gpsd18SetAssistanceAccelERNSt3__16vectorIhNS6_9allocatorIhEEEERN5proto4gpsd18SetAssistanceAccelE : 424 -> 404
~ __ZN12ProtobufUtil7convert20cpbSetAssistanceGyroERKN6cproto4gpsd17SetAssistanceGyroERNSt3__16vectorIhNS6_9allocatorIhEEEERN5proto4gpsd17SetAssistanceGyroE : 424 -> 404
~ __ZNSt3__16vectorIN6cproto4gnss4SvIdENS_9allocatorIS3_EEE6resizeEm : 404 -> 408
~ __ZNSt3__16vectorIN6cproto4gpsd18RecoveryStatistics13RecoveryPointENS_9allocatorIS4_EEE6resizeEm : 404 -> 408
~ __ZN12ProtobufUtil7convert21cpbRecoveryStatisticsERKN6cproto4gpsd18RecoveryStatisticsERNSt3__16vectorIhNS6_9allocatorIhEEEERN5proto4gpsd18RecoveryStatisticsE : 660 -> 664
~ __ZNSt3__16vectorIjNS_9allocatorIjEEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorIN6cproto4gnss9Emergency11LteCellInfoENS_9allocatorIS4_EEE6resizeEm : 404 -> 408
~ __ZNSt3__16vectorIN6cproto4gnss9Emergency11GsmCellInfoENS_9allocatorIS4_EEE6resizeEm : 404 -> 408
~ __ZN12ProtobufUtil7convert13cpbLocationIdERKN6cproto4gnss9Emergency10LocationIdERNSt3__16vectorIhNS7_9allocatorIhEEEERN5proto4gnss9Emergency10LocationIdE : 1360 -> 1380
~ __ZN12ProtobufUtil7convert22cpbWlanMeasurementListERKN6cproto4gnss9Emergency19WlanMeasurementListERNSt3__16vectorIhNS7_9allocatorIhEEEERN5proto4gnss9Emergency19WlanMeasurementListE : 516 -> 520
~ __ZNSt3__16vectorIN6cproto4gnss9Emergency23GanssMeasurementElementENS_9allocatorIS4_EEE6resizeEm : 444 -> 448
~ __ZN12ProtobufUtil7convert29cpbGanssSignalMeasurementInfoERKN6cproto4gnss9Emergency26GanssSignalMeasurementInfoERNSt3__16vectorIhNS7_9allocatorIhEEEERN5proto4gnss9Emergency26GanssSignalMeasurementInfoE : 540 -> 544
~ __ZN12ProtobufUtil7convert18cpbGpsMeasurementsERKN6cproto4gnss9Emergency15GpsMeasurementsERNSt3__16vectorIhNS7_9allocatorIhEEEERN5proto4gnss9Emergency15GpsMeasurementsE : 796 -> 812
~ __ZN12ProtobufUtil7convert19cpbGpsReferenceTimeERKN6cproto4gnss9Emergency16GpsReferenceTimeERNSt3__16vectorIhNS7_9allocatorIhEEEERN5proto4gnss9Emergency16GpsReferenceTimeE : 664 -> 676
~ __ZNSt3__16vectorIN6cproto4gnss9Emergency12GpsEphemerisENS_9allocatorIS4_EEE6resizeEm : 372 -> 376
~ __ZN12ProtobufUtil7convert21cpbGpsNavigationModelERKN6cproto4gnss9Emergency18GpsNavigationModelERNSt3__16vectorIhNS7_9allocatorIhEEEERN5proto4gnss9Emergency18GpsNavigationModelE : 488 -> 500
~ __ZNSt3__16vectorIN4cCLP8LogEntry11PrivateData17SvBandCorrectionsENS_9allocatorIS4_EEE6resizeEm : 404 -> 408
~ __ZN12ProtobufUtil7convert9cpbSvInfoERKN4cCLP8LogEntry11PrivateData6SvInfoERNSt3__16vectorIhNS7_9allocatorIhEEEERN3CLP8LogEntry11PrivateData6SvInfoE : 1388 -> 1408
~ __ZNSt3__16vectorIN4cCLP8LogEntry11PrivateData23ReceiverBandCorrectionsENS_9allocatorIS4_EEE6resizeEm : 404 -> 408
~ __ZNSt3__16vectorIN4cCLP8LogEntry11PrivateData26AntennaPhaseCenterSvOffsetENS_9allocatorIS4_EEE6resizeEm : 444 -> 448
~ __ZN12ProtobufUtil7convert36cpbMeasurementReportCallbackContentsERKN4cCLP8LogEntry11PrivateData33MeasurementReportCallbackContentsERNSt3__16vectorIhNS7_9allocatorIhEEEERN3CLP8LogEntry11PrivateData33MeasurementReportCallbackContentsE : 1776 -> 1784
~ __ZN12ProtobufUtil10toProtobufERKN4gnss9Emergency4Supl10LocationIdEPN5proto4gnss9Emergency10LocationIdE : 920 -> 924
~ __ZN12ProtobufUtil10toProtobufERKN4gnss9Emergency6Cplane26GanssSignalMeasurementInfoEPN5proto4gnss9Emergency26GanssSignalMeasurementInfoE : 300 -> 304
~ __ZN12ProtobufUtil10toProtobufERKN4gnss9Emergency6Cplane15GpsMeasurementsEPN5proto4gnss9Emergency15GpsMeasurementsE : 536 -> 548
~ __ZN12ProtobufUtil10toProtobufERKN4gnss9Emergency6Cplane23GanssAidRequestPerGanssEPN5proto4gnss9Emergency23GanssAidRequestPerGanssE : 632 -> 640
~ __ZN12ProtobufUtil10toProtobufERKN4gnss9Emergency6Cplane16GpsReferenceTimeEPN5proto4gnss9Emergency16GpsReferenceTimeE : 408 -> 416
~ __ZN12ProtobufUtil10toProtobufERKN4gnss9Emergency6Cplane18GpsNavigationModelEPN5proto4gnss9Emergency18GpsNavigationModelE : 376 -> 388
~ __ZNSt3__16vectorIP18GpsdSessionHandlerNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_ : 184 -> 176
~ __ZN24GpsdPlatformInfoHardware14detectHardwareEv : 2664 -> 3080
~ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_20MeasurementExtensionERKNSt3__16vectorIhNS5_9allocatorIhEEEERN4gnss20MeasurementExtensionE : 744 -> 756
~ __ZNSt3__114__split_bufferIPNS_6vectorIhNS_9allocatorIhEEEENS2_IS5_EEE12emplace_backIJRS5_EEEvDpOT_ : 248 -> 252
CStrings:
+ "#version,CoreGPS-365.0.9.0.1,machContSec,%{public}.3f,BuildTime,{Aug 13 2026,21:42:35}"
- "#version,CoreGPS-365.0.9.0.1,machContSec,%{public}.3f,BuildTime,{Aug 13 2026,22:26:38}"
```
