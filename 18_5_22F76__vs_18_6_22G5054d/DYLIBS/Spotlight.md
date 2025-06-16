## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0x517ac
-  __TEXT.__auth_stubs: 0x1050
-  __TEXT.__objc_methlist: 0x1fec
+2333.55.0.0.0
+  __TEXT.__text: 0x51c3c
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__objc_methlist: 0x1ffc
   __TEXT.__const: 0x180
-  __TEXT.__gcc_except_tab: 0x4b4c
+  __TEXT.__gcc_except_tab: 0x4b94
   __TEXT.__cstring: 0x294f
-  __TEXT.__oslogstring: 0x2526
+  __TEXT.__oslogstring: 0x25f7
   __TEXT.__unwind_info: 0xc18
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x231
-  __TEXT.__objc_methname: 0x9239
+  __TEXT.__objc_methname: 0x9253
   __TEXT.__objc_methtype: 0x1e35
-  __TEXT.__objc_stubs: 0x8940
+  __TEXT.__objc_stubs: 0x8960
   __DATA_CONST.__got: 0x12f8
   __DATA_CONST.__const: 0xbc0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27c8
+  __DATA_CONST.__objc_selrefs: 0x27d0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x3a8
-  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__auth_got: 0x838
   __AUTH_CONST.__const: 0x688
   __AUTH_CONST.__cfstring: 0x2b00
   __AUTH_CONST.__objc_const: 0x3750

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F74FFC4B-8804-3D17-AC51-868C57621A49
-  Functions: 939
-  Symbols:   4646
-  CStrings:  2807
+  UUID: 27A48C09-B01D-372C-A173-7C8716EE8E67
+  Functions: 941
+  Symbols:   4650
+  CStrings:  2813
 
Symbols:
+ -[SPCSSearchQuery skipResult:installedApps:]
+ -[SPCSSearchQuery skipResult:installedApps:].cold.1
+ -[SPCSSearchQuery skipResult:installedApps:].cold.2
+ GCC_except_table23
+ GCC_except_table27
+ ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.669
+ ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.669.cold.1
+ ___block_literal_global.667
+ _objc_msgSend$skipResult:installedApps:
- -[SPCSSearchQuery addSearchResult:withFoundBundleID:].cold.1
- GCC_except_table26
- GCC_except_table30
- __ZN12_GLOBAL__N_113installedAppsEv
- ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.667
- ____ZN12_GLOBAL__N_117updateMailVIPListEv_block_invoke.667.cold.1
- ___block_literal_global.665
- _objc_release_x2
CStrings:
+ "No bundleID for result %@"
+ "Skipping restricted app %@"
+ "Skipping settings %@ for disabled app %@"
+ "Skipping settings %@ for non-installed %@"
+ "Skipping settings %@ for non-installed app %@"
+ "Skipping settings %@ for restricted app %@"
+ "Skipping shortcut %@ for disabled app %@"
+ "Skipping shortcut %@ for restricted app %@"
+ "skipResult:installedApps:"
- "Skipping Settings item for app %@"
- "Skipping for uninstalled %@"
- "Skipping shortcut for disabled app %@"

```
