## GamePolicy

> `/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy`

```diff

-3.0.20.0.0
-  __TEXT.__text: 0x2346c
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_methlist: 0xe4c
-  __TEXT.__const: 0x142c
+3.0.24.1.0
+  __TEXT.__text: 0x249b0
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0xea4
+  __TEXT.__const: 0x149c
   __TEXT.__gcc_except_tab: 0x4c
-  __TEXT.__cstring: 0x20c1
+  __TEXT.__cstring: 0x2101
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__oslogstring: 0xc3
-  __TEXT.__swift5_typeref: 0x5a5
-  __TEXT.__swift5_reflstr: 0x93b
-  __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__constg_swiftt: 0x1018
-  __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_fieldmd: 0xa44
-  __TEXT.__swift5_proto: 0x94
-  __TEXT.__swift5_types: 0xb8
+  __TEXT.__oslogstring: 0x193
+  __TEXT.__swift5_typeref: 0x607
+  __TEXT.__swift5_reflstr: 0x97b
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__constg_swiftt: 0x105c
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_fieldmd: 0xa78
+  __TEXT.__swift5_proto: 0xbc
+  __TEXT.__swift5_types: 0xc0
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0xc38
-  __TEXT.__eh_frame: 0x38
+  __TEXT.__unwind_info: 0xcd0
+  __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_classname: 0xac
-  __TEXT.__objc_methname: 0xf2a
-  __TEXT.__objc_methtype: 0xf8
-  __TEXT.__objc_stubs: 0x760
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x678
+  __TEXT.__objc_methname: 0x107e
+  __TEXT.__objc_methtype: 0x131
+  __TEXT.__objc_stubs: 0x800
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x6a0
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x458
+  __DATA_CONST.__objc_selrefs: 0x498
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x5c8
-  __AUTH_CONST.__const: 0x6e8
+  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__const: 0x750
   __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x2628
+  __AUTH_CONST.__objc_const: 0x2720
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x17a8
-  __AUTH.__data: 0x738
-  __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x708
-  __DATA.__bss: 0x1260
+  __AUTH.__objc_data: 0x17b0
+  __AUTH.__data: 0x748
+  __DATA.__objc_ivar: 0x30
+  __DATA.__data: 0x788
+  __DATA.__bss: 0x1760
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x540
-  __DATA_DIRTY.__data: 0x4d8
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__objc_data: 0x548
+  __DATA_DIRTY.__data: 0x4b8
+  __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ArgumentParserInternal.framework/ArgumentParserInternal
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: BA565F09-160D-32FC-A2D5-75E7CBFA93AB
-  Functions: 1457
-  Symbols:   983
-  CStrings:  440
+  UUID: 06F693A3-6D3C-34DA-B1AB-04CF8AD867D7
+  Functions: 1510
+  Symbols:   1029
+  CStrings:  467
 
Symbols:
+ +[GPGameLibrary gameLibraryAppsFromGameLibraryGames:]
+ -[GPGameLibrary installedGamesDidChange:]
+ -[GPGameLibrary installedGamesDidChange:].cold.1
+ -[GPGameLibrary installedGamesDidChange:].cold.2
+ -[GPGameLibrary refreshInstalledGamesLibrary]
+ -[GPGameLibrary registerInstalledGamesDidChangeHandler:]
+ -[GPGameLibraryApp initWithPersistentIdentifier:bundleID:adamID:isGame:]
+ -[GPGameLibraryApp persistentIdentifier]
+ _OBJC_IVAR_$_GPGameLibrary._creationDate
+ _OBJC_IVAR_$_GPGameLibrary._gameLibrary
+ _OBJC_IVAR_$_GPGameLibrary._gameLibraryChangedHandler
+ _OBJC_IVAR_$_GPGameLibrary._libraryInitialized
+ _OBJC_IVAR_$_GPGameLibraryApp._persistentIdentifier
+ _OUTLINED_FUNCTION_1
+ __PROTOCOLS__TtC10GamePolicy24SustainedExecutionStatus.4
+ ___41-[GPGameLibrary installedGamesDidChange:]_block_invoke
+ ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.7
+ ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.7.cold.1
+ ___45-[GPGameLibrary refreshInstalledGamesLibrary]_block_invoke
+ ___45-[GPGameLibrary refreshInstalledGamesLibrary]_block_invoke_2
+ ___56-[GPGameLibrary registerInstalledGamesDidChangeHandler:]_block_invoke
+ ___56-[GPGameLibrary registerInstalledGamesDidChangeHandler:]_block_invoke.cold.1
+ ___NSArray0__struct
+ ___block_descriptor_32_e17_v16?0"NSArray"8l
+ ___block_literal_global.14
+ ___block_literal_global.5
+ ___swift_memcpy33_8
+ _associated conformance 10GamePolicy9SEMPolicyOSHAASQ
+ _associated conformance So22LSPersistentIdentifieraSHSCSQ
+ _associated conformance So22LSPersistentIdentifieras20_SwiftNewtypeWrapperSCSY
+ _associated conformance So22LSPersistentIdentifieras20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _memcmp
+ _objc_msgSend$count
+ _objc_msgSend$gameLibraryAppsFromGameLibraryGames:
+ _objc_msgSend$initWithPersistentIdentifier:bundleID:adamID:isGame:
+ _objc_msgSend$now
+ _objc_msgSend$persistentIdentifier
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_retainBlock
+ _objc_retain_x26
+ _objc_retain_x27
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic So6NSDataC
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 10GamePolicy9SEMPolicyO
+ _symbolic _____ So22LSPersistentIdentifiera
+ _symbolic _____Sg So22LSPersistentIdentifiera
+ _type_layout_string So22LSPersistentIdentifiera
- +[GPGameMonitorEnvoy deviceSupportsGamePolicy].cold.1
- -[GPGameLibraryApp initWithBundleID:adamID:isGame:]
- _MGIsDeviceOneOfType
- __PROTOCOLS__TtC10GamePolicy24SustainedExecutionStatus.5
- ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.6
- ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.6.cold.1
- ___46+[GPGameMonitorEnvoy deviceSupportsGamePolicy]_block_invoke
- ___block_literal_global.30
- ___block_literal_global.33
- ___swift_memcpy25_8
- __os_feature_enabled_impl
- _deviceSupportsGamePolicy._deviceSupportsGamePolicy
- _deviceSupportsGamePolicy.onceToken
- _objc_msgSend$initWithBundleID:adamID:isGame:
CStrings:
+ "?"
+ "@\"NSArray\""
+ "@\"NSData\""
+ "@\"NSDate\""
+ "@44@0:8@16@24@32B40"
+ "@?"
+ "Calling gameLibraryChangedHandler with locally cached library of %lu games"
+ "GPGameLibrary installed games initialized from cache in %f seconds."
+ "GPGameLibrary installedGamesDidChange, library now has %lu games"
+ "T@\"NSData\",N,R"
+ "T@\"NSData\",R,N,V_persistentIdentifier"
+ "_creationDate"
+ "_gameLibrary"
+ "_gameLibraryChangedHandler"
+ "_libraryInitialized"
+ "_persistentIdentifier"
+ "activePolicy"
+ "count"
+ "gameLibraryAppsFromGameLibraryGames:"
+ "initWithPersistentIdentifier:bundleID:adamID:isGame:"
+ "installedGamesDidChange:"
+ "now"
+ "persistentIdentifier"
+ "refreshInstalledGamesLibrary"
+ "registerInstalledGamesDidChangeHandler:"
+ "timeIntervalSinceDate:"
+ "v24@0:8@\"NSArray\"16"
- "@36@0:8@16@24B32"
- "GamePolicy"
- "initWithBundleID:adamID:isGame:"
- "universalGamePolicySupport"

```
