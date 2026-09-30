## PromotedContentUI

> `/System/Library/PrivateFrameworks/PromotedContentUI.framework/PromotedContentUI`

```diff

-556.5.18.0.0
-  __TEXT.__text: 0x175e60
-  __TEXT.__auth_stubs: 0x6330
-  __TEXT.__objc_methlist: 0x2064
-  __TEXT.__const: 0xdbc4
-  __TEXT.__constg_swiftt: 0x74b8
-  __TEXT.__swift5_typeref: 0x638e
+556.5.25.1.0
+  __TEXT.__text: 0x181400
+  __TEXT.__auth_stubs: 0x63d0
+  __TEXT.__objc_methlist: 0x20fc
+  __TEXT.__const: 0xde74
+  __TEXT.__constg_swiftt: 0x7494
+  __TEXT.__swift5_typeref: 0x666e
   __TEXT.__swift5_builtin: 0x21c
-  __TEXT.__swift5_reflstr: 0x5988
-  __TEXT.__swift5_fieldmd: 0x517c
-  __TEXT.__swift5_assocty: 0x938
-  __TEXT.__cstring: 0x8506
+  __TEXT.__swift5_reflstr: 0x5ad8
+  __TEXT.__swift5_fieldmd: 0x5234
+  __TEXT.__swift5_assocty: 0x970
+  __TEXT.__cstring: 0x8544
   __TEXT.__swift5_proto: 0x7c0
-  __TEXT.__swift5_types: 0x4f4
-  __TEXT.__oslogstring: 0x52fe
-  __TEXT.__swift5_protos: 0xfc
-  __TEXT.__swift5_capture: 0x13c0
+  __TEXT.__swift5_types: 0x4fc
+  __TEXT.__oslogstring: 0x53d4
+  __TEXT.__swift5_protos: 0xf8
+  __TEXT.__swift5_capture: 0x168c
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__swift_as_entry: 0x1a8
-  __TEXT.__swift_as_ret: 0x174
-  __TEXT.__unwind_info: 0x4648
-  __TEXT.__eh_frame: 0x5c14
-  __TEXT.__objc_classname: 0x1e51
-  __TEXT.__objc_methname: 0x8fad
-  __TEXT.__objc_methtype: 0x23f3
-  __TEXT.__objc_stubs: 0x51c0
-  __DATA_CONST.__got: 0x15a8
+  __TEXT.__swift_as_entry: 0x1bc
+  __TEXT.__swift_as_ret: 0x17c
+  __TEXT.__unwind_info: 0x4808
+  __TEXT.__eh_frame: 0x5f94
+  __TEXT.__objc_classname: 0x1e71
+  __TEXT.__objc_methname: 0x934d
+  __TEXT.__objc_methtype: 0x2429
+  __TEXT.__objc_stubs: 0x5400
+  __DATA_CONST.__got: 0x15e0
   __DATA_CONST.__const: 0x410
-  __DATA_CONST.__objc_classlist: 0x3b0
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cd0
+  __DATA_CONST.__objc_selrefs: 0x1d58
   __DATA_CONST.__objc_protorefs: 0x108
-  __AUTH_CONST.__auth_got: 0x31a0
-  __AUTH_CONST.__const: 0x9b98
-  __AUTH_CONST.__objc_const: 0x9dc0
-  __AUTH.__objc_data: 0x3208
-  __AUTH.__data: 0x2fc8
-  __DATA.__data: 0x4110
-  __DATA.__bss: 0xb110
-  __DATA.__common: 0x220
+  __AUTH_CONST.__auth_got: 0x31f0
+  __AUTH_CONST.__const: 0xa518
+  __AUTH_CONST.__objc_const: 0x9fd0
+  __AUTH.__objc_data: 0x32f8
+  __AUTH.__data: 0x3070
+  __DATA.__data: 0x41e0
+  __DATA.__bss: 0xb200
+  __DATA.__common: 0x240
   __DATA_DIRTY.__objc_data: 0x3868
   __DATA_DIRTY.__data: 0x3778
   __DATA_DIRTY.__bss: 0x2080

   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/EventKitUI.framework/EventKitUI
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/StoreKit.framework/StoreKit

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/WebKit.framework/WebKit
   - /System/Library/Frameworks/_AdAttributionKit_StoreKit.framework/_AdAttributionKit_StoreKit
-  - /System/Library/Frameworks/_WebKit_SwiftUI.framework/_WebKit_SwiftUI
   - /System/Library/PrivateFrameworks/APConfigurationSystem.framework/APConfigurationSystem
   - /System/Library/PrivateFrameworks/APFoundation.framework/APFoundation
   - /System/Library/PrivateFrameworks/AdCore.framework/AdCore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 26E501E9-2CBF-3286-AD92-890EFCD9AAC6
-  Functions: 5998
-  Symbols:   474
-  CStrings:  2741
+  UUID: 1AF633FE-B39D-3D29-A7C2-50FEE79667C5
+  Functions: 6241
+  Symbols:   479
+  CStrings:  2776
 
Symbols:
+ _OBJC_CLASS_$_WKWebViewConfiguration
+ _UIAccessibilityTraitStaticText
+ _UIFontWeightSemibold
+ _UISceneWillDeactivateNotification
+ _swift_task_deinitOnExecutor
CStrings:
+ "$__lazy_storage_$_stackView"
+ "' }\n    };\n\n    document.addEventListener('click', function(event) {\n        var target = event.target;\n        while (target && target.tagName !== 'A') {\n            target = target.parentElement;\n        }\n        if (target && target.href) {\n            console.log('[TransparencyWebView] Link tapped: ' + target.href);\n            window.webkit.messageHandlers.nativeBridge.postMessage({\n                type: 'linkTapped',\n                url: target.href\n            });\n            event.preventDefault();\n            event.stopPropagation();\n        }\n    }, true);"
+ "Ad Card Image"
+ "Did receive didFinishPlayback already. Not sending additional metrics."
+ "Failed to retrieve play fill image for playback control."
+ "Failed to retrieve play slash fill image for playback control."
+ "PromotedContentUI.WeakScriptMessageHandler"
+ "PromotedContentUI/TransparencyNavigationHandler.swift"
+ "PromotedContentUI/ViewControllerResolver.swift"
+ "Unlock puzzles is feature flag disabled."
+ "[AdTransparencySheet]  ViewControllerResolver captured: %s"
+ "[AdTransparencySheet] App entered background, dismissing sheet."
+ "[TransparencyWebView]  Cleaned up WKWebView on disappear"
+ "[TransparencyWebView]  External link: %s"
+ "[TransparencyWebView]  Falling back to Settings deep link"
+ "[TransparencyWebView]  Invalid JS message format"
+ "[TransparencyWebView]  JS message received: %s"
+ "[TransparencyWebView]  Link tapped from JS: %s"
+ "[TransparencyWebView]  Load timeout (%lds) — showing fallback"
+ "[TransparencyWebView]  Location link matched"
+ "[TransparencyWebView]  Network available — proceeding to load"
+ "[TransparencyWebView]  Network lost detected via poll (elapsed: %lds) — showing fallback"
+ "[TransparencyWebView]  Network offline at sheet open — showing fallback, skipping WKWebView entirely"
+ "[TransparencyWebView]  OBPrivacyPresenter failed to initialize"
+ "[TransparencyWebView]  OBPrivacyPresenter.present() called"
+ "[TransparencyWebView]  Privacy & Advertising link matched"
+ "[TransparencyWebView]  Still loading... (%lds elapsed, network: %s)"
+ "[TransparencyWebView]  Unhandled link type: %s"
+ "[TransparencyWebView]  Web content process terminated"
+ "[TransparencyWebView]  didFail (code: %ld): %s"
+ "[TransparencyWebView]  didFailProvisionalNavigation (code: %ld): %s"
+ "[TransparencyWebView]  didFinish navigation"
+ "[TransparencyWebView]  fallbackView appeared — error state confirmed visible"
+ "[TransparencyWebView]  hasError changed to: %{bool}d"
+ "[TransparencyWebView]  hasError set to true on thread: %s"
+ "[TransparencyWebView] Loading request: %s"
+ "[TransparencyWebView] didStartProvisionalNavigation"
+ "[TransparencyWebView] openPrivacyAdvertisingSettings - presentingVC: %s"
+ "[TransparencyWebView] setupWebView - rendererURL: %s"
+ "[TransparencyWebView] wireHandler complete"
+ "_TtC17PromotedContentUI24WeakScriptMessageHandler"
+ "_TtC17PromotedContentUI29TransparencyNavigationHandler"
+ "_TtCV17PromotedContentUI22ViewControllerResolver22ResolverViewController"
+ "_hasError"
+ "_isLoading"
+ "_isWebViewLoaded"
+ "animateWithDuration:delay:options:animations:completion:"
+ "appLifecycleObserverTask"
+ "blurMaskLayer"
+ "buttonFontSize"
+ "colorWithAlphaComponent:"
+ "com.apple.promotedcontentui.networkcheck"
+ "contentLayoutGuide"
+ "controlHidingDelay"
+ "defaultWebpagePreferences"
+ "didSelectAdMarker:"
+ "didSelectCallToAction:"
+ "didSetupQuartileObservers"
+ "fetchImageTask"
+ "frameLayoutGuide"
+ "hideControlsTask"
+ "hidingAnimationDuration"
+ "imageViewHeightConstraint"
+ "imageWithConfiguration:"
+ "labelColor"
+ "onDismiss"
+ "preferredFontForTextStyle:compatibleWithTraitCollection:"
+ "removeScriptMessageHandlerForName:"
+ "setAllowsContentJavaScript:"
+ "setCanCancelContentTouches:"
+ "setMask:"
+ "setUserContentController:"
+ "stopLoading"
+ "systemImageNamed:"
+ "textAndLockupContainer"
+ "traitCollectionWithPreferredContentSizeCategory:"
+ "userContentController"
+ "videoPlaybackCompleted"
+ "videoPlayerAccessoryBaseBackgroundColor"
+ "wasPausedByUser"
- "' }\n    };\n\n    // Intercept all anchor taps and forward to native\n    document.addEventListener('click', function(event) {\n        var target = event.target;\n        // Walk up DOM to find anchor tag\n        while (target && target.tagName !== 'A') {\n            target = target.parentElement;\n        }\n        if (target && target.href) {\n            console.log('[TransparencyWebView] Link tapped: ' + target.href);\n            window.webkit.messageHandlers.nativeBridge.postMessage({\n                type: 'linkTapped',\n                url: target.href\n            });\n            event.preventDefault();\n            event.stopPropagation();\n        }\n    }, true);"
- "Failed to get prefetch store for context %s."
- "PromotedContentUI.AdCardFooterGradientLayer"
- "PromotedContentUI/AdTransparencySheet.swift"
- "[AdTransparencySheet] App moved to background, dismissing sheet."
- "[AdTransparencySheet] openPrivacyAdvertisingSettings - presentingVC: %s"
- "[AdTransparencySheet] ↩️ Falling back to Settings deep link"
- "[AdTransparencySheet] ⚠️ Unhandled link type: %s"
- "[AdTransparencySheet] ⚠️ Unknown link type in decidePolicy, allowing: %s"
- "[AdTransparencySheet] ⚡️ decidePolicy - type: %ld, url: %s"
- "[AdTransparencySheet] ✅ Location link matched"
- "[AdTransparencySheet] ✅ Location matched in decidePolicy"
- "[AdTransparencySheet] ✅ OBPrivacyPresenter.present() called"
- "[AdTransparencySheet] ✅ Privacy & Advertising link matched"
- "[AdTransparencySheet] ✅ Privacy & Advertising matched in decidePolicy"
- "[AdTransparencySheet] ✅ ViewControllerResolver captured: %s"
- "[AdTransparencySheet] ❌ Invalid JS message format"
- "[AdTransparencySheet] ❌ OBPrivacyPresenter failed to initialize for identifier: com.apple.onboarding.advertising"
- "[AdTransparencySheet] 🌐 External link matched in decidePolicy: %s"
- "[AdTransparencySheet] 🌐 External link: %s"
- "[AdTransparencySheet] 📨 JS message received: %s"
- "[AdTransparencySheet] 🔗 Link tapped from JS: %s"
- "[TransparencyWebView] Navigation event: %s"
- "[TransparencyWebView] setupWebPage - presentingViewController: %s"
- "[TransparencyWebView] ✅ Navigation completed successfully."
- "[TransparencyWebView] ❌ Navigation failed with unexpected error: %s"
- "[TransparencyWebView] ❌ Navigation failed with unknown NavigationError"
- "[TransparencyWebView] ❌ Navigation failed: invalid URL"
- "[TransparencyWebView] ❌ Navigation failed: page was closed"
- "[TransparencyWebView] ❌ Navigation failed: web content process terminated"
- "[TransparencyWebView] ❌ Provisional navigation failed (code: %ld): %s"
- "_TtC17PromotedContentUIP33_CAE73D18DC0AE71FA8555FD4663C094517NavigationHandler"
- "_TtCV17PromotedContentUIP33_CAE73D18DC0AE71FA8555FD4663C094522ViewControllerResolver22ResolverViewController"
- "backgroundImageViewTopConstraint"
- "blurImageViewTopConstraint"
- "didTapCallToAction"
- "fontDescriptor"
- "gradientLayer"
- "init(layer:)"
- "insertSublayer:below:"
- "objectWillChange"
- "skrimViewBottomConstraint"
- "tapActionHandler"
- "tertiarySystemFillColor"
- "vendedCache"

```
