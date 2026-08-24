## aopfw-mac16gaop_l4.RELEASE.im4p

> `Firmware/AOP/aopfw-mac16gaop_l4.RELEASE.im4p`

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

-  __TEXT.__text: 0xb30bc
-  __TEXT.__const: 0xa820
-  __TEXT.__cstring: 0x79bc
+  __TEXT.__text: 0xb3cec
+  __TEXT.__const: 0xa878
+  __TEXT.__cstring: 0x7a38
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x2c
   __DATA._rtk_boot: 0x3000

   __DATA._rtk_exc_stack: 0x1000
   __DATA._rtk_ext_stack: 0x1800
   __DATA._rtk_heap: 0x14220
-  __DATA.__const: 0xefa8
+  __DATA.__const: 0xef90
   __DATA.__data: 0x72c8
-  __DATA._rtk_patchbay: 0x2fa
+  __DATA._rtk_patchbay: 0x306
   __DATA._rtk_mtab: 0x5e0
   __DATA.__version: 0x8
   __DATA._spu_service: 0x390

   __DATA._rtk_threads: 0x0
   __DATA._spu_exts: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xab078
-  __ETEXT.__text: 0x133ac
+  __DATA.__zerofill: 0xab518
+  __ETEXT.__text: 0x13470
   __ETEXT.__StaticInit: 0x2110
-  __ETEXT.__const: 0x570
+  __ETEXT.__const: 0x580
   __EDATA.__data: 0x1cc0
   __EDATA.__const: 0x0
-  __OS_LOG.__string: 0x2937a
+  __OS_LOG.__string: 0x29442
   __MISC.__apf_list: 0x30
-  __CMA.__cma_log_string: 0x123f
-  Functions: 2793
+  __CMA.__cma_log_string: 0x1259
+  Functions: 2777
   Symbols:   0
-  CStrings:  2939
+  CStrings:  2943
 
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
+ "[AUD] expression \"mPDMC.writeReg<uint32_t>( PDMC_BLK_RXFIFOCFG_OFFSET, (PDMC_BLK_RXFIFOCFG_LOW_WATER_INSRT(_getLowWatermark(*config)) | PDMC_BLK_RXFIFOCFG_HIGH_WATER_INSRT(_getHighWatermark(*config))))\" failed, %s(), line %d, status: 0x%x"
- "00:05:46"
- "00:05:47"
- "23:59:37"
- "AppleSPUFirmware-2444.0.12~90"
- "Jul  9 2026"
- "Jul 10 2026"
- "[AUD] aop-audprovr3 v600.20 built %s %s"
- "[AUD] aop-audprovr3 v600.20 built %s %s, %s state"
- "[AUD] expression \"mPDMC.writeReg<uint32_t>(PDMC_BLK_RXFIFOCFG_OFFSET, (PDMC_BLK_RXFIFOCFG_LOW_WATER_INSRT(config->burstSize) | PDMC_BLK_RXFIFOCFG_HIGH_WATER_INSRT(config->burstSize - 1)))\" failed, %s(), line %d, status: 0x%x"
```
