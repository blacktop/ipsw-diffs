## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-209.12.1.0.0
-  __TEXT.__text: 0x370c4
-  __TEXT.__auth_stubs: 0xd90
+209.13.1.0.0
+  __TEXT.__text: 0x37150
+  __TEXT.__auth_stubs: 0xda0
   __TEXT.__objc_methlist: 0x2a1c
   __TEXT.__const: 0x22a
-  __TEXT.__cstring: 0x4f8d
-  __TEXT.__oslogstring: 0x3305
+  __TEXT.__cstring: 0x4fad
+  __TEXT.__oslogstring: 0x3347
   __TEXT.__gcc_except_tab: 0xdcc
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x1328
-  __AUTH_CONST.__auth_got: 0x6d8
+  __AUTH_CONST.__auth_got: 0x6e0
   __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__cfstring: 0x5820
   __AUTH_CONST.__objc_const: 0x6c38

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 588E01EF-BD00-3089-AC38-B56DB421CC0D
-  Functions: 1231
-  Symbols:   4615
-  CStrings:  3045
+  UUID: FC26AECD-4059-39E4-8EBC-6C2D399E86CF
+  Functions: 1232
+  Symbols:   4618
+  CStrings:  3047
 
Symbols:
+ -[_BMDirectFileManager _fileHandleForFileAtPath:flags:protection:error:].cold.3
+ _fsetxattr
Functions:
~ -[_BMDirectFileManager _fileHandleForFileAtPath:flags:protection:error:] : 1236 -> 1332
+ -[_BMDirectFileManager _fileHandleForFileAtPath:flags:protection:error:].cold.2
CStrings:
+ "Unable to set extended attribute allowing locking while suspended"
+ "com.apple.runningboard.can-suspend-locked"

```
