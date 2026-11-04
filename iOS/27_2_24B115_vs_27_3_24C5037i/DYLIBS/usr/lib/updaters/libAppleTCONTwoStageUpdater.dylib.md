## libAppleTCONTwoStageUpdater.dylib

> `/usr/lib/updaters/libAppleTCONTwoStageUpdater.dylib`

```diff

-230.40.6.0.0
-  __TEXT.__text: 0xb04
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x5fa
-  __TEXT.__const: 0x8
+230.60.4.0.0
+  __TEXT.__text: 0x3f34
+  __TEXT.__cstring: 0x1304
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x31
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__unwind_info: 0x1b8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x28
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xc0
-  __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__const: 0x108
+  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__weak_auth_got: 0x20
+  __AUTH_CONST.__auth_got: 0x238
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libPCDSUpdater.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 20
-  Symbols:   70
-  CStrings:  33
+  - /usr/lib/libz.1.dylib
+  Functions: 77
+  Symbols:   203
+  CStrings:  180
 
Symbols:
+ GCC_except_table0
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table4
+ GCC_except_table47
+ _AMSupportCFDictionarySetBoolean
+ _AMSupportCFDictionarySetInteger32
+ _AMSupportGetUInt32
+ _AMSupportGetValueForKeyPathInDict
+ _CFArrayGetCount
+ _CFArrayGetTypeID
+ _CFArrayGetValueAtIndex
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFDataCreate
+ _CFDataCreateMutable
+ _CFDataGetBytePtr
+ _CFDataGetBytes
+ _CFDataGetLength
+ _CFDataGetMutableBytePtr
+ _CFDataGetTypeID
+ _CFDataSetLength
+ _CFDictionaryGetTypeID
+ _CFDictionaryGetValue
+ _CFEqual
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFPropertyListCreateWithData
+ _CFStringGetCString
+ _IOAVDisplayMemoryCreateWithName
+ _IOAVDisplayMemoryRead
+ _IOAVDisplayMemoryWrite
+ _IOObjectRelease
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __ZN15AppleTCONDevice17eventCmdQueryInfoEPK14__CFDictionaryPS0_
+ __ZN15AppleTCONDevice24eventCmdPerformNextStageEPK14__CFDictionaryS2_Rh
+ __ZN15AppleTCONDeviceD0Ev
+ __ZN15AppleTCONDeviceD1Ev
+ __ZN20AppleTCONDPUnifiedFW14decompressGzipEPK8__CFData
+ __ZN20AppleTCONDPUnifiedFW16applyBxdiffPatchEPKhmS1_m
+ __ZN20AppleTCONDPUnifiedFWC1EPK8__CFDatajjjj
+ __ZN20AppleTCONDPUnifiedFWC2EPK8__CFDatajjjj
+ __ZN20AppleTCONDPUnifiedFWD1Ev
+ __ZN20AppleTCONDPUnifiedFWD2Ev
+ __ZN24AppleTCONDPUnifiedDevice10getBoardIDEPj
+ __ZN24AppleTCONDPUnifiedDevice11getVendorIDEPj
+ __ZN24AppleTCONDPUnifiedDevice12getLifeCycleEPK14__CFDictionaryPj
+ __ZN24AppleTCONDPUnifiedDevice12waitForReadyEPh
+ __ZN24AppleTCONDPUnifiedDevice13getPRODStatusEPh
+ __ZN24AppleTCONDPUnifiedDevice13getSDOMStatusEPh
+ __ZN24AppleTCONDPUnifiedDevice14submitDeviceIDEPh
+ __ZN24AppleTCONDPUnifiedDevice15getOptionsValueEPK14__CFDictionaryPK10__CFString
+ __ZN24AppleTCONDPUnifiedDevice15resetAndRecoverEv
+ __ZN24AppleTCONDPUnifiedDevice16testOptionsValueEPK14__CFDictionaryPK10__CFStringPKv
+ __ZN24AppleTCONDPUnifiedDevice17eventCmdQueryInfoEPK14__CFDictionaryPS0_
+ __ZN24AppleTCONDPUnifiedDevice17updateConfigImageEPKhjhh
+ __ZN24AppleTCONDPUnifiedDevice17writeDataIndirectEjPKhj
+ __ZN24AppleTCONDPUnifiedDevice18updateFWComponentsEPK14__CFDictionaryP20AppleTCONDPUnifiedFW
+ __ZN24AppleTCONDPUnifiedDevice19getTCONOptionsValueEPK14__CFDictionaryPK10__CFString
+ __ZN24AppleTCONDPUnifiedDevice19isOTPUpdateRequiredEPK14__CFDictionary
+ __ZN24AppleTCONDPUnifiedDevice21downloadFirmwareImageEPKhj
+ __ZN24AppleTCONDPUnifiedDevice24eventCmdPerformNextStageEPK14__CFDictionaryS2_Rh
+ __ZN24AppleTCONDPUnifiedDevice28isFWComponentsUpdateRequiredEPK14__CFDictionaryS2_P20AppleTCONDPUnifiedFW
+ __ZN24AppleTCONDPUnifiedDevice7getECIDEPhj
+ __ZN24AppleTCONDPUnifiedDevice7sendCmdEhhhhj
+ __ZN24AppleTCONDPUnifiedDevice8dfuResetEv
+ __ZN24AppleTCONDPUnifiedDevice8getHWCIDEPj
+ __ZN24AppleTCONDPUnifiedDevice8getNonceEPhj
+ __ZN24AppleTCONDPUnifiedDevice8readDataEjPh
+ __ZN24AppleTCONDPUnifiedDevice9dfuUpdateEPK14__CFDictionaryP20AppleTCONDPUnifiedFW
+ __ZN24AppleTCONDPUnifiedDevice9updateOTPEPK14__CFDictionary
+ __ZN24AppleTCONDPUnifiedDevice9writeDataEPKhj
+ __ZN24AppleTCONDPUnifiedDeviceC1EjPK14__CFDictionary
+ __ZN24AppleTCONDPUnifiedDeviceC2EjPK14__CFDictionary
+ __ZN24AppleTCONDPUnifiedDeviceD0Ev
+ __ZN24AppleTCONDPUnifiedDeviceD1Ev
+ __ZN24AppleTCONDPUnifiedDeviceD2Ev
+ __ZN33AppleTCONTwoStageUpdateController57AppleTCONTwoStageUpdateControllerIsPreflightTicketMissingEPK14__CFDictionary
+ __ZTI15AppleTCONDevice
+ __ZTI24AppleTCONDPUnifiedDevice
+ __ZTS15AppleTCONDevice
+ __ZTS24AppleTCONDPUnifiedDevice
+ __ZTV15AppleTCONDevice
+ __ZTV24AppleTCONDPUnifiedDevice
+ __ZTVN10__cxxabiv117__class_type_infoE
+ __ZTVN10__cxxabiv120__si_class_type_infoE
+ __ZZN20AppleTCONDPUnifiedFW16applyBxdiffPatchEPKhmS1_mEN11Accumulator5writeEPvPKvy
+ __ZdaPvSt19__type_descriptor_t
+ __ZnamSt19__type_descriptor_t
+ _bzero
+ _dlclose
+ _dlerror
+ _dlopen
+ _dlsym
+ _free
+ _inflate
+ _inflateEnd
+ _inflateInit2_
+ _kAppleTCONCommonOptionDebugRegisterAccess
+ _kAppleTCONCommonOptionForceDFU
+ _kAppleTCONCommonOptionFuseProd
+ _kAppleTCONCommonOptionFuseSDOM
+ _kAppleTCONCommonOptionInternalBundle
+ _kAppleTCONCommonOptionSkipSameVersion
+ _kAppleTCONCommonTagDeviceBoardID
+ _kAppleTCONCommonTagDeviceChipID
+ _kAppleTCONCommonTagDeviceDebugRegisterAccess
+ _kAppleTCONCommonTagDeviceECID
+ _kAppleTCONCommonTagDeviceHWCID
+ _kAppleTCONCommonTagDeviceLife
+ _kAppleTCONCommonTagDeviceMinorVersion
+ _kAppleTCONCommonTagDeviceNonce
+ _kAppleTCONCommonTagDeviceProductionMode
+ _kAppleTCONCommonTagDeviceSDOM
+ _kAppleTCONCommonTagDeviceVendorID
+ _kAppleTCONCommonTagResponseTicket
+ _malloc_type_malloc
+ _malloc_type_realloc
+ _memcpy
+ _memset
+ _printf
+ _puts
+ _usleep
- GCC_except_table3
CStrings:
+ "/usr/lib/libParallelCompression.dylib"
+ "1.2.12"
+ "Address"
+ "AppleTCONDPUnifiedDevice::eventCmdPerformNextStage: Finished Personalization\n"
+ "AppleTCONDPUnifiedDevice::eventCmdPerformStage stage=%d commit=%d\n"
+ "AppleTCONDPUnifiedFW"
+ "AppleTCONDPUnifiedFW: BXPatch5 failed (result=%d)\n"
+ "AppleTCONDPUnifiedFW: BXPatch5 symbol not found: %s\n"
+ "AppleTCONDPUnifiedFW: gzip ISIZE is zero, file may be corrupt"
+ "AppleTCONDPUnifiedFW: gzip inflate failed, status=%d msg=%s\n"
+ "AppleTCONDPUnifiedFW: gzip input too small (%ld bytes)\n"
+ "AppleTCONDPUnifiedFW: init fails."
+ "AppleTCONDPUnifiedFW: libParallelCompression unavailable: %s\n"
+ "AppleTCONTwoStageUpdateController::start: no preflight ticket, skipping update\n"
+ "AppleTconDev(v3):(%d:%d:%d:%d:%d)\n"
+ "BOOTROM_SECURE_SEQUENCE=0x%x\n"
+ "BOOTROM_SEQUENCE=0x%x\n"
+ "BXPatch5"
+ "Baobab,BoardID"
+ "Baobab,ChipID"
+ "Baobab,DebugRegisterAccess"
+ "Baobab,ECID"
+ "Baobab,HWCID"
+ "Baobab,Life"
+ "Baobab,MinorVersion"
+ "Baobab,Nonce"
+ "Baobab,ProductionMode"
+ "Baobab,SecurityDomain"
+ "Baobab,Ticket"
+ "Baobab,VendorID"
+ "BoardID"
+ "BootedOS"
+ "Build"
+ "ConfigSubCmd"
+ "Configs"
+ "Configurations"
+ "DFU update complete: major=0x%02x minor=0x%02x dfuVersion=0x%08x\n"
+ "DPCD_STAT=0x%x\n"
+ "DebugRegisterAccess"
+ "DeferredCommit"
+ "Dev:CmdQueryInfo failure %s\n"
+ "Dev:next stage failure %s\n"
+ "DeviceID"
+ "Digest"
+ "DirectNVMUpdatePreferred"
+ "FW Update Options I:%d S:%d Matched:%d ver:%d(%d)\n"
+ "FWConfigAPICMD"
+ "FWConfigDigest"
+ "FWConfigs"
+ "FWImg"
+ "FWImgDigest"
+ "FW_SEQUENCE=0x%x\n"
+ "Failed to get DFU NVM major version\n"
+ "Failed to get DFU NVM minor version\n"
+ "Failed to get DFU version\n"
+ "Failed to get Prod status\n"
+ "Failed to get SDOM status\n"
+ "Failed to get major version\n"
+ "Failed to get memoryRef handle\n"
+ "Failed to get minor version\n"
+ "Failed to get panel revision\n"
+ "Failed to getIORegRootNode. Will Attempt fallback.\n"
+ "FirmwareData"
+ "ForceDFU"
+ "ForceDFU requested\n"
+ "Fuse Prod (%d:%d)\n"
+ "Fuse SDOM (%d:%d)\n"
+ "FusePROD"
+ "FuseSDOM"
+ "HALT REASON=0x%x\n"
+ "HWConfig"
+ "INTERRUPT_STATUS=0x%x\n"
+ "ImageProperties"
+ "Length"
+ "Limited"
+ "Major"
+ "Minor"
+ "Name"
+ "Option2"
+ "Options.%@"
+ "Options.DeferredCommit"
+ "Options.PreflightRequired"
+ "Options.PreflightTickets"
+ "PORUpdatePreferred"
+ "Patches"
+ "Payload"
+ "PreflightContext"
+ "ProtectedRegions"
+ "RestoreInternal"
+ "RestoreOptions.AppleTCONTwoStageOptions.%@"
+ "RestoreOptions.AppleTCONTwoStageOptions.LifeCycle"
+ "S6TUDP1"
+ "SDOM not fused. No Fusing option. Skip updating.\n"
+ "SkipSameVersion"
+ "Update to 0x%02x\n"
+ "Zero dev bundle ver detected, force DFU\n"
+ "alloc: failed"
+ "apply staged firmware failed"
+ "bxdiff"
+ "complete_binary"
+ "conversion error"
+ "download boot param failed"
+ "download config failed"
+ "download dmem failed"
+ "download dmem size failed"
+ "download fw failed"
+ "download imem failed"
+ "download imem size failed"
+ "download img4 failed"
+ "ecid alloc failed"
+ "end update failed"
+ "failed to auth"
+ "failed to dfu update"
+ "failed to find config"
+ "failed to find firmware"
+ "firmware missing"
+ "get vendor:id failed"
+ "getBoardID failed"
+ "getHWCID failed"
+ "getLifeCycle %s\n"
+ "getLifeCycle failed"
+ "getVendorID failed"
+ "invalid TSS response size"
+ "invalid config size"
+ "invalid firmware size"
+ "invalid fw"
+ "invalid type"
+ "major"
+ "memory alloc failed"
+ "no device id"
+ "nonce alloc failed"
+ "otp update failed"
+ "out of range"
+ "patches_policy"
+ "read dpcd stat failed"
+ "readData timed out.\n"
+ "resetAndRecover timed out. Last status: 0x%02X\n"
+ "start update failed"
+ "submit dev:id failed"
+ "tcon-registers"
+ "ticket missing"
+ "update fw error:%s\n"
+ "updates failed"
+ "version_check_policy"
+ "waitForReady timed out. Last status: 0x%02X\n"
+ "write fw load failed"
+ "writeData timed out. Last status: 0x%02X\n"
```
