## UserSafetyUI

> `/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI`

```diff

-130.1.2.0.0
-  __TEXT.__text: 0x388c
-  __TEXT.__auth_stubs: 0x480
+130.2.9.2.0
+  __TEXT.__text: 0x3a0c
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_methlist: 0x3a4
   __TEXT.__const: 0x2a4
-  __TEXT.__cstring: 0x5a4
+  __TEXT.__cstring: 0x554
   __TEXT.__ustring: 0x3c
   __TEXT.__oslogstring: 0x58
   __TEXT.__swift5_typeref: 0x232

   __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x178
-  __TEXT.__objc_classname: 0xce
-  __TEXT.__objc_methname: 0x773
+  __TEXT.__unwind_info: 0x170
+  __TEXT.__objc_classname: 0x11c
+  __TEXT.__objc_methname: 0x763
   __TEXT.__objc_methtype: 0x101
-  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x880
   __DATA_CONST.__got: 0xf8
   __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x280
-  __AUTH_CONST.__auth_got: 0x248
+  __DATA_CONST.__objc_selrefs: 0x278
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x140
   __AUTH_CONST.__cfstring: 0x7c0
   __AUTH_CONST.__objc_const: 0x850

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6C7D8A91-77E4-3043-A6D3-58153C6645E0
+  UUID: CF83A1BE-CE3F-3CDA-8BD4-0F71FC2642A2
   Functions: 119
-  Symbols:   459
-  CStrings:  253
+  Symbols:   461
+  CStrings:  252
 
Symbols:
+ _objc_msgSend$actionID
+ _objc_msgSend$actions
+ _objc_msgSend$destructive
+ _objc_msgSend$getCurrentInterventionType
+ _objc_msgSend$modelWithOptions:interventionType:
+ _objc_msgSend$title
+ _objc_release_x1
+ _objc_retain_x21
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x27
- _objc_retain_x3
- _objc_retain_x4
Functions:
~ +[USUIInterventionScreenBullet bullet:imageName:emoji:] : 152 -> 144
~ +[USUIInterventionScreenModel modelForScreen:workflow:type:options:] : 312 -> 332
~ +[USUIInterventionScreenModel titleForScreen:workflow:] : 116 -> 120
~ +[USUIInterventionScreenModel imageNameForScreen:] : 28 -> 76
~ +[USUIInterventionScreenModel emojiForScreen:] : 28 -> 76
~ +[USUIInterventionScreenModel bulletsForScreen:workflow:type:] : 152 -> 180
~ +[USUIInterventionScreenModel bulletsForScreenOneUnder13:] : 428 -> 456
~ +[USUIInterventionScreenModel bulletsForScreenOneOver13:] : 332 -> 352
~ +[USUIInterventionScreenModel bulletsForScreenTwoUnder13:] : 332 -> 352
~ +[USUIInterventionScreenModel bulletsForScreenTwoOver13:] : 336 -> 356
~ +[USUIInterventionScreenModel actionsForScreen:workflow:type:options:] : 96 -> 108
~ +[USUIInterventionScreenModel actionsForScreenOne:type:options:] : 396 -> 428
~ +[USUIInterventionScreenModel actionsForScreenTwo:type:] : 404 -> 432
~ ___67+[USUIContactParentsHelper openChatWithParentsForInterventionType:]_block_invoke : 96 -> 100
~ ___67+[USUIContactParentsHelper openChatWithParentsForInterventionType:]_block_invoke_3 : 96 -> 100
~ +[USUIContactParentsHelper obtainChatWithParentsURLForInterventionType:completionHandler:] : 220 -> 224
~ ___90+[USUIContactParentsHelper obtainChatWithParentsURLForInterventionType:completionHandler:]_block_invoke : 104 -> 108
~ +[USUIContactParentsHelper openChatWithURL:] : 112 -> 116
~ +[USUIContactParentsHelper urlFromAddressList:] : 420 -> 452
~ +[USUIContactParentsHelper obtainParentsForCurrentContact:] : 168 -> 164
~ ___59+[USUIContactParentsHelper obtainParentsForCurrentContact:]_block_invoke : 932 -> 988
~ +[UIImage(UserSafety) usImageNamed:] : 136 -> 144
~ +[USUIMoreHelpMenuModel modelWithOptions:interventionType:] : 212 -> 216
~ +[USUIMoreHelpMenuModel menuTitleWith:] : 76 -> 80
~ +[USUIMoreHelpMenuModel addMenuActionsTo:interventionType:] : 192 -> 200
~ +[USUIMoreHelpMenuModel addDefaultActionsTo:] : 160 -> 168
~ +[USUIMoreHelpMenuModel addOptionalActionsTo:options:] : 340 -> 372
~ -[USUIMoreHelpMenuModel setActions:] : 12 -> 64
~ sub_2757d6878 -> sub_299ebaa80 : 320 -> 312
~ sub_2757d69b8 -> sub_299ebabb8 : 244 -> 228
~ sub_2757d6d3c -> sub_299ebaf2c : 1268 -> 1256
~ sub_2757d723c -> sub_299ebb420 : 612 -> 588
~ sub_2757d7610 -> sub_299ebb7dc : 28 -> 4
~ sub_2757d76f8 -> sub_299ebb8ac : 324 -> 320
~ sub_2757d783c -> sub_299ebb9ec : 456 -> 452
~ sub_2757d7c50 -> sub_299ebbdfc : 288 -> 280
~ sub_2757d7ebc -> sub_299ebc060 : 80 -> 76
~ sub_2757d7f0c -> sub_299ebc0ac : 16 -> 24
~ sub_2757d7f1c -> sub_299ebc0c4 : 80 -> 76
~ sub_2757d7f6c -> sub_299ebc110 : 16 -> 24
~ sub_2757d7fd0 -> sub_299ebc17c : 52 -> 48
~ sub_2757d8034 -> sub_299ebc1dc : 296 -> 288
~ sub_2757d815c -> sub_299ebc2fc : 268 -> 236
CStrings:
- "bundleForClass:"

```
