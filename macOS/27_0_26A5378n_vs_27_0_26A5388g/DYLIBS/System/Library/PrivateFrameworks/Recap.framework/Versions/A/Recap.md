## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Versions/A/Recap`

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
-  __TEXT.__text: 0x20ba0
-  __TEXT.__objc_methlist: 0x32a8
+198.0.0.0.0
+  __TEXT.__text: 0x20d30
+  __TEXT.__objc_methlist: 0x32c0
   __TEXT.__const: 0x340
   __TEXT.__cstring: 0x1aa9
   __TEXT.__oslogstring: 0x425
   __TEXT.__gcc_except_tab: 0xb18
   __TEXT.__ustring: 0x1e
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0x8c8
+  __TEXT.__unwind_info: 0x8d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bc0
+  __DATA_CONST.__objc_selrefs: 0x1bd0
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0x7f0
   __AUTH_CONST.__cfstring: 0x2000
-  __AUTH_CONST.__objc_const: 0x4f78
+  __AUTH_CONST.__objc_const: 0x4ff8
   __AUTH_CONST.__objc_intobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x374
+  __DATA.__objc_ivar: 0x384
   __DATA.__data: 0x9c8
-  __DATA.__bss: 0x138
+  __DATA.__bss: 0x110
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0xb8
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 971
-  Symbols:   2614
-  CStrings:  369
+  Functions: 973
+  Symbols:   2623
+  CStrings:  370
 
Symbols:
+ -[RCPSyntheticFluidSwipeEventStream appendVelocityChildToEvent:]
+ -[RCPSyntheticFluidSwipeEventStream trackVelocityRate]
+ OBJC_IVAR_$_RCPEventStreamRecorder._rawEventsLock
+ OBJC_IVAR_$_RCPSyntheticFluidSwipeEventStream._latestVelocityRate
+ OBJC_IVAR_$_RCPSyntheticFluidSwipeEventStream._previousEventProgress
+ OBJC_IVAR_$_RCPSyntheticFluidSwipeEventStream._previousEventTimeOffset
+ _IOHIDEventCreateVelocityEvent
+ _objc_msgSend$appendVelocityChildToEvent:
+ _objc_msgSend$trackVelocityRate
CStrings:
+ "!!"
+ "01:42:26"
+ "Jul  8 2026"
- "03:19:45"
- "Jun 23 2026"
```
