## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Recap`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-197.0.0.0.0
-  __TEXT.__text: 0x21fd0
-  __TEXT.__objc_methlist: 0x34e0
+198.0.0.0.0
+  __TEXT.__text: 0x22174
+  __TEXT.__objc_methlist: 0x34f8
   __TEXT.__const: 0x380
   __TEXT.__cstring: 0x1bf1
   __TEXT.__oslogstring: 0x605
   __TEXT.__gcc_except_tab: 0xc00
   __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x9f0
+  __TEXT.__unwind_info: 0x9f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e48
+  __DATA_CONST.__objc_selrefs: 0x1e58
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__got: 0x408
   __AUTH_CONST.__const: 0x3c0
   __AUTH_CONST.__cfstring: 0x2080
-  __AUTH_CONST.__objc_const: 0x53b8
+  __AUTH_CONST.__objc_const: 0x5438
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH_CONST.__auth_got: 0x750
+  __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x3a8
+  __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x9c8
-  __DATA.__bss: 0x170
+  __DATA.__bss: 0x148
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0xa8
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1024
-  Symbols:   2840
-  CStrings:  395
+  Functions: 1026
+  Symbols:   2849
+  CStrings:  396
 
Symbols:
+ -[RCPSyntheticFluidSwipeEventStream appendVelocityChildToEvent:]
+ -[RCPSyntheticFluidSwipeEventStream trackVelocityRate]
+ _IOHIDEventCreateVelocityEvent
+ _OBJC_IVAR_$_RCPEventStreamRecorder._rawEventsLock
+ _OBJC_IVAR_$_RCPSyntheticFluidSwipeEventStream._latestVelocityRate
+ _OBJC_IVAR_$_RCPSyntheticFluidSwipeEventStream._previousEventProgress
+ _OBJC_IVAR_$_RCPSyntheticFluidSwipeEventStream._previousEventTimeOffset
+ _objc_msgSend$appendVelocityChildToEvent:
+ _objc_msgSend$trackVelocityRate
CStrings:
+ "!!"
+ "03:28:05"
+ "Jul  8 2026"
- "04:42:07"
- "Jun 23 2026"
```
