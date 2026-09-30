## com.apple.driver.AppleLockdownMode

> `com.apple.driver.AppleLockdownMode`

```diff

   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x4976
-  __TEXT_EXEC.__text: 0x155e8
+  __TEXT_EXEC.__text: 0x155e0
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38
Sections:
~ __TEXT.__cstring : content changed
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
- DeallocCredentialList.kalloc_type_view_1943
- DeserializeCredentialList.kalloc_type_view_1905
Functions:
~ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx : 1532 -> 1524
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.xl45bN/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"

```
