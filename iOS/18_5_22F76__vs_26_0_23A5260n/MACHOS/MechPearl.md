## MechPearl

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismPlugins/MechPearl.bundle/MechPearl`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0x68ec
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x13e0
-  __TEXT.__objc_methlist: 0x58c
+2005.0.13.0.0
+  __TEXT.__text: 0x68b0
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x1440
+  __TEXT.__objc_methlist: 0x5dc
   __TEXT.__const: 0xe0
-  __TEXT.__objc_methname: 0x162f
-  __TEXT.__oslogstring: 0x727
-  __TEXT.__cstring: 0x324
-  __TEXT.__objc_classname: 0xb0
-  __TEXT.__objc_methtype: 0x574
+  __TEXT.__objc_methname: 0x1704
+  __TEXT.__oslogstring: 0x6eb
+  __TEXT.__cstring: 0x377
+  __TEXT.__objc_classname: 0xea
+  __TEXT.__objc_methtype: 0x605
   __TEXT.__gcc_except_tab: 0x164
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x1c8
-  __DATA_CONST.__got: 0xc8
+  __TEXT.__unwind_info: 0x268
+  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__const: 0x450
-  __DATA_CONST.__cfstring: 0x300
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_intobj: 0x288
-  __DATA.__objc_const: 0x810
-  __DATA.__objc_selrefs: 0x6c0
+  __DATA_CONST.__objc_intobj: 0x270
+  __DATA.__objc_const: 0x890
+  __DATA.__objc_selrefs: 0x700
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x240
+  __DATA.__data: 0x300
   __DATA.__bss: 0x14
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/LocalAuthentication.framework/Support/MechanismBase.framework/MechanismBase
   - /System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
-  - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9EBFBA3-0D69-3D67-9E31-9B7DFA0979FA
-  Functions: 129
-  Symbols:   91
-  CStrings:  448
+  UUID: 08621D39-0DEF-315C-BFC8-4044CFB0AB8F
+  Functions: 128
+  Symbols:   96
+  CStrings:  464
 
Symbols:
+ _LACErrorCodeBiometryNotAvailable
+ _LACPolicyOptionConcurrentBiometryAndCompanion
+ _LACPurposeSecureUIRecording
+ _NSStringFromProtocol
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACTCCManager
- _kTCCServiceFaceID
CStrings:
+ "@\"<LACEvaluationRequestProcessor>\"16@0:8"
+ "Companion authentication is active and concurrent run with biometry is not allowed"
+ "LACCompanionAuthenticationService"
+ "LACDomainStateProviding"
+ "TB,R,N"
+ "cancelAllRequests"
+ "cancelRequestsForContextID:"
+ "domainStateForRequest:completion:"
+ "errorWithCode:debugDescription:"
+ "faceIDServiceName"
+ "failuresInfoDictionaryWithError:unboundMatch:"
+ "isActive"
+ "isCompanionDeviceAvailable"
+ "processor"
+ "serviceLocator"
+ "serviceWithIdentifier:"
+ "startServices"
+ "v24@0:8@\"NSUUID\"16"
+ "v32@0:8@\"<LACDomainStateRequest>\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@16@?24"
- "%{public}@ ignoring failure limit: %d for policy %{public}@"
- "_shouldRespectFailureLimit"
- "isEnabled"
- "isRunningDTOPolicy"
- "isSupported"

```
