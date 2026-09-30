## LocalAuthenticationPrivateUI

> `/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`

```diff

-1656.40.25.0.0
-  __TEXT.__text: 0x2f0c4
-  __TEXT.__auth_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x13e0
-  __TEXT.__const: 0x920
-  __TEXT.__gcc_except_tab: 0x32ac
-  __TEXT.__cstring: 0xd6e
-  __TEXT.__oslogstring: 0x4ff
+1656.60.119.0.1
+  __TEXT.__text: 0x3154c
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x1578
+  __TEXT.__const: 0x988
+  __TEXT.__gcc_except_tab: 0x3368
+  __TEXT.__cstring: 0xf0a
+  __TEXT.__oslogstring: 0x809
   __TEXT.__dlopen_cstrs: 0x73
-  __TEXT.__unwind_info: 0x13c0
-  __TEXT.__objc_classname: 0x376
-  __TEXT.__objc_methname: 0x4487
-  __TEXT.__objc_methtype: 0x19c0
-  __TEXT.__objc_stubs: 0x41c0
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x518
-  __DATA_CONST.__objc_classlist: 0xb8
+  __TEXT.__unwind_info: 0x1458
+  __TEXT.__objc_classname: 0x38e
+  __TEXT.__objc_methname: 0x4934
+  __TEXT.__objc_methtype: 0x1a22
+  __TEXT.__objc_stubs: 0x46e0
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__const: 0x578
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13a8
+  __DATA_CONST.__objc_selrefs: 0x1510
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH_CONST.__const: 0x778
-  __AUTH_CONST.__cfstring: 0x880
-  __AUTH_CONST.__objc_const: 0x3f48
-  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__const: 0x7d8
+  __AUTH_CONST.__cfstring: 0xbe0
+  __AUTH_CONST.__objc_const: 0x4188
+  __AUTH_CONST.__objc_intobj: 0x348
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x150
-  __DATA.__objc_ivar: 0x31c
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x344
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libAccessibility.dylib

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 943
-  Symbols:   1275
-  CStrings:  1279
+  Functions: 1000
+  Symbols:   1341
+  CStrings:  1391
 
Symbols:
+ _LACLogFaceIDUI
+ _LAUIIsSecureFaceIDAvailable
+ _LAUIIsSecureFaceIDAvailableAndEnabled
+ _LAUIIsSecureFaceIDUIEnabled
+ _LAUIIsSecureFaceIDUISupported
+ _NSStringFromLAUISecureFaceIDViewState
+ _NSStringFromLAUISecureFaceIDViewType
+ _OBJC_CLASS_$_CADisplayLink
+ _OBJC_CLASS_$_CASecureFlipBookLayer
+ _OBJC_CLASS_$_LACFlags
+ _OBJC_CLASS_$_LACSecureFaceIDUIUtilities
+ _OBJC_CLASS_$_LACUIDevice
+ _OBJC_CLASS_$_LAUISecureFaceIDView
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_METACLASS_$_LAUISecureFaceIDView
CStrings:
+ "\x011\x13\x81\xf0\xb11"
+ " State"
+ "%!@(MISSING) (via %!@(MISSING))"
+ "%!@(MISSING) -> %!@(MISSING)"
+ "%!@(MISSING)(%!d(MISSING))"
+ "%!@(MISSING)-%!d(MISSING)x"
+ "%!{(MISSING)public}@ can't transition from '%!@(MISSING)' to '%!@(MISSING)', must transition to '%!@(MISSING)' first"
+ "%!{(MISSING)public}@ can't transition to _desiredState: %!d(MISSING)"
+ "%!{(MISSING)public}@ can't transition to _nextStateOnPathToDesiredState: %!d(MISSING)"
+ "%!{(MISSING)public}@ couldn't transition from '%!@(MISSING)' to '%!@(MISSING)'"
+ "%!{(MISSING)public}@ does not want to transition from '%!@(MISSING)' to '%!@(MISSING)' directly, will transition to '%!@(MISSING)' first"
+ "%!{(MISSING)public}@ now can transition to %!{(MISSING)public}@"
+ "%!{(MISSING)public}@ successfully transitioned from %!@(MISSING) to %!@(MISSING)"
+ "%!{(MISSING)public}@ tick:%!f(MISSING)"
+ "<%!@(MISSING) %!p(MISSING); flipBookState: '%!@(MISSING)', state: '%!@(MISSING)'>"
+ "@\"CASecureFlipBookLayer\""
+ "@\"LAUISecureFaceIDView\""
+ "@\"NSDate\""
+ "@\"NSString\"8@?0"
+ "Acquiring State"
+ "B24@0:8q16"
+ "Could not create secure glyph, secure variant disabled."
+ "Could not create secure glyph."
+ "Created %!@(MISSING), currentState: %!@(MISSING)"
+ "Default"
+ "Empty State"
+ "FaceID"
+ "FaceID-40"
+ "FaceID-69"
+ "FaceID-70"
+ "Failed to create CASecureFlipBookLayer"
+ "Finished State"
+ "Found flipbook for %!d(MISSING)x scale: %!@(MISSING)"
+ "Found flipbook: %!@(MISSING)"
+ "Idle State"
+ "Invalid LAUISecureFaceIDViewState: %!d(MISSING)"
+ "Invalid LAUISecureFaceIDViewType: %!d(MISSING)"
+ "LAUISecureFaceIDView"
+ "Matched State"
+ "Processing State"
+ "Small"
+ "States: %!@(MISSING)"
+ "T@\"CASecureFlipBookLayer\",R,N,V_secureFlipBookLayer"
+ "T@\"NSNumber\",R,N"
+ "TB,N,V_secureVariantEnabled"
+ "Tq,N"
+ "Tq,N,V_secureVariantType"
+ "Using engineering flipbook: %!@(MISSING)"
+ "Verifying State"
+ "_caStateNameForState:"
+ "_canTransitionViewToState:"
+ "_descriptionOfState:"
+ "_desiredState"
+ "_disableDisplayLink"
+ "_displayLink"
+ "_enableDisplayLink"
+ "_flipbookFromLAUISecureFaceIDViewType:"
+ "_nextStateForUnwantedTransitionFrom:to:"
+ "_nextStateOnPathToDesiredState"
+ "_nextStateOnShortestPathFrom:to:"
+ "_secureFaceIdView"
+ "_secureFlipBookLayer"
+ "_secureVariantEnabled"
+ "_secureVariantType"
+ "_shortNameForState:"
+ "_tick"
+ "_tickWithInterval:frequency:"
+ "_timeAppeared"
+ "_transitionDict"
+ "_transitionDictForFullFlow"
+ "_transitionDictForProtectedAppsFlow"
+ "_transitionViewToState:"
+ "_type"
+ "activateConstraints:"
+ "canTransitionToState:"
+ "centerXAnchor"
+ "checkmark State"
+ "constraintEqualToConstant:"
+ "currentState"
+ "empty State"
+ "face State"
+ "faceid State"
+ "faceid-36-%!d(MISSING)x"
+ "faceid-spinner-111"
+ "heightAnchor"
+ "initWithType:"
+ "isDynamicIslandAvailable"
+ "isEnabled"
+ "isSupported"
+ "now"
+ "numberWithInteger:"
+ "objectForKey:"
+ "q32@0:8q16q24"
+ "remainingMinDisplayTimeInterval"
+ "secureFlipBookLayer"
+ "secureFlipBookWithType:"
+ "secureVariantEnabled"
+ "secureVariantType"
+ "setSecureVariantEnabled:"
+ "setSecureVariantType:"
+ "sharedInstance"
+ "states"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "sublayers"
+ "tick:"
+ "timestamp"
+ "transitionToState:"
+ "v28@0:8d16i24"
+ "valueForFlagSecureUIMinDisplayTime"
+ "widthAnchor"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}8@?0"
+ "\xf0\xf0\xf0A"
- "\x011\x13\x81\xf0\xe1"
- "\xf0\xf0\xf01"

```
