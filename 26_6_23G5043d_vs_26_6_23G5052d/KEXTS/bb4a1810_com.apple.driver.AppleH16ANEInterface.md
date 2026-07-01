## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

-  __TEXT.__const: 0xd90
-  __TEXT.__cstring: 0x11391
-  __TEXT.__os_log: 0x370f9
-  __TEXT_EXEC.__text: 0x10a06c
+  __TEXT.__const: 0xd10
+  __TEXT.__cstring: 0x113dc
+  __TEXT.__os_log: 0x37320
+  __TEXT_EXEC.__text: 0x10a7c4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4838
   __DATA.__common: 0x680
   __DATA.__bss: 0x630
-  __DATA_CONST.__auth_got: 0x998
+  __DATA_CONST.__auth_got: 0x9a8
   __DATA_CONST.__got: 0x148
   __DATA_CONST.__mod_init_func: 0x250
   __DATA_CONST.__mod_term_func: 0x118
   __DATA_CONST.__const: 0xcbf8
-  __DATA_CONST.__kalloc_type: 0x3b00
+  __DATA_CONST.__kalloc_type: 0x3b80
   __DATA_CONST.__kalloc_var: 0x3200
   Functions: 3577
   Symbols:   0
-  CStrings:  4480
+  CStrings:  4489
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_var : content changed
Functions:
~ __ZN12ANEScheduler33ANE_CheckForPendingRequests_gatedEv : 964 -> 1040
~ sub_fffffe0008a444d8 -> sub_fffffe0008a4cc64 : 280 -> 292
~ sub_fffffe0008a447d4 -> sub_fffffe0008a4cf6c : 300 -> 312
~ __ZN11ANEHWDevice20queuePendingRequestsEjb : 396 -> 460
~ __ZN11ANEHWDevice39ANE_ProgramCheckandPrewireBuffers_gatedEP14ANEBufferCacheP21ANEProgramRequestArgsP37ANEProgramSendRequestAdditionalParamsRNSt3__110unique_ptrI21ANEResourceCollectionNS6_14default_deleteIS8_EEEE : 1548 -> 1880
~ __ZN11ANEHWDevice26ANE_MemoryMapRequest_gatedEPK18ANEMemoryMapParamsbbRNSt3__110unique_ptrI21ANEResourceCollectionNS3_14default_deleteIS5_EEEE : 12348 -> 12564
~ __ZN11ANEHWDevice8ANE_InitEv : 13540 -> 13524
~ __ZN11ANEHWDevice15mapFwCTRRRegionEv : 3924 -> 3920
~ __ZN11ANEHWDevice5startEP9IOService : 17124 -> 17112
~ __ZN11ANEHWDevice23initializeANEPropertiesEv : 1472 -> 1492
~ __ZN11ANEHWDevice22initializeANESoCConfigEv : 10780 -> 11024
~ __ZN11ANEHWDevice27ANEPowerChangeHandler_gatedEjP9IOServicePvm : 2812 -> 3152
~ __ZN18ANEProgramResource23ANE_ProgramInitialSetupEP11ANEHWDeviceP20ANEProgramCreateArgsP26ANEProgramCreateArgsOutputP32ANEProgramCreateAdditionalParams : 5892 -> 5896
~ __ZN11ANEHWDevice45ANE_PatchClusterProcessInstanceWeightsBuffersEP10ANEProcessP30ANEClientProgramInstanceParamsP4task : 4940 -> 4944
~ __ZN11ANEHWDevice38ANE_PatchProcessInstanceWeightsBuffersEP10ANEProcessP30ANEClientProgramInstanceParamsP4task : 2352 -> 2356
~ __ZN11ANEHWDevice25aneVnodeTrustVerificationEP11vfs_contextP5vnodeP4taski12ANEVnodeTypePb : 1272 -> 1776
~ __Z14aneVnodeLookupPKcPmPP11vfs_context : 816 -> 896
CStrings:
+ "%s: %s: One second sleep timed out waiting for checkForPendingRequests thread to block. Retries=%u\n"
+ "%s: %s: Shared iPad - checking further filePath: %s\n"
+ "%s: %s: Shared iPad DataVault verification succeeded\n"
+ "%s: %s: WARN: fCheckForPendingRequestsThreadRunning is still true. Returning from will sleep anyway\n"
+ "/.resolve/2%s"
+ "/Library/Caches/com.apple.aned/"
+ "/private/var/MobileAsset/AssetsV2/"
+ "/private/var/Users/"
+ "/private/var/mobile/Library/AppleIntelligencePlatform/AppModelAssets/"
+ "/private/var/mobile/Library/Caches/com.apple.aned/"
+ "[ERROR] %s: %s: ERROR: Failed to lookup file at %s err=%d\n"
+ "[ERROR] %s: %s: Shared iPad - clientInDataVault: %d clientFilePath: %s\n"
+ "[ERROR] %s: %s: Total number of uncached IO > max allowed in auto-prewiring: %u\n"
+ "aneVnodeSecureLookup"
- "%s: %s: ERROR: Failed to lookup macho file at %s\n"
- "/private/var/MobileAsset/AssetsV2"
- "/private/var/mobile/Library/AppleIntelligencePlatform/AppModelAssets"
- "/private/var/mobile/Library/Caches/com.apple.aned"
- "aneVnodeLookup"

```
