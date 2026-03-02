## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-130.12.0.0.0
-  __TEXT.__cstring: 0x5df1
-  __TEXT.__os_log: 0x4b91
+130.13.0.0.0
+  __TEXT.__cstring: 0x5e27
+  __TEXT.__os_log: 0x4bbf
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x3f91c
+  __TEXT_EXEC.__text: 0x3f9b4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x460
   __DATA.__common: 0x898

   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0x1090
   __DATA_CONST.__assert: 0xa0
-  UUID: D49AA5BA-4A7B-3F1B-8CB0-AFAD9A4BDD1C
+  UUID: BECCFE2D-BF6B-3963-8391-BA2F709EBFFD
   Functions: 1982
   Symbols:   0
-  CStrings:  876
+  CStrings:  878
 
Functions:
~ __ZN11IOGPUDevice12new_resourceEP20IOGPUNewResourceArgsP26IOGPUNewResourceReturnDatayPj : 2308 -> 2312
~ __ZN29IOGPUMappingCommandDescriptor15performMappingsEv : 452 -> 600
CStrings:
+ "%s mapping descriptor prepare failed (0x%X)\n\n"
+ "void IOGPUMappingCommandDescriptor::performMappings()"

```
