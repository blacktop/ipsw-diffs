## enhancedloggingd

> `/usr/libexec/enhancedloggingd`

```diff

-80.0.0.0.0
-  __TEXT.__text: 0x2dfb0
-  __TEXT.__auth_stubs: 0x1080
+92.0.0.0.0
+  __TEXT.__text: 0x31b20
+  __TEXT.__auth_stubs: 0x10a0
   __TEXT.__objc_stubs: 0xb80
   __TEXT.__objc_methlist: 0x704
-  __TEXT.__const: 0xfc0
-  __TEXT.__cstring: 0x11cc
-  __TEXT.__objc_methname: 0x1bfc
+  __TEXT.__const: 0x10ec
+  __TEXT.__cstring: 0x12c3
+  __TEXT.__objc_methname: 0x1c50
   __TEXT.__objc_classname: 0x79
   __TEXT.__objc_methtype: 0x260
-  __TEXT.__oslogstring: 0xcb6
-  __TEXT.__constg_swiftt: 0x450
-  __TEXT.__swift5_typeref: 0x799
-  __TEXT.__swift5_builtin: 0xb4
-  __TEXT.__swift5_reflstr: 0x2be
+  __TEXT.__oslogstring: 0xe46
+  __TEXT.__constg_swiftt: 0x468
+  __TEXT.__swift5_typeref: 0x7eb
+  __TEXT.__swift5_builtin: 0xc8
+  __TEXT.__swift5_reflstr: 0x35e
+  __TEXT.__swift5_fieldmd: 0x32c
   __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift5_fieldmd: 0x2d4
-  __TEXT.__swift5_proto: 0xc4
-  __TEXT.__swift5_types: 0x40
-  __TEXT.__swift5_capture: 0x2a4
-  __TEXT.__swift_as_entry: 0x60
-  __TEXT.__swift_as_ret: 0x7c
+  __TEXT.__swift5_proto: 0xcc
+  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_capture: 0x370
+  __TEXT.__swift_as_entry: 0x7c
+  __TEXT.__swift_as_ret: 0x98
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x890
-  __TEXT.__eh_frame: 0x10c8
-  __DATA_CONST.__auth_got: 0x848
-  __DATA_CONST.__got: 0x510
-  __DATA_CONST.__auth_ptr: 0x1c8
-  __DATA_CONST.__const: 0xda0
+  __TEXT.__unwind_info: 0x940
+  __TEXT.__eh_frame: 0x1208
+  __DATA_CONST.__auth_got: 0x858
+  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__auth_ptr: 0x200
+  __DATA_CONST.__const: 0x1010
   __DATA_CONST.__cfstring: 0xc0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0xcc0
-  __DATA.__objc_selrefs: 0x850
+  __DATA.__objc_const: 0xd20
+  __DATA.__objc_selrefs: 0x878
   __DATA.__objc_ivar: 0x38
-  __DATA.__objc_data: 0x380
-  __DATA.__data: 0x970
-  __DATA.__bss: 0x1790
+  __DATA.__objc_data: 0x388
+  __DATA.__data: 0x990
+  __DATA.__bss: 0x1890
   __DATA.__common: 0xf0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 91491F77-9C93-39F6-8AF2-88E92D90C105
-  Functions: 685
-  Symbols:   493
-  CStrings:  556
+  UUID: 9377DDD7-8E56-3174-9D94-28C298C0343F
+  Functions: 748
+  Symbols:   506
+  CStrings:  573
 
Symbols:
+ _$s15EnhancedLogging12SessionErrorO23deviceDiscoveryTimedOutyA2CmFWC
+ _$sSL1goiySbx_xtFZTq
+ _$sSL1loiySbx_xtFZTq
+ _$sSL2geoiySbx_xtFZTq
+ _$sSL2leoiySbx_xtFZTq
+ _$sSLMp
+ _$sSLSQTb
+ _$sSS10describingSSx_tclufC
+ _$sScT6cancelyyF
+ _$sScTss5NeverORszABRs_rlE5sleep11nanosecondsys6UInt64V_tYaKFZ
+ _$sScTss5NeverORszABRs_rlE5sleep11nanosecondsys6UInt64V_tYaKFZTu
+ _$sSis23CustomStringConvertiblesWP
+ _$ss5ErrorWS
+ _ELSDomain
+ _ELSEventTypeSessionError
+ _ELSEventTypeUploadConsentApprovedCellular
- _$s15EnhancedLogging12SessionErrorO015failedToConnectf3BugC0yA2CmFWC
- _$ss23withCheckedContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5NeverOGXEtYalF
- _$ss23withCheckedContinuation9isolation8function_xScA_pSgYi_SSyScCyxs5NeverOGXEtYalFTu
CStrings:
+ "Bug session %{public}s is finished; dropping"
+ "Current user defaults format version is %{public}s, expected %{public}ld"
+ "Device discovery timed out after %f seconds"
+ "Extension identifier is nil"
+ "Failed to reconnect to %{public}s"
+ "Failed to reconnect to %{public}s; dropping"
+ "Flushing user defaults"
+ "Last bug session was dropped"
+ "No session found, attempting to clear follow up items if present."
+ "_persistedUserDefaultsFormatVersion"
+ "awaitAllSessionDevicesReady(timeout:)"
+ "code"
+ "com.apple.AppleElementsSupport.AppleElementsDiagnostic"
+ "createLoggingEventWith:postfix:"
+ "currentUserDefaultsFormatVersion"
+ "deviceDiscoveryTimeout"
+ "domain"
+ "extensionIdentifier"
+ "hasRecentlyFinishedSessionWithIdentifier:"
+ "operatingSystemVersion"
+ "sessionController(_:didEndWithError:shouldFlush:)"
+ "typeName"
- "Bug session %s is no longer active"
- "hasActiveSessionForIdentifier:completion:"
- "sessionController(_:didEndWithError:)"
- "stringValue"
- "v12@?0B8"

```
