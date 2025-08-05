## nanoregistryd

> `/usr/libexec/nanoregistryd`

```diff

-1027.10.0.0.0
-  __TEXT.__text: 0x104474
+1027.12.0.0.0
+  __TEXT.__text: 0x1045d8
   __TEXT.__auth_stubs: 0x10f0
   __TEXT.__objc_stubs: 0x10dc0
   __TEXT.__objc_methlist: 0xd8ec
   __TEXT.__const: 0x688
   __TEXT.__gcc_except_tab: 0x2694
-  __TEXT.__objc_methname: 0x1c1a4
-  __TEXT.__cstring: 0xdab2
-  __TEXT.__oslogstring: 0x15879
+  __TEXT.__objc_methname: 0x1c1cd
+  __TEXT.__cstring: 0xdaca
+  __TEXT.__oslogstring: 0x158f9
   __TEXT.__objc_classname: 0x225b
   __TEXT.__objc_methtype: 0x49be
   __TEXT.__dlopen_cstrs: 0xef

   __DATA_CONST.__got: 0xc88
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x4a00
-  __DATA_CONST.__cfstring: 0xbc20
+  __DATA_CONST.__cfstring: 0xbc40
   __DATA_CONST.__objc_classlist: 0x7c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA.__objc_const: 0x19f60
+  __DATA.__objc_const: 0x19f80
   __DATA.__objc_selrefs: 0x5de8
-  __DATA.__objc_ivar: 0x11c8
+  __DATA.__objc_ivar: 0x11cc
   __DATA.__objc_data: 0x4dd0
   __DATA.__data: 0x19d8
   __DATA.__bss: 0x488

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 2D9CBCAE-18FD-346D-AFAA-2AF38B6CB1C0
+  UUID: CC921EF6-7116-3E14-BD67-8600ECEFA7D1
   Functions: 5758
   Symbols:   696
-  CStrings:  10160
+  CStrings:  10164
 
Functions:
~ sub_100063e58 : 352 -> 372
~ sub_1000641dc -> sub_1000641f0 : 88 -> 96
~ sub_100066248 -> sub_100066264 : 492 -> 556
~ sub_10006b95c -> sub_10006b9b8 : 236 -> 248
~ sub_10008205c -> sub_1000820c4 : 1120 -> 1372
CStrings:
+ "34"
+ "NanoRegistry-1027.12"
+ "Watch to unpair is past activation state, setting obliteration even though not originally requested"
+ "[Push] Not calling requestAuthMethodForDevice with method %lu for candidate %@ (pending %{BOOL}d, presharedRequested %{BOOL}d)"
+ "_globalPresharedAuthRequestedIdentifiers"
+ "unpairingPastActivation"
- "20"
- "NanoRegistry-1027.10"
- "[Push] Not calling requestAuthMethodForDevice with method %lu on an already requested candidate %@"

```
