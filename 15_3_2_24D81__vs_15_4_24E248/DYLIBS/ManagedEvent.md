## ManagedEvent

> `/System/Library/PrivateFrameworks/Symptoms.framework/Versions/A/Frameworks/ManagedEvent.framework/Versions/A/ManagedEvent`

```diff

-2001.80.5.0.0
-  __TEXT.__text: 0xb68
+2022.100.26.0.0
+  __TEXT.__text: 0xb5c
   __TEXT.__auth_stubs: 0x1e0
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x184

   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
-  UUID: B002DD5A-DF0E-3A3B-B25A-8636A1F943B4
-  Functions: 21
-  Symbols:   158
+  UUID: 2F38100D-5A95-38D4-AB09-0053E00DF11E
+  Functions: 22
+  Symbols:   160
   CStrings:  95
 
Symbols:
+ __managed_event_send_with_reply_block_invoke.cold.1
+ managed_event_send_with_reply.cold.1
Functions:
~ _managed_event_send_with_reply : 184 -> 168
~ ___managed_event_send_with_reply_block_invoke : 408 -> 392
- _managed_event_fetch_completion

```
