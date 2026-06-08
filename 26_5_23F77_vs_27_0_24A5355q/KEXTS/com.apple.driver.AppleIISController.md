## com.apple.driver.AppleIISController

> `com.apple.driver.AppleIISController`

```diff

-540.4.0.0.0
-  __TEXT.__cstring: 0x97e
-  __TEXT_EXEC.__text: 0x6d38
+600.3.0.0.0
+  __TEXT.__cstring: 0x9b8
+  __TEXT.__os_log: 0x436
+  __TEXT_EXEC.__text: 0x7e84
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x188
   __DATA.__common: 0x100
   __DATA.__bss: 0x10
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1868
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 8E4FF9AA-BDDE-30E6-9596-602A254E49F1
+  __DATA_CONST.__auth_got: 0x178
+  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__auth_ptr: 0x8
+  UUID: C1AB3534-4B61-3AB6-B6A7-7219AC8D3DF5
   Functions: 201
   Symbols:   0
-  CStrings:  85
+  CStrings:  108
 
Functions:
~ sub_fffffe0008cca9c0 -> sub_fffffe0008f98080 : 56 -> 60
~ __ZN21AppleARMIISController5startEP9IOService -> sub_fffffe0008f98154 : 1548 -> 2216
~ sub_fffffe0008ccb680 -> sub_fffffe0008f98fe0 : 124 -> 236
~ __ZN21AppleARMIISController22enqueueIISCommandGatedEP17AppleARMIISDevicejP18AppleARMIISCommand -> sub_fffffe0008f990cc : 1660 -> 3052
~ __ZN21AppleARMIISController18completeIISCommandEP18AppleARMIISCommand -> sub_fffffe0008f99cb8 : 1056 -> 1484
~ __ZN21AppleARMIISController20completeIISNoCommandEv -> sub_fffffe0008f9a284 : 160 -> 276
~ sub_fffffe0008ccc244 -> sub_fffffe0008f9a3a4 : 328 -> 716
~ sub_fffffe0008ccc750 -> sub_fffffe0008f9aa34 : 76 -> 228
~ __ZNK17AppleARMIISDevice12getIISConfigEP17AppleARMIISConfig -> sub_fffffe0008f9b1c8 : 212 -> 352
~ __ZN17AppleARMIISDevice12setIISConfigEP17AppleARMIISConfig -> sub_fffffe0008f9b328 : 280 -> 420
~ __ZN17AppleARMIISDevice14validIISConfigEP17AppleARMIISConfig -> sub_fffffe0008f9b4cc : 252 -> 404
~ __ZN17AppleARMIISDevice12transferDataEP18IOMemoryDescriptorjyyP21AppleARMIISCompletionPK13mach_timespec -> sub_fffffe0008f9b6d0 : 724 -> 1072
~ __ZN17AppleARMIISDevice16setMCLKFrequencyEy -> sub_fffffe0008f9bd68 : 252 -> 364
~ __ZN17AppleARMIISDevice21initWithRegistryEntryEP15IORegistryEntryP9IOService -> sub_fffffe0008f9c6fc : 764 -> 1040
CStrings:
+ "%s:%s::%s:%d: %s\n"
+ "121111121222121212122211111111112122222222222222222222222222222222222222222222222222222"
+ "init"
- "1211111212221212121222111111111121"

```
