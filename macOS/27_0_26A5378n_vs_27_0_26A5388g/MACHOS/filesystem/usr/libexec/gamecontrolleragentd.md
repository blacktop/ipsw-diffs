## gamecontrolleragentd

> `/usr/libexec/gamecontrolleragentd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-14.0.19.0.0
-  __TEXT.__text: 0x2d34
+14.0.21.0.0
+  __TEXT.__text: 0x2e68
   __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_stubs: 0x780
+  __TEXT.__objc_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x3ac
   __TEXT.__const: 0x38
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__cstring: 0x35c
-  __TEXT.__oslogstring: 0x5e3
-  __TEXT.__objc_methname: 0x952
+  __TEXT.__cstring: 0x399
+  __TEXT.__oslogstring: 0x60d
+  __TEXT.__objc_methname: 0x98c
   __TEXT.__objc_classname: 0xe5
   __TEXT.__objc_methtype: 0x46c
   __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__const: 0x2f0
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__got: 0x98
   __DATA.__objc_const: 0x4f8
-  __DATA.__objc_selrefs: 0x318
+  __DATA.__objc_selrefs: 0x320
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x1e0

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 114
-  Symbols:   79
-  CStrings:  238
+  Functions: 116
+  Symbols:   80
+  CStrings:  241
 
Symbols:
+ _OBJC_CLASS_$_GCUserNotificationManager
Functions:
~ sub_100000e70 : 408 -> 536
+ sub_1000011ac
+ sub_100003238
CStrings:
+ "Connection to UserNotification failed: %@"
+ "connectToUserNotificationXPCProxyServiceWithClient:reply:"
+ "v24@?0@\"<GCUserNotificationXPCClientInterface>\"8@\"NSError\"16"
```
