## storagekitd

> `/usr/libexec/storagekitd`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
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
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__common`

```diff

-1076.0.1.0.0
-  __TEXT.__text: 0x17cfa4
-  __TEXT.__auth_stubs: 0x2ed0
+1076.0.3.0.0
+  __TEXT.__text: 0x17d220
+  __TEXT.__auth_stubs: 0x2ee0
   __TEXT.__objc_stubs: 0xeb80
-  __TEXT.__objc_methlist: 0x7ec4
+  __TEXT.__objc_methlist: 0x7edc
   __TEXT.__const: 0xc88
-  __TEXT.__objc_methname: 0x14cb3
+  __TEXT.__objc_methname: 0x14cf3
   __TEXT.__oslogstring: 0x61c6
   __TEXT.__objc_classname: 0xd0d
   __TEXT.__objc_methtype: 0x5da7
-  __TEXT.__cstring: 0x60820
+  __TEXT.__cstring: 0x608f2
   __TEXT.__gcc_except_tab: 0x2544
-  __TEXT.__unwind_info: 0x2818
+  __TEXT.__unwind_info: 0x2828
   __TEXT.__eh_frame: 0x138
   __DATA_CONST.__const: 0x2ab0
-  __DATA_CONST.__cfstring: 0x3af20
+  __DATA_CONST.__cfstring: 0x3af60
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arrayobj: 0x8e8
   __DATA_CONST.__objc_dictobj: 0x5c8
   __DATA_CONST.__objc_intobj: 0x168
-  __DATA_CONST.__auth_got: 0x1778
+  __DATA_CONST.__auth_got: 0x1780
   __DATA_CONST.__got: 0xbb0
   __DATA_CONST.__auth_ptr: 0xb0
-  __DATA.__objc_const: 0xf198
-  __DATA.__objc_selrefs: 0x4518
-  __DATA.__objc_ivar: 0x9c4
+  __DATA.__objc_const: 0xf1c8
+  __DATA.__objc_selrefs: 0x4520
+  __DATA.__objc_ivar: 0x9c8
   __DATA.__objc_data: 0x28f0
   __DATA.__data: 0x918
   __DATA.__bss: 0x578

   - /usr/lib/libcsfde.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3576
-  Symbols:   1122
-  CStrings:  13859
+  Functions: 3579
+  Symbols:   1123
+  CStrings:  13866
 
Symbols:
+ _memcmp
CStrings:
+ ". picture file outside allowed dirs: canonical=%s"
+ ". picture file realpath failed: path=%@ errno=%d"
+ "/Library/User Pictures/"
+ "/System/Library/Templates/Data/Library/User Pictures/"
+ "T@\"SKDaemonConnection\",&,V_connection"
+ "_DMOpenUserPictureFileForPreboot"
+ "initWithDisk:snapshotName:mountPoint:connection:completionBlock:"
+ "setConnection:"
- "initWithDisk:snapshotName:mountPoint:completionBlock:"
```
