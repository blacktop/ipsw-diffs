## DiskManagement

> `/System/Library/PrivateFrameworks/DiskManagement.framework/Versions/A/DiskManagement`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-1076.0.1.0.0
-  __TEXT.__text: 0x95f9c
-  __TEXT.__objc_methlist: 0x239c
-  __TEXT.__cstring: 0x352e8
-  __TEXT.__const: 0x14d4
-  __TEXT.__gcc_except_tab: 0xe40
+1076.0.3.0.0
+  __TEXT.__text: 0x962b4
+  __TEXT.__objc_methlist: 0x23a4
+  __TEXT.__cstring: 0x35343
+  __TEXT.__const: 0x152c
+  __TEXT.__gcc_except_tab: 0xe50
   __TEXT.__oslogstring: 0x33
-  __TEXT.__unwind_info: 0x1748
+  __TEXT.__unwind_info: 0x1758
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd8
+  __DATA_CONST.__objc_selrefs: 0x1ce0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0xe48
   __DATA_CONST.__got: 0x408
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x20aa0
-  __AUTH_CONST.__objc_const: 0x1fa0
+  __AUTH_CONST.__const: 0x4d0
+  __AUTH_CONST.__cfstring: 0x20ac0
+  __AUTH_CONST.__objc_const: 0x1fc0
   __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0xce8
+  __AUTH_CONST.__auth_got: 0xd08
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x134
-  __DATA.__data: 0xbc8
+  __DATA.__objc_ivar: 0x138
+  __DATA.__data: 0xbf0
   __DATA.__common: 0x450
   __DATA.__bss: 0xa9
   __DATA_DIRTY.__objc_data: 0x500

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1913
-  Symbols:   3762
-  CStrings:  5620
+  Functions: 1919
+  Symbols:   3784
+  CStrings:  5622
 
Symbols:
+ -[DMManagerPrivVars teardownXPCConnectionWaitingForQuiesce:]
+ OBJC_IVAR_$_DMManagerPrivVars._xpcInvalidatedSem
+ ___block_descriptor_40_e8_32o_e5_v8?0l
+ ___copy_helper_block_e8_32o
+ ___der_key_last_mesa_auth
+ ___der_key_last_mesa_unlock
+ ___der_key_last_passcode_auth
+ ___der_key_last_passcode_unlock
+ ___der_key_sks_heap_stats
+ ___destroy_helper_block_e8_32o
+ _aks_get_convenience_bio_state
+ _aks_get_sks_heap_stats
+ _der_key_last_mesa_auth
+ _der_key_last_mesa_unlock
+ _der_key_last_passcode_auth
+ _der_key_last_passcode_unlock
+ _der_key_sks_heap_stats
+ _dispatch_release
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_msgSend$teardownXPCConnectionWaitingForQuiesce:
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tSt0vh/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tSt0vh/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tSt0vh/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tSt0vh/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.tSt0vh/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "23:10:30"
+ "Jul 10 2026"
+ "aks_get_convenience_bio_state"
+ "callback port invalidated during teardown; dropping callback"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QPzQcM/Sources/AppleKeyStore_libs/shared_crypto.c"
- "00:09:01"
- "Jun 27 2026"
```
