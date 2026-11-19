## Installer

> `/System/Library/CoreServices/Installer.app/Contents/MacOS/Installer`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1365.0.0.0.0
-  __TEXT.__text: 0x19784
-  __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_stubs: 0x6fa0
-  __TEXT.__objc_methlist: 0x1b10
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x304b
-  __TEXT.__objc_methname: 0x69af
+1368.41.1.0.0
+  __TEXT.__text: 0x19410
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_stubs: 0x6e40
+  __TEXT.__objc_methlist: 0x1b08
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x2fa5
+  __TEXT.__objc_methname: 0x6899
   __TEXT.__objc_classname: 0x450
   __TEXT.__objc_methtype: 0xd06
   __TEXT.__gcc_except_tab: 0xdc
   __TEXT.__unwind_info: 0x8d8
   __DATA_CONST.__const: 0x4b8
-  __DATA_CONST.__cfstring: 0x28c0
+  __DATA_CONST.__cfstring: 0x28e0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x308
-  __DATA_CONST.__got: 0x500
-  __DATA.__objc_const: 0x3720
-  __DATA.__objc_selrefs: 0x2188
-  __DATA.__objc_ivar: 0x2d4
+  __DATA_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0x4f8
+  __DATA.__objc_const: 0x3740
+  __DATA.__objc_selrefs: 0x2130
+  __DATA.__objc_ivar: 0x2d8
   __DATA.__objc_data: 0xaf0
   __DATA.__data: 0x270
   __DATA.__common: 0x8

   - /usr/lib/libDiskUnlock.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 554
-  Symbols:   277
-  CStrings:  1928
+  Functions: 553
+  Symbols:   275
+  CStrings:  1914
 
Symbols:
- _NSFileTypeDirectory
- _mkdtemp
CStrings:
+ ".."
+ "Installer Plugins: Ignoring section path that escapes the package's plugins directory: %s"
+ "Installer Plugins: Pinned %lu section path(s) from the package's section list"
+ "_didPinSectionPaths"
+ "_pinnedSectionPaths"
+ "pinnedInstallerSectionPaths"
+ "pluginArchitecturesForSectionPaths:"
- "/tmp/com.apple.installerXXXXXXXX"
- "Couldn't create installer tmp directory"
- "Failed copying bundle path %s to %s (%s)"
- "Failed creating plugin path at %s (%s)"
- "Failed to create link for plugin path at %s with contents %s (%s)"
- "Installer Plugins: %s relocated to %s"
- "Installer Plugins: Plugins on removable media relocated to (executable only) %s"
- "_createShellBundleDirectory"
- "_createShellBundleForBundleAtPath:"
- "_shellBundleDirectory"
- "copyItemAtPath:toPath:error:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "createSymbolicLinkAtPath:withDestinationPath:error:"
- "enumeratorAtPath:"
- "fileAttributes"
- "fileType"
- "initWithUTF8String:"
- "pathIsRemovable:"
- "pluginArchitecturesForDocument:"
- "rootVolumeIsReadOnly"
- "skipDescendents"
```
