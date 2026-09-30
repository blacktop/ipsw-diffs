## com.apple.cloudsettings.keyboard

> `/System/Library/PrivateFrameworks/CloudSettings.framework/XPCServices/com.apple.cloudsettings.keyboard.xpc/com.apple.cloudsettings.keyboard`

```diff

-109.300.0.0.0
+119.0.0.0.0
   __TEXT.__text: 0x2b40
   __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x420

   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CloudSettings.framework/CloudSettings
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
-  - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3566F4BF-4379-34BA-B935-7E88B01D961B
+  UUID: D10CE151-2E3C-3C58-9E01-17FD55DDE6BB
   Functions: 104
   Symbols:   72
   CStrings:  301

```
