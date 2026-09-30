## tipsd

> `/usr/libexec/tipsd`

```diff

-818.0.0.0.0
-  __TEXT.__text: 0x12d98
-  __TEXT.__auth_stubs: 0xbd0
+822.0.0.0.0
+  __TEXT.__text: 0x13530
+  __TEXT.__auth_stubs: 0xc50
   __TEXT.__objc_stubs: 0x2400
-  __TEXT.__objc_methlist: 0xbe8
-  __TEXT.__const: 0x24a
-  __TEXT.__cstring: 0xd79
-  __TEXT.__objc_methname: 0x314e
+  __TEXT.__objc_methlist: 0xc20
+  __TEXT.__const: 0x246
+  __TEXT.__cstring: 0xeb9
+  __TEXT.__objc_methname: 0x31ab
   __TEXT.__oslogstring: 0x108a
   __TEXT.__objc_classname: 0x1ad
-  __TEXT.__objc_methtype: 0xdae
+  __TEXT.__objc_methtype: 0xdb1
   __TEXT.__gcc_except_tab: 0x230
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x1e5

   __TEXT.__swift5_types: 0x4
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x4d8
+  __TEXT.__unwind_info: 0x4f0
   __TEXT.__eh_frame: 0x5d8
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0x9e8
+  __DATA_CONST.__auth_got: 0x638
+  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__auth_ptr: 0xe0
+  __DATA_CONST.__const: 0x9f8
   __DATA_CONST.__cfstring: 0x820
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x90
+  __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xb80
-  __DATA.__objc_selrefs: 0xc68
+  __DATA.__objc_const: 0xbf8
+  __DATA.__objc_selrefs: 0xc70
   __DATA.__objc_ivar: 0x64
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x640
+  __DATA.__data: 0x650
   __DATA.__common: 0x20
   __DATA.__bss: 0x200
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
+  - /System/Library/PrivateFrameworks/SupportFlowCore.framework/SupportFlowCore
   - /System/Library/PrivateFrameworks/TipsCore.framework/TipsCore
   - /System/Library/PrivateFrameworks/TipsDaemon.framework/TipsDaemon
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 161F58DF-6B34-3C5A-AC16-5707DDAACD2D
-  Functions: 377
-  Symbols:   364
-  CStrings:  840
+  UUID: C8456037-B207-36E2-8409-ED2AE68A8E96
+  Functions: 384
+  Symbols:   377
+  CStrings:  851
 
Symbols:
+ _$s10Foundation11JSONDecoderC6decode_4fromxxm_AA4DataVtKSeRzlFTj
+ _$s10Foundation11JSONDecoderCACycfc
+ _$s10Foundation11JSONDecoderCMa
+ _$s10Foundation4DataV36_unconditionallyBridgeFromObjectiveCyACSo6NSDataCSgFZ
+ _$s15SupportFlowCore0aB14SessionManagerO06updateD3Map7sessionyAA0abD0V_tFZ
+ _$s15SupportFlowCore0aB14SessionManagerO14logAllSessionsyyFZ
+ _$s15SupportFlowCore0aB7SessionVMa
+ _$s15SupportFlowCore0aB7SessionVSeAAMc
+ _$s8TipsCore0A3LogV9analyticsACvgZ
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ _OBJC_CLASS_$_SupportFlowSessionProcessor
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftUIKit
- _OBJC_CLASS_$_TPSFeatureFlags
- _objc_retain_x7
CStrings:
+ "TPSSupportFlowSessionAnalyticsInterface"
+ "contentFromOrigin:systemEducationRequest:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:"
+ "logForAppTerminate"
+ "logForAppTerminate - Logging final analytics before app termination"
+ "tipsd"
+ "tipsd1"
+ "updateContentFromOrigin:systemEducationRequest:indexContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:"
+ "updateSessionMap - Failed to decode session data for "
+ "updateSessionMap - Session ID: "
+ "updateSessionMap finished - Session ID: "
+ "updateSessionMapWithIdentifier:data:"
+ "v32@0:8@\"NSString\"16@\"NSData\"24"
+ "v64@0:8B16B20B24B28B32B36@40@?48@?56"
- "allowsDE"
- "contentFromOrigin:processTipKitContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:"
- "updateContentFromOrigin:indexContent:contextualEligibility:widgetEligibility:notificationEligibility:preferredNotificationIdentifiers:shouldDeferBlock:completionHandler:"
- "v60@0:8B16B20B24B28B32@36@?44@?52"

```
