## rans.t603x_ASP3.release.im4p

> `rans.t603x_ASP3.release.im4p`

```diff

 
   __TEXT.text_first: 0x4488
-  __TEXT.__text: 0x1e50e0
-  __TEXT.shared: 0xe784
-  __TEXT.read: 0x72dc
-  __TEXT.__const: 0x6548
+  __TEXT.__text: 0x1e7600
+  __TEXT.shared: 0xeb2c
+  __TEXT.read: 0x75ec
+  __TEXT.__const: 0x65b8
   __TEXT.idle_hooks: 0x10
-  __TEXT.__cstring: 0x242b4
+  __TEXT.__cstring: 0x245af
   __TEXT.__chain_starts: 0x0
   __TEXT.__constructor: 0x0
   __TEXT._rtk_mtab: 0x540

   __DATA._rtk_power: 0x160
   __DATA._rtk_patchbay: 0x3ff
   __DATA._rtk_tunables: 0x5b0
-  __DATA.__const: 0x3900
+  __DATA.__const: 0x3910
   __DATA.__data: 0x8800
   __DATA._rtk_init_stack: 0x1000
   __DATA._rtk_irq_stack: 0x1000

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__mod_init_func: 0x0
-  __DATA.core_globals: 0x15c
+  __DATA.core_globals: 0x15d
   __DATA.large_stacks: 0x20000
   __DATA.small_stacks: 0x2000
-  __DATA.__zerofill: 0x5a0918
+  __DATA.__zerofill: 0x5a0a88
   Functions: 0
   Symbols:   0
-  CStrings:  4004
+  CStrings:  4009
 
CStrings:
+ " BandsTemp_getDeviceTemperatureAll -> %ums"
+ "2077.120.68.0.1"
+ "77.120.68.0.1~82"
+ "AppleStorageFirmware-2077.120.68.0.1~82"
+ "FADUMP: Dumping FA to memory..."
+ "FADUMP: ERROR! Couldn't assert asi device %d"
+ "FADUMP: ERROR! FA dump is disabled"
+ "FADUMP: ERROR! FA dump is not supported"
+ "FADUMP: ERROR! FA dump was already executed"
+ "FADUMP: ERROR! FAdump Init failed!"
+ "FADUMP: ERROR! Memory address is not 0x%x aligned!"
+ "FADUMP: ERROR! Memory size is not 0x%x aligned!"
+ "FADUMP: ERROR! Nand Discovery not completed"
+ "FADUMP: ERROR! No memory!"
+ "FADUMP: ERROR! No space in Util panic log for MSP FA"
+ "FADUMP: ERROR! RTK_mc_assume failed: %d"
+ "FADUMP: Error: failed to check if device %d is asserted"
+ "FADUMP: FA stored 0x%x"
+ "FADUMP: FA_AllocationSize: %d"
+ "FADUMP: FA_Init isEnabled: %d, Size: %d"
+ "FADUMP: Finalizing FA dump: magic 0x%x, crc 0x%x"
+ "FADUMP: Forcing assert on asi device %d"
+ "FADUMP: Found Prev Assert[%d][%d,%d,%d]"
+ "FADUMP: MSP FA size: %d"
+ "FADUMP: Possible data incoherency"
+ "FADUMP: WARNING! Compression buffer allocation failed."
+ "FADUMP: WARNING! Couldn't get fa size for asi device %d"
+ "FADUMP: WARNING! FA Mem Release failed. status: 0x%x"
+ "FADUMP: WARNING! Failed to compress MSP %d"
+ "FADUMP: WARNING! Failed to store ASI logger"
+ "FADUMP: WARNING! Failed to store FTL entry %d"
+ "FADUMP: WARNING! No space left to store MSP %d"
+ "FADUMP: WARNING! Not extracting asi logger. size %d, addr 0x%x"
+ "FADUMP: WARNING! failed to read FA data for asi device %d"
+ "FADUMP: comressed req:%d, SizeAvg %d"
+ "FADUMP: deflate failed. status %d, Sec left to store: %d"
+ "FADUMP: deflateEnd failed. status %d"
+ "FADUMP: deflateInit2 failed. status %d"
+ "MassScan: Pilot scan done on %d bands after %lld seconds, but can't exit early, because %d bands failed, need to continue to full scan"
+ "Set DC table ver %u by %s"
+ "Setting thermal self throttling temp thresholds. En: %u, lowest lev: %u, Max: %d, High: %d, Low: %d"
+ "Such status is not allowed for block scan read command"
+ "Tried to read feature bit %d but feature bits struct is not initialized"
+ "cross temp detected, band %u temp (%d,%d) read temp (%d,%d), opType %d, isNew %u"
+ "cross temp isQualityError, band %u, opType %u"
+ "cross temp thershold not set yet"
+ "e=0x%x"
+ "forced temperature: %d, core temp %d, enable %u, reset stats %u"
+ "smc_drv_send_query_response_ans_nand_temperature got a bad msp_id, sending error to smc"
+ "temperature average exceeded max allowed %u - %u, %u"
+ "wrong high threshold crossed %u %d %d"
+ "wrong low threshold crossed %u %d %d"
- " PreNandEng_getDeviceTemperature -> %ums"
- ".100.377.0.1~113"
- "2077.100.377.0.1"
- "AppleStorageFirmware-2077.100.377.0.1~113"
- "CTL cross temp detected on flow %d, lba %d opType %d, size %d shouldCount %d"
- "Dumping FA to memory..."
- "ERROR! Couldn't assert asi device %d"
- "ERROR! FA dump is disabled"
- "ERROR! FA dump is not supported"
- "ERROR! FA dump was already executed"
- "ERROR! FAdump Init failed!"
- "ERROR! Memory address is not 0x%x aligned!"
- "ERROR! Memory size is not 0x%x aligned!"
- "ERROR! Nand Discovery not completed"
- "ERROR! No memory!"
- "ERROR! No space in Util panic log for MSP FA"
- "ERROR! RTK_mc_assume failed: %d"
- "Error: failed to check if device %d is asserted"
- "FA stored 0x%x"
- "FA_AllocationSize: %d"
- "FA_Init isEnabled: %d, Size: %d"
- "Finalizing FA dump: magic 0x%x, crc 0x%x"
- "Forcing assert on asi device %d"
- "Found Prev Assert[%d][%d,%d,%d]"
- "MSP FA size: %d"
- "Possible data incoherency"
- "Set thermal throttling costs table ver %u by %s"
- "WARNING! Compression buffer allocation failed."
- "WARNING! Couldn't get fa size for asi device %d"
- "WARNING! FA Mem Release failed. status: 0x%x"
- "WARNING! Failed to compress MSP %d"
- "WARNING! Failed to store ASI logger"
- "WARNING! Failed to store FTL entry %d"
- "WARNING! No space left to store MSP %d"
- "WARNING! Not extracting asi logger. size %d, addr 0x%x"
- "WARNING! failed to read FA data for asi device %d"
- "WARNING: thermal self throttling is not supported"
- "comressed req:%d, SizeAvg %d"
- "deflate failed. status %d, Sec left to store: %d"
- "deflateEnd failed. status %d"
- "deflateInit2 failed. status %d"
- "done scan ET bands %u"
- "forced device temperature is: %d"
- "forced tunnel temperature is: %d"
- "must be blocking"
- "must be valid temperatute at this point"
- "reset temprature stats"

```
