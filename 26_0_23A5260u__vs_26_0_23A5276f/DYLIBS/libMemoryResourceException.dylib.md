## libMemoryResourceException.dylib

> `/usr/lib/libMemoryResourceException.dylib`

```diff

-301.0.0.0.0
-  __TEXT.__text: 0x18cc4
-  __TEXT.__auth_stubs: 0xcc0
+305.0.0.0.1
+  __TEXT.__text: 0x18e70
+  __TEXT.__auth_stubs: 0xce0
   __TEXT.__objc_methlist: 0x154c
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x1dc4
-  __TEXT.__oslogstring: 0x9b5
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x1dbe
+  __TEXT.__oslogstring: 0xa7b
   __TEXT.__gcc_except_tab: 0x3cc
   __TEXT.__ustring: 0xd0
   __TEXT.__unwind_info: 0x450

   __DATA_CONST.__objc_selrefs: 0xf20
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__auth_got: 0x680
   __AUTH_CONST.__const: 0x250
   __AUTH_CONST.__cfstring: 0x2720
   __AUTH_CONST.__objc_const: 0x2ea0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8DECBBE5-0A88-3A51-B876-B3BC3015EDE5
+  UUID: 016CD325-F185-37A2-BAD4-7F9817106E75
   Functions: 468
-  Symbols:   310
-  CStrings:  1634
+  Symbols:   312
+  CStrings:  1638
 
Symbols:
+ _MobileGestalt_copy_hwModelDescriptionForPowerPerf_obj
+ _MobileGestalt_get_current_device
Functions:
~ sub_225669cb0 -> sub_225b3ecb0 : 88 -> 516
CStrings:
+ "Failed to get current device from MobileGestalt: %{darwin.errno}d"
+ "Failed to get hwModel from MobileGestalt: %{darwin.errno}d"
+ "Got an empty hwModel string from MobileGestalt"
+ "HWModelStr"
+ "Looking up kMGQHWModelStr"
- "HWModelUniqueStr"

```
