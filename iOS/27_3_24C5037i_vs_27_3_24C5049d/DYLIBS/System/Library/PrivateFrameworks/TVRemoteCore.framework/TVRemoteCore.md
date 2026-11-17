## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-627.20.10.0.0
-  __TEXT.__text: 0x489f8
+627.20.15.0.0
+  __TEXT.__text: 0x48c24
   __TEXT.__lazy_helpers: 0x5d4
-  __TEXT.__objc_methlist: 0x6910
+  __TEXT.__objc_methlist: 0x6920
   __TEXT.__const: 0x252
-  __TEXT.__oslogstring: 0x7055
+  __TEXT.__oslogstring: 0x716a
   __TEXT.__cstring: 0x3853
   __TEXT.__gcc_except_tab: 0xbb4
   __TEXT.__unwind_info: 0x18c8

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3388
+  __DATA_CONST.__objc_selrefs: 0x3390
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x480
   __AUTH_CONST.__cfstring: 0x4bc0
-  __AUTH_CONST.__objc_const: 0xa2a0
+  __AUTH_CONST.__objc_const: 0xa2a8
   __AUTH_CONST.__lazy_load_got: 0x88
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/swift/libswift_Builtin_float.dylib
   Functions: 2166
   Symbols:   3764
-  CStrings:  1331
+  CStrings:  1333
 
Functions:
~ -[TVRCKeyboardController _setCurrentState:] : 504 -> 916
~ ___36-[TVRCXPCClient deviceUpdatedState:]_block_invoke : 132 -> 276
CStrings:
+ "Keyboard state update: wasEditing %{bool}d, editing %{bool}d, old attributes %p (payload %{public}@, %lu bytes), new attributes %p (payload %{public}@, %lu bytes), same object %{bool}d, equal %{bool}d"
+ "finished delivering state update for %{public}@ (keyboard editing %{bool}d)"
```
