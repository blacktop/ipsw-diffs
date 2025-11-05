## LoginUIKit

> `/System/Library/PrivateFrameworks/LoginUIKit.framework/Versions/A/LoginUIKit`

```diff

-370.3.2.0.0
-  __TEXT.__text: 0x947f0
-  __TEXT.__auth_stubs: 0x1db0
-  __TEXT.__objc_methlist: 0x8e2c
-  __TEXT.__const: 0x9a6
-  __TEXT.__cstring: 0x87d5
-  __TEXT.__gcc_except_tab: 0x1038
+370.5.3.0.0
+  __TEXT.__text: 0x93cac
+  __TEXT.__auth_stubs: 0x1d50
+  __TEXT.__objc_methlist: 0x9744
+  __TEXT.__const: 0x8c6
+  __TEXT.__cstring: 0x843d
+  __TEXT.__gcc_except_tab: 0x103c
   __TEXT.__dlopen_cstrs: 0x288
   __TEXT.__ustring: 0x3a
-  __TEXT.__oslogstring: 0x47b
+  __TEXT.__oslogstring: 0x471
+  __TEXT.__swift5_typeref: 0x1ea
   __TEXT.__constg_swiftt: 0x130
-  __TEXT.__swift5_typeref: 0x1c6
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0xf8
   __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift5_fieldmd: 0x4c
   __TEXT.__swift5_reflstr: 0x5
-  __TEXT.__unwind_info: 0x25e0
-  __TEXT.__eh_frame: 0xc78
-  __TEXT.__objc_classname: 0x11ab
-  __TEXT.__objc_methname: 0x1456a
+  __TEXT.__unwind_info: 0x2618
+  __TEXT.__eh_frame: 0xc08
+  __TEXT.__objc_classname: 0x11c0
+  __TEXT.__objc_methname: 0x145ec
   __TEXT.__objc_methtype: 0x2c7b
-  __TEXT.__objc_stubs: 0xdf60
-  __DATA_CONST.__got: 0xfc0
-  __DATA_CONST.__const: 0x858
-  __DATA_CONST.__objc_classlist: 0x528
+  __TEXT.__objc_stubs: 0xdfe0
+  __DATA_CONST.__got: 0xfc8
+  __DATA_CONST.__const: 0x880
+  __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5120
+  __DATA_CONST.__objc_selrefs: 0x5410
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x470
-  __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0xee8
-  __AUTH_CONST.__const: 0x1b80
-  __AUTH_CONST.__cfstring: 0x6f20
-  __AUTH_CONST.__objc_const: 0xfe38
-  __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__objc_intobj: 0x168
+  __DATA_CONST.__objc_superrefs: 0x478
+  __DATA_CONST.__objc_arraydata: 0x108
+  __AUTH_CONST.__auth_got: 0xeb8
+  __AUTH_CONST.__const: 0x1c10
+  __AUTH_CONST.__cfstring: 0x6f40
+  __AUTH_CONST.__objc_const: 0xeed0
+  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x33c0
+  __AUTH.__objc_data: 0x3410
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x9d4
-  __DATA.__data: 0xdb8
+  __DATA.__objc_ivar: 0x9d8
+  __DATA.__data: 0xdc0
   __DATA.__bss: 0x5f0
-  __DATA.__common: 0xd8
+  __DATA.__common: 0xc8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIOKit.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 9367EF56-283E-39F8-939B-6644F68E0DF5
-  Functions: 3725
-  Symbols:   8566
-  CStrings:  6350
+  UUID: F218054C-B89E-3CDC-8147-76323B70AC9A
+  Functions: 3751
+  Symbols:   8622
+  CStrings:  6338
 
Symbols:
+ +[LUIAuthenticationManager sharedManager].cold.1
+ +[LUIClockTimer sharedClockTimer].cold.1
+ +[LUIDebugUserController sharedManger].cold.1
+ +[LUIManagedPrefs managedPrefs].cold.1
+ +[LUINetworkStatus sharedNetworkStatus].cold.1
+ +[LUIUnmanagedSpaceManager sharedUnmanagedSpaceManager].cold.1
+ +[LUIUserController sharedUserController].cold.1
+ +[NSBundle(LUIHelpers) bundleForLoginUIKit].cold.1
+ +[ODRecord(UserConvenience) desiredAttributes].cold.1
+ -[LUI2BatteryViewController _imageForBattery:].cold.1
+ -[LUI2BigTimeTextField mouseUp:]
+ -[LUI2InputMethodViewController _alternateAttributedStringFromString:].cold.1
+ -[LUI2InputMethodViewController _attributedStringFromString:].cold.1
+ -[LUI2MultiWindowController _displaysDidReconfigure].cold.1
+ -[LUI2MultiWindowController _displaysDidReconfigure].cold.2
+ -[LUI2MultiWindowController _displaysDidReconfigure].cold.3
+ -[LUI2MultiWindowController _displaysWillReconfigure].cold.1
+ -[LUI2MultiWindowController _displaysWillReconfigure].cold.2
+ -[LUI2MultiWindowController _displaysWillReconfigure].cold.3
+ -[LUI2RecoveryKeyFormatter _allowedCharacters].cold.1
+ -[LUI2SafeBootViewController _safeBootFont].cold.1
+ -[LUI2TimeViewController _loadSymbols].cold.1
+ -[LUIBatteryStatusController _imageForBattery:].cold.1
+ -[LUIDebugUserController users].cold.1
+ -[LUIPopUpButtonCell drawBezelWithFrame:inView:].cold.1
+ -[LUIUser _userDispatchQueue].cold.1
+ -[LUIUserController _updateAllowNetworkUsersToLogin]
+ -[LUIUserController allowNetworkUsersToLogin]
+ -[LUIUserController setAllowNetworkUsersToLogin:]
+ -[TRMPort _updatePropertiesFromService].cold.1
+ -[TRMPortManager _handleServiceAdded:].cold.1
+ -[TRMPortManager _handleServiceAdded:].cold.2
+ GCC_except_table52
+ LAContextClass.cold.1
+ LUI2MultiWindowControllerDisplayReconfiguration.cold.2
+ LUI2MultiWindowControllerDisplayReconfiguration.cold.3
+ LUI2MultiWindowControllerDisplayReconfiguration.cold.4
+ LUIAvatarAvatarsSupported.cold.1
+ LUIAvatarCreateAvatarInfoFromData.cold.1
+ LUIAvatarQueue.cold.1
+ LUIBootArgs.cold.1
+ LUIDBLoggingControllerStart.cold.1
+ OBJC_IVAR_$_LUIUserController._allowNetworkUsersToLogin
+ _OBJC_CLASS_$_LUI2BigTimeTextField
+ _OBJC_METACLASS_$_LUI2BigTimeTextField
+ __45-[TRMPortManager _startMatchingNotifications]_block_invoke.cold.1
+ __58-[LUIUserController _updateUsersSetIncludingNetworkUsers:]_block_invoke.246
+ __58-[LUIUserController _updateUsersSetIncludingNetworkUsers:]_block_invoke_2.253
+ __BUIImageClass_block_invoke.cold.1
+ __LAContextClass_block_invoke.cold.1
+ __OBJC_$_INSTANCE_METHODS_LUI2BigTimeTextField
+ __OBJC_CLASS_RO_$_LUI2BigTimeTextField
+ __OBJC_METACLASS_RO_$_LUI2BigTimeTextField
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.290
+ __set_hibernation_preview_block_invoke.27
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ __swift_FORCE_LOAD_$_swiftDataDetection_$_LoginUIKit
+ _objc_msgSend$_updateAllowNetworkUsersToLogin
+ _objc_msgSend$allowNetworkUsersToLogin
+ _objc_msgSend$mouseUp:
+ _objc_msgSend$nextResponder
+ _objc_msgSend$setAllowNetworkUsersToLogin:
+ _symbolic IeyB_Sg
+ _symbolic Sccy___________pG So10CGImageRefa s5ErrorP
+ _symbolic Sccyyt_____G s5NeverO
+ _symbolic yXlSgIeyBy_Sg
+ block_copy_helper.15
+ block_descriptor.17
+ block_destroy_helper.16
+ getLUIAVTViewClass.cold.1
- -[LUIUserController _allowNetworkUsersToLogin]
- GCC_except_table51
- GCC_except_table55
- GCC_except_table62
- _OUTLINED_FUNCTION_57
- _OUTLINED_FUNCTION_58
- _OUTLINED_FUNCTION_59
- __58-[LUIUserController _updateUsersSetIncludingNetworkUsers:]_block_invoke.228
- __58-[LUIUserController _updateUsersSetIncludingNetworkUsers:]_block_invoke_2.244
- __block_literal_global.281
- __set_hibernation_preview_block_invoke.25
- _objc_msgSend$_allowNetworkUsersToLogin
- _swift_endAccess
- _symbolic IeyB_
- _symbolic yXlSgIeyBy_
- block_descriptor.15
CStrings:
+ "/AppleInternal/Library/BuildRoots/79ef05cb-ffe7-11ef-b000-f2a857e00a32/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.4.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
+ "GUEST_ACCOUNT_RECORD_NAME"
+ "LUI2BigTimeTextField"
+ "TB,V_allowNetworkUsersToLogin"
+ "_updateAllowNetworkUsersToLogin"
+ "allowNetworkUsersToLogin"
+ "nextResponder"
+ "setAllowNetworkUsersToLogin:"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX15.3.Internal.sdk/usr/local/include/iBoot/hibernation_ui_sequence.h"
- "Division by zero"
- "Division results in an overflow"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "UnsafeMutableRawPointer.initializeMemory with negative count"
- "invalid Collection: less than 'count' elements in collection"

```
