## SymptomEvaluator

> `/System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/SymptomEvaluator.framework/Versions/A/SymptomEvaluator`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.evaluator_cfg`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__data`

```diff

-2385.0.0.0.0
-  __TEXT.__text: 0x1f4a40
-  __TEXT.__objc_methlist: 0x1237c
-  __TEXT.__cstring: 0x1b73f
+2394.0.0.0.0
+  __TEXT.__text: 0x1f4e08
+  __TEXT.__objc_methlist: 0x123bc
+  __TEXT.__cstring: 0x1b76f
   __TEXT.__const: 0xe80
-  __TEXT.__oslogstring: 0x2a9e5
-  __TEXT.__gcc_except_tab: 0x309c
+  __TEXT.__oslogstring: 0x2aa45
+  __TEXT.__gcc_except_tab: 0x30ac
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__swift5_typeref: 0x38d
   __TEXT.__swift5_capture: 0x518

   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x78
   __TEXT.evaluator_cfg: 0x6532
-  __TEXT.__unwind_info: 0x5940
+  __TEXT.__unwind_info: 0x5968
   __TEXT.__eh_frame: 0x7d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2cd8
+  __DATA_CONST.__const: 0x2ce8
   __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9e90
+  __DATA_CONST.__objc_selrefs: 0x9eb8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__got: 0xd08
   __AUTH_CONST.__const: 0x5390
-  __AUTH_CONST.__cfstring: 0x16000
-  __AUTH_CONST.__objc_const: 0x2dad8
+  __AUTH_CONST.__cfstring: 0x16040
+  __AUTH_CONST.__objc_const: 0x2db28
   __AUTH_CONST.__objc_intobj: 0x600
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x13d8
-  __AUTH.__objc_data: 0xef8
+  __AUTH.__objc_data: 0xcc8
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x1f00
-  __DATA.__data: 0x18c0
+  __DATA.__objc_ivar: 0x1f08
+  __DATA.__data: 0x18a0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xf00
+  __DATA.__bss: 0xdc8
   __DATA.__common: 0xa8
-  __DATA_DIRTY.__objc_data: 0x3598
-  __DATA_DIRTY.__data: 0x190
-  __DATA_DIRTY.__bss: 0x1108
+  __DATA_DIRTY.__objc_data: 0x37c8
+  __DATA_DIRTY.__data: 0x1a0
+  __DATA_DIRTY.__bss: 0x1250
   __DATA_DIRTY.__common: 0x1a8
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9434
-  Symbols:   18544
-  CStrings:  8433
+  Functions: 9441
+  Symbols:   18555
+  CStrings:  8436
 
Symbols:
+ -[NoBackhaulHandler _configurePolicyDefaults]
+ -[NoBackhaulHandler _ensureICMPProbeDictionariesAllocated]
+ -[WiFiShim isConnectivityAssistEnabled]
+ -[WiFiStateRelay isConnAssistDisabled]
+ -[WiFiStateRelay setIsConnAssistDisabled:]
+ GCC_except_table147
+ GCC_except_table155
+ GCC_except_table383
+ GCC_except_table50
+ GCC_except_table66
+ OBJC_IVAR_$_NoBackhaulHandler._policyDefaults
+ OBJC_IVAR_$_WiFiStateRelay._isConnAssistDisabled
+ ___38-[WiFiStateRelay isConnAssistDisabled]_block_invoke
+ ___42-[WiFiStateRelay setIsConnAssistDisabled:]_block_invoke
+ _kWiFiShimIsConnectivityAssistEnabled
+ _objc_msgSend$_configurePolicyDefaults
+ _objc_msgSend$_ensureICMPProbeDictionariesAllocated
+ _objc_msgSend$isConnectivityAssistEnabled
+ _objc_msgSend$setIsConnAssistDisabled:
- GCC_except_table110
- GCC_except_table139
- GCC_except_table145
- GCC_except_table149
- GCC_except_table47
- GCC_except_table51
- GCC_except_table54
- GCC_except_table64
CStrings:
+ "dropping upward post (code %llu): handler administratively disabled"
+ "isConnAssistDisabled"
+ "isConnectivityAssistEnabled"
+ "re-setting no_backhaul_rx_recovery_enabled to default: %{BOOL}d"
+ "re-setting no_backhaul_verify_default_gateway to its platform default: %{BOOL}d"
+ "set to a new value for no_backhaul_rx_recovery_enabled (was/is): %{BOOL}d/%{BOOL}d"
+ "set to a new value for no_backhaul_verify_default_gateway behavior (was/is): %{BOOL}d/%{BOOL}d"
- "re-setting no_backhaul_rx_recovery_enabled to default: %d"
- "re-setting no_backhaul_verify_default_gateway to a default behavior: %d"
- "set to a new value for no_backhaul_rx_recovery_enabled (was/is): %d/%d"
- "set to a new value for no_backhaul_verify_default_gateway behavior (was/is): %d/%d"
```
