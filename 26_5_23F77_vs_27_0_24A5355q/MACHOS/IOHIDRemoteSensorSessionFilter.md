## IOHIDRemoteSensorSessionFilter

> `/System/Library/HIDPlugins/SessionFilters/IOHIDRemoteSensorSessionFilter.plugin/IOHIDRemoteSensorSessionFilter`

```diff

-210.100.2.0.0
-  __TEXT.__text: 0x2ac
-  __TEXT.__auth_stubs: 0xe0
+223.0.0.0.0
+  __TEXT.__text: 0x270
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_stubs: 0x120
   __TEXT.__objc_methlist: 0x234
   __TEXT.__objc_methname: 0x2cb
-  __TEXT.__cstring: 0x48
-  __TEXT.__objc_classname: 0x3b
+  __TEXT.__cstring: 0x4a
+  __TEXT.__objc_classname: 0x39
   __TEXT.__objc_methtype: 0x245
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x78
-  __DATA_CONST.__got: 0x10
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x10
   __DATA.__objc_const: 0x2a0
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_ivar: 0x8

   - /System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC16440E-282A-3B90-BFEA-5A2A51E8B0FF
+  UUID: 240801AA-5ED4-30E1-BBE1-AA4D4CB1F6B7
   Functions: 14
-  Symbols:   24
+  Symbols:   25
   CStrings:  87
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_a74 : 56 -> 8
~ sub_b1c -> sub_aec : 200 -> 196
~ sub_c1c -> sub_be8 : 68 -> 64
~ sub_c60 -> sub_c28 : 68 -> 64

```
