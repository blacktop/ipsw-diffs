## coreauthd

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/coreauthd`

```diff

-1394.40.33.0.0
-  __TEXT.__text: 0x215ec
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_stubs: 0x1fe0
-  __TEXT.__objc_methlist: 0x9bc
+1394.62.1.0.0
+  __TEXT.__text: 0x227dc
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_stubs: 0x2240
+  __TEXT.__objc_methlist: 0xb84
   __TEXT.__const: 0xf84
-  __TEXT.__objc_methname: 0x280e
-  __TEXT.__cstring: 0x1ea1
-  __TEXT.__objc_classname: 0x33a
-  __TEXT.__objc_methtype: 0x1104
+  __TEXT.__objc_methname: 0x2c2c
+  __TEXT.__cstring: 0x1ee2
+  __TEXT.__objc_classname: 0x3d1
+  __TEXT.__objc_methtype: 0x139f
   __TEXT.__oslogstring: 0x12e8
-  __TEXT.__gcc_except_tab: 0x148
-  __TEXT.__unwind_info: 0x8cc
-  __DATA_CONST.__auth_got: 0x660
-  __DATA_CONST.__got: 0xa0
+  __TEXT.__gcc_except_tab: 0x160
+  __TEXT.__unwind_info: 0x948
+  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__got: 0x98
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1e18
-  __DATA_CONST.__cfstring: 0xae0
-  __DATA_CONST.__objc_classlist: 0x98
-  __DATA_CONST.__objc_protolist: 0xa0
+  __DATA_CONST.__const: 0x1ea8
+  __DATA_CONST.__cfstring: 0xb20
+  __DATA_CONST.__objc_classlist: 0xb8
+  __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xd8
-  __DATA.__objc_const: 0x3be0
-  __DATA.__objc_selrefs: 0x9a8
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0x190
-  __DATA.__objc_superrefs: 0x60
-  __DATA.__objc_ivar: 0xd0
-  __DATA.__objc_data: 0x5f0
-  __DATA.__data: 0xec8
-  __DATA.__bss: 0x128
+  __DATA_CONST.__objc_arraydata: 0x10
+  __DATA_CONST.__objc_dictobj: 0x28
+  __DATA.__objc_const: 0x4900
+  __DATA.__objc_selrefs: 0xa68
+  __DATA.__objc_protorefs: 0x30
+  __DATA.__objc_classrefs: 0x1b8
+  __DATA.__objc_superrefs: 0x80
+  __DATA.__objc_ivar: 0xe4
+  __DATA.__objc_data: 0x730
+  __DATA.__data: 0xfe8
+  __DATA.__bss: 0x148
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14FC388C-D589-3A6F-ACD3-3B6750FD160B
-  Functions: 720
-  Symbols:   274
-  CStrings:  1126
+  UUID: F123BB90-2EA7-3B01-86EE-5183F1199E2A
+  Functions: 758
+  Symbols:   279
+  CStrings:  1191
 
Symbols:
+ _NSStringFromProtocol
+ _OBJC_CLASS_$_LACDarwinNotificationCenter
+ _OBJC_CLASS_$_LACServiceLocator
+ _OBJC_CLASS_$_NSConstantDictionary
+ _objc_alloc_init
+ _objc_autorelease
- _kLAServiceTypeSecureStorage
CStrings:
+ "@\"<LACDarwinNotificationCenter>\""
+ "@\"<LACServiceLocator>\""
+ "@\"SecureStorageConfiguration\""
+ "@20@0:8B16"
+ "@24@0:8@\"NSString\"16"
+ "@32@0:8@16q24"
+ "@40@0:8q16@24^@32"
+ "B24@0:8@\"<LACDarwinNotificationCenterObserver>\"16"
+ "B56@0:8q16q24@32@40@?48"
+ "DaemonServiceLocator"
+ "LACDarwinNotificationCenter"
+ "LACServiceLocator"
+ "LACXPCClientInfo"
+ "Operation not supported for key: %d."
+ "SecureStorageConfiguration"
+ "SecureStorageMock"
+ "SecureStorageProvider"
+ "T@\"<LACDarwinNotificationCenter>\",R,N,V_darwinNotificationCenter"
+ "T@\"SecureStorageConfiguration\",R,N,V_config"
+ "TB,R,N,V_bypassEntitlementChecks"
+ "_bypassEntitlementChecks"
+ "_checkEntitlementForKey:operation:value:connection:failureHandler:"
+ "_config"
+ "_darwinNotificationCenter"
+ "_evaluatePolicy:options:originator:preflightKey:uiDelegate:request:reply:"
+ "_locator"
+ "_notificationObservers"
+ "_startNotificationServices"
+ "_storageObjectForKey:data:error:"
+ "_updateOptionsWithServerProperties:policy:"
+ "aclForKey:contextUUID:connection:completionHandler:"
+ "addObserver:"
+ "addObserver:notification:"
+ "allowsMultipleClientsForServiceType:"
+ "bypassEntitlementChecks"
+ "checkKey:supportsOperation:"
+ "config"
+ "darwinNotificationCenter"
+ "errorNotSupported"
+ "hasObserver:"
+ "initWithBypassEntitlementChecks:"
+ "initWithConfig:"
+ "kLAServiceTypeSecureStorage"
+ "listenToLaunchNotifications"
+ "objectForKey:contextUUID:connection:completionHandler:"
+ "performAsyncUpdatesWithCompletion:"
+ "postNotification:"
+ "registerService:identifier:"
+ "removeObjectForKey:contextUUID:connection:completionHandler:"
+ "removeObserver:"
+ "secureStorage"
+ "secureStorageWithConfig:"
+ "serviceWithIdentifier:"
+ "setObject:acl:forKey:contextUUID:connection:completionHandler:"
+ "setServiceLocator:"
+ "startServices"
+ "v24@0:8@\"<LACDarwinNotificationCenterObserver>\"16"
+ "v24@0:8^{__CFString=}16"
+ "v32@0:8@\"<LACDarwinNotificationCenterObserver>\"16^{__CFString=}24"
+ "v32@0:8@16@\"NSString\"24"
+ "v32@0:8@16^{__CFString=}24"
+ "v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v48@0:8q16@\"NSUUID\"24@\"NSXPCConnection\"32@?<v@?@@\"NSError\">40"
+ "v64@0:8@\"NSData\"16@\"NSData\"24q32@\"NSUUID\"40@\"NSXPCConnection\"48@?<v@?@@\"NSError\">56"
+ "v64@0:8@16@24q32@40@48@?56"
+ "v72@0:8q16@24@32@40@48@56@?64"
- "B48@0:8q16q24@32@?40"
- "_checkEntitlementForKey:operation:value:failureHandler:"
- "_evaluatePolicy:options:originator:preflightKey:uiDelegate:reply:"

```
