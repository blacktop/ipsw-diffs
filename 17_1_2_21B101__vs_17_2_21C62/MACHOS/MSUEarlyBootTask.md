## MSUEarlyBootTask

> `/usr/libexec/MSUEarlyBootTask`

```diff

-1856.42.1.0.0
+1856.60.8.0.0
   __TEXT.__text: 0x4080
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__objc_stubs: 0x4c0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 507A1E54-6162-3AC0-9DEC-6063EEE9B928
+  UUID: 140B6322-4481-3490-9E39-062AEA4EF53C
   Functions: 22
   Symbols:   301
   CStrings:  330

```
