## com.apple.driver.AppleH11ANEInterface

> `com.apple.driver.AppleH11ANEInterface`

```diff

 9.512.0.0.0
-  __TEXT.__os_log: 0x36016
+  __TEXT.__os_log: 0x36061
   __TEXT.__cstring: 0xcf7a
   __TEXT.__const: 0xcf8
-  __TEXT_EXEC.__text: 0xf20c0
+  __TEXT_EXEC.__text: 0xf21a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4834
   __DATA.__common: 0x680

   __DATA_CONST.__kalloc_var: 0x3200
   __DATA_CONST.__kalloc_type: 0x3b80
   Functions: 2981
-  Symbols:   7795
-  CStrings:  4206
+  Symbols:   7796
+  CStrings:  4207
 
Symbols:
+ __ZZN24ANEProgramLegacyResource29populateProcedureLiveInParamsEP26ANEProgramCreateArgsOutputjE11_os_log_fmt_9
Functions:
~ __ZN24ANEProgramLegacyResource10preProcessEP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParamsP26ANEProgramCreateArgsOutput : 3916 -> 3960
~ __ZN24ANEProgramLegacyResource24programLoadFromMachoFileEP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParams : 9424 -> 9460
~ __ZN24ANEProgramLegacyResource25initMutableKernelSectionsEP26ANEProgramCreateArgsOutputP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParams : 2476 -> 2468
~ __ZN24ANEProgramLegacyResource34populateProcedureMutableKernelInfoEP26ANEProgramCreateArgsOutputj : 820 -> 824
~ __ZN24ANEProgramLegacyResource29populateProcedureLiveInParamsEP26ANEProgramCreateArgsOutputj : 3068 -> 3216
CStrings:
+ "[ERROR] %s: %s: Number of SNE ops exceeded max allowed: %u for procID: %d\n"
```
