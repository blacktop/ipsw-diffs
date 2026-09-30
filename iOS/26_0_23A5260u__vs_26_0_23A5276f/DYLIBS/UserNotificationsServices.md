## UserNotificationsServices

> `/System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices`

```diff

-616.0.1.0.0
-  __TEXT.__text: 0x22114
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x4fc
-  __TEXT.__const: 0x3664
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__cstring: 0x906
-  __TEXT.__oslogstring: 0xaa7
+623.0.0.0.0
+  __TEXT.__text: 0x23480
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_methlist: 0x58c
+  __TEXT.__const: 0x3684
+  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__cstring: 0x9e6
+  __TEXT.__oslogstring: 0xbd5
   __TEXT.__swift5_typeref: 0x771
   __TEXT.__swift5_reflstr: 0x737
   __TEXT.__swift5_assocty: 0x228

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x36c
   __TEXT.__swift5_types: 0xd0
-  __TEXT.__unwind_info: 0xa08
+  __TEXT.__dlopen_cstrs: 0x4b
+  __TEXT.__unwind_info: 0xa98
   __TEXT.__eh_frame: 0xa10
-  __TEXT.__objc_classname: 0x101
-  __TEXT.__objc_methname: 0x1682
-  __TEXT.__objc_methtype: 0x275
-  __TEXT.__objc_stubs: 0x1320
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__objc_classname: 0x119
+  __TEXT.__objc_methname: 0x1af0
+  __TEXT.__objc_methtype: 0x2cf
+  __TEXT.__objc_stubs: 0x16e0
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__const: 0x200
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x618
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x5f8
-  __AUTH_CONST.__const: 0x1338
-  __AUTH_CONST.__cfstring: 0x280
-  __AUTH_CONST.__objc_const: 0x868
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x40
+  __DATA_CONST.__objc_selrefs: 0x710
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x648
+  __AUTH_CONST.__const: 0x1358
+  __AUTH_CONST.__cfstring: 0x380
+  __AUTH_CONST.__objc_const: 0x980
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0xde0
-  __DATA.__bss: 0x6890
+  __DATA.__bss: 0x68c0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x720
   __DATA_DIRTY.__bss: 0x520

   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D6FDDE8C-11BD-3870-B18C-D52CC7A7D249
-  Functions: 1129
-  Symbols:   870
-  CStrings:  405
+  UUID: 74D69BCA-63E2-306F-849D-8F86E891C1D1
+  Functions: 1155
+  Symbols:   991
+  CStrings:  470
 
Symbols:
+ +[UNSAvatarImageRenderer sharedInstanceForPointSize:]
+ +[UNSAvatarImageRenderer sharedInstanceForPointSize:].cold.1
+ -[UNSAvatarImageRenderer .cxx_destruct]
+ -[UNSAvatarImageRenderer _decrementAvatarImageGenerationQueueUsageCountAndInvalidateIfNeeded]
+ -[UNSAvatarImageRenderer _getAvatarImageGenerationQueueAndIncrementUsageCount]
+ -[UNSAvatarImageRenderer _imageNamed:inBundleIdentifier:traitCollection:]
+ -[UNSAvatarImageRenderer _imageNamed:inBundleIdentifier:traitCollection:].cold.1
+ -[UNSAvatarImageRenderer _initWithPointSize:]
+ -[UNSAvatarImageRenderer _queue_imageForContacts:compatibleWithTraitCollection:circular:]
+ -[UNSAvatarImageRenderer _silhouetteFallbackImageNameForContacts:]
+ -[UNSAvatarImageRenderer _systemImageNamed:traitCollection:]
+ -[UNSAvatarImageRenderer renderAvatarForCommunicationContext:bundleIdentifier:compatibleWithTraitCollection:completion:]
+ GCC_except_table0
+ GCC_except_table13
+ GCC_except_table3
+ GCC_except_table7
+ GCC_except_table8
+ GCC_except_table9
+ _BSDispatchQueueCreateSerialWithQoS
+ _ContactsUILibrary
+ _ContactsUILibraryCore.frameworkLibrary
+ _NSStringFromClass
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$_UIImageSymbolConfiguration
+ _OBJC_CLASS_$_UNSAvatarImageRenderer
+ _OBJC_IVAR_$_UNSAvatarImageRenderer._avatarImageGenerationQueue
+ _OBJC_IVAR_$_UNSAvatarImageRenderer._avatarImageGenerationQueueUsageCount
+ _OBJC_IVAR_$_UNSAvatarImageRenderer._avatarRenderer
+ _OBJC_IVAR_$_UNSAvatarImageRenderer._pointSize
+ _OBJC_METACLASS_$_UNSAvatarImageRenderer
+ _UNLogCommunicationNotifications
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_UNSAvatarImageRenderer
+ __OBJC_$_INSTANCE_METHODS_UNSAvatarImageRenderer
+ __OBJC_$_INSTANCE_VARIABLES_UNSAvatarImageRenderer
+ __OBJC_CLASS_RO_$_UNSAvatarImageRenderer
+ __OBJC_METACLASS_RO_$_UNSAvatarImageRenderer
+ ___120-[UNSAvatarImageRenderer renderAvatarForCommunicationContext:bundleIdentifier:compatibleWithTraitCollection:completion:]_block_invoke
+ ___120-[UNSAvatarImageRenderer renderAvatarForCommunicationContext:bundleIdentifier:compatibleWithTraitCollection:completion:]_block_invoke.3
+ ___53+[UNSAvatarImageRenderer sharedInstanceForPointSize:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___ContactsUILibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_91_e8_32s40s48s56s64bs72r80r_e5_v8?0ls64l8r72l8s32l8s40l8s48l8r80l8s56l8
+ ___getCNAvatarImageRendererClass_block_invoke
+ ___getCNAvatarImageRendererClass_block_invoke.cold.1
+ ___getCNAvatarImageRendererSettingsClass_block_invoke
+ ___getCNAvatarImageRendererSettingsClass_block_invoke.cold.1
+ ___getCNAvatarImageRenderingScopeClass_block_invoke
+ ___getCNAvatarImageRenderingScopeClass_block_invoke.cold.1
+ __sl_dlopen
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_UserNotificationsServices
+ _abort_report_np
+ _dispatch_async
+ _free
+ _getCNAvatarImageRendererClass
+ _getCNAvatarImageRendererClass.softClass
+ _getCNAvatarImageRendererSettingsClass.softClass
+ _getCNAvatarImageRenderingScopeClass.softClass
+ _objc_getClass
+ _objc_msgSend$URL
+ _objc_msgSend$_decrementAvatarImageGenerationQueueUsageCountAndInvalidateIfNeeded
+ _objc_msgSend$_getAvatarImageGenerationQueueAndIncrementUsageCount
+ _objc_msgSend$_imageNamed:inBundleIdentifier:traitCollection:
+ _objc_msgSend$_initWithPointSize:
+ _objc_msgSend$_queue_imageForContacts:compatibleWithTraitCollection:circular:
+ _objc_msgSend$_silhouetteFallbackImageNameForContacts:
+ _objc_msgSend$_systemImageNamed:traitCollection:
+ _objc_msgSend$avatarImageForContacts:scope:
+ _objc_msgSend$bundleForClass:
+ _objc_msgSend$bundleWithURL:
+ _objc_msgSend$configurationWithPointSize:
+ _objc_msgSend$configurationWithTraitCollection:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$descriptorForRequiredKeys
+ _objc_msgSend$displayScale
+ _objc_msgSend$generateEphemeralContactsForImageRenderingWithContext:bundleIdentifier:descriptorForRequiredKeys:
+ _objc_msgSend$imageName
+ _objc_msgSend$imageNamed:inBundle:compatibleWithTraitCollection:
+ _objc_msgSend$initWithSettings:
+ _objc_msgSend$isBusinessCorrespondence
+ _objc_msgSend$isSystemImage
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$offMainThreadSynchronousRenderingOnlySettingsWithCacheSize:
+ _objc_msgSend$scopeWithPointSize:scale:rightToLeft:style:backgroundStyle:
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$systemImageNamed:withConfiguration:
+ _objc_msgSend$unkit_applicationRecordIfEligibleToDeliverNotificationsForBundleIdentifier:
+ _objc_msgSend$userInterfaceStyle
+ _objc_retainBlock
+ _objc_retain_x9
+ _sharedInstanceForPointSize:.__pointSizesToRenderers
+ _sharedInstanceForPointSize:.onceToken
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_UserNotificationsServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_UserNotificationsServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_UserNotificationsServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_UserNotificationsServices
CStrings:
+ "%s"
+ ".%@.avatarGeneration"
+ "<NULL>"
+ "@\"CNAvatarImageRenderer\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@24@0:8d16"
+ "CNAvatarImageRenderer"
+ "CNAvatarImageRendererSettings"
+ "CNAvatarImageRenderingScope"
+ "Error loading image named '%{public}@' in bundle '%{public}@'. Error: %@"
+ "NO"
+ "UNSAvatarImageRenderer"
+ "URL"
+ "Unable to find class %s"
+ "YES"
+ "YES with count of '%lu'"
+ "[%{public}@]: Context identifier:%{public}@ - Rendered avatar image: %{public}@. Tried System Image: %{public}@, Tried Bundle Image: %{public}@, Tried Ephemeral Contacts: %{public}@, Tried Silhouette Fallback of Name: %{public}@"
+ "_avatarImageGenerationQueue"
+ "_avatarImageGenerationQueueUsageCount"
+ "_avatarRenderer"
+ "_decrementAvatarImageGenerationQueueUsageCountAndInvalidateIfNeeded"
+ "_getAvatarImageGenerationQueueAndIncrementUsageCount"
+ "_imageNamed:inBundleIdentifier:traitCollection:"
+ "_initWithPointSize:"
+ "_pointSize"
+ "_queue_imageForContacts:compatibleWithTraitCollection:circular:"
+ "_silhouetteFallbackImageNameForContacts:"
+ "_systemImageNamed:traitCollection:"
+ "avatarImageForContacts:scope:"
+ "bundleForClass:"
+ "bundleWithURL:"
+ "configurationWithPointSize:"
+ "configurationWithTraitCollection:"
+ "copy"
+ "count"
+ "d"
+ "descriptorForRequiredKeys"
+ "displayScale"
+ "imageName"
+ "imageNamed:inBundle:compatibleWithTraitCollection:"
+ "initWithSettings:"
+ "isBusinessCorrespondence"
+ "isSystemImage"
+ "numberWithDouble:"
+ "offMainThreadSynchronousRenderingOnlySettingsWithCacheSize:"
+ "person.2.circle.fill"
+ "person.3.fill"
+ "person.crop.circle.fill"
+ "renderAvatarForCommunicationContext:bundleIdentifier:compatibleWithTraitCollection:completion:"
+ "scopeWithPointSize:scale:rightToLeft:style:backgroundStyle:"
+ "sharedInstanceForPointSize:"
+ "softlink:r:path:/System/Library/Frameworks/ContactsUI.framework/ContactsUI"
+ "stringByAppendingFormat:"
+ "systemImageNamed:withConfiguration:"
+ "unkit_applicationRecordIfEligibleToDeliverNotificationsForBundleIdentifier:"
+ "userInterfaceStyle"
+ "v48@0:8@16@24@32@?40"

```
