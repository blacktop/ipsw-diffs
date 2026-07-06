## CoreRepairKit

> `/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit`

```diff

-  __TEXT.__text: 0x1940
+  __TEXT.__text: 0x183c
   __TEXT.__objc_methlist: 0x28c
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x186
-  __TEXT.__oslogstring: 0x2e9
+  __TEXT.__cstring: 0x157
+  __TEXT.__oslogstring: 0x2f2
   __TEXT.__gcc_except_tab: 0x38
   __TEXT.__unwind_info: 0xc0
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x290
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__got: 0x90
-  __AUTH_CONST.__cfstring: 0x220
+  __DATA_CONST.__got: 0x88
+  __AUTH_CONST.__cfstring: 0x1a0
   __AUTH_CONST.__objc_const: 0x4f8
-  __AUTH_CONST.__auth_got: 0x178
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x190
   __DATA.__data: 0x120
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/updaters/libT200Updater.dylib
   Functions: 40
-  Symbols:   83
-  CStrings:  62
+  Symbols:   79
+  CStrings:  54
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _OBJC_CLASS_$_CRBatteryUpdaterFactory
- _BC__getInfo
- _OBJC_CLASS_$_NSMutableDictionary
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_opt_new
Functions:
~ sub_257e2a2e8 -> sub_25c905250 : 492 -> 232
CStrings:
+ "Battery FW version dict: %@"
+ "Failed to get battery FW version info"
- "Configuration"
- "DNVDSector1"
- "DNVDSector2"
- "Failed to get version info for battery"
- "Firmware"
- "versiondict is:%@"

```
