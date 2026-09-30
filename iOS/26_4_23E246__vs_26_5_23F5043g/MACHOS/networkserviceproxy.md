## networkserviceproxy

> `/usr/libexec/networkserviceproxy`

```diff

-921.100.18.0.0
-  __TEXT.__text: 0xc2c6c
+921.120.2.0.0
+  __TEXT.__text: 0xc3094
   __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_stubs: 0xc540
   __TEXT.__objc_methlist: 0x4e74
   __TEXT.__const: 0x275
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__gcc_except_tab: 0x3f08
-  __TEXT.__oslogstring: 0x108cc
-  __TEXT.__cstring: 0xd4a2
+  __TEXT.__oslogstring: 0x10a52
+  __TEXT.__cstring: 0xd4a7
   __TEXT.__objc_methname: 0xf974
   __TEXT.__objc_classname: 0xc81
   __TEXT.__objc_methtype: 0x2a19

   __DATA_CONST.__got: 0x6e8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x20e8
-  __DATA_CONST.__cfstring: 0x8300
+  __DATA_CONST.__cfstring: 0x8320
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xf0

   - /usr/lib/libmrc.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87070E4A-A6FC-307B-9A26-2864D97F2981
+  UUID: D3BEBF77-D6B2-3E49-A9E6-3C74D9478868
   Functions: 2102
   Symbols:   627
-  CStrings:  7128
+  CStrings:  7136
 
Functions:
~ sub_100012d98 : 3124 -> 3224
~ sub_100087998 -> sub_1000879fc : 8904 -> 8972
~ sub_10008cad4 -> sub_10008cb7c : 1080 -> 1556
~ sub_10008cf0c -> sub_10008d190 : 1072 -> 1492
CStrings:
+ "%@ Safari UUID not available, skipping Safari-specific main policies"
+ "%@ failed to create \"Safari App Bundles Private All\" policies"
+ "%@ failed to create \"Safari App Bundles Private Search\" policies"
+ "%@ failed to create \"SafariTechnologyPreview Private All\" policies"
+ "%@ failed to create \"SafariTechnologyPreview Private Search\" policies"
+ "Ignoring proxy match dictionary, not applicable for seed"
+ "Seed"

```
