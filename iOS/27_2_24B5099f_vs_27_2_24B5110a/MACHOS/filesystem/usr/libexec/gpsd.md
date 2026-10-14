## gpsd

> `/usr/libexec/gpsd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_protos`
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

-367.0.1.0.0
-  __TEXT.__text: 0x171e68
+367.0.2.0.0
+  __TEXT.__text: 0x171ed4
   __TEXT.__auth_stubs: 0x20b0
   __TEXT.__objc_stubs: 0x860
   __TEXT.__init_offsets: 0x30

   __TEXT.__swift5_reflstr: 0x11c
   __TEXT.__swift5_fieldmd: 0x29c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__oslogstring: 0x1214f
+  __TEXT.__oslogstring: 0x12162
   __TEXT.__swift5_types: 0x54
   __TEXT.__objc_classname: 0x28b
   __TEXT.__objc_methname: 0x822

   - /usr/lib/swift/libswiftos.dylib
   Functions: 10144
   Symbols:   15589
-  CStrings:  2569
+  CStrings:  2570
 
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-381bc0d6d1d9cb2ddfd738b76d01572f.o)
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-08a6ba2f97614e390e5951ea6af36173.o)
Functions:
~ __ZN7GnssHal12GpioEmbedded12setResetHighEv : 104 -> 212
CStrings:
+ "#gpio,setResetHigh"
+ "#version,CoreGPS-367.0.2,machContSec,%{public}.3f,BuildTime,{Oct 10 2026,01:18:38}"
- "#version,CoreGPS-367.0.1,machContSec,%{public}.3f,BuildTime,{Sep 27 2026,23:16:15}"
```
