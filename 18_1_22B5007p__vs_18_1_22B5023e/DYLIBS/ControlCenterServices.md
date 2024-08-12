## ControlCenterServices

> `/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices`

```diff

-587.100.0.0.0
-  __TEXT.__text: 0xcb00
+594.0.0.0.0
+  __TEXT.__text: 0xd674
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x978
+  __TEXT.__objc_methlist: 0x9d8
   __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0xc0
-  __TEXT.__cstring: 0x136b
-  __TEXT.__oslogstring: 0xdf6
-  __TEXT.__unwind_info: 0x400
+  __TEXT.__cstring: 0x17d7
+  __TEXT.__oslogstring: 0xfe6
+  __TEXT.__unwind_info: 0x420
   __TEXT.__objc_classname: 0x1b5
-  __TEXT.__objc_methname: 0x2750
-  __TEXT.__objc_methtype: 0x59a
-  __TEXT.__objc_stubs: 0x1d00
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__const: 0x6b8
+  __TEXT.__objc_methname: 0x28b8
+  __TEXT.__objc_methtype: 0x5f0
+  __TEXT.__objc_stubs: 0x1da0
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x7d8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x818
+  __DATA_CONST.__objc_selrefs: 0x850
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x278
   __AUTH_CONST.__auth_got: 0x2e8
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x1040
-  __AUTH_CONST.__objc_const: 0x1938
+  __AUTH_CONST.__cfstring: 0x1340
+  __AUTH_CONST.__objc_const: 0x19b8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__bss: 0x98
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 329
-  Symbols:   501
-  CStrings:  688
+  Functions: 351
+  Symbols:   525
+  CStrings:  732
 
Symbols:
+ _CCSModuleSizeFromNSString
+ _NSStringFromCCSModuleSize
+ _NSStringFromIconElementRequestErrorCode
+ _OBJC_CLASS_$_INIntent
CStrings:
+ "\x114"
+ "@\"INIntent\""
+ "@48@0:8q16@24@32q40"
+ "CCSIconElementRequestErrorCodeFailedToCreateDataSource"
+ "CCSIconElementRequestErrorCodeFailedToFindIconElementToRemove"
+ "CCSIconElementRequestErrorCodeIconElementIsAlreadyInControlCenter"
+ "CCSIconElementRequestErrorCodeIconElementIsNotSupportedOnThisDevice"
+ "CCSIconElementRequestErrorCodeUnknown"
+ "CCSIconElementRequestErrorCodeUnknownElementType"
+ "CCSIconElementRequestErrorCodeUnknownIntentType"
+ "CCSIconElementRequestIntentAddIfElementDoesNotExistInControlCenter"
+ "CCSIconElementRequestIntentGetState"
+ "CCSIconElementTypeModuleWithDeprecatedSize"
+ "CCSModuleSizeLarge"
+ "CCSModuleSizeLargeExtraTall"
+ "CCSModuleSizeLargeTall"
+ "CCSModuleSizeMedium"
+ "CCSModuleSizeMediumWide"
+ "CCSModuleSizeSmall"
+ "CCSModuleSizeSmallExtraWide"
+ "CCSModuleSizeSmallTall"
+ "CCSModuleSizeSmallWide"
+ "Failed to request CCSIconElementState for CCSIconElementRequest error=%!@(MISSING)"
+ "No matching module size found for string: %!@(MISSING)"
+ "T@\"INIntent\",&,N,V_intentConfiguration"
+ "The application-identifier in your entitlements file is not allow-listed for handling CCSControlCenterOperationRequest"
+ "The application-identifier in your entitlements file is not allow-listed for handling CCSIconElementRequest"
+ "The application-identifier in your entitlements file is not allow-listed for requesting CCSIconElementState for CCSControlCenterOperationRequest"
+ "The application-identifier in your entitlements file is not allow-listed for this SPI. Please contact the Control Center team."
+ "Tq,R,N,V_moduleSize"
+ "_intentConfiguration"
+ "_moduleSize"
+ "com.apple.ControlCenter.RemoteServiceConnection.requestIconElementState"
+ "com.apple.Music"
+ "com.apple.accessibility.heard"
+ "com.apple.amp.MusicUI.MusicUIEngagementExtension"
+ "com.apple.tvremoted"
+ "initWithIntent:moduleIdentifier:containerBundleIdentifier:moduleSize:"
+ "intentConfiguration"
+ "intentDescription"
+ "kCSSIconElementRequestContainerBundleIdentifier"
+ "kCSSIconElementRequestControlKind"
+ "kCSSIconElementRequestControlType"
+ "kCSSIconElementRequestElementType"
+ "kCSSIconElementRequestExtensionBundleIdentifier"
+ "kCSSIconElementRequestIntent"
+ "kCSSIconElementRequestIntentConfiguration"
+ "kCSSIconElementRequestModuleIdentifier"
+ "kCSSIconElementRequestModuleSize"
+ "kCSSIconElementRequestSize"
+ "moduleSize"
+ "requestIconElementState:completionHandler:"
+ "requestIconElementStateWithOperationService:iconElementRequest:completionHandler:"
+ "setIntentConfiguration:"
+ "v24@?0Q8@\"NSError\"16"
+ "v32@0:8@\"CCSIconElementRequest\"16@?<v@?Q@\"NSError\">24"
- "#\x11"
- "Missing entitlement for handling CCSControlCenterOperationRequest"
- "Missing entitlement for handling CCSControlCenterOperationRequest"
- "Missing entitlement for handling CCSIconElementRequest"

```
