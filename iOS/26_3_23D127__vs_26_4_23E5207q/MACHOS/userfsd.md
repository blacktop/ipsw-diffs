## userfsd

> `/System/Library/PrivateFrameworks/UserFS.framework/userfsd`

```diff

-741.0.3.0.0
-  __TEXT.__text: 0x3904
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_stubs: 0x740
+741.100.13.0.0
+  __TEXT.__text: 0x382c
+  __TEXT.__auth_stubs: 0x3d0
+  __TEXT.__objc_stubs: 0x760
   __TEXT.__objc_methlist: 0x400
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x3f7
-  __TEXT.__oslogstring: 0x6a0
-  __TEXT.__objc_methname: 0x9e4
+  __TEXT.__cstring: 0x442
+  __TEXT.__oslogstring: 0x6d7
+  __TEXT.__objc_methname: 0xa00
   __TEXT.__objc_classname: 0xe2
-  __TEXT.__objc_methtype: 0x7d5
+  __TEXT.__objc_methtype: 0x7e1
   __TEXT.__gcc_except_tab: 0x25c
-  __TEXT.__unwind_info: 0x130
-  __DATA_CONST.__auth_got: 0x208
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__auth_got: 0x1f8
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x168
   __DATA_CONST.__cfstring: 0xc0

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0xc48
-  __DATA.__objc_selrefs: 0x330
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x240

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EF127101-17D1-3110-8DEB-D18A5000D643
-  Functions: 82
-  Symbols:   88
-  CStrings:  273
+  UUID: E3DE55AE-98E8-333D-B7B3-32F445DC96F3
+  Functions: 88
+  Symbols:   86
+  CStrings:  276
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x8
CStrings:
+ "%s: cleanup mounts of volume names (%@)"
+ "-[UVFSServiceNotifciations serviceExitingForDevice:volumeNames:withReply:]"
+ "cleanUpStateIfNeeded:kernelMounts: %@:volumeNames:%@"
+ "containsObject:"
+ "serviceExitingForDevice:volumeNames:withReply:"
+ "v40@0:8@\"NSString\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
- "cleanUpStateIfNeeded:kernelMounts: %@"
- "serviceExitingForDevice:withReply:"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"

```
