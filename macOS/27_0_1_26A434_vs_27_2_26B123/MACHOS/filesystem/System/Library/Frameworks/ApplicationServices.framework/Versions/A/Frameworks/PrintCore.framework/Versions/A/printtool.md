## printtool

> `/System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Versions/A/printtool`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-610.0.0.0.0
-  __TEXT.__text: 0xde50
-  __TEXT.__auth_stubs: 0x1090
+610.1.0.0.0
+  __TEXT.__text: 0xe1f4
+  __TEXT.__auth_stubs: 0x10c0
   __TEXT.__objc_stubs: 0x1840
   __TEXT.__objc_methlist: 0x50c
   __TEXT.__const: 0xf0
-  __TEXT.__oslogstring: 0x1457
-  __TEXT.__cstring: 0x18eb
-  __TEXT.__gcc_except_tab: 0x2e8
+  __TEXT.__oslogstring: 0x1516
+  __TEXT.__cstring: 0x1955
+  __TEXT.__gcc_except_tab: 0x30c
   __TEXT.__objc_methname: 0x1301
   __TEXT.__objc_classname: 0x55
   __TEXT.__objc_methtype: 0x8db
-  __TEXT.__info_plist: 0x53c
-  __TEXT.__unwind_info: 0x530
+  __TEXT.__info_plist: 0x53e
+  __TEXT.__unwind_info: 0x548
   __DATA_CONST.__const: 0x820
   __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x28

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x858
+  __DATA_CONST.__auth_got: 0x870
   __DATA_CONST.__got: 0x1b8
   __DATA.__objc_const: 0x780
   __DATA.__objc_selrefs: 0x688

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcups.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 353
-  Symbols:   328
-  CStrings:  751
+  Functions: 356
+  Symbols:   331
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
