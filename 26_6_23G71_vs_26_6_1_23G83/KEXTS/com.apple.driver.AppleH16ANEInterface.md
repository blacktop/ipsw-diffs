## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

 9.512.0.0.0
   __TEXT.__const: 0xd10
   __TEXT.__cstring: 0x113dc
-  __TEXT.__os_log: 0x372d5
-  __TEXT_EXEC.__text: 0x10a730
+  __TEXT.__os_log: 0x37320
+  __TEXT_EXEC.__text: 0x10a810
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4838
   __DATA.__common: 0x680

   __DATA_CONST.__kalloc_var: 0x3200
   Functions: 3577
   Symbols:   0
-  CStrings:  4485
+  CStrings:  4486
 
Functions:
~ __ZN24ANEProgramLegacyResource10preProcessEP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParamsP26ANEProgramCreateArgsOutput : 3880 -> 3924
~ __ZN24ANEProgramLegacyResource24programLoadFromMachoFileEP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParams : 9424 -> 9460
~ __ZN24ANEProgramLegacyResource25initMutableKernelSectionsEP26ANEProgramCreateArgsOutputP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParams : 2484 -> 2476
~ __ZN24ANEProgramLegacyResource34populateProcedureMutableKernelInfoEP26ANEProgramCreateArgsOutputj : 820 -> 824
~ __ZN24ANEProgramLegacyResource29populateProcedureLiveInParamsEP26ANEProgramCreateArgsOutputj : 3068 -> 3216
CStrings:
+ "[ERROR] %s: %s: Number of SNE ops exceeded max allowed: %u for procID: %d\n"
```
