## ControlCenterServices

> `/System/Library/PrivateFrameworks/ControlCenterServices.framework/ControlCenterServices`

```diff

-520.1.0.0.0
-  __TEXT.__text: 0xb138
+520.7.100.0.0
+  __TEXT.__text: 0xb4d8
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x7b8
+  __TEXT.__objc_methlist: 0x7c8
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__cstring: 0x10a6
-  __TEXT.__oslogstring: 0xc14
-  __TEXT.__unwind_info: 0x374
+  __TEXT.__cstring: 0x10cb
+  __TEXT.__oslogstring: 0xca5
+  __TEXT.__unwind_info: 0x370
   __TEXT.__objc_classname: 0x17b
-  __TEXT.__objc_methname: 0x2231
-  __TEXT.__objc_methtype: 0x497
-  __TEXT.__objc_stubs: 0x1ae0
+  __TEXT.__objc_methname: 0x22e1
+  __TEXT.__objc_methtype: 0x49a
+  __TEXT.__objc_stubs: 0x1b20
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x660
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a90
-  __DATA_CONST.__objc_selrefs: 0x750
+  __DATA_CONST.__objc_const: 0x1ac0
+  __DATA_CONST.__objc_selrefs: 0x760
   __DATA_CONST.__objc_arraydata: 0x328
-  __AUTH_CONST.__cfstring: 0xce0
-  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0xd20
+  __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__objc_const: 0x550
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x150

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x108
   __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0x98
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x88

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 281
-  Symbols:   1181
-  CStrings:  595
+  Functions: 284
+  Symbols:   1191
+  CStrings:  603
 
Symbols:
+ +[CCSModuleMetadata _requiredIncapabilitiesForInfoDictionary:]
+ -[CCSModuleMetadata _initWithModuleIdentifier:supportedDeviceFamilies:requiredDeviceCapabilities:requiredDeviceIncapabilities:associatedBundleIdentifier:associatedBundleMinimumVersion:visibilityPreference:moduleBundleURL:]
+ -[CCSModuleMetadata requiredDeviceIncapabilities]
+ _OBJC_IVAR_$_CCSModuleMetadata._requiredDeviceIncapabilities
+ ___62+[CCSModuleMetadata _requiredIncapabilitiesForInfoDictionary:]_block_invoke
+ ___block_literal_global.25
+ __unnamed_array_storage.123
+ __unnamed_array_storage.129
+ __unnamed_array_storage.132
+ __unnamed_array_storage.135
+ __unnamed_array_storage.141
+ __unnamed_array_storage.148
+ __unnamed_array_storage.151
+ __unnamed_array_storage.154
+ __unnamed_array_storage.160
+ __unnamed_array_storage.163
+ __unnamed_array_storage.166
+ _objc_msgSend$_initWithModuleIdentifier:supportedDeviceFamilies:requiredDeviceCapabilities:requiredDeviceIncapabilities:associatedBundleIdentifier:associatedBundleMinimumVersion:visibilityPreference:moduleBundleURL:
+ _objc_msgSend$_requiredIncapabilitiesForInfoDictionary:
+ _objc_msgSend$requiredDeviceIncapabilities
- -[CCSModuleMetadata _initWithModuleIdentifier:supportedDeviceFamilies:requiredDeviceCapabilities:associatedBundleIdentifier:associatedBundleMinimumVersion:visibilityPreference:moduleBundleURL:]
- ___block_literal_global.17
- __unnamed_array_storage.124
- __unnamed_array_storage.130
- __unnamed_array_storage.133
- __unnamed_array_storage.136
- __unnamed_array_storage.142
- __unnamed_array_storage.149
- __unnamed_array_storage.152
- __unnamed_array_storage.155
- __unnamed_array_storage.161
- __unnamed_array_storage.164
- __unnamed_array_storage.167
- _objc_msgSend$_initWithModuleIdentifier:supportedDeviceFamilies:requiredDeviceCapabilities:associatedBundleIdentifier:associatedBundleMinimumVersion:visibilityPreference:moduleBundleURL:
CStrings:
+ "\x06\x11"
+ "@80@0:8@16@24@32@40@48@56Q64@72"
+ "CCRequiredDeviceIncapabilities"
+ "Found module metadata at URL %{public}@: %{public}@"
+ "Ignoring disallowed module at URL: %{public}@"
+ "Ignoring unsupported module at URL: %{public}@"
+ "Required Device Incapabilities"
+ "T@\"NSSet\",R,C,N,V_requiredDeviceIncapabilities"
+ "_initWithModuleIdentifier:supportedDeviceFamilies:requiredDeviceCapabilities:requiredDeviceIncapabilities:associatedBundleIdentifier:associatedBundleMinimumVersion:visibilityPreference:moduleBundleURL:"
+ "_requiredDeviceIncapabilities"
+ "_requiredIncapabilitiesForInfoDictionary:"
+ "requiredDeviceIncapabilities"
- "\x05\x11"
- "@72@0:8@16@24@32@40@48Q56@64"
- "ButtonInteractionClassic"
- "_initWithModuleIdentifier:supportedDeviceFamilies:requiredDeviceCapabilities:associatedBundleIdentifier:associatedBundleMinimumVersion:visibilityPreference:moduleBundleURL:"

```
