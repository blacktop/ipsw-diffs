## profiled

> `/usr/libexec/profiled`

```diff

-2253.0.0.0.0
-  __TEXT.__text: 0x98d90
+2261.0.0.0.0
+  __TEXT.__text: 0x99290
   __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_stubs: 0xf3a0
-  __TEXT.__objc_methlist: 0x4b98
+  __TEXT.__objc_stubs: 0xf440
+  __TEXT.__objc_methlist: 0x4bb8
   __TEXT.__gcc_except_tab: 0x126c
-  __TEXT.__oslogstring: 0xc01d
-  __TEXT.__cstring: 0x89b3
+  __TEXT.__oslogstring: 0xc0bb
+  __TEXT.__cstring: 0x89e0
   __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x12e26
+  __TEXT.__objc_methname: 0x12eae
   __TEXT.__objc_classname: 0xb36
   __TEXT.__objc_methtype: 0x1ffc
-  __TEXT.__unwind_info: 0x15c4
+  __TEXT.__unwind_info: 0x15cc
   __DATA_CONST.__auth_got: 0x1058
-  __DATA_CONST.__got: 0x1580
+  __DATA_CONST.__got: 0x1588
   __DATA_CONST.__const: 0x1af0
-  __DATA_CONST.__cfstring: 0x8340
+  __DATA_CONST.__cfstring: 0x8360
   __DATA_CONST.__objc_classlist: 0x2c8
   __DATA_CONST.__objc_catlist: 0x1e8
   __DATA_CONST.__objc_protolist: 0x68

   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x70f0
-  __DATA.__objc_selrefs: 0x4178
+  __DATA.__objc_selrefs: 0x4198
   __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x7f8
+  __DATA.__objc_classrefs: 0x800
   __DATA.__objc_superrefs: 0x140
   __DATA.__objc_ivar: 0x1c0
   __DATA.__objc_data: 0x1bd0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HomeKit.framework/HomeKit
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F5037A0D-85A7-3507-B5C1-BB5012D8AAF8
-  Functions: 1900
-  Symbols:   1424
-  CStrings:  5823
+  UUID: 600AE817-46BA-3118-A63B-056822D80280
+  Functions: 1902
+  Symbols:   1426
+  CStrings:  5831
 
Symbols:
+ _MCErrorRestrictionCauseStolenDeviceProtection
+ _OBJC_CLASS_$_LARatchetManager
CStrings:
+ "Fixing UserEnrollment in profile stub and MDM.plist"
+ "OTA_SERVER_RETURNED_FORBIDDEN_PROFILE_IN_SDP"
+ "Profile '%{public}@' disallowed for queueing during SDP because it contains a payload of type: %{public}@"
+ "_checkValidUserEnrollment"
+ "isFeatureEnabled"
+ "isInteractiveProfileInstallationAllowedBySDP:"
+ "unavailablePayloadsWithStolenDeviceProtection"

```
