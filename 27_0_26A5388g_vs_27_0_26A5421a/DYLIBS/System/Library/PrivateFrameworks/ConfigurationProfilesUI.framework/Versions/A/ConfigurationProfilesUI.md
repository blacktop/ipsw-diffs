## ConfigurationProfilesUI

> `/System/Library/PrivateFrameworks/ConfigurationProfilesUI.framework/Versions/A/ConfigurationProfilesUI`

```diff

-1911.0.1.0.0
-  __TEXT.__text: 0x5ac5c
+1911.1.1.0.0
+  __TEXT.__text: 0x5ac74
   __TEXT.__objc_methlist: 0x31a8
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xb9c4
-  __TEXT.__cstring: 0xe047
+  __TEXT.__gcc_except_tab: 0xb9b0
+  __TEXT.__cstring: 0xe088
   __TEXT.__ustring: 0x60
   __TEXT.__dlopen_cstrs: 0x129
   __TEXT.__oslogstring: 0xe

   __DATA_CONST.__objc_arraydata: 0x318
   __DATA_CONST.__got: 0x7f0
   __AUTH_CONST.__const: 0x1bc0
-  __AUTH_CONST.__cfstring: 0xb6a0
+  __AUTH_CONST.__cfstring: 0xb6e0
   __AUTH_CONST.__objc_const: 0x4c38
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0xf0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1758
-  Symbols:   4227
-  CStrings:  1623
+  Symbols:   4226
+  CStrings:  1625
 
Symbols:
- _objc_msgSend$isManaged
Functions:
~ -[CPUI_CloudConfigurationWelcomeController _updateUI:reason:] : 3432 -> 3456
CStrings:
+ "%@: updateUI(%@ : %@): state: %@; phase: %@; DEPNag: %@; MDMMig: %@"
+ "Wait for cloud configuration timed out (will allow retry)"
+ "managed (config present)"
+ "unmanaged (empty config)"
- "%@: updateUI(%@ : %@): isManaged: %@; phase: %@; DEPNag: %@; MDMMig: %@"
- "Wait for cloud configuration timed out"
```
