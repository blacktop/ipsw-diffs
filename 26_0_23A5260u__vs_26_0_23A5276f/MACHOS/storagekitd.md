## storagekitd

> `/usr/libexec/storagekitd`

```diff

-1000.0.0.0.0
-  __TEXT.__text: 0x2d750
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_stubs: 0x6220
-  __TEXT.__objc_methlist: 0x2874
+1014.0.0.0.1
+  __TEXT.__text: 0x2d624
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_stubs: 0x6280
+  __TEXT.__objc_methlist: 0x2884
   __TEXT.__objc_classname: 0x4fc
-  __TEXT.__objc_methname: 0x6419
-  __TEXT.__objc_methtype: 0xf6e
+  __TEXT.__objc_methname: 0x6427
+  __TEXT.__objc_methtype: 0xf25
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xc8c
-  __TEXT.__cstring: 0x2d66
-  __TEXT.__oslogstring: 0x2745
-  __TEXT.__unwind_info: 0xa58
-  __DATA_CONST.__auth_got: 0x630
+  __TEXT.__cstring: 0x2d8a
+  __TEXT.__oslogstring: 0x2768
+  __TEXT.__unwind_info: 0xa60
+  __DATA_CONST.__auth_got: 0x628
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xec8
-  __DATA_CONST.__cfstring: 0x1f20
+  __DATA_CONST.__const: 0xef0
+  __DATA_CONST.__cfstring: 0x1f60
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5d68
-  __DATA.__objc_selrefs: 0x1c58
-  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_const: 0x5d90
+  __DATA.__objc_selrefs: 0x1c60
+  __DATA.__objc_ivar: 0x2b4
   __DATA.__objc_data: 0xf50
   __DATA.__data: 0x700
   __DATA.__bss: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: DA83CB25-A84A-3576-86FA-CF664A77D0AE
-  Functions: 895
-  Symbols:   373
-  CStrings:  2386
+  UUID: 53926604-AD00-318C-9846-2281E85E2245
+  Functions: 896
+  Symbols:   372
+  CStrings:  2392
 
Symbols:
+ _chown
- _devname_r
- _fstatat
CStrings:
+ "%s: Building filesystems array"
+ "%s: Received sync request"
+ "%s: chown on %@ failed with errno %d"
+ "-[SKDaemonConnection chownFileAtURL:error:]"
+ "-[SKDaemonConnection filesystemsWithCallbackBlock:]"
+ "-[SKDaemonConnection syncAllDisksWithCompletionBlock:]"
+ "Chown operation failed"
+ "Invalid URL for chown operation"
+ "T@\"NSMutableArray\",&,N,V_mountArgs"
+ "_mountArgs"
+ "arrayWithArray:"
+ "chownFileAtURL:error:"
+ "mountArgs"
+ "setMountArgs:"
- "%s: Can't get BSD name for %@"
- "%s: fstatat of %@ failed: %s"
- "-[SKDaemonConnection diskForPath:withCompletionUUID:]"
- "-[SKDaemonConnection filesystemsWithCompletionUUID:]"
- "-[SKDaemonManager diskForPath:withCallbackBlock:]_block_invoke"
- "diskForPath:withCallbackBlock:"
- "diskForPath:withCompletionUUID:"
- "filesystemsWithCompletionUUID:"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"SKDisk\">24"

```
