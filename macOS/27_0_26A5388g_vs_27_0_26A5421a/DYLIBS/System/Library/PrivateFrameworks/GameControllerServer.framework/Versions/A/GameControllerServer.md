## GameControllerServer

> `/System/Library/PrivateFrameworks/GameControllerServer.framework/Versions/A/GameControllerServer`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-14.0.21.0.0
-  __TEXT.__text: 0x16174
+14.0.24.0.0
+  __TEXT.__text: 0x161d8
   __TEXT.__objc_methlist: 0x10e4
   __TEXT.__const: 0x522
-  __TEXT.__gcc_except_tab: 0x1968
+  __TEXT.__gcc_except_tab: 0x1974
   __TEXT.__cstring: 0xb14
   __TEXT.__oslogstring: 0x12b9
   __TEXT.__swift5_typeref: 0x392

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xac8
+  __DATA_CONST.__objc_selrefs: 0xad0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x220
   __AUTH_CONST.__const: 0x7a8
   __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x2948
+  __AUTH_CONST.__objc_const: 0x2968
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0x600
   __AUTH.__objc_data: 0x570
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1f0
+  __DATA.__objc_ivar: 0x1f4
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x350
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 493
-  Symbols:   1575
+  Symbols:   1577
   CStrings:  217
 
Symbols:
+ OBJC_IVAR_$__GCHapticLogicalDevice._hapticsPlaying
+ _objc_msgSend$endHaptics
Functions:
~ -[_GCHapticServerManager processActiveEventsForStartTime:endTime:] : 2504 -> 2596
~ -[_GCHapticLogicalDevice stopAllHaptics] : 216 -> 224
```
