## handwritingd

> `/usr/libexec/handwritingd`

```diff

-492.2.0.0.0
-  __TEXT.__text: 0x12db8
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_stubs: 0x2d80
-  __TEXT.__objc_methlist: 0x8a0
+494.0.0.0.0
+  __TEXT.__text: 0x13b7c
+  __TEXT.__auth_stubs: 0x770
+  __TEXT.__objc_stubs: 0x2f20
+  __TEXT.__objc_methlist: 0x91c
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x1a04
-  __TEXT.__cstring: 0x12a5
-  __TEXT.__objc_methname: 0x3471
+  __TEXT.__gcc_except_tab: 0x1b88
+  __TEXT.__cstring: 0x12ce
+  __TEXT.__objc_methname: 0x3648
   __TEXT.__objc_classname: 0x22c
-  __TEXT.__objc_methtype: 0x897
+  __TEXT.__objc_methtype: 0x90a
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__oslogstring: 0x16f4
-  __TEXT.__unwind_info: 0x698
-  __DATA_CONST.__auth_got: 0x3c8
-  __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x640
+  __TEXT.__oslogstring: 0x17af
+  __TEXT.__unwind_info: 0x728
+  __DATA_CONST.__auth_got: 0x3d0
+  __DATA_CONST.__got: 0x318
+  __DATA_CONST.__const: 0x6e0
   __DATA_CONST.__cfstring: 0xec0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_doubleobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x1868
-  __DATA.__objc_selrefs: 0xc80
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_const: 0x18a8
+  __DATA.__objc_selrefs: 0xcf0
+  __DATA.__objc_ivar: 0xe0
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x360
   __DATA.__bss: 0x80
-  __DATA.__common: 0x70
+  __DATA.__common: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 245
-  Symbols:   231
-  CStrings:  873
+  Functions: 261
+  Symbols:   233
+  CStrings:  901
 
Symbols:
+ _CGRectGetMaxX
+ _CGRectGetWidth
+ _OBJC_CLASS_$_CHSessionStateCounter
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "\x02\x1a"
+ "@\"CHSessionStateCounter\""
+ "B24@0:8d16"
+ "B32@0:8d16d24"
+ "Line wrapper for eviction with idle lifetime=%!f(MISSING)"
+ "Not triggering optimizeResourceUsage. There are %!i(MISSING) active sessions."
+ "Number of active sessions: %!i(MISSING)"
+ "SessionTracker"
+ "Staging style inventory for eviction with idle lifetime=%!f(MISSING)"
+ "Staging synthesizer for eviction with idle lifetime=%!f(MISSING)"
+ "Triggering optimizeResourceUsage"
+ "_activeSessionCounter"
+ "_cleanupCachedRecognizersTargetLifetime:"
+ "_hasIdleLifetimeElapsed:"
+ "_hasIdleLifetimeElapsed:targetIdleLifetime:"
+ "_stageEvictionOfLineWrapperWithTargetIdleLifetime:"
+ "_stageEvictionOfResourceWithTargetLifetime:block:"
+ "counter"
+ "decrement"
+ "drawingScaledByFactor:"
+ "fastPathCharacterStylesWithVariations"
+ "handleSessionStateUpdate got unknown state=%!l(MISSING)i"
+ "handleSessionStateUpdate:"
+ "hasActiveSessions"
+ "hasIdleLifetimeElapsed:"
+ "hasStyleInventoryIdleLifetimeElapsed:"
+ "increment"
+ "optimizeResourceUsage"
+ "optimizeResourceUsageWithTimeout:onQueue:idleCallbackBlock:"
+ "reset"
+ "shouldResetInventory"
+ "sortedArrayUsingSelector:"
+ "stageEvictionOfStyleInventoryWithTargetIdleLifetime:"
+ "stageEvictionOfTextSynthesizerWithTargetIdleLifetime:"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@0:8d16"
+ "v28@?0@\"CHDrawing\"8B16d20"
+ "v32@0:8d16@?24"
+ "v40@0:8d16@24@?32"
- "\x02\x19"
- "Line wrapper for eviction with idle lifetime=%!f(MISSING)"
- "Staging style inventory for eviction with idle lifetime=%!f(MISSING)"
- "Staging synthesizer for eviction with idle lifetime=%!f(MISSING)"
- "_cleanupCachedRecognizers"
- "_hasIdleLifetimeElapsed"
- "_stageEvictionOfLineWrapper"
- "hasIdleLifetimeElapsed"
- "hasStyleInventoryIdleLifetimeElapsed"
- "stageEvictionOfStyleInventory"
- "stageEvictionOfTextSynthesizer"

```
