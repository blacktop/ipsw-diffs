## Weather

> `/System/Library/PrivateFrameworks/Weather.framework/Weather`

```diff

   __DATA.__bss: 0x130
   __DATA.__common: 0x5
   __DATA_DIRTY.__objc_data: 0xfa0
-  __DATA_DIRTY.__bss: 0x2b8
+  __DATA_DIRTY.__bss: 0x2c0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/Frameworks/NotificationCenter.framework/NotificationCenter
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CoreUI.framework/CoreUI

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 5AD5D650-856A-371B-AE4D-50F006C388AA
+  UUID: B45680BE-6EFD-3EFC-9F7B-FD9AF11046F8
   Functions: 1822
   Symbols:   6727
   CStrings:  4788
Functions:
~ _WAImageForConditionNamed -> sub_22de379b0 : 20 -> 192
~ _WAImageForLegacyConditionCode -> sub_22de37a70 : 144 -> 180
~ _WAMapsImageForLegacyConditionCode -> _WAImageForConditionNamed : 448 -> 20
~ sub_2267caba4 -> _WAImageForLegacyConditionCode : 192 -> 144
~ _WAMapsImageWithinBundle -> _WAMapsImageForLegacyConditionCode : 204 -> 448
~ _WAImageForConditionCode -> _WAMapsImageWithinBundle : 552 -> 204
~ sub_2267caf58 -> _WAImageForConditionCode : 180 -> 552

```
