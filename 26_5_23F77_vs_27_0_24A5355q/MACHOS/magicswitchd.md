## magicswitchd

> `/usr/libexec/magicswitchd`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0xc124
-  __TEXT.__auth_stubs: 0x580
+43.0.0.0.0
+  __TEXT.__text: 0xad74
+  __TEXT.__auth_stubs: 0x5d0
   __TEXT.__objc_stubs: 0x1560
   __TEXT.__objc_methlist: 0x13c0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x4f9
+  __TEXT.__cstring: 0x523
   __TEXT.__objc_methname: 0x2e2d
   __TEXT.__oslogstring: 0x1f5e
-  __TEXT.__objc_classname: 0x2f1
+  __TEXT.__objc_classname: 0x2c7
   __TEXT.__objc_methtype: 0x9dc
-  __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__unwind_info: 0x478
-  __DATA_CONST.__auth_got: 0x2d0
-  __DATA_CONST.__got: 0x198
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__unwind_info: 0x378
   __DATA_CONST.__const: 0x2a8
   __DATA_CONST.__cfstring: 0x300
   __DATA_CONST.__objc_classlist: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_intobj: 0x18
+  __DATA_CONST.__auth_got: 0x2f8
+  __DATA_CONST.__got: 0x198
   __DATA.__objc_const: 0x3d10
   __DATA.__objc_selrefs: 0xad0
   __DATA.__objc_ivar: 0x15c

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 420D70DC-5600-3BC7-8734-27A3094F1738
+  UUID: 9117B346-BB1E-3FEB-B187-D7ACB7207306
   Functions: 351
-  Symbols:   147
+  Symbols:   152
   CStrings:  878
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_release_x10
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "MagicSwitchEnabler --- Launching; \"MagicSwitch-43\" \"1060\""
- "MagicSwitchEnabler --- Launching; \"MagicSwitch-40\" \"9023\""

```
