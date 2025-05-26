## dietappleh16camerad

> `/usr/sbin/dietappleh16camerad`

```diff

-1.300.0.0.0
-  __TEXT.__text: 0x14334
-  __TEXT.__auth_stubs: 0xdc0
+2.403.0.0.0
+  __TEXT.__text: 0x14e8c
+  __TEXT.__auth_stubs: 0xe10
   __TEXT.__objc_stubs: 0x4c0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__const: 0x18d0
-  __TEXT.__oslogstring: 0x1109
-  __TEXT.__cstring: 0x2f7b
+  __TEXT.__const: 0x14f8
+  __TEXT.__oslogstring: 0x12fb
+  __TEXT.__cstring: 0x32dd
   __TEXT.__gcc_except_tab: 0x334
   __TEXT.__objc_methname: 0x334
-  __TEXT.__unwind_info: 0x50c
+  __TEXT.__unwind_info: 0x514
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0x6f0
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__got: 0xf0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xd500
-  __DATA_CONST.__cfstring: 0x1180
+  __DATA_CONST.__const: 0x3f20
+  __DATA_CONST.__cfstring: 0x1360
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_selrefs: 0x130
-  __DATA.__objc_classrefs: 0x58
-  __DATA.__data: 0x109b80
+  __DATA.__data: 0x1c1b80
   __DATA.__common: 0x7
   __DATA.__bss: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 332
-  Symbols:   273
-  CStrings:  496
+  Functions: 335
+  Symbols:   277
+  CStrings:  538
 
Symbols:
+ _AMFDRCreateInstanceString
+ _AMFDRSealingMapCopyLocalMinimalManifestForInstance
+ _CFBooleanGetValue
+ _os_log_create
+ _remove
- ___stderrp
CStrings:
+ "%@-%@"
+ "%s - Parsing ISPUnitInfo.plist\n"
+ "%s : Status = %08x; HPR - %s \n"
+ "%s : noHPR boot-arg set \n"
+ "%s No module or Unauthorized swap (cmpmStatus = 0x%x) or No CmPM data (perhaps cuz the device does not support CmPM) [error]: %s \n"
+ "%s [error]: %s \n"
+ "%s: type=0x%X, isOverride=%d, size=%u, isEarlyBoot=%d, status=%08x\n"
+ "/usr/local/share/firmware/isp/2224_01XX.dat"
+ "/usr/local/share/firmware/isp/3624_01XX.dat"
+ "/usr/local/share/firmware/isp/3624_02XX.dat"
+ "/usr/local/share/firmware/isp/4524_01XX.dat"
+ "/usr/local/share/firmware/isp/7324_01XX.dat"
+ "/usr/local/share/firmware/isp/7524_01XX.dat"
+ "/usr/local/share/firmware/isp/CmPM-DPCd.DAT"
+ "/usr/local/share/firmware/isp/CmPM-DPCm.DAT"
+ "/usr/local/share/firmware/isp/CmPM-brcl.DAT"
+ "/usr/local/share/firmware/isp/CmPM-brgd.DAT"
+ "/usr/local/share/firmware/isp/CmPM-dcnu.DAT"
+ "/usr/local/share/firmware/isp/Savage/FrontIRHPR.DER"
+ "/var/mobile/Library/ISP/CalData/DCNUMetadata_0"
+ "/var/mobile/Library/ISP/CalData/DCNUPixbuf_0"
+ "2.403"
+ "BackCameraSNUM"
+ "BackCameraSNUM/BackSuperWideCameraSNUM exists - load FDR CmPM calibration data\n"
+ "BackSuperWideCameraSNUM"
+ "CmPM"
+ "Couldn't combine frontIR chipIDStr and uidStr"
+ "Couldn't create SavageChipID string ref"
+ "Couldn't create SavageUID string ref"
+ "Couldn't read BackCameraSNUM and BackSuperWideCameraSNUM. Sensor is hosed/disconnected. Skip loading FDR CmPM calibration data\n"
+ "Couldn't read SavageChipID"
+ "Couldn't read SavageUID"
+ "DPCd"
+ "DPCm"
+ "Found FrontIR override (has highest precedence) HPR file - camChannel = %d"
+ "GetUnitInfoPropertyDict"
+ "H16ISPServicesAssistant: setProperty %d complete (res=0x%08X)\n"
+ "H16ISPServicesRemoteIORegPropertyDataKey"
+ "H16ISPServicesRemoteIORegPropertyNameKey"
+ "IgnoreUnitInfoPlist"
+ "LoadFDRDataFileCMPM"
+ "LoadFrontIRHPRFile"
+ "LoadHPR"
+ "No HPR file for frontIR found"
+ "SavageChipID"
+ "SavageUID"
+ "brcl"
+ "brgd"
+ "com.apple.isp"
+ "dcnu"
+ "services"
- "/usr/local/share/firmware/isp/7523_01XX.dat"
- "/usr/local/share/firmware/isp/h13_isp_fw.bin"
- "/usr/local/share/firmware/isp/h14_isp_fw.bin"
- "1.300"
- "Error: ISP_OverrideSensorClockFrequency returned an error: 0x%08X\n"
- "H10ISPServicesAssistant: setProperty %d complete (res=0x%08X)\n"
- "H16ISP: Cannot cache bufferPoolInfo[%u][%u], result = 0x%08x"
- "Parsing ISPUnitInfo.plist \n"
- "Successfully set camera %d clock divider over-ride: 0x%08X\n"

```
