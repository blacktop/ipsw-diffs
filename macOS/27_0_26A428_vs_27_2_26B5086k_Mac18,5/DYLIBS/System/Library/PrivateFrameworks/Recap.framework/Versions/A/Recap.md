## Recap

> `/System/Library/PrivateFrameworks/Recap.framework/Versions/A/Recap`

```diff

-200.0.0.0.0
-  __TEXT.__text: 0x201b8
-  __TEXT.__objc_methlist: 0x32f8
+201.108.0.0.0
+  __TEXT.__text: 0x20748
+  __TEXT.__objc_methlist: 0x3420
   __TEXT.__const: 0x340
-  __TEXT.__cstring: 0x1ab7
+  __TEXT.__cstring: 0x1b9f
   __TEXT.__oslogstring: 0x425
-  __TEXT.__gcc_except_tab: 0xb18
+  __TEXT.__gcc_except_tab: 0xb3c
   __TEXT.__ustring: 0x1e
   __TEXT.__dlopen_cstrs: 0x5c
-  __TEXT.__unwind_info: 0xb00
+  __TEXT.__unwind_info: 0xb30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
+  __DATA_CONST.__objc_selrefs: 0x1c68
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x4a0
   __DATA_CONST.__got: 0x2e8
   __AUTH_CONST.__const: 0x810
   __AUTH_CONST.__cfstring: 0x2020
-  __AUTH_CONST.__objc_const: 0x5038
+  __AUTH_CONST.__objc_const: 0x50c0
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x388
+  __DATA.__objc_ivar: 0x38c
   __DATA.__data: 0x9c8
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x550
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 980
-  Symbols:   2636
-  CStrings:  370
+  Functions: 995
+  Symbols:   2662
+  CStrings:  374
 
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
+ OBJC_IVAR_$_RCPPlayerPlaybackOptions._displayUUIDOverrideSpecified
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
- supplyMissingStandardProperties:senderID:.deviceCount
CStrings:
+ "Canceling a %s isn't supported. Use the \"%s\" command with a trailing \"%s\" to cancel a multi-finger sequence.\n"
+ "Canceling a %s isn't supported. Use the \"%s\" command with a trailing \"%s\" to cancel an arbitrary touch sequence.\n"
+ "cancel"
+ "pinch"
+ "stretch"
- "recap-bus-%d"
```
