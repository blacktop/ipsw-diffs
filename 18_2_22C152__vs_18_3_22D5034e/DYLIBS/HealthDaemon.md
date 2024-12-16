## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-5200.2.12.1.1
-  __TEXT.__text: 0x7638dc
+5200.3.4.0.0
+  __TEXT.__text: 0x7638e8
   __TEXT.__auth_stubs: 0x3730
   __TEXT.__objc_methlist: 0x3cda0
   __TEXT.__const: 0x1c38c

   __TEXT.__swift5_typeref: 0x387
   __TEXT.__swift5_fieldmd: 0x20c
   __TEXT.__constg_swiftt: 0x4fc
-  __TEXT.__cstring: 0x76609
+  __TEXT.__cstring: 0x76696
   __TEXT.__swift5_reflstr: 0x1b0
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_protos: 0x8

   __AUTH_CONST.__auth_got: 0x1bb0
   __AUTH_CONST.__auth_ptr: 0xa8
   __AUTH_CONST.__const: 0xdc98
-  __AUTH_CONST.__cfstring: 0x3c860
+  __AUTH_CONST.__cfstring: 0x3c880
   __AUTH_CONST.__objc_const: 0x83b70
   __AUTH_CONST.__objc_arrayobj: 0x1ef0
   __AUTH_CONST.__objc_intobj: 0x4440

   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 33372
   Symbols:   39913
-  CStrings:  35776
+  CStrings:  35777
 
CStrings:
+ "UPDATE sqlite_sequence SET seq=(SELECT seq FROM sqlite_sequence WHERE name = 'associations') WHERE sqlite_sequence.name = 'associations_new'"

```
