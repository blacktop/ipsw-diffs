## HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

```diff

-331.0.0.0.0
-  __TEXT.__text: 0x18c9c
+331.1.0.0.0
+  __TEXT.__text: 0x18e04
   __TEXT.__auth_stubs: 0x780
   __TEXT.__objc_stubs: 0x3680
-  __TEXT.__objc_methlist: 0x19c0
+  __TEXT.__objc_methlist: 0x19c8
   __TEXT.__const: 0x250
-  __TEXT.__oslogstring: 0x19d3
+  __TEXT.__oslogstring: 0x1a81
   __TEXT.__cstring: 0x2b34
-  __TEXT.__objc_classname: 0x2c7
-  __TEXT.__objc_methname: 0x6c32
+  __TEXT.__objc_classname: 0x2c8
+  __TEXT.__objc_methname: 0x6c4c
   __TEXT.__objc_methtype: 0xd95
   __TEXT.__gcc_except_tab: 0x2dc
   __TEXT.__unwind_info: 0x678

   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x44e0
+  __DATA.__objc_const: 0x4500
   __DATA.__objc_selrefs: 0x1400
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_ivar: 0x394
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x450
   __DATA.__bss: 0x268

   - /usr/lib/libobjc.A.dylib
   Functions: 764
   Symbols:   200
-  CStrings:  1944
+  CStrings:  1947
 
CStrings:
+ " Avoided redundant hud line clear and render context invalidation."
+ "\x01\x15D"
+ " Invalid HUD line clear request found. The number of HUD lines is 0."
+ "cachedTopMargin is set to %!f(MISSING) where DisplayScale is %!f(MISSING). The orientation is %!@(MISSING)"
+ "_hud_clear_lock"
+ "hasHudRenderContextInvalidated"
- "hangtracer HUD context is invalidated."
- "\x06D"
- "invalidateHUDContext"

```
