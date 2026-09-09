## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

 752.0.0.0.0
-  __TEXT.__text: 0x93904
-  __TEXT.__objc_methlist: 0x9c9c
+  __TEXT.__text: 0x94480
+  __TEXT.__objc_methlist: 0x9cbc
   __TEXT.__const: 0x498
   __TEXT.__dlopen_cstrs: 0x6a1
   __TEXT.__swift5_typeref: 0x196

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x10
-  __TEXT.__cstring: 0x9141
-  __TEXT.__oslogstring: 0x6c4b
-  __TEXT.__gcc_except_tab: 0x186c
+  __TEXT.__cstring: 0x91b0
+  __TEXT.__oslogstring: 0x6d3e
+  __TEXT.__gcc_except_tab: 0x18d0
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2370
+  __TEXT.__unwind_info: 0x2388
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1398
+  __DATA_CONST.__const: 0x13d8
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5680
+  __DATA_CONST.__objc_selrefs: 0x56a8
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __DATA_CONST.__got: 0xac8
+  __DATA_CONST.__got: 0xad8
   __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x86c0
-  __AUTH_CONST.__objc_const: 0x103d0
-  __AUTH_CONST.__objc_intobj: 0x378
+  __AUTH_CONST.__cfstring: 0x87a0
+  __AUTH_CONST.__objc_const: 0x103d8
+  __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x678
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH.__objc_data: 0x1718
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x63c

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3357
-  Symbols:   7602
-  CStrings:  2059
+  Functions: 3363
+  Symbols:   7615
+  CStrings:  2070
 
Symbols:
+ +[SettingsCellularUtils simTypePrefixForLocation:]
+ -[PSUICellularController launchSIMConfigFlowFromURL:]
+ -[PSUITurnOnThisLineSpecifier simSetupFlowCompleted:]
+ GCC_except_table137
+ _TSUserInfoSIMConfigSwitchToEuiccKey
+ ___53-[PSUITurnOnThisLineSpecifier simSetupFlowCompleted:]_block_invoke
+ ___53-[PSUITurnOnThisLineSpecifier simSetupFlowCompleted:]_block_invoke_2
+ ___56-[PSUITurnOnThisLineSpecifier setPlanEnabled:specifier:]_block_invoke
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ _objc_msgSend$isEuiccSimSlotConfigured
+ _objc_msgSend$launchSIMConfigFlowFromURL:
+ _objc_msgSend$simLocation
+ _objc_msgSend$simStatusCache
+ _objc_msgSend$simTypePrefixForLocation:
+ _objc_msgSend$supportsDynamicSIMConfiguration
- GCC_except_table136
- _objc_retain_x7
CStrings:
+ "Back SIM"
+ "DELETE_ESIM_CONFIRMATION_PP_MODE"
+ "Gemini-V63"
+ "Plan is no longer selectable — popping back to the Cellular page"
+ "Plan no longer exists — popping back to the Cellular page"
+ "Presenting SIM config switch flow for %@ plan"
+ "SIM config switch flow did not finish (type %lu) — reverting toggle"
+ "SIM_TYPE_BACK_SIM"
+ "SIM_TYPE_ESIM"
+ "SIM_TYPE_FRONT_SIM"
+ "action"
```
