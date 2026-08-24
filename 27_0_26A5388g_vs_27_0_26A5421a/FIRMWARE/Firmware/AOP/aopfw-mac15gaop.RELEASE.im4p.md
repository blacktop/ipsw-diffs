## aopfw-mac15gaop.RELEASE.im4p

> `Firmware/AOP/aopfw-mac15gaop.RELEASE.im4p`

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

-  __TEXT.__text: 0x89d30
-  __TEXT.__const: 0x55c0
-  __TEXT.__cstring: 0x6cc2
+  __TEXT.__text: 0x8a9d4
+  __TEXT.__const: 0x5628
+  __TEXT.__cstring: 0x6d3e
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x12f68
-  __DATA.__const: 0x99d8
+  __DATA.__const: 0x99c8
   __DATA.__data: 0x9dd8
   __DATA._rtk_mtab: 0x6c0
-  __DATA._rtk_patchbay: 0x2fa
+  __DATA._rtk_patchbay: 0x306
   __DATA.__version: 0x8
   __DATA._spu_service: 0x330
   __DATA._spu_endpoint: 0x60

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xb7250
-  __ETEXT.__text: 0x12c30
-  __ETEXT.__StaticInit: 0x972c
-  __ETEXT.__const: 0x4c0
+  __DATA.__zerofill: 0xb76f0
+  __ETEXT.__text: 0x12cf4
+  __ETEXT.__StaticInit: 0x9734
+  __ETEXT.__const: 0x4d0
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x12b23
+  __OS_LOG.__string: 0x12bdd
   __MISC.__apf_list: 0xa0
-  __CMA.__cma_log_string: 0x123f
-  Functions: 2269
+  __CMA.__cma_log_string: 0x1259
+  Functions: 2255
   Symbols:   0
-  CStrings:  2049
+  CStrings:  2053
 
