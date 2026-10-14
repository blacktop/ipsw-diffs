## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8160.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__chain_fixups`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__TIGHTBEAM`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__PDATA.__auth_ptr`
- `__PDATA.__const`
- `__PDATA.__data`
- `__PDATA.__shared_cache`

```diff

-1777.40.34.0.0
-  __TEXT.__text: 0xf33e40
+1777.40.37.0.0
+  __TEXT.__text: 0xf369a8
   __TEXT.__lcxx_override: 0xd0
-  __TEXT.__cstring: 0xb5851
-  __TEXT.__const: 0x208314
-  __TEXT.__swift5_typeref: 0x329ba
-  __TEXT.__swift5_reflstr: 0x55368
+  __TEXT.__cstring: 0xb5ce1
+  __TEXT.__const: 0x2084f4
+  __TEXT.__swift5_typeref: 0x329ca
+  __TEXT.__swift5_reflstr: 0x553b8
   __TEXT.__swift5_assocty: 0x10288
-  __TEXT.__swift5_fieldmd: 0x8ef54
-  __TEXT.__constg_swiftt: 0x78c8c
+  __TEXT.__swift5_fieldmd: 0x8efa8
+  __TEXT.__constg_swiftt: 0x78d34
   __TEXT.__swift5_protos: 0x14c0
   __TEXT.__swift5_proto: 0xccec
   __TEXT.__swift5_types: 0x84ac
   __TEXT.__swift5_types2: 0xc4
   __TEXT.__swift5_builtin: 0x2bc0
-  __TEXT.__swift5_capture: 0x3c1c
+  __TEXT.__swift5_capture: 0x3d7c
   __TEXT.__objc_methtype: 0x576
   __TEXT.__swift5_mpenum: 0xdc4
   __TEXT.__swift_as_entry: 0x169c

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x170
-  __TEXT.__eh_frame: 0x83718
+  __TEXT.__eh_frame: 0x83720
   __DATA.__TIGHTBEAM_VT: 0x1530
   __DATA.__TIGHTBEAM: 0x590
-  __DATA.__const: 0x1688a8
-  __DATA.__data: 0x600c8
+  __DATA.__const: 0x1688c0
+  __DATA.__data: 0x60158
   __DATA.__mod_init_func: 0x40
   __DATA.__ENDPOINTS: 0x1bcd7
   __DATA.__auth_ptr: 0xb878

   __DATA_CONST.__mod_term_func: 0x0
   Functions: 1451
   Symbols:   1
-  CStrings:  16856
+  CStrings:  16872
 
Functions:
~ sub_82b12b8 : 1177448 -> 1178564
~ sub_8544800 -> sub_8544c5c : 458584 -> 458672
~ sub_85b6e8c -> sub_85b7340 : 1354448 -> 1358196
~ sub_87f6a94 -> sub_87f7dec : 25612 -> 25980
~ sub_87fcea0 -> sub_87fe368 : 34552 -> 34516
~ sub_8805608 -> sub_8806aac : 916 -> 948
~ sub_880599c -> sub_8806e60 : 1016 -> 1040
~ sub_8805d94 -> sub_8807270 : 664 -> 652
~ sub_880602c -> sub_88074fc : 1160 -> 1176
~ sub_8bf0d5c -> sub_8bf223c : 5776 -> 5792
~ sub_8c0a098 -> sub_8c0b588 : 31104 -> 31240
~ sub_8c1af7c -> sub_8c1c4f4 : 40552 -> 40968
~ sub_8c24e04 -> sub_8c2651c : 44 -> 48
~ sub_8c24e30 -> sub_8c2654c : 44 -> 48
~ sub_8c24e8c -> sub_8c265ac : 48 -> 44
~ sub_8c24ebc -> sub_8c265d8 : 292 -> 288
~ sub_8c250cc -> sub_8c267e4 : 39636 -> 39712
~ sub_8c4a8ec -> sub_8c4c050 : 84832 -> 84828
~ sub_8c5fbb0 -> sub_8c61310 : 613724 -> 618780
~ sub_8d4ac30 -> sub_8d4d750 : 1980996 -> 1981068
CStrings:
+ " lastVerdictAge="
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Thu Oct  8 00:11:07 PDT 2026; root:AppleImage4_exclavecore-374~19439/ExclaveImage4/RELEASE_ARM64E"
+ "ANEExclave version: ANEExclave_exclavecore-13.102.2"
+ "Build Date: Wed Oct  7 23:45:10 PDT 2026"
+ "ExclaveCameraSISP-20.109"
+ "ExclaveOS Image4 Framework Version 7.0.0: Thu Oct  8 00:11:07 PDT 2026; root:AppleImage4_exclavecore-374~19439/ExclaveImage4/RELEASE_ARM64E"
+ "FaceLivelinessFull"
+ "PatchKeypointTracker"
+ "Start not allowed: camera disabled by EDT policy"
+ "Status not allowed: camera disabled by EDT policy"
+ "System/ExclaveKit/System/Library/Frameworks/Vision.framework/faceliveliness_ek_fp16.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/Frameworks/Vision.framework/facelivelinessfull_ek_fp16.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/PrivateFrameworks/ODTL.framework/PhoneTracking/odtl/0/0/PatchKeypointTracker.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/PrivateFrameworks/ODTL.framework/PhoneTracking/odtl/ObjectDetector.bundle/*.bundle/main/main_ane"
+ "System/ExclaveKit/System/Library/PrivateFrameworks/Visage.framework/VGUnifiedLightingH5Models.bundle/img_to_sg_exclave_model.bundle/*.bundle/main/main_ane"
+ "[BrightnessCheck] NOT EVALUATED ("
+ "])\n  deviceStateDisplayWake: allowance="
+ "fpwm-frequency-hz"
+ "policy-sil-disable"
+ "sil-disable-config"
+ "sil-disable-offset"
+ "skipping harvested tunables: ISP HW not powered (state="
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Mon Sep 28 22:45:47 PDT 2026; root:AppleImage4_exclavecore-374~19125/ExclaveImage4/RELEASE_ARM64E"
- "ANEExclave version: ANEExclave_exclavecore-13.102.1"
- "Build Date: Mon Sep 28 22:24:15 PDT 2026"
- "ExclaveCameraSISP-20.106.4"
- "ExclaveOS Image4 Framework Version 7.0.0: Mon Sep 28 22:45:47 PDT 2026; root:AppleImage4_exclavecore-374~19125/ExclaveImage4/RELEASE_ARM64E"
- "])\n  medinaStateDisplayWake: allowance="
```
