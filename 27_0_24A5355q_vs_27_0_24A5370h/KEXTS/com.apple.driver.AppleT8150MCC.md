## com.apple.driver.AppleT8150MCC

> `com.apple.driver.AppleT8150MCC`

```diff

-120.0.0.0.0
+125.0.0.0.0
   __TEXT.__const: 0x50 sha256:d286682f23a67ee50eff5899c281dd20cd1cdf36757f3e052cd40ea84e0d7840
-  __TEXT.__cstring: 0x5833 sha256:aa9f926ea85d755a3f9822b368e68e02b0e29e9b2b7766e0ca0bfbf928678aa8
-  __TEXT.__os_log: 0x244a sha256:600c53f3efab43f4e4efe945b56e21c528a20cfbb2d194b788ff482e3481cb69
-  __TEXT_EXEC.__text: 0x15bd0 sha256:b8fb456932f0e59794e943695d588c32a6eb632a3cb39d154996c7d7cd12ccb2
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x9130 sha256:d50536b0a545a1177bd5135a66c6c25ed0c30f25fc738732f22c8e8d223eb4c9
+  __TEXT.__cstring: 0x5ba7 sha256:80d1c4e3ac75c7eeb696fee7a3d12258f834c742d07cac454a368108eca28779
+  __TEXT.__os_log: 0x2701 sha256:024f420c9a7e816cc402d88823c89b0b3731991d5db2b333323f6e430b8b3069
+  __TEXT_EXEC.__text: 0x169b4 sha256:2b1984c50de09da03fe41382430d03f51fc88466bcc7601e150e56257247505e
+  __TEXT_EXEC.__auth_stubs: 0x5b0 sha256:15b7d502183b4ba3158139049c5c493422bed4f53fa36e4ee91e367f1aed169e
+  __DATA.__data: 0x9130 sha256:1407ce76ed0cc528497aee077bb01c14c680f9dde0dbc16706120b7751b7e9d9
   __DATA.__common: 0x1f0 sha256:882993b55cc0c527f0a6059b69b3faf4ef3ccb9cecd3d8847ca0e49a1444debe
   __DATA.__bss: 0x54 sha256:4fea5e6a3ec5f5474a26d858bc77b6d7bd3ab864ea02d988683fdc648602b248
-  __DATA_CONST.__mod_init_func: 0x20 sha256:d3a6f652b6f61a227472afb943e6b27d3da4ef5f5bfcb1fda78f596e4ce786fc
-  __DATA_CONST.__mod_term_func: 0x20 sha256:82bcb7d40df7d9b3ce8c2d4ce81241ef5c4eff0fe4fc63da8904eed9b1b425b4
-  __DATA_CONST.__const: 0x3370 sha256:5677ddee64c66c393b4f9de331e598be8b88e4ca909598d06de7ba5aa3cfff9c
-  __DATA_CONST.__kalloc_type: 0x440 sha256:6066fc27bbea0fbb14f3bd7f05e11d4e645600eca36794c1f66cfdcef6d332f4
-  __DATA_CONST.__kalloc_var: 0x140 sha256:14d0bc6c64eba5ac6ab80eda108cec86b49df24f572f681fcb02fd8da914c1fd
-  __DATA_CONST.__auth_got: 0x2d8 sha256:043f34c3f5dbbea5a03acca1cc35d3e82d348be327ba997967488490328d9f93
-  __DATA_CONST.__got: 0xc0 sha256:4d1cc04eab6d4a6bc3da864e3185775df14f1fbd18931b091dd82c85a0a5edf5
-  UUID: C04C3CAD-8782-39E7-800A-69B98859101B
-  Functions: 562
+  __DATA_CONST.__mod_init_func: 0x20 sha256:f598ec2512fd70c34622bb01c763e115032b43eeef582d37c3100873c17136e3
+  __DATA_CONST.__mod_term_func: 0x20 sha256:baad7a843d93185ed7d813118a8b6203db4cd5311be770a98deb18666a868bd2
+  __DATA_CONST.__const: 0x33c0 sha256:399025c1aca984a1870cb3381ee270f17f62485350440ed01a4f0a261a9cfc14
+  __DATA_CONST.__kalloc_type: 0x440 sha256:ed4537b00dab6ca61d84a0cd3a2875d6c92e5d8c1cf2de26f49a445fa9f21adc
+  __DATA_CONST.__kalloc_var: 0x140 sha256:796794515df9187922fce67b31202f1547201a655cc6105bbfe9f6c06859c5ad
+  __DATA_CONST.__auth_got: 0x2d8 sha256:a704a1ddbc5e46d79af727147ffdffff5bc2a1689571157b8fe0602a7f81289d
+  __DATA_CONST.__got: 0xc0 sha256:8c68ea715141edcfee624d6545eff028ee30216586e080397ba3926aa26246ec
+  UUID: 8C0D5A5F-E2A5-3890-BF14-344405F138D0
+  Functions: 570
   Symbols:   0
-  CStrings:  903
+  CStrings:  934
 
CStrings:
+ "\"%s has not been implemented by platform\" @%s:%d"
+ "\"%s has not been implemented by platform.\" @%s:%d"
+ "\"%s: \" \"Failed to map memory aperture %u\" @%s:%d"
+ "%s: EDT blob too small (%u bytes, need %zu)"
+ "%s:%d: %s: EDT blob too small (%u bytes, need %zu)\n"
+ "%s:%d: DRAMECC: Invalid register table for memory hashing\n\n"
+ "%s:%d: DRAMECC: Starting init mem hash param\n\n"
+ "%s:%d: DRAMECC: bank-drop-mask0 is missing in mcc node in EDT\n\n"
+ "%s:%d: DRAMECC: bank-drop-mask1 is missing in mcc node in EDT\n\n"
+ "%s:%d: DRAMECC: bank-group-drop-mask0 is missing in mcc node in EDT\n\n"
+ "%s:%d: DRAMECC: bank-group-drop-mask1 is missing in mcc node in EDT\n\n"
+ "%s:%d: DRAMECC: rank-drop-mask0 is missing in mcc node in EDT\n\n"
+ "%s:%d: DRAMECC: row-drop-mask is missing in mcc node in EDT\n\n"
+ "%s:%d: _dcsNumChannels = %d _dcsEnableMask = 0x%llx\n"
+ "%s:%d: dcs-channel-enable-mask is not set in EDT. Setting dcs channel mask to 0x%llx\n"
+ "%s:%d: dcs-channel-enable-mask: 0x%llx\n\n"
+ "%s:%d: regIdx = %d _apertureNum = %d _apertureEnableMask = 0x%llx\n"
+ "12111112122212121111111111111111111111111111112111111111111111111111111111111111111111111111111111111111111111111111111111211111112121111121"
+ "121111121222121211111111111111111111111111111121111111111111111111111111111111111111111111111111111111111111111111111111112111111121211111212221122222222222211111112111121211121212121212"
+ "DRAMECC: Invalid register table for memory hashing\n"
+ "DRAMECC: Starting init mem hash param\n"
+ "DRAMECC: bank-drop-mask0 is missing in mcc node in EDT\n"
+ "DRAMECC: bank-drop-mask1 is missing in mcc node in EDT\n"
+ "DRAMECC: bank-group-drop-mask0 is missing in mcc node in EDT\n"
+ "DRAMECC: bank-group-drop-mask1 is missing in mcc node in EDT\n"
+ "DRAMECC: rank-drop-mask0 is missing in mcc node in EDT\n"
+ "DRAMECC: row-drop-mask is missing in mcc node in EDT\n"
+ "_dcsNumChannels = %d _dcsEnableMask = 0x%llx"
+ "_initMemHashParam"
+ "bank-drop-mask0"
+ "bank-drop-mask1"
+ "bank-group-drop-mask0"
+ "bank-group-drop-mask1"
+ "dcs-channel-enable-mask is not set in EDT. Setting dcs channel mask to 0x%llx"
+ "dcs-channel-enable-mask: 0x%llx\n"
+ "getAmccInstanceLp6"
+ "getDcsInstanceFromHashBitVal"
+ "getDcsScFromHashBitVal"
+ "getMCCProperty"
+ "rank-drop-mask0"
+ "regIdx = %d _apertureNum = %d _apertureEnableMask = 0x%llx"
+ "row-drop-mask"
- "\"%s: \" \"Failed to map amcc aperture %u\" @%s:%d"
- "%s:%d: _dcsNumChannels = %d _dcsEnableMask = 0x%x\n"
- "%s:%d: dcs-channel-enable-mask is not set in EDT. Setting dcs channel mask to 0x%x\n"
- "%s:%d: dcs-channel-enable-mask: 0x%x\n\n"
- "%s:%d: regIdx = %d _apertureNum = %d _apertureEnableMask = 0x%x\n"
- "1211111212221212111111111111111111111111112111111111111111111111111111111111111111111111111111111111111111111111111111211111112121111121"
- "1211111212221212111111111111111111111111112111111111111111111111111111111111111111111111111111111111111111111111111111211111112121111121112222222222211111112111121211121212121212"
- "_dcsNumChannels = %d _dcsEnableMask = 0x%x"
- "dcs-channel-enable-mask is not set in EDT. Setting dcs channel mask to 0x%x"
- "dcs-channel-enable-mask: 0x%x\n"
- "regIdx = %d _apertureNum = %d _apertureEnableMask = 0x%x"

```
