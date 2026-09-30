## ContextSync

> `/System/Library/PrivateFrameworks/ContextSync.framework/Versions/A/ContextSync`

```diff

-165.7.0.0.0
-  __TEXT.__text: 0x122ac
+166.17.1.0.0
+  __TEXT.__text: 0x12154
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x938
+  __TEXT.__objc_methlist: 0xca4
   __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x450
   __TEXT.__cstring: 0xc63
   __TEXT.__oslogstring: 0x104b
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_classname: 0x279
   __TEXT.__objc_methname: 0x2e3d
   __TEXT.__objc_methtype: 0x1052

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x940
+  __DATA_CONST.__objc_selrefs: 0xaa8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x340
   __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x1c70
+  __AUTH_CONST.__objc_const: 0x15f0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x3c0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 71D0BC3B-0D49-3E68-9174-6C771F5C1FC1
+  UUID: BBE4E23A-1179-355F-9C3E-D9208B1D2167
   Functions: 342
   Symbols:   929
   CStrings:  840
Symbols:
+ +[BMDistributedContextService distributedContextManager].cold.1
+ +[BMDistributedContextStreamWriter sharedEventQueue].cold.1
- -[BMDSL bmdsl_serialize].cold.1
- -[NSData bmdsl_deserialize].cold.1

```
