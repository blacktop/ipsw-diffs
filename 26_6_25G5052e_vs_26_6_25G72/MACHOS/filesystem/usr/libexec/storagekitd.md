## storagekitd

> `/usr/libexec/storagekitd`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__common`

```diff

-1037.120.10.0.0
-  __TEXT.__text: 0x194fd4
+1037.160.3.0.0
+  __TEXT.__text: 0x194c0c
   __TEXT.__auth_stubs: 0x2ec0
-  __TEXT.__objc_stubs: 0xef40
-  __TEXT.__objc_methlist: 0x80e4
+  __TEXT.__objc_stubs: 0xef00
+  __TEXT.__objc_methlist: 0x80f4
   __TEXT.__const: 0xc98
-  __TEXT.__objc_methname: 0x158f8
+  __TEXT.__objc_methname: 0x158e2
   __TEXT.__oslogstring: 0x6407
   __TEXT.__objc_classname: 0xd84
-  __TEXT.__objc_methtype: 0x6348
+  __TEXT.__objc_methtype: 0x631b
   __TEXT.__gcc_except_tab: 0x2718
-  __TEXT.__cstring: 0x68390
-  __TEXT.__unwind_info: 0x2af0
+  __TEXT.__cstring: 0x680c4
+  __TEXT.__unwind_info: 0x2af8
   __TEXT.__eh_frame: 0x168
   __DATA_CONST.__auth_got: 0x1770
   __DATA_CONST.__got: 0xb48
   __DATA_CONST.__auth_ptr: 0xb0
   __DATA_CONST.__const: 0x2b80
-  __DATA_CONST.__cfstring: 0x3f9c0
+  __DATA_CONST.__cfstring: 0x3f7a0
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arrayobj: 0x990
   __DATA_CONST.__objc_dictobj: 0x5c8
   __DATA_CONST.__objc_intobj: 0x180
-  __DATA.__objc_const: 0xf610
-  __DATA.__objc_selrefs: 0x4630
-  __DATA.__objc_ivar: 0xa28
+  __DATA.__objc_const: 0xf640
+  __DATA.__objc_selrefs: 0x4628
+  __DATA.__objc_ivar: 0xa2c
   __DATA.__objc_data: 0x2990
   __DATA.__data: 0x918
   __DATA.__bss: 0x578

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3621
+  Functions: 3622
   Symbols:   1120
-  CStrings:  14587
+  CStrings:  14568
 
CStrings:
+ "T@\"SKDaemonConnection\",&,V_connection"
+ "initWithDisk:snapshotName:mountPoint:connection:completionBlock:"
+ "setConnection:"
- "-[DMToolRepairDiskPART checkForAppleVendorDirInESPUDS:needsRemoval:doRemove:detailError:]"
- "APPLE"
- "Checking the EFI system partition's folder content"
- "FSO exists but is not a dir, and authorized to remove, so: deleting FSO"
- "appleFSONeedsRemoval=%d"
- "checkForAppleVendorDirInESPUDS:needsRemoval:doRemove:detailError:"
- "checking for a dir at path=%@"
- "checking for a dir at path=%@ using stat"
- "did checkForAppleVendorDirInESPUDS; eDirsNotOK=%d"
- "did delete; err=%@"
- "did mount ESP in custom place"
- "did unmount ESP"
- "doing checkForAppleVendorDirInESPUDS; authorizedToDoFix=%d"
- "efiFSONeedsRemoval=%d"
- "i44@0:8^{DMUDSPrivRec=Qq[150c]}16^B24B32^i36"
- "inESPUDS=%@"
- "initWithDisk:snapshotName:mountPoint:completionBlock:"
- "pathWithComponents:"
- "retErr=%d outNeedsRemoval=%d outDetailErr=%d"
- "stat return code is %d"
- "{ESP}/EFI/: aFSOExists=%d statbuf.st_mode=%08X aFSOIsDir=%d"
- "{ESP}/EFI/APPLE/: aFSOExists=%d statbuf.st_mode=%08X aFSOIsDir=%d"
```
