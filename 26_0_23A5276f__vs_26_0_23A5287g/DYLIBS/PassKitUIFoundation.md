## PassKitUIFoundation

> `/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`

```diff

-1622.6.0.0.0
-  __TEXT.__text: 0x2844c
-  __TEXT.__auth_stubs: 0xc90
+1624.7.1.0.0
+  __TEXT.__text: 0x285cc
+  __TEXT.__auth_stubs: 0xca0
   __TEXT.__objc_methlist: 0x1ec4
   __TEXT.__const: 0x668
-  __TEXT.__cstring: 0xe7a
-  __TEXT.__oslogstring: 0x128e
-  __TEXT.__gcc_except_tab: 0x7ec
-  __TEXT.__unwind_info: 0xac0
+  __TEXT.__cstring: 0xe31
+  __TEXT.__oslogstring: 0x13f3
+  __TEXT.__gcc_except_tab: 0x870
+  __TEXT.__unwind_info: 0xae0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x66f
-  __TEXT.__objc_methname: 0x708b
-  __TEXT.__objc_methtype: 0x14d3
+  __TEXT.__objc_methname: 0x7059
+  __TEXT.__objc_methtype: 0x14d7
   __TEXT.__objc_stubs: 0x5da0
   __DATA_CONST.__got: 0x568
-  __DATA_CONST.__const: 0xfb8
+  __DATA_CONST.__const: 0xf90
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_selrefs: 0x1c58
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__auth_got: 0x658
+  __AUTH_CONST.__auth_got: 0x660
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0xf80
   __AUTH_CONST.__objc_const: 0x4bd0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/GLKit.framework/GLKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI
   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalKit.framework/MetalKit

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FEA5E60-6321-3615-B583-295FF3E77525
-  Functions: 849
-  Symbols:   3625
-  CStrings:  1933
+  UUID: 374A8768-2B12-33C0-9578-593592F2E8A0
+  Functions: 847
+  Symbols:   3626
+  CStrings:  1934
 
Symbols:
+ -[PKAuthenticatorEvaluationContext _requestRemoteAuthenticatorViewControllerOfType:withHostingConfiguration:]
+ GCC_except_table10
+ GCC_except_table104
+ GCC_except_table11
+ GCC_except_table17
+ GCC_except_table177
+ GCC_except_table185
+ GCC_except_table189
+ GCC_except_table197
+ GCC_except_table2
+ GCC_except_table3
+ _NSStringFromClass
+ _OBJC_CLASS_$_LAHostingController
+ ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.489
+ ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke.269
+ ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke_2.270
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e30_v16?0"PKPeerPayment3DScene"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_73_e8_32s_e8_v12?0B8ls32l8
+ ___block_literal_global.268
+ ___block_literal_global.272
+ ___block_literal_global.326
+ ___block_literal_global.328
+ ___block_literal_global.598
+ ___block_literal_global.613
+ _objc_msgSend$_requestRemoteAuthenticatorViewControllerOfType:withHostingConfiguration:
+ _objc_msgSend$makeHostingControllerWithConfiguration:
- -[PKAuthenticatorEvaluationContext _requestRemoteAuthenticatorViewControllerOfType:withClassName:bundleIdentifier:completion:]
- GCC_except_table105
- GCC_except_table179
- GCC_except_table187
- GCC_except_table191
- GCC_except_table201
- _OBJC_CLASS_$__UIRemoteViewController
- ___126-[PKAuthenticatorEvaluationContext _requestRemoteAuthenticatorViewControllerOfType:withClassName:bundleIdentifier:completion:]_block_invoke
- ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.492
- ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke.271
- ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke_2.272
- ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke_4
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e30_v16?0"PKPeerPayment3DScene"8ls32l8
- ___block_descriptor_48_e8_32bs_e45_v24?0"_UIRemoteViewController"8"NSError"16ls32l8
- ___block_descriptor_72_e8_32s_e26_v16?0"UIViewController"8ls32l8
- ___block_descriptor_80_e8_32s_e8_v12?0B8ls32l8
- ___block_literal_global.270
- ___block_literal_global.274
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.599
- ___block_literal_global.614
- _objc_msgSend$_requestRemoteAuthenticatorViewControllerOfType:withClassName:bundleIdentifier:completion:
- _objc_msgSend$requestViewController:fromServiceWithBundleIdentifier:connectionHandler:
CStrings:
+ "@28@0:8C16@20"
+ "PKAuthenticatorEvaluationContext (%p): failed to create remote authenticator VC of type %u using LA provided configuration."
+ "PKAuthenticatorEvaluationContext (%p): no configuration data provided for remote authenticator VC of type %u."
+ "PKAuthenticatorEvaluationContext (%p): using (%{public}@:%p) as authenticator VC of type %u from LA provided configuration."
+ "PKAuthenticatorEvaluationContext (%p): using externally provided (%{public}@:%p) as authenticator VC of type %u."
+ "_requestRemoteAuthenticatorViewControllerOfType:withHostingConfiguration:"
+ "makeHostingControllerWithConfiguration:"
+ "v20@0:8C16"
+ "v28@0:8C16@20"
- "Failed to Remote Authenticator VC of Type:%ld"
- "Failed to present Remote Authenticator VC of Type:%ld withError: %@"
- "_requestRemoteAuthenticatorViewControllerOfType:withClassName:bundleIdentifier:completion:"
- "requestViewController:fromServiceWithBundleIdentifier:connectionHandler:"
- "v16@?0@\"UIViewController\"8"
- "v24@?0@\"_UIRemoteViewController\"8@\"NSError\"16"
- "v32@0:8q16@24"
- "v48@0:8q16@24@32@?40"

```
