## libsystem_sanitizers.dylib

> `/usr/lib/system/libsystem_sanitizers.dylib`

```diff

-  __TEXT.__text: 0x7a68
+  __TEXT.__text: 0x7a58
   __TEXT.__const: 0x160
   __TEXT.__cstring: 0xf7c
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x38
-  __DATA.__bss: 0x529
+  __DATA.__bss: 0x521
   __DATA.__common: 0x8
+  __DATA_DIRTY.__data: 0x38
+  __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x18
-  __DATA_DIRTY.__bss: 0x30
   __TPRO_CONST.__data: 0x8
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libmacho.dylib
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ __ZNK4asan19GlobalsRegistryImpl12getGlobalVarEm : 120 -> 104
~ __ZN4asan15ReportGenerator8StackVar5parseERPKc : 212 -> 200
~ __ZNK10ASanShadow16regionIsPoisonedEmm : 268 -> 264
~ __ZNK10ASanShadow16getAllocationEndEN4asan12MemoryAccessE : 276 -> 292

```
