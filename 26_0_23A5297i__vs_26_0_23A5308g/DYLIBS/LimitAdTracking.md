## LimitAdTracking

> `/System/Library/PrivateFrameworks/LimitAdTracking.framework/LimitAdTracking`

```diff

-637.1.7.0.0
-  __TEXT.__text: 0x38c0
+637.1.11.0.0
+  __TEXT.__text: 0x3a10
   __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_methlist: 0x268
+  __TEXT.__objc_methlist: 0x270
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x9c
-  __TEXT.__cstring: 0x177
-  __TEXT.__oslogstring: 0xcd5
+  __TEXT.__cstring: 0x184
+  __TEXT.__oslogstring: 0xd24
   __TEXT.__unwind_info: 0x160
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x7dd
+  __TEXT.__objc_methname: 0x7f3
   __TEXT.__objc_methtype: 0xc5
-  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x7e0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x280
+  __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_protorefs: 0x8
   __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x260
+  __AUTH_CONST.__cfstring: 0x280
   __AUTH_CONST.__objc_const: 0x3d0
   __AUTH.__objc_data: 0xa0
   __DATA.__data: 0x60

   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F50F729-275E-3338-85CB-2A609B983FAA
-  Functions: 70
-  Symbols:   311
-  CStrings:  199
+  UUID: A89FAA09-DF98-3103-9A68-B90A440D8D02
+  Functions: 71
+  Symbols:   314
+  CStrings:  204
 
Symbols:
+ -[ADTrackingTransparency _isUserProtoTeenState]
+ GCC_except_table10
+ ___43-[ADTrackingTransparency shouldDisplayPAUI]_block_invoke.27
+ ___43-[ADTrackingTransparency shouldDisplayPAUI]_block_invoke.30
+ ___45-[ADTrackingTransparency setPersonalizedAds:]_block_invoke.71
+ ___51-[ADTrackingTransparency personalizedAdsAvailable:]_block_invoke.51
+ ___51-[ADTrackingTransparency personalizedAdsAvailable:]_block_invoke.58
+ ___58-[ADTrackingTransparency accountLevelSwitchDisabledReason]_block_invoke.20
+ ___58-[ADTrackingTransparency accountLevelSwitchDisabledReason]_block_invoke.23
+ ___block_literal_global.26
+ ___block_literal_global.29
+ ___block_literal_global.50
+ ___block_literal_global.57
+ ___block_literal_global.70
+ ___block_literal_global.96
+ _objc_msgSend$_isUserProtoTeenState
- GCC_except_table5
- GCC_except_table9
- ___43-[ADTrackingTransparency shouldDisplayPAUI]_block_invoke.23
- ___43-[ADTrackingTransparency shouldDisplayPAUI]_block_invoke.26
- ___45-[ADTrackingTransparency setPersonalizedAds:]_block_invoke.62
- ___51-[ADTrackingTransparency personalizedAdsAvailable:]_block_invoke.47
- ___51-[ADTrackingTransparency personalizedAdsAvailable:]_block_invoke.50
- ___58-[ADTrackingTransparency accountLevelSwitchDisabledReason]_block_invoke.16
- ___58-[ADTrackingTransparency accountLevelSwitchDisabledReason]_block_invoke.19
- ___block_literal_global.18
- ___block_literal_global.25
- ___block_literal_global.46
- ___block_literal_global.49
- ___block_literal_global.61
- ___block_literal_global.93
Functions:
~ -[ADTrackingTransparency _userAllowedToChangeSettings] : 432 -> 524
+ -[ADTrackingTransparency _isUserProtoTeenState]
~ -[ADTrackingTransparency accountRestrictionReason] : 484 -> 600
~ -[ADTrackingTransparency adSwitchDisabledReasons] : 480 -> 528
CStrings:
+ "ProtoAccount"
+ "[%@] The device is in Proto Teen Mode."
+ "[%@] The device is in Proto Teen state."
+ "_isUserProtoTeenState"

```
