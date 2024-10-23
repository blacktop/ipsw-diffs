## promotedcontentd

> `/usr/libexec/promotedcontentd`

```diff

-552.1.0.0.0
-  __TEXT.__text: 0x195e40
-  __TEXT.__auth_stubs: 0x2270
-  __TEXT.__objc_stubs: 0x177c0
-  __TEXT.__objc_methlist: 0x12d6c
+554.9.0.0.0
+  __TEXT.__text: 0x196658
+  __TEXT.__auth_stubs: 0x2290
+  __TEXT.__objc_stubs: 0x17680
+  __TEXT.__objc_methlist: 0x12ddc
   __TEXT.__const: 0x12ec0
-  __TEXT.__objc_methname: 0x232d1
-  __TEXT.__oslogstring: 0xc28f
-  __TEXT.__cstring: 0xe1ea
+  __TEXT.__objc_methname: 0x233c4
+  __TEXT.__oslogstring: 0xc26f
+  __TEXT.__cstring: 0xe2da
   __TEXT.__objc_classname: 0x249d
-  __TEXT.__objc_methtype: 0x4863
-  __TEXT.__gcc_except_tab: 0x1598
+  __TEXT.__objc_methtype: 0x4893
+  __TEXT.__gcc_except_tab: 0x15ac
   __TEXT.__constg_swiftt: 0x1cdc
   __TEXT.__swift5_typeref: 0x1386
   __TEXT.__swift5_fieldmd: 0x15a8

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x49d8
-  __TEXT.__eh_frame: 0x1e08
-  __DATA_CONST.__auth_got: 0x1148
+  __TEXT.__unwind_info: 0x49e0
+  __TEXT.__eh_frame: 0x1e50
+  __DATA_CONST.__auth_got: 0x1158
   __DATA_CONST.__got: 0xba0
-  __DATA_CONST.__auth_ptr: 0x700
-  __DATA_CONST.__const: 0xae30
-  __DATA_CONST.__cfstring: 0xe4e0
+  __DATA_CONST.__auth_ptr: 0x698
+  __DATA_CONST.__const: 0xae60
+  __DATA_CONST.__cfstring: 0xe560
   __DATA_CONST.__objc_classlist: 0xb90
-  __DATA_CONST.__objc_catlist: 0xc0
+  __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf0

   __DATA_CONST.__objc_dictobj: 0xa28
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x25ee8
-  __DATA.__objc_selrefs: 0x8828
-  __DATA.__objc_ivar: 0x1464
+  __DATA.__objc_const: 0x25fa8
+  __DATA.__objc_selrefs: 0x8858
+  __DATA.__objc_ivar: 0x146c
   __DATA.__objc_data: 0x6e48
-  __DATA.__data: 0x5d98
+  __DATA.__data: 0x5da8
   __DATA.__bss: 0x4a50
   __DATA.__common: 0xd8
   - /AppleInternal/Library/Frameworks/TestHookService.framework/TestHookService

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_errno.dylib

   - /usr/lib/swift/libswift_stdio.dylib
   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8172
-  Symbols:   2039
-  CStrings:  10625
+  Functions: 8184
+  Symbols:   2047
+  CStrings:  10641
 
Symbols:
+ OBJC_IVAR_$_APPBAdAction._prefersToOpenInstalledApp
+ OBJC_IVAR_$_APPBElement._action
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftsimd
CStrings:
+ "\x06\x11"
+ "@\"APPBAdAction\""
+ "@48@0:8@16@24Q32^@40"
+ "Client info missing in ad request. Unable to create payload for legacy interface."
+ "Config System Background Task Expired before request."
+ "Config System Background Task retry after Success."
+ "Expired"
+ "Failed to construct URL using actionURL."
+ "Legacy Interface"
+ "T@\"APPBAdAction\",&,N,V_action"
+ "TB,N,V_prefersToOpenInstalledApp"
+ "_expireTask:"
+ "_prefersToOpenInstalledApp"
+ "hasAction"
+ "hasPrefersToOpenInstalledApp"
+ "initWithAdData:element:elementIndex:error:"
+ "makeTapActionWithLegacyAction:iTunesMetadata:error:"
+ "prefersToOpenInstalledApp"
+ "requestTypes"
+ "setHasPrefersToOpenInstalledApp:"
+ "setOpensInstalledApp:"
+ "setPrefersToOpenInstalledApp:"
+ "{?=\"adamIdentifier\"b1\"autoDismissInterval\"b1\"appStoreViewTemplate\"b1\"backgroundColor\"b1\"confirmedClickTimeInterval\"b1\"letterboxStoryboardColor\"b1\"storyboardPresentationOrientations\"b1\"storyboardSupportedOrientations\"b1\"transitionType\"b1\"adManagesPurchaseFlow\"b1\"allowSelfDismissal\"b1\"loadNewImpressionOnActionComplete\"b1\"prefersToOpenInstalledApp\"b1\"scrolling\"b1\"suppressesPermissionToExitDialog\"b1}"
- "\x05\x11"
- "@40@0:8@16Q24^@32"
- "Action URL for content %!{(MISSING)public}@ is empty."
- "Config System Background Task trying to retry after."
- "Content %!{(MISSING)public}@ has no actions."
- "Tap Action is nil"
- "URLWithString:encodingInvalidCharacters:"
- "_tapActionFromAdData:error:"
- "initWithElement:elementIndex:error:"
- "{?=\"adamIdentifier\"b1\"autoDismissInterval\"b1\"appStoreViewTemplate\"b1\"backgroundColor\"b1\"confirmedClickTimeInterval\"b1\"letterboxStoryboardColor\"b1\"storyboardPresentationOrientations\"b1\"storyboardSupportedOrientations\"b1\"transitionType\"b1\"adManagesPurchaseFlow\"b1\"allowSelfDismissal\"b1\"loadNewImpressionOnActionComplete\"b1\"scrolling\"b1\"suppressesPermissionToExitDialog\"b1}"

```
