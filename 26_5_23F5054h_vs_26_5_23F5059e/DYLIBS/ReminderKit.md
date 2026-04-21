## ReminderKit

> `/System/Library/PrivateFrameworks/ReminderKit.framework/ReminderKit`

```diff

-3975.0.0.0.0
-  __TEXT.__text: 0x14d558
+3976.0.0.0.0
+  __TEXT.__text: 0x14d5c0
   __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0x157e0
-  __TEXT.__const: 0x16f7
+  __TEXT.__objc_methlist: 0x157f0
+  __TEXT.__const: 0x1717
   __TEXT.__oslogstring: 0x11a48
-  __TEXT.__cstring: 0xe370
+  __TEXT.__cstring: 0xe354
   __TEXT.__gcc_except_tab: 0x8360
-  __TEXT.__ustring: 0x292
+  __TEXT.__ustring: 0x2aa
   __TEXT.__dlopen_cstrs: 0xb4
   __TEXT.__unwind_info: 0x71a8
   __TEXT.__objc_classname: 0x3b5b
-  __TEXT.__objc_methname: 0x27a04
-  __TEXT.__objc_methtype: 0x4244
+  __TEXT.__objc_methname: 0x27a23
+  __TEXT.__objc_methtype: 0x4252
   __TEXT.__objc_stubs: 0x16740
   __DATA_CONST.__got: 0xf48
   __DATA_CONST.__const: 0x2a38

   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ac0
+  __DATA_CONST.__objc_selrefs: 0x7ac8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xa28
   __DATA_CONST.__objc_arraydata: 0x998

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 39C31515-0A3A-3801-8BEE-D8607BC086AD
-  Functions: 8751
-  Symbols:   28320
-  CStrings:  11447
+  UUID: 1137D2A7-E9F7-35F8-BF72-55843C4005DF
+  Functions: 8752
+  Symbols:   28322
+  CStrings:  11448
 
Symbols:
+ +[REMSnoozeTimeUtils nextThirdsHourFromHour:minute:]
+ _objc_msgSend$nextThirdsHourFromHour:minute:
- _objc_msgSend$nextThirdsHourFromHour:
Functions:
~ -[REMReminderChangeItem(Snooze) snoozeToNextThirds] : 272 -> 284
~ +[REMSnoozeTimeUtils nextThirdsHourFromHour:] : 152 -> 8
+ +[REMSnoozeTimeUtils nextThirdsHourFromHour:minute:]
CStrings:
+ "%1$@ – %2$@"
+ "Remind Me Tomorrow at %@"
+ "Remind Me at %@"
+ "Remind Me in 1 Hour"
+ "nextThirdsHourFromHour:minute:"
+ "q32@0:8q16q24"
- "Remind Me This Afternoon"
- "Remind Me Tonight"
- "Remind Me in an Hour"
- "Remind Me in the Morning"

```
