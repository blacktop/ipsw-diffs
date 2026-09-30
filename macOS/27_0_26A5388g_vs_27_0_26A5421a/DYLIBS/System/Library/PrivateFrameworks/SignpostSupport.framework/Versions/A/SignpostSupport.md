## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/Versions/A/SignpostSupport`

```diff

-201.0.0.0.0
-  __TEXT.__text: 0x7eeb0
-  __TEXT.__objc_methlist: 0xa0a4
-  __TEXT.__const: 0x1a18
-  __TEXT.__cstring: 0x1a775
+203.0.0.0.0
+  __TEXT.__text: 0x7ee9c
+  __TEXT.__objc_methlist: 0xa02c
+  __TEXT.__const: 0x19f8
+  __TEXT.__cstring: 0x1a737
   __TEXT.__oslogstring: 0xef4
   __TEXT.__gcc_except_tab: 0x2654
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0x24f8
+  __TEXT.__unwind_info: 0x24e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc00
-  __DATA_CONST.__objc_classlist: 0x530
+  __DATA_CONST.__const: 0xbe8
+  __DATA_CONST.__objc_classlist: 0x528
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bc8
+  __DATA_CONST.__objc_selrefs: 0x3b78
   __DATA_CONST.__objc_superrefs: 0x488
   __DATA_CONST.__objc_arraydata: 0x50c8
   __DATA_CONST.__got: 0x470
   __AUTH_CONST.__const: 0x2228
-  __AUTH_CONST.__cfstring: 0x1cac0
-  __AUTH_CONST.__objc_const: 0x16d58
+  __AUTH_CONST.__cfstring: 0x1ca60
+  __AUTH_CONST.__objc_const: 0x16c38
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0xf38
+  __DATA.__objc_ivar: 0xf30
   __DATA.__data: 0x1180
   __DATA.__bss: 0x408
-  __DATA_DIRTY.__objc_data: 0x33e0
+  __DATA_DIRTY.__objc_data: 0x3390
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4150
-  Symbols:   8911
-  CStrings:  3923
+  Functions: 4141
+  Symbols:   8887
+  CStrings:  3920
 
Symbols:
+ -[SignpostSupportObjectExtractor didComplete]
+ -[SignpostSupportObjectExtractor setDidComplete:]
+ -[SignpostUpdateSequenceInterval setThreadID:]
+ -[SignpostUpdateSequenceInterval threadID]
+ GCC_except_table100
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table112
+ GCC_except_table118
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table173
+ GCC_except_table18
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table209
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table252
+ GCC_except_table277
+ GCC_except_table29
+ GCC_except_table313
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table8
+ GCC_except_table84
+ GCC_except_table88
+ GCC_except_table90
+ GCC_except_table97
+ OBJC_IVAR_$_SignpostSupportObjectExtractor._didComplete
+ OBJC_IVAR_$_SignpostUpdateSequenceInterval._threadID
+ _objc_msgSend$didComplete
+ _objc_msgSend$setDidComplete:
+ _objc_msgSend$set_stopProcessingBlock:
+ _timeRatioForTimeIntervalArray:applyPerceptionAdjustments:.concurrentAdjustment
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
- GCC_except_table101
- GCC_except_table102
- GCC_except_table104
- GCC_except_table109
- GCC_except_table11
- GCC_except_table120
- GCC_except_table121
- GCC_except_table124
- GCC_except_table137
- GCC_except_table14
- GCC_except_table144
- GCC_except_table145
- GCC_except_table147
- GCC_except_table148
- GCC_except_table149
- GCC_except_table156
- GCC_except_table161
- GCC_except_table167
- GCC_except_table170
- GCC_except_table172
- GCC_except_table177
- GCC_except_table185
- GCC_except_table192
- GCC_except_table194
- GCC_except_table199
- GCC_except_table205
- GCC_except_table208
- GCC_except_table21
- GCC_except_table210
- GCC_except_table213
- GCC_except_table215
- GCC_except_table220
- GCC_except_table221
- GCC_except_table225
- GCC_except_table226
- GCC_except_table229
- GCC_except_table230
- GCC_except_table233
- GCC_except_table237
- GCC_except_table246
- GCC_except_table257
- GCC_except_table262
- GCC_except_table27
- GCC_except_table275
- GCC_except_table283
- GCC_except_table31
- GCC_except_table312
- GCC_except_table45
- GCC_except_table49
- GCC_except_table50
- GCC_except_table55
- GCC_except_table63
- GCC_except_table67
- GCC_except_table76
- GCC_except_table78
- GCC_except_table83
- GCC_except_table85
- GCC_except_table86
- GCC_except_table87
- GCC_except_table89
- GCC_except_table99
- OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._defaultGraceTimeMs
- OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInitiatedGraceTimeMs
- OBJC_IVAR_$_SignpostSupportAnimationGraceTimeController._userInteractiveGraceTimeMs
- OBJC_IVAR_$_SignpostSupportObjectExtractor._animationFirstFrameGraceTimeController
- _OBJC_CLASS_$_SignpostSupportAnimationGraceTimeController
- _OBJC_METACLASS_$_SignpostSupportAnimationGraceTimeController
- __OBJC_$_INSTANCE_METHODS_SignpostSupportAnimationGraceTimeController
- __OBJC_$_INSTANCE_VARIABLES_SignpostSupportAnimationGraceTimeController
- __OBJC_$_PROP_LIST_SignpostSupportAnimationGraceTimeController
- __OBJC_CLASS_RO_$_SignpostSupportAnimationGraceTimeController
- __OBJC_METACLASS_RO_$_SignpostSupportAnimationGraceTimeController
- _kSignpostSupportDefaultFirstFrameGraceTimeMs
- _kSignpostSupportDefaultUserInitiatedFirstFrameGraceTimeMs
- _kSignpostSupportDefaultUserInteractiveFirstFrameGraceTimeMs
- _objc_msgSend$animationType
- _objc_msgSend$setNotificationProcessingQueue:
- _timeRatioForTimeIntervalArray:applyPerceptionAdjustments:.concurrentAdjustement
CStrings:
+ "Animation Interval \"%@\" [%llu - %llu]\nDuration: %.4fs\nTelemetry:%@\n%@%@%@"
- "Animation Interval \"%@\" [%llu - %llu]\nDuration: %.4fs\nTelemetry:%@\nAnimation Type: %@\n%@%@%@"
- "User Initiated"
- "User Interactive"
- "overridden"
```
