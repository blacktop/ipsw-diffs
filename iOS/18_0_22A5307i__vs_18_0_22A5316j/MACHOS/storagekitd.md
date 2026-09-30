## storagekitd

> `/usr/libexec/storagekitd`

```diff

-934.0.0.0.0
-  __TEXT.__text: 0x2d500
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_stubs: 0x6140
-  __TEXT.__objc_methlist: 0x23cc
+934.0.6.0.0
+  __TEXT.__text: 0x2d298
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_stubs: 0x6120
+  __TEXT.__objc_methlist: 0x23c4
   __TEXT.__objc_classname: 0x4f5
-  __TEXT.__objc_methname: 0x634a
-  __TEXT.__objc_methtype: 0xfa3
+  __TEXT.__objc_methname: 0x6301
+  __TEXT.__objc_methtype: 0xf98
   __TEXT.__const: 0x90
-  __TEXT.__gcc_except_tab: 0xd40
-  __TEXT.__cstring: 0x2d13
-  __TEXT.__oslogstring: 0x27b7
-  __TEXT.__info_plist: 0x448
+  __TEXT.__gcc_except_tab: 0xd4c
+  __TEXT.__cstring: 0x2cb4
+  __TEXT.__oslogstring: 0x2742
+  __TEXT.__info_plist: 0x451
   __TEXT.__unwind_info: 0xa48
-  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__auth_got: 0x610
   __DATA_CONST.__got: 0x510
   __DATA_CONST.__const: 0xe88
-  __DATA_CONST.__cfstring: 0x1e80
+  __DATA_CONST.__cfstring: 0x1e20
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x18
   __DATA.__objc_const: 0x65a0
-  __DATA.__objc_selrefs: 0x1b70
+  __DATA.__objc_selrefs: 0x1b68
   __DATA.__objc_ivar: 0x2b0
   __DATA.__objc_data: 0xf50
   __DATA.__data: 0x700

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 880
-  Symbols:   373
-  CStrings:  2150
+  Symbols:   367
+  CStrings:  2140
 
Symbols:
- _close
- _ioctl
- _open
- _wipefs_alloc
- _wipefs_free
- _wipefs_wipe
CStrings:
+ "%!s(MISSING): Failed to reProbe %!@(MISSING) (LiveFS), %!@(MISSING)"
+ "%!s(MISSING): Failed to reProbe %!@(MISSING), %!@(MISSING)"
+ "-[SKFSTaskMessageHandler completed:replyHandler:]"
+ "getSectorSize"
+ "removePostProcessWithCachedDisk:"
+ "requiresEraseDiskForAPFS"
- "%!s(MISSING): Failed to get block size of %!@(MISSING), ioctl err %!d(MISSING)"
- "%!s(MISSING): Failed to get block size of %!@(MISSING), open err %!d(MISSING)"
- "+[SKPartitionTable getSectorSizeWithDisk:]"
- "-[SKFSTaskMessageHandler completed:reply:]"
- "Failed to open disk"
- "Failed to reProbe %!@(MISSING) (which contains an encrypted volume), %!@(MISSING)"
- "Failed to reProbe %!@(MISSING), %!@(MISSING)"
- "I24@0:8@16"
- "childCount"
- "failWithPOSIXCode:debugDescription:error:"
- "getSectorSizeWithDisk:"
- "prompt:reply:"
- "promptTrueFalse:reply:"
- "supportedPartitionSchemeForAPFS"
- "wipefs_alloc failed"
- "wipefs_wipe failed"

```
