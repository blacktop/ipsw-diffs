## appprotectiond

> `/usr/libexec/appprotectiond`

```diff

-35.1.1.0.0
+35.1.4.0.0
   __TEXT.__text: 0x34
   __TEXT.__auth_stubs: 0x10
   __TEXT.__objc_stubs: 0x20

   __DATA.__objc_selrefs: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
+  - /System/Library/PrivateFrameworks/AppProtectionDaemon.framework/AppProtectionDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1
Symbols:
+ _APDServerEntry
- _APRunServerUntilTheEndOfTime

```
