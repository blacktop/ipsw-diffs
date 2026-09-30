## ManagedConfigurationUI

> `/System/Library/PreferenceBundles/ManagedConfigurationUI.bundle/ManagedConfigurationUI`

```diff

-4.30.0.0.0
+4.34.0.0.0
   __TEXT.__text: 0x534
   __TEXT.__auth_stubs: 0x170
   __TEXT.__objc_stubs: 0x2a0

   __DATA.__objc_ivar: 0x4
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
+  - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/ManagedConfigurationUI.framework/ManagedConfigurationUI
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 7

```
