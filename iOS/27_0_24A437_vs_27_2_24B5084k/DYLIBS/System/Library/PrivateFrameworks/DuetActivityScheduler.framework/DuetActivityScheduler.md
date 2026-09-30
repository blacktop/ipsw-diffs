## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-2467.2.2.0.0
-  __TEXT.__text: 0x3e0b0
-  __TEXT.__objc_methlist: 0x4a00
+2467.40.37.0.0
+  __TEXT.__text: 0x3e1a8
+  __TEXT.__objc_methlist: 0x4a30
   __TEXT.__const: 0x200
-  __TEXT.__gcc_except_tab: 0x1624
-  __TEXT.__cstring: 0x41a7
-  __TEXT.__oslogstring: 0x32ed
+  __TEXT.__gcc_except_tab: 0x1628
+  __TEXT.__cstring: 0x4276
+  __TEXT.__oslogstring: 0x32d7
   __TEXT.__unwind_info: 0x1768
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2938
+  __DATA_CONST.__objc_selrefs: 0x2958
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x180
   __DATA_CONST.__got: 0x330
   __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x5280
-  __AUTH_CONST.__objc_const: 0x7f88
+  __AUTH_CONST.__cfstring: 0x5320
+  __AUTH_CONST.__objc_const: 0x7fb8
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x228

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x6e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x4a4
+  __DATA.__objc_ivar: 0x4a8
   __DATA.__data: 0xd68
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1689
-  Symbols:   3668
-  CStrings:  1004
+  Functions: 1693
+  Symbols:   3674
+  CStrings:  1009
 
Symbols:
+ -[_DASActivity isMindPalaceAmbientActivity]
+ -[_DASActivity isMindPalaceUserInitiatedActivity]
+ -[_DASContinuedProcessingWrapper hostManagedProgressUI]
+ -[_DASContinuedProcessingWrapper setHostManagedProgressUI:]
+ GCC_except_table140
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._hostManagedProgressUI
+ _objc_msgSend$setHostManagedProgressUI:
- GCC_except_table138
CStrings:
+ "ERROR Submitting %@: Please contact us to prevent this activity from getting rejected. Configuration: %@"
+ "Verify: dastool compute activityTimeline %@ --start -48h"
+ "com.apple.mindpalace.executeCompaction"
+ "com.apple.mindpalace.executeCompactionUserInitiated"
+ "com.apple.mindpalace.executeExtraction"
+ "com.apple.mindpalace.executeExtractionUserInitiated"
+ "hostManagedProgressUI"
- "ERROR Submitting %@: Please contact das-core@group.apple.com to prevent this activity from getting rejected. Configuration: %@"
- "Verify: dastool compute activityTimeline %@ --last 48"
```
