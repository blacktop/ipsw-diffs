## NRDUpdated

> `/usr/libexec/NRDUpdated`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__objc_classname`
- `__TEXT.__objc_methtype`
- `__TEXT.__oslogstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2718.0.5.0.0
+2718.0.12.0.0
   __TEXT.__text: 0xb24c
   __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_stubs: 0x1be0
   __TEXT.__objc_methlist: 0xc54
-  __TEXT.__const: 0x90
   __TEXT.__cstring: 0x119a
-  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__const: 0x90
+  __TEXT.__oslogstring: 0x17bd
   __TEXT.__objc_methname: 0x1af1
   __TEXT.__objc_classname: 0x204
   __TEXT.__objc_methtype: 0x833
-  __TEXT.__oslogstring: 0x17bd
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__gcc_except_tab: 0x19c
+  __TEXT.__unwind_info: 0x348
   __DATA_CONST.__const: 0x6b0
   __DATA_CONST.__cfstring: 0xf80
   __DATA_CONST.__objc_classlist: 0x30

   __DATA.__objc_ivar: 0xa0
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x540
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x59
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
Symbols:
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MobileSoftwareUpdate_MainOSOnly/Common/
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/MobileSoftwareUpdate_MainOSOnly/
CStrings:
+ "02:21:34"
+ "Jul 10 2026"
- "03:51:09"
- "Jun 27 2026"
```