CStrings:
+ "15:34:21"
+ "15:39:41"
+ "AppleSPUFirmware-2444.1.1~66"
+ "Aug  8 2026"
+ "BMI284::bmi284_nvm_crc_check(): NVM CRC mismatch crc_reg=0x%x crc_calc=0x%x -- accel/gyro services will be DISABLED"
+ "BMI284::initialize() FAILED -- accel/gyro services will be DISABLED ()"
+ "BMI284::probeSensor() retry no.%d"
+ "BMI284::start() FAILED -- accel/gyro services will be DISABLED ()"
+ "SCM Error: Reconfiguring channel=%u"
+ "[AUD] aop-audprovr2 v600.21 built %s %s, %s state"
+ "[AUD] exp \"_doCfgData()\" fail, %s(), ln 352, stat %#x"
+ "[AUD] exp \"_doEnableData(false)\" fail, %s(), ln 390, stat %#x"
+ "[AUD] exp \"_doEnableData(true)\" fail, %s(), ln 353, stat %#x"
+ "[AUD] exp \"_doGetInputBytesAvail(byteCount)\" fail, %s(), ln 421"
+ "[AUD] exp \"_doReadInputBytes(inBuffer, byteCount)\" fail, %s(), ln 569, stat %#x"
+ "[AUD] exp \"_enableClk(false)\" fail, %s(), ln 229, stat %#x"
+ "[AUD] exp \"_enableClk(true)\" fail, %s(), ln 215, stat %#x"
+ "[AUD] exp \"_enableClkNoRefCount(false)\" fail, %s(), ln 255, stat %#x"
+ "[AUD] exp \"_enableClkNoRefCount(true)\" fail, %s(), ln 251, stat %#x"
+ "[AUD] exp \"_enableData(false)\" fail, %s(), ln 232, stat %#x"
+ "[AUD] exp \"_enableData(true)\" fail, %s(), ln 218, stat %#x"
+ "[AUD] exp \"_enableDataNoRefCount(false)\" fail, %s(), ln 291, stat %#x"
+ "[AUD] exp \"_enableDataNoRefCount(true)\" fail, %s(), ln 287, stat %#x"
+ "[AUD] exp \"_enableHPClk(false)\" fail, %s(), ln 205, stat %#x"
+ "[AUD] exp \"_enableHPClk(true)\" fail, %s(), ln 201, stat %#x"
+ "[AUD] exp \"_setClkCfg(cfg)\" fail, %s(), ln 656, stat %#x"
+ "[AUD] exp \"_setClkCfg(cfg)\" fail, %s(), ln 671, stat %#x"
+ "[AUD] exp \"_setClkCfg(cfg)\" fail, %s(), ln 688, stat %#x"
+ "[AUD] exp \"mClkPolicy.enableClk(false)\" fail, %s(), ln 274, stat %#x"
+ "[AUD] exp \"mClkPolicy.enableClk(true)\" fail, %s(), ln 270, stat %#x"
+ "[AUD] exp \"mClkPolicy.setApPowerState(false)\" fail, %s(), ln 174, stat %#x"
+ "[AUD] exp \"mClkPolicy.setApPowerState(true)\" fail, %s(), ln 168, stat %#x"
+ "[AUD] exp \"mClkPolicy.setClkCfg(PDMClkPolicy::kLowPower, (PDM2ClockSource)mLowPowerConfig->clockSource, mLowPowerConfig->pdmFrequency)\" fail, %s(), ln 136, stat %#x"
+ "[AUD] exp \"mHPClkSwitch.setHPClkCfg((PDM2ClockSource)mHighPowerConfig->clockSource, mHighPowerConfig->pdmFrequency)\" fail, %s(), ln 403, stat %#x"
+ "[AUD] exp \"mHPClkSwitch.setHPClkCfg(PDM2ClockSource::kInputCLKOff, 0)\" fail, %s(), ln 407, stat %#x"
+ "[AUD] exp \"mPdmClk->_doCfgClk(inCfg.mSrc, inCfg.mFreq)\" fail, %s(), ln 740, stat %#x"
+ "[AUD] exp \"mPdmClk->_doEnableClk(false)\" fail, %s(), ln 697, stat %#x"
+ "[AUD] exp \"mPdmClk->_doEnableClk(true)\" fail, %s(), ln 690, stat %#x"
+ "[AUD] exp \"mPdmNode->_enableClkNoRefCount(false)\" fail, %s(), ln 810, stat %#x"
+ "[AUD] exp \"mPdmNode->_enableClkNoRefCount(true)\" fail, %s(), ln 841, stat %#x"
+ "[AUD] exp \"mPdmNode->_enableDataNoRefCount(false)\" fail, %s(), ln 808, stat %#x"
+ "[AUD] exp \"mPdmNode->_enableDataNoRefCount(true)\" fail, %s(), ln 844, stat %#x"
+ "[AUD] exp \"mPdmNode->mClkPolicy.enableClk(false)\" fail, %s(), ln 816, stat %#x"
+ "[AUD] exp \"mPdmNode->mClkPolicy.enableClk(true)\" fail, %s(), ln 822, stat %#x"
+ "[AUD] exp \"mPdmNode->mClkPolicy.setClkCfg(PDMAudioNodeBase::PDMClkPolicy::kHighPower, inSrc, inFreq)\" fail, %s(), ln 819, stat %#x"
+ "[AUD] exp \"super::_setProperty( inProperty, inPropertyData, inPropertySize )\" fail, %s(), ln 118"
+ "[AUD] exp \"super::_setProperty( inProperty, inPropertyData, inPropertySize )\" fail, %s(), ln 121, stat %#x"
+ "[AUD] exp \"super::init(inProvider)\" fail, %s(), ln 97, stat %#x"
+ "[AUD] ptr \"mLowPowerConfig\" is null, cant cont, %s(), ln 128, stat %#x"
- "00:05:40"
- "23:59:37"
- "AppleSPUFirmware-2444.0.12~90"
- "Jul  9 2026"
- "Jul 10 2026"
- "[AUD] aop-audprovr2 v600.20 built %s %s, %s state"
- "[AUD] exp \"_doCfgData()\" fail, %s(), ln 323, stat %#x"
- "[AUD] exp \"_doEnableData(false)\" fail, %s(), ln 350, stat %#x"
- "[AUD] exp \"_doEnableData(true)\" fail, %s(), ln 324, stat %#x"
- "[AUD] exp \"_doGetInputBytesAvail(byteCount)\" fail, %s(), ln 381"
- "[AUD] exp \"_doReadInputBytes(inBuffer, byteCount)\" fail, %s(), ln 416, stat %#x"
- "[AUD] exp \"_enableClk(false)\" fail, %s(), ln 212, stat %#x"
- "[AUD] exp \"_enableClk(true)\" fail, %s(), ln 198, stat %#x"
- "[AUD] exp \"_enableClkNoRefCount(false)\" fail, %s(), ln 238, stat %#x"
- "[AUD] exp \"_enableClkNoRefCount(true)\" fail, %s(), ln 234, stat %#x"
- "[AUD] exp \"_enableData(false)\" fail, %s(), ln 215, stat %#x"
- "[AUD] exp \"_enableData(true)\" fail, %s(), ln 201, stat %#x"
- "[AUD] exp \"_enableDataNoRefCount(false)\" fail, %s(), ln 274, stat %#x"
- "[AUD] exp \"_enableDataNoRefCount(true)\" fail, %s(), ln 270, stat %#x"
- "[AUD] exp \"_enableHPClk(false)\" fail, %s(), ln 188, stat %#x"
- "[AUD] exp \"_enableHPClk(true)\" fail, %s(), ln 184, stat %#x"
- "[AUD] exp \"_setClkCfg(cfg)\" fail, %s(), ln 471, stat %#x"
- "[AUD] exp \"_setClkCfg(cfg)\" fail, %s(), ln 486, stat %#x"
- "[AUD] exp \"_setClkCfg(cfg)\" fail, %s(), ln 503, stat %#x"
- "[AUD] exp \"mClkPolicy.enableClk(false)\" fail, %s(), ln 257, stat %#x"
- "[AUD] exp \"mClkPolicy.enableClk(true)\" fail, %s(), ln 253, stat %#x"
- "[AUD] exp \"mClkPolicy.setApPowerState(false)\" fail, %s(), ln 157, stat %#x"
- "[AUD] exp \"mClkPolicy.setApPowerState(true)\" fail, %s(), ln 151, stat %#x"
- "[AUD] exp \"mClkPolicy.setClkCfg(PDMClkPolicy::kLowPower, (PDM2ClockSource)mLowPowerConfig->clockSource, mLowPowerConfig->pdmFrequency)\" fail, %s(), ln 119, stat %#x"
- "[AUD] exp \"mHPClkSwitch.setHPClkCfg((PDM2ClockSource)mHighPowerConfig->clockSource, mHighPowerConfig->pdmFrequency)\" fail, %s(), ln 363, stat %#x"
- "[AUD] exp \"mHPClkSwitch.setHPClkCfg(PDM2ClockSource::kInputCLKOff, 0)\" fail, %s(), ln 367, stat %#x"
- "[AUD] exp \"mPdmClk->_doCfgClk(inCfg.mSrc, inCfg.mFreq)\" fail, %s(), ln 555, stat %#x"
- "[AUD] exp \"mPdmClk->_doEnableClk(false)\" fail, %s(), ln 512, stat %#x"
- "[AUD] exp \"mPdmClk->_doEnableClk(true)\" fail, %s(), ln 505, stat %#x"
- "[AUD] exp \"mPdmNode->_enableClkNoRefCount(false)\" fail, %s(), ln 617, stat %#x"
- "[AUD] exp \"mPdmNode->_enableClkNoRefCount(true)\" fail, %s(), ln 636, stat %#x"
- "[AUD] exp \"mPdmNode->_enableDataNoRefCount(false)\" fail, %s(), ln 615, stat %#x"
- "[AUD] exp \"mPdmNode->_enableDataNoRefCount(true)\" fail, %s(), ln 639, stat %#x"
- "[AUD] exp \"mPdmNode->mClkPolicy.enableClk(false)\" fail, %s(), ln 623, stat %#x"
- "[AUD] exp \"mPdmNode->mClkPolicy.enableClk(true)\" fail, %s(), ln 629, stat %#x"
- "[AUD] exp \"mPdmNode->mClkPolicy.setClkCfg(PDMAudioNodeBase::PDMClkPolicy::kHighPower, inSrc, inFreq)\" fail, %s(), ln 626, stat %#x"
- "[AUD] exp \"super::_setProperty( inProperty, inPropertyData, inPropertySize )\" fail, %s(), ln 101"
- "[AUD] exp \"super::_setProperty( inProperty, inPropertyData, inPropertySize )\" fail, %s(), ln 104, stat %#x"
- "[AUD] exp \"super::init(inProvider)\" fail, %s(), ln 80, stat %#x"
- "[AUD] ptr \"mLowPowerConfig\" is null, cant cont, %s(), ln 111, stat %#x"
```
