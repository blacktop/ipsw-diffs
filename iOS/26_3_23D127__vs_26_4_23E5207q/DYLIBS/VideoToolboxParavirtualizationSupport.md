## VideoToolboxParavirtualizationSupport

> `/System/Library/PrivateFrameworks/VideoToolboxParavirtualizationSupport.framework/VideoToolboxParavirtualizationSupport`

```diff

-63.4.3.0.0
-  __TEXT.__text: 0x654
-  __TEXT.__auth_stubs: 0x180
+64.4.4.0.0
+  __TEXT.__text: 0x684
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__const: 0x68
   __TEXT.__cstring: 0x68
   __TEXT.__unwind_info: 0x80
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x48
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x20
   __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /usr/lib/libSystem.B.dylib
-  UUID: DEBBCAA3-31F2-36FD-89A7-B387F5707316
-  Functions: 9
-  Symbols:   56
+  UUID: 9FD853E6-49A2-3CD0-A62B-391D61FE5011
+  Functions: 10
+  Symbols:   62
   CStrings:  3
 
Symbols:
+ _OUTLINED_FUNCTION_2
+ _dispatch_activate
+ _dispatch_queue_create_with_target$V2
+ _dispatch_release
+ _dispatch_workloop_create_inactive
+ _dispatch_workloop_set_scheduler_priority
- _dispatch_queue_create
Functions:
~ ___VTParavirtualizationGuestSupportSetUpWithHandlers_block_invoke : 312 -> 368
+ _OUTLINED_FUNCTION_2
~ _vtParavirtualizationGuestSupportUpdateBuffersForSize : 176 -> 164
~ _VTParavirtualizationGuestSupportSendRawMessageToHost : 468 -> 452

```
