## mediasetupd

> `/usr/libexec/mediasetupd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-261.0.0.0.0
+261.10.1.0.0
   __TEXT.__text: 0x2e77c
   __TEXT.__auth_stubs: 0x6e0
   __TEXT.__objc_stubs: 0x4c40
-  __TEXT.__objc_methlist: 0x1fdc
+  __TEXT.__objc_methlist: 0x1fec
   __TEXT.__cstring: 0x242d
   __TEXT.__oslogstring: 0x58f7
   __TEXT.__const: 0x118
-  __TEXT.__objc_methname: 0x6b9e
+  __TEXT.__objc_methname: 0x6c27
   __TEXT.__objc_classname: 0x31c
   __TEXT.__objc_methtype: 0x1313
   __TEXT.__gcc_except_tab: 0xc40

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x380
   __DATA_CONST.__got: 0x560
-  __DATA.__objc_const: 0x3108
-  __DATA.__objc_selrefs: 0x1bd8
+  __DATA.__objc_const: 0x3118
+  __DATA.__objc_selrefs: 0x1be8
   __DATA.__objc_ivar: 0x15c
   __DATA.__objc_data: 0x730
   __DATA.__data: 0x4e0

   - /usr/lib/libobjc.A.dylib
   Functions: 962
   Symbols:   289
-  CStrings:  1966
+  CStrings:  1968
 
CStrings:
+ "homeManager:didRemoveCurrentAccessoryWithRegulatoryEraseRequired:"
+ "profileConnectionDidReceiveAllowCloudSyncChangedNotification:userInfo:"
```
