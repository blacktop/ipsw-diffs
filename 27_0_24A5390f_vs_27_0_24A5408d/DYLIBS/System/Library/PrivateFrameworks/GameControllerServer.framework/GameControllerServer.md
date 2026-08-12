## GameControllerServer

> `/System/Library/PrivateFrameworks/GameControllerServer.framework/GameControllerServer`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-14.0.21.0.0
-  __TEXT.__text: 0x102c4
+14.0.24.0.0
+  __TEXT.__text: 0x10328
   __TEXT.__objc_methlist: 0xe3c
   __TEXT.__const: 0x342
-  __TEXT.__gcc_except_tab: 0x1864
+  __TEXT.__gcc_except_tab: 0x1870
   __TEXT.__oslogstring: 0x1150
   __TEXT.__cstring: 0x884
   __TEXT.__swift5_typeref: 0x2e0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c8
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x180
   __AUTH_CONST.__const: 0x310
   __AUTH_CONST.__cfstring: 0x7c0
-  __AUTH_CONST.__objc_const: 0x2318
+  __AUTH_CONST.__objc_const: 0x2338
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH_CONST.__auth_got: 0x518
   __AUTH.__objc_data: 0x430
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_ivar: 0x190
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 358
-  Symbols:   1228
+  Symbols:   1230
   CStrings:  191
 
Symbols:
+ _OBJC_IVAR_$__GCHapticLogicalDevice._hapticsPlaying
+ _objc_msgSend$endHaptics
Functions:
~ -[_GCHapticServerManager processActiveEventsForStartTime:endTime:] : 2440 -> 2532
~ -[_GCHapticLogicalDevice stopAllHaptics] : 212 -> 220
```
