## storagekitd

> `/usr/libexec/storagekitd`

```diff

-  __TEXT.__text: 0x17d3bc
-  __TEXT.__auth_stubs: 0x2ec0
-  __TEXT.__objc_stubs: 0xebc0
-  __TEXT.__objc_methlist: 0x7ecc
+  __TEXT.__text: 0x17cfa4
+  __TEXT.__auth_stubs: 0x2ed0
+  __TEXT.__objc_stubs: 0xeb80
+  __TEXT.__objc_methlist: 0x7ec4
   __TEXT.__const: 0xc88
-  __TEXT.__objc_methname: 0x14d09
-  __TEXT.__oslogstring: 0x61a1
+  __TEXT.__objc_methname: 0x14cb3
+  __TEXT.__oslogstring: 0x61c6
   __TEXT.__objc_classname: 0xd0d
-  __TEXT.__objc_methtype: 0x5dd4
-  __TEXT.__cstring: 0x60acc
+  __TEXT.__objc_methtype: 0x5da7
+  __TEXT.__cstring: 0x60820
   __TEXT.__gcc_except_tab: 0x2544
   __TEXT.__unwind_info: 0x2818
   __TEXT.__eh_frame: 0x138
   __DATA_CONST.__const: 0x2ab0
-  __DATA_CONST.__cfstring: 0x3b140
+  __DATA_CONST.__cfstring: 0x3af20
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arrayobj: 0x8e8
   __DATA_CONST.__objc_dictobj: 0x5c8
   __DATA_CONST.__objc_intobj: 0x168
-  __DATA_CONST.__auth_got: 0x1770
-  __DATA_CONST.__got: 0xb50
+  __DATA_CONST.__auth_got: 0x1778
+  __DATA_CONST.__got: 0xbb0
   __DATA_CONST.__auth_ptr: 0xb0
   __DATA.__objc_const: 0xf198
-  __DATA.__objc_selrefs: 0x4528
+  __DATA.__objc_selrefs: 0x4518
   __DATA.__objc_ivar: 0x9c4
   __DATA.__objc_data: 0x28f0
   __DATA.__data: 0x918

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 3576
-  Symbols:   1121
-  CStrings:  21499
+  Symbols:   1122
+  CStrings:  21463
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__common : content changed
Symbols:
+ _DARegisterExitCallback
CStrings:
+ "%s: Received DA daemon exit callback"
+ "void DaemonExitCallback(void *)"
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
- "pathWithComponents:"
- "retErr=%d outNeedsRemoval=%d outDetailErr=%d"
- "stat return code is %d"
- "{ESP}/EFI/: aFSOExists=%d statbuf.st_mode=%08X aFSOIsDir=%d"
- "{ESP}/EFI/APPLE/: aFSOExists=%d statbuf.st_mode=%08X aFSOIsDir=%d"

```
