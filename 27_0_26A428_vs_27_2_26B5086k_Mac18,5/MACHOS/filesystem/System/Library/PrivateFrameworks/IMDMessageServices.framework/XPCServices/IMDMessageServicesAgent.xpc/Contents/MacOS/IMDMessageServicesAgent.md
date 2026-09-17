## IMDMessageServicesAgent

> `/System/Library/PrivateFrameworks/IMDMessageServices.framework/XPCServices/IMDMessageServicesAgent.xpc/Contents/MacOS/IMDMessageServicesAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-1491.100.1.1.11
-  __TEXT.__text: 0x7664
+1491.200.63.0.0
+  __TEXT.__text: 0x772c
   __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0xce0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x800
+  __TEXT.__gcc_except_tab: 0x80c
   __TEXT.__cstring: 0x358
-  __TEXT.__oslogstring: 0x1252
+  __TEXT.__oslogstring: 0x12aa
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methname: 0xfbc
   __TEXT.__objc_methtype: 0x2f2

   - /usr/lib/libobjc.A.dylib
   Functions: 148
   Symbols:   152
-  CStrings:  331
+  CStrings:  332
 
Functions:
~ sub_100006868 : 1540 -> 1740
CStrings:
+ "Watchdog: message %@ on service '%@' is not retry-eligible, failing instead of retrying"
```
