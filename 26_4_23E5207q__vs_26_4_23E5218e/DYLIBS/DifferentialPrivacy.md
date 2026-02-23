## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-684.100.52.0.1
-  __TEXT.__text: 0x62838
-  __TEXT.__auth_stubs: 0x1120
-  __TEXT.__objc_methlist: 0x591c
-  __TEXT.__const: 0x9e8
-  __TEXT.__cstring: 0x482c
-  __TEXT.__oslogstring: 0x4237
-  __TEXT.__gcc_except_tab: 0xd0c
+684.100.58.0.1
+  __TEXT.__text: 0x623e4
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x58c4
+  __TEXT.__const: 0x9d8
+  __TEXT.__cstring: 0x47ec
+  __TEXT.__oslogstring: 0x41ef
+  __TEXT.__gcc_except_tab: 0xcd4
   __TEXT.__ustring: 0x4
-  __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__constg_swiftt: 0x300
   __TEXT.__swift5_typeref: 0x2b4
   __TEXT.__swift5_reflstr: 0x327

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x1990
+  __TEXT.__unwind_info: 0x1970
   __TEXT.__eh_frame: 0x798
-  __TEXT.__objc_classname: 0xed3
-  __TEXT.__objc_methname: 0xa1ad
-  __TEXT.__objc_methtype: 0x1407
-  __TEXT.__objc_stubs: 0x7f60
+  __TEXT.__objc_classname: 0xec3
+  __TEXT.__objc_methname: 0xa00d
+  __TEXT.__objc_methtype: 0x13c7
+  __TEXT.__objc_stubs: 0x7ec0
   __DATA_CONST.__got: 0x800
-  __DATA_CONST.__const: 0x1238
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __DATA_CONST.__const: 0x1220
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2540
+  __DATA_CONST.__objc_selrefs: 0x2500
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x108
-  __AUTH_CONST.__auth_got: 0x8a8
-  __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x4340
-  __AUTH_CONST.__objc_const: 0xafd8
+  __AUTH_CONST.__auth_got: 0x890
+  __AUTH_CONST.__const: 0x760
+  __AUTH_CONST.__cfstring: 0x4320
+  __AUTH_CONST.__objc_const: 0xaf38
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH.__data: 0x168
   __DATA.__objc_ivar: 0x534
   __DATA.__data: 0x9d0
-  __DATA.__bss: 0x950
+  __DATA.__bss: 0x930
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x25d8
+  __DATA_DIRTY.__objc_data: 0x2588
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/VDAF.framework/VDAF
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DFB6BC42-85C1-3F78-9B18-5E75DDF9469A
-  Functions: 2460
-  Symbols:   7918
-  CStrings:  3574
+  UUID: 3EE8E75F-C705-3651-BA88-9F078CF75F49
+  Functions: 2456
+  Symbols:   7886
+  CStrings:  3556
 
Symbols:
+ -[_DPDaemonConnection recordBitValues:metadata:forKey:withReply:].cold.1
+ -[_DPDaemonConnection recordBitVectors:metadata:forKey:withReply:].cold.1
+ -[_DPDaemonConnection recordFloatVectors:metadata:forKey:withReply:].cold.1
+ ___65-[_DPDaemonConnection recordBitValues:metadata:forKey:withReply:]_block_invoke_2
+ ___65-[_DPDaemonConnection recordBitValues:metadata:forKey:withReply:]_block_invoke_2.cold.1
+ ___66-[_DPDaemonConnection recordBitVectors:metadata:forKey:withReply:]_block_invoke_2
+ ___66-[_DPDaemonConnection recordBitVectors:metadata:forKey:withReply:]_block_invoke_2.cold.1
+ ___68-[_DPDaemonConnection recordFloatVectors:metadata:forKey:withReply:]_block_invoke_2.cold.1
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
- +[_DPLHBitacoraLogger bitacoraDprivacydEventWithEventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:]
- +[_DPLHBitacoraLogger bitacoraDprivacydEventWithEventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:].cold.1
- +[_DPLHBitacoraLogger bitacoraDprivacydEventWithEventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:].cold.2
- +[_DPLHBitacoraLogger donateEventToBitacoraForKey:eventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:telemetryAllowed:]
- +[_DPLHBitacoraLogger trialIdentifiersForKey:]
- +[_DPServer missingEntitlementError]
- -[_DPServer metadataMethodsAllowed]
- _LighthouseBitacoraFrameworkLibrary
- _LighthouseBitacoraFrameworkLibraryCore.frameworkLibrary
- _OBJC_CLASS_$__DPLHBitacoraLogger
- _OBJC_METACLASS_$__DPLHBitacoraLogger
- __OBJC_$_CLASS_METHODS__DPLHBitacoraLogger
- __OBJC_$_CLASS_METHODS__DPServer
- __OBJC_CLASS_RO_$__DPLHBitacoraLogger
- __OBJC_METACLASS_RO_$__DPLHBitacoraLogger
- ___LighthouseBitacoraFrameworkLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
- ___block_literal_global.10
- ___block_literal_global.8
- ___getLBFDprivacydEventClass_block_invoke
- ___getLBFDprivacydEventClass_block_invoke.cold.1
- ___getLBFTrialIdentifiersClass_block_invoke
- ___getLBFTrialIdentifiersClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringLighthouseBitacoraFramework
- _getLBFDprivacydEventClass.softClass
- _getLBFTrialIdentifiersClass.softClass
- _objc_getClass
- _objc_msgSend$currentConnection
- _objc_msgSend$initWithBMLTTaskID:deploymentID:
- _objc_msgSend$initWithEventPhase:eventUUID:succeeded:error:aggregateFunction:count:
- _objc_msgSend$metadataMethodsAllowed
- _objc_msgSend$missingEntitlementError
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIiugB3VPbmD9ky-5ijiGd0n9Jd4QST7J6zvFw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "Begin: recordBitValues:metadata: for key %@"
+ "Begin: recordFloatVectors:metadata: for key %@"
+ "End: recordBitValues:metadata: for key %@"
+ "End: recordFloatVectors:metadata: for key %@"
+ "Failed to create XPC remote object proxy."
+ "com.apple.DifferentialPrivacy.DaemonConnectionError"
- "%@:%@:%@"
- "%s"
- "/AppleInternal/Library/BuildRoots/4~CH9OugCbzjzGWiYQltZlb6O4i_KGXChAfcmtpYM/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__hash_table:1892: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "@52@0:8i16@20B28i32@36i44i48"
- "B64@0:8@16i24@28B36i40@44i52i56B60"
- "Failed to donate to Bitacora; event is not succeeded but no error code provided"
- "Failed to donate to Bitacora; event phase is unknown"
- "LBFDprivacydEvent"
- "LBFTrialIdentifiers"
- "Missing entitlement required for this method"
- "Skipping donation to Bitacora; malformed collection ID %@. The number of colon separated components is less than %ld"
- "TB,R,D,N"
- "Unable to find class %s"
- "_DPLHBitacoraLogger"
- "bitacoraDprivacydEventWithEventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:"
- "com.apple.private.dprivacyd.metadata.allow"
- "currentConnection"
- "donateEventToBitacoraForKey:eventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:telemetryAllowed:"
- "initWithBMLTTaskID:deploymentID:"
- "initWithEventPhase:eventUUID:succeeded:error:aggregateFunction:count:"
- "metadataMethodsAllowed"
- "missingEntitlementError"
- "softlink:r:path:/System/Library/PrivateFrameworks/LighthouseBitacoraFramework.framework/LighthouseBitacoraFramework"
- "trialIdentifiersForKey:"

```
