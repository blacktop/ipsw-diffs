## IMDPersistenceAgent

> `/System/Library/PrivateFrameworks/IMDPersistence.framework/XPCServices/IMDPersistenceAgent.xpc/IMDPersistenceAgent`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0x8a0
-  __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_stubs: 0x100
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0xc8
-  __TEXT.__cstring: 0x118
-  __TEXT.__oslogstring: 0x25d
-  __TEXT.__objc_methname: 0x6e
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x168
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0xe8
+1481.100.29.2.9
+  __TEXT.__text: 0x58c
+  __TEXT.__auth_stubs: 0x1d0
+  __TEXT.__objc_stubs: 0xc0
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x90
+  __TEXT.__cstring: 0xbd
+  __TEXT.__oslogstring: 0x20f
+  __TEXT.__objc_methname: 0x3d
+  __TEXT.__unwind_info: 0x88
+  __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x40
+  __DATA_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x38
+  __DATA.__objc_selrefs: 0x30
   __DATA.__data: 0x8
-  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48CE6AE8-4BF2-3BE4-A130-A2598DFABDAC
-  Functions: 10
-  Symbols:   59
-  CStrings:  28
+  UUID: 09A0A487-3C43-3FD0-BF02-24DC3B7CBA91
+  Functions: 4
+  Symbols:   42
+  CStrings:  21
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _IMDPersistenceProtectionMerge_CurrentlyUsingUnprotectedDatabase
- _OBJC_CLASS_$_IMFeatureFlags
- __NSConcreteStackBlock
- ___IMDPersistenceIPCServer_peer_event_handler
- ___stack_chk_fail
- ___stack_chk_guard
- _dispatch_once
- _dispatch_queue_create
- _objc_release
- _objc_release_x1
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x19
- _xpc_connection_resume
- _xpc_connection_set_event_handler
- _xpc_connection_set_target_queue
- _xpc_main
CStrings:
- "IMDPersistenceAgentConnectionQueue"
- "ProtectionMerge"
- "We are past first unlock but still using the unprotected database. Restarting"
- "isModernPersistenceXPCEnabled"
- "sharedFeatureFlags"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"
- "v8@?0"

```
