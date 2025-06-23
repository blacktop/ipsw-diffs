## tailspind

> `/usr/libexec/tailspind`

```diff

-234.0.0.0.0
-  __TEXT.__text: 0xd544
+237.0.0.0.0
+  __TEXT.__text: 0xd454
   __TEXT.__auth_stubs: 0xbc0
-  __TEXT.__objc_stubs: 0x920
-  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__objc_stubs: 0x960
+  __TEXT.__objc_methlist: 0x1f4
   __TEXT.__const: 0x12c
-  __TEXT.__cstring: 0x100c
-  __TEXT.__objc_methname: 0xc06
-  __TEXT.__oslogstring: 0x25ba
-  __TEXT.__objc_classname: 0x17
+  __TEXT.__cstring: 0xff9
+  __TEXT.__objc_methname: 0xc42
+  __TEXT.__oslogstring: 0x25d3
+  __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methtype: 0xfb
   __TEXT.__gcc_except_tab: 0x238
   __TEXT.__unwind_info: 0x390

   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x408
-  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__cfstring: 0x5c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2d0
-  __DATA.__objc_selrefs: 0x2e0
-  __DATA.__objc_ivar: 0x30
+  __DATA.__objc_const: 0x300
+  __DATA.__objc_selrefs: 0x2f0
+  __DATA.__objc_ivar: 0x34
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x2160
   __DATA.__crash_info: 0x148

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 591A5355-AD80-31E1-8AF6-7622BF104407
-  Functions: 243
+  UUID: 3D08932A-DB1D-33F6-BB61-5505F4A9D107
+  Functions: 244
   Symbols:   242
-  CStrings:  482
+  CStrings:  485
 
CStrings:
+ "Detected fd %d from %s [%d] with non-zero file size %lld!"
+ "Detected fd %d from %{public}s [%d] with non-zero file size %lld! Path: %{public}@"
+ "FAILED due to reason: %{public}@.\nFile path: %{public}@"
+ "Save from %s [%d] exceeded %ds timeout! Size: %lld"
+ "Save from %{public}s [%d] (request ID %llu) exceeded %ds timeout! Size: %lld, Path: %{public}@"
+ "Succeeded.\nFile path: %{public}@"
+ "T@\"NSString\",&,N,V_filePath"
+ "_filePath"
+ "filePath"
+ "setFilePath:"
- "11"
- "Detected fd %d from %s [%d] with non-zero file size %lld! Path: %s"
- "Detected fd %d from %{public}s [%d] with non-zero file size %lld! Path: %s"
- "FAILED due to reason: %{public}@"
- "Received request for fd %d, path: %s"
- "Save from %s [%d] exceeded %ds timeout! Size: %lld, Path: %s"
- "Save from %{public}s [%d] (request ID %llu) exceeded %ds timeout! Size: %lld, Path: %s"

```
