## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-201.0.0.0.0
-  __TEXT.__text: 0x775a4
-  __TEXT.__objc_methlist: 0xa0a4
-  __TEXT.__const: 0x1a08
-  __TEXT.__cstring: 0x1a775
+202.0.0.0.0
+  __TEXT.__text: 0x7753c
+  __TEXT.__objc_methlist: 0xa014
+  __TEXT.__const: 0x19f8
+  __TEXT.__cstring: 0x1a737
   __TEXT.__oslogstring: 0xef4
   __TEXT.__gcc_except_tab: 0x2604
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x2550
+  __TEXT.__unwind_info: 0x2540
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1448
-  __DATA_CONST.__objc_classlist: 0x530
+  __DATA_CONST.__const: 0x1430
+  __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bc8
+  __DATA_CONST.__objc_selrefs: 0x3b68
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x50c8
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x1868
-  __AUTH_CONST.__cfstring: 0x1cac0
-  __AUTH_CONST.__objc_const: 0x16d58
+  __AUTH_CONST.__cfstring: 0x1ca60
+  __AUTH_CONST.__objc_const: 0x16c08
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1db0
-  __DATA.__objc_ivar: 0xf38
+  __DATA.__objc_ivar: 0xf2c
   __DATA.__data: 0x1180
   __DATA.__bss: 0x410
-  __DATA_DIRTY.__objc_data: 0x1630
+  __DATA_DIRTY.__objc_data: 0x3390
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4114
-  Symbols:   8843
-  CStrings:  3923
+  Functions: 4103
+  Symbols:   8818
+  CStrings:  3920
 
Symbols:
+ -[SignpostUpdateSequenceInterval setThreadID:]
+ -[SignpostUpdateSequenceInterval threadID]
+ _OBJC_IVAR_$_SignpostUpdateSequenceInterval._threadID
+ __timeRatioForTimeIntervalArray:applyPerceptionAdjustments:.concurrentAdjustment
- -[SignpostAnimationInterval animationType]
- -[SignpostAnimationInterval firstFrameGraceTimeMs]
- -[SignpostSupportAnimationGraceTimeController defaultGraceTimeMs]
- -[SignpostSupportAnimationGraceTimeController gracetimeMsForSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController init]
- -[SignpostSupportAnimationGraceTimeController setAnimationType:forSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController setDefaultGraceTimeMs:]
- -[SignpostSupportAnimationGraceTimeController setFirstFrameGraceTimeMs:forSubsystem:category:name:]
- -[SignpostSupportAnimationGraceTimeController setUserInitiatedGraceTimeMs:]
- -[SignpostSupportAnimationGraceTimeController setUserInteractiveGraceTimeMs:]
- -[SignpostSupportAnimationGraceTimeController userInitiatedGraceTimeMs]
- -[SignpostSupportAnimationGraceTimeController userInteractiveGraceTimeMs]
- -[SignpostSupportObjectExtractor animationFirstFrameGraceTimeController]
- _OBJC_CLASS_$_SignpostSupportAnimationGraceTimeController
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._defaultGraceTimeMs
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInitiatedGraceTimeMs
- _OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInteractiveGraceTimeMs
- _OBJC_IVAR_$_SignpostSupportObjectExtractor._animationFirstFrameGraceTimeController
- _OBJC_METACLASS_$_SignpostSupportAnimationGraceTimeController
- __OBJC_$_INSTANCE_METHODS_SignpostSupportAnimationGraceTimeController
- __OBJC_$_INSTANCE_VARIABLES_SignpostSupportAnimationGraceTimeController
- __OBJC_$_PROP_LIST_SignpostSupportAnimationGraceTimeController
- __OBJC_CLASS_RO_$_SignpostSupportAnimationGraceTimeController
- __OBJC_METACLASS_RO_$_SignpostSupportAnimationGraceTimeController
- __timeRatioForTimeIntervalArray:applyPerceptionAdjustments:.concurrentAdjustement
- _kSignpostSupportDefaultFirstFrameGraceTimeMs
- _kSignpostSupportDefaultUserInitiatedFirstFrameGraceTimeMs
- _kSignpostSupportDefaultUserInteractiveFirstFrameGraceTimeMs
- _objc_msgSend$animationType
CStrings:
+ "Animation Interval \"%@\" [%llu - %llu]\nDuration: %.4fs\nTelemetry:%@\n%@%@%@"
- "Animation Interval \"%@\" [%llu - %llu]\nDuration: %.4fs\nTelemetry:%@\nAnimation Type: %@\n%@%@%@"
- "User Initiated"
- "User Interactive"
- "overridden"
```
