## RemoteManagement

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/Versions/A/RemoteManagement`

```diff

-624.0.10.0.0
-  __TEXT.__text: 0x52a50
-  __TEXT.__objc_methlist: 0x1c38
+624.1.3.0.0
+  __TEXT.__text: 0x52a00
+  __TEXT.__objc_methlist: 0x1c48
   __TEXT.__const: 0x1a70
-  __TEXT.__cstring: 0x2521
+  __TEXT.__cstring: 0x2561
   __TEXT.__oslogstring: 0x4aeb
   __TEXT.__gcc_except_tab: 0x3e0
   __TEXT.__swift5_typeref: 0x6ae

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e0
+  __DATA_CONST.__objc_selrefs: 0x13e8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__got: 0x5f8
   __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__cfstring: 0x1b60
   __AUTH_CONST.__objc_const: 0x2f60
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0xb68

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1469
-  Symbols:   2062
-  CStrings:  715
+  Functions: 1470
+  Symbols:   2064
+  CStrings:  717
 
Symbols:
+ +[RMFeatureFlags isAccountTakeoverEnabled]
+ -[RMManagedDevice isAwaitingConfigurationWithScope:]
+ _RMConfigurationTypeExtensibleSSO
- -[RMManagedDevice isAwaitingConfiguration]
CStrings:
+ "AccountTakeover"
+ "com.apple.configuration.extensible-sso"
```
