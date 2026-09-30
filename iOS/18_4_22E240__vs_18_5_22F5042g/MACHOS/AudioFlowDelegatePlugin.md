## AudioFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/AudioFlowDelegatePlugin.bundle/AudioFlowDelegatePlugin`

```diff

-3404.75.2.11.1
-  __TEXT.__text: 0x270138
-  __TEXT.__auth_stubs: 0x6de0
+3405.17.1.0.0
+  __TEXT.__text: 0x276064
+  __TEXT.__auth_stubs: 0x6e60
   __TEXT.__objc_methlist: 0x6e8
   __TEXT.__const: 0x8732
-  __TEXT.__cstring: 0x78cc
-  __TEXT.__swift5_typeref: 0x4114
-  __TEXT.__oslogstring: 0x23fe7
-  __TEXT.__constg_swiftt: 0x5580
+  __TEXT.__cstring: 0x79ac
+  __TEXT.__swift5_typeref: 0x41b0
+  __TEXT.__oslogstring: 0x24347
+  __TEXT.__constg_swiftt: 0x55b0
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x3e9b
+  __TEXT.__swift5_reflstr: 0x3eeb
   __TEXT.__swift5_assocty: 0xa40
   __TEXT.__swift5_proto: 0x464
   __TEXT.__swift5_types: 0x31c
   __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x297e
+  __TEXT.__objc_methname: 0x29fc
   __TEXT.__objc_methtype: 0x3ef
-  __TEXT.__swift5_fieldmd: 0x2fbc
-  __TEXT.__swift5_capture: 0x3844
-  __TEXT.__swift_as_entry: 0x194
-  __TEXT.__swift_as_ret: 0x208
+  __TEXT.__swift5_fieldmd: 0x2fd4
+  __TEXT.__swift5_capture: 0x3904
+  __TEXT.__swift_as_entry: 0x198
+  __TEXT.__swift_as_ret: 0x20c
   __TEXT.__swift5_protos: 0x58
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x33c8
-  __TEXT.__eh_frame: 0x32e0
-  __DATA_CONST.__auth_got: 0x36f0
-  __DATA_CONST.__got: 0x1dd8
-  __DATA_CONST.__auth_ptr: 0x1f20
-  __DATA_CONST.__const: 0xa7e0
+  __TEXT.__unwind_info: 0x3438
+  __TEXT.__eh_frame: 0x32d0
+  __DATA_CONST.__auth_got: 0x3730
+  __DATA_CONST.__got: 0x1e00
+  __DATA_CONST.__auth_ptr: 0x2140
+  __DATA_CONST.__const: 0xa920
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA.__objc_const: 0xa468
-  __DATA.__objc_selrefs: 0xdb8
+  __DATA.__objc_const: 0xa4a8
+  __DATA.__objc_selrefs: 0xdd8
   __DATA.__objc_data: 0x12a8
-  __DATA.__data: 0xbbe0
+  __DATA.__data: 0xbc70
   __DATA.__bss: 0x7a10
   __DATA.__common: 0x470
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
+  - /System/Library/PrivateFrameworks/SharedWebCredentials.framework/SharedWebCredentials
   - /System/Library/PrivateFrameworks/SiriAppResolution.framework/SiriAppResolution
   - /System/Library/PrivateFrameworks/SiriAudioIntentUtils.framework/SiriAudioIntentUtils
   - /System/Library/PrivateFrameworks/SiriAudioInternal.framework/SiriAudioInternal

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5043
-  Symbols:   385
-  CStrings:  2993
+  Functions: 5076
+  Symbols:   387
+  CStrings:  3017
 
Symbols:
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
+ "experience rankedResults "
+ "initWithServiceType:applicationIdentifier:domain:"
+ "serviceDetailsWithServiceSpecifier:error:"
+ "serviceSpecifier"
- "CommonIntentAppResolver#resolveApp persisting resolution result with bundleID: %s and resolutionResultType: %s in intent: %@"
- "SiriAudioOutputProvider#emptyOutput creating errorOutput %{public}s"
- "SiriAudioOutputProvider#emptyOutput returning errorOutput using RF 2.0 %{public}s"
- "SiriAudioOutputProvider#emptyOutput with responseMode = %s"
- "SiriAudioOutputProvider#emptyOutput... %{public}s"

```
