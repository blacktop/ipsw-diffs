## fskit_helper

> `/usr/libexec/fskit_helper`

```diff

-470.40.4.0.0
-  __TEXT.__text: 0x192c
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0x320
+474.60.39.0.0
+  __TEXT.__text: 0x1510
+  __TEXT.__auth_stubs: 0x2e0
+  __TEXT.__objc_stubs: 0x300
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x1ba
+  __TEXT.__cstring: 0x161
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methname: 0x3a0
-  __TEXT.__objc_methtype: 0x219
-  __TEXT.__oslogstring: 0x3c4
-  __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__const: 0x50
-  __TEXT.__unwind_info: 0xd8
-  __DATA_CONST.__auth_got: 0x1a0
+  __TEXT.__objc_methname: 0x365
+  __TEXT.__objc_methtype: 0x1b1
+  __TEXT.__oslogstring: 0x30c
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__const: 0x40
+  __TEXT.__unwind_info: 0xc0
+  __DATA_CONST.__auth_got: 0x180
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__const: 0x50
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA.__objc_const: 0x518
-  __DATA.__objc_selrefs: 0xe8
+  __DATA.__objc_selrefs: 0xe0
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x120
   __DATA.__common: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 34
-  Symbols:   67
-  CStrings:  115
+  Functions: 26
+  Symbols:   63
+  CStrings:  107
 
Symbols:
- __Block_object_dispose
- _objc_retain_x21
- _wipefs_except_blocks
- _wipefs_include_blocks
CStrings:
+ "%!s(MISSING):reply(EINVAL): Can't find queue for BSD name (%!@(MISSING)), resource wasn't opened or was revoked already"
+ "-[FSKitHelper wipeFS:replyHandler:]"
+ "-[FSKitHelper wipeFS:replyHandler:]_block_invoke"
+ "wipeFS:replyHandler:"
- "%!s(MISSING):reply(EINVAL): Can't find queue for BSD name (%!@(MISSING)), resouce wasn't opened or was revoked already"
- "-[FSKitHelper wipeFS:includingRanges:excludingRanges:replyHandler:]"
- "-[FSKitHelper wipeFS:includingRanges:excludingRanges:replyHandler:]_block_invoke"
- "FSKitHelper:wipeFS:wipefs_except_blocks:%!s(MISSING)"
- "FSKitHelper:wipeFS:wipefs_except_blocks::%!l(MISSING)u.%!l(MISSING)u"
- "FSKitHelper:wipeFS:wipefs_include_blocks:%!l(MISSING)u.%!l(MISSING)u"
- "FSKitHelper:wipeFS:wipefs_include_blocks:%!s(MISSING)"
- "enumerateRangesUsingBlock:"
- "v32@?0{_NSRange=QQ}8^B24"
- "v48@0:8@\"FSBlockDeviceResource\"16@\"NSIndexSet\"24@\"NSIndexSet\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "wipeFS:includingRanges:excludingRanges:replyHandler:"

```
