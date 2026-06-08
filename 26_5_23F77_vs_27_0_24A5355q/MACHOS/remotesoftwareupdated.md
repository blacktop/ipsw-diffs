## remotesoftwareupdated

> `/usr/libexec/remotesoftwareupdated`

```diff

 1.0.0.0.0
-  __TEXT.__text: 0x1b8
-  __TEXT.__auth_stubs: 0x100
+  __TEXT.__text: 0x17c
+  __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__objc_methlist: 0x164
   __TEXT.__objc_methname: 0x1f0
-  __TEXT.__cstring: 0x20
-  __TEXT.__objc_classname: 0x39
+  __TEXT.__cstring: 0x22
+  __TEXT.__objc_classname: 0x37
   __TEXT.__objc_methtype: 0x10d
   __TEXT.__oslogstring: 0x16
-  __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x10
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x78
+  __DATA_CONST.__got: 0x10
   __DATA.__objc_const: 0x230
   __DATA.__objc_selrefs: 0xe0
   __DATA.__objc_ivar: 0x4

   - /System/Library/PrivateFrameworks/RemoteSoftwareUpdate.framework/RemoteSoftwareUpdate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7B84E9E-F7FF-3403-BBDD-6E12528A068D
+  UUID: 21FFA8E0-F658-3743-A694-685AD46BE68E
   Functions: 6
-  Symbols:   25
+  Symbols:   23
   CStrings:  59
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ sub_100000bf0 : 172 -> 164
~ sub_100000cac -> sub_100000ca4 : 64 -> 12

```
