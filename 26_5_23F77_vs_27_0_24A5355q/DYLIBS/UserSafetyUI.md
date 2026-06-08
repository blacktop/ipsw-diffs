## UserSafetyUI

> `/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI`

```diff

-130.4.1.0.0
-  __TEXT.__text: 0x3a0c
-  __TEXT.__auth_stubs: 0x430
+145.0.0.0.0
+  __TEXT.__text: 0x38c0
   __TEXT.__objc_methlist: 0x3a4
-  __TEXT.__const: 0x2a4
-  __TEXT.__cstring: 0x554
+  __TEXT.__const: 0x2b4
+  __TEXT.__cstring: 0x624
   __TEXT.__ustring: 0x3c
   __TEXT.__oslogstring: 0x58
-  __TEXT.__swift5_typeref: 0x232
+  __TEXT.__swift5_typeref: 0x274
   __TEXT.__swift5_reflstr: 0xa3
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0xfc

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
   __TEXT.__unwind_info: 0x170
-  __TEXT.__objc_classname: 0x11c
-  __TEXT.__objc_methname: 0x763
-  __TEXT.__objc_methtype: 0x101
-  __TEXT.__objc_stubs: 0x880
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x178
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x170
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x278
-  __AUTH_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x120
   __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0x850
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH.__objc_data: 0x230
   __AUTH.__data: 0x98
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x68
+  __DATA.__data: 0xa0
   __DATA.__bss: 0x288
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE2BF175-91C0-3578-99EB-F75B82FB6A4A
-  Functions: 119
-  Symbols:   461
-  CStrings:  252
+  UUID: CFED1E67-F9F8-3221-A0C4-DBD23AF0B40E
+  Functions: 122
+  Symbols:   474
+  CStrings:  131
 
Symbols:
+ +[USUIInterventionScreenModel titleForScreen:workflow:type:]
+ ___swift_closure_destructor
+ ___swift_closure_destructor.8
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_UserSafetyUI
+ _get_witness_table 7SwiftUI4ViewRzlAA4MenuVyxAA12TupleContentVyAA08ModifiedF0VyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGSg_AA7ForEachVySaySo012USUIMoreHelpD6ActionCGSOAA6ButtonVyAJGGQPGGAaBHPyHC.6
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$titleForScreen:workflow:type:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x4
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x8
+ _swift_retain_x27
+ _symbolic _____ySiSgG 7SwiftUI30_EnvironmentKeyWritingModifierV
+ _symbolic _____y__________ySiSgGG 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV
+ _symbolic _____y__________ySiSgGGSg 7SwiftUI15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV
+ _symbolic _____y_____y__________ySiSgGGSg______ySaySo22USUIMoreHelpMenuActionCGSO_____yACGGQPG 7SwiftUI12TupleContentV AA08ModifiedD0V AA4TextV AA30_EnvironmentKeyWritingModifierV AA7ForEachV AA6ButtonV
+ _symbolic _____yx_____y_____y__________ySiSgGGSg______ySaySo22USUIMoreHelpMenuActionCGSO_____yADGGQPGG 7SwiftUI4MenuV AA12TupleContentV AA08ModifiedE0V AA4TextV AA30_EnvironmentKeyWritingModifierV AA7ForEachV AA6ButtonV
- +[USUIInterventionScreenModel titleForScreen:workflow:]
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_UserSafetyUI
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- __swift_FORCE_LOAD_$_swiftVideoToolbox_$_UserSafetyUI
- _get_witness_table 7SwiftUI4ViewRzlAA4MenuVyxAA05TupleC0VyAA15ModifiedContentVyAA4TextVAA30_EnvironmentKeyWritingModifierVySiSgGGSg_AA7ForEachVySaySo012USUIMoreHelpD6ActionCGSOAA6ButtonVyAJGGtGGAaBHPyHC.6
- _objc_msgSend$titleForScreen:workflow:
- _objc_release_x1
- _objc_retain_x21
- _symbolic _____y_____y__________ySiSgGGSg______ySaySo22USUIMoreHelpMenuActionCGSO_____yACGGtG 7SwiftUI9TupleViewV AA15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA7ForEachV AA6ButtonV
- _symbolic _____yx_____y_____y__________ySiSgGGSg______ySaySo22USUIMoreHelpMenuActionCGSO_____yADGGtGG 7SwiftUI4MenuV AA9TupleViewV AA15ModifiedContentV AA4TextV AA30_EnvironmentKeyWritingModifierV AA7ForEachV AA6ButtonV
CStrings:
+ "ADULT_RECEIVE_FIRST_EDU_SCREEN_TITLE"
+ "ADULT_RECEIVE_SECOND_EDU_SCREEN_TITLE"
+ "ADULT_SEND_FIRST_EDU_SCREEN_TITLE"
+ "ADULT_SEND_SECOND_EDU_SCREEN_TITLE"
+ "TEEN_OR_CHILD_RECEIVE_FIRST_EDU_SCREEN_TITLE"
+ "TEEN_OR_CHILD_RECEIVE_SECOND_EDU_SCREEN_TITLE"
+ "TEEN_OR_CHILD_SEND_FIRST_EDU_SCREEN_TITLE"
+ "TEEN_OR_CHILD_SEND_SECOND_EDU_SCREEN_TITLE"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8q16q24"
- "@36@0:8@16B24q28"
- "@40@0:8@16@24@32"
- "@40@0:8q16q24@32"
- "@40@0:8q16q24q32"
- "@48@0:8q16q24q32q40"
- "B"
- "B16@0:8"
- "RECEIVE_FIRST_EDU_SCREEN_TITLE"
- "RECEIVE_SECOND_EDU_SCREEN_TITLE"
- "SEND_FIRST_EDU_SCREEN_TITLE"
- "SEND_SECOND_EDU_SCREEN_TITLE"
- "T@\"NSArray\",&,N,V_actions"
- "T@\"NSArray\",C,N,V_actions"
- "T@\"NSArray\",C,N,V_bullets"
- "T@\"NSString\",C,N,V_emoji"
- "T@\"NSString\",C,N,V_imageName"
- "T@\"NSString\",C,N,V_text"
- "T@\"NSString\",C,N,V_title"
- "TB,N,V_destructive"
- "TB,N,V_primary"
- "Tq,N,V_actionID"
- "URL"
- "USUIContactParentsHelper"
- "USUIInterventionScreenAction"
- "USUIInterventionScreenBullet"
- "USUIInterventionScreenModel"
- "USUIInterventionViewController"
- "USUIMoreHelpMenuAction"
- "USUIMoreHelpMenuModel"
- "UserSafety"
- "_TtC12UserSafetyUIP33_817C96E6A49D0A34B0D9DE18410C6E1819ResourceBundleClass"
- "_actionID"
- "_actions"
- "_bullets"
- "_destructive"
- "_emoji"
- "_imageName"
- "_primary"
- "_text"
- "_title"
- "action:destructive:actionID:"
- "action:primary:actionID:"
- "actionID"
- "actions"
- "actionsForScreen:workflow:type:options:"
- "actionsForScreenOne:type:options:"
- "actionsForScreenTwo:type:"
- "addDefaultActionsTo:"
- "addMenuActionsTo:interventionType:"
- "addObject:"
- "addOptionalActionsTo:options:"
- "age"
- "arrayWithObjects:count:"
- "bullet:imageName:emoji:"
- "bullets"
- "bulletsForScreen:workflow:type:"
- "bulletsForScreenOneOver13:"
- "bulletsForScreenOneUnder13:"
- "bulletsForScreenTwoOver13:"
- "bulletsForScreenTwoUnder13:"
- "clientUI"
- "componentsJoinedByString:"
- "componentsWithString:"
- "contact"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "destructive"
- "emailAddresses"
- "emoji"
- "emojiForScreen:"
- "firstObject"
- "getCurrentInterventionType"
- "imageName"
- "imageNameForScreen:"
- "imageNamed:inBundle:compatibleWithTraitCollection:"
- "isMe"
- "isParent"
- "length"
- "localizedStringForKey:"
- "mainBundle"
- "memberType"
- "members"
- "menuTitleWith:"
- "modelForScreen:workflow:type:"
- "modelForScreen:workflow:type:options:"
- "modelWithOptions:interventionType:"
- "mutableCopy"
- "obtainChatWithParentsURLForInterventionType:completionHandler:"
- "obtainParentsForCurrentContact:"
- "openChatWithParentsForInterventionType:"
- "openChatWithURL:"
- "openURL:options:completionHandler:"
- "phoneNumbers"
- "primary"
- "q"
- "q16@0:8"
- "queryItemWithName:value:"
- "setActionID:"
- "setActions:"
- "setBullets:"
- "setDestructive:"
- "setEmoji:"
- "setImageName:"
- "setPrimary:"
- "setQueryItems:"
- "setText:"
- "setTitle:"
- "sharedApplication"
- "startRequestWithCompletionHandler:"
- "stringValue"
- "text"
- "title"
- "titleForScreen:workflow:"
- "urlFromAddressList:"
- "usImageNamed:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8q16"
- "v32@0:8@16q24"
- "v32@0:8q16@?24"
- "value"
- "viewControllerWithWorkflow:assetType:contextDictionary:"
- "viewControllerWithWorkflow:contextDictionary:"

```
