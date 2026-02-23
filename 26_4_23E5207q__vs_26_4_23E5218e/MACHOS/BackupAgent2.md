## BackupAgent2

> `/usr/libexec/BackupAgent2`

```diff

-2969.100.18.0.0
-  __TEXT.__text: 0x9dc8c
+2969.100.30.0.0
+  __TEXT.__text: 0x9da2c
   __TEXT.__auth_stubs: 0x18a0
-  __TEXT.__objc_stubs: 0xd060
+  __TEXT.__objc_stubs: 0xd020
   __TEXT.__objc_methlist: 0x6730
   __TEXT.__const: 0x4c8
-  __TEXT.__cstring: 0x18f46
-  __TEXT.__oslogstring: 0xe000
-  __TEXT.__objc_methname: 0xf4e5
+  __TEXT.__cstring: 0x18e91
+  __TEXT.__oslogstring: 0xdf4b
+  __TEXT.__objc_methname: 0xf4c5
   __TEXT.__objc_classname: 0xa9f
   __TEXT.__objc_methtype: 0x1f94
   __TEXT.__gcc_except_tab: 0x25c8

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0xa430
-  __DATA.__objc_selrefs: 0x4080
+  __DATA.__objc_selrefs: 0x4078
   __DATA.__objc_ivar: 0x5e0
   __DATA.__objc_data: 0x2440
   __DATA.__data: 0x878

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: B0D80C45-CD32-34A2-9A25-E1A27CEA4DA0
+  UUID: 59ACDBDE-CB87-3CBC-94F5-355DB64E8C83
   Functions: 2595
   Symbols:   574
-  CStrings:  8526
+  CStrings:  8519
 
Functions:
~ sub_10001ce74 : 808 -> 508
~ sub_10007a12c -> sub_10007a000 : 1360 -> 1096
~ sub_10007aa6c -> sub_10007a838 : 1052 -> 1004
~ sub_10007aef4 -> sub_10007ac90 : 628 -> 632
CStrings:
+ "No Apple account exists"
- "Extended attributes size greater than supported (%lu > %d): %@"
- "Extended attributes size greater than supported (%{bytes}lu > %{bytes}d): %@"
- "No Apple acount exists"
- "Passcode policy evalutation succeeded: %@"
- "internalIgnoreSetDatalessErrors"

```
