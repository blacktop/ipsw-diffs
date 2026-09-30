## MobileContainerManager

> `/System/Library/PrivateFrameworks/MobileContainerManager.framework/MobileContainerManager`

```diff

-725.0.8.0.0
+725.0.10.0.0
   __TEXT.__text: 0x2cc0
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_methlist: 0x39c
   __TEXT.__const: 0x330
   __TEXT.__cstring: 0xa2
   __TEXT.__oslogstring: 0x171
-  __TEXT.__unwind_info: 0x100
+  __TEXT.__unwind_info: 0xf8
   __TEXT.__objc_classname: 0x1a0
   __TEXT.__objc_methname: 0x67f
   __TEXT.__objc_methtype: 0x1b9

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87380E18-0044-3B59-9017-A47A875F3A2D
+  UUID: 72B5C3F3-795F-3992-A356-2BC6AB6B7DD5
   Functions: 64
   Symbols:   430
   CStrings:  136
Functions:
~ +[MCMPluginKitPluginDataContainer typeContainerClass] -> sub_22ddc1cf8 : 76 -> 56
~ sub_22d964e28 -> +[MCMInternalDaemonDataContainer typeContainerClass] : 56 -> 76
~ +[MCMPluginKitPluginContainer typeContainerClass] -> -[MCMDataContainer wipeAllMyContainerContent:] : 76 -> 176
~ -[MCMDataContainer wipeAllMyContainerContent:] -> +[MCMAppContainer typeContainerClass] : 176 -> 76

```
