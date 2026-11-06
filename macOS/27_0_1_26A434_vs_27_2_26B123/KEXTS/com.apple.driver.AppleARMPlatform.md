## com.apple.driver.AppleARMPlatform

> `com.apple.driver.AppleARMPlatform`

```diff

-1150.0.1.0.0
+1150.40.5.0.0
   __TEXT.__const: 0x1ae0
-  __TEXT.__os_log: 0x14f7
-  __TEXT.__cstring: 0xd0ec
-  __TEXT_EXEC.__text: 0x58648
+  __TEXT.__os_log: 0x1553
+  __TEXT.__cstring: 0xd158
+  __TEXT_EXEC.__text: 0x587a8
   __TEXT_EXEC.__auth_stubs: 0xd60
   __DATA.__data: 0x6c8
   __DATA.__common: 0xcd8

   __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x1f8
   Functions: 2244
-  Symbols:   3609
-  CStrings:  1738
+  Symbols:   3611
+  CStrings:  1742
 
Symbols:
+ __ZZN18AppleMCCUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptorE11_os_log_fmt_3
+ __ZZZN23AppleMemCacheController30getDataCollectionMemDescriptorEvEUb4_E11_os_log_fmt_0
Functions:
~ __ZN18AppleMCCUserClient19clientMemoryForTypeEjPjPP18IOMemoryDescriptor : 600 -> 700
~ ____ZN23AppleMemCacheController21disableDataCollectionEv_block_invoke : 336 -> 368
~ ____ZN23AppleMemCacheController30getDataCollectionMemDescriptorEv_block_invoke : 256 -> 412
~ __ZN16AppleARMFunction34InitWithTargetDataAndSymbol_InvokeE5IORPCP15OSMetaClassBasePFbS2_P9IOServiceP6OSDataP8OSStringE : 308 -> 312
~ __ZN16AppleARMFunction13Create_InvokeE5IORPCPFiP9IOServiceP6OSDataP8OSStringPPS_E : 312 -> 316
~ __ZN16AppleARMFunction19WithProvider_InvokeE5IORPCPFiP9IOServiceP8OSStringjPPS_E : 264 -> 268
~ __ZN16AppleARMFunction29RegisterFunctionParent_InvokeE5IORPCPFiP9IOServiceS2_E : 260 -> 264
~ __ZN16AppleARMIODevice24EnableDeviceClock_InvokeE5IORPCP15OSMetaClassBasePFiS2_jjE : 168 -> 172
~ __ZN16AppleARMIODevice24EnableDevicePower_InvokeE5IORPCP15OSMetaClassBasePFiS2_jPjjE : 172 -> 176
~ __ZN16AppleARMIODevice27EnableDevicePinGroup_InvokeE5IORPCP15OSMetaClassBasePFiS2_jjE : 168 -> 172
~ __ZN16AppleARMIODevice26SetDevicePowerState_InvokeE5IORPCP15OSMetaClassBasePFiS2_26AppleARMIODevicePowerStatejE : 168 -> 172
~ __ZN16AppleARMIODevice23EnablePsdService_InvokeE5IORPCP15OSMetaClassBasePFiS2_jjjjE : 172 -> 176
~ __ZN16AppleARMIODevice22ResetPsdService_InvokeE5IORPCP15OSMetaClassBasePFiS2_jjE : 168 -> 172
~ __ZN16AppleARMIODevice25GetPsdServiceState_InvokeE5IORPCP15OSMetaClassBasePFiS2_PjjjE : 172 -> 176
~ __ZN16AppleARMIODevice20IsDMACoherent_InvokeE5IORPCP15OSMetaClassBasePFiS2_jPbE : 172 -> 176
~ __ZN16AppleARMIODevice26CopyClockNameString_InvokeE5IORPCP15OSMetaClassBasePFiS2_PP8OSStringjE : 200 -> 204
~ __ZN16AppleARMIODevice33GetClockFrequencyWithIndex_InvokeE5IORPCP15OSMetaClassBasePFiS2_jPyE : 172 -> 176
~ __ZN16AppleARMIODevice32GetClockFrequencyWithName_InvokeE5IORPCP15OSMetaClassBasePFiS2_PKcPyE : 220 -> 224
~ __ZN16AppleARMIODevice34GetClockFrequencyWithSymbol_InvokeE5IORPCP15OSMetaClassBasePFiS2_P8OSStringPyE : 236 -> 240
CStrings:
+ "%s:%d: Failed to create mem descriptor for shared data queue\n\n"
+ "%s:%d: No data collection buffer available\n\n"
+ "Failed to create mem descriptor for shared data queue\n"
+ "No data collection buffer available\n"
```
