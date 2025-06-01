## CallDirectorySettings

> `/System/Library/PreferenceBundles/CallDirectorySettings.bundle/CallDirectorySettings`

```diff

-2869.400.41.2.2
-  __TEXT.__text: 0x69f0
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_stubs: 0x1420
-  __TEXT.__objc_methlist: 0x5f8
-  __TEXT.__cstring: 0x65c
-  __TEXT.__objc_methname: 0x188e
-  __TEXT.__oslogstring: 0x63f
-  __TEXT.__objc_classname: 0x1e9
-  __TEXT.__objc_methtype: 0x3a0
+2869.500.151.2.2
+  __TEXT.__text: 0x76cc
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0x14e0
+  __TEXT.__objc_methlist: 0x6e8
+  __TEXT.__cstring: 0x7e5
+  __TEXT.__objc_methname: 0x1b24
+  __TEXT.__oslogstring: 0x70c
+  __TEXT.__objc_classname: 0x229
+  __TEXT.__objc_methtype: 0x3e5
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x1ec
-  __DATA_CONST.__auth_got: 0x1f8
-  __DATA_CONST.__got: 0xa8
+  __TEXT.__unwind_info: 0x22c
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__const: 0x268
-  __DATA_CONST.__cfstring: 0x620
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x50
-  __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA.__objc_const: 0x10d8
-  __DATA.__objc_selrefs: 0x5f0
-  __DATA.__objc_classrefs: 0xe8
-  __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0x74
-  __DATA.__objc_data: 0x280
+  __DATA_CONST.__objc_classrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arrayobj: 0x78
+  __DATA_CONST.__objc_intobj: 0x18
+  __DATA.__objc_const: 0x1330
+  __DATA.__objc_selrefs: 0x638
+  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_data: 0x320
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x40
   - /System/Library/Frameworks/CallKit.framework/CallKit

   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E7BB952D-A53B-3AE2-A96A-FDCC815CBC72
-  Functions: 161
-  Symbols:   138
-  CStrings:  466
+  UUID: 85790AAF-9F49-30D0-AD76-A346CFEF3F7F
+  Functions: 180
+  Symbols:   145
+  CStrings:  509
 
Symbols:
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_PHBusinessCallingController
+ _OBJC_CLASS_$_PHBusinessCallingListController
+ _OBJC_CLASS_$_PHBusinessConnectCallingController
+ _OBJC_METACLASS_$_PHBusinessCallingController
+ _OBJC_METACLASS_$_PHBusinessCallingListController
+ _OBJC_METACLASS_$_PHBusinessConnectCallingController
+ _TUBusinessConnectCallingDisabledKey
+ __os_feature_enabled_impl
- _OBJC_CLASS_$_PHBrandedCallingListController
- _OBJC_METACLASS_$_PHBrandedCallingListController
CStrings:
+ "@\"PHBusinessCallingController\""
+ "@\"PHBusinessConnectCallingController\""
+ "BUSINESS_CALLING_OFF"
+ "BUSINESS_CALLING_ON"
+ "BUSINESS_CALLING_SINGLE_CARRIER_FOOTER_TEXT"
+ "BUSINESS_CALLING_SPECIFIER_TITLE"
+ "BUSINESS_CALLING_TWO_CARRIER_FOOTER_TEXT"
+ "BUSINESS_CONNECT_CALLING_FOOTER_TEXT"
+ "BUSINESS_CONNECT_CALLING_GROUP_HEADER"
+ "BUSINESS_CONNECT_CALLING_SPECIFIER_TITLE"
+ "BusinessCallingGroup"
+ "BusinessConnectCallingGroup"
+ "PHBusinessCallingController"
+ "PHBusinessCallingListController"
+ "PHBusinessConnectCallingController"
+ "Retrieved verstat feature capability value '%@' for subscription %@"
+ "Retrieving verstat feature capability value for subscription %@ failed with error %@"
+ "T@\"NSString\",?,R,C"
+ "T@\"PHBrandedCallingController\",&,N,V_brandedCallingController"
+ "T@\"PHBusinessCallingController\",R,N,V_businessCallingController"
+ "T@\"PHBusinessConnectCallingController\",&,N,V_businessConnectCallingController"
+ "T@\"PHBusinessConnectCallingController\",R,N,V_businessConnectCallingController"
+ "TelephonyUtilities"
+ "User toggled business connect calling switch to %@"
+ "VerstatFeatureCapability"
+ "_businessCallingController"
+ "_businessConnectCallingController"
+ "addBusinessCallingSpecifierIfNecessary:"
+ "businessCallingController"
+ "businessConnectCallingController"
+ "callsBusinessMetadataQuery"
+ "featureEnabledForAtLeastOneContext"
+ "getBooleanFromUserDefaults:default:"
+ "getBusinessConnectCallingEnabled"
+ "groupFooterTextFor:"
+ "i"
+ "isBusinessCallingEnabled"
+ "setBrandedCallingController:"
+ "setBusinessConnectCallingController:"
+ "setCallBusinessConnectCallingEnabled:"
+ "setValue:forKey:"
+ "setValueInUserDefaults:forKey:"
+ "shouldShow extensions=%ld service providers=%ld business calling specifiers=%ld"
+ "supportsBusinessConnectCallingForSubscriptionContext:"
+ "updateBusinessCallingState"
- "BRANDED_CALLING_OFF"
- "BRANDED_CALLING_ON"
- "PHBrandedCallingListController"
- "T@\"PHBrandedCallingController\",&,N,V_controller"
- "_controller"
- "addBrandedCallingSpecifierIfNecessary:"
- "controller"
- "groupFooterText"
- "groupSpecifierWithName:"
- "multiSimGetter"
- "setController:"
- "shouldShow extensions=%ld service providers=%ld branded calling specifiers=%ld"

```
