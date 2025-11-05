## com.apple.driver.AppleAHCIPort

> `com.apple.driver.AppleAHCIPort`

```diff

-383.0.0.0.0
+384.0.0.0.0
   __TEXT.__const: 0x270
   __TEXT.__cstring: 0x2765
-  __TEXT_EXEC.__text: 0xeb80
+  __TEXT_EXEC.__text: 0xf2f8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x120
   __DATA.__common: 0x108

   __DATA_CONST.__mod_term_func: 0x20
   __DATA_CONST.__const: 0x12688
   __DATA_CONST.__kalloc_type: 0x180
-  UUID: 530E1A97-CF3A-367E-8C9D-C3AFDEA2B8F1
-  Functions: 316
-  Symbols:   824
+  UUID: 8EB8C9F9-70FA-3270-9B91-7D4C16B7982A
+  Functions: 401
+  Symbols:   916
   CStrings:  320
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _ZN13AppleAHCIPort10AttachPortEP9IOService.cold.1
+ _ZN13AppleAHCIPort10AttachPortEP9IOService.cold.2
+ _ZN13AppleAHCIPort13InitWithRangeEPVhyjP9AppleAHCIP15IORegistryEntry.cold.1
+ _ZN13AppleAHCIPort13InitWithRangeEPVhyjP9AppleAHCIP15IORegistryEntry.cold.2
+ _ZN13AppleAHCIPort13setPropertiesEP8OSObject.cold.1
+ _ZN13AppleAHCIPort13setPropertiesEP8OSObject.cold.2
+ _ZN13AppleAHCIPort13setPropertiesEP8OSObject.cold.3
+ _ZN13AppleAHCIPort13setPropertiesEP8OSObject.cold.4
+ _ZN13AppleAHCIPort15HandleHotInsertEv.cold.1
+ _ZN13AppleAHCIPort15HandleHotInsertEv.cold.2
+ _ZN13AppleAHCIPort18ProcessAHCIRequestEP8OSObject.cold.1
+ _ZN13AppleAHCIPort18WaitForLinkPresentEj.cold.1
+ _ZN13AppleAHCIPort18WaitForLinkPresentEj.cold.2
+ _ZN13AppleAHCIPort19SoftResetDevicePortEjP8OSObjectPj.cold.1
+ _ZN13AppleAHCIPort23ProcessAHCIRequestGatedEP8OSObjectj.cold.2
+ _ZN13AppleAHCIPort24PreparePolledAHCIRequestEP18IOMemoryDescriptor.cold.1
+ _ZN13AppleAHCIPort24PreparePolledAHCIRequestEP18IOMemoryDescriptor.cold.2
+ _ZN13AppleAHCIPort24PreparePolledAHCIRequestEP18IOMemoryDescriptor.cold.3
+ _ZN13AppleAHCIPort24ProcessPolledAHCIRequestEyy.cold.1
+ _ZN13AppleAHCIPort24ProcessPolledAHCIRequestEyy.cold.2
+ _ZN13AppleAHCIPort24ProcessPolledAHCIRequestEyy.cold.3
+ _ZN13AppleAHCIPort25CompletePolledAHCIRequestEv.cold.1
+ _ZN13AppleAHCIPort29AllocateAHCIRequestsWithCountEj.cold.1
+ _ZN13AppleAHCIPort29AllocateAHCIRequestsWithCountEj.cold.2
+ _ZN13AppleAHCIPort29AllocateAHCIRequestsWithCountEj.cold.3
+ _ZN13AppleAHCIPort29AllocateAHCIRequestsWithCountEj.cold.4
+ _ZN13AppleAHCIPort29AllocateAHCIRequestsWithCountEj.cold.5
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.1
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.2
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.3
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.4
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.5
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.6
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.7
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.8
+ _ZN16ASMediaAppleAHCI12LoadFirmwareEv.cold.9
+ _ZN16ASMediaAppleAHCI19ProgramPCIeDMATableEv.cold.1
+ _ZN16ASMediaAppleAHCI19ProgramPCIeDMATableEv.cold.2
+ _ZN16ASMediaAppleAHCI19ProgramPCIeDMATableEv.cold.3
+ _ZN16ASMediaAppleAHCI19ProgramPCIeDMATableEv.cold.4
+ _ZN16ASMediaAppleAHCI19ProgramPCIeDMATableEv.cold.5
+ _ZN16ASMediaAppleAHCI19ProgramPCIeDMATableEv.cold.6
+ _ZN16ASMediaAppleAHCI19ProgramPCIeDMATableEv.cold.7
+ _ZN16ASMediaAppleAHCI22CalculateHardwareCRC32Ej.cold.1
+ _ZN16ASMediaAppleAHCI9MapBufferEPP12IODMACommandPyP18IOMemoryDescriptor.cold.1
+ _ZN16ASMediaAppleAHCI9MapBufferEPP12IODMACommandPyP18IOMemoryDescriptor.cold.2
+ _ZN16ASMediaAppleAHCI9MapBufferEPP12IODMACommandPyP18IOMemoryDescriptor.cold.3
+ _ZN16ASMediaAppleAHCI9MapBufferEPP12IODMACommandPyP18IOMemoryDescriptor.cold.4
+ _ZN20AppleAHCIEventSource9WithOwnerEP13AppleAHCIPortPFvP8OSObjectzE.cold.1
+ _ZN20AppleAHCIEventSource9WithOwnerEP13AppleAHCIPortPFvP8OSObjectzE.cold.2
+ _ZN22AppleAHCIPolledAdapter9WithOwnerEP9AppleAHCI.cold.1
+ _ZN26AppleAHCIPortPolledAdapter19WithOwnerAndRequestEP13AppleAHCIPortP8OSObject.cold.1
+ _ZN26AppleAHCIPortPolledAdapter19WithOwnerAndRequestEP13AppleAHCIPortP8OSObject.cold.2
+ _ZN26AppleAHCIPortPolledAdapter19WithOwnerAndRequestEP13AppleAHCIPortP8OSObject.cold.3
+ _ZN26AppleAHCIPortPolledAdapter4openEjP18IOMemoryDescriptor.cold.1
+ _ZN26AppleAHCIPortPolledAdapter4openEjP18IOMemoryDescriptor.cold.2
+ _ZN26AppleAHCIPortPolledAdapter4openEjP18IOMemoryDescriptor.cold.3
+ _ZN26AppleAHCIPortPolledAdapter7startIOEjjyy18IOPolledCompletion.cold.1
+ _ZN9AppleAHCI10handleOpenEP9IOServicejPv.cold.1
+ _ZN9AppleAHCI13setPowerStateEmP9IOService.cold.1
+ _ZN9AppleAHCI13setPropertiesEP8OSObject.cold.1
+ _ZN9AppleAHCI13setPropertiesEP8OSObject.cold.2
+ _ZN9AppleAHCI20CreateIndividualPortEj.cold.1
+ _ZN9AppleAHCI20CreateIndividualPortEj.cold.2
+ _ZN9AppleAHCI20CreateIndividualPortEj.cold.3
+ _ZN9AppleAHCI25GetDeviceTreeEntryForPortEj.cold.1
+ _ZN9AppleAHCI5startEP9IOService.cold.1
+ _ZN9AppleAHCI5startEP9IOService.cold.10
+ _ZN9AppleAHCI5startEP9IOService.cold.11
+ _ZN9AppleAHCI5startEP9IOService.cold.12
+ _ZN9AppleAHCI5startEP9IOService.cold.13
+ _ZN9AppleAHCI5startEP9IOService.cold.14
+ _ZN9AppleAHCI5startEP9IOService.cold.2
+ _ZN9AppleAHCI5startEP9IOService.cold.3
+ _ZN9AppleAHCI5startEP9IOService.cold.4
+ _ZN9AppleAHCI5startEP9IOService.cold.5
+ _ZN9AppleAHCI5startEP9IOService.cold.6
+ _ZN9AppleAHCI5startEP9IOService.cold.7
+ _ZN9AppleAHCI5startEP9IOService.cold.8
+ _ZN9AppleAHCI5startEP9IOService.cold.9
+ _ZN9AppleAHCI8ResetHBAEv.cold.1
+ _gASM1062FirmwareSize
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleAHCI/ASMediaAppleAHCI.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleAHCI/AppleAHCI.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleAHCI/AppleAHCIPort.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleAHCI/AppleAHCIPortPolledAdapter.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAHCI/ASMediaAppleAHCI.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAHCI/AppleAHCI.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAHCI/AppleAHCIPort.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AppleAHCI/AppleAHCIPortPolledAdapter.cpp"

```
