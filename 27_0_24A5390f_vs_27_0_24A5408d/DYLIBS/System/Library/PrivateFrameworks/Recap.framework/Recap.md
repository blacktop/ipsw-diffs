## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Recap`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-198.0.0.0.0
-  __TEXT.__text: 0x22174
-  __TEXT.__objc_methlist: 0x34f8
+200.0.0.0.0
+  __TEXT.__text: 0x224f0
+  __TEXT.__objc_methlist: 0x3530
   __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x1bf1
+  __TEXT.__cstring: 0x1bff
   __TEXT.__oslogstring: 0x605
   __TEXT.__gcc_except_tab: 0xc00
   __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0xa00
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e58
+  __DATA_CONST.__objc_selrefs: 0x1e80
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x470
+  __DATA_CONST.__objc_arraydata: 0x4a0
   __DATA_CONST.__got: 0x408
-  __AUTH_CONST.__const: 0x3c0
-  __AUTH_CONST.__cfstring: 0x2080
-  __AUTH_CONST.__objc_const: 0x5438
-  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__const: 0x3e0
+  __AUTH_CONST.__cfstring: 0x20a0
+  __AUTH_CONST.__objc_const: 0x5478
+  __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH_CONST.__objc_dictobj: 0x230
+  __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x3b8
+  __DATA.__objc_ivar: 0x3bc
   __DATA.__data: 0x9c8
-  __DATA.__bss: 0x148
+  __DATA.__bss: 0x158
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x4b0
   __DATA_DIRTY.__bss: 0xd0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1026
-  Symbols:   2849
-  CStrings:  396
+  Functions: 1033
+  Symbols:   2862
+  CStrings:  397
 
Symbols:
+ +[RCPEventSenderProperties genericPencilGestureSender]
+ -[RCPEventStream recordedDisplayUUIDs]
+ -[RCPPlayer _senderPropertiesApplyingDisplayUUIDOverride:]
+ -[RCPPlayerPlaybackOptions displayUUIDOverride]
+ -[RCPPlayerPlaybackOptions setDisplayUUIDOverride:]
+ _OBJC_IVAR_$_RCPPlayerPlaybackOptions._displayUUIDOverride
+ ___54+[RCPEventSenderProperties genericPencilGestureSender]_block_invoke
+ _genericPencilGestureSender.onceToken
+ _genericPencilGestureSender.sender
+ _objc_msgSend$_senderPropertiesApplyingDisplayUUIDOverride:
+ _objc_msgSend$displayUUIDOverride
+ _objc_msgSend$setPlaybackOptions:
+ _objc_msgSend$wantsDisplayUUID
CStrings:
+ "09:36:05"
+ "Aug  4 2026"
+ "B"
+ "pencilGesture"
- "03:28:05"
- "A"
- "Jul  8 2026"
```
