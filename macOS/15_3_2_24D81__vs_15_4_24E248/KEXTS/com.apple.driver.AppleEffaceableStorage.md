## com.apple.driver.AppleEffaceableStorage

> `com.apple.driver.AppleEffaceableStorage`

```diff

 88.0.0.0.0
   __TEXT.__cstring: 0x148b
   __TEXT.__const: 0x44
-  __TEXT_EXEC.__text: 0x5020
+  __TEXT_EXEC.__text: 0x4eb0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x60

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0x1478
   __DATA_CONST.__kalloc_type: 0x300
-  UUID: 776534A1-E1A7-3499-86B9-A09F917EFABD
-  Functions: 142
+  UUID: FD9026D5-F4D4-3B83-8601-6721D66C037E
+  Functions: 132
   Symbols:   529
   CStrings:  114
 
Functions:
~ _startEffaceableStorage : 1792 -> 1800
~ _revealCopy : 236 -> 244
~ _isCopyValid : 312 -> 328
~ _setLockerWithIDExternal : 568 -> 572
~ _wipeStorage : 444 -> 448
~ _getLockerInternal : 272 -> 276
~ _discardLockers : 136 -> 140
~ _setLockerInternal : 556 -> 564
~ _effaceLockerInternal : 404 -> 408
~ _writeClone : 1068 -> 1072
~ __ZN22AppleEffaceableStorage15registerServiceEj : 232 -> 252
~ __ZN22AppleEffaceableStorage8efReturnEi : 292 -> 312
- sub_fffffe0009780488
~ __Z10setMemHookP18_effaceable_systemPvhj : 64 -> 60
~ __Z11moveMemHookP18_effaceable_systemPvPKvj : 64 -> 60
~ __Z10cmpMemHookP18_effaceable_systemPKvS2_j : 64 -> 60
~ __Z14readRandomHookP18_effaceable_systemPvj : 60 -> 56
~ __Z12calcSHA1HookP18_effaceable_systemPKvjPv : 48 -> 44
~ __Z9crc32HookP18_effaceable_systemjPKvjb : 64 -> 60
~ __Z15setPropertyHookP18_effaceable_systemPKcj : 100 -> 96
~ __ZN32AppleEffaceableStorageUserClient14externalMethodEjP25IOExternalMethodArgumentsP24IOExternalMethodDispatchP8OSObjectPv : 1784 -> 1800
- sub_fffffe0009781398

```
