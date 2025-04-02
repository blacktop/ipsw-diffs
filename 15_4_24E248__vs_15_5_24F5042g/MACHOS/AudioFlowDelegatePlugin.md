## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/Contents/MacOS/AudioFlowDelegatePlugin`

```diff

-3404.75.2.14.1
-  __TEXT.__text: 0x22ac9c
-  __TEXT.__auth_stubs: 0x6460
+3405.17.1.0.0
+  __TEXT.__text: 0x230c18
+  __TEXT.__auth_stubs: 0x6500
   __TEXT.__objc_methlist: 0x6e8
   __TEXT.__const: 0x8152
-  __TEXT.__cstring: 0x71bc
-  __TEXT.__swift5_typeref: 0x3a7c
-  __TEXT.__oslogstring: 0x1d6c7
-  __TEXT.__constg_swiftt: 0x52a0
+  __TEXT.__cstring: 0x727c
+  __TEXT.__swift5_typeref: 0x3b18
+  __TEXT.__oslogstring: 0x1da27
+  __TEXT.__constg_swiftt: 0x52d0
   __TEXT.__swift5_builtin: 0x140
-  __TEXT.__swift5_reflstr: 0x3b3b
+  __TEXT.__swift5_reflstr: 0x3b8b
   __TEXT.__swift5_assocty: 0xa00
   __TEXT.__swift5_proto: 0x458
   __TEXT.__swift5_types: 0x308
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x258c
+  __TEXT.__objc_methname: 0x260a
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x2e04
-  __TEXT.__swift5_capture: 0x2cdc
-  __TEXT.__swift_as_entry: 0x17c
-  __TEXT.__swift_as_ret: 0x1f4
+  __TEXT.__swift5_fieldmd: 0x2e1c
+  __TEXT.__swift5_capture: 0x2d9c
+  __TEXT.__swift_as_entry: 0x180
+  __TEXT.__swift_as_ret: 0x1f8
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x2f50
-  __TEXT.__eh_frame: 0x2bf8
-  __DATA_CONST.__auth_got: 0x3230
-  __DATA_CONST.__got: 0x1b28
-  __DATA_CONST.__auth_ptr: 0x1df0
-  __DATA_CONST.__const: 0x9158
+  __TEXT.__unwind_info: 0x2f98
+  __TEXT.__eh_frame: 0x2be8
+  __DATA_CONST.__auth_got: 0x3280
+  __DATA_CONST.__got: 0x1b58
+  __DATA_CONST.__auth_ptr: 0x1e20
+  __DATA_CONST.__const: 0x9298
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0x92a0
-  __DATA.__objc_selrefs: 0xba8
+  __DATA.__objc_const: 0x92e0
+  __DATA.__objc_selrefs: 0xbc8
   __DATA.__objc_data: 0x12a8
-  __DATA.__data: 0xb3f0
+  __DATA.__data: 0xb478
   __DATA.__bss: 0x7910
   __DATA.__common: 0x468
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /System/Library/PrivateFrameworks/PegasusAPI.framework/Versions/A/PegasusAPI
   - /System/Library/PrivateFrameworks/SAObjects.framework/Versions/A/SAObjects
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation
+  - /System/Library/PrivateFrameworks/SharedWebCredentials.framework/Versions/A/SharedWebCredentials
   - /System/Library/PrivateFrameworks/SiriAppResolution.framework/Versions/A/SiriAppResolution
   - /System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/Versions/A/SiriAudioIntentUtils
   - /System/Library/PrivateFrameworks/SiriAudioInternal.framework/Versions/A/SiriAudioInternal

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4596
-  Symbols:   315
-  CStrings:  2621
+  Functions: 4628
+  Symbols:   318
+  CStrings:  2644
 
Symbols:
+ _OBJC_CLASS_$_SAAppsLaunchApp
+ _OBJC_CLASS_$__SWCServiceDetails
+ _OBJC_CLASS_$__SWCServiceSpecifier
+ __SWCServiceTypeAppLinks
- _OBJC_CLASS_$_CATResult
CStrings:
+ "App to open the link doesn't match requested app"
+ "CommonAppResolver.resolveSelectedApp.appNotSupported"
+ "CommonIntentAppResolver#resolveSelectedApp app IS installed but doesn't support any Sirikit audio intents: %{public}s"
+ "INPlayMediaIntent#toServerConversionParse nlIntent:%s"
+ "INPlayMediaIntent#toServerConversionParse sirikitIntent:%@"
+ "IntentResponseCode"
+ "ShimFlow#execute Link bundle identifier %@ does not match requested app bundle identifier %s"
+ "ShimFlow#execute Link bundle identifier %@, requested bundle identifier %s"
+ "ShimFlow#execute ServiceDetails %s"
+ "ShimFlow#execute Universal link could not be resolved %@"
+ "ShimFlow#execute invalid link, no host: %s"
+ "ShimUtilities AudioResult %s"
+ "ShimUtilities AudioResult deserialization error: %@"
+ "ShimUtilities AudioResult uncast %s"
+ "ShimUtilities#getAppBundleId Not ifClientAction parse"
+ "ShimUtilities#getAppBundleId app parameter: %s"
+ "ShimUtilities#getAppBundleId app shimParameter not found"
+ "ShimUtilities#getAppBundleId app value: %s"
+ "ShimUtilities#getAppBundleId app: %s"
+ "ShimUtilities#getAppBundleId shim parameter: %s"
+ "ShimUtilities#getAppBundleId unable to extract appValue"
+ "ShimUtilities#getAppBundleId unable to extract appValue typed entity"
+ "UnsupportedValueStrategy#makeUnsupportedValueOutput punching out to Podcasts app for GDPR"
+ "addFlowWithAppResolution"
+ "bundleIdentifier"
+ "initWithServiceType:applicationIdentifier:domain:"
+ "serviceDetailsWithServiceSpecifier:error:"
+ "serviceSpecifier"
- "CommonIntentAppResolver#resolveApp persisting resolution result with bundleID: %s and resolutionResultType: %s in intent: %@"
- "SiriAudioOutputProvider#emptyOutput creating errorOutput %{public}s"
- "SiriAudioOutputProvider#emptyOutput returning errorOutput using RF 2.0 %{public}s"
- "SiriAudioOutputProvider#emptyOutput with responseMode = %s"
- "SiriAudioOutputProvider#emptyOutput... %{public}s"

```
