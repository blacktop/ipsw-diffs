## companiond

> `/usr/libexec/companiond`

```diff

-98.10.9.0.0
-  __TEXT.__text: 0x1ee3c
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_stubs: 0x3200
-  __TEXT.__objc_methlist: 0x1cc4
+156.20.24.1.1
+  __TEXT.__text: 0x1f9d8
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_stubs: 0x3360
+  __TEXT.__objc_methlist: 0x1de8
   __TEXT.__const: 0x8e
-  __TEXT.__gcc_except_tab: 0x1304
-  __TEXT.__cstring: 0x16d7
-  __TEXT.__oslogstring: 0x1db9
-  __TEXT.__objc_classname: 0x642
-  __TEXT.__objc_methtype: 0x11eb
-  __TEXT.__objc_methname: 0x4797
+  __TEXT.__gcc_except_tab: 0x1344
+  __TEXT.__cstring: 0x1724
+  __TEXT.__oslogstring: 0x1eab
+  __TEXT.__objc_classname: 0x6b3
+  __TEXT.__objc_methtype: 0x1249
+  __TEXT.__objc_methname: 0x49ff
   __TEXT.__ustring: 0x40
-  __TEXT.__unwind_info: 0xb10
-  __DATA_CONST.__auth_got: 0x378
-  __DATA_CONST.__got: 0x3f8
+  __TEXT.__unwind_info: 0xb40
+  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0x418
   __DATA_CONST.__const: 0xa70
-  __DATA_CONST.__cfstring: 0x16c0
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__cfstring: 0x1760
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x130
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5378
-  __DATA.__objc_selrefs: 0xed0
-  __DATA.__objc_ivar: 0x33c
-  __DATA.__objc_data: 0xd20
-  __DATA.__data: 0x4e0
+  __DATA.__objc_const: 0x5810
+  __DATA.__objc_selrefs: 0xf80
+  __DATA.__objc_ivar: 0x350
+  __DATA.__objc_data: 0xe10
+  __DATA.__data: 0x600
   __DATA.__bss: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/AuthenticationServicesCore.framework/AuthenticationServicesCore

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
+  - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /System/Library/PrivateFrameworks/SafariFoundation.framework/SafariFoundation
   - /System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials

   - /System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 948
-  Symbols:   240
-  CStrings:  1398
+  Functions: 969
+  Symbols:   247
+  CStrings:  1452
 
Symbols:
+ _OBJC_CLASS_$_ISSymbol
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_UTType
+ _RPOptionSenderIDSDeviceID
+ __os_signpost_emit_with_name_impl
+ _cps_signpost_log
+ _os_signpost_enabled
CStrings:
+ "@\"CPSDevice\""
+ "@\"LSApplicationRecord\""
+ "@24@0:8@\"NSCoder\"16"
+ "@40@0:8@16@24^@32"
+ "CDAuthInfoInstalledApplication"
+ "CDAuthInfoProvider"
+ "CDAuthInfoProviding"
+ "CPSUIBannerRequest"
+ "CPSUIBannerRequest: device = nil"
+ "CPSUIBannerRequest: device model = %!@(MISSING)"
+ "CPSUIBannerRequest: device model = nil, device = %!@(MISSING)"
+ "Failed to load application record: %!@(MISSING)"
+ "Missing bundle identifier"
+ "NSCoding"
+ "NSSecureCoding"
+ "Received get auth type request."
+ "Rejecting get notif info request from device with IDS ID %!@(MISSING)"
+ "StartAuthentication"
+ "T@\"CPSDevice\",&,N,V_device"
+ "T@\"NSString\",&,N,V_text"
+ "T@\"NSString\",R,N,V_iconImageName"
+ "T@\"NSString\",R,N,V_requestIdentifier"
+ "TB,R"
+ "_applicationRecord"
+ "_device"
+ "_iconImageName"
+ "_notifyDeviceIDSIdentifier"
+ "_requestIdentifier"
+ "_text"
+ "_typeWithDeviceModelCode:"
+ "applicationIdentifier"
+ "auth session/handle get auth type request"
+ "createWithRequest:client:error:"
+ "decodeObjectOfClass:forKey:"
+ "device"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "iconImageName"
+ "initWithApplicationRecord:"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithCoder:"
+ "iphone"
+ "localizedName"
+ "requestIdentifier"
+ "setDevice:"
+ "setText:"
+ "supportsSecureCoding"
+ "symbolForTypeIdentifier:error:"
+ "teamIdentifier"
+ "text"
+ "v24@0:8@\"NSCoder\"16"
+ "websiteDomain"
- "Received get auth info request."
- "auth session/handle get auth info request"

```
