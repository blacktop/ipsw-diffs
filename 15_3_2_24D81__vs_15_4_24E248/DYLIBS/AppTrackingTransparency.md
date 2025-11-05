## AppTrackingTransparency

> `/System/Library/Frameworks/AppTrackingTransparency.framework/Versions/A/AppTrackingTransparency`

```diff

 104.0.0.0.0
-  __TEXT.__text: 0x118c
+  __TEXT.__text: 0x1198
   __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_methlist: 0xc8
   __TEXT.__const: 0x60

   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 05210F7F-57C3-3A2F-B183-E0575BA09BAC
-  Functions: 25
-  Symbols:   124
+  UUID: 14C7B4E4-A60D-39E4-AB1E-78203E9EE613
+  Functions: 28
+  Symbols:   127
   CStrings:  68
 
Symbols:
+ +[ATTrackingManager _TCCServer].cold.1
+ +[ATTrackingManager _applicationHasDisqualifyingEntitlement].cold.1
+ +[ATTrackingManager applicationStateActive].cold.1
Functions:
~ +[ATTrackingManager _applicationHasDisqualifyingEntitlement] : 68 -> 56
~ +[ATTrackingManager _TCCServer] : 84 -> 68
~ +[ATTrackingManager _trackingAuthorizationStatus] : 136 -> 132
~ +[ATTrackingManager applicationStateActive] : 92 -> 76

```
