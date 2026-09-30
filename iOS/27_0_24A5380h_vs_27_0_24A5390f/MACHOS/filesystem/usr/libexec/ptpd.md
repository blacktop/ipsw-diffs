## ptpd

> `/usr/libexec/ptpd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2114.0.0.0.0
-  __TEXT.__text: 0x224f0
+2116.0.0.0.0
+  __TEXT.__text: 0x22818
   __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x4160
-  __TEXT.__objc_methlist: 0x1a30
+  __TEXT.__objc_stubs: 0x41a0
+  __TEXT.__objc_methlist: 0x1a80
   __TEXT.__const: 0x4c
   __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__cstring: 0x252d
-  __TEXT.__objc_methname: 0x4e95
+  __TEXT.__cstring: 0x259a
+  __TEXT.__objc_methname: 0x4f63
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0xc32
   __TEXT.__objc_classname: 0xef
   __TEXT.__objc_methtype: 0x8a3
-  __TEXT.__unwind_info: 0x5c0
-  __DATA_CONST.__const: 0x3e0
-  __DATA_CONST.__cfstring: 0x3200
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__const: 0x408
+  __DATA_CONST.__cfstring: 0x3260
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20

   __DATA_CONST.__auth_got: 0x510
   __DATA_CONST.__got: 0x220
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x25d8
-  __DATA.__objc_selrefs: 0x1600
-  __DATA.__objc_ivar: 0x280
+  __DATA.__objc_const: 0x26c8
+  __DATA.__objc_selrefs: 0x1628
+  __DATA.__objc_ivar: 0x284
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x1b0
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 610
+  Functions: 615
   Symbols:   238
-  CStrings:  1577
+  CStrings:  1588
 
CStrings:
+ "%@\n%@"
+ "Stopping group notifications for storage 0x%x."
+ "Storage torn down -- not re-arming group notifications."
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",C,N,V_mediaItemIdentifier"
+ "U"
+ "_mediaItemIdentifier"
+ "cameraFileWithAssetIdentifier:"
+ "mediaItemIdentifier"
+ "mediaItemIdentifierForAsset:"
+ "mediaItemWithIdentifier:"
+ "setMediaItemIdentifier:"
+ "stopGroupNotifications"
- "T"
- "objectMatchingAssetHandle:"
```
