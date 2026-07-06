## CoreRepairKit

> `/System/Library/PrivateFrameworks/CoreRepairKit.framework/Versions/A/CoreRepairKit`

```diff

-  __TEXT.__text: 0x12c4
+  __TEXT.__text: 0x11bc
   __TEXT.__objc_methlist: 0x118
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x18b
-  __TEXT.__oslogstring: 0x17b
+  __TEXT.__cstring: 0x15c
+  __TEXT.__oslogstring: 0x184
   __TEXT.__gcc_except_tab: 0x38
   __TEXT.__unwind_info: 0xc8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1a0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__got: 0x78
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x240
+  __AUTH_CONST.__cfstring: 0x1c0
   __AUTH_CONST.__objc_const: 0x260
-  __AUTH_CONST.__auth_got: 0xa8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__data: 0x60
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/updaters/libT200Updater.dylib
   Functions: 32
-  Symbols:   51
-  CStrings:  50
+  Symbols:   47
+  CStrings:  42
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__const : content changed
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
~ sub_236b3d394 -> sub_2376de2fc : 512 -> 248
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
