## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler`

```diff

-2467.0.40.0.0
-  __TEXT.__text: 0x3e144
-  __TEXT.__objc_methlist: 0x46d8
+2467.40.37.0.0
+  __TEXT.__text: 0x3e23c
+  __TEXT.__objc_methlist: 0x4708
   __TEXT.__const: 0x1f8
-  __TEXT.__cstring: 0x3e4f
-  __TEXT.__oslogstring: 0x2c77
-  __TEXT.__gcc_except_tab: 0x1434
+  __TEXT.__cstring: 0x3f1e
+  __TEXT.__oslogstring: 0x2c61
+  __TEXT.__gcc_except_tab: 0x1438
   __TEXT.__unwind_info: 0x15d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x26d8
+  __DATA_CONST.__objc_selrefs: 0x26f8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__got: 0x300
   __AUTH_CONST.__const: 0xea0
-  __AUTH_CONST.__cfstring: 0x4ea0
-  __AUTH_CONST.__objc_const: 0x7b28
+  __AUTH_CONST.__cfstring: 0x4f40
+  __AUTH_CONST.__objc_const: 0x7b58
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x690
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x454
+  __DATA.__objc_ivar: 0x458
   __DATA.__data: 0xd68
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1626
-  Symbols:   3573
-  CStrings:  939
+  Functions: 1630
+  Symbols:   3580
+  CStrings:  944
 
Symbols:
+ -[_DASActivity isMindPalaceAmbientActivity]
+ -[_DASActivity isMindPalaceUserInitiatedActivity]
+ -[_DASContinuedProcessingWrapper hostManagedProgressUI]
+ -[_DASContinuedProcessingWrapper setHostManagedProgressUI:]
+ GCC_except_table145
+ GCC_except_table150
+ OBJC_IVAR_$__DASContinuedProcessingWrapper._hostManagedProgressUI
+ _objc_msgSend$setHostManagedProgressUI:
- GCC_except_table143
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
