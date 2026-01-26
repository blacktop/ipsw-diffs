## storagekitd

> `/usr/libexec/storagekitd`

```diff

-1024.80.3.0.0
-  __TEXT.__text: 0x2d640
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_stubs: 0x62e0
-  __TEXT.__objc_methlist: 0x2914
+1024.80.4.0.0
+  __TEXT.__text: 0x2db24
+  __TEXT.__auth_stubs: 0xc50
+  __TEXT.__objc_stubs: 0x6300
+  __TEXT.__objc_methlist: 0x294c
   __TEXT.__objc_classname: 0x523
-  __TEXT.__objc_methname: 0x64c9
-  __TEXT.__objc_methtype: 0xfa0
+  __TEXT.__objc_methname: 0x6508
+  __TEXT.__objc_methtype: 0xfe9
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xc8c
-  __TEXT.__cstring: 0x2dc6
-  __TEXT.__oslogstring: 0x2670
-  __TEXT.__unwind_info: 0xa80
-  __DATA_CONST.__auth_got: 0x628
+  __TEXT.__cstring: 0x2e3b
+  __TEXT.__oslogstring: 0x26ab
+  __TEXT.__unwind_info: 0xa88
+  __DATA_CONST.__auth_got: 0x638
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xf60

   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x5f00
-  __DATA.__objc_selrefs: 0x1c70
+  __DATA.__objc_const: 0x5f30
+  __DATA.__objc_selrefs: 0x1c80
   __DATA.__objc_ivar: 0x2c0
   __DATA.__objc_data: 0xfa0
   __DATA.__data: 0x700

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: C6977189-8062-3DC2-B6F7-244B526E5B02
-  Functions: 908
-  Symbols:   372
-  CStrings:  2392
+  UUID: 183E0CA9-8151-30AD-93AE-D3415261A866
+  Functions: 912
+  Symbols:   374
+  CStrings:  2400
 
Symbols:
+ _devname_r
+ _fstatat
CStrings:
+ "%s: Can't get BSD name for %@"
+ "%s: fstatat of %@ failed: %s"
+ "-[SKDaemonConnection diskForPath:withCompletionUUID:]"
+ "-[SKDaemonManager diskForPath:withCallbackBlock:]_block_invoke"
+ "diskForPath:withCallbackBlock:"
+ "diskForPath:withCompletionUUID:"
+ "v32@0:8@\"NSString\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"SKDisk\">24"

```
