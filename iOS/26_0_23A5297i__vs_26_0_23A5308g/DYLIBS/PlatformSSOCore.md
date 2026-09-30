## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.0.28.0.0
-  __TEXT.__text: 0x8de20
+483.0.35.0.1
+  __TEXT.__text: 0x8e3e0
   __TEXT.__auth_stubs: 0x1ae0
-  __TEXT.__objc_methlist: 0x5ec0
-  __TEXT.__const: 0x16f4
-  __TEXT.__cstring: 0xa436
+  __TEXT.__objc_methlist: 0x5f10
+  __TEXT.__const: 0x1704
+  __TEXT.__cstring: 0xa4f6
   __TEXT.__oslogstring: 0x19e7
   __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__dlopen_cstrs: 0xa6

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
-  __TEXT.__unwind_info: 0x1fc8
+  __TEXT.__unwind_info: 0x1fe8
   __TEXT.__eh_frame: 0x5b8
   __TEXT.__objc_classname: 0xd3d
-  __TEXT.__objc_methname: 0xc7fb
+  __TEXT.__objc_methname: 0xc8f3
   __TEXT.__objc_methtype: 0x28de
-  __TEXT.__objc_stubs: 0x7020
-  __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x2430
+  __TEXT.__objc_stubs: 0x7040
+  __DATA_CONST.__got: 0x918
+  __DATA_CONST.__const: 0x2450
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ab8
+  __DATA_CONST.__objc_selrefs: 0x2af0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
   __AUTH_CONST.__auth_got: 0xd80
   __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x73a0
+  __AUTH_CONST.__cfstring: 0x7460
   __AUTH_CONST.__objc_const: 0x141b8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3E16BE8A-FCBB-3CD6-881F-89F7F0F5B320
-  Functions: 3591
-  Symbols:   11928
-  CStrings:  5056
+  UUID: 265D68EF-4459-3737-B2E7-02DB786B849F
+  Functions: 3602
+  Symbols:   11951
+  CStrings:  5077
 
Symbols:
+ +[POAnalytics analyticsForDeviceRegistrationInBuddy:]
+ +[POAnalytics analyticsForSetupAssistantLoginType:result:]
+ +[POAnalytics analyticsForTempSessionLoginType:result:]
+ +[POAnalytics analyticsForUserRegistrationInBuddy:]
+ +[POSecKeyHelper systemKeyForData:context:]
+ +[POSecKeyHelper systemKeyForData:context:].cold.1
+ -[PODeviceConfiguration deviceEncryptionKeyWithContext:]
+ -[PODeviceConfiguration deviceSigningKeyWithContext:]
+ ___43+[POSecKeyHelper systemKeyForData:context:]_block_invoke
+ ___43+[POSecKeyHelper systemKeyForData:context:]_block_invoke.cold.1
+ ___51+[POAnalytics analyticsForUserRegistrationInBuddy:]_block_invoke
+ ___53+[POAnalytics analyticsForDeviceRegistrationInBuddy:]_block_invoke
+ ___55+[POAnalytics analyticsForTempSessionLoginType:result:]_block_invoke
+ ___58+[POAnalytics analyticsForSetupAssistantLoginType:result:]_block_invoke
+ ___block_descriptor_33_e19_"NSDictionary"8?0l
+ ___block_literal_global.158
+ ___block_literal_global.450
+ ___block_literal_global.78
+ _objc_msgSend$systemKeyForData:context:
- +[POSecKeyHelper systemKeyForData:].cold.1
- ___35+[POSecKeyHelper systemKeyForData:]_block_invoke
- ___35+[POSecKeyHelper systemKeyForData:]_block_invoke.cold.1
- ___block_literal_global.157
- ___block_literal_global.447
- ___block_literal_global.72
- _xmlFree
CStrings:
+ "+[POSecKeyHelper systemKeyForData:context:]"
+ "?"
+ "analyticsForDeviceRegistrationInBuddy:"
+ "analyticsForSetupAssistantLoginType:result:"
+ "analyticsForTempSessionLoginType:result:"
+ "analyticsForUserRegistrationInBuddy:"
+ "beforeEnrollment"
+ "com.apple.PlatformSSO.setup.device"
+ "com.apple.PlatformSSO.setup.user"
+ "com.apple.PlatformSSO.setupAssistantLogin"
+ "com.apple.PlatformSSO.tempSessionLogin"
+ "deviceEncryptionKeyWithContext:"
+ "deviceSigningKeyWithContext:"
+ "postSessionChange"
+ "systemKeyForData:context:"
- "+[POSecKeyHelper systemKeyForData:]"

```
