## Diagnostic-8290-EFD

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8290-EFD.appex/Diagnostic-8290-EFD`

```diff

-1066.40.34.0.0
-  __TEXT.__text: 0xec1c
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x33a0
-  __TEXT.__objc_methlist: 0x1334
+1066.40.45.0.0
+  __TEXT.__text: 0xed5c
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__objc_stubs: 0x33c0
+  __TEXT.__objc_methlist: 0x134c
   __TEXT.__const: 0xd0
   __TEXT.__cstring: 0xa38
   __TEXT.__objc_methname: 0x3fcb
-  __TEXT.__oslogstring: 0x14a5
-  __TEXT.__objc_classname: 0x20e
+  __TEXT.__oslogstring: 0x155b
+  __TEXT.__objc_classname: 0x223
   __TEXT.__objc_methtype: 0x647
   __TEXT.__gcc_except_tab: 0x160
   __TEXT.__unwind_info: 0x300
-  __DATA_CONST.__auth_got: 0x378
+  __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x240
   __DATA_CONST.__cfstring: 0xee0
   __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_arraydata: 0x28

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_floatobj: 0x40
-  __DATA.__objc_const: 0x2890
+  __DATA.__objc_const: 0x28b0
   __DATA.__objc_selrefs: 0xe78
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x640
-  __DATA.__data: 0x240
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0xc
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC76C543-24D0-3F99-B25F-9AE15C11E8D0
+  UUID: 8833CDA7-363A-323F-9A32-EFD2DBF32C83
   Functions: 423
-  Symbols:   231
-  CStrings:  1208
+  Symbols:   232
+  CStrings:  1212
 
Symbols:
+ _DiagnosticsKitLogHandleForCategory
Functions:
~ sub_100002d1c -> sub_100002d6c : 276 -> 364
~ sub_100007b70 -> sub_100007c18 : 900 -> 920
~ sub_100008b00 -> sub_100008bbc : 384 -> 424
~ sub_10000be64 -> sub_10000bf48 : 160 -> 244
~ sub_10000c934 -> sub_10000ca6c : 168 -> 256
CStrings:
+ "Attempt to stop DAChamberDetector that hasn't been started."
+ "Attempt to stop DAWifiSensor that hasn't been started."
+ "DAALSSensor: Attempt to stop DAALSSensor that hasn't been started."
+ "DKVolumeHUDResponder"

```
