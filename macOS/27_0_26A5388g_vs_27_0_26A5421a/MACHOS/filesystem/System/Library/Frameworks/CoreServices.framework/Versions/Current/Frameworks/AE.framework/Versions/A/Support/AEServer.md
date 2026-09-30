## AEServer

> `/System/Library/Frameworks/CoreServices.framework/Versions/Current/Frameworks/AE.framework/Versions/A/Support/AEServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-994.0.0.0.0
-  __TEXT.__text: 0xf41c
+995.0.0.0.0
+  __TEXT.__text: 0xf40c
   __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x14
-  __TEXT.__const: 0x1b8
+  __TEXT.__const: 0x1b0
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__cstring: 0xdcb
-  __TEXT.__oslogstring: 0x17b0
+  __TEXT.__cstring: 0xdc4
+  __TEXT.__oslogstring: 0x17ae
   __TEXT.__objc_classname: 0x20
   __TEXT.__objc_methname: 0xc0
   __TEXT.__objc_methtype: 0xb

   - /usr/lib/libobjc.A.dylib
   Functions: 201
   Symbols:   313
-  CStrings:  324
+  CStrings:  322
 
Functions:
~ sub_100003664 : 1332 -> 1308
~ sub_10000db08 -> sub_10000daf0 : 284 -> 292
CStrings:
+ "%{public}*cEPPCIOStream::becomeSecure( asServer=%{BOOL}d)"
- "%{public}*cEPPCIOStream::becomeSecure( asServer=%{public}s)"
- "NO"
- "YES"
```
