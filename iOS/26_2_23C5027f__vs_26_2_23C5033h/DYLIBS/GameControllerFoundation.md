## GameControllerFoundation

> `/System/Library/PrivateFrameworks/GameControllerFoundation.framework/GameControllerFoundation`

```diff

-13.2.7.0.0
-  __TEXT.__text: 0x6eaf4
+13.2.8.0.0
+  __TEXT.__text: 0x6eadc
   __TEXT.__auth_stubs: 0x1440
   __TEXT.__objc_methlist: 0x6934
   __TEXT.__const: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09223D50-FBBD-3E37-99B4-AF195B97FEF7
+  UUID: 3B01088D-C890-3FF1-935D-345820BDAD8B
   Functions: 2858
-  Symbols:   9861
+  Symbols:   9862
   CStrings:  4322
 
Symbols:
+ ___chkstk_darwin
Functions:
~ _OUTLINED_FUNCTION_5 : 24 -> 28
~ _OUTLINED_FUNCTION_6 : 20 -> 24
~ _OUTLINED_FUNCTION_7 : 28 -> 20
~ -[NSXPCConnection(GC) gc_peerBundleIdentifier] : 396 -> 416
~ -[GCHIDInputElement valueChanged:] : 360 -> 356
~ -[__GCHIDSystemObservation NOTIFY_OBSERVER_SERVICES_CHANGED:ADDED_SERVICES:REMOVED_SERVICES:] : 140 -> 136
~ -[__GCHIDSystemObservation DO_OBSERVER_CALLOUT_FOR_EVENT:FROM:] : 136 -> 132
~ -[GCHIDEventSystemClient _servicesQueue] : 60 -> 56
~ -[GCHIDEventSystemClient servicesQueue] : 60 -> 56
~ _IOGCCircularControlQueueEntryModify : 328 -> 324
~ _IOGCCircularControlQueueEntryResetModifications : 328 -> 316
~ _IOGCFastPathInputQueueCancel.cold.2 : 60 -> 56
~ -[GCFuture _init] : 76 -> 72

```
