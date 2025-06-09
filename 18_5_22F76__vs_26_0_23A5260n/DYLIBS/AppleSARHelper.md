## AppleSARHelper

> `/System/Library/PrivateFrameworks/AppleSARHelper.framework/AppleSARHelper`

```diff

-1249.1.0.0.0
-  __TEXT.__text: 0x176c
-  __TEXT.__auth_stubs: 0x320
+1371.0.1.0.0
+  __TEXT.__text: 0x1b30
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__const: 0xeb
-  __TEXT.__cstring: 0x3e1
-  __TEXT.__gcc_except_tab: 0x15c
-  __TEXT.__oslogstring: 0x1c2
-  __TEXT.__unwind_info: 0x160
-  __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x230
-  __AUTH_CONST.__auth_got: 0x198
-  __AUTH_CONST.__const: 0xd0
+  __TEXT.__cstring: 0x51f
+  __TEXT.__gcc_except_tab: 0x138
+  __TEXT.__oslogstring: 0x1cc
+  __TEXT.__unwind_info: 0x158
+  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__const: 0x2c0
+  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__const: 0xc0
   __DATA.__bss: 0x400
-  __DATA_DIRTY.__bss: 0x70
+  __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: C62E25E8-9342-3505-B561-82EAA55AEDA6
-  Functions: 40
-  Symbols:   148
-  CStrings:  87
+  UUID: FEDE795D-B820-3A88-9329-1BA492680379
+  Functions: 42
+  Symbols:   142
+  CStrings:  109
 
Symbols:
+ GCC_except_table14
+ GCC_except_table25
+ GCC_except_table7
+ GCC_except_table8
+ GCC_except_table9
+ __ZN3sar8toStringENS_10DataActionE
+ __ZN3sar8toStringENS_11ProductTypeE
+ __ZN3sar8toStringENS_14SARRequestTypeE
+ __ZN3sar8toStringENS_20CellularSARBoostModeE
+ __ZN3sar8toStringENS_7SARModeE
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrI14AppleSARHelperNS_14default_deleteIS1_EEED2B8ne200100Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__16vectorIN8dispatch8callbackIU13block_pointerFvN3sar19AppleSARMessageTypeEPvEEENS_9allocatorIS8_EEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__16vectorIN8dispatch8callbackIU13block_pointerFvN3sar19AppleSARMessageTypeEPvEEENS_9allocatorIS8_EEED2B8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ____ZL16sGetOsLogContextv_block_invoke
+ ___block_descriptor_tmp.10
- GCC_except_table13
- GCC_except_table23
- GCC_except_table5
- __Z15GetGlobalLoggerNSt3__110shared_ptrIN3ctu9LogServerEEE
- __ZN3ctu12OsLogContextC1ERKS0_
- __ZN3ctu12StaticLoggerC1ENS_12OsLogContextERKNSt3__110shared_ptrINS_9LogServerEEE
- __ZN3ctu12StaticLoggerC1Ev
- __ZN3ctu12StaticLoggerD1Ev
- __ZN3ctu16LoggerCommonBaseaSERKS0_
- __ZNKSt3__16vectorIN8dispatch8callbackIU13block_pointerFvN3sar19AppleSARMessageTypeEPvEEENS_9allocatorIS8_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110unique_ptrI14AppleSARHelperNS_14default_deleteIS1_EEED1B8ne190102Ev
- __ZNSt3__119__shared_weak_count14__release_weakEv
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__16vectorIN8dispatch8callbackIU13block_pointerFvN3sar19AppleSARMessageTypeEPvEEENS_9allocatorIS8_EEED1B8ne190102Ev
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- ____Z15GetGlobalLoggerNSt3__110shared_ptrIN3ctu9LogServerEEE_block_invoke
- ___block_descriptor_tmp.3
- ___copy_helper_block_e8_32c42_ZTSNSt3__110shared_ptrIN3ctu9LogServerEEE
- ___cxa_atexit
- ___cxa_guard_abort
- ___destroy_helper_block_e8_32c42_ZTSNSt3__110shared_ptrIN3ctu9LogServerEEE
CStrings:
+ "Clear Override"
+ "Connection has not been established yet!"
+ "Dynamic"
+ "Failed to creat IO notification port for %s"
+ "Failed to create notification queue for %s"
+ "Failed to create the service!"
+ "Failed to get SPMI tracking list (ret = %d)"
+ "Failed to get the connection (ret = %d)"
+ "Failed to release the service!"
+ "Failed to run the command for selector %d (0x%x) (ret = %d)"
+ "Failed to setup callback (ret = %d)"
+ "Get"
+ "Legacy"
+ "MPE"
+ "No Table"
+ "Override"
+ "Product Type 1"
+ "Product Type 2"
+ "Product Type 3"
+ "SAR"
+ "SAR Boost always"
+ "SAR Boost default"
+ "SAR Boost disabled"
+ "SAR Boost during AP sleep"
+ "SAR Boost during WRM crash"
+ "SAR Boost durng BB crash"
+ "Set"
+ "Unknown Data Action"
+ "Unknown SAR Boost Mode"
+ "Unknown SAR Limit Type"
+ "sar.helper"
- "Connection has not established yet!"
- "Failed to create a queue for the notification for %s"
- "Failed to create service!"
- "Failed to find the notification for %s"
- "Failed to get SPMI Tracking List (ret: 0x%x)"
- "Failed to get the connection. ret: %u"
- "Failed to relase the service!"
- "Failed to run the command for %d (0x%x): result: 0x%x"
- "Failed to setup callback: (ret: 0x%x)"

```
