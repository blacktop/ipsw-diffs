## triald

> `/usr/libexec/triald`

```diff

-474.2.18.2.0
-  __TEXT.__text: 0x4e4
-  __TEXT.__auth_stubs: 0x1c0
+501.0.0.0.0
+  __TEXT.__text: 0x49c
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0xa0
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x130
+  __TEXT.__const: 0x40
+  __TEXT.__cstring: 0x131
   __TEXT.__oslogstring: 0x3e
   __TEXT.__objc_methname: 0xb8
-  __TEXT.__objc_classname: 0x1a
+  __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methtype: 0x13
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x28
   __DATA.__objc_const: 0x40
   __DATA.__objc_selrefs: 0x38
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/TrialServer.framework/TrialServer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F732629F-CC92-34DA-840F-FB5D7423725A
+  UUID: C30EADDE-3070-3515-B498-299B716A32A2
   Functions: 5
-  Symbols:   38
+  Symbols:   39
   CStrings:  25
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ sub_100000b38 : 220 -> 176
~ sub_100000c9c -> sub_100000c70 : 264 -> 256
~ sub_100000da4 -> sub_100000d70 : 460 -> 448
~ sub_100000f70 -> sub_100000f30 : 172 -> 164

```
