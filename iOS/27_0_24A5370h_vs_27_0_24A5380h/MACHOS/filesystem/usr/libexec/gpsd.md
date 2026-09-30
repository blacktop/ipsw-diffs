## gpsd

> `/usr/libexec/gpsd`

```diff

-  __TEXT.__text: 0x16ee08
-  __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_stubs: 0x860
+  __TEXT.__text: 0x16ef08
+  __TEXT.__auth_stubs: 0x20b0
+  __TEXT.__objc_stubs: 0x880
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__gcc_except_tab: 0x8ad0
+  __TEXT.__gcc_except_tab: 0x8ae8
   __TEXT.__const: 0xecc0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x6a4

   __TEXT.__swift5_reflstr: 0x11c
   __TEXT.__swift5_fieldmd: 0x29c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__oslogstring: 0x10bd7
+  __TEXT.__oslogstring: 0x10c19
   __TEXT.__swift5_types: 0x54
   __TEXT.__objc_classname: 0x28b
-  __TEXT.__objc_methname: 0x822
+  __TEXT.__objc_methname: 0x832
   __TEXT.__swift5_capture: 0x188
-  __TEXT.__cstring: 0xa640
+  __TEXT.__cstring: 0xa652
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_protos: 0xc
   __TEXT.__objc_methtype: 0x16c
-  __TEXT.__unwind_info: 0x8238
+  __TEXT.__unwind_info: 0x8250
   __TEXT.__eh_frame: 0xbd0
-  __DATA_CONST.__const: 0x10008
-  __DATA_CONST.__cfstring: 0x1220
+  __DATA_CONST.__const: 0x10028
+  __DATA_CONST.__cfstring: 0x1240
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_intobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x1068
+  __DATA_CONST.__auth_got: 0x1070
   __DATA_CONST.__got: 0x348
   __DATA_CONST.__auth_ptr: 0xe8
   __DATA.__objc_const: 0xd28
-  __DATA.__objc_selrefs: 0x2d0
+  __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_data: 0x1f0
   __DATA.__data: 0xc50
   __DATA.__common: 0x9e2a0
-  __DATA.__bss: 0x3b8
+  __DATA.__bss: 0x3d0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9992
-  Symbols:   59862
-  CStrings:  2725
+  Functions: 9993
+  Symbols:   59872
+  CStrings:  2729
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-5a0131e3adc059d69b87924e6e6341a8.o)
+ __ZNK15GpsdPreferences17acLongitudeOffsetEv
+ __ZThn304_N21GpsdGnssDeviceManager13handleRequestERKN5proto4gpsd7RequestE
+ __ZThn304_N21GpsdGnssDeviceManagerD0Ev
+ __ZThn304_N21GpsdGnssDeviceManagerD1Ev
+ ____ZNK15GpsdPreferences17acLongitudeOffsetEv_block_invoke
+ _objc_msgSend$floatValue
+ _objc_opt_isKindOfClass
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/CoreGPS/install/Symbols/BuiltProducts/libGPSDaemon.a(GpsdClientManager-d70f5d96e9af4663fc198895c2234454.o)
- _$s9Tightbeam0A7EncoderVSgWOh
- __ZL9fDefaults
- __ZThn296_N21GpsdGnssDeviceManager13handleRequestERKN5proto4gpsd7RequestE
- __ZThn296_N21GpsdGnssDeviceManagerD0Ev
- __ZThn296_N21GpsdGnssDeviceManagerD1Ev
CStrings:
+ "#gdm,ACLongitudeOffset,applied,%{public}.6f,trackAge,%{public}.3f"
+ "#version,CoreGPS-365.0.6,machContSec,%{public}.3f,BuildTime,{Jun 30 2026,21:07:20}"
+ "21:10:40"
+ "ACLongitudeOffset"
+ "Jun 30 2026"
+ "floatValue"
- "#version,CoreGPS-365.0.5,machContSec,%{public}.3f,BuildTime,{Jun 18 2026,19:48:09}"
- "19:51:04"
- "Jun 18 2026"

```
