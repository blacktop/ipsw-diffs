## AppSSO

> `/System/Library/PrivateFrameworks/AppSSO.framework/AppSSO`

```diff

-483.0.6.0.1
-  __TEXT.__text: 0x29038
+483.0.19.0.0
+  __TEXT.__text: 0x2901c
   __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_methlist: 0x1a94
   __TEXT.__const: 0x148
   __TEXT.__gcc_except_tab: 0x1bcc
-  __TEXT.__cstring: 0x2f83
+  __TEXT.__cstring: 0x2f86
   __TEXT.__dlopen_cstrs: 0x5e4
-  __TEXT.__oslogstring: 0x4283
+  __TEXT.__oslogstring: 0x4276
   __TEXT.__unwind_info: 0xd18
   __TEXT.__objc_classname: 0x3be
-  __TEXT.__objc_methname: 0x49e7
+  __TEXT.__objc_methname: 0x49ea
   __TEXT.__objc_methtype: 0xa91
   __TEXT.__objc_stubs: 0x3800
   __DATA_CONST.__got: 0x220

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE53F2B6-2414-3A97-B6B9-A528FCB62D98
+  UUID: 412890F5-CADE-3374-A2C4-0433EE4A2079
   Functions: 971
   Symbols:   3476
   CStrings:  1645
Symbols:
+ -[SOExtensionManager isLoadedExtensionWithBundleIdentifier:]
+ -[SOExtensionManager isLoadedExtensionWithBundleIdentifier:].cold.1
+ -[SOExtensionManager loadExtensionWithBundleIdentifier:completion:]
+ -[SOExtensionManager loadedExtensionWithBundleIdentifier:]
+ -[SOExtensionManager loadedExtensionWithBundleIdentifier:].cold.1
+ ___67-[SOExtensionManager loadExtensionWithBundleIdentifier:completion:]_block_invoke
+ _objc_msgSend$isLoadedExtensionWithBundleIdentifier:
+ _objc_msgSend$loadExtensionWithBundleIdentifier:completion:
+ _objc_msgSend$loadedExtensionWithBundleIdentifier:
- -[SOExtensionManager isLoadedExtensionWithBundleIdentifer:]
- -[SOExtensionManager isLoadedExtensionWithBundleIdentifer:].cold.1
- -[SOExtensionManager loadExtensionWithBundleIdentifer:completion:]
- -[SOExtensionManager loadedExtensionWithBundleIdentifer:]
- -[SOExtensionManager loadedExtensionWithBundleIdentifer:].cold.1
- ___66-[SOExtensionManager loadExtensionWithBundleIdentifer:completion:]_block_invoke
- _objc_msgSend$isLoadedExtensionWithBundleIdentifer:
- _objc_msgSend$loadExtensionWithBundleIdentifer:completion:
- _objc_msgSend$loadedExtensionWithBundleIdentifer:
Functions:
~ -[SOExtensionManager loadedExtensionWithBundleIdentifer:] -> -[SOExtensionManager loadedExtensionWithBundleIdentifier:] : 568 -> 540
CStrings:
+ "%s %{public}@ => %{public}@ on %@"
+ "-[SOExtensionManager isLoadedExtensionWithBundleIdentifier:]"
+ "-[SOExtensionManager loadExtensionWithBundleIdentifier:completion:]"
+ "-[SOExtensionManager loadedExtensionWithBundleIdentifier:]"
+ "isLoadedExtensionWithBundleIdentifier:"
+ "loadExtensionWithBundleIdentifier: identifier = %{public}@, extension = %{public}@, error = %{public}@"
+ "loadExtensionWithBundleIdentifier:completion:"
+ "loadedExtensionWithBundleIdentifier:"
- "%s %{public}@ => %{public}@ in %{public}@ on %@"
- "-[SOExtensionManager isLoadedExtensionWithBundleIdentifer:]"
- "-[SOExtensionManager loadExtensionWithBundleIdentifer:completion:]"
- "-[SOExtensionManager loadedExtensionWithBundleIdentifer:]"
- "isLoadedExtensionWithBundleIdentifer:"
- "loadExtensionWithBundleIdentifer: identifier = %{public}@, extension = %{public}@, error = %{public}@"
- "loadExtensionWithBundleIdentifer:completion:"
- "loadedExtensionWithBundleIdentifer:"

```
