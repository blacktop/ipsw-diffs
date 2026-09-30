## FrontBoard

> `/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`

```diff

 1000.1.4.0.0
-  __TEXT.__text: 0x8cd44
+  __TEXT.__text: 0x8cd34
   __TEXT.__auth_stubs: 0xfd0
   __TEXT.__objc_methlist: 0x5b38
   __TEXT.__const: 0x324

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7B8DC64-4E69-371F-95C9-90C3713E4D1C
+  UUID: 3388287C-1B35-3247-AC40-E76808832340
   Functions: 3051
   Symbols:   10520
   CStrings:  6040
Functions:
~ -[FBSceneObserver delegate] : 80 -> 68
~ -[FBSceneSynchronizer _setWaitingForConnect] : 136 -> 144
~ -[FBScene _resetUpdateState] : 108 -> 116
~ -[FBWorkspaceConnection workspaceLock_isValid] : 64 -> 60
~ -[FBWorkspaceConnection isOutgoing] : 64 -> 60
~ -[FBWorkspaceEndpointPromise isResolvedNullEndpoint] : 144 -> 140
~ -[FBWorkspaceOutgoingConnection initWithWorkspace:] : 48 -> 44
~ -[FBWorkspaceOutgoingConnection queue_isVerified] : 84 -> 80

```
