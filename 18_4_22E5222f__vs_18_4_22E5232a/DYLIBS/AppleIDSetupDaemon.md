## AppleIDSetupDaemon

> `/System/Library/PrivateFrameworks/AppleIDSetupDaemon.framework/AppleIDSetupDaemon`

```diff

-50.461.2.0.0
-  __TEXT.__text: 0xd84d4
-  __TEXT.__auth_stubs: 0x2340
+50.466.0.0.0
+  __TEXT.__text: 0xde2fc
+  __TEXT.__auth_stubs: 0x23a0
   __TEXT.__objc_methlist: 0x6f4
   __TEXT.__const: 0x1f20
-  __TEXT.__cstring: 0x14ac
-  __TEXT.__oslogstring: 0x5386
-  __TEXT.__constg_swiftt: 0x1534
+  __TEXT.__cstring: 0x14dc
+  __TEXT.__oslogstring: 0x573a
+  __TEXT.__constg_swiftt: 0x154c
   __TEXT.__swift5_typeref: 0x186e
   __TEXT.__swift5_reflstr: 0xb24
   __TEXT.__swift5_fieldmd: 0xbb8

   __TEXT.__swift5_assocty: 0x170
   __TEXT.__swift5_proto: 0x128
   __TEXT.__swift5_types: 0xd8
-  __TEXT.__swift_as_entry: 0x348
-  __TEXT.__swift_as_ret: 0x58c
-  __TEXT.__swift5_capture: 0x85c
+  __TEXT.__swift_as_entry: 0x35c
+  __TEXT.__swift_as_ret: 0x5ac
+  __TEXT.__swift5_capture: 0x86c
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x3670
-  __TEXT.__eh_frame: 0xc198
+  __TEXT.__unwind_info: 0x3748
+  __TEXT.__eh_frame: 0xc688
   __TEXT.__objc_classname: 0xe3
-  __TEXT.__objc_methname: 0x1238
+  __TEXT.__objc_methname: 0x126f
   __TEXT.__objc_methtype: 0x7d5
   __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0xaa0
+  __DATA_CONST.__got: 0xab8
   __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x520
+  __DATA_CONST.__objc_selrefs: 0x530
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x11a8
-  __AUTH_CONST.__auth_ptr: 0x6d8
-  __AUTH_CONST.__const: 0x2200
+  __AUTH_CONST.__auth_got: 0x11d8
+  __AUTH_CONST.__auth_ptr: 0x6e8
+  __AUTH_CONST.__const: 0x2230
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__objc_const: 0x2e20
   __AUTH.__objc_data: 0x498
-  __AUTH.__data: 0xb28
+  __AUTH.__data: 0xb38
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x1cb0
+  __DATA.__data: 0x1cc8
   __DATA.__bss: 0x1e80
   __DATA_DIRTY.__objc_data: 0x138
   __DATA_DIRTY.__data: 0x578

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2221
+  Functions: 2260
   Symbols:   347
-  CStrings:  811
+  CStrings:  831
 
CStrings:
+ "Account is SA account. Skipping preflight repair."
+ "Checking IdMS-CK symptom for account: %s"
+ "Checking IdMS-PRK symptom for account: %s"
+ "Checking for PRK loss symptom using account: %@"
+ "Continuing to SRP"
+ "Detected PRK loss symptom, account will not be able to magic auth: %@"
+ "Finished preflight repair"
+ "Found a valid PRK, IdMS account for altDSID: %s is good: %{sensitive}s"
+ "Generated Preflight Setup symptom report: %s"
+ "Generating Preflight Setup symptom report for account with id: %s"
+ "Marked as terminal auth, finishing auth stream continuation early"
+ "No symptoms found. Cleared for takeoff."
+ "Performing Preflight Repair ..."
+ "Preflight check failed. Defaulting to needing preflight repair."
+ "Received signIn report: %s"
+ "Setup as server authStreamContinuation...: %s"
+ "Setup preflight check if repair is needed for account: %s"
+ "Throwing error during auth: %s"
+ "Throwing error during auth: CommandRouter.Failure.userCancelled"
+ "User completed repair with success: %{bool}d"
+ "Waiting on preflight to finish"
+ "com.apple.appleidsetup.preflightCheck"
+ "passwordResetTokenForAccount:"
+ "securityLevelForAccount:"
- "Checking IdMS symptom for account: %s"
- "Ignoring error during auth: %s"
- "Received report: %s"
- "Throwing CommandRouter.Failure.userCancelled"

```
