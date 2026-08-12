## SystemExtensions

> `/System/Library/Frameworks/SystemExtensions.framework/SystemExtensions`

```diff

-224.0.2.0.0
-  __TEXT.__text: 0xc08
+224.0.4.0.0
+  __TEXT.__text: 0xb00
   __TEXT.__objc_methlist: 0x160
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x18d
-  __TEXT.__oslogstring: 0x24
+  __TEXT.__cstring: 0x11c
+  __TEXT.__oslogstring: 0xa6
   __TEXT.__unwind_info: 0x90
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x180
+  __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x370
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 27
-  Symbols:   162
-  CStrings:  15
+  Symbols:   158
+  CStrings:  12
 
Symbols:
+ _NSPOSIXErrorDomain
+ _NSUnderlyingErrorKey
+ _objc_msgSend$code
+ _objc_msgSend$domain
+ _objc_msgSend$driverApprovalStatesForCurrentAppWithError:
+ _objc_retain_x23
+ _objc_retain_x8
- _CFBooleanGetTypeID
- _CFBooleanGetValue
- _CFGetTypeID
- _SecTaskCopyValueForEntitlement
- _SecTaskCreateFromSelf
- _objc_msgSend$driverApprovalStatesForThirdPartyApp:
- _objc_msgSend$localizedDescription
- _objc_msgSend$refreshForCurrentAppSync
- _objc_msgSend$stringWithFormat:
- _objc_release_x8
- _objc_retain_x25
Functions:
~ -[OSSystemExtensionsWorkspace systemExtensionsForApplicationWithBundleID:error:] : 1388 -> 1124
CStrings:
+ "Driver approval state query failed: caller is missing the com.apple.developer.system-extension.install entitlement"
+ "Failed to fetch driver approval states: %{public}@"
+ "Missing the com.apple.developer.system-extension.install entitlement"
- "%{public}@"
- "DriverManagement returned nil for %@"
- "Failed to create SecTask"
- "Missing the %@ entitlement"
- "Require com.apple.developer.system-extension.install:true in entitlement"
- "com.apple.developer.system-extension.install"
```
