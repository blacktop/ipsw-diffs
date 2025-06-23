## com.apple.driver.corecapture

> `com.apple.driver.corecapture`

```diff

-1301.62.0.0.0
-  __TEXT.__os_log: 0x411d
+1301.70.0.0.0
+  __TEXT.__os_log: 0x4234
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x2024
-  __TEXT_EXEC.__text: 0x28938
+  __TEXT.__cstring: 0x202e
+  __TEXT_EXEC.__text: 0x28cd0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc4
   __DATA.__common: 0x308
   __DATA.__bss: 0x294
-  __DATA_CONST.__auth_got: 0x398
-  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__mod_init_func: 0x88
   __DATA_CONST.__mod_term_func: 0x80
   __DATA_CONST.__const: 0x7008
   __DATA_CONST.__kalloc_type: 0x10c0
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: B46183CF-47BF-33DC-9FDB-2735A90E8D3E
+  UUID: 90430CF8-7322-3913-BC70-4AD5D6F63565
   Functions: 874
   Symbols:   0
-  CStrings:  651
+  CStrings:  654
 
Functions:
~ sub_fffffff00aeec920 -> sub_fffffff00af39c60 : 12 -> 28
~ sub_fffffff00aeec92c -> sub_fffffff00af39c7c : 12 -> 28
~ __ZN15CCFaultReporter25SpinDeferredCommonCaptureEv : 360 -> 480
~ __ZN15CCFaultReporter11reportFaultEjPKcjS1_P12OSDictionaryiS1_z : 540 -> 556
~ __ZN9CCLogPipe27updateStreamConsoleLogFlagsEPKcS1_j : 388 -> 452
~ __ZN9CCLogPipe24setStreamConsoleLogLevelEPKc16CCStreamLogLevel : 492 -> 544
~ __ZN9CCLogPipe24setStreamConsoleLogFlagsEPKcy : 340 -> 412
~ __ZN9CCLogPipe17setStreamLogLevelEPKc16CCStreamLogLevel : 492 -> 544
~ __ZN9CCLogPipe20updateStreamLogFlagsEPKcS1_j : 388 -> 452
~ __ZN9CCLogPipe17setStreamLogFlagsEPKcy : 360 -> 420
~ __ZN9CCLogPipe9setPolicyE11CCLogPolicy : 8 -> 144
~ __ZN9CCLogPipe12setPolicyIntE11CCLogPolicy : 756 -> 816
~ __ZN9CCLogPipe9getPolicyEP11CCLogPolicy : 328 -> 392
~ __ZN9CCLogPipe25setWatermarkLevelToNotifyEm : 524 -> 588
~ __ZN9CCLogPipe16setNotifyTimeoutEj : 316 -> 380
CStrings:
+ "%s:%d pipe is stopped\n"
+ "FaultReporter is stopped\n"
+ "setPolicy"

```
