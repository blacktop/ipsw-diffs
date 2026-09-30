## CarbonCore

> `/System/Library/PrivateFrameworks/CarbonCore.framework/CarbonCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__data`

```diff

-1404.0.0.0.0
-  __TEXT.__text: 0x342bc
+1405.0.0.0.0
+  __TEXT.__text: 0x34288
   __TEXT.__const: 0x24d0
   __TEXT.__cstring: 0x20126
   __TEXT.__oslogstring: 0x4801

   __AUTH_CONST.__const: 0x1630
   __AUTH_CONST.__cfstring: 0xba0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xa48
+  __AUTH_CONST.__auth_got: 0xa38
   __AUTH.__data: 0x1e8
   __DATA.__data: 0x2e8
   __DATA.__crash_info: 0x148

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   Functions: 1099
-  Symbols:   1608
+  Symbols:   1606
   CStrings:  4670
 
Symbols:
- ___sprintf_chk
- ___strcpy_chk
Functions:
~ ___FileIDTreeGetCachedPort_block_invoke : 340 -> 284
~ _FSNodeServer_SyncSystemUniverseInternal : 1552 -> 1572
~ _FSNodeSyncVolumesCallback : 500 -> 516
~ _FSNodeServer_SyncWithSystemUniverseInternal : 896 -> 900
~ _FileIDTreePrintNodeTreeInternal : 416 -> 392
~ _PrintVolumeIDCallbacks_LeafNodeFoundCallback : 348 -> 320
~ _FileIDTreeGetAndLockVolumeEntryFromVolumeStringPtr : 1076 -> 1080
~ _OUTLINED_FUNCTION_33 : 20 -> 12
~ _OUTLINED_FUNCTION_34 : 12 -> 20
~ _OUTLINED_FUNCTION_38 : 20 -> 12
~ _OUTLINED_FUNCTION_39 : 12 -> 20
~ _TERMINATING_DUE_TO_FILE_ID_TREE_PORTCACHE_MEMORY_CORRUPTION : 216 -> 212
~ _FileIDTree_BeginTransactionInternal : 816 -> 832
```
