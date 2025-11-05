## FaceTimeDockSupport

> `/System/Library/PrivateFrameworks/FaceTimeDockSupport.framework/Versions/A/FaceTimeDockSupport`

```diff

-2975.400.141.0.0
-  __TEXT.__text: 0x968c
+2975.500.181.1.1
+  __TEXT.__text: 0x966c
   __TEXT.__auth_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0x658
+  __TEXT.__objc_methlist: 0x774
   __TEXT.__const: 0x98
   __TEXT.__cstring: 0x683
   __TEXT.__gcc_except_tab: 0x7c
   __TEXT.__ustring: 0xc
   __TEXT.__oslogstring: 0x2e1
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0x96
   __TEXT.__objc_methname: 0x1d8a
   __TEXT.__objc_methtype: 0x339

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x828
+  __DATA_CONST.__objc_selrefs: 0x8c8
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0x270
   __AUTH_CONST.__cfstring: 0xa00
-  __AUTH_CONST.__objc_const: 0xbd8
+  __AUTH_CONST.__objc_const: 0x9c8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x64

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/Versions/A/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CD2F17AA-E398-378D-A3AB-44C30C43B1E2
-  Functions: 179
-  Symbols:   660
+  UUID: 27EFE4EE-71BE-38B5-B688-938C54B1032B
+  Functions: 184
+  Symbols:   665
   CStrings:  583
 
Symbols:
+ +[FTRecentsController decimalFormatter].cold.1
+ +[FTTelephonyCapabilityManager sharedInstance].cold.1
+ -[NSDate(FaceTimeAdditions) faceTimeDateStringFromBundle:].cold.1
+ -[NSDate(FaceTimeAdditions) faceTimeDateStringFromBundle:].cold.2
+ FaceTimeOSLog.cold.1
Functions:
~ +[FTTelephonyCapabilityManager sharedInstance] : 84 -> 68
~ -[FTRecentsController initWithIsRTLBlock:] : 616 -> 612
~ -[FTRecentsController metadataCache] : 84 -> 80
~ -[FTRecentsController recentCalls] : 84 -> 80
~ ___41-[FTRecentsController itemForRecentCall:]_block_invoke : 6128 -> 6136
~ -[FTRecentsController localizedDisplayStringForItem:] : 4300 -> 4292
~ +[FTRecentsController decimalFormatter] : 84 -> 68
~ -[FTRecentsController contactFormatter] : 84 -> 80
~ -[FTRecentsController setContactFormatter:] : 120 -> 116
~ -[FTRecentsController numberFormatter] : 84 -> 80
~ -[FTRecentsController setNumberFormatter:] : 120 -> 116
~ -[FTRecentsController setRecentCalls:] : 232 -> 228
~ ___42-[FTRecentsController setUnreadCallCount:]_block_invoke : 172 -> 176
~ -[NSDate(FaceTimeAdditions) faceTimeDateStringFromBundle:] : 616 -> 584
~ _FaceTimeOSLog : 84 -> 68
~ _SetByHostObjectForKey : 400 -> 376

```
