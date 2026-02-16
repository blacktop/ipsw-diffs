## remotesoftwareupdated

> `/usr/libexec/remotesoftwareupdated`

```diff

 1.0.0.0.0
-  __TEXT.__text: 0x17c
-  __TEXT.__auth_stubs: 0xe0
+  __TEXT.__text: 0x1b8
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x80
   __TEXT.__objc_methlist: 0x164
   __TEXT.__objc_methname: 0x1f0

   __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methtype: 0x10d
   __TEXT.__oslogstring: 0x16
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x78
+  __TEXT.__unwind_info: 0x68
+  __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8

   - /System/Library/PrivateFrameworks/RemoteSoftwareUpdate.framework/RemoteSoftwareUpdate
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58588312-C699-33D7-9CE3-464F354D9E92
+  UUID: AC2FC94B-362F-34FA-A3BC-6E948B649CBF
   Functions: 6
-  Symbols:   23
+  Symbols:   25
   CStrings:  59
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
Functions:
~ sub_100000bf0 : 164 -> 172
~ sub_100000ca4 -> sub_100000cac : 12 -> 64

```
