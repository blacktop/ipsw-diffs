## SiriPlaybackControlIntents

> `/System/Library/PrivateFrameworks/SiriPlaybackControlIntents.framework/SiriPlaybackControlIntents`

```diff

-3404.26.1.0.0
-  __TEXT.__text: 0x2445e0
-  __TEXT.__auth_stubs: 0x4780
+3404.28.1.1.1
+  __TEXT.__text: 0x250164
+  __TEXT.__auth_stubs: 0x48a0
   __TEXT.__objc_methlist: 0x2748
-  __TEXT.__const: 0x18b80
-  __TEXT.__cstring: 0x7e28
-  __TEXT.__constg_swiftt: 0x6940
-  __TEXT.__swift5_typeref: 0x5c4a
-  __TEXT.__swift5_builtin: 0x500
-  __TEXT.__swift5_reflstr: 0x4ce3
-  __TEXT.__swift5_fieldmd: 0x59a0
-  __TEXT.__swift5_assocty: 0x1b40
-  __TEXT.__swift5_proto: 0x155c
-  __TEXT.__swift5_types: 0x6b0
-  __TEXT.__swift5_protos: 0xc0
-  __TEXT.__swift5_capture: 0x4358
-  __TEXT.__oslogstring: 0x1aea6
-  __TEXT.__swift_as_entry: 0xd4
-  __TEXT.__swift_as_ret: 0xe0
-  __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x7050
-  __TEXT.__eh_frame: 0x4e08
+  __TEXT.__const: 0x192f0
+  __TEXT.__cstring: 0x8018
+  __TEXT.__constg_swiftt: 0x6c5c
+  __TEXT.__swift5_typeref: 0x5e1a
+  __TEXT.__swift5_builtin: 0x514
+  __TEXT.__swift5_reflstr: 0x4f23
+  __TEXT.__swift5_fieldmd: 0x5be4
+  __TEXT.__swift5_assocty: 0x1c00
+  __TEXT.__swift5_proto: 0x15c8
+  __TEXT.__swift5_types: 0x6d0
+  __TEXT.__swift5_protos: 0xc4
+  __TEXT.__swift5_capture: 0x4400
+  __TEXT.__oslogstring: 0x1bf86
+  __TEXT.__swift_as_entry: 0xe4
+  __TEXT.__swift_as_ret: 0xf0
+  __TEXT.__swift5_mpenum: 0x20
+  __TEXT.__unwind_info: 0x72c0
+  __TEXT.__eh_frame: 0x4eb0
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methname: 0x2d45
   __TEXT.__objc_methtype: 0x1d0
-  __DATA_CONST.__got: 0xe78
+  __DATA_CONST.__got: 0xea0
   __DATA_CONST.__const: 0xb88
-  __DATA_CONST.__objc_classlist: 0x5b0
+  __DATA_CONST.__objc_classlist: 0x5c8
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xf20
   __DATA_CONST.__objc_protorefs: 0x100
-  __AUTH_CONST.__auth_got: 0x23c0
-  __AUTH_CONST.__auth_ptr: 0x1bc0
-  __AUTH_CONST.__const: 0x127c0
-  __AUTH_CONST.__objc_const: 0x11e28
-  __AUTH.__objc_data: 0x5770
-  __AUTH.__data: 0x6f48
-  __DATA.__data: 0x43f8
-  __DATA.__bss: 0x23a00
-  __DATA.__common: 0x268
+  __AUTH_CONST.__auth_got: 0x2450
+  __AUTH_CONST.__auth_ptr: 0x1c18
+  __AUTH_CONST.__const: 0x12d10
+  __AUTH_CONST.__objc_const: 0x121c0
+  __AUTH.__objc_data: 0x5810
+  __AUTH.__data: 0x73d8
+  __DATA.__data: 0x4680
+  __DATA.__bss: 0x24680
+  __DATA.__common: 0x2a8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 13818
-  Symbols:   4609
-  CStrings:  2824
+  Functions: 14103
+  Symbols:   4740
+  CStrings:  2892
 
CStrings:
+ "HomeAutomationRedirectableIntent#resolveOrRedirect error resolving devices: %s"
+ "HomeAutomationRedirectableIntent#resolveOrRedirect found other accessories, redirecting to HomeAutomation"
+ "HomeAutomationRedirectableIntent#resolveOrRedirect no matching devices found. Checking for other accessories to determine if we should redirect to HomeAutomation..."
+ "HomeAutomationRedirectableIntent#resolveOrRedirect still no devices found."
+ "HomeAutomationRedirectableIntent#resolveOrRedirect success resolving devices: %s"
+ "HomeAutomationRedirectableIntent#resolveOrRedirect unknown deviceSelectingError"
+ "HomeAutomationRedirectableIntent#shouldCheckForHomeAutomationRedirect all queries specify a deviceType, pushing PauseMediaFlow, returning false"
+ "HomeAutomationRedirectableIntent#shouldCheckForHomeAutomationRedirect intent can potentially redirect to HomeAutomation, returning true"
+ "HomeAutomationRedirectableIntent#shouldCheckForHomeAutomationRedirect queries don't contain an accessory name, returning false"
+ "HomeAutomationRedirectableIntent#shouldCheckForHomeAutomationRedirect this is an implicit request, returning false"
+ "HomeAutomationRedirectableIntent#shouldCheckForHomeAutomationRedirect we have a mediaType specified %s, returning false"
+ "Initializing PauseMediaFlow with intent"
+ "Initializing PauseMediaRoutingFlow"
+ "Initializing ResumeMediaRoutingFlow"
+ "Intent already has device with destinationDeviceId: %s, returning it"
+ "PauseMediaRoutingFlow#execute Unable to transform home automation NLV3 parse"
+ "PauseMediaRoutingFlow#execute called"
+ "PauseMediaRoutingFlow#execute input is NLv3IntentOnly, transform to HomeAutomationNLV3Intent parse"
+ "PauseMediaRoutingFlow#execute input is nil, can't redirect to HomeAutomation"
+ "PauseMediaRoutingFlow#execute mediaPlayerIntent is nil, falling back to PauseMediaFlow"
+ "PauseMediaRoutingFlow#execute not necessary to check for HomeAutomation redirect, pushing PauseMediaFlow"
+ "PauseMediaRoutingFlow#execute pushing PauseMediaFlow so we can dialog a relevant error"
+ "PauseMediaRoutingFlow#execute setting devices in intent and pushing PauseMediaFlow"
+ "PauseMediaRoutingFlow#execute transformed home automation NLV3 parse %s"
+ "PauseMediaRoutingFlow#on called"
+ "PauseMediaRoutingFlow#on received an unsupported parse type %s"
+ "PauseMediaRoutingFlow#on supported parse"
+ "PauseMediaRoutingFlow#on unable to create MediaPlayerIntent from parse"
+ "ResumeMediaRoutingFlow#execute Unable to transform home automation NLV3 parse"
+ "ResumeMediaRoutingFlow#execute called"
+ "ResumeMediaRoutingFlow#execute input is NLv3IntentOnly, transform to HomeAutomationNLV3Intent parse"
+ "ResumeMediaRoutingFlow#execute input is nil, can't redirect to HomeAutomation"
+ "ResumeMediaRoutingFlow#execute mediaPlayerIntent is nil, falling back to ResumeMediaFlow"
+ "ResumeMediaRoutingFlow#execute not necessary to check for HomeAutomation redirect, pushing PauseMediaFlow"
+ "ResumeMediaRoutingFlow#execute pushing PauseMediaFlow so we can dialog a relevant error"
+ "ResumeMediaRoutingFlow#execute setting devices in intent and pushing ResumeMediaFlow"
+ "ResumeMediaRoutingFlow#execute transformed home automation NLV3 parse %s"
+ "ResumeMediaRoutingFlow#on called"
+ "ResumeMediaRoutingFlow#on received an unsupported parse type %s"
+ "ResumeMediaRoutingFlow#on supported parse"
+ "ResumeMediaRoutingFlow#on unable to create MediaPlayerIntent from parse"
+ "Transformer#homeAutomationNLV3Transformer Devices: %s"
+ "Transformer#homeAutomationNLV3Transformer MediaPlayerNLv3Intent %s"
+ "Transformer#homeAutomationNLV3Transformer Parse doesn't contain an NLv3 intent, returning untransformed parse"
+ "Transformer#homeAutomationNLV3Transformer final homeAutomationNLIntent: %s"
+ "Transformer#homeAutomationNLV3Transformer no accessory type found in native matter devices %s"
+ "Transformer#homeAutomationNLV3Transformer no mapped HomeAutomationState for this verb %s"
+ "Transformer#homeAutomationNLV3Transformer no mapped HomeAutomationVerb for this verb %s"
+ "Transformer#homeAutomationNLV3Transformer unable to unwrap mediaPlayerIntent verb, returning parse"
+ "_TtC26SiriPlaybackControlIntents21PauseMediaRoutingFlow"
+ "_TtC26SiriPlaybackControlIntents22ResumeMediaRoutingFlow"
+ "_TtCV26SiriPlaybackControlIntents24HomeAutomationNLV3Intent7Builder"
+ "accessoryTypes"
+ "childNodes"
+ "com.apple.siri.HomeAutomationFlowDelegatePlugin"
+ "get_state"
+ "hold_state"
+ "homeAutomationAccessoryType"
+ "homeAutomationState"
+ "homeAutomationVerb"
+ "input"
+ "mediaPlayerIntent"
+ "paused"
+ "resumed"
+ "robotVacuumCleaner"
+ "set_state"
+ "stopped"

```
