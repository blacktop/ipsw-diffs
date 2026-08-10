## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-635.0.4.0.0
-  __TEXT.__text: 0x68e44
+635.0.7.0.0
+  __TEXT.__text: 0x68e3c
   __TEXT.__objc_methlist: 0x5fb0
   __TEXT.__const: 0x268
-  __TEXT.__cstring: 0x6b00
+  __TEXT.__cstring: 0x6b1f
   __TEXT.__oslogstring: 0x7016
   __TEXT.__gcc_except_tab: 0x1fd8
   __TEXT.__unwind_info: 0x16d8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24d8
+  __DATA_CONST.__const: 0x24e0
   __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__got: 0x8d8
   __AUTH_CONST.__const: 0x680
-  __AUTH_CONST.__cfstring: 0x6c60
+  __AUTH_CONST.__cfstring: 0x6c80
   __AUTH_CONST.__objc_const: 0x9aa8
   __AUTH_CONST.__objc_intobj: 0x480
   __AUTH_CONST.__objc_arrayobj: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2276
-  Symbols:   5676
-  CStrings:  1448
+  Symbols:   5677
+  CStrings:  1449
 
Symbols:
+ _TVPPlaybackNeedsMachineAuthKey
Functions:
~ -[TVPPlayer playbackErrorFromError:forMediaItem:] : 1984 -> 1976
CStrings:
+ "TVPPlaybackNeedsMachineAuthKey"
```
