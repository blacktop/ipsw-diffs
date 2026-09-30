## AAUIFollowUpExtension

> `/System/Library/PrivateFrameworks/AppleAccountUI.framework/PlugIns/AAUIFollowUpExtension.appex/AAUIFollowUpExtension`

```diff

-520.229.0.0.0
-  __TEXT.__text: 0x7e50
+520.456.0.0.0
+  __TEXT.__text: 0x80e8
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x1520
-  __TEXT.__objc_methlist: 0x278
+  __TEXT.__objc_stubs: 0x1600
+  __TEXT.__objc_methlist: 0x550
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__cstring: 0x4f2
-  __TEXT.__objc_methname: 0x1ab5
-  __TEXT.__oslogstring: 0x1758
+  __TEXT.__cstring: 0x547
+  __TEXT.__objc_methname: 0x1b3f
+  __TEXT.__oslogstring: 0x172b
   __TEXT.__objc_classname: 0x117
   __TEXT.__objc_methtype: 0x7a4
   __TEXT.__unwind_info: 0x208
   __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x488
-  __DATA_CONST.__cfstring: 0x3e0
+  __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x9f0
-  __DATA.__objc_selrefs: 0x5c8
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA.__objc_const: 0x4e0
+  __DATA.__objc_selrefs: 0x740
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x300

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/AAAFoundation.framework/AAAFoundation
   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication

   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 158
-  Symbols:   137
-  CStrings:  457
+  Functions: 157
+  Symbols:   142
+  CStrings:  468
 
Symbols:
+ _AAFollowUpIdentifierChildProtoConnect
+ _OBJC_CLASS_$_AAAnalyticsRTCReporter
+ _OBJC_CLASS_$_AAFAnalyticsEvent
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSUUID
CStrings:
+ "UUID"
+ "UUIDString"
+ "analyticsEventWithName:altDSID:flowID:"
+ "client"
+ "com.apple.appleAccount.processRenewCredentials"
+ "i"
+ "numberWithBool:"
+ "populateUnderlyingErrorsStartingWithRootError:"
+ "proxiedDevices"
+ "reporter"
+ "sendEvent:"
- "_renewCredentialsForFollowUpItem starting..."

```
