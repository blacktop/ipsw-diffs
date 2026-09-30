## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

   __TEXT.__const: 0x36
-  __TEXT.__cstring: 0x2bfe
-  __TEXT_EXEC.__text: 0xd61c
+  __TEXT.__cstring: 0x2c0d
+  __TEXT_EXEC.__text: 0xd614
   __TEXT_EXEC.__auth_stubs: 0x4d0
   __DATA.__data: 0x320
   __DATA.__common: 0xe8
   __DATA.__bss: 0x140
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x2170
+  __DATA_CONST.__const: 0x21a0
   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__auth_got: 0x268
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x10
   Functions: 192
   Symbols:   659
-  CStrings:  378
+  CStrings:  381
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Functions:
~ __ZN18AppleDialogSPMIPMU23_resetLpemInRestoreModeEv : 364 -> 368
~ __ZN18AppleDialogSPMIPMU21_updateBootPropertiesEb : 2596 -> 2604
~ __ZN18AppleDialogSPMIPMU17_writeLpemLogDataEv : 516 -> 496
CStrings:
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 23:27:16 Jun 29 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 23:27:16 Jun 29 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 23:27:17 Jun 29 2026\n"
+ "%s::start: %s _pmuNub: %p built 23:27:17 Jun 29 2026\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.8vLtKn/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
+ "B2CA"
+ "B2PD"
+ "B2VT"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 22:21:10 Jun 15 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 22:21:10 Jun 15 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 22:21:11 Jun 15 2026\n"
- "%s::start: %s _pmuNub: %p built 22:21:11 Jun 15 2026\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.K9DP2B/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"

```
