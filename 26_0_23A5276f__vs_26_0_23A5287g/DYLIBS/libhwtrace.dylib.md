## libhwtrace.dylib

> `/usr/lib/libhwtrace.dylib`

```diff

-133.0.14.0.0
-  __TEXT.__text: 0x21accc
+133.0.18.0.0
+  __TEXT.__text: 0x21b1f0
   __TEXT.__auth_stubs: 0x1690
-  __TEXT.__const: 0x1ae020
-  __TEXT.__cstring: 0x1995c
-  __TEXT.__oslogstring: 0x6b0
+  __TEXT.__const: 0x1ae010
+  __TEXT.__cstring: 0x19c6f
+  __TEXT.__oslogstring: 0x6a5
   __TEXT.__gcc_except_tab: 0x290
   __TEXT.__unwind_info: 0x2b90
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_methname: 0xa9
   __TEXT.__objc_stubs: 0x120
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x48af8
+  __DATA_CONST.__const: 0x48b10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
   __AUTH_CONST.__auth_got: 0xb58

   - /usr/lib/libncurses.5.4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BB646619-7580-361C-A417-FC09227ADC3B
+  UUID: AEC5EC23-7172-3CEB-8F76-C7230592432F
   Functions: 4324
   Symbols:   573
-  CStrings:  5701
+  CStrings:  5704
 
Functions:
~ sub_29a365b64 -> sub_29a9f3b64 : 1276 -> 1312
~ sub_29a375140 -> sub_29aa03164 : 736 -> 744
~ sub_29a3997f4 -> sub_29aa27820 : 136 -> 188
~ sub_29a3c3210 -> sub_29aa51270 : 816 -> 848
~ sub_29a3f3404 -> sub_29aa81484 : 2560 -> 2896
~ sub_29a4029a0 -> sub_29aa90b70 : 5420 -> 5700
~ sub_29a40fa0c -> sub_29aa9dcf4 : 4016 -> 4172
~ sub_29a4109bc -> sub_29aa9ed40 : 1244 -> 1252
~ sub_29a41620c -> sub_29aaa4598 : 1540 -> 1648
~ sub_29a42c490 -> sub_29aaba888 : 13996 -> 14296
CStrings:
+ "\n         +--------------------------------------------------------------------+\n         | Support for PIO-based configuration of cputrace on XNU is          |\n         | deprecated in favor of a safer, more performant, and feature-rich  |\n         | replacement through a driver. PIO support will be removed in an    |\n         | upcoming SU: pass -driver=1 or --CPUTrace:driver=1 to migrate now. |\n         | Reach out on Slack to share feedback or ask questions. See:        |\n         | 'at' dot 'apple.com/ariadne-cputrace' for migration help, some     |\n         | required bootargs have changed and SIP no longer must be disabled. |\n         +--------------------------------------------------------------------+\n    "
+ "MP"
+ "initKernelspaceImagesACC"
+ "kern.static_if_abi sysctl failed"
+ "libhwtrace @ tag libhwtrace-133.0.18"
+ "libhwtrace @ tag libhwtrace-133.0.18\n"
- "libhwtrace @ tag libhwtrace-133.0.14"
- "libhwtrace @ tag libhwtrace-133.0.14\n"
- "{public}%s"

```
