## com.apple.driver.AppleM68Buttons

> `com.apple.driver.AppleM68Buttons`

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

 132.0.0.0.0
-  __TEXT.__cstring: 0x4f5d
+  __TEXT.__cstring: 0x4f9a
   __TEXT.__const: 0x208
   __TEXT.__os_log: 0x61f
-  __TEXT_EXEC.__text: 0x1db34
+  __TEXT_EXEC.__text: 0x1db74
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0xca
   __DATA.__common: 0x88

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 327
   Symbols:   952
-  CStrings:  628
+  CStrings:  629
 
Symbols:
+ DeallocCredentialList.kalloc_type_view_1975
+ DeserializeCredentialList.kalloc_type_view_1937
- DeallocCredentialList.kalloc_type_view_1969
- DeserializeCredentialList.kalloc_type_view_1931
Functions:
~ _DeserializeCredential : 1456 -> 1520
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.UTBWzh/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"
+ "sigSize > 0 && sigSize <= kACMCredentialDataSignatureMaxSize"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelLib.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/ACMKernelLib/ACMKernelTransport.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/CommonMem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.2qR07k/Sources/AppleCredentialManager_KernelLibs/common/LibSerialization.c"
```
