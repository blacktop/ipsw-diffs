## printtool

> `System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Versions/A/printtool`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-601.3.0.0.0
-  __TEXT.__text: 0xecf0
-  __TEXT.__auth_stubs: 0x1080
+601.4.0.0.0
+  __TEXT.__text: 0xf0bc
+  __TEXT.__auth_stubs: 0x10b0
   __TEXT.__objc_stubs: 0x1840
   __TEXT.__objc_methlist: 0x50c
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x1457
-  __TEXT.__cstring: 0x18e4
-  __TEXT.__gcc_except_tab: 0x42c
+  __TEXT.__oslogstring: 0x1516
+  __TEXT.__cstring: 0x194e
+  __TEXT.__gcc_except_tab: 0x430
   __TEXT.__objc_classname: 0x5c
   __TEXT.__objc_methname: 0x1301
   __TEXT.__objc_methtype: 0x8db
-  __TEXT.__unwind_info: 0x478
-  __DATA_CONST.__auth_got: 0x850
+  __TEXT.__unwind_info: 0x480
+  __DATA_CONST.__auth_got: 0x868
   __DATA_CONST.__got: 0x1a8
   __DATA_CONST.__const: 0x820
   __DATA_CONST.__cfstring: 0xb00

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcups.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 356
-  Symbols:   327
-  CStrings:  751
+  Functions: 360
+  Symbols:   330
+  CStrings:  762
 
Symbols:
+ _ppdFindNextAttr
+ _sscanf
+ _strchr
CStrings:
+ "%15[^/]/%31s%d%1023s"
+ "%s: rejected outMime with printer/ prefix"
+ "%s: rejected ppd with untrusted filter references"
+ "%s: rejected spoolFileName containing path separator or traversal"
+ "%s: untrusted filter: %{public}s"
+ ".."
+ "/usr/libexec/cups/filter/%s"
+ "cupsPreFilter"
+ "isSecureFilter"
+ "printer/"
+ "toolConvertFile"
```
