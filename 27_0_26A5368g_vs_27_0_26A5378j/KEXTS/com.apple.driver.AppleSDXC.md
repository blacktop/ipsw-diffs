## com.apple.driver.AppleSDXC

> `com.apple.driver.AppleSDXC`

```diff

-  __TEXT.__cstring: 0x26ff
-  __TEXT.__os_log: 0x1f0b
+  __TEXT.__cstring: 0x2728
+  __TEXT.__os_log: 0x2035
   __TEXT.__const: 0x5f0
-  __TEXT_EXEC.__text: 0x23110
+  __TEXT_EXEC.__text: 0x235bc
   __TEXT_EXEC.__auth_stubs: 0x670
   __DATA.__data: 0x118
   __DATA.__common: 0x108

   __DATA_CONST.__kalloc_type: 0x180
   __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0xe0
-  Functions: 697
-  Symbols:   1444
-  CStrings:  561
+  Functions: 700
+  Symbols:   1454
+  CStrings:  570
 
Sections:
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
Symbols:
+ __ZN13AppleSDXCSlot14DisableSDClockEv
+ __ZN13AppleSDXCSlot18IsInjectionAllowedEv
+ __ZZN13AppleSDXCSlot12SwitchTo1_8VEvE11_os_log_fmt_0
+ __ZZN13AppleSDXCSlot13UHSModeChangeEjE11_os_log_fmt_3
+ __ZZN13AppleSDXCSlot14DisableSDClockEvE11_os_log_fmt
+ __ZZN13AppleSDXCSlot14DisableSDClockEvE11_os_log_fmt_0
+ __ZZN13AppleSDXCSlot6Read32EjPjE11_os_log_fmt
+ __ZZN13AppleSDXCSlot6Read64EyPyE11_os_log_fmt
+ __ZZN13AppleSDXCSlot9BigRead32EjPjE11_os_log_fmt
Functions:
~ __ZN13AppleSDXCSlot6Read32EjPj : 152 -> 260
~ __ZN13AppleSDXCSlot15HandleInterruptEP22IOInterruptEventSourcei : 3076 -> 3072
~ __ZN13AppleSDXCSlot6Read64EyPy : 164 -> 276
~ __ZN13AppleSDXCSlot9BigRead32EjPj : 156 -> 264
~ __ZN13AppleSDXCSlot18StepDownClockSpeedEv : 1000 -> 960
+ __ZN13AppleSDXCSlot14DisableSDClockEv
~ __ZN13AppleSDXCSlot17ForceAutoCMDErrorEj : 568 -> 564
+ __ZN13AppleSDXCSlot18IsInjectionAllowedEv
~ _OUTLINED_FUNCTION_52 : 36 -> 12
~ _OUTLINED_FUNCTION_53 : 12 -> 28
~ _OUTLINED_FUNCTION_54 : 28 -> 16
~ _OUTLINED_FUNCTION_56 : 16 -> 24
~ _OUTLINED_FUNCTION_60 : 24 -> 12
~ _OUTLINED_FUNCTION_80 : 16 -> 60
~ _OUTLINED_FUNCTION_81 : 60 -> 16
~ _OUTLINED_FUNCTION_102 : 12 -> 28
~ _OUTLINED_FUNCTION_104 : 28 -> 12
~ _OUTLINED_FUNCTION_109 : 32 -> 24
~ _OUTLINED_FUNCTION_110 : 24 -> 32
~ _OUTLINED_FUNCTION_115 : 44 -> 28
~ _OUTLINED_FUNCTION_117 : 28 -> 44
~ _OUTLINED_FUNCTION_120 : 12 -> 28
~ _OUTLINED_FUNCTION_141 : 12 -> 24
~ _OUTLINED_FUNCTION_142 : 24 -> 12
~ _OUTLINED_FUNCTION_159 : 28 -> 24
~ _OUTLINED_FUNCTION_162 : 24 -> 28
~ _OUTLINED_FUNCTION_164 : 28 -> 24
~ _OUTLINED_FUNCTION_166 : 24 -> 12
~ _OUTLINED_FUNCTION_167 : 20 -> 12
~ _OUTLINED_FUNCTION_172 : 12 -> 20
~ _OUTLINED_FUNCTION_174 : 20 -> 12
~ _OUTLINED_FUNCTION_175 : 12 -> 20
~ _OUTLINED_FUNCTION_177 : 20 -> 12
~ _OUTLINED_FUNCTION_179 : 12 -> 20
~ _OUTLINED_FUNCTION_181 : 20 -> 12
~ _OUTLINED_FUNCTION_191 : 12 -> 20
~ __ZN13AppleSDXCSlot24SetGL9755DrivingStrengthEh : 1252 -> 1328
~ __ZN13AppleSDXCSlot11ThreadEntryEv : 1288 -> 1264
~ __ZN13AppleSDXCSlot22PrepareSlotForNewMediaEb : 232 -> 248
~ __ZN13AppleSDXCSlot15FilterInterruptEP28IOFilterInterruptEventSource : 252 -> 256
~ __ZN13AppleSDXCSlot13ConfigureCardEv : 1888 -> 1872
~ __ZN13AppleSDXCSlot20SetClockSpeedDivisorEt : 476 -> 504
~ __ZN13AppleSDXCSlot16ConfigureSDMediaEv : 1364 -> 1356
~ __ZN13AppleSDXCSlot17ConfigureMMCMediaEv : 536 -> 532
~ __ZN13AppleSDXCSlot12SwitchTo1_8VEv : 800 -> 1104
~ __ZN13AppleSDXCSlot22ConfigureSDMediaUHSTwoEv : 1376 -> 1388
~ __ZN13AppleSDXCSlot23EnableHighSpeedHostModeEv : 568 -> 584
~ __ZN13AppleSDXCSlot13UHSModeChangeEj : 744 -> 840
~ __ZN13AppleSDXCSlot19ForceErrorInterruptEj : 432 -> 428
~ __ZN13AppleSDXCSlot24ForceUHSIIErrorInterruptEj : 516 -> 520
~ _ZN13AppleSDXCSlot18StepDownClockSpeedEv.cold.2 : 164 -> 84
+ _ZN13AppleSDXCSlot18StepDownClockSpeedEv.cold.3
CStrings:
+ "%s:  Rd16 Failure vIDdID=0x%x Value=0x%x\n "
+ "%s:  Rd32 Failure vIDdID=0x%x Value=0x%x\n "
+ "%s:  bRd32 Failure vIDdID=0x%x Value=0x%x\n "
+ "%s: DisableSDClock: clockControl=0x%x presentState=0x%x\n"
+ "%s: UHSModeChange: draining block I/O queue before power cycle\n"
+ "%s: clk invert failed\n"
+ "%s: clk invert failed \n"
+ "gl9755-reg_60-cl-uhs2"
+ "sdxc-reg60-cl_uhs2"

```
