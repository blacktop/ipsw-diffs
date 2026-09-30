## com.apple.driver.AppleCredentialManager

> `com.apple.driver.AppleCredentialManager`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-949.0.9.0.0
-  __TEXT.__cstring: 0x1c55d
+949.0.13.0.0
+  __TEXT.__cstring: 0x1c7bc
   __TEXT.__const: 0x4a0
-  __TEXT_EXEC.__text: 0x7c8a8
+  __TEXT_EXEC.__text: 0x7cdd8
   __TEXT_EXEC.__auth_stubs: 0x750
   __DATA.__data: 0xa501
   __DATA.__common: 0x9c8

   __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x30
-  Functions: 1365
-  Symbols:   2067
-  CStrings:  2926
+  Functions: 1368
+  Symbols:   2070
+  CStrings:  2936
 
Symbols:
+ CredSet_AddCredEntry.kalloc_type_view_175
+ CredSet_AddCredEntry.kalloc_type_view_199
+ DeallocCredentialList.kalloc_type_view_1975
+ DeserializeCredentialList.kalloc_type_view_1937
+ __ZN14ACMKernelUtils18waitForSEPEndpointEy
+ __ZN22AppleCredentialManager18setPowerStateGatedEPKm
+ __ZN22AppleCredentialManager18systemWillShutdownEj
+ __ZN22AppleCredentialManager29markSystemIsShuttingDownGatedEv
+ __ZN22AppleCredentialManager41setWaitForSEPEndpointSystemIsShuttingDownEb
- CredSet_AddCredEntry.kalloc_type_view_176
- CredSet_AddCredEntry.kalloc_type_view_201
- DeallocCredentialList.kalloc_type_view_1969
- DeserializeCredentialList.kalloc_type_view_1931
- __ZN14ACMKernelUtils18waitForSEPEndpointEv
- __ZN22AppleCredentialManager18setPowerStateGatedEPm
CStrings:
+ "%s: %s: *** GOING OFFLINE *** ---> aborting SEP command=%u (isPoweringOff=%s, isSystemShuttingDown=%s).\n"
+ "%s: %s: kACMCredentialTypeSignature ignored, signatureSize %u out of range.\n"
+ "%s: %s: marked system shutting down, stateFlags=0x%x.\n"
+ "%s: %s: newState=%u (prev=%u), stateFlags=0x%x.\n"
+ "%s: %s: prepared for system shutdown.\n"
+ "%s: %s: preparing for system shutdown.\n"
+ "%s: %s: timed out waiting for %s (timeoutMs=%llu).\n"
+ "%s: %s: timed out waiting for AppleSEPManager (timeoutMs=%llu).\n"
+ "%s: %s: wait canceled, system is shutting down (cmd=%u).\n"
+ "%s: %s: waiting (cmd=%u).\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAnalyticsKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeIOState.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMTRMInductivePolicy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CommonCrypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreCmd.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreCred.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreCredSet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreDER.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreDeveloperMode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreEnv.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreExec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreOTI.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CorePrague.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreSEPControl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreStats.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreStorage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreStorageProtection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreTimer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreUserIntent.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CoreUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/CredUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/Credentials.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2fE8jC/Sources/AppleCredentialManager/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "121111121222121212111111111111112121122211122212211"
+ "21:29:10"
+ "Jul 14 2026"
+ "Jul 14 2026, 21:29:22"
+ "markSystemIsShuttingDownGated"
+ "newState"
+ "sigSize > 0 && sigSize <= kACMCredentialDataSignatureMaxSize"
+ "systemWillShutdown"
+ "waitForSEPEndpoint"
- "%s: %s: called, currentState=%u -> newState=%u.\n"
- "%s: %s: waiting cmd=%u.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAnalyticsKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeIOState.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeUtil.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMTRMInductivePolicy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonCrypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreCmd.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreCred.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreCredSet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreDER.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreDeveloperMode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreEnv.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreExec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreOTI.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CorePrague.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreSEPControl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreStats.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreStorage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreStorageProtection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreTimer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreUserIntent.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CredUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/Credentials.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/LibSerialization.c"
- "112"
- "12111112122212121211111111111111212112211122212211"
- "23:26:36"
- "Jun 29 2026"
- "Jun 29 2026, 23:26:53"
- "newstate"
- "sepEndpoint"
```
