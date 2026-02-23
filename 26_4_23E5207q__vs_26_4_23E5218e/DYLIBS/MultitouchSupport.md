## MultitouchSupport

> `/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport`

```diff

-9140.1.0.0.0
-  __TEXT.__text: 0x1e2f0
+9140.3.0.0.0
+  __TEXT.__text: 0x1e404
   __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__const: 0x1ff8
   __TEXT.__cstring: 0x169e
-  __TEXT.__oslogstring: 0x10b8
+  __TEXT.__oslogstring: 0x1136
   __TEXT.__tpad_act_plist: 0xe22d
   __TEXT.__unwind_info: 0x6e0
   __TEXT.__objc_classname: 0x49

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 766BDC93-3106-3C7C-8D8F-CBE06B80F9D1
+  UUID: AAC15E04-BBA2-3570-84D6-BA0B6ED2BD5E
   Functions: 668
   Symbols:   1430
-  CStrings:  617
+  CStrings:  619
 
Functions:
~ _mt_UncompressTouchpadCodecV1Force : 384 -> 624
~ _MTParse_CompactV10BinaryPath : 380 -> 456
~ _MTProcess_0xC5_Data : 388 -> 348
CStrings:
+ "Force sensor position(%d) exceeded the force pixel count(%d)"
+ "Raw force sensor position(%d) exceeded the force pixel count(%d)"

```
