## libsystem_c.dylib

> `/usr/lib/system/libsystem_c.dylib`

```diff

-1782.0.0.0.0
-  __TEXT.__text: 0x7ade0 sha256:3b2f4c59b66563dec554f4067ef0271c54333920fdb5ced0ea025ea5ada3502d
-  __TEXT.__const: 0x28a8 sha256:5c3d4835d294b0678d6b50d5c1df473991754db0173eb68f2c53ec0c922e22d1
-  __TEXT.__cstring: 0x311a sha256:07cfdd40cdcdf8ce15817306e01466216a0ddfa2ee3ffef65cc7d787a48a2142
+1786.0.0.0.0
+  __TEXT.__text: 0x7b52c sha256:32d0fdd92dcf6590ae1a84ab5b3747c1ab41c8ef505aa1819468625db2c2418b
+  __TEXT.__const: 0x2978 sha256:b826d45557a63a7067a9ed638512d71455a9611322edc01617003183b9218e98
+  __TEXT.__cstring: 0x3127 sha256:60b607e334c9fb1adc4192770db87b30bd5783025dc845dfb8151215ea735905
   __TEXT.__oslogstring: 0x5c sha256:e92abd2425eea19ceb9753e5a03c845a003307f9d96eabe6c26d5f8226f52910
-  __TEXT.__unwind_info: 0x1448 sha256:d025f2d6a97af5c6f6b55afd0c4d6e75f9732889c769a0f3f29245f0595781c8
+  __TEXT.__unwind_info: 0x1458 sha256:c0127bc1d7fa5a119b305ccb415864b0d65b3155786ecf65638594ed276e2c03
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x1838 sha256:5a6d5b4b99300c533e8d4ff8494c3bee0d0b48c80089e06f42ab45576cc031a6
-  __DATA_CONST.__weak_got: 0x8 sha256:999948e3fdc5664f16c5e6b160669e7a5cc7c81ea05a81b6862549ff16e30c63
+  __DATA_CONST.__const: 0x1858 sha256:3b05e0a188da4918329f1804c3d89ef0d4d7f41dac9df4618771b4846eaee62f
+  __DATA_CONST.__weak_got: 0x8 sha256:027727c9dee2f36bea2cbfed74c842dffe68ebd22969f9e678e2fc82b46b4732
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xc0 sha256:5512ec44144fb334d4491742adf37179e389e0892a0bcd0da86fa580b3954ece
-  __AUTH_CONST.__auth_got: 0x840 sha256:654e60c7347dbac914d848e152e907743952c6ee08e1d431f28c252f56314ccf
-  __AUTH.__data: 0x30 sha256:072d95ae0faecc66823a6392eef31c0455858e1ac335fb1f4e700712b79e2fbd
-  __AUTH.__constrw: 0x80 sha256:bc69dec99f46e34034fcdda56a7d43ac8c6224e38feb1d57dff50233560579b8
+  __AUTH_CONST.__const: 0xc0 sha256:3b634ff551e68992ce4e78b37643d6b5d88b2b6738b22b40eba6137bbbf01240
+  __AUTH_CONST.__auth_got: 0x848 sha256:a592311c6711605d1bb73b776e9f378bd2efc3b00469972140082e68c5262660
+  __AUTH.__data: 0x30 sha256:7b9330e6f699d3602bf10fdadc2830b9d96a0456f0ea4c198d824ff0252c87d1
+  __AUTH.__constrw: 0x80 sha256:bcdba206248a3cb5ffd34a7e7f82293ad735825cc95252496b80551b45435e84
   __DATA.__crash_info: 0x148 sha256:6da6349e97370e8d430272961ce52dff296ff7c22208bd465045a16f557b12e4
-  __DATA.__data: 0x61c sha256:a29e008a2a5d7dc30ed6a136deb3d0174fd8e6713546e5835dc9e7c705c8fa0d
+  __DATA.__data: 0x61c sha256:79475546b6290e0b0090744ebef0789f1c62c87cb2f44a879501bb6b762dd436
   __DATA.__constrw: 0xc88 sha256:ab180433466284910df2842700a53dc6cca9f3502d8580f8777224996b80adcc
   __DATA.__bss: 0xc78 sha256:8913aeb6cc98525f129f5d85a2d68d30d08a23df864edb71b3e3d526fa21d867
   __DATA.__common: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __DATA_DIRTY.__data: 0x1238 sha256:5160dff6bc83821a49d94d640b7ada86468086c44620789471cda19050eead61
+  __DATA_DIRTY.__data: 0x1238 sha256:dbbca0cf74048a5b1707d1fdee845bb3c13b732cf6ab7261e09e0f075aee7812
   __DATA_DIRTY.__bss: 0x1ad0 sha256:cff05fb4568facfcc0a26fead342b64a0165ddb18f5b5ce69b024adad40006b1
   __DATA_DIRTY.__common: 0x9c sha256:59bf9091f4cbbd2a8796bfe086a501c57226c42739dcf8ad323e7493ad51e38f
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: C2A23F09-8FE3-31C4-8EF2-FB0E0382F409
-  Functions: 1897
-  Symbols:   2576
-  CStrings:  880
+  UUID: 89A80A15-32DD-3640-942E-D37128D99302
+  Functions: 1899
+  Symbols:   2581
+  CStrings:  883
 
Symbols:
+ _filter_utmpx
+ _getpwnam_r
+ _putpair
+ _safechar
+ _ufslike_filesystems
CStrings:
+ "apfs"
+ "hfs"
+ "nfs"

```
