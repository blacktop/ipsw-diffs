## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Recap`

```diff

-200.0.0.0.0
-  __TEXT.__text: 0x215c8
-  __TEXT.__objc_methlist: 0x3530
+201.108.0.0.0
+  __TEXT.__text: 0x21b50
+  __TEXT.__objc_methlist: 0x3658
   __TEXT.__const: 0x380
-  __TEXT.__cstring: 0x1bff
+  __TEXT.__cstring: 0x1ce7
   __TEXT.__oslogstring: 0x605
-  __TEXT.__gcc_except_tab: 0xc00
+  __TEXT.__gcc_except_tab: 0xc24
   __TEXT.__dlopen_cstrs: 0x120
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xbf8
+  __TEXT.__unwind_info: 0xc28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e80
+  __DATA_CONST.__objc_selrefs: 0x1ef0
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0x4a0
   __DATA_CONST.__got: 0x408
   __AUTH_CONST.__const: 0x3e0
   __AUTH_CONST.__cfstring: 0x20a0
-  __AUTH_CONST.__objc_const: 0x5478
+  __AUTH_CONST.__objc_const: 0x5500
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x3bc
+  __DATA.__objc_ivar: 0x3c0
   __DATA.__data: 0x9c8
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x4b0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1033
-  Symbols:   2862
-  CStrings:  396
+  Functions: 1048
+  Symbols:   2888
+  CStrings:  400
 
Symbols:
+ -[RCPPlayerPlaybackOptions displayUUIDOverrideSpecified]
+ -[RCPPlayerPlaybackOptions setDisplayUUIDOverrideSpecified:]
+ -[RCPSyntheticEventStream _flickWithStartPoint:endPoint:duration:pressure:radius:lift:]
+ -[RCPSyntheticEventStream cancel:]
+ -[RCPSyntheticEventStream cancel:touchCount:]
+ -[RCPSyntheticEventStream cancelAtAllActivePoints]
+ -[RCPSyntheticEventStream cancelAtPoints:touchCount:]
+ -[RCPSyntheticEventStream dragAndCancelWithStartPoint:endPoint:duration:]
+ -[RCPSyntheticEventStream dragAndCancelWithStartPoint:endPoint:duration:radius:]
+ -[RCPSyntheticEventStream dragAndCancelWithStartPoint:endPoint:duration:tapAndWait:radius:]
+ -[RCPSyntheticEventStream flickAndCancelWithStartPoint:endPoint:duration:]
+ -[RCPSyntheticEventStream flickAndCancelWithStartPoint:endPoint:duration:radius:]
+ -[RCPSyntheticEventStream tapAndCancel:]
+ -[RCPSyntheticEventStream tapAndCancel:radius:]
+ _OBJC_IVAR_$_RCPPlayerPlaybackOptions._displayUUIDOverrideSpecified
+ _isTouchCancelArgument
+ _objc_msgSend$_flickWithStartPoint:endPoint:duration:pressure:radius:lift:
+ _objc_msgSend$cancel:
+ _objc_msgSend$cancel:touchCount:
+ _objc_msgSend$cancelAtAllActivePoints
+ _objc_msgSend$cancelAtPoints:touchCount:
+ _objc_msgSend$displayUUIDOverrideSpecified
+ _objc_msgSend$dragAndCancelWithStartPoint:endPoint:duration:radius:
+ _objc_msgSend$dragAndCancelWithStartPoint:endPoint:duration:tapAndWait:radius:
+ _objc_msgSend$flickAndCancelWithStartPoint:endPoint:duration:radius:
+ _objc_msgSend$tapAndCancel:radius:
+ _objc_msgSend$touchDown:touchCount:radius:
- _supplyMissingStandardProperties:senderID:.deviceCount
CStrings:
+ "Canceling a %s isn't supported. Use the \"%s\" command with a trailing \"%s\" to cancel a multi-finger sequence.\n"
+ "Canceling a %s isn't supported. Use the \"%s\" command with a trailing \"%s\" to cancel an arbitrary touch sequence.\n"
+ "cancel"
+ "pinch"
+ "stretch"
- "recap-bus-%d"
```
