## storagekitd

> `/usr/libexec/storagekitd`

```diff

-934.82.1.0.0
-  __TEXT.__text: 0x2d5e0
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_stubs: 0x61e0
-  __TEXT.__objc_methlist: 0x23e4
+934.100.30.0.0
+  __TEXT.__text: 0x2d528
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_stubs: 0x61c0
+  __TEXT.__objc_methlist: 0x2854
   __TEXT.__objc_classname: 0x50d
-  __TEXT.__objc_methname: 0x63a2
-  __TEXT.__objc_methtype: 0xf79
+  __TEXT.__objc_methname: 0x637a
+  __TEXT.__objc_methtype: 0xf6e
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0xc7c
-  __TEXT.__cstring: 0x2cea
-  __TEXT.__oslogstring: 0x2742
+  __TEXT.__cstring: 0x2d70
+  __TEXT.__oslogstring: 0x26ee
   __TEXT.__unwind_info: 0xa48
-  __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0xe88
-  __DATA_CONST.__cfstring: 0x1ea0
+  __DATA_CONST.__auth_got: 0x628
+  __DATA_CONST.__got: 0x508
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0xe60
+  __DATA_CONST.__cfstring: 0x1f20
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_dictobj: 0x1b8
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x6590
-  __DATA.__objc_selrefs: 0x1b98
-  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_const: 0x5d50
+  __DATA.__objc_selrefs: 0x1c30
+  __DATA.__objc_ivar: 0x2ac
   __DATA.__objc_data: 0xf50
   __DATA.__data: 0x760
   __DATA.__bss: 0x98

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 883
-  Symbols:   368
-  CStrings:  2147
+  Functions: 890
+  Symbols:   370
+  CStrings:  2145
 
Symbols:
+ _DADiskClaim
+ _DADiskUnclaim
+ _objc_retainAutoreleasedReturnValue
- _OBJC_CLASS_$_NSTimer
CStrings:
+ "\x03\x12\x11\x16\x19\x12"
+ "Mount options must be a dictionary"
+ "Mount point must be a string"
+ "Mount tool options must be an array"
+ "Multiple disks to mount, cannot specify mount point"
+ "errorWithPOSIXCode:debugDescription:error:"
- "\x03\x12\x11\x17\x19\x12"
- "%s: Multiple disks to mount, cannot specify mount point"
- "@\"NSTimer\""
- "Timeout waiting for DA idle"
- "daForceIdleTimer"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "startForceIdleTimer"
- "v16@?0@\"NSTimer\"8"

```
