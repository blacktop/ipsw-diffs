## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-652.2.0.0.0
-  __TEXT.__text: 0x89228
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x8d4c
+652.3.0.0.0
+  __TEXT.__text: 0x89244
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_methlist: 0x8d54
   __TEXT.__const: 0x7c8
   __TEXT.__dlopen_cstrs: 0x649
-  __TEXT.__cstring: 0x810b
+  __TEXT.__cstring: 0x8105
   __TEXT.__constg_swiftt: 0x2c8
   __TEXT.__swift5_typeref: 0x2ae
   __TEXT.__swift5_fieldmd: 0xe8

   __TEXT.__unwind_info: 0x20c0
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x13f6
-  __TEXT.__objc_methname: 0x13aaf
+  __TEXT.__objc_methname: 0x13b04
   __TEXT.__objc_methtype: 0x2972
-  __TEXT.__objc_stubs: 0xda60
-  __DATA_CONST.__got: 0x958
+  __TEXT.__objc_stubs: 0xdac0
+  __DATA_CONST.__got: 0x960
   __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bc0
+  __DATA_CONST.__objc_selrefs: 0x4bd8
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x700
+  __AUTH_CONST.__auth_got: 0x720
   __AUTH_CONST.__const: 0x628
   __AUTH_CONST.__cfstring: 0x6ba0
-  __AUTH_CONST.__objc_const: 0xede8
+  __AUTH_CONST.__objc_const: 0xedc8
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x1c30
   __AUTH.__data: 0x298
-  __DATA.__objc_ivar: 0x5d4
+  __DATA.__objc_ivar: 0x5d0
   __DATA.__data: 0xb38
   __DATA.__bss: 0x7f0
   __DATA_DIRTY.__objc_ivar: 0x504

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 50AE9A85-1AEE-3DAA-B5FB-49D23E0916F2
-  Functions: 3112
-  Symbols:   10187
-  CStrings:  6368
+  UUID: 1B7B2E92-98C4-3855-99EA-0A2C401C447D
+  Functions: 3113
+  Symbols:   10196
+  CStrings:  6371
 
Symbols:
+ +[SettingsCellularUtils satelliteDataPlanTierRequiresUsageFooter]
+ _OBJC_CLASS_$_CTDataConnectionAgentData
+ _nw_path_create_default_evaluator
+ _nw_path_evaluator_cancel
+ _nw_path_evaluator_copy_path
+ _nw_path_evaluator_start
+ _objc_msgSend$dataPlanTier
+ _objc_msgSend$initAgentDataFromInternetPath:
+ _objc_msgSend$satelliteDataPlanTierRequiresUsageFooter
- _OBJC_IVAR_$_PSUISatelliteSubgroup._planItem
Functions:
+ +[SettingsCellularUtils satelliteDataPlanTierRequiresUsageFooter]
~ -[PSUISatelliteSubgroup initWithHostController:context:planReference:mode:] : 432 -> 384
~ -[PSUISatelliteSubgroup setGroupFooterText] : 928 -> 880
~ -[PSUISatelliteSubgroup .cxx_destruct] : 136 -> 124
CStrings:
+ "SATELLITE_USAGE_FOOTER"
+ "dataPlanTier"
+ "initAgentDataFromInternetPath:"
+ "satelliteDataPlanTierRequiresUsageFooter"
- "SATELLITE_USAGE_FOOTER_%@_%@"

```
