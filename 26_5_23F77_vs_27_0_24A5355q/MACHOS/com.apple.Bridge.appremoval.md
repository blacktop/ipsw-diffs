## com.apple.Bridge.appremoval

> `/System/Library/AppRemovalServices/com.apple.Bridge.appremoval.xpc/com.apple.Bridge.appremoval`

```diff

-1310.13.0.0.0
-  __TEXT.__text: 0x8a0
-  __TEXT.__auth_stubs: 0x1c0
+1350.1.0.0.0
+  __TEXT.__text: 0x894
+  __TEXT.__auth_stubs: 0x1d0
   __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x224
   __TEXT.__objc_classname: 0x8b

   __TEXT.__cstring: 0x37f
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x38
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__got: 0x38
   __DATA.__objc_const: 0x398
   __DATA.__objc_selrefs: 0x188
   __DATA.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 631D6DDB-2C96-39D9-90CD-59F73BFEF5C7
+  UUID: AD098A0E-F6FF-3659-A095-4CEB6850C2AE
   Functions: 18
-  Symbols:   49
+  Symbols:   50
   CStrings:  123
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x21
+ _objc_release_x8
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x22
Functions:
~ sub_100000bd8 : 116 -> 112
~ _main : 96 -> 92
~ sub_100000f9c -> sub_100000f94 : 160 -> 156

```
