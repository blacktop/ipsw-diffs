## batterytrapd

> `/usr/libexec/batterytrapd`

```diff

-8.100.2.0.0
-  __TEXT.__text: 0x16e4
-  __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_stubs: 0x500
-  __TEXT.__objc_methlist: 0x188
-  __TEXT.__const: 0x28
-  __TEXT.__oslogstring: 0x41f
-  __TEXT.__cstring: 0x211
-  __TEXT.__objc_methname: 0x356
+21.0.0.0.0
+  __TEXT.__text: 0x1d70
+  __TEXT.__auth_stubs: 0x360
+  __TEXT.__objc_stubs: 0x620
+  __TEXT.__objc_methlist: 0x1cc
+  __TEXT.__const: 0x30
+  __TEXT.__oslogstring: 0x552
+  __TEXT.__cstring: 0x25d
+  __TEXT.__objc_methname: 0x417
   __TEXT.__objc_classname: 0x24
-  __TEXT.__objc_methtype: 0xba
+  __TEXT.__objc_methtype: 0xc7
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x1b8
-  __DATA_CONST.__got: 0x88
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x1c0
+  __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x88
-  __DATA_CONST.__cfstring: 0x220
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0x2a8
-  __DATA.__objc_selrefs: 0x188
-  __DATA.__objc_ivar: 0x1c
+  __DATA.__objc_const: 0x2c8
+  __DATA.__objc_selrefs: 0x1d8
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xf0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 1DE50D79-0FB4-3F63-84DE-2F3D85C91D9A
-  Functions: 53
-  Symbols:   79
-  CStrings:  136
+  UUID: 363DD4F3-56A9-39D2-BCA4-F00A4FB180AF
+  Functions: 68
+  Symbols:   81
+  CStrings:  163
 
Symbols:
+ _NSLocaleLanguageCode
+ _objc_retain_x19
CStrings:
+ "B"
+ "B24@0:8@16"
+ "Clearing all variables\n"
+ "Couldn't clear nvram variable: %@, error:0x%x"
+ "Couldn't sync nvram, error:0x%x"
+ "IONVRAM-DELETEWRET-PROPERTY"
+ "Language direction is invalid, will set it to default 1 (LTR)"
+ "Skipping nvram sync call, none of batterytrapd variables were updated"
+ "_numberingSystem"
+ "alpm-language-direction"
+ "alpm-number-system"
+ "characterDirectionForLanguage:"
+ "clearAllVariables"
+ "clearNVRAM:"
+ "latn"
+ "length"
+ "numberingSystem(%@) len(%lu) out of range, will set it to default 'latn'"
+ "numberingSystem: %@, len: %lu"
+ "objectForKey:"
+ "readLanguageDirection"
+ "readNumberingSystem"
+ "setLanguageDirection"
+ "setNumberingSystem"
+ "syncPending"
- "Couldn't sync nvram to device"

```
