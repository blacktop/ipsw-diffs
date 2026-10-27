## mdsync

> `/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Support/mdsync`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__dof_MetadataI`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0x52d3c
+2465.1.9.0.0
+  __TEXT.__text: 0x5306c
   __TEXT.__auth_stubs: 0x2d10
   __TEXT.__objc_stubs: 0x2500
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0xa44
-  __TEXT.__const: 0x2114
-  __TEXT.__cstring: 0x9ce2
+  __TEXT.__const: 0x2104
+  __TEXT.__cstring: 0x9c95
   __TEXT.__objc_methname: 0x2649
   __TEXT.__objc_classname: 0x1ea
   __TEXT.__objc_methtype: 0xbc8
-  __TEXT.__gcc_except_tab: 0x81c
-  __TEXT.__oslogstring: 0x2dcd
+  __TEXT.__gcc_except_tab: 0x82c
+  __TEXT.__oslogstring: 0x2f0c
   __TEXT.__ustring: 0x86
   __TEXT.__dof_MetadataI: 0x1e9
-  __TEXT.__unwind_info: 0x16b0
-  __DATA_CONST.__const: 0x50b8
+  __TEXT.__unwind_info: 0x16c8
+  __DATA_CONST.__const: 0x5118
   __DATA_CONST.__cfstring: 0x4760
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1713
+  Functions: 1722
   Symbols:   908
-  CStrings:  2682
+  CStrings:  2681
 
CStrings:
+ "Backup scan request for %s had no usable parameters (%u bytes); proceeding with no path filter"
+ "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, plugin:%s"
+ "Importer request has no FILE_PATH (parameters:%p); importing nothing"
+ "Scan request for %s had no usable parameters (%u bytes); proceeding with no path filter"
+ "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s typeExtension:%d bundleId:%s"
+ "~~~ bundleFinder importFile, request has no FILE_PATH (parameters:%p); importing nothing"
- "/Library/Mail/V4"
- "/Library/Mail/V5"
- "/Library/Mail/V6"
- "/Library/Mail/V7"
- "Could not activate sandbox profile at '%s'. sandbox_init() error %d: error:%s, home:%s, extra:%s, lib:%s, mail:%s, mail2:%s, plugin:%s"
- "_MAIL_V2"
- "sandbox profile activated time:%g uid:%d profile:%s cache:%s temp:%s home:%s lib:%s M:%s MV2:%s typeExtension:%d bundleId:%s"
```
