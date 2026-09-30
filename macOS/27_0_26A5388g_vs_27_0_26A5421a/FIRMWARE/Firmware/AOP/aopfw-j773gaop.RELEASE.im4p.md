## aopfw-j773gaop.RELEASE.im4p

> `Firmware/AOP/aopfw-j773gaop.RELEASE.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__version`
- `__DATA._spu_service`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x8bd30
+  __TEXT.__text: 0x8be00
   __TEXT.__const: 0x84f0
-  __TEXT.__cstring: 0x4c64
+  __TEXT.__cstring: 0x4c63
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x28
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_heap: 0xca20
   __DATA.__const: 0xaab0
   __DATA.__data: 0x6b30
-  __DATA._rtk_patchbay: 0x2fa
+  __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x5f8
   __DATA.__version: 0x8
   __DATA._spu_service: 0x120

   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0x99960
-  __ETEXT.__text: 0x66fc
+  __ETEXT.__text: 0x66f8
   __ETEXT.__StaticInit: 0xf0c
   __ETEXT.__const: 0x135
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x29b22
+  __OS_LOG.__string: 0x29b54
   __MISC.__apf_list: 0x30
-  Functions: 2146
+  Functions: 2147
   Symbols:   0
-  CStrings:  2558
+  CStrings:  2559
 
CStrings:
+ "15:35:12"
+ "15:39:41"
+ "AppleSPUFirmware-2444.1.1~66"
+ "Aug  8 2026"
+ "SCM Error: Reconfiguring channel=%u"
+ "[AUD] aop-audprovr2 v600.21 built %s %s, %s state"
+ "[AUD] exp \"AppleAOPAudioFirmware::System::getWorkLoop( AppleAOPAudioFirmware::Platform::RunLoopType::kAudio, workLoop)\" fail, %s(), ln 135, stat %#x"
+ "[AUD] exp \"AppleAOPAudioFirmware::System::getWorkLoop( AppleAOPAudioFirmware::Platform::RunLoopType::kAudio, workLoop)\" fail, %s(), ln 91, stat %#x"
+ "[AUD] exp \"RTKitAudioPlatform::initPlatform(&sRtkadIntrWorkLoop)\" fail, %s(), ln 97, stat %#x"
+ "[AUD] exp \"_transferData(transferReq)\" fail, %s(), ln 793, stat %#x"
+ "[AUD] exp \"initInterfaceMap(*outInterfaces)\" fail, %s(), ln 194, stat %#x"
+ "[AUD] exp \"initInterfaceMap(sInterfaceMap)\" fail, %s(), ln 202, stat %#x"
+ "[AUD] exp \"initRTKitAudioPlatform()\" fail, %s(), ln 190, stat %#x"
+ "[AUD] exp \"mAudioPacketRingBufferWriter.init()\" fail, %s(), ln 235, stat %#x"
+ "[AUD] exp \"ret\" fail, %s(), ln 816, stat %#x"
+ "[AUD] exp \"sEventQueueInterface.init(*workLoop)\" fail, %s(), ln 137, stat %#x"
+ "[AUD] exp \"sSecureEventQueueInterface.init(*workLoop)\" fail, %s(), ln 97, stat %#x"
+ "[AUD] exp \"super::_performStateChange(inClientMgrId, inChg, outPending)\" fail, %s(), ln 478, stat %#x"
+ "[AUD] exp \"super::ready()\" fail, %s(), ln 233, stat %#x"
+ "[AUD] expression \"mPDMC.writeReg<uint32_t>( PDMC_BLK_RXFIFOCFG_OFFSET, (PDMC_BLK_RXFIFOCFG_LOW_WATER_INSRT(_getLowWatermark(*config)) | PDMC_BLK_RXFIFOCFG_HIGH_WATER_INSRT(_getHighWatermark(*config))))\" failed, %s(), line %d, status: 0x%x"
+ "[AUD] fail, stat %#x, %s(), ln 240"
+ "[AUD] ptr \"workLoop\" is null, cant cont, %s(), ln 136, stat %#x"
+ "[AUD] ptr \"workLoop\" is null, cant cont, %s(), ln 92, stat %#x"
- "00:00:09"
- "00:05:40"
- "AppleSPUFirmware-2444.0.12~90"
- "Jul 10 2026"
- "[AUD] aop-audprovr2 v600.20 built %s %s, %s state"
- "[AUD] exp \"AppleAOPAudioFirmware::System::getWorkLoop( AppleAOPAudioFirmware::Platform::RunLoopType::kAudio, workLoop)\" fail, %s(), ln 130, stat %#x"
- "[AUD] exp \"AppleAOPAudioFirmware::System::getWorkLoop( AppleAOPAudioFirmware::Platform::RunLoopType::kAudio, workLoop)\" fail, %s(), ln 88, stat %#x"
- "[AUD] exp \"RTKitAudioPlatform::initPlatform(&sRtkadIntrWorkLoop)\" fail, %s(), ln 92, stat %#x"
- "[AUD] exp \"_transferData(transferReq)\" fail, %s(), ln 788, stat %#x"
- "[AUD] exp \"initInterfaceMap(*outInterfaces)\" fail, %s(), ln 189, stat %#x"
- "[AUD] exp \"initInterfaceMap(sInterfaceMap)\" fail, %s(), ln 197, stat %#x"
- "[AUD] exp \"initRTKitAudioPlatform()\" fail, %s(), ln 185, stat %#x"
- "[AUD] exp \"mAudioPacketRingBufferWriter.init()\" fail, %s(), ln 107, stat %#x"
- "[AUD] exp \"ret\" fail, %s(), ln 811, stat %#x"
- "[AUD] exp \"sEventQueueInterface.init(*workLoop)\" fail, %s(), ln 132, stat %#x"
- "[AUD] exp \"sSecureEventQueueInterface.init(*workLoop)\" fail, %s(), ln 94, stat %#x"
- "[AUD] exp \"super::_performStateChange(inClientMgrId, inChg, outPending)\" fail, %s(), ln 217, stat %#x"
- "[AUD] exp \"super::ready()\" fail, %s(), ln 105, stat %#x"
- "[AUD] expression \"mPDMC.writeReg<uint32_t>(PDMC_BLK_RXFIFOCFG_OFFSET, (PDMC_BLK_RXFIFOCFG_LOW_WATER_INSRT(config->burstSize) | PDMC_BLK_RXFIFOCFG_HIGH_WATER_INSRT(config->burstSize - 1)))\" failed, %s(), line %d, status: 0x%x"
- "[AUD] fail, stat %#x, %s(), ln 112"
- "[AUD] ptr \"workLoop\" is null, cant cont, %s(), ln 131, stat %#x"
- "[AUD] ptr \"workLoop\" is null, cant cont, %s(), ln 89, stat %#x"
```
