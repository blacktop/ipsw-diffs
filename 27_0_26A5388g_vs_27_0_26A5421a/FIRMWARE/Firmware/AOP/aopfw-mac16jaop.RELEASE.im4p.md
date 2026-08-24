## aopfw-mac16jaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac16jaop.RELEASE.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__version`
- `__DATA._spu_service`
- `__DATA._spu_endpoint`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0xbceec
-  __TEXT.__const: 0x9e20
-  __TEXT.__cstring: 0x51c3
+  __TEXT.__text: 0xbdb00
+  __TEXT.__const: 0x9e78
+  __TEXT.__cstring: 0x523f
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x2de20
-  __DATA.__const: 0xe008
+  __DATA.__const: 0xdff0
   __DATA.__data: 0x7158
-  __DATA._rtk_patchbay: 0x2fa
+  __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x5f8
   __DATA.__version: 0x8
   __DATA._spu_service: 0x300

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xb1180
-  __ETEXT.__text: 0x12354
+  __DATA.__zerofill: 0xb15a0
+  __ETEXT.__text: 0x12418
   __ETEXT.__StaticInit: 0x1c54
   __ETEXT.__const: 0x4c0
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x2c7e7
+  __OS_LOG.__string: 0x2c8a1
   __MISC.__apf_list: 0x80
-  __CMA.__cma_log_string: 0x123f
-  Functions: 2667
+  __CMA.__cma_log_string: 0x1259
+  Functions: 2652
   Symbols:   0
-  CStrings:  2868
+  CStrings:  2872
 
CStrings:
+ "15:34:21"
+ "15:39:45"
+ "15:39:46"
+ "AppleSPUFirmware-2444.1.1~66"
+ "Aug  8 2026"
+ "BMI284::bmi284_nvm_crc_check(): NVM CRC mismatch crc_reg=0x%x crc_calc=0x%x -- accel/gyro services will be DISABLED"
+ "BMI284::initialize() FAILED -- accel/gyro services will be DISABLED ()"
+ "BMI284::probeSensor() retry no.%d"
+ "BMI284::start() FAILED -- accel/gyro services will be DISABLED ()"
+ "SCM Error: Reconfiguring channel=%u"
+ "[AUD] aop-audprovr3 v600.21 built %s %s"
+ "[AUD] aop-audprovr3 v600.21 built %s %s, %s state"
+ "[AUD] exp \"AppleAOPAudioFirmware::System::getWorkLoop( AppleAOPAudioFirmware::Platform::RunLoopType::kAudio, workLoop)\" fail, %s(), ln 117, stat %#x"
+ "[AUD] exp \"RTKitAudioPlatform::initPlatform(&sRtkadIntrWorkLoop)\" fail, %s(), ln 86, stat %#x"
+ "[AUD] exp \"_transferData(transferReq)\" fail, %s(), ln 793, stat %#x"
+ "[AUD] exp \"initInterfaceMap(sInterfaceMap)\" fail, %s(), ln 177, stat %#x"
+ "[AUD] exp \"initRTKitAudioPlatform()\" fail, %s(), ln 160, stat %#x"
+ "[AUD] exp \"mAudioPacketRingBufferWriter.init()\" fail, %s(), ln 235, stat %#x"
+ "[AUD] exp \"ret\" fail, %s(), ln 816, stat %#x"
+ "[AUD] exp \"sEventQueueInterface.init(*workLoop)\" fail, %s(), ln 119, stat %#x"
+ "[AUD] exp \"sSecureEventQueueInterface.init(*workLoop)\" fail, %s(), ln 124, stat %#x"
+ "[AUD] exp \"super::_performStateChange(inClientMgrId, inChg, outPending)\" fail, %s(), ln 478, stat %#x"
+ "[AUD] exp \"super::ready()\" fail, %s(), ln 233, stat %#x"
+ "[AUD] fail, stat %#x, %s(), ln 240"
+ "[AUD] ptr \"workLoop\" is null, cant cont, %s(), ln 118, stat %#x"
- "00:05:46"
- "00:05:47"
- "23:59:37"
- "AppleSPUFirmware-2444.0.12~90"
- "Jul  9 2026"
- "Jul 10 2026"
- "[AUD] aop-audprovr3 v600.20 built %s %s"
- "[AUD] aop-audprovr3 v600.20 built %s %s, %s state"
- "[AUD] exp \"AppleAOPAudioFirmware::System::getWorkLoop( AppleAOPAudioFirmware::Platform::RunLoopType::kAudio, workLoop)\" fail, %s(), ln 112, stat %#x"
- "[AUD] exp \"RTKitAudioPlatform::initPlatform(&sRtkadIntrWorkLoop)\" fail, %s(), ln 81, stat %#x"
- "[AUD] exp \"_transferData(transferReq)\" fail, %s(), ln 788, stat %#x"
- "[AUD] exp \"initInterfaceMap(sInterfaceMap)\" fail, %s(), ln 172, stat %#x"
- "[AUD] exp \"initRTKitAudioPlatform()\" fail, %s(), ln 155, stat %#x"
- "[AUD] exp \"mAudioPacketRingBufferWriter.init()\" fail, %s(), ln 107, stat %#x"
- "[AUD] exp \"ret\" fail, %s(), ln 811, stat %#x"
- "[AUD] exp \"sEventQueueInterface.init(*workLoop)\" fail, %s(), ln 114, stat %#x"
- "[AUD] exp \"sSecureEventQueueInterface.init(*workLoop)\" fail, %s(), ln 119, stat %#x"
- "[AUD] exp \"super::_performStateChange(inClientMgrId, inChg, outPending)\" fail, %s(), ln 217, stat %#x"
- "[AUD] exp \"super::ready()\" fail, %s(), ln 105, stat %#x"
- "[AUD] fail, stat %#x, %s(), ln 112"
- "[AUD] ptr \"workLoop\" is null, cant cont, %s(), ln 113, stat %#x"
```
