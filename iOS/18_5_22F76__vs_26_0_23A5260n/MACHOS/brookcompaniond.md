## brookcompaniond

> `/usr/libexec/brookcompaniond`

```diff

-241.0.0.0.0
+246.0.0.0.0
   __TEXT.__text: 0x1f50
   __TEXT.__auth_stubs: 0x310
   __TEXT.__objc_stubs: 0x820

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BrookServices.framework/BrookServices
   - /System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 524753D3-A216-3FF7-943A-9265D8AC36C7
+  UUID: 36DFF736-30F5-357E-ACDF-B4E03BE3578F
   Functions: 31
   Symbols:   81
   CStrings:  241

```
