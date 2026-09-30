## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1395.100.1.0.0
-  __TEXT.__text: 0x67528
-  __TEXT.__objc_methlist: 0x9254
+1397.100.1.0.0
+  __TEXT.__text: 0x67700
+  __TEXT.__objc_methlist: 0x927c
   __TEXT.__const: 0x130
   __TEXT.__cstring: 0x63ab
-  __TEXT.__oslogstring: 0x3b4d
+  __TEXT.__oslogstring: 0x3bb1
   __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__unwind_info: 0x1dd8
+  __TEXT.__unwind_info: 0x1de8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34d0
+  __DATA_CONST.__objc_selrefs: 0x34e8
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3236
-  Symbols:   6832
-  CStrings:  1004
+  Functions: 3240
+  Symbols:   6840
+  CStrings:  1005
 
Symbols:
+ -[CXChannelProvider _registerCurrentConfigurationIfAudioSessionIDStaleOnQueue]
+ -[CXChannelProvider _registerCurrentConfigurationOnQueue]
+ -[CXChannelProvider currentOpaqueAudioSessionID]
+ ___35-[CXChannelProvider performAction:]_block_invoke
+ ___57-[CXChannelProvider _registerCurrentConfigurationOnQueue]_block_invoke
+ _objc_msgSend$_registerCurrentConfigurationIfAudioSessionIDStaleOnQueue
+ _objc_msgSend$_registerCurrentConfigurationOnQueue
+ _objc_msgSend$currentOpaqueAudioSessionID
CStrings:
+ "Cached audioSessionID %u no longer matches current opaqueSessionID %u; re-registering configuration"
```
