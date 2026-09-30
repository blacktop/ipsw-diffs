## LiveFS

> `/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS`

```diff

-531.140.7.0.2
+531.140.9.0.3
   __TEXT.__text: 0x1d750
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x1f8c

   __TEXT.__gcc_except_tab: 0xd00
   __TEXT.__unwind_info: 0xa08
   __TEXT.__objc_classname: 0x334
-  __TEXT.__objc_methname: 0x42d9
+  __TEXT.__objc_methname: 0x42e2
   __TEXT.__objc_methtype: 0x2aac
   __TEXT.__objc_stubs: 0x2860
   __DATA_CONST.__got: 0x188

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 841FD563-6867-399F-8465-EBEFC45D1A27
+  UUID: B9639C32-E8A2-3010-9990-3B2AFD714219
   Functions: 781
   Symbols:   2673
   CStrings:  1363
Symbols:
+ -[LiveFSUserClient configureUserClient:pid:pidversion:supportBlockResource:]
+ -[LiveFSUserClient configureUserClient:pid:pidversion:supportBlockResource:].cold.1
- -[LiveFSUserClient configureUserClient:pid:pidversion:supportKOIO:]
- -[LiveFSUserClient configureUserClient:pid:pidversion:supportKOIO:].cold.1
CStrings:
+ "configureUserClient:pid:pidversion:supportBlockResource:"
- "configureUserClient:pid:pidversion:supportKOIO:"

```
