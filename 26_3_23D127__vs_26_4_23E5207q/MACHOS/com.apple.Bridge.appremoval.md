## com.apple.Bridge.appremoval

> `/System/Library/AppRemovalServices/com.apple.Bridge.appremoval.xpc/com.apple.Bridge.appremoval`

```diff

-1310.1.2.0.0
-  __TEXT.__text: 0x890
-  __TEXT.__auth_stubs: 0x1d0
+1310.9.0.0.0
+  __TEXT.__text: 0x8a0
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_stubs: 0x360
   __TEXT.__objc_methlist: 0x224
   __TEXT.__objc_classname: 0x8b

   __TEXT.__cstring: 0x37f
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0xf0
+  __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x18

   - /System/Library/PrivateFrameworks/PBBridgeSupport.framework/PBBridgeSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FCC79ABD-373B-302E-A8EA-2769777343AF
+  UUID: 865E7EA7-8E8C-3C57-B5F7-5575557AAB95
   Functions: 18
-  Symbols:   50
+  Symbols:   49
   CStrings:  123
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_release_x21
- _objc_release_x8
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ sub_100000bd8 : 112 -> 116
~ _main : 92 -> 96
~ sub_100000f94 -> sub_100000f9c : 156 -> 160
~ sub_100001030 -> sub_10000103c : 356 -> 360

```
