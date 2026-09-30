## AppleLockdownMode

> `/System/Library/Extensions/AppleLockdownMode.kext/AppleLockdownMode`

```diff

   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x4892
-  __TEXT_EXEC.__text: 0x1506c
+  __TEXT_EXEC.__text: 0x15064
   __TEXT_EXEC.__auth_stubs: 0x220
   __DATA.__data: 0xc6
   __DATA.__common: 0x38
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ DeallocCredentialList.kalloc_type_view_1969
+ DeserializeCredentialList.kalloc_type_view_1931
- DeallocCredentialList.kalloc_type_view_1943
- DeserializeCredentialList.kalloc_type_view_1905
Functions:
~ _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx : 1512 -> 1504

```
