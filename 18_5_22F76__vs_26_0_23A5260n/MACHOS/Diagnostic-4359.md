## Diagnostic-4359

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4359.appex/Diagnostic-4359`

```diff

-820.122.1.0.0
+1053.0.0.0.0
   __TEXT.__text: 0xe74
   __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x320

   __DATA.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/WirelessInsights.framework/WirelessInsights
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
-  - /System/Library/PrivateFrameworks/WirelessInsights.framework/WirelessInsights
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 79069060-8731-363C-A599-1DCAE0D6653B
+  UUID: 0F8F69A4-2EF0-316F-AE28-B4FD22E4799C
   Functions: 17
   Symbols:   58
   CStrings:  62

```
