## ADAccountsNotificationPlugin

> `/System/Library/Accounts/Notification/ADAccountsNotificationPlugin.bundle/ADAccountsNotificationPlugin`

```diff

-637.1.7.0.0
-  __TEXT.__text: 0x73c
-  __TEXT.__auth_stubs: 0x160
+637.1.11.0.0
+  __TEXT.__text: 0xa28
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_methlist: 0x1a4
-  __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x214
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x255
+  __TEXT.__oslogstring: 0x45
   __TEXT.__unwind_info: 0x78
   __TEXT.__objc_classname: 0x43
-  __TEXT.__objc_methname: 0x379
+  __TEXT.__objc_methname: 0x451
   __TEXT.__objc_methtype: 0x204
-  __TEXT.__objc_stubs: 0x1a0
-  __DATA_CONST.__got: 0x20
+  __TEXT.__objc_stubs: 0x320
+  __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb8
+  __AUTH_CONST.__auth_got: 0x108
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x1c0
+  __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0x230
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AdCore.framework/AdCore
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C80909B7-B5CA-337D-B81E-5295A07D8C36
+  UUID: B1542DF0-B9B9-337C-A855-B14FD45EBB42
   Functions: 7
-  Symbols:   36
-  CStrings:  104
+  Symbols:   54
+  CStrings:  124
 
Symbols:
+ _MCFeatureApplePersonalizedAdvertisingAllowed
+ _MCFeatureIdentifierForAdvertisingAllowed
+ _NSSelectorFromString
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_NSUserDefaults
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __os_log_default
+ __os_log_impl
+ _objc_alloc
+ _objc_opt_respondsToSelector
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retain
+ _objc_retain_x21
+ _os_log_type_enabled
- _objc_retain_x19
Functions:
~ sub_248b82da4 -> sub_2984f0ec4 : 928 -> 1676
CStrings:
+ "ProtoAccount"
+ "[%@] This is a Proto Teen Account!"
+ "[%@] This is a Proto U13 Account!"
+ "aa_isChildProtoAccount"
+ "aa_isTeenProtoAccount"
+ "com.apple.AdPlatforms"
+ "getReturnValue:"
+ "initWithSuiteName:"
+ "invocationWithMethodSignature:"
+ "invoke"
+ "methodSignatureForSelector:"
+ "protoAccount"
+ "removeObjectForKey:"
+ "setBool:forKey:"
+ "setBoolValue:forSetting:"
+ "setSelector:"
+ "setTarget:"
+ "sharedConnection"
- "proto_ageRange"

```
