## gpsd

> `/usr/libexec/gpsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__oslogstring`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 369.0.1.0.0
-  __TEXT.__text: 0x173140
+  __TEXT.__text: 0x17318c
   __TEXT.__auth_stubs: 0x20b0
   __TEXT.__objc_stubs: 0x860
   __TEXT.__init_offsets: 0x30
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-c8300d79cb68cac9209b12a357e5dd0d.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-296fc0eaea17dda65539ea1236967c5b.o)
Functions:
~ __ZN16GnssDeviceCommon21performSpoofingChecksERN4gnss3FixE : 820 -> 824
~ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5 : 112 -> 124
~ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1g5 : 112 -> 124
~ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtF9GPSDaemon10DataClientV_Tg5 : 300 -> 324
~ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFSS_Tg5 : 260 -> 284
CStrings:
+ "#version,CoreGPS-369.0.1,machContSec,%{public}.3f,BuildTime,{Nov 10 2026,21:55:54}"
- "#version,CoreGPS-369.0.1,machContSec,%{public}.3f,BuildTime,{Oct 24 2026,01:38:14}"
```
