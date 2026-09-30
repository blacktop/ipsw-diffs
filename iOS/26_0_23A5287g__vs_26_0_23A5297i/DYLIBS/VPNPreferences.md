## VPNPreferences

> `/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences`

```diff

-368.0.0.0.0
-  __TEXT.__text: 0x26054
+369.0.0.0.0
+  __TEXT.__text: 0x26254
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x2584
+  __TEXT.__objc_methlist: 0x258c
   __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__cstring: 0x1350
+  __TEXT.__cstring: 0x13b8
   __TEXT.__const: 0xa0
   __TEXT.__oslogstring: 0x1a4
-  __TEXT.__unwind_info: 0x5c0
+  __TEXT.__unwind_info: 0x5c8
   __TEXT.__objc_classname: 0x211
-  __TEXT.__objc_methname: 0x6d6e
+  __TEXT.__objc_methname: 0x6d98
   __TEXT.__objc_methtype: 0xd54
-  __TEXT.__objc_stubs: 0x5720
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x580
+  __TEXT.__objc_stubs: 0x5760
+  __DATA_CONST.__got: 0x3c0
+  __DATA_CONST.__const: 0x5a0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c60
+  __DATA_CONST.__objc_selrefs: 0x1c70
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x21a0
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x21c0
   __AUTH_CONST.__objc_const: 0x31f0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH.__objc_data: 0x550

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6B202DB8-0FD1-30DF-A2E3-0154E0F2D58E
-  Functions: 759
-  Symbols:   2921
-  CStrings:  1962
+  UUID: FF93E0E1-46AE-38A7-B208-2CDFBB379CD3
+  Functions: 761
+  Symbols:   2930
+  CStrings:  1967
 
Symbols:
+ -[VPNConnectionStore isMDM:]
+ _OBJC_CLASS_$_NEURLFilterManagerPrivate
+ ___52-[URLFilterController setURLFilterActive:specifier:]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ _objc_msgSend$enableConfig:serviceID:completion:
+ _objc_msgSend$isMDM:
Functions:
+ -[VPNConnectionStore isMDM:]
~ -[URLFilterController setURLFilterActive:specifier:] : 232 -> 308
+ ___52-[URLFilterController setURLFilterActive:specifier:]_block_invoke
CStrings:
+ "%s: Failed to setURLFilterActive - %@"
+ "-[URLFilterController setURLFilterActive:specifier:]_block_invoke"
+ "enableConfig:serviceID:completion:"
+ "isMDM:"

```
