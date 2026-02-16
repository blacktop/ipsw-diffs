## com.apple.driver.AppleT6020PCIePIODMA

> `com.apple.driver.AppleT6020PCIePIODMA`

```diff

-936.80.10.0.0
-  __TEXT.__cstring: 0xac9
-  __TEXT_EXEC.__text: 0x8048
+936.100.34.0.0
+  __TEXT.__cstring: 0xacb
+  __TEXT_EXEC.__text: 0x7998
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x70

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xd20
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 6F47B024-C91A-3683-B030-E5CF829C06A6
+  UUID: 1C28DBC3-7B31-325E-8442-8346EFCD3B01
   Functions: 72
   Symbols:   0
   CStrings:  67
Functions:
~ __ZN20AppleT6020PCIePIODMA5startEP9IOService : 212 -> 204
~ sub_fffffe0009cc7d28 -> sub_fffffe0009401680 : 120 -> 112
~ sub_fffffe0009cc7da0 -> sub_fffffe00094016f0 : 120 -> 112
~ __ZN15ApplePCIePIODMA5startEP9IOService : 2280 -> 2116
~ sub_fffffe0009cc8b48 -> sub_fffffe00094023ec : 608 -> 560
~ __ZN15ApplePCIePIODMA12hostToDeviceEP18IOMemoryDescriptoryS1_yy -> sub_fffffe0009402744 : 2196 -> 2044
~ __ZN15ApplePCIePIODMA27getBaseAddressRegisterIndexEy : 1008 -> 992
~ __ZN15ApplePCIePIODMA12hostToDeviceEPKvP18IOMemoryDescriptoryy -> __ZN15ApplePCIePIODMA12hostToDeviceEP18IOMemoryDescriptoryS1_yy : 2180 -> 2028
~ __ZN15ApplePCIePIODMA12deviceToHostEP18IOMemoryDescriptoryS1_yy : 1556 -> 1436
~ __ZN15ApplePCIePIODMA12deviceToHostEP18IOMemoryDescriptoryPvy -> sub_fffffe00094040a8 : 1540 -> 1420
~ sub_fffffe0009ccaff0 -> sub_fffffe0009404634 : 7212 -> 6740
~ __ZN15ApplePCIePIODMA27_applyOffloadEngineTunablesEv : 324 -> 308
~ sub_fffffe0009cccf4c -> sub_fffffe00094063a8 : 2140 -> 1996
~ sub_fffffe0009ccd840 -> sub_fffffe0009406c0c : 1616 -> 1532
~ sub_fffffe0009ccde90 -> sub_fffffe0009407208 : 744 -> 712
~ sub_fffffe0009cce178 -> sub_fffffe00094074d0 : 744 -> 712
~ sub_fffffe0009cce460 -> sub_fffffe0009407798 : 744 -> 712
~ sub_fffffe0009cce748 -> sub_fffffe0009407a60 : 744 -> 712
~ __ZN15ApplePCIePIODMA22_applyTunablesFromDataEPK6OSDataMS_FjjEMS_FvjjEPKc : 3116 -> 3044
CStrings:
+ "121111121222121212121111111122111111111111222222"
+ "12111112122212121212111111112211111111111122222212"
- "12111112122212121212111111112211111111111122222"
- "1211111212221212121211111111221111111111112222212"

```
