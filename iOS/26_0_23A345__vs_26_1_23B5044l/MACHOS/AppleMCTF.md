## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-904.76.7.0.0
-  __TEXT.__text: 0x75a3c
+904.88.0.0.0
+  __TEXT.__text: 0x75aa8
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
   __TEXT.__gcc_except_tab: 0x63c
-  __TEXT.__cstring: 0x23475
+  __TEXT.__cstring: 0x236d5
   __TEXT.__const: 0x1eaf8
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x608
   __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4180
+  __DATA_CONST.__const: 0x4188
   __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x100
+  __DATA.__data: 0x198
   __DATA.__bss: 0x860
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6A2FE0F-9E59-3554-AD80-363341B59876
-  Functions: 613
+  UUID: EB04649E-56E2-38D3-AF7C-4B68FE81EFBD
+  Functions: 614
   Symbols:   354
-  CStrings:  2976
+  CStrings:  2980
 
CStrings:
+ "\t[%p %s rI:%d/%d L:%d U:%d S:%d]"
+ "\t[%p %s rI:%d/%d L:%d U:%d S:%d]\n"
+ "%lld %d AVE %s: \t[%p %s rI:%d/%d L:%d U:%d S:%d]"
+ "%lld %d AVE %s: \t[%p %s rI:%d/%d L:%d U:%d S:%d]\n"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %d %d"
+ "%lld %d AVE %s: %s:%d %s | AVE_MCTF_AdjustStrength failed %p %p %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | Device not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d"
+ "%lld %d AVE %s: %s:%d %s | Device not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d\n"
+ "%lld %d AVE %s: %s:%d %s | SensorID not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d"
+ "%lld %d AVE %s: %s:%d %s | SensorID not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %p %p"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %p %p\n"
+ "(0 <= psInfo->iNum) && (psInfo->iNum < (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (((32) < (256) ? (32) : (256)) + 1)))"
+ "(0 <= psInfo->iNum) && (psInfo->iNum <= (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (((32) < (256) ? (32) : (256)) + 1)))"
+ "(psData != __null) && (piRangeIdx != __null) && (piStrength != __null) && eDevType > AVE_DevType_None && eDevType < AVE_DevType_Max && eMCTFWorkMode > AVE_MCTF_WorkMode_None && eMCTFWorkMode < AVE_MCTF_WorkMode_Max"
+ "20:27:11"
+ "904.88.0"
+ "MCTF_SMap"
+ "Sep 16 2025"
- "%lld %d AVE %s: %s:%d %s | device not supported %d"
- "%lld %d AVE %s: %s:%d %s | device not supported %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p\n"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x\n"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %p %p"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %p %p\n"
- "(0 <= psInfo->iNum) && (psInfo->iNum < (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * ((32) < (256) ? (32) : (256)) + 1))"
- "(0 <= psInfo->iNum) && (psInfo->iNum <= (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * ((32) < (256) ? (32) : (256)) + 1))"
- "(psData != __null) && (piRangeIdx != __null) && (piStrength != __null)"
- "20:21:38"
- "904.76.7"
- "Aug 26 2025"
- "res"

```
