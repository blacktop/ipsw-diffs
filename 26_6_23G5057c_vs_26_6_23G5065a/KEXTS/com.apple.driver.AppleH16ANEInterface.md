## com.apple.driver.AppleH16ANEInterface

> `com.apple.driver.AppleH16ANEInterface`

```diff

   __TEXT.__const: 0xd10
   __TEXT.__cstring: 0x113dc
-  __TEXT.__os_log: 0x37320
-  __TEXT_EXEC.__text: 0x10a810
+  __TEXT.__os_log: 0x372d5
+  __TEXT_EXEC.__text: 0x10a730
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4838
   __DATA.__common: 0x680

   __DATA_CONST.__kalloc_var: 0x3200
   Functions: 3577
   Symbols:   0
-  CStrings:  4489
+  CStrings:  4488
 
Sections:
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
Functions:
~ __ZN24ANEProgramLegacyResource10preProcessEP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParamsP26ANEProgramCreateArgsOutput : 3924 -> 3880
~ __ZN24ANEProgramLegacyResource24programLoadFromMachoFileEP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParams : 9460 -> 9424
~ __ZN24ANEProgramLegacyResource25initMutableKernelSectionsEP26ANEProgramCreateArgsOutputP20ANEProgramCreateArgsP32ANEProgramCreateAdditionalParams : 2476 -> 2484
~ __ZN24ANEProgramLegacyResource34populateProcedureMutableKernelInfoEP26ANEProgramCreateArgsOutputj : 824 -> 820
~ __ZN24ANEProgramLegacyResource29populateProcedureLiveInParamsEP26ANEProgramCreateArgsOutputj : 3216 -> 3068
CStrings:
- "[ERROR] %s: %s: Number of SNE ops exceeded max allowed: %u for procID: %d\n"

```
