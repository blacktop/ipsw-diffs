## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

-1153.2.2.0.0
-  __TEXT.__text: 0x81d30
-  __TEXT.__objc_methlist: 0x5af0
-  __TEXT.__const: 0x2cc
-  __TEXT.__cstring: 0xb4e1
+1153.3.2.0.0
+  __TEXT.__text: 0x823bc
+  __TEXT.__objc_methlist: 0x5b10
+  __TEXT.__const: 0x2dc
+  __TEXT.__cstring: 0xb551
   __TEXT.__oslogstring: 0x6176
-  __TEXT.__gcc_except_tab: 0xd8c
+  __TEXT.__gcc_except_tab: 0xda0
   __TEXT.__dlopen_cstrs: 0x20a
-  __TEXT.__unwind_info: 0x2d88
+  __TEXT.__unwind_info: 0x2da8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2848
+  __DATA_CONST.__const: 0x2880
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3848
+  __DATA_CONST.__objc_selrefs: 0x3858
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x228
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x908
   __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x8ee0
-  __AUTH_CONST.__objc_const: 0xb6f8
+  __AUTH_CONST.__cfstring: 0x8fe0
+  __AUTH_CONST.__objc_const: 0xb728
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xc30
-  __DATA.__objc_ivar: 0x95c
+  __DATA.__objc_ivar: 0x960
   __DATA.__data: 0x1d40
   __DATA_DIRTY.__objc_data: 0xeb0
   __DATA_DIRTY.__bss: 0x1b8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3174
-  Symbols:   4772
-  CStrings:  1775
+  Functions: 3184
+  Symbols:   4778
+  CStrings:  1782
 
Symbols:
+ +[FBProcessWatchdogEventContext contextForEvent:visibility:settings:transitionContext:]
+ -[FBProcessWatchdogEventContext _initWithEvent:visibility:settings:transitionContext:]
+ -[FBProcessWatchdogEventContext visibility]
+ -[FBSystemService _isTrustedRequest:forCaller:fromClient:forBundleInfo:withOptions:shouldLogResult:fatalError:]
+ _FBProcessWatchdogEventVisibilityIsValid
+ _NSStringFromProcessWatchdogEventVisibility
+ _OBJC_IVAR_$_FBProcessWatchdogEventContext._visibility
- -[FBSystemService _isTrustedRequest:forCaller:fromClient:forBundleInfo:withOptions:fatalError:]
CStrings:
+ "FBProcessWatchdogEvents.m"
+ "bg"
+ "fg"
+ "fg->bg"
+ "invalid event: %@"
+ "invalid visibility: %@"
+ "notSet"
+ "outError != ((void *)0)"
- "!"
```
