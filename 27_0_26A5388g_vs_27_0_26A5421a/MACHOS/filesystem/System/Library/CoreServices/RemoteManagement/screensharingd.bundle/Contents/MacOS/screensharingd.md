## screensharingd

> `/System/Library/CoreServices/RemoteManagement/screensharingd.bundle/Contents/MacOS/screensharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-756.34.0.0.0
-  __TEXT.__text: 0x77500
+756.36.5.2.0
+  __TEXT.__text: 0x77aa0
   __TEXT.__auth_stubs: 0x1e10
   __TEXT.__objc_stubs: 0x2120
   __TEXT.__objc_methlist: 0xd48
-  __TEXT.__const: 0x2380
-  __TEXT.__oslogstring: 0xcae3
-  __TEXT.__cstring: 0x14763
+  __TEXT.__const: 0x2370
+  __TEXT.__oslogstring: 0xcbbf
+  __TEXT.__cstring: 0x14857
   __TEXT.__gcc_except_tab: 0x194
   __TEXT.__objc_methname: 0x2340
   __TEXT.__objc_classname: 0xde
   __TEXT.__objc_methtype: 0x6c0
-  __TEXT.__unwind_info: 0xa30
+  __TEXT.__unwind_info: 0xa20
   __DATA_CONST.__const: 0xe18
   __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0x48

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1129
+  Functions: 1135
   Symbols:   590
-  CStrings:  2996
+  CStrings:  3002
 
CStrings:
+ "Refuse to run file receiver as uid %u"
+ "Refuse to run file sender as uid %u"
+ "SaveAdvertisedAuthTypes"
+ "bad auth type list - length %u count %u"
+ "viewer requested RSA SRP but SRP was not advertised"
+ "viewer selected auth type %u which was not advertised"
```
