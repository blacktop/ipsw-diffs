## MobileContainerManager

> `/System/Library/PrivateFrameworks/MobileContainerManager.framework/Versions/A/MobileContainerManager`

```diff

-689.0.0.0.0
-  __TEXT.__text: 0x2fc0
+689.100.6.0.0
+  __TEXT.__text: 0x2f74
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_methlist: 0x39c
-  __TEXT.__const: 0x328
+  __TEXT.__const: 0x330
   __TEXT.__cstring: 0xa2
   __TEXT.__oslogstring: 0x171
   __TEXT.__unwind_info: 0xf8

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12914BFF-FF48-372A-972E-C68E19050BAD
+  UUID: 4D3835C6-183E-312C-AAC3-12C403285317
   Functions: 66
   Symbols:   350
   CStrings:  136
Functions:
~ -[MCMContainerManager replaceContainer:withContainer:error:withCompletion:] : 408 -> 404
~ -[MCMContainerManager init] : 120 -> 104
~ -[MCMContainerManager(Internal) _containersWithClass:temporary:error:] : 1128 -> 1124
~ -[MCMContainer description] : 420 -> 416
~ -[MCMContainer diskUsageWithError:] : 204 -> 184
~ -[MCMContainer infoValueForKey:error:] : 280 -> 284
~ -[MCMContainer initWithIdentifier:createIfNecessary:existed:temp:error:] : 684 -> 672
~ -[MCMContainer init] : 120 -> 104
~ -[MCMContainer(Internal) initWithIdentifier:path:uniquePathComponent:uuid:personaUniqueString:uid:error:] : 876 -> 872

```
