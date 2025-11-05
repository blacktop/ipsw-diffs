## libSESShared.dylib

> `/usr/lib/libSESShared.dylib`

```diff

-53.2.0.0.0
-  __TEXT.__text: 0xd1f4
+54.21.1.0.0
+  __TEXT.__text: 0xd910
   __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x7e8
+  __TEXT.__objc_methlist: 0x838
   __TEXT.__const: 0xa50
-  __TEXT.__cstring: 0x99a
-  __TEXT.__oslogstring: 0x541
+  __TEXT.__cstring: 0xa17
+  __TEXT.__oslogstring: 0x5c1
   __TEXT.__gcc_except_tab: 0x12c
-  __TEXT.__unwind_info: 0x330
-  __TEXT.__objc_classname: 0x11b
-  __TEXT.__objc_methname: 0x1269
-  __TEXT.__objc_methtype: 0x47c
-  __TEXT.__objc_stubs: 0xde0
+  __TEXT.__unwind_info: 0x358
+  __TEXT.__objc_classname: 0x12c
+  __TEXT.__objc_methname: 0x12bd
+  __TEXT.__objc_methtype: 0x488
+  __TEXT.__objc_stubs: 0xe00
   __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__const: 0xc8
+  __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
-  __DATA_CONST.__objc_superrefs: 0x38
+  __DATA_CONST.__objc_selrefs: 0x680
+  __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0xcc0
+  __AUTH_CONST.__cfstring: 0xfa0
+  __AUTH_CONST.__objc_const: 0xdd0
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x74
+  __AUTH.__objc_data: 0x410
+  __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x8
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 739FA4D7-7B63-333E-9009-C573A785921F
-  Functions: 249
-  Symbols:   698
-  CStrings:  634
+  UUID: 28A81E89-6AD1-39A9-A8A5-47C477AFB7EC
+  Functions: 267
+  Symbols:   727
+  CStrings:  656
 
Symbols:
+ +[CertificationLogging getInstance].cold.1
+ +[CertificationLogging logEncryptedAPDU:decrypted:].cold.1
+ +[SESAlarm sharedObject].cold.1
+ +[SESBootUUID getBootUUID]
+ +[SESBootUUID getInstance].cold.1
+ +[SESXPCEventListener sharedObject].cold.1
+ -[NSArray(Functional) ses_contains:]
+ -[SESBootUUID bootUUID]
+ -[SESBootUUID setBootUUID:]
+ -[SESConfigAliro .cxx_destruct]
+ -[SESConfigAliro getConfiguration:]
+ -[SESConfigAliro init]
+ OBJC_IVAR_$_SESConfigAliro._mgDeviceClass
+ OBJC_IVAR_$_SESConfigAliro._mgProductVersion
+ OBJC_IVAR_$_SESConfigAliro._productVersion
+ SESDefaultLogObject.cold.1
+ SESInternalVariant.cold.1
+ _OBJC_CLASS_$_SESConfigAliro
+ _OBJC_METACLASS_$_SESConfigAliro
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_INSTANCE_METHODS_SESConfigAliro
+ __OBJC_$_INSTANCE_VARIABLES_SESConfigAliro
+ __OBJC_$_PROP_LIST_SESBootUUID
+ __OBJC_CLASS_RO_$_SESConfigAliro
+ __OBJC_METACLASS_RO_$_SESConfigAliro
+ _objc_msgSend$bootUUID
- -[NSArray(Functional) contains:]
CStrings:
+ "@24@0:8^@16"
+ "Aliro"
+ "EnableSharingFromWatch"
+ "Failed to retrieve version %@"
+ "KeyUpgradeEnabledForFriendKey"
+ "KeyUpgradeEnabledForOwnerKey"
+ "No applicable configuration found"
+ "No asset available"
+ "SESConfigAliro"
+ "T@\"NSString\",&,N,V_bootUUID"
+ "Wrong class for configurations"
+ "bootUUID"
+ "getBootUUID"
+ "getConfiguration:"
+ "ses_contains:"
+ "setBootUUID:"
- "KeyUpgradeEnabled"
- "contains:"

```
