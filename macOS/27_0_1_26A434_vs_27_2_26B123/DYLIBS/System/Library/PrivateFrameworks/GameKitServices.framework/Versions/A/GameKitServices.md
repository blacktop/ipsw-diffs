## GameKitServices

> `/System/Library/PrivateFrameworks/GameKitServices.framework/Versions/A/GameKitServices`

```diff

-2235.63.5.2.0
-  __TEXT.__text: 0x77c9c
+2260.15.1.0.0
+  __TEXT.__text: 0x783ac
   __TEXT.__objc_methlist: 0x2f40
   __TEXT.__const: 0x1960
   __TEXT.__gcc_except_tab: 0x764
-  __TEXT.__cstring: 0x69ae
-  __TEXT.__oslogstring: 0x11f20
+  __TEXT.__cstring: 0x69d1
+  __TEXT.__oslogstring: 0x11f93
   __TEXT.__unwind_info: 0xfe8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__auth_got: 0x900
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x504

   - /usr/lib/libz.1.dylib
   Functions: 1651
   Symbols:   3204
-  CStrings:  1876
+  CStrings:  1878
 
Functions:
~ _GCKSessionReceiveDOOB : 4728 -> 6556
~ ___GCKSessionReceiveDOOB_block_invoke : 100 -> 104
~ __GCKSessionReceiveDOOB_block_invoke.9 : 120 -> 124
~ __GCKSessionReceiveDOOB_block_invoke.11 : 120 -> 124
~ __GCKSessionReceiveDOOB_block_invoke.15 : 120 -> 124
~ __GCKSessionReceiveDOOB_block_invoke.19 : 120 -> 124
~ __GCKSessionReceiveDOOB_block_invoke.23 : 100 -> 104
~ __GCKSessionReceiveDOOB_block_invoke.27 : 100 -> 104
~ __GCKSessionReceiveDOOB_block_invoke.31 : 120 -> 124
~ __GCKSessionReceiveDOOB_block_invoke.35 : 120 -> 124
~ __GCKSessionReceiveDOOB_block_invoke.39 : 120 -> 124
~ -[GKVoiceChatServicePrivate receivedData:fromParticipantID:] : 4904 -> 4852
~ -[GKVoiceChatServicePrivate getNSError:code:description:reason:] : 400 -> 392
CStrings:
+ " [%s] %s:%d GCKSessionReceiveDOOB: session=%p unavailable (closing or invalid), dropped obType=%d participant=%08X"
+ "18:50:26"
+ "GCKSessionReceiveDOOB_block_invoke"
+ "Oct  3 2026"
- "19:45:49"
- "Aug  8 2026"
```
