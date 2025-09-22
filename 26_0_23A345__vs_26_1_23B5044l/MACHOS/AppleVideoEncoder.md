## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

-904.76.7.0.0
-  __TEXT.__text: 0x18c824
+904.88.0.0.0
+  __TEXT.__text: 0x1807d8
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0xc
   __TEXT.__const: 0x22528
-  __TEXT.__cstring: 0x52375
+  __TEXT.__cstring: 0x526cc
   __TEXT.__gcc_except_tab: 0x720
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x8a8
+  __TEXT.__unwind_info: 0x8a0
   __DATA_CONST.__auth_got: 0x838
   __DATA_CONST.__got: 0x760
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0xa0d8
+  __DATA_CONST.__const: 0xa0e0
   __DATA_CONST.__cfstring: 0x30a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__data: 0x178
+  __DATA.__data: 0x210
   __DATA.__bss: 0xff0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 65A59C3B-E587-3267-A0DF-A4528136A5F8
+  UUID: 6841F1EA-48F3-391B-A5FF-3BBA214827CC
   Functions: 1578
   Symbols:   511
-  CStrings:  6981
+  CStrings:  6986
 
CStrings:
+ "\t[%p %s rI:%d/%d L:%d U:%d S:%d]"
+ "\t[%p %s rI:%d/%d L:%d U:%d S:%d]\n"
+ "%lld %d AVE %s: \t[%p %s rI:%d/%d L:%d U:%d S:%d]"
+ "%lld %d AVE %s: \t[%p %s rI:%d/%d L:%d U:%d S:%d]\n"
+ "%lld %d AVE %s: %s:%d %s | Device not supported for MCTF in all-light: devType=%d, sensorID=0x%x, workMode=%d"
+ "%lld %d AVE %s: %s:%d %s | Device not supported for MCTF in all-light: devType=%d, sensorID=0x%x, workMode=%d\n"
+ "%lld %d AVE %s: %s:%d %s | Device not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d"
+ "%lld %d AVE %s: %s:%d %s | Device not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d\n"
+ "%lld %d AVE %s: %s:%d %s | Sensor not supported for MCTF in all-light: devType=%d, sensorID=0x%x, workMode=%d"
+ "%lld %d AVE %s: %s:%d %s | Sensor not supported for MCTF in all-light: devType=%d, sensorID=0x%x, workMode=%d\n"
+ "%lld %d AVE %s: %s:%d %s | SensorID not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d"
+ "%lld %d AVE %s: %s:%d %s | SensorID not supported for MCTF strength adjustment: devType=%d, sensorID=0x%x, workMode=%d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %p %p"
+ "%lld %d AVE %s: %s:%d %s | wrong params, %p %d %d %p %p\n"
+ "%lld %d AVE %s: %s:%d Disable B frames for encoding %dx%d frames at %dfps with MCTF to achieve realtime performance."
+ "%lld %d AVE %s: %s:%d Disable B frames for encoding %dx%d frames at %dfps with MCTF to achieve realtime performance.\n"
+ "(0 <= psInfo->iNum) && (psInfo->iNum < (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (((32) < (256) ? (32) : (256)) + 1)))"
+ "(0 <= psInfo->iNum) && (psInfo->iNum <= (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (((32) < (256) ? (32) : (256)) + 1)))"
+ "(psData != __null) && (piRangeIdx != __null) && (piStrength != __null) && eDevType > AVE_DevType_None && eDevType < AVE_DevType_Max && eMCTFWorkMode > AVE_MCTF_WorkMode_None && eMCTFWorkMode < AVE_MCTF_WorkMode_Max"
+ "20:37:31"
+ "20:37:33"
+ "20:37:35"
+ "20:37:36"
+ "904.88.0"
+ "MCTF_SMap"
+ "Sep 16 2025"
+ "eDevType > AVE_DevType_None && eDevType < AVE_DevType_Max && eMCTFWorkMode > AVE_MCTF_WorkMode_None && eMCTFWorkMode < AVE_MCTF_WorkMode_Max"
- "%lld %d AVE %s: %s:%d %s | Failed to get property value %p %lld %p %p %p"
- "%lld %d AVE %s: %s:%d %s | Failed to get property value %p %lld %p %p %p\n"
- "%lld %d AVE %s: %s:%d %s | Failed to get value %p %lld %p %p %p"
- "%lld %d AVE %s: %s:%d %s | Failed to get value %p %lld %p %p %p\n"
- "%lld %d AVE %s: %s:%d %s | device not supported %d"
- "%lld %d AVE %s: %s:%d %s | device not supported %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p\n"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p %d"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p %d\n"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p %d %d"
- "%lld %d AVE %s: %s:%d %s | fail to get value %p %lld %p %p %p %d %d\n"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x\n"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %p %p"
- "%lld %d AVE %s: %s:%d %s | wrong params, %p %p %p\n"
- "(0 <= psInfo->iNum) && (psInfo->iNum < (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * ((32) < (256) ? (32) : (256)) + 1))"
- "(0 <= psInfo->iNum) && (psInfo->iNum <= (((2) < ((63 + 1)) ? (2) : ((63 + 1))) * ((32) < (256) ? (32) : (256)) + 1))"
- "(psData != __null) && (piRangeIdx != __null) && (piStrength != __null)"
- "20:31:18"
- "20:31:19"
- "20:31:21"
- "904.76.7"
- "Aug 26 2025"

```
