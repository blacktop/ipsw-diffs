## sysdiagnose_helper

> `/usr/libexec/sysdiagnose_helper`

```diff

-1527.0.2.0.0
-  __TEXT.__text: 0x39268
+1527.0.4.0.0
+  __TEXT.__text: 0x395bc
   __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_stubs: 0x1560
-  __TEXT.__objc_methlist: 0x564
+  __TEXT.__objc_stubs: 0x1600
+  __TEXT.__objc_methlist: 0x57c
   __TEXT.__const: 0x3f8
-  __TEXT.__gcc_except_tab: 0x848
-  __TEXT.__oslogstring: 0x222b
-  __TEXT.__cstring: 0x2efe5
+  __TEXT.__gcc_except_tab: 0x7f4
+  __TEXT.__oslogstring: 0x228e
+  __TEXT.__cstring: 0x2f18a
   __TEXT.__objc_classname: 0xc4
   __TEXT.__objc_methtype: 0x29b
-  __TEXT.__objc_methname: 0x1558
-  __TEXT.__unwind_info: 0x558
+  __TEXT.__objc_methname: 0x15c1
+  __TEXT.__unwind_info: 0x568
   __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x1b40
+  __DATA_CONST.__const: 0x660
+  __DATA_CONST.__cfstring: 0x1b60
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x78
   __DATA_CONST.__objc_intobj: 0x60
   __DATA.__objc_const: 0x6d8
-  __DATA.__objc_selrefs: 0x5c8
+  __DATA.__objc_selrefs: 0x5f0
   __DATA.__objc_ivar: 0x38
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x4b8

   - /System/Library/PrivateFrameworks/GenerativeExperiences.framework/GenerativeExperiences
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/NetworkRelay.framework/NetworkRelay

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libtzupdate.dylib
-  UUID: B12161A9-9B4F-32B4-84DD-26A8881C9758
-  Functions: 333
-  Symbols:   256
-  CStrings:  4307
+  UUID: 22DD16FF-F37B-3F0E-BE9E-E49AB717E3B2
+  Functions: 338
+  Symbols:   257
+  CStrings:  4323
 
Symbols:
+ _OBJC_CLASS_$_MCProfileConnection
CStrings:
+ "ASPFTLParseBufferToCxt: nandReadsByMode(1463): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: nandReadsByMode(1463): Cannot add 6 elements to context"
+ "ASPFTLParseBufferToCxt: nandWritesByMode(1462): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: nandWritesByMode(1462): Cannot add 6 elements to context"
+ "BT profile SPI not found, assuming not installed"
+ "BT profile SPI returned nil array, assuming not installed"
+ "Error querying W5Client: %@, assuming profile not installed"
+ "Found profile status of wifi: %d, bt: %d"
+ "Profile checks timed out, assuming not installed"
+ "W5Client SPI not found, assuming profile not installed"
+ "W5Client client nil, assuming profile not installed"
+ "bluetooth.logging"
+ "boot_rd_sdl_overflow"
+ "boot_wr_sdl_overflow"
+ "coge_cache_hit_program"
+ "coge_cache_hit_read"
+ "coge_cache_miss_program"
+ "coge_cache_miss_read"
+ "coge_lru_num_of_replacement"
+ "coge_lru_num_of_searches"
+ "containsString:"
+ "coreCaptureConfigBTProfileCheck"
+ "coreCaptureConfigWifiProfileCheck"
+ "dspExceptionParameter152"
+ "dspExceptionParameter153"
+ "dspExceptionParameter154"
+ "dspExceptionParameter155"
+ "dspExceptionParameter156"
+ "dspExceptionParameter157"
+ "dspExceptionParameter169"
+ "installedProfileIdentifiers"
+ "isBTProfileInstalled"
+ "isWifiProfileInstalled"
+ "msp_number_hw_sram_flips"
+ "nandReadsByMode_"
+ "nandStageOfLife105"
+ "nandStageOfLife106"
+ "nandStageOfLife111"
+ "nandStageOfLife112"
+ "nandStageOfLife113"
+ "nandStageOfLife114"
+ "nandStageOfLife115"
+ "nandStageOfLife116"
+ "nandStageOfLife117"
+ "nandStageOfLife118"
+ "nandStageOfLife119"
+ "nandWritesByMode_"
+ "periodic_rd_sdl_overflow"
+ "periodic_rd_training_failure"
+ "periodic_wr_sdl_overflow"
+ "periodic_wr_training_failure"
+ "pge_rd_sdl_overflow"
+ "pge_rd_training_failure"
+ "pge_wr_sdl_overflow"
+ "pge_wr_training_failure"
+ "readStage111"
+ "sharedConnection"
+ "throttlingSecPerTTPerMW"
+ "too_frequent_temp_change_rd"
+ "too_frequent_temp_change_wr"
- "CoreCaptureConfig task timed out"
- "Error querying Wifi Velocity configuration for peer due to %@. Assuming WiFiVelocity MegaProfile is not enabled"
- "W5Client is nil"
- "WiFi Velocity SPI not found"
- "WiFiVelocity MegaProfile is enabled"
- "WiFiVelocity MegaProfile is not enabled"
- "boot_rd_sdl_overflow_"
- "boot_wr_sdl_overflow_"
- "coge_cache_hit_program_"
- "coge_cache_hit_read_"
- "coge_cache_miss_program_"
- "coge_cache_miss_read_"
- "coge_lru_num_of_replacement_"
- "coge_lru_num_of_searches_"
- "dspExceptionParameter152_"
- "dspExceptionParameter153_"
- "dspExceptionParameter154_"
- "dspExceptionParameter155_"
- "dspExceptionParameter156_"
- "dspExceptionParameter157_"
- "dspExceptionParameter169_"
- "msp_number_hw_sram_flips_"
- "nandStageOfLife105_"
- "nandStageOfLife106_"
- "nandStageOfLife111_"
- "nandStageOfLife112_"
- "nandStageOfLife113_"
- "nandStageOfLife114_"
- "nandStageOfLife115_"
- "nandStageOfLife116_"
- "nandStageOfLife117_"
- "nandStageOfLife118_"
- "nandStageOfLife119_"
- "periodic_rd_sdl_overflow_"
- "periodic_rd_training_failure_"
- "periodic_wr_sdl_overflow_"
- "periodic_wr_training_failure_"
- "pge_rd_sdl_overflow_"
- "pge_rd_training_failure_"
- "pge_wr_sdl_overflow_"
- "pge_wr_training_failure_"
- "readStage111_"
- "too_frequent_temp_change_rd_"
- "too_frequent_temp_change_wr_"
- "wiFiVelocityMegaProfile"

```
