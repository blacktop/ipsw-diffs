## TVPlayback

> `/System/Library/PrivateFrameworks/TVPlayback.framework/TVPlayback`

```diff

-598.40.16.0.0
-  __TEXT.__text: 0x6d75c
+598.40.17.0.0
+  __TEXT.__text: 0x6d828
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_methlist: 0x5ef0
   __TEXT.__const: 0x260
   __TEXT.__cstring: 0x6877
-  __TEXT.__oslogstring: 0x69e1
+  __TEXT.__oslogstring: 0x6a97
   __TEXT.__gcc_except_tab: 0x21f4
   __TEXT.__unwind_info: 0x1be8
   __TEXT.__objc_classname: 0x84b

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52016DEC-763E-3224-AE10-A2284799F508
+  UUID: 3F128281-4261-3314-A990-FDC672DB93D3
   Functions: 2256
   Symbols:   8333
-  CStrings:  5551
+  CStrings:  5553
 
Functions:
~ -[TVPPlayer setSynchronizationIdentifier:] : 132 -> 240
~ -[TVPPlayer _updateSynchronizationForAVQueuePlayer:synchronizationIdentifier:] : 732 -> 828
CStrings:
+ "Synchronization: Failed to sync with coordinator medium using identifier %@, error %@"
+ "Synchronization: Player %@, already synced using medium %@, with synchronizationIdentifier %@"
+ "Synchronization: Successfully synced player %@, using medium %@, with synchronizationIdentifier %@"
+ "Synchronization: synchronizationIdentifier set to: %@"
- "Failed to sync with coordinator medium using identifier %@, error %@"
- "Successfully synced player %@, using medium %@, with synchronizationIdentifier %@"

```
