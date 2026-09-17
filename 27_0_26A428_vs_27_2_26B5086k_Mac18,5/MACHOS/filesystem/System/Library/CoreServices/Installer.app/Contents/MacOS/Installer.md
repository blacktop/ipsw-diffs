## Installer

> `/System/Library/CoreServices/Installer.app/Contents/MacOS/Installer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1365.0.0.0.0
-  __TEXT.__text: 0x19784
+1368.0.0.0.0
+  __TEXT.__text: 0x1995c
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0x6fa0
-  __TEXT.__objc_methlist: 0x1b10
+  __TEXT.__objc_stubs: 0x6fc0
+  __TEXT.__objc_methlist: 0x1b20
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x304b
-  __TEXT.__objc_methname: 0x69af
+  __TEXT.__cstring: 0x30f6
+  __TEXT.__objc_methname: 0x69f7
   __TEXT.__objc_classname: 0x450
   __TEXT.__objc_methtype: 0xd06
   __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__unwind_info: 0x8e0
   __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__cfstring: 0x28c0
+  __DATA_CONST.__cfstring: 0x28e0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0x308
   __DATA_CONST.__got: 0x500
-  __DATA.__objc_const: 0x3720
-  __DATA.__objc_selrefs: 0x2188
-  __DATA.__objc_ivar: 0x2d4
+  __DATA.__objc_const: 0x3760
+  __DATA.__objc_selrefs: 0x2190
+  __DATA.__objc_ivar: 0x2dc
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x270
   __DATA.__common: 0x8

   - /usr/lib/libDiskUnlock.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 554
+  Functions: 555
   Symbols:   277
-  CStrings:  1928
+  CStrings:  1934
 
CStrings:
+ ".."
+ "Installer Plugins: Ignoring section path that escapes the package's plugins directory: %s"
+ "Installer Plugins: Pinned %lu section path(s) from the package's section list"
+ "_didPinSectionPaths"
+ "_pinnedSectionPaths"
+ "pinnedInstallerSectionPaths"
+ "pluginArchitecturesForSectionPaths:"
- "pluginArchitecturesForDocument:"
```
