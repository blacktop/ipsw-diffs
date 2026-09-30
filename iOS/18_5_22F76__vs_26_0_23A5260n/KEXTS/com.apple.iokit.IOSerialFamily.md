## com.apple.iokit.IOSerialFamily

> `com.apple.iokit.IOSerialFamily`

```diff

-117.0.0.0.0
+118.0.0.0.0
   __TEXT.__const: 0x30
-  __TEXT.__cstring: 0x3df
-  __TEXT_EXEC.__text: 0x7cf0
+  __TEXT.__cstring: 0x640
+  __TEXT_EXEC.__text: 0x81b8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x258
   __DATA.__common: 0x130
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x21
   __DATA_CONST.__auth_got: 0x248
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__mod_init_func: 0x10

   __DATA_CONST.__const: 0x1f70
   __DATA_CONST.__kalloc_type: 0x140
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 48BEB718-286E-3DF8-BD70-4AC4E4900AFE
+  UUID: A7CF6D48-9A2C-3DD8-AFDE-E20F751504C0
   Functions: 154
   Symbols:   0
-  CStrings:  48
+  CStrings:  70
 
Functions:
~ sub_fffffff00a3a0d08 -> sub_fffffff00a7b3028 : 376 -> 400
~ sub_fffffff00a3a0e80 -> sub_fffffff00a7b31b8 : 280 -> 304
~ sub_fffffff00a3a0f98 -> sub_fffffff00a7b32e8 : 1840 -> 1864
~ sub_fffffff00a3a1b24 -> __ZN6kernel24IOSerialBSDClientGlobals12assign_dev_tEv : 216 -> 348
~ sub_fffffff00a3a1bfc -> __ZN6kernel24IOSerialBSDClientGlobals11registerTTYEiP17IOSerialBSDClient : 64 -> 192
~ sub_fffffff00a3a1c3c -> __ZN6kernel24IOSerialBSDClientGlobals18getUniqueTTYSuffixEPK8OSSymbolS3_ib : 696 -> 776
~ sub_fffffff00a3a1ef4 -> __ZN6kernel24IOSerialBSDClientGlobals22releaseUniqueTTYSuffixEPK8OSSymbolS3_ : 160 -> 236
~ __ZN17IOSerialBSDClient14createDevNodesEb : 2532 -> 2716
~ sub_fffffff00a3a2978 -> __ZN17IOSerialBSDClient17setBaseTypeForDevEv : 380 -> 488
~ __ZN17IOSerialBSDClient5startEP9IOService : 624 -> 804
~ sub_fffffff00a3a33d4 -> sub_fffffff00a7b5ab4 : 284 -> 272
~ sub_fffffff00a3a3558 -> sub_fffffff00a7b5c2c : 416 -> 440
~ __ZN17IOSerialBSDClient11waitForIdleEv : 112 -> 108
~ __ZN17IOSerialBSDClient4openEiiiP4proc : 1388 -> 1444
~ __ZN17IOSerialBSDClient5closeEiiiP4proc : 944 -> 964
~ sub_fffffff00a3a4450 -> sub_fffffff00a7b6b84 : 428 -> 452
~ __ZN17IOSerialBSDClient13preemptActiveEv : 340 -> 364
~ sub_fffffff00a3a51f8 -> sub_fffffff00a7b795c : 88 -> 84
~ sub_fffffff00a3a553c -> sub_fffffff00a7b7c9c : 236 -> 260
~ __ZN17IOSerialBSDClient7getDataEPNS_7SessionE : 616 -> 636
~ __ZN17IOSerialBSDClient9procEventEPNS_7SessionE : 368 -> 388
~ __ZN17IOSerialBSDClient6txloadEPNS_7SessionEPj : 652 -> 676
~ sub_fffffff00a3a6414 -> sub_fffffff00a7b8bcc : 1184 -> 1232
CStrings:
+ "AppleVirtIOAgentDevice"
+ "IOSerialFamily::%s:  Cleanup Resources\n"
+ "IOSerialFamily::%s:  finished\n"
+ "IOSerialFamily::%s: begin\n"
+ "IOSerialFamily::%s: end\n"
+ "IOSerialFamily::%s: end normal\n"
+ "IOSerialFamily::%s: end not normal\n"
+ "IOSerialFamily::%s: finish\n"
+ "IOSerialFamily::%s: finish error\n"
+ "IOSerialFamily::%s: finish normal\n"
+ "IOSerialFamily::%s: no Nub for basename\n"
+ "IOSerialFamily::%s: no Nub for basename SET\n"
+ "IOSerialFamily::%s: no UniqueTTYSuffix\n"
+ "IOSerialFamily::%s: no suffix\n"
+ "IOSerialFamily::%s: no suffix SET\n"
+ "assign_dev_t"
+ "createDevNodes"
+ "getUniqueTTYSuffix"
+ "registerTTY"
+ "releaseUniqueTTYSuffix"
+ "setBaseTypeForDev"
+ "start"

```
