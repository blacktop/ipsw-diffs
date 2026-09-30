## livefiles_hfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_hfs.dylib`

```diff

 715.160.9.0.0
-  __TEXT.__text: 0x3dd00
+  __TEXT.__text: 0x3dd80
   __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x4e60
-  __TEXT.__oslogstring: 0x5cc6
+  __TEXT.__oslogstring: 0x5d0d
   __TEXT.__cstring: 0x26fb
   __TEXT.__unwind_info: 0x6d0
   __DATA_CONST.__got: 0x30

   - /usr/lib/libSystem.B.dylib
   Functions: 678
   Symbols:   647
-  CStrings:  739
+  CStrings:  740
 
Functions:
~ _HeadTruncateFile : 1276 -> 1404
CStrings:
+ "HeadTruncateFile: too many tail extents, marking volume inconsistent.\n"
```
