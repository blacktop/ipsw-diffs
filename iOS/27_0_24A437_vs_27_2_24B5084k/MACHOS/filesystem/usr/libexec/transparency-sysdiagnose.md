## transparency-sysdiagnose

> `/usr/libexec/transparency-sysdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1766.0.60.0.0
-  __TEXT.__text: 0xf18
-  __TEXT.__auth_stubs: 0x2b0
+1766.40.47.0.0
+  __TEXT.__text: 0x1158
+  __TEXT.__auth_stubs: 0x2c0
   __TEXT.__objc_stubs: 0x440
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x15d
-  __TEXT.__oslogstring: 0x74
+  __TEXT.__const: 0x20
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__cstring: 0x1de
+  __TEXT.__oslogstring: 0xaf
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x5b6
   __TEXT.__objc_methtype: 0x12f
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__const: 0xa8
-  __DATA_CONST.__cfstring: 0xe0
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0xe8
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x168
+  __DATA_CONST.__auth_got: 0x170
   __DATA_CONST.__got: 0x98
   __DATA.__objc_const: 0x200
   __DATA.__objc_selrefs: 0x1d8

   - /System/Library/PrivateFrameworks/Transparency.framework/Transparency
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21
-  Symbols:   71
-  CStrings:  102
+  Functions: 25
+  Symbols:   72
+  CStrings:  105
 
Symbols:
+ _objc_release_x25
CStrings:
+ "no application support directory to read the fallback report from: %@"
+ "no directory to delete %@ from"
+ "no directory to write %@ to"
```
