## DASDelegate

> `/System/Library/PrivateFrameworks/DASDelegate.framework/DASDelegate`

```diff

-2109.80.9.0.0
-  __TEXT.__text: 0xbc8
-  __TEXT.__auth_stubs: 0x1d0
+2109.100.198.0.0
+  __TEXT.__text: 0xc24
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0xa0
   __TEXT.__const: 0x58
   __TEXT.__gcc_except_tab: 0x20
   __TEXT.__cstring: 0xdc
   __TEXT.__oslogstring: 0x125
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x29
   __TEXT.__objc_methname: 0x20e
   __TEXT.__objc_methtype: 0xde

   __DATA_CONST.__objc_selrefs: 0x98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x128
   __DATA.__objc_ivar: 0x8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 46617A3D-54B7-3F81-ACCB-CF32B4FF888A
+  UUID: E09E526B-C941-3B3C-9DA0-5A3F360A8164
   Functions: 22
-  Symbols:   126
+  Symbols:   121
   CStrings:  49
 
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x3
Functions:
~ -[DASDelegate connect] : 196 -> 204
~ -[DASDelegate disconnect] : 128 -> 132
~ -[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:] : 396 -> 388
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke : 124 -> 128
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.13 : 264 -> 268
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.15 : 156 -> 160
~ -[DASDelegate evaluateTailspinAt:withReply:] : 296 -> 292
~ ___44-[DASDelegate evaluateTailspinAt:withReply:]_block_invoke : 128 -> 132
~ ___44-[DASDelegate evaluateTailspinAt:withReply:]_block_invoke.20 : 520 -> 516
~ -[DASDelegate setLog:] : 12 -> 64
~ -[DASDelegate setConnectionToService:] : 12 -> 64
~ _OUTLINED_FUNCTION_0 : 28 -> 20
~ _OUTLINED_FUNCTION_1 : 12 -> 28
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.cold.1 : 52 -> 44
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.10.cold.1 : 52 -> 44
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.13.cold.1 : 52 -> 44
~ ___70-[DASDelegate appLaunchResumeInfoWithStartDate:withEndDate:withReply:]_block_invoke.15.cold.1 : 52 -> 44

```
