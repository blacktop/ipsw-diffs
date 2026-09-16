## IMDMessageServicesAgent

> `/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/IMDMessageServicesAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-1491.100.1.2.25
-  __TEXT.__text: 0x7648
+1491.200.63.2.1
+  __TEXT.__text: 0x7710
   __TEXT.__auth_stubs: 0x6d0
   __TEXT.__objc_stubs: 0xea0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x85c
+  __TEXT.__gcc_except_tab: 0x868
   __TEXT.__cstring: 0x35f
-  __TEXT.__oslogstring: 0x1303
+  __TEXT.__oslogstring: 0x135b
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methname: 0x10b2
   __TEXT.__objc_methtype: 0x2f2

   - /usr/lib/libobjc.A.dylib
   Functions: 127
   Symbols:   177
-  CStrings:  345
+  CStrings:  346
 
Functions:
~ sub_10000694c : 1452 -> 1652
CStrings:
+ "Watchdog: message %@ on service '%@' is not retry-eligible, failing instead of retrying"
```
