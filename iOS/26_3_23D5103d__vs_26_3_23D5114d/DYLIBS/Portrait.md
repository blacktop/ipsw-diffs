## Portrait

> `/System/Library/PrivateFrameworks/Portrait.framework/Portrait`

```diff

-492.80.6.0.0
-  __TEXT.__text: 0xa0b58
+492.80.9.0.0
+  __TEXT.__text: 0xa0d0c
   __TEXT.__auth_stubs: 0x1410
   __TEXT.__delay_stubs: 0x440
   __TEXT.__delay_helper: 0x30c
-  __TEXT.__objc_methlist: 0x9dbc
+  __TEXT.__objc_methlist: 0x9df4
   __TEXT.__const: 0x21320
   __TEXT.__cstring: 0x7127
-  __TEXT.__oslogstring: 0x4a6e
-  __TEXT.__gcc_except_tab: 0x1a78
+  __TEXT.__oslogstring: 0x4a9d
+  __TEXT.__gcc_except_tab: 0x1aec
   __TEXT.__ustring: 0x30
-  __TEXT.__unwind_info: 0x21d0
-  __TEXT.__objc_classname: 0x144c
-  __TEXT.__objc_methname: 0x1beee
+  __TEXT.__unwind_info: 0x21e8
+  __TEXT.__objc_classname: 0x144d
+  __TEXT.__objc_methname: 0x1bfbe
   __TEXT.__objc_methtype: 0x59e8
-  __TEXT.__objc_stubs: 0x103a0
+  __TEXT.__objc_stubs: 0x10420
   __DATA_CONST.__got: 0x950
   __DATA_CONST.__const: 0x998
   __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5320
+  __DATA_CONST.__objc_selrefs: 0x5348
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_classrefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x510

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6DD97739-DF26-3076-A1F2-73FB60EA0B07
-  Functions: 4181
-  Symbols:   15531
-  CStrings:  7873
+  UUID: D74D462A-08D5-3ACC-AB94-867C2B087494
+  Functions: 4185
+  Symbols:   15544
+  CStrings:  7880
 
Symbols:
+ -[PTEffect handleReactionDuringVFXInit:effectRenderRequest:renderCall:]
+ -[PTEffect pendingReactionDuringVFXInitialization]
+ -[PTEffect setPendingReactionDuringVFXInitialization:]
+ -[PTEffectRenderer isVFXInitialized]
+ -[PTEffectRenderer sharedResources]
+ -[PTVFXResources isInitialized]
+ GCC_except_table105
+ GCC_except_table26
+ _OBJC_IVAR_$_PTEffect._pendingReactionDuringVFXInitialization
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$handleReactionDuringVFXInit:effectRenderRequest:renderCall:
+ _objc_msgSend$isInitialized
+ _objc_msgSend$isVFXInitialized
+ _objc_msgSend$pendingReactionDuringVFXInitialization
+ _objc_msgSend$setPendingReactionDuringVFXInitialization:
- -[PTVFXResources initializationCancelled]
- -[PTVFXResources setInitializationCancelled:]
- GCC_except_table23
- _OBJC_IVAR_$_PTVFXResources._initializationCancelled
- _objc_msgSend$initializationCancelled
- _objc_msgSend$setInitializationCancelled:
CStrings:
+ "Render pending reaction"
+ "Save pending reaction"
+ "T@\"PTEffectReaction\",&,V_pendingReactionDuringVFXInitialization"
+ "VFX initialization complete"
+ "_pendingReactionDuringVFXInitialization"
+ "arrayByAddingObject:"
+ "handleReactionDuringVFXInit:effectRenderRequest:renderCall:"
+ "isInitialized"
+ "isVFXInitialized"
+ "pendingReactionDuringVFXInitialization"
+ "setPendingReactionDuringVFXInitialization:"
+ "sharedResources"
- "TB,V_initializationCancelled"
- "VFX initialization aborted"
- "_initializationCancelled"
- "initializationCancelled"
- "setInitializationCancelled:"

```
