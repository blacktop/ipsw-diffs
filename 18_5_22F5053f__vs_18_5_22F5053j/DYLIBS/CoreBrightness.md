## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-1902.120.20.0.0
-  __TEXT.__text: 0x1aa2b4
+1902.120.21.0.1
+  __TEXT.__text: 0x1aa718
   __TEXT.__auth_stubs: 0x1590
-  __TEXT.__objc_methlist: 0x8004
+  __TEXT.__objc_methlist: 0x801c
   __TEXT.__cstring: 0x9708
   __TEXT.__const: 0x10a60
-  __TEXT.__oslogstring: 0x147ae
+  __TEXT.__oslogstring: 0x1481b
   __TEXT.__gcc_except_tab: 0x20fc
   __TEXT.__dlopen_cstrs: 0x1d5
   __TEXT.__unwind_info: 0x2fd0
   __TEXT.__objc_classname: 0xb38
-  __TEXT.__objc_methname: 0x11de0
-  __TEXT.__objc_methtype: 0x4171
-  __TEXT.__objc_stubs: 0xd3a0
+  __TEXT.__objc_methname: 0x11e2d
+  __TEXT.__objc_methtype: 0x4190
+  __TEXT.__objc_stubs: 0xd3e0
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__const: 0x22b8
   __DATA_CONST.__objc_classlist: 0x430
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3fb0
+  __DATA_CONST.__objc_selrefs: 0x3fc0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x7a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4846
-  Symbols:   15305
-  CStrings:  7735
+  Functions: 4849
+  Symbols:   15313
+  CStrings:  7739
 
Symbols:
+ -[CBIndicatorBrightnessModule updateMaxContrastBoostedBrightness:]
+ -[CBIndicatorBrightnessModule updateMaxContrastBoostedBrightnessGated:]
+ ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.312
+ ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke.23
+ ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke.29
+ ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke_2.30
+ ___54-[CBIndicatorBrightnessModule startMonitoringForRTPLC]_block_invoke.60
+ ___66-[CBIndicatorBrightnessModule updateMaxContrastBoostedBrightness:]_block_invoke
+ ___block_literal_global.86
+ _objc_msgSend$updateMaxContrastBoostedBrightness:
+ _objc_msgSend$updateMaxContrastBoostedBrightnessGated:
- ___52-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:]_block_invoke.308
- ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke.24
- ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke_2.25
- ___53-[CBDisplayModuleiOS initWithBacklight:queue:brtCtl:]_block_invoke_3
- ___54-[CBIndicatorBrightnessModule startMonitoringForRTPLC]_block_invoke.59
- ___block_literal_global.81
CStrings:
+ "Could not fetch the minimum panel nits!"
+ "[updateMaxContrastBoostedBrightness] maxContrastBoostedBrightness=%f"
+ "updateMaxContrastBoostedBrightness:"
+ "updateMaxContrastBoostedBrightnessGated:"
+ "{?=\"maxContrastBoostedBrightness\"f\"sdrBrightness\"f\"appliedHeadroom\"f\"minimumIndicatorBrightness\"f\"lux\"f\"rtplc\"{?=\"cap\"f\"applied\"B}\"hasEDR\"B\"silEnabled\"B\"dirty\"B}"
- "{?=\"sdrBrightness\"f\"appliedHeadroom\"f\"minimumIndicatorBrightness\"f\"lux\"f\"rtplc\"{?=\"cap\"f\"applied\"B}\"hasEDR\"B\"silEnabled\"B\"dirty\"B}"

```
