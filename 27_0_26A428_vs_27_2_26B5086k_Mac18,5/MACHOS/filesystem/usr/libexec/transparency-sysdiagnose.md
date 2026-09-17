## transparency-sysdiagnose

> `/usr/libexec/transparency-sysdiagnose`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1766.0.60.0.0
-  __TEXT.__text: 0xe70
+1766.40.47.0.0
+  __TEXT.__text: 0x10cc
   __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_stubs: 0x420
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x10
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__cstring: 0x15f
-  __TEXT.__oslogstring: 0x59
+  __TEXT.__const: 0x18
+  __TEXT.__gcc_except_tab: 0x60
+  __TEXT.__cstring: 0x1e0
+  __TEXT.__oslogstring: 0x94
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x5d0
   __TEXT.__objc_methtype: 0x12f
-  __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0xe0
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/Transparency.framework/Versions/A/Transparency
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 21
+  Functions: 25
   Symbols:   53
-  CStrings:  102
+  CStrings:  105
 
CStrings:
+ "no application support directory to read the fallback report from: %@"
+ "no directory to delete %@ from"
+ "no directory to write %@ to"
```
