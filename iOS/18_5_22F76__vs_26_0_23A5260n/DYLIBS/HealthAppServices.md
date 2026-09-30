## HealthAppServices

> `/System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x1cf78
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x7f4
-  __TEXT.__const: 0xdb2
-  __TEXT.__cstring: 0xf12
+6074.1.2.4.0
+  __TEXT.__text: 0x1c3f4
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_methlist: 0x93c
+  __TEXT.__const: 0xdc2
+  __TEXT.__cstring: 0xff2
   __TEXT.__oslogstring: 0x2cb
-  __TEXT.__swift5_typeref: 0x44c
+  __TEXT.__swift5_typeref: 0x43e
   __TEXT.__swift5_reflstr: 0x4a6
   __TEXT.__swift5_assocty: 0x198
-  __TEXT.__constg_swiftt: 0x4c8
+  __TEXT.__constg_swiftt: 0x458
   __TEXT.__swift5_fieldmd: 0x540
   __TEXT.__swift5_proto: 0xac
   __TEXT.__swift5_types: 0x60
-  __TEXT.__swift5_capture: 0x194
+  __TEXT.__swift5_capture: 0x174
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x6d8
+  __TEXT.__unwind_info: 0x6a0
   __TEXT.__eh_frame: 0x108
   __TEXT.__objc_classname: 0x1df
-  __TEXT.__objc_methname: 0x193d
+  __TEXT.__objc_methname: 0x1c2b
   __TEXT.__objc_methtype: 0x2e9
-  __TEXT.__objc_stubs: 0xd60
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x278
+  __TEXT.__objc_stubs: 0xf20
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
+  __DATA_CONST.__objc_selrefs: 0x788
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH_CONST.__const: 0x1488
-  __AUTH_CONST.__cfstring: 0x7a0
-  __AUTH_CONST.__objc_const: 0xf48
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__const: 0x1430
+  __AUTH_CONST.__cfstring: 0x9a0
+  __AUTH_CONST.__objc_const: 0x1038
   __AUTH.__objc_data: 0x410
-  __AUTH.__data: 0x2a0
+  __AUTH.__data: 0x208
   __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0x490
+  __DATA.__data: 0x428
   __DATA.__bss: 0x1080
-  __DATA_DIRTY.__objc_data: 0x188
-  __DATA_DIRTY.__data: 0x2a8
+  __DATA_DIRTY.__objc_data: 0x130
+  __DATA_DIRTY.__data: 0x338
   __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 4B1E7600-CF59-3345-92D6-B7491CBC148A
-  Functions: 729
-  Symbols:   863
-  CStrings:  527
+  UUID: 20EB5BCA-4828-3B5E-A186-B653310387D9
+  Functions: 708
+  Symbols:   920
+  CStrings:  584
 
Symbols:
+ +[HAServicesDefines appendBundleIdentifierIfNecessary:toPath:]
+ +[HAServicesDefines appleAccountHostName]
+ +[HAServicesDefines appsHostName]
+ +[HAServicesDefines generalHostName]
+ +[HAServicesDefines getInternalURLStringFor:]
+ +[HAServicesDefines healthAppHealthChecklistHostName]
+ +[HAServicesDefines healthSettingsBundleIdentifier]
+ +[HAServicesDefines healthSettingsHealthDetailsSpecifier]
+ +[HAServicesDefines healthSettingsHealthRecordsSpecifier]
+ +[HAServicesDefines healthSettingsMedicalIDSpecifier]
+ +[HAServicesDefines healthSettingsSourcesItemSpecifier]
+ +[HAServicesDefines healthSettingsSourcesSpecifier]
+ +[HAServicesDefines hostValueFor:]
+ +[HAServicesDefines internalAppSettingsURLHost]
+ +[HAServicesDefines internalAppleAccountSettingsURLString]
+ +[HAServicesDefines internalGeneralSettingsURLString]
+ +[HAServicesDefines internalHealthSettingsURLString]
+ +[HAServicesDefines internalHealthSettingsURLTo:]
+ +[HAServicesDefines internalPasscodeSettingsURLString]
+ +[HAServicesDefines internalPrivacySettingsURLString]
+ +[HAServicesDefines internalScreenTimeSettingsURLString]
+ +[HAServicesDefines internalSettingsHostURLStringFor:]
+ +[HAServicesDefines internalSettingsURLHost]
+ +[HAServicesDefines internalSettingsURLString]
+ +[HAServicesDefines internalSoundsSettingsURLString]
+ +[HAServicesDefines passcodeHostName]
+ +[HAServicesDefines privacyAndSecurityHostName]
+ +[HAServicesDefines screenTimeHostName]
+ +[HAServicesDefines soundsHostName]
+ __DATA__TtCC17HealthAppServices28HealthAppOrchestrationClientP33_916F1C2454B8A8DF9DD0CE00DE63E20915WeakClientProxy
+ __IVARS__TtCC17HealthAppServices28HealthAppOrchestrationClientP33_916F1C2454B8A8DF9DD0CE00DE63E20915WeakClientProxy
+ __METACLASS_DATA__TtCC17HealthAppServices28HealthAppOrchestrationClientP33_916F1C2454B8A8DF9DD0CE00DE63E20915WeakClientProxy
+ __PROTOCOLS__TtCC17HealthAppServices28HealthAppOrchestrationClientP33_916F1C2454B8A8DF9DD0CE00DE63E20915WeakClientProxy
+ __PROTOCOLS__TtCC17HealthAppServices28HealthAppOrchestrationClientP33_916F1C2454B8A8DF9DD0CE00DE63E20915WeakClientProxy.103
+ ___swift_project_boxed_opaque_existential_0
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HealthAppServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HealthAppServices
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HealthAppServices
+ _block_copy_helper.107
+ _block_descriptor.109
+ _block_destroy_helper.108
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$appleAccountHostName
+ _objc_msgSend$appsHostName
+ _objc_msgSend$generalHostName
+ _objc_msgSend$healthSettingsBundleIdentifier
+ _objc_msgSend$healthSettingsSourcesItemSpecifier
+ _objc_msgSend$hostValueFor:
+ _objc_msgSend$internalAppSettingsURLHost
+ _objc_msgSend$internalHealthSettingsURLString
+ _objc_msgSend$internalSettingsHostURLStringFor:
+ _objc_msgSend$internalSettingsURLHost
+ _objc_msgSend$passcodeHostName
+ _objc_msgSend$privacyAndSecurityHostName
+ _objc_msgSend$screenTimeHostName
+ _objc_msgSend$soundsHostName
+ _objc_retain_x23
+ _swift_coroFrameAlloc
+ _swift_getErrorValue
+ _swift_setDeallocating
+ _symbolic _____ 17HealthAppServices0aB19OrchestrationClientC04WeakE5Proxy33_916F1C2454B8A8DF9DD0CE00DE63E209LLC
+ _symbolic _____ySS______pGIeghg_ s6ResultOsRi_zRi0_zrlE s5ErrorP
+ _symbolic _____ySaySSG______pGIeghg_ s6ResultOsRi_zRi0_zrlE s5ErrorP
- +[HAServicesDefines healthSettingsSourcesHostName]
- __DATA__TtCC17HealthAppServices28HealthAppOrchestrationClient15WeakClientProxy
- __IVARS__TtCC17HealthAppServices28HealthAppOrchestrationClient15WeakClientProxy
- __METACLASS_DATA__TtCC17HealthAppServices28HealthAppOrchestrationClient15WeakClientProxy
- __PROTOCOLS__TtCC17HealthAppServices28HealthAppOrchestrationClient15WeakClientProxy
- __PROTOCOLS__TtCC17HealthAppServices28HealthAppOrchestrationClient15WeakClientProxy.104
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_HealthAppServices
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_HealthAppServices
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_HealthAppServices
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_HealthAppServices
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_HealthAppServices
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_HealthAppServices
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_HealthAppServices
- _block_copy_helper.111
- _block_descriptor.113
- _block_destroy_helper.112
- _keypath_getTm
- _objc_msgSend$healthSettingsSourcesHostName
- _objc_retain_x28
- _swift_beginAccess
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_endAccess
- _swift_isaMask
- _swift_lookUpClassMethod
- _symbolic SaySsG
- _symbolic _____ 17HealthAppServices0aB19OrchestrationClientC04WeakE5ProxyC
- _symbolic _____ SS5IndexV
- _symbolic _____ySS______pGIeghg_ s6ResultOsRi_zrlE s5ErrorP
- _symbolic _____ySaySSG______pGIeghg_ s6ResultOsRi_zrlE s5ErrorP
CStrings:
+ "%@.%@"
+ "%@/%@"
+ "%@://%@"
+ "AppleAccount"
+ "Apps"
+ "General"
+ "HEALTH_DETAILS_ITEM"
+ "HEALTH_RECORDS_ITEM"
+ "HealthChecklist"
+ "MEDICAL_ID_ITEM"
+ "Passcode"
+ "PrivacyAndSecurity"
+ "SOURCES"
+ "ScreenTime"
+ "Sounds"
+ "URLWithString:"
+ "_TtCC17HealthAppServices28HealthAppOrchestrationClientP33_916F1C2454B8A8DF9DD0CE00DE63E20915WeakClientProxy"
+ "appleAccountHostName"
+ "appsHostName"
+ "com.apple.Settings"
+ "generalHostName"
+ "getInternalURLStringFor:"
+ "healthAppHealthChecklistHostName"
+ "healthSettingsBundleIdentifier"
+ "healthSettingsHealthDetailsSpecifier"
+ "healthSettingsHealthRecordsSpecifier"
+ "healthSettingsMedicalIDSpecifier"
+ "healthSettingsSourcesItemSpecifier"
+ "healthSettingsSourcesSpecifier"
+ "hostValueFor:"
+ "internalAppSettingsURLHost"
+ "internalAppleAccountSettingsURLString"
+ "internalGeneralSettingsURLString"
+ "internalHealthSettingsURLString"
+ "internalHealthSettingsURLTo:"
+ "internalPasscodeSettingsURLString"
+ "internalPrivacySettingsURLString"
+ "internalScreenTimeSettingsURLString"
+ "internalSettingsHostURLStringFor:"
+ "internalSettingsURLHost"
+ "internalSettingsURLString"
+ "internalSoundsSettingsURLString"
+ "passcodeHostName"
+ "privacyAndSecurityHostName"
+ "screenTimeHostName"
+ "settings-navigation"
+ "soundsHostName"
- "%@&path=%@"
- "_TtCC17HealthAppServices28HealthAppOrchestrationClient15WeakClientProxy"
- "features"
- "healthSettingsSourcesHostName"
- "root=HEALTH"
- "stanley"

```
