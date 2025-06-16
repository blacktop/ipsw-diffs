## WorkflowResponsiveness

> `/System/Library/PrivateFrameworks/WorkflowResponsiveness.framework/WorkflowResponsiveness`

```diff

-383.14.0.0.0
-  __TEXT.__text: 0x26150
+383.17.0.0.0
+  __TEXT.__text: 0x261a8
   __TEXT.__auth_stubs: 0x750
   __TEXT.__objc_methlist: 0x790
   __TEXT.__const: 0xf0

   __TEXT.__oslogstring: 0x4014
   __TEXT.__unwind_info: 0x588
   __TEXT.__objc_classname: 0x11a
-  __TEXT.__objc_methname: 0x241c
+  __TEXT.__objc_methname: 0x2436
   __TEXT.__objc_methtype: 0x26a
-  __TEXT.__objc_stubs: 0x1c60
+  __TEXT.__objc_stubs: 0x1c80
   __DATA_CONST.__got: 0x1b8
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x830
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x3b8

   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x140
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x20
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 514C8F6D-127F-33A1-972A-E1336425890C
+  UUID: 618956CD-672C-35F0-97F9-4BC54808FBB6
   Functions: 568
-  Symbols:   1881
-  CStrings:  1216
+  Symbols:   1883
+  CStrings:  1217
 
Symbols:
+ _WRSanitizeForCA.removedCharactersExcludingUnderscore
+ _WRSanitizeForCA.removedCharactersIncludingUnderscore
+ ___block_literal_global.538
+ ___block_literal_global.547
+ _objc_msgSend$removeCharactersInString:
- _WRSanitizeForCA.removedCharacters
- ___block_literal_global.535
- ___block_literal_global.541
Functions:
~ -[WRWorkflowEventTracker reportCoreAnalyticsEventForSignpost:allCount:allDurationUnionSec:allDurationSumSec:allDurationLongestSec:allDurationUntrackedSec:allDurationNonNetworkBoundSec:allTimeUntilFirstSignpost:allTimeAfterLastSignpost:incompleteCount:completeDurationUnionSec:completeDurationSumSec:completeDurationLongestSec:completeTimeUntilFirstSignpost:environment:] : 1532 -> 1540
~ _WRSanitizeForCA : 152 -> 192
~ ___WRSanitizeForCA_block_invoke : 92 -> 128
~ ___370-[WRWorkflowEventTracker reportCoreAnalyticsEventForSignpost:allCount:allDurationUnionSec:allDurationSumSec:allDurationLongestSec:allDurationUntrackedSec:allDurationNonNetworkBoundSec:allTimeUntilFirstSignpost:allTimeAfterLastSignpost:incompleteCount:completeDurationUnionSec:completeDurationSumSec:completeDurationLongestSec:completeTimeUntilFirstSignpost:environment:]_block_invoke : 696 -> 700
CStrings:
+ "removeCharactersInString:"

```
