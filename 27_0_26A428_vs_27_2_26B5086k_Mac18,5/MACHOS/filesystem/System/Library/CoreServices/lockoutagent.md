## lockoutagent

> `/System/Library/CoreServices/lockoutagent`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-26.0.0.0.0
-  __TEXT.__text: 0x34b4
+28.0.0.0.0
+  __TEXT.__text: 0x396c
   __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_stubs: 0xe20
-  __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0x70
+  __TEXT.__objc_stubs: 0xe60
+  __TEXT.__objc_methlist: 0x61c
+  __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__objc_methname: 0xdb5
-  __TEXT.__cstring: 0x2ae
-  __TEXT.__oslogstring: 0x2d1
+  __TEXT.__objc_methname: 0xde7
+  __TEXT.__cstring: 0x2b5
+  __TEXT.__oslogstring: 0x413
   __TEXT.__objc_classname: 0x14a
-  __TEXT.__objc_methtype: 0x3a9
-  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__objc_methtype: 0x3c2
+  __TEXT.__unwind_info: 0x1f0
   __DATA_CONST.__const: 0x210
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x1c0
-  __DATA_CONST.__got: 0x108
+  __DATA_CONST.__got: 0x110
   __DATA.__objc_const: 0x17f0
-  __DATA.__objc_selrefs: 0x460
+  __DATA.__objc_selrefs: 0x470
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x300

   - /System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/SkyLight
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 119
-  Symbols:   97
-  CStrings:  300
+  Functions: 124
+  Symbols:   98
+  CStrings:  311
 
Symbols:
+ __kLSPreviousValueKey
CStrings:
+ "App did exit: %{private}@"
+ "App did launch: %{private}@"
+ "App type changed data is not a dictionary"
+ "App type changed data missing type info: old=%{private}@, new=%{private}@"
+ "Is standard: %{private}@ for application type: %{private}@, java: %{private}@, finder: %{private}@"
+ "NO"
+ "Recieved LS notification: %d for ASNRef: %{private}@"
+ "YES"
+ "_isVisibleApplicationType:"
+ "appDidChange:withData:"
+ "v32@0:8^{__LSASN=}16^v24"
```
