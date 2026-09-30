## GamePolicy

> `/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy`

```diff

-3.3.3.0.0
-  __TEXT.__text: 0x19168
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0xd74
-  __TEXT.__const: 0xef0
-  __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__cstring: 0x1de6
+3.4.3.0.0
+  __TEXT.__text: 0x18e00
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_methlist: 0xe2c
+  __TEXT.__const: 0xf20
+  __TEXT.__cstring: 0xd56
+  __TEXT.__gcc_except_tab: 0x6c
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__oslogstring: 0x193
-  __TEXT.__swift5_typeref: 0x565
-  __TEXT.__swift5_fieldmd: 0x664
+  __TEXT.__oslogstring: 0x1d3
+  __TEXT.__swift5_typeref: 0x597
+  __TEXT.__swift5_fieldmd: 0x67c
   __TEXT.__constg_swiftt: 0xd70
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x528
+  __TEXT.__swift5_reflstr: 0x548
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x970
-  __TEXT.__eh_frame: 0xe0
-  __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methname: 0x10bb
-  __TEXT.__objc_methtype: 0x146
-  __TEXT.__objc_stubs: 0x840
+  __TEXT.__unwind_info: 0x988
+  __TEXT.__eh_frame: 0x80
+  __TEXT.__objc_classname: 0x7f6
+  __TEXT.__objc_methname: 0x188f
+  __TEXT.__objc_methtype: 0x89b
+  __TEXT.__objc_stubs: 0xbe0
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0x588
-  __DATA_CONST.__objc_classlist: 0x100
+  __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a8
+  __DATA_CONST.__objc_selrefs: 0x4e8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x650
-  __AUTH_CONST.__const: 0x5a8
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x2040
+  __AUTH_CONST.__auth_got: 0x648
+  __AUTH_CONST.__const: 0x5b0
+  __AUTH_CONST.__cfstring: 0x260
+  __AUTH_CONST.__objc_const: 0x21f8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1430
+  __AUTH.__objc_data: 0x1480
   __AUTH.__data: 0x6b8
-  __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x560
+  __DATA.__objc_ivar: 0x40
+  __DATA.__data: 0x538
   __DATA.__bss: 0xed0
-  __DATA_DIRTY.__objc_data: 0x3f0
-  __DATA_DIRTY.__data: 0xd8
+  __DATA_DIRTY.__objc_data: 0x3f8
+  __DATA_DIRTY.__data: 0x128
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal
-  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/GamePolicyFoundation.framework/GamePolicyFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AE0E328E-75B7-31A8-A109-AE09AD55D215
-  Functions: 1117
-  Symbols:   977
-  CStrings:  444
+  UUID: 327B53B5-9C0D-3D57-B5D1-2D4AF62C256A
+  Functions: 1130
+  Symbols:   1051
+  CStrings:  476
 
Symbols:
+ +[GPGameLibrary libraryForUserIdentifier:]
+ +[GameMetadataHints supportsSecureCoding]
+ -[GPGameLibrary _onqueue_connectToXPCService].cold.1
+ -[GPGameLibrary initWithUserIdentifier:]
+ -[GPGameLibraryApp gameMetadataHints]
+ -[GPGameLibraryApp initWithPersistentIdentifier:bundleID:adamID:isGame:gameMetadataHints:]
+ -[GameMetadataHints .cxx_destruct]
+ -[GameMetadataHints displayName]
+ -[GameMetadataHints encodeWithCoder:]
+ -[GameMetadataHints executableURL]
+ -[GameMetadataHints initWithCoder:]
+ -[GameMetadataHints initWithDisplayName:executableURL:]
+ -[GameMetadataHints init]
+ GCC_except_table39
+ GCC_except_table5
+ _OBJC_CLASS_$_GameMetadataHints
+ _OBJC_CLASS_$_NSURL
+ _OBJC_IVAR_$_GPGameLibrary._userIdentifier
+ _OBJC_IVAR_$_GPGameLibraryApp._gameMetadataHints
+ _OBJC_IVAR_$_GameMetadataHints._displayName
+ _OBJC_IVAR_$_GameMetadataHints._executableURL
+ _OBJC_METACLASS_$_GameMetadataHints
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_CLASS_METHODS_GameMetadataHints
+ __OBJC_$_CLASS_PROP_LIST_GameMetadataHints
+ __OBJC_$_INSTANCE_METHODS_GameMetadataHints
+ __OBJC_$_INSTANCE_VARIABLES_GameMetadataHints
+ __OBJC_$_PROP_LIST_GameMetadataHints
+ __OBJC_CLASS_PROTOCOLS_$_GameMetadataHints
+ __OBJC_CLASS_RO_$_GameMetadataHints
+ __OBJC_METACLASS_RO_$_GameMetadataHints
+ __PROTOCOLS_GamingMetadataModel.25
+ __PROTOCOLS__GamePolicyAssertion_Attribute.16
+ __PROTOCOLS__TtC10GamePolicy18GameModeCCUIStatus.63
+ __PROTOCOLS__TtC10GamePolicy19GamePolicyAssertion.10
+ __PROTOCOLS__TtC10GamePolicy22GameModeCCUIStatusInfo.47
+ __PROTOCOLS__TtC10GamePolicy24GameModeCCUIStatusBundle.57
+ __PROTOCOLS___GamePolicyAgentUpdateGameEvent.16
+ ___40-[GPGameLibrary initWithUserIdentifier:]_block_invoke
+ ___swift_memcpy48_8
+ _geteuid
+ _objc_alloc_init
+ _objc_msgSend$boolValue
+ _objc_msgSend$compare:
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$copy
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$description
+ _objc_msgSend$displayName
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$executableURL
+ _objc_msgSend$gameMetadataHints
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getValue:size:
+ _objc_msgSend$init
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithDisplayName:executableURL:
+ _objc_msgSend$initWithPersistentIdentifier:bundleID:adamID:isGame:gameMetadataHints:
+ _objc_msgSend$initWithUnsignedInt:
+ _objc_msgSend$initWithUnsignedInteger:
+ _objc_msgSend$initWithUserIdentifier:
+ _objc_msgSend$initializeGameLibraryWithUserIdentifier:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$postNotification:
+ _objc_msgSend$requestLaunchGamesApp
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$unsignedIntegerValue
+ _objc_release_x28
+ _objc_retain_x5
+ _symbolic So17GameMetadataHintsCSg
+ _symbolic So17GameMetadataHintsCm
- +[GPGameCenterMediator launchOverlayForGameBundleId:auditToken:]
- GCC_except_table3
- _OBJC_CLASS_$_BSAuditToken
- __PROTOCOLS_GamingMetadataModel.24
- __PROTOCOLS__GamePolicyAssertion_Attribute.15
- __PROTOCOLS__TtC10GamePolicy18GameModeCCUIStatus.61
- __PROTOCOLS__TtC10GamePolicy19GamePolicyAssertion.9
- __PROTOCOLS__TtC10GamePolicy22GameModeCCUIStatusInfo.45
- __PROTOCOLS__TtC10GamePolicy24GameModeCCUIStatusBundle.55
- __PROTOCOLS___GamePolicyAgentUpdateGameEvent.10
- ___21-[GPGameLibrary init]_block_invoke
- ___swift_memcpy33_8
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_GamePolicy
- _malloc
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$initWithAuditToken:
- _objc_msgSend$initWithPersistentIdentifier:bundleID:adamID:isGame:
- _objc_msgSend$launchOverlayForGameBundleId:auditToken:
- _objc_retain_x1
- _objc_retain_x3
CStrings:
+ "@\"GameMetadataHints\""
+ "@\"NSURL\""
+ "@20@0:8I16"
+ "@32@0:8@16@24"
+ "@52@0:8@16@24@32B40@44"
+ "GameMetadataHints"
+ "GamingMetadataModel"
+ "I"
+ "Initializing GPGameLibrary for user %d with gamepolicyd."
+ "T@\"GameMetadataHints\",N,R,VgameMetadataHints"
+ "T@\"GameMetadataHints\",R,N,V_gameMetadataHints"
+ "T@\"NSString\",R,N,V_displayName"
+ "T@\"NSURL\",R,N,V_executableURL"
+ "_displayName"
+ "_executableURL"
+ "_gameMetadataHints"
+ "_userIdentifier"
+ "com.apple.gamepolicyd.app"
+ "copy"
+ "decodeObjectOfClass:forKey:"
+ "displayName"
+ "executableURL"
+ "gameMetadataHints"
+ "initWithDisplayName:executableURL:"
+ "initWithPersistentIdentifier:bundleID:adamID:isGame:gameMetadataHints:"
+ "initWithUserIdentifier:"
+ "initializeGameLibraryWithUserIdentifier:"
+ "libraryForUserIdentifier:"
+ "v20@0:8I16"
- "initWithAuditToken:"
- "launchOverlayForGameBundleId:auditToken:"
- "v56@0:8@16{?=[8I]}24"

```
