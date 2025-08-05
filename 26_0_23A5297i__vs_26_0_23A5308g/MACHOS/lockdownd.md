## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1350.0.0.0.0
-  __TEXT.__text: 0x9caf8
+1350.0.1.0.0
+  __TEXT.__text: 0x97dcc
   __TEXT.__auth_stubs: 0x1d40
   __TEXT.__objc_stubs: 0x1360
   __TEXT.__objc_methlist: 0xe8
-  __TEXT.__cstring: 0x39d98
-  __TEXT.__const: 0x10e80
+  __TEXT.__cstring: 0x39f6d
+  __TEXT.__const: 0x10e90
   __TEXT.__oslogstring: 0x1e6
-  __TEXT.__gcc_except_tab: 0x9b4
+  __TEXT.__gcc_except_tab: 0x9c8
   __TEXT.__objc_classname: 0x27
   __TEXT.__objc_methname: 0xd61
   __TEXT.__objc_methtype: 0x120
   __TEXT.__services: 0x2d8e
   __TEXT.__unwind_info: 0xb78
-  __TEXT.__eh_frame: 0xb8
+  __TEXT.__eh_frame: 0x80
   __DATA_CONST.__auth_got: 0xeb0
   __DATA_CONST.__got: 0x3e8
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x7cb8
-  __DATA_CONST.__cfstring: 0xd9c0
+  __DATA_CONST.__const: 0x7da8
+  __DATA_CONST.__cfstring: 0xda00
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_data: 0x50
   __DATA.__data: 0x1e78
   __DATA.__bss: 0x200
-  __DATA.__common: 0xa28
+  __DATA.__common: 0xa30
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libramrod.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4207355E-6A6E-3DB3-B04D-8E7DCE65392D
-  Functions: 861
+  UUID: 5B441120-98F4-3E04-BC1B-3BFCB5641DA5
+  Functions: 863
   Symbols:   616
-  CStrings:  7235
+  CStrings:  7247
 
CStrings:
+ "ASPFTLParseBufferToCxt: nandReadsByMode(1463): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: nandReadsByMode(1463): Cannot add 6 elements to context"
+ "ASPFTLParseBufferToCxt: nandWritesByMode(1462): (#6) cfg elements != (%d) buffer elements"
+ "ASPFTLParseBufferToCxt: nandWritesByMode(1462): Cannot add 6 elements to context"
+ "Peer is unsafe (generic failure)."
+ "Peer is unsafe (non kernel peer, pid %d)"
+ "Peer is unsafe (usbmux is not connected to host)."
+ "boot_rd_sdl_overflow"
+ "boot_wr_sdl_overflow"
+ "coge_cache_hit_program"
+ "coge_cache_hit_read"
+ "coge_cache_miss_program"
+ "coge_cache_miss_read"
+ "coge_lru_num_of_replacement"
+ "coge_lru_num_of_searches"
+ "dspExceptionParameter152"
+ "dspExceptionParameter153"
+ "dspExceptionParameter154"
+ "dspExceptionParameter155"
+ "dspExceptionParameter156"
+ "dspExceptionParameter157"
+ "dspExceptionParameter169"
+ "msp_number_hw_sram_flips"
+ "nandReadsByMode"
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
+ "nandWritesByMode"
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
+ "too_frequent_temp_change_rd"
+ "too_frequent_temp_change_wr"
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
- "non kernel peer, pid %d!\n"
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

```
