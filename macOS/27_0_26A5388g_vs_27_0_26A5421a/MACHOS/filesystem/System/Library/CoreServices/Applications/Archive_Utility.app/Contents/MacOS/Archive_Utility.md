## Archive Utility

> `/System/Library/CoreServices/Applications/Archive Utility.app/Contents/MacOS/Archive Utility`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-182.0.0.0.0
-  __TEXT.__text: 0x2dba4
-  __TEXT.__auth_stubs: 0x10f0
-  __TEXT.__objc_stubs: 0x43c0
-  __TEXT.__objc_methlist: 0x1dd0
-  __TEXT.__cstring: 0x50e2
+183.0.0.0.0
+  __TEXT.__text: 0x2e338
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_stubs: 0x44c0
+  __TEXT.__objc_methlist: 0x1ea8
+  __TEXT.__cstring: 0x520e
   __TEXT.__const: 0x14c4
-  __TEXT.__gcc_except_tab: 0x24e8
-  __TEXT.__objc_methname: 0x5929
+  __TEXT.__gcc_except_tab: 0x258c
+  __TEXT.__objc_methname: 0x5a24
   __TEXT.__objc_classname: 0x4fb
-  __TEXT.__objc_methtype: 0x1170
+  __TEXT.__objc_methtype: 0x11ac
   __TEXT.__ustring: 0xa04
-  __TEXT.__unwind_info: 0xc90
-  __DATA_CONST.__const: 0x1290
-  __DATA_CONST.__cfstring: 0x2d80
+  __TEXT.__unwind_info: 0xcc8
+  __DATA_CONST.__const: 0x12b0
+  __DATA_CONST.__cfstring: 0x2e00
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x890
+  __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0x2a0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x2fb0
-  __DATA.__objc_selrefs: 0x1818
-  __DATA.__objc_ivar: 0x278
+  __DATA.__objc_const: 0x2fe8
+  __DATA.__objc_selrefs: 0x1858
+  __DATA.__objc_ivar: 0x27c
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x468
   __DATA.__common: 0x288

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 725
-  Symbols:   354
-  CStrings:  2307
+  Functions: 743
+  Symbols:   355
+  CStrings:  2323
 
Symbols:
+ __qtn_file_apply_to_fd
+ __qtn_file_init_with_fd
+ _dup
- __qtn_file_apply_to_path
- __qtn_file_init_with_path
CStrings:
+ "-_propagateQuarantineInformation: DSQuarantine error on %@: %@"
+ "-_propagateQuarantineInformation: DSQuarantine error on root %@: %@"
+ "@28@0:8i16^i20"
+ "B24@0:8^i16"
+ "B32@0:8@16^@24"
+ "TB,V_isIntermediateItem"
+ "Ti,R,N,V_sourceFD"
+ "_isIntermediateItem"
+ "_openSecureSourceDescriptor:"
+ "_sourceFD"
+ "copyQuarantineInfoFrom: %@ - cannot open source (%d)\n"
+ "copyQuarantineInfoFrom: %@ - cannot open target (%d)\n"
+ "defaultQuarantineData"
+ "enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:"
+ "intermediateWorkItemForRecursion"
+ "intermediateWorkItemForRecursion: XPC error: %@"
+ "isDearchivable:whichController:"
+ "isDearchivable:whichController:updateIsolation:"
+ "isIntermediateItem"
+ "needsPinnedSourceDescriptor"
+ "readOnlyWrapperForIntermediateItem:withReply:"
+ "readsSourceQuarantineInProcess"
+ "serializedQuarantineForDescriptor: qtn_file_init_with_fd = %d"
+ "serializedQuarantineForDescriptor:quarantineError:"
+ "setIsIntermediateItem:"
+ "sourceDescriptor"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSSecurityScopedURLWrapper\">24"
- "B40@0:8@16^@24B32B36"
- "TB,V_srcIsIntermediateItem"
- "_srcIsIntermediateItem"
- "copyQuarantine"
- "dearchiveItem:withController:isIntermediateItem:"
- "isDearchivable:whichController:isIntermediateItem:"
- "isDearchivable:whichController:isIntermediateItem:updateIsolation:"
- "qtn_file_init_with_path = %d (%s)"
- "setSrcIsIntermediateItem:"
- "srcIsIntermediateItem"
- "v36@0:8@16@24B32"
```
