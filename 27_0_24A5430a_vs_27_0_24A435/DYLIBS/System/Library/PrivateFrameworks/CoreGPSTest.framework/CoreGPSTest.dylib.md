## CoreGPSTest.dylib

> `/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

 365.0.9.0.1
-  __TEXT.__text: 0x66ca0
+  __TEXT.__text: 0x66e6c
   __TEXT.__init_offsets: 0xc
   __TEXT.__objc_methlist: 0x164
-  __TEXT.__const: 0x64c0
+  __TEXT.__const: 0x6570
   __TEXT.__gcc_except_tab: 0x3988
   __TEXT.__oslogstring: 0xaa72
   __TEXT.__constg_swiftt: 0x408
Functions:
~ __ZN12MessageQueueIN6cproto4gpsd10IndicationELm16EE4pushERKS2_b : 420 -> 424
~ __ZN17GnssDevicePayload16flushIndicationsEv : 280 -> 284
~ __ZN14GnssByteBufferILm65536EE4tickEy : 292 -> 296
~ __ZN12MessageQueueIN6cproto4gpsd10IndicationELm16EE4tickEy : 180 -> 184
~ __ZN14GnssByteBufferILm65536EE4pushEPKhm : 636 -> 640
~ __ZNSt3__16vectorIN7GnssHal7NvStore4ItemENS_9allocatorIS3_EEE6resizeEm : 352 -> 364
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE6resizeEm : 284 -> 288
~ __ZNSt3__16vectorIP18GpsdSessionHandlerNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRS2_EEEPS2_DpOT_ : 184 -> 176
~ __ZNSt3__16vectorIN6cproto4gnss9Emergency12GpsEphemerisENS_9allocatorIS4_EEE6resizeEm : 404 -> 408
~ __ZN24GpsdPlatformInfoHardware14detectHardwareEv : 2664 -> 3080
~ __ZN4cCLP8LogEntry11PrivateData6cpbHalERKNS1_20MeasurementExtensionERKNSt3__16vectorIhNS5_9allocatorIhEEEERN4gnss20MeasurementExtensionE : 744 -> 756
CStrings:
+ "#version,CoreGPS-365.0.9.0.1,machContSec,%{public}.3f,BuildTime,{Aug 13 2026,21:42:35}"
- "#version,CoreGPS-365.0.9.0.1,machContSec,%{public}.3f,BuildTime,{Aug 13 2026,22:26:38}"
```
