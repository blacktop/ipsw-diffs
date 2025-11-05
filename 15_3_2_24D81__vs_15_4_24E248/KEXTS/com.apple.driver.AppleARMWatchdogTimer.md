## com.apple.driver.AppleARMWatchdogTimer

> `com.apple.driver.AppleARMWatchdogTimer`

```diff

-277.80.2.0.0
-  __TEXT.__cstring: 0x14bc
-  __TEXT_EXEC.__text: 0x5ac0
+299.100.5.0.0
+  __TEXT.__cstring: 0x152a
+  __TEXT_EXEC.__text: 0x5c90
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x118
   __DATA.__common: 0xe8

   __DATA_CONST.__const: 0x2268
   __DATA_CONST.__kalloc_type: 0x100
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: E967D87A-28D3-32FA-8A3E-E5E55F622585
-  Functions: 192
+  UUID: 76E7361D-05BC-3F14-9F32-93F043E32951
+  Functions: 191
   Symbols:   688
-  CStrings:  139
+  CStrings:  141
 
Functions:
~ __ZN21AppleARMWatchdogTimer5startEP9IOService : 4884 -> 5000
~ __ZN21AppleARMWatchdogTimer20_handlePEHaltRestartEj : 728 -> 740
~ __ZN21AppleARMWatchdogTimer14setPMUVariableEPKcj : 308 -> 352
~ __ZN21AppleARMWatchdogTimer32enableReconfigWatchdogMonitoringEv : 256 -> 260
~ __ZN21AppleARMWatchdogTimer28enableAONWatchdogForReconfigEv : 192 -> 196
~ __ZN21AppleARMWatchdogTimer16enableAPWatchdogEv : 312 -> 372
~ __ZN21AppleARMWatchdogTimer29disableAONWatchdogForReconfigEv : 72 -> 76
~ __ZN21AppleARMWatchdogTimer29enablePanicLongPeriodWatchdogEv : 396 -> 408
~ __ZN21AppleARMWatchdogTimer19extendPanicWatchdogEv : 228 -> 272
~ __ZN21AppleARMWatchdogTimer29_writeApWatchdogConfigurationEv : 116 -> 120
~ __ZN21AppleARMWatchdogTimer14extendWatchdogEv : 60 -> 64
~ __ZN21AppleARMWatchdogTimer14enableWatchdogEv : 204 -> 208
~ __ZN21AppleARMWatchdogTimer15disableWatchdogEv : 172 -> 176
~ __ZN21AppleARMWatchdogTimer17_readLogicalReg32Eyy : 12 -> 16
~ __ZL11_dtReadpropPK13OpaqueDTEntryPKcPy : 184 -> 160
- sub_fffffe000913eeb0
~ __ZN20IOWatchdogUserClient11clientCloseEv : 96 -> 104
~ __ZN37AppleARMWatchdogTimerHibernateHandler4openEjP18IOMemoryDescriptor : 40 -> 52
~ __ZN37AppleARMWatchdogTimerHibernateHandler5closeEj : 84 -> 96
~ __ZN37AppleARMWatchdogTimerHibernateHandler12checkForWorkEv : 40 -> 52
~ __ZN10IOWatchdog5startEP9IOServiceyy : 1536 -> 1580
~ __ZN10IOWatchdog20handle_defang_sysctlEP10sysctl_oidPviP10sysctl_req : 256 -> 260
~ __ZN10IOWatchdog13checkWatchdogEv : 232 -> 236
~ __ZN10IOWatchdog21shutdownCheckWatchdogEy : 364 -> 380
~ __ZN10IOWatchdog13newUserClientEP4taskPvjP12OSDictionaryPP12IOUserClient : 572 -> 640
~ __ZN10IOWatchdog36userspaceReenableUserspaceMonitoringEP8OSObjectPvP25IOExternalMethodArguments : 168 -> 172
~ __ZN10IOWatchdog36userspaceCheckIOKitMonitoringEnabledEP8OSObjectPvP25IOExternalMethodArguments : 128 -> 136
~ __ZN10IOWatchdog35toggleUserSpaceMonitoringWithReasonEjPKc : 156 -> 164
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.2 : 96 -> 44
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.3 : 96 -> 44
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.4 : 52 -> 44
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.5 : 44 -> 104
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.6 : 44 -> 96
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.7 : 44 -> 96
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.8 : 96 -> 52
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.11 : 52 -> 96
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.12 : 96 -> 44
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.13 : 96 -> 44
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.14 : 96 -> 44
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.16 : 104 -> 96
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.17 : 44 -> 52
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.18 : 44 -> 96
~ _ZN21AppleARMWatchdogTimer5startEP9IOService.cold.19 : 44 -> 96
~ _ZN21AppleARMWatchdogTimer20_handlePEHaltRestartEj.cold.1 : 44 -> 60
~ _ZN21AppleARMWatchdogTimer20_handlePEHaltRestartEj.cold.2 : 60 -> 44
~ _ZN10IOWatchdog13checkWatchdogEv.cold.1 : 132 -> 108
~ _ZN10IOWatchdog13checkWatchdogEv.cold.2 : 108 -> 132
CStrings:
+ "AP Watchdog enabled in panic flow (%llu secs)\n"
+ "AP Watchdog extended in panic flow by (%llu secs)\n"
+ "System Watchdog enabled in panic flow (%llu secs)\n"
+ "System Watchdog extended in panic flow by (%llu secs)\n"
- "AP Watchdog enabled in panic flow (%d secs)\n"
- "System Watchdog enabled in panic flow (%d secs)\n"

```
