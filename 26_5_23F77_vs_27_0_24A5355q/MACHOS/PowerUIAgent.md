## PowerUIAgent

> `/usr/libexec/PowerUIAgent`

```diff

-702.122.1.0.0
-  __TEXT.__text: 0x858
-  __TEXT.__auth_stubs: 0x220
-  __TEXT.__objc_stubs: 0x240
+752.0.0.0.0
+  __TEXT.__text: 0x828
+  __TEXT.__auth_stubs: 0x240
+  __TEXT.__objc_stubs: 0x260
   __TEXT.__const: 0x10
-  __TEXT.__cstring: 0x21b
+  __TEXT.__cstring: 0x211
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__objc_methname: 0x16c
-  __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x118
-  __DATA_CONST.__got: 0x98
+  __TEXT.__objc_methname: 0x173
+  __TEXT.__unwind_info: 0x78
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x90
+  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__got: 0x90
+  __DATA.__objc_selrefs: 0x98
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B57F2456-F624-35DA-9F19-F482C6BB4D98
+  UUID: FC14B10C-AF80-348E-B46A-F06EE014D260
   Functions: 6
-  Symbols:   58
+  Symbols:   59
   CStrings:  46
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release
+ _objc_retain_x1
+ _objc_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_100000b38 : 420 -> 380
~ sub_100000cdc -> sub_100000cb4 : 1176 -> 1096
~ sub_100001174 -> sub_1000010fc : 16 -> 92
~ sub_100001224 -> sub_1000011f8 : 364 -> 360
CStrings:
+ "isiPad"
- "chargeRec"

```
