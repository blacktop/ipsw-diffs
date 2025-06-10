## com.apple.driver.IOPAudioClientManagerDevice

> `com.apple.driver.IOPAudioClientManagerDevice`

```diff

-240.13.0.0.0
+300.21.0.0.0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xcc3
-  __TEXT.__os_log: 0x8b8
-  __TEXT_EXEC.__text: 0x4d78
+  __TEXT.__cstring: 0xd09
+  __TEXT.__os_log: 0x986
+  __TEXT_EXEC.__text: 0x503c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xef8
   __DATA_CONST.__kalloc_type: 0x80
-  UUID: 9698F76B-A357-3AA0-A123-0608BDF6A6C6
+  UUID: BD1F4C66-2FC3-398C-A5D4-0C4DA2DC625D
   Functions: 158
   Symbols:   0
-  CStrings:  68
+  CStrings:  73
 
Functions:
~ sub_fffffff00a3172a0 -> sub_fffffff00a7123a0 : 72 -> 76
~ sub_fffffff00a3172e8 -> sub_fffffff00a7123ec : 72 -> 76
~ sub_fffffff00a317534 -> sub_fffffff00a71263c : 108 -> 112
~ __ZN27IOPAudioClientManagerDevice18_handleDeviceReadyEP9IOService : 424 -> 488
~ sub_fffffff00a317854 -> __ZN27IOPAudioClientManagerDevice20_handleSetPowerStateEmP9IOService : 104 -> 464
~ __ZN27IOPAudioClientManagerDevice11handleCloseEP9IOServicej : 180 -> 232
~ sub_fffffff00a317c60 -> sub_fffffff00a712f48 : 12 -> 16
~ ____ZN27IOPAudioClientManagerDevice19enableClientManagerEbjj_block_invoke : 132 -> 136
~ ____ZN27IOPAudioClientManagerDevice22notifyUserClientClosedEj_block_invoke : 152 -> 148
~ __ZN27IOPAudioClientManagerDevice15_retrieveConfigEP9IOServiceRNS_6ConfigE : 748 -> 964
~ __ZN27IOPAudioClientManagerDevice10_configureEP9IOService : 148 -> 144
~ sub_fffffff00a318cd8 -> sub_fffffff00a714098 : 12 -> 16
CStrings:
+ "%s::%s(%lu) disabling client managers [PreviousEnabledMask=%#llx mCurrentlyEnabledMask=%#llx ret=%#x]"
+ "%s::%s(%lu) re-enabling client managers [PreviousEnabledMask=%#llx mCurrentlyEnabledMask=%#llx ret=%#x]"
+ "_handleSetPowerState"
+ "power-up-on-set-power-state-on"
+ "power-up-on-start"

```
