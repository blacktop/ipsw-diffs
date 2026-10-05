## ARKitCore

> `/System/Library/SubFrameworks/ARKitCore.framework/ARKitCore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-781.40.3.0.0
-  __TEXT.__text: 0x195140
+781.40.6.0.0
+  __TEXT.__text: 0x195174
   __TEXT.__objc_methlist: 0x1143c
   __TEXT.__const: 0x25d88
   __TEXT.__cstring: 0x1d99a
-  __TEXT.__gcc_except_tab: 0x134bc
-  __TEXT.__oslogstring: 0x20dd9
+  __TEXT.__gcc_except_tab: 0x13584
+  __TEXT.__oslogstring: 0x20dbe
   __TEXT.__ustring: 0xe6
-  __TEXT.__unwind_info: 0x7960
+  __TEXT.__unwind_info: 0x7978
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__got: 0x15f8
   __AUTH_CONST.__const: 0x3e18
   __AUTH_CONST.__cfstring: 0xff40
-  __AUTH_CONST.__objc_const: 0x3d100
+  __AUTH_CONST.__objc_const: 0x3d120
   __AUTH_CONST.__weak_auth_got: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x38b8
   __AUTH_CONST.__auth_got: 0x1f10
-  __AUTH.__objc_data: 0xf0
-  __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x203c
-  __DATA.__data: 0x1c90
+  __DATA.__objc_ivar: 0x2040
+  __DATA.__data: 0x40
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x5500
-  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__objc_data: 0x55f0
+  __DATA_DIRTY.__data: 0x1c70
   __DATA_DIRTY.__common: 0x28
   __DATA_DIRTY.__bss: 0xa90
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
   Functions: 8017
-  Symbols:   14603
-  CStrings:  4554
+  Symbols:   14604
+  CStrings:  4553
 
Symbols:
+ _OBJC_IVAR_$_ARReplaySensorPublic._metadataCacheLock
Functions:
~ -[ARReplaySensorPublic initWithSequenceURL:replayMode:] : 3472 -> 3484
~ -[ARReplaySensorPublic prepareForReplay] : 2744 -> 2832
~ -[ARReplaySensorPublic _endReplay] : 224 -> 124
~ -[ARReplaySensorPublic getWrappedItemsFromStream:upToMovieTime:withBlock:] : 464 -> 516
CStrings:
- "%{public}@ <%p>: endReplay"
```
