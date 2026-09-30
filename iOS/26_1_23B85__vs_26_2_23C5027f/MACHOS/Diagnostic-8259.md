## Diagnostic-8259

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8259.appex/Diagnostic-8259`

```diff

-921.40.62.0.0
+921.60.24.0.0
   __TEXT.__text: 0x2e9c
   __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x9e0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore
+  - /System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED21EAC2-EB02-30FC-A688-BD302DF3A19A
+  UUID: 7525E1D6-745B-36D0-85E1-10779C02E0C3
   Functions: 42
   Symbols:   89
   CStrings:  259

```
