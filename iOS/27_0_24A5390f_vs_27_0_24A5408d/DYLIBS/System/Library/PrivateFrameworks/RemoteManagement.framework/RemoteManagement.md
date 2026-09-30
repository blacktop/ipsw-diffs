## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/RemoteManagement`

```diff

-624.0.10.0.0
-  __TEXT.__text: 0x4bc9c
-  __TEXT.__objc_methlist: 0x1be0
+624.2.3.0.0
+  __TEXT.__text: 0x4bcc8
+  __TEXT.__objc_methlist: 0x1bf0
   __TEXT.__const: 0x180c
-  __TEXT.__cstring: 0x2357
+  __TEXT.__cstring: 0x2397
   __TEXT.__oslogstring: 0x492b
   __TEXT.__gcc_except_tab: 0x41c
   __TEXT.__swift5_typeref: 0x63b

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x658
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f8
+  __DATA_CONST.__objc_selrefs: 0x1418
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x598
   __AUTH_CONST.__const: 0xbf0
-  __AUTH_CONST.__cfstring: 0x1ae0
+  __AUTH_CONST.__cfstring: 0x1b00
   __AUTH_CONST.__objc_const: 0x2eb8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0xb68

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1388
-  Symbols:   2024
-  CStrings:  689
+  Functions: 1389
+  Symbols:   2028
+  CStrings:  691
 
Symbols:
+ +[RMFeatureFlags isAccountTakeoverEnabled]
+ -[RMManagedDevice isAwaitingConfigurationWithScope:]
+ _RMConfigurationTypeExtensibleSSO
+ _objc_msgSend$awaitUserConfigurationEnabled
+ _objc_msgSend$isAwaitingUserConfigured
- -[RMManagedDevice isAwaitingConfiguration]
CStrings:
+ "AccountTakeover"
+ "com.apple.configuration.extensible-sso"
```
