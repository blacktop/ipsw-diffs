## helpd

> `/System/Library/PrivateFrameworks/HelpData.framework/Versions/Current/Resources/helpd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-241.0.0.0.0
-  __TEXT.__text: 0xf9f4
-  __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_stubs: 0x2a40
+243.0.0.0.0
+  __TEXT.__text: 0xfb64
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__objc_stubs: 0x2a80
   __TEXT.__objc_methlist: 0xb5c
   __TEXT.__gcc_except_tab: 0x8bc
   __TEXT.__cstring: 0x13da
-  __TEXT.__objc_methname: 0x253b
+  __TEXT.__objc_methname: 0x2553
   __TEXT.__objc_classname: 0x11f
   __TEXT.__objc_methtype: 0x50d
   __TEXT.__const: 0x38
   __TEXT.__oslogstring: 0x60
   __TEXT.__unwind_info: 0x478
-  __DATA_CONST.__const: 0x4d0
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__cfstring: 0x15e0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x458
-  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__auth_got: 0x480
+  __DATA_CONST.__got: 0x318
   __DATA.__objc_const: 0x1178
-  __DATA.__objc_selrefs: 0xc50
+  __DATA.__objc_selrefs: 0xc60
   __DATA.__objc_ivar: 0xbc
   __DATA.__objc_data: 0x320
   __DATA.__data: 0x240

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 277
-  Symbols:   236
-  CStrings:  749
+  Functions: 278
+  Symbols:   250
+  CStrings:  751
 
Symbols:
+ _HPDRunningFromLaunchd
+ _OBJC_CLASS_$_NSProcessInfo
+ _XPC_ACTIVITY_DELAY
+ _XPC_ACTIVITY_GRACE_PERIOD
+ _XPC_ACTIVITY_INTERVAL_15_MIN
+ _XPC_ACTIVITY_INTERVAL_1_MIN
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_UTILITY
+ _XPC_ACTIVITY_REPEATING
+ _xpc_activity_register
+ _xpc_dictionary_create
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_string
Functions:
~ sub_10000a4f0 : 1072 -> 1432
+ sub_10000aa90
CStrings:
+ "environment"
+ "processInfo"
```
