## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-  __TEXT.__text: 0x6da78
+  __TEXT.__text: 0x6db20
   __TEXT.__auth_stubs: 0x1d60
   __TEXT.__objc_stubs: 0x4480
   __TEXT.__objc_methlist: 0x1dbc
   __TEXT.__const: 0x360
-  __TEXT.__cstring: 0x7a0e
+  __TEXT.__cstring: 0x7a77
   __TEXT.__objc_methname: 0x5c5c
-  __TEXT.__oslogstring: 0xbd1c
+  __TEXT.__oslogstring: 0xbcf4
   __TEXT.__objc_classname: 0x2a8
   __TEXT.__objc_methtype: 0x7b1
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__dlopen_cstrs: 0x152
   __TEXT.__unwind_info: 0x13b0
   __DATA_CONST.__const: 0x2570
-  __DATA_CONST.__cfstring: 0x6ac0
+  __DATA_CONST.__cfstring: 0x6b20
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x348
   __DATA_CONST.__auth_got: 0xec0
-  __DATA_CONST.__got: 0x338
+  __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x3648
   __DATA.__objc_selrefs: 0x16c0
   __DATA.__objc_ivar: 0x2b8
   __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x8f8
-  __DATA.__bss: 0xf20
-  __DATA.__common: 0x11d0
+  __DATA.__bss: 0xf28
+  __DATA.__common: 0x1270
   __CGPreLoginApp.__cgpreloginapp: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration

   - /usr/lib/libsystemstats.dylib
   Functions: 2326
   Symbols:   589
-  CStrings:  4559
+  CStrings:  4564
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Functions:
~ sub_10001df60 : 1208 -> 1200
~ sub_10002ceb8 -> sub_10002ceb0 : 2904 -> 2964
~ sub_10002e360 -> sub_10002e394 : 680 -> 724
~ sub_100034110 -> sub_100034170 : 2612 -> 2700
~ sub_100034b44 -> sub_100034bfc : 84 -> 88
~ sub_100039d1c -> sub_100039dd8 : 64 -> 68
~ sub_10003ca50 -> sub_10003cb10 : 636 -> 644
~ sub_10003f4b0 -> sub_10003f578 : 96 -> 92
~ sub_10004aa90 -> sub_10004ab54 : 400 -> 336
~ sub_100057f58 -> sub_100057fdc : 508 -> 544
CStrings:
+ "No battery pack slots. Can't start BDC"
+ "PreventSystemSleepSecurityIndicator"
+ "com.apple.private.iokit.preventSystemSleepSecurityIndicator"
- "No battery present. Can't start BDC\n"
- "No battery serial number. Can't start BDC"

```
