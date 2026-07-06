## com.apple.driver.AppleCredentialManager

> `com.apple.driver.AppleCredentialManager`

```diff

-  __TEXT.__cstring: 0x1c50a
+  __TEXT.__cstring: 0x1c55d
   __TEXT.__const: 0x4a0
-  __TEXT_EXEC.__text: 0x7c430
+  __TEXT_EXEC.__text: 0x7c8a8
   __TEXT_EXEC.__auth_stubs: 0x750
   __DATA.__data: 0xa501
   __DATA.__common: 0x9c8

   __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__auth_ptr: 0x30
-  Functions: 1364
-  Symbols:   2114
-  CStrings:  2923
+  Functions: 1365
+  Symbols:   2115
+  CStrings:  2926
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ DeallocCredentialList.kalloc_type_view_1969
+ DeserializeCredentialList.kalloc_type_view_1931
+ _verifyPolicyDoublePressAndBio
+ copyCredentials.kalloc_type_view_9320
- DeallocCredentialList.kalloc_type_view_1943
- DeserializeCredentialList.kalloc_type_view_1905
- copyCredentials.kalloc_type_view_9213
Functions:
~ _Exec_ACMContextCredentialGetProperty_Impl : 1672 -> 1680
~ _verifyPolicy : 3708 -> 3776
+ _verifyPolicyDoublePressAndBio
~ __ZN31ACMPersistentStoreKernelService8_loadAllEPb : 1304 -> 1292
~ __ZN25ACMAnalyticsKernelService5_fromERKNS_14CommandLatencyE : 2432 -> 2424
~ _checkTransportEncryptionVersion : 108 -> 100
~ _CredSetPool_AllocCredSetEntry : 192 -> 188
~ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx : 1532 -> 1524
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAnalyticsKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeIOState.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeUtil.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMTRMInductivePolicy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonCrypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreCmd.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreCred.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreCredSet.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreDER.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreDeveloperMode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreEnv.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreExec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreOTI.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CorePrague.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreSEPControl.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreStats.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreStorage.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreStorageProtection.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreTimer.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreUserIntent.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CoreUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/CredUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/Credentials.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rMfhUd/Sources/AppleCredentialManager/common/LibSerialization.c"
+ "23:26:36"
+ "DoublePressAndBio"
+ "Jun 29 2026"
+ "Jun 29 2026, 23:26:53"
+ "rootReq && pushButtonReq && bioReq"
+ "verifyPolicyDoublePressAndBio"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/ACMKernelUtils.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerShared.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/AppleCredentialManagerUserClient.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAccessoryCacheKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMAnalyticsKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMBridgeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMFirstResponderKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMKeybagKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMLockdownModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMPersistentStoreKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeAnalyticsKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeIOState.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeKernelService.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMRestrictedModeUtil.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/AppleCredentialManager/Services/ACMTRMInductivePolicy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CommonCrypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CommonTRMLegacy.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreAuthMethod.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreCmd.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreCred.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreCredSet.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreDER.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreDeveloperMode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreEnv.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreExec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreOTI.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CorePrague.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreReqAlgo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreSEPControl.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreStats.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreStorage.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreStorageProtection.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreTRMAccCache.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreTRMMultiState.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreTimer.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreUserIntent.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CoreUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/CredUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/Credentials.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8MkJiH/Sources/AppleCredentialManager/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "22:28:28"
- "Jun 15 2026"
- "Jun 15 2026, 22:28:50"

```
